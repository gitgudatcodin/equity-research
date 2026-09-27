#!/usr/bin/env python3
"""Build the SoFi Technologies (SOFI) equity research note PDF."""
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

OUT = "/home/hatch/workspace/your_files/sofi-equity-research/sofi-equity-research-note.pdf"

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

# ============ VALUATION MATH (computed first so the note is internally consistent) ============
SHARES_BN = 1.31          # diluted shares outstanding, billions
PRICE = 16.58             # Sept 25, 2026 close

def earn_dcf(ni_2026, growth, coe, g_term):
    ni = ni_2026; pv = 0.0
    for i, g in enumerate(growth):
        ni *= (1 + g)
        pv += ni / (1 + coe) ** (i + 1)
    tv = ni * (1 + g_term) / (coe - g_term)
    pv += tv / (1 + coe) ** len(growth)
    return pv / 1000.0    # $bn equity value

base_g = [0.38, 0.32, 0.27, 0.22, 0.17, 0.13, 0.10, 0.07, 0.05]
bear_g = [0.30, 0.25, 0.20, 0.15, 0.12, 0.10, 0.08, 0.06, 0.04]
bull_g = [0.45, 0.38, 0.30, 0.25, 0.20, 0.15, 0.12, 0.09, 0.06]

dcf_base = earn_dcf(825, base_g, 0.12, 0.035)
dcf_bear = earn_dcf(800, bear_g, 0.135, 0.025)
dcf_bull = earn_dcf(850, bull_g, 0.105, 0.040)

px_bear = dcf_bear / SHARES_BN
px_base = dcf_base / SHARES_BN
px_bull = dcf_bull / SHARES_BN
px_wtd = 0.25 * px_bear + 0.50 * px_base + 0.25 * px_bull
TARGET = round(px_wtd * 2) / 2
UPSIDE = (TARGET - PRICE) / PRICE * 100

# SOTP cross-check (annualized Q2 2026 segment economics)
sotp = (399 * 4 * 10.0 + 0.46 * 466 * 4 * 12.0 + 84.5 * 4 * 9.0) / 1000.0  # $bn
px_sotp = sotp / SHARES_BN

print(f"DCF bear/base/bull equity ($bn): {dcf_bear:.1f} / {dcf_base:.1f} / {dcf_bull:.1f}")
print(f"DCF per-share: ${px_bear:.2f} / ${px_base:.2f} / ${px_bull:.2f}  -> weighted ${px_wtd:.2f}")
print(f"SOTP: ${sotp:.1f}bn -> ${px_sotp:.2f}/sh")
print(f"TARGET ${TARGET:.2f}  UPSIDE {UPSIDE:.1f}%")

story = []
W, H = A4

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7); canvas.setFillColor(DGRAY)
    canvas.drawString(18*mm, 12*mm, "SoFi Technologies, Inc. (NASDAQ: SOFI)  \u2014  Equity Research Note  \u2014  September 2026")
    canvas.drawRightString(W - 18*mm, 12*mm, f"Page {doc.page}")
    canvas.setStrokeColor(MGRAY); canvas.setLineWidth(0.5)
    canvas.line(18*mm, 14.5*mm, W - 18*mm, 14.5*mm)
    canvas.restoreState()

# ============ COVER ============
story.append(Spacer(1, 24*mm))
story.append(P("SOFI TECHNOLOGIES, INC.", ParagraphStyle("x", parent=s_sub, fontName="Helvetica-Bold", fontSize=13, textColor=ACCENT, spaceAfter=2)))
story.append(P("The One-Stop Shop<br/>at Half Price", s_title))
story.append(Spacer(1, 4*mm))
story.append(P("Equity Research Note  \u00b7  Financials \u2014 Diversified Banks / Fintech  \u00b7  September 26, 2026", s_sub))
story.append(Spacer(1, 8*mm))

rating_data = [
    [hdr("Recommendation", s_theadL), hdr("12-Mo. Price Target"), hdr("Current Price"), hdr("Implied Upside"), hdr("Risk Rating")],
    [Paragraph("<b><font color=\"#0E7C3E\" size=\"13\">BUY</font></b>", s_cellC),
     Paragraph(f"<b><font size=\"12\">${TARGET:.2f}</font></b>", s_cellC),
     Paragraph("<b><font size=\"12\">$16.58</font></b><br/><font size=\"7\" color=\"#5A6472\">Sep 25, 2026 close</font>", s_cellC),
     Paragraph(f"<b><font color=\"#0E7C3E\" size=\"12\">+{UPSIDE:.0f}%</font></b>", s_cellC),
     Paragraph("<b>High</b>", s_cellC)],
]
story.append(styled_table(rating_data, [34*mm, 34*mm, 34*mm, 34*mm, 34*mm], fontsize=9))
story.append(Spacer(1, 6*mm))

story.append(P("SoFi just printed its strongest quarter ever \u2014 40% revenue growth, 30% adjusted-EBITDA margins, a Rule-of-40 score of 70 (its 19th straight quarter clearing the bar), a tenth consecutive GAAP-profitable quarter, and record member and product growth \u2014 and the stock fell 9% on the print and sits 45% below its November 2025 high. The derating is about the macro, not the micro: the Fed hiked rates on September 16 for the first time since 2023, the 10-year is above 5%, and the market is pricing SoFi like a cyclical subprime lender at peak credit. We think that misreads the business. SoFi is a deposit-funded national bank ($45.5 billion of deposits, growing $5+ billion a quarter at 156 bp below warehouse funding costs) with a high-income prime borrower base (weighted-average FICO 745, income ~$157k), improving credit metrics, and a fee-based engine \u2014 interchange, brokerage, and the Loan Platform Business \u2014 that is now 39% of revenue and compounding at 50%+. At $16.58 the shares trade at ~28x 2026E adjusted EPS of $0.60 and 2.3x tangible book, a discount to every large fintech peer despite faster growth. Our scenario-weighted earnings-power DCF points to "
+ f"${px_wtd:.2f}; we set a <b>${TARGET:.2f}</b> target and rate the shares <b>BUY</b>. This is a high-beta, high-risk call \u2014 the Fed's hiking cycle is the swing factor \u2014 sized accordingly.", s_body))
story.append(Spacer(1, 3*mm))

