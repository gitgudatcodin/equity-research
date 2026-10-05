#!/usr/bin/env python3
"""Build the IBM equity research note PDF — v2 hardened rebuild, October 4, 2026."""
import numpy as np
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, HRFlowable)
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import VerticalBarChart

OUT = "/home/hatch/workspace/your_files/IBM-equity-research/ibm-equity-research-note.pdf"

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
    canvas.drawString(18*mm, 12*mm, "International Business Machines Corp. (NYSE: IBM)  \u2014  Equity Research Note  \u2014  October 2026")
    canvas.drawRightString(W - 18*mm, 12*mm, f"Page {doc.page}")
    canvas.setStrokeColor(MGRAY); canvas.setLineWidth(0.5)
    canvas.line(18*mm, 14.5*mm, W - 18*mm, 14.5*mm)
    canvas.restoreState()

# ================= v2 valuation engine =================
# 10-yr scenario DCF on IBM-reported FCF (excl. financing-receivables swings),
# off the $15.7B 2026E guide. Discount tiers: base 9% (mature compounder),
# bear = base + 250bp, bull = base \u2013 150bp (floor 8%). Terminal growth \u22642.5%
# on year-10 FCF at normalized mid-cycle margins. Growth inputs independently
# justified: base 5%\u21923.2% FCF growth fades toward the company's 2023\u201325 FCF
# trajectory; bear models 1.5% revenue CAGR with FCF margins compressing
# 23%\u219219% (\u2013400bp); bull 6%\u21923.6% assumes Red Hat re-acceleration sticks.
SHARES = 942.134e6          # Oct 2, 2026, Yahoo
NET_DEBT = 53.8e9           # $62.0B debt / $8.2B cash (Q2'26)
PRICE = 222.64              # Oct 2, 2026 close
FCF0 = 15.7e9               # 2026E guided FCF

def cum_path(g):
    v = FCF0; out = []
    for x in g:
        v *= 1 + x; out.append(v)
    return out

G_BASE = [.050, .048, .046, .044, .042, .040, .038, .036, .034, .032]
G_BULL = [.060, .057, .054, .051, .048, .045, .042, .040, .038, .036]
# bear: explicit revenue + margin model (rev0 $70.4B, 1.5% CAGR, margin 23%->19%)
REV0 = 70.4e9
rev_bear = [REV0*1.015**t for t in range(1, 11)]
mg_bear  = [0.23 - (0.23-0.19)*t/10 for t in range(1, 11)]
FCF_BEAR = [r_*m for r_, m in zip(rev_bear, mg_bear)]

SCEN = {
    "bear": dict(fcf=FCF_BEAR,        r=0.115, g=0.010, label="Enterprise stall, Z cycle disappoints"),
    "base": dict(fcf=cum_path(G_BASE), r=0.09,  g=0.025, label="4\u20135% cc growth, steady mix shift"),
    "bull": dict(fcf=cum_path(G_BULL), r=0.08,  g=0.025, label="Red Hat re-accelerates, GenAI converts"),
}

def scen_dcf(s):
    fcf = np.array(s["fcf"], float)
    pv = float(sum(f/(1+s["r"])**(t+1) for t, f in enumerate(fcf)))
    tv = float(fcf[-1]*(1+s["g"])/(s["r"]-s["g"]))
    pv_tv = float(tv/(1+s["r"])**10)
    ev = pv + pv_tv
    return dict(ev=ev, tv_share=pv_tv/ev, fv=(ev-NET_DEBT)/SHARES, fcf10=fcf[-1])

RES = {k: scen_dcf(v) for k, v in SCEN.items()}
W_FV = 0.25*RES["bear"]["fv"] + 0.50*RES["base"]["fv"] + 0.25*RES["bull"]["fv"]
TARGET = round(W_FV)
UPSIDE = TARGET/PRICE - 1

