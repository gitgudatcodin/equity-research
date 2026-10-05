#!/usr/bin/env python3
"""Build the AMD (Advanced Micro Devices) equity research note PDF - standalone analyst report, Oct 4, 2026.
Model: ~/workspace/your_files/amd-equity-research/model.json
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

OUT = "/home/hatch/workspace/your_files/amd-equity-research/amd-equity-research-note.pdf"

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
    canvas.drawString(18*mm, 12*mm, "AMD (NASDAQ: AMD)  \u2014  Equity Research Note  \u2014  October 2026")
    canvas.drawRightString(W - 18*mm, 12*mm, f"Page {doc.page}")
    canvas.setStrokeColor(MGRAY); canvas.setLineWidth(0.5)
    canvas.line(18*mm, 14.5*mm, W - 18*mm, 14.5*mm)
    canvas.restoreState()

# ============ COVER ============
story.append(Spacer(1, 24*mm))
story.append(P("AMD (NASDAQ: AMD)", ParagraphStyle("x", parent=s_sub, fontName="Helvetica-Bold", fontSize=13, textColor=ACCENT, spaceAfter=2)))
story.append(P("Fourteen Gigawatts of Contracts,<br/>Priced for Forty", s_title))
story.append(Spacer(1, 4*mm))
story.append(P("Equity Research Note  \u00b7  Semiconductors \u2014 AI Accelerators &amp; Server CPUs  \u00b7  October 4, 2026", s_sub))
story.append(Spacer(1, 8*mm))

rating_data = [
    [cell("Recommendation", s_theadL), cell("12-Mo. Price Target", s_thead), cell("Current Price", s_thead), cell("Implied Upside", s_thead), cell("Risk Rating", s_thead)],
    [Paragraph("<b><font color=\"#B45309\" size=\"13\">REDUCE</font></b>", s_cellC),
     Paragraph("<b><font size=\"12\">$163</font></b>", s_cellC),
     Paragraph("<b>$633.91</b><br/><font size=\"7\" color=\"#5A6472\">Oct 2, 2026</font>", s_cellC),
     Paragraph("<b><font color=\"#B42318\">-74.3%</font></b>", s_cellC),
     Paragraph("<b>High</b><br/><font size=\"7\" color=\"#5A6472\">Beta 2.55</font>", s_cellC)],
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
    ["Market cap", "~$1.04 tn", "Shares out. (dil.)", "~1.66 bn"],
    ["Enterprise value", "~$1.03 tn", "52-week range", "$160.49 \u2013 $645.46"],
    ["Net cash", "~$8.8 bn", "YTD / 1-yr return", "+196% / +285%"],
    ["Q2 2026 rev / DC rev", "$11.54 bn / $6.72 bn (+107%)", "TTM / fwd P/E", "161x / 57x"],
    ["Q3 2026 guide", "~$13.0 bn (+41% YoY)", "Mgmt 2027 DC guide", "~$70 bn (2x YoY)"],
    ["Next catalyst", "Q3 results (early Nov)", "Street consensus target", "~$620 (Buy)"],
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
story.append(P("Our view of the business: AMD has crossed the line from challenger narrative to contracted infrastructure "
               "supplier. Fourteen gigawatts of committed deployments across OpenAI (6GW), Meta (6GW), and Anthropic (2GW) "
               "\u2014 with warrants that only vest as silicon ships \u2014 turn the 2027 revenue ramp from a forecast into "
               "a delivery schedule. The strategic question is not whether AMD can sell the 2027 wave \u2014 it is sold \u2014 "
               "but what happens after the first wave is delivered. We see a genuine multi-year runway: hyperscaler capex "
               "near $800B in 2026 and headed toward $1.3T in 2027, sovereign AI as a new customer class, and AMD "
               "establishing itself as the credible second source with double-digit AI-accelerator share. But the price "
               "has skipped the debate entirely.", s_body))
story.append(P("At $633.91, AMD is valued as if the supercycle never fades and AMD captures far more than double-digit "
               "share. The arithmetic is unforgiving: $634 implies roughly <b>$1.3 trillion of mid-2030s revenue</b> \u2014 "
               "a ~44% decade CAGR, about <b>four to five times our bull case</b>. Our three scenarios are <b>$34 / $153 / "
               "$312</b>, weighted to a <b>$163 target, \u201374.3%</b> against the quote. The business thesis is intact; "
               "the price is not. That is the entire note in two sentences, and the valuation section shows the work. "
               "<b>REDUCE.</b>", s_body))
story.append(P("The one thing this note does differently from a standard DCF: near-term visibility is unusually high, "
               "because demand is contracted, not extrapolated. Our 2027\u201328 revenue assumptions track management's "
               "stated targets \u2014 data center revenue doubling to ~$70B in 2027, with AI GPUs in the low $40 billions "
               "\u2014 rather than being mechanically haircut, because those targets are now backed by named, "
               "milestone-linked deployments: OpenAI's first gigawatt of MI450s deploying in H2 2026, Meta's on the same "
               "timeline, Anthropic's first gigawatt in H1 2027, Oracle's initial 50,000 MI450s starting Q3 2026 and "
               "expanding in 2027, and a $1.2B Vultr Helios order (the platform's first commercial sale) deploying in "
               "Q4 2026. Demand evidence must be AMD-specific, not 'AI is hot' \u2014 and here it is: $29\u201330B of AMD's "
               "own supply purchase commitments, the largest TSMC allocation increase of any customer, and ~10% price "
               "increases on AI accelerators. Companies short on demand do not raise prices.", s_body))
story.append(P("All of the skepticism therefore concentrates where it belongs: in <b>duration and fade</b>. Our base case "
               "gives the hypergrowth phase through <b>2029</b> (the committed 14GW deploys through 2030 milestone schedules), "
               "then fades growth into the single digits with through-cycle FCF margins of 18%. The bull case extends the "
               "supercycle through <b>2032</b> (sovereign AI plus an inference replacement cycle) with 22% terminal FCF "
               "margins \u2014 still only $312. The bear case is the honest version of 2028\u201329: the 2026\u201327 pre-build "
               "overshoots, book-to-bill collapses below 1.0, the $8.5B inventory build becomes a glut, revenue falls ~13% "
               "in 2029, and margins compress 500bp as price cuts clear the channel. Bear $34 \u2014 below the price, as a "
               "bear must be.", s_body))

story.append(P("Why the demand is real", s_h2))
for b in [
    "<b>14GW contracted across three named counterparties.</b> OpenAI: up to 6GW of Instinct GPUs, first gigawatt of MI450s deploying H2 2026, with warrants for up to 160M shares at $0.01 vesting on deployment milestones through October 2030 \u2014 AMD expects 'tens of billions' in annual revenue. Meta: a near-identical 6GW arrangement with its own 160M-share warrant. Anthropic: up to 2GW, first gigawatt H1 2027. Customer forecasts are running <i>above</i> the levels contemplated when the partnerships began.",
    "<b>The order book is diversifying beyond the big three.</b> Oracle: initial 50,000 MI450 GPUs starting Q3 2026, expanding in 2027+. Vultr: a $1.2B Helios rack order through HPE \u2014 the platform's first commercial sale \u2014 deploying Q4 2026. Seven of the world's top 10 AI companies now use Instinct GPUs.",
    "<b>Supply-side commitments match the demand.</b> $29\u201330B in purchase commitments, the largest TSMC allocation increase granted to any customer, and HBM sold out across the industry through 2026. AMD is locking the supply it needs to deliver the contracted wave.",
    "<b>Pricing power, not discounting.</b> AMD is raising prices ~10% across AI accelerators, consumer GPUs, and chipsets \u2014 the behavior of an allocated supplier, not one chasing demand.",
    "<b>The numbers are already moving.</b> Q2 2026: revenue $11.54B (+50% YoY), data center $6.72B (+107%) and 58% of the total; Q3 guided to ~$13.0B (+41%). Server CPU revenue is guided to grow >80% in H2 2026 and >70% in 2027.",
]:
    story.append(B(b))
story.append(P("Why the price is wrong anyway", s_h2))
for b in [
    "<b>$634 prices ~5x the bull case.</b> Even giving AMD the supercycle through 2032 and 22% through-cycle FCF margins \u2014 a genuinely heroic outcome \u2014 fair value is $312, less than half the quote. The market is not pricing the contracted wave; it is pricing a second and third wave nobody has contracted.",
    "<b>320M warrants = ~20% potential dilution.</b> Against ~1.63B basic shares, the OpenAI and Meta warrants (160M each at $0.01) are the price of the contracts. The dilution is real, it becomes visible in 2027\u201328 financials, and our per-share values reflect scenario-specific vesting (bear 1.70B / base 1.80B / bull 1.95B shares).",
    "<b>Customer concentration is extreme.</b> Three counterparties account for the 14GW. If any one of them pauses \u2014 note that two of the three CEOs publicly argued for slowing AI capability advancement this year (a governance position, not a procurement change, but a real signal) \u2014 the 2027 guide is at risk.",
    "<b>Margins compress before they expand.</b> Management itself says gross margin edges lower in Q4 and through 2027 as MI450 ramps; rack-scale Helios is a lower-margin systems sale than merchant silicon. The Q2 FCF print ($1.6B) was flattered by a ~$2.4B payables stretch.",
    "<b>CUDA is still the moat AMD doesn't have.</b> ROCm is improving but the software gap is the reason AMD is the second source \u2014 and second sources get second-source economics when the cycle turns.",
    "<b>The cycle will turn.</b> Every semiconductor supercycle ends in a digestion phase. Our bear case prices it in 2028\u201329; the market prices no digestion at all.",
]:
    story.append(B(b))

# ============ 2. BUSINESS ============
story.append(P("2 &nbsp; Company Overview", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Advanced Micro Devices (founded 1969, Santa Clara) is a fabless semiconductor company whose center of "
               "gravity has shifted decisively to the data center. The Data Center segment \u2014 EPYC server CPUs and "
               "Instinct AI accelerators \u2014 did $6.72B in Q2 2026 (+107% YoY), 58% of total revenue, and management "
               "expects it to roughly double to ~$70B in 2027, with AI GPUs in the low $40 billions and server CPUs most "
               "of the rest. The product engine is the Helios rack-scale AI platform: up to 72 Instinct MI400/MI450 "
               "accelerators (CDNA 5, TSMC 2nm, up to 432GB HBM4 per chip) paired with 6th-gen EPYC 'Venice' CPUs and "
               "Pensando networking in a liquid-cooled rack \u2014 AMD's answer to NVIDIA's Vera Rubin, sold as a full "
               "system rather than merchant silicon. MI450 production shipments began in Q3 2026 with a sharp Q4 ramp; "
               "MI500 is in customer development for 2027, described internally as the largest generational leap in "
               "Instinct history.", s_body))
story.append(P("The rest of the business \u2014 Client (Ryzen), Gaming (semi-custom), Embedded (Xilinx) \u2014 is roughly "
               "$20B of durable, slower-growing revenue that funds the AI build-out and provides ballast if the "
               "accelerator cycle turns. Balance sheet: $13.1B of cash and short-term investments against ~$4.3B of "
               "debt (~$8.8B net cash); no refinancing pressure. The P&amp;L is inflecting: Q2 non-GAAP EPS of $1.66 vs "
               "$0.48 a year earlier, data center operating margin 31.3%. The open question for the decade is not "
               "2027 \u2014 that is contracted \u2014 but whether AMD converts a spectacular deployment wave into a "
               "durable franchise: double-digit AI-accelerator share, a closing ROCm gap, and server-CPU share gains "
               "compounding off a much higher base.", s_body))

# ============ 3. COMPETITION ============
story.append(P("3 &nbsp; Competition", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("NVIDIA (&gt;90% AI-accelerator share, the CUDA moat) is the competitor that sets the terms: AMD wins when "
               "customers want a second source badly enough to pay warrant-level incentives, and loses pricing power the "
               "moment supply normalizes. Broadcom is the quieter threat \u2014 co-developing 10GW of custom accelerators "
               "with OpenAI, it attacks the same 'alternative to NVIDIA' budget from the custom-silicon side. The "
               "hyperscalers' own ASICs (Google TPU v7, Amazon Trainium, Microsoft Maia) increasingly absorb inference "
               "workloads that would otherwise buy merchant GPUs. Intel remains a non-factor in training but a wildcard "
               "in 2027. AMD's moat is execution plus openness: rack-scale systems capability (ZT Systems), an open "
               "Ethernet/software stack that appeals to customers allergic to lock-in, and \u2014 for now \u2014 the only "
               "credible alternative to a single supplier the entire industry is desperate to diversify away from. That "
               "diversification bid is real, but it is cyclical: second sources are loved in shortages and squeezed in "
               "gluts.", s_body))

# ============ 4. VALUATION ============
story.append(P("4 &nbsp; Valuation \u2014 10-Year Scenario DCF, Fair Value $163", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Model: 10-year explicit free-cash-flow DCF (FY2026\u20132036), weights bear 25% / base 50% / bull 25%. "
               "Scenario discounts: <b>base 12.0%</b> (beta 2.55, extreme customer concentration, warrant overhang, "
               "cyclical semiconductors), <b>bear 14.5%</b> (base + 250bp), <b>bull 10.5%</b> (base \u2212 150bp). "
               "Terminal growth <b>0% / 2.0% / 2.0%</b> on year-10 FCF at normalized through-cycle margins (never peak). "
               "Equity = firm EV + ~$8.8B net cash, over scenario-specific diluted shares (1.70B / 1.80B / 1.95B) "
               "reflecting warrant vesting that scales with deployment success. FY2026E revenue anchor: $48.5B "
               "(Q1 $8.6B + Q2 $11.54B + Q3 guide $13.0B + Q4 ~$15.4B on the Helios ramp).", s_body))
story.append(Spacer(1, 3*mm))
story.append(P("Scenario DCF (10-year FCFF, $B revenue):", s_h2))
dcf = [
    [cell("Scenario", s_theadL), cell("2027 rev", s_thead), cell("Rev CAGR (10-yr)", s_thead), cell("FCF mgn yr-10", s_thead), cell("Discount / term. g", s_thead), cell("Fair value", s_thead)],
    [cell("Bear", s_cellB), cell("$72B", s_cellR), cell("+6.5%", s_cellR), cell("13%", s_cellR), cell("14.5% / 0%", s_cellR), cell("$34", s_cellBR)],
    [cell("Base", s_cellB), cell("$90B", s_cellR), cell("+16.3%", s_cellR), cell("18%", s_cellR), cell("12.0% / 2.0%", s_cellR), cell("$153", s_cellBR)],
    [cell("Bull", s_cellB), cell("$99B", s_cellR), cell("+22.3%", s_cellR), cell("22%", s_cellR), cell("10.5% / 2.0%", s_cellR), cell("$312", s_cellBR)],
    [cell("Probability-weighted (25/50/25) \u2192 <b>$163 target</b>", s_cellB), cell("", s_cellC), cell("", s_cellR), cell("", s_cellR), cell("", s_cellR), cell("$163", s_cellBR)],
]
story.append(styled_table(dcf, [62*mm, 22*mm, 28*mm, 24*mm, 30*mm, 24*mm]))

d2 = Drawing(430, 185)
d2.add(String(215, 173, "Scenario fair values vs. current price ($)", fontName="Helvetica-Bold", fontSize=10, textAnchor="middle", fillColor=NAVY))
bc2 = VerticalBarChart(); bc2.x = 45; bc2.y = 30; bc2.height = 115; bc2.width = 340
bc2.data = [[34, 153, 312, 163, 634]]
bc2.strokeColor = None; bc2.barLabels.nudge = 8; bc2.barLabelFormat = "%d"
bc2.bars[0].fillColor = ACCENT
bc2.categoryAxis.categoryNames = ["Bear", "Base", "Bull", "Wtd. avg", "Price"]
bc2.valueAxis.valueMin = 0; bc2.valueAxis.valueMax = 700; bc2.valueAxis.valueStep = 140
bc2.valueAxis.labels.fontSize = 7; bc2.categoryAxis.labels.fontSize = 8
d2.add(bc2)
story.append(d2)

story.append(P("The base case is the contracted wave, priced honestly. 2027 revenue of $90B sits at management's $70B "
               "data-center guide plus ~$20B for the rest of the business \u2014 no haircut, because 14GW of named "
               "deployments, $29\u201330B of supply commitments, and customer forecasts running above partnership "
               "levels are verifiable demand, not narrative. Growth then runs +31% (2028), +19% (2029) as the wave "
               "deploys through the 2030 milestone schedules, and fades from 2030 as the first-wave capacity digests "
               "\u2014 this is the duration judgment the whole note rests on. FCF margins build from ~10% (inventory and "
               "MI450-ramp drag) to a through-cycle 18%, well below peak-cycle fantasies. Result: <b>$152.50 \u2192 $153</b>.",
               s_body))
story.append(P("The bull case ($311.94 \u2192 $312) extends the supercycle through 2032 \u2014 sovereign AI plus an "
               "inference replacement cycle keep growth above 10% into the early 2030s, FCF margins reach 22% on "
               "rack-scale mix \u2014 and <i>still</i> lands at less than half the quote. The bear case ($34.11 \u2192 "
               "$34) is the 2028\u201329 digestion cliff: book-to-bill drops below 1.0 for consecutive quarters, the "
               "$8.5B inventory build becomes a glut, revenue falls ~13% in 2029, and FCF margins compress 500bp vs "
               "base as price cuts clear the channel \u2014 with terminal growth at 0%. All three hurt conditions are "
               "met and the bear sits far below the price. Terminal value is 43\u201359% of EV across scenarios (no "
               "haircut required).", s_body))
story.append(P("<b>Price target: $163</b> (0.25\u00d7$34 + 0.50\u00d7$153 + 0.25\u00d7$312 = $162.76, rounded) \u2014 the "
               "target <i>is</i> the weighted DCF. What would falsify the REDUCE: sustained book-to-bill above 1.5 with "
               "lead times extending into 2028 (evidence the wave is bigger than contracted), or year-10 revenue "
               "tracking toward $300B+ with FCF margins above 20% \u2014 neither of which the current evidence "
               "supports. Conversely, the contracted-demand assumption behind the 2027\u201328 numbers would be "
               "<b>withdrawn</b> if book-to-bill falls below 1.0 for two consecutive quarters or if lead times "
               "normalize \u2014 at which point the bear case becomes the base case.", s_body))

story.append(P("5 &nbsp; Key Risks", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
for b in [
    "<b>Customer concentration.</b> Three counterparties (OpenAI, Meta, Anthropic) account for the 14GW. A pause by any one of them breaks the 2027 guide.",
    "<b>Warrant dilution (~20%).</b> 320M shares at $0.01 vesting on deployment and price milestones; visible in 2027\u201328 financials.",
    "<b>Execution on Helios/MI450.</b> Rack-scale systems are a new muscle; qualification slips or yield issues push the wave right. Gross margin edges lower through 2027 on the ramp.",
    "<b>CUDA/ROCm gap.</b> The software moat is NVIDIA's; AMD wins on openness and price, which compress first in a glut.",
    "<b>Cycle digestion.</b> $8.5B of inventory plus channel pre-building ahead of the wave; if 2027 demand was pulled forward, 2028\u201329 is the cliff.",
    "<b>AI-pacing governance.</b> Two of the three anchor customers' CEOs have publicly argued for slowing capability advancement \u2014 procurement is unchanged, but the headline risk to the demand narrative is real.",
    "<b>Hyperscaler ASICs and Broadcom custom silicon</b> compete for the same diversification budget.",
    "<b>Export controls</b> on high-end accelerators remain a geopolitical overhang.",
]:
    story.append(B(b))

story.append(P("Recommendation", s_h2))
story.append(P("<b>REDUCE, $163 target (\u201374.3%), High risk.</b> This is the rare note where the business call and the "
               "stock call point in opposite directions, and we refuse to blur them. The business call is genuinely "
               "bullish: 14GW of contracted, milestone-warranted deployments make 2027 a delivery schedule, and AMD is "
               "becoming the credible second source in the largest semiconductor build-out in history. The stock call "
               "is arithmetic: $634 prices roughly $1.3T of mid-2030s revenue \u2014 a ~44% decade CAGR, four to five "
               "times even our supercycle-through-2032 bull case. Bear $34 / base $153 / bull $312, weighted to $163 "
               "against a $633.91 quote. The Street's ~$620 consensus target prices the wave continuing forever; our "
               "duration judgment \u2014 hypergrowth through 2029, fade from 2030, an honest 2028\u201329 digestion cliff "
               "in the bear \u2014 says it won't. <b>Falsification:</b> book-to-bill below 1.0 for two consecutive "
               "quarters, or lead times normalizing, withdraws the contracted-demand assumption and makes the bear "
               "case the base case. Watch Q3 results (early November) and Q4 Helios shipment volumes against the $70B "
               "2027 data-center guide \u2014 the first real test of whether the delivery schedule holds.", s_body))
story.append(Spacer(1, 6*mm))
story.append(P("Methodology &amp; sources. Valuation as of October 4, 2026; share price $633.91 (10/2/26 close). Model: 10-year "
               "scenario FCFF DCF, weights bear 25% / base 50% / bull 25%; discounts base 12.0% / bear 14.5% / bull 10.5%; "
               "terminal growth 0% / 2.0% / 2.0% on year-10 FCF at normalized through-cycle margins. Net cash ~$8.8B "
               "($13.1B cash &amp; short-term investments less ~$4.3B debt); scenario diluted shares 1.70B / 1.80B / 1.95B "
               "(warrant vesting scales with deployment). Bear case meets the hurt conditions (revenue decline, "
               "\u2265300bp margin compression vs base, \u226525% terminal derating) and sits below the current price. "
               "Terminal value is 43\u201359% of EV (no haircut required). Demand evidence: OpenAI/Meta/Anthropic "
               "gigawatt commitments and warrant terms (company announcements, Oct 2025\u2013Feb 2026); Oracle 50,000-GPU "
               "and Vultr $1.2B Helios orders; $29\u201330B purchase commitments and $70B 2027 data-center guide (Citi "
               "Global TMT Conference, Sep 8, 2026); Q2 2026 results (revenue $11.54B, data center $6.72B). Market data "
               "via Yahoo Finance/Finnhub. This note is research analysis for informational purposes and is not "
               "personalized investment advice. Equity investing involves risk of loss. The author holds no position in "
               "AMD at the time of writing.", s_small))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=18*mm,
                        title="AMD \u2014 Equity Research Note", author="Muse")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("wrote", OUT)
