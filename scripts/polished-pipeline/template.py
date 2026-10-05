"""
Polished equity-research note template — shared infrastructure for the 56-note rebuild.

Usage (from ~/workspace/polished-notes/):
    from template import build_note
    build_note(data, "WYNN-equity-research-note.pdf")

Dependencies: reportlab, matplotlib (Agg backend). Nothing exotic.

House rules enforced by this module (workers: do NOT work around them):
  * Verdict / fair value / price / risk shown on the cover are rendered exactly
    from the data dict — the authoritative 56-name table's numbers are FINAL.
  * No version labels anywhere in output text. The words "v2", "addendum",
    "rebuild", "old note", "prior target", "previous note" must not appear in
    any string you pass in. Every note reads as a fresh October 4, 2026
    analyst note. (validate() scans your strings and raises if it finds them.)
  * Charts render each name's ACTUAL scenario numbers from data — no
    placeholders, no invented series. Missing chart inputs -> omit that chart,
    never fake it.

DATA SCHEMA
-----------
Required keys:
  ticker        str   e.g. "WYNN"
  company       str   e.g. "Wynn Resorts, Limited"
  exchange      str   e.g. "NASDAQ" (or "NASDAQ / HK: 9618")
  sector        str   e.g. "Consumer Discretionary — Casinos & Gaming"
  verdict       str   one of BUY | HOLD | REDUCE | SELL
  fair_value    float probability-weighted fair value = 12-mo price target ($)
  price         float current share price, October 2, 2026 close ($)
  risk          str   e.g. "High", "Medium-High", "Medium", "Low"
  headline      str   cover subtitle, 1-2 lines, the call in a sentence
  snapshot      list[(label, value)]  key-facts grid on the cover
                (market cap, EV, 52wk range, net cash/debt, TTM revenue,
                 next catalyst, sell-side consensus + PT range where known, ...)
  thesis        list[str]  3-5 paragraphs. FORWARD-LOOKING: the analyst's
                judgment of the FUTURE of the business, not extrapolation.
  business      list[str]  paragraphs describing what the company does now
  outlook       list[str]  forward outlook: drivers, 2-3 year view
  financials    list[str]  financial-analysis paragraphs
  moat          list[(lead, rest)]  bullets with bold leads
  risks         list[(lead, rest)]  bullets with bold leads
  falsification str   what would change our mind / downgrade triggers
  valuation_method str  e.g. "10-year scenario FCFE DCF"
  valuation_intro   list[str]  paragraphs describing the valuation setup
  scenarios     dict  keys "bear"/"base"/"bull", each a dict:
                  fair_value   float  scenario fair value per share ($)
                  assumptions  str    1-3 sentences of key scenario assumptions
                  rev_cagr     str    e.g. "+4.6%"  (10-yr revenue CAGR)
                  margin_end   str    e.g. "31%"    (terminal-year margin)
                  discount     float  e.g. 0.12
                  terminal_g   float  e.g. 0.02
                  tv_share     float  e.g. 0.53  (terminal value share of equity)
                  pv_explicit  float  PV of explicit-period cash flows
                  pv_terminal  float  PV of terminal value
                  cashflow_unit str   "$mn" or "$/sh" — unit of pv_explicit/pv_terminal
  weights       dict  {"bear":0.25,"base":0.5,"bull":0.25}
  charts        dict:
                  "scenario": {"bear":..,"base":..,"bull":..,"weighted":..,"price":..}
                  "trajectory": {"years_hist":[...], "revenue_hist":[...], "fcf_hist":[...],
                                 "years_proj":[...], "revenue_proj":[...], "fcf_proj":[...],
                                 "unit": "$bn", "note": str (footnote),
                                 "fcf_label": "FCF"}  # None values allowed -> line breaks
                  "composition": {"bear":{"pv_explicit":..,"pv_terminal":..}, ...,
                                  "unit": "$mn"}     # same unit for all scenarios
                  "extra": {"type":"pie","title":str,"labels":[...],"values":[...]}
                           or {"type":"line","title":str,"years":[...],
                               "series":[{"label":str,"values":[...]}], "ylabel":str}
                           # segment mix pie or margin-trajectory line; optional

Optional keys:
  price_note    str   default "Oct 2, 2026"
  ceo, hq       str   shown in business section opener if provided
  thesis_subhead str  e.g. "Why the market will care (eventually)"
  thesis_bullets    list[(lead, rest)]
  business_bullets  list[(lead, rest)]  e.g. growth projects, "what the company is doing now"
  business_subheads dict  {"main": str, "bullets": str}  subhead strings
  segment_table {"headers":[...], "rows":[[...]], "footnote": str}
  fin_table     {"headers":[...], "rows":[[...]], "footnote": str}
  outlook_bullets   list[(lead, rest)]
  scenario_note str   extra line under the scenario table
  risks_subhead str   default "Key risks"
  methodology   list[str]  overrides the default appendix (present tense, no version labels)
  date          str   default "October 4, 2026"
  price_date    str   default "October 2, 2026"

All prose strings are plain text. Minimal inline markup supported: **bold**
(double asterisks) is rendered bold; everything else is escaped. Keep the
double-asterisk usage light (lead-ins), the tuple bullets already bold leads.
"""