# ============ COVER ============
story.append(Spacer(1, 24*mm))
story.append(P("INTERNATIONAL BUSINESS MACHINES CORP. (NYSE: IBM)", ParagraphStyle("x", parent=s_sub, fontName="Helvetica-Bold", fontSize=13, textColor=ACCENT, spaceAfter=2)))
story.append(P("The Enterprise AI Compounder<br/>at a Fair Price", s_title))
story.append(Spacer(1, 4*mm))
story.append(P("Equity Research Note  \u00b7  Technology \u2014 IT Services / Enterprise Software / Infrastructure  \u00b7  October 4, 2026", s_sub))
story.append(Spacer(1, 8*mm))

rating_data = [
    [cell("Recommendation", s_theadL), cell("12-Mo. Price Target", s_thead), cell("Current Price", s_thead), cell("Implied Upside", s_thead), cell("Risk Rating", s_thead)],
    [Paragraph("<b><font color=\"#1D4ED8\" size=\"13\">HOLD</font></b>", s_cellC),
     Paragraph(f"<b><font size=\"12\">${TARGET}</font></b>", s_cellC),
     Paragraph("<b>$222.64</b><br/><font size=\"7\" color=\"#5A6472\">Oct 2, 2026</font>", s_cellC),
     Paragraph(f"<b>+{UPSIDE:.1%}</b>", s_cellC),
     Paragraph("<b>Medium</b><br/><font size=\"7\" color=\"#5A6472\">Beta ~0.7</font>", s_cellC)],
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
    ["Market cap", "~$209.8 bn", "Shares outstanding", "~942 mn"],
    ["Enterprise value", "~$263.6 bn", "52-week range", "$199.19 \u2013 $332.46"],
    ["Net debt", "~$53.8 bn", "YTD / 1-yr return", "\u201324.5% / \u201321.9%"],
    ["Q2'26 revenue", "$17.16 bn (+1% y/y)", "Q2'26 operating EPS", "$2.93 (+5% y/y)"],
    ["FY2025 revenue / FCF", "$67.5 bn (+8%) / $14.7 bn", "FY2026E FCF (guide)", "~$15.7 bn"],
    ["Dividend", "$1.69/q ($6.76; 3.0% yield)", "Dividend streak", "31 consecutive annual increases"],
    ["ARR", "$24.6 bn (+8% y/y)", "Q3'26 earnings", "October 21, 2026 (AMC)"],
]
sd = [[cell(r[0], s_cellB), cell(r[1], s_cell), cell(r[2], s_cellB), cell(r[3], s_cell)] for r in snap]
story.append(styled_table([[cell("Snapshot", s_theadL), cell("", s_thead), cell("", s_thead), cell("", s_thead)]] + sd,
               [38*mm, 42*mm, 42*mm, 48*mm], header_rows=1))
story.append(Spacer(1, 8*mm))
story.append(P("This note is independent research-style analysis for informational purposes only and is not investment advice. "
               "Figures are drawn from IBM's SEC filings and earnings releases, company IR, and reputable financial press "
               "as of October 2, 2026. Projections and the price target are the author's estimates under a hardened "
               "10-year scenario-DCF methodology.", s_small))
story.append(PageBreak())

