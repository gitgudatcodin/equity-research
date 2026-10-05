#!/usr/bin/env python3
"""Master PDF: Valuation Methodology Addenda (Compounder-Quality Override + International Framework).
Assembles the two addenda, the 54-name qualification table, re-run results, and summary.
House style (reportlab, A4). Research analysis, not investment advice.
"""
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                HRFlowable, PageBreak)
from reportlab.lib import colors

BASE = "/home/hatch/workspace/valuation-addenda"
OUT = "/home/hatch/workspace/your_files/valuation-addenda-compounder-international-2026-10-04.pdf"

NAVY = HexColor("#0F2A44"); ACCENT = HexColor("#0E7C3E"); ORANGE = HexColor("#D96C06")
GOLD = HexColor("#C9A227"); LGRAY = HexColor("#F2F4F7"); MGRAY = HexColor("#D9DEE5")
DGRAY = HexColor("#5A6472"); RED = HexColor("#B42318"); INK = HexColor("#1A2332")
BLUE = HexColor("#1F5FA8")

s_title = ParagraphStyle("t", fontName="Helvetica-Bold", fontSize=26, leading=30, textColor=NAVY)
s_sub = ParagraphStyle("s", fontName="Helvetica", fontSize=11, leading=15, textColor=DGRAY)
s_h1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=14, leading=18, textColor=NAVY, spaceBefore=10, spaceAfter=5)
s_h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=NAVY, spaceBefore=8, spaceAfter=4)
s_h3 = ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=10, leading=13, textColor=NAVY, spaceBefore=6, spaceAfter=3)
s_body = ParagraphStyle("b", fontName="Helvetica", fontSize=9.5, leading=14.5, textColor=INK, alignment=TA_JUSTIFY, spaceAfter=5)
s_bull = ParagraphStyle("bu", parent=s_body, leftIndent=12, bulletIndent=4, spaceAfter=3, alignment=TA_LEFT)
s_quote = ParagraphStyle("q", parent=s_body, leftIndent=14, borderPadding=(4, 4, 4), textColor=DGRAY, spaceAfter=6)
s_small = ParagraphStyle("sm", fontName="Helvetica", fontSize=7.5, leading=10.5, textColor=DGRAY)
s_cell = ParagraphStyle("c", fontName="Helvetica", fontSize=8, leading=11, textColor=INK)
s_cellB = ParagraphStyle("cb", parent=s_cell, fontName="Helvetica-Bold")
s_cellR = ParagraphStyle("cr", parent=s_cell, alignment=TA_RIGHT)
s_cellBR = ParagraphStyle("cbr", parent=s_cellB, alignment=TA_RIGHT)
s_cellC = ParagraphStyle("cc", parent=s_cell, alignment=TA_CENTER)
s_cellBC = ParagraphStyle("cbc", parent=s_cellB, alignment=TA_CENTER)
s_thead = ParagraphStyle("th", parent=s_cell, fontName="Helvetica-Bold", textColor=white, alignment=TA_CENTER, fontSize=7.5, leading=10)
s_theadL = ParagraphStyle("thl", parent=s_thead, alignment=TA_LEFT)
s_tinyc = ParagraphStyle("tc", fontName="Helvetica", fontSize=7, leading=9.5, textColor=INK)
s_tinycB = ParagraphStyle("tcb", parent=s_tinyc, fontName="Helvetica-Bold")
s_tinycR = ParagraphStyle("tcr", parent=s_tinyc, alignment=TA_RIGHT)
s_tinycC = ParagraphStyle("tcc", parent=s_tinyc, alignment=TA_CENTER)
s_caption = ParagraphStyle("cap", fontName="Helvetica-Oblique", fontSize=8, leading=11, textColor=DGRAY, spaceBefore=2, spaceAfter=6)

def P(txt, style=s_body): return Paragraph(txt, style)
def cell(txt, st=s_cell): return Paragraph(txt, st)
def styled_table(data, col_widths, header_rows=1, fontsize=8, rowback=(white, LGRAY)):
    t = Table(data, colWidths=col_widths, repeatRows=header_rows)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, header_rows - 1), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, header_rows - 1), white),
        ("FONTNAME", (0, 0), (-1, header_rows - 1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), fontsize),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("GRID", (0, 0), (-1, -1), 0.4, MGRAY),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("ROWBACKGROUNDS", (0, header_rows), (-1, -1), list(rowback)),
    ]))
    return t

# ---------- markdown -> flowables ----------
def inline_md(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"`([^`]+)`", r'<font face="Courier" size="8">\1</font>', t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\w)\*([^*]+)\*(?!\w)", r"<i>\1</i>", t)
    return t

def md_to_flowables(text, story, title_skip=1):
    lines = text.split("\n")
    i, n = 0, len(lines)
    # skip leading title + italic status line
    skipped = 0
    while skipped < title_skip and i < n:
        if lines[i].startswith("#"):
            skipped += 1
        i += 1
    while i < n and (lines[i].strip() == "" or lines[i].strip().startswith("*Addendum to")):
        i += 1
    buf = []
    def flush_para():
        if buf:
            story.append(P(inline_md(" ".join(buf)), s_body))
            buf.clear()
    while i < n:
        ln = lines[i].rstrip()
        s = ln.strip()
        if s == "":
            flush_para(); i += 1; continue
        if s.startswith("#### "):
            flush_para(); story.append(P(inline_md(s[5:]), s_h3)); i += 1; continue
        if s.startswith("### "):
            flush_para(); story.append(P(inline_md(s[4:]), s_h3)); i += 1; continue
        if s.startswith("## "):
            flush_para(); story.append(P(inline_md(s[3:]), s_h2)); i += 1; continue
        if s.startswith("# "):
            flush_para(); story.append(P(inline_md(s[2:]), s_h1)); i += 1; continue
        if s == "---":
            flush_para(); story.append(HRFlowable(width="100%", thickness=0.5, color=MGRAY, spaceAfter=6, spaceBefore=6)); i += 1; continue
        if s.startswith("&gt;") or s.startswith(">"):
            flush_para()
            q = []
            while i < n and lines[i].strip().startswith(">"):
                q.append(inline_md(lines[i].strip()[1:].strip())); i += 1
            story.append(P("<br/>".join(q), s_quote)); continue
        if re.match(r"^\|.*\|$", s):
            flush_para()
            tbl = []
            while i < n and re.match(r"^\|.*\|$", lines[i].strip()):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if all(re.match(r"^:?-{2,}:?$", c.replace(" ", "")) for c in cells if c):
                    i += 1; continue
                tbl.append(cells); i += 1
            if tbl:
                hdr = [Paragraph(inline_md(c), s_thead) for c in tbl[0]]
                body = [[Paragraph(inline_md(c), s_cell) for c in r] for r in tbl[1:]]
                w = (W - 36*mm) / len(tbl[0])
                story.append(styled_table([hdr] + body, [w]*len(tbl[0]), header_rows=1))
            continue
        if re.match(r"^[-*]\s", s):
            flush_para()
            items = []
            while i < n and re.match(r"^[-*]\s", lines[i].strip()):
                items.append(lines[i].strip()[2:].strip()); i += 1
            for it in items:
                story.append(Paragraph("\u2022\u2003" + inline_md(it), s_bull))
            continue
        if re.match(r"^\d+[.)]\s", s):
            flush_para()
            items = []
            while i < n and re.match(r"^\d+[.)]\s", lines[i].strip()):
                items.append(re.sub(r"^\d+[.)]\s", "", lines[i].strip())); i += 1
            for k, it in enumerate(items, 1):
                story.append(Paragraph(f"<b>{k}.</b>\u2003" + inline_md(it), s_bull))
            continue
        buf.append(s); i += 1
    flush_para()