stats = [
    [cell("<b>Market cap</b>", s_cellB), cellR("~$21.7 bn"), cell("<b>Shares out. (diluted)</b>", s_cellB), cellR("~1.31 bn")],
    [cell("<b>52-week range</b>", s_cellB), cellR("$14.88 \u2013 $32.73"), cell("<b>YTD / 1-yr return</b>", s_cellB), cellR("-37% / -41%")],
    [cell("<b>Tangible book value</b>", s_cellB), cellR("$9.5 bn (+80% YoY)"), cell("<b>P / tangible book</b>", s_cellB), cellR("~2.3x")],
    [cell("<b>FY26E adj. rev / adj. EPS</b>", s_cellB), cellR("$4.75\u20134.85 bn / $0.60"), cell("<b>Fwd P/E / PEG</b>", s_cellB), cellR("~28x / ~1.4x")],
]
story.append(styled_table(stats, [42*mm, 43*mm, 42*mm, 43*mm], header_rows=0, zebra=True, fontsize=8.5))
story.append(Spacer(1, 4*mm))
story.append(P("Prices as of September 25, 2026 close. Financial figures from company releases (Q2 2026 reported July 29, 2026; Q1 2026 April 29, 2026; Q4/FY2025 January 30, 2026). This note is an independent research-style analysis for informational purposes, not investment advice.", s_small))

