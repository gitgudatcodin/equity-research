#!/usr/bin/env python3
"""Build the McDonald's equity research note PDF."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, HRFlowable)
from reportlab.graphics.shapes import Drawing, String, Rect
from reportlab.graphics.charts.barcharts import VerticalBarChart

OUT = "/home/hatch/workspace/your_files/mcdonalds-equity-research/mcdonalds-equity-research-note.pdf"

NAVY = HexColor("#0F2A44"); ACCENT = HexColor("#0E7C3E"); GOLD = HexColor("#C9A227")
LGRAY = HexColor("#F2F4F7"); MGRAY = HexColor("#D9DEE5"); DGRAY = HexColor("#5A6472")
RED = HexColor("#B42318")

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

def styled_table(data, col_widths, header_rows=1):
    t = Table(data, colWidths=col_widths, repeatRows=header_rows)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, header_rows - 1), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, header_rows - 1), white),
        ("FONTNAME", (0, 0), (-1, header_rows - 1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("GRID", (0, 0), (-1, -1), 0.4, MGRAY),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("ROWBACKGROUNDS", (0, header_rows), (-1, -1), [white, LGRAY]),
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
    canvas.drawString(18*mm, 12*mm, "McDonald's Corporation (NYSE: MCD)  \u2014  Equity Research Note  \u2014  September 2026")
    canvas.drawRightString(W - 18*mm, 12*mm, f"Page {doc.page}")
    canvas.setStrokeColor(MGRAY); canvas.setLineWidth(0.5)
    canvas.line(18*mm, 14.5*mm, W - 18*mm, 14.5*mm)
    canvas.restoreState()

# ============ COVER ============
story.append(Spacer(1, 26*mm))
story.append(P("McDONALD'S CORPORATION", ParagraphStyle("x", parent=s_sub, fontName="Helvetica-Bold", fontSize=13, textColor=ACCENT, spaceAfter=2)))
story.append(P("Fallen Arches?<br/>A Dividend King at a 52-Week Low", s_title))
story.append(Spacer(1, 4*mm))
story.append(P("Equity Research Note  \u00b7  Consumer Discretionary \u2014 Restaurants (QSR)  \u00b7  September 26, 2026", s_sub))
story.append(Spacer(1, 8*mm))

rating_data = [
    [cell("Recommendation", s_theadL), cell("12-Mo. Price Target", s_thead), cell("Current Price", s_thead), cell("Implied Upside", s_thead), cell("Risk Rating", s_thead)],
    [Paragraph("<b><font color=\"#0E7C3E\" size=\"13\">BUY</font></b>", s_cellC),
     Paragraph("<b><font size=\"12\">$300.00</font></b>", s_cellC),
     Paragraph("<b>$236.50</b><br/><font size=\"7\" color=\"#5A6472\">Sep 25, 2026</font>", s_cellC),
     Paragraph("<b><font color=\"#0E7C3E\">+27%</font></b>", s_cellC),
     Paragraph("<b>Medium</b><br/><font size=\"7\" color=\"#5A6472\">Beta 0.45</font>", s_cellC)],
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
    ["Market cap", "~$167.9 bn", "Shares out. (dil.)", "~710 mn"],
    ["Enterprise value", "~$207 bn", "52-week range", "$234.03 \u2013 $341.75"],
    ["Net debt", "~$39.2 bn", "YTD / 1-yr return", "-22.6% / -22.1%"],
    ["TTM P/E / 2027E P/E", "19.1\u00d7 / 17.0\u00d7", "Dividend yield", "3.26% ($7.72 annualized)"],
    ["FY2025 revenue", "$26.89 bn (+4%)", "FY2025 op. margin", "46.1%"],
    ["Next catalyst", "Q3'26 earnings, ~Oct 22", "Analyst consensus", "Moderate Buy, PT ~$300\u2013$321"],
]
sd = [[cell(r[0], s_cellB), cell(r[1], s_cell), cell(r[2], s_cellB), cell(r[3], s_cell)] for r in snap]
st2 = styled_table([[cell("Snapshot", s_theadL), cell("", s_thead), cell("", s_thead), cell("", s_thead)]] + sd,
                   [38*mm, 38*mm, 38*mm, 56*mm], header_rows=1)
story.append(st2)
story.append(Spacer(1, 8*mm))
story.append(P("This note is an independent research-style analysis for informational purposes only and is not investment advice. "
               "Figures are drawn from McDonald's SEC filings, earnings releases, the September 23, 2026 Investor Day materials, "
               "and reputable financial press as of September 26, 2026. Projections and the $300 price target are the author's estimates.",
               s_small))
story.append(PageBreak())

# ============ 1. EXECUTIVE SUMMARY ============
story.append(P("1 &nbsp; Executive Summary", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("McDonald's (MCD) is the world's largest quick-service restaurant system \u2014 <b>46,028 restaurants in 100+ countries, "
               "95% franchised, serving 70 million customers a day</b> \u2014 and its stock is trading at <b>$236.50, essentially the 52-week "
               "low</b> and down 22.6% year-to-date. The selloff is not mysterious: U.S. comparable sales grew just 0.8% in Q2 2026 on "
               "<i>declining guest counts</i>, management openly admitted it \"simply didn't execute,\" Burger King just posted an 8.5% U.S. "
               "comp on sharper value, and the market hated the price tag on the new growth plan unveiled at the September 23 Investor Day "
               "($8.5 billion of franchisee support through 2036 \u2014 shares fell ~6% that day).", s_body))
story.append(P("We rate MCD a <b>BUY</b> with a <b>$300.00</b> 12-month price target (~27% upside). Our thesis: the market is pricing McDonald's "
               "as a no-growth bond proxy with broken U.S. execution, but the underlying machine is intact \u2014 a 46% operating margin, "
               "27%+ ROIC, ~$7.2 billion of annual free cash flow, a 50-year dividend-growth streak (new Dividend King, 3.26% yield), and a "
               "credible 2030 roadmap to low-to-mid-50% margins. At 19\u00d7 trailing earnings \u2014 below Yum! Brands and Domino's despite "
               "superior margins \u2014 the stock offers the rare combination of <b>defensive quality at a cyclical price</b>. The key debate "
               "is execution, not strategy: new U.S. president Skye Anderson's value reset and the \"Make It Golden\" service program (launching "
               "October 5) must convert traffic declines into gains by early 2027. This is a <b>medium-risk</b> compounder, not a deep-value "
               "turnaround \u2014 size positions accordingly and expect the dividend to pay you to wait.", s_body))

story.append(P("Investment thesis \u2014 why own it", s_h2))
for b in [
    "<b>The selloff has decoupled price from business quality.</b> MCD has fallen 23% from its $341.75 high while 2025 delivered record revenue ($26.9 bn), a 46.1% operating margin, and $7.2 bn of free cash flow. Trailing P/E has compressed from the low-20s to 19.1\u00d7 \u2014 now <i>below</i> Yum! (17.4\u00d7 is close) and Domino's on earnings despite best-in-class margins and ROIC. EV/EBITDA of ~15\u00d7 sits well under its 18\u201319\u00d7 five-year average.",
    "<b>The franchise model is the moat that keeps compounding.</b> 95% franchised restaurants generate rents and royalties \u2014 high-margin, capital-light cash flows insulated from store-level labor and food-cost volatility. $28.2 bn of owned real estate, 670 million pounds of annual U.S. beef purchasing power, and the world's #1 restaurant brand ($42.6 bn brand value) are not replicable by any competitor.",
    "<b>The NEXT strategy has real, quantified targets \u2014 and the spending is an investment, not a bailout.</b> By 2030: operating margin in the low-to-mid 50% range (from 47%), ~250 bps of restaurant-level efficiency (~$100K of annual cash flow per average U.S. restaurant, ~4-year franchisee payback), mid-to-high-80% free-cash-flow conversion, and +1.5 points of share in chicken and beverages. The $8.5 bn franchisee commitment that spooked the market is spread over a decade and earns high-teens corporate returns.",
    "<b>Management named the problem and changed the leadership.</b> Kempczinski's candor (\"We don't have a strategy problem. We simply didn't execute\") plus the appointment of Skye Anderson as U.S. president, a reset of the under-$3 Everyday Affordable Price value platform (only 60\u201365% of restaurants were complying), and the October 5 \"Make It Golden\" hospitality relaunch give a concrete, near-term path to traffic recovery.",
    "<b>You are paid 3.26% to wait, with 50 years of raises behind it.</b> The September 17 dividend increase to $1.93/quarter ($7.72 annualized) marked the 50th consecutive annual raise \u2014 Dividend King status held by fewer than 60 U.S. companies. The payout ratio is a comfortable ~56%.",
]:
    story.append(B(b))

story.append(P("Key risks \u2014 why the market is scared", s_h2))
for b in [
    "<b>U.S. traffic is still falling.</b> Q2's +0.8% U.S. comp was all price/mix; guest counts declined. Burger King's +8.5% and Taco Bell's +7% show value-seeking customers are defecting to sharper-priced rivals. If Anderson's reset doesn't stabilize traffic by early 2027, the multiple stays depressed.",
    "<b>Beef inflation is brutal and structural.</b> U.S. beef costs are expected to run above 10% in 2026, the cattle herd is the smallest since 1951, and beef is ~38% of U.S. food-and-paper costs. The CFO called company-operated store margins \"not acceptable.\"",
    "<b>Franchisee relations are strained.</b> 95% of surveyed franchisees saw store-level profitability fall in Q1 2026; the NEXT plan asks ~$800K per restaurant on top of $400\u2013450K remodel cycles. Rent relief helps, but adoption risk is real \u2014 and 95% franchised means McDonald's can't force the pace.",
    "<b>GLP-1 drugs are a slow-burn demand risk.</b> ~30 million Americans now use them; Redburn estimates up to 28 million fewer annual McDonald's visits (~$0.5\u20130.7 bn revenue drag). Management's protein-forward menu response (chicken bowls, egg bites) is sensible but unproven at scale.",
]:
    story.append(B(b))

# ============ 2. COMPANY OVERVIEW ============
story.append(P("2 &nbsp; Company Overview \u2014 What McDonald's Is and What It Is Doing", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("McDonald's Corporation, headquartered in Chicago, Illinois (~150,000 employees), is the world's largest restaurant company by "
               "systemwide sales. The business is best understood not as a restaurant operator but as a <b>franchisor and landlord</b>: "
               "independent owner-operators run ~95% of the 46,028 restaurants, while McDonald's collects rent (it owns most of the underlying "
               "land and buildings) plus royalties and fees \u2014 a model that produced a 46.1% consolidated operating margin in 2025.", s_body))
story.append(P("Three reporting segments:", s_h2))
for b in [
    "<b>United States</b> \u2014 ~39% of systemwide sales; ~13,800 restaurants, nearly all franchised. The profit engine and the current problem child (traffic declines, value-execution miss).",
    "<b>International Operated Markets (IOM)</b> \u2014 ~35% of systemwide sales; company-operated and franchised restaurants in markets including the U.K., Germany, France, Australia, and Canada. The current growth driver: Q2 revenue +4.1%, operating income +5.4%.",
    "<b>International Developmental Licensed Markets (IDLM)</b> \u2014 ~26% of systemwide sales; licensed and developmental markets including China and Japan. Highest unit-growth potential; China comps were negative in Q2 on a soft consumer backdrop.",
]:
    story.append(B(b))
story.append(P("Revenue mix (2025): franchised rents, royalties and fees <b>$16.55 bn (+5%)</b>; company-operated restaurant sales "
               "<b>$9.69 bn (\u20131%)</b>; other revenues $0.65 bn; total <b>$26.89 bn (+4%)</b>. Systemwide sales \u2014 the true scale of the "
               "brand, including franchisee sales \u2014 reached <b>$139.4 bn in 2025 (+7%)</b> and ~$37 bn in Q2 2026 alone.", s_body))

story.append(P("What the company is doing right now \u2014 the five active fronts", s_h2))
for b in [
    "<b>1. McDonald's &gt; NEXT (unveiled June 2026, detailed September 23).</b> The successor to 2020's \"Accelerating the Arches,\" organized around four pillars \u2014 <b>Menu, Consumer, Restaurant, People</b> \u2014 with the stated ambition to be \"the first choice for more customers, more often.\" 2030 targets: low-to-mid-50% operating margin; ~250 bps of gross restaurant-level efficiency (~$100K annual cash flow per average U.S. restaurant); +1.5 pp of global share in <b>chicken</b> and <b>beverages</b> while holding beef leadership; free-cash-flow conversion in the mid-to-high 80% range; G&amp;A down to ~1.9% of systemwide sales; new units contributing ~2.5% to systemwide sales growth in 2027 (~2% by 2030). Backed by ~$8.5 bn of franchisee partnering support through 2036 (~$5 bn by 2030 via rent relief and capital), plus ~$3 bn/yr baseline capex.",
    "<b>2. Fixing U.S. value execution.</b> The January 2025 <b>McValue</b> platform (Buy-One-Add-One $1, in-app deals) and April 2026 McValue 2.0 (10 items under $3) failed on execution: only ~60\u201365% of U.S. restaurants honored the recommended \"Every Day Affordable Price\" pricing and consumer awareness fell short. New U.S. president <b>Skye Anderson</b> is leading the reset \u2014 temporary menu items, national digital promotions, personalized loyalty offers \u2014 with base menu pricing on beef, chicken and beverages now positioned below nearest competitors.",
    "<b>3. \"Make It Golden\" hospitality relaunch (October 5).</b> A multi-year, systemwide customer-experience commitment \u2014 great food plus great hospitality \u2014 with global retraining of 2M+ crew and partners, timed to Founder's Day. The explicit goal: fix the service-speed and satisfaction scores that deteriorated as crews were overloaded with simultaneous deployments.",
    "<b>4. Technology and AI at restaurant scale.</b> <b>ArchIQ</b>, a generative-AI restaurant operating system (multilingual order-taking, inventory, scheduling, AI suggestive-selling to lift average check), plus a <b>retail media network</b> being piloted in 450 company restaurants \u2014 envisioned as a potential billion-dollar, high-margin business. The digital backbone is formidable: ~220M 90-day active loyalty members (+13%) across 70 markets driving $40B+ of annual loyalty sales (+20%), all feeding a unified global data lake for AI personalization.",
    "<b>5. Menu: chicken and beverages as the growth vectors.</b> With beef costs squeezing, McDonald's is pushing where the puck is going: <b>McCrispy</b> now in 70+ markets, hand-breaded chicken expanding to more U.S. markets and Ireland in 2027, grilled chicken sandwiches/wraps, new McNugget flavors, and protein/GLP-1-oriented items (chicken bowls, snack wraps, egg bites). A new <b>beverage platform</b> (launched May 2026) is beating expectations in the U.S., Canada and Germany \u2014 higher checks (~50% above the full-day average), with over half of beverage traffic arriving after lunch. The failed <b>CosMc's</b> beverage concept (closed June 2025) was folded back into the mainline menu, and a dedicated beverage category team now owns the +1.5 pp share target.",
]:
    story.append(B(b))
story.append(P("Net assessment: this is an unusually <i>legible</i> corporate plan \u2014 quantified 2030 targets, named owners, dated launches \u2014 "
               "from a management team that has just publicly graded its own execution a fail. The question for investors is not whether the "
               "strategy is coherent (it is) but whether a 95%-franchised system can execute it at pace.", s_body))

# ============ 3. FINANCIAL ANALYSIS ============
story.append(P("3 &nbsp; Financial Analysis", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("The P&amp;L is a study in resilience: revenue has compounded through inflation, COVID, and consumer wobbles while the operating "
               "margin has held in the mid-40s \u2014 a profile no restaurant peer matches. 2022's dip reflects Russia-exit charges; the "
               "underlying franchise economics never broke.", s_body))

fin = [
    [cell("$ mn", s_theadL), cell("2021", s_thead), cell("2022", s_thead), cell("2023", s_thead), cell("2024", s_thead), cell("2025", s_thead), cell("H1'26", s_thead)],
    [cell("Revenue", s_cellB), cell("23,223", s_cellR), cell("23,183", s_cellR), cell("25,494", s_cellR), cell("25,920", s_cellR), cell("26,885", s_cellR), cell("13,616", s_cellR)],
    [cell("YoY growth", s_cell), cell("+21%", s_cellR), cell("\u20130%", s_cellR), cell("+10%", s_cellR), cell("+2%", s_cellR), cell("+4%", s_cellR), cell("+4%", s_cellR)],
    [cell("Operating income", s_cellB), cell("10,356", s_cellR), cell("9,371", s_cellR), cell("11,647", s_cellR), cell("11,712", s_cellR), cell("12,392", s_cellR), cell("6,292", s_cellR)],
    [cell("Operating margin", s_cell), cell("44.6%", s_cellR), cell("40.4%", s_cellR), cell("45.7%", s_cellR), cell("45.2%", s_cellR), cell("46.1%", s_cellR), cell("46.2%", s_cellR)],
    [cell("Net income", s_cellB), cell("7,545", s_cellR), cell("6,177", s_cellR), cell("8,469", s_cellR), cell("8,224", s_cellR), cell("8,563", s_cellR), cell("4,345", s_cellR)],
    [cell("Diluted EPS (GAAP)", s_cell), cell("$10.04", s_cellR), cell("$8.33", s_cellR), cell("$11.56", s_cellR), cell("$11.39", s_cellR), cell("$11.95", s_cellR), cell("$6.10", s_cellR)],
    [cell("Diluted EPS (adj.)", s_cell), cell("$9.28", s_cellR), cell("$10.10", s_cellR), cell("$11.94", s_cellR), cell("$11.72", s_cellR), cell("$12.20", s_cellR), cell("$6.21", s_cellR)],
    [cell("Free cash flow", s_cell), cell("\u2014", s_cellC), cell("\u2014", s_cellC), cell("\u2014", s_cellR), cell("6,700", s_cellR), cell("7,200", s_cellR), cell("\u2014", s_cellC)],
    [cell("FCF conversion", s_cell), cell("94%", s_cellR), cell("89%", s_cellR), cell("86%", s_cellR), cell("81%", s_cellR), cell("84%", s_cellR), cell("\u2014", s_cellC)],
    [cell("Dividend / share", s_cell), cell("$5.25", s_cellR), cell("$5.66", s_cellR), cell("$6.23", s_cellR), cell("$6.78", s_cellR), cell("$7.17", s_cellR), cell("$3.72", s_cellR)],
]
story.append(styled_table(fin, [32*mm, 22*mm, 22*mm, 22*mm, 22*mm, 22*mm, 22*mm]))
story.append(P("Sources: McDonald's 10-K filings (SEC EDGAR), Q2 2026 earnings release; FCF conversion from company Investor Overview Deck. "
               "2021/22 operating income classification differs across data providers due to Russia-sale charges; net income and EPS agree.", s_small))

d = Drawing(430, 190)
d.add(String(215, 178, "Revenue ($ bn, bars) vs. Adjusted Diluted EPS ($, line proxy)", fontName="Helvetica-Bold", fontSize=10, textAnchor="middle", fillColor=NAVY))
bc = VerticalBarChart(); bc.x = 45; bc.y = 30; bc.height = 120; bc.width = 340
bc.data = [[23.2, 23.2, 25.5, 25.9, 26.9, 28.2]]
bc.strokeColor = None; bc.barLabels.nudge = 8; bc.barLabelFormat = "%.1f"
bc.bars[0].fillColor = NAVY
bc.categoryAxis.labels.boxAnchor = "ne"
bc.categoryAxis.categoryNames = ["2021", "2022", "2023", "2024", "2025", "2026E"]
bc.valueAxis.valueMin = 0; bc.valueAxis.valueMax = 30; bc.valueAxis.valueStep = 6
bc.valueAxis.labels.fontSize = 7; bc.categoryAxis.labels.fontSize = 8
d.add(bc)
d.add(String(215, 12, "Adj. EPS: $9.28 \u2192 $10.10 \u2192 $11.94 \u2192 $11.72 \u2192 $12.20 \u2192 $12.93E  (+39% over five years)",
             fontName="Helvetica-Oblique", fontSize=8, textAnchor="middle", fillColor=DGRAY))
story.append(d)
story.append(Spacer(1, 2*mm))

story.append(P("Q2 2026 \u2014 the quarter that broke the stock's momentum", s_h2))
q = [
    [cell("", s_theadL), cell("Q2'26", s_thead), cell("YoY", s_thead), cell("vs. consensus", s_thead)],
    [cell("Revenue", s_cellB), cell("$7,099 mn", s_cellR), cell("+3.7%", s_cellR), cell("in line ($7.13 bn est.)", s_cellC)],
    [cell("GAAP / adjusted EPS", s_cellB), cell("$3.32 / $3.38", s_cellR), cell("+6% / +6%", s_cellR), cell("adj. beat by 1.8%", s_cellC)],
    [cell("Global comparable sales", s_cell), cell("+1.3%", s_cellC), cell("vs +3.8% in Q2'25", s_cellC), cell("soft", s_cellC)],
    [cell("U.S. comparable sales", s_cell), cell("+0.8%", s_cellC), cell("negative guest counts", s_cellC), cell("weak", s_cellC)],
    [cell("IOM revenue / op. income", s_cell), cell("+4.1% / +5.4%", s_cellC), cell("growth driver", s_cellC), cell("solid", s_cellC)],
    [cell("Operating margin", s_cellB), cell("47.0%", s_cellC), cell("flat YoY", s_cellC), cell("\u2014", s_cellC)],
    [cell("Systemwide sales", s_cell), cell("$37.0 bn", s_cellR), cell("+5% (+4% cc)", s_cellR), cell("\u2014", s_cellC)],
    [cell("Restaurants", s_cell), cell("46,028", s_cellR), cell("+1,915 YoY", s_cellR), cell("\u2014", s_cellC)],
]
story.append(styled_table(q, [52*mm, 34*mm, 38*mm, 56*mm]))
story.append(P("The quarter's real news was qualitative. Kempczinski: <i>\"We don't have a strategy problem. We simply didn't execute at the "
               "level we needed to.\"</i> Three admitted failures: inconsistent Everyday Affordable Price execution, crews overwhelmed by too "
               "many simultaneous deployments (slower service, lower satisfaction), and underwhelming marketing (June FIFA campaign). The CFO "
               "cut the full-year FX tailwind to $0.15/share and flagged a \"challenging\" China backdrop. The 50,000-restaurant target was "
               "pushed from 2027 to 2028.", s_body))

story.append(P("Balance sheet, cash flow &amp; capital returns", s_h2))
for b in [
    "<b>Leverage is elevated but investment-grade and stable.</b> Long-term debt $40.0 bn at 12/31/25 ($38.4 bn a year earlier); cash $0.8 bn \u2192 net debt ~$39.2 bn. Company-presented Debt/EBITDA improved from 4.1\u00d7 (2020) to <b>2.7\u00d7 (2024)</b>. Ratings: Moody's Baa1 / S&amp;P BBB+, both stable.",
    "<b>Negative book equity is a feature, not a bug.</b> Shareholders' deficit was $(1.79) bn at 12/31/25 (from $(3.80) bn in 2024), driven by decades of buybacks exceeding retained earnings. P/B and D/E are meaningless here \u2014 judge the balance sheet on cash flow coverage, which is ample ($10.6 bn of operating cash flow in 2025 vs. $3.4 bn capex).",
    "<b>Capital returns are the quiet compounding engine.</b> $7.1 bn returned in 2025 (dividends + buybacks); $3.9 bn in H1 2026 including $1.25 bn of buybacks. The share count has been ground down for decades, adding ~2 points a year to EPS growth.",
    "<b>The dividend is aristocratic.</b> $1.93/quarter declared September 17 (+4%) \u2192 <b>$7.72 annualized, 3.26% yield</b> \u2014 the <b>50th consecutive annual increase</b> (Dividend King; fewer than 60 U.S. companies qualify). 10-year dividend CAGR 7.65%; payout ratio ~56%. At the current price the yield is the highest in 6+ years.",
    "<b>Returns on capital are elite.</b> ROIC ~27\u201328%, stable over five years even as the capital base grew ~65% \u2014 the signature of a wide-moat compounder.",
]:
    story.append(B(b))

# ============ 4. GROWTH OUTLOOK & PROJECTIONS ============
story.append(P("4 &nbsp; Growth Outlook &amp; Forward Projections", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("We model revenue compounding at ~5\u20136% (2025\u201330) with operating margins expanding from 46% toward the low-50s as NEXT "
               "efficiency gains land and G&amp;A leverage kicks in. Our 2026\u201327 estimates anchor to consensus ($12.93 / $13.89 EPS); the "
               "out-year ramp reflects the Investor Day margin framework. EPS grows faster than revenue on buybacks (~2%/yr share reduction).", s_body))
proj = [
    [cell("$ mn", s_theadL), cell("2025A", s_thead), cell("2026E", s_thead), cell("2027E", s_thead), cell("2028E", s_thead), cell("2029E", s_thead), cell("2030E", s_thead)],
    [cell("Revenue", s_cellB), cell("26,885", s_cellR), cell("28,150", s_cellR), cell("29,600", s_cellR), cell("31,200", s_cellR), cell("32,900", s_cellR), cell("34,700", s_cellR)],
    [cell("Growth", s_cell), cell("4%", s_cellR), cell("5%", s_cellR), cell("5%", s_cellR), cell("5%", s_cellR), cell("5%", s_cellR), cell("5%", s_cellR)],
    [cell("Operating margin", s_cell), cell("46.1%", s_cellR), cell("46.5%", s_cellR), cell("47.5%", s_cellR), cell("49.0%", s_cellR), cell("50.5%", s_cellR), cell("52.0%", s_cellR)],
    [cell("Adj. diluted EPS", s_cellB), cell("$12.20", s_cellR), cell("$12.93", s_cellR), cell("$13.89", s_cellR), cell("$15.10", s_cellR), cell("$16.40", s_cellR), cell("$17.85", s_cellR)],
    [cell("EPS growth", s_cell), cell("+4%", s_cellR), cell("+6%", s_cellR), cell("+7%", s_cellR), cell("+9%", s_cellR), cell("+9%", s_cellR), cell("+9%", s_cellR)],
    [cell("Free cash flow", s_cell), cell("7,200", s_cellR), cell("7,600", s_cellR), cell("8,100", s_cellR), cell("8,700", s_cellR), cell("9,300", s_cellR), cell("9,900", s_cellR)],
    [cell("Dividend / share", s_cell), cell("$7.17", s_cellR), cell("$7.72", s_cellR), cell("$8.20", s_cellR), cell("$8.75", s_cellR), cell("$9.35", s_cellR), cell("$10.00", s_cellR)],
]
story.append(styled_table(proj, [30*mm, 25*mm, 25*mm, 25*mm, 25*mm, 25*mm, 25*mm]))
story.append(P("2026E/2027E revenue and EPS per Street consensus (Zacks/Yahoo); 2028E+ and margins are author estimates calibrated to the 2030 "
               "Investor Day targets (low-to-mid-50% operating margin, mid-to-high-80% FCF conversion). Dividend path assumes continued "
               "mid-single-digit raises.", s_small))

d2 = Drawing(430, 190)
d2.add(String(215, 178, "Projected Revenue ($ bn) and Operating Margin Path (2025A\u20132030E)", fontName="Helvetica-Bold", fontSize=10, textAnchor="middle", fillColor=NAVY))
bc2 = VerticalBarChart(); bc2.x = 45; bc2.y = 30; bc2.height = 120; bc2.width = 340
bc2.data = [[26.9, 28.2, 29.6, 31.2, 32.9, 34.7]]
bc2.strokeColor = None; bc2.bars[0].fillColor = NAVY; bc2.barLabels.nudge = 8; bc2.barLabelFormat = "%.1f"
bc2.categoryAxis.categoryNames = ["2025A", "2026E", "2027E", "2028E", "2029E", "2030E"]
bc2.valueAxis.valueMin = 0; bc2.valueAxis.valueMax = 36; bc2.valueAxis.valueStep = 9
bc2.valueAxis.labels.fontSize = 7; bc2.categoryAxis.labels.fontSize = 8
d2.add(bc2)
d2.add(String(215, 12, "Op. margin: 46.1% \u2192 46.5% \u2192 47.5% \u2192 49.0% \u2192 50.5% \u2192 52.0%  (2030 target: low-to-mid 50%)",
             fontName="Helvetica-Oblique", fontSize=8, textAnchor="middle", fillColor=DGRAY))
story.append(d2)
story.append(Spacer(1, 2*mm))

story.append(P("Growth bridges (2026\u20132030)", s_h2))
for b in [
    "<b>Traffic recovery in the U.S. (~35% of growth).</b> The highest-leverage, least-certain driver. Anderson's value reset + \"Make It Golden\" must turn negative guest counts positive. Every 1 point of U.S. comp is worth roughly $130\u2013140 mn of high-margin franchised revenue.",
    "<b>Unit expansion (~30%).</b> ~2,600 gross openings in 2026; new units contributing ~2.5% to systemwide sales growth in 2027 (~2% by 2030); 50,000 restaurants by 2028. Development is overwhelmingly franchised \u2014 capital-light for McDonald's.",
    "<b>Chicken and beverage share gains (~20%).</b> The +1.5 pp category-share targets attack the two fastest-growing QSR occasions. Beverages carry the highest margins in the building and skew to afternoon/daypart expansion (over half of new beverage traffic arrives after lunch).",
    "<b>Digital, delivery and personalization (~15%).</b> 220M loyalty members and a unified data lake feeding AI-driven offers; delivery is a ~$20 bn systemwide business with a goal of routing 30% through the company's own app by end-2027 (lower aggregator fees, richer data).",
]:
    story.append(B(b))

# ============ 5. MOAT ============
story.append(P("5 &nbsp; Moat Assessment", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("McDonald's moat is <b>wide</b> \u2014 among the strongest in consumer \u2014 but it is a moat of scale and system, not of "
               "product. We score each pillar:", s_body))
moat = [
    [cell("Moat pillar", s_theadL), cell("Strength", s_thead), cell("Evidence", s_thead)],
    [cell("Brand", s_cellB), cell("Very strong", s_cellC), cell("World's #1 restaurant brand at $42.6 bn brand value (Brand Finance 2026), ahead of Starbucks ($37 bn) and KFC ($16.5 bn); 17 menu brands each generating $1 bn+ in annual sales.", s_cell)],
    [cell("Scale / purchasing", s_cellB), cell("Very strong", s_cellC), cell("~670M lbs of U.S. beef annually; unmatched supplier leverage; $139 bn of systemwide sales fund marketing no rival can match.", s_cell)],
    [cell("Real estate", s_cellB), cell("Strong", s_cellC), cell("$28.2 bn net property &amp; equipment; ownership of land/buildings leased to franchisees = high-margin rental income plus site control.", s_cell)],
    [cell("Franchise system", s_cellB), cell("Very strong", s_cellC), cell("95% franchised \u2192 46% operating margins, 27%+ ROIC, earnings insulated from store-level labor/food volatility; franchisee sunk capital makes defection uneconomic.", s_cell)],
    [cell("Digital ecosystem", s_cellB), cell("Moderate\u2013Strong", s_cellC), cell("220M loyalty members, $40B+ loyalty sales, unified global data lake; personalization and the retail-media pilot are emerging advantages.", s_cell)],
    [cell("Switching costs", s_cellB), cell("Weak", s_cellC), cell("Consumers multi-home across QSR; the moat is on the franchisee side (long leases, sunk remodel capital), not the consumer side.", s_cell)],
    [cell("Cost advantage durability", s_cellB), cell("Moderate", s_cellC), cell("Scale purchasing is real but beef inflation and franchisee cost pressure are currently testing it; efficiency gains (ArchIQ, 250 bps) are the offset.", s_cell)],
]
story.append(styled_table(moat, [36*mm, 26*mm, 118*mm]))
story.append(P("Net: a <b>wide, scale-based moat with a demand-side soft spot</b>. Nobody can replicate the system; the risk is that value-conscious "
               "consumers temporarily rent their loyalty to whoever prices sharpest \u2014 which is exactly what Burger King and Taco Bell did in "
               "Q2. Moats don't prevent traffic quarters; they ensure the traffic comes back.", s_body))

# ============ 6. COMPETITION ============
story.append(P("6 &nbsp; Competitive Landscape", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Global QSR is a scale game McDonald's invented \u2014 and in Q2 2026, two scaled rivals out-executed it on the one dimension that "
               "currently matters: <b>value</b>. The competitive picture is a barbell: burger/QSR peers attacking on price, and fast-casual "
               "players attacking on quality perception.", s_body))
comp = [
    [cell("Competitor", s_theadL), cell("Scale", s_thead), cell("Q2'26 read", s_thead), cell("Threat assessment", s_thead)],
    [cell("Restaurant Brands (QSR)\nBurger King / Popeyes / Tim Hortons", s_cellB), cell("~31K units", s_cellC), cell("Global comp +3.8%;\nBK U.S. +8.5%;\nPopeyes \u20135.1%", s_cellC), cell("<b>The sharpest near-term threat.</b> BK's 2-for-$5 / 3-for-$7 value crushed MCD's +0.8% U.S. comp. Execution gap, not brand gap \u2014 which cuts both ways.", s_cell)],
    [cell("Yum! Brands (YUM)\nTaco Bell / KFC / Pizza Hut", s_cellB), cell("57K units", s_cellC), cell("Taco Bell SSS +7%;\nsystem sales +8%", s_cellC), cell("Taco Bell is the best-run QSR concept in America right now; beverage pilots (Live M\u00e1s Caf\u00e9, +18% checks) attack MCD's beverage push directly.", s_cell)],
    [cell("Wendy's (WEN)", s_cell), cell("~7K units", s_cellC), cell("Deep value: 9.7\u00d7 '26E P/E", s_cellC), cell("Direct burger rival but sub-scale and struggling; trades at half MCD's multiple for a reason. Not the share-taker.", s_cell)],
    [cell("Chipotle (CMG)", s_cell), cell("~3.7K units", s_cellC), cell("~30\u00d7 P/E", s_cellC), cell("Fast-casual quality halo at a growth multiple; competes for lunch/dinner occasions but at 2\u00d7 the price point. Different customer mission.", s_cell)],
    [cell("Starbucks (SBUX)", s_cell), cell("~40K stores", s_cellC), cell("Breakfast/beverage rival", s_cellC), cell("The beverage-share battle (+1.5 pp target) runs straight through Starbucks' morning daypart; MCD's price advantage is its weapon.", s_cell)],
    [cell("Domino's (DPZ)", s_cell), cell("~21K stores", s_cellC), cell("16.2\u00d7 P/E", s_cellC), cell("Best-in-class QSR operator on delivery/tech; a valuation comp more than a direct traffic rival.", s_cell)],
]
story.append(styled_table(comp, [42*mm, 24*mm, 30*mm, 84*mm]))
story.append(P("The scoreboard that matters right now is U.S. value execution: BK +8.5% and Taco Bell +7% vs. MCD +0.8% is the entire bear case in "
               "one line. The bull case is that this is a <i>self-inflicted, fixable</i> gap \u2014 60\u201365% EDAP compliance is a management "
               "failure, not a structural defeat \u2014 and Anderson was hired specifically to close it.", s_body))

story.append(P("Relative valuation \u2014 MCD screens cheap against its own peer set", s_h2))
rel = [
    [cell("Company", s_theadL), cell("P/E (TTM / '26E)", s_thead), cell("EV/EBITDA ('26E)", s_thead), cell("Op. margin", s_thead), cell("Dividend yield", s_thead)],
    [cell("McDonald's", s_cellB), cell("19.1\u00d7 / ~18\u00d7", s_cellC), cell("~15\u00d7", s_cellC), cell("46%", s_cellC), cell("3.26%", s_cellC)],
    [cell("Yum! Brands", s_cell), cell("17.4\u00d7 / 21.6\u00d7", s_cellC), cell("16.4\u00d7", s_cellC), cell("~36%", s_cellC), cell("~2.0%", s_cellC)],
    [cell("Restaurant Brands", s_cell), cell("~18.5\u00d7 / 16.9\u00d7", s_cellC), cell("13.8\u00d7", s_cellC), cell("~38%", s_cellC), cell("~3.4%", s_cellC)],
    [cell("Domino's", s_cell), cell("16.2\u00d7 / 21.1\u00d7", s_cellC), cell("16.8\u00d7", s_cellC), cell("~18%", s_cellC), cell("~1.6%", s_cellC)],
    [cell("Wendy's", s_cell), cell("9.7\u00d7 ('26E)", s_cellC), cell("8.2\u00d7", s_cellC), cell("~16%", s_cellC), cell("~5%+", s_cellC)],
    [cell("Chipotle", s_cell), cell("~30\u00d7", s_cellC), cell("\u2014", s_cellC), cell("~17%", s_cellC), cell("nil", s_cellC)],
]
story.append(styled_table(rel, [36*mm, 32*mm, 30*mm, 28*mm, 28*mm]))
story.append(P("MCD now trades at a discount to Yum! and Domino's on earnings <i>despite</i> the highest margins, the highest ROIC, and the only "
               "Dividend King payout in the group. That relative mispricing is the core of the valuation case in Section 9.", s_body))

# ============ 7. PRODUCT EVALUATION ============
story.append(P("7 &nbsp; Product Evaluation", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("McDonald's menu strategy is <b>\"fewer, bigger, better\"</b>: 17 billion-dollar brands, ruthless SKU discipline, and growth "
               "concentrated in two vectors \u2014 chicken and beverages \u2014 where the company is under-shared relative to its beef dominance. "
               "We grade each platform on scale, economics, and strategic fit:", s_body))
prod = [
    [cell("Platform", s_theadL), cell("Scale / status", s_thead), cell("Economics &amp; fit", s_thead), cell("Grade", s_thead)],
    [cell("Beef (Big Mac, Quarter Pounder, burgers)", s_cellB), cell("Core; global beef share leader", s_cell), cell("Highest brand equity, but beef is ~38% of U.S. food-and-paper and inflation is >10%. Strategy: <i>hold</i> share, not chase it.", s_cell), cell("<b>A\u2013</b>", s_cellC)],
    [cell("Chicken (McCrispy, McNuggets, wraps)", s_cellB), cell("McCrispy in 70+ markets; hand-breaded expanding '27", s_cell), cell("Lower input-cost volatility than beef; the +1.5 pp share target attacks Popeyes/Chick-fil-A's turf. Highest menu priority.", s_cell), cell("<b>A\u2013</b>", s_cellC)],
    [cell("Beverages (McCaf\u00e9, new platform)", s_cellB), cell("New platform launched May '26; beating plan", s_cell), cell("Best margins in the building; checks ~50% above average; afternoon daypart expansion. CosMc's learnings folded in.", s_cell), cell("<b>A</b>", s_cellC)],
    [cell("Breakfast", s_cellB), cell("U.S. daypart leader", s_cell), cell("Defensible ritual occasion; Egg McMuffin equity is durable; GLP-1 protein items (egg bites) extend it.", s_cell), cell("<b>B+</b>", s_cellC)],
    [cell("McValue / EDAP (value platform)", s_cellB), cell("National; execution failed in Q2", s_cell), cell("Only 60\u201365% pricing compliance killed the value signal. The <i>platform</i> is right; the <i>execution</i> was F-grade. Anderson's fix is the #1 near-term variable.", s_cell), cell("<b>C+ \u2192 ?</b>", s_cellC)],
    [cell("Digital / Loyalty / Delivery", s_cellB), cell("220M members; $40B loyalty sales; ~$20B delivery", s_cell), cell("Data + personalization + owned-app delivery = structural check and frequency lift. Retail-media pilot is free optionality.", s_cell), cell("<b>A\u2013</b>", s_cellC)],
]
story.append(styled_table(prod, [44*mm, 44*mm, 62*mm, 30*mm]))
story.append(P("Product thesis in one line: the core (beef, breakfast) defends, chicken and beverages attack, value is being repaired, and digital "
               "is the connective tissue \u2014 a coherent portfolio with exactly one failing grade, and it is the one management just replaced "
               "the leadership over.", s_body))

# ============ 8. VALUATION ============
story.append(P("8 &nbsp; Valuation \u2014 Four Models, One Fair Price", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("We triangulate fair value with four independent approaches: (1) a <b>discounted cash flow</b> on free cash flow (primary, 40% "
               "weight \u2014 appropriate for a cash-compounding franchise model); (2) <b>forward P/E</b> vs. history and peers (30%); "
               "(3) <b>EV/EBITDA</b> (20%); and (4) a <b>Gordon dividend discount model</b> (10% \u2014 a Dividend King deserves a DDM cross-check). "
               "All models use the September 25, 2026 close of <b>$236.50</b> as the reference price.", s_body))

story.append(P("8.1 &nbsp; Discounted cash flow (primary)", s_h2))
story.append(P("We discount projected free cash flow (2026E $7.6 bn \u2192 2030E $9.9 bn, calibrated to the mid-to-high-80% FCF-conversion "
               "target) at a 6.5% WACC \u2014 itself conservative against the 5.8% CAPM-implied rate (beta 0.45, 4% risk-free, 5% equity risk "
               "premium) \u2014 with 3% terminal growth, and subtract $39.2 bn of net debt across ~710 mn diluted shares.", s_body))
dcf = [
    [cell("WACC \u2192", s_theadL), cell("g = 2%", s_thead), cell("g = 3% (base)", s_thead), cell("g = 4%", s_thead)],
    [cell("6.0%", s_cell), cell("$301", s_cellR), cell("$354", s_cellR), cell("$427", s_cellR)],
    [cell("6.5% (base)", s_cellB), cell("$256", s_cellR), cell("<b>$295</b>", s_cellBR), cell("$347", s_cellR)],
    [cell("7.0%", s_cell), cell("$221", s_cellR), cell("$251", s_cellR), cell("$289", s_cellR)],
    [cell("7.5%", s_cell), cell("$193", s_cellR), cell("$216", s_cellR), cell("$245", s_cellR)],
    [cell("8.0%", s_cell), cell("$170", s_cellR), cell("$189", s_cellR), cell("$212", s_cellR)],
]
story.append(styled_table(dcf, [36*mm, 36*mm, 42*mm, 36*mm]))
story.append(P("Base DCF: enterprise value $248.6 bn (of which $291.3 bn is terminal value \u2014 normal for a perpetual compounder), "
               "less $39.2 bn net debt \u2192 equity $209.4 bn \u2192 <b>$295/share</b>. Note the sensitivity: even at a punitive 7.5% WACC the "
               "model yields $216 \u2014 only 9% below today's price \u2014 which frames the downside.", s_body))

d4 = Drawing(430, 165)
d4.add(String(215, 155, "DCF Value per Share Across WACC (g = 3%) vs. Current Price", fontName="Helvetica-Bold", fontSize=10, textAnchor="middle", fillColor=NAVY))
vals = [("Current $237", 236.5, DGRAY), ("8.0% $189", 189, RED), ("7.0% $251", 251, GOLD), ("6.5% $295", 295, ACCENT), ("6.0% $354", 354, NAVY)]
x = 40
for name, v, col in vals:
    h = v * 0.36
    d4.add(Rect(x, 30, 60, h, fillColor=col, strokeColor=None))
    d4.add(String(x + 30, 30 + h + 6, f"${v:.0f}", fontName="Helvetica-Bold", fontSize=9, textAnchor="middle", fillColor=col))
    d4.add(String(x + 30, 18, name.split(" ")[0], fontName="Helvetica", fontSize=8, textAnchor="middle", fillColor=DGRAY))
    x += 78
story.append(d4)

story.append(P("8.2 &nbsp; Forward P/E", s_h2))
story.append(P("On 2027E consensus EPS of $13.89: McDonald's five-year average forward multiple is ~24\u00d7; franchised QSR peers (Yum!, Domino's) "
               "trade ~21\u201322\u00d7 2026E. We use <b>22\u00d7</b> \u2014 a discount to MCD's own history reflecting near-term execution risk, "
               "but a premium to peers reflecting superior margins and ROIC \u2192 <b>$306/share</b> (range: 20\u00d7 \u2192 $278; 24\u00d7 \u2192 $333).", s_body))

story.append(P("8.3 &nbsp; EV/EBITDA", s_h2))
story.append(P("2027E EBITDA of ~$15.9 bn (~47% operating margin on $29.6 bn revenue, plus ~$2 bn D&amp;A). Peers: Yum! 16.4\u00d7, Domino's 16.8\u00d7, "
               "Restaurant Brands 13.8\u00d7; MCD's own five-year average is 18\u201319\u00d7. At a peer-line <b>16.5\u00d7</b> \u2192 EV $262 bn, "
               "less $39.2 bn net debt \u2192 <b>$314/share</b> (range: 15\u00d7 \u2192 $281; 18\u00d7 \u2192 $348).", s_body))

story.append(P("8.4 &nbsp; Gordon dividend discount model", s_h2))
story.append(P("With a $7.72 annualized dividend, 6% perpetual dividend growth (vs. 7.65% ten-year CAGR and 50 years of raises), and a 9% required "
               "return: $7.72 \u00d7 1.06 / (0.09 \u2212 0.06) = <b>$273/share</b> (range $234\u2013$329 across 8.5\u20139.5% required returns). "
               "The DDM is the most conservative of the four \u2014 a useful anchor.", s_body))

story.append(P("8.5 &nbsp; Blended fair value", s_h2))
blend = [
    [cell("Model", s_theadL), cell("Weight", s_thead), cell("Fair value / share", s_thead), cell("Implied upside", s_thead)],
    [cell("DCF (WACC 6.5%, g 3%)", s_cellB), cell("40%", s_cellC), cell("$295", s_cellR), cell("+25%", s_cellR)],
    [cell("Forward P/E (22\u00d7 2027E)", s_cellB), cell("30%", s_cellC), cell("$306", s_cellR), cell("+29%", s_cellR)],
    [cell("EV/EBITDA (16.5\u00d7 2027E)", s_cellB), cell("20%", s_cellC), cell("$314", s_cellR), cell("+33%", s_cellR)],
    [cell("Dividend discount (9% / 6%)", s_cell), cell("10%", s_cellC), cell("$273", s_cellR), cell("+15%", s_cellR)],
    [cell("<b>Blended fair value \u2192 12-mo. target</b>", s_cellB), cell("100%", s_cellC), cell("<b>$300</b>", s_cellBR), cell("<b>+27%</b>", s_cellBR)],
]
story.append(styled_table(blend, [62*mm, 24*mm, 44*mm, 44*mm]))
story.append(P("Four independent models converge on <b>~$295\u2013$315</b>; the $300 blend sits at the <i>low end</i> of the Street's $300\u2013$321 "
               "consensus range \u2014 we are deliberately a touch more conservative than the average analyst on execution timing. Every model "
               "implies double-digit upside from $236.50.", s_body))

story.append(P("8.6 &nbsp; Scenario analysis", s_h2))
scen = [
    [cell("Scenario", s_theadL), cell("Key assumptions", s_thead), cell("Target", s_thead)],
    [cell("Bull \u2014 $365", s_cellB), cell("NEXT executes; U.S. traffic recovers by mid-'27; comps 3\u20134%; op margin hits 52% by 2030; multiple re-rates to 25\u00d7 on $14.60 bull-case 2027 EPS.", s_cell), cell("<b>+54%</b>", s_cellBR)],
    [cell("Base \u2014 $300", s_cellB), cell("Gradual traffic stabilization; margins expand per Investor Day glide path; 22\u00d7 multiple on $13.89 consensus 2027 EPS.", s_cell), cell("<b>+27%</b>", s_cellBR)],
    [cell("Bear \u2014 $212", s_cellB), cell("U.S. traffic stays negative; beef inflation persists; franchisee resistance delays NEXT; EPS stalls ~$12.50; multiple de-rates to 17\u00d7.", s_cell), cell("<b>\u201310%</b>", s_cellBR)],
]
story.append(styled_table(scen, [30*mm, 110*mm, 40*mm]))
story.append(P("Probability-weighted (50% base / 25% bull / 25% bear): 0.5\u00d7$300 + 0.25\u00d7$365 + 0.25\u00d7$212 = <b>$294 \u2192 $300 target</b> "
               "(rounded). The asymmetry is attractive: $64 of upside to base vs. $25 of downside to bear.", s_body))

story.append(P("8.7 &nbsp; What the Street thinks", s_h2))
story.append(P("Consensus is <b>Moderate Buy</b> (1 Strong Buy / 17 Buy / 11 Hold) with an average target of <b>~$300\u2013$321</b> depending on "
               "source \u2014 implying ~27\u201336% upside even at the low end. September saw broad target cuts (TD Cowen to $270 Hold; RBC $285 "
               "Sector Perform; BTIG $295 Buy; UBS $260; Morgan Stanley $308 Equal Weight; Deutsche $300 Buy; Citi $310 Buy; Jefferies $325 Buy; "
               "Argus $310 Buy; Bernstein $295 Market Perform; Guggenheim $290 Neutral; Baird $250 Neutral; Seaport initiated at Neutral) \u2014 "
               "but <i>no</i> Sell ratings. Our $300 sits at the cautious end of consensus: we agree on the destination, we are simply underwriting "
               "a slower traffic recovery than the optimists.", s_body))

# ============ 9. RISKS & CATALYSTS ============
story.append(P("9 &nbsp; Risks, Catalysts &amp; What to Watch", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
rc = [
    [cell("Risk / catalyst", s_theadL), cell("Direction", s_thead), cell("Timing", s_thead), cell("Why it matters", s_thead)],
    [cell("\"Make It Golden\" launch (Oct 5)", s_cellB), cell("Catalyst \u2191", s_cellC), cell("Q4'26", s_cellC), cell("First measurable read on service-speed and satisfaction recovery; early traffic data in Q4.", s_cell)],
    [cell("Q3'26 earnings", s_cellB), cell("Catalyst \u2191\u2193", s_cellC), cell("~Oct 22", s_cellC), cell("U.S. comp and guest-count trajectory under Anderson is the single most important print of the year.", s_cell)],
    [cell("U.S. value reset traction", s_cell), cell("Binary", s_cellC), cell("H1'27", s_cellC), cell("EDAP compliance back above 90% + positive guest counts = thesis confirmed; continued share loss to BK/Taco Bell = thesis broken.", s_cell)],
    [cell("Beef inflation / herd rebuild", s_cell), cell("Risk \u2193", s_cellC), cell("2026\u201328", s_cellC), cell(">10% U.S. beef inflation in 2026; herd smallest since 1951; no rebuild before 2028. Caps franchisee margins.", s_cell)],
    [cell("Franchisee adoption of NEXT", s_cell), cell("Risk \u2193", s_cellC), cell("2027\u201330", s_cellC), cell("$800K/store ask on strained balance sheets; 95% franchised means McDonald's persuades, not commands.", s_cell)],
    [cell("GLP-1 demand drag", s_cell), cell("Risk \u2193", s_cellC), cell("Structural", s_cellC), cell("~30M U.S. users; Redburn est. up to 28M fewer visits/yr. Protein-menu pivot is the mitigant to watch.", s_cell)],
    [cell("Tariffs / input costs", s_cell), cell("Risk \u2193", s_cellC), cell("Ongoing", s_cellC), cell("Imported inputs and equipment cost pressure; broad inflation \"sticky... around the world\" (Kempczinski).", s_cell)],
    [cell("China / IDLM softness + FX", s_cell), cell("Risk \u2193", s_cellC), cell("2026\u201327", s_cellC), cell("Negative China comps; FY26 FX tailwind cut to $0.15/share.", s_cell)],
    [cell("Investor Day target delivery", s_cell), cell("Catalyst \u2191", s_cellC), cell("2027\u201330", s_cellC), cell("250 bps efficiency and low-50s margins are 2027\u201328 stories; early franchisee ROI prints de-risk the $8.5 bn commitment.", s_cell)],
]
story.append(styled_table(rc, [46*mm, 22*mm, 18*mm, 94*mm]))

# ============ 10. RECOMMENDATION ============
story.append(P("10 &nbsp; Recommendation", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("We rate McDonald's a <b>BUY</b> with a <b>$300.00</b> 12-month price target, implying ~27% upside from $236.50. "
               "This is the rare setup where <b>price and quality have diverged</b>: a wide-moat, 46%-margin, 27%-ROIC franchise compounder "
               "with a 50-year dividend-growth streak is trading at a 52-week low, at 19\u00d7 earnings \u2014 cheaper than Yum! and Domino's "
               "on earnings despite superior economics \u2014 because of a fixable U.S. execution failure and market skepticism toward a "
               "well-quantified investment plan. Four independent valuation models converge on $295\u2013$315 of fair value; the $300 target "
               "sits at the cautious end of the Street's $300\u2013$321 consensus.", s_body))
story.append(P("The investment case rests on three beliefs: (1) the traffic problem is <i>executional</i>, not structural \u2014 new U.S. leadership, "
               "a repaired value platform, and the October 5 \"Make It Golden\" relaunch address the named causes directly; (2) the NEXT strategy's "
               "2030 targets (low-to-mid-50% margins, 250 bps efficiency, mid-to-high-80% FCF conversion) are achievable because they are "
               "substantially within management's control via technology and G&amp;A leverage; and (3) at 3.26% yield with a 56% payout ratio, "
               "shareholders are paid handsomely to wait for the recovery.", s_body))
story.append(P("Position sizing guidance: this is a <b>medium-risk BUY</b> \u2014 a core defensive-compounder position, not a speculation. "
               "The dividend funds patience, but size for the possibility that traffic recovery slips into mid-2027. Key invalidation: U.S. "
               "guest counts still negative by Q2 2027 combined with continued share loss to Burger King/Taco Bell, or franchisee revolt that "
               "forces a material cut to the NEXT investment cadence. Conversely, two consecutive quarters of positive U.S. traffic would likely "
               "re-rate the stock toward the $340+ pre-selloff range quickly, given how depressed expectations are.", s_body))
story.append(Spacer(1, 2*mm))
story.append(P("Analyst certification &amp; disclosures: This report is an independent research-style analysis prepared for informational purposes "
               "only. It is not investment advice, a recommendation to buy/sell any security, or an offer to transact. Financial figures are sourced "
               "from McDonald's SEC filings (10-K FY2025, 10-Qs), earnings releases and calls, September 23, 2026 Investor Day materials, and "
               "reputable financial press; projections and the $300.00 price target are the author's estimates and involve uncertainty. "
               "Past performance does not predict future results. Investors should conduct their own due diligence and consult a licensed advisor.",
               s_small))
story.append(Spacer(1, 2*mm))
story.append(P("Sources: McDonald's 2025 10-K and Q1/Q2 2026 10-Qs (SEC EDGAR); Q2 2026 earnings release (PR Newswire, Aug 4, 2026); "
               "Investor Day press release (McDonald's MediaRoom, Sep 23, 2026); Dow Jones Newswires; AP; Reuters (RBI Q2 2026); "
               "Brand Finance 2026; Zacks; MarketBeat; Finnhub market data. Dated September 26, 2026.", s_small))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=18*mm,
                        title="McDonald's (MCD) Equity Research Note", author="Muse")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("WROTE", OUT)