story = []
W, H = A4

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7); canvas.setFillColor(DGRAY)
    canvas.drawString(18*mm, 12*mm, "Valuation Methodology Addenda \u2014 Compounder-Quality Override & International Framework \u2014 October 2026")
    canvas.drawRightString(W - 18*mm, 12*mm, f"Page {doc.page}")
    canvas.setStrokeColor(MGRAY); canvas.setLineWidth(0.5)
    canvas.line(18*mm, 14.5*mm, W - 18*mm, 14.5*mm)
    canvas.restoreState()

# ============ 1. TITLE PAGE ============
story.append(Spacer(1, 30*mm))
story.append(P("VALUATION METHODOLOGY ADDENDA", ParagraphStyle("x", parent=s_sub, fontName="Helvetica-Bold", fontSize=13, textColor=ORANGE, spaceAfter=2)))
story.append(P("Compounder-Quality Override<br/>&amp; International Framework", s_title))
story.append(Spacer(1, 4*mm))
story.append(P("Addenda to the v2 Valuation Framework \u00b7 October 4, 2026", s_sub))
story.append(Spacer(1, 10*mm))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=8, spaceBefore=4))
story.append(P("<b>This document is research analysis, not investment advice.</b> It describes two extensions to the "
               "v2 valuation framework used in the equity-research notes: (A) a compounder-quality override that rewards "
               "demonstrated decade-plus economics with a lower discount rate and a longer explicit forecast period, and "
               "(B) an international framework that prices country risk explicitly in the discount rate and forces "
               "structural risks (VIE structures, confiscation, trapped cash) into cash flows instead of footnotes. "
               "Valuations shown are ~10-year scenario-weighted expected values under the stated assumptions; upside "
               "figures are measured against October 2, 2026 closing prices.", s_body))
story.append(Spacer(1, 6*mm))
toc = [
    [Paragraph("<b>Section</b>", s_theadL), Paragraph("<b>Contents</b>", s_thead)],
    [cell("1"), cell("Title page")],
    [cell("2"), cell("Addendum A — Compounder-Quality Override (full text)")],
    [cell("3"), cell("Addendum B — International Valuation Framework (full text)")],
    [cell("4"), cell("Qualification screen — 54-name results (PASS / BORDERLINE / FAIL)")],
    [cell("5"), cell("Re-run results — override rebuilds; international re-valuations; scenario inputs; judgment calls")],
    [cell("6"), cell("Summary: what moved and why; limitations")],
]
story.append(styled_table(toc, [20*mm, 154*mm]))
story.append(Spacer(1, 8*mm))
story.append(P("Valuation verdict bands used throughout: BUY \u2265 +30% upside, HOLD \u221215% to +30%, "
               "REDUCE \u221240% to \u221215%, SELL < \u221240%. Scenario weights 25% bear / 50% base / 25% bull.", s_small))
story.append(PageBreak())

# ============ 2. ADDENDUM A ============
story.append(P("2 &nbsp; Addendum A \u2014 Compounder-Quality Override", s_h1))
story.append(P("*Addendum to the v2 valuation framework (2026-10-04).*", s_small))
with open(f"{BASE}/addendum-a-compounder-override.md", encoding="utf-8") as f:
    md_to_flowables(f.read(), story, title_skip=1)
story.append(PageBreak())

# ============ 3. ADDENDUM B ============
story.append(P("3 &nbsp; Addendum B \u2014 International Valuation Framework", s_h1))
story.append(P("*Addendum to the v2 valuation framework (2026-10-04).*", s_small))
with open(f"{BASE}/addendum-b-international-framework.md", encoding="utf-8") as f:
    md_to_flowables(f.read(), story, title_skip=1)
story.append(PageBreak())

# ============ 4. QUALIFICATION SCREEN ============
story.append(P("4 &nbsp; Qualification Screen \u2014 54-Name Results", s_h1))
story.append(P("All three Addendum A tests applied to reported history only (SEC EDGAR XBRL companyfacts, FY2013\u2013FY2026; "
               "R-file consolidated statements where it mattered). ROIC = NOPAT \u00f7 invested capital; gross margins from "
               "filings where tagged; FCF conversion = cumulative free cash flow \u00f7 cumulative net income over the "
               "qualification period. Screens run in three batches (18 + 18 + 18); method differences are disclosed in the "
               "batch notes. Result: <b>4 strict PASS, 4 borderline</b> (shown separately for adjudication), 46 FAIL. "
               "This is research analysis, not investment advice.", s_body))

def chip(result):
    if result.startswith("PASS"):
        return f'<b><font color="#0E7C3E">{result}</font></b>'
    if result.startswith("BORDERLINE"):
        return f'<b><font color="#D96C06">{result}</font></b>'
    return f'<font color="#5A6472">{result}</font>'