import io
import os
import re
import tempfile

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, Image, KeepTogether,
                                PageBreak, NextPageTemplate)
from reportlab.lib.utils import ImageReader
from xml.sax.saxutils import escape as _xml_escape

# ----------------------------------------------------------------------------
# House style
# ----------------------------------------------------------------------------

NAVY = colors.HexColor("#14365D")
INK = colors.HexColor("#1B1B1B")
GREY = colors.HexColor("#5A6B7C")
LIGHT_BG = colors.HexColor("#F2F5F9")
RULE = colors.HexColor("#D5DDE6")

VERDICT_COLORS = {
    "BUY": colors.HexColor("#157F3D"),
    "HOLD": colors.HexColor("#B8860B"),
    "REDUCE": colors.HexColor("#C75B12"),
    "SELL": colors.HexColor("#B3271E"),
}

CHART_PALETTE = ["#14365D", "#2E86AB", "#E8A838", "#C75B12", "#7FB069", "#8E8E93"]

BANNED_RE = re.compile(
    r"\bv2\b|addendum|rebuild|old note|prior target|previous note|stand-?alone rebuild",
    re.IGNORECASE,
)

SEP = "\u00a0\u00a0"  # non-breaking spaces for section numbers

PAGE_W, PAGE_H = A4
MARGIN = 50
CONTENT_W = PAGE_W - 2 * MARGIN

DEFAULT_DATE = "October 4, 2026"
DEFAULT_PRICE_DATE = "October 2, 2026"

DEFAULT_METHODOLOGY = [
    "We value companies on a multi-year scenario discounted-cash-flow framework. "
    "Each note builds bear, base, and bull scenarios with scenario-specific discount "
    "rates and terminal growth assumptions, probability-weighted 25% / 50% / 25% "
    "unless the note states otherwise.",
    "Discount rates reflect the equity risk of the business: roughly 9% for stable "
    "franchises, 10% for standard operating companies, and 12% or higher for levered, "
    "cyclical, or development-stage businesses. The bear case adds 250 basis points "
    "to the base discount rate; the bull case subtracts 150 basis points. International "
    "businesses carry an explicit country-risk premium where the note's framework requires it.",
    "Terminal growth is set at or below long-run nominal GDP growth, applied to "
    "normalized mid-cycle margins — never peak margins. Project and segment economics "
    "are modeled on haircut assumptions, not on management guidance. Share counts are "
    "fully diluted, and minority interests are priced through the forecast every year.",
    "We cross-check DCF fair values against trading multiples, reverse-DCF implied "
    "growth, and sum-of-the-parts where the business has separable assets. The "
    "published target is the probability-weighted fair value, stated as a 12-month "
    "horizon reference.",
    "Risk ratings (Low / Medium / Medium-High / High) combine the volatility of the "
    "business model, the balance sheet, and the valuation. A High risk rating is not "
    "a veto on a BUY — it is the reason the upside exists — but it sizes the position.",
]

DEFAULT_DISCLAIMER = (
    "This note is independent research-style analysis for informational purposes only "
    "and is not investment advice. Financial figures are drawn from company releases "
    "and SEC filings; market data as of October 2, 2026. Projections and the price "
    "target are the author's estimates and involve uncertainty. Past performance does "
    "not predict future results."
)


# ----------------------------------------------------------------------------
# Small text helpers
# ----------------------------------------------------------------------------

def _md(text):
    """Render **bold** markup, escape the rest for reportlab Paragraph."""
    parts = re.split(r"(\*\*.+?\*\*)", text)
    out = []
    for p in parts:
        if p.startswith("**") and p.endswith("**") and len(p) > 4:
            out.append("<b>%s</b>" % _xml_escape(p[2:-2]))
        else:
            out.append(_xml_escape(p))
    return "".join(out)


def _money(x, digits=2):
    if x is None:
        return "—"
    return "$%s" % format(x, ",.%df" % digits)


def _pct(x, digits=1, signed=False):
    if x is None:
        return "—"
    s = "%s%.*f%%" % ("+" if signed and x >= 0 else "", digits, x)
    return s


# ----------------------------------------------------------------------------
# Styles
# ----------------------------------------------------------------------------

