#!/usr/bin/env python3
"""Build the Home Depot (HD) equity research note PDF - compounder-quality override rebuild, Oct 4 2026."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, HRFlowable)
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import VerticalBarChart

OUT = "/home/hatch/workspace/your_files/home-depot-equity-research/home-depot-equity-research-note.pdf"

NAVY = HexColor("#0F2A44"); ACCENT = HexColor("#C2410C"); GOLD = HexColor("#C9A227")
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
    canvas.drawString(18*mm, 12*mm, "The Home Depot, Inc. (NYSE: HD)  \u2014  Equity Research Note  \u2014  October 2026")
    canvas.drawRightString(W - 18*mm, 12*mm, f"Page {doc.page}")
    canvas.setStrokeColor(MGRAY); canvas.setLineWidth(0.5)
    canvas.line(18*mm, 14.5*mm, W - 18*mm, 14.5*mm)
    canvas.restoreState()

# ============ COVER ============
story.append(Spacer(1, 24*mm))
story.append(P("THE HOME DEPOT, INC. (NYSE: HD)", ParagraphStyle("x", parent=s_sub, fontName="Helvetica-Bold", fontSize=13, textColor=ACCENT, spaceAfter=2)))
story.append(P("Great Company, Fair Price<br/>The Override Closes the Gap", s_title))
story.append(Spacer(1, 4*mm))
story.append(P("Equity Research Note  \u00b7  Consumer Discretionary \u2014 Home Improvement Retail  \u00b7  October 4, 2026", s_sub))
story.append(Spacer(1, 8*mm))

rating_data = [
    [cell("Recommendation", s_theadL), cell("12-Mo. Price Target", s_thead), cell("Current Price", s_thead), cell("Implied Upside", s_thead), cell("Risk Rating", s_thead)],
    [Paragraph("<b><font color=\"#B45309\" size=\"13\">HOLD</font></b>", s_cellC),
     Paragraph("<b><font size=\"12\">$268</font></b>", s_cellC),
     Paragraph("<b>$282.85</b><br/><font size=\"7\" color=\"#5A6472\">Oct 2, 2026</font>", s_cellC),
     Paragraph("<b>\u22125.4%</b>", s_cellC),
     Paragraph("<b>Medium</b><br/><font size=\"7\" color=\"#5A6472\">Beta 0.96</font>", s_cellC)],
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
    ["Market cap", "~$282 bn", "Shares (diluted)", "~0.998 bn"],
    ["Enterprise value", "~$343 bn", "52-week range", "$277.15 \u2013 $397.63"],
    ["Net debt", "~$61 bn", "YTD / 1-yr return", "negative / ~-24%"],
    ["TTM revenue / op. margin", "$176.3 bn / ~13.5%", "TTM / FY27E P/E", "19.8x / 17.7x"],
    ["Normalized FCF", "$15\u201316 bn", "Dividend yield", "3.3% ($9.32 annualized)"],
    ["Next catalyst", "Q3'26 earnings ~Nov 17", "Analyst consensus", "Moderate Buy, avg PT ~$376"],
]
sd = [[cell(r[0], s_cellB), cell(r[1], s_cell), cell(r[2], s_cellB), cell(r[3], s_cell)] for r in snap]
story.append(styled_table([[cell("Snapshot", s_theadL), cell("", s_thead), cell("", s_thead), cell("", s_thead)]] + sd,
               [38*mm, 42*mm, 42*mm, 48*mm], header_rows=1))
story.append(Spacer(1, 8*mm))
story.append(P("This note is independent research-style analysis for informational purposes only and is not investment advice. "
               "Figures are drawn from Home Depot's SEC filings and earnings releases and market data as of October 2, 2026. "
               "Projections and the price target are the author's estimates under the compounder-quality override (Addendum A): "
               "15-year scenario DCF, base discount 8.0%, terminal growth up to 3.0% on demonstrated margins. This note supersedes the October 4, 2026 "
               "v2 edition (REDUCE, $208 target), which is withdrawn.", s_small))
story.append(PageBreak())

# ============ 1. INVESTMENT THESIS ============
story.append(P("1 &nbsp; Investment Thesis", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("We are upgrading Home Depot from REDUCE to <b>HOLD</b> and raising the target from $208 to <b>$268</b>. "
               "Nothing about the business changed \u2014 the lens changed. Home Depot passes the compounder-quality override (Addendum A) on all three "
               "legs: <b>16 consecutive years of ROIC above 15%</b> (2010\u20132025), gross margins flat at <b>33.9% \u2192 33.3%</b> (economically flat, "
               "not contraction), and <b>106% cumulative FCF conversion</b> \u2014 the strongest band. The October 4 v2 note priced this oligopoly "
               "compounder as a turnaround: a 9.0% base discount and a 10-year horizon. The override moves the base discount to <b>8.0%</b>, the bear to "
               "<b>10.5%</b> (base + 250bp), the bull to <b>8.0%</b> (base \u2013 150bp, at the floor \u2014 the floor binds, disclosed), the explicit horizon "
               "to <b>15 years</b> (base/bull; 10 years in the bear), and terminal growth to <b>3.0% / 3.0% / 1.5%</b> on demonstrated FCF margins "
               "(9.5% / 10.5% / 6.5%). Fair value is <b>$267.64 \u2192 $268 target, 5.4% below the $282.85 quote</b>. The v2 gap to the price was 26%; "
               "the override closes most of it \u2014 because a 16-year compounder was being discounted like a cyclical retailer.", s_body))
story.append(P("To be explicit about what $283 implies under the override: our base case \u2014 comps recover to +2\u20133%, operating margins re-expand "
               "toward 13.5%, free cash flow compounds ~5% a year for fifteen years to well above $24B, leverage falls below 2x \u2014 is worth <b>$305.02</b>, "
               "<i>above</i> the quote. The market is not pricing the recovery; it is pricing recovery-skepticism. The weighted fair value ($267.64) is "
               "pulled below the price by the bear case ($58.75): housing stays frozen, tariffs stick, the Pro integration disappoints \u2014 revenue "
               "declines \u22120.5%/yr, FCF margin compresses to 6.5%, and the derating is 79%. That bear satisfies every discipline check, and at 25% "
               "weight it is the honest price of the housing-freeze tail. The verdict follows the arithmetic: <b>if the price sat at the base case, this "
               "would be a BUY; weighted for the genuine downside, it is a HOLD.</b>", s_body))
story.append(P("Why not REDUCE anymore? The business is genuinely elite \u2014 through-cycle compounder, 33\u201334% gross margins "
               "held for four years, the only scaled Pro-distribution network in the industry \u2014 and the dividend "
               "(3.3%, raised 16+ straight years) pays the wait. The v2 REDUCE rested on a 9% discount and a 10-year horizon; "
               "on the record \u2014 sixteen years above 15% ROIC \u2014 that discount was unearned pessimism. HOLD, not BUY: the bear case ($58.75) "
               "requires housing to stay frozen <i>and</i> tariffs to stick <i>and</i> the Pro integration to disappoint, but it is a real 25%-weighted "
               "outcome. We would turn buyers toward <b>$205\u2013210</b>, where the weighted fair value offers a margin of safety.", s_body))

story.append(P("Why own it (at the right price)", s_h2))
for b in [
    "<b>The Pro flywheel is the real growth engine.</b> SRS ($18.25B) + GMS (~$5.5B) + Mingledorff's ($1.1B) build a 1,200+-facility trade-distribution network aimed at the complex Pro \u2014 higher tickets, stickier relationships, better margins. Pro is well over 30% of revenue and rising; nationwide 3-hour express delivery (launched August 2026) extends the logic to the store base.",
    "<b>Comps have inflected.</b> Q2 FY2026 comps +1.7% globally (+1.3% U.S.), the strongest print since Q3 FY2022; Q1 was +0.6%. Two quarters of positive comps after a two-year drought.",
    "<b>Margins are stable, not broken.</b> Gross margin 33\u201334% for four straight years \u2014 remarkable pricing discipline through tariffs and mix shifts. Operating margin compressed 15.3% \u2192 12.7% on integration and deleverage; re-expanding (Q2 adj. 14.7%) as comps turn.",
    "<b>The balance sheet funds the wait.</b> ~$61B net debt (~2.2x EBITDA) is elevated but investment-grade (A2/A); $3.0B retired in H1 FY26; the $9.32 dividend is covered ~1.7x by earnings.",
]:
    story.append(B(b))
story.append(P("Why the market should be nervous", s_h2))
for b in [
    "<b>The price assumes the recovery the fundamentals haven't delivered.</b> $282.85 is 19.8x TTM earnings and sits 26% above our hardened base case. The September note's own DCF sensitivity table showed $283 at 8% WACC \u2014 i.e., the market is discounting a cyclical, levered retailer like a bond.",
    "<b>The Q2 gross-margin beat was borrowed from the future.</b> A one-time ~$685M IEEPA tariff refund (~$0.52/share) flattered the print; management expects fuel, energy, and input-cost inflation to offset it over the full year. Underlying margin recovery is unproven.",
    "<b>Big-ticket deferral has lasted longer than every prior cycle's pause.</b> Appliances, flooring, kitchen remodel \u2014 HD's highest-ticket categories \u2014 remain in a consumer 'deferral mindset' since 2023. ~70% of mortgages sit below 5%; turnover near 4M annualized is a record-low freeze, not a thaw.",
    "<b>Leverage is the highest in HD's modern history.</b> Net debt/EBITDA ~2.2x; buybacks paused since March 2024. If Pro-distribution integration stumbles or comps disappoint, deleveraging slows and the historical ~2\u20133% buyback yield stays sidelined.",
    "<b>Tariff regime risk.</b> A 15% across-the-board tariff (floated after the Supreme Court struck down prior duties) would test HD's diversification and could force price hikes that hurt units.",
]:
    story.append(B(b))

# ============ 2. BUSINESS ============
story.append(P("2 &nbsp; Business Overview", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Home Depot (founded 1978, Atlanta) is the world's largest home-improvement retailer: ~2,350 warehouse-format "
               "stores across the U.S., Canada, and Mexico, $176.3B of trailing sales. Three customer cohorts: DIY (~half of "
               "sales, the most cyclical), Pro (well over 30% and rising \u2014 contractors, remodelers, trades; higher "
               "ticket, repeat purchase, lower price sensitivity), and DIFM installation services. Revenue is ~90%+ North "
               "American; online comps grew 11% in Q2, the fifth straight double-digit quarter. Management describes demand "
               "as a barbell: average ticket +2.8% while transactions fell 1.0% \u2014 fewer, larger baskets; smaller "
               "repair/remodel projects and Pro demand offsetting weak big-ticket discretionary.", s_body))
story.append(P("Two structural edges. First, exclusive brands: Milwaukee and Ryobi (via TTI), BEHR paint, Husky, HDX, "
               "LifeProof \u2014 unavailable at Lowe's or Amazon, converting tool and paint aisles into destination "
               "categories with pricing power. Second, the Pro ecosystem: the SRS/GMS trade network's same-day/next-day "
               "jobsite delivery that pure retail cannot match. The weak spots are the big-ticket discretionary categories "
               "(appliances, flooring, kitchen/bath) \u2014 cyclical, not structural, and precisely what a housing-turnover "
               "recovery would unlock. Leadership: CEO Ted Decker on temporary medical leave announced August 12, 2026; "
               "EVP Ann-Marie Campbell and CFO Richard McPhail running the company in the interim.", s_body))

# ============ 3. FINANCIALS ============
story.append(P("3 &nbsp; Financial Situation", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("A through-cycle compounder whose earnings flatlined \u2014 not collapsed \u2014 through the housing freeze. "
               "Revenue compounded through the SRS/GMS acquisitions while organic comps were negative in FY23\u2013FY24; "
               "net income troughed in FY25 and is re-accelerating on a TTM basis. TTM free cash flow of $10.8B looks soft "
               "but absorbs a $2B YoY inventory build and tariff working-capital noise; normalized FCF power is $15\u201316B.", s_body))
fin = [
    [cell("$ bn (FY ends early Feb)", s_theadL), cell("FY22", s_thead), cell("FY23", s_thead), cell("FY24", s_thead), cell("FY25", s_thead), cell("TTM", s_thead)],
    [cell("Revenue", s_cellB), cell("157.4", s_cellR), cell("152.7", s_cellR), cell("159.5", s_cellR), cell("164.7", s_cellR), cell("176.3", s_cellR)],
    [cell("Revenue growth", s_cell), cell("+4.1%", s_cellR), cell("\u22123.0%", s_cellR), cell("+4.5%", s_cellR), cell("+3.3%", s_cellR), cell("+10.4%", s_cellR)],
    [cell("Gross margin", s_cell), cell("33.5%", s_cellR), cell("33.4%", s_cellR), cell("33.4%", s_cellR), cell("33.3%", s_cellR), cell("33.4%", s_cellR)],
    [cell("Operating margin", s_cell), cell("15.3%", s_cellR), cell("14.2%", s_cellR), cell("13.5%", s_cellR), cell("12.7%", s_cellR), cell("~13.5%", s_cellR)],
    [cell("Diluted EPS (GAAP)", s_cell), cell("$16.69", s_cellR), cell("$15.11", s_cellR), cell("$14.91", s_cellR), cell("$14.23", s_cellR), cell("$16.28", s_cellR)],
    [cell("Free cash flow", s_cell), cell("11.5", s_cellR), cell("18.0", s_cellR), cell("16.3", s_cellR), cell("12.7", s_cellR), cell("10.8", s_cellR)],
]
story.append(styled_table(fin, [46*mm, 24*mm, 24*mm, 24*mm, 24*mm, 24*mm]))
story.append(P("TTM includes ~$685M one-time IEEPA tariff refund in Q2 (~$0.52/share). Sources: 10-K/10-Q filings; Yahoo Finance.", s_small))
story.append(P("Management's reaffirmed FY2026 guidance (ends January 2027): total sales +2.5% to +4.5%, comps flat to +2%, "
               "gross margin ~33.1%, operating margin 12.4\u201312.6% (12.8\u201313.0% adjusted), GAAP/adjusted EPS flat to "
               "+4% off $14.23/$14.69 bases. The guidance explicitly includes the IEEPA refunds, expected to be offset over "
               "the full year by fuel, energy, and input-cost inflation \u2014 we model accordingly.", s_body))

# ============ 4. COMPETITION ============
story.append(P("4 &nbsp; Competitive Landscape", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("A two-player national oligopoly with a long tail of specialists. Lowe's is the cleaner DIY operator (higher "
               "ROIC, dividend Aristocrat) and trades cheaper \u2014 ~14.5x forward vs HD's 17.7x. But Q2 revealed the "
               "gap: +0.2% organic comps vs HD's +1.7%, with margins compressing while HD's held. Lowe's is now mimicking "
               "the Pro-distribution playbook (Foundation Building Materials, Artisan Design Group), validating HD's "
               "strategy while trailing its execution. Beyond Lowe's: Amazon lacks jobsite logistics and Pro relationships "
               "(HD's 3-hour express delivery is a direct answer); specialty distributors (ABC Supply, QXO/Beacon) are the "
               "true Pro rivals \u2014 SRS/GMS was built to fight them on their own turf.", s_body))

# ============ 5. VALUATION ============
story.append(P("5 &nbsp; Valuation \u2014 Compounder Override, Fair Value $268", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("The October 4 v2 note's $208 target priced Home Depot on a 10-year scenario DCF at a 9.0% base discount \u2014 turnaround pricing for a "
               "16-year compounder. The override (Addendum A) re-tiers the lens the record earns: a <b>15-year explicit horizon</b> (base/bull; 10 years "
               "in the bear), scenario-specific discounts <b>bear 10.5%</b> (base + 250bp) / <b>base 8.0%</b> (the strongest band \u2014 16 consecutive "
               "years of ROIC above 15%, flat gross margins, 106% FCF conversion) / <b>bull 8.0%</b> (base \u2013 150bp, at the floor \u2014 the floor "
               "binds, disclosed), and terminal growth of <b>3.0% / 3.0% / 1.5%</b> on year-N FCF at <b>demonstrated FCF margins (9.5% / 10.5% / 6.5%)</b> "
               "\u2014 the 8.6\u201310.2% typical range since 2015 (2025: 7.7% on SRS integration). Operating projections are carried from the v2 note "
               "(base 4.2% revenue CAGR; bear \u22120.5%; bull 5.8%). Net debt $61B; 0.998B shares. Terminal value is 37% / 52% / 54% of EV \u2014 under "
               "the 70% haircut line everywhere.", s_body))
story.append(Spacer(1, 3*mm))
story.append(P("Scenario DCF (15-year base/bull, 10-year bear):", s_h2))
dcf = [
    [cell("Scenario", s_theadL), cell("Rev CAGR", s_thead), cell("Terminal FCF margin", s_thead), cell("Discount / term. g", s_thead), cell("Fair value", s_thead)],
    [cell("Bear", s_cellB), cell("\u22120.5%", s_cellC), cell("6.5%", s_cellR), cell("10.5% / 1.5%", s_cellR), cell("$58.75", s_cellBR)],
    [cell("Base", s_cellB), cell("+4.2%", s_cellC), cell("9.5%", s_cellR), cell("8.0% / 3.0%", s_cellR), cell("$305.02", s_cellBR)],
    [cell("Bull", s_cellB), cell("+5.8%", s_cellC), cell("10.5%", s_cellR), cell("8.0%* / 3.0%", s_cellR), cell("$401.77", s_cellBR)],
    [cell("Probability-weighted (25/50/25) \u2192 <b>$268 target</b>", s_cellB), cell("", s_cellC), cell("", s_cellR), cell("", s_cellR), cell("$268", s_cellBR)],
]
story.append(styled_table(dcf, [52*mm, 24*mm, 26*mm, 24*mm, 30*mm, 24*mm]))

d2 = Drawing(430, 185)
d2.add(String(215, 173, "Scenario fair values vs. current price ($)", fontName="Helvetica-Bold", fontSize=10, textAnchor="middle", fillColor=NAVY))
bc2 = VerticalBarChart(); bc2.x = 45; bc2.y = 30; bc2.height = 115; bc2.width = 340
bc2.data = [[59, 305, 402, 268, 283]]
bc2.strokeColor = None; bc2.barLabels.nudge = 8; bc2.barLabelFormat = "%d"
bc2.bars[0].fillColor = ACCENT
bc2.categoryAxis.categoryNames = ["Bear", "Base", "Bull", "Wtd. avg", "Price"]
bc2.valueAxis.valueMin = 0; bc2.valueAxis.valueMax = 450; bc2.valueAxis.valueStep = 90
bc2.valueAxis.labels.fontSize = 7; bc2.categoryAxis.labels.fontSize = 8
d2.add(bc2)
story.append(d2)

story.append(P("*Bull discount floor binds (8.0% \u2013 150bp = 6.5% \u2192 8.0% floor), disclosed per Addendum A. "
               "The bear case hurts the way the rules require: housing stays frozen, comps go flat-to-negative, tariff "
               "costs stick, and the Pro integration disappoints \u2014 revenue declines \u22120.5%/yr, FCF margin "
               "compresses to 6.5% (300bp below base), and the derating is 79%. Bear fair value <b>$58.75</b>, far "
               "below the quote. The base case is generous \u2014 comps +2\u20133%, margins back toward 13.5%, FCF "
               "compounding ~5%/yr for fifteen years \u2014 and it is worth <b>$305.02</b>, <i>above</i> the price: the market "
               "is pricing recovery-skepticism, not the recovery. The bull case ($401.77: housing-turnover snapback, comps +4%, "
               "SRS/GMS synergies beat) is 42% above the quote. What changed vs v2: \u2212100bp on the base discount (9% \u2192 8%), "
               "10y \u2192 15y horizon, terminal 2.5% \u2192 3.0% on demonstrated margins. FV +28.6% vs v2; the price had already "
               "reflected much of it \u2192 HOLD.", s_body))
story.append(P("<b>Price target: $268.</b> The target <i>is</i> the probability-weighted override DCF "
               "(0.25\u00d7$58.75 + 0.50\u00d7$305.02 + 0.25\u00d7$401.77 = $267.64, rounded) \u2014 with no multiple "
               "overrule. What would falsify the HOLD: a genuine housing-turnover recovery (existing-home sales sustainably "
               "above 4.5M annualized) with comps printing +4% would argue for the bull case \u2014 as would buyback resumption "
               "ahead of schedule with leverage falling below 2x. Falsification of the override itself: two consecutive sub-15% "
               "ROIC years would revoke the compounder discount (note: HD ROIC has trended down 48.9% \u2192 27.2% from 2021 to 2025 \u2014 "
               "watch this).", s_body))

story.append(P("6 &nbsp; Key Risks", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
for b in [
    "<b>Housing / rates (the big one).</b> HD is a leveraged play on turnover. If mortgage rates stay ~6%+ and existing-home sales languish near 4M, the big-ticket recovery underpinning any bull case never arrives; comps could re-decelerate to flat.",
    "<b>Tariff pass-through.</b> The Q2 gross-margin beat was flattered by the one-time IEEPA refund; a 15% across-the-board tariff would test HD's diversification and could force unit-hurting price hikes.",
    "<b>Leverage and paused buybacks.</b> Net debt/EBITDA ~2.2x is the highest in HD's modern history; the historical ~2\u20133% buyback yield stays sidelined until deleveraging progresses.",
    "<b>Big-ticket deferral persistence.</b> The consumer 'deferral mindset' since 2023 has lasted longer than every prior cycle's pause; prolonged deferral caps ticket growth.",
    "<b>Leadership transition noise.</b> CEO on temporary medical leave since August 2026; any extension creates an overhang into the holiday season.",
    "<b>Competition.</b> Lowe's copying the Pro-distribution playbook; Amazon compressing delivery expectations; specialty distributors defending Pro share.",
]:
    story.append(B(b))

story.append(P("Recommendation", s_h2))
story.append(P("<b>HOLD, $268 target (\u22125.4%).</b> Home Depot is a superb business trading at a fair price \u2014 the compounder-quality override "
               "recognizes what the v2 note's turnaround discount ignored: sixteen consecutive years of ROIC above 15%, flat gross margins, 106% FCF "
               "conversion. The override 15-year DCF values the equity at $268 (bear $58.75 / base $305.02 / bull $401.77) against a $282.85 quote. "
               "The price sits <i>below</i> the base case \u2014 the market prices recovery-skepticism \u2014 but the 25%-weighted bear ($58.75, "
               "housing stays frozen) is the honest price of the downside, and it pulls the weighted value 5.4% below the quote. <b>Current holders "
               "should hold</b> \u2014 the dividend (3.3%) pays the wait, and selling a 16-year compounder over a 5% gap has a poor hit rate. "
               "We would turn buyers below ~$205, where the weighted fair value finally offers a margin of safety, and upgrade to BUY toward $200. "
               "<b>Falsification:</b> a sustained housing-turnover recovery with +4% comps, or buyback resumption with leverage below 2x ahead of "
               "schedule, would argue the market is right to price the bull case \u2014 and we would revisit. Watch the override's own tripwire: "
               "HD's ROIC has trended down (48.9% \u2192 27.2%, 2021\u20132025); two consecutive sub-15% years revokes the compounder discount.", s_body))
story.append(Spacer(1, 6*mm))
story.append(P("Methodology &amp; sources. Valuation as of October 4, 2026; share price $282.85 (10/2/26 close). Model: compounder-quality "
               "override (Addendum A) \u2014 15-year scenario FCFF DCF, weights bear 25% / base 50% / bull 25%; discounts base 8.0% (strongest band) / "
               "bear 10.5% / bull 8.0% (floor binds, disclosed); terminal growth 3.0% / 1.5% / 3.0% on year-N FCF at demonstrated mid-cycle margins "
               "(9.5% / 6.5% / 10.5%). Qualification: 16 consecutive years ROIC &gt;15% (2010\u20132025), gross margins 33.9% \u2192 33.3%, 106% "
               "cumulative FCF conversion; falsification watch: ROIC trending down (48.9% \u2192 27.2%, 2021\u20132025), two consecutive sub-15% years "
               "revokes the override. "
               "Net debt $61B; 0.998B diluted shares. Bear case meets all hurt conditions and sits below the current price. Terminal value is "
               "37\u201354% of EV (no haircut required). Financials from SEC 10-K/10-Q filings (CIK 354950) and earnings "
               "releases; market data via Yahoo Finance. This note is research analysis for informational purposes and is "
               "not personalized investment advice. Equity investing involves risk of loss. The author holds no position in "
               "HD at the time of writing.", s_small))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=18*mm,
                        title="Home Depot (HD) \u2014 Equity Research Note", author="Muse")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("wrote", OUT)