# (ticker, ROIC streak, GM trend, FCF conv, result, key note)
Q = [
 # --- batch 1 (compounder-screen/COMPOUNDER_SCREEN_REPORT.md) ---
 ("NKE", ">15% all 14 yrs (2013\u20132026); min 15.8% (FY18 tax-reform yr); avg 25.4%", "44.6%\u219242.9%, roughly stable", "97% avg (97% med), 14y", "PASS", "Full 14-yr streak; strongest band evidence"),
 ("ZTS", "10 consec. yrs >15% (2016\u20132025, 16.3%\u219221.4%); 2013\u201315 below", "Expanding 69.6%\u219271.8%", "91% avg (89% med), 13y", "PASS", "Trailing-10 run satisfies rule as written; NOPAT via NI+interest fallback (no OI tag)"),
 ("ADBE", "9 consec. yrs >15% (2017\u20132025, 18.7%\u219247.1%); 2013\u201316 below", "Expanding 85.5%\u219289.3%", "183% avg (145% med), 13y", "BORDERLINE", "1 yr short of the 10-yr letter; miss yrs = deliberate Creative-Cloud transition revenue deferral"),
 ("INTU", "9 consec. yrs >15% (2013\u20132021); 2022\u201324 below 9.0/11.1/12.9%; 2025\u201326 back above (15.6/20.1)", "n/a (Intuit discloses no gross profit)", "173% avg (156% med), 14y", "BORDERLINE", "Strict FAIL; failure is $12B Mailchimp-goodwill accounting, not operating decay; GM leg unverifiable"),
 ("APH", "Only 4 trailing yrs >15% (2022\u201325); 6 yrs below (13.0\u201314.9%)", "Expanding 32.5%\u219236.9%", "101% avg (105% med), 11y", "FAIL", "Not close on test 1"),
 ("NFLX", "9 of 13 yrs below 15% (min 3.8%, avg 11.9%)", "Expanding 28.7%\u219248.5%", "\u2212144% avg (content capex cycle)", "FAIL", "Test 1 fail; negative conversion"),
 ("AVGO", "7 of 9 yrs below (min 4.7%, avg 12.6%)", "Expanding 48.2%\u219267.8%", "198%", "FAIL", "Test 1 fail; acquisition-heavy capital base"),
 ("FISV", "Max 10.3%, avg 8.7%", "~87% flat", "177%", "FAIL", "Never clears 15%"),
 ("TMUS", "Max 7.4%, avg 4.8%", "n/a", "\u221283% avg", "FAIL", "Never clears 15%; negative conversion"),
 ("AMZN", "Max 14.9%, avg 9.5%", "Expanding 35.1%\u219250.3%", "434%", "FAIL", "Peak 14.9% \u2014 just misses the line; never sustains"),
 ("VST", "Max 11.1%, avg 3.5%, negative yrs", "n/a", "206%", "FAIL", "Test 1 fail"),
 ("VITL", "Max ~24%, avg 12.3%; 4 yrs <7%", "32.6%\u219237.6%", "\u2212193% avg", "FAIL", "Test 1 fail; negative conversion"),
 ("PATH", "Deeply negative to 2025", "82.3%\u219283.2%", "n/a (1 pos-NI yr)", "FAIL", "No positive-ROIC history"),
 ("DKNG", "Negative to 2025 (\u22120.7%)", "33.8%\u219241.3%", "n/a", "FAIL", "No positive-ROIC history"),
 ("CELH", "Negative avg (\u221219.7%)", "41.4%\u219250.4%", "\u2212329% avg", "FAIL", "Test 1 + conversion fail"),
 ("SE", "Negative/garbage (near-zero IC yrs)", "32.7%\u219252.2%", "n/a", "FAIL", "Test 1 fail; loss-history distorts IC"),
 ("AXP", "2.4\u20135.2% (avg 4.1%)", "n/a", "196%", "FAIL", "<i>As specified</i> \u2014 ROIC is the wrong metric for a card lender (IC includes the loan book); ROE ~28\u201333% is the right metric"),
 ("GRAB", "Insufficient data", "n/a", "n/a", "FAIL", "Listed Dec 2021 (<7-yr minimum); IFRS filer, no US-GAAP companyfacts series; loss-making until recently"),
 # --- batch 2 (valuation-addenda/screen-18/REPORT.md) ---
 ("MCD", "12 of 15 yrs \u226515% (avg 17.8%); longest strict run 4 yrs; misses: 2015 at 14.96% (4bp), 2020 COVID 12.5%, 2022 Russia 14.8%", "Stable 54.2%\u219257.4% (2021\u201325)", "85.9% avg / 87.2% med, 10y", "BORDERLINE", "Substance pass: 12/15 yrs \u226515%, every 10-yr window >16% avg; strict reading FAILS on a 4bp print \u2014 see judgment call"),
 ("SOFI", "Bank; ROIC n/a; ROE never \u226515%", "n/a (bank)", "n/a", "FAIL", "ROIC structurally inapplicable to a bank"),
 ("FIS", "ROIC 0.5\u20133.5%, 14/14 yrs <15%", "Up 33\u219237%", "270% avg", "FAIL", "Test 1 fail"),
 ("NVDA", "Longest run 3 yrs (2019\u201321); breaks 2011\u201318, 2022 (14.1%), 2023 (13.9%)", "Up 35%\u219273%", "~85% (recent yrs)", "FAIL", "Test 1 fail \u2014 elite margins do not equal decade ROIC"),
 ("APP", "Listed 2021, 5 yrs history (<7 minimum)", "n/a", "neg", "FAIL", "Insufficient history"),
 ("BKNG", "Longest run 4 yrs (2022\u201325: 23/33/53/57%); breaks 2016 (13.9%), 2017 (14.0%), 2020 (\u22122.2%), 2021 (11.1%)", "Expanding 50.7%\u219298.1% (2010\u201319; undisclosed after)", "PASS (FCF-rich)", "FAIL", "Test 1 fail \u2014 magnificent recent compounder, not a decade record (R-file verified)"),
 ("SPGI", "Longest run 6 yrs (2017\u201322); breaks 2014 (13.8%), 2016 (\u22122.0%), 2023 (9.3%, IHS Markit)", "Insufficient \u2014 no GP tag", "~122% med", "FAIL", "Test 1 fail; IHS Markit deal re-based the capital base"),
 ("WCN", "ROIC ~4% avg, 12/12 yrs <15%", "Insufficient \u2014 no GP tag", "123% avg", "FAIL", "Test 1 fail"),
 ("TIGR", "Insufficient usable data; loss-making 2019\u201322", "n/a", "n/a", "FAIL", "Foreign private issuer; tags unusable"),
 ("PYPL", "ROIC 8\u201311%, 6/6 yrs <15%", "Insufficient \u2014 no GP tag", "175% avg", "FAIL", "Test 1 fail"),
 ("LITE", "ROIC ~5% avg", "Down 29%\u219219%", "27% avg", "FAIL", "Tests 1\u20133 all fail"),
 ("TTD", "ROIC ~10%, only 2 valid yrs; listed 2016", "Insufficient \u2014 no GP tag", "253% avg", "FAIL", "Test 1 fail"),
 ("GRBK", "ROIC ~neg; homebuilder, interest capitalized", "Up 29%\u219231%", "\u221289% avg (land reinvestment eats earnings)", "FAIL", "Tests 1, 3 fail"),
 ("ARM", "Listed Sep 2023 (<7 yrs)", "95% (IP)", "177%", "FAIL", "Insufficient history"),
 ("RTX", "ROIC ~7% avg, 9/9 yrs <15%", "Up 5%\u21927%", "116%", "FAIL", "Test 1 fail"),
 ("DDOG", "ROIC negative (4 valid yrs)", "Up 77%\u219281%", "Deeply neg (SBC-era NI)", "FAIL", "Tests 1, 3 fail"),
 ("RGTI", "ROIC \u2212124% avg (pre-revenue)", "n/a", "n/a", "FAIL", "Test 1 fail"),
 ("MELI", "ROIC data insufficient for 10-yr run", "<b>Down 64.8%\u219250.2%</b>", "Volatile (NI near zero early)", "FAIL", "Tests 1, 2 fail"),
 # --- batch 3 (compounder-screen/COMPOUNDER_OVERRIDE_REPORT.md) ---
 ("BULL", "2 yrs data only", "n/a (not reported)", "n/a", "FAIL", "IPO Apr 2025; cannot meet 7-yr minimum"),
 ("COIN", "5 yrs data only (229/\u221243/\u22122/61/17%)", "n/a (not reported)", "172%", "FAIL", "IPO 2021; volatile by construction"),
 ("WHR", "2 yrs >15% (2013, 2021) of 16", "14.8\u219215.4%, stable-ish", "117%", "FAIL", "Test 1 fail"),
 ("META", "13 consec. yrs >15% (2013\u20132025; 2012: 7.3%)", "73.2\u219282.0% (+8.8pp); mechanical 3-yr contraction window 2018\u201320 (86.6\u219280.6)", "112%", "PASS*", "Pass with asterisk: trailing GM far above start; dip = Reality Labs scale-up + infra mix, not ad-pricing erosion; strict-mechanical reading fails criterion 2 \u2014 see judgment call"),
 ("SHOP", "0 yrs >15% (max 12.3%)", "55.2\u219248.1% declining", "155%", "FAIL", "Test 1 fail; GM declining"),
 ("AMD", "5 consec. yrs (2018\u20132022)", "Expanding 45.6%\u219249.5%", "125%", "FAIL", "Test 1 fail \u2014 Xilinx (2022) stepped up invested capital, crushing post-deal ROIC"),
 ("WYNN", "4 consec. yrs (2011\u20132014)", "n/a (not reported)", "103%", "FAIL", "Test 1 fail; cyclical; COVID yrs negative"),
 ("CMCSA", "0 yrs >15% (max 9.2%)", "n/a (not reported)", "122%", "FAIL", "Test 1 fail"),
 ("HD", "16 consec. yrs >15% (2010\u20132025; 2009: 12.9%)", "33.9\u219233.3%, flat", "106%", "PASS", "Longest streak in the screen; flat GM is economically flat (0.5pp on 34%)"),
 ("RH", "4 consec. yrs (2018\u20132021)", "Expanding 36.6%\u219244.1%", "67%", "FAIL", "Test 1 + conversion fail (conversion <80%)"),
 ("BABA", "1 yr >15% (2017) of 8", "57.2\u219239.8% then stable ~40", "170%", "FAIL", "Test 1 fail (country risk handled separately per Addendum B)"),
 ("FUBO", "0 yrs (all negative)", "n/a", "46%", "FAIL", "Tests 1, 3 fail"),
 ("JD", "0 yrs >15% (max 11.4%, 12-yr ROIC series)", "14.0\u219214.6%", "n/a (NI tags gappy)", "FAIL", "Test 1 fail \u2014 retail economics; never clears 15% (12-yr series, airtight)"),
 ("NRG", "1 yr >15% (2021) of 17", "40.5\u219219.4% declining", "156%", "FAIL", "Test 1 fail; merchant-power cyclicality"),
 ("VICI", "0 yrs >15% (max 10.9%, 9-yr EBIT proxy)", "97.8\u219298.6%", "110%", "FAIL", "Test 1 fail \u2014 structural: 15% ROIC unattainable for a triple-net REIT"),
 ("CDNS", "15 consec. yrs >15% (2011\u20132025; 2010 n/a)", "~90% stable (two-source: EDGAR 2010\u201312 + yfinance 2022\u201325)", "127%", "PASS", "Mid-period GM unobserved in filings data; both observed ends consistent with ~90%"),
 ("EXE", "Cyclical (\u221256%\u2026+58%)", "n/a (E&P)", "38%", "FAIL", "Tests 1, 3 fail; ex-Chesapeake CIK; Oct-2024 Southwestern merger caveat"),
 ("IBM", "\u22643 consec. yrs (EBIT proxy; Kyndryl spin 2021 breaks series)", "Expanding 45.7%\u219258.2%", "145%", "FAIL", "Test 1 fail"),
]

