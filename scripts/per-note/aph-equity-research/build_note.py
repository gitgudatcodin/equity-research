#!/usr/bin/env python3
"""Build the APH (Amphenol Corporation) equity research note PDF - standalone analyst note, Oct 4 2026."""
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

OUT = "/home/hatch/workspace/your_files/aph-equity-research/aph-equity-research-note.pdf"
M = json.load(open("/home/hatch/workspace/your_files/aph-equity-research/valuation_output.json"))
Y = M["yearly"]

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

def ai_rev(k, year):
    for r in Y[k]:
        if r["year"] == year:
            return r["ai"] / 1e3
    return 0.0

story = []
W, H = A4

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7); canvas.setFillColor(DGRAY)
    canvas.drawString(18*mm, 12*mm, "APH (NYSE: APH)  \u2014  Equity Research Note  \u2014  October 2026")
    canvas.drawRightString(W - 18*mm, 12*mm, f"Page {doc.page}")
    canvas.setStrokeColor(MGRAY); canvas.setLineWidth(0.5)
    canvas.line(18*mm, 14.5*mm, W - 18*mm, 14.5*mm)
    canvas.restoreState()

# ============ COVER ============
story.append(Spacer(1, 24*mm))
story.append(P("APH (NYSE: APH)", ParagraphStyle("x", parent=s_sub, fontName="Helvetica-Bold", fontSize=13, textColor=ACCENT, spaceAfter=2)))
story.append(P("The Central Nervous System of AI<br/>On Allocation \u2014 But Priced for Perfection", s_title))
story.append(Spacer(1, 4*mm))
story.append(P("Equity Research Note  \u00b7  Industrials \u2014 Electronic Components  \u00b7  October 4, 2026", s_sub))
story.append(Spacer(1, 8*mm))

rating_data = [
    [cell("Recommendation", s_theadL), cell("12-Mo. Price Target", s_thead), cell("Current Price", s_thead), cell("Implied Upside", s_thead), cell("Risk Rating", s_thead)],
    [Paragraph("<b><font color=\"#C9A227\" size=\"13\">REDUCE</font></b>", s_cellC),
     Paragraph("<b><font size=\"12\">$78</font></b>", s_cellC),
     Paragraph("<b>$86.96</b><br/><font size=\"7\" color=\"#5A6472\">Oct 2, 2026</font>", s_cellC),
     Paragraph("<b><font color=\"#B42318\">-10.3%</font></b>", s_cellC),
     Paragraph("<b>Medium</b><br/><font size=\"7\" color=\"#5A6472\">Net lev. 1.3x</font>", s_cellC)],
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
    ["Market cap", "~$224 bn", "Shares out. (dil.)", "~2.58 bn (post 2:1 split)"],
    ["Enterprise value", "~$238 bn", "52-week range", "$58.67 \u2013 $89.26"],
    ["Net debt / leverage", "$13.4 bn / 1.3x", "Q2 2026 sales", "$8.76 bn (+55%; +30% organic)"],
    ["Q2 orders / book-to-bill", "$10.7 bn (record) / 1.23", "IT datacom share", "43% of sales (+89% YoY)"],
    ["Adj. operating margin", "29.8% (record)", "Q3 2026 guide", "$9.3\u20139.4 bn sales"],
    ["CommScope (closed Jan \u201926)", "$10.5 bn; \u201926 sales ~$4.6 bn", "Next catalyst", "Q3 results (late Oct)"],
]
sd = [[cell(r[0], s_cellB), cell(r[1], s_cell), cell(r[2], s_cellB), cell(r[3], s_cell)] for r in snap]
story.append(styled_table([[cell("Snapshot", s_theadL), cell("", s_thead), cell("", s_thead), cell("", s_thead)]] + sd,
               [38*mm, 42*mm, 42*mm, 48*mm], header_rows=1))
story.append(Spacer(1, 8*mm))
story.append(P("This note is independent research-style analysis for informational purposes only and is not investment advice. "
               "Financial figures from company filings, press releases, and earnings calls; market data as of October 2, 2026. "
               "Projections and the price target are the author's estimates.", s_small))
story.append(PageBreak())