# ============ 1. INVESTMENT THESIS ============
story.append(P("1. Investment thesis", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
for t in [
    "<b>Durable hypergrowth with real profitability.</b> Adjusted net revenue has grown 35\u201341% for seven straight quarters; adjusted EBITDA margins sit near 30%; GAAP profitability is now ten quarters deep; and the Rule-of-40 score hit 70 in Q2 (40% growth + 30% margin) \u2014 the 19th consecutive quarter meeting the benchmark. Few financials globally combine this growth with this margin.",
    "<b>The deposit franchise is the moat.</b> $45.5 billion of deposits, up $5.3 billion in a single quarter, funded at ~156 bp below warehouse costs \u2014 a $713 million annualized funding advantage that flows straight to net interest income. Deposits have compounded from $1.2 billion at the January 2022 bank-charter grant to $45.5 billion today. This is what separates SoFi from Upstart, Affirm and every other non-bank lender.",
    "<b>Credit quality is improving into the growth.</b> All-in personal-loan net charge-offs of ~3.7% improved 70 bp sequentially and 80 bp YoY; 90-day delinquencies sit at 40 bp; recent vintages are tracking well below the 7\u20138% lifetime-loss tolerance. The borrower is prime: $157k average income, 745 FICO on personal loans, 773 on student loans.",
    "<b>The mix shift de-risks the story every quarter.</b> Fee-based revenue hit $472 million in Q2 (39% of revenue, +50% YoY trajectory), driven by interchange (+~60%), brokerage fees (2.4x YoY) and the capital-light Loan Platform Business ($3.1 billion originated for third parties in Q2; new $1B Sixth Street and $3B BasePoint mandates). Lending is still the engine, but it is no longer the whole car.",
    "<b>Valuation disconnect.</b> At ~28x 2026E adjusted EPS and 2.3x tangible book, SoFi trades at a steep discount to Robinhood (~52x trailing P/E), Block (~129x) and Upstart (~38x) despite 40% revenue growth and superior profitability \u2014 and the stock is down 45% from its November 2025 high on macro fears. Our DCF (bear $"
    + f"{px_bear:.2f} / base ${px_base:.2f} / bull ${px_bull:.2f}, weighted ${px_wtd:.2f}) and SOTP (${px_sotp:.2f}) both support a <b>${TARGET:.2f}</b> target.",
    "<b>Catalyst path is visible.</b> Q3 results in late October, continued deposit and LPB scaling, SoFi Plus monetization (>200k paid members and climbing), stablecoin/SEN adoption, and any Fed pivot back toward cuts in 2027 (Morningstar's base case) could each re-rate the shares.",
    "<b>Risks are genuine \u2014 hence High risk, not a core holding.</b> The Fed just started hiking again (Sept 16, more signaled); a credit downturn would hit a fast-growing $46.6 billion loan book; the Technology Platform is shrinking; and at 2.3x tangible book with 6.2% ROE, the market is paying for growth that must continue. Size for a 30\u201340% drawdown scenario.",
]:
    story.append(B(t))

# ============ 2. COMPANY OVERVIEW ============
story.append(P("2. Company overview: what SoFi actually does", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
story.append(P("SoFi Technologies (NASDAQ: SOFI), founded in 2011 by Stanford GSB students as a student-loan refinancing upstart and listed via SPAC in May 2021, describes itself as a member-centric \u201cone-stop shop\u201d for digital financial services: borrow, save, spend, invest and protect. CEO Anthony Noto (ex-Goldman Sachs COO, ex-Twitter COO) has run the company since 2018. The defining strategic move was the January 2022 acquisition of Golden Pacific Bancorp and the resulting <b>national bank charter</b> \u2014 making SoFi one of the first fintechs to become a regulated bank holding company, able to take deposits and fund its own loans. It reports in three segments:", s_body))
story.append(P("<b>Lending (~59% of revenue).</b> The original engine and still the largest segment: student loan refinancing (the founding product), personal loans ($10.7B originated in Q2, +54% YoY \u2014 the volume driver), home loans including a new home-equity product ($1.4B, +74%), and newly launched small-business loans. Q2 2026: adjusted net revenue $711.7M (+59% YoY), contribution profit $399M (+63%). SoFi both holds loans on balance sheet ($46.6B at fair value) and operates an originate-to-distribute <b>Loan Platform Business</b>, selling whole loans and LPB economics to institutional partners.", s_body))
story.append(P("<b>Financial Services (~38% of revenue, the diversification engine).</b> SoFi Money (checking/savings), SoFi Invest (brokerage), credit card, insurance marketplace, Relay (credit-score monitoring), estate planning, plus newer subscription and AI layers \u2014 SoFi Plus ($10/month premium tier, >200k paid members) and SoFi Coach (AI financial guidance, 500k+ conversations, 90%+ positive feedback). Q2 2026: revenue $466M (+29% YoY), contribution margin 46%. Interchange revenue surged ~60% on $28B+ of annualized card spend; brokerage fee revenue rose 2.4x; Invest products +38%.", s_body))
story.append(P("<b>Technology Platform (~7% of revenue, currently the problem child).</b> Galileo (acquired 2020, ~$1.2B) \u2014 API-based payments processing and card issuing for fintechs and brands \u2014 plus Technisys (acquired 2022, ~$1.1B) \u2014 cloud-native core banking (Cyberbank Core). Relaunched in 2026 as <b>SoFi Tech Solutions</b> (processing, core ledger, payments hub, risk/fraud). Q2 2026: revenue $84.5M (\u201323% YoY) after a major client departed pre-year-end 2025; contribution profit $11.8M (\u201365%); +13% sequentially. SoFi acquired Peach Finance (card/BNPL servicing) to broaden the stack, and Galileo just signed a commercial sponsor-banking program built on Cyberbank Core.", s_body))
story.append(P("<b>How it makes money:</b> net interest income on the loan book (NIM 5.98% in Q2, NII $788M, +52% YoY), loan origination and sale gains, interchange and brokerage fees, LPB fees, and technology-platform processing revenue. The model is branchless: no physical footprint, with customer acquisition driven by brand marketing (unaided awareness at an all-time high of 9.6%) and the deposit-rate advantage.", s_body))

# ============ 3. FINANCIAL REVIEW ============
story.append(P("3. Financial review", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
story.append(P("<b>Q2 2026 (reported July 29, 2026): record quarter, punished stock.</b> Every operating metric was a record \u2014 revenue, originations ($14.8B, +69%), members (+1.1M), products (+2.2M) \u2014 and revenue beat consensus by 8%. The stock fell 9% to $15.25 anyway: management raised the 2026 revenue guide (to $4.75\u20134.85B, +32\u201335%) but held adjusted EPS at ~$0.60, and the market read the flat profit guide as a lack of operating leverage. The shares have since recovered ~20% but remain far below the highs.", s_body))

q2 = [
    [hdr("Q2 2026 metric", s_theadL), hdr("Q2 2026"), hdr("Q2 2025"), hdr("YoY")],
    [cell("Adjusted net revenue"), cellR("$1.21 bn"), cellR("$864 m"), cellR("+40%")],
    [cell("GAAP net revenue"), cellR("$1.22 bn"), cellR("$857 m"), cellR("+43%")],
    [cell("Net interest income (NIM)"), cellR("$788 m (5.98%)"), cellR("$519 m (5.86%)"), cellR("+52%")],
    [cell("Fee-based revenue (% of rev)"), cellR("$472 m (39%)"), cellR("~$315 m"), cellR("+50%")],
    [cell("Adjusted EBITDA (margin)"), cellR("$358 m (30%)"), cellR("$249 m (29%)"), cellR("+44%")],
    [cell("GAAP net income / EPS"), cellR("$157 m / $0.12"), cellR("$97 m / $0.08"), cellR("+61% / +50%")],
    [cell("Members / products"), cellR("15.8 m / 24.4 m"), cellR("11.7 m / 17.2 m"), cellR("+35% / +42%")],
    [cell("Loan originations"), cellR("$14.8 bn"), cellR("$8.8 bn"), cellR("+69%")],
    [cell("Deposits"), cellR("$45.5 bn"), cellR("$34.8 bn*"), cellR("+31%")],
    [cell("Tangible book value"), cellR("$9.5 bn"), cellR("$5.3 bn"), cellR("+80%")],
]
story.append(styled_table(q2, [62*mm, 36*mm, 36*mm, 36*mm]))
story.append(P("*Q2 2025 deposits estimated from reported growth rates. Source: company Q2 2026 press release and earnings materials.", s_small))
story.append(Spacer(1, 2*mm))

story.append(P("<b>Q1 2026 (April 29, 2026):</b> adjusted net revenue $1.087B (+41%), adjusted EBITDA $340M (+62%, 31% margin), net income $167M (+134%), EPS $0.12 (doubled), members 14.7M (+35%), products 22.2M (+39%), originations $12.2B (+68%) with records across personal ($8.3B), student ($2.6B, 2.2x) and home ($1.2B, 2.4x) loans, deposits $40.2B. Lending adj. revenue $629M (+53%); Financial Services $429M (+41%); Technology Platform $75M (\u201327% reported, +12% like-for-like ex the lost client).", s_body))
story.append(P("<b>FY2025: the first full year of GAAP profitability.</b> Total net revenue $3.613B (+35%), adjusted net revenue $3.591B (+38%), GAAP net income $481M (first full profitable year; 2024's $499M included a one-off $271M tax-valuation-release benefit), adjusted EBITDA $1.054B (+58%), adjusted EPS $0.39 (+160%). Q4 2025 alone: revenue crossed $1B for the first time, members 13.7M (+35%), products 20.2M (+37%), Rule-of-40 score 68.", s_body))

story.append(P("<b>Seven-quarter trend: growth on every line, margins holding near 30%.</b>", s_body))
trend = [
    [hdr("Quarter", s_theadL), hdr("Adj. net revenue"), hdr("Adj. EBITDA"), hdr("Net income"), hdr("Members"), hdr("Products")],
    [cell("Q4 2024"), cellR("$739 m"), cellR("$198 m"), cellR("$61 m*"), cellR("10.1 m"), cellR("14.7 m")],
    [cell("Q1 2025"), cellR("$771 m"), cellR("$210 m"), cellR("$71 m"), cellR("10.9 m"), cellR("16.0 m")],
    [cell("Q2 2025"), cellR("$864 m"), cellR("$249 m"), cellR("$97 m"), cellR("11.7 m"), cellR("17.2 m")],
    [cell("Q3 2025"), cellR("$950 m"), cellR("$277 m"), cellR("$139 m"), cellR("12.6 m"), cellR("18.6 m")],
    [cell("Q4 2025"), cellR("$1,013 m"), cellR("$318 m"), cellR("$174 m"), cellR("13.7 m"), cellR("20.2 m")],
    [cell("Q1 2026"), cellR("$1,087 m"), cellR("$340 m"), cellR("$167 m"), cellR("14.7 m"), cellR("22.2 m")],
    [cell("Q2 2026"), cellR("$1,210 m"), cellR("$358 m"), cellR("$157 m"), cellR("15.8 m"), cellR("24.4 m")],
]
story.append(styled_table(trend, [26*mm, 30*mm, 28*mm, 28*mm, 28*mm, 30*mm], fontsize=8))
story.append(P("*Q4 2024 adjusted net income; GAAP net income was $333m including a one-off tax benefit. Source: company releases.", s_small))
story.append(Spacer(1, 2*mm))

d = Drawing(170*mm, 62*mm)
bc = VerticalBarChart()
bc.x = 12*mm; bc.y = 12*mm; bc.height = 42*mm; bc.width = 140*mm
bc.data = [[739,771,864,950,1013,1087,1210],[198,210,249,277,318,340,358]]
bc.strokeColor = colors.white
bc.barLabels.nudge = 8
bc.categoryAxis.labels.boxAnchor = "ne"; bc.categoryAxis.labels.angle = 0
bc.categoryAxis.categoryNames = ["Q4'24","Q1'25","Q2'25","Q3'25","Q4'25","Q1'26","Q2'26"]
bc.categoryAxis.labels.fontSize = 6.5
bc.valueAxis.valueMin = 0; bc.valueAxis.valueMax = 1320; bc.valueAxis.valueStep = 330
bc.valueAxis.labels.fontSize = 6.5
bc.bars[0].fillColor = NAVY; bc.bars[1].fillColor = ACCENT
bc.barLabelFormat = "%d"
story.append(d)
story.append(P("Quarterly adjusted net revenue (navy, $m) and adjusted EBITDA (green, $m): seven quarters of uninterrupted growth on both lines. Source: company releases.", s_small))
story.append(Spacer(1, 2*mm))

story.append(P("<b>Balance sheet: deposit-funded and well capitalized.</b> Total assets $61.0B (from $50.7B at YE2025); loans held at fair value $46.6B (personal $27.5B); deposits $45.5B (+$5.3B in Q2 alone, +21% from YE2025) at an average rate ~156 bp below warehouse funding \u2014 management quantifies the annualized savings at $713M. Total risk-based capital ratio 18.8%; available liquidity $13.7B; tangible book value $9.5B (+80% YoY); ROE 6.2% and rising; debt-to-equity 0.30. Operating cash flow was \u2013$6.2B, entirely a function of the growing loan pipeline (originate-to-hold/sell), not operating weakness.", s_body))
story.append(P("<b>Credit quality (the heart of the bear case \u2014 and it is holding).</b> Excluding late-stage delinquent-loan sales, the all-in annualized personal-loan net charge-off rate was ~3.7%, improving 70 bp sequentially and 80 bp YoY; the reported rate fell to 2.62%. 90-day personal delinquencies: 40 bp (\u20137 bp QoQ); student: 11 bp, with student NCOs at 0.61%. The 7\u20138% maximum cumulative-loss assumption remains intact \u2014 vintages from Q4 2022 through Q3 2025 show 4.68% cumulative losses with 35% of principal still outstanding, tracking well below the 2017 vintage curve. Unit economics: 12.9% weighted-average coupon, 3.1% funding cost, ~3.7% losses \u2192 ~6.1% risk-adjusted margin on personal loans.", s_body))

# ============ 4. GROWTH OUTLOOK ============
story.append(P("4. Growth outlook", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
story.append(P("<b>2026 guidance (raised July 29, 2026):</b> adjusted net revenue $4.75\u20134.85B (+32\u201335% YoY), adjusted EBITDA ~$1.6B (~33\u201334% margin), adjusted net income ~$825M, adjusted EPS ~$0.60, and member growth of at least 30%. Consensus sits at ~$0.59\u20130.61 for 2026 and $0.80 for 2027 (+35%).", s_body))
story.append(P("<b>What drives the next leg:</b>", s_h2))
for t in [
    "<b>Deposits compounding into NII.</b> $5B+ of quarterly deposit growth at a 156 bp funding advantage is a self-reinforcing flywheel: cheaper funding \u2192 better loan/deposit pricing \u2192 more members \u2192 more deposits. Every $5B of deposits shifted from warehouse funding saves roughly $78M annually.",
    "<b>Loan Platform Business scaling (capital-light growth).</b> $3.1B originated for third parties in Q2; new mandates \u2014 Sixth Street (up to $1B personal loans), BasePoint ($3B small-business loans over three years), home-equity transfers to a global bank \u2014 plus the newly launched small-business loan product. LPB converts balance-sheet growth into fee income without capital consumption \u2014 critical with CET1 under watch (Mizuho flagged the ratio).",
    "<b>Financial Services monetization deepening.</b> Interchange +~60% on $28B+ annualized spend, brokerage fees 2.4x, SoFi Plus past 200k paid subscribers at $10/month, SoFi Coach driving engagement. Cross-buy hit 51% of new products in Q2 (vs 35% a year ago); products per member reached a record 1.54.",
    "<b>Digital assets as a call option.</b> Crypto trading relaunched in 2025; SoFiUSD \u2014 the first U.S. national-bank-issued stablecoin \u2014 launched May 2026 (~$300M in circulation at Q2-end), went live for settlement across a $25B Mastercard card program in September, and listed on Kraken alongside the Payward/SEN 24/7 settlement partnership (Sept 3). Tiny today; strategically, it positions SoFi's charter as crypto-market infrastructure.",
    "<b>Technology Platform repair.</b> The \u201323% YoY decline is the acknowledged weak spot. The Peach Finance acquisition, the Cyberbank Core sponsor-banking program, and the unified \u201cSoFi Tech Solutions\u201d go-to-market are the repair kit; management guides the segment back to growth on a like-for-like basis (+12% in Q1, +13% QoQ in Q2).",
]:
    story.append(B(t))
story.append(P("<b>The macro swing factor: the Fed is hiking again.</b> On September 16, 2026 the FOMC raised the funds rate to 3.75\u20134.00% \u2014 the first hike since July 2023 \u2014 under new Chair Kevin Warsh, citing energy-driven inflation (gasoline $4.17/gal, +37% YoY; core CPI 0.29% MoM in August). The September SEP median implies one more hike to 4.1% by year-end and no cuts until late decade; the 10-year Treasury is above 5% and the 30-year mortgage is 6.97%. For SoFi this is a double-edged sword: higher rates support deposit gathering and NIM if deposit betas stay contained, but they pressure loan demand (notably mortgages), fair values on the held loan book, and credit performance if unemployment rises. SoFi's 2026 guidance was built on a no-cut assumption, so the hiking pivot \u2014 not priced in July \u2014 is the single biggest risk to the 2027 trajectory. Morningstar's base case sees cuts resuming in 2027\u201328 as inflation cools, which would be a meaningful tailwind.", s_body))

# ============ 5. MOAT & PRODUCT EVALUATION ============
story.append(P("5. Moat assessment and product evaluation", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
story.append(P("SoFi's moat is <b>charter + integration + cross-sell</b>, not any single product. We rate it a <b>narrow-to-moderate moat, widening</b>: the bank charter and deposit base are genuinely hard to replicate (only a handful of fintechs hold one), the vertically integrated tech stack (Galileo + Technisys + bank core) lowers marginal product-launch costs, and the cross-sell engine is demonstrably working (51% of new products from existing members). It is not yet a wide moat: lending products are commoditized, switching costs are low, and big-tech/bank competitors can copy features. Sources of the moat:", s_body))
for t in [
    "<b>Regulatory moat (bank charter):</b> deposit funding at 156 bp below wholesale \u2014 a $713M/year structural cost advantage over non-bank lenders (Upstart, Affirm) that widens as deposits scale. Charter applications take years; SoFi is already through the door.",
    "<b>Vertical technology integration:</b> owning the processor (Galileo), the core (Technisys/Cyberbank) and the bank lets SoFi launch products (SoFiUSD, SEN settlement, sponsor banking) that competitors must assemble from vendors.",
    "<b>Data and cross-sell flywheel:</b> 15.8M members generating transaction, cash-flow and investing data feed underwriting and personalization; 1.54 products per member and rising; SoFi Plus/Coach deepen engagement and switching costs.",
    "<b>Brand:</b> unaided awareness at an all-time high of 9.6%; 'SoFi' is increasingly the default digital-finance brand for younger prime borrowers.",
]:
    story.append(B(t))
story.append(P("Product-by-product evaluation (with pricing model for each):", s_h2))
prod = [
    [hdr("Product", s_theadL), hdr("Pricing model"), hdr("Assessment")],
    [cell("<b>SoFi Money</b><br/>(checking/savings)"), cell("Freemium: 3.30% APY savings w/ direct deposit (0.80% w/o), 0.50% checking; no fees; $50\u2013$400 DD bonus; 4.20% 6-mo new-member boost"), cell("<b>Best-in-class.</b> Top-decile rate vs Ally (3.10%); the deposit engine of the whole company. Rate has fallen with the cycle (was 4.60%) but the DD qualifier builds primary-bank relationships.")],
    [cell("<b>Student loan refi</b>"), cell("Net interest margin: borrow ~3.1%, lend at prime rates; origination fees; LPB sale gains"), cell("<b>Franchise product.</b> $2.7B originations (+170% YoY); 773 avg FICO, 0.61% NCOs \u2014 pristine credit. The product that built the brand.")],
    [cell("<b>Personal loans</b>"), cell("NIM: 12.9% avg coupon \u2212 3.1% funding \u2212 ~3.7% losses \u2248 6.1% risk-adj. margin; LPB distribution fees"), cell("<b>Strong but cyclical.</b> $10.7B (+54%); prime borrowers ($157k income, 745 FICO); losses improving. The volume engine \u2014 and the main credit-cycle exposure.")],
    [cell("<b>Home loans</b>"), cell("NIM + gain-on-sale; new home-equity product; transfers to bank partners"), cell("<b>Reaccelerating.</b> $1.4B (+74%) despite 6.97% mortgage rates; home-equity is a smart counter-cyclical addition.")],
    [cell("<b>Small-biz loans</b>"), cell("NIM + LPB (BasePoint $3B 3-yr mandate)"), cell("<b>New, promising.</b> Launched 2026 on observed member demand; capital-light via LPB from day one.")],
    [cell("<b>SoFi Invest</b>"), cell("$0 commissions; monetizes via order flow, margin lending, plus-tier perks"), cell("<b>Scaling fast.</b> Brokerage fees 2.4x YoY; Invest products +38%. Feature set still trails Robinhood (options depth, Gold ecosystem) but the cross-sell from banking is the edge.")],
    [cell("<b>Credit card</b>"), cell("Interchange (~2%) funds rewards; no annual fee"), cell("<b>Effective acquisition tool.</b> $28B+ annualized spend driving interchange +~60%; card spend data feeds underwriting.")],
    [cell("<b>SoFi Plus</b>"), cell("Subscription: $10/month for top rates + perks"), cell("<b>Early but working.</b> 200k+ paid members (~$24M run-rate); converts free riders into ARPU; the 'Prime-ification' of SoFi.")],
    [cell("<b>Crypto + SoFiUSD</b>"), cell("Trading spreads; stablecoin float/reserve income; SEN settlement fees"), cell("<b>Free call option.</b> ~$300M SoFiUSD circulating; Kraken listing + Mastercard settlement live. Immaterial to 2026 earnings; potentially material infrastructure by 2028.")],
    [cell("<b>Galileo / Tech Solutions</b>"), cell("B2B SaaS/processing: per-account, per-transaction fees"), cell("<b>Turnaround story.</b> \u201323% YoY on a lost anchor client; +13% QoQ; Peach acquisition + Cyberbank sponsor banking are credible repairs, but proof is pending.")],
]
story.append(styled_table(prod, [34*mm, 62*mm, 74*mm], fontsize=7.5))
story.append(Spacer(1, 2*mm))
story.append(P("Net: the consumer products are genuinely best-in-class for the target demographic (young, prime, digital-first); the B2B platform is the laggard. The pricing architecture \u2014 freemium banking funded by NIM, subscription upsell, capital-light LPB fees \u2014 is coherent and increasingly diversified: fee-based revenue is 39% of the total and rising.", s_body))

# ============ 6. COMPETITION ============
story.append(P("6. Competition", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
comp = [
    [hdr("Rival", s_theadL), hdr("Where it competes"), hdr("Threat"), hdr("Read-through")],
    [cell("<b>Robinhood</b><br/>$109B, ~52x P/E"), cell("Invest + crypto + creeping into banking (Gold 4.8M subs, +39%)"), cell("High"), cell("The closest comp and the valuation benchmark. 5x SoFi's market cap on ~$2B net income; SoFi's banking-first model is the mirror image of HOOD's trading-first model.")],
    [cell("<b>Block (Cash App)</b><br/>$46B, ~129x P/E"), cell("P2P, banking-lite, bitcoin; Afterpay lending"), cell("Medium"), cell("Larger, slower-growing; Cash App's 50M+ MAUs are the prize SoFi is chasing with Money.")],
    [cell("<b>Affirm</b><br/>$24B, ~12x P/E"), cell("BNPL / point-of-sale lending"), cell("Medium"), cell("No charter, no deposits \u2014 structurally higher funding costs than SoFi; SoFi's Peach acquisition nods at BNPL servicing.")],
    [cell("<b>Upstart</b><br/>$2.3B, ~38x P/E"), cell("AI personal-loan marketplace"), cell("Medium"), cell("Pure marketplace model: no balance sheet, no deposits. SoFi's charter is the structural rebuttal \u2014 $713M/yr funding edge.")],
    [cell("<b>Ally Financial</b><br/>~$12B, ~9x P/E"), cell("Digital banking + auto lending"), cell("Medium"), cell("The 'what SoFi looks like grown up' comp: branchless bank at ~1x book. SoFi's 2.3x book is the growth premium; Ally's 9x earnings is the derated destination if growth stalls.")],
    [cell("<b>Megabanks</b><br/>(JPM, C1/Discover)"), cell("Everything, at scale"), cell("Medium"), cell("10x the marketing budgets and entrenched primary-bank status; compete on rate and convenience, not innovation. SoFi wins the young-prime cohort they underserve.")],
    [cell("<b>Dave / Chime</b>"), cell("Neobank checking"), cell("Low"), cell("Challengers without charters or lending engines; several are Galileo clients \u2014 SoFi gets paid either way.")],
]
story.append(styled_table(comp, [30*mm, 44*mm, 18*mm, 78*mm], fontsize=7.5))
story.append(Spacer(1, 2*mm))
story.append(P("The competitive map favors SoFi's structure: every pure fintech lender (Upstart, Affirm, Dave) funds itself wholesale while SoFi funds itself with deposits; every megabank carries branch costs SoFi doesn't. Robinhood is the real long-term threat \u2014 it is attacking from the investing side toward banking, while SoFi attacks from banking toward investing. Both can win; the question is who cross-sells faster.", s_body))

# ============ 7. RISKS ============
story.append(P("7. Key risks", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
for t in [
    "<b>Fed hiking cycle (the #1 risk).</b> The September 16 hike to 3.75\u20134.00% \u2014 with the SEP implying more \u2014 arrived after SoFi set 2026 guidance on a no-cut assumption. Sustained higher rates compress loan demand and gain-on-sale margins, raise deposit competition, pressure fair values on the $46.6B held book, and have already crushed the multiple (10Y >5%). A 2027 pivot to cuts (Morningstar base case) would reverse all of this; a 'higher for longer' 2027 would not.",
    "<b>Credit cyclicality.</b> Personal loans are 73% of originations and the book is growing ~70% into a hiking cycle. Current metrics are excellent (3.7% all-in NCOs, 40 bp delinquencies), but fast-growing books always look best right before they don't. The 7\u20138% lifetime-loss tolerance is the line to watch \u2014 vintages sit at 4.68% with 35% of principal outstanding.",
    "<b>Lending concentration.</b> ~59% of revenue still comes from lending. The fee-based mix (39% and rising) mitigates but does not eliminate the cyclicality.",
    "<b>Technology Platform decline.</b> \u201323% YoY on a lost anchor client; contribution profit down 65%. The segment is small but was supposed to be the high-multiple growth leg. Another client loss would damage the 'fintech infrastructure' narrative.",
    "<b>Operating leverage proving slower than hoped.</b> The market's core complaint: 40% revenue growth with flat $0.60 EPS guidance, FinSvcs contribution margin compressing 6 pts to 46%, and Mizuho flagging a lower CET1 ratio. If 2027 doesn't show EPS leverage, the growth-multiple case breaks.",
    "<b>Valuation and sentiment.</b> 28x forward earnings and 2.3x tangible book leave no room for disappointment; beta of 2.3 means macro selloffs hit 2x as hard (YTD \u201337%). An early-2026 short-seller report and ongoing insider 10b5-1 sales add overhang.",
    "<b>Regulatory.</b> As a bank holding company SoFi faces OCC/Fed oversight; crypto and stablecoin (SoFiUSD) regulation remains unsettled; any adverse ruling on bank-fintech partnerships would hit Galileo.",
]:
    story.append(B(t))

# ============ 8. VALUATION ============
story.append(P("8. Valuation: three lenses, one answer", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
story.append(P("<b>Lens 1 \u2014 earnings-power DCF (primary).</b> Banks are valued on earnings, not revenue. We discount adjusted net income \u2014 a close proxy for free cash flow to equity given minimal dividends and buybacks roughly offsetting SBC dilution \u2014 from 2026 to 2035, with a Gordon terminal value. 2026E anchors to guidance (~$825M adjusted net income).", s_body))
dcfv = [
    [hdr("Scenario", s_theadL), hdr("Key assumptions"), hdr("Equity value"), hdr("Per share"), hdr("Weight")],
    [cell("<b>Bear</b>"), cell("Fed stays high; credit normalizes upward; Tech Platform keeps shrinking; NI CAGR ~14%; CoE 13.5%, g 2.5%"), cellR(f"${dcf_bear:.1f} bn"), cellR(f"<b>${px_bear:.2f}</b>"), cellR("25%")],
    [cell("<b>Base</b>"), cell("Deposits + LPB compound; fee mix to ~45%; NI CAGR ~18% to $3.8B by 2035; CoE 12%, g 3.5%"), cellR(f"${dcf_base:.1f} bn"), cellR(f"<b>${px_base:.2f}</b>"), cellR("50%")],
    [cell("<b>Bull</b>"), cell("Fed cuts 2027\u201328; LPB + SoFiUSD scale; NI CAGR ~22%; CoE 10.5%, g 4.0%"), cellR(f"${dcf_bull:.1f} bn"), cellR(f"<b>${px_bull:.2f}</b>"), cellR("25%")],
    [cell("<b>Weighted</b>"), cell("25 / 50 / 25"), cell(""), cellR(f"<b>${px_wtd:.2f}</b>"), cell("")],
]
story.append(styled_table(dcfv, [22*mm, 74*mm, 26*mm, 24*mm, 24*mm], fontsize=8))
story.append(Spacer(1, 2*mm))
story.append(P("<b>Lens 2 \u2014 peer multiples.</b> SoFi is the cheapest large fintech on earnings despite the fastest growth \u2014 the market prices it as a bank, not a platform. On a growth-adjusted basis (PEG ~1.4 screen, ~0.8 on 2026\u201327 EPS growth of ~35%), the discount looks excessive versus Robinhood and Block.", s_body))
mult = [
    [hdr("Company", s_theadL), hdr("Market cap"), hdr("Trailing P/E"), hdr("Comment")],
    [cell("<b>SoFi</b>"), cellR("$21.7 bn"), cellR("34.1x"), cellR("~28x 2026E ($0.60); 2.3x tangible book; 40% rev growth")],
    [cell("Robinhood"), cellR("$108.6 bn"), cellR("52.4x"), cellR("Closest comp; 5x the cap, slower user growth")],
    [cell("Block"), cellR("$46.2 bn"), cellR("129.2x"), cellR("Slower growth, far richer multiple")],
    [cell("Affirm"), cellR("$24.1 bn"), cellR("12.5x"), cellR("Trailing depressed; no charter, wholesale-funded")],
    [cell("Upstart"), cellR("$2.3 bn"), cellR("38.4x"), cellR("Marketplace model; +42% revenue, barely profitable")],
    [cell("Ally Financial"), cellR("~$11.7 bn"), cellR("9.1x"), cellR("Pure digital bank; the derated end-state comp")],
]
story.append(styled_table(mult, [32*mm, 28*mm, 28*mm, 82*mm], fontsize=8))
story.append(P("Market caps and trailing P/E as of September 25\u201326, 2026 (Finnhub). A straight Robinhood-multiple re-rating is not the thesis \u2014 even a partial close of the fintech/bank multiple gap, funded by 35%+ EPS growth, gets the stock to our target.", s_small))
story.append(Spacer(1, 2*mm))
story.append(P("<b>Lens 3 \u2014 sum of the parts (annualized Q2 2026).</b> Lending contribution profit ($399M \u00d7 4) at 10x bank-like earnings = $16.0B; Financial Services contribution (~46% margin on $466M \u00d7 4) at 12x = $10.3B; Technology Platform revenue ($84.5M \u00d7 4) at 9x SaaS-like sales = $3.0B. Total equity ~$29.3B \u00f7 1.31B shares = <b>$"
+ f"{px_sotp:.2f}/share</b> \u2014 within 5% of our DCF-weighted value, despite the Tech Platform trough depressing its slice.", s_body))
story.append(P("<b>Target:</b> DCF-weighted $"
+ f"{px_wtd:.2f} and SOTP ${px_sotp:.2f} bracket our <b>${TARGET:.2f}</b> 12-month target, implying <b>+{UPSIDE:.0f}% upside</b> from $16.58. Street consensus averages ~$22.50 (23 analysts: 9 Buy, 11 Hold, 3 Sell) \u2014 we sit a touch above the Street, with a more constructive view on deposit-led operating leverage.", s_small))

# ============ 9. RECOMMENDATION ============
story.append(P("9. Recommendation", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
story.append(P("We rate SoFi <b><font color=\"#0E7C3E\">BUY</font></b> with a <b>$"
+ f"{TARGET:.2f}</b> 12-month price target (+{UPSIDE:.0f}% upside), <b>High risk</b>. The thesis in one line: the market is valuing a 40%-growth, 30%-margin, deposit-funded digital bank with improving credit and a scaling fee engine at a cyclical-lender multiple because the Fed started hiking again \u2014 we think the earnings power wins.", s_body))
story.append(P("<b>What gets us there (catalysts):</b> Q3 2026 results in late October confirming the 30%+ member-growth and LPB trajectory; continued $5B+/quarter deposit growth compounding the funding advantage; SoFi Plus scaling past 500k paid members; any Fed signal toward 2027 cuts; stablecoin/SEN adoption milestones.", s_body))
story.append(P("<b>What breaks the thesis:</b> a 'higher for longer' 2027 that stalls originations and pressures credit; personal-loan losses breaching the 7\u20138% lifetime tolerance; further Technology Platform client losses; or another year of revenue growth without EPS leverage \u2014 any of which pushes fair value toward our $"
+ f"{px_bear:.2f} bear case. That is why this is a starter-sized, high-risk position, not a core holding.", s_body))
story.append(P("<b>Positioning:</b> for investors who can tolerate macro volatility and a 2.3 beta, SoFi offers 40% upside to our $"
+ f"{TARGET:.2f} target ($"+ f"{px_bull:.2f} bull case, +{px_bull/PRICE*100-100:.0f}%) with a profitable, deposit-funded core limiting the downside. Initiate at current levels; add on Q3 evidence that credit and LPB momentum are intact through the hiking cycle.", s_body))

# ============ APPENDIX ============
story.append(P("Appendix: sources and verification notes", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
story.append(P("Company: SoFi Q2 2026 press release (Business Wire, July 29, 2026); Q1 2026 release (April 29, 2026); Q4/FY2025 release (Business Wire, Jan 30, 2026); Q2 2026 earnings call commentary (CFO Chris Lapointe, CEO Anthony Noto). Market data as of September 25\u201326, 2026 (Finnhub; MarketBeat consensus). Press/analysis: CoinDesk and Unchained (SoFi\u2013Kraken/Payward partnership, Sept 3, 2026); IBD (SoFiUSD/stablecoin, Sept 2026); securities.io (Mastercard/SoFiUSD settlement); Zacks (credit quality, Sept 22, 2026); Motley Fool (charter advantage, Sept 19/24/26, 2026); Reuters/coresight (Sept 16 FOMC hike); Morningstar (rate outlook); analyst actions via MarketBeat/tickergate (Scotiabank, Piper Sandler, Needham, Mizuho, Goldman Sachs, Wells Fargo, Truist, Morgan Stanley, Loop Capital). Product pricing: sofi.com rate sheet (Sept 23, 2026) \u2014 3.30% APY savings with direct deposit, 0.50% checking, $10/month SoFi Plus.", s_small))
story.append(Spacer(1, 2*mm))
story.append(P("Items we could not fully verify and excluded from the valuation: the identity of the departed Technology Platform anchor client; the precise Galileo enabled-account count (company no longer discloses; last public figure 100M+ in 2022); the early-2026 short-seller report's specific claims; exact Q3 2025 segment splits beyond reported totals. Q2 2025 deposit figure is estimated from reported growth rates. Adjusted metrics are non-GAAP; see company reconciliations. This analysis was prepared September 26, 2026 for informational purposes only and is not investment advice; all forward-looking statements involve risk and uncertainty.", s_small))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=18*mm,
                        title="SoFi Technologies (SOFI) \u2014 Equity Research Note", author="Investment Research")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("wrote", OUT)