# ============ 1. EXECUTIVE SUMMARY ============
story.append(P("1 &nbsp; Executive Summary", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("IBM has finished the strategic pivot it promised in 2020: it is now a software-led, recurring-revenue "
               "enterprise-AI company whose economics no longer resemble the melting-ice-cube narrative the stock price "
               "still implies. Software is ~46% of revenue, ~80% of it recurring, carrying $24.6 bn of ARR growing 8%. "
               "Red Hat \u2014 the $34 bn 2019 acquisition the market once doubted \u2014 is growing 11% and compounding inside "
               "a hybrid-cloud portfolio that also includes HashiCorp (2024) and Confluent ($11 bn, closed 2026). The company "
               "generated $14.7 bn of free cash flow in 2025 and guides ~$15.7 bn for 2026, funding a 3.0%-yielding dividend "
               "with 31 consecutive annual increases and steady deleveraging.", s_body))
story.append(P("Yet the shares trade 33% below their 52-week high ($332.46) and are down 24% year-to-date after a soft Q2 \u2014 "
               "revenue +1% on large-deal timing, and a guidance trim to 4\u20135% constant-currency growth from 'above 5%.' "
               "At $222.64 the stock sells at 17.1\u00d7 forward operating earnings versus its own 19.7\u00d7 historical "
               "average, while the business it describes is higher-quality than the one that earned that average: more "
               "software, more recurring, less cyclical. The prior note read this as a BUY with a $250 target. The hardened "
               "rebuild disagrees \u2014 not because the business story changed, but because the leverage math says the "
               "equity is fairly priced: <b>$53.8B of net debt absorbs more than half of the DCF enterprise value</b>, "
               "leaving a probability-weighted fair value of <b>$223, essentially the current price</b>. HOLD.", s_body))

story.append(P("Audit of the October 2 note (red-team lens)", s_h2))
story.append(P("The prior note said BUY with a $250 target, dated October 2, 2026. Its business analysis was thorough and "
               "its DCF base case ($247) was not far from our own ($241). The flaw was in how the target was set: a "
               "four-lens 'synthesis' that weighted in <b>Street consensus ($254) at 15%</b> alongside peer multiples and "
               "sum-of-the-parts to reach $250. That is consensus anchoring doing the target-setting work \u2014 the hardened "
               "methodology sets the target <i>at</i> the weighted DCF ($223) with no overrule, because a target that leans "
               "on what everyone else thinks is a survey, not a valuation. The three strongest arguments against the old "
               "note's BUY: <b>(1)</b> the equity is a levered stub \u2014 $62B gross debt (~3.3\u00d7 EBITDA) with $2.5B of "
               "annual interest means any FCF forecast miss hits the equity far harder than the enterprise value; "
               "<b>(2)</b> the Q2 slippage is assumed to be timing, but consulting signings were flat and software growth "
               "decelerated to +5% \u2014 if Q3 (Oct 21) shows it is demand, the 4\u20135% growth algorithm breaks; "
               "<b>(3)</b> the old bear case ($155) never asked what a real stall looks like \u2014 ours ($94, \u201358%) does, "
               "and that asymmetry is why a +0.1% upside is a HOLD, not a BUY. The load-bearing assumption of every bullish "
               "case is that $15.7B of 2026E FCF is real and repeatable \u2014 ~23% FCF margins at a mature services company, "
               "growing mid-single digits. Defensible, but fragile given the leverage: the forecast is doing the work that "
               "the balance sheet cannot.", s_body))

story.append(P("Why the market is wrong \u2014 in brief", s_h2))
for b in [
    "<b>The Q2 miss was timing, not demand:</b> management disclosed several large software transactions slipped past quarter-end as clients redirected budget to supply-constrained servers/storage/memory; signings still grew 6% and infrastructure exited with a ~$500m backlog.",
    "<b>The AI disclosure change spooked people unnecessarily:</b> IBM stopped publishing its cumulative GenAI 'book of business' ($12.5bn at Q4'25) in favor of mix metrics \u2014 GenAI is ~half of Consulting signings and &gt;30% of backlog. Less transparent, yes; but bookings are bookings, and they are growing.",
    "<b>The balance sheet is misunderstood:</b> $62bn of gross debt screens scary, but $15.1bn is financing-receivables-backed, FCF covers interest roughly 10\u00d7, and the dividend is 41% of guided FCF \u2014 the payout has survived far worse cycles.",
]:
    story.append(B(b))
story.append(P("What would change our mind", s_h2))
for b in [
    "<b>Q3 (Oct 21) shows the Q2 slippage was not timing</b> \u2014 software growth decelerates toward low-single digits and consulting signings roll over.",
    "<b>Red Hat growth breaks below high-single digits,</b> removing the engine of the software story.",
    "<b>Leverage rises instead of falls,</b> or the dividend payout pushes past ~60% of FCF.",
]:
    story.append(B(b))

# ============ 2. WHAT IBM IS DOING ============
story.append(P("2 &nbsp; What IBM Is Doing: The Hybrid-Cloud-and-AI Thesis", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Under CEO Arvind Krishna (since 2020), IBM executed a deliberate portfolio rotation: spin off the low-margin "
               "managed-infrastructure business (Kyndryl, 2021), divest non-core assets, and concentrate capital on two "
               "compounding arenas \u2014 hybrid cloud software and enterprise AI \u2014 sold and implemented by a global "
               "consulting arm. The M&amp;A checkbook tells the story: Red Hat ($34 bn, 2019), Apptio ($4.6 bn, 2023), "
               "HashiCorp ($6.4 bn, 2024), and Confluent ($11 bn, closed 2026) \u2014 over $55 bn deployed into open, "
               "recurring-revenue software. IBM also launched self-hosted deployment for IBM Bob, its agentic "
               "software-development platform (October 1, 2026) \u2014 on-prem, sovereign-cloud and air-gapped \u2014 a direct "
               "pitch to regulated industries that cannot send code to public AI services.", s_body))
story.append(P("Four segments, Q2 2026 (reported July 22, 2026): <b>Software</b> ($7.76 bn, +5%) \u2014 Red Hat +11%, Data "
               "+19% (watsonx, Confluent), Automation +4%, Transaction Processing \u20138% on deal timing; <b>Consulting</b> "
               "($5.33 bn, flat / +1% cc) \u2014 signings +6% to $5.0 bn, GenAI ~50% of signings, &gt;30% of backlog; "
               "<b>Infrastructure</b> ($3.84 bn, \u20137%) \u2014 IBM Z \u201342% (z17 cycle trough; the program runs at ~130% of "
               "the z16 trajectory), Distributed Infrastructure +37% (Power, Storage) with a ~$500m backlog; "
               "<b>Financing</b> ($0.24 bn, +12%). Two structural facts matter more than any quarter: ~80% of software "
               "revenue is recurring, underpinning $24.6 bn of ARR growing 8% \u2014 the ballast that lets IBM miss a quarter "
               "of license timing without impairing the franchise.", s_body))

story.append(P("Financial situation: a cash machine with a debt overhang", s_h2))
story.append(P("Full-year 2025 was IBM's best operating year of the Krishna era, which makes the 2026 derating a sentiment "
               "story rather than a solvency story \u2014 but the derating has a mathematical core. Revenue: $61.9 bn (2023) "
               "\u2192 $62.8 bn (2024) \u2192 $67.5 bn (2025, +7.6%) \u2192 ~$70.4 bn 2026E (+4.3%). Operating EPS (non-GAAP): "
               "$9.76 \u2192 $10.35 \u2192 $11.59 \u2192 ~$12.32. Free cash flow: $12.1 bn \u2192 $12.7 bn \u2192 $14.7 bn \u2192 "
               "~$15.7 bn guided. Dividend: $6.63 \u2192 $6.68 \u2192 $6.72 \u2192 $6.76 (3.0% yield, 41% of guided FCF \u2014 safe, "
               "with room to grow). Balance sheet (Q2'26): $62.0 bn total debt (incl. $15.1 bn financing-receivables-backed), "
               "$8.2 bn cash \u2192 $53.8 bn net debt, ~3.3\u00d7 trailing adjusted EBITDA. The trajectory is deleveraging \u2014 "
               "FCF covers the $6.4 bn dividend 2.5\u00d7 and leaves ~$9 bn annually for debt paydown \u2014 but the Confluent "
               "$11 bn deal is the reason net debt has not fallen faster. We expect leverage below 3\u00d7 by end-2027 on FCF "
               "alone.", s_body))
story.append(P("The moat, honestly graded: <b>switching costs</b> (wide in pockets \u2014 mainframe migrations cost nine "
               "figures and take years; Red Hat/OpenShift and Terraform embed in enterprise DevOps toolchains); "
               "<b>regulated-industry trust</b> (narrowing but real \u2014 watsonx.governance, self-hosted Bob, sovereign "
               "options win where Microsoft and AWS cannot go); <b>distribution</b> (underrated \u2014 IBM Consulting puts "
               "100k+ practitioners inside client transformation budgets, creating a proprietary channel for software "
               "pull-through). What is NOT a moat: raw AI model capability (Granite trails frontier labs; IBM wisely "
               "rents/partners), public-cloud scale, or consulting differentiation outside AI-led deals. Growth algorithm "
               "(base): Software 6\u20138% + Consulting 2\u20134% + Infrastructure flat-to-up \u2192 4\u20135% constant-currency "
               "revenue growth, with margin expansion from mix shift and the $4.5 bn productivity program.", s_body))

# ============ 3. VALUATION — HARDENED 10-YEAR DCF ============
story.append(P("3 &nbsp; Valuation \u2014 Hardened 10-Year DCF, Fair Value $223", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("The prior note synthesized four lenses and weighted in Street consensus to reach $250. The hardened rebuild "
               "values IBM on a single disciplined lens: a <b>10-year scenario free-cash-flow DCF</b> \u2014 weights bear 25% / "
               "base 50% / bull 25% \u2014 on IBM-reported FCF (the economically correct series, excluding "
               "financing-receivables noise), from the $15.7 bn 2026E guide. Discount rates are scenario-specific: "
               "<b>bear 11.5%</b> (base + 250bp), <b>base 9.0%</b> (mature-compounder tier), <b>bull 8.0%</b> (base \u2013 150bp, "
               "at the floor). Terminal growth is <b>2.5% / 2.5% / 1.0%</b>, applied to year-10 FCF at normalized mid-cycle "
               "margins \u2014 never peak. Growth inputs are independently justified: the base case's 5%\u21923.2% FCF growth "
               "fades toward the company's own 2023\u201325 trajectory (no management guidance taken at face value); the "
               "bear models an enterprise-spending stall with 1.5% revenue CAGR and FCF margins compressing 23%\u219219% "
               "(\u2013400bp).", s_body))
story.append(Spacer(1, 3*mm))
story.append(P("Scenario DCF (10-year, IBM-reported FCF):", s_h2))
dcf = [
    [cell("Scenario", s_theadL), cell("2036 FCF", s_thead), cell("FCF margin path", s_thead), cell("Discount / term. g", s_thead), cell("TV share of EV", s_thead), cell("Fair value", s_thead)],
    [cell("Bear: enterprise stall", s_cell), cell("$15.5 bn", s_cellR), cell("23% \u2192 19%", s_cellR), cell("11.5% / 1.0%", s_cellR), cell(f"{RES['bear']['tv_share']:.0%}", s_cellR), cell(f"${RES['bear']['fv']:.2f}", s_cellBR)],
    [cell("Base: 4\u20135% cc growth", s_cell), cell("$23.5 bn", s_cellR), cell("~23% stable", s_cellR), cell("9.0% / 2.5%", s_cellR), cell(f"{RES['base']['tv_share']:.0%}", s_cellR), cell(f"${RES['base']['fv']:.2f}", s_cellBR)],
    [cell("Bull: Red Hat re-accelerates", s_cell), cell("$24.9 bn", s_cellR), cell("~24% stable", s_cellR), cell("8.0% / 2.5%", s_cellR), cell(f"{RES['bull']['tv_share']:.0%}", s_cellR), cell(f"${RES['bull']['fv']:.2f}", s_cellBR)],
    [cell(f"Probability-weighted (25/50/25) \u2192 <b>${TARGET} target</b>", s_cellB), cell("", s_cellC), cell("", s_cellR), cell("", s_cellR), cell("", s_cellR), cell(f"${W_FV:.0f}", s_cellBR)],
]
story.append(styled_table(dcf, [44*mm, 22*mm, 26*mm, 26*mm, 26*mm, 26*mm], fontsize=7.8))
story.append(P("The bear hurts on all three required axes: revenue CAGR 1.5% (&lt;3%), FCF margins 19% vs ~23% base "
               "(400bp compression), and the 250bp derating (11.5% vs 9.0%). Bear fair value $93.78 is 58% below the price \u2014 "
               "the leverage turns a forecast miss into an equity event. No terminal-value haircut is needed: TV is "
               "35\u201361% of EV across scenarios, under the 70% guardrail. The honest read of this table: the base case "
               "alone ($241.42) offers +8.4% \u2014 a HOLD on its own \u2014 but the bear leg drags the weighted value to "
               "$222.90 because the debt makes the downside disproportionately large. That is the leverage asymmetry the "
               "prior note's synthesis smoothed over.", s_small))

d = Drawing(430, 185)
d.add(String(215, 173, "Scenario fair values vs. current price ($)", fontName="Helvetica-Bold", fontSize=10, textAnchor="middle", fillColor=NAVY))
bc = VerticalBarChart(); bc.x = 45; bc.y = 30; bc.height = 115; bc.width = 340
bc.data = [[94, 241, 315, 223, 223]]
bc.strokeColor = None; bc.barLabels.nudge = 8; bc.barLabelFormat = "%d"
bc.bars[0].fillColor = ACCENT
bc.categoryAxis.categoryNames = ["Bear", "Base", "Bull", "Wtd. avg", "Price"]
bc.valueAxis.valueMin = 0; bc.valueAxis.valueMax = 360; bc.valueAxis.valueStep = 90
bc.valueAxis.labels.fontSize = 7; bc.categoryAxis.labels.fontSize = 8
d.add(bc)
story.append(d)
story.append(P("Reverse DCF: what is priced in?", s_h2))
story.append(P("At $222.64, enterprise value is ~$263.6B. Holding a 9% discount rate and 2.5% terminal growth, the price "
               "implies roughly <b>3.3% annual free-cash-flow growth for a decade</b> \u2014 essentially our base case. The "
               "market is not pricing perfection here, nor distress; it is pricing the base case as the expected case, "
               "which is exactly what 'fair value' means. The prior note's $250 target required either multiple "
               "normalization to 19.7\u00d7 (a bet on the multiple, not the cash flows) or the consensus's own $254 \u2014 "
               "both anchoring moves. On hardened cash-flow math, there is no margin of safety and no required re-rating "
               "\u2014 the stock is priced for the business it has.", s_body))
story.append(P(f"<b>Price target: ${TARGET}.</b> The target <i>is</i> the probability-weighted hardened DCF \u2014 "
               f"0.25\u00d7${RES['bear']['fv']:.2f} + 0.50\u00d7${RES['base']['fv']:.2f} + 0.25\u00d7${RES['bull']['fv']:.2f} "
               f"\u2014 with no multiple overrule and no consensus anchoring. Implied upside +{UPSIDE:.1%}. "
               "What would falsify it: Q3 (Oct 21) restoring the 'above 5%' growth narrative with software re-accelerating "
               "toward high-single digits \u2014 that would argue the bear leg is overstated and the base case deserves more "
               "weight \u2014 or, on the downside, Q3 confirming the Q2 slippage was demand, in which case the bear case "
               "moves toward the center and this note's HOLD becomes a REDUCE.", s_body))

# ============ 4. RISKS & CATALYSTS ============
story.append(P("4 &nbsp; Risks &amp; Catalysts", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Risks", s_h2))
for b in [
    "<b>Execution on large deals:</b> Q2 showed IBM still loses quarters to slipped mega-transactions; a repeat in Q3 (Oct 21) would reframe timing as demand.",
    "<b>Consulting cyclicality:</b> flat revenue with macro-sensitive clients; a genuine enterprise-spending downturn hits signings 2\u20133 quarters later.",
    "<b>Mainframe cycle:</b> Z revenue is lumpy; a weak z17 ramp would remove the 2027\u201328 earnings kicker.",
    "<b>Leverage:</b> $62 bn gross debt limits flexibility for another Confluent-sized deal and keeps interest expense ~$2.5 bn annually \u2014 the equity is a levered stub on the FCF forecast.",
    "<b>AI monetization opacity:</b> dropping the cumulative GenAI bookings disclosure reduces our ability to verify the AI narrative quarter to quarter.",
    "<b>Currency:</b> ~60% of revenue is non-US; a strong dollar is a 1\u20132 pt annual headwind.",
]:
    story.append(B(b))
story.append(P("Catalysts (next 12 months)", s_h2))
for b in [
    "<b>Q3 earnings, Oct 21, 2026:</b> a beat-and-raise restoring the 'above 5%' growth narrative is the single most important event for this note's thesis \u2014 in either direction.",
    "<b>z17 ramp through 2027:</b> mainframe refresh cycles are multi-year margin tailwinds; 130% of z16 trajectory is the leading indicator.",
    "<b>Red Hat re-acceleration:</b> OpenShift $2.2 bn ARR compounding at 15%+ would force a software-multiple re-rating.",
    "<b>32nd dividend increase (April 2027)</b> and continued deleveraging below 3\u00d7.",
    "<b>Rate cuts:</b> as a low-beta, high-yield compounder, IBM benefits disproportionately from falling discount rates.",
]:
    story.append(B(b))

# ============ 5. RECOMMENDATION ============
story.append(P("5 &nbsp; Recommendation", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P(f"<b>HOLD, ${TARGET} target (+{UPSIDE:.1%}).</b> IBM offers a genuinely improved business \u2014 a 3% dividend "
               "yield growing for 31 straight years, $15 bn+ of annual free cash flow, a software business compounding at "
               "high-single digits inside a flat headline number \u2014 and a stock priced as if the market has done the "
               "math: 33% off its high, at a 13% P/E discount to its own history, and a quote that reverse-engineers to "
               "~3.3% annual FCF growth for a decade \u2014 the base case, priced as the expected case. The hardened 10-year "
               "DCF values the equity at $223 (bear $93.78 / base $241.42 / bull $314.98) against a $222.64 quote. The prior "
               "note's $250 target rested on peer-multiple normalization and a 15% weight on Street consensus; the rebuild "
               "rejects both as anchoring. The base case alone offers +8.4% \u2014 not enough for a BUY under our +20% "
               "threshold \u2014 and the bear leg is a genuine \u201358% because $53.8B of net debt turns a forecast miss "
               "into an equity event.", s_body))
story.append(P("Size it as a core compounder, not a trade; add on weakness below $210, and reassess only if Q3 breaks the "
               "'timing, not demand' thesis \u2014 a soft Q3 converts this note's bear case toward the base case and the "
               "HOLD toward a REDUCE, while a restored 'above 5%' narrative argues the bear leg is overstated and opens "
               "the path back to BUY.", s_body))
story.append(Spacer(1, 6*mm))
story.append(P("Disclosure: This note is independent research for informational purposes only and is not investment "
               "advice, a recommendation to buy or sell any security, or personalized financial advice. Valuation uses a "
               "hardened 10-year scenario DCF on IBM-reported free cash flow (excl. financing-receivables swings), 9.0% "
               "base discount, 2.5% terminal growth cap. Financials from IBM Q4'25 and Q2'26 press releases (furnished on "
               "8-K), company IR. Market data: Yahoo Finance (Oct 2, 2026). Estimates are the author's and will prove "
               "wrong in detail. Past performance does not predict future results. The author holds no position in IBM.", s_small))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=18*mm,
                        title="IBM \u2014 Equity Research Note", author="Muse")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("wrote", OUT)
print(f"IBM v2: bear ${RES['bear']['fv']:.2f} / base ${RES['base']['fv']:.2f} / bull ${RES['bull']['fv']:.2f} "
      f"-> weighted ${W_FV:.2f} -> target ${TARGET} vs price ${PRICE:.2f} (+{UPSIDE:.1%})")
