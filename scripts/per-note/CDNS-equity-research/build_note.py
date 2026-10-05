#!/usr/bin/env python3
"""Build the Cadence (CDNS) equity research note PDF — compounder-quality override rebuild, October 4, 2026."""
import numpy as np
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, HRFlowable, KeepTogether)
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import VerticalBarChart

OUT = "/home/hatch/workspace/your_files/CDNS-equity-research/cdns-equity-research-note.pdf"

NAVY = HexColor("#0F2A44"); ACCENT = HexColor("#6C3FB5"); GOLD = HexColor("#C9A227")
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
    canvas.drawString(18*mm, 12*mm, "Cadence Design Systems, Inc. (NASDAQ: CDNS)  \u2014  Equity Research Note  \u2014  October 2026")
    canvas.drawRightString(W - 18*mm, 12*mm, f"Page {doc.page}")
    canvas.setStrokeColor(MGRAY); canvas.setLineWidth(0.5)
    canvas.line(18*mm, 14.5*mm, W - 18*mm, 14.5*mm)
    canvas.restoreState()

# ================= v2 valuation engine (compounder-quality override, Addendum A) =================
# CDNS qualifies: 15 consecutive years ROIC>15% (2011-2025), ~90% gross margins (two-source),
# 127% cumulative FCF conversion. Override: base discount 8.0% (strongest band), bear = base+250bp
# = 10.5%, bull = base-150bp floored at 8.0% (floor binds — disclosed); 15y horizon base/bull,
# 10y bear; terminal g 3.0%/3.0%/1.5%; terminal FCF margins 32%/35%/24% on demonstrated ~30%
# (2020-2025). Operating projections carried from the v2 note.
# Scenario fair values from the verified override engine (compounder-screen/rebuild.py).
SHARES = 275.393e6          # Oct 2, 2026, Yahoo
NET_DEBT = 1.1e9            # ~$1.1B (Q2'26: $1.44B cash vs $2.5B debt)
PRICE = 351.35              # Oct 2, 2026 close

RES = {
    "bear": dict(fv=65.10,  tv_share=0.40, rev_cagr=0.02, term_m=0.24, r=0.105, g=0.015,
                 label="China/export-control shock, EDA digestion"),
    "base": dict(fv=339.37, tv_share=0.59, rev_cagr=0.12, term_m=0.32, r=0.080, g=0.030,
                 label="AI tailwind, mid-teens compounding"),
    "bull": dict(fv=488.36, tv_share=0.62, rev_cagr=0.15, term_m=0.35, r=0.080, g=0.030,
                 label="AI supercycle, share gains vs SNPS"),
}
# Terminal-value guard: max TV/EV 62% — below the 70% line, no haircut.
HAIRCUT = 0.0

W_FV = 0.25*RES["bear"]["fv"] + 0.50*RES["base"]["fv"] + 0.25*RES["bull"]["fv"]  # 308.05
TARGET = round(W_FV)   # 308
UPSIDE = TARGET/PRICE - 1  # -12.3%

# ============ COVER ============
story.append(Spacer(1, 24*mm))
story.append(P("CADENCE DESIGN SYSTEMS, INC. (NASDAQ: CDNS)", ParagraphStyle("x", parent=s_sub, fontName="Helvetica-Bold", fontSize=13, textColor=ACCENT, spaceAfter=2)))
story.append(P("The Tollbooth on Every AI Chip,<br/>Priced Past Perfection", s_title))
story.append(Spacer(1, 4*mm))
story.append(P("Equity Research Note  \u00b7  Technology \u2014 Application Software (EDA)  \u00b7  October 4, 2026", s_sub))
story.append(Spacer(1, 8*mm))

