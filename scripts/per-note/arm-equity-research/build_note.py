#!/usr/bin/env python3
"""Build the ARM (Arm Holdings plc) equity research note PDF - standalone analyst note, Oct 4 2026."""
import json
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, HRFlowable)
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import VerticalBarChart

OUT = "/home/hatch/workspace/your_files/arm-equity-research/arm-equity-research-note.pdf"
M = json.load(open("/home/hatch/workspace/your_files/arm-equity-research/valuation_output.json"))

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
    canvas.drawString(18*mm, 12*mm, "ARM (NASDAQ: ARM)  \u2014  Equity Research Note  \u2014  October 2026")
    canvas.drawRightString(W - 18*mm, 12*mm, f"Page {doc.page}")
    canvas.setStrokeColor(MGRAY); canvas.setLineWidth(0.5)
    canvas.line(18*mm, 14.5*mm, W - 18*mm, 14.5*mm)
    canvas.restoreState()

# ============ COVER ============
story.append(Spacer(1, 24*mm))
story.append(P("ARM (NASDAQ: ARM)", ParagraphStyle("x", parent=s_sub, fontName="Helvetica-Bold", fontSize=13, textColor=ACCENT, spaceAfter=2)))
story.append(P("Wonderful Business, Bubble Price<br/>The Royalty Machine at 52\u00d7 Sales", s_title))
story.append(Spacer(1, 4*mm))
story.append(P("Equity Research Note  \u00b7  Technology \u2014 Semiconductors (IP Licensing)  \u00b7  October 4, 2026", s_sub))
story.append(Spacer(1, 8*mm))

rating_data = [
    [cell("Recommendation", s_theadL), cell("12-Mo. Price Target", s_thead), cell("Current Price", s_thead), cell("Implied Upside", s_thead), cell("Risk Rating", s_thead)],
    [Paragraph("<b><font color=\"#B42318\" size=\"13\">SELL</font></b>", s_cellC),
     Paragraph("<b><font size=\"12\">$48</font></b>", s_cellC),
     Paragraph("<b>$307.49</b><br/><font size=\"7\" color=\"#5A6472\">Oct 2, 2026</font>", s_cellC),
     Paragraph("<b><font color=\"#B42318\">-84.3%</font></b>", s_cellC),
     Paragraph("<b>High</b><br/><font size=\"7\" color=\"#5A6472\">Beta 3.78</font>", s_cellC)],
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
    ["Market cap", "~$313.6 bn", "Shares out. (dil. ADS)", "~1.03 bn"],
    ["Enterprise value", "~$309.7 bn", "52-week range", "$100.02 \u2013 $452.70"],
    ["Net cash", "~$3.9 bn", "YTD / 1-yr return", "+181% / +101%"],
    ["FY26 rev / royalty / license", "$4.92 bn / $2.61 bn / $2.31 bn", "Trailing P/E", "~300x"],
    ["ACV / RPO", "$1.73 bn (+13%) / $2.07 bn (-7%)", "Next catalyst", "Q2 FYE27 (Nov 4); Qualcomm trial (Oct 5)"],
    ["Q1 FYE27 revenue", "$1.289 bn (+22% YoY, record)", "DC royalties", "More than doubled YoY"],
]
sd = [[cell(r[0], s_cellB), cell(r[1], s_cell), cell(r[2], s_cellB), cell(r[3], s_cell)] for r in snap]
story.append(styled_table([[cell("Snapshot", s_theadL), cell("", s_thead), cell("", s_thead), cell("", s_thead)]] + sd,
               [38*mm, 42*mm, 42*mm, 48*mm], header_rows=1))
story.append(Spacer(1, 8*mm))
story.append(P("This note is independent research-style analysis for informational purposes only and is not investment advice. "
               "Financial figures from company filings and shareholder letters; market data as of October 2, 2026. "
               "Projections and the price target are the author's estimates.", s_small))
story.append(PageBreak())