# ============ 1. INVESTMENT THESIS ============
story.append(P("1 &nbsp; Investment Thesis", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("We rate Amphenol <b>REDUCE</b> with a <b>$78</b> price target, <b>\u221210.3%</b> below the $86.96 "
               "quote. This is the trickiest call in our AI-infrastructure coverage, because two true things collide. "
               "First: the AI-interconnect business is <b>genuinely on allocation</b>. Record $10.7B of quarterly "
               "orders against $8.76B of sales (book-to-bill 1.23), fiber lead times stretching to ~50 weeks, and "
               "hyperscalers securing capacity years ahead through long-term agreements \u2014 this is not narrative "
               "demand, it is contracted demand, and it earns aggressive near-term growth assumptions. Second: it is "
               "<b>one slice of a conglomerate</b>, and the market has already priced most of it. Our 10-year "
               "two-slice DCF \u2014 bear $10.36 / base $65.56 / bull $170.70, weighted 25/50/25 \u2014 grants the "
               "AI-datacom slice (43% of sales) full AI-cycle growth while the other 57% compounds at ordinary "
               "industrial rates, and still lands 10% below the quote. The expected return does not compensate for "
               "the left tail: in the bear case the AI cycle breaks in 2028 and the equity is worth $10.", s_body))
story.append(P("The demand-regime test is the analytical core of this note, so we show the work. We grant "
               "AI-cycle growth assumptions only where verifiable demand evidence exists \u2014 contracted backlog, "
               "extended allocation/lead times, customer prepayments or take-or-pay commitments, hyperscaler capex "
               "committing to the supplier's category \u2014 and <b>only to the revenue slice the evidence covers</b>:", s_body))
for b in [
    "<b>Allocation/lead times: confirmed.</b> September 2026 channel checks (Edgewater Research) report connector supply tightening incrementally with lead times extending, and Amphenol/CCS fiber lead times extending to ~50 weeks as hyperscalers secure capacity years ahead. Demand is running ahead of capacity \u2014 orders arrived 23% faster than shipments in Q2.",
    "<b>Take-or-pay-style commitments: confirmed.</b> The same checks report hyperscalers locking capacity years ahead through long-term agreements and purchase orders; management acknowledged long-term non-cancelable customer commitments on the Q2 call (specifics undisclosed by policy).",
    "<b>Hyperscaler capex naming the category: confirmed.</b> NVIDIA has asked Amphenol to license its VR Ultra backplane IP to Foxconn Interconnect and TE Connectivity; Google's TPU9i is expected to adopt cabled backplane with Amphenol as lead designer, driving connector content above $750 per TPU versus $300\u2013350 in TPU7/8. Virtually all of the IT-datacom segment's growth is AI-infrastructure interconnect \u2014 high-speed copper, fiber, and power.",
    "<b>Scope discipline: the evidence covers 43% of sales, not 100%.</b> Industrial, automotive, military/aerospace, mobile, and broadband \u2014 plus the newly acquired CommScope base \u2014 show no such regime. The AI-cycle assumptions stop at the IT-datacom boundary. This apportionment is the difference between analysis and extrapolation.",
]:
    story.append(B(b))
story.append(P("The key judgment call is <b>supercycle duration</b>, and we concentrate all our skepticism there "
               "rather than in the near term:", s_body))
for b in [
    "<b>Bear: the cycle ends in 2027; 2028 is a cliff.</b> AI-datacom revenue falls 20% in 2028 as book-to-bill collapses below 1.0, long-term agreements are renegotiated, and the channel works off a double-ordered inventory glut \u2014 the classic interconnect overbuild pattern. Margins compress to 15% as peak mix reverses. Equity worth $10.36.",
    "<b>Base: the cycle runs through 2030, then fades.</b> The committed hyperscaler AI-capex wave sustains +50%/+35%/+28% AI-slice growth in 2027\u201329, stepping down from 2031 as penetration saturates toward 5% by 2035\u201336. Through-cycle AI margins of 18% \u2014 above the old industrial base, below the 2026 record mix. Equity worth $65.56.",
    "<b>Bull: the cycle runs through 2033.</b> Agentic-AI inference architectures disaggregate across specialized hardware, raising networking intensity per unit of compute and keeping interconnect demand ahead of capacity for most of the decade. Equity worth $170.70.",
]:
    story.append(B(b))
story.append(P("<b>What would falsify the REDUCE:</b> book-to-bill below 1.0 for two consecutive quarters, or fiber/connector "
               "lead times normalizing, revokes the AI-slice assumptions entirely \u2014 fair value falls toward the "
               "bear case and we would downgrade. Conversely, book-to-bill sustained above 1.15 with ~50-week lead "
               "times through 2028 validates the bull duration, and we would revisit to the upside.", s_body))

story.append(P("Why own it anyway", s_h2))
for b in [
    "<b>Best-in-class compounder with AI leverage.</b> Thirty-plus years of acquisition compounding at high-teens returns, now with its largest end market (43% of sales) growing 63% organically. The IT-datacom business is roughly four times its size two years ago.",
    "<b>Architecture-neutral: copper or optical, Amphenol wins.</b> The $10.5B CommScope CCS acquisition (closed January 2026) added the fiber portfolio the company lacked \u2014 whatever the rack's physics, the interconnect spend lands here. Communications Solutions revenue rose 85% to $5.38B in Q2.",
    "<b>Design-win moat in the AI rack.</b> VR Ultra backplane IP licensing at NVIDIA's request and lead-designer status on TPU9i's cabled backplane embed Amphenol in the next two accelerator generations, not just the current one.",
    "<b>Fortress cash generation funds the machine.</b> Q2 operating cash flow of $1.6B (88% of net income), free cash flow $1.2B, $8.4B of total liquidity; the acquisition engine and the dividend both run on internally generated cash.",
]:
    story.append(B(b))

# ============ 2. BUSINESS ============
story.append(P("2 &nbsp; Company Overview", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Amphenol (founded 1932, Wallingford, Connecticut) is the world's largest interconnect manufacturer: "
               "electrical, electronic, and fiber-optic connectors, cable assemblies, sensors, and antennas sold "
               "across IT datacom, industrial, automotive, military/aerospace, mobile devices, and broadband. The "
               "model is decentralized \u2014 ~130 business units run as entrepreneurial P&amp;Ls \u2014 wrapped "
               "around a disciplined acquisition machine that has compounded for decades. Q2 2026 was, by the "
               "company's account, the strongest quarter in its 94-year history: sales of $8.76B (+55% year over "
               "year, +30% organic), adjusted EPS of $1.35 (+67%), and a record 29.8% adjusted operating margin "
               "(+420bp), albeit flattered by an $80M non-recurring tariff recovery (~+0.9pp). Orders of $10.7B "
               "grew 94% year over year.", s_body))
story.append(P("The mix shift is the story. <b>IT datacom is now 43% of sales</b> \u2014 the largest end market \u2014 "
               "after growing 89% year over year (63% organically) in Q2, with AI-related products driving virtually "
               "all of the sequential increase. Customers are buying high-speed copper, fiber-optic, and power "
               "interconnect for AI training and inference clusters; CEO Adam Norwitt calls interconnect 'the "
               "central nervous system of AI,' and the order book agrees. Management guided Q3 2026 to $9.3\u2013"
               "$9.4B of sales and $1.40\u20131.42 of adjusted EPS (pre-split basis). The CommScope CCS business \u2014 "
               "$2.1B of sales and $190M of net income in H1 2026 at a 9.1% net margin versus the group's 20.2% \u2014 "
               "is guided to ~$4.6B of 2026 sales; lifting it toward group margins is the main 2027 earnings lever. "
               "Balance sheet: $18.8B of total debt and $13.4B of net debt at June 30 (net leverage 1.3x on $3B of "
               "quarterly EBITDA), $5.4B of cash and short-term investments. The adjusted effective tax rate was "
               "raised to 27% from 24.5% after $390M of China tax determinations \u2014 a structural, not one-off, "
               "reset. A 2-for-1 stock split took effect September 3, 2026.", s_body))

# ============ 3. COMPETITION ============
story.append(P("3 &nbsp; Competition", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("In high-speed interconnect Amphenol's sparring partners are <b>TE Connectivity</b> (broadline, now "
               "licensing Amphenol's VR Ultra IP at NVIDIA's request \u2014 a telling hierarchy), <b>Molex</b> "
               "(Koch-owned, strong in datacom copper), and <b>Luxshare/FIT</b> on cost. In fiber, the CommScope "
               "acquisition bought a seat at the table with <b>Corning</b>-fed supply chains; hyperscalers now bring "
               "Amphenol a Corning spec and ask it to source equivalents because Corning itself is capacity-constrained "
               "\u2014 scarcity as a moat. The architectural risk is the copper-to-optical migration: co-packaged "
               "optics and photonic interconnect (Lightmatter, Ayar Labs) could eventually strand copper content, but "
               "Amphenol's DesignCon 2026 co-packaged-copper demonstrations (448G-capable) extend copper's runway, "
               "and the CommScope fiber portfolio hedges the transition. No competitor matches the breadth \u2014 "
               "copper, fiber, power, backplane IP \u2014 inside the AI rack. Moat: wide in interconnect design and "
               "manufacturing scale, reinforced by qualification cycles that lock suppliers in for accelerator "
               "generations.", s_body))

# ============ 4. VALUATION ============
story.append(P("4 &nbsp; Valuation \u2014 Two-Slice 10-Year DCF, Fair Value $78", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("The model splits FY2026E revenue ($35.4B) into the <b>AI-datacom slice</b> ($15.2B, 43%) and "
               "<b>everything else</b> ($20.2B, 57%), and values them separately over ten explicit years "
               "(2027\u20132036), weighted bear 25% / base 50% / bull 25%. The AI slice gets AI-cycle growth with "
               "duration/fade assumptions per scenario; the rest compounds at ordinary industrial rates (1% / 4.5% / "
               "6.5%). Free-cash-flow margins are through-cycle, not peak: AI slice 15% / 18% / 19%, rest 9% / "
               "11.5% / 13% \u2014 the blended base margin (~14\u201316%) matches the company's current cash "
               "conversion and sits below the record 29.8% operating-margin mix. Discounts keep the compounder "
               "structure: <b>base 9.0%</b>, <b>bear 11.5%</b> (+250bp), <b>bull 8.0%</b> (\u2212150bp, floor 8%). "
               "Terminal growth 1.5% / 2.5% / 2.5% on through-cycle margins. Equity = firm EV minus $13.4B of net "
               "debt (June 30, 2026), over ~2.58B split-adjusted diluted shares.", s_body))
story.append(Spacer(1, 3*mm))
story.append(P("AI-datacom slice revenue path ($B):", s_h2))
sl = [
    [cell("Scenario", s_theadL), cell("2027", s_thead), cell("2028", s_thead), cell("2029", s_thead), cell("2030", s_thead), cell("2036", s_thead), cell("Supercycle duration", s_thead)],
    [cell("Bear: cliff in 2028", s_cellB), cell(f"${ai_rev('bear',2027):.1f}", s_cellR), cell(f"${ai_rev('bear',2028):.1f}", s_cellR), cell(f"${ai_rev('bear',2029):.1f}", s_cellR), cell(f"${ai_rev('bear',2030):.1f}", s_cellR), cell(f"${ai_rev('bear',2036):.1f}", s_cellR), cell("Ends 2027; \u221220% in 2028", s_cell)],
    [cell("Base: +50/+35/+28%", s_cellB), cell(f"${ai_rev('base',2027):.1f}", s_cellR), cell(f"${ai_rev('base',2028):.1f}", s_cellR), cell(f"${ai_rev('base',2029):.1f}", s_cellR), cell(f"${ai_rev('base',2030):.1f}", s_cellR), cell(f"${ai_rev('base',2036):.1f}", s_cellR), cell("Through 2030; fades 2031\u201336", s_cell)],
    [cell("Bull: +60/+50/+45%", s_cellB), cell(f"${ai_rev('bull',2027):.1f}", s_cellR), cell(f"${ai_rev('bull',2028):.1f}", s_cellR), cell(f"${ai_rev('bull',2029):.1f}", s_cellR), cell(f"${ai_rev('bull',2030):.1f}", s_cellR), cell(f"${ai_rev('bull',2036):.1f}", s_cellR), cell("Through 2033; fades 2034\u201336", s_cell)],
]
story.append(styled_table(sl, [34*mm, 20*mm, 20*mm, 20*mm, 20*mm, 20*mm, 46*mm]))
story.append(Spacer(1, 3*mm))
story.append(P("Scenario fair values:", s_h2))
dcf = [
    [cell("Scenario", s_theadL), cell("Total rev CAGR", s_thead), cell("2036 revenue", s_thead), cell("Discount / term. g", s_thead), cell("Fair value", s_thead)],
    [cell("Bear", s_cellB), cell("+1.2%", s_cellC), cell("$39.7 bn", s_cellR), cell("11.5% / 1.5%", s_cellR), cell("$10.36", s_cellBR)],
    [cell("Base", s_cellB), cell("+11.2%", s_cellC), cell("$102.3 bn", s_cellR), cell("9.0% / 2.5%", s_cellR), cell("$65.56", s_cellBR)],
    [cell("Bull", s_cellB), cell("+19.2%", s_cellC), cell("$205.4 bn", s_cellR), cell("8.0% / 2.5%", s_cellR), cell("$170.70", s_cellBR)],
    [cell("Probability-weighted (25/50/25) \u2192 <b>$78 target</b>", s_cellB), cell("", s_cellC), cell("", s_cellR), cell("", s_cellR), cell("", s_cellR), cell("$78", s_cellBR)],
]
story.append(styled_table(dcf, [52*mm, 24*mm, 28*mm, 30*mm, 24*mm]))

d2 = Drawing(430, 185)
d2.add(String(215, 173, "Scenario fair values vs. current price ($)", fontName="Helvetica-Bold", fontSize=10, textAnchor="middle", fillColor=NAVY))
bc2 = VerticalBarChart(); bc2.x = 45; bc2.y = 30; bc2.height = 115; bc2.width = 340
bc2.data = [[10, 66, 171, 78, 87]]
bc2.strokeColor = None; bc2.barLabels.nudge = 8; bc2.barLabelFormat = "%d"
bc2.bars[0].fillColor = ACCENT
bc2.categoryAxis.categoryNames = ["Bear", "Base", "Bull", "Wtd. avg", "Price"]
bc2.valueAxis.valueMin = 0; bc2.valueAxis.valueMax = 190; bc2.valueAxis.valueStep = 47.5
bc2.valueAxis.labels.fontSize = 7; bc2.categoryAxis.labels.fontSize = 8
d2.add(bc2)
story.append(d2)

story.append(P("What moved the math: the AI slice carries the valuation. In the base case it grows from $15.2B to "
               "$71.1B by 2036 (+50%/+35%/+28% in 2027\u201329, supercycle through 2030, fade to 5% by 2035\u201336) "
               "while the rest compounds at 4.5% \u2014 total revenue CAGR of 11.2% versus the ~23% five-year growth "
               "the market price implies. The base case alone ($65.56) sits 25% below the quote; only the bull case "
               "($170.70, supercycle through 2033 on inference-disaggregation networking intensity) clears it. "
               "Discounted terminal value is 60% of base-case EV \u2014 within discipline, no haircut required \u2014 "
               "and the terminal rests on through-cycle margins, not the 2026 record mix. The weighted $78.05 rounds "
               "to the <b>$78 target</b>, \u221210.3% against $86.96.", s_body))
story.append(P("Cross-checks: 2027E free cash flow of ~$6.5B (base) is a ~2.9% FCF yield on the $224B market cap \u2014 "
               "a rich price for a business whose AI slice can fall 20% in a year if the cycle breaks. Split-adjusted "
               "forward P/E sits in the low-30s, pricing near-bull execution against record order intake. "
               "<b>Duration is the entire debate:</b> every $10 of the $78 target is a judgment about how long "
               "hyperscalers keep buying interconnect faster than Amphenol can build it. Our base says through 2030; "
               "the price says well beyond.", s_body))

story.append(P("5 &nbsp; Key Risks", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
for b in [
    "<b>AI-capex pause (the #1 risk).</b> 43% of sales now rides AI-infrastructure interconnect. Any sustained pause in hyperscaler data-center spend \u2014 or a double-ordering unwind like 2001/2016 \u2014 hits the highest-margin, highest-multiple slice first. The bear case ($10.36) is what that looks like.",
    "<b>Leverage and the tax reset.</b> $18.8B of total debt ($13.4B net) after the CommScope deal; interest expense has more than doubled year over year. The adjusted effective tax rate stepped permanently to 27% from 24.5% after $390M of China tax determinations.",
    "<b>CommScope integration.</b> $2.1B of H1 sales at a 9.1% net margin versus 20.2% for the group; $179M of backlog/inventory step-up amortization flattered the optics. Lifting CCS toward group margins is assumed, not demonstrated.",
    "<b>Copper-to-optical migration.</b> Co-packaged optics and photonic interconnect could strand copper content over time; Amphenol is hedged (CommScope fiber, co-packaged-copper R&amp;D) but not immune.",
    "<b>Buybacks offset dilution rather than reducing it.</b> 2.8M shares repurchased in H1 against 4.4M option exercises in Q2 alone; diluted share count rose 1.3% year over year.",
    "<b>Tariff and working-capital drag.</b> The $80M Q2 tariff recovery was non-recurring; working capital consumed $614M of operating cash flow in Q2 as receivables and inventory grew with the order book.",
]:
    story.append(B(b))

story.append(P("Recommendation", s_h2))
story.append(P("<b>REDUCE, $78 target (\u221210.3%), Medium risk.</b> Amphenol is an elite compounder riding a genuine "
               "allocation cycle \u2014 1.23 book-to-bill, ~50-week fiber lead times, hyperscalers contracting "
               "capacity years ahead \u2014 and the AI-datacom slice earns every point of its +50%/+35%/+28% "
               "near-term growth. But the cycle is the investment now: 43% of sales, a bear-case cliff to $10.36, "
               "and a quote that already discounts a supercycle running well past 2030. Bear $10.36 / base $65.56 / "
               "bull $170.70, weighted to $78 against $86.96. <b>Trim into strength; do not chase.</b> Revisit to "
               "the upside only if book-to-bill holds above 1.15 with extended lead times through 2028 (the bull "
               "duration case); a print below 1.0 for two consecutive quarters, or normalizing lead times, revokes "
               "the AI-slice assumptions and the call becomes a downgrade. <b>Falsification triggers are stated "
               "above and will be applied mechanically.</b>", s_body))
story.append(Spacer(1, 6*mm))
story.append(P("Methodology &amp; sources. Valuation as of October 4, 2026; share price $86.96 (10/2/26 close, "
               "split-adjusted). Model: 10-year two-slice scenario FCFF DCF off FY2026E revenue of $35.36B "
               "(Q1 act $7.60B + Q2 act $8.76B + Q3 guide $9.35B + Q4 est $9.65B), AI-datacom slice 43% / rest 57%, "
               "weights bear 25% / base 50% / bull 25%; discounts base 9.0% / bear 11.5% / bull 8.0%; terminal growth "
               "2.5% / 1.5% / 2.5% on year-10 FCF at through-cycle margins (AI slice 18% base, rest 11.5% base). Net "
               "debt $13.4B (June 30, 2026); ~2.58B diluted shares (post 2:1 split, Sep 3, 2026). AI-cycle growth "
               "assumptions applied only to the AI-exposed slice, on verifiable demand evidence: ~50-week fiber "
               "lead times and extending connector lead times (Edgewater Research channel checks, September 2026), "
               "hyperscaler long-term agreements securing capacity years ahead, record $10.7B quarterly orders at "
               "1.23 book-to-bill, and accelerator design wins (VR Ultra backplane IP; TPU9i cabled backplane lead "
               "designer). The bear case meets the hurt conditions (AI-slice revenue \u221220% in 2028, margin "
               "compression, deep derating) and sits 88% below the current price. Discounted terminal value is 60% "
               "of base-case EV (no haircut required). Financials from Q2 2026 press release, 10-Q balance sheet, "
               "and earnings call (July 29, 2026); market data via Yahoo Finance. This note is research analysis for "
               "informational purposes and is not personalized investment advice. Equity investing involves risk of "
               "loss. The author holds no position in APH at the time of writing.", s_small))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=18*mm,
                        title="APH \u2014 Equity Research Note", author="Muse")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("wrote", OUT)