def _styles():
    s = {}
    s["title"] = ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=19,
                               leading=23, textColor=NAVY, alignment=TA_LEFT)
    s["headline"] = ParagraphStyle("headline", fontName="Helvetica-Bold", fontSize=12.5,
                                  leading=16, textColor=INK, alignment=TA_LEFT,
                                  spaceAfter=4)
    s["banner"] = ParagraphStyle("banner", fontName="Helvetica-Bold", fontSize=13,
                                leading=16, textColor=colors.white, alignment=TA_CENTER)
    s["meta"] = ParagraphStyle("meta", fontName="Helvetica", fontSize=8.5,
                              leading=11, textColor=GREY, alignment=TA_CENTER)
    s["section"] = ParagraphStyle("section", fontName="Helvetica-Bold", fontSize=12.5,
                                  leading=15, textColor=NAVY, spaceBefore=14,
                                  spaceAfter=6, keepWithNext=True)
    s["subhead"] = ParagraphStyle("subhead", fontName="Helvetica-Bold", fontSize=10,
                                 leading=13, textColor=INK, spaceBefore=8,
                                 spaceAfter=4, keepWithNext=True)
    s["body"] = ParagraphStyle("body", fontName="Helvetica", fontSize=9.2,
                              leading=13.6, textColor=INK, alignment=TA_JUSTIFY,
                              spaceAfter=5)
    s["bullet"] = ParagraphStyle("bullet", parent=None, fontName="Helvetica",
                                fontSize=9.2, leading=13.4, textColor=INK,
                                leftIndent=14, firstLineIndent=0,
                                bulletIndent=6, spaceAfter=4, alignment=TA_LEFT)
    s["table_cell"] = ParagraphStyle("tcell", fontName="Helvetica", fontSize=8.4,
                                    leading=11, textColor=INK, alignment=TA_LEFT)
    s["table_cell_r"] = ParagraphStyle("tcellr", parent=None, fontName="Helvetica",
                                      fontSize=8.4, leading=11, textColor=INK,
                                      alignment=TA_CENTER)
    s["table_head"] = ParagraphStyle("thead", fontName="Helvetica-Bold", fontSize=8.4,
                                    leading=11, textColor=colors.white, alignment=TA_LEFT)
    s["table_head_c"] = ParagraphStyle("theadc", parent=None, fontName="Helvetica-Bold",
                                      fontSize=8.4, leading=11, textColor=colors.white,
                                      alignment=TA_CENTER)
    s["footnote"] = ParagraphStyle("footnote", fontName="Helvetica-Oblique", fontSize=7.6,
                                  leading=10.5, textColor=GREY, spaceAfter=4)
    s["caption"] = ParagraphStyle("caption", fontName="Helvetica-Bold", fontSize=8.8,
                                  leading=11.5, textColor=NAVY, alignment=TA_CENTER,
                                  spaceBefore=6, spaceAfter=3)
    s["appendix"] = ParagraphStyle("appendix", fontName="Helvetica", fontSize=8.6,
                                   leading=12.4, textColor=INK, alignment=TA_JUSTIFY,
                                   spaceAfter=4)
    s["disclaimer"] = ParagraphStyle("disclaimer", fontName="Helvetica-Oblique",
                                    fontSize=7.8, leading=11, textColor=GREY,
                                    alignment=TA_JUSTIFY, spaceBefore=8)
    return s


# ----------------------------------------------------------------------------
# Validation — the contract workers must satisfy
# ----------------------------------------------------------------------------

_REQUIRED = ["ticker", "company", "exchange", "sector", "verdict", "fair_value",
             "price", "risk", "headline", "snapshot", "thesis", "business",
             "outlook", "financials", "moat", "risks", "falsification",
             "valuation_method", "valuation_intro", "scenarios", "weights", "charts"]

_CHART_REQUIRED = {
    "scenario": ["bear", "base", "bull", "weighted", "price"],
    "trajectory": ["years_hist", "revenue_hist", "fcf_hist",
                   "years_proj", "revenue_proj", "fcf_proj"],
    "composition": ["bear", "base", "bull"],
}

_SCEN_REQUIRED = ["fair_value", "assumptions", "rev_cagr", "margin_end",
                  "discount", "terminal_g", "tv_share", "pv_explicit",
                  "pv_terminal", "cashflow_unit"]


def _scan_banned(obj, where):
    """Recursively scan worker strings for banned version-label language."""
    if isinstance(obj, str):
        m = BANNED_RE.search(obj)
        if m:
            raise ValueError(
                "Banned version-label language in %s: %r (matched %r). "
                "Notes must read as fresh October 4, 2026 analyst notes with zero "
                "references to prior reports, old targets, or rebuilds." % (where, obj[:90], m.group(0)))
    elif isinstance(obj, dict):
        for k, v in obj.items():
            _scan_banned(v, "%s[%r]" % (where, k))
    elif isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            _scan_banned(v, "%s[%d]" % (where, i))