assert len(Q) == 54, f"expected 54 rows, got {len(Q)}"
hd = [Paragraph("<b>Ticker</b>", s_thead), Paragraph("<b>ROIC streak (yrs)</b>", s_thead),
      Paragraph("<b>Gross margin trend</b>", s_thead), Paragraph("<b>FCF conv.</b>", s_thead),
      Paragraph("<b>Result</b>", s_thead), Paragraph("<b>Key note</b>", s_thead)]
rows = []
for t, roic, gm, fcf, res, note in Q:
    rows.append([
        Paragraph(f"<b>{t}</b>", s_tinycC),
        Paragraph(inline_md(roic), s_tinyc),
        Paragraph(inline_md(gm), s_tinyc),
        Paragraph(inline_md(fcf), s_tinycC),
        Paragraph(chip(res), s_tinycC),
        Paragraph(inline_md(note), s_tinyc),
    ])
cw = [13*mm, 46*mm, 30*mm, 25*mm, 24*mm, 36*mm]
t54 = Table([hd] + rows, colWidths=cw, repeatRows=1)
t54.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), NAVY), ("TEXTCOLOR", (0, 0), (-1, 0), white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"), ("FONTSIZE", (0, 0), (-1, -1), 7),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("GRID", (0, 0), (-1, -1), 0.35, MGRAY),
    ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, LGRAY]),
]))
story.append(t54)
story.append(Spacer(1, 4*mm))
story.append(P("*Batch notes:* batch 1 (NKE/ZTS/ADBE/INTU + 14 fails) used FY2013\u201326 EDGAR series with duration-filtered "
               "annual facts, avg-span FCF conversion; batch 2 (MCD + 17) cross-validated MCD/BKNG against 10-K R-file consolidated "
               "statements (a naive pull misattributes comparative columns \u2014 corrected); batch 3 (META/HD/CDNS + 15) used "
               "averaged beginning/end invested capital with CY-frame year keys and cumulative FCF/NI per rule A1.3. "
               "ZTS and MCD NOPAT use NI+after-tax-interest fallback where OperatingIncomeLoss is untagged. "
               "NKE = Nike, ZTS = Zoetis, HD = Home Depot, CDNS = Cadence Design Systems, META = Meta Platforms, MCD = McDonald\u2019s, "
               "ADBE = Adobe, INTU = Intuit.", s_small))