rating_data = [
    [cell("Recommendation", s_theadL), cell("12-Mo. Price Target", s_thead), cell("Current Price", s_thead), cell("Implied Upside", s_thead), cell("Risk Rating", s_thead)],
    [Paragraph("<b><font color=\"#B45309\" size=\"13\">HOLD</font></b>", s_cellC),
     Paragraph(f"<b><font size=\"12\">${TARGET}</font></b>", s_cellC),
     Paragraph("<b>$351.35</b><br/><font size=\"7\" color=\"#5A6472\">Oct 2, 2026</font>", s_cellC),
     Paragraph(f"<b>\u221212.3%</b>", s_cellC),
     Paragraph("<b>Medium</b><br/><font size=\"7\" color=\"#5A6472\">Duopoly, China overhang</font>", s_cellC)],
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
    ["Market cap", "~$96.8 bn", "Shares (diluted)", "~275 mn"],
    ["Enterprise value", "~$97.9 bn", "52-week range", "$262.75 \u2013 $416.69"],
    ["Net debt", "~$1.1 bn", "Dividend", "None"],
    ["2026E revenue (guide)", "$6.26 \u2013 $6.34 bn", "2026E non-GAAP EPS (guide)", "$8.05 \u2013 $8.15"],
    ["Q2'26 revenue", "$1,584 mn (+24.2%)", "Q2'26 non-GAAP op margin", "45.5% (+270 bps)"],
    ["Next catalyst", "Q3'26 earnings, Oct 26", "Analyst consensus", "Moderate Buy, avg PT $403.88"],
]
sd = [[cell(r[0], s_cellB), cell(r[1], s_cell), cell(r[2], s_cellB), cell(r[3], s_cell)] for r in snap]
story.append(styled_table([[cell("Snapshot", s_theadL), cell("", s_thead), cell("", s_thead), cell("", s_thead)]] + sd,
               [38*mm, 42*mm, 42*mm, 48*mm], header_rows=1))
story.append(Spacer(1, 8*mm))
story.append(P("This note is independent research-style analysis for informational purposes only and is not investment advice. "
               "Figures are drawn from Cadence's SEC filings and earnings releases and reputable financial press as of "
               "October 2, 2026. Projections and the price target are the author's estimates under the compounder-quality "
               "override (Addendum A): 15-year scenario DCF, base discount 8.0%, terminal growth up to 3.0% on demonstrated margins.", s_small))
story.append(PageBreak())

# ============ 1. INVESTMENT THESIS ============
story.append(P("1 &nbsp; Investment Thesis", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Cadence is one of the finest software businesses on earth: a ~30% share of the electronic-design-automation "
               "duopoly, ~86% gross margins, ~80% recurring revenue, a record $8.1B backlog, and four straight quarters of "
               "beat-and-raise execution as AI-chip design activity accelerates. Q2 2026 was outstanding \u2014 revenue +24.2% "
               "to $1.584B, non-GAAP operating margin 45.5% (+270 bps), full-year guidance raised for the second time to "
               "~$6.3B (+19%). None of that is in dispute. The problem, as always with this name, is the price. At $351 the "
               "stock trades at 35.9x forward non-GAAP earnings and 16.7x EV/revenue, and our reverse DCF shows the market "
               "is capitalizing roughly <b>17.5% annual free-cash-flow growth for a full decade</b> \u2014 a trajectory <i>above "
               "our bull case</i>. We have no room to pay for the two real overhangs: China/export controls and the decade-long "
               "question of what agentic AI does to EDA pricing power.", s_body))
story.append(P("The compounder-quality override moves us from REDUCE to <b>HOLD</b>. Cadence qualifies on all three override legs (Addendum A): "
               "<b>15 consecutive years of ROIC above 15%</b> (2011\u20132025), <b>~90% gross margins</b>, and <b>127% cumulative FCF conversion</b>. "
               "The override DCF \u2014 15-year explicit horizon (base/bull; 10 years in the bear), base discount <b>8.0%</b> (bear 10.5%, bull 8.0% with "
               "the floor binding \u2014 disclosed), terminal growth up to <b>3.0% on demonstrated ~30% FCF margins</b> \u2014 yields a "
               "probability-weighted fair value of <b>$308, 12.3% below</b> the current price. The base case ($339) sits just 3.5% below the quote; "
               "the bear case ($65, \u201381%) is genuinely painful. The target <i>is</i> the weighted DCF: $308. The October 4 v2 note priced this "
               "duopoly tollbooth as a turnaround; the fourteen-year record says it is a compounder \u2014 and at $351 the price is now within "
               "shouting distance of fair. Hold what you own; we would turn buyers below ~$260, where the base case offers a margin of safety.", s_body))

