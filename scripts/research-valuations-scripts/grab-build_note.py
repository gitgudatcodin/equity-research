#!/usr/bin/env python3
"""Build the Grab Holdings equity research note PDF."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, HRFlowable)
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.lib import colors

OUT = "/home/hatch/workspace/your_files/grab-equity-research/grab-equity-research-note.pdf"

NAVY = HexColor("#0F2A44"); ACCENT = HexColor("#0E7C3E"); GOLD = HexColor("#C9A227")
LGRAY = HexColor("#F2F4F7"); MGRAY = HexColor("#D9DEE5"); DGRAY = HexColor("#5A6472")
RED = HexColor("#B42318"); BLUE = HexColor("#1D4ED8"); INK = HexColor("#1A2332")

s_title = ParagraphStyle("t", fontName="Helvetica-Bold", fontSize=25, leading=29, textColor=NAVY)
s_sub = ParagraphStyle("s", fontName="Helvetica", fontSize=10.5, leading=15, textColor=DGRAY)
s_h1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=14, leading=18, textColor=NAVY, spaceBefore=10, spaceAfter=5)
s_h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=NAVY, spaceBefore=8, spaceAfter=4)
s_body = ParagraphStyle("b", fontName="Helvetica", fontSize=9.5, leading=14.5, textColor=INK, alignment=TA_JUSTIFY, spaceAfter=5)
s_bull = ParagraphStyle("bu", parent=s_body, leftIndent=12, bulletIndent=4, spaceAfter=3, alignment=TA_LEFT)
s_small = ParagraphStyle("sm", fontName="Helvetica", fontSize=7.5, leading=10.5, textColor=DGRAY)
s_cell = ParagraphStyle("c", fontName="Helvetica", fontSize=8.5, leading=11.5, textColor=INK)
s_cellB = ParagraphStyle("cb", parent=s_cell, fontName="Helvetica-Bold")
s_cellR = ParagraphStyle("cr", parent=s_cell, alignment=TA_RIGHT)
s_cellBR = ParagraphStyle("cbr", parent=s_cellB, alignment=TA_RIGHT)
s_cellC = ParagraphStyle("cc", parent=s_cell, alignment=TA_CENTER)
s_thead = ParagraphStyle("th", parent=s_cell, fontName="Helvetica-Bold", textColor=white, alignment=TA_CENTER, fontSize=7.5)
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
def cellR(txt, st=s_cellR): return Paragraph(txt, st)
def hdr(txt, st=s_thead): return Paragraph(txt, st)

story = []
W, H = A4

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7); canvas.setFillColor(DGRAY)
    canvas.drawString(18*mm, 12*mm, "Grab Holdings Ltd. (NASDAQ: GRAB)  \u2014  Equity Research Note  \u2014  September 2026")
    canvas.drawRightString(W - 18*mm, 12*mm, f"Page {doc.page}")
    canvas.setStrokeColor(MGRAY); canvas.setLineWidth(0.5)
    canvas.line(18*mm, 14.5*mm, W - 18*mm, 14.5*mm)
    canvas.restoreState()

# ============ COVER ============
story.append(Spacer(1, 26*mm))
story.append(P("GRAB HOLDINGS LIMITED", ParagraphStyle("x", parent=s_sub, fontName="Helvetica-Bold", fontSize=13, textColor=ACCENT, spaceAfter=2)))
story.append(P("Southeast Asia's Super-App<br/>at a 52-Week Low", s_title))
story.append(Spacer(1, 4*mm))
story.append(P("Equity Research Note  \u00b7  Communication Services \u2014 Internet Platforms  \u00b7  September 19, 2026", s_sub))
story.append(Spacer(1, 8*mm))

rating_data = [
    [hdr("Recommendation", s_theadL), hdr("12-Mo. Price Target"), hdr("Current Price"), hdr("Implied Upside"), hdr("Risk Rating")],
    [Paragraph("<b><font color=\"#0E7C3E\" size=\"13\">BUY</font></b>", s_cellC),
     Paragraph("<b><font size=\"12\">$6.00</font></b>", s_cellC),
     Paragraph("<b><font size=\"12\">$2.79</font></b><br/><font size=\"7\" color=\"#5A6472\">Sep 18, 2026 close</font>", s_cellC),
     Paragraph("<b><font color=\"#0E7C3E\" size=\"12\">+115%</font></b>", s_cellC),
     Paragraph("<b>High</b>", s_cellC)],
]
story.append(styled_table(rating_data, [34*mm, 34*mm, 34*mm, 34*mm, 34*mm], fontsize=9))
story.append(Spacer(1, 6*mm))

story.append(P("The market has priced Grab like a melting ice cube. The numbers say otherwise: 18 consecutive quarters of adjusted-EBITDA growth, the first full-year GAAP profit in company history (FY2025), guidance raised twice this year, and a net-cash balance sheet with $5.0 billion in the bank. At $2.79 the stock sits at its 52-week low, down 56% in a year, trading at 1.6x forward revenue and 8.8x forward adjusted EBITDA \u2014 roughly half the multiple of Uber and a fraction of DoorDash \u2014 despite growing revenue 22%+ and adjusted EBITDA 44\u201348%. The derating is real and partly earned: Indonesia capped ride-hailing commissions, management just wrote its largest-ever check ($1.49 billion for BNPL player Atome), and Uber is about to own Grab's biggest delivery rival. But we see an asymmetric setup: a dominant regional platform (55% food-delivery share, 70%+ ride-hailing share in most markets) with a fintech business compounding at triple-digit rates, now valued as if the growth story were over. Our scenario-weighted DCF points to $6.19; we set a $6.00 target and rate the shares <b>BUY</b>. This is a high-risk call \u2014 regulation and capital allocation are the swing factors \u2014 sized accordingly.", s_body))
story.append(Spacer(1, 3*mm))

# key stats box
stats = [
    [cell("<b>Market cap</b>", s_cellB), cellR("~$11.4 bn"), cell("<b>Shares out.</b>", s_cellB), cellR("~4.09 bn")],
    [cell("<b>52-week range</b>", s_cellB), cellR("$2.81 \u2013 $6.62"), cell("<b>1-yr return</b>", s_cellB), cellR("-56%")],
    [cell("<b>Net cash</b>", s_cellB), cellR("$5.0 bn"), cell("<b>FY26E rev / adj. EBITDA</b>", s_cellB), cellR("$4.1 bn / $730 m")],
    [cell("<b>EV / FY26E rev</b>", s_cellB), cellR("~1.6x"), cell("<b>EV / FY26E adj. EBITDA</b>", s_cellB), cellR("~8.8x")],
]
story.append(styled_table(stats, [42*mm, 43*mm, 42*mm, 43*mm], header_rows=0, zebra=True, fontsize=8.5))
story.append(Spacer(1, 4*mm))
story.append(P("Prices as of September 18, 2026 close. Financial figures from company releases (Q2 2026 reported Aug 4, 2026; FY2025 reported Feb 12, 2026). This note is an independent research-style analysis for informational purposes, not investment advice.", s_small))

# ============ 1. INVESTMENT THESIS ============
story.append(P("1. Investment thesis", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
for t in [
    "<b>Dominant, defensible regional platform.</b> Grab is the #1 food-delivery platform in Southeast Asia (55% GMV share, Momentum Works 2025) and holds 70%+ ride-hailing share in most of its eight markets. The super-app structure \u2014 one user base across rides, food, groceries, payments and banking \u2014 creates cross-sell and data advantages that single-vertical rivals cannot easily replicate.",
    "<b>Profitability inflection is real and accelerating.</b> Adjusted EBITDA has grown 18 quarters in a row; FY2025 delivered the first full-year GAAP profit ($200m); adj. EBITDA margin expanded from 12.6% (Q3 2024) to 16.9% (Q2 2026). FY2026 guidance was raised twice and now calls for $720\u2013740m of adjusted EBITDA (+44\u201348%).",
    "<b>Fintech is the second growth engine.</b> Financial Services revenue grew 59% YoY in Q2 2026; the gross loan book nearly tripled to $2.3b; deposits hit $2.5b across three digital banks; the segment is nearing adjusted-EBITDA breakeven. Management targets $500m of FinSvcs adjusted EBITDA and a $6b+ loan book by 2028.",
    "<b>Valuation disconnect.</b> At 1.6x FY26E revenue and 8.8x FY26E adjusted EBITDA, Grab trades at a steep discount to Uber (2.4x / ~14x), DoorDash (4.1x / ~45\u201350x) and Sea (~24.5x EBITDA) despite comparable or faster growth. Our DCF (bear $3.12 / base $6.00 / bull $9.65, weighted $6.19) and SOTP ($5.65) both support a $6.00 target.",
    "<b>Catalyst path is visible.</b> FinSvcs EBITDA inflection (expected H2 2026), Atome integration (close Q3 2027), continued buybacks (~$900m remaining), and any easing of the Indonesia commission overhang could each re-rate the shares.",
    "<b>Risks are genuine \u2014 hence High risk, not a core holding.</b> Indonesia's 8% commission cap, the $1.49b Atome bet on BNPL credit, Uber's acquisition of foodpanda-owner Delivery Hero, and emerging-market FX/fuel volatility are all live. Size the position for a 30\u201340% drawdown scenario.",
]:
    story.append(B(t))

# ============ 2. COMPANY OVERVIEW ============
story.append(P("2. Company overview: what Grab actually does", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
story.append(P("Grab Holdings (NASDAQ: GRAB), headquartered in Singapore and listed via SPAC in December 2021, is Southeast Asia's leading super-app across <b>eight markets</b>: Cambodia, Indonesia, Malaysia, Myanmar, the Philippines, Singapore, Thailand and Vietnam. It reports in three segments:", s_body))
story.append(P("<b>On-Demand (core, ~87% of revenue).</b> Two sub-verticals:", s_h2))
for t in [
    "<b>Deliveries \u2014 GrabFood, GrabMart, GrabExpress.</b> Food delivery is the anchor; GrabMart covers groceries and quick-commerce; GrabExpress is on-demand logistics. Q2 2026: GMV $4.25b, revenue $531m (+21% YoY), segment adj. EBITDA $96m. Revenue/GMV take rate ~12.5%. GrabAds \u2014 advertising sold to merchants on the platform \u2014 reached 1.7% of Deliveries GMV in early 2025 and is a growing, high-margin contributor.",
    "<b>Mobility \u2014 GrabCar, GrabBike and tiers.</b> Ride-hailing across cars and two-wheelers, with premium, airport, and budget tiers (Saver/Priority) to segment demand. Q2 2026: GMV $2.21b, revenue $331m (+12% YoY), take rate ~15.0%, segment adj. EBITDA margin ~8.6% of GMV \u2014 the highest-margin on-demand vertical.",
]:
    story.append(B(t))
story.append(P("<b>Financial Services (~13% of revenue, growing ~60%).</b> GrabFin lending (PayLater/BNPL, driver and merchant loans), digital banks \u2014 GXS Bank (Singapore, JV with Singtel), GX Bank (Malaysia, JV with Kuok Group) and Superbank (Indonesia, consolidated June 2026) \u2014 plus GrabPay wallets and insurance. Q2 2026: revenue $134m (+59% YoY), adj. EBITDA \u2013$15m (narrowing from \u2013$26m). The flywheel logic: 53.9m monthly transacting users generate proprietary behavioral data that feeds AI underwriting, enabling lending to thin-file borrowers traditional banks avoid.", s_body))
story.append(P("<b>Enterprise / Other.</b> GrabAds (reported inside Deliveries economics) and small other revenue. Advertising is strategically important: it monetizes the same GMV twice \u2014 once via commission, once via ads \u2014 with minimal incremental cost.", s_body))
story.append(P("<b>How it makes money:</b> commissions/take rates on every ride and delivery (10.9% of GMV was reinvested as incentives in Q2 2026, partly to support driver earnings amid elevated fuel costs), advertising, and net interest/lending margins. The model is asset-light: no vehicle fleet, no restaurant kitchens, no bank branches.", s_body))

# ============ 3. FINANCIAL REVIEW ============
story.append(P("3. Financial review", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
story.append(P("<b>Q2 2026 (reported August 4, 2026): beat-and-raise.</b> Revenue of $997m (+22% YoY) was a touch light versus the $1.00b consensus, but EPS of $0.06 crushed the $0.01 estimate, adjusted EBITDA of $168m (+54%) beat, and management raised full-year guidance for the second time. GAAP profit of $235m was flattered by a $307m one-off gain on consolidating Superbank \u2014 the underlying operating profit was $19m.", s_body))

q2 = [
    [hdr("Q2 2026 metric", s_theadL), hdr("Q2 2026"), hdr("Q2 2025"), hdr("YoY")],
    [cell("Revenue"), cellR("$997 m"), cellR("$819 m"), cellR("+22%")],
    [cell("On-Demand GMV"), cellR("$6.46 bn"), cellR("$5.35 bn"), cellR("+21%")],
    [cell("Monthly transacting users"), cellR("53.9 m"), cellR("46.2 m"), cellR("+17%")],
    [cell("Adjusted EBITDA (margin)"), cellR("$168 m (16.9%)"), cellR("$109 m (13.3%)"), cellR("+54%")],
    [cell("GAAP profit for period"), cellR("$235 m*"), cellR("$20 m"), cellR("\u2014")],
    [cell("Adjusted FCF (TTM)"), cellR("$450 m"), cellR("\u2014"), cellR("\u2014")],
    [cell("Gross loan portfolio"), cellR("$2,318 m"), cellR("$781 m"), cellR("+197%")],
]
story.append(styled_table(q2, [62*mm, 36*mm, 36*mm, 36*mm]))
story.append(P("*Includes a $307m one-off gain from the Superbank consolidation; operating profit was $19m. Source: company Q2 2026 press release.", s_small))
story.append(Spacer(1, 2*mm))

story.append(P("<b>FY2025: the year Grab turned profitable.</b> Revenue $3,307m (+20%), first-ever full-year GAAP net profit of $200m (vs \u2013$158m in 2024), adjusted EBITDA $500m (+60%), adjusted free cash flow $290m (+113%).", s_body))

story.append(P("<b>Eight-quarter trend: growth with expanding margins.</b> Revenue has grown 17\u201324% every quarter; GMV growth accelerated from 15% to 24%; adjusted EBITDA has risen for 18 straight quarters.", s_body))
trend = [
    [hdr("Quarter", s_theadL), hdr("Revenue"), hdr("GMV"), hdr("MTUs"), hdr("Adj. EBITDA"), hdr("GAAP profit")],
    [cell("Q3 2024"), cellR("$716 m"), cellR("$4.70 bn"), cellR("42.0 m"), cellR("$90 m"), cellR("$15 m")],
    [cell("Q4 2024"), cellR("$764 m"), cellR("$5.03 bn"), cellR("43.9 m"), cellR("$97 m"), cellR("$11 m")],
    [cell("Q1 2025"), cellR("$773 m"), cellR("$4.93 bn"), cellR("44.5 m"), cellR("$106 m"), cellR("$10 m")],
    [cell("Q2 2025"), cellR("$819 m"), cellR("$5.35 bn"), cellR("46.2 m"), cellR("$109 m"), cellR("$20 m")],
    [cell("Q3 2025"), cellR("$873 m"), cellR("$5.77 bn"), cellR("47.7 m"), cellR("$136 m"), cellR("$17 m")],
    [cell("Q4 2025"), cellR("$906 m"), cellR("$6.10 bn"), cellR("50.5 m"), cellR("$148 m"), cellR("$153 m*")],
    [cell("Q1 2026"), cellR("$955 m"), cellR("$6.13 bn"), cellR("51.6 m"), cellR("$154 m"), cellR("$120 m*")],
    [cell("Q2 2026"), cellR("$997 m"), cellR("$6.46 bn"), cellR("53.9 m"), cellR("$168 m"), cellR("$235 m*")],
]
story.append(styled_table(trend, [26*mm, 28*mm, 30*mm, 26*mm, 32*mm, 28*mm], fontsize=8))
story.append(P("*GAAP profit is noisy \u2014 inflated by one-off gains (e.g., $307m Superbank gain in Q2 2026). Adjusted EBITDA is the cleaner operating read. Source: company releases.", s_small))
story.append(Spacer(1, 2*mm))

# chart: quarterly revenue and adj EBITDA
d = Drawing(170*mm, 62*mm)
bc = VerticalBarChart()
bc.x = 12*mm; bc.y = 12*mm; bc.height = 42*mm; bc.width = 140*mm
bc.data = [[716,764,773,819,873,906,955,997],[90,97,106,109,136,148,154,168]]
bc.strokeColor = colors.white
bc.barLabels.nudge = 8
bc.categoryAxis.labels.boxAnchor = "ne"; bc.categoryAxis.labels.angle = 0
bc.categoryAxis.categoryNames = ["Q3'24","Q4'24","Q1'25","Q2'25","Q3'25","Q4'25","Q1'26","Q2'26"]
bc.categoryAxis.labels.fontSize = 6.5
bc.valueAxis.valueMin = 0; bc.valueAxis.valueMax = 1100; bc.valueAxis.valueStep = 275
bc.valueAxis.labels.fontSize = 6.5
bc.bars[0].fillColor = NAVY; bc.bars[1].fillColor = ACCENT
bc.barLabelFormat = "%d"
story.append(d)
story.append(P("Quarterly revenue (navy, $m, left scale) and adjusted EBITDA (green, $m): eight quarters of growth on both lines. Source: company releases.", s_small))
story.append(Spacer(1, 2*mm))

story.append(P("<b>Balance sheet: fortress, but about to be drawn down.</b> Gross cash liquidity was $6.9b at March 31, 2026 with net cash of $5.0b and a debt-to-equity ratio of ~0.06 \u2014 effectively unlevered. Pro forma for the $1.49b Atome cash consideration (payable on close, expected Q3 2027) and the remaining ~$900m of the authorized buyback, net cash falls toward ~$2.6b: still comfortable, but the era of the ever-growing cash pile is ending as management pivots to offense.", s_body))

# ============ 4. GROWTH OUTLOOK ============
story.append(P("4. Growth outlook and the 2028 targets", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
story.append(P("<b>2026 guidance (raised twice; latest August 4, 2026):</b> revenue $4.10\u20134.15b (+22\u201323% YoY) and adjusted EBITDA $720\u2013740m (+44\u201348%). The raise was driven by the Superbank consolidation and the Stash acquisition, with management noting the core business remains on track despite FX pressure.", s_body))
story.append(P("<b>2028 targets (raised September 15, 2026 alongside the Atome deal):</b>", s_body))
for t in [
    "Adjusted EBITDA of <b>$1.7 billion</b> (raised from $1.5b) \u2014 more than doubling from 2026 guidance;",
    "<b>30%+ revenue CAGR from 2025 to 2028</b>;",
    "Financial Services adjusted EBITDA of <b>$500m</b> by 2028;",
    "Combined loan portfolio <b>above $6 billion</b> by 2028 (already $2.3b at Q2 2026, +197% YoY).",
]:
    story.append(B(t))
story.append(P("<b>What drives it:</b>", s_h2))
for t in [
    "<b>Digital banks scaling toward profitability.</b> Deposits of $2.5b across GXS, GX Bank and Superbank (vs $1.6b at end-2025), 7.4m deposit customers, 60\u201393% of whom are existing Grab users \u2014 the cross-sell engine working as designed. GXS's FY2025 net loss narrowed to S$208m while its loan book tripled to S$1b and expected-credit-loss rates improved from 6.8% to 4.6%. FinSvcs adjusted EBITDA (\u2013$15m in Q2) is expected to inflect positive in H2 2026.",
    "<b>Atome (60% for $1.49b cash, closing expected Q3 2027).</b> Grab's largest-ever acquisition adds ~25m BNPL users and a ready-made lending book, underpinning the raised 2028 targets. The market hated the price (\u20133.6% on announcement) on credit-risk and overpayment concerns \u2014 the key execution debate on the stock.",
    "<b>GrabAds compounding.</b> Ad revenue hit 1.7% of Deliveries GMV in early 2025 (from 1.3% a year earlier) and continues to lift Deliveries revenue growth. This is structurally high-margin revenue layered on existing GMV.",
    "<b>AI and autonomy.</b> A platform-wide 'intelligence layer' drives pricing, underwriting and driver productivity; AI underwriting is directly powering the lending scale-up. WeRide's autonomous shuttle Ai.R began public rides in Punggol, Singapore (April 2026) with commercial operations targeted for late 2026 \u2014 a long-dated call option on driver-cost deflation.",
    "<b>Capital returns.</b> A new $750m buyback was authorized in August 2026 (cumulative $1.75b since 2024), with ~$900m still to be executed within 12 months \u2014 meaningful support at ~8% of market cap.",
]:
    story.append(B(t))

# ============ 5. MOAT & PRODUCT EVALUATION ============
story.append(P("5. Moat assessment and product evaluation", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
story.append(P("Grab's moat is <b>regional scale + super-app density</b>, not technology. We rate it a <b>narrow moat</b>: leadership positions are durable (multi-year #1 shares, driver and merchant networks that took a decade to build) but contestable at the margin by well-funded rivals, and regulators can redraw the economics overnight (see Indonesia). Sources of the moat:", s_body))
for t in [
    "<b>Two-sided network effects:</b> 53.9m monthly users and millions of driver/merchants; liquidity (short wait times, wide restaurant coverage) is the product.",
    "<b>Data flywheel in lending:</b> transaction history feeds proprietary underwriting that banks cannot replicate for thin-file borrowers.",
    "<b>Cross-sell:</b> 60\u201393% of digibank depositors are existing Grab users \u2014 customer acquisition cost near zero versus standalone neobanks.",
    "<b>Brand and habit:</b> 'Grab' is a verb in much of Southeast Asia; the app sits on the home screen.",
]:
    story.append(B(t))
story.append(P("Product-by-product evaluation:", s_h2))
prod = [
    [hdr("Product", s_theadL), hdr("Position"), hdr("Strengths"), hdr("Watch items")],
    [cell("<b>GrabFood</b>"), cell("#1 SEA, 55% GMV share"), cell("Widest coverage; GrabAds monetization; duopoly in SG after Deliveroo exit"), cell("ShopeeFood now #2; Uber-owned foodpanda from 2027")],
    [cell("<b>GrabMart / Express</b>"), cell("Leading quick-commerce"), cell("Leverages same driver fleet; grocery = higher frequency"), cell("Lower take rates than food; thin margins")],
    [cell("<b>Mobility (Car/Bike)</b>"), cell("70%+ share most markets; ~50% Indonesia"), cell("Highest on-demand margins (~8.6% of GMV); tiered pricing"), cell("Indonesia 8% commission cap; fuel-cost pass-through")],
    [cell("<b>GrabFin / PayLater</b>"), cell("Scaling fast"), cell("Loan book +197% YoY; AI underwriting; zero-CAC via app"), cell("Credit risk in downturn; Atome integration")],
    [cell("<b>Digital banks</b>"), cell("Early, sub-scale vs Sea"), cell("Deposits $2.5b; losses narrowing; ECL improving"), cell("Behind SeaBank/Monee ($11.1b book); capital-intensive")],
    [cell("<b>GrabAds</b>"), cell("Early innings"), cell("1.7% of Deliveries GMV and rising; ~100% incremental margin"), cell("Small base; merchant ad-budget sensitivity")],
]
story.append(styled_table(prod, [30*mm, 30*mm, 55*mm, 55*mm], fontsize=8))
story.append(Spacer(1, 2*mm))
story.append(P("Net: the on-demand products are best-in-class regionally; fintech is the high-beta leg \u2014 larger upside, larger credit and execution risk. Grab's product suite is stronger than any single rival's, which is precisely the super-app thesis.", s_body))

# ============ 6. COMPETITION ============
story.append(P("6. Competition", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
comp = [
    [hdr("Rival", s_theadL), hdr("Where it competes"), hdr("Threat level"), hdr("Latest")],
    [cell("<b>GoTo (Gojek)</b>"), cell("Indonesia rides + delivery; fintech"), cell("High"), cell("#2 in Indonesia (~41.5% ride-hail GMV); fintech adj.-EBITDA positive; merger speculation perennial but unconfirmed")],
    [cell("<b>ShopeeFood (Sea Ltd)</b>"), cell("Food delivery region-wide; SeaBank/Monee in lending"), cell("High"), cell("Overtook foodpanda as SEA #2 in delivery; Monee loan book $11.1b \u2014 well ahead of Grab's digibanks")],
    [cell("<b>foodpanda / Uber</b>"), cell("Delivery in SG, MY, others"), cell("Rising"), cell("Uber agreed to buy Delivery Hero for $14.8b (Jul 2026) \u2014 Grab's biggest delivery rival gets a deep-pocketed owner; Uber already ~13% Grab shareholder")],
    [cell("<b>Line Man Wongnai</b>"), cell("Thailand delivery"), cell("Medium"), cell("Strong local #2 in Thailand; no verified 2026 share data")],
    [cell("<b>Bolt / inDrive</b>"), cell("Ride-hailing, price-led"), cell("Medium"), cell("Undercut on price in select cities; limited regional scale")],
    [cell("<b>GreenSM</b>"), cell("Vietnam ride-hailing (EV fleet)"), cell("Medium"), cell(">25% Vietnam share vs Grab's 62%")],
]
story.append(styled_table(comp, [30*mm, 42*mm, 22*mm, 76*mm], fontsize=8))
story.append(Spacer(1, 2*mm))
story.append(P("The competitive temperature has cooled from the subsidy wars of 2018\u20132022 into 'affordability initiatives' and tiered pricing \u2014 better for industry margins. The two structural shifts to watch: (1) <b>Uber swallowing foodpanda's parent</b> creates a genuinely formidable delivery competitor from 2027, albeit one whose parent is also a major Grab shareholder with aligned incentives; (2) <b>Sea out-executing in fintech</b> \u2014 Monee's $11.1b loan book and positive EBITDA set the benchmark Grab's digibanks are chasing.", s_body))

# ============ 7. RISKS ============
story.append(P("7. Key risks", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
for t in [
    "<b>Regulation (the #1 risk).</b> Indonesia's Presidential Regulation 27/2026 caps two-wheel ride-hailing commissions at 8% (from 20%) effective July 1, 2026, plus mandatory driver insurance; Maybank estimates a ~3\u20136% EBITDA hit, ~10% if extended to four-wheelers. Vietnam's regulator is probing fare-setting and drivers staged a September boycott. Driver-reclassification debates simmer region-wide. Regulators, not competitors, are the historic source of Grab's worst drawdowns.",
    "<b>Atome capital allocation.</b> $1.49b cash \u2014 ~13% of market cap \u2014 for 60% of a BNPL lender, at a moment the balance sheet was a key bull argument. If credit losses spike or synergies disappoint, the 'disciplined compounder' narrative breaks.",
    "<b>Uber\u2013Delivery Hero.</b> A combined $236b-GMV behemoth could reignite delivery subsidies in Grab's most profitable markets (Singapore, Malaysia).",
    "<b>Macro and FX.</b> The 2026 fuel-price shock (Strait of Hormuz) forced elevated driver incentives; a strong dollar and ~5% US yields compress EM growth multiples. Grab reports in USD but earns in rupiah, ringgit, baht and pesos.",
    "<b>Execution on fintech.</b> Tripling a loan book in a year is how you discover your underwriting is wrong. ECL rates are improving (6.8% \u2192 4.6% at GXS), but a regional downturn would test the book.",
]:
    story.append(B(t))

# ============ 8. VALUATION ============
story.append(P("8. Valuation: three lenses, one answer", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
story.append(P("<b>Lens 1 \u2014 DCF (primary).</b> We model 2026\u20132035 revenue growing from $4.13b to $14.8b (base), with adjusted free-cash-flow margins expanding from 11% to 18% as fintech scales and incentives normalize. Net cash is taken pro forma at $3.5b ($5.0b reported less the $1.49b Atome consideration). WACC 11% base / 12% bear / 10% bull; terminal growth 3.5% / 2.5% / 4.0%.", s_body))
dcfv = [
    [hdr("Scenario", s_theadL), hdr("Key assumptions"), hdr("Implied EV"), hdr("Implied price"), hdr("Weight")],
    [cell("<b>Bear</b>"), cell("Slower growth; ID cap spreads; Atome credit losses; FCF margin peaks 15%"), cellR("$10.2 bn"), cellR("$3.12"), cellR("25%")],
    [cell("<b>Base</b>"), cell("2028 rev $6.45b / adj. EBITDA ~$1.68b (in line with mgmt $1.7b); margin to 18%"), cellR("$21.0 bn"), cellR("$6.00"), cellR("50%")],
    [cell("<b>Bull</b>"), cell("Fintech flywheel + Atome synergies; margin to 21%; possible consolidation"), cellR("$36.0 bn"), cellR("$9.65"), cellR("25%")],
    [cell("<b>Weighted</b>"), cell("25 / 50 / 25"), cell(""), cellR("<b>$6.19</b>"), cell("")],
]
story.append(styled_table(dcfv, [22*mm, 72*mm, 28*mm, 24*mm, 24*mm], fontsize=8))
story.append(Spacer(1, 2*mm))
story.append(P("<b>Lens 2 \u2014 peer multiples.</b> Grab is the cheapest name in its peer set on both sales and EBITDA, despite 22%+ revenue growth and 44\u201348% EBITDA growth \u2014 the market is pricing regulatory and execution risk, not the growth.", s_body))
mult = [
    [hdr("Company", s_theadL), hdr("EV / fwd revenue"), hdr("EV / EBITDA"), hdr("Comment")],
    [cell("<b>Grab</b>"), cellR("~1.6x"), cellR("~8.8x"), cellR("FY26E; cheapest in group")],
    [cell("Uber"), cellR("2.4x"), cellR("~14x"), cellR("Closest comp; global scale")],
    [cell("DoorDash"), cellR("4.1x"), cellR("~45\u201350x"), cellR("Premium for US growth + profitability")],
    [cell("Sea Limited"), cellR("\u2014"), cellR("~24.5x"), cellR("Fintech + e-commerce optionality")],
    [cell("GoTo"), cellR("1.7x"), cellR("13.1x"), cellR("ID-focused; similar discount")],
    [cell("Lyft"), cellR("0.7x"), cellR("~18x"), cellR("US #2; no growth premium")],
]
story.append(styled_table(mult, [32*mm, 30*mm, 30*mm, 78*mm], fontsize=8))
story.append(P("Multiples as of September 17\u201319, 2026 (FactSet via MarketWatch/TradingView; Maybank for Sea; multiples.vc for GoTo). A straight Uber-multiple re-rating (2.4x sales) would imply ~$3.60 \u2014 the DCF premium reflects that Grab's EBITDA is growing 3x faster than Uber's from a depressed base.", s_small))
story.append(Spacer(1, 2*mm))
story.append(P("<b>Lens 3 \u2014 sum of the parts (2028E).</b> On-Demand (Deliveries + Mobility) 2028E adj. EBITDA ~$1.2b at 13x (between Uber and GoTo) = $15.6b; Financial Services 2028E adj. EBITDA $0.5b (mgmt target) at 8x (fintech-growth discount) = $4.0b; pro-forma net cash $3.5b. Total equity $23.1b \u00f7 4.09b shares = <b>$5.65/share</b> \u2014 within 6% of our target.", s_body))
story.append(P("<b>Target:</b> DCF-weighted $6.19 and SOTP $5.65 bracket our <b>$6.00</b> 12-month target, implying <b>115% upside</b> from $2.79. Street consensus averages $6.01\u2013$6.11 (11 analysts: 8 Buy, 1 Strong Buy, 1 Hold, 1 Sell) \u2014 we are in line, though we note published targets look stale relative to the September price collapse.", s_small))

# ============ 9. RECOMMENDATION ============
story.append(P("9. Recommendation", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
story.append(P("We rate Grab <b><font color=\"#0E7C3E\">BUY</font></b> with a <b>$6.00</b> 12-month price target (115% upside), <b>High risk</b>. The thesis in one line: the market is valuing a dominant, newly profitable regional platform with a triple-digit-growth fintech arm at distressed multiples because of regulatory headlines and one expensive acquisition \u2014 we think the earnings power wins.", s_body))
story.append(P("<b>What gets us there (catalysts):</b> FinSvcs adjusted-EBITDA inflection in H2 2026; Q4/FY2026 results confirming the $1.7b 2028 EBITDA trajectory; Atome closing cleanly in Q3 2027 with credit metrics intact; ~$900m of buybacks executed; any softening of Indonesia's commission stance.", s_body))
story.append(P("<b>What breaks the thesis:</b> commission caps spreading to four-wheelers or food delivery; Atome credit blowup; Uber reigniting a delivery price war; a disorderly EM FX/fuel shock. Any of these would push fair value toward our $3.12 bear case \u2014 down ~12% from here on further bad news, which is why this is a starter-sized, high-risk position, not a core holding.", s_body))
story.append(P("<b>Positioning:</b> for investors who can tolerate EM regulatory volatility, Grab offers venture-like upside ($9.65 bull case, +246%) with a profitable, cash-generative core limiting the downside. Initiate at current levels; add on evidence that FinSvcs has turned EBITDA-positive or that Atome credit quality is holding.", s_body))

# ============ APPENDIX ============
story.append(P("Appendix: sources and verification notes", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
story.append(P("Company: Grab Q2 2026 press release (Aug 4, 2026); Q1 2026 release (May 5, 2026); Q4/FY2025 release (Feb 12, 2026); Atome acquisition press release (Sep 15, 2026); Q2 2026 earnings presentation; 6-K filings. Market data as of September 18, 2026 close. Press/analysis: Reuters (Indonesia commission cap Jun 2026; Uber\u2013Delivery Hero Jul/Sep 2026; Atome Sep 2026); Morningstar/Dow Jones; Momentum Works 2025 (SEA food-delivery shares); ABI Research H1 2025 (ride-hail shares); Maybank research; FactSet multiples via MarketWatch/TradingView (Sep 17, 2026); MarketBeat consensus (Sep 17, 2026); Motley Fool (Sep 12, 2026).", s_small))
story.append(Spacer(1, 2*mm))
story.append(P("Items we could not fully verify and excluded from the valuation: a reported CEO share sale on Sep 8, 2026 (single blog source, no SEC Form 4 found); the reported $600m foodpanda-Taiwan agreement (closure unconfirmed); precise Vietnam probe details; 2026 share data for Line Man Wongnai, Bolt and inDrive. GAAP profit figures include one-off gains and should be read alongside adjusted EBITDA. This analysis was prepared September 19, 2026 for informational purposes only and is not investment advice; all forward-looking statements involve risk and uncertainty.", s_small))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=18*mm,
                        title="Grab Holdings (GRAB) \u2014 Equity Research Note", author="Investment Research")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("wrote", OUT)
