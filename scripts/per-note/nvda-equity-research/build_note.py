#!/usr/bin/env python3
"""Build the NVDA (NVIDIA) equity research note PDF - standalone analyst report, Oct 4, 2026.
Model: ~/workspace/your_files/nvda-equity-research/model.json
Research analysis, not investment advice.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, HRFlowable)
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import VerticalBarChart

OUT = "/home/hatch/workspace/your_files/nvda-equity-research/nvda-equity-research-note.pdf"

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
    canvas.drawString(18*mm, 12*mm, "NVDA (NASDAQ: NVDA)  \u2014  Equity Research Note  \u2014  October 2026")
    canvas.drawRightString(W - 18*mm, 12*mm, f"Page {doc.page}")
    canvas.setStrokeColor(MGRAY); canvas.setLineWidth(0.5)
    canvas.line(18*mm, 14.5*mm, W - 18*mm, 14.5*mm)
    canvas.restoreState()

# ============ COVER ============
story.append(Spacer(1, 24*mm))
story.append(P("NVDA (NASDAQ: NVDA)", ParagraphStyle("x", parent=s_sub, fontName="Helvetica-Bold", fontSize=13, textColor=ACCENT, spaceAfter=2)))
story.append(P("The AI Factory:<br/>Supply-Constrained at $5.7 Trillion", s_title))
story.append(Spacer(1, 4*mm))
story.append(P("Equity Research Note  \u00b7  Semiconductors \u2014 AI Compute Platforms  \u00b7  October 4, 2026", s_sub))
story.append(Spacer(1, 8*mm))

rating_data = [
    [cell("Recommendation", s_theadL), cell("12-Mo. Price Target", s_thead), cell("Current Price", s_thead), cell("Implied Upside", s_thead), cell("Risk Rating", s_thead)],
    [Paragraph("<b><font color=\"#1D4ED8\" size=\"13\">HOLD</font></b>", s_cellC),
     Paragraph("<b><font size=\"12\">$223</font></b>", s_cellC),
     Paragraph("<b>$233.95</b><br/><font size=\"7\" color=\"#5A6472\">Oct 2, 2026</font>", s_cellC),
     Paragraph("<b>-4.5%</b>", s_cellC),
     Paragraph("<b>Med-High</b><br/><font size=\"7\" color=\"#5A6472\">Cycle concentration</font>", s_cellC)],
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
    ["Market cap", "~$5.7 tn", "Shares out. (dil.)", "~24.3 bn"],
    ["Net cash (liquid)", "~$18.2 bn", "52-week range", "$164.27 \u2013 $236.54"],
    ["Q2 FY27 rev / DC rev", "$96.2 bn / $89.0 bn (+117%)", "Gross / net margin", "75.0% / 62.0%"],
    ["Q3 FY27 guide", "$108 bn (\u00b12%)", "FY28 guide (first ever)", "+~70% revenue YoY"],
    ["Buyback authorization", "$235 bn thru FY28", "Street consensus target", "~$323 (48 Buy / 4 Hold)"],
    ["Next catalyst", "Q3 FY27 (Nov)", "Rubin status", "Full production since Mar 2026"],
]
sd = [[cell(r[0], s_cellB), cell(r[1], s_cell), cell(r[2], s_cellB), cell(r[3], s_cell)] for r in snap]
story.append(styled_table([[cell("Snapshot", s_theadL), cell("", s_thead), cell("", s_thead), cell("", s_thead)]] + sd,
               [38*mm, 42*mm, 42*mm, 48*mm], header_rows=1))
story.append(Spacer(1, 8*mm))
story.append(P("This note is independent research-style analysis for informational purposes only and is not investment advice. "
               "Financial figures from company releases and SEC filings; market data as of October 2, 2026. "
               "Projections and the price target are the author's estimates.", s_small))
story.append(PageBreak())

# ============ 1. INVESTMENT THESIS ============
story.append(P("1 &nbsp; Investment Thesis", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Our view of the business: NVIDIA is the one company in this cycle whose demand visibility is contractual "
               "rather than aspirational. In August the company issued its first-ever full-year revenue guide \u2014 "
               "fiscal 2028 (ending January 2028) up <b>~70% year over year</b>, to roughly $670B \u2014 and CFO Colette "
               "Kress was explicit that the number is <b>supply-constrained</b>: 'Real demand is much higher than 70%. "
               "Supply is what determines the 70% we can confidently deliver.' When a company guiding to ~$670B tells "
               "you demand is running hotter than the guide, the near term is not a forecast to be haircut; it is a "
               "capacity allocation problem. That is why our 2027\u201328 assumptions track guidance rather than "
               "sitting below it.", s_body))
story.append(P("But this note is not a victory lap, and the call is not about the next four quarters. The entire call "
               "is <b>duration and fade</b>. Our base case gives the supercycle through <b>2030</b> \u2014 the Rubin and "
               "Rubin Ultra waves, Vera Rubin already in full production and on pace for the fastest ramp in company "
               "history, sovereign AI as a demand floor beneath the hyperscalers \u2014 then fades growth into the "
               "single digits with FCF margins normalizing to a through-cycle 48%. The market at $233.95 is paying for "
               "something close to that: our scenarios are <b>$56 / $224 / $391</b>, weighted to a <b>$223 target, "
               "\u20134.5%</b> against the quote. The business is exceptional, the cycle is real, and the price is "
               "roughly fair. <b>HOLD.</b>", s_body))
story.append(P("The bear case deserves emphasis because it is the scenario the price ignores. It is the honest version "
               "of 2029\u201330: the 2026\u201328 pre-build \u2014 top-5 hyperscaler capex near $800B in 2026 and ~$1.3T "
               "in 2027 \u2014 overshoots, book-to-bill drops below 1.0, the inventory pre-build (raw materials up 71% "
               "quarter over quarter) becomes a glut, revenue falls ~17% in FY29, and FCF margins compress 900bp vs "
               "base as price cuts clear the channel. Bear $56 \u2014 far below the price, as a bear must be. Skepticism "
               "belongs in duration and fade, not in the next four quarters.", s_body))

story.append(P("Why the demand is contracted, not extrapolated", s_h2))
for b in [
    "<b>A 70% FY28 guide that is explicitly supply-capped.</b> August 2026: Q2 FY27 revenue $96.22B (+106% YoY), data center $89.0B (+117%), GAAP gross margin 75.0%; Q3 guided to $108B (\u00b12%) at 74% gross margin \u2014 and the first-ever full-year guide of ~70% FY28 growth, with management saying customer forecasts point to demand roughly doubling. Wall Street had been at ~45%.",
    "<b>$279B of supply commitments and rising prices.</b> TrendForce reports NVIDIA's supply commitments have soared to ~$279B as memory costs surge; the company has notified its largest customers of price increases exceeding 15% on AI server systems (including Vera Rubin and Grace Blackwell configurations) hitting systems shipped in early 2027. Allocation, not discounting.",
    "<b>Memory and foundry are hard constraints through 2028.</b> HBM is reported sold out for all of 2026, with SK Hynix warning the shortfall could stretch toward the end of the decade; Blackwell PRO lead times run 3\u20137 months; TSMC N3 capacity is near full utilization through at least 2027. NVIDIA itself cautions that supply constraints persist through fiscal 2028.",
    "<b>Named multi-year deployments.</b> Amazon has committed to deploying 2 million NVIDIA GPUs through 2029; Anthropic locked in a 2.5GW commitment; Rubin NVL72 racks are already delivering to Google Cloud, Microsoft, and Oracle, with systems up at CoreWeave and Nebius.",
    "<b>Sovereign AI is a second demand curve.</b> Saudi Arabia's HUMAIN ($10B partnership, part of a $100B AI ecosystem), the UK's \u00a318B compute program, South Korea's 260,000-Blackwell build-out \u2014 nations treating compute as strategic infrastructure put a floor under demand that is independent of Silicon Valley capex cycles.",
    "<b>$40B per gigawatt.</b> In the Rubin generation the revenue opportunity per gigawatt of data-center capacity expands to ~$40B, because the sale is the full AI factory \u2014 GPU, CPU, networking, inference silicon \u2014 not the chip. Networking has grown from under 9% to ~18% of data center revenue in a year.",
]:
    story.append(B(b))
story.append(P("Why we still won't pay up", s_h2))
for b in [
    "<b>The price already assumes the supercycle runs through 2030.</b> Our base case \u2014 $1.52T of FY37 revenue, 48% through-cycle FCF margins, 12% discount \u2014 is worth $224. At $234 the market is paying full freight for the duration call with nothing left for the fade risk.",
    "<b>The digestion cliff is a when, not an if.</b> Every compute build-out ends in digestion. $1.3T of 2027 hyperscaler capex, 119 days of inventory, and raw-materials tripling year over year are exactly what the top of a cycle looks like. Our bear case prices the 2029\u201330 version honestly; the price assigns it ~zero weight.",
    "<b>Cash conversion is deteriorating at the peak.</b> Receivables up 54.9% quarter over quarter vs revenue up 17.9% \u2014 days sales outstanding expanded to ~60 days. Q2 free cash flow was $21.3B on $96.2B of revenue (22%), because working capital is absorbing the ramp. $36.9B of newly-appearing restricted cash is opaque.",
    "<b>$94B of circular exposure.</b> NVIDIA carries roughly $94B of equity positions in other companies \u2014 many of them its own customers (AI labs, infrastructure financiers). Vendor-financing-style arrangements flatter both revenue and the investment book; in a downturn they unwind together.",
    "<b>Margin pressure is guided, not hypothetical.</b> Gross margin bottoms at 71\u201372% in Q4 FY27 and settles at 72\u201373% in FY28 on memory pricing \u2014 the price increases only partly offset. The 75% print is the peak, and our terminal margins assume the market knows it.",
    "<b>Concentration and substitution.</b> A handful of hyperscalers drive the majority of revenue; their own ASICs (TPU v7, Trainium, Maia) and Broadcom's 10GW OpenAI custom-silicon deal steadily erode the merchant-GPU share of each incremental data-center dollar.",
]:
    story.append(B(b))

# ============ 2. BUSINESS ============
story.append(P("2 &nbsp; Company Overview", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("NVIDIA (founded 1993, Santa Clara) has completed its transformation from chipmaker to AI-factory "
               "platform: the product is no longer the GPU but the gigawatt-scale data center, sold as an integrated "
               "stack of compute (Blackwell Ultra today, Vera Rubin ramping), CPU (Vera/Grace), networking (InfiniBand "
               "and Spectrum-X Ethernet, now ~18% of data center revenue), and CUDA software. Q2 FY27 (ended July 26, "
               "2026): revenue $96.22B (+106% YoY), data center $89.0B (+117% YoY) on the Blackwell Ultra ramp, GAAP "
               "gross margin 75.0%, net margin 62.0%, diluted EPS $2.46. Vera Rubin entered full production in March "
               "2026 and is on pace for the fastest product ramp in company history, with NVL72 systems delivering to "
               "Google Cloud, Microsoft Azure, Oracle Cloud, CoreWeave, and Nebius \u2014 meaning NVIDIA is currently "
               "running two product cycles simultaneously.", s_body))
story.append(P("The forward picture: Q3 FY27 guided to $108B (\u00b12%, gross margin 74.0%, excluding any China data "
               "center revenue); FY28 guided to ~70% revenue growth (~$670B) on supply that management says cannot "
               "meet demand; a $150B buyback top-up taking remaining authorization to $235B through FY28; and a "
               "balance sheet with $56.6B of liquid resources against $38.4B of debt \u2014 plus $42.8B of marketable "
               "equity securities and $51.2B of non-marketable stakes in AI labs and partners. The open question for "
               "the decade mirrors AMD's in reverse: not whether the next two years are sold (they are, several times "
               "over) but how long the build-out lasts and what the business earns when the factories are built. "
               "Our judgment: supercycle through 2030, then a long fade \u2014 with a genuine 2029\u201330 digestion "
               "cliff as the live alternative.", s_body))

# ============ 3. COMPETITION ============
story.append(P("3 &nbsp; Competition", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("NVIDIA's moat is the full stack \u2014 CUDA's 20-year software ecosystem, the networking layer that "
               "locks racks together, and a one-generation lead in execution \u2014 and it is genuinely wide: no "
               "competitor ships a comparable rack-scale system at volume. The threats are structural, not cyclical. "
               "AMD's MI450/Helios is now a contracted second source at three frontier labs plus Oracle. Broadcom's "
               "10GW custom-silicon partnership with OpenAI attacks from the custom side, where NVIDIA's merchant "
               "margin doesn't apply. Hyperscaler ASICs (Google TPU v7, Amazon Trainium, Microsoft Maia) steadily "
               "absorb inference workloads internally \u2014 the 'NVIDIA tax' the hyperscalers are explicitly trying "
               "to reduce. Export controls have effectively ceded China's data-center market (Q3 guidance excludes "
               "it entirely), and DOJ/EU antitrust scrutiny of the networking lock-in is a live overhang. None of "
               "this dents 2027\u201328. All of it shapes the fade.", s_body))

# ============ 4. VALUATION ============
story.append(P("4 &nbsp; Valuation \u2014 10-Year Scenario DCF, Fair Value $223", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Model: 10-year explicit free-cash-flow DCF (FY2027\u2013FY2037; fiscal year ends January), weights bear "
               "25% / base 50% / bull 25%. Scenario discounts: <b>base 12.0%</b> (cycle concentration, customer "
               "concentration, geopolitical and antitrust overhangs), <b>bear 14.5%</b> (base + 250bp), <b>bull "
               "10.5%</b> (base \u2212 150bp). Terminal growth <b>1.5% / 2.5% / 2.5%</b> on year-10 FCF at normalized "
               "through-cycle margins (never peak). Equity = firm EV + ~$18.2B net liquid cash ($22.4B cash + $34.1B "
               "marketable debt securities less $38.4B debt; restricted cash and equity stakes excluded), over "
               "scenario-specific diluted shares (24.3B / 23.5B / 22.8B \u2014 buybacks continue in base/bull, pause "
               "in bear). FY2027E revenue anchor: $396B (Q2 $96.22B, Q3 guide $108B).", s_body))
story.append(Spacer(1, 3*mm))
story.append(P("Scenario DCF (10-year FCFF, $B revenue):", s_h2))
dcf = [
    [cell("Scenario", s_theadL), cell("FY28 rev", s_thead), cell("Rev CAGR (10-yr)", s_thead), cell("FCF mgn yr-10", s_thead), cell("Discount / term. g", s_thead), cell("Fair value", s_thead)],
    [cell("Bear", s_cellB), cell("$545B", s_cellR), cell("+5.2%", s_cellR), cell("39%", s_cellR), cell("14.5% / 1.5%", s_cellR), cell("$56", s_cellBR)],
    [cell("Base", s_cellB), cell("$673B", s_cellR), cell("+14.4%", s_cellR), cell("48%", s_cellR), cell("12.0% / 2.5%", s_cellR), cell("$224", s_cellBR)],
    [cell("Bull", s_cellB), cell("$745B", s_cellR), cell("+18.2%", s_cellR), cell("50%", s_cellR), cell("10.5% / 2.5%", s_cellR), cell("$391", s_cellBR)],
    [cell("Probability-weighted (25/50/25) \u2192 <b>$223 target</b>", s_cellB), cell("", s_cellC), cell("", s_cellR), cell("", s_cellR), cell("", s_cellR), cell("$223", s_cellBR)],
]
story.append(styled_table(dcf, [62*mm, 22*mm, 28*mm, 24*mm, 30*mm, 24*mm]))

d2 = Drawing(430, 185)
d2.add(String(215, 173, "Scenario fair values vs. current price ($)", fontName="Helvetica-Bold", fontSize=10, textAnchor="middle", fillColor=NAVY))
bc2 = VerticalBarChart(); bc2.x = 45; bc2.y = 30; bc2.height = 115; bc2.width = 340
bc2.data = [[56, 224, 391, 223, 234]]
bc2.strokeColor = None; bc2.barLabels.nudge = 8; bc2.barLabelFormat = "%d"
bc2.bars[0].fillColor = ACCENT
bc2.categoryAxis.categoryNames = ["Bear", "Base", "Bull", "Wtd. avg", "Price"]
bc2.valueAxis.valueMin = 0; bc2.valueAxis.valueMax = 440; bc2.valueAxis.valueStep = 110
bc2.valueAxis.labels.fontSize = 7; bc2.categoryAxis.labels.fontSize = 8
d2.add(bc2)
story.append(d2)

story.append(P("The base case is the guided wave, priced honestly. FY28 revenue of $673B is management's own ~70% "
               "guide \u2014 supply-constrained, with demand running higher \u2014 followed by +26% and +18% as the "
               "Rubin generation scales and the $40B-per-gigawatt full-stack mix builds. The duration judgment: the "
               "supercycle runs through <b>2030</b> (Rubin + Rubin Ultra waves, sovereign AI as a floor), then fades "
               "from 2031 as the installed base digests \u2014 growth stepping down through the high single digits to "
               "~3.5%, FCF margins normalizing to a through-cycle 48% (well below today's 60%+ net margins, above "
               "any historical semiconductor norm). Result: <b>$223.62 \u2192 $224</b>.", s_body))
story.append(P("The bull case ($390.70 \u2192 $391) extends the supercycle through <b>2032</b> \u2014 sovereign AI "
               "compounds, the full-stack $40B/GW economics hold, growth stays double-digit into the early 2030s "
               "with 50% through-cycle FCF margins. The bear case ($55.56 \u2192 $56) is the 2029\u201330 digestion "
               "cliff: the 2026\u201328 pre-build overshoots, book-to-bill drops below 1.0, revenue falls ~17% in "
               "FY29 and another 7% in FY30, FCF margins compress 900bp vs base as price cuts clear the glut, and "
               "terminal growth is 1.5%. All three hurt conditions are met and the bear sits far below the price. "
               "Terminal value is 39\u201356% of EV across scenarios (no haircut required).", s_body))
story.append(P("<b>Price target: $223</b> (0.25\u00d7$56 + 0.50\u00d7$224 + 0.25\u00d7$391 = $223.38, rounded) \u2014 the "
               "target <i>is</i> the weighted DCF. The Street's ~$323 mean target prices roughly our bull case as the "
               "expected outcome; our duration judgment \u2014 supercycle through 2030, fade from 2031, an honest "
               "2029\u201330 digestion cliff in the bear \u2014 leaves fair value at the quote. What would change the "
               "call: evidence the wave is <i>bigger</i> than contracted (book-to-bill sustained above 1.5 with lead "
               "times extending into 2028) pushes toward the bull; conversely, the contracted-demand assumption "
               "behind the 2027\u201328 numbers would be <b>withdrawn</b> if book-to-bill falls below 1.0 for two "
               "consecutive quarters or if lead times normalize \u2014 at which point the bear case becomes the base "
               "case and this note becomes a SELL.", s_body))

story.append(P("5 &nbsp; Key Risks", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
for b in [
    "<b>The digestion cliff (the #1 risk).</b> $1.3T of 2027 hyperscaler capex, 119 days of inventory, raw materials tripling YoY \u2014 the top-of-cycle signature. When the pre-build overshoots, the correction is violent (bear: \u201317% FY29 revenue).",
    "<b>Cash conversion at the peak.</b> DSO expanding to ~60 days, receivables +54.9% QoQ vs revenue +17.9%; Q2 FCF only 22% of revenue. If customers are being financed to take supply, the demand signal is softer than the revenue line.",
    "<b>$94B of circular exposure.</b> Equity stakes in customers and infrastructure financiers unwind together with demand in a downturn.",
    "<b>Margin compression is guided.</b> Gross margin bottoming 71\u201372% in Q4 FY27 on memory pricing; the 75% print is the peak.",
    "<b>Customer and geographic concentration.</b> A handful of hyperscalers; China data-center revenue excluded entirely; export policy can tighten further.",
    "<b>Substitution.</b> Hyperscaler ASICs and Broadcom/OpenAI custom silicon erode the merchant-GPU share of each new data-center dollar \u2014 the fade mechanism in miniature.",
    "<b>Antitrust.</b> DOJ/EU scrutiny of networking lock-in; a forced unbundling would compress the $40B/GW full-stack economics.",
    "<b>Power.</b> Gigawatt-scale data centers face grid and permitting constraints that can push deployments right regardless of chip supply.",
]:
    story.append(B(b))

story.append(P("Recommendation", s_h2))
story.append(P("<b>HOLD, $223 target (\u20134.5%), Medium-High risk.</b> NVIDIA is the best business in the AI build-out "
               "and the one whose near-term demand is most verifiable \u2014 a 70% FY28 guide management calls "
               "supply-constrained, $279B of supply commitments, HBM sold out through 2026, and sovereign AI putting "
               "a floor under the cycle. But 'best business' and 'best stock' are different questions at $233.95. "
               "Our scenarios \u2014 bear $56 (the honest 2029\u201330 digestion cliff) / base $224 (supercycle through "
               "2030, then fade) / bull $391 (supercycle through 2032) \u2014 weight to $223, essentially the quote. "
               "The Street's ~$323 mean target is paying for the bull case as the expected outcome; we are not. Own "
               "it if you own the duration call; there is no margin of safety at this price for the fade arriving "
               "early. <b>Falsification:</b> book-to-bill below 1.0 for two consecutive quarters, or lead times "
               "normalizing, withdraws the contracted-demand assumption \u2014 the bear becomes the base and this "
               "HOLD becomes a SELL. Watch Q3 FY27 (November): DSO normalization and Rubin shipment linearity are the "
               "two numbers that matter.", s_body))
story.append(Spacer(1, 6*mm))
story.append(P("Methodology &amp; sources. Valuation as of October 4, 2026; share price $233.95 (10/2/26 close). Model: 10-year "
               "scenario FCFF DCF (FY2027\u2013FY2037), weights bear 25% / base 50% / bull 25%; discounts base 12.0% / "
               "bear 14.5% / bull 10.5%; terminal growth 1.5% / 2.5% / 2.5% on year-10 FCF at normalized "
               "through-cycle margins. Net liquid cash ~$18.2B ($22.4B cash + $34.1B marketable debt securities less "
               "$38.4B debt; restricted cash and equity stakes excluded); scenario diluted shares 24.3B / 23.5B / "
               "22.8B. Bear case meets the hurt conditions (revenue decline, \u2265300bp margin compression vs base, "
               "\u226525% terminal derating) and sits below the current price. Terminal value is 39\u201356% of EV (no "
               "haircut required). Demand evidence: Q2 FY27 results and FY28 guide (company earnings call, Aug 26, "
               "2026); Rubin production status (company statements, Mar\u2013Sep 2026); $279B supply commitments "
               "(TrendForce, Aug 2026); >15% system price increases (SiliconAnalysts, Aug 2026); HBM sold out 2026 "
               "(SK Hynix); hyperscaler capex figures (CFO commentary); HUMAIN/UK/South Korea sovereign programs. "
               "Market data via Yahoo Finance. This note is research analysis for informational purposes and is not "
               "personalized investment advice. Equity investing involves risk of loss. The author holds no position in "
               "NVDA at the time of writing.", s_small))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=18*mm,
                        title="NVDA \u2014 Equity Research Note", author="Muse")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("wrote", OUT)
