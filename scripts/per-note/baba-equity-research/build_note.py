#!/usr/bin/env python3
"""Build the Alibaba (BABA) equity research note PDF - v2 hardened rebuild, Oct 4 2026."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, HRFlowable)
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import VerticalBarChart

OUT = "/home/hatch/workspace/your_files/baba-equity-research/baba-equity-research-note.pdf"

NAVY = HexColor("#0F2A44"); ACCENT = HexColor("#B4531C"); GOLD = HexColor("#C9A227")
LGRAY = HexColor("#F2F4F7"); MGRAY = HexColor("#D9DEE5"); DGRAY = HexColor("#5A6472")
RED = HexColor("#B42318"); GREEN = HexColor("#0E7C3E"); BLUE = HexColor("#1D4ED8")

s_title = ParagraphStyle("t", fontName="Helvetica-Bold", fontSize=26, leading=30, textColor=NAVY)
s_sub = ParagraphStyle("s", fontName="Helvetica", fontSize=11, leading=15, textColor=DGRAY)
s_h1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=14, leading=18, textColor=NAVY, spaceBefore=10, spaceAfter=5)
s_h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=NAVY, spaceBefore=8, spaceAfter=4)
s_body = ParagraphStyle("b", fontName="Helvetica", fontSize=9.5, leading=14.5, textColor=HexColor("#1A2332"), alignment=TA_JUSTIFY, spaceAfter=5)
s_bull = ParagraphStyle("bu", parent=s_body, leftIndent=12, bulletIndent=4, spaceAfter=3, alignment=TA_LEFT)
s_small = ParagraphStyle("sm", fontName="Helvetica", fontSize=7.5, leading=10.5, textColor=DGRAY)
s_cell = ParagraphStyle("c", fontName="Helvetica", fontSize=8.5, leading=11.5, textColor=HexColor("#1A2332"))
s_cellB = ParagraphStyle("cb", parent=s_cell, fontName="Helvetica-Bold")
s_cellR = ParagraphStyle("cr", parent=s_cell, alignment=TA_RIGHT)
s_cellBR = ParagraphStyle("cbr", parent=s_cellB, alignment=TA_RIGHT)
s_cellC = ParagraphStyle("cc", parent=s_cell, alignment=TA_CENTER)
s_thead = ParagraphStyle("th", parent=s_cell, fontName="Helvetica-Bold", textColor=white, alignment=TA_CENTER, fontSize=8)
s_theadL = ParagraphStyle("thl", parent=s_thead, alignment=TA_LEFT)

def styled_table(data, col_widths, header_rows=1, zebra=True, fontsize=8.5):
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
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("ROWBACKGROUNDS", (0, header_rows), (-1, -1), [white, LGRAY] if zebra else [white, white]),
    ]))
    return t

def P(txt, style=s_body): return Paragraph(txt, style)
def B(txt): return Paragraph(f"<b>{txt}</b>", s_bull)
def cell(txt, st=s_cell): return Paragraph(txt, st)

story = []
W, H = A4

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7); canvas.setFillColor(DGRAY)
    canvas.drawString(18*mm, 12*mm, "Alibaba Group (NYSE: BABA / HK: 9988)  \u2014  Equity Research Note  \u2014  October 2026")
    canvas.drawRightString(W - 18*mm, 12*mm, f"Page {doc.page}")
    canvas.setStrokeColor(MGRAY); canvas.setLineWidth(0.5)
    canvas.line(18*mm, 14.5*mm, W - 18*mm, 14.5*mm)
    canvas.restoreState()

# ============ COVER ============
story.append(Spacer(1, 24*mm))
story.append(P("ALIBABA GROUP HOLDING LIMITED (NYSE: BABA / HK: 9988)", ParagraphStyle("x", parent=s_sub, fontName="Helvetica-Bold", fontSize=12, textColor=ACCENT, spaceAfter=2)))
story.append(P("The AI Cloud Re-Rating:<br/>Repriced for China Risk, Held Not Bought", s_title))
story.append(Spacer(1, 4*mm))
story.append(P("Equity Research Note  \u00b7  Internet \u2014 E-commerce &amp; Cloud  \u00b7  October 4, 2026", s_sub))
story.append(Spacer(1, 8*mm))

rating_data = [
    [cell("Recommendation", s_theadL), cell("12-Mo. Price Target", s_thead), cell("Current Price", s_thead), cell("Implied Upside", s_thead), cell("Risk Rating", s_thead)],
    [Paragraph("<b><font color=\"#B45309\" size=\"13\">HOLD</font></b>", s_cellC),
     Paragraph("<b><font size=\"12\">$132</font></b>", s_cellC),
     Paragraph("<b>$105.85</b><br/><font size=\"7\" color=\"#5A6472\">Oct 2, 2026</font>", s_cellC),
     Paragraph("<b>+24.7%</b>", s_cellC),
     Paragraph("<b>High</b><br/><font size=\"7\" color=\"#5A6472\">VIE / geopolitical</font>", s_cellC)],
]
t = Table(rating_data, colWidths=[36*mm, 36*mm, 36*mm, 36*mm, 36*mm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), NAVY), ("TEXTCOLOR", (0, 0), (-1, 0), white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"), ("FONTSIZE", (0, 0), (-1, 0), 8.5),
    ("GRID", (0, 0), (-1, -1), 0.5, MGRAY), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("BACKGROUND", (0, 1), (-1, 1), LGRAY), ("TOPPADDING", (0, 0), (-1, -1), 7),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 7), ("LEFTPADDING", (0, 0), (-1, -1), 8),
]))
story.append(t)
story.append(Spacer(1, 8*mm))

snap = [
    ["Market cap", "~$263 bn", "ADSs out. (dil.)", "~2.49 bn"],
    ["52-week range", "$91.99 \u2013 $189.61", "Net cash (narrow)", "~$30.7 bn"],
    ["TTM revenue / adj. EBITA", "RMB 1,046 bn / ~RMB 64 bn", "FY26 adj. EBITA margin", "7.5%"],
    ["Forward P/E (FY27E)", "11.5x (12.1x ex-cash)", "Dividend yield", "~1.0%"],
    ["AI Cloud growth", "+45% (9th accel. qtr)", "AI-product rev growth", "Triple digits, 12 qtrs"],
    ["Next catalyst", "Sept-qtr print ~mid-Nov", "MaaS ARR target", "RMB 30B by Dec 2026"],
]
sd = [[cell(r[0], s_cellB), cell(r[1], s_cell), cell(r[2], s_cellB), cell(r[3], s_cell)] for r in snap]
story.append(styled_table([[cell("Snapshot", s_theadL), cell("", s_thead), cell("", s_thead), cell("", s_thead)]] + sd,
               [38*mm, 42*mm, 42*mm, 48*mm], header_rows=1))
story.append(Spacer(1, 8*mm))
story.append(P("This note is independent research-style analysis for informational purposes only and is not investment advice. "
               "Financial figures from company releases (June quarter FY2027 reported August 2026; FY2026 10-K/press release). "
               "FX: $1 = RMB 7.20. Prices as of October 2, 2026 close. Projections and the price target are the author's "
               "estimates. This note supersedes the October 4, 2026 v2 edition (BUY, $180 target), which is withdrawn. "
               "The $180 target was a US-discount-rate artifact: it ran China VIE/regulatory risk at US rates. Addendum B "
               "(international framework, adopted October 4, 2026) applies an explicit +250bp China country-risk premium to "
               "every scenario discount rate. China ADR investing involves VIE-structure risk, regulatory risk, and currency risk.", s_small))
story.append(PageBreak())

# ============ 1. INVESTMENT THESIS ============
story.append(P("1 &nbsp; Investment Thesis", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("We downgrade Alibaba from <b>BUY to HOLD</b> and cut the target from $180 to <b>$132</b>. The business case is "
               "untouched \u2014 AI Cloud is still the best AI-infrastructure asset in China, still accelerating \u2014 but the old verdict was built "
               "on a US-discount-rate artifact: the October 4 v2 note ran China VIE/regulatory risk at US discount rates (base 10.0%). Addendum B "
               "(international framework) applies an explicit <b>+250bp China country-risk premium</b> to every scenario discount rate: <b>bear "
               "15.0%</b> / <b>base 12.5%</b> / <b>bull 11.0%</b>. The CRP is the entire verdict change. Fair value is <b>$132.39 \u2192 $132 target, "
               "+24.7%</b> against the $105.85 quote \u2014 and +24.7% no longer clears the +30% BUY bar at this risk level. The 20% haircut on "
               "RMB471B of investment carrying values is kept (embedded in all scenarios: RMB598B net claim = RMB221B narrow net cash + RMB471B "
               "investments at 80%). At $105.85 the name is fairly priced for its China risk; the old $180 was not.", s_body))
story.append(P("The core judgment is unchanged: Alibaba is two companies wearing one stock price \u2014 a mature Chinese "
               "e-commerce cash machine generating roughly RMB 40B of adjusted EBITA per quarter, and the fastest-scaling "
               "AI cloud business in China (+45% revenue growth for nine straight quarters of acceleration, margins now "
               "expanding from 7.2% to ~11.6%). The market sees only the first company and its problems: the stock has "
               "fallen 44% from its $190 high, pricing the shares at just 12.1x forward earnings ex-cash \u2014 a multiple "
               "that assumes the AI cycle contributes nothing. The 10-year DCF is the right lens because the story is the "
               "J-curve's <i>shape</i>: FCF prints \u2212RMB 45B in FY27, inflects positive in FY29\u201330 as the RMB 380B "
               "capex envelope completes, and compounds to RMB 336B by FY36. A 5-year model values the trough and misses "
               "the recovery; that was the old model's structural error.", s_body))

story.append(P("Why own it", s_h2))
for b in [
    "<b>The e-commerce engine still prints cash.</b> The E-commerce Group generated RMB 39.7B of adjusted EBITA in the June quarter alone (\u22121% YoY, held flat despite the quick-commerce scale-up) \u2014 an annualized ~RMB 160B funding base for the AI build, valued at a distressed multiple.",
    "<b>AI Cloud is the best AI-infrastructure asset in China, and it is accelerating.</b> Revenue +45% YoY (ninth straight quarter of acceleration), adjusted EBITA +133% with margins expanding to ~11.6%; AI-related product revenue growing triple digits for twelve consecutive quarters \u2014 now RMB 12.4B/quarter, ~35% of external cloud revenue. MaaS ARR passed RMB 16B in August against a RMB 30B December target.",
    "<b>The capex J-curve is the price of a durable moat, and the company can afford it.</b> RMB 67.7B of June-quarter capex (+75%) drove a record RMB \u221244.7B FCF outflow \u2014 but ~RMB 190B of the RMB 380B three-year AI plan is spent with two-thirds of the timeline remaining, narrow net cash sits at ~$30.7B, and the August HK$80B placement was 3x covered in under an hour with Middle East SWFs and European long-onlys taking 40%+.",
    "<b>Proprietary silicon de-risks the spend.</b> T-Head has shipped 500,000+ prior-generation chips; the Zhenwu M890 is commercially deployed with 650+ external customers, running inference for 2T-parameter-class models; the V900 launched at the September Apsara Conference. Every proprietary chip that replaces a procured GPU avoids 60\u201380% vendor gross margins \u2014 management targets capex payback shortening from ~3 years to ~2.5 years.",
    "<b>The open-source flywheel is underappreciated.</b> The Qwen family has 3B+ downloads and 300,000+ derivative models \u2014 the most-used open model family in the world. Open-sourcing Qwen3.8-Max sacrifices near-term API revenue to own the developer standard and route inference demand back to Alibaba Cloud.",
]:
    story.append(B(b))
story.append(P("Why the market should be nervous", s_h2))
for b in [
    "<b>The bear case ($64.36) is a real scenario, not a stress test.</b> If the RMB 380B capex program overruns with weak returns, quick-commerce losses never inflect (profitability not expected until FY2029), and chip controls tighten further, fair value is 39% below the price \u2014 revenue CAGR stalls at 3%, FCF margins compress 490bp vs base, and the J-curve becomes an L-curve.",
    "<b>VIE structure: holders own a contract, not the assets.</b> The HFCAA delisting risk is dormant but persistent by statute; the June 2026 DoD 1260H listing, a pending US securities class action (lead-plaintiff deadline October 5, 2026), and the \u20ac550M EU DSA fine (July 2026) all demand position sizing with humility. Any escalation re-rates the risk premium overnight.",
    "<b>China e-commerce share is structurally fragmented.</b> CMR decelerated to +1% like-for-like (from +8%); PDD and Douyin continue to take share. If core monetization stalls structurally rather than cyclically, normalized earnings power is lower than modeled.",
    "<b>The buyback era has paused.</b> US$12.5B (FY24) and US$11.9B (FY25) of repurchases collapsed to ~US$1B in FY26; SBC dilution is no longer being offset. Buybacks are a call option on the J-curve inflecting, not current price support.",
]:
    story.append(B(b))

# ============ 2. BUSINESS ============
story.append(P("2 &nbsp; Business Overview: The AI-First Conglomerate", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Alibaba (founded 1999, Hangzhou) is China's largest e-commerce platform operator and its largest public "
               "cloud provider, executing an 'AI-first, user-first' pivot under CEO Eddie Wu (in seat since September 2023, "
               "with Chairman Joe Tsai). The strategy is full-stack: proprietary models (Qwen) \u2192 proprietary "
               "semiconductors (T-Head) \u2192 data centers and cloud (Alibaba Cloud) \u2192 AI applications (Qwen app, "
               "QwenWork). The June quarter introduced a new four-segment reporting structure: Alibaba E-commerce Group "
               "(RMB 205.9B rev, +4%; RMB 39.7B adj. EBITA \u2014 the cash machine), AI Cloud &amp; Compute Services "
               "(RMB 48.4B, +45%; EBITA +133% \u2014 the growth engine), AI Labs &amp; Applications (RMB 3.3B rev, "
               "\u2212RMB 13.9B EBITA \u2014 the investment), and All Others (RMB 28.8B, +1%). Consolidated: RMB 269.0B "
               "(+9%), adj. EBITA RMB 27.3B (\u221230%) \u2014 the arithmetic of the J-curve.", s_body))
story.append(P("The pricing architecture is the moat's plumbing: the ad auction on Taobao/Tmall monetizes intent at ~5%+ "
               "take rates with near-zero marginal cost; cloud converts that cash into token-priced inference sold at a "
               "structural cost advantage via proprietary silicon; open-sourcing Qwen sacrifices licensing revenue to "
               "maximize the inference volume flowing back through the stack. A vertically integrated AI toll road, each "
               "layer reinforcing the others.", s_body))
story.append(P("Moat assessment: bifurcated \u2014 widening in AI infrastructure (cloud scale + enterprise switching costs, "
               "~36\u201340% China public-cloud share; full-stack AI integration no other Chinese tech company matches; "
               "T-Head cost advantage), narrowing in traditional e-commerce (two-sided network effects fragmenting as PDD "
               "~23% and Douyin ~17% take share). The investment case is a bet that the market is pricing the average "
               "while the mix shifts toward the widening half.", s_body))

# ============ 3. FINANCIALS ============
story.append(P("3 &nbsp; Financial Condition: Fortress Balance Sheet, J-Curve Income Statement", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Three stories at once: the balance sheet is a fortress, the income statement is mid-J-curve, cash flow is "
               "at maximum strain \u2014 and the investment case requires holding all three in mind. Revenue re-accelerated "
               "to +9% in the June quarter (fastest in over a year); the profit collapse (adj. EBITA margin 17.3% \u2192 "
               "7.5%) is four identifiable items \u2014 a \u20ac550M DSA provision, RMB 4.5B goodwill impairment, halved "
               "investment gains, and deliberate AI/quick-commerce investment \u2014 the first three largely non-recurring, "
               "the fourth the strategy.", s_body))
fin = [
    [cell("RMB mn (FY ends Mar 31)", s_theadL), cell("FY2024", s_thead), cell("FY2025", s_thead), cell("FY2026", s_thead), cell("Jun qtr FY27", s_thead)],
    [cell("Revenue", s_cellB), cell("941,168", s_cellR), cell("996,347", s_cellR), cell("1,023,670", s_cellR), cell("268,953", s_cellR)],
    [cell("Revenue growth", s_cell), cell("\u2014", s_cellC), cell("+5.9%", s_cellR), cell("+2.7%", s_cellR), cell("+9%", s_cellR)],
    [cell("Adjusted EBITA", s_cell), cell("165,114", s_cellR), cell("172,277", s_cellR), cell("76,416", s_cellR), cell("27,329", s_cellR)],
    [cell("Adj. EBITA margin", s_cell), cell("17.5%", s_cellR), cell("17.3%", s_cellR), cell("7.5%", s_cellR), cell("10.2%", s_cellR)],
    [cell("Capital expenditure", s_cell), cell("~45,000", s_cellR), cell("~88,000", s_cellR), cell("~122,800", s_cellR), cell("67,678", s_cellR)],
    [cell("Free cash flow", s_cell), cell("~137,600", s_cellR), cell("73,870", s_cellR), cell("\u221246,609", s_cellR), cell("\u221244,670", s_cellR)],
]
story.append(styled_table(fin, [46*mm, 28*mm, 28*mm, 32*mm, 30*mm]))
story.append(P("Sources: company press releases and filings. The CFO explicitly warned against annualizing the June quarter (procurement lumpiness, a one-off CPU capacity surge for AI agents, chip-component price inflation). Cash and liquid investments of RMB 474.5B at June 30, 2026; narrow net cash ~$30.7B; debt-to-equity 0.21.", s_small))

# ============ 4. VALUATION ============
story.append(P("4 &nbsp; Valuation \u2014 Addendum B: China Country-Risk Premium, Fair Value $132", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("The October 4 v2 note valued Alibaba at $180 on a 10-year scenario FCFF DCF with US discount rates (base "
               "10.0%, bear 12.5%, bull 8.5%) \u2014 pricing China VIE/regulatory risk nowhere in the cost of capital. "
               "Addendum B (international framework) stacks an explicit <b>+250bp China country-risk premium</b> on every "
               "scenario rate \u2014 VIE contractual-claim enforceability, the regulatory confiscation tail, US\u2013China "
               "decoupling/delisting repricing; Damodaran-style China ERP ~5.5\u20136% vs US ~4.5%, plus a VIE-structure "
               "premium \u2014 taking rates to <b>bear 15.0%</b> / <b>base 12.5%</b> / <b>bull 11.0%</b>. Operating "
               "projections are carried unchanged from the v2 note; the premium is a required-return adjustment, not a "
               "business downgrade. Terminal value is 65.6% of base-case EV (no haircut required).", s_body))
story.append(P("The balance-sheet bridge is hardened too: <b>RMB 598B of non-operating assets</b> = narrow net cash "
               "RMB 221B + RMB471B of investment securities at 80% of carrying (a <b>20% haircut, disclosed</b>, for "
               "regulatory/liquidity risk on the Ant Group stake and listed holdings \u2014 strategic stakes are not "
               "overnight liquidity, and their income is excluded from operating FCF, so carrying value was never the "
               "right number). 2.486B ADSs; FX 7.20.", s_body))
story.append(P("The balance-sheet bridge is hardened too: <b>RMB 598B of non-operating assets</b> = narrow net cash "
               "RMB 221B + investment securities at 80% of carrying (a <b>20% haircut, disclosed</b>, for "
               "regulatory/liquidity risk on the Ant Group stake and listed holdings \u2014 strategic stakes are not "
               "overnight liquidity, and their income is excluded from operating FCF, so carrying value was never the "
               "right number). 2.486B ADSs; FX 7.20.", s_body))
story.append(Spacer(1, 3*mm))
story.append(P("Scenario DCF (10-year FCFF, RMB B; post-CRP):", s_h2))
dcf = [
    [cell("Scenario", s_theadL), cell("Rev CAGR", s_thead), cell("FCF path (RMB B)", s_thead), cell("FCF mgn yr-10", s_thead), cell("Discount / term. g", s_thead), cell("Fair value", s_thead)],
    [cell("Bear", s_cellB), cell("+3.0%", s_cellC), cell("\u221260 \u2192 144", s_cellR), cell("9.4%", s_cellR), cell("15.0% / 0.5%", s_cellR), cell("$55.23", s_cellBR)],
    [cell("Base", s_cellB), cell("+7.5%", s_cellC), cell("\u221244 \u2192 336", s_cellR), cell("14.3%", s_cellR), cell("12.5% / 2.0%", s_cellR), cell("$130.62", s_cellBR)],
    [cell("Bull", s_cellB), cell("+9.5%", s_cellC), cell("\u221230 \u2192 492", s_cellR), cell("17.4%", s_cellR), cell("11.0% / 2.0%*", s_cellR), cell("$213.07", s_cellBR)],
    [cell("Probability-weighted (25/50/25) \u2192 <b>$132 target</b>", s_cellB), cell("", s_cellC), cell("", s_cellR), cell("", s_cellR), cell("", s_cellR), cell("$132", s_cellBR)],
]
story.append(styled_table(dcf, [52*mm, 22*mm, 28*mm, 24*mm, 30*mm, 24*mm]))
story.append(P("*Bull terminal growth haircut 2.5% \u2192 2.0% to keep terminal value \u226470% of EV (disclosed).", s_small))

d2 = Drawing(430, 185)
d2.add(String(215, 173, "Scenario fair values vs. current price ($/ADS)", fontName="Helvetica-Bold", fontSize=10, textAnchor="middle", fillColor=NAVY))
bc2 = VerticalBarChart(); bc2.x = 45; bc2.y = 30; bc2.height = 115; bc2.width = 340
bc2.data = [[55, 131, 213, 132, 106]]
bc2.strokeColor = None; bc2.barLabels.nudge = 8; bc2.barLabelFormat = "%d"
bc2.bars[0].fillColor = ACCENT
bc2.categoryAxis.categoryNames = ["Bear", "Base", "Bull", "Wtd. avg", "Price"]
bc2.valueAxis.valueMin = 0; bc2.valueAxis.valueMax = 250; bc2.valueAxis.valueStep = 50
bc2.valueAxis.labels.fontSize = 7; bc2.categoryAxis.labels.fontSize = 8
d2.add(bc2)
story.append(d2)

story.append(P("The bear case ($55.23, \u201348% vs price) hurts the way the rules require: AI capex overruns with weak returns, "
               "quick-commerce losses never inflecting, share loss to PDD/Douyin, and a geopolitical shock \u2014 FCF margins compress "
               "490bp vs base (14.3% \u2192 9.4%), and the bear sits well below the quote. The base case \u2014 the capex envelope "
               "completes in FY28, cloud compounds ~25% for five years, EBITA margins recover toward 20% as AI Labs burn halves \u2014 is worth "
               "<b>$130.62</b>. The bull case \u2014 MaaS beats its December target, T-Head substitution accelerates, Ant crystallizes \u2014 is worth "
               "<b>$213.07</b>, even after the terminal-growth haircut. What changed, line by line, vs v2: <b>+250bp on every discount rate</b> "
               "(12.5/10.0/8.5% \u2192 15.0/12.5/11.0%); nothing else moved. Bear $64.36 \u2192 $55.23; base $174.02 \u2192 $130.62; "
               "bull $306.26 \u2192 $213.07. The verdict change is mechanical: +69.7% \u2192 +24.7% no longer clears the +30% BUY bar.", s_body))
story.append(P("<b>Price target: $132</b> (0.25\u00d7$55.23 + 0.50\u00d7$130.62 + 0.25\u00d7$213.07 = $132.39, rounded). "
               "The target <i>is</i> the probability-weighted DCF \u2014 no show-me discount, no multiple overrule. Cross-check "
               "(disclosed): the new fair value is <b>14.4x forward EPS ($9.19)</b> vs a China big-tech median of ~11.3x (Tencent 11.7, "
               "Meituan 14.5, Baidu 10.9, NetEase 10.9) \u2014 regional multiples imply ~$104, <b>contradicting the DCF by ~27%</b>. "
               "The DCF pays for AI-cloud option value and the investment book that regional multiples don't price. The multiple says the "
               "market prices the operating business near $104; the DCF says the full book is worth $132. The contradiction is the AI-cloud "
               "premium, stated plainly. What would falsify the HOLD: VIE enforcement relaxation or an Ant re-rating (the confiscation tail "
               "lifting) would argue the 250bp premium is too punitive; MaaS ARR missing the RMB 30B December target while capex guidance "
               "rises would argue the premium is too small. We would sell on thesis convergence toward $132, not on volatility.", s_body))

story.append(P("5 &nbsp; Key Risks", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
for b in [
    "<b>Geopolitics and US-listing overhang (High).</b> VIE structure; HFCAA delisting risk dormant but persistent by statute; June 2026 DoD 1260H listing; pending US securities class action (lead-plaintiff deadline October 5, 2026).",
    "<b>AI-chip export controls (High).</b> The January 2026 BIS rule restricts Nvidia H200/AMD MI325X flows into China; controls accelerate T-Head substitution but restrict frontier training capacity and inflate component prices.",
    "<b>Capex overrun / weak returns (High).</b> ~RMB 190B of the RMB 380B envelope spent at one-third of the timeline; management says spend will 'likely be exceeded.' If AI demand disappoints, the J-curve becomes an L-curve.",
    "<b>Quick-commerce losses that never inflect (Medium-High).</b> Overall profitability not expected until FY2029; the Meituan/JD subsidy war already drew RMB 3.6B of regulator fines.",
    "<b>China e-commerce share loss (Medium).</b> CMR at +1% like-for-like; PDD and Douyin take share; a structural stall lowers normalized earnings power.",
    "<b>EU regulatory exposure (Medium).</b> The \u20ac550M DSA fine (July 2026) comes with an October 2026 remedial-action deadline and a December compliance review.",
    "<b>Execution and key-person risk (Medium).</b> The thesis rides on Eddie Wu's AI-first pivot; authority is increasingly concentrated.",
]:
    story.append(B(b))

story.append(P("Catalysts (next 12 months)", s_h2))
for b in [
    "<b>September-quarter print (~mid-November 2026):</b> cloud acceleration holding (10th quarter), MaaS ARR progress toward RMB 30B, quick-commerce unit-economics improvement.",
    "<b>December 2026 MaaS ARR target (RMB 30B):</b> already ahead of plan at RMB 16B in August \u2014 a hit or beat validates AI monetization.",
    "<b>Ant Group IPO path:</b> Ant International's eyed Hong Kong IPO would mark the ~33% stake to market \u2014 a direct SOTP unlock.",
    "<b>Buyback resumption:</b> >US$19B of authorization unused; any re-acceleration signals management's view that the J-curve is inflecting.",
    "<b>Zhenwu silicon milestones:</b> second-generation chips in development; rising external customer counts de-risk the capex payback thesis.",
]:
    story.append(B(b))

story.append(P("Recommendation", s_h2))
story.append(P("<b>HOLD, $132 target (+24.7%), High risk.</b> Alibaba is a net-cash AI-infrastructure leader whose "
               "business case is untouched \u2014 but the old $180 target was a US-discount-rate artifact. Addendum B stacks an explicit "
               "<b>+250bp China country-risk premium</b> on every scenario rate, and the DCF now values the "
               "equity at $132 (bear $55.23 / base $130.62 / bull $213.07) against a $105.85 quote \u2014 even with "
               "investment carrying values haircut 20%, the bull's terminal growth haircut, and VIE/geopolitical risk "
               "priced into an 11\u201315% discount curve. The v2 $180 target is withdrawn: it priced China risk at US rates. "
               "+24.7% does not clear the +30% BUY bar at this risk level. <b>Size with humility:</b> VIE structure, US-China chip controls, the pending class action, and "
               "the execution risk of a RMB 380B+ capex program are all real. At $105.85 the name is fairly priced for its "
               "China risk \u2014 holders should hold, and new money should wait for the premium to narrow or the verdict "
               "thresholds to clear. <b>Falsification:</b> VIE enforcement relaxation or an Ant re-rating (the 250bp premium "
               "lifting) would argue for BUY; a MaaS ARR miss with rising capex guidance, two quarters of negative "
               "like-for-like CMR, or an HFCAA/VIE escalation \u2014 any of which breaks the base case from the inside, "
               "and we would exit.", s_body))
story.append(Spacer(1, 6*mm))
story.append(P("Methodology &amp; sources. Valuation as of October 4, 2026; share price $105.85 (10/2/26 close). Model: 10-year "
               "scenario FCFF DCF, weights bear 25% / base 50% / bull 25%; discounts base 12.5% (incl. +250bp China CRP) / bear 15.0% / "
               "bull 11.0%; terminal growth 2.0% / 0.5% / 2.0% (bull haircut from 2.5%, disclosed) on year-10 FCF at "
               "normalized mid-cycle margins. Non-operating assets RMB 598B (narrow net cash RMB 221B + investments at 80% "
               "of carrying, 20% haircut disclosed); 2.486B ADSs; FX 7.20. Bear case meets two of three hurt conditions "
               "(margin compression, derating) and sits below the current price. Terminal value is 65.6% of base-case EV "
               "(no haircut required). Build: valuation_model.py \u2192 valuation_output.json \u2192 build_note.py "
               "(reportlab). Financials from company press releases (June quarter FY2027, FY2026 results); market data via "
               "Yahoo Finance. This note is research analysis for informational purposes and is not personalized investment "
               "advice. Equity investing involves risk of loss. The author holds no position in BABA at the time of writing.",
               s_small))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=18*mm,
                        title="Alibaba (BABA) \u2014 Equity Research Note", author="Muse")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("wrote", OUT)