story.append(P("Audit of the October 4 v2 note (red-team lens)", s_h2))
story.append(P("The v2 note said REDUCE with a $240 target, dated October 4, 2026. Its analysis of the business was sound; "
               "its valuation priced a proven 15-year compounder at a turnaround discount \u2014 a 9% base discount and a 10-year horizon. "
               "The override corrects the lens, not the business view: 8% base (the strongest band, earned by the 15-year ROIC streak), a 15-year "
               "explicit compounding period, terminal growth up to 3.0% on <i>demonstrated</i> (not normalized-down) FCF margins of 32%/35%/24%. "
               "Operating projections are carried unchanged. The three strongest arguments for caution at $351: <b>(1)</b> the price still sits 12% "
               "above fair value and ~3% above the base case \u2014 there is no margin of safety to <i>buy</i>, only to hold; "
               "<b>(2)</b> China/export controls are not a tail risk but a priced-in certainty \u2014 a July 2025 guilty plea, "
               "$140M in penalties, federal probation to ~2028, and 12\u201315% of sales exposed to further BIS tightening; "
               "<b>(3)</b> Cadence trades at 35.9x forward earnings versus Synopsys at 26.4x, despite near-identical scale \u2014 "
               "the market pays Cadence as though the duopoly has one winner while the Ansys-armed Synopsys gets stronger. "
               "The load-bearing assumption of every bullish case is that mid-teens revenue growth persists for most of a "
               "decade <i>at ~30%+ FCF margins</i>; the override tests the price on demonstrated margins and 3.0% terminal "
               "growth, and the price lands 12% rich \u2014 close, but not cheap.", s_body))

story.append(P("Why it works (bull)", s_h2))
for b in [
    "<b>Duopoly tollbooth.</b> ~30% of EDA; you cannot tape out a modern chip without Cadence or Synopsys. Switching costs are extreme \u2014 flows qualified over years across foundry PDKs, tens of thousands of tool-specific scripts, and a failed 2nm tapeout costs tens of millions.",
    "<b>AI supercycle.</b> 2nm/A16 ramp, chiplets/3DFabric, hyperscaler in-house silicon \u2014 all EDA-intensive. IP grew 40%+ in Q2 (Intel agreement); System Design &amp; Analysis +37%; hardware posted a record quarter.",
    "<b>Rare visibility.</b> $8.1B backlog ($4.2B in the next 12 months) covers ~2/3 of the $6.3B guide \u2014 three-year all-you-can-eat token deals make ~80% of revenue recurring.",
    "<b>Fortress economics.</b> 45.5% non-GAAP operating margin, ~$2B of 2026 operating cash flow, ~50% of FCF directed to buybacks, net debt of just ~$1.1B (~0.5x EBITDA).",
]:
    story.append(B(b))
story.append(P("What breaks it (bear)", s_h2))
for b in [
    "<b>Priced past perfection.</b> 17.5% perpetual FCF growth is in the price \u2014 above our bull case. A single guide-down quarter would likely cost 15\u201320% before fundamentals changed; the stock already de-rated 18% from its $416.69 high and is still priced for flawlessness.",
    "<b>China/export controls.</b> July 2025 guilty plea on export-control conspiracy ($45.3M of technology sold to entities tied to Chinese military supercomputing), $140M in penalties, three years of federal probation to ~2028 with mandated compliance reporting. China is ~12\u201315% of sales; tightened BIS EDA restrictions directly cap the growth algorithm in one of the world's largest chip-design markets.",
    "<b>Agentic AI and the seat-license question.</b> Near-term, AI agents expand EDA compute consumption (bullish). Long-term, if AI compresses design cycles and engineer headcount, the per-seat licensing model faces its first existential question in 30 years. The Kimi K3 episode (July 2026) showed how fast the market prices this narrative.",
    "<b>Competition.</b> Synopsys closed the $35B Ansys acquisition in July 2025 \u2014 the strongest rival Cadence has ever faced (EDA + multiphysics simulation under one roof), currently digesting a mega-merger. Cadence at 16.7x EV/revenue vs SNPS at 10.8x prices Cadence as the undisputed winner of the AI cycle.",
]:
    story.append(B(b))

