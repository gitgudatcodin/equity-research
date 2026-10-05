#!/usr/bin/env python3
"""Build the DraftKings equity research note PDF."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, KeepTogether, HRFlowable)
from reportlab.graphics.shapes import Drawing, Line, String, Rect
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.lib import colors

OUT = "/home/hatch/workspace/your_files/draftkings-equity-research/draftkings-equity-research-note.pdf"

NAVY = HexColor("#0F2A44"); ACCENT = HexColor("#0E7C3E"); GOLD = HexColor("#C9A227")
LGRAY = HexColor("#F2F4F7"); MGRAY = HexColor("#D9DEE5"); DGRAY = HexColor("#5A6472")
RED = HexColor("#B42318"); BLUE = HexColor("#1D4ED8")

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
    style = [
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
    ]
    t.setStyle(TableStyle(style))
    return t

def P(txt, style=s_body): return Paragraph(txt, style)
def B(txt): return Paragraph(f"<b>{txt}</b>", s_bull)
def cell(txt, st=s_cell): return Paragraph(txt, st)

story = []
W, H = A4

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7); canvas.setFillColor(DGRAY)
    canvas.drawString(18*mm, 12*mm, "DraftKings Inc. (NASDAQ: DKNG)  \u2014  Equity Research Note  \u2014  September 2026")
    canvas.drawRightString(W - 18*mm, 12*mm, f"Page {doc.page}")
    canvas.setStrokeColor(MGRAY); canvas.setLineWidth(0.5)
    canvas.line(18*mm, 14.5*mm, W - 18*mm, 14.5*mm)
    canvas.restoreState()

# ============ COVER ============
story.append(Spacer(1, 28*mm))
story.append(P("DRAFTKINGS INC.", ParagraphStyle("x", parent=s_sub, fontName="Helvetica-Bold", fontSize=13, textColor=ACCENT, spaceAfter=2)))
story.append(P("The House Always Wins?<br/>Profitability Inflection Meets<br/>Prediction-Market Disruption", s_title))
story.append(Spacer(1, 4*mm))
story.append(P("Equity Research Note  \u00b7  Consumer Discretionary \u2014 Online Gaming  \u00b7  September 19, 2026", s_sub))
story.append(Spacer(1, 8*mm))

rating_data = [
    [cell("Recommendation", s_theadL), cell("12-Mo. Price Target", s_thead), cell("Current Price", s_thead), cell("Implied Upside", s_thead), cell("Risk Rating", s_thead)],
    [Paragraph("<b><font color=\"#0E7C3E\" size=\"13\">BUY</font></b>", s_cellC),
     Paragraph("<b><font size=\"12\">$36.00</font></b>", s_cellC),
     Paragraph("<b>$21.75</b><br/><font size=\"7\" color=\"#5A6472\">Sep 19, 2026</font>", s_cellC),
     Paragraph("<b><font color=\"#0E7C3E\">+65%</font></b>", s_cellC),
     Paragraph("<b>High</b><br/><font size=\"7\" color=\"#5A6472\">Beta 1.68</font>", s_cellC)],
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
    ["Market cap", "$10.9 bn", "Shares out.", "~496.5 mn"],
    ["Enterprise value", "~$11.9 bn", "52-week range", "$20.46 \u2013 $44.22"],
    ["Net debt", "~$1.0 bn", "YTD / 1-yr return", "-36.9% / -49.9%"],
    ["2026E revenue (guide)", "$6.5 \u2013 $6.9 bn", "2026E adj. EBITDA (guide)", "$700 \u2013 $900 mn"],
    ["FY2025 revenue", "$6.06 bn (+27%)", "FY2025 adj. EBITDA", "$620 mn (10.2%)"],
    ["Next catalyst", "Q3'26 earnings, ~Nov 5", "Analyst consensus", "Moderate Buy, PT ~$34.4"],
]
sd = [[cell(r[0], s_cellB), cell(r[1], s_cell), cell(r[2], s_cellB), cell(r[3], s_cell)] for r in snap]
st2 = styled_table([[cell("Snapshot", s_theadL), cell("", s_thead), cell("", s_thead), cell("", s_thead)]] + sd,
                   [38*mm, 38*mm, 38*mm, 56*mm], header_rows=1)
story.append(st2)
story.append(Spacer(1, 8*mm))
story.append(P("This note is an independent research-style analysis for informational purposes only and is not investment advice. "
               "Figures are drawn from DraftKings' SEC filings, earnings releases, and reputable financial press as of September 19, 2026. "
               "Projections are the author's estimates.", s_small))
story.append(PageBreak())

# ============ 1. EXECUTIVE SUMMARY ============
story.append(P("1 &nbsp; Executive Summary", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("DraftKings (DKNG) is the #2 online sportsbook and iGaming operator in the United States, trading at "
               "<b>$21.75 \u2014 within 6% of its 52-week low</b> and down ~50% over the past year. The selloff reflects a genuine strategic "
               "inflection point: the company's core sportsbook has just proven it can print money (first-ever GAAP profit in 2025, adjusted "
               "EBITDA tripling to $620 mn), while the market is repricing the business for a new competitive threat \u2014 federally regulated "
               "prediction markets (Kalshi, Polymarket) operating nationwide in states where DraftKings' sportsbook cannot legally exist.", s_body))
story.append(P("We rate DKNG a <b>BUY</b> with a <b>$36.00</b> 12-month price target (~65% upside). Our thesis: the profitability inflection is "
               "structural, not cyclical; the prediction-market threat is real but DraftKings has responded with its own federally regulated "
               "Predictions platform that is scaling explosively ($11 bn annualized volume by July 2026, up ~5x from April) and carries structurally "
               "higher margins; and the current price embeds an overly punitive bear case. That said, this is a <b>high-risk</b> name: quarterly "
               "earnings are hostage to sports outcomes, courts will decide the prediction-market endgame, and state tax pressure is a slow bleed.", s_body))

story.append(P("Investment thesis \u2014 why own it", s_h2))
for b in [
    "<b>The land-grab is over; the harvest has begun.</b> With online sports betting legal in 38 states plus D.C. and DraftKings live across ~53% of the U.S. population, the era of scorched-earth customer acquisition is ending. Cohort economics are visibly improving: Q4'25 average revenue per payer surged 43% to $139 on better hold and parlay mix, and management is guiding to a long-term adjusted EBITDA margin of <b>\u226530%</b> (vs. 10.2% in 2025).",
    "<b>Profitability is proven, not promised.</b> FY2025 delivered $6.06 bn revenue (+27%), $620 mn adjusted EBITDA (+242%), and the company's first full-year GAAP profit ($3.7 mn). Q1'26 added a second consecutive quarter of positive net income. The business model \u2014 high fixed-cost leverage on a growing handle base \u2014 is now demonstrably working.",
    "<b>Predictions is a free call option the market prices as a liability.</b> DraftKings Predictions (launched Dec 2025, built on the acquired CFTC-licensed Railbird exchange plus an in-house market-making desk) reaches nearly 100% of Americans \u2014 double the sportsbook footprint. Management cites <b>10\u201330 points of gross-margin advantage</b> over the sportsbook (no state gaming tax, lower promo intensity) and targets \"hundreds of millions\" in annual revenue within a few years. 2026 guidance <i>excludes</i> Predictions revenue while including its costs \u2014 i.e., guidance is understated by design.",
    "<b>Expectations have been reset to the floor.</b> February's guidance ($6.7 bn revenue midpoint vs. $7.3 bn consensus) plus Q2's hold-driven miss have crushed the stock 37% YTD. Street targets cluster at $28\u2013$40 with consensus ~$34.4; at $21.75 the bar for positive surprise is low heading into the seasonally strong NFL-driven second half.",
    "<b>Capital allocation has turned shareholder-friendly.</b> ~22.7 mn shares repurchased for ~$773 mn through mid-2026 (16 mn in FY2025 alone), and a 2026 refinancing ($700 mn Term B + $750 mn revolver) pushed maturities out and funded flexibility.",
]:
    story.append(B(b))

story.append(P("Key risks \u2014 why the market is scared", s_h2))
for b in [
    "<b>Prediction-market cannibalization / adverse court rulings.</b> Kalshi/Polymarket moved an estimated $44\u201363 bn in 2025 volume and now offer sports event contracts \u2014 including parlays \u2014 nationwide under CFTC licenses. If courts uphold federal preemption of state gambling law, DraftKings' state-by-state moat is permanently impaired; DraftKings itself faces lawsuits over its own Predictions platform.",
    "<b>Hold volatility makes quarterly earnings a coin flip.</b> Q2'26 revenue fell 5% despite record $13.1 bn handle because customers won (~$80 mn headwind from a Knicks title and bettor-friendly World Cup). Q3 hold was tracking ~7% vs. ~11.8% structural in September per Morgan Stanley. You are underwriting variance, not just growth.",
    "<b>State tax creep.</b> Illinois added a per-wager tax; New Jersey and Louisiana raised digital rates; Kansas headlines keep coming. Management's guidance assumes tax rates stay flat \u2014 a fragile assumption.",
    "<b>Execution risk on the pivot.</b> 2\u201315% headcount rightsizing, a Super App migration, and a prediction-market build-out are happening simultaneously. Costs are in guidance; revenues are not.",
]:
    story.append(B(b))

# ============ 2. COMPANY OVERVIEW ============
story.append(P("2 &nbsp; Company Overview \u2014 What DraftKings Is and What It Is Doing", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("DraftKings Inc., headquartered in Boston, MA (~5,500 employees), is a digital sports entertainment and gaming company. "
               "Founded in 2012 as a daily fantasy sports (DFS) operator, it went public in April 2020 via SPAC merger (Diamond Eagle), "
               "acquired its core technology stack through <b>SBTech</b> (2020), expanded into iGaming with <b>Golden Nugget Online Gaming</b> (2022), "
               "and added lottery distribution via <b>Jackpocket</b> (2024, ~$750 mn). The strategic arc is consistent: own the customer relationship "
               "across every legal form of U.S. online wagering, on proprietary technology.", s_body))
story.append(P("What the company is doing right now \u2014 the 2026 strategic pivot", s_h2))
for b in [
    "<b>Super App consolidation.</b> In 2026 DraftKings launched <b>DraftKings Sports &amp; Casino</b> nationwide, merging Sportsbook, Predictions, Casino (iGaming) and Lottery into one app with a single account and wallet, access tailored by jurisdiction. Phase one shipped ahead of March Madness. The goal is classic cross-sell: one acquired customer monetized across four verticals.",
    "<b>Prediction-market build-out.</b> DraftKings Predictions (Dec 2025) is the company's answer to Kalshi/Polymarket: federally regulated event contracts on sports (and eventually non-sports) available in all 50 states. The 2026 roadmap added the <b>Railbird</b> exchange acquisition and a proprietary <b>market-making division</b> to internalize trading economics. Management calls this \"the most exciting growth opportunity since PASPA\" (2018).",
    "<b>Efficiency mandate.</b> With the land-grab phase largely complete, management is rightsizing headcount by an estimated 2\u201315%, deploying AI across trading, marketing and support, and harvesting operating leverage \u2014 2026 guidance implies ~11% revenue growth but ~30% adjusted EBITDA growth at the midpoint.",
    "<b>Geographic expansion at the margin.</b> Missouri (Dec 2025) was \"one of the best state openings ever\"; Alberta, Canada launched in 2026, taking Canadian coverage to ~51% of the population. The next leg is iGaming legalization (only 5 states, ~11% of Americans) \u2014 the highest-margin white space in U.S. gaming.",
]:
    story.append(B(b))
story.append(P("At its March 2026 Investor Day, management framed the destination: a <b>$55\u201380 bn industry gross-revenue opportunity by 2030</b> "
               "(continued legalization + existing-state growth + Predictions), with DraftKings targeting a long-term adjusted EBITDA margin of "
               "<b>at least 30%</b>. The message: DraftKings intends to be a consolidator and margin-expander, not just a growth story.", s_body))

# ============ 3. FINANCIAL ANALYSIS ============
story.append(P("3 &nbsp; Financial Analysis", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("The P&amp;L tells a clean three-act story: hyper-growth at any cost (2020\u201323), the turn to operating leverage (2024), and the "
               "profitability inflection (2025\u201326E).", s_body))

fin = [
    [cell("$ mn", s_theadL), cell("2023", s_thead), cell("2024", s_thead), cell("2025", s_thead), cell("2026E*", s_thead)],
    [cell("Revenue", s_cellB), cell("3,665", s_cellR), cell("4,768", s_cellR), cell("6,055", s_cellR), cell("6,700", s_cellR)],
    [cell("YoY growth", s_cell), cell("+53%", s_cellR), cell("+30%", s_cellR), cell("+27%", s_cellR), cell("+11%", s_cellR)],
    [cell("Cost of revenue", s_cell), cell("(2,411)", s_cellR), cell("(2,985)", s_cellR), cell("(3,600)", s_cellR), cell("\u2014", s_cellC)],
    [cell("Gross margin", s_cell), cell("~34%", s_cellR), cell("~37%", s_cellR), cell("~41%", s_cellR), cell("\u2014", s_cellC)],
    [cell("Sales &amp; marketing", s_cell), cell("(1,184)", s_cellR), cell("(1,279)", s_cellR), cell("(1,400)", s_cellR), cell("\u2014", s_cellC)],
    [cell("Net income (GAAP)", s_cellB), cell("(802)", s_cellR), cell("(507)", s_cellR), cell("3.7", s_cellR), cell("\u2014", s_cellC)],
    [cell("Adjusted EBITDA", s_cellB), cell("(151)", s_cellR), cell("181", s_cellR), cell("620", s_cellR), cell("800", s_cellR)],
    [cell("Adj. EBITDA margin", s_cell), cell("n.m.", s_cellC), cell("3.8%", s_cellR), cell("10.2%", s_cellR), cell("11.9%", s_cellR)],
    [cell("Adj. diluted EPS", s_cell), cell("($0.41)", s_cellR), cell("$0.24", s_cellR), cell("$0.66", s_cellR), cell("~$0.49", s_cellR)],
]
story.append(styled_table(fin, [46*mm, 28*mm, 28*mm, 28*mm, 28*mm]))
story.append(P("*2026E at guidance midpoints; 2023 figures per 10-K. Sources: DraftKings 10-K (FY2025), Q1'26/Q2'26 shareholder letters.", s_small))

# Bar chart: revenue + adj EBITDA 2023-2026E
d = Drawing(430, 190)
d.add(String(215, 178, "Revenue vs. Adjusted EBITDA ($ mn)", fontName="Helvetica-Bold", fontSize=10, textAnchor="middle", fillColor=NAVY))
bc = VerticalBarChart(); bc.x = 45; bc.y = 30; bc.height = 120; bc.width = 340
bc.data = [[3665, 4768, 6055, 6700], [-151, 181, 620, 800]]
bc.strokeColor = None; bc.barLabels.nudge = 8; bc.barLabelFormat = "%d"
bc.bars[0].fillColor = NAVY; bc.bars[1].fillColor = ACCENT
bc.categoryAxis.labels.boxAnchor = "ne"; bc.categoryAxis.labels.angle = 0
bc.categoryAxis.categoryNames = ["2023", "2024", "2025", "2026E"]
bc.valueAxis.valueMin = -600; bc.valueAxis.valueMax = 7200; bc.valueAxis.valueStep = 1800
bc.valueAxis.labels.fontSize = 7; bc.categoryAxis.labels.fontSize = 8
d.add(bc)
for i, lab in enumerate(["Revenue", "Adj. EBITDA"]):
    d.add(Rect(300 + i*95, 12, 12, 8, fillColor=[NAVY, ACCENT][i], strokeColor=None))
    d.add(String(316 + i*95, 14, lab, fontName="Helvetica", fontSize=8, fillColor=DGRAY))
story.append(d)
story.append(Spacer(1, 2*mm))

story.append(P("Quarterly pulse \u2014 the last four quarters", s_h2))
q = [
    [cell("", s_theadL), cell("Q3'25", s_thead), cell("Q4'25", s_thead), cell("Q1'26", s_thead), cell("Q2'26", s_thead)],
    [cell("Revenue ($ mn)", s_cellB), cell("1,144", s_cellR), cell("1,989", s_cellR), cell("1,646", s_cellR), cell("1,443", s_cellR)],
    [cell("Net income ($ mn)", s_cell), cell("(257)", s_cellR), cell("136", s_cellR), cell("21", s_cellR), cell("(68)", s_cellR)],
    [cell("Adj. EBITDA ($ mn)", s_cell), cell("\u2014", s_cellC), cell("343", s_cellR), cell("~168", s_cellR), cell("115", s_cellR)],
    [cell("Sports handle ($ bn)", s_cell), cell("\u2014", s_cellC), cell("16.8", s_cellR), cell("\u2014", s_cellC), cell("13.1", s_cellR)],
    [cell("Monthly unique payers (mn)", s_cell), cell("\u2014", s_cellC), cell("4.8", s_cellR), cell("4.2", s_cellR), cell("3.6", s_cellR)],
    [cell("Avg. revenue / payer", s_cell), cell("\u2014", s_cellC), cell("$139", s_cellR), cell("$131", s_cellR), cell("$132", s_cellR)],
]
story.append(styled_table(q, [52*mm, 28*mm, 28*mm, 28*mm, 28*mm]))
story.append(P("Q4'25 was the blowout (revenue +43%, EBITDA margin 17.3%, net revenue margin 8.0% on handle). Q1'26 grew revenue ~17% with a second "
               "straight profitable quarter. Q2'26 is the seasonal trough (baseball-only quarter) and was hit by a perfect storm: customer-friendly "
               "outcomes (~$80 mn drag from the Knicks' NBA title and World Cup results), +10% planned acquisition spend into the World Cup/NBA Finals, "
               "and a step-up in Predictions investment. Handle still grew 15% \u2014 demand was healthy; hold was not.", s_body))

story.append(P("Unit economics \u2014 the flywheel is working", s_h2))
for b in [
    "<b>Handle \u2192 hold \u2192 margin.</b> Sportsbook net revenue margin hit 8.0% in Q4'25 (vs. 5.5% a year earlier) and management's structural hold target is ~10%+. The engine is <b>parlay mix</b>: NBA parlay handle mix rose 400+ bps YoY in Q2'26. Parlays carry ~2x the hold of single bets, and DraftKings' same-game-parlay product is the industry benchmark.",
    "<b>Promo normalization.</b> External acquisition promos are declining as a share of handle as states mature; Q2's promo uptick was deliberate (World Cup, Predictions launch), not structural.",
    "<b>Cohort LTV.</b> Per management, every annual cohort since 2022 has shown predictable, improving economics \u2014 customers acquired in mature states now generate contribution margins well above acquisition cost within year one.",
    "<b>iGaming is the steadier compounder.</b> Q2 iGaming revenue grew 7.5% to $462 mn with none of the sportsbook's outcome volatility. Only 5 states are live (~11% of Americans) \u2014 every new iGaming state is high-margin incremental revenue on the same fixed-cost base.",
]:
    story.append(B(b))

story.append(P("Balance sheet &amp; cash flow", s_h2))
story.append(P("The balance sheet is levered but manageable, and 2026's refinancing extended the runway:", s_body))
for b in [
    "<b>Liquidity:</b> $999 mn cash (Mar 31, 2026) plus a $750 mn undrawn revolver (expanded 2026).",
    "<b>Debt:</b> $1.265 bn zero-coupon convertible notes due <b>March 2028</b> (conversion price $94.85; capped-call hedge to $135.50 limits dilution) and a $700 mn Term B loan (refinanced 2026 from $576 mn). Total funded debt ~$1.96 bn \u2192 net debt ~$1.0 bn, or ~1.2x 2026E adjusted EBITDA.",
    "<b>Buyback:</b> ~22.7 mn shares repurchased for ~$773 mn through June 2026 (16 mn shares in FY2025) \u2014 ~4.5% of shares outstanding retired, a credible signal given the stock's 50% drawdown.",
    "<b>Cash flow:</b> the business is now self-funding; capex is light (~$50\u201370 mn/yr, mostly tech), and working capital is structurally negative (customer funds held on balance sheet).",
]:
    story.append(B(b))
story.append(P("Watch item: the March 2028 converts ($1.265 bn) must be refinanced or repaid within 18 months. At current prices conversion is "
               "out of the money, so expect a refinancing \u2014 the 2026 Term B deal shows management can access secured markets, but rising "
               "secured debt ahead of 2028 bears monitoring.", s_body))

# ============ 4. GROWTH OUTLOOK & PROJECTIONS ============
story.append(P("4 &nbsp; Growth Outlook &amp; Forward Projections", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("We model revenue compounding at ~14% (2025\u201330) with margins expanding from 10% to 20% as states mature, iGaming scales, and "
               "Predictions contributes. Our 2026\u201327 estimates sit near guidance/consensus; the out-year ramp reflects the 30%+ steady-state "
               "margin framework from Investor Day.", s_body))
proj = [
    [cell("$ mn", s_theadL), cell("2025A", s_thead), cell("2026E", s_thead), cell("2027E", s_thead), cell("2028E", s_thead), cell("2029E", s_thead), cell("2030E", s_thead)],
    [cell("Revenue", s_cellB), cell("6,055", s_cellR), cell("6,700", s_cellR), cell("7,700", s_cellR), cell("8,900", s_cellR), cell("10,100", s_cellR), cell("11,400", s_cellR)],
    [cell("Growth", s_cell), cell("27%", s_cellR), cell("11%", s_cellR), cell("15%", s_cellR), cell("16%", s_cellR), cell("13%", s_cellR), cell("13%", s_cellR)],
    [cell("Adj. EBITDA", s_cellB), cell("620", s_cellR), cell("800", s_cellR), cell("1,080", s_cellR), cell("1,420", s_cellR), cell("1,820", s_cellR), cell("2,280", s_cellR)],
    [cell("Margin", s_cell), cell("10.2%", s_cellR), cell("11.9%", s_cellR), cell("14.0%", s_cellR), cell("16.0%", s_cellR), cell("18.0%", s_cellR), cell("20.0%", s_cellR)],
    [cell("Free cash flow*", s_cell), cell("~480", s_cellR), cell("680", s_cellR), cell("950", s_cellR), cell("1,250", s_cellR), cell("1,550", s_cellR), cell("1,900", s_cellR)],
]
story.append(styled_table(proj, [30*mm, 25*mm, 25*mm, 25*mm, 25*mm, 25*mm, 25*mm]))
story.append(P("*FCF \u2248 adj. EBITDA less capex, cash taxes and working-capital investment; author estimates. Sources: company guidance (2026E), author model thereafter.", s_small))

d2 = Drawing(430, 190)
d2.add(String(215, 178, "Projected Revenue & Adj. EBITDA Margin (2025A\u20132030E)", fontName="Helvetica-Bold", fontSize=10, textAnchor="middle", fillColor=NAVY))
bc2 = VerticalBarChart(); bc2.x = 45; bc2.y = 30; bc2.height = 120; bc2.width = 340
bc2.data = [[6055, 6700, 7700, 8900, 10100, 11400]]
bc2.strokeColor = None; bc2.bars[0].fillColor = NAVY; bc2.barLabels.nudge = 8; bc2.barLabelFormat = "%d"
bc2.categoryAxis.categoryNames = ["2025A", "2026E", "2027E", "2028E", "2029E", "2030E"]
bc2.valueAxis.valueMin = 0; bc2.valueAxis.valueMax = 12000; bc2.valueAxis.valueStep = 3000
bc2.valueAxis.labels.fontSize = 7; bc2.categoryAxis.labels.fontSize = 8
d2.add(bc2)
d2.add(String(215, 12, "Margin path: 10.2% \u2192 11.9% \u2192 14.0% \u2192 16.0% \u2192 18.0% \u2192 20.0%  (LT target \u226530%)",
             fontName="Helvetica-Oblique", fontSize=8, textAnchor="middle", fillColor=DGRAY))
story.append(d2)
story.append(Spacer(1, 2*mm))

story.append(P("Growth bridges (2026\u20132030)", s_h2))
for b in [
    "<b>Existing-state maturation (~40% of growth).</b> Hold expansion via parlay mix +400 bps/yr, promo normalization, and ARPPU growth. This is the highest-confidence, highest-margin growth in the model.",
    "<b>iGaming legalization (~25%).</b> Only ~11% of Americans can play legal online casino today. Each new large state (New York, Illinois debates recur annually) adds high-margin revenue with minimal incremental marketing \u2014 casino players are acquired through the existing sportsbook funnel.",
    "<b>Predictions (~20%).</b> From zero to \"hundreds of millions\" in annual revenue per management; our model assumes $250\u2013400 mn by 2028 at 60%+ gross margins (no state gaming tax). Available to ~100% of the U.S. population \u2014 it is DraftKings' first truly national product.",
    "<b>New sportsbook states + Canada (~15%).</b> Missouri ramping, Alberta ramping, and line-of-sight launches (California/Texas/Florida remain the long-dated prizes but are not in our numbers).",
]:
    story.append(B(b))

# ============ 5. MOAT ============
story.append(P("5 &nbsp; Moat Assessment", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("DraftKings' moat is <b>narrow but real</b>, built on scale and regulatory position rather than technology alone. We score each pillar:", s_body))
moat = [
    [cell("Moat pillar", s_theadL), cell("Strength", s_thead), cell("Evidence", s_thead)],
    [cell("Scale / liquidity", s_cellB), cell("Strong", s_cellC), cell("35% handle share; $13 bn quarterly handle funds tighter pricing, bigger parlay menus, and marketing efficiency smaller books cannot match.", s_cell)],
    [cell("Brand &amp; distribution", s_cellB), cell("Strong", s_cellC), cell("Top-2 unaided awareness in U.S. betting; 10.9 mn unique customers in last 12 months; Super App deepens the funnel.", s_cell)],
    [cell("Regulatory licenses", s_cellB), cell("Moderate", s_cellC), cell("27-state + DC + PR footprint is a sunk-cost barrier \u2014 but CFTC-licensed prediction markets can bypass it entirely.", s_cell)],
    [cell("Data &amp; trading tech", s_cellB), cell("Moderate", s_cellC), cell("SBTech stack + 14 years of pricing data improve hold; parlay pricing is the crown jewel. Replicable over time by FanDuel/bet365.", s_cell)],
    [cell("Switching costs", s_cellB), cell("Weak", s_cellC), cell("Multi-homing is rampant: bettors hold 3+ apps and line-shop. Retention rests on product and promos, not lock-in.", s_cell)],
    [cell("Network effects", s_cellB), cell("Weak\u2013Moderate", s_cellC), cell("Limited direct network effects; indirect via liquidity for Predictions market-making (early).", s_cell)],
]
story.append(styled_table(moat, [36*mm, 26*mm, 118*mm]))
story.append(P("Net: a <b>scale-and-brand moat with a regulatory overhang</b>. The moat widens as states mature (marketing leverage, hold expansion) but "
               "narrows if prediction markets achieve permanent federal preemption \u2014 the single most important variable in this thesis.", s_body))

# ============ 6. COMPETITION ============
story.append(P("6 &nbsp; Competitive Landscape", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("U.S. online betting is a <b>duopoly with a lengthening tail</b>: FanDuel and DraftKings control ~78% of gross gaming revenue. "
               "The tail, however, is getting sharper \u2014 Fanatics and bet365 are gaining handle share, and prediction markets attack from outside "
               "the regulatory perimeter entirely.", s_body))

comp = [
    [cell("Operator", s_theadL), cell("U.S. OSB share*", s_thead), cell("iGaming share", s_thead), cell("Threat assessment", s_thead)],
    [cell("FanDuel (Flutter)", s_cellB), cell("~44% GGR", s_cellC), cell("~29%", s_cellC), cell("The benchmark competitor: larger share, first to sustained U.S. profitability, global trading tech via Flutter. DraftKings is closing the handle gap (35% vs 32% in Q1'26).", s_cell)],
    [cell("DraftKings", s_cellB), cell("~34% GGR", s_cellC), cell("~24%", s_cellC), cell("Best-in-class parlay product and promos engine; #1-rated app. Monetization (ARPPU +43% in Q4'25) is the catch-up lever.", s_cell)],
    [cell("Fanatics Sportsbook", s_cell), cell("~9% handle", s_cellC), cell("small", s_cellC), cell("The riser: passed BetMGM in H2'25; 11.7% of NY handle in May'26. Deep-pocketed, merchandise-data flywheel, aggressive promos.", s_cell)],
    [cell("BetMGM", s_cell), cell("~8% handle", s_cellC), cell("mid-teens", s_cellC), cell("Stuck in third: omnichannel (MGM resorts) helps iGaming, but OSB share is flat-to-down.", s_cell)],
    [cell("bet365", s_cell), cell("~4% (11 states)", s_cellC), cell("\u2014", s_cellC), cell("Quietly dangerous: 7% share in states where live; best-in-class in-play product and pricing discipline from the UK.", s_cell)],
    [cell("Caesars / theScore / ESPN exit", s_cell), cell("declining", s_cellC), cell("\u2014", s_cellC), cell("Caesars' May'26 NY hold was the worst among majors; Penn killed ESPN Bet (Dec'25), laid off 75 in interactive.", s_cell)],
    [cell("Kalshi / Polymarket", s_cellB), cell("n/a \u2013 federal", s_cellC), cell("n/a", s_cellC), cell("<b>The disruptor.</b> ~$44\u201363 bn 2025 volume; sports parlays with better effective odds; legal in CA/TX/FL where DKNG can't operate. Courts decide the endgame.", s_cell)],
]
story.append(styled_table(comp, [40*mm, 28*mm, 22*mm, 90*mm]))
story.append(P("*Handle share per SportsBusiness Journal (Q1'26, 15 trackable states): DKNG 35%, FanDuel 32%. GGR share per industry trackers. Sources: SBJ 5/29/26, Flutter H1'26 report, state regulator filings.", s_small))

d3 = Drawing(430, 150)
d3.add(String(215, 140, "U.S. Online Sportsbook Handle Share (Q1 2026, trackable states)", fontName="Helvetica-Bold", fontSize=10, textAnchor="middle", fillColor=NAVY))
shares = [("DraftKings 35%", 35, NAVY), ("FanDuel 32%", 32, HexColor("#1F6F43")), ("Fanatics 9%", 9, GOLD),
          ("BetMGM 8%", 8, DGRAY), ("bet365 4%", 4, HexColor("#8A94A6")), ("Others 12%", 12, MGRAY)]
y = 110
for name, pct, col in shares:
    wbar = pct * 9.5
    d3.add(Rect(110, y, wbar, 14, fillColor=col, strokeColor=None))
    d3.add(String(105, y + 4, name, fontName="Helvetica", fontSize=8, textAnchor="end", fillColor=DGRAY))
    y -= 20
story.append(d3)

story.append(P("Competitive dynamics to watch:", s_h2))
for b in [
    "<b>Handle vs. revenue share.</b> DraftKings leads in <i>handle</i> (35% vs. 32%) but trails in <i>revenue</i> (~34% vs. ~44%) \u2014 the gap is hold and mix. Closing it (parlays, pricing) is the single biggest earnings lever management controls.",
    "<b>Fanatics is the real #3 now</b>, not BetMGM \u2014 and bet365's per-state efficiency suggests the tail won't stay docile.",
    "<b>Prediction markets compete on price:</b> Kalshi's parlay payouts have been quoted ~20%+ richer than sportsbooks' ($1,043 vs. $850 on a sample ticket). If that persists, price-sensitive volume migrates \u2014 DraftKings' answer is to <i>be</i> a prediction market.",
]:
    story.append(B(b))

# ============ 7. PRODUCT EVALUATION ============
story.append(P("7 &nbsp; Product Evaluation", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
prod = [
    [cell("Product", s_theadL), cell("Scale / status", s_thead), cell("Economics", s_thead), cell("Verdict", s_thead)],
    [cell("Online Sportsbook", s_cellB), cell("$13.1 bn Q2 handle (+15%); 27 states + DC + PR", s_cell), cell("Structural hold ~10%+; parlay mix +400 bps; promo normalizing", s_cell), cell("<b>A\u2013.</b> Best-in-class SGP product; hold volatility is the cost of the model.", s_cell)],
    [cell("iGaming (Casino)", s_cellB), cell("$462 mn Q2 rev (+7.5%); 5 states", s_cell), cell("Highest margins; no outcome volatility; cross-sold from sportsbook", s_cell), cell("<b>A.</b> The steadiest compounder; legalization is pure upside.", s_cell)],
    [cell("DraftKings Predictions", s_cellB), cell("$11 bn annualized vol. (Jul'26); national", s_cell), cell("10\u201330 pts gross-margin edge; no state tax; lower promo", s_cell), cell("<b>B+ (option value).</b> Hypergrowth, unproven monetization; binary legal risk.", s_cell)],
    [cell("Daily Fantasy Sports", s_cell), cell("Legacy; all 50 states (paid + free)", s_cell), cell("Low growth; valuable acquisition funnel &amp; brand", s_cell), cell("<b>B.</b> Mature cash contributor; feeds the ecosystem.", s_cell)],
    [cell("Jackpocket (lottery courier)", s_cell), cell("Acquired 2024; exited TX in 2025", s_cell), cell("Thin margins; MUP drag on exit", s_cell), cell("<b>C+.</b> Strategic (lottery cross-sell) but sub-scale; TX exit was prudent.", s_cell)],
    [cell("Super App (Sports &amp; Casino)", s_cellB), cell("Nationwide 2026; single wallet", s_cell), cell("Cross-sell \u2192 ARPPU; lower blended CAC", s_cell), cell("<b>B+.</b> Right strategy; migration execution risk in 2026.", s_cell)],
]
story.append(styled_table(prod, [38*mm, 48*mm, 48*mm, 46*mm]))
story.append(P("Product thesis in one line: the sportsbook acquires, iGaming monetizes, Predictions expands the addressable market, "
               "and the Super App binds them \u2014 a coherent ecosystem, not a collection of bets.", s_body))

# ============ 8. VALUATION ============
story.append(P("8 &nbsp; Valuation", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("We triangulate fair value with (a) a scenario-weighted DCF \u2014 the primary method, given the margin-expansion story \u2014 "
               "and (b) trading multiples as a cross-check.", s_body))

story.append(P("8.1 &nbsp; Discounted cash flow \u2014 three scenarios", s_h2))
story.append(P("Key assumptions: ~496.5 mn diluted shares; net debt ~$1.0 bn (converts $1.265 bn + Term B $0.7 bn \u2212 cash ~$1.0 bn); "
               "FCF \u2248 adj. EBITDA less capex, cash taxes and WC. WACC reflects beta 1.68 and a levered consumer-discretionary profile.", s_body))
dcf = [
    [cell("Scenario", s_theadL), cell("Revenue CAGR '25\u2013'30", s_thead), cell("2030 adj. EBITDA margin", s_thead), cell("WACC / g", s_thead), cell("Implied EV ($ bn)", s_thead), cell("Value / share", s_thead)],
    [cell("Bear \u2014 prediction markets win share; tax hikes; hold disappoints", s_cell), cell("~7%", s_cellC), cell("13%", s_cellC), cell("12% / 2.0%", s_cellC), cell("9.1", s_cellR), cell("<b>$16</b>", s_cellBR)],
    [cell("Base \u2014 maturation + iGaming + Predictions ramp; LT margin \u2192 25%+", s_cell), cell("~13.5%", s_cellC), cell("20%", s_cellC), cell("11% / 3.0%", s_cellC), cell("19.0", s_cellR), cell("<b>$36</b>", s_cellBR)],
    [cell("Bull \u2014 Predictions breakout; iGaming wave; 30% LT margins", s_cell), cell("~17%", s_cellC), cell("25%", s_cellC), cell("10% / 3.5%", s_cellC), cell("28.0", s_cellR), cell("<b>$55</b>", s_cellBR)],
]
story.append(styled_table(dcf, [62*mm, 28*mm, 28*mm, 22*mm, 24*mm, 24*mm]))

d4 = Drawing(430, 165)
d4.add(String(215, 155, "DCF Scenario Values vs. Current Price ($)", fontName="Helvetica-Bold", fontSize=10, textAnchor="middle", fillColor=NAVY))
vals = [("Current $21.75", 21.75, DGRAY), ("Bear $16", 16, RED), ("Base $36", 36, ACCENT), ("Bull $55", 55, NAVY)]
x = 70
for name, v, col in vals:
    h = v * 2.1
    d4.add(Rect(x, 30, 55, h, fillColor=col, strokeColor=None))
    d4.add(String(x + 27.5, 30 + h + 6, f"${v:g}", fontName="Helvetica-Bold", fontSize=9, textAnchor="middle", fillColor=col))
    d4.add(String(x + 27.5, 18, name.split(" ")[0], fontName="Helvetica", fontSize=8, textAnchor="middle", fillColor=DGRAY))
    x += 95
story.append(d4)

story.append(P("<b>Scenario weighting:</b> Base 50% \u00d7 $36 + Bull 25% \u00d7 $55 + Bear 25% \u00d7 $16 = <b>$35.75 \u2192 $36.00 target</b> "
               "(rounded). The bear case is deliberately punitive: it assumes prediction markets permanently impair the sportsbook moat and "
               "state taxes grind 2\u20133 points off margins.", s_body))

story.append(P("8.2 &nbsp; Multiples cross-check", s_h2))
mult = [
    [cell("Multiple", s_theadL), cell("DKNG today", s_thead), cell("Implied by $36 target", s_thead), cell("Context", s_thead)],
    [cell("EV / 2026E revenue", s_cellB), cell("~1.75\u00d7", s_cellC), cell("~2.8\u00d7", s_cellC), cell("Susquehanna's framework (5.1\u00d7 group sales, 30% DKNG discount \u2192 ~3.6\u00d7) suggests the target multiple is conservative.", s_cell)],
    [cell("EV / 2026E adj. EBITDA", s_cellB), cell("~14.7\u00d7", s_cellC), cell("~23.5\u00d7", s_cellC), cell("Full price for 2026 \u2014 but on 2028E EBITDA (~$1.4 bn) the target is ~13\u00d7, in line with scaled consumer platforms.", s_cell)],
    [cell("P / E (2027E adj. EPS ~$1.3)", s_cellB), cell("~17\u00d7", s_cellC), cell("~28\u00d7", s_cellC), cell("Growth-adjusted: PEG <1.0\u00d7 on 30%+ EPS CAGR '26\u2013'30.", s_cell)],
]
story.append(styled_table(mult, [44*mm, 30*mm, 32*mm, 74*mm]))
story.append(P("The target prices in the margin expansion the model earns by 2028\u201330 \u2014 i.e., you are paying for execution, not for "
               "today's earnings. That is appropriate for a business at an inflection point but demands the risk rating stay High.", s_body))

story.append(P("8.3 &nbsp; What the Street thinks", s_h2))
story.append(P("Consensus is <b>Moderate Buy</b> with an average target of <b>~$34.4</b> (30 Buys, 8 Holds, 2 Sells per MarketBeat). Recent prints: "
               "Wolfe Research initiated at Outperform/$40 (Sep'26), UBS $48 Buy, Citizens $37, Morgan Stanley $36, JPM $33, Barclays $34, "
               "Guggenheim $33, Bernstein $29, Truist $29, MoffettNathanson $27 Neutral (prediction-market concerns). Our $36 sits modestly above "
               "consensus \u2014 we are more constructive on Predictions optionality and the 2027\u201328 margin ramp than the median analyst.", s_body))

# ============ 9. RISKS & CATALYSTS ============
story.append(P("9 &nbsp; Risks, Catalysts &amp; What to Watch", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
rc = [
    [cell("Risk / catalyst", s_theadL), cell("Direction", s_thead), cell("Timing", s_thead), cell("Why it matters", s_thead)],
    [cell("Q3'26 earnings (NFL hold normalization)", s_cellB), cell("Catalyst \u2191", s_cellC), cell("~Nov 5", s_cellC), cell("Street expects $1.42 bn rev / \u2013$0.16 EPS; a clean hold quarter re-rates the H2 story.", s_cell)],
    [cell("Prediction-market court rulings", s_cellB), cell("Binary", s_cellC), cell("Ongoing", s_cellC), cell("Federal preemption upheld \u2192 DKNG's moat impaired but its Predictions asset validated. Adverse \u2192 threat removed.", s_cell)],
    [cell("State tax legislation", s_cell), cell("Risk \u2193", s_cellC), cell("2027 sessions", s_cellC), cell("Each 1 pt of blended tax \u2248 ~$65\u201370 mn of EBITDA at current scale.", s_cell)],
    [cell("iGaming legalization bills", s_cell), cell("Catalyst \u2191", s_cellC), cell("2026\u201327", s_cellC), cell("One large state (e.g., NY/IL) could add $300 mn+ high-margin revenue.", s_cell)],
    [cell("Predictions monetization disclosure", s_cell), cell("Catalyst \u2191", s_cellC), cell("2027", s_cellC), cell("First revenue/margin disclosure turns the call option into a valued asset.", s_cell)],
    [cell("2028 converts refinancing", s_cell), cell("Risk \u2193", s_cellC), cell("By Mar'28", s_cellC), cell("$1.265 bn maturity; expect refi \u2014 terms will signal credit-market confidence.", s_cell)],
    [cell("Sport-outcome variance", s_cell), cell("Noise", s_cellC), cell("Quarterly", s_cellC), cell("Structural hold ~10%+; quarterly realized hold of 7\u201312% is normal. Size positions accordingly.", s_cell)],
]
story.append(styled_table(rc, [52*mm, 22*mm, 20*mm, 86*mm]))

# ============ 10. RECOMMENDATION ============
story.append(P("10 &nbsp; Recommendation", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("We initiate/maintain a <b>BUY</b> rating on DraftKings with a <b>$36.00</b> 12-month price target, implying ~65% upside from $21.75. "
               "DraftKings has crossed the profitability Rubicon \u2014 $620 mn of adjusted EBITDA and a first GAAP profit in 2025 \u2014 yet trades "
               "like a broken growth story, near 52-week lows, at ~1.75\u00d7 2026E revenue. The market is pricing the prediction-market threat as a "
               "near-certainty and the core business at trough multiples; we see a mispricing on both counts: the core flywheel (parlay-led hold "
               "expansion, promo normalization, iGaming) supports mid-teens growth with margins marching toward 20% by 2030, while Predictions offers "
               "asymmetric upside to a national footprint at structurally superior margins.", s_body))
story.append(P("Position sizing guidance: this is a <b>High-risk BUY</b>. Quarterly hold variance (Q2'26: \u20135% revenue on +15% handle) and binary "
               "legal outcomes argue for a starter position with room to add on court clarity or a hold-normalized quarter \u2014 not a full position "
               "into NFL-season variance. Key invalidation: sustained GGR share loss to prediction markets combined with adverse federal rulings, "
               "or 2027 guidance that walks back the \u226530% long-term margin framework.", s_body))
story.append(Spacer(1, 2*mm))
story.append(P("Analyst certification &amp; disclosures: This report is an independent research-style analysis prepared for informational purposes "
               "only. It is not investment advice, a recommendation to buy/sell any security, or an offer to transact. Financial figures are sourced "
               "from DraftKings' SEC filings (10-K FY2025, 10-Qs), earnings releases and calls, and reputable financial press; projections and the "
               "$36.00 price target are the author's estimates and involve uncertainty. Past performance does not predict future results. "
               "Investors should conduct their own due diligence and consult a licensed advisor.", s_small))
story.append(Spacer(1, 2*mm))
story.append(P("Sources: DraftKings 10-K FY2025 (SEC EDGAR); Q4'25, Q1'26, Q2'26 earnings releases &amp; call transcripts; March 2026 Investor Day "
               "materials; SportsBusiness Journal (5/29/26); Flutter H1'26 results; MarketBeat/consensus data; Finnhub market data. Dated September 19, 2026.", s_small))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=18*mm,
                        title="DraftKings (DKNG) Equity Research Note", author="Muse")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("WROTE", OUT)