def validate(data):
    """Check the data dict contract. Raises ValueError with a clear message."""
    for k in _REQUIRED:
        if k not in data:
            raise ValueError("Missing required key: %r" % k)
    if data["verdict"] not in VERDICT_COLORS:
        raise ValueError("verdict must be one of %s" % sorted(VERDICT_COLORS))
    for sk in ("bear", "base", "bull"):
        if sk not in data["scenarios"]:
            raise ValueError("scenarios missing %r" % sk)
        for k in _SCEN_REQUIRED:
            if k not in data["scenarios"][sk]:
                raise ValueError("scenarios[%r] missing %r" % (sk, k))
    for ck, sub in _CHART_REQUIRED.items():
        if ck not in data["charts"]:
            raise ValueError("charts missing %r" % ck)
        c = data["charts"][ck]
        if ck == "composition":
            for sk in sub:
                if sk not in c or "pv_explicit" not in c[sk] or "pv_terminal" not in c[sk]:
                    raise ValueError("charts.composition[%r] needs pv_explicit/pv_terminal" % sk)
        else:
            for k in sub:
                if k not in c:
                    raise ValueError("charts.%s missing %r" % (ck, k))
    extra = data["charts"].get("extra")
    if extra:
        if extra.get("type") not in ("pie", "line"):
            raise ValueError("charts.extra type must be 'pie' or 'line'")
    _scan_banned(data, "data")
    return True


# ----------------------------------------------------------------------------
# Charts (matplotlib, house style)
# ----------------------------------------------------------------------------

def _house_style():
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["DejaVu Sans"],
        "font.size": 9,
        "axes.titlesize": 10,
        "axes.titleweight": "bold",
        "axes.labelsize": 8.5,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "axes.edgecolor": "#B9C4D0",
        "axes.facecolor": "white",
        "figure.facecolor": "white",
        "grid.color": "#E3E8EE",
        "grid.linestyle": "--",
        "grid.linewidth": 0.6,
    })


def _save(fig, path, width_in=7.2, height_in=3.4):
    fig.set_size_inches(width_in, height_in)
    fig.tight_layout(pad=1.2)
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


def chart_scenario(values, tmpdir):
    """(a) Horizontal bars: bear/base/bull/weighted fair values vs current price."""
    _house_style()
    fig, ax = plt.subplots()
    labels = ["Bear", "Base", "Bull", "Wtd. avg"]
    vals = [values["bear"], values["base"], values["bull"], values["weighted"]]
    cols = ["#C75B12", "#14365D", "#157F3D", "#2E86AB"]
    y = range(len(labels))
    bars = ax.barh(list(y), vals, color=cols, edgecolor="white", height=0.55)
    for bar, v in zip(bars, vals):
        ax.text(bar.get_width() + max(vals) * 0.012, bar.get_y() + bar.get_height() / 2,
                "$%.0f" % v, va="center", fontsize=9, fontweight="bold")
    px = values["price"]
    ax.axvline(px, color="#B3271E", linestyle="--", linewidth=1.4)
    ax.text(px, len(labels) - 0.55, "  Price $%.2f" % px, color="#B3271E",
            fontsize=8.5, fontweight="bold", va="center")
    ax.set_yticks(list(y))
    ax.set_yticklabels(labels)
    ax.set_xlabel("Fair value per share ($)")
    ax.set_title("Scenario fair values vs. current price ($)")
    ax.grid(axis="x", alpha=0.7)
    ax.set_xlim(0, max(max(vals), px) * 1.22)
    return _save(fig, os.path.join(tmpdir, "chart_scenario.png"))