story.append(P("Net: 4 strict qualifiers (NKE, ZTS, HD, CDNS) rebuilt below; 4 borderlines (ADBE, INTU, META*, MCD) shown as "
               "flagged sensitivities for adjudication; 46 fail.", s_body))
story.append(PageBreak())

# ============ 5. RE-RUN RESULTS ============
story.append(P("5 &nbsp; Re-run Results", s_h1))
story.append(P("All upsides are vs. October 2, 2026 closes (yfinance-verified). Verdict bands: BUY \u2265 +30%, "
               "HOLD \u221215%\u2026+30%, REDUCE \u221240%\u2026\u221215%, SELL < \u221240%. This is research analysis, not investment advice.", s_body))

story.append(P("5.1 &nbsp; Compounder-override rebuilds", s_h2))
story.append(P("Base discount 8.25% (batch 1) or 8.0\u20138.25% (batch 2/3, strongest-band qualifiers at 8.0%); "
               "bear = base + 250bp; bull = base \u2212 150bp floored at 8%; horizon 15y base/bull, 10y bear; "
               "terminal growth cap 3.0% on demonstrated sustained margins; weights 25/50/25. TV/EV \u2264 65% everywhere "
               "(no 70%-rule haircut). Bear cases all meet \u22652 hurt criteria and sit below price.", s_body))

# Ticker | Old FV | New FV | dFV | Price | Upside | Verdict | Key
O = [
 ("NKE", "$31", "$63.74", "+105%", "$33.87", "+88%", "HOLD \u2192 <b>BUY</b>", "8.25%; bear $23.83 \u2713"),
 ("ZTS", "$64", "$95.40", "+49%", "$69.69", "+37%", "HOLD \u2192 <b>BUY</b>", "8.25%; bear $29.55 \u2713"),
 ("HD", "$208", "$267.64", "+29%", "$282.85", "\u22125%", "REDUCE \u2192 <b>HOLD</b>", "8.0% (strongest band); bear $58.75 \u2713"),
 ("CDNS", "$240", "$308.05", "+28%", "$351.35", "\u221212%", "REDUCE \u2192 <b>HOLD</b>", "8.0% (strongest band); bear $65.10 \u2713"),
 ("META", "$675", "$879.80", "+30%", "$728.08", "+21%", "HOLD \u2192 <b>HOLD</b>", "8.25% mid-band; bull floor binds; bear $165.84 \u2713"),
 ("ADBE*", "$465", "$616.34", "+33%", "$237.69", "+159%", "BUY \u2192 <b>BUY</b>", "Borderline sensitivity \u2014 shown, not adopted"),
 ("INTU*", "$535", "$719.75", "+35%", "$281.08", "+156%", "BUY \u2192 <b>BUY</b>", "Borderline sensitivity \u2014 shown, not adopted"),
 ("MCD*", "$122", "$129.32", "+6%", "$231.89", "\u221244%", "<b>REDUCE</b> (unchanged)", "Borderline sensitivity \u2014 shown, not adopted; even $213 bull sits below price"),
]
ohd = [Paragraph("<b>Ticker</b>", s_thead), Paragraph("<b>Old v2 FV</b>", s_thead),
       Paragraph("<b>New FV</b>", s_thead), Paragraph("<b>\u0394 FV</b>", s_thead),
       Paragraph("<b>Price (Oct 2)</b>", s_thead), Paragraph("<b>Upside</b>", s_thead),
       Paragraph("<b>Verdict</b>", s_thead), Paragraph("<b>Key notes</b>", s_thead)]
orows = []
for t, old, new, d, pr, up, v, k in O:
    orows.append([
        Paragraph(f"<b>{t}</b>", s_tinycC),
        Paragraph(old, s_tinycR), Paragraph(f"<b>{new}</b>", s_tinycR), Paragraph(d, s_tinycR),
        Paragraph(pr, s_tinycR), Paragraph(f"<b>{up}</b>", s_tinycR),
        Paragraph(inline_md(v), s_tinycC), Paragraph(inline_md(k), s_tinyc),
    ])
story.append(styled_table([ohd] + orows, [13*mm, 18*mm, 19*mm, 15*mm, 22*mm, 16*mm, 33*mm, 38*mm], fontsize=7))
story.append(P("Table 1 \u2014 Override rebuilds. *Borderline sensitivities shown for adjudication, not adopted.*", s_caption))