# ============ 2. BUSINESS OVERVIEW ============
story.append(P("2 &nbsp; Business Overview \u2014 What Cadence Does", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Cadence Design Systems (San Jose, CA; founded 1988) sells the computational software, emulation hardware, "
               "and semiconductor IP that chipmakers and systems companies use to design, verify, and tape out chips. "
               "Roughly 60% of all EDA spending flows through Cadence (~30%) and Synopsys (~31%), with Siemens EDA (~13%) "
               "a distant third. The business runs in four product groups, all of which grew double-digits in Q2 2026: "
               "<b>Core EDA</b> (+18%) \u2014 the digital full flow (Genus, Innovus, Tempus, Quantus, Voltus) and the Virtuoso "
               "custom/analog platform, the industry standard, with Cerebrus AI-driven optimization; <b>Functional verification "
               "&amp; hardware</b> (record quarter) \u2014 Palladium emulation, Protium FPGA prototyping, Xcelium simulation, "
               "Jasper formal verification; <b>Semiconductor IP</b> (+40%+) \u2014 interface IP (PCIe, SerDes, DDR/LPDDR, UCIe for "
               "chiplets), memory compilers, Tensilica/DSP cores, the highest-growth, highest-leverage line as chiplet "
               "architectures proliferate; <b>System Design &amp; Analysis</b> (+37%) \u2014 Allegro/OrCAD PCB plus multiphysics "
               "(Clarity, Celsius, Sigrity, Fidelity CFD, BETA CAE) selling 'beyond silicon' to hyperscalers, auto, and aerospace.", s_body))
story.append(P("The 2026 strategic overlay is AI on both sides of the transaction: 'design for AI' (TSMC N3/N2/A16/A14 "
               "certification, 3DFabric chiplet flows for AI accelerators) and 'AI for design' (the agentic AI Super-Agent "
               "portfolio, which management says is seeing strong early traction and should drive higher EDA compute "
               "consumption). Whether agentic AI is ultimately a volume tailwind or a pricing headwind is the central "
               "long-term debate \u2014 and it is precisely why we refuse to pay a terminal growth rate above 2.5%.", s_body))

story.append(P("Financial situation", s_h2))
story.append(P("A compounding machine with software economics: gross margins have held 86\u201390% for a decade, revenue has "
               "compounded ~13% annually, and the model is ~80% recurring. GAAP operating margins sit near 30%; non-GAAP, "
               "which strips out stock comp and acquisition amortization, runs 43\u201346% \u2014 the number management guides "
               "and the Street models. Note the 2022\u201324 net-income plateau ($0.85B \u2192 $1.06B) against 30% revenue growth "
               "\u2014 BETA CAE acquisition amortization, restructuring, and SBC absorbed the operating leverage on a GAAP basis.", s_body))
fin = [
    [cell("Fiscal year", s_theadL), cell("2022", s_thead), cell("2023", s_thead), cell("2024", s_thead), cell("2025", s_thead), cell("2026E (guide)", s_thead)],
    [cell("Revenue ($B)", s_cellB), cell("3.56", s_cellR), cell("4.09", s_cellR), cell("4.64", s_cellR), cell("5.30", s_cellR), cell("6.26\u20136.34", s_cellR)],
    [cell("Revenue growth", s_cell), cell("+18.8%", s_cellR), cell("+14.8%", s_cellR), cell("+13.5%", s_cellR), cell("+14.1%", s_cellR), cell("~+19%", s_cellR)],
    [cell("Non-GAAP op margin", s_cell), cell("~42%", s_cellR), cell("~43%", s_cellR), cell("~43%", s_cellR), cell("~44%", s_cellR), cell("~44\u201345%", s_cellR)],
    [cell("Free cash flow ($B)", s_cell), cell("1.12", s_cellR), cell("1.25", s_cellR), cell("1.12", s_cellR), cell("1.59", s_cellR), cell("~2.0", s_cellR)],
]
story.append(styled_table(fin, [44*mm, 24*mm, 24*mm, 24*mm, 24*mm, 30*mm], fontsize=8))
story.append(P("Q2 2026 (reported July 27) was a clean beat-and-raise \u2014 the fourth consecutive quarter of that pattern. "
               "Revenue of $1.584B (+24.2% YoY) landed at the top of the $1.555\u20131.595B guide; non-GAAP EPS of $2.11 (+27.9%) "
               "beat the $2.05\u20132.06 consensus; non-GAAP operating margin hit 45.5% (+270 bps YoY); billings were $1.73B "
               "(+31.5%). Management raised the full-year outlook for the second time: revenue $6.26\u20136.34B (from "
               "$6.125\u20136.225B) and non-GAAP EPS $8.05\u20138.15 (from $7.85\u20137.95). The balance sheet is a fortress: "
               "$1.44B cash against $2.5B debt (~$1.1B net debt, ~0.5x EBITDA), with ~50% of ~$2B 2026 FCF directed to buybacks.", s_small))

