#!/usr/bin/env python3
"""Build the Booking Holdings equity research note PDF."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, HRFlowable)
from reportlab.graphics.shapes import Drawing, String, Rect
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.lib import colors

OUT_DIR = "/home/hatch/workspace/your_files/booking-holdings-equity-research"
os.makedirs(OUT_DIR, exist_ok=True)
OUT = os.path.join(OUT_DIR, "booking-holdings-equity-research-note.pdf")

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
    canvas.drawString(18*mm, 12*mm, "Booking Holdings Inc. (NASDAQ: BKNG)  \u2014  Equity Research Note  \u2014  September 2026")
    canvas.drawRightString(W - 18*mm, 12*mm, f"Page {doc.page}")
    canvas.setStrokeColor(MGRAY); canvas.setLineWidth(0.5)
    canvas.line(18*mm, 14.5*mm, W - 18*mm, 14.5*mm)
    canvas.restoreState()

# ============ COVER ============
story.append(Spacer(1, 26*mm))
story.append(P("BOOKING HOLDINGS INC.", ParagraphStyle("x", parent=s_sub, fontName="Helvetica-Bold", fontSize=13, textColor=ACCENT, spaceAfter=2)))
story.append(P("The Toll Road of Global Travel<br/>at a Discount to Its Own History", s_title))
story.append(Spacer(1, 4*mm))
story.append(P("Equity Research Note  \u00b7  Consumer Discretionary \u2014 Online Travel  \u00b7  September 19, 2026", s_sub))
story.append(Spacer(1, 8*mm))

rating_data = [
    [cell("Recommendation", s_theadL), cell("12-Mo. Price Target", s_thead), cell("Current Price", s_thead), cell("Implied Upside", s_thead), cell("Risk Rating", s_thead)],
    [Paragraph("<b><font color=\"#0E7C3E\" size=\"13\">BUY</font></b>", s_cellC),
     Paragraph("<b><font size=\"12\">$222.00</font></b>", s_cellC),
     Paragraph("<b>$167.90</b><br/><font size=\"7\" color=\"#5A6472\">Sep 18, 2026 close</font>", s_cellC),
     Paragraph("<b><font color=\"#0E7C3E\">+32%</font></b>", s_cellC),
     Paragraph("<b>Med-High</b><br/><font size=\"7\" color=\"#5A6472\">Beta ~1.16</font>", s_cellC)],
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
    ["Market cap", "~$128 bn", "Shares out.", "~816 mn (post-split)"],
    ["Enterprise value", "~$131 bn", "52-week range", "$150.14 \u2013 $225.00"],
    ["Net debt (6/30/26)", "~$3.0 bn", "YTD / 1-yr return", "-21.6% / -22.9%"],
    ["FY2025 revenue", "$26.9 bn (+13%)", "FY2025 adj. EBITDA", "$9.9 bn (36.9%)"],
    ["FY2025 free cash flow", "$9.1 bn (33.8%)", "2026E adj. EPS (cons.)", "~$10.42 (+14\u201315%)"],
    ["Analyst consensus", "38 Buy / 8 Hold / 0 Sell", "Consensus price target", "~$239 (+42%)"],
    ["Next catalyst", "Q3'26 earnings, ~Oct 27", "2026E revenue (cons.)", "~$29.3 bn (+9%)"],
]
sd = [[cell(r[0], s_cellB), cell(r[1], s_cell), cell(r[2], s_cellB), cell(r[3], s_cell)] for r in snap]
story.append(styled_table([[cell("Snapshot", s_theadL), cell("", s_thead), cell("", s_thead), cell("", s_thead)]] + sd,
                   [38*mm, 38*mm, 38*mm, 56*mm], header_rows=1))
story.append(Spacer(1, 6*mm))
story.append(P("Basis note: BKNG effected a 25-for-1 stock split on April 2, 2026 (pre-split close $4,269.99). All per-share figures in this note "
               "are post-split; FY2023\u201325 GAAP/adjusted EPS reported pre-split have been divided by 25.", s_small))
story.append(Spacer(1, 4*mm))
story.append(P("This note is an independent research-style analysis for informational purposes only and is not investment advice. "
               "Figures are drawn from Booking Holdings' SEC filings, earnings releases, and reputable financial press as of September 19, 2026. "
               "Projections are the author's estimates.", s_small))
story.append(PageBreak())

# ============ 1. EXECUTIVE SUMMARY ============
story.append(P("1 &nbsp; Executive Summary", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Booking Holdings (BKNG) is the largest and most profitable online travel agency in the world, trading at <b>$167.90 \u2014 down ~23% "
               "over the past year and within 12% of its 52-week low</b>. The selloff has a price tag on it: the market is discounting BKNG for three "
               "things \u2014 Google's AI-driven disintermediation of travel search, the EU's DMA gatekeeper enforcement hanging over Booking.com, "
               "and a softer-than-feared Q3'26 guide (revenue below consensus). Against that stands a business putting up the best numbers in the "
               "industry: 36.9% adjusted EBITDA margins, $9.1 bn of free cash flow (1.7x net income), high-single-digit bookings growth, and a "
               "buyback machine that has retired 21% of shares since 2022.", s_body))
story.append(P("We rate BKNG a <b>BUY</b> with a <b>$222.00</b> 12-month price target (~32% upside). Our thesis: BKNG trades at ~12.8x EV/EBITDA and "
               "~16x forward earnings versus a 3-year average of 16\u201317.5x and a historical 20\u201325x P/E \u2014 a full re-rating gap for a "
               "company growing revenue 9\u201313% with expanding margins. The structural economics are intact: the agency-to-merchant migration "
               "lifts take rates (14.5% and rising), Genius loyalty and the app keep direct traffic above 50%, and a $650 mn transformation program "
               "defends margins against marketing inflation. We set our target <i>below</i> the Street's $239 \u2014 we fully charge the DMA fine "
               "overhang and the AI-search risk in our scenario weights until both are resolved.", s_body))

story.append(P("Investment thesis \u2014 why own it", s_h2))
for b in [
    "<b>The toll road of global travel, on sale.</b> 1.235 <i>billion</i> room nights in 2025 (8% growth), $186 bn of gross bookings, 9.1 mn listings "
    "across 220+ countries. No competitor operates at this scale \u2014 and scale funds the lowest effective customer-acquisition cost in the industry.",
    "<b>The best unit economics in online travel.</b> 36.9% adjusted EBITDA margin and 33.8% FCF margin \u2014 roughly double Expedia's EBITDA margin "
    "and ~2.7x Trip.com's. FCF ($9.1 bn) persistently exceeds net income because merchant-of-record float produces structurally negative working capital.",
    "<b>Merchant migration is a hidden take-rate engine.</b> 73% of Q2'26 gross bookings now flow through Booking.com Payments (from 54% in 2023). "
    "Card rebates plus payments revenue let revenue compound at or above bookings growth even with flat accommodation commissions.",
    "<b>Loyalty + app = defense against Google.</b> Genius Levels 2/3 drive high-50% of room nights at materially higher direct-booking rates; the "
    "direct channel is mid-50% of room nights (mid-60s% in the U.S.). That is the structural answer to rising CPCs and AI search.",
    "<b>Shareholder returns are relentless.</b> $7.3 bn of buybacks in H1'26 alone (record $4.1 bn returned in Q2), $14.5 bn of authorization "
    "remaining, and a dividend raised 9.4% to $1.68/share annualized. This is a compounder that shrinks its share count ~5% per year.",
]:
    story.append(B(b))

story.append(P("Key risks \u2014 why the market is scared", s_h2))
for b in [
    "<b>EU DMA enforcement.</b> Booking.com has been a DMA gatekeeper since May 2024; in April 2026 the European Parliament explicitly named its "
    "\"prohibited parity clauses\" as non-compliance needing urgent enforcement. No fine has been announced \u2014 fines can reach 10% of worldwide "
    "turnover (~$2.7 bn). This is the single biggest valuation overhang.",
    "<b>Google AI disintermediation.</b> An August 2026 study of 4,000 Google AI Mode hotel queries found 79% of clicks stay inside Google; OTAs "
    "capture just 3.6%. Marketing spend (+11% y/y in Q2'26) is already growing faster than bookings (+9%).",
    "<b>Travel cyclicality and geopolitics.</b> Q2'26 showed Middle East conflict denting long-haul demand and shortening booking windows; "
    "2020 remains the downside template (~50% room-night decline in a severe shock).",
    "<b>Competition is not standing still.</b> Airbnb (8M+ listings, 64% app penetration) fights the alt-accommodation battle; Expedia's B2B is "
    "compounding at 26% y/y; Trip.com overlaps in Asia. The U.S. remains BKNG's weak spot versus Airbnb.",
]:
    story.append(B(b))

# ============ 2. COMPANY OVERVIEW ============
story.append(P("2 &nbsp; Company Overview \u2014 What Booking Holdings Is and What It Is Doing", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Booking Holdings Inc., headquartered in Norwalk, Connecticut (with its economic center of gravity in the Netherlands \u2014 "
               "~81% of FY2025 revenue was booked through its Dutch entity), is the world's largest online travel agency. CEO Glenn Fogel has run "
               "the company since 2017. The portfolio: <b>Booking.com</b> (the flagship, acquired for $133 mn in 2005 \u2014 one of the great "
               "acquisitions in business history), <b>Priceline</b>, <b>Agoda</b> (Asia), <b>KAYAK</b> (meta-search; $457 mn impairment taken in "
               "2025), <b>OpenTable</b>, and <b>Rentalcars.com</b>. The company reports a single operating segment \u2014 online travel and related "
               "services \u2014 with revenue disaggregated by type.", s_body))
story.append(P("The defining structural shift in the business is the <b>agency-to-merchant migration</b> at Booking.com. Merchant revenue has gone "
               "from 51% of revenue in 2023 to 66% in 2025 (agency 44% \u2192 30%); 73% of Q2'26 gross bookings flowed through Booking.com Payments "
               "as merchant of record. The payoff: card rebates, incremental payments revenue, and negative working capital that converts operating "
               "profit into free cash flow at ~1.7x net income.", s_body))
story.append(P("What the company is doing right now \u2014 the 2026 strategic agenda", s_h2))
for b in [
    "<b>Connected Trip.</b> The cross-sell engine: transactions spanning two or more verticals (stay + flight/car/attraction) are now a low-double-digit "
    "share of all bookings and growing ~2x the overall rate (high-20s% growth in FY2025). This is BKNG's answer to Airbnb's stays-centric model \u2014 "
    "a bigger share of the travel wallet per customer.",
    "<b>Genius loyalty deepening.</b> Levels 2 and 3 (10\u201320% discounts plus perks) account for a high-50% share of room nights with materially "
    "higher direct-booking rates \u2014 the flywheel that keeps performance-marketing dependence in check.",
    "<b>AI at scale.</b> Management says AI has been deployed \"at scale for more than a decade\"; the 2026 push adds the GenAI Trip Planner "
    "(booking-integrated, early ChatGPT App Store presence) and a GenAI Smart Messenger cutting customer-service cost per booking by double-digit "
    "percentages. A $700 mn above-baseline 2026 reinvestment funds GenAI/agentic commerce, Connected Trip, Asia and U.S. marketing.",
    "<b>Transformation program.</b> Target raised on the Q2'26 call to <b>~$650 mn of annual run-rate savings by end-2027</b> (from $550 mn) \u2014 "
    "the margin defense against marketing inflation.",
    "<b>Alternative accommodations.</b> ~37% of Booking.com room nights (+4% y/y in Q2'26) \u2014 the only major OTA with a credible Airbnb alternative "
    "built inside a hotel platform; the U.S. remains the gap to close.",
]:
    story.append(B(b))

# ============ 3. FINANCIAL ANALYSIS ============
story.append(P("3 &nbsp; Financial Analysis", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Three years of compounding: revenue +26% cumulatively, adjusted EBITDA +41%, and a margin trajectory that is the envy of the "
               "industry. FY2025 GAAP net income dipped 8% on higher taxes and discrete items \u2014 adjusted EPS still grew 22%, which is the "
               "number that matters for the compounding story.", s_body))
fin = [
    [cell("$ mn", s_theadL), cell("2023", s_thead), cell("2024", s_thead), cell("2025", s_thead), cell("2026E*", s_thead)],
    [cell("Revenue", s_cellB), cell("21,365", s_cellR), cell("23,739", s_cellR), cell("26,917", s_cellR), cell("29,300", s_cellR)],
    [cell("YoY growth", s_cell), cell("+25%", s_cellR), cell("+11%", s_cellR), cell("+13%", s_cellR), cell("+9%", s_cellR)],
    [cell("Gross bookings ($ bn)", s_cell), cell("150.6", s_cellR), cell("165.6", s_cellR), cell("186.1", s_cellR), cell("~202", s_cellR)],
    [cell("Room nights (mn)", s_cell), cell("1,049", s_cellR), cell("1,144", s_cellR), cell("1,235", s_cellR), cell("~1,300", s_cellR)],
    [cell("Take rate (rev / GB)", s_cell), cell("14.2%", s_cellR), cell("14.3%", s_cellR), cell("14.5%", s_cellR), cell("14.5%", s_cellR)],
    [cell("Operating income / margin", s_cellB), cell("5,835 / 27.3%", s_cellR), cell("7,555 / 31.8%", s_cellR), cell("8,825 / 32.8%", s_cellR), cell("\u2014 / ~33%", s_cellR)],
    [cell("Adjusted EBITDA / margin", s_cellB), cell("~7,000 / ~33%", s_cellR), cell("8,300 / 35.0%", s_cellR), cell("9,900 / 36.9%", s_cellR), cell("~10,750 / ~36.7%", s_cellR)],
    [cell("GAAP net income", s_cell), cell("4,289", s_cellR), cell("5,882", s_cellR), cell("5,404", s_cellR), cell("\u2014", s_cellC)],
    [cell("Adj. EPS (post-split)", s_cellB), cell("$6.08", s_cellR), cell("$7.48", s_cellR), cell("$9.12", s_cellR), cell("$10.42", s_cellR)],
    [cell("Free cash flow", s_cellB), cell("7,000", s_cellR), cell("7,900", s_cellR), cell("9,100", s_cellR), cell("~10,200", s_cellR)],
]
story.append(styled_table(fin, [46*mm, 28*mm, 28*mm, 28*mm, 28*mm]))
story.append(P("*2026E: consensus/derived estimates; adjusted EPS per-share figures converted to post-split basis (\u00f725). Sources: BKNG 10-K "
               "FY2025, Q1'26/Q2'26 releases, 2026 proxy statement.", s_small))

d = Drawing(430, 190)
d.add(String(215, 178, "Revenue vs. Adjusted EBITDA ($ mn), 2023\u20132026E", fontName="Helvetica-Bold", fontSize=10, textAnchor="middle", fillColor=NAVY))
bc = VerticalBarChart(); bc.x = 45; bc.y = 30; bc.height = 120; bc.width = 340
bc.data = [[21365, 23739, 26917, 29300], [7000, 8300, 9900, 10750]]
bc.strokeColor = None; bc.barLabels.nudge = 8; bc.barLabelFormat = "%d"
bc.bars[0].fillColor = NAVY; bc.bars[1].fillColor = ACCENT
bc.categoryAxis.categoryNames = ["2023", "2024", "2025", "2026E"]
bc.valueAxis.valueMin = 0; bc.valueAxis.valueMax = 32000; bc.valueAxis.valueStep = 8000
bc.valueAxis.labels.fontSize = 7; bc.categoryAxis.labels.fontSize = 8
d.add(bc)
for i, lab in enumerate(["Revenue", "Adj. EBITDA"]):
    d.add(Rect(300 + i*95, 12, 12, 8, fillColor=[NAVY, ACCENT][i], strokeColor=None))
    d.add(String(316 + i*95, 14, lab, fontName="Helvetica", fontSize=8, fillColor=DGRAY))
story.append(d)
story.append(Spacer(1, 2*mm))

story.append(P("Quarterly pulse \u2014 Q2'26 beat, Q3'26 guided soft", s_h2))
q = [
    [cell("", s_theadL), cell("Q3'25", s_thead), cell("Q4'25", s_thead), cell("Q1'26", s_thead), cell("Q2'26", s_thead)],
    [cell("Revenue ($ mn)", s_cellB), cell("8,583", s_cellR), cell("6,067", s_cellR), cell("6,779", s_cellR), cell("7,352", s_cellR)],
    [cell("YoY growth", s_cell), cell("+13%", s_cellR), cell("+15%", s_cellR), cell("+16%", s_cellR), cell("+8%", s_cellR)],
    [cell("Room nights (mn)", s_cell), cell("368", s_cellR), cell("261", s_cellR), cell("293", s_cellR), cell("325", s_cellR)],
    [cell("Gross bookings ($ bn)", s_cell), cell("48.4", s_cellR), cell("42.6", s_cellR), cell("46.7", s_cellR), cell("51.0", s_cellR)],
    [cell("Adj. EBITDA ($ mn)", s_cell), cell("3,327", s_cellR), cell("2,074", s_cellR), cell("2,265", s_cellR), cell("2,650", s_cellR)],
    [cell("Adj. EPS (post-split)", s_cell), cell("$2.67", s_cellR), cell("$1.92", s_cellR), cell("$2.22", s_cellR), cell("$2.54", s_cellR)],
]
story.append(styled_table(q, [52*mm, 28*mm, 28*mm, 28*mm, 28*mm]))
story.append(P("Q2'26 (Aug 4) beat across the board \u2014 room nights 325 mn (+5%) vs. ~320.5 mn expected, bookings $51.0 bn vs. $49.4 bn, revenue "
               "$7.35 bn (+2.3% beat), adjusted EPS $2.54 (+15%) vs. ~$2.44 expected \u2014 then management guided Q3'26 revenue "
               "(+$4\u20136%) below the ~$9.71 bn consensus. The stock popped ~6% on the print and faded; it is down ~20% YTD. Read-through: "
               "demand is resilient, but the guide says management is not chasing the Street's number into a geopolitically noisy H2.", s_body))

story.append(P("Balance sheet, cash flow &amp; capital allocation", s_h2))
for b in [
    "<b>Fortress with leverage optics.</b> $17.2 bn cash &amp; investments (6/30/26) against $20.2 bn of debt \u2192 net debt only ~$3.0 bn, or "
    "<b>~0.29x TTM adjusted EBITDA</b>. Book equity is negative (~$10.8 bn deficit) \u2014 a known artifact of cumulative buybacks, not distress; "
    "the company is investment-grade and self-funding.",
    "<b>FCF is the crown jewel.</b> $9.1 bn in FY2025 (33.8% of revenue, +15% y/y), tracking ~$9.6\u201310.2 bn in 2026E. FCF persistently exceeds "
    "net income (1.7x in FY2025) because the merchant-of-record float produces negative working capital \u2014 customers' money funds the business.",
    "<b>Buyback machine, accelerating.</b> FY23 >$10 bn (share count \u20139% y/y), FY24 ~$6.0 bn, FY25 $5.9 bn, and <b>$7.3 bn in H1'26 alone</b> "
    "($3.6 bn Q1 + $3.7 bn Q2) \u2014 buying the dip aggressively. $21.8 bn of authorization at end-2025; <b>$14.5 bn remains</b> (6/30/26).",
    "<b>Dividend, raised steadily.</b> Initiated Q1'24 at $8.75/qtr (pre-split); raised to $9.60 (2025, +9.7%) and $10.50 (2026, +9.4%) \u2014 "
    "<b>$0.42/qtr post-split, $1.68 annualized, ~1.0% yield</b>, ~$1.2 bn of annual cash at an 18\u201323% payout ratio. Buyback-first, dividend-second: "
    "exactly right for a compounder.",
]:
    story.append(B(b))

# ============ 4. GROWTH OUTLOOK & PROJECTIONS ============
story.append(P("4 &nbsp; Growth Outlook &amp; Forward Projections", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("We model revenue compounding at ~8.6% (2025\u201330) with adjusted EBITDA margins expanding from 36.9% to ~39.6% \u2014 conservative "
               "versus management's low-double-digit FY26 revenue guide and consensus, which leaves room for the transformation savings and "
               "merchant-mix lift to surprise to the upside. FCF compounds faster than revenue (~12% CAGR) on margin expansion and the float.", s_body))
proj = [
    [cell("$ mn", s_theadL), cell("2025A", s_thead), cell("2026E", s_thead), cell("2027E", s_thead), cell("2028E", s_thead), cell("2029E", s_thead), cell("2030E", s_thead)],
    [cell("Revenue", s_cellB), cell("26,917", s_cellR), cell("29,300", s_cellR), cell("32,000", s_cellR), cell("34,900", s_cellR), cell("37,800", s_cellR), cell("40,700", s_cellR)],
    [cell("Growth", s_cell), cell("13%", s_cellR), cell("9%", s_cellR), cell("9%", s_cellR), cell("9%", s_cellR), cell("8%", s_cellR), cell("8%", s_cellR)],
    [cell("Adj. EBITDA", s_cellB), cell("9,900", s_cellR), cell("10,750", s_cellR), cell("11,900", s_cellR), cell("13,300", s_cellR), cell("14,700", s_cellR), cell("16,100", s_cellR)],
    [cell("Margin", s_cell), cell("36.9%", s_cellR), cell("36.7%", s_cellR), cell("37.2%", s_cellR), cell("38.1%", s_cellR), cell("38.9%", s_cellR), cell("39.6%", s_cellR)],
    [cell("Free cash flow", s_cellB), cell("9,100", s_cellR), cell("10,200", s_cellR), cell("11,600", s_cellR), cell("13,200", s_cellR), cell("14,700", s_cellR), cell("16,300", s_cellR)],
]
story.append(styled_table(proj, [30*mm, 25*mm, 25*mm, 25*mm, 25*mm, 25*mm, 25*mm]))
story.append(P("Author estimates; 2026E revenue/adj. EPS anchored to consensus. FCF \u2248 adj. EBITDA less capex, cash taxes and WC (structurally "
               "negative WC).", s_small))

d2 = Drawing(430, 190)
d2.add(String(215, 178, "Projected Revenue & Adj. EBITDA Margin (2025A\u20132030E)", fontName="Helvetica-Bold", fontSize=10, textAnchor="middle", fillColor=NAVY))
bc2 = VerticalBarChart(); bc2.x = 45; bc2.y = 30; bc2.height = 120; bc2.width = 340
bc2.data = [[26917, 29300, 32000, 34900, 37800, 40700]]
bc2.strokeColor = None; bc2.bars[0].fillColor = NAVY; bc2.barLabels.nudge = 8; bc2.barLabelFormat = "%d"
bc2.categoryAxis.categoryNames = ["2025A", "2026E", "2027E", "2028E", "2029E", "2030E"]
bc2.valueAxis.valueMin = 0; bc2.valueAxis.valueMax = 44000; bc2.valueAxis.valueStep = 11000
bc2.valueAxis.labels.fontSize = 7; bc2.categoryAxis.labels.fontSize = 8
d2.add(bc2)
d2.add(String(215, 12, "Margin path: 36.9% \u2192 36.7% \u2192 37.2% \u2192 38.1% \u2192 38.9% \u2192 39.6%  (transformation program: ~$650 mn run-rate savings by end-2027)",
             fontName="Helvetica-Oblique", fontSize=8, textAnchor="middle", fillColor=DGRAY))
story.append(d2)
story.append(Spacer(1, 2*mm))

story.append(P("Growth bridges (2026\u20132030)", s_h2))
for b in [
    "<b>Merchant-mix take-rate lift (~25% of growth).</b> Every point of merchant share adds payments revenue and float at near-zero marginal CAC; "
    "take rate 14.2% \u2192 14.5% in two years with accommodation commissions flat.",
    "<b>Connected Trip cross-sell (~25%).</b> Multi-vertical bookings growing ~2x the overall rate; a bigger share of each traveler's wallet with "
    "lower blended acquisition cost.",
    "<b>Asia-Pacific and ROW (~20%).</b> Agoda-led APAC positioning in the fastest-growing travel market; mid-single-digit room-night growth with "
    "room to accelerate as outbound travel normalizes.",
    "<b>U.S. share gains (~15%).</b> BKNG is under-indexed in the U.S. versus Expedia/Airbnb; Genius penetration and the app habit are the "
    "weapons \u2014 mid-60s% direct-booking rates in the U.S. already.",
    "<b>AI-driven cost leverage (~15%).</b> ~$650 mn transformation savings by end-2027 plus GenAI customer-service costs down double-digits per "
    "booking \u2014 margin expansion without pricing power games.",
]:
    story.append(B(b))

# ============ 5. MOAT ============
story.append(P("5 &nbsp; Moat Assessment", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Booking Holdings has the <b>widest moat in online travel</b> \u2014 two-sided network effects, brand scale, and a loyalty/app habit "
               "that competitors cannot replicate cheaply. We score each pillar:", s_body))
moat = [
    [cell("Moat pillar", s_theadL), cell("Strength", s_thead), cell("Evidence", s_thead)],
    [cell("Two-sided network effects", s_cellB), cell("Strong", s_cellC), cell("9.1 mn listings (+8% y/y) across 220+ countries \u2192 best inventory draws travelers \u2192 traffic funds the lowest effective CAC in the industry.", s_cell)],
    [cell("Brand &amp; distribution", s_cellB), cell("Strong", s_cellC), cell("Booking.com is the default accommodation brand in Europe and much of Asia; 1.235 bn annual room nights = unmatched demand liquidity.", s_cell)],
    [cell("Loyalty &amp; app habit", s_cellB), cell("Strong", s_cellC), cell("Genius L2/L3 = high-50% of room nights; app = high-50% of room nights; direct channel mid-50% (mid-60s% in the U.S.) \u2014 the structural defense against Google CPC inflation.", s_cell)],
    [cell("Payments float", s_cellB), cell("Moderate\u2013Strong", s_cellC), cell("73% merchant-of-record mix; FCF 1.7x net income via negative working capital. A cash-conversion moat Expedia has not matched (its merchant mix trails).", s_cell)],
    [cell("Scale cost advantage", s_cellB), cell("Moderate", s_cellC), cell("$26.9 bn revenue on a largely fixed tech/marketing base; 36.9% EBITDA margin vs. Expedia 23.8%. Transformation program adds $650 mn of run-rate savings.", s_cell)],
    [cell("Switching costs", s_cellB), cell("Weak\u2013Moderate", s_cellC), cell("Travelers multi-home (Google, direct hotel sites). Genius tiers and the app create soft lock-in; Connected Trip deepens it.", s_cell)],
]
story.append(styled_table(moat, [36*mm, 26*mm, 118*mm]))
story.append(P("Net: a <b>wide moat</b>, but one under active siege from two directions \u2014 regulatory (DMA parity-clause enforcement) and "
               "technological (Google AI search capturing the top of the funnel). The moat widens if the DMA overhang resolves without a "
               "business-model-breaking remedy and if direct/app share keeps climbing; it narrows if AI search permanently inserts Google between "
               "travelers and OTAs.", s_body))

# ============ 6. COMPETITION ============
story.append(P("6 &nbsp; Competitive Landscape", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("BKNG is <b>the largest OTA by bookings and by far the most profitable</b>. The industry is a four-player global oligopoly \u2014 "
               "Booking, Expedia, Airbnb, Trip.com \u2014 with Google as the frenemy that controls the funnel. On every scale and profitability "
               "metric that matters, BKNG leads; the market's discount is about the future of the funnel, not the present economics.", s_body))
comp = [
    [cell("Operator", s_theadL), cell("Gross bookings", s_thead), cell("Adj. EBITDA margin", s_thead), cell("EV / EBITDA", s_thead), cell("Threat assessment", s_thead)],
    [cell("Booking Holdings", s_cellB), cell("$186 bn", s_cellC), cell("<b>36.9%</b>", s_cellC), cell("~12.8x", s_cellC), cell("Scale + margin leader; discount to own history is the opportunity.", s_cell)],
    [cell("Expedia (EXPE)", s_cellB), cell("$119.6 bn", s_cellC), cell("23.8%", s_cellC), cell("~9.1x", s_cellC), cell("The value alternative; B2B compounding at 26% y/y (17th straight quarter of DD growth); Vrbo. Cheaper, weaker margins.", s_cell)],
    [cell("Airbnb (ABNB)", s_cellB), cell("$91.3 bn GBV", s_cellC), cell("35% (FCF 38%)", s_cellC), cell("~14\u201316x NTM", s_cellC), cell("The alt-accommodation benchmark: 8M+ listings, 64% app penetration, no loyalty program (BKNG's opening). Richer multiple, take-rate compressing.", s_cell)],
    [cell("Trip.com (TCOM)", s_cellB), cell("~$157 bn", s_cellC), cell("~25% op margin", s_cellC), cell("~10.7x", s_cellC), cell("Cheapest multiple; Asia overlap with Agoda. China-macro and ADR overhang explain the discount.", s_cell)],
    [cell("Google (travel)", s_cellB), cell("n/a \u2013 funnel", s_cellC), cell("n/a", s_cellC), cell("n/a", s_cellC), cell("Controls the top of the funnel; AI Mode keeps 79% of hotel clicks in-Google. Frenemy: BKNG is also its biggest travel advertiser.", s_cell)],
]
story.append(styled_table(comp, [34*mm, 22*mm, 28*mm, 24*mm, 72*mm]))
story.append(P("FY2025 figures; multiples as of mid-September 2026 (free-source providers; convention differences are directionally consistent). "
               "Sources: BKNG/EXPE/ABNB/TCOM filings; financecharts; valueinvesting.io.", s_small))

d3 = Drawing(430, 175)
d3.add(String(215, 165, "FY2025 Adjusted EBITDA Margin \u2014 BKNG vs. Peers", fontName="Helvetica-Bold", fontSize=10, textAnchor="middle", fillColor=NAVY))
margs = [("Booking 36.9%", 36.9, NAVY), ("Airbnb ~35%", 35, HexColor("#1F6F43")), ("Trip.com ~25%", 25, GOLD),
         ("Expedia 23.8%", 23.8, DGRAY)]
y = 135
for name, pct, col in margs:
    wbar = pct * 9.0
    d3.add(Rect(110, y, wbar, 16, fillColor=col, strokeColor=None))
    d3.add(String(105, y + 4, name, fontName="Helvetica", fontSize=8, textAnchor="end", fillColor=DGRAY))
    d3.add(String(110 + wbar + 6, y + 4, f"{pct}%", fontName="Helvetica-Bold", fontSize=8, fillColor=DGRAY))
    y -= 26
story.append(d3)

story.append(P("Competitive dynamics to watch:", s_h2))
for b in [
    "<b>The margin gap is the moat, quantified.</b> BKNG earns 36.9% EBITDA margins vs. Expedia's 23.8% on a business 55% larger in bookings \u2014 "
    "that is operating leverage, not accounting. Airbnb matches on margin but at half the bookings and 3x the multiple.",
    "<b>Expedia is the credible #2, not a disruptor.</b> Its B2B engine (26% y/y) and Vrbo give it two growth legs BKNG lacks, and at ~9x EV/EBITDA "
    "it is the defensive value alternative. But it trails on take rate (12.3% vs. 14.5%) and merchant-mix maturity.",
    "<b>The real fight is the funnel, not each other.</b> Google's AI search and DMA enforcement are common-mode risks to all OTAs; BKNG's "
    "direct/app share is its best shield \u2014 and its scale makes every point of direct shift worth ~$190 mn of bookings economics.",
]:
    story.append(B(b))

# ============ 7. PRODUCT EVALUATION ============
story.append(P("7 &nbsp; Product Evaluation", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("BKNG is the only travel platform with a full vertical stack \u2014 stays, flights, cars, attractions, restaurants \u2014 which is "
               "what makes the Connected Trip strategy structurally possible. Competitors are best-in-class in one vertical; BKNG is the only "
               "credible everything-store.", s_body))
prod = [
    [cell("Product / vertical", s_theadL), cell("Scale / status", s_thead), cell("Economics", s_thead), cell("Verdict", s_thead)],
    [cell("Booking.com (accommodation)", s_cellB), cell("9.1 mn listings; 1.235 bn room nights (FY25); ~37% alt-accommodations", s_cell), cell("Take rate ~14.5%; merchant 73% of GB; Genius drives direct", s_cell), cell("<b>A.</b> The category killer; alt-accommodation build is the Airbnb hedge.", s_cell)],
    [cell("Flights", s_cellB), cell("68 mn tickets sold in 2025 (36 mn in 2023)", s_cell), cell("Lower take rate; acquisition funnel for stays", s_cell), cell("<b>B+.</b> 89% growth in two years; feeds Connected Trip.", s_cell)],
    [cell("Rentalcars.com + attractions", s_cell), cell("88 mn rental-car days; FareHarbor experiences", s_cell), cell("Attach revenue; high incremental margin", s_cell), cell("<b>B.</b> Solid attach verticals; not standalone differentiators.", s_cell)],
    [cell("Priceline / Agoda", s_cellB), cell("U.S. value brand; Asia OTA leader", s_cell), cell("Agoda = APAC growth engine; Priceline stable", s_cell), cell("<b>B+.</b> Right regional coverage; Agoda faces Trip.com.", s_cell)],
    [cell("KAYAK (meta-search)", s_cell), cell("$457 mn impairment in 2025", s_cell), cell("Meta-search squeezed by Google", s_cell), cell("<b>C.</b> Structurally challenged; Google owns meta-search now.", s_cell)],
    [cell("OpenTable (+ Libro 2026)", s_cell), cell("Restaurant reservations; Libro adds Canada", s_cell), cell("Connected Trip restaurant leg", s_cell), cell("<b>B.</b> Niche but strategic; completes the trip stack.", s_cell)],
    [cell("Genius loyalty + app", s_cellB), cell("L2/L3 = high-50% of room nights; app = high-50%", s_cell), cell("Direct channel mid-50% (mid-60s% U.S.); lowers CAC", s_cell), cell("<b>A.</b> The economic engine of the moat.", s_cell)],
]
story.append(styled_table(prod, [38*mm, 48*mm, 48*mm, 46*mm]))
story.append(P("Product thesis in one line: Booking.com acquires at global scale, Genius and the app retain at low CAC, flights/cars/attractions "
               "expand the wallet, and Booking.com Payments converts it all into float \u2014 the industry's most complete flywheel.", s_body))

# ============ 8. VALUATION ============
story.append(P("8 &nbsp; Valuation", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("We triangulate fair value with (a) a scenario-weighted DCF \u2014 the primary method, appropriate for a cash-compounder with "
               "negative working capital \u2014 and (b) trading multiples as a cross-check. Key inputs: ~816 mn diluted shares (post-split), "
               "net debt ~$3.0 bn, FY2025 FCF $9.1 bn compounding to $16.3 bn by 2030 in our base case.", s_body))

story.append(P("8.1 &nbsp; Discounted cash flow \u2014 three scenarios", s_h2))
dcf = [
    [cell("Scenario", s_theadL), cell("Revenue CAGR '25\u2013'30", s_thead), cell("2030 EBITDA margin", s_thead), cell("WACC / g", s_thead), cell("Value / share", s_thead)],
    [cell("Bear \u2014 AI disintermediation bites; DMA fine + remedy; marketing inflation persists", s_cell), cell("~4.5%", s_cellC), cell("30%", s_cellC), cell("12.0% / 2.0%", s_cellC), cell("<b>$121</b>", s_cellBR)],
    [cell("Base \u2014 merchant mix + Genius + transformation; direct share keeps climbing", s_cell), cell("~8.6%", s_cellC), cell("39.6%", s_cellC), cell("10.5% / 3.0%", s_cellC), cell("<b>$222</b>", s_cellBR)],
    [cell("Bull \u2014 Connected Trip inflects; U.S. share gains; AI as tailwind not threat", s_cell), cell("~12.5%", s_cellC), cell("42%+", s_cellC), cell("10.0% / 3.5%", s_cellC), cell("<b>$290</b>", s_cellBR)],
]
story.append(styled_table(dcf, [62*mm, 28*mm, 28*mm, 24*mm, 28*mm]))

d4 = Drawing(430, 165)
d4.add(String(215, 155, "DCF Scenario Values vs. Current Price ($)", fontName="Helvetica-Bold", fontSize=10, textAnchor="middle", fillColor=NAVY))
vals = [("Current $167.90", 167.90, DGRAY), ("Bear $121", 121, RED), ("Base $222", 222, ACCENT), ("Bull $290", 290, NAVY)]
x = 60
for name, v, col in vals:
    h = v * 0.44
    d4.add(Rect(x, 30, 55, h, fillColor=col, strokeColor=None))
    d4.add(String(x + 27.5, 30 + h + 6, f"${v:g}", fontName="Helvetica-Bold", fontSize=9, textAnchor="middle", fillColor=col))
    d4.add(String(x + 27.5, 18, name.split(" ")[0], fontName="Helvetica", fontSize=8, textAnchor="middle", fillColor=DGRAY))
    x += 95
story.append(d4)

story.append(P("<b>Scenario weighting:</b> Base 50% \u00d7 $222 + Bull 30% \u00d7 $290 + Bear 20% \u00d7 $121 = <b>$222.00 target</b>. "
               "The bear case fully charges the DMA overhang (a 10%-of-turnover fine is ~$2.7 bn \u2014 roughly one year of FCF, survivable but "
               "material) and assumes Google's AI funnel permanently raises CAC. The 20% bear weight is the price of intellectual honesty on the "
               "two genuine overhangs.", s_body))

story.append(P("8.2 &nbsp; Multiples cross-check", s_h2))
mult = [
    [cell("Multiple", s_theadL), cell("BKNG today", s_thead), cell("Implied by $222 target", s_thead), cell("Context", s_thead)],
    [cell("P / E (2026E adj. EPS ~$10.42)", s_cellB), cell("~16x", s_cellC), cell("~21.3x", s_cellC), cell("Target multiple sits squarely inside BKNG's historical 20\u201325x forward P/E range \u2014 a return to normal, not a stretch.", s_cell)],
    [cell("EV / 2027E adj. EBITDA (~$11.9 bn)", s_cellB), cell("~12.8x (TTM)", s_cellC), cell("~15.0x", s_cellC), cell("3-yr average 16.0\u201317.5x: the target prices a re-rating to just below historical average.", s_cell)],
    [cell("PEG (P/E 16x / ~13% EPS growth)", s_cellB), cell("~1.2x", s_cellC), cell("~1.6x", s_cellC), cell("Growth-at-reasonable-price today; the target embeds a modest quality premium.", s_cell)],
    [cell("FCF yield (2026E ~$10.2 bn)", s_cellB), cell("~8.0%", s_cellC), cell("~5.8%", s_cellC), cell("Today's 8% FCF yield is deep value for a 9%-grower; the target yield still beats investment-grade credit.", s_cell)],
]
story.append(styled_table(mult, [44*mm, 30*mm, 32*mm, 74*mm]))
story.append(P("The target does not require BKNG to trade at a premium to its own history \u2014 it requires the market to stop pricing it at a "
               "discount. That is the entire valuation argument in one sentence.", s_body))

story.append(P("8.3 &nbsp; What the Street thinks", s_h2))
story.append(P("Consensus is overwhelmingly positive: <b>38 Buys, 8 Holds, 0 Sells</b> with a mean target of <b>~$239</b> (+42%) and a median of $240 "
               "(high $301, low $188 \u2014 Bernstein's Market Perform). Recent actions: Morgan Stanley assumed coverage at <b>Overweight, $230</b> "
               "(Sep 16, calling BKNG its preferred OTA pick), TD Cowen upgraded to <b>Strong Buy</b> (Sep 14), Rosenblatt initiated at <b>Buy, $245</b> "
               "(Sep 1); post-Q2 PT cluster: B. Riley $274, Evercore $270, UBS $266. Our $222 sits <b>modestly below consensus</b> \u2014 we are "
               "more cautious than the median analyst on the DMA/AI overhangs and prefer to underwrite the re-rating as those clear rather than "
               "before.", s_body))

# ============ 9. RISKS & CATALYSTS ============
story.append(P("9 &nbsp; Risks, Catalysts &amp; What to Watch", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
rc = [
    [cell("Risk / catalyst", s_theadL), cell("Direction", s_thead), cell("Timing", s_thead), cell("Why it matters", s_thead)],
    [cell("Q3'26 earnings", s_cellB), cell("Catalyst \u2191", s_cellC), cell("~Oct 27", s_cellC), cell("A revenue beat vs. the soft guide resets the H2 narrative; watch room nights +3\u20135% and EBITDA +4\u20136%.", s_cell)],
    [cell("DMA enforcement outcome", s_cellB), cell("Binary", s_cellC), cell("H2'26\u2013'27", s_cellC), cell("Fine or clearance removes the #1 overhang; a business-model remedy (parity ban) would hit take rates.", s_cell)],
    [cell("Google AI search evolution", s_cell), cell("Risk \u2193", s_cellC), cell("Ongoing", s_cellC), cell("Watch marketing as % of GB: sustained rises above ~4.7% signal funnel capture by Google.", s_cell)],
    [cell("Italy AGCM probe / Spain CNMC appeal", s_cell), cell("Risk \u2193", s_cellC), cell("Ongoing", s_cellC), cell("Preferred Partner probe (opened Apr'26) + appealed ~\u20ac500 mn Spanish fine; headline risk, contained economics.", s_cell)],
    [cell("Transformation savings delivery", s_cell), cell("Catalyst \u2191", s_cellC), cell("Through end-'27", s_cellC), cell("~$650 mn run-rate savings = ~2 pts of margin; quarterly progress validates the expansion story.", s_cell)],
    [cell("Buyback cadence", s_cell), cell("Support", s_cellC), cell("Quarterly", s_cellC), cell("$14.5 bn authorization remaining; H1'26 pace ($7.3 bn) retires ~5\u20136% of shares annually.", s_cell)],
    [cell("Travel demand shocks", s_cell), cell("Risk \u2193", s_cellC), cell("Unpredictable", s_cellC), cell("Geopolitics/macro are the historical drawdown trigger; 2020 is the stress template.", s_cell)],
]
story.append(styled_table(rc, [52*mm, 22*mm, 20*mm, 86*mm]))

# ============ 10. RECOMMENDATION ============
story.append(P("10 &nbsp; Recommendation", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("We rate Booking Holdings a <b>BUY</b> with a <b>$222.00</b> 12-month price target, implying ~32% upside from $167.90. BKNG is the "
               "highest-quality business in online travel \u2014 36.9% EBITDA margins, $9.1 bn of free cash flow at 1.7x net income, 8% room-night "
               "growth \u2014 trading at a 16x forward P/E and ~12.8x EV/EBITDA that are both well below its own history. The market is charging "
               "full price for the DMA fine overhang and the Google AI threat while giving no credit for the structural defenses (Genius, the app, "
               "the merchant float) or the $650 mn transformation program. Our target deliberately stays below the Street's $239: we underwrite the "
               "re-rating as the overhangs clear, not before.", s_body))
story.append(P("Position sizing guidance: a <b>Medium-High-risk BUY</b>. This is a core-quality compounder, not a speculation \u2014 but the DMA "
               "outcome is binary and travel is cyclical, so size it as a large-cap growth anchor rather than a concentrated bet. Consider adding "
               "on any DMA-related headline weakness (the fine, if it comes, is a one-year-FCF event, not a thesis-breaker) or on a Q3'26 beat that "
               "re-accelerates the guide. Key invalidation: a DMA remedy that breaks the parity/merchant model, or sustained marketing-cost "
               "inflation that reverses the margin trajectory.", s_body))
story.append(Spacer(1, 2*mm))
story.append(P("Analyst certification &amp; disclosures: This report is an independent research-style analysis prepared for informational purposes "
               "only. It is not investment advice, a recommendation to buy/sell any security, or an offer to transact. Financial figures are sourced "
               "from Booking Holdings' SEC filings (10-K FY2025, 10-Qs, 2026 proxy statement), earnings releases and calls, and reputable financial "
               "press; projections and the $222.00 price target are the author's estimates and involve uncertainty. Past performance does not predict "
               "future results. Investors should conduct their own due diligence and consult a licensed advisor.", s_small))
story.append(Spacer(1, 2*mm))
story.append(P("Sources: BKNG 10-K FY2025 &amp; 10-Qs (SEC EDGAR); Q4'25, Q1'26, Q2'26 earnings releases &amp; call transcripts; 2026 proxy statement "
               "(PRE 14A); European Parliament DMA statement (4/30/26); Italian AGCM probe notice (4/22/26); consensus data (stockanalysis.com, "
               "Simply Wall St, Zacks, MarketBeat); Finnhub/financecharts market data. Dated September 19, 2026.", s_small))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=18*mm,
                        title="Booking Holdings (BKNG) Equity Research Note", author="Muse")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("WROTE", OUT)
