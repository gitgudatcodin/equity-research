#!/usr/bin/env python3
"""Build the RH (RH) equity research note PDF - v2 hardened rebuild, Oct 4 2026."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, HRFlowable)
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import VerticalBarChart

OUT = "/home/hatch/workspace/your_files/rh-equity-research/rh-equity-research-note.pdf"

NAVY = HexColor("#0F2A44"); ACCENT = HexColor("#7C3A2D"); GOLD = HexColor("#C9A227")
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
    canvas.drawString(18*mm, 12*mm, "RH (NYSE: RH)  \u2014  Equity Research Note  \u2014  October 2026")
    canvas.drawRightString(W - 18*mm, 12*mm, f"Page {doc.page}")
    canvas.setStrokeColor(MGRAY); canvas.setLineWidth(0.5)
    canvas.line(18*mm, 14.5*mm, W - 18*mm, 14.5*mm)
    canvas.restoreState()

# ============ COVER ============
story.append(Spacer(1, 24*mm))
story.append(P("RH (NYSE: RH)", ParagraphStyle("x", parent=s_sub, fontName="Helvetica-Bold", fontSize=13, textColor=ACCENT, spaceAfter=2)))
story.append(P("The Levered Luxury Bet<br/>A Call Option, Repriced Honestly", s_title))
story.append(Spacer(1, 4*mm))
story.append(P("Equity Research Note  \u00b7  Consumer Discretionary \u2014 Homefurnishing Retail  \u00b7  October 4, 2026", s_sub))
story.append(Spacer(1, 8*mm))

rating_data = [
    [cell("Recommendation", s_theadL), cell("12-Mo. Price Target", s_thead), cell("Current Price", s_thead), cell("Implied Upside", s_thead), cell("Risk Rating", s_thead)],
    [Paragraph("<b><font color=\"#0E7C3E\" size=\"13\">BUY</font></b>", s_cellC),
     Paragraph("<b><font size=\"12\">$177</font></b>", s_cellC),
     Paragraph("<b>$120.46</b><br/><font size=\"7\" color=\"#5A6472\">Oct 2, 2026</font>", s_cellC),
     Paragraph("<b>+46.9%</b>", s_cellC),
     Paragraph("<b>High</b><br/><font size=\"7\" color=\"#5A6472\">Beta 1.86</font>", s_cellC)],
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
    ["Market cap", "~$2.28 bn", "Shares out. (dil.)", "~18.9 m"],
    ["Enterprise value", "~$4.54 bn", "52-week range", "$106.30 \u2013 $239.40"],
    ["Net financial debt", "$2.26 bn / 4.2x EBITDA", "YTD / 1-yr return", "-31% / -38%"],
    ["FY26E rev / adj. EBITDA", "$3.63\u20133.68 bn / 15\u201316%", "Trailing / fwd P/E", "21.3x / 14.1x"],
    ["Term loan maturity", "$2.5B, Oct 2028", "Book equity", "$61 m (buybacks)"],
    ["Next catalyst", "Q3 results (Dec)", "Street consensus", "$165.57 avg (Hold)"],
]
sd = [[cell(r[0], s_cellB), cell(r[1], s_cell), cell(r[2], s_cellB), cell(r[3], s_cell)] for r in snap]
story.append(styled_table([[cell("Snapshot", s_theadL), cell("", s_thead), cell("", s_thead), cell("", s_thead)]] + sd,
               [38*mm, 42*mm, 42*mm, 48*mm], header_rows=1))
story.append(Spacer(1, 8*mm))
story.append(P("This note is independent research-style analysis for informational purposes only and is not investment advice. "
               "Financial figures from company releases and SEC filings; market data as of October 2, 2026. "
               "Projections and the price target are the author's estimates. This note supersedes the September 28, 2026 "
               "edition (BUY, $265 target), which is withdrawn.", s_small))
story.append(PageBreak())

# ============ 1. INVESTMENT THESIS ============
story.append(P("1 &nbsp; Investment Thesis", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("We keep the <b>BUY</b> but cut the target from $265 to <b>$177</b>. The September note's DCF had three "
               "leaks the hardened rebuild closes: terminal growth of <b>2.8% base / 3.3% bull</b> (above the 2.5% cap), "
               "weights of <b>30/50/20</b> instead of 25/50/25, and \u2014 most importantly \u2014 a <b>9.5% base discount</b> "
               "for a company with 4.2x leverage, $61M of book equity, a $2.5B term loan maturing in October 2028, and a "
               "beta of 1.86. That is not a 9.5% cost of capital; it is a 12% one (speculative tier), with the bear at "
               "14.5% and the bull at 10.5%. Rebuilt honestly, the three scenarios are <b>~$0 / $191 / $326</b>, weighted "
               "to <b>$176.85 \u2192 $177 target, +46.9%</b> against the $120.46 quote. The thesis is unchanged \u2014 "
               "a luxury brand at an earnings inflection with a product catalyst, a fading margin drag, and a capital "
               "structure that turns modest enterprise-value recovery into a large equity return \u2014 but the price of "
               "admission is now stated correctly: this equity is a call option, and options demand a discount rate that "
               "knows it.", s_body))
story.append(P("Read the bear case first, because the leverage means it first. In our bear case \u2014 housing frozen to "
               "2028, tariffs lingering, Estates underwhelming \u2014 the firm is worth $2.0B against $2.26B of net "
               "financial debt, and the equity is worth <b>~$0</b>. That is not a modeling artifact; it is what 4.2x "
               "leverage does. The September note's bear was $10; the hardened bear, discounted at 14.5% with revenue "
               "CAGR under 3% and margins compressed 650bp vs base, rounds to zero. Size this as a high-conviction, "
               "high-risk position \u2014 2\u20134% of a portfolio, not a core holding \u2014 and the asymmetry is real: "
               "+47% to the weighted target, +171% to the bull case, against a well-defined zero.", s_body))

story.append(P("Why own it", s_h2))
for b in [
    "<b>Inflection is underway; the price hasn't noticed.</b> Q2 FY26 revenue ($922.2M, +2.6%) and normalized adjusted EBITDA margin (13.4%) both beat the high end of guidance, with growth accelerating 4.2 points from Q1. The stock fell 48% from its high anyway \u2014 the market sees only the housing freeze and the margin drag.",
    "<b>RH Estates is the most important product launch in the company's history.</b> A new collection priced ~45% above the core line, aimed at the 60% of luxury homes with classic/traditional architecture RH historically underserved \u2014 management believes it can double the addressable market. Early reads: genuinely new customers, 'overwhelmingly positive' response, 80% of volume galleries carrying it on the main floor by mid-November.",
    "<b>International swings from drag to driver.</b> London Mayfair built a $7M design pipeline in eight weeks \u2014 on par with Newport and New York. With no new European openings in FY27, the ~340bp pre-opening margin drag steps down while the revenue builds. Adjusted capex falls to $175\u2013200M from $240\u2013260M.",
    "<b>Mid-cycle earnings power is far above current earnings.</b> At the last housing peak RH did $3.59B of revenue at ~19.5% EBITDA margins; our base case compounds revenue ~7% to ~$7.1B by FY35 with margins recovering to 20% (below the 27%+ FY21 peak), generating ~$850M of annual free cash flow that delevers the balance sheet.",
    "<b>The gallery flywheel is a genuine moat.</b> 138 locations including palatial Design Galleries with restaurants that generate ~65% of the aggregate rent of the galleries they sit in \u2014 the hospitality traffic pays for the real estate. New single-story galleries and Compounds (Naples/Aventura, 2027, 12\u201318-month paybacks) cut build costs as the capex cycle peaks.",
]:
    story.append(B(b))
story.append(P("Why the market should be nervous", s_h2))
for b in [
    "<b>The October 2028 maturity is the #1 risk.</b> The $2.5B term loan (SOFR + 3.25%) must be refinanced; interest runs ~$225M a year \u2014 nearly 2x FY25 net income. Any sustained earnings disappointment raises covenant and refinancing risk, and the refinancing will almost certainly come at a higher spread than the 2021 vintage.",
    "<b>Housing could stay frozen through 2028.</b> Existing-home sales at multi-decade lows, the 30-year mortgage near 7%. Furniture demand tracks turnover with a lag; if the freeze extends, revenue stagnates and the bear case ($0) plays out.",
    "<b>Tariffs are a higher-cost world for 6\u201312 months.</b> ~40% of the assortment sourced from China; resourcing takes 18\u201324 months. The $55.1M Q2 tariff benefit flattered gross margin by ~600bp \u2014 the underlying cost pressure is the real story.",
    "<b>Estates could miss.</b> 'The most prolific collection in the history of our industry' at a 45% premium, launched into a housing downturn. A miss delays the inflection 12\u201318 months and turns the inventory bet into a markdown problem.",
    "<b>Key-man risk: Gary Friedman.</b> No public company in this sector depends as completely on one individual's taste and force of will. No disclosed succession plan.",
    "<b>Shareholder litigation.</b> Multiple suits filed April 2026 investigate buyback timing and disclosures \u2014 the $2.25B of 2022\u201323 buybacks at prices far above today's will be Exhibit A.",
]:
    story.append(B(b))

# ============ 2. BUSINESS ============
story.append(P("2 &nbsp; Company Overview", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("RH (founded 1979, rebranded 2012) is a luxury home-furnishings company Chairman/CEO Gary Friedman has spent "
               "15 years transforming into a luxury lifestyle brand and experiential retail/hospitality platform: furniture, "
               "lighting, textiles, rugs, bath, outdoor and d\u00e9cor across Interiors, Modern, Outdoor, Baby &amp; Child, "
               "Teen, and now Estates \u2014 sold through 138 RH Galleries, outlets, Source Books, and digital. The "
               "commercial engine is a $200/year membership (30% off everything, free design services): the Costco playbook "
               "applied to $10,000 sectionals. More than a dozen galleries house restaurants; the company is building "
               "'the world's largest residential interior design firm,' moving from selling products to selling whole spaces.",
               s_body))
story.append(P("The cycle in four years: FY22 (ended Jan 2023) was the peak \u2014 $3.59B revenue, $528.6M net income, "
               "19.5% EBITDA margins. Then the housing freeze: revenue fell 15.6% in FY23, net income collapsed to "
               "$127.6M, FY24 troughed at $72.4M. FY25 began the recovery: revenue +8.1% to $3.44B, EBITDA +20% to "
               "$543.6M, free cash flow +$249M. The business is roughly back to peak revenue at roughly two-thirds of "
               "peak earnings \u2014 that gap is the opportunity, and the international build-out is the reason it "
               "persists. Q2 FY26 (reported Sept 10, 2026): revenue and normalized EBITDA both beat the high end of "
               "guidance; adjusted EPS of $2.70 crushed the $0.39 consensus \u2014 but $55.1M of tariff benefits flattered "
               "the print and Q3 guidance came in below the Street.", s_body))
story.append(P("Balance sheet: the buyback legacy. FY22\u201323 buybacks of $2.25B \u2014 funded by the $2.5B term loan "
               "\u2014 cut diluted shares from 26.6M to 19.8M and wiped out book equity ($61M today). Net financial debt "
               "$2.26B is 4.2x TTM adjusted EBITDA (~$1.5B of operating-lease liabilities treated as operating rent, "
               "consistent with the company's own leverage metric). Liquidity is adequate ($125.5M cash, guided "
               "$300\u2013400M annual cash generation), but there is no margin for a multi-year earnings disappointment.",
               s_body))

# ============ 3. COMPETITION ============
story.append(P("3 &nbsp; Competition", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Williams-Sonoma is the quality comp and the valuation benchmark: 2.3x RH's revenue at 14.7% net margins "
               "vs RH's 3.6% \u2014 WSM shows what RH's P&amp;L looks like without the international drag and leverage "
               "(growing +6.7% last quarter vs RH's +2.6%). Arhaus (+7.4% growth, lean balance sheet) is the purest "
               "premium-furniture comp and shows the category has legs. Wayfair competes for the wallet, not the luxury "
               "positioning. RH's moat is brand + experience + ecosystem \u2014 narrow-to-moderate, widening if Estates "
               "and international execute: experiential flagships competitors cannot copy cheaply, membership economics, "
               "design IP (Estates protected by trade dress/pending patents), and hospitality that manufactures desire.",
               s_body))

# ============ 4. VALUATION ============
story.append(P("4 &nbsp; Valuation \u2014 Hardened 10-Year DCF, Fair Value $177", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("The September note's DCF is rebuilt under hardened rules: 10-year explicit free-cash-flow horizon "
               "(FY26\u2013FY35), weights bear 25% / base 50% / bull 25% (not 30/50/20), terminal growth capped at "
               "<b>2.5%</b> (not 2.8%/3.3%), and \u2014 the change that matters most \u2014 scenario-specific discounts "
               "priced for the leverage: <b>base 12.0%</b> (speculative tier: 4.2x net debt/EBITDA, $61M book equity, "
               "$2.5B maturity in October 2028, beta 1.86, single-key-man brand), <b>bear 14.5%</b> (base + 250bp), "
               "<b>bull 10.5%</b> (base \u2013 150bp). Terminal growth is <b>2.5% / 1.0% / 2.5%</b> on year-10 FCF at "
               "normalized mid-cycle margins (11.9% base \u2014 well below the 27%+ FY21 peak, never peak margins). "
               "Equity = firm EV minus $2.26B of company-disclosed net financial debt, over 18.93M shares.", s_body))
story.append(Spacer(1, 3*mm))
story.append(P("Scenario DCF (10-year FCFF):", s_h2))
dcf = [
    [cell("Scenario", s_theadL), cell("Rev CAGR", s_thead), cell("FCF path ($M)", s_thead), cell("FCF mgn yr-10", s_thead), cell("Discount / term. g", s_thead), cell("Fair value", s_thead)],
    [cell("Bear", s_cellB), cell("+2.5%", s_cellC), cell("340 \u2192 253", s_cellR), cell("5.4%", s_cellR), cell("14.5% / 1.0%", s_cellR), cell("~$0", s_cellBR)],
    [cell("Base", s_cellB), cell("+6.9%", s_cellC), cell("350 \u2192 848", s_cellR), cell("11.9%", s_cellR), cell("12.0% / 2.5%", s_cellR), cell("$190.73", s_cellBR)],
    [cell("Bull", s_cellB), cell("+9.5%", s_cellC), cell("372 \u2192 1,029", s_cellR), cell("11.4%", s_cellR), cell("10.5% / 2.5%", s_cellR), cell("$325.96", s_cellBR)],
    [cell("Probability-weighted (25/50/25) \u2192 <b>$177 target</b>", s_cellB), cell("", s_cellC), cell("", s_cellR), cell("", s_cellR), cell("", s_cellR), cell("$177", s_cellBR)],
]
story.append(styled_table(dcf, [52*mm, 22*mm, 28*mm, 24*mm, 30*mm, 24*mm]))

d2 = Drawing(430, 185)
d2.add(String(215, 173, "Scenario fair values vs. current price ($)", fontName="Helvetica-Bold", fontSize=10, textAnchor="middle", fillColor=NAVY))
bc2 = VerticalBarChart(); bc2.x = 45; bc2.y = 30; bc2.height = 115; bc2.width = 340
bc2.data = [[0, 191, 326, 177, 120]]
bc2.strokeColor = None; bc2.barLabels.nudge = 8; bc2.barLabelFormat = "%d"
bc2.bars[0].fillColor = ACCENT
bc2.categoryAxis.categoryNames = ["Bear", "Base", "Bull", "Wtd. avg", "Price"]
bc2.valueAxis.valueMin = 0; bc2.valueAxis.valueMax = 360; bc2.valueAxis.valueStep = 90
bc2.valueAxis.labels.fontSize = 7; bc2.categoryAxis.labels.fontSize = 8
d2.add(bc2)
story.append(d2)

story.append(P("The spread is the story, and it is wider than September's: 4.2x leverage makes this equity a call option. "
               "In the bear case \u2014 housing frozen to 2028, tariffs lingering, Estates underwhelming \u2014 revenue "
               "CAGR stays under 3%, FCF margins compress 650bp vs base (11.9% \u2192 5.4%), and the derating is total: "
               "firm EV of $2.0B against $2.26B of debt leaves the equity at <b>~$0</b>. All three hurt conditions are met "
               "and the bear sits below the price, as the rules require. In the base case \u2014 Estates and galleries "
               "work, housing normalizes, revenue compounds 6.9% to ~$7.1B, margins recover to 20% EBITDA \u2014 the firm "
               "is worth $5.9B and the equity <b>$190.73</b>. In the bull case \u2014 Estates doubles the addressable "
               "market, housing snaps back \u2014 <b>$325.96</b>. Terminal value is 50% of base-case EV (no haircut "
               "required).", s_body))
story.append(P("<b>Price target: $177</b> (0.25\u00d7$0 + 0.50\u00d7$190.73 + 0.25\u00d7$325.96 = $176.85, rounded) \u2014 "
               "the target <i>is</i> the weighted hardened DCF, with no multiple overrule. The September note's $265 "
               "rested on a 9.5% discount that underpriced the leverage by ~250bp and terminal growth above the cap; "
               "closing those leaks costs $88 of target and none of the thesis. Cross-checks: 18x forward EPS on "
               "recovered earnings \u2192 ~$157; 11x FY26E EV/EBITDA \u2192 ~$209 \u2014 both below the DCF because they "
               "price trough-to-early-cycle earnings while the DCF captures the full deleveraging arc. What would "
               "falsify the BUY: housing frozen through 2028, an Estates miss, or a dilutive/distressed refinancing of "
               "the 2028 term loan \u2014 any of which pushes fair value toward the $0 bear case.", s_body))

story.append(P("5 &nbsp; Key Risks", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
for b in [
    "<b>Leverage and the October 2028 maturity (the #1 risk).</b> $2.26B net financial debt at 4.2x EBITDA; $61M book equity; $2.5B term loan (SOFR + 3.25%) must be refinanced, almost certainly at a higher spread.",
    "<b>Housing freeze persists.</b> Four years of 'the worst housing market in 4 decades'; existing-home sales at multi-decade lows; 30-year mortgage near 7%.",
    "<b>Tariffs.</b> ~40% China-sourced; 'a higher cost world for at least the next 6\u201312 months'; resourcing takes 18\u201324 months.",
    "<b>International execution.</b> Germany impairments are a reminder the US playbook doesn't auto-translate; the FY26 drag is 340bp of margin.",
    "<b>RH Estates product miss.</b> Enormous expectations at a 45% premium into a downturn; a miss delays the inflection 12\u201318 months.",
    "<b>Key-man risk: Gary Friedman.</b> No disclosed succession plan.",
    "<b>Shareholder litigation.</b> April 2026 suits on buyback timing and disclosures; headline risk regardless of merit.",
]:
    story.append(B(b))

story.append(P("Recommendation", s_h2))
story.append(P("<b>BUY, $177 target (+46.9%), High risk.</b> The market is pricing a trough cyclical retailer with a scary "
               "balance sheet; the hardened DCF prices a luxury brand at an earnings inflection with a product catalyst "
               "(Estates), a fading margin drag (international), and a capital structure that turns modest enterprise-value "
               "recovery into a large equity return \u2014 at a discount rate that finally respects the leverage. Bear "
               "~$0 / base $190.73 / bull $325.96, weighted to $177 against a $120.46 quote. The September $265 target "
               "is withdrawn: it was directionally right and arithmetically generous \u2014 a 9.5% discount and "
               "above-cap terminal growth flattered the equity by $88. <b>This is a starter-sized, high-conviction, "
               "high-risk position: 2\u20134% of a portfolio, not a core holding.</b> Initiate at current levels; add on "
               "Q3 evidence that Estates is converting design pipelines into delivered revenue and that the international "
               "drag is rolling off on schedule. <b>Falsification:</b> housing frozen through 2028, an Estates miss, or "
               "a distressed 2028 refinancing pushes fair value toward the $0 bear case \u2014 and we would exit.", s_body))
story.append(Spacer(1, 6*mm))
story.append(P("Methodology &amp; sources. Valuation as of October 4, 2026; share price $120.46 (10/2/26 close). Model: 10-year "
               "scenario FCFF DCF, weights bear 25% / base 50% / bull 25%; discounts base 12.0% (speculative tier) / "
               "bear 14.5% / bull 10.5%; terminal growth 2.5% / 1.0% / 2.5% on year-10 FCF at normalized mid-cycle "
               "margins. Net financial debt $2.26B (company metric); 18.93M diluted shares. Bear case meets the hurt "
               "conditions (revenue CAGR &lt;3%, \u2265300bp margin compression, \u226525% derating) and sits below the "
               "current price. Terminal value is 50% of base-case EV (no haircut required). Financials from company "
               "10-K filings and Q2 FY26 press release/earnings call (September 10, 2026); market data via Yahoo Finance. "
               "This note is research analysis for informational purposes and is not personalized investment advice. "
               "Equity investing involves risk of loss. The author holds no position in RH at the time of writing.", s_small))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=18*mm,
                        title="RH \u2014 Equity Research Note", author="Muse")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("wrote", OUT)