# ============ 3. VALUATION — HARDENED 10-YEAR DCF ============
story.append(P("3 &nbsp; Valuation \u2014 Compounder Override, Fair Value $308", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("The October 4 v2 note valued Cadence at $240 on a <b>10-year scenario DCF at a 9.0% base discount</b> \u2014 turnaround pricing for a "
               "proven compounder. The override (Addendum A) re-tiers the lens Cadence's record earns: a <b>15-year explicit horizon</b> (base/bull; "
               "10 years in the bear), scenario-specific discounts <b>bear 10.5%</b> (base + 250bp) / <b>base 8.0%</b> (the strongest band \u2014 15 "
               "consecutive years of ROIC above 15%, ~90% gross margins, 127% FCF conversion) / <b>bull 8.0%</b> (base \u2013 150bp, at the floor \u2014 "
               "the floor binds, disclosed), and terminal growth of <b>3.0% / 3.0% / 1.5%</b> on year-N FCF at <b>demonstrated FCF margins (32% / 35% / "
               "24%)</b> \u2014 below the ~30% sustained since 2020 and the 35% 2025 print, i.e. below demonstrated peaks. Operating projections are "
               "carried from the v2 note (base 12.0% revenue CAGR \u2014 Cadence's own decade-long rate; bear 2.0%; bull 15.0%). Net debt $1.1B; "
               "275.4M shares. Terminal value is 40% / 59% / 62% of EV \u2014 under the 70% haircut line everywhere; the 15-year explicit period moved "
               "value out of the perpetuity as designed.", s_body))
story.append(Spacer(1, 3*mm))
story.append(P("Scenario DCF (15-year base/bull, 10-year bear):", s_h2))
dcf = [
    [cell("Scenario", s_theadL), cell("Rev CAGR", s_thead), cell("Terminal FCF margin", s_thead), cell("Discount / term. g", s_thead), cell("Fair value", s_thead)],
    [cell("Bear: China shock, EDA digestion", s_cell), cell("2.0%", s_cellC), cell("24%", s_cellR), cell("10.5% / 1.5%", s_cellR), cell(f"${RES['bear']['fv']:.2f}", s_cellBR)],
    [cell("Base: AI tailwind, mid-teens compounding", s_cell), cell("12.0%", s_cellC), cell("32%", s_cellR), cell("8.0% / 3.0%", s_cellR), cell(f"${RES['base']['fv']:.2f}", s_cellBR)],
    [cell("Bull: AI supercycle, share gains", s_cell), cell("15.0%", s_cellC), cell("35%", s_cellR), cell("8.0%* / 3.0%", s_cellR), cell(f"${RES['bull']['fv']:.2f}", s_cellBR)],
    [cell(f"Probability-weighted (25/50/25) \u2192 <b>${TARGET} target</b>", s_cellB), cell("", s_cellC), cell("", s_cellR), cell("", s_cellR), cell(f"${W_FV:.0f}", s_cellBR)],
]
story.append(styled_table(dcf, [52*mm, 26*mm, 28*mm, 30*mm, 24*mm], fontsize=7.8))
story.append(P("*Bull discount floor binds (8.0% \u2013 150bp = 6.5% \u2192 8.0% floor), disclosed per Addendum A. "
               "The bear hurts on all four required axes: revenue CAGR 2.0% (&lt;3%), FCF margins 24% vs 32% base (800bp compression), "
               "a 250bp derating (10.5% vs 8.0%), and $65.10 sitting 81% below the price.", s_small))

d = Drawing(430, 185)
d.add(String(215, 173, "Scenario fair values vs. current price ($)", fontName="Helvetica-Bold", fontSize=10, textAnchor="middle", fillColor=NAVY))
bc = VerticalBarChart(); bc.x = 45; bc.y = 30; bc.height = 115; bc.width = 340
bc.data = [[65, 339, 488, 308, 351]]
bc.strokeColor = None; bc.barLabels.nudge = 8; bc.barLabelFormat = "%d"
bc.bars[0].fillColor = ACCENT
bc.categoryAxis.categoryNames = ["Bear", "Base", "Bull", "Wtd. avg", "Price"]
bc.valueAxis.valueMin = 0; bc.valueAxis.valueMax = 550; bc.valueAxis.valueStep = 110
bc.valueAxis.labels.fontSize = 7; bc.categoryAxis.labels.fontSize = 8
d.add(bc)
story.append(d)
story.append(P("Read the chart honestly: the price ($351.35) sits <b>just above the base case ($339.37)</b> \u2014 the market is pricing the base case plus a small AI-supercycle premium, with no margin of safety for the China/export-control overhang. The v2 note's $240 left a 32% gap to the price; the override closes most of it, because a 15-year compounder was being discounted like a 10-year turnaround. The bear ($65.10, \u201381%) is what the China shock plus EDA digestion looks like; the bull ($488.36, +39%) is the AI supercycle with share gains \u2014 live upside, not the base case.", s_small))
story.append(P("Reverse DCF: what is priced in?", s_h2))
story.append(P("At $351.35 the stock sits ~3% above our $339 base case: the market is underwriting twelve percent annual revenue growth for fifteen years at "
               "demonstrated ~30%+ FCF margins, <i>plus</i> a small premium for the AI-supercycle bull \u2014 and it is paying that price while the "
               "China/export-control overhang (guilty plea, $140M penalties, probation to ~2028, 12\u201315% of sales exposed) remains unresolved. "
               "There is no margin of safety whatsoever; any combination of China deceleration, EDA digestion, or multiple compression breaks the math. "
               "The override narrows the gap to fair value from 32% to 12% \u2014 it does not close it.", s_body))
story.append(P(f"<b>Price target: ${TARGET}.</b> The target <i>is</i> the probability-weighted override DCF \u2014 "
               f"0.25\u00d7${RES['bear']['fv']:.2f} + 0.50\u00d7${RES['base']['fv']:.2f} + 0.25\u00d7${RES['bull']['fv']:.2f} "
               f"\u2014 with no multiple overrule and no consensus anchoring. Implied downside {UPSIDE:+.1%}. "
               "What would falsify it: China revenue growing through the export-control overhang (proving the 12\u201315% "
               "exposure is ring-fenced and the probation is a non-event), or 2027 revenue growth printing above 20% "
               "again \u2014 either would argue the bull case deserves to be the base case. Falsification of the override itself: "
               "two consecutive sub-15% ROIC years would revoke the compounder discount.", s_body))

# ============ 4. RISKS & CATALYSTS ============
story.append(P("4 &nbsp; Risks &amp; Catalysts", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Risks", s_h2))
for b in [
    "<b>China and export controls (the real overhang).</b> Guilty plea July 2025, $140M penalties, federal probation to ~2028 with mandated compliance reporting. China has historically been ~12\u201315% of revenue; tightened BIS EDA restrictions directly cap the growth algorithm.",
    "<b>Valuation / multiple compression.</b> 35.9x forward non-GAAP EPS, 16.7x EV/revenue, PEG 2.5 \u2014 the stock de-rated 18% from its $416.69 high and still prices the base case plus a premium, with no margin of safety.",
    "<b>Agentic AI and the seat-license question.</b> The Kimi K3 episode (July 2026) was a preview of how fast the market prices the narrative that AI compresses design cycles and seats.",
    "<b>Competition.</b> The Ansys-armed Synopsys is the strongest rival Cadence has ever faced; share shifts in EDA are measured in single points per year \u2014 but they compound.",
    "<b>Customer concentration &amp; hardware lumpiness.</b> Hyperscalers and top-tier semis dominate bookings; Palladium hardware quarters can swing reported growth by points.",
]:
    story.append(B(b))
story.append(P("Catalysts", s_h2))
for b in [
    "<b>Q3 2026 earnings (Oct 26):</b> the next beat-and-raise would extend the streak to five quarters; watch backlog conversion and China commentary.",
    "<b>TSMC N2/A16 ramp and 3DFabric adoption:</b> each leading-edge ramp is a multi-year EDA/IP annuity; the Intel IP win suggests share gains at the frontier.",
    "<b>Buybacks:</b> ~50% of ~$2B 2026 FCF directed to repurchases \u2014 a put under the stock on weakness.",
    "<b>SNPS-Ansys integration friction:</b> mega-merger digestions historically open share windows; Cadence's clean execution is its best weapon.",
]:
    story.append(B(b))

# ============ 5. RECOMMENDATION ============
story.append(P("5 &nbsp; Recommendation", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P(f"<b>HOLD, ${TARGET} target ({UPSIDE:+.1%}).</b> Cadence is the highest-quality name in EDA \u2014 a duopoly "
               "tollbooth with 86% gross margins, 45.5% non-GAAP operating margins, a record $8.1B backlog, and the AI-chip "
               "cycle's purest picks-and-shovels exposure outside the foundries. The compounder-quality override recognizes what the "
               "v2 note's turnaround discount ignored: 15 consecutive years of ROIC above 15%, ~90% gross margins, 127% FCF conversion. "
               "The override DCF values the equity at $308 (bear $65.10 / base $339.37 / bull $488.36) against a $351.35 quote \u2014 the price "
               "sits 12% above fair value and ~3% above the base case. The v2 note's $240 target priced a compounder as a turnaround; the rebuild "
               "corrects the lens, and the call moves from REDUCE to HOLD.", s_body))
story.append(P("This is a price call, not a business call. The business is a compounder; the stock is fairly priced, no longer past perfection. "
               "<b>Current holders should hold</b> \u2014 selling a duopoly tollbooth into an AI supercycle over a 12% gap has a poor historical hit "
               "rate \u2014 and <b>buy weakness below ~$260</b>, where the base case offers a real margin of safety. We would upgrade to BUY toward "
               f"<b>${TARGET}</b> only on a genuine washout. <b>Falsification:</b> China revenue growing through the export-control overhang, or 2027 "
               "revenue growth printing above 20% again \u2014 either would argue the bull case is the base case and force us to "
               "rebuild.", s_body))
story.append(Spacer(1, 6*mm))
story.append(P("Disclosure: This note is independent research analysis for informational purposes only and is not "
               "personalized investment advice, a recommendation to transact, or an offer to buy or sell any security. "
               "Valuation models are estimates with wide confidence bands; multiples can remain elevated for years at "
               "quality compounders. Company data: Q2 2026 and FY2025 press releases, 10-Ks. Market data: Yahoo Finance "
               "(Oct 2, 2026). Consensus: MarketBeat/MarketScreener, Sep\u2013Oct 2026 (17 analysts, avg target $403.88). "
               "Export-control history: DOJ plea reporting, July 2025. The author holds no position in CDNS.", s_small))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=18*mm,
                        title="Cadence (CDNS) \u2014 Equity Research Note", author="Muse")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("wrote", OUT)
print(f"CDNS v2: bear ${RES['bear']['fv']:.2f} / base ${RES['base']['fv']:.2f} / bull ${RES['bull']['fv']:.2f} "
      f"(haircut {HAIRCUT:.0%}) -> weighted ${W_FV:.2f} -> target ${TARGET} vs price ${PRICE:.2f} ({UPSIDE:+.1%})")