# ============ 1. INVESTMENT THESIS ============
story.append(P("1 &nbsp; Investment Thesis", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("We rate Arm <b>SELL</b> with a <b>$48</b> price target, <b>\u221284.3%</b> below the $307.49 quote. "
               "This is not a call on the business, which is wonderful \u2014 98% gross margins, 350 billion chips "
               "shipped, the instruction set inside nearly every smartphone on earth, and now the CPU architecture of "
               "the hyperscalers' custom AI silicon. It is a call on the price. At $307.49 the market values Arm at "
               "roughly <b>52\u00d7 forward sales</b> and ~300\u00d7 trailing earnings. Our 10-year scenario DCF \u2014 "
               "bear $17.12 / base $46.34 / bull $82.73, weighted 25/50/25 \u2014 says even the <b>bull case sits 73% "
               "below the quote</b>. Reverse-engineering the price: it demands roughly <b>$290 billion of FYE36 "
               "revenue</b>, about twelve times management's own $25 billion FYE31 bull plan and nearly sixty times "
               "this year's revenue. No plausible operating outcome bridges that gap.", s_body))
story.append(P("The temptation is to grant Arm a hypergrowth pass: AI is real, data-center royalties more than doubled "
               "last quarter, and the new AGI CPU chip \u2014 co-developed with Meta \u2014 has demand exceeding "
               "supply. We tested that temptation against the demand evidence and it fails, for a structural reason: "
               "<b>Arm is an IP licensor, not a shovel-seller.</b> Royalty revenue is earned when <i>customers</i> "
               "ship chips; there is no contracted chip backlog, no allocation queue, no take-or-pay volume. Arm's "
               "own remaining performance obligations were <b>$2.07 billion \u2014 about 4.4 months of guided "
               "revenue, down 7% year over year</b> \u2014 and management has stopped reporting the metric, calling it "
               "'less relevant to our growth.' A hypergrowth regime requires verifiable contracted demand covering "
               "well over a year of revenue; Arm has roughly a third of a year, shrinking. So years 1\u20133 are "
               "modeled at scenario growth rates with the usual skepticism, not at guidance: base 16.1% CAGR, bull "
               "20.7% (which already haircuts management's $25B FYE31 plan by cutting its $15B CPU contribution to "
               "$8B). What would falsify this SELL: year-10 revenue tracking at or above $24B with free-cash-flow "
               "margins at or above 34% \u2014 i.e., the company compounding at the top of the bull case for a "
               "decade.", s_body))

story.append(P("Why the business is wonderful", s_h2))
for b in [
    "<b>The royalty flywheel is the best in semiconductors.</b> License fees today become per-unit royalties for the 20-year life of a chip family. Armv9 and Compute Subsystems carry higher royalty rates per chip than v8, so mix \u2014 not just units \u2014 drives royalty growth. Q1 FYE27: royalty revenue +22% to $715M, license +23% to $574M, both quarterly records.",
    "<b>Data center is genuinely inflecting.</b> Data-center royalty revenue more than doubled year over year as Arm Neoverse adoption accelerated across cloud providers. The hyperscalers' custom CPUs \u2014 AWS Graviton, Google Axion, Microsoft Cobalt \u2014 are Arm-based, and Arm's first production silicon, the AGI CPU for agentic-AI data centers co-developed with Meta, carries more than $2B of customer demand across FYE27\u201328 against a $15B long-term forecast.",
    "<b>350 billion chips shipped; the ecosystem moat is unassailable.</b> Cumulative Arm-based shipments passed 350 billion in March 2026. Software toolchains, foundry enablement, and two decades of design wins compound into switching costs no open ISA can replicate quickly.",
    "<b>Fortress balance sheet, 98% gross margins.</b> ~$3.9B of cash and short-term investments, negligible debt, GAAP gross margin 97.9%. Non-GAAP operating margin ~41% even while R&amp;D investment runs +33%.",
]:
    story.append(B(b))
story.append(P("Why the price is the problem", s_h2))
for b in [
    "<b>Every scenario prices below the quote \u2014 including the bull.</b> Bull-case fair value is $82.73, 73% below $307.49. The market is not pricing Arm's fundamentals; it is pricing a scarcity premium on 'AI CPU exposure' with no earnings anchor.",
    "<b>The Qualcomm trial starts tomorrow (October 5, 2026).</b> Qualcomm \u2014 one of Arm's largest royalty payers \u2014 alleges Arm breached its architecture license agreement; Arm disputes it. An adverse outcome threatens both a major royalty stream and the pricing power of the ALA program itself. This binary is unpriced at 300\u00d7 earnings.",
    "<b>RISC-V is a slow bleed, not a sudden death.</b> The open ISA keeps winning sockets at the low end and in China, capping Arm's pricing power exactly where unit growth is fastest.",
    "<b>Smartphone royalties face a cyclical headwind.</b> Higher memory prices are pressuring device sales, and smartphones remain the largest royalty base. The AI narrative has not repealed the handset cycle.",
    "<b>Related-party and ownership overhangs.</b> SoftBank's majority stake, the Arm China structure, and a beta of 3.78 mean this stock falls 3\u20134\u00d7 as fast as the market when AI sentiment wobbles \u2014 as the September Anthropic-essay selloff (down ~40% from the $452.70 high) demonstrated.",
]:
    story.append(B(b))

# ============ 2. BUSINESS ============
story.append(P("2 &nbsp; Company Overview", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Arm Holdings (founded 1990, Cambridge, UK; re-listed on Nasdaq in September 2023; majority-owned by "
               "SoftBank) does not sell chips. It licenses processor IP \u2014 CPU designs, the Arm instruction-set "
               "architecture, and increasingly full Compute Subsystems \u2014 to ~1,000 semiconductor partners, "
               "collecting an upfront license fee and then a per-unit royalty on substantially every chip shipped with "
               "Arm technology inside. Two revenue lines: <b>royalty revenue</b> ($2.613B in FY2026, +22% in Q1 FYE27 "
               "to $715M), driven by chip volumes and the mix shift to higher-rate Armv9/CSS designs; and "
               "<b>license and other revenue</b> ($2.307B in FY2026, +23% in Q1 to $574M), driven by new architecture "
               "licenses and backlog conversion. Annualized contract value \u2014 the normalized run-rate of the "
               "licensing book \u2014 was $1.73B, +13% year over year.", s_body))
story.append(P("Fiscal 2026 (ended March 31, 2026) was a record: $4.92B of revenue, +23% year over year, non-GAAP "
               "diluted EPS of $1.77, non-GAAP free cash flow of $882M. Q1 FYE27 (June quarter, reported July 29, "
               "2026) set another record at $1.289B (+22%), with non-GAAP EPS of $0.45 (+29%, above guidance) and "
               "non-GAAP operating margin near 41%. The strategic pivot underway is from pure IP to <b>production "
               "silicon</b>: the AGI CPU, Arm's first own chip for cloud AI data centers, co-developed with Meta, "
               "with management citing demand 'much higher than supply' and more than $2B of customer demand across "
               "FYE27\u201328. Two more Compute Subsystem licenses were signed in the quarter for smartphone and "
               "autonomous-driving chips.", s_body))
story.append(P("What Arm is not: it has no fabs, no chip inventory, and no order backlog in the semiconductor sense. "
               "Its 'backlog' is license-contract RPO \u2014 $2.07B at the end of FY2026, down 7% year over year, "
               "which the company has now stopped disclosing quarterly as 'less relevant to our growth.' Royalty "
               "revenue lags the capex cycle by design: hyperscalers commit billions to data centers, NVIDIA and "
               "Broadcom ship accelerators, and Arm collects its few-dollars-per-socket royalty when the custom CPUs "
               "beside them ship. Leverage to the AI buildout is real but derivative and lagged.", s_body))

# ============ 3. COMPETITION ============
story.append(P("3 &nbsp; Competition", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("The x86 duopoly (Intel, AMD) still owns the data-center CPU socket Arm is attacking \u2014 Neoverse's "
               "share gains are real but start from a small base, and both incumbents are counter-attacking with "
               "custom-silicon programs of their own. <b>RISC-V</b> is the structural threat: royalty-free, gaining "
               "in embedded, IoT, and Chinese SoCs, and improving at the high end; every RISC-V socket is a socket "
               "Arm never gets to tax. In AI accelerators Arm is a complement, not a competitor, to NVIDIA \u2014 but "
               "that complementarity is precisely what makes Arm's AI revenue hostage to someone else's cycle. The "
               "nearest-term contest is legal, not technical: the <b>Qualcomm</b> architecture-license dispute, going "
               "to trial October 5, 2026, over whether Qualcomm's Nuvia-derived CPUs breach its ALA. Qualcomm is both "
               "a top royalty payer and the proof-point for Arm's high-end pricing; a loss impairs both. Moat "
               "assessment: wide in mobile/embedded (ecosystem, toolchains, 350B-unit installed base), narrowing at "
               "the edges where RISC-V and in-house ISAs compete \u2014 which is exactly where the marginal unit "
               "growth lives.", s_body))

# ============ 4. VALUATION ============
story.append(P("4 &nbsp; Valuation \u2014 10-Year Scenario DCF, Fair Value $48", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Ten-year explicit free-cash-flow DCF, weights bear 25% / base 50% / bull 25%. The discount structure "
               "is priced for the risk: <b>base 12.0%</b> (beta 3.78, the Qualcomm litigation binary, RISC-V "
               "encroachment, SoftBank/Arm-China related parties), <b>bear 14.5%</b> (base + 250bp), <b>bull "
               "10.5%</b> (base \u2212 150bp). Terminal growth is capped at <b>1.0% / 2.0% / 2.5%</b> on year-10 "
               "free cash flow at normalized margins \u2014 never peak margins. Equity = firm EV plus $3.9B of net "
               "cash, over ~1.03B diluted ADS. Crucially, the model grants <b>no hypergrowth exemption</b>: the "
               "demand evidence (Section 1) does not support it, so years 1\u20133 grow at scenario rates with full "
               "skepticism, and the bull case already haircuts management's $25B FYE31 plan (its $15B CPU "
               "contribution cut to $8B).", s_body))
story.append(Spacer(1, 3*mm))
story.append(P("Scenario DCF (10-year FCFF, FY2027E revenue base $5.6B):", s_h2))
dcf = [
    [cell("Scenario", s_theadL), cell("Rev CAGR", s_thead), cell("FCF margin (yr-1\u2192yr-10)", s_thead), cell("Discount / term. g", s_thead), cell("Fair value", s_thead)],
    [cell("Bear", s_cellB), cell("+5.3%", s_cellC), cell("25.2% \u2192 25.2%", s_cellR), cell("14.5% / 1.0%", s_cellR), cell("$17.12", s_cellBR)],
    [cell("Base", s_cellB), cell("+16.1%", s_cellC), cell("25.5% \u2192 30.0%", s_cellR), cell("12.0% / 2.0%", s_cellR), cell("$46.34", s_cellBR)],
    [cell("Bull", s_cellB), cell("+20.7%", s_cellC), cell("26.5% \u2192 31.0%", s_cellR), cell("10.5% / 2.5%", s_cellR), cell("$82.73", s_cellBR)],
    [cell("Probability-weighted (25/50/25) \u2192 <b>$48 target</b>", s_cellB), cell("", s_cellC), cell("", s_cellR), cell("", s_cellR), cell("", s_cellR), cell("$48", s_cellBR)],
]
story.append(styled_table(dcf, [62*mm, 20*mm, 36*mm, 30*mm, 22*mm]))

d2 = Drawing(430, 185)
d2.add(String(215, 173, "Scenario fair values vs. current price ($)", fontName="Helvetica-Bold", fontSize=10, textAnchor="middle", fillColor=NAVY))
bc2 = VerticalBarChart(); bc2.x = 45; bc2.y = 30; bc2.height = 115; bc2.width = 340
bc2.data = [[17, 46, 83, 48, 307]]
bc2.strokeColor = None; bc2.barLabels.nudge = 8; bc2.barLabelFormat = "%d"
bc2.bars[0].fillColor = ACCENT
bc2.categoryAxis.categoryNames = ["Bear", "Base", "Bull", "Wtd. avg", "Price"]
bc2.valueAxis.valueMin = 0; bc2.valueAxis.valueMax = 340; bc2.valueAxis.valueStep = 85
bc2.valueAxis.labels.fontSize = 7; bc2.categoryAxis.labels.fontSize = 8
d2.add(bc2)
story.append(d2)

story.append(P("The chart is the whole argument: the current price is off the scale of every scenario. In the bear "
               "case \u2014 handset softness, RISC-V share loss, an adverse Qualcomm outcome \u2014 revenue compounds "
               "5.3% to $9.4B and the equity is worth <b>$17.12</b>; the bear sits 94% below the quote, as the rules "
               "require a bear that hurts. In the base case \u2014 Neoverse/CSS mix drives 16.1% compounding to "
               "$24.9B of FYE36 revenue at 30% FCF margins \u2014 fair value is <b>$46.34</b>. In the bull case "
               "\u2014 20.7% compounding to $36.8B, AGI CPU ramping to plan \u2014 <b>$82.73</b>. Terminal value is "
               "56% of base-case EV (no haircut required). The weighted $48.13 rounds to the <b>$48 target</b>, "
               "\u221284.3% against $307.49.", s_body))
story.append(P("Cross-checks confirm the direction. Reverse DCF: justifying $307.49 at a 12% discount requires roughly "
               "<b>$290B of FYE36 revenue</b> \u2014 about 52\u00d7 FY2027E revenue, growing at ~49% a year for a "
               "decade, a pace no IP licensor has ever sustained. Multiples: ~52\u00d7 forward sales and ~300\u00d7 "
               "trailing earnings price Arm as if royalties were software subscriptions; they are cyclical, "
               "per-unit, and hostage to other companies' shipment volumes. <b>What would falsify the SELL:</b> "
               "FYE36 revenue tracking at or above $24B with FCF margins at or above 34% \u2014 sustained top-of-bull "
               "execution for a decade \u2014 or a decisive Qualcomm victory that reprices ALA royalty rates "
               "structurally upward.", s_body))

story.append(P("5 &nbsp; Key Risks", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
for b in [
    "<b>Qualcomm litigation (trial begins October 5, 2026).</b> An adverse ruling could impair a top royalty stream and reset ALA pricing power downward; a favorable one is the clearest near-term upside catalyst and the main risk to this SELL.",
    "<b>RISC-V encroachment.</b> Royalty-free ISAs keep winning embedded, IoT, and China sockets \u2014 the highest-unit-growth segments \u2014 pressuring Arm's take rate over time.",
    "<b>Handset cycle.</b> Smartphones remain the largest royalty base; elevated memory prices are pressuring device volumes and near-term royalty growth.",
    "<b>AI-sentiment beta.</b> At beta 3.78 and 300\u00d7 earnings, any wobble in AI capex sentiment reprices the stock violently \u2014 the September drawdown from $452.70 showed the mechanism.",
    "<b>SoftBank overhang / Arm China.</b> Majority ownership and the related-party China structure remain governance discounts the market applies intermittently.",
    "<b>Production-silicon execution.</b> The AGI CPU moves Arm from licensing IP to competing with its own customers' chip programs; 'demand exceeding supply' must convert to shipped, royalty-bearing volume.",
]:
    story.append(B(b))

story.append(P("Recommendation", s_h2))
story.append(P("<b>SELL, $48 target (\u221284.3%), High risk.</b> Arm is a wonderful business and a terrible stock at "
               "$307.49. The AI story is real \u2014 data-center royalties doubled, the AGI CPU is supply-constrained, "
               "Neoverse is inside the hyperscalers' custom silicon \u2014 but none of it is contracted, and the "
               "price demands a decade of 49% annual revenue growth that no IP licensor has ever delivered. Bear "
               "$17.12 / base $46.34 / bull $82.73, weighted to $48 against a $307.49 quote; even the bull case is "
               "73% underwater. The Qualcomm trial starting October 5 is a live binary that could change the "
               "royalty-rate outlook in either direction \u2014 until it resolves, there is no reason to pay 52\u00d7 "
               "sales for a cyclical royalty stream. <b>Do not own this above $100;</b> revisit only on a decisive "
               "litigation win or a derating toward the base case. <b>Falsification:</b> FYE36 revenue tracking "
               "\u2265$24B with FCF margins \u226534%, or structural ALA repricing from the Qualcomm outcome, voids "
               "the SELL.", s_body))
story.append(Spacer(1, 6*mm))
story.append(P("Methodology &amp; sources. Valuation as of October 4, 2026; share price $307.49 (10/2/26 close). Model: 10-year "
               "scenario FCFF DCF off FY2027E revenue of $5.6B, weights bear 25% / base 50% / bull 25%; discounts base "
               "12.0% / bear 14.5% / bull 10.5%; terminal growth 2.0% / 1.0% / 2.5% on year-10 FCF at normalized "
               "margins (25\u201331% glide, below the 41% non-GAAP operating margin peak). Net cash $3.9B (June 30, "
               "2026); ~1.03B diluted ADS. The bear case meets the hurt conditions and sits 94% below the current "
               "price. Terminal value is 56% of base-case EV (no haircut required). Demand-regime check: RPO $2.07B "
               "(~4.4 months of guided revenue, \u22127% YoY, disclosure discontinued); no allocation/lead-time "
               "mechanism in IP licensing; no take-or-pay volume commitments; hyperscaler capex commits to data "
               "centers/accelerators with Arm's royalty a lagging derivative \u2014 hypergrowth-regime assumptions "
               "not granted. Financials from FY2026 20-F and Q1 FYE27 shareholder letter/investor presentation "
               "(July 29, 2026); litigation status from Qualcomm Inc. Form 10-K (trial scheduled October 5, 2026); "
               "market data via Yahoo Finance/Finnhub. This note is research analysis for informational purposes and "
               "is not personalized investment advice. Equity investing involves risk of loss. The author holds no "
               "position in ARM at the time of writing.", s_small))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=18*mm,
                        title="ARM \u2014 Equity Research Note", author="Muse")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("wrote", OUT)