story.append(P("Scenario inputs (visible, per name)", s_h3))
scen = [
 ("<b>NKE</b>", "Rev CAGR bear/base/bull 0.5%/2.7%/4.5%; terminal FCF margin 7%/10%/12% (demonstrated 9.5\u201313.4% through-cycle 2019\u201324 ex-COVID; current 4.7% depressed \u2014 the turnaround bet, same as v2); term g 1.5%/2.5%/3.0%; disc 10.75%/8.25%/8.0%. Scenario FVs $23.83 / $63.74 / $103.63. Net debt $2.76B, 1.202B shares."),
 ("<b>ZTS</b>", "Rev CAGR 1.5%/4.5%/6.5%; terminal FCF margin 18%/23%/25% (demonstrated 16.4%\u219224.8% 2022\u201325, v2 used 24%); term g 1.5%/2.5%/3.0%. Scenario FVs $29.55 / $98.53 / $154.98. Net debt $7.58B, 413.2M shares."),
 ("<b>HD</b>", "Rev CAGR (y1\u201310) \u22120.5%/+4.2%/+5.8% fading to terminal g over yrs 11\u201315; terminal FCF margin 6.5%/9.5%/10.5% (demonstrated 8.6\u201310.2% since 2015; 2025: 7.7%, SRS integration); term g 1.5%/3.0%/3.0% (cap); disc 10.50%/8.00%/8.00% (bull floor binds). Scenario FVs $58.75 / $305.02 / $401.77. Net debt \u2212$61.0B, 0.998B shares, rev0 $170.5B."),
 ("<b>CDNS</b>", "Rev CAGR (y1\u201310) +2.0%/+12.0%/+15.0%; terminal FCF margin 24%/32%/35% (sustained ~30% 2020\u201325, 24\u201335% range); term g 1.5%/3.0%/3.0% (cap); disc 10.50%/8.00%/8.00% (bull floor binds). Scenario FVs $65.10 / $339.37 / $488.36. Net debt \u2212$1.12B, 275.4M shares, rev0 $6.30B (FY26E)."),
 ("<b>META</b>", "Rev CAGR (y1\u201310) +1.5%/+11.8%/+14.0%; terminal FCF margin 20%/30%/33% (27\u201343% in 8 of last 11 yrs; 2022 16.5% and 2025 22.9% were capex-cycle troughs); term g 1.5%/3.0%/3.0% (cap); disc 10.75%/8.25%/8.00% (bull floor binds). Scenario FVs $165.84 / $976.80 / $1,399.76. Net cash +$47.0B (cash $41.9B + securities $33.9B \u2212 LTD $28.8B, FY25 10-K), 2.54B diluted shares, rev0 $201.0B."),
 ("<b>ADBE* (borderline, not adopted)</b>", "Rev CAGR 0.5%/6.0%/8.5%; terminal FCF margin 30%/38%/40% (demonstrated 35.8\u201342.0% 2022\u201325; v2 used ~39%); term g 1.0%/2.5%/3.0%. Scenario FVs $204.46 / $639.42 / $982.06. Net debt $1.15B, 397.5M shares."),
 ("<b>INTU* (borderline, not adopted)</b>", "Rev CAGR 1.0%/6.8%/9.5%; terminal FCF margin 27%/33%/35% (demonstrated 28.5\u201340.2% FY23\u201326; v2 used 27/33/35%); term g 1.5%/2.5%/3.0%. Scenario FVs $232.74 / $736.79 / $1,172.68. Net debt $1.22B, 267.2M shares."),
 ("<b>MCD* (borderline, not adopted)</b>", "f0: FY2025 revenue $26,885M, FCF $7,186M (26.7% margin, 10-K R-files). Rev CAGR: base 4.5% yrs 1\u201310 \u2192 3.5% yrs 11\u201315; bull 6.0% \u2192 4.0%; bear \u22124% yr 1 then 2% (~1.3% 10-yr CAGR). Terminal FCF margin 20%/27%/28.5% (demonstrated 2021\u201325 avg 27.0%). Term g 1.5%/2.75%/3.0% (cap). Disc 10.75%/8.25%/8.00%. Scenario FVs $8.92 / $147.48 / $213.41. Net debt $54,056M, 708M shares. Bear rebuilt harsher ($41\u2192$9: genuine 700bp compression at 10.75%), so weighted FV only moves $122\u2192$129 despite base $127\u2192$147 and bull $193\u2192$213. Even the $213 bull sits 8% below the $232 price."),
]
for t, d in scen:
    story.append(Paragraph(f"\u2022\u2003{t} \u2014 " + inline_md(d), s_bull))

story.append(P("Judgment calls \u2014 borderline handling", s_h3))
story.append(P("<b>META:</b> qualifies on the level test (trailing GM 82.0% vs starting 73.2%, +8.8pp; 112% conversion; 13-yr ROIC streak), but a mechanical 3-year contraction window (2018\u20132020: 86.6\u219280.6) fails criterion 2 on the strict reading \u2014 the dip is Reality Labs scale-up and infra mix, not ad-pricing-power erosion. Rebuilt as a flagged sensitivity; if the strict reading is applied, the override is revoked and META falls back to its v2 $675 HOLD. Verdict is HOLD either way (+20.8% vs +30% BUY bar), so the adjudication moves the target ($880 vs $675), not the call.", s_body))
story.append(P("<b>MCD:</b> substance-pass borderline (12 of 15 years \u226515%, 15-yr avg 17.8%, every 10-yr window >16%; misses are a 4bp print, COVID, and a Russia-exit charge) that a strict 10-consecutive-years reading fails. Shown as a sensitivity; verdict REDUCE either way, since even the $213 override bull sits below the $232 price.", s_body))
story.append(P("<b>ADBE / INTU:</b> 9-year streaks, 1 year short of the letter; ADBE's miss years are the deliberate Creative-Cloud transition revenue deferral, INTU's are Mailchimp-goodwill accounting. Sensitivities shown (+33\u201335% FV lift vs v2), not adopted pending adjudication.", s_body))

story.append(PageBreak())
story.append(P("5.2 &nbsp; Internationals under Addendum B", s_h2))
story.append(P("Country-risk premiums stacked on every scenario discount rate (China +250bp, SE Asia +150bp, LatAm +200bp); "
               "structural risks modeled in cash flows and bear cases per rule B3 (VIE haircuts, confiscation mechanics, "
               "commission-cap modeling, currency drag); no-double-counting enforced per name. v2 rules kept throughout "
               "(tiered discounts, terminal \u22642.5%, bear must hurt and sit below price). Two of the eight were new v2 "
               "builds (PDD $127.91, TME $16.54 pre-CRP) with audit hits fixed.", s_body))
I = [
 ("BABA", "$179.68", "$132.39", "+25%", "BUY \u2192 <b>HOLD</b>", "+250bp", "20% VIE haircut on RMB471B investment portfolio (all scenarios); regional cross-check 14.4\u00d7 vs China big-tech ~11.3\u00d7 \u2014 contradicts DCF"),
 ("JD", "$65.39", "$55.42", "+115%", "<b>BUY</b> (unch.)", "+250bp", "New 20% VIE haircut on ~RMB110B listed stakes (RMB235.5B net claim); bear unchanged \u2014 balance-sheet attack already modeled, no layered confiscation"),
 ("PDD", "$127.91*", "$107.93", "+43%", "<b>BUY</b> (new)", "+250bp", "*New v2 build (audit fixes: cash counted once, Temu as active cash drain); 25% bear confiscation haircut"),
 ("TME", "$16.54*", "$13.03", "+68%", "<b>BUY</b> (new)", "+250bp", "*New v2 build (real bear $5.36, widened tiers, 2.5% terminal cap, no judgmental uplift); 25% bear confiscation haircut"),
 ("SE", "$181.17", "$149.31", "+57%", "<b>BUY</b> (unch.)", "+150bp SEA", "Bear margin path prices Indonesia take-rate pressure (populist precedent, not a footnote)"),
 ("GRAB", "$3.91", "$3.38", "+10%", "<b>HOLD</b> (unch.)", "+150bp SEA", "Indonesia 20%\u21928% commission cap in bear cash flows (kept); net cash $4.5B = $1.13/sh (33% of FV) floors left tail; most fragile HOLD"),
 ("TIGR", "$16.11", "$12.86", "+209%", "<b>BUY</b> (unch.)", "+250bp", "Bear keeps CSRC mechanics ($75M 2027 disgorgement + mainland wind-down); 40% gross-cash haircut; belt-and-suspenders disclosed"),
 ("MELI", "$1,485.23", "$1,118.98", "\u221234%", "HOLD \u2192 <b>REDUCE</b>", "+200bp LatAm", "Bear = LatAm crisis path (ARS/BRL via margin path, credit-book stress); $7.462B net debt"),
]
ihd = [Paragraph("<b>Ticker</b>", s_thead), Paragraph("<b>Old FV</b>", s_thead),
       Paragraph("<b>New FV</b>", s_thead), Paragraph("<b>Upside</b>", s_thead),
       Paragraph("<b>Verdict</b>", s_thead), Paragraph("<b>CRP</b>", s_thead),
       Paragraph("<b>Key structural treatment</b>", s_thead)]