def chart_trajectory(tr, tmpdir):
    """(b) Revenue & FCF: history (solid) + projected base case (dashed)."""
    _house_style()
    fig, ax1 = plt.subplots()
    yh, rh, fh = tr["years_hist"], tr["revenue_hist"], tr["fcf_hist"]
    yp, rp, fp = tr["years_proj"], tr["revenue_proj"], tr["fcf_proj"]
    unit = tr.get("unit", "$bn")
    fcf_label = tr.get("fcf_label", "FCF")

    def _clean(xs, ys):
        xs2, ys2 = [], []
        for x, y in zip(xs, ys):
            if y is not None:
                xs2.append(x); ys2.append(y)
        return xs2, ys2

    ax1.set_xlabel("Year")
    ax1.set_ylabel("Revenue (%s)" % unit, color="#14365D")
    xh, yhv = _clean(yh, rh)
    xp, ypv = _clean(yp, rp)
    l1, = ax1.plot(xh, yhv, color="#14365D", linewidth=2.2, marker="o", markersize=4,
                   label="Revenue — actual")
    l2, = ax1.plot(xp, ypv, color="#14365D", linewidth=2.0, linestyle="--", marker="s",
                   markersize=3.5, label="Revenue — base-case projection")
    ax1.tick_params(axis="y", labelcolor="#14365D")
    ax1.grid(alpha=0.7)

    ax2 = ax1.twinx()
    ax2.set_ylabel("%s (%s)" % (fcf_label, unit), color="#2E86AB")
    xh2, fhv = _clean(yh, fh)
    xp2, fpv = _clean(yp, fp)
    l3, = ax2.plot(xh2, fhv, color="#2E86AB", linewidth=2.2, marker="o", markersize=4,
                   label="%s — actual" % fcf_label)
    l4, = ax2.plot(xp2, fpv, color="#2E86AB", linewidth=2.0, linestyle="--", marker="s",
                   markersize=3.5, label="%s — base-case projection" % fcf_label)
    ax2.tick_params(axis="y", labelcolor="#2E86AB")
    # shade the projection zone
    if xp:
        ax1.axvspan(min(xp) - 0.5, max(xp) + 0.5, color="#F2F5F9", alpha=0.8, zorder=0)
    ax1.set_title("Revenue & %s trajectory — history vs. base-case projection" % fcf_label)
    lines = [l1, l2, l3, l4]
    ax1.legend(lines, [l.get_label() for l in lines], loc="upper left", fontsize=7.5,
               framealpha=0.95)
    return _save(fig, os.path.join(tmpdir, "chart_trajectory.png"), height_in=3.6)


def chart_composition(comp, tmpdir):
    """(c) Stacked bars per scenario: PV of explicit-period CFs vs terminal value."""
    _house_style()
    fig, ax = plt.subplots()
    labels = ["Bear", "Base", "Bull"]
    expl = [comp[s]["pv_explicit"] for s in ("bear", "base", "bull")]
    term = [comp[s]["pv_terminal"] for s in ("bear", "base", "bull")]
    unit = comp.get("unit", "$mn")
    x = range(len(labels))
    b1 = ax.bar(x, expl, color="#14365D", edgecolor="white", label="PV of explicit-period cash flows")
    b2 = ax.bar(x, term, bottom=expl, color="#E8A838", edgecolor="white", label="PV of terminal value")
    for i, (e, t) in enumerate(zip(expl, term)):
        tot = e + t
        ax.text(i, e / 2, "%.0f" % e, ha="center", va="center", fontsize=8.5,
                color="white", fontweight="bold")
        ax.text(i, e + t / 2, "%.0f" % t, ha="center", va="center", fontsize=8.5,
                color="#14365D", fontweight="bold")
        ax.text(i, tot * 1.015, "%.0f" % tot, ha="center", va="bottom", fontsize=8.5,
                fontweight="bold")
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels)
    ax.set_ylabel("Value (%s)" % unit)
    ax.set_title("DCF composition by scenario — explicit period vs. terminal value")
    ax.legend(fontsize=8, loc="upper right")
    ax.set_ylim(0, max(e + t for e, t in zip(expl, term)) * 1.14)
    return _save(fig, os.path.join(tmpdir, "chart_composition.png"))


def chart_extra(extra, tmpdir):
    """(d) Segment-mix pie or margin-trajectory line — whichever the story warrants."""
    _house_style()
    fig, ax = plt.subplots()
    if extra["type"] == "pie":
        vals = extra["values"]
        ax.pie(vals, labels=extra["labels"], autopct="%1.0f%%", startangle=90,
               colors=CHART_PALETTE, textprops={"fontsize": 8},
               wedgeprops={"edgecolor": "white", "linewidth": 1.5})
        ax.set_title(extra.get("title", "Revenue mix"))
    else:
        years = extra["years"]
        for i, srs in enumerate(extra["series"]):
            xs = [x for x, y in zip(years, srs["values"]) if y is not None]
            ys = [y for y in srs["values"] if y is not None]
            ax.plot(xs, ys, marker="o", markersize=4, linewidth=2,
                    color=CHART_PALETTE[i % len(CHART_PALETTE)], label=srs["label"])
        ax.set_xlabel("Year")
        ax.set_ylabel(extra.get("ylabel", "%"))
        ax.set_title(extra.get("title", "Margin trajectory"))
        ax.legend(fontsize=8)
        ax.grid(alpha=0.7)
    return _save(fig, os.path.join(tmpdir, "chart_extra.png"))


# ----------------------------------------------------------------------------
# PDF assembly
# ----------------------------------------------------------------------------

