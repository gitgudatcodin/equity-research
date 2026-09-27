#!/usr/bin/env python3
"""Build Nike (NKE) equity research note PDF. All figures verified against
Nike FY2026 10-K / Q4 FY26 press release (June 30, 2026), investor relations,
and market data as of September 18-19, 2026."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, Image, HRFlowable, KeepTogether)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

OUT = os.path.expanduser("~/workspace/your_files/nike-equity-research/nike-equity-research-note.pdf")
CHART_DIR = os.path.expanduser("~/workspace/nike-research/charts")
os.makedirs(CHART_DIR, exist_ok=True)

# ---- palette ----
INK = "#111418"
MUTED = "#5b6470"
VOLT = "#9dbb1a"          # nike volt accent (muted for print)
VOLT_DARK = "#6e8512"
BAND = "#16181d"
LIGHT_BG = "#f2f4f6"
GRID = "#d7dce1"
BLUE = "#1f5fa8"
RED = "#c0392b"
GREEN = "#1e8449"

styles = getSampleStyleSheet()
sTitle = ParagraphStyle("Title2", parent=styles["Title"], fontSize=26, leading=30,
                       textColor=colors.HexColor(INK), alignment=TA_LEFT, spaceAfter=4)
sSub = ParagraphStyle("Sub", parent=styles["Normal"], fontSize=11, leading=15,
                     textColor=colors.HexColor(MUTED), alignment=TA_LEFT)
sH1 = ParagraphStyle("H1", parent=styles["Heading1"], fontSize=15, leading=18,
                    textColor=colors.HexColor(INK), spaceBefore=14, spaceAfter=6,
                    keepWithNext=True)
sH2 = ParagraphStyle("H2", parent=styles["Heading2"], fontSize=11.5, leading=14.5,
                    textColor=colors.HexColor(BAND), spaceBefore=10, spaceAfter=4,
                    keepWithNext=True)
sBody = ParagraphStyle("Body", parent=styles["Normal"], fontSize=9.2, leading=13.4,
                       textColor=colors.HexColor("#23272e"), alignment=TA_JUSTIFY, spaceAfter=5)
sBodyL = ParagraphStyle("BodyL", parent=sBody, alignment=TA_LEFT)
sBullet = ParagraphStyle("Bullet", parent=sBody, alignment=TA_LEFT, leftIndent=14,
                         firstLineIndent=0, bulletIndent=6, spaceAfter=3)
sCap = ParagraphStyle("Cap", parent=styles["Normal"], fontSize=7.6, leading=10.5,
                      textColor=colors.HexColor(MUTED), alignment=TA_CENTER, spaceAfter=8)
sSmall = ParagraphStyle("Small", parent=styles["Normal"], fontSize=8.2, leading=11.5,
                        textColor=colors.HexColor(MUTED), alignment=TA_LEFT, spaceAfter=3)
sTableCell = ParagraphStyle("TC", parent=styles["Normal"], fontSize=8.3, leading=10.8,
                            textColor=colors.HexColor("#23272e"), alignment=TA_LEFT)
sTableCellR = ParagraphStyle("TCR", parent=sTableCell, alignment=TA_RIGHT)
sTableCellC = ParagraphStyle("TCC", parent=sTableCell, alignment=TA_CENTER)
sTableHead = ParagraphStyle("TH", parent=styles["Normal"], fontSize=8.3, leading=10.8,
                            textColor=colors.white, alignment=TA_CENTER, fontName="Helvetica-Bold")
sTableHeadL = ParagraphStyle("THL", parent=sTableHead, alignment=TA_LEFT)
sTableHeadR = ParagraphStyle("THR", parent=sTableHead, alignment=TA_RIGHT)
sKPI = ParagraphStyle("KPI", parent=styles["Normal"], fontSize=8.4, leading=11,
                      textColor=colors.HexColor(MUTED), alignment=TA_CENTER)
sKPIV = ParagraphStyle("KPIV", parent=styles["Normal"], fontSize=13.5, leading=16,
                       textColor=colors.HexColor(INK), alignment=TA_CENTER, fontName="Helvetica-Bold")
sKPIL = ParagraphStyle("KPIL", parent=styles["Normal"], fontSize=7.8, leading=10,
                       textColor=colors.HexColor(MUTED), alignment=TA_CENTER)

def P(txt, style=sBody):
    return Paragraph(txt, style)

def styled_table(data, col_widths, header=True, zebra=True, fontsize=8.3, aligns=None):
    t = Table(data, colWidths=col_widths, repeatRows=1 if header else 0)
    sty = []
    if header:
        sty += [("BACKGROUND", (0, 0), (-1, 0), colors.HexColor(BAND)),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), fontsize),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 7),
                ("TOPPADDING", (0, 0), (-1, 0), 7)]
    if zebra:
        for i in range(1, len(data)):
            if i % 2 == 0:
                sty.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor(LIGHT_BG)))
    sty += [("FONTSIZE", (0, 0), (-1, -1), fontsize),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 1), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 1), (-1, -1), 4),
            ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("GRID", (0, 0), (-1, -1), 0.6, colors.HexColor(GRID)),
            ("LINEBELOW", (0, 0), (-1, 0), 1.6, colors.HexColor(VOLT_DARK))]
    t.setStyle(TableStyle(sty))
    return t

def cell(txt, align="L"):
    st = {"L": sTableCell, "R": sTableCellR, "C": sTableCellC}[align]
    return Paragraph(txt, st)

def hcell(txt, align="C"):
    st = {"L": sTableHeadL, "R": sTableHeadR, "C": sTableHead}[align]
    return Paragraph(txt, st)

def section_num(n, title):
    return P(f'<font color="{VOLT_DARK}"><b>{n}.</b></font>&nbsp;&nbsp;<b>{title}</b>', sH1)

# ============ CHARTS ============
plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False})

def chart_revenue_eps():
    yrs = ["FY21", "FY22", "FY23", "FY24", "FY25", "FY26"]
    rev = [44.5, 46.7, 51.2, 51.4, 46.3, 46.4]
    eps = [3.56, 3.75, 3.23, 3.73, 2.16, 2.10]
    fig, ax1 = plt.subplots(figsize=(7.2, 3.1))
    x = np.arange(len(yrs))
    b = ax1.bar(x, rev, color="#1f5fa8", alpha=0.88, width=0.62, label="Revenue ($B)")
    ax1.set_ylabel("Revenue ($B)", color="#1f5fa8")
    ax1.set_xticks(x); ax1.set_xticklabels(yrs)
    ax1.set_ylim(0, 58)
    for i, v in enumerate(rev):
        ax1.text(i, v + 0.9, f"{v:.1f}", ha="center", fontsize=8, color="#1f5fa8")
    ax2 = ax1.twinx()
    ax2.plot(x, eps, color="#c0392b", marker="o", lw=2.2, label="Diluted EPS ($)")
    ax2.set_ylabel("Diluted EPS ($)", color="#c0392b")
    ax2.set_ylim(0, 4.4)
    for i, v in enumerate(eps):
        ax2.annotate(f"${v:.2f}", (i, v), textcoords="offset points", xytext=(8, 16), fontsize=8, color="#c0392b",
                     bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.85))
    ax2.spines["top"].set_visible(False)
    plt.title("Nike revenue and diluted EPS, FY2021–FY2026", fontsize=10.5, loc="left", pad=10)
    fig.tight_layout()
    p = os.path.join(CHART_DIR, "rev_eps.png"); fig.savefig(p, dpi=170); plt.close(fig)
    return p

def chart_margins():
    yrs = ["FY21", "FY22", "FY23", "FY24", "FY25", "FY26"]
    gm = [44.8, 46.0, 43.5, 44.6, 42.7, 42.9]
    om = [15.6, 14.3, 11.5, 12.3, 8.0, 8.2]
    nm = [12.9, 12.9, 9.9, 11.1, 6.9, 6.7]
    x = np.arange(len(yrs)); w = 0.24
    fig, ax = plt.subplots(figsize=(7.2, 3.0))
    ax.bar(x - w, gm, w, label="Gross margin", color="#1f5fa8")
    ax.bar(x, om, w, label="Operating margin", color="#9dbb1a")
    ax.bar(x + w, nm, w, label="Net margin", color="#c0392b")
    ax.set_xticks(x); ax.set_xticklabels(yrs)
    ax.set_ylabel("Margin (%)"); ax.set_ylim(0, 52)
    ax.legend(frameon=True, facecolor="white", framealpha=0.9, ncol=3, loc="upper right", fontsize=8.5)
    plt.title("Nike margin profile, FY2021–FY2026", fontsize=10.5, loc="left", pad=8)
    fig.tight_layout()
    p = os.path.join(CHART_DIR, "margins.png"); fig.savefig(p, dpi=170); plt.close(fig)
    return p

def chart_dcf():
    labels = ["Bear\n$20", "Base\n$48", "Bull\n$67"]
    vals = [20, 48, 67]
    cols = ["#c0392b", "#1f5fa8", "#1e8449"]
    fig, ax = plt.subplots(figsize=(7.2, 3.0))
    b = ax.bar(labels, vals, color=cols, alpha=0.9, width=0.55)
    ax.axhline(35.56, color="#111418", ls="--", lw=1.4, label="Current price $35.56")
    ax.axhline(45, color="#6e8512", ls=":", lw=1.4, label="Probability-weighted fair value $45")
    for i, v in enumerate(vals):
        ax.text(i, v + 1.2, f"${v}", ha="center", fontsize=10, fontweight="bold")
    ax.set_ylabel("Value per share ($)")
    ax.set_ylim(0, 80)
    ax.legend(frameon=False, fontsize=8.5, loc="upper left")
    plt.title("DCF scenario values vs. current price", fontsize=10.5, loc="left", pad=10)
    fig.tight_layout()
    p = os.path.join(CHART_DIR, "dcf.png"); fig.savefig(p, dpi=170); plt.close(fig)
    return p

def chart_peers():
    names = ["Nike", "Adidas", "Deckers", "On Holding", "Lululemon"]
    ttm = [17.0, 20.0, 11.1, 22.7, 9.3]
    cols = ["#1f5fa8", "#5b6470", "#5b6470", "#5b6470", "#5b6470"]
    fig, ax = plt.subplots(figsize=(7.2, 3.0))
    b = ax.bar(names, ttm, color=cols, alpha=0.9, width=0.58)
    ax.axhline(28.4, color="#c0392b", ls="--", lw=1.2, label="Nike 5-yr avg P/E (28.4×)")
    for i, v in enumerate(ttm):
        ax.text(i, v + 0.5, f"{v:.1f}×", ha="center", fontsize=9)
    ax.set_ylabel("Trailing P/E (×)")
    ax.set_ylim(0, 34)
    ax.legend(frameon=False, fontsize=8.5)
    plt.title("Trailing P/E: Nike vs. peers (Sep 2026)", fontsize=10.5, loc="left", pad=10)
    fig.tight_layout()
    p = os.path.join(CHART_DIR, "peers.png"); fig.savefig(p, dpi=170); plt.close(fig)
    return p

def chart_china():
    brands = ["Nike", "Adidas", "Anta\n(core)", "Li-Ning", "361°", "Xtep\n(core)"]
    g = [-13, 16, 2, 3.3, 8, -4]
    cols = ["#c0392b" if v < 0 else "#1e8449" for v in g]
    fig, ax = plt.subplots(figsize=(7.2, 3.0))
    b = ax.bar(brands, g, color=cols, alpha=0.9, width=0.58)
    ax.axhline(0, color="#111418", lw=0.8)
    for i, v in enumerate(g):
        ax.text(i, v + (0.5 if v >= 0 else -1.1), f"{v:+.0f}%" if v == int(v) else f"{v:+.1f}%",
                ha="center", fontsize=9, fontweight="bold")
    ax.set_ylabel("China revenue growth (%, c-c)")
    ax.set_ylim(-18, 20)
    plt.title("Greater China growth, most recent period (currency-neutral)", fontsize=10.5, loc="left", pad=10)
    fig.tight_layout()
    p = os.path.join(CHART_DIR, "china.png"); fig.savefig(p, dpi=170); plt.close(fig)
    return p

c_rev = chart_revenue_eps(); c_marg = chart_margins(); c_dcf = chart_dcf()
c_peer = chart_peers(); c_china = chart_china()

# ============ DOCUMENT ============
doc = SimpleDocTemplate(OUT, pagesize=LETTER, leftMargin=0.72*inch, rightMargin=0.72*inch,
                        topMargin=0.6*inch, bottomMargin=0.6*inch,
                        title="Nike, Inc. (NKE) Equity Research — September 2026",
                        author="Equity Research")

story = []

def hr():
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor(GRID), spaceAfter=6, spaceBefore=6))

def kpi_row(items):
    # items: list of (value, label)
    row = [[P(f'<b>{v}</b>', sKPIV) for v, l in items]]
    row.append([P(l, sKPIL) for v, l in items])
    t = Table(row, colWidths=[7.06*inch/len(items)]*len(items))
    t.setStyle(TableStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                           ("TOPPADDING", (0,0), (-1,-1), 3),
                           ("BOTTOMPADDING", (0,0), (-1,-1), 3)]))
    story.append(t)

def img(path, width=7.0*inch):
    story.append(Image(path, width=width, height=width*0.44))

# ============ COVER ============
story.append(Spacer(1, 0.55*inch))
story.append(P("EQUITY RESEARCH", ParagraphStyle("k", parent=sSub, fontSize=10, textColor=colors.HexColor(VOLT_DARK), fontName="Helvetica-Bold")))
story.append(P("NIKE, Inc.", sTitle))
story.append(P("NYSE: NKE &nbsp;·&nbsp; Athletic Footwear & Apparel", sSub))
story.append(Spacer(1, 0.12*inch))
story.append(HRFlowable(width="100%", thickness=3, color=colors.HexColor(BAND), spaceAfter=10, spaceBefore=4))

verdict_data = [
    [P("<b>VERDICT</b>", sKPI), P("<b>12-MONTH TARGET</b>", sKPI), P("<b>IMPLIED UPSIDE</b>", sKPI), P("<b>RISK RATING</b>", sKPI)],
    [P('<font color="#1e8449"><b>BUY</b></font>', ParagraphStyle("vv", parent=sKPIV, fontSize=17)),
     P("<b>$46.00</b>", ParagraphStyle("vv2", parent=sKPIV, fontSize=17)),
     P('<font color="#1e8449"><b>+29%</b></font>', ParagraphStyle("vv3", parent=sKPIV, fontSize=17)),
     P('<font color="#c0392b"><b>HIGH</b></font>', ParagraphStyle("vv4", parent=sKPIV, fontSize=17))],
]
vt = Table(verdict_data, colWidths=[1.70*inch]*4)
vt.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,0), colors.HexColor(LIGHT_BG)),
                        ("BOX", (0,0), (-1,-1), 1, colors.HexColor(GRID)),
                        ("INNERGRID", (0,0), (-1,-1), 0.6, colors.HexColor(GRID)),
                        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6)]))
story.append(vt)
story.append(Spacer(1, 0.18*inch))

kpi_row([("$35.56", "Price (close 9/18/26)"), ("$52.7B", "Market cap"),
         ("$45", "DCF fair value (wtd.)"), ("4.6%", "Dividend yield")])
story.append(Spacer(1, 0.12*inch))
story.append(P("Date: September 19, 2026 &nbsp;·&nbsp; Fiscal year ends May 31 &nbsp;·&nbsp; Most recent results: Q4/FY2026 (reported June 30, 2026). "
               "Q1 FY2027 earnings are scheduled for October 1, 2026; Investor Day November 16–17, 2026.", sSmall))
story.append(Spacer(1, 0.28*inch))
story.append(P("<b>Thesis in one paragraph.</b> Nike is the world's largest athletic footwear and apparel company trading at a 12-year low after "
               "losing ~79% from its 2021 peak — not because the brand is dying, but because three self-inflicted and cyclical wounds converged: an "
               "over-pivot to DTC that alienated wholesale partners, a fashion-cycle rotation away from retro lifestyle franchises, and a China-specific "
               "execution failure while Adidas grew 16% in the same market. CEO Elliott Hill's turnaround (wholesale re-engagement, marketplace cleanup, "
               "a 'Sport Offense' reorg) is showing early green shoots — North America wholesale up 10% in Q4, positive Foot Locker comps for the first time "
               "in four years — but FY2027 is explicitly a transition year with revenue guided down and China getting worse on purpose. At $35.56 the stock "
               "prices in failure: 17× trough earnings (vs. a 5-year average of 28×), a 4.6% dividend yield (highest in the Dow), and a probability-weighted "
               "DCF fair value of ~$45. We rate NKE a <b>BUY</b> with <b>High</b> risk: a small starter position now, with dry powder reserved for the "
               "October 1 print and the November Investor Day.", sBody))
story.append(Spacer(1, 0.18*inch))
story.append(P("This report is independent analysis for informational purposes and is not investment advice. All figures are sourced; see Sources (Section 10).", sSmall))

# ============ 1. EXECUTIVE SUMMARY ============
story.append(section_num(1, "Executive summary"))
story.append(P("Nike closed FY2026 (May 2026) with revenue of <b>$46.4 billion — flat</b> year over year — and diluted EPS of <b>$2.10</b>, down 3%. "
               "The headline numbers flatter reality: Q4 included an expected ~$986 million recovery of IEEPA tariffs that added ~900 bps to gross margin "
               "and $0.52 to EPS. Excluding it, FY2026 EPS was closer to <b>$1.58</b> and underlying gross margin ~40.8%, still below the 43–46% Nike earned "
               "in FY2021–24. The business is a tale of two channels: <b>wholesale rebounded</b> (+6% for the year, +10% in North America in Q4) as Hill "
               "re-engaged retail partners, while <b>Nike Direct deteriorated</b> (–6% for the year, digital –12%). Greater China fell 13% currency-neutral "
               "for the eighth straight declining quarter; Converse collapsed 31% to $1.2B. The balance sheet remains investment-grade ($9.0B cash vs. "
               "$7.9B debt), but free cash flow fell to $2.2B and the dividend now consumes more than underlying net income — buybacks were effectively "
               "paused at $123M.", sBody))
snap = [
    [hcell("Metric", "L"), hcell("Value"), hcell("Metric", "L"), hcell("Value")],
    [cell("Share price (9/18/26 close)"), cell("$35.56", "R"), cell("52-week range"), cell("$35.50 – $76.97", "R")],
    [cell("Market capitalization"), cell("~$52.7B", "R"), cell("Shares outstanding (diluted)"), cell("~1.48B", "R")],
    [cell("YTD / 1-yr / 5-yr price return"), cell("–44.3% / –49.9% / ~–76%", "R"), cell("Beta"), cell("1.06", "R")],
    [cell("TTM P/E (GAAP) / forward P/E"), cell("~17× / ~18–21×", "R"), cell("EV / EBITDA (TTM)"), cell("~9.0×", "R")],
    [cell("Dividend (FY26) / yield"), cell("$1.63 / 4.6%", "R"), cell("Net debt / (cash)"), cell("~$(1.1)B net cash", "R")],
    [cell("Consensus rating / avg. target"), cell("Hold–Buy / ~$48", "R"), cell("Our 12-mo target / upside"), cell("$46.00 / +29%", "R")],
]
story.append(styled_table(snap, [2.1*inch, 1.43*inch, 2.1*inch, 1.43*inch]))
story.append(P("Figure notes: price, market cap, 52-week range, beta, returns via Finnhub/MarketBeat/Robinhood quote pages, Sep 18–19, 2026. "
               "P/E and EV/EBITDA per Forbes/Finnhub; net cash = $9.0B cash & ST investments less $7.9B total debt (FY26 10-K). "
               "Consensus target ~$48 average across aggregators (range $30–$75).", sSmall))

# ============ 2. COMPANY & BUSINESS OVERVIEW ============
story.append(section_num(2, "Company & business overview"))
story.append(P("Founded in 1964 as Blue Ribbon Sports and headquartered in Beaverton, Oregon, NIKE, Inc. is the <b>largest seller of athletic footwear "
               "and apparel in the world</b>. It designs and markets products under the Nike, Jordan (Jumpman) and Converse brands across footwear, "
               "apparel, equipment and accessories, selling through wholesale partners (~18,000 retail accounts worldwide), Nike Direct (company-owned "
               "stores plus Nike Brand Digital, including the Nike App and SNKRS), and independent distributors. Reportable segments are North America, "
               "EMEA, Greater China, Asia Pacific & Latin America (APLA), Global Brand Divisions, Converse, and Corporate.", sBody))
story.append(P("<b>Leadership.</b> Elliott Hill became President & CEO in October 2024, returning after 32 years at Nike. His turnaround program — "
               "dubbed the <b>'Sport Offense'</b> — reverses the prior DTC-first strategy: re-engaging wholesale (Foot Locker, Dick's and others), "
               "cleaning up excess inventory and discounting, cutting retro-lifestyle overexposure, and reorganizing around sport verticals with "
               "dedicated teams for sportswear and Jordan. CFO Matthew Friend is being succeeded by an external hire ('Denton') who started August 17, "
               "2026; the chief accounting officer/controller resigned effective September 4, 2026, with the new CFO doubling as interim controller — "
               "a finance-function transition to watch into the November Investor Day. Executive Chairman is Mark Parker.", sBody))
story.append(P("<b>FY2026 revenue mix</b> (year ended May 31, 2026; per Q4 FY26 press release):", sH2))
mix = [
    [hcell("Category", "L"), hcell("FY2026 revenue"), hcell("Reported y/y"), hcell("Currency-neutral y/y")],
    [cell("Nike Brand footwear"), cell("$29.5B", "R"), cell("flat", "R"), cell("–2%", "R")],
    [cell("Nike Brand apparel"), cell("$13.4B", "R"), cell("+4%", "R"), cell("+2%", "R")],
    [cell("Nike Brand equipment"), cell("$2.2B", "R"), cell("flat", "R"), cell("–2%", "R")],
    [cell("<b>Total Nike Brand</b>"), cell("<b>$45.2B</b>", "R"), cell("<b>+1%</b>", "R"), cell("<b>–1%</b>", "R")],
    [cell("Wholesale"), cell("$27.5B", "R"), cell("+6%", "R"), cell("+4%", "R")],
    [cell("Nike Direct (stores + digital)"), cell("$17.7B", "R"), cell("–6%", "R"), cell("–8%", "R")],
    [cell("of which: Jordan Brand"), cell("$7.0B", "R"), cell("–3%", "R"), cell("–5%", "R")],
    [cell("Converse"), cell("$1.2B", "R"), cell("–31%", "R"), cell("–32%", "R")],
    [cell("<b>Total NIKE, Inc.</b>"), cell("<b>$46.4B</b>", "R"), cell("<b>flat</b>", "R"), cell("<b>–2%</b>", "R")],
]
story.append(styled_table(mix, [2.6*inch, 1.3*inch, 1.55*inch, 1.61*inch]))
story.append(P("Geography: North America grew in Q4 (+3% reported; wholesale +10%), EMEA fell 6%, APLA fell 1%, and Greater China fell 17% "
               "currency-neutral. Full-year Greater China revenue was $5.85B (–11% reported / –13% c-c) with EBIT down 20% to ~$1.3B — its eighth "
               "consecutive declining quarter. The US is now ~44% of revenue by subtraction rather than growth, raising tariff and consumer-cycle "
               "concentration.", sBody))

# ============ 3. FINANCIAL DEEP-DIVE ============
story.append(section_num(3, "Financial deep-dive"))
story.append(P("<b>Income statement trend.</b> FY2025 was the reset year — revenue fell 10%, operating margin compressed to 8.0%, and FCF was cut "
               "roughly in half. FY2026 stabilized revenue but earnings quality deteriorated: the IEEPA tariff recovery (~$986M pre-tax in Q4) is "
               "non-recurring, and without it EPS would have been ~$1.58 rather than $2.10.", sH2))
inc = [
    [hcell("$ millions except per-share", "L"), hcell("FY21"), hcell("FY22"), hcell("FY23"), hcell("FY24"), hcell("FY25"), hcell("FY26")],
    [cell("Revenue"), cell("44,538", "R"), cell("46,710", "R"), cell("51,217", "R"), cell("51,362", "R"), cell("46,309", "R"), cell("46,398", "R")],
    [cell("Revenue growth"), cell("—", "C"), cell("+4.9%", "R"), cell("+9.6%", "R"), cell("+0.3%", "R"), cell("–9.8%", "R"), cell("+0.2%", "R")],
    [cell("Gross profit"), cell("19,962", "R"), cell("21,479", "R"), cell("22,292", "R"), cell("22,887", "R"), cell("19,790", "R"), cell("19,911", "R")],
    [cell("Gross margin"), cell("44.8%", "R"), cell("46.0%", "R"), cell("43.5%", "R"), cell("44.6%", "R"), cell("42.7%", "R"), cell("42.9%*", "R")],
    [cell("SG&A"), cell("13,025", "R"), cell("14,804", "R"), cell("16,377", "R"), cell("16,576", "R"), cell("16,088", "R"), cell("16,114", "R")],
    [cell("Operating income"), cell("6,937", "R"), cell("6,675", "R"), cell("5,915", "R"), cell("6,311", "R"), cell("3,702", "R"), cell("3,797", "R")],
    [cell("Operating margin"), cell("15.6%", "R"), cell("14.3%", "R"), cell("11.5%", "R"), cell("12.3%", "R"), cell("8.0%", "R"), cell("8.2%", "R")],
    [cell("Net income"), cell("5,727", "R"), cell("6,046", "R"), cell("5,070", "R"), cell("5,700", "R"), cell("3,219", "R"), cell("3,108", "R")],
    [cell("Diluted EPS (GAAP)"), cell("$3.56", "R"), cell("$3.75", "R"), cell("$3.23", "R"), cell("$3.73", "R"), cell("$2.16", "R"), cell("$2.10*", "R")],
    [cell("Operating cash flow"), cell("6,657", "R"), cell("5,188", "R"), cell("5,841", "R"), cell("7,429", "R"), cell("3,698", "R"), cell("2,868", "R")],
    [cell("Free cash flow"), cell("5,962", "R"), cell("4,430", "R"), cell("4,872", "R"), cell("6,617", "R"), cell("3,268", "R"), cell("2,184", "R")],
]
story.append(styled_table(inc, [1.86*inch, 0.87*inch, 0.87*inch, 0.87*inch, 0.87*inch, 0.87*inch, 0.87*inch], fontsize=7.9))
story.append(P("* FY2026 includes the expected IEEPA tariff recovery (~$986M pre-tax; +210 bps to full-year gross margin; +$0.52 to Q4/FY EPS). "
               "Ex-tariff FY2026: gross margin ~40.8%, diluted EPS ~$1.58. FY21–25 per 10-K filings via MarketBeat/Zacks compilations; FY26 per June 30, 2026 release and 10-K.", sSmall))
story.append(P("Key reads:", sH2))
story.append(P("• <b>Margins are troughing, not recovered.</b> Gross margin of 42.9% is 170–310 bps below the FY21–24 range; ex-tariff it is ~40.8%. "
               "SG&A was flat at $16.1B only because severance and FX headwinds offset cost discipline — demand-creation spend actually rose 1% to $4.8B. "
               "Q4 SG&A fell 2% to $4.1B (37.2% of revenue) and Q4 EBIT margin hit 12.0% including tariffs — early evidence the cost base is responding.", sBullet))
story.append(P("• <b>Cash conversion weakened.</b> Operating cash flow fell 22% to $2.87B, driven by a $1.68B working-capital drag — notably a jump in "
               "accounts receivable to $5.9B from the outstanding IEEPA tariff receivable plus higher wholesale shipments. Capex was $684M; FCF of $2.18B "
               "fell 33%.", sBullet))
story.append(P("• <b>Channel inversion is the story.</b> Wholesale (+6%) more than offset Direct (–6%); Nike Brand Digital fell 12% for the year and 25% "
               "in Greater China in Q4. Management is deliberately sacrificing near-term Direct revenue to restore full-price health — gross margins are "
               "guided to turn slightly positive starting Q1 FY27.", sBullet))
story.append(P("• <b>Balance sheet: solid but less fortress-like.</b> $9.0B of cash & short-term investments vs. $7.9B of total debt ($2.0B current + "
               "$5.9B long-term); net cash ~$1.1B. Inventories flat at $7.5B — the multi-year glut is cleared. But shareholder returns are now "
               "dividend-only: $2.4B of dividends (+5%; $1.63/share) plus just $123M of buybacks (1.8M shares) under the $18B authorization. The dividend "
               "payout was 77% of GAAP net income — and <b>~103% of ex-tariff net income</b> — a coverage flag worth monitoring.", sBody))
img(c_rev, 7.06*inch)
story.append(P("Nike revenue peaked in FY2024 at $51.4B and has been flat-to-down since; diluted EPS has fallen 44% from the FY2022 peak of $3.75. "
               "FY2026 GAAP EPS of $2.10 includes the $0.52 non-recurring tariff benefit.", sCap))
img(c_marg, 7.06*inch)
story.append(P("Operating margin has nearly halved from the FY2021 peak (15.6% → 8.2%); gross margin ex-tariff (~40.8% in FY26) sits ~300–500 bps "
               "below the FY21–22 level. Recovery of both is the core of the bull case.", sCap))
story.append(P("<b>Q4 FY2026 snapshot</b> (the quarter that set the FY27 bar): revenue $11.0B (–1% reported / –4% c-c); wholesale $6.6B (+4%); Direct $4.1B "
               "(–7%); gross margin 49.2% (+890 bps incl. ~900 bps tariff benefit); net income $1.1B (+407%); EPS $0.72 incl. $0.52 tariff benefit ($0.20 "
               "ex-benefit, vs. $0.11 consensus). North America +3% (wholesale +10%; positive Foot Locker comps for the first time in four years); "
               "Greater China –17% c-c; EMEA –6%; APLA –1%.", sBody))
story.append(P("<b>FY2027 guidance</b> (June 30 call; no full-year guide — deferred to the November Investor Day): Q1 FY27 revenue down <b>low-to-mid "
               "single digits</b> with no FX benefit; Q2 to decelerate sequentially on a 'multipoint headwind' (EMEA digital-promo comps, a North America "
               "wholesale shipment-timing anomaly); cumulative H1 EPS roughly <b>flattish excluding the tariff benefit</b>, with the mix shifting toward "
               "lower revenue but higher gross margins (turning slightly positive from Q1). Tariff headwinds persist through Q1 FY27; margin expansion "
               "is expected from Q2. For calendar 2026, management guides revenue down a low-single-digit percentage, with North America growth offset by "
               "China declines. UBS (September) expects a ~$0.05 Q1 EPS miss and sees Q2 EPS of $0.31–0.43 vs. $0.53 consensus — the near-term bar is low, "
               "but so is visibility.", sBody))

# ============ 4. GROWTH DRIVERS, MOAT, PROJECTIONS ============
story.append(section_num(4, "Growth drivers, moat, and future projections"))
story.append(P("<b>Moat assessment: wide but narrowing.</b> Nike's moat rests on four pillars: (1) <b>brand equity</b> — still the most recognized "
               "athletic brand globally, with the Swoosh, Jordan and Converse in the portfolio; (2) <b>athlete IP</b> — lifetime/flagship relationships "
               "(Cristiano Ronaldo's reported $1B lifetime deal, LeBron James, and a newly extended long-term Victor Wembanyama deal with a signature line, "
               "July 2026); (3) <b>innovation</b> — Nike Air, ZoomX and React platforms, Vaporfly/Alphafly racers that reset marathon records; and (4) "
               "<b>scale</b> — $46B of revenue funding R&D and marketing at a level no challenger can match. The moat is intact but has demonstrably "
               "narrowed: share losses to Hoka/On in performance running, to Adidas in China and lifestyle, and fashion-cycle fatigue in retro franchises "
               "show the brand no longer converts automatically into growth.", sBody))
story.append(P("<b>Growth drivers under the turnaround:</b>", sH2))
story.append(P("• <b>Wholesale reset.</b> The deliberate reversal of the DTC over-pivot is working where it matters: North America wholesale +10% in Q4, "
               "positive Foot Locker revenue and retail-sales comps for the first time in four years. Wholesale is higher-velocity and lower-cost than "
               "Nike's own digital operation, and partner sell-through is the cleanest read on brand health.", sBullet))
story.append(P("• <b>Performance-product pipeline.</b> Management cites momentum in performance running and says <b>more than a dozen new footwear styles "
               "— new silhouettes leveraging innovation, not retro reissues — launch in H2 FY2027</b>. Hill: 'This work will take time to scale.' "
               "The 2026 FIFA World Cup (Nike kitted 12 of 48 nations) was a brand showcase, though share of kits fell from ~40% at Qatar 2022.", sBullet))
story.append(P("• <b>China reset — the swing factor.</b> Nike is executing a 'comprehensive reset': local product creation, sport-led storytelling, and a "
               "July 2026 <b>distributor overhaul severing thousands of online distributors effective January 1, 2027</b> to kill discount-driven "
               "marketplace pollution. Management says the cleanup keeps revenue pressured through FY2027 but that <b>profitability 'should bottom "
               "sooner'</b>. Digital full-price realization is improving and China inventory fell double digits — the right leading indicators, even as "
               "reported revenue keeps falling.", sBullet))
story.append(P("• <b>Margin normalization.</b> Gross margin ex-tariff (~40.8%) has 300–500 bps of recovery potential toward the historical 43–46% band "
               "as promotions normalize, freight/tariff headwinds ease from Q2 FY27, and mix shifts back to full-price performance product. Every 100 bps "
               "of gross margin on ~$47B of revenue is worth ~$0.25 of EPS.", sBullet))
story.append(P("• <b>Capital allocation optionality.</b> With net cash and a $18B buyback authorization barely touched ($123M used in FY26), any "
               "stabilization of earnings would let Nike resume meaningful repurchases at 12-year-low prices — powerful EPS leverage the market is not "
               "pricing in.", sBullet))
img(c_china, 7.06*inch)
story.append(P("Nike's –13% c-c decline in Greater China is a Nike-specific execution failure, not a structural rejection of Western brands: Adidas grew "
               "+16% c-c in H1 2026 in the same market, and the domestic champions (Anta core low-single-digit, Li-Ning +3.3% on promotions, Xtep core "
               "negative) are not absorbing Nike's lost volume — it is fragmenting to Adidas and premium specialists. That makes the problem fixable, "
               "but also removes the macro excuse.", sCap))
story.append(P("<b>Our projections (base case).</b> We model FY2027 as the transition trough — revenue roughly flat with H1 declines offset by H2 "
               "stabilization, margins beginning to recover from Q2 — followed by mid-single-digit growth as the pipeline scales and China laps the "
               "distributor reset. Key assumptions: gross margin recovers ~100–150 bps/year toward 44% by FY29; SG&A grows slower than revenue "
               "(operating leverage returns); tax rate ~19–20%; share count roughly flat (buybacks offset SBC until earnings stabilize).", sH2))
proj = [
    [hcell("Base case", "L"), hcell("FY26A"), hcell("FY27E"), hcell("FY28E"), hcell("FY29E")],
    [cell("Revenue ($B)"), cell("46.4", "R"), cell("47.0", "R"), cell("49.5", "R"), cell("52.2", "R")],
    [cell("Revenue growth"), cell("+0.2%", "R"), cell("+1.3%", "R"), cell("+5.3%", "R"), cell("+5.5%", "R")],
    [cell("Gross margin"), cell("42.9%*", "R"), cell("41.5%", "R"), cell("42.8%", "R"), cell("43.6%", "R")],
    [cell("Operating margin"), cell("8.2%", "R"), cell("8.8%", "R"), cell("10.8%", "R"), cell("12.2%", "R")],
    [cell("Diluted EPS ($)"), cell("$2.10*", "R"), cell("$1.90", "R"), cell("$2.70", "R"), cell("$3.40", "R")],
    [cell("Free cash flow ($B)"), cell("2.2", "R"), cell("2.6", "R"), cell("3.3", "R"), cell("4.0", "R")],
]
story.append(styled_table(proj, [2.26*inch, 1.2*inch, 1.2*inch, 1.2*inch, 1.2*inch]))
story.append(P("* FY26 GAAP incl. $0.52/share tariff benefit (ex-benefit EPS ~$1.58; ex-benefit gross margin ~40.8%). Our FY27E EPS of $1.90 sits "
               "between Argus ($1.70) and the June-vintage consensus (~$1.9); one aggregator's $3.00 FY27E looks stale against management's "
               "'flattish H1 ex-tariff' guide and we do not use it. FY28E $2.70 vs. Argus $2.25 — our bull-leaning H2 FY27 pipeline assumption is the "
               "difference, and the key forecast risk.", sSmall))

# ============ 5. PRODUCT EVALUATION ============
story.append(section_num(5, "Product evaluation"))
story.append(P("<b>Franchise scorecard.</b> Nike's portfolio splits into performance (running, basketball, football/soccer, training) and sportswear/"
               "lifestyle (retro and heritage silhouettes). The last three years over-indexed on the latter — Air Force 1, Dunk and Air Jordan 1 "
               "flooded the market through DTC, training consumers to wait for discounts and hollowing out full-price credibility. That is the "
               "fashion-cycle half of Nike's problem, and Hill's team is explicitly correcting it: fewer retro reissues, more innovation-led "
               "silhouettes, tighter marketplace supply.", sBody))
prod = [
    [hcell("Franchise / line", "L"), hcell("Status"), hcell("Assessment")],
    [cell("Pegasus / Vomero (daily trainers)"), cell("Core", "C"),
     cell("Workhorses of the running line; Vomero has been a bright spot in performance running's rebound.")],
    [cell("Vaporfly / Alphafly (racers)"), cell("Leadership", "C"),
     cell("Still the reference marathon racers; the halo that authenticates the running brand.")],
    [cell("Air Force 1 / Dunk"), cell("Fatigued", "C"),
     cell("Oversupplied during the DTC push; the epicenter of discounting and the deliberate pullback.")],
    [cell("Air Jordan (Brand: $7.0B, –3%)"), cell("Resetting", "C"),
     cell("Cultural icon but overexposed; dedicated Jordan team now in place under the Sport Offense.")],
    [cell("Football (soccer)"), cell("Pressured", "C"),
     cell("World Cup kits down to 12/48 nations; On's signing of Mbappé (Sep 2026) attacks this stronghold directly.")],
    [cell("New H2 FY27 pipeline (12+ styles)"), cell("Watch", "C"),
     cell("Innovation-led, not retro — the single most important product catalyst; unproven at scale.")],
    [cell("Nike App / SNKRS / Membership"), cell("Underused", "C"),
     cell("Best-in-class digital assets starved by the Direct pullback; digital –12% in FY26.")],
    [cell("Converse ($1.2B, –31%)"), cell("Distressed", "C"),
     cell("EBIT –93%; 490 bps gross-margin contraction on discounting and reset costs. Turnaround or exit candidate.")],
]
story.append(styled_table(prod, [2.2*inch, 1.15*inch, 3.71*inch], fontsize=8.0))
story.append(P("Net: the innovation engine (Air/ZoomX platforms, racing halo) is intact and the pipeline is the most promising in three years, but "
               "Nike must prove it can create <i>new</i> cultural hits rather than re-monetize old ones, and must do it while Converse burns and "
               "Jordan is deliberately cooled. Product risk is execution risk, not R&D risk.", sBody))

# ============ 6. COMPETITIVE LANDSCAPE ============
story.append(section_num(6, "Competitive landscape"))
story.append(P("Nike is being squeezed from three directions: <b>premium performance specialists</b> taking the serious runner, <b>Adidas</b> "
               "out-executing it in lifestyle and China, and <b>value/domestic brands</b> pressuring price ladders in Asia.", sBody))
story.append(P("• <b>Adidas — the benchmark turnaround.</b> ~€25B market cap, TTM P/E ~18–22×, forward ~14×. H1 2026 China +16% c-c with DTC +22–27%; "
               "14 World Cup kits (vs. Nike's 12); Samba/Gazelle lifestyle momentum sustained. Adidas is the proof that Nike's China problem is "
               "fixable — and the competitor most directly absorbing Nike's lost share.", sBullet))
story.append(P("• <b>On Holding (ONON, $27.26, –41% YTD)</b> — $9.1B cap, TTM P/E ~19–23× after a 40% derating, $3.2B TTM revenue (+13.5% last quarter), "
               "12.3% net margin, net-cash balance sheet. The Mbappé signing (September 2026) is a declaration of war on Nike's football franchise. "
               "Premium, high-growth, but itself facing tariff headwinds and wholesale throttle-down in the Americas.", sBullet))
story.append(P("• <b>Deckers (DECK, $78.43)</b> — Hoka continues to take performance-running share; the stock has derated to 11.1× TTM (5-yr avg 20.4×) "
               "on growth deceleration — a warning that challenger multiples compress fast when momentum stalls.", sBullet))
story.append(P("• <b>Lululemon</b> — P/E ~9–10×; China +28% but North America soft. Competes at the premium apparel edge where Nike's apparel (+4% in "
               "FY26) is actually holding up.", sBullet))
story.append(P("• <b>Anta / Li-Ning / 361° / Xtep (China)</b> — the 'guochao' wave has crested: Anta's core brand is low-single-digit and its brand CEO "
               "resigned in July 2026 after missing a RMB 60B target by ~40%; Li-Ning grows only via promotions (gross margin down); Xtep's core brand "
               "is shrinking. The domestic threat is fragmenting, not consolidating.", sBullet))
story.append(P("• <b>Puma</b> — loss-making (negative P/E), 11 World Cup kits, and the symbolic coup of Ronaldo — Nike's own $1B lifetime athlete — "
               "spotted wearing Puma pre-match at the World Cup. Weak financially, but culturally opportunistic.", sBullet))
story.append(P("• <b>New Balance</b> — privately held; the quiet share-taker in lifestyle/retro, competing precisely where Nike is pulling back.", sBullet))
img(c_peer, 7.06*inch)
story.append(P("Nike at ~17× TTM trades below Adidas (~18–22×) and On (~19–23×), roughly in line with its trough-earnings reality but well below its "
               "own 5-year average of 28.4×. Deckers (11.1×) and Lululemon (~9.3×) show how far consumer multiples can compress on growth scares; Puma is "
               "loss-making. Multiples per FinanceCharts/Finnhub/MarketBeat, September 2026; Nike 5-yr avg per FinanceCharts.", sCap))

# ============ 7. VALUATION ============
story.append(section_num(7, "Valuation"))
story.append(P("<b>DCF — scenario-weighted (core of our fair value).</b> We value Nike on unlevered free cash flow, appropriate given the net-cash "
               "balance sheet (equity value ≈ enterprise value). WACC 8.5% in the base case: cost of equity ~9.1% (beta 1.06, risk-free ~4.3%, ERP ~4.5%) "
               "blended with a small weight of ~4.5% after-tax debt cost. FCF bridges from the Section 4 projections (EBITDA less cash taxes, capex "
               "~$0.7B, normalized working capital).", sBody))
dcf = [
    [hcell("Scenario", "L"), hcell("Probability"), hcell("FCF FY27–30 ($B)"), hcell("WACC / term. growth"), hcell("Value/share", "R")],
    [cell("<b>Bear —</b> China keeps declining; Direct falls further; margins stuck ~8%; dividend coverage forces a cut"),
     cell("25%", "C"), cell("1.8 / 2.0 / 2.1 / 2.2", "C"), cell("9.5% / 2.5%", "C"), cell("<b>$20</b>", "R")],
    [cell("<b>Base —</b> FY27 trough, H2 pipeline + wholesale momentum; GM recovers toward 44%; China stabilizes in FY28"),
     cell("55%", "C"), cell("2.6 / 3.3 / 4.0 / 4.6", "C"), cell("8.5% / 2.75%", "C"), cell("<b>$48</b>", "R")],
    [cell("<b>Bull —</b> pipeline becomes cultural hits; China inflects; margins return to 13%+; buybacks resume aggressively"),
     cell("20%", "C"), cell("3.0 / 3.9 / 4.8 / 5.6", "C"), cell("8.0% / 3.0%", "C"), cell("<b>$67</b>", "R")],
    [cell("<b>Probability-weighted fair value</b>"), cell("100%", "C"), cell("—", "C"), cell("—", "C"), cell("<b>~$45</b>", "R")],
]
story.append(styled_table(dcf, [2.9*inch, 0.85*inch, 1.35*inch, 1.1*inch, 0.86*inch], fontsize=7.9))
img(c_dcf, 7.06*inch)
story.append(P("Scenario values vs. the $35.56 close. The weighted fair value of ~$45 anchors our $46 target; the bear case ($20) quantifies why "
               "position sizing must stay small — this is a wide-distribution stock.", sCap))
story.append(P("<b>Sensitivity.</b> At the base-case cash flows, fair value ranges from ~$41 (WACC 9.5%, g 2.0%) to ~$57 (WACC 7.5%, g 3.25%). The "
               "valuation is more sensitive to the margin-recovery assumption than to WACC: if FY30 FCF stalls at $3.5B instead of $4.6B, base-case "
               "value falls to ~$39 — still ~10% above the current price, but the margin of safety thins materially.", sBody))
story.append(P("<b>Relative valuation.</b> On TTM GAAP earnings Nike trades at ~17× — a ~40% discount to its own 5-year average P/E of 28.4× "
               "(FinanceCharts). But trailing earnings are trough earnings: on ex-tariff EPS (~$1.58) the multiple is ~22×, and on FY27E consensus "
               "it is ~18–21× depending on the estimate vintage — i.e., <b>optically cheap on GAAP, fairly priced on normalized forward earnings</b>. "
               "EV/EBITDA of ~9.0× (Forbes) sits at the low end of Nike's historical 12–18× range. Versus peers, Nike trades at a small discount to "
               "Adidas and On on trailing earnings despite superior scale and a net-cash balance sheet — the market is charging Nike a "
               "'show-me' discount for the China/turnaround execution risk. A return to even a 24× multiple on our FY28E EPS of $2.70 implies ~$65, "
               "which frames the bull case; we do not underwrite multiple expansion until the November Investor Day gives multi-year targets.", sBody))
story.append(P("<b>Synthesis → price target.</b> Our probability-weighted DCF fair value is ~$45. Blending with (a) the peer/own-history multiple "
               "cross-check, which supports $44–52 on FY28E earnings at 20–24×, and (b) the ~$48 analyst consensus average target, we set a "
               "<b>12-month price target of $46.00</b> — ~29% upside from $35.56 — with a <b>fair-value range of $40–52</b>. The target embeds "
               "execution of the H2 FY27 pipeline and China stabilization, but no heroic re-rating: it is ~24× our FY27E EPS and ~17× our FY28E EPS.", sBody))

# ============ 8. KEY RISKS ============
story.append(section_num(8, "Key risks"))
risks = [
    ("<b>Greater China — the binary risk.</b> Eight straight declining quarters; FY27 is guided to get worse on purpose (distributor reset effective "
     "Jan 2027). If the reset fails or guochao re-accelerates, the $20 bear case dominates. Mitigant: Adidas's +16% proves demand exists; Nike's "
     "problem is execution, which is fixable.",),
    ("<b>Tariffs & trade policy.</b> The $986M IEEPA recovery is a one-off; underlying tariff headwinds persist through Q1 FY27 and any reversal of the "
     "recovery expectation would hit both earnings and the receivable. Vietnam/Indonesia/China sourcing concentration remains a structural exposure.",),
    ("<b>Nike Direct deterioration.</b> Digital –12% in FY26 and –25% in China in Q4. If wholesale recovery is just channel restocking rather than "
     "sell-through, revenue re-accelerates downward in H2.",),
    ("<b>Fashion-cycle risk.</b> Retro franchises (AF1/Dunk/Jordan 1) drove the last cycle; the new pipeline is unproven at scale. A miss on the "
     "12+ H2 FY27 launches pushes recovery into FY28+.",),
    ("<b>Challenger momentum.</b> Hoka, On (now armed with Mbappé and entering football), and Adidas are all taking specific, high-value segments. "
     "Nike must win back the serious runner while defending lifestyle — a two-front war.",),
    ("<b>Dividend coverage.</b> $2.4B of dividends vs. ~$2.3B of ex-tariff net income; OCF did not cover dividends + capex in FY26. A cut is unlikely "
     "given 22 years of consecutive growth and $9B of cash, but buybacks cannot resume until earnings recover.",),
    ("<b>Execution & finance turnover.</b> New external CFO (Aug 2026) also serving as interim controller after the CAO's resignation, ~10 weeks before "
     "the Investor Day. Turnarounds die in the details; this bears watching.",),
    ("<b>FX & macro.</b> ~56% of revenue outside the US; a strong dollar and discretionary-spending pressure (noted by management from mid-April) "
     "are unhedgeable drags.",),
]
for r in risks:
    story.append(P("• " + r[0], sBullet))

# ============ 9. RECOMMENDATION ============
story.append(section_num(9, "Final recommendation"))
story.append(P("We rate Nike a <b>BUY</b> with a <b>$46.00 12-month price target</b> (~29% upside) and <b>High</b> risk. The rating balances an "
               "unusually favorable price — a 12-year low, 17× trough earnings, a 4.6% yield that pays you to wait, and credible early turnaround "
               "evidence (wholesale, Foot Locker comps, cost discipline, consistent EPS beats: four straight quarters ahead of consensus) — against "
               "a genuinely wide outcome distribution: our bear case is $20, and FY2027 is explicitly guided down with China getting worse before it "
               "gets better.", sBody))
story.append(P("<b>Positioning.</b> Starter position only (1–2% for most portfolios); this is a turnaround option, not a compounder to back up the "
               "truck on. Reserve dry powder for two dated catalysts: <b>Q1 FY27 earnings (October 1, 2026)</b> — watch China trajectory, Digital's "
               "decline rate, and gross margin ex-items — and the <b>Investor Day (November 16–17, 2026)</b>, where multi-year targets will either "
               "validate or reset the recovery math. Add on evidence of China stabilization or pipeline sell-through; reassess on a dividend cut, a "
               "failed pipeline launch, or further Direct deterioration. Suitable for patient, contrarian capital with a 2–3 year horizon; not for "
               "investors who need near-term earnings momentum.", sBody))
story.append(P("<b>What would change our mind.</b> Upgrade conviction (raise target toward $55+): sustained China revenue stabilization, wholesale "
               "sell-through (not just sell-in) growth, and gross margin ex-items inflecting by Q2 FY27. Downgrade to Hold/Sell: Q1 FY27 miss with "
               "China accelerating down, pipeline delays, or finance-function instability persisting past the Investor Day.", sBody))

# ============ 10. SOURCES ============
story.append(section_num(10, "Sources & methodology notes"))
story.append(P("All financial figures are from NIKE, Inc.'s Q4/FY2026 earnings release (June 30, 2026) and FY2026 Form 10-K (filed July 15, 2026) "
               "unless noted. Market data (price $35.56 close 9/18/26; 52-week $35.50–$76.97; market cap ~$52.7B; beta 1.06; returns; dividend $1.63–1.64; "
               "yield ~4.5–4.6%) via Finnhub, MarketBeat, Forbes and Robinhood quote pages, September 18–19, 2026. Guidance and call color via the "
               "Q4 FY26 earnings call (BigGo Finance transcript summary; Sporting Goods Intelligence). Analyst actions/targets via tickergate, "
               "MarketBeat, StockAnalysis, TradingNews, UBS/Argus notes as aggregated September 2026. Peer multiples via FinanceCharts (Sep 18, 2026), "
               "Finnhub and MarketBeat. China competitive data via company reports (Adidas H1 2026, Anta, Li-Ning, 361°, Xtep) as compiled September "
               "2026. World Cup kit counts via Seoul Economic Daily/Nikkei (July 2026). Insider buying (Tim Cook, CEO Hill, directors) via market "
               "reporting, April 2026. S&P 100 removal effective September 21, 2026, per S&P Dow Jones Indices. DCF and projections are the author's "
               "estimates with stated assumptions; consensus figures vary by provider and vintage and are shown as ranges where they conflict.", sBody))
story.append(P("Could not be independently verified: exact FY2025 Greater China revenue base (implied ~$6.6B from reported growth rates; Nike reports "
               "the growth rates, not always the base, in the release text); Nike's precise historical forward P/E series (shown via 5-yr average "
               "28.4× from FinanceCharts); New Balance revenue (private company — discussed qualitatively only).", sBody))
story.append(Spacer(1, 0.2*inch))
story.append(P("— End of report —", ParagraphStyle("end", parent=sCap, fontName="Helvetica-Oblique")))

def footer(canvas, doc_):
    canvas.saveState()
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(colors.HexColor(MUTED))
    canvas.drawString(0.72*inch, 0.45*inch, "Nike, Inc. (NKE) — Equity Research — September 19, 2026 — For informational purposes; not investment advice.")
    canvas.drawRightString(LETTER[0] - 0.72*inch, 0.45*inch, f"Page {doc_.page}")
    canvas.restoreState()

def cover_footer(canvas, doc_):
    if doc_.page == 1:
        return
    footer(canvas, doc_)

doc.build(story, onFirstPage=cover_footer, onLaterPages=footer)
print("Wrote", OUT, os.path.getsize(OUT), "bytes")