irows = []
for t, old, new, up, v, crp, k in I:
    irows.append([
        Paragraph(f"<b>{t}</b>", s_tinycC),
        Paragraph(old, s_tinycR), Paragraph(f"<b>{new}</b>", s_tinycR),
        Paragraph(f"<b>{up}</b>", s_tinycR),
        Paragraph(inline_md(v), s_tinycC), Paragraph(crp, s_tinycC),
        Paragraph(inline_md(k), s_tinyc),
    ])
story.append(styled_table([ihd] + irows, [13*mm, 20*mm, 20*mm, 16*mm, 33*mm, 22*mm, 50*mm], fontsize=7))
story.append(P("Table 2 \u2014 Addendum B re-valuations. *PDD/TME \u201cold\u201d FVs are new hardened-v2 builds; the Addendum B move is pre-CRP \u2192 post-CRP.*", s_caption))

story.append(P("Scenario inputs (visible, per name)", s_h3))
iscen = [
 ("<b>BABA</b>", "Rates 12.5/10/8.5% \u2192 15/12.5/11%. Scenario FVs: bear $64.37\u2192$55.23 / base $174.03\u2192$130.62 / bull $306.27\u2192$213.07. Structural: 20% haircut on investment portfolio embedded (RMB598B net claim = 221B net cash + 471B investments @80%)."),
 ("<b>JD</b>", "Rates 14.5/12/10.5% \u2192 17/14.5/13%. Scenario FVs: bear $19.95\u2192$21.11 / base $70.82\u2192$60.85 / bull $99.95\u2192$78.87. Net claim RMB235.5B ($26.21/ADS, 47% of new FV)."),
 ("<b>PDD</b>", "Rates 14.5/12/10.5% \u2192 17/14.5/13%. Scenario FVs: bear $53.83 / base $103.58 / bull $170.72. Bear \u221229% vs price: 0% revenue CAGR + 700bp margin compression + 25% confiscation haircut. Temu modeled as active drain (base blended FCF margins 13%\u219215%; domestic ~35% net of Temu losses). Bull prices the binary 6\u00d7\u219211\u201312\u00d7 VIE-discount-close re-rating."),
 ("<b>TME</b>", "Rates 14.5/12/10.5% \u2192 17/14.5/13%. Scenario FVs: bear $4.84 / base $12.70 / bull $21.87. Bear carries 25% confiscation haircut; without it the operating bear is only \u22128% \u2014 the VIE tail does the work (disclosed). Net cash $3.85B (RMB27.7B) unhaircut in base/bull."),
 ("<b>SE</b>", "Rates 14.5/12/10.5% \u2192 16/13.5/12%. Scenario FVs: bear $72.43\u2192$64.40 / base $165.94\u2192$138.72 / bull $320.36\u2192$255.41. Bear margin path prices Indonesia take-rate/commission pressure explicitly."),
 ("<b>GRAB</b>", "Rates 14.5/12/10.5% \u2192 16/13.5/12%. Scenario FVs: bear $1.40\u2192$1.36 / base $3.85\u2192$3.37 / bull $6.53\u2192$5.43. Indonesia commission cap modeled in bear cash flows."),
 ("<b>TIGR</b>", "Rates 14.5/12/10.5% \u2192 17/14.5/13%. Scenario FVs: bear $3.70\u2192$3.41 / base $16.05\u2192$12.65 / bull $31.41\u2192$22.72. 40% gross-cash haircut ($1.59/ADS net cash, 12% of FV)."),
 ("<b>MELI</b>", "Rates 14.5/12/10.5% \u2192 16.5/14/12.5%. Scenario FVs: bear $161.92\u2192$116.16 / base $1,442.67\u2192$1,106.57 / bull $2,893.95\u2192$2,146.62. The price embeds ~18% 10-yr growth with no margin of safety \u2014 at 14% base discount that growth is worth $1,107, not $1,697."),
]
for t, d in iscen:
    story.append(Paragraph(f"\u2022\u2003{t} \u2014 " + inline_md(d), s_bull))

story.append(P("Judgment calls \u2014 disclosed quirks", s_h3))
story.append(P("<b>JD bear-above-old-bear quirk:</b> the new bear ($21.11) prints slightly <i>above</i> the old bear ($19.95). "
               "The bear's cash flows are negative early and back-loaded, so the higher discount rate discounts the near-term "
               "burn harder than the later recovery. Economically coherent; immaterial to the call.", s_body))
story.append(P("<b>TIGR no-double-count disclosure:</b> the +250bp CRP sits on top of bear-case CSRC mechanics "
               "($75M 2027 overseas disgorgement + mainland buy-freeze \u2192 wind-down). This is deliberate: the bear prices the "
               "<i>conditional realization</i> of a named event; the CRP prices the <i>unconditional required return</i> for "
               "bearing China-regulatory risk in the base and bull cases (the open \u201csecond CSRC action\u201d question). "
               "Belt-and-suspenders by construction \u2014 disclosed as conservative, not as an error.", s_body))
story.append(P("<b>JD confiscation haircut withheld from bear:</b> the bear keeps the published cash-incineration mechanics "
               "(subsidy war, \u22120.8% FCF margin) with no added confiscation haircut \u2014 the balance-sheet attack is "
               "already modeled; layering a haircut on top would double-count it. TME's bear does carry the 25% confiscation "
               "haircut, because there the operating bear alone is only \u22128%. The asymmetry is intentional.", s_body))
story.append(P("<b>PDD audit reconciliation:</b> post-CRP $107.93 lands inside the audit's suggested $105\u2013115 band "
               "coincidentally \u2014 the base keeps TTM-anchored operating margins while the audit's band implied deeper "
               "Temu drag. The key falsifier is Temu losses failing to narrow by Q1'27.", s_body))