def _header_footer(canvas, doc):
    canvas.saveState()
    d = doc._note_data
    s = doc._styles
    # running head
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(GREY)
    canvas.drawString(MARGIN, PAGE_H - 32,
                      "%s (%s: %s)  —  Equity Research Note  —  October 2026"
                      % (d["company"], d["exchange"], d["ticker"]))
    canvas.drawRightString(PAGE_W - MARGIN, PAGE_H - 32, "Page %d" % doc.page)
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.6)
    canvas.line(MARGIN, PAGE_H - 38, PAGE_W - MARGIN, PAGE_H - 38)
    # footer
    canvas.setFont("Helvetica-Oblique", 7)
    canvas.setFillColor(GREY)
    canvas.drawCentredString(PAGE_W / 2, 30,
                             "Independent research-style analysis — not investment advice")
    canvas.restoreState()


def _p(style, text):
    return Paragraph(_md(text), style)


def _bullets(items, styles):
    out = []
    for lead, rest in items:
        out.append(Paragraph("<b>%s</b> %s" % (_xml_escape(lead), _md(rest)),
                             styles["bullet"], bulletText="•"))
    return out


def _styled_table(headers, rows, styles, col_widths=None, header_center=False,
                  zebra=True, fontsize=None):
    """headers: list[str]; rows: list[list[str]] (plain text, **bold** ok)."""
    hs = styles["table_head_c"] if header_center else styles["table_head"]
    data = [[Paragraph(_md(h), hs) for h in headers]]
    for r in rows:
        data.append([Paragraph(_md(c), styles["table_cell"]) for c in r])
    t = Table(data, colWidths=col_widths, repeatRows=1)
    st = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.5, RULE),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]
    if zebra:
        for i in range(1, len(data)):
            if i % 2 == 0:
                st.append(("BACKGROUND", (0, i), (-1, i), LIGHT_BG))
    t.setStyle(TableStyle(st))
    return t


def _section_head(text, styles):
    flow = [Paragraph(_md(text), styles["section"])]
    t = Table([[""]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, 0), 1.2, NAVY),
                           ("TOPPADDING", (0, 0), (-1, 0), 0),
                           ("BOTTOMPADDING", (0, 0), (-1, 0), 2)]))
    flow.append(t)
    flow.append(Spacer(1, 4))
    return flow


def _cover(data, styles):
    flow = []
    vc = VERDICT_COLORS[data["verdict"]]
    flow.append(Paragraph(_xml_escape(data["company"].upper()), styles["title"]))
    flow.append(Paragraph("(%s: %s)" % (_xml_escape(data["exchange"]),
                                       _xml_escape(data["ticker"])), styles["meta"]))
    flow.append(Spacer(1, 6))
    flow.append(Paragraph(_md(data["headline"]), styles["headline"]))
    flow.append(Spacer(1, 8))

    # verdict banner
    upside = (data["fair_value"] - data["price"]) / data["price"] * 100
    banner_text = "%s — %s Target" % (data["verdict"], _money(data["fair_value"]))
    bt = Table([[Paragraph(banner_text, styles["banner"])]], colWidths=[CONTENT_W])
    bt.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), vc),
                            ("TOPPADDING", (0, 0), (-1, -1), 8),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                            ("LEFTPADDING", (0, 0), (-1, -1), 10),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                            ("ROUNDEDCORNERS", [3, 3, 3, 3])]))
    flow.append(bt)
    flow.append(Spacer(1, 6))
    flow.append(Paragraph(
        "Equity Research Note · %s · %s" % (_xml_escape(data["sector"]),
                                           _xml_escape(data.get("date", DEFAULT_DATE))),
        styles["meta"]))
    flow.append(Spacer(1, 8))

    # cover key-numbers table
    price_note = data.get("price_note", DEFAULT_PRICE_DATE)
    ud_label = "Implied Upside" if upside >= 0 else "Implied Downside"
    headers = ["Recommendation", "12-Mo. Price Target", "Current Price",
               ud_label, "Risk Rating"]
    row = [data["verdict"], _money(data["fair_value"]), _money(data["price"]),
           _pct(upside, signed=True), data["risk"]]
    cw = CONTENT_W / 5
    flow.append(_styled_table(headers, [row], styles,
                              col_widths=[cw] * 5, header_center=True, zebra=False))
    flow.append(Paragraph("Current price as of %s close." % _xml_escape(price_note),
                          styles["footnote"]))
    flow.append(Spacer(1, 8))

    # snapshot key-facts grid (two columns of label/value pairs)
    flow.append(Paragraph("Snapshot", styles["subhead"]))
    snap = data["snapshot"]
    half = (len(snap) + 1) // 2
    left, right = snap[:half], snap[half:]
    grid = []
    for i in range(half):
        l = left[i] if i < len(left) else ("", "")
        r = right[i] if i < len(right) else ("", "")
        grid.append([
            Paragraph("<b>%s</b>" % _xml_escape(l[0]), styles["table_cell"]),
            Paragraph(_md(l[1]), styles["table_cell"]),
            Paragraph("<b>%s</b>" % _xml_escape(r[0]), styles["table_cell"]),
            Paragraph(_md(r[1]), styles["table_cell"]),
        ])
    cw2 = [CONTENT_W * 0.22, CONTENT_W * 0.28, CONTENT_W * 0.22, CONTENT_W * 0.28]
    st = Table(grid, colWidths=cw2)
    tstyle = [("VALIGN", (0, 0), (-1, -1), "TOP"),
              ("GRID", (0, 0), (-1, -1), 0.5, RULE),
              ("TOPPADDING", (0, 0), (-1, -1), 4),
              ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
              ("LEFTPADDING", (0, 0), (-1, -1), 6),
              ("RIGHTPADDING", (0, 0), (-1, -1), 6)]
    for i in range(len(grid)):
        if i % 2 == 1:
            tstyle.append(("BACKGROUND", (0, i), (-1, i), LIGHT_BG))
    st.setStyle(TableStyle(tstyle))
    flow.append(st)
    flow.append(Spacer(1, 6))
    return flow


