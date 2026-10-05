#!/usr/bin/env python3
"""Build the Fidelity National Information Services (FIS) equity research note PDF."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                HRFlowable)
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.lib import colors

OUT = "/home/hatch/workspace/your_files/fis-equity-research/fis-equity-research-note.pdf"

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
SHARES_BN = 0.515         # diluted shares outstanding, billions (~FY2025 10-K: 519m)
NET_DEBT_BN = 16.2        # Q2 2026 10-Q: $16.95B debt - $0.74B cash, post-TSYS deal
PRICE = 35.41             # Sept 25, 2026 close (priced Sept 26, 2026)

def fcf_dcf(fcf0, growth, wacc, g_term):
    fcf = fcf0; pv = 0.0
    for i, g in enumerate(growth):
        fcf *= (1 + g)
        pv += fcf / (1 + wacc) ** (i + 1)
    tv = fcf * (1 + g_term) / (wacc - g_term)
    pv += tv / (1 + wacc) ** len(growth)
    return pv             # $bn enterprise value

base_g = [0.07, 0.065, 0.06, 0.055, 0.05, 0.045, 0.04, 0.035, 0.03, 0.03]
bear_g = [0.04, 0.035, 0.03, 0.03, 0.025, 0.025, 0.02, 0.02, 0.02, 0.02]
bull_g = [0.09, 0.085, 0.08, 0.07, 0.065, 0.055, 0.05, 0.045, 0.04, 0.035]

ev_base = fcf_dcf(2.20, base_g, 0.09, 0.025)
ev_bear = fcf_dcf(2.20, bear_g, 0.10, 0.020)
ev_bull = fcf_dcf(2.20, bull_g, 0.085, 0.030)

px_bear = (ev_bear - NET_DEBT_BN) / SHARES_BN
px_base = (ev_base - NET_DEBT_BN) / SHARES_BN
px_bull = (ev_bull - NET_DEBT_BN) / SHARES_BN
px_wtd = 0.25 * px_bear + 0.50 * px_base + 0.25 * px_bull
TARGET = round(px_wtd * 2) / 2
UPSIDE = (TARGET - PRICE) / PRICE * 100

# Adjusted-P/E cross-check on 2027E adjusted EPS (~$6.63 = 2026E $6.195 x 1.07)
px_pe_low = 6.63 * 7.0
px_pe_high = 6.63 * 8.5

print(f"DCF EV ($bn): bear {ev_bear:.1f} / base {ev_base:.1f} / bull {ev_bull:.1f}")
print(f"DCF per-share: ${px_bear:.2f} / ${px_base:.2f} / ${px_bull:.2f}  -> weighted ${px_wtd:.2f}")
print(f"Adj-P/E cross-check 2027E: ${px_pe_low:.2f} - ${px_pe_high:.2f}")
print(f"TARGET ${TARGET:.2f}  UPSIDE {UPSIDE:.1f}%")

story = []
W, H = A4

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7); canvas.setFillColor(DGRAY)
    canvas.drawString(18*mm, 12*mm, "Fidelity National Information Services, Inc. (NYSE: FIS)  \u2014  Equity Research Note  \u2014  September 2026")
    canvas.drawRightString(W - 18*mm, 12*mm, f"Page {doc.page}")
    canvas.setStrokeColor(MGRAY); canvas.setLineWidth(0.5)
    canvas.line(18*mm, 14.5*mm, W - 18*mm, 14.5*mm)
    canvas.restoreState()

# ============ COVER ============
story.append(Spacer(1, 24*mm))
story.append(P("FIDELITY NATIONAL INFORMATION SERVICES, INC.", ParagraphStyle("x", parent=s_sub, fontName="Helvetica-Bold", fontSize=13, textColor=ACCENT, spaceAfter=2)))
story.append(P("The Worldpay Hangover<br/>Is Over", s_title))
story.append(Spacer(1, 4*mm))
story.append(P("Equity Research Note  \u00b7  Technology \u2014 Financial Infrastructure / Payments  \u00b7  September 26, 2026", s_sub))
story.append(Spacer(1, 8*mm))

rating_data = [
    [hdr("Recommendation", s_theadL), hdr("12-Mo. Price Target"), hdr("Current Price"), hdr("Implied Upside"), hdr("Risk Rating")],
    [Paragraph("<b><font color=\"#0E7C3E\" size=\"13\">BUY</font></b>", s_cellC),
     Paragraph(f"<b><font size=\"12\">${TARGET:.2f}</font></b>", s_cellC),
     Paragraph("<b><font size=\"12\">$35.41</font></b><br/><font size=\"7\" color=\"#5A6472\">Sep 25, 2026 close</font>", s_cellC),
     Paragraph(f"<b><font color=\"#0E7C3E\" size=\"12\">+{UPSIDE:.0f}%</font></b>", s_cellC),
     Paragraph("<b>High</b>", s_cellC)],
]
story.append(styled_table(rating_data, [34*mm, 34*mm, 34*mm, 34*mm, 34*mm], fontsize=9))
story.append(Spacer(1, 6*mm))

story.append(P("FIS trades at <b>5.7x 2026E adjusted EPS</b> and a <b>12% free-cash-flow yield</b> while paying a <b>5% dividend</b> \u2014 pricing more appropriate to a melting legacy vendor than to the company that just closed the defining transaction of its decade. On January 9, 2026, FIS completed the twin deal that ends the Worldpay era: it acquired Global Payments' Issuer Solutions business (the former TSYS \u2014 the world's largest card-issuing platform) for $13.5 billion enterprise value, and simultaneously sold its remaining 45% Worldpay stake. The non-cash-generating minority holding is gone; in its place sits a high-margin, recurring-revenue issuing franchise with 72% of revenue contracted through 2029 and $150M+ of targeted EBITDA synergies by 2028. Q2 2026 showed the machine working: pro-forma revenue +5.3%, adjusted EBITDA +7.4% with 113 bps of margin expansion, adjusted EPS +8.8%, and free cash flow more than tripling to $525M \u2014 prompting a $100M raise to the full-year FCF outlook ($2.15\u20132.25B). Yes, management trimmed the 2026 revenue outlook, and yes, the balance sheet now carries ~$16B of net debt. But at $35.41 \u2014 a 52-week low, down 47% year-to-date \u2014 the market prices FIS as if the TSYS deal were another Worldpay. We think it is the opposite: a disciplined swap of a passive stake for an operating asset that management knows how to run. Our scenario-weighted FCF DCF points to $"
+ f"{px_wtd:.2f}; we set a <b>${TARGET:.2f}</b> target and rate the shares <b>BUY</b>. This is a <b>High-risk</b> call \u2014 leverage, integration, and a management team with a $17B writedown in its past demand position sizing, not conviction sizing.", s_body))
story.append(Spacer(1, 3*mm))

stats = [
    [cell("<b>Market cap</b>", s_cellB), cellR("~$18.1 bn"), cell("<b>Shares out. (diluted)</b>", s_cellB), cellR("~515 m")],
    [cell("<b>52-week range</b>", s_cellB), cellR("$34.22 \u2013 $69.14"), cell("<b>YTD / 1-yr return</b>", s_cellB), cellR("-47% / -45%")],
    [cell("<b>2026E adj. EPS / P/E</b>", s_cellB), cellR("$6.15\u20136.24 / ~5.7x"), cell("<b>2026E FCF / yield</b>", s_cellB), cellR("$2.15\u20132.25 bn / ~12%")],
    [cell("<b>Dividend (annualized)</b>", s_cellB), cellR("$1.76 (~5.0% yield)"), cell("<b>Net debt (Q2 2026)</b>", s_cellB), cellR("~$16.2 bn")],
]
story.append(styled_table(stats, [42*mm, 43*mm, 42*mm, 43*mm], header_rows=0, zebra=True, fontsize=8.5))
story.append(Spacer(1, 4*mm))
story.append(P("Prices as of September 25, 2026 close. Financial figures from company releases (Q2 2026 reported August 4, 2026; Q1 2026 May 2026) and SEC filings (Q2 2026 10-Q filed August 4, 2026; FY2025 10-K filed February 24, 2026). Not to be confused with Fiserv, Inc. (FI) \u2014 a separate company. This note is an independent research-style analysis for informational purposes, not investment advice.", s_small))

# ============ 1. INVESTMENT THESIS ============
story.append(P("1. Investment thesis", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
for t in [
    "<b>The Worldpay chapter is closed \u2014 and the market hasn't noticed.</b> The January 2026 twin transaction (acquire TSYS Issuer Solutions for $13.5B EV; sell the remaining 45% Worldpay stake to Global Payments) converts a passive, non-cash-generating minority holding into the world's largest card-issuing business: 40B+ transactions a year, 75+ countries, 150+ financial-institution clients, and 72% of its revenue already contracted through 2029. FIS is now a focused banking-and-capital-markets technology provider, not a sprawling fintech conglomerate.",
    "<b>The operating numbers are working.</b> Q2 2026: revenue $3.38B (+29.1% reported, +5.3% pro forma), Banking Solutions +6.1% pro forma on strong demand for payments, fraud, data and modernization products; Capital Market Solutions +3.5% with a 51.9% adjusted EBITDA margin; adjusted EPS $1.48 (+8.8%, a beat); free cash flow $525M \u2014 more than tripled YoY \u2014 driving a $100M raise to the full-year FCF guide ($2.15\u20132.25B). FCF is the metric that matters here, and it is accelerating.",
    "<b>Absurd valuation for the cash being generated.</b> At 5.7x 2026E adjusted EPS ($6.15\u20136.24 guide), a ~12% FCF yield, and a 5.0% dividend yield covered at just 27% of adjusted earnings, FIS is priced like a declining business. Peers: Fiserv ~8.7x P/E, Global Payments ~6.3x 2026E adjusted EPS, Adyen ~24x. A mere re-rating to 7.5\u20138.5x 2027E adjusted EPS (~$6.63) implies $50\u2013$56 \u2014 before any synergy upside.",
    "<b>Synergies are concrete and contracted.</b> Management targets $150M+ of EBITDA benefit from the TSYS integration by 2028; joint-client ACV sales are already up 35% YoY; and two large international banks signed in Q2. This is cross-sell into FIS's installed banking base \u2014 the lowest-risk kind of synergy.",
    "<b>Capital allocation is shareholder-friendly.</b> The $1.76 annualized dividend (5.0% yield) was just paid September 25; the payout ratio is a conservative 27% of adjusted EPS, leaving ample room for deleveraging from the current ~2.9x net-debt-to-adjusted-EBITDA toward management's comfort zone.",
    "<b>Our DCF: $"
    + f"{px_bear:.2f} / ${px_base:.2f} / ${px_bull:.2f} (bear/base/bull), weighted ${px_wtd:.2f}.</b> The base case assumes mid-single-digit FCF growth compounding off the $2.2B 2026E base at a 9% cost of capital \u2014 hardly heroic for a business with 90%+ recurring revenue. Even the bear case ($"
    + f"{px_bear:.2f}) is within shouting distance of today's price, which is what a margin of safety looks like.",
    "<b>Why it is High risk, not a core holding.</b> Net debt of ~$16B after the $13.5B TSYS bet; management trimmed 2026 revenue guidance (pro-forma growth cut to 4.5\u20135.0%); Baird cut its target on September 25; and this is the team that paid $43B for Worldpay in 2019 and wrote down ~$17B. The stock sits at its 52-week low for a reason \u2014 execution must now be flawless. Size accordingly.",
]:
    story.append(B(t))

# ============ 2. COMPANY OVERVIEW ============
story.append(P("2. Company overview: what FIS actually does", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
story.append(P("Fidelity National Information Services, Inc. (NYSE: FIS), headquartered in Jacksonville, Florida, is a global financial-technology company providing software and technology solutions to banks, businesses, and financial institutions \u2014 core banking platforms, payments processing, capital-markets systems, and related services. CEO Stephanie Ferris has led the company through the Worldpay separation and the portfolio reshaping. Following the January 2026 transactions, FIS reports in two segments:", s_body))
story.append(P("<b>Banking Solutions (~74% of revenue).</b> Core banking platforms, digital banking, payments (including the newly acquired <b>FIS Total Issuing Solutions</b> \u2014 the former TSYS \u2014 the world's largest card-issuing business: credit processing, fraud, loyalty, 40B+ annual transactions across 75+ countries), plus lending, fraud prevention, data and cybersecurity solutions sold to financial institutions. Q2 2026: $2.5B revenue (+44% reported on the acquisition, +6.1% pro forma), adjusted EBITDA +10.6% pro forma, recurring revenue +5%. Management cites accelerating demand for modernization and AI-adjacent products (TreasuryGPT, Banker Assist).", s_body))
story.append(P("<b>Capital Market Solutions (~24% of revenue).</b> Trading, risk, treasury and wealth-management technology for buy-side and sell-side institutions \u2014 the highest-margin, most software-like part of FIS. Q2 2026: $810M revenue (+3.5%) at a 51.9% adjusted EBITDA margin. This segment is the quiet compounder inside the conglomerate.", s_body))
story.append(P("<b>How it makes money:</b> predominantly recurring \u2014 multi-year outsourcing and processing contracts, per-transaction and per-account fees, software licenses and maintenance. Banking Solutions' recurring revenue grew 5% in Q2; 72% of Total Issuing revenue is contracted through 2029 or later. The model is the classic bank-tech annuity: sticky, high-switching-cost, and cash-generative.", s_body))

# ============ 3. THE WORLDPAY/TSYS TRANSFORMATION ============
story.append(P("3. The Worldpay-to-TSYS transformation", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
story.append(P("To understand FIS at $35, you must understand the $43 billion mistake \u2014 and its resolution:", s_body))
for t in [
    "<b>2019: the empire-building peak.</b> FIS acquired Worldpay for ~$43B, becoming a merchant-acquiring giant just as Stripe, Adyen and Square were rewriting the category.",
    "<b>2022\u20132023: the reckoning.</b> The merchant business underperformed; FIS recorded a ~$17B impairment that drove a $16.7B GAAP net loss in 2022 (SEC 10-K), settled a $210M investor lawsuit, and began a multi-year restructuring.",
    "<b>January 2024: the first exit.</b> FIS sold a 55% stake in Worldpay Merchant Solutions to GTCR, retaining a 45% non-controlling interest \u2014 a passive holding generating no cash for FIS.",
    "<b>January 9, 2026: the clean break.</b> In a single coordinated close, FIS (i) acquired Global Payments' Issuer Solutions business (TSYS) at $13.5B enterprise value \u2014 $12B net including $1.5B of NPV tax assets \u2014 funded by ~$7.7B of new debt plus the Worldpay stake, and (ii) sold its remaining 45% Worldpay interest to Global Payments. FIS now owns zero of Worldpay.",
]:
    story.append(B(t))
story.append(P("The strategic logic is sound: FIS traded a <b>passive minority stake</b> for an <b>operating asset it understands</b> \u2014 issuing is the natural complement to its banking platform (issuers and acquirers are two sides of the same card transaction), the revenue is high-margin and recurring, and the cross-sell runs into FIS's existing bank relationships rather than requiring new customer acquisition. The $1.5B of tax assets sweeten the effective price to ~$12B net, or roughly 10x the unit's EBITDA \u2014 a full but fair multiple for the world's largest issuing franchise. The risk, stated plainly: it is another large, debt-funded acquisition from the team that authored Worldpay. The difference this time is that FIS is buying what it knows (bank technology) rather than what it didn't (merchant acquiring).", s_body))

# ============ 4. FINANCIAL REVIEW ============
story.append(P("4. Financial review", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
story.append(P("<b>Q2 2026 (reported August 4, 2026): the machine is working; the guide was trimmed.</b> Revenue of $3.38B (+29.1% reported, +5.3% pro forma) met consensus; adjusted EPS of $1.48 beat by a penny and grew 8.8%; adjusted EBITDA of $1.4B grew 7.4% pro forma with 113 bps of margin expansion; and adjusted free cash flow of $525M more than tripled YoY. Management raised the full-year FCF outlook by $100M \u2014 but narrowed the revenue outlook (adjusted revenue $13.63\u201313.70B; pro-forma growth 4.5\u20135.0%, down from 5.1\u20135.7%) and the EBITDA growth outlook (5.9\u20136.9% pro forma). The market punished the trim: the stock fell 1.2% on the print and has since slid to its 52-week low. Q3 2026 guidance: adjusted EPS $1.58\u20131.62.", s_body))

q2 = [
    [hdr("Q2 2026 metric", s_theadL), hdr("Q2 2026"), hdr("Q2 2025"), hdr("Change")],
    [cell("Revenue (reported / pro forma)"), cellR("$3.38 bn"), cellR("$2.62 bn"), cellR("+29.1% / +5.3% pf")],
    [cell("Banking Solutions revenue"), cellR("$2.50 bn"), cellR("n/a"), cellR("+44% / +6.1% pf")],
    [cell("Capital Market Solutions revenue"), cellR("$810 m"), cellR("n/a"), cellR("+3.5%")],
    [cell("CMS adjusted EBITDA margin"), cellR("51.9%"), cellR("n/a"), cellR("software-like")],
    [cell("Adjusted EBITDA"), cellR("$1.40 bn"), cellR("~$1.04 bn"), cellR("+35% / +7.4% pf")],
    [cell("Adjusted EPS"), cellR("$1.48"), cellR("$1.36"), cellR("+8.8%, beat by $0.01")],
    [cell("Adjusted free cash flow"), cellR("$525 m"), cellR("~$164 m"), cellR("more than tripled")],
    [cell("Net margin (GAAP) / ROE"), cellR("27.6% / 21.0%"), cellR("n/a"), cellR("GAAP, incl. items")],
]
story.append(styled_table(q2, [62*mm, 36*mm, 36*mm, 36*mm]))
story.append(P("pf = pro forma (as if the TSYS acquisition had been owned throughout). Source: company Q2 2026 release; MarketBeat consensus.", s_small))
story.append(Spacer(1, 2*mm))

story.append(P("<b>Quarterly revenue trajectory (SEC 10-Q filings):</b> the step-change in Q1 2026 is the TSYS acquisition closing (January 9, 2026).", s_body))
d = Drawing(170*mm, 62*mm)
bc = VerticalBarChart()
bc.x = 12*mm; bc.y = 12*mm; bc.height = 42*mm; bc.width = 140*mm
bc.data = [[2616,2717,2700,3295,3377]]
bc.strokeColor = colors.white
bc.barLabels.nudge = 8
bc.categoryAxis.labels.boxAnchor = "ne"; bc.categoryAxis.labels.angle = 0
bc.categoryAxis.categoryNames = ["Q2'25","Q3'25","Q4'25*","Q1'26","Q2'26"]
bc.categoryAxis.labels.fontSize = 6.5
bc.valueAxis.valueMin = 0; bc.valueAxis.valueMax = 3750; bc.valueAxis.valueStep = 750
bc.valueAxis.labels.fontSize = 6.5
bc.bars[0].fillColor = NAVY
bc.barLabelFormat = "%d"
story.append(d)
story.append(P("Quarterly revenue ($m). *Q4 2025 estimated from reported full-year trajectory. Q1\u2013Q2 2026 include Total Issuing Solutions. Source: SEC 10-Q filings (EDGAR).", s_small))
story.append(Spacer(1, 2*mm))

story.append(P("<b>Full-year anchors (SEC 10-K, filed February 24, 2026):</b> FY2025 GAAP net income $511M (vs $281M in 2024 and the $16.7B Worldpay-impairment loss in 2022) \u2014 GAAP earnings remain depressed by acquisition amortization, which is why the market's 5.4x P/E is quoted on a GAAP EPS of ~$0.73 while adjusted EPS runs at $6+. Diluted shares ~519M. FY2026 guidance (revised August 4, 2026): adjusted revenue $13.63\u201313.70B, adjusted EBITDA growth 5.9\u20136.9% pro forma, adjusted EPS $6.15\u20136.24 (+7.0\u20138.5%), adjusted FCF $2.15\u20132.25B (raised $100M).", s_body))
story.append(P("<b>Balance sheet: levered, but the debt bought cash flow.</b> Q2 2026 10-Q: total debt $16.95B ($15.43B noncurrent + $1.52B current), cash $0.74B \u2192 net debt ~$16.2B, or ~2.9x 2026E adjusted EBITDA (~$5.7B). Debt-to-equity 0.96; current ratio 0.53 (typical for the business model \u2014 client settlement balances). The $7.7B of new debt funded the TSYS acquisition; deleveraging from FCF ($2.2B/year) is now the central capital-allocation task alongside the dividend.", s_body))
story.append(P("<b>Capital allocation: dividend first, deleverage second.</b> Quarterly dividend $0.44 ($1.76 annualized, ~5.0% yield), just paid September 25 to holders of record September 11 \u2014 the payout ratio is only ~27% of adjusted EPS, so the dividend is secure and has room to grow. With FCF of $2.15\u20132.25B against $0.9B of dividend payments, roughly $1.3B annually is available for debt paydown (and, in time, buybacks).", s_body))

# ============ 5. GROWTH OUTLOOK ============
story.append(P("5. Growth outlook", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
for t in [
    "<b>TSYS integration and the $150M synergy target.</b> 72% of Total Issuing revenue is contracted through 2029+; joint-client ACV sales +35% YoY; two large international bank wins in Q2. Issuing cross-sell into FIS's banking base is the near-term growth engine, with the synergy benefit building toward $150M+ of EBITDA by 2028.",
    "<b>Banking modernization demand.</b> Management cites strong demand across payments, fraud prevention, data, lending, and cybersecurity \u2014 recurring revenue +5% in Q2. Regional and mid-market banks are the structural buyers: they cannot build this technology themselves.",
    "<b>AI products as an upsell vector.</b> TreasuryGPT, Banker Assist, and a new commerce product letting banks transact with AI agents \u2014 management describes ~20% growth in recurring ACV partly driven by AI upselling. Early, but it gives the sales force something new to sell into the installed base.",
    "<b>Capital Market Solutions compounding.</b> The 51.9%-margin segment grows mid-single-digits on trading-technology and risk demand \u2014 the closest thing FIS has to a pure software business, and a natural candidate for a premium multiple in any sum-of-the-parts.",
]:
    story.append(B(t))
story.append(P("The 2026 guide trim is the cloud: pro-forma revenue growth cut to 4.5\u20135.0% says the core is growing, but not accelerating. Our DCF assumes mid-single-digit FCF growth \u2014 consistent with the guide, not heroic versus it. The upside case is that TSYS synergies and AI upsell push growth back toward the high single digits by 2028.", s_body))

# ============ 6. MOAT ============
story.append(P("6. Moat assessment", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
story.append(P("FIS's moat is <b>switching costs + scale in bank technology</b> \u2014 we rate it <b>narrow-to-moderate, stable</b>. Core banking platforms and card-issuing systems are deeply embedded in a bank's operations; replacing them is a multi-year, high-risk project, which is why 72% of issuing revenue is contracted through 2029 and recurring revenue grows steadily. Scale matters: the combined FIS/TSYS issuing platform processes 40B+ transactions annually, giving it data and cost advantages smaller processors cannot match. It is not a wide moat \u2014 banks periodically re-bid, fintechs (Adyen, Stripe) attack the edges, and the Worldpay episode proved management can impair the franchise \u2014 but the annuity-like revenue base (90%+ recurring) and the Capital Markets segment's software margins support a durable, if unexciting, competitive position.", s_body))

# ============ 7. COMPETITION ============
story.append(P("7. Competition", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
comp = [
    [hdr("Rival", s_theadL), hdr("Where it competes"), hdr("Threat"), hdr("Read-through")],
    [cell("<b>Fiserv (FI)</b><br/>~$25B, ~8.7x P/E"), cell("Core banking + merchant (Clover); the closest comp"), cell("High"), cell("The valuation benchmark: similar business, similar growth, 8.7x earnings vs FIS at 5.7x. The gap is the opportunity \u2014 or a warning about FIS-specific hair.")],
    [cell("<b>Global Payments (GPN)</b><br/>~$22.6B, ~6.3x '26E adj. EPS"), cell("Merchant (now incl. Worldpay) + former issuer unit"), cell("Medium"), cell("The mirror image of FIS's 2026 deal: GPN bought Worldpay, sold TSYS to FIS. GPN guides $13.60\u201313.80 adj. EPS; both stocks are deeply derated.")],
    [cell("<b>Adyen</b><br/>~24x P/E"), cell("Enterprise payments platform"), cell("Medium"), cell("The growth premium comp (20\u201326x EBITDA). Shows what the market pays for clean execution \u2014 FIS trades at ~6x EV/EBITDA, a 4x discount.")],
    [cell("<b>Jack Henry (JKHY)</b>"), cell("Core banking for community banks"), cell("Medium"), cell("The pure-play bank-tech comp; consistently earns a premium multiple on best-in-class execution \u2014 the multiple FIS would merit if it executed like JKHY.")],
    [cell("<b>Stripe / Square / fintechs</b>"), cell("Payments edges, SMB"), cell("Low\u2013Med"), cell("Took share from Worldpay's merchant business \u2014 the problem FIS has now exited. Less relevant to the remaining banking/issuing franchise.")],
]
story.append(styled_table(comp, [30*mm, 44*mm, 18*mm, 78*mm], fontsize=7.5))
story.append(Spacer(1, 2*mm))
story.append(P("The competitive map now favors FIS's focus: it no longer fights Stripe and Adyen for merchants \u2014 it sells picks-and-shovels to the banks that all of them ultimately settle through.", s_body))

# ============ 8. RISKS ============
story.append(P("8. Key risks", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
for t in [
    "<b>Leverage after the $13.5B bet.</b> Net debt of ~$16.2B is ~2.9x 2026E adjusted EBITDA. The FCF ($2.2B) covers the dividend ($0.9B) with ~$1.3B left for paydown \u2014 adequate, but a recession that dents bank IT spending would slow deleveraging and could pressure the dividend-growth story.",
    "<b>TSYS integration risk.</b> Large bank-tech integrations are where value goes to die: client churn, synergy shortfalls, or culture clashes would replay the Worldpay trauma. The $150M synergy target by 2028 and the 35% ACV growth are early but not yet proof.",
    "<b>Management's M&A track record.</b> The team that paid $43B for Worldpay and wrote down ~$17B is asking to be trusted on a $13.5B deal. The strategic logic is better this time (buying what they know), but the burden of proof is on them \u2014 and the market is pricing skepticism.",
    "<b>The guidance trim.</b> Cutting 2026 pro-forma revenue growth to 4.5\u20135.0% two quarters into the TSYS era raises the question of whether the core is decelerating. Another trim would break the thesis; our bear case ($"
    + f"{px_bear:.2f}) assumes exactly that.",
    "<b>Analyst sentiment is soft.</b> Baird cut its price target on September 25; the 50-day ($40.85) and 200-day ($42.92) moving averages sit well above the price \u2014 the chart is in a confirmed downtrend and value traps can stay cheap.",
    "<b>Client concentration and bank consolidation.</b> Large-bank mergers can strand FIS contracts; the business depends on banks continuing to outsource rather than build.",
]:
    story.append(B(t))

# ============ 9. VALUATION ============
story.append(P("9. Valuation: three lenses, one answer", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
story.append(P("<b>Lens 1 \u2014 free-cash-flow DCF (primary).</b> For a mature, acquisitive processor, free cash flow is the honest metric \u2014 it cuts through the amortization that depresses GAAP EPS to ~$0.73. We discount adjusted FCF from the 2026E base of $2.20B (the raised guidance midpoint) over ten years with a Gordon terminal value, then subtract $16.2B of net debt (Q2 2026 10-Q, post-TSYS).", s_body))
dcfv = [
    [hdr("Scenario", s_theadL), hdr("Key assumptions"), hdr("Enterprise value"), hdr("Per share"), hdr("Weight")],
    [cell("<b>Bear</b>"), cell("Integration stumbles; FCF CAGR ~2.5%; WACC 10%, g 2.0%"), cellR(f"${ev_bear:.1f} bn"), cellR(f"<b>${px_bear:.2f}</b>"), cellR("25%")],
    [cell("<b>Base</b>"), cell("Mid-single-digit FCF growth; synergies land; WACC 9%, g 2.5%"), cellR(f"${ev_base:.1f} bn"), cellR(f"<b>${px_base:.2f}</b>"), cellR("50%")],
    [cell("<b>Bull</b>"), cell("High-single-digit FCF growth; AI upsell; WACC 8.5%, g 3.0%"), cellR(f"${ev_bull:.1f} bn"), cellR(f"<b>${px_bull:.2f}</b>"), cellR("25%")],
    [cell("<b>Weighted</b>"), cell("25 / 50 / 25"), cell(""), cellR(f"<b>${px_wtd:.2f}</b>"), cell("")],
]
story.append(styled_table(dcfv, [22*mm, 74*mm, 26*mm, 24*mm, 24*mm], fontsize=8))
story.append(Spacer(1, 2*mm))
story.append(P("<b>Lens 2 \u2014 peer multiples.</b> On 2026E adjusted EPS of ~$6.20, FIS trades at 5.7x \u2014 a 35% discount to Fiserv (8.7x) and a ~10% discount to Global Payments (~6.3x on 2026E adjusted EPS), despite comparable growth and a superior FCF profile. Rolling to 2027E adjusted EPS of ~$6.63, a 7.0\u20138.5x multiple \u2014 still a discount to Fiserv \u2014 implies <b>$"
+ f"{px_pe_low:.2f}\u2013${px_pe_high:.2f}</b>. On EV/EBITDA, FIS trades at ~6.1x 2026E ($34.6B EV on ~$5.7B adjusted EBITDA) versus Adyen at 20x+: the market assigns zero value to any re-rating.", s_body))
story.append(Spacer(1, 2*mm))
story.append(P("<b>Lens 3 \u2014 dividend and FCF yield.</b> A 5.0% dividend yield at a 27% payout ratio is the market's way of saying the dividend is safe but the business is ex-growth. If FIS merely sustains mid-single-digit FCF growth, a 12% FCF yield is the kind of starting valuation from which even modest multiple normalization generates 40%+ total returns.", s_body))
story.append(P("<b>Target:</b> DCF-weighted $"
+ f"{px_wtd:.2f} and the peer-multiple cross-check (${px_pe_low:.2f}\u2013${px_pe_high:.2f}) bracket our <b>${TARGET:.2f}</b> 12-month target, implying <b>+{UPSIDE:.0f}% upside</b> from $35.41 plus the 5% dividend. The bear case ($"
+ f"{px_bear:.2f}) sits near today's price \u2014 the downside is the multiple staying where it is, not a fundamental impairment.", s_small))

# ============ 10. RECOMMENDATION ============
story.append(P("10. Recommendation", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
story.append(P("We rate FIS <b><font color=\"#0E7C3E\">BUY</font></b> with a <b>$"
+ f"{TARGET:.2f}</b> 12-month price target (+{UPSIDE:.0f}% upside), <b>High risk</b>. The thesis in one line: the market is pricing FIS for the Worldpay disaster it just exited, while the company it actually is today \u2014 a focused bank-tech annuity generating $2.2B of annual free cash flow, paying a 5% dividend, and integrating the world's largest issuing franchise \u2014 trades at 5.7x adjusted earnings.", s_body))
story.append(P("<b>What gets us there (catalysts):</b> Q3 2026 results on ~November 4 confirming the TSYS integration and the $1.58\u20131.62 adjusted EPS guide; synergy milestones and large-bank issuing wins; continued FCF beats funding visible deleveraging; any stabilization in the chart that forces quant/value re-engagement.", s_body))
story.append(P("<b>What breaks the thesis:</b> a second 2026 guidance cut; TSYS client churn or synergy shortfalls; leverage failing to decline; or renewed large-bank consolidation stranding contracts \u2014 any of which pushes fair value toward our $"
+ f"{px_bear:.2f} bear case. This is a high-conviction-on-valuation, low-conviction-on-management position: size it as a deep-value stub, not a core holding, and let the $1.76 dividend pay you to wait.", s_body))

# ============ APPENDIX ============
story.append(P("Appendix: sources and verification notes", s_h1))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=4))
story.append(P("Company: FIS Q2 2026 earnings release (August 4, 2026); Q2 2026 10-Q filed August 4, 2026 (EDGAR); FY2025 10-K filed February 24, 2026 (EDGAR) \u2014 revenue, net income, debt, cash, shares and segment facts pulled directly from XBRL companyfacts; FIS 8-K on the January 9, 2026 closing of the Issuer Solutions acquisition and Worldpay minority-interest sale (via StockTitan); FIS January 2026 closing announcement (CEO Stephanie Ferris; $13.5B EV / $12B net incl. $1.5B tax assets; $7.7B new debt; 40B+ transactions, 75+ countries, 150+ clients). Market data as of September 25\u201326, 2026 (Finnhub; MarketBeat; Barchart). Peer data: Fiserv (FI) P/E ~8.7x (Simply Wall St, Sept 2026); Global Payments (GPN) FY2026 adj. EPS guide $13.60\u201313.80, consensus target $92.85 (MarketBeat/americanbankingnews, Sept 2026); Adyen P/E ~23.7x (Finnhub). Analyst action: Robert W. Baird target cut, September 25, 2026 (MarketBeat). Dividend: $0.44 quarterly declared, paid September 25, 2026 (record September 11). Background: Worldpay $43B acquisition (2019), ~$17B impairment and $16.7B 2022 GAAP net loss (SEC 10-K), 55% sale to GTCR (January 2024).", s_small))
story.append(Spacer(1, 2*mm))
story.append(P("Items we could not fully verify and excluded from the valuation: Q1 2026 adjusted EPS and segment EBITDA splits beyond reported revenue; the precise post-deal share count (10-Q diluted share figure pending \u2014 we use ~515m vs FY2025's 519m); the exact net-debt figure after post-close paydowns (we use the Q2 2026 10-Q's $16.95B debt / $0.74B cash); FY2023\u20132024 adjusted revenue on a comparable basis (segment tags changed after the Worldpay deconsolidation \u2014 the quarterly 10-Q trend shown is directly from EDGAR). Q4 2025 revenue is estimated. Adjusted metrics are non-GAAP; see company reconciliations. This analysis was prepared September 26, 2026 for informational purposes only and is not investment advice; all forward-looking statements involve risk and uncertainty.", s_small))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=18*mm,
                        title="Fidelity National Information Services (FIS) \u2014 Equity Research Note", author="Investment Research")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("wrote", OUT)
