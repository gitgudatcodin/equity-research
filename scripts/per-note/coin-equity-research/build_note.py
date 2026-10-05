#!/usr/bin/env python3
"""Build the Coinbase (COIN) equity research note PDF."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, HRFlowable)
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart

OUT = "/home/hatch/workspace/your_files/coin-equity-research/coinbase-coin-equity-research-note.pdf"

NAVY = HexColor("#0F2A44"); ACCENT = HexColor("#6C3FB5"); GOLD = HexColor("#C9A227")
LGRAY = HexColor("#F2F4F7"); MGRAY = HexColor("#D9DEE5"); DGRAY = HexColor("#5A6472")
RED = HexColor("#B42318"); GREEN = HexColor("#0E7C3E"); BLUE = HexColor("#1D4ED8")
INK = HexColor("#1A2332")

s_title = ParagraphStyle("t", fontName="Helvetica-Bold", fontSize=26, leading=30, textColor=NAVY)
s_sub = ParagraphStyle("s", fontName="Helvetica", fontSize=11, leading=15, textColor=DGRAY)
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
def H1(txt): return P(txt, s_h1)
def H2(txt): return P(txt, s_h2)
def cell(txt, st=s_cell): return Paragraph(txt, st)

story = []
W, H = A4

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7); canvas.setFillColor(DGRAY)
    canvas.drawString(18*mm, 12*mm, "Coinbase Global, Inc. (NASDAQ: COIN)  \u2014  Equity Research Note  \u2014  September 2026")
    canvas.drawRightString(W - 18*mm, 12*mm, f"Page {doc.page}")
    canvas.setStrokeColor(MGRAY); canvas.setLineWidth(0.5)
    canvas.line(18*mm, 14.5*mm, W - 18*mm, 14.5*mm)
    canvas.restoreState()


# ============ COVER ============
story.append(Spacer(1, 22*mm))
story.append(P("COINBASE GLOBAL, INC. (NASDAQ: COIN)", ParagraphStyle("x", parent=s_sub, fontName="Helvetica-Bold", fontSize=13, textColor=ACCENT, spaceAfter=2)))
story.append(P("The Recovery Is Priced, Not the Trough<br/>Downgrading to REDUCE", s_title))
story.append(Spacer(1, 4*mm))
story.append(P("Equity Research Note  \u00b7  Financials \u2014 Capital Markets / Crypto  \u00b7  September 30, 2026", s_sub))
story.append(Spacer(1, 8*mm))

rating_data = [
    [cell("Recommendation", s_theadL), cell("12-Mo. Price Target", s_thead), cell("Current Price", s_thead), cell("Implied Return", s_thead), cell("Risk Rating", s_thead)],
    [Paragraph("<b><font color=\"#B42318\" size=\"13\">REDUCE</font></b>", s_cellC),
     Paragraph("<b><font size=\"12\">$155</font></b>", s_cellC),
     Paragraph("<b>$186.41</b><br/><font size=\"7\" color=\"#5A6472\">Sep 30, 2026</font>", s_cellC),
     Paragraph("<b>-16.8%</b>", s_cellC),
     Paragraph("<b>High</b><br/><font size=\"7\" color=\"#5A6472\">Beta ~3.3</font>", s_cellC)],
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
    ["Market cap", "~$53 bn (285M diluted)", "Enterprise value", "~$46.1 bn"],
    ["Net cash", "~$7.0 bn", "52-week range", "$139.11 \u2013 $402.16"],
    ["YTD / 1-yr return", "-17.6% / -46.2%", "ATH", "~$420 (Jul 2025); -56% since"],
    ["2025 revenue", "$7.18 bn", "2026E revenue", "~$5.1 bn (-29%)"],
    ["Q2'26 revenue / adj. EBITDA", "$1.22 bn / $208 mn", "Q2'26 GAAP net", "-$359 mn (-$1.36/sh)"],
    ["Next catalyst", "Q3'26 earnings, Oct 29", "Street consensus", "Hold; avg PT $222.94"],
]
sd = [[cell(a, s_cellB), cell(b), cell(c, s_cellB), cell(d)] for a, b, c, d in snap]
story.append(styled_table(
    [[cell("Snapshot", s_theadL), cell("", s_thead), cell("", s_thead), cell("", s_thead)]] + sd,
    [42*mm, 48*mm, 42*mm, 48*mm], fontsize=8.5))
story.append(Spacer(1, 6*mm))
story.append(P("This is a <b>price call, not a business call</b>. Coinbase is the highest-quality franchise in crypto "
    "financial services: the SEC lawsuit is gone, the GENIUS Act is law, subscription &amp; services is a record 48% of "
    "revenue, and the balance sheet holds ~$7 bn of net cash. The problem is arithmetic. At $186 the equity prices a "
    "V-shaped 2027 recovery (the Street models +50% revenue), ~4.9% perpetual growth on normalized free cash flow, and "
    "no further take-rate compression \u2014 while retail take rates have fallen from 1.91% to ~1.35% in three years, "
    "Robinhood and Schwab are attacking Coinbase's highest-margin retail flow, and Fed rate cuts threaten the $1.2 bn "
    "stablecoin annuity. Our probability-weighted fair value is ~$150; we set the $155 target between the DCF blend "
    "($149) and mid-cycle FCF power ($161 at 18x). We would turn constructive on weakness toward <b>$130\u2013$140</b>, "
    "where the risk/reward turns decisively positive into the 2028\u201329 cycle.", s_body))

# ============ INVESTMENT THESIS ============
story.append(H1("1. Investment Thesis"))
story.append(P("Coinbase has quietly become two companies: a <b>cyclical retail brokerage</b> whose economics are "
    "deteriorating (take-rate compression, fee cuts, well-funded attackers) and a <b>structural compounder</b> in "
    "subscription &amp; services (stablecoin revenue +48% in 2025, Circle economics locked through 2029, ETF custody "
    "for 8 of 11 spot bitcoin ETFs, Base the largest Ethereum L2). The market is valuing the whole at the "
    "compounder's multiple. We disagree:", s_body))
for b in [
    "<b>Trough earnings, peak multiple.</b> 2026 is a cyclical trough (revenue -29%, three straight quarterly GAAP losses, three straight quarterly misses), yet the stock trades at ~11x annualized revenue and ~36x our normalized FCF. Troughs are for buying \u2014 at trough <i>prices</i>. $186 is not one.",
    "<b>The recovery is fully priced.</b> Morgan Stanley's fresh initiation models 2027 revenue +50% and EBITDA more than doubling; the $223 consensus target needs it. Our cycle work (2021 peak $7.84 bn \u2192 2022 trough $3.19 bn \u2192 2025 peak $7.18 bn) suggests a slower rebuild: take rates are structurally lower each cycle, and each revenue peak buys fewer dollars of earnings.",
    "<b>The $1.2 bn stablecoin annuity is rate-sensitive.</b> Stablecoin revenue ($292 mn in Q2 on $20 bn of USDC balances) is reserve interest \u2014 it falls when the Fed cuts, and the GENIUS Act's yield ban plus a stalled CLARITY Act cap Coinbase's ability to differentiate on USDC rewards.",
    "<b>Competition is converging from both sides.</b> Robinhood did $156 mn of prediction-market revenue in Q2 (+10x YoY, larger than its crypto <i>and</i> equity trading revenue) and tokenized 2,000+ stocks; Schwab now sells spot BTC/ETH at 75 bps to 35 mn accounts. Coinbase cut Advanced Trade fees on Sept 16 \u2014 the right volume defense, and a near-term yield sacrifice.",
    "<b>Shareholders pay ~$1 bn a year in SBC.</b> ~$240 mn a quarter of stock comp with no buyback in 2026 is a persistent 2%-a-year tax on owners, and Q3'25 diluted share count (292 mn) already sits 11% above the Q2'26 basic count used in headline market-cap math.",
]:
    story.append(B(b))
story.append(P("What would change our mind: a washout toward <b>$130\u2013$140</b> (our DCF-blend zone), where even the "
    "bear case ($72) offers a margin of safety and the 2028\u201329 cycle provides 2\u20133x upside optionality; or "
    "evidence that take rates have stabilized while S&amp;S compounds above 20%. Until then, this is a superb business "
    "at the wrong price.", s_body))

# ============ BUSINESS ============
story.append(H1("2. What the Company Does"))
story.append(P("Coinbase (founded 2012; listed April 2021; S&amp;P 500 member since May 2025) is a multi-product crypto "
    "financial-services platform, not merely an exchange. Twelve products each generate $100 mn+ of annualized revenue "
    "(Q1'26 shareholder letter):", s_body))
for b in [
    "<b>Retail trading</b> \u2014 the Coinbase app (simple buy/sell) and <b>Coinbase Advanced Trade</b> (order-book interface, successor to Coinbase Pro). Still the profit engine and still the most cyclical line.",
    "<b>Coinbase One</b> \u2014 subscription ($4.99\u2013$299.99/mo) with fee waivers and priority support; &gt;1 mn paid subscribers, at an all-time high in Q2'26.",
    "<b>Coinbase Prime (institutional)</b> \u2014 custody via its NY limited-purpose trust company, execution, financing, and staking. Custodian for <b>8 of 11 US spot bitcoin ETFs</b> (incl. BlackRock's IBIT) and 7 of 9 ether ETFs; &gt;80% of US bitcoin-ETF assets sit with Coinbase Custody.",
    "<b>Derivatives</b> \u2014 CFTC-registered futures (Coinbase Financial Markets), the International Exchange, and <b>Deribit</b>, the world's largest crypto options venue, acquired for ~$2.9 bn and closed August 2025 (~$185 bn July volume, 85%+ options share).",
    "<b>Developer platform &amp; Base</b> \u2014 the Coinbase Developer Platform and <b>Base</b>, its Ethereum L2 (launched 2023), now the largest L2 by TVL ($6.2 bn record, Sept 2026; ~4x the next L2). Coinbase keeps ~80\u201395% of sequencer fees (~$92 mn in 2024 at ~92% margin).",
    "<b>2026 launches (\u201ceverything exchange\u201d)</b> \u2014 prediction markets (revenue +106% QoQ in Q2, crossing $100 mn annualized) and <b>tokenized US equities</b> on Base (launched Aug 2026 for non-US users; 1:1 real-share backing via Alpaca/ADGM with dividends and voting passed through; &gt;$1 bn volume by late September).",
]:
    story.append(B(b))
story.append(P("The strategic arc is clear: monetize trust and regulatory licenses across every crypto-adjacent "
    "transaction type, while the subscription &amp; services book (48% of Q2'26 revenue, a record) dampens the historic "
    "boom-bust. The arc is working \u2014 the 2026 trough ($5.1 bn revenue) is 60% deeper in <i>level</i> terms than the "
    "2022 trough ($3.19 bn) was shallow in <i>relative</i> terms (71% of prior peak vs 41% last cycle). But "
    "diversification has not repealed cyclicality: transaction revenue still fell 31% YoY on the consumer side in Q2.", s_body))

# ============ PRODUCTS & PRICING ============
story.append(H1("3. Product & Pricing Evaluation"))
story.append(P("Coinbase monetizes across five distinct pricing models. Evaluated product by product:", s_body))
story.append(H2("Retail brokerage: simple app vs Advanced Trade"))
story.append(P("The simple app charges ~0.5% spread plus $0.99\u2013$2.99 flat fees \u2014 typically 1\u20131.5%+ all-in, "
    "among the highest in US crypto retail. <b>Advanced Trade</b> is tiered maker/taker; after the <b>Sept 16, 2026 fee "
    "cut</b>, US entry is 0.50% maker / 0.90% taker (tiers now start at $10k combined spot+derivatives volume, down from "
    "$25k), flooring at 0.00%/0.05% above $250 mn/month. The cut is strategically correct \u2014 it defends volume "
    "share (a record 10.3% of global crypto trading volume in Q2, three quarterly records running) \u2014 but it "
    "trades near-term yield for flow, and the blended retail take rate has still compressed from 1.91% (2023) to "
    "~1.35% (2026E). Versus Kraken Pro (0.25%/0.40%), Gemini (0.20%/0.40%) and Binance (0.10%/0.10%), Coinbase charges "
    "a 2\u20134x premium that only trust, UX and on-ramp convenience sustain.", s_body))
story.append(H2("Coinbase One: the subscription hedge"))
story.append(P("Basic $4.99/mo (zero trading fees to $500/mo volume), Preferred $29.99/mo (zero fees to $10k/mo + 25% "
    "Advanced spot-fee rebate), Premium $299.99/mo (uncapped). Spreads still apply \u2014 the spread is the quiet "
    "margin. With &gt;1 mn paid subscribers at an all-time high, One converts volatile transaction revenue into "
    "recurring revenue and raises switching costs. This is the single best product response to take-rate compression, "
    "and it is working.", s_body))
story.append(H2("Prime & custody: the institutional annuity"))
story.append(P("Public schedule: 50 bps annualized custody fee ($500k minimum; large mandates negotiated), plus "
    "implementation fees. As custodian for 8 of 11 spot bitcoin ETFs and 7 of 9 ether ETFs \u2014 over 80% of US "
    "bitcoin-ETF assets \u2014 custody is a genuine annuity with deep issuer integration. The wrinkle: concentration "
    "is pushing issuers toward multi-custody (BlackRock added Anchorage Digital as IBIT co-custodian), and SAB 121's "
    "rescission lets banks compete. Custody pricing power is real but no longer unchallenged.", s_body))
story.append(H2("USDC & staking: the two rent streams"))
story.append(P("<b>Stablecoin revenue</b> ($292 mn in Q2, +48% YoY in 2025 to $1.35 bn) is Coinbase's largest recurring "
    "line: 100% of reserve income on USDC held on-platform plus an off-platform share, with the Circle revenue-share "
    "renewed on existing terms through 2029 and $20 bn of average USDC balances on platform (an all-time high). "
    "Coinbase held ~30% of USDC circulation. The risk is macro, not competitive: reserve income falls with Fed cuts, "
    "and JPMorgan flagged a Hyperliquid deal routing 90% of reserve yield on ~$6 bn USDC back to Hyperliquid \u2014 a "
    "template other venues may copy. <b>Staking</b> (blockchain rewards $677 mn in 2025) runs at ~35% commission for "
    "most assets \u2014 a high, defensible take for a trusted validator set, modestly discounted for One tiers.", s_body))
story.append(H2("New bets: Base, Deribit, prediction markets, tokenized stocks"))
story.append(P("<b>Base</b> keeps ~80\u201395% of sequencer fees (~$92 mn in 2024 at ~92% margin; TVL at a $6.2 bn record) "
    "but is not broken out in filings \u2014 treat third-party 2026 estimates as approximate, and note the "
    "concentration (90% of Base stablecoins are USDC; ~70% of TVL sits in Morpho Blue lending). <b>Deribit</b> "
    "($2.9 bn, closed Aug 2025) bought the dominant crypto options franchise (85%+ share, $30 bn+ open interest, 80% "
    "institutional flow); institutional transaction revenue grew 65% YoY in Q2 on its back. <b>Prediction markets</b> "
    "crossed $100 mn annualized (+106% QoQ) \u2014 real, but Robinhood did $156 mn in the same quarter (+10x YoY). "
    "<b>Tokenized stocks</b> passed $1 bn volume by late September on genuine 1:1 backing, and the SEC's Sept 17 "
    "five-year Innovation Exemption (+10.7% on the stock) is a real regulatory breakthrough \u2014 though it is "
    "temporary, conditional, and currently non-US only. Verdict: the new bets are credible and diversifying, but none "
    "yet offsets a $600 mn quarterly decline in consumer transaction revenue.", s_body))

# ============ FINANCIALS ============
story.append(H1("4. Financial Situation"))
story.append(P("Coinbase is a textbook cyclical: violent operating leverage on the way up, violent deleverage on the "
    "way down \u2014 now cushioned by a subscription book that did not exist at this scale in the last cycle.", s_body))
fin = [
    ["$ mn", "2022", "2023", "2024", "2025", "H1'26"],
    ["Total revenue", "3,194", "3,108", "6,564", "7,181", "2,633"],
    ["Transaction revenue", "2,753*", "1,483*", "3,986", "4,055", "1,355"],
    ["Subscription & services", "793*", "1,362*", "2,307", "2,828", "1,139"],
    ["S&S share of net revenue", "~22%", "~44%", "~37%", "~41%", "~48%"],
    ["Operating income", "(1,947)", "(54)", "2,235", "1,456", "(16)"],
    ["Net income", "(2,625)", "95", "2,579", "1,260", "(754)"],
    ["Adj. EBITDA", "(371)*", "964*", "3,287*", "3,151*", "511"],
    ["Operating cash flow", "(1,585)", "673", "3,104", "2,426", "~500*"],
]
fd = [[cell(r[0], s_cellB)] + [cell(c, s_cellR) for c in r[1:]] for r in fin]
story.append(styled_table(
    [[cell("Revenue & profitability ($ mn)", s_theadL), cell("", s_thead), cell("", s_thead), cell("", s_thead), cell("", s_thead), cell("", s_thead)]] + fd,
    [52*mm, 26*mm, 26*mm, 26*mm, 26*mm, 26*mm], fontsize=8))
story.append(P("<font size=\"7.5\" color=\"#5A6472\">*Approximate/derived. Q2'25 net income of $1,429 mn included large non-operating crypto-asset gains "
    "(adj. net income was only $33 mn) \u2014 GAAP net income is polluted by fair-value marks on crypto holdings; adjusted EBITDA and operating cash flow "
    "are the cleaner lenses. Sources: 10-K/10-Q filings via EDGAR; company 8-K decks.</font>", s_small))
story.append(P("<b>Balance sheet (June 30, 2026):</b> $13.15 bn cash, cash equivalents and restricted cash against "
    "$5.9 bn long-term debt \u2014 ~$7 bn net cash after a conservative haircut for restricted balances. The $1.3 bn "
    "of 0.50% converts maturing June 2026 were fully repaid; $3.0 bn of new converts were issued in Aug 2025. "
    "No buybacks or dividends in 2026. <b>Cash conversion</b> is excellent at the top of the cycle (2024 OCF $3.1 bn on "
    "$6.6 bn revenue; capex is negligible) and merely okay at the trough (Q2'26 OCF $197 mn). <b>SBC</b> runs "
    "~$240 mn/quarter (~$1 bn annualized) \u2014 the single largest recurring shareholder cost, with headcount cut 14% "
    "(~700 people) in May 2026 to protect the downside ($600 mn of annualized cost removed; FY26E adjusted expenses "
    "narrowed to $4.2\u20134.45 bn).", s_body))
story.append(P("<b>What the numbers say:</b> (1) the subscription pivot is real \u2014 S&amp;S at a record 48% of Q2'26 "
    "net revenue vs ~22% in 2022; (2) the trough is shallower than 2022 in relative terms (71% of prior peak vs 41%), "
    "evidence the model is genuinely less cyclical; (3) but earnings quality is still poor at the bottom \u2014 three "
    "straight GAAP losses and three straight quarterly misses, with the GAAP/adjusted gap driven by SBC, crypto "
    "revaluations (-$210 mn in Q2) and restructuring.", s_body))

# ============ REVENUE CYCLE CHART ============
story.append(H2("The cycle in one chart: annual total revenue ($ bn)"))
d = Drawing(460, 170)
bc = VerticalBarChart()
bc.x = 50; bc.y = 30; bc.height = 115; bc.width = 380
bc.data = [[7.84, 3.19, 3.11, 6.56, 7.18, 5.10]]
bc.categoryAxis.categoryNames = ["2021", "2022", "2023", "2024", "2025", "2026E"]
bc.categoryAxis.labels.fontSize = 8
bc.valueAxis.valueMin = 0; bc.valueAxis.valueMax = 9
bc.valueAxis.labels.fontSize = 8
bc.bars[0].fillColor = NAVY
bc.barLabels.fontSize = 7.5; bc.barLabelFormat = "%.2f"
d.add(bc)
story.append(d)
story.append(P("<font size=\"7.5\" color=\"#5A6472\">2021 actual ~$7.84 bn; 2026E ~$5.1 bn (H1 $2.63 bn + Q3 guide run-rate). Note each peak arrives on lower take rates than the last.</font>", s_small))

# ============ GROWTH / MOAT / COMPETITION ============
story.append(H1("5. Growth Outlook"))
for b in [
    "<b>Subscription compounding.</b> S&amp;S grew ~23% in 2025 (stablecoin +48%) against a -29% total-revenue 2026E. With the Circle deal locked through 2029, GENIUS Act legitimacy expanding USDC use cases, and One subscribers at records, a 12\u201315% S&amp;S CAGR through the cycle is credible \u2014 the structural bull case.",
    "<b>Derivatives &amp; international.</b> Deribit makes Coinbase the institutional options venue (85%+ share) and perps migrated there in Sept 2026; derivatives launched in Canada with US perps on the roadmap. Institutional transaction revenue +65% YoY in Q2 is the early proof.",
    "<b>Tokenized equities &amp; prediction markets.</b> The SEC's five-year Innovation Exemption (Sept 17, 2026) is the first federal blessing for tokenized NMS stocks; Coinbase self-certified single-stock perpetual futures on 50+ names the next day. Prediction markets at $100 mn annualized and doubling quarterly. Both are genuine options \u2014 neither is yet material.",
    "<b>Base as infrastructure.</b> Largest Ethereum L2 by TVL (4x the next), ~92%-margin sequencer fees, and the settlement layer for tokenized stocks. Not broken out in filings; underwrite cautiously.",
    "<b>The 2028\u201329 cycle.</b> The April-2028 halving sets up the next volume peak (~2029). Coinbase enters it with a far larger recurring base than it had for the 2024\u201325 peak \u2014 the reason our bull case ($252) is more than 3x the bear case ($72).",
]:
    story.append(B(b))

story.append(H1("6. Moat"))
for b in [
    "<b>Regulatory licenses \u2014 hardest to replicate:</b> NY limited-purpose trust (qualified custody), CFTC-registered FCM, MiCA authorization across the EEA, 100+ country footprint. Every competitor must re-earn these one jurisdiction at a time.",
    "<b>ETF custody network effects:</b> 8 of 11 BTC ETFs and 7 of 9 ETH ETFs, &gt;80% of US bitcoin-ETF assets. Deep operational integration with the world's largest asset managers \u2014 though concentration is now pushing issuers toward multi-custody.",
    "<b>Brand, trust, public-company scrutiny:</b> first major US-listed crypto exchange, audited financials, S&amp;P 500 membership. In an industry still defined by offshore blowups, this is a durable retail acquisition advantage.",
    "<b>Developer ecosystem:</b> Base + the Coinbase Developer Platform; 12 products at $100 mn+ revenue; real switching costs for Prime custody clients.",
    "<b>Moat limits (honestly):</b> retail take rates compressing 1.91% \u2192 ~1.35%; Schwab/Robinhood erode the trusted-on-ramp advantage; the GENIUS yield ban constrains USDC-rewards differentiation; and improving multi-agency regulation <i>lowers</i> the barrier that historically protected Coinbase.",
]:
    story.append(B(b))

story.append(H1("7. Competition"))
story.append(P("Coinbase charges a trust premium \u2014 2\u20134x the entry take of offshore and discount venues \u2014 into a market where two well-funded attackers are converging on its highest-margin flow:", s_body))
for b in [
    "<b>Robinhood \u2014 the closest threat.</b> Q2'26 prediction-market revenue of $156 mn (+10x YoY) exceeded <i>both</i> its crypto and equity trading revenue; 4.7 bn prediction contracts in August (+15x YoY); 2,000+ tokenized stocks across 120+ countries within a month of launch; its own chain doing $15.9 mn/week. Robinhood funds prediction flow with <i>fresh</i> cash; Coinbase risks cannibalizing its own crypto trading. Mizuho judged HOOD better placed for prediction upside.",
    "<b>Traditional brokers.</b> Schwab rolled out spot BTC/ETH at 75 bps to ~35 mn accounts (clients already hold ~20% of US spot crypto ETPs); Fidelity charges 1.00% and self-custodies FBTC. The \u201ctradfi on-ramp\u201d advantage is no longer Coinbase's alone.",
    "<b>Offshore &amp; specialists.</b> Binance (0.10%/0.10%, deepest liquidity) dominates global volume; Kraken (SEC case dismissed Mar 2025) holds the compliant-US middle ground; Crypto.com undercuts on price; Hyperliquid is winning perps and now bidding for USDC distribution economics.",
]:
    story.append(B(b))
story.append(P("Coinbase's answer \u2014 the Sept 2026 Advanced Trade fee cut, One subscriptions, and the everything-exchange "
    "build-out \u2014 is directionally right. But the take-rate trend (1.91% \u2192 1.55% \u2192 1.39% \u2192 ~1.35%) says "
    "pricing power, not just price, is eroding.", s_body))

# ============ VALUATION ============
story.append(H1("8. Valuation \u2014 Four Lenses"))
story.append(P("COIN cannot be valued on current earnings \u2014 2026 is a trough. We triangulate across a cycle-aware "
    "scenario DCF (primary), mid-cycle FCF power, a sum-of-the-parts, and a reverse-DCF asking what the price implies.", s_body))
story.append(H2("Lens 1 \u2014 Scenario DCF (10-yr, FCF-based; 25/50/25 weights)"))
story.append(P("Revenue paths follow the ~4-year crypto cycle (peak Oct-2025 \u2192 trough 2026 \u2192 recovery 2027\u201328 "
    "\u2192 next peak ~2029 post Apr-2028 halving \u2192 normalization 2030). FCF margins trough at 8\u201316% and peak at "
    "37\u201342%; WACC 11% base (10.5% bull / 11.5% bear) against a net-cash balance sheet; terminal growth 3%.", s_body))
val = [
    ["Scenario", "2026E rev", "2029 peak rev", "PV of FCF", "Terminal value", "Fair value / sh"],
    ["Bear: winter extends", "$5.0 bn", "$7.2 bn", "$6.0 bn", "$7.6 bn", "$72.42"],
    ["Base: cycle repeats", "$5.1 bn", "$9.6 bn", "$13.8 bn", "$18.0 bn", "$136.07"],
    ["Bull: everything-exchange", "$5.3 bn", "$13.0 bn", "$23.5 bn", "$41.4 bn", "$252.43"],
    ["<b>Blended (25/50/25)</b>", "\u2014", "\u2014", "\u2014", "\u2014", "<b>$149.25</b>"],
]
vd = [[cell(r[0], s_cellB if "Blended" not in r[0] else s_cellB)] + [cell(c, s_cellR) for c in r[1:]] for r in val]
story.append(styled_table(
    [[cell("Scenario DCF ($ mn except per-share)", s_theadL)] + [cell("", s_thead)]*5] + vd,
    [52*mm, 26*mm, 26*mm, 26*mm, 26*mm, 28*mm], fontsize=8))
d2 = Drawing(460, 165)
bc2 = VerticalBarChart()
bc2.x = 60; bc2.y = 30; bc2.height = 110; bc2.width = 360
bc2.data = [[72.42, 136.07, 252.43, 149.25]]
bc2.categoryAxis.categoryNames = ["Bear $72", "Base $136", "Bull $252", "Blended $149"]
bc2.categoryAxis.labels.fontSize = 8
bc2.valueAxis.valueMin = 0; bc2.valueAxis.valueMax = 280
bc2.valueAxis.labels.fontSize = 8
bc2.bars[0].fillColor = ACCENT
bc2.barLabels.fontSize = 7.5; bc2.barLabelFormat = "%.0f"
d2.add(bc2)
story.append(d2)
story.append(P("<font size=\"7.5\" color=\"#5A6472\">Current price $186.41 sits between the base and bull cases \u2014 i.e., the market is paying for a better-than-base cycle.</font>", s_small))
story.append(H2("Lens 2 \u2014 Mid-cycle FCF power"))
story.append(P("Normalize across the cycle: $7.2 bn mid-cycle revenue (between 2024's $6.56 bn and 2025's $7.18 bn, "
    "below our 2029 peak) at a 30% normalized FCF margin = <b>$2.16 bn of mid-cycle FCF</b> (vs $3.10 bn actual in "
    "2024, so this is not heroic). Capitalize it:", s_body))
mc = [
    ["Multiple on mid-cycle FCF", "16x", "18x", "20x", "22x"],
    ["Fair value / sh (incl. $7 bn net cash)", "$145.82", "$160.98", "$176.14", "$191.30"],
]
mc_rows = [[cell(r[0], s_theadL if i == 0 else s_cellB)] +
             [cell(c, s_thead if i == 0 else s_cellC) for c in r[1:]]
             for i, r in enumerate(mc)]
story.append(styled_table(mc_rows,
    [64*mm, 29*mm, 29*mm, 29*mm, 29*mm], fontsize=8.5))
story.append(P("18x \u2192 <b>$161</b> is our preferred mid-cycle read: it compensates cyclicality while crediting the "
    "structural growth in the recurring book.", s_body))
story.append(H2("Lens 3 \u2014 Sum of the parts"))
story.append(P("Value the two companies separately: S&amp;S (~$2.5 bn run-rate, sticky, Circle-locked) at 8\u201310x revenue; "
    "transaction (~$2.6 bn run-rate, cyclical) at 3.5\u20134.5x revenue; add $7 bn net cash:", s_body))
sp = [
    ["SOTP", "Conservative (8x / 3.5x)", "Mid (9x / 4x)", "Stretched (10x / 4.5x)"],
    ["Fair value / sh", "$126.67", "$140.00", "$153.33"],
]
sp_rows = [[cell(r[0], s_theadL if i == 0 else s_cellB)] +
             [cell(c, s_thead if i == 0 else s_cellC) for c in r[1:]]
             for i, r in enumerate(sp)]
story.append(styled_table(sp_rows,
    [52*mm, 42*mm, 42*mm, 44*mm], fontsize=8.5))
story.append(H2("Lens 4 \u2014 Reverse DCF: what does $186 imply?"))
story.append(P("Growing our $2.16 bn normalized FCF at 10% for five years, then discounting at 11%, the current price "
    "implies <b>~4.9% perpetual growth</b> thereafter. That is a demanding bar: it asks the <i>normalized</i> business "
    "to compound near nominal GDP+ forever, with no further take-rate decay \u2014 the opposite of the last three "
    "years' evidence (1.91% \u2192 ~1.35%). The price is not pricing the trough; it is pricing the recovery <i>and</i> "
    "perpetual structural growth on top.", s_body))
story.append(H2("Blended fair value &amp; target"))
story.append(P("The four lenses cluster at <b>$140\u2013$161</b> (DCF blend $149; SOTP mid $140; mid-cycle 18x $161). "
    "We set the 12-month target at <b>$155</b> \u2014 between the DCF blend and mid-cycle power, the driver being "
    "trough-cycle earnings power plus structural S&amp;S compounding. WACC sensitivity on the base case: 10% \u2192 $154; "
    "12% \u2192 $122 \u2014 even the friendly end of the range sits below today's price. Implied 12-month return: "
    "<b>-16.8%</b>.", s_body))

# ============ RISKS / CATALYSTS / STREET ============
story.append(H1("9. Risks"))
for b in [
    "<b>Cycle risk (the big one).</b> Revenue and earnings still swing violently with crypto prices and volumes; beta ~3.3. A deeper or longer winter breaks the bear case ($72) rather than the base case.",
    "<b>Rate sensitivity.</b> ~$1.2 bn of annualized stablecoin revenue is reserve interest; Fed cuts flow straight to the bottom line. The GENIUS yield ban limits pricing offsets.",
    "<b>Take-rate compression.</b> Three years of decline (1.91% \u2192 ~1.35%); the Sept 2026 fee cut defends share at the cost of yield.",
    "<b>Concentration.</b> &gt;80% of US bitcoin-ETF assets in Coinbase Custody \u2014 an operational or security incident would be systemic; issuers are already diversifying.",
    "<b>Competition.</b> Robinhood (prediction markets, tokenized stocks, own chain), Schwab/Fidelity (tradfi on-ramps), Binance/Kraken (price), Hyperliquid (perps + USDC economics).",
    "<b>Regulatory.</b> CLARITY Act stalled \u2014 market-structure clarity still pending; the tokenized-stock exemption is five-year and conditional.",
    "<b>Execution &amp; dilution.</b> Heavy M&amp;A (Deribit, Echo), 14% workforce cut, \u201ceverything exchange\u201d sprawl; ~$1 bn/yr of SBC with no buyback.",
]:
    story.append(B(b))
story.append(H1("10. Catalysts &amp; What to Watch"))
for b in [
    "<b>Q3'26 earnings, Oct 29</b> \u2014 the near-term proving ground after three straight misses; watch S&amp;S vs the $500\u2013580 mn guide and any take-rate stabilization.",
    "<b>CLARITY Act Senate path</b> \u2014 passage would extend the regulatory tailwind; continued stall keeps the overhang.",
    "<b>Fed policy</b> \u2014 cuts are the direct headwind to stablecoin revenue; the market has not priced this linkage, in our view.",
    "<b>Prediction-market &amp; tokenized-stock scale</b> \u2014 $100 mn annualized doubling quarterly is the line to watch for the \u201ceverything exchange\u201d thesis.",
    "<b>Crypto cycle turn</b> \u2014 any sustained BTC recovery re-levers the whole model; our $130\u2013140 buy zone is calibrated to arrive <i>before</i> that turn is obvious.",
]:
    story.append(B(b))
story.append(H1("11. Street View"))
story.append(P("Consensus is <b>Hold</b> with an average 12-month target of <b>$222.94</b> (20 Buy / 12 Hold / 3 Sell; "
    "range $95 Barclays Underweight to $330 Bernstein Outperform; Morningstar ~$150). Recent actions skew constructive: "
    "KBW initiated Outperform $237 (Sep 28), Baird raised $130 \u2192 $205 Neutral, Morgan Stanley initiated Equal Weight "
    "$250 modeling 2026 revenue -18% then 2027 +50% with EBITDA more than doubling, Goldman raised to $219 Buy. "
    "We sit <b>below consensus on price but agree on the business quality</b>: the Street's targets require the "
    "V-shaped 2027 our cycle work does not support at current take rates. The most useful Street datapoint is "
    "Morgan Stanley's \u2014 it makes the priced-in recovery explicit, and we are fading it.", s_body))

# ============ RECOMMENDATION ============
story.append(H1("12. Final Recommendation: REDUCE"))
story.append(P("Coinbase is the best house in a cyclical neighborhood, and the neighborhood is in a downturn. The "
    "franchise deserves its premium \u2014 record subscription mix, the Circle annuity locked through 2029, ETF custody "
    "dominance, a net-cash balance sheet, and genuine regulatory tailwinds. But $186.41 pays for the recovery before "
    "it happens: our probability-weighted fair value is ~$150, the price implies ~4.9% perpetual growth on normalized "
    "cash flow, and every lens we ran lands 15\u201325% below the quote.", s_body))
story.append(P("<b>We downgrade to REDUCE with a $155 12-month target (-16.8%).</b> This is a price call, not a business "
    "call: we would turn constructive on weakness toward <b>$130\u2013140</b>, where the DCF blend offers a margin of "
    "safety and the 2028\u201329 cycle provides multi-year upside optionality. For long-term holders, the instruction "
    "is patience, not panic \u2014 trim into strength, reload the trough. High risk: beta ~3.3, three straight "
    "quarterly misses, and earnings that still answer to the price of bitcoin.", s_body))
story.append(Spacer(1, 4*mm))
story.append(HRFlowable(width="100%", thickness=0.5, color=MGRAY, spaceAfter=4))
story.append(P("Research framing only \u2014 not investment advice. Figures from company filings (EDGAR 10-K/10-Q), "
    "company 8-K decks and earnings calls, and market data as of September 30, 2026. Valuation reflects the author's "
    "cycle assumptions and is sensitive to crypto prices, take rates, interest rates and regulation; actual results may "
    "differ materially. The author holds no position in COIN.", s_small))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=18*mm,
                        title="Coinbase (COIN) Equity Research Note", author="Research Desk")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("wrote", OUT)