def _img(path, max_w=CONTENT_W):
    img = Image(path)
    iw, ih = img.imageWidth, img.imageHeight
    scale = max_w / iw
    img.drawWidth = max_w
    img.drawHeight = ih * scale
    return img


def build_note(data, out_path):
    """Validate the data dict, render all sections + 4 charts, write the PDF."""
    validate(data)
    styles = _styles()
    tmpdir = tempfile.mkdtemp(prefix="polished_note_")

    # charts first (all from data — actual numbers only)
    ch = data["charts"]
    p_scen = chart_scenario(ch["scenario"], tmpdir)
    p_traj = chart_trajectory(ch["trajectory"], tmpdir)
    p_comp = chart_composition(ch["composition"], tmpdir)
    p_extra = chart_extra(ch["extra"], tmpdir) if ch.get("extra") else None

    story = []
    story += _cover(data, styles)

    # 1. Investment thesis
    story += _section_head("1" + SEP + "Investment Thesis", styles)
    for para in data["thesis"]:
        story.append(_p(styles["body"], para))
    if data.get("thesis_bullets"):
        sub = data.get("thesis_subhead", "Why the market will care")
        story.append(Paragraph(_md(sub), styles["subhead"]))
        story += _bullets(data["thesis_bullets"], styles)

    # 2. Business overview
    story += _section_head("2" + SEP + "Business Overview — What %s Is Doing"
                           % _xml_escape(data["company"].split(",")[0].split(" Inc")[0]),
                           styles)
    opener_bits = []
    if data.get("hq"):
        opener_bits.append(data["hq"])
    if data.get("ceo"):
        opener_bits.append("CEO %s" % data["ceo"])
    if opener_bits:
        story.append(Paragraph("(%s)" % "; ".join(_xml_escape(b) for b in opener_bits),
                               styles["footnote"]))
    for para in data["business"]:
        story.append(_p(styles["body"], para))
    if data.get("segment_table"):
        seg = data["segment_table"]
        n = len(seg["headers"])
        cw = [CONTENT_W * w for w in _auto_widths(n)]
        story.append(Spacer(1, 4))
        story.append(_styled_table(seg["headers"], seg["rows"], styles, col_widths=cw))
        if seg.get("footnote"):
            story.append(Paragraph(_md(seg["footnote"]), styles["footnote"]))
    if data.get("business_bullets"):
        sub = (data.get("business_subheads") or {}).get("bullets", "What the company is doing now")
        story.append(Paragraph(_md(sub), styles["subhead"]))
        story += _bullets(data["business_bullets"], styles)

    # 3. Financial analysis
    story += _section_head("3" + SEP + "Financial Analysis", styles)
    if data.get("fin_table"):
        ft = data["fin_table"]
        n = len(ft["headers"])
        cw = [CONTENT_W * w for w in _auto_widths(n)]
        story.append(_styled_table(ft["headers"], ft["rows"], styles, col_widths=cw))
        if ft.get("footnote"):
            story.append(Paragraph(_md(ft["footnote"]), styles["footnote"]))
        story.append(Spacer(1, 4))
    for para in data["financials"]:
        story.append(_p(styles["body"], para))
    # revenue & FCF trajectory chart lives with the financials
    story.append(Paragraph("Revenue & cash-flow trajectory", styles["caption"]))
    story.append(_img(p_traj))
    if ch["trajectory"].get("note"):
        story.append(Paragraph(_md(ch["trajectory"]["note"]), styles["footnote"]))

    # 4. Moat & competition
    story += _section_head("4" + SEP + "Moat & Competition", styles)
    story += _bullets(data["moat"], styles)

    # segment / margin chart where the story warrants it
    if p_extra:
        story.append(Paragraph(_md(ch["extra"].get("title", "Business mix")),
                               styles["caption"]))
        story.append(_img(p_extra))

    # 5. Valuation
    story += _section_head("5" + SEP + "Valuation — %s, Fair Value %s"
                           % (_xml_escape(data["valuation_method"]),
                              _money(data["fair_value"], 0)), styles)
    for para in data["valuation_intro"]:
        story.append(_p(styles["body"], para))
    sc = data["scenarios"]
    scen_rows = []
    for key, label in (("bear", "Bear"), ("base", "Base"), ("bull", "Bull")):
        s = sc[key]
        scen_rows.append([
            label,
            _md(s["assumptions"]),
            s["rev_cagr"],
            s["margin_end"],
            "%.1f%% / %.1f%%" % (s["discount"] * 100, s["terminal_g"] * 100),
            _pct(s["tv_share"] * 100, 0),
            _money(s["fair_value"]),
        ])
    w = data["weights"]
    wline = "Probability-weighted (%d/%d/%d) → **%s** target" % (
        round(w["bear"] * 100), round(w["base"] * 100), round(w["bull"] * 100),
        _money(data["fair_value"]))
    scen_rows.append(["Wtd. avg", wline, "", "", "", "", _money(data["fair_value"])])
    cw = [CONTENT_W * x for x in (0.09, 0.37, 0.09, 0.09, 0.13, 0.09, 0.14)]
    story.append(_styled_table(
        ["Scenario", "Key assumptions", "Rev CAGR", "End margin",
         "Discount / term. g", "TV share", "Fair value"],
        scen_rows, styles, col_widths=cw))
    if data.get("scenario_note"):
        story.append(Paragraph(_md(data["scenario_note"]), styles["footnote"]))
    story.append(Spacer(1, 4))
    story.append(Paragraph("Scenario fair values vs. current price ($)", styles["caption"]))
    story.append(_img(p_scen))
    story.append(Paragraph("DCF composition by scenario", styles["caption"]))
    story.append(_img(p_comp))
    comp_unit = ch["composition"].get("unit", "$mn")
    story.append(Paragraph(
        "Stacked bars show the present value of explicit-period cash flows (dark) "
        "versus the present value of the terminal value (gold), in %s. A heavy "
        "terminal-value share means the call rests on the long run, not the forecast window."
        % _xml_escape(comp_unit), styles["footnote"]))

    # 6. Risks & falsification
    story += _section_head("6" + SEP + "Risks & Falsification", styles)
    story.append(Paragraph(_md(data.get("risks_subhead", "Key risks")), styles["subhead"]))
    story += _bullets(data["risks"], styles)
    story.append(Paragraph("What would change our mind", styles["subhead"]))
    story.append(_p(styles["body"], data["falsification"]))

    # 7. Methodology appendix + disclaimer
    story += _section_head("7" + SEP + "Methodology", styles)
    for para in data.get("methodology", DEFAULT_METHODOLOGY):
        story.append(Paragraph(_md(para), styles["appendix"]))
    story.append(Paragraph(_md(data.get("disclaimer", DEFAULT_DISCLAIMER)),
                           styles["disclaimer"]))

    doc = BaseDocTemplate(out_path, pagesize=A4,
                          leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=52, bottomMargin=44,
                          title="%s Equity Research Note" % data["ticker"],
                          author="Equity Research")
    doc._note_data = data
    doc._styles = styles
    frame = Frame(MARGIN, 44, CONTENT_W, PAGE_H - 52 - 44, id="main")
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame],
                                       onPage=_header_footer)])
    doc.build(story)

    # temp chart PNGs are embedded by build(); safe to remove now
    for f in (p_scen, p_traj, p_comp, p_extra):
        try:
            if f and os.path.exists(f):
                os.remove(f)
        except OSError:
            pass
    try:
        os.rmdir(tmpdir)
    except OSError:
        pass
    return out_path


def _auto_widths(n):
    """First column wider for label-heavy tables; last column medium."""
    if n <= 2:
        return [0.35, 0.65][:n]
    w = [0.16] + [0.72 / (n - 2)] * (n - 2) + [0.12]
    tot = sum(w)
    return [x / tot for x in w]


if __name__ == "__main__":
    import sys
    print("template.py — import build_note(data, out_path) to render a note.")
    print("Run validate(data) to check the data-dict contract.")
    sys.exit(0)