# ============ 6. SUMMARY ============
story.append(P("6 &nbsp; Summary", s_h1))
story.append(P("What moved and why", s_h2))
story.append(P("The compounder override (Addendum A) is, mechanically, a ~28\u2013105% fair-value lift for the four names "
               "that earned it: the base discount falls 100\u2013175bp (9\u201310% \u2192 8.0\u20138.25%), the explicit "
               "horizon stretches from 10 to 15 years, and the terminal cap moves 2.5% \u2192 3.0% on demonstrated \u2014 "
               "not normalized-down \u2014 margins. Two names flip HOLD\u2192BUY (NKE $31\u2192$63.74, ZTS $64\u2192$95.40) "
               "purely on this math; two improve within their bands (HD REDUCE\u2192HOLD at $267.64, CDNS REDUCE\u2192HOLD "
               "at $308.05). META ($675\u2192$879.80) stays HOLD: the override lifts fair value +30% but the +30% BUY bar "
               "is still not cleared, and its qualification itself carries the one asterisk in the screen. The "
               "four borderline sensitivities (ADBE, INTU, MCD, plus META on the strict reading) are shown but not "
               "adopted \u2014 the override is a reward for decade-proven economics, and the letter of the rule matters "
               "enough to require an explicit adjudication before it is waived.", s_body))
story.append(P("The international framework (Addendum B) moves the other way: pricing country risk explicitly shaves "
               "15\u201335pp of upside off every non-US name, because a portion of the old cheapness was a "
               "US-discount-rate artifact, not mispricing. BABA ($180\u2192$132.39, BUY\u2192HOLD) and MELI "
               "($1,485\u2192$1,118.98, HOLD\u2192REDUCE) change verdicts mechanically \u2014 both businesses are "
               "untouched; what changed is the cost of capital repriced for China-VIE and LatAm-macro risk. JD, PDD, "
               "TME, SE, and TIGR keep their BUY verdicts with trimmed upside; GRAB keeps its HOLD at a now-thin +10%, "
               "flagged as the most fragile HOLD in the set. The framework's discipline is visible in the asymmetries: "
               "JD's bear carries no confiscation haircut because the cash-incineration mechanics already model a "
               "balance-sheet attack; TME's does, because its operating bear alone is only \u22128%; TIGR layers the CRP "
               "over named CSRC mechanics as disclosed belt-and-suspenders.", s_body))
story.append(P("Taken together, the two addenda do opposite but consistent things: Addendum A says proven quality "
               "deserves a cheaper cost of capital, priced in the explicit forecast period rather than smuggled into "
               "the perpetuity; Addendum B says foreign institutional risk deserves a more expensive cost of capital, "
               "priced in the discount rate with structural risks in the cash flows rather than footnoted. Both "
               "disciplines \u2014 the bear that must still hurt, the no-double-counting rule, the documented split "
               "between what the discount covers and what the cash flows cover \u2014 are there to stop the analyst "
               "from reaching the same number through layered optimism or layered pessimism. The verdict migration "
               "across the two re-runs (4 upgrades via A, 2 downgrades via B) is the framework working as designed: "
               "risk repriced in both directions, with every assumption on the page.", s_body))

story.append(P("Limitations", s_h2))
lim = [
 "Both addenda are judgment overlays, not measured constants: the 8.0\u20138.5% override band, the 3.0% terminal cap, and the CRP reference table (+250/+150/+200bp) are calibrated reasoning, not market-observed parameters. The pick-within-band still requires its written justification or it becomes the vibes-based discounting v2 was built to kill.",
 "Mean reversion is real and unmodeled: ten years of >15% ROIC is evidence, not a guarantee of an eleventh. High returns attract competition and capital; ROIC can also be flattered by asset-light accounting, underinvestment (capex persistently below D&A), or one-time working-capital releases. The FCF-conversion test catches most of this, which is why all three tests are required \u2014 but the analyst must still sanity-check capex intensity.",
 "The CRP is country-blunt: it does not differentiate an SOE from a founder-led company, onshore from offshore cash, or a state-favored sector from a state-targeted one. Firm-level differentiation lives in the B3 cash-flow modeling \u2014 use it. Regional comp sets can be thin (two credible peers, not five): report the thinness, never pad with US names.",
 "Double-counting is the evergreen failure mode of Addendum B: CRP in the discount rate <i>and</i> a kitchen-sink bear case <i>and</i> a VIE haircut <i>and</i> a currency haircut can stack into \u201cuninvestable at any price.\u201d The no-double-counting rule (B1) is the guardrail; the review step is where it is enforced.",
 "Double-qualifiers stack additively: a qualifying compounder domiciled in a high-risk country gets the override base <i>plus</i> the country-risk premium (e.g., a Chinese compounder at 8.25% override base is discounted at 10.75%). No name in this re-run triggered the stack; the rule stands for future notes.",
 "Falsification is mechanical: 2 consecutive years of ROIC <15%, or trailing gross margin >200bp below the qualification-period average, revokes the override (A4); CRP moves only on regime breaks or the annual January true-up (B1). FCF conversion breaking below 60% for two consecutive years triggers a full re-qualification review \u2014 often the first crack in the story.",
 "Method heterogeneity across the three screen batches is disclosed (batch notes under Section 4): year-key conventions, NOPAT fallbacks, and FCF-conversion averaging vs cumulative differ slightly. Verdicts were cross-checked against the stated rules; borderlines are flagged rather than smoothed over.",
 "All valuations are ~10-year scenario-weighted expected values under the stated assumptions, measured against October 2, 2026 closes. This is research analysis, not investment advice; no position is recommended and no personal financial circumstances have been considered.",
]
for it in lim:
    story.append(Paragraph("\u2022\u2003" + inline_md(it), s_bull))

story.append(Spacer(1, 6*mm))
story.append(P("Source files: addenda \u2014 <font face=\"Courier\" size=\"8\">~/workspace/valuation-addenda/addendum-a-compounder-override.md</font>, "
               "<font face=\"Courier\" size=\"8\">addendum-b-international-framework.md</font>; screens \u2014 "
               "<font face=\"Courier\" size=\"8\">~/workspace/compounder-screen/</font>, "
               "<font face=\"Courier\" size=\"8\">~/workspace/valuation-addenda/screen-18/</font>; internationals \u2014 "
               "<font face=\"Courier\" size=\"8\">~/workspace/valuation-catchup/</font>.", s_small))
story.append(P("Prepared October 4, 2026. Research analysis, not investment advice.", s_small))

doc = SimpleDocTemplate(OUT, pagesize=A4, topMargin=20*mm, bottomMargin=18*mm,
                        leftMargin=18*mm, rightMargin=18*mm,
                        title="Valuation Methodology Addenda \u2014 Compounder-Quality Override & International Framework",
                        author="Equity Research Desk")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("OK:", OUT)
