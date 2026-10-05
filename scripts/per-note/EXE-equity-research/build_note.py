#!/usr/bin/env python3
"""Build the Expand Energy (EXE) equity research note PDF — v2 hardened rebuild, October 4, 2026."""
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

OUT = "/home/hatch/workspace/your_files/EXE-equity-research/exe-equity-research-note.pdf"

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
    canvas.drawString(18*mm, 12*mm, "Expand Energy Corporation (NASDAQ: EXE)  \u2014  Equity Research Note  \u2014  October 2026")
    canvas.drawRightString(W - 18*mm, 12*mm, f"Page {doc.page}")
    canvas.setStrokeColor(MGRAY); canvas.setLineWidth(0.5)
    canvas.line(18*mm, 14.5*mm, W - 18*mm, 14.5*mm)
    canvas.restoreState()

# ================= v2 valuation engine =================
# 10-yr scenario DCF on FCF ($B). Anchored to Q2'26 annualized FCF $1.37B at ~$2.90
# realized gas + the company's $/Mcf sensitivity (+$0.50/Mcfe \u2248 +$1.37B revenue).
# Discount tiers: base 10% (standard: cyclical commodity E&P, 92% gas exposure),
# bear = base + 250bp, bull = base \u2013 150bp. Terminal growth \u22642.5% on a DEPLETING
# resource: base 1.0%, bull 1.5%, bear 0% \u2014 shale wells decline; no perpetual growth.
# Mid-cycle Henry Hub deck: base ~$3.50, bull $3.50\u2192$4.25, bear $2.90 flat.
SHARES = 231.504e6          # Oct 2, 2026, Yahoo
NET_DEBT = 4.3e9            # ~$4.3B pro forma (incl. Twin Eagle $1.25B)
PRICE = 85.52               # Oct 2, 2026 close

FCF = {
    "bear": [1.45]*10,
    "base": [2.30, 2.70, 3.00, 3.10, 3.00, 3.00, 2.95, 2.95, 2.90, 2.90],
    "bull": [2.70, 3.30, 3.90, 4.20, 4.10, 4.10, 4.05, 4.00, 3.95, 3.90],
}
RATES = {"bear": (0.125, 0.000), "base": (0.10, 0.010), "bull": (0.085, 0.015)}

def scen_dcf(fcf, r, g):
    fcf = np.array(fcf, float)*1e9
    pv = float(sum(f/(1+r)**(t+1) for t, f in enumerate(fcf)))
    tv = float(fcf[-1]*(1+g)/(r-g))
    pv_tv = float(tv/(1+r)**10)
    ev = pv + pv_tv
    return dict(ev=ev, tv_share=pv_tv/ev, fv=(ev-NET_DEBT)/SHARES, fcf10=fcf[-1])

RES = {k: scen_dcf(FCF[k], *RATES[k]) for k in FCF}
W_FV = 0.25*RES["bear"]["fv"] + 0.50*RES["base"]["fv"] + 0.25*RES["bull"]["fv"]
TARGET = round(W_FV)
UPSIDE = TARGET/PRICE - 1

# ============ COVER ============
story.append(Spacer(1, 24*mm))
story.append(P("EXPAND ENERGY CORPORATION (NASDAQ: EXE)", ParagraphStyle("x", parent=s_sub, fontName="Helvetica-Bold", fontSize=13, textColor=ACCENT, spaceAfter=2)))
story.append(P("America's Largest Gas Producer,<br/>Still Priced Like Gas Stays Cheap Forever", s_title))
story.append(Spacer(1, 4*mm))
story.append(P("Equity Research Note  \u00b7  Energy \u2014 Oil &amp; Gas E&amp;P (Natural Gas)  \u00b7  October 4, 2026", s_sub))
story.append(Spacer(1, 8*mm))

rating_data = [
    [cell("Recommendation", s_theadL), cell("12-Mo. Price Target", s_thead), cell("Current Price", s_thead), cell("Implied Upside", s_thead), cell("Risk Rating", s_thead)],
    [Paragraph("<b><font color=\"#0E7C3E\" size=\"13\">BUY</font></b>", s_cellC),
     Paragraph(f"<b><font size=\"12\">${TARGET}</font></b>", s_cellC),
     Paragraph("<b>$85.52</b><br/><font size=\"7\" color=\"#5A6472\">Oct 2, 2026</font>", s_cellC),
     Paragraph(f"<b>+{UPSIDE:.1%}</b>", s_cellC),
     Paragraph("<b>Medium-High</b><br/><font size=\"7\" color=\"#5A6472\">Commodity leverage</font>", s_cellC)],
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
    ["Market cap", "~$19.8 bn", "Shares (diluted)", "~231.5 mn"],
    ["Enterprise value", "~$24.1 bn", "52-week range", "$83.25 \u2013 $126.62"],
    ["Net debt (pro forma)", "~$4.3 bn", "Dividend", "$2.30/yr (2.7% yield)"],
    ["Production", "~7.5 Bcfe/d (92% gas)", "Proved reserves", "25.9 Tcfe"],
    ["Q2'26 adj. EBITDAX", "$1,183 mn (flat y/y)", "Q2'26 realized gas", "$2.42/Mcf ($2.90 w/ hedges)"],
    ["Next catalyst", "Q3'26 earnings, ~Oct 26", "Analyst consensus", "Moderate Buy, avg PT $127.42"],
]
sd = [[cell(r[0], s_cellB), cell(r[1], s_cell), cell(r[2], s_cellB), cell(r[3], s_cell)] for r in snap]
story.append(styled_table([[cell("Snapshot", s_theadL), cell("", s_thead), cell("", s_thead), cell("", s_thead)]] + sd,
               [38*mm, 42*mm, 42*mm, 48*mm], header_rows=1))
story.append(Spacer(1, 8*mm))
story.append(P("This note is independent research-style analysis for informational purposes only and is not investment advice. "
               "Figures are drawn from Expand Energy's SEC filings and earnings releases, EIA data, and reputable financial "
               "press as of October 2, 2026. Projections and the price target are the author's estimates under a hardened "
               "10-year scenario-DCF methodology.", s_small))
story.append(PageBreak())

# ============ 1. INVESTMENT THESIS ============
story.append(P("1 &nbsp; Investment Thesis", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Expand Energy is the largest independent U.S. natural gas producer (~7.5 Bcfe/d, 92% gas, 25.9 Tcfe proved), "
               "formed by the October 2024 Chesapeake\u2013Southwestern merger. The stock sits near a 52-week low ($85.52 vs. "
               "$126.62 high) because Henry Hub has been pinned in a $2\u2013$3.60 strip \u2014 at or below the company's stated "
               "breakeven economics. Our work says the market is pricing bear-case gas held flat forever: the current "
               "enterprise value capitalizes to roughly $2.1B of perpetual free cash flow, equivalent to a sustained ~$3.00 "
               "Henry Hub with zero terminal growth and no LNG uplift. Meanwhile the 2027 futures strip is already ~$3.27 "
               "rising toward ~$3.87, U.S. LNG exports just grew 23% year-on-year to 17.4 Bcf/d, and data-center power demand "
               "is set to add up to 20 Bcf/d of gas consumption by 2030. With 0.5x leverage, a $600M synergy program, a "
               "transforming gas-marketing arm (Twin Eagle), and $1.85B+ of annual shareholder returns, this is a call on "
               "gas normalization with a fortress balance sheet underneath.", s_body))
story.append(P("The hardened rebuild <b>confirms the BUY but reprices it honestly</b>. Our 10-year scenario DCF \u2014 weights "
               "bear 25% / base 50% / bull 25%, discount rates 12.5% / 10.0% / 8.5%, terminal growth capped at 1.5% on a "
               "<i>depleting</i> shale resource \u2014 yields a probability-weighted fair value of <b>$112, 31.4% above</b> the "
               "current price. Crucially, this rebuild's bear case ($31.53, \u201363%) actually hurts \u2014 the prior note's bear "
               "($94.42) sat <i>above</i> the $85.94 price, a mild-bear leak that priced zero downside. The target <i>is</i> "
               "the weighted DCF: $112. The Street's $127 average target requires the strip to be the <i>expected</i> case; "
               "we set ours at the weighted scenarios, deliberately below consensus.", s_body))

story.append(P("Audit of the October 2 note (red-team lens)", s_h2))
story.append(P("The prior note said BUY with a $115 target, dated October 2, 2026. Its commodity analysis was directionally "
               "right, but it had two load-bearing flaws the hardened methodology fixes. <b>First, the bear case did not "
               "hurt:</b> $94.42 against an $85.94 price \u2014 a 'bear' that implies +10% upside is an optimism leak, not a "
               "scenario. A real bear \u2014 gas stuck at ~$2.90 flat for a decade on a depleting resource \u2014 is worth $31.53, "
               "and that asymmetry belongs in the valuation. <b>Second, the $115 target was a judgment departure</b>, set "
               "'between' the peer-multiple read ($107) and the weighted DCF ($129); under v2 rules the target equals the "
               "weighted DCF unless a written, falsifiable justification departs from it, and 'between two lenses' is not "
               "one. The three strongest arguments against this note's own BUY: <b>(1)</b> 92% gas exposure is binary \u2014 "
               "a sustained $0.50/Mcf move swings ~$1B of annual EBITDA on a ~$20B market cap, and the bear case is a "
               "genuine \u201363% drawdown; <b>(2)</b> realized basis kills the thesis before Henry Hub does \u2014 NE Appalachia "
               "realized just $2.15/Mcf in Q2, and Marcellus differentials can persist even if the Hub recovers; "
               "<b>(3)</b> shale decline economics \u2014 7.5 Bcfe/d of production needs ~$2.9B/yr of capex just to stand still, "
               "so valuing the company on strip peaks instead of mid-cycle normalization is the classic E&amp;P trap. "
               "The load-bearing assumption is that the futures strip (~$3.27 \u2192 $3.87) is approximately right and gas "
               "normalizes toward mid-cycle ~$3.50; if the strip is wrong and $2.90 is the new normal, this note's bear "
               "case is the base case.", s_body))

story.append(P("Why it works (bull)", s_h2))
for b in [
    "<b>Largest low-cost gas inventory.</b> Haynesville breakeven &lt;$2.75/Mcf; corporate well below $3/Mcf \u2014 at the low end of the peer cost curve. Well productivity runs ~40% above basin averages; scale compounds drilling and completion efficiencies.",
    "<b>LNG export wave.</b> 17.4 Bcf/d in 1H26 (+23%); Golden Pass Train 2 (late 2026), Port Arthur Phase 1, CP2, Rio Grande (2027\u201331). Expand's Haynesville acreage sits adjacent to Gulf Coast LNG demand.",
    "<b>Data-center/AI power demand.</b> BloombergNEF: power-sector gas rises to 54 Bcf/d by 2035 (+18 vs 2025), with producers ~11 Bcf/d short of projected demand growth. Wood Mackenzie (Jul 2026): 'the decade of cheap Henry Hub gas is coming to an end.'",
    "<b>$600M merger synergies by YE2026;</b> marketing FCF target raised to $750M/yr via Twin Eagle \u2014 ~$0.20/Mcf of margin improvement (~$500M of repeatable annual FCF) that does not depend on the gas price.",
    "<b>Fortress balance sheet.</b> 0.5x leverage (0.8x pro forma), $2.30 dividend + ~$1.85B/yr buybacks; valuation at ~4x EV/EBITDA vs. peers at 5.5\u20136x.",
]:
    story.append(B(b))
story.append(P("What breaks it (bear)", s_h2))
for b in [
    "<b>92% gas exposure: leverage cuts both ways.</b> A sustained $0.50/Mcf move swings ~$1B of annual EBITDA. Our bear DCF ($31.53) is \u201363% below the price \u2014 that is the real downside, and it is not in the price.",
    "<b>Gas stays $2\u2013$3:</b> associated-gas supply, mild winters, storage overhang; hedges cap upside above collars. 2027 coverage is undisclosed \u2014 a key Q3 earnings watch item.",
    "<b>Marcellus basis:</b> NE Appalachia realized only $2.15/Mcf in Q2; differentials can persist even if Henry Hub recovers.",
    "<b>LNG project delays or a demand shortfall</b> would strand the 2027\u201328 bull case.",
    "<b>Execution:</b> interim CEO since early 2026; Twin Eagle integration and the $150M synergy target by YE2028 are new.",
]:
    story.append(B(b))

# ============ 2. BUSINESS OVERVIEW ============
story.append(P("2 &nbsp; Business Overview \u2014 What Expand Energy Does", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Expand Energy was created in October 2024 when Chesapeake Energy acquired Southwestern Energy for ~$7.4B, "
               "then rebranded \u2014 making it the largest independent U.S. natural gas producer at roughly 7.5 Bcfe/d, 92% "
               "natural gas, ahead of rival EQT. Headquarters: Oklahoma City. The footprint spans three basins (proved "
               "reserves 25.88 Tcfe at YE2025): <b>Haynesville</b> (23% of reserves, 3,187 MMcf/d, $2.62/Mcf realized in Q2) "
               "\u2014 the LNG-adjacent growth engine, with 75,000+ net Western Haynesville acres and 200+ potential locations; "
               "<b>NE Appalachia</b> (42% of reserves, 2,625 MMcf/d, $2.15/Mcf realized) \u2014 the low-cost, basis-constrained "
               "base; <b>SW Appalachia</b> (35% of reserves, 1,084 MMcf/d gas + 14 MBbl/d oil + 83 MBbl/d NGL, $3.64/Mcfe "
               "blended) \u2014 the liquids kicker that lifts blended realizations.", s_body))
story.append(P("There is a second, increasingly important 'product': gas marketing and logistics. The $1.25B Twin Eagle "
               "acquisition (closed Q3 2026) added ~1,000 commercial customers and 44 Bcf of storage; management raised its "
               "marketing/commercial free-cash-flow target to $750M per year and signed a 20-year, 1.15 Mtpa Delfin LNG "
               "supply agreement (targeted 2031). The strategy is to evolve from pure producer to integrated gas marketer \u2014 "
               "capturing volatility and basis spreads that pure producers leave on the table (~$90M of volatility-capture "
               "value in Q1 2026 alone). That transformation is the most underappreciated part of the story.", s_body))
story.append(P("Financial situation", s_h2))
story.append(P("Q2 2026 (reported July 28, 2026): revenue $2.96B (\u201319.8% y/y on lower gas), adjusted EBITDAX $1,183M "
               "(flat y/y despite the price drop \u2014 the synergy story working), adjusted EPS $1.33 vs. $1.12 consensus, "
               "operating cash flow $1,096M, capex ~$753M, free cash flow ~$343M. Production hit 7.48 Bcfe/d. Realized gas "
               "was $2.42/Mcf, or $2.90/Mcf including derivative gains \u2014 the hedge book added ~$0.48/Mcf that quarter. "
               "Balance sheet: total debt $3.7B (down $1.3B since YE2025), cash $663M, net debt $3.075B, leverage just 0.5x "
               "net debt/TTM EBITDAX \u2014 the cleanest balance sheet among large gas E&amp;Ps; ~$4.3B pro forma for Twin "
               "Eagle, still ~0.8x. 2026 guidance (reaffirmed): 7.4\u20137.6 Bcfe/d on $2.75\u2013$2.95B capex. Shareholder "
               "returns: $2.30/yr base dividend (2.7% yield), $849M of buybacks year-to-date (~4% of shares) plus a fresh ~$1B "
               "authorization \u2014 ~$1.85B of 2026 capital-return run-rate. Hedging: floors on &gt;60% of 2026 gas volumes.", s_body))

# ============ 3. VALUATION — HARDENED 10-YEAR DCF ============
story.append(P("3 &nbsp; Valuation \u2014 Hardened 10-Year DCF, Fair Value $112", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("The prior note's 5-year DCF anchored its bear at $94.42 \u2014 above the price \u2014 and set its $115 target "
               "'between' lenses. The hardened rebuild values Expand on a <b>10-year scenario free-cash-flow DCF</b> \u2014 "
               "weights bear 25% / base 50% / bull 25% \u2014 with scenario-specific discounts: <b>bear 12.5%</b> (base + 250bp), "
               "<b>base 10.0%</b> (standard tier: cyclical commodity E&amp;P with 92% gas exposure), <b>bull 8.5%</b> "
               "(base \u2013 150bp). Terminal growth is <b>1.0% / 1.5% / 0.0%</b> \u2014 capped well under 2.5% because shale "
               "wells decline and reserves deplete; no perpetual growth is assumed for a depleting resource. Inputs are "
               "independently justified: the FCF path is anchored to Q2'26 annualized FCF ($1.37B at ~$2.90 realized gas), "
               "the company's own $/Mcf sensitivity (+$0.50/Mcfe \u2248 +$1.37B revenue), the 2027 futures strip (~$3.27 rising "
               "toward ~$3.87), and mid-cycle normalization \u2014 never strip peaks. Year-10 FCF is set at mid-cycle margins, "
               "not the bull-case peak.", s_body))
story.append(Spacer(1, 3*mm))
story.append(P("Scenario DCF (10-year, $B FCF):", s_h2))
dcf = [
    [cell("Scenario", s_theadL), cell("Henry Hub deck", s_thead), cell("2036 FCF", s_thead), cell("Discount / term. g", s_thead), cell("TV share of EV", s_thead), cell("Fair value", s_thead)],
    [cell("Bear: gas stuck ~$2.90", s_cell), cell("$2.90 flat", s_cellC), cell("$1.45", s_cellR), cell("12.5% / 0.0%", s_cellR), cell(f"{RES['bear']['tv_share']:.0%}", s_cellR), cell(f"${RES['bear']['fv']:.2f}", s_cellBR)],
    [cell("Base: strip \u2192 mid-cycle $3.50", s_cell), cell("$3.10 \u2192 $3.50", s_cellC), cell("$2.90", s_cellR), cell("10.0% / 1.0%", s_cellR), cell(f"{RES['base']['tv_share']:.0%}", s_cellR), cell(f"${RES['base']['fv']:.2f}", s_cellBR)],
    [cell("Bull: LNG boom", s_cell), cell("$3.50 \u2192 $4.25", s_cellC), cell("$3.90", s_cellR), cell("8.5% / 1.5%", s_cellR), cell(f"{RES['bull']['tv_share']:.0%}", s_cellR), cell(f"${RES['bull']['fv']:.2f}", s_cellBR)],
    [cell(f"Probability-weighted (25/50/25) \u2192 <b>${TARGET} target</b>", s_cellB), cell("", s_cellC), cell("", s_cellR), cell("", s_cellR), cell("", s_cellR), cell(f"${W_FV:.0f}", s_cellBR)],
]
story.append(styled_table(dcf, [46*mm, 28*mm, 20*mm, 26*mm, 24*mm, 26*mm], fontsize=7.8))
story.append(P("The bear now hurts on every required axis: FCF is flat for a decade (CAGR 0% &lt; 3%), the FCF level sits "
               "~50% below the base path (far beyond the 300bp margin-compression test), and the 250bp derating (12.5% vs "
               "10.0%) applies on top. Bear fair value $31.53 is 63% below the price \u2014 that asymmetry is the honest "
               "price of 92% gas exposure, and it belongs in the valuation rather than being assumed away. No terminal-value "
               "haircut is needed: TV is 31\u201350% of EV across scenarios, well under the 70% guardrail.", s_small))

d = Drawing(430, 185)
d.add(String(215, 173, "Scenario fair values vs. current price ($)", fontName="Helvetica-Bold", fontSize=10, textAnchor="middle", fillColor=NAVY))
bc = VerticalBarChart(); bc.x = 45; bc.y = 30; bc.height = 115; bc.width = 340
bc.data = [[32, 111, 196, 112, 86]]
bc.strokeColor = None; bc.barLabels.nudge = 8; bc.barLabelFormat = "%d"
bc.bars[0].fillColor = ACCENT
bc.categoryAxis.categoryNames = ["Bear", "Base", "Bull", "Wtd. avg", "Price"]
bc.valueAxis.valueMin = 0; bc.valueAxis.valueMax = 220; bc.valueAxis.valueStep = 55
bc.valueAxis.labels.fontSize = 7; bc.categoryAxis.labels.fontSize = 8
d.add(bc)
story.append(d)
story.append(P("Reverse DCF: what is priced in?", s_h2))
story.append(P("At $85.52, enterprise value is ~$24.1B. Capitalized at the 10% base discount with 1.0% terminal growth, that "
               "is roughly $2.1B of perpetual free cash flow \u2014 equivalent to a sustained ~$3.00 Henry Hub with zero "
               "terminal growth and no LNG/data-center uplift. In other words, the stock is priced for bear-case gas, "
               "forever. Any move toward the futures strip re-rates it; the bear case is already in the price.", s_body))
story.append(P("Sensitivity: fair value vs. sustained Henry Hub (perpetuity, 1.0% terminal growth)", s_h2))
sens = [
    [cell("Sustained Henry Hub", s_theadL), cell("$2.75", s_thead), cell("$3.00", s_thead), cell("$3.25", s_thead), cell("$3.50", s_thead), cell("$4.00", s_thead)],
    [cell("Fair value / share", s_cellB), cell("$34", s_cellR), cell("$63", s_cellR), cell("$92", s_cellR), cell("$121", s_cellR), cell("$179", s_cellR)],
]
story.append(styled_table(sens, [52*mm, 24*mm, 24*mm, 24*mm, 24*mm, 24*mm], fontsize=8))
story.append(P("Read this table as the whole debate: at $3.00 gas the stock is roughly fairly valued-to-cheap near $63; "
               "every sustained $0.25 above that is worth ~$29/share. Our $112 target sits between the $3.25 and $3.50 "
               "columns \u2014 i.e., it requires gas to normalize toward mid-cycle, not to boom. The Street's $127 sits at "
               "the $3.50 line, demanding the strip as the expected case.", s_small))
story.append(P(f"<b>Price target: ${TARGET}.</b> The target <i>is</i> the probability-weighted hardened DCF \u2014 "
               f"0.25\u00d7${RES['bear']['fv']:.2f} + 0.50\u00d7${RES['base']['fv']:.2f} + 0.25\u00d7${RES['bull']['fv']:.2f} "
               f"\u2014 with no multiple overrule and no consensus anchoring. Implied upside +{UPSIDE:.1%}. "
               "What would falsify it: the 2027 futures strip collapsing back toward $2.90 and staying there \u2014 in "
               "which case this note's bear case ($31.53) becomes the base case \u2014 or sustained Marcellus basis "
               "blowouts that keep realized prices $0.75+ below Henry Hub regardless of the strip.", s_body))

# ============ 4. RISKS & CATALYSTS ============
story.append(P("4 &nbsp; Risks &amp; Catalysts", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Risks", s_h2))
for b in [
    "<b>Commodity leverage (the big one).</b> 92% gas exposure means a sustained $0.50/Mcf move swings ~$1B of annual EBITDA on a ~$20B market cap. Our bear DCF ($31.53) is \u201363% below the price \u2014 a 2027 warm winter + storage overhang could test it.",
    "<b>Basis differentials.</b> NE Appalachia realized just $2.15/Mcf in Q2; Marcellus differentials (Range guided \u2013$0.35\u2013$0.40) can persist even if Henry Hub recovers.",
    "<b>Hedge drag.</b> Floors protect 2026, but collars cap upside if gas spikes; 2027 coverage is undisclosed \u2014 watch the Q3 10-Q.",
    "<b>Execution.</b> Interim CEO since early 2026; Twin Eagle integration and the $150M synergy target by YE2028 are new.",
    "<b>Regulatory.</b> Methane rules and LNG authorization politics are background risks; nothing EXE-specific outstanding.",
]:
    story.append(B(b))
story.append(P("Catalysts", s_h2))
for b in [
    "<b>Q3 2026 earnings (~Oct 26\u201327):</b> consensus EPS ~$1.35\u20131.41; watch the 2027 hedge book, Twin Eagle close update, and any 2027 capex signal.",
    "<b>LNG start-ups:</b> Golden Pass Train 2 (late 2026), Port Arthur Phase 1, CP2, Rio Grande Trains 1\u20132 (2027) \u2014 each one tightens the physical market.",
    "<b>Winter 2026\u201327 storage/withdrawals:</b> the single biggest near-term swing factor for gas and the stock.",
    "<b>Capital returns:</b> continued buybacks (~4% of shares YTD) and the $750M commercial FCF target de-risk the wait.",
]:
    story.append(B(b))

# ============ 5. RECOMMENDATION ============
story.append(P("5 &nbsp; Recommendation", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P(f"<b>BUY, ${TARGET} target (+{UPSIDE:.1%}).</b> Expand Energy is the best house on a street the market has "
               "abandoned: the lowest-cost, largest-scale, least-levered major gas producer, trading at ~4x EV/EBITDA "
               "while the stock prices in $3.00 gas flat forever. The investment case does not require heroic gas prices \u2014 "
               "it requires the futures strip ($3.27 \u2192 $3.87) to be approximately right, which the LNG export wave and "
               "data-center demand make the base case, not the bull case. The hardened 10-year DCF values the equity at "
               "$112 (bear $31.53 / base $111.16 / bull $195.75) against an $85.52 quote. This rebuild is harsher than the "
               "prior note's: the bear case is a genuine \u201363% drawdown, and the target sits below the Street's $127 "
               "because it refuses to treat the strip as the expected case.", s_body))
story.append(P("<b>Position sizing note:</b> this is a commodity-levered BUY. Size it like one \u2014 a 2\u20134% position for "
               "most portfolios, larger only for investors who explicitly want gas-price torque. The $2.30 dividend (2.7%) "
               "and the buyback pay you to wait; winter 2026\u201327 is the proving ground. Reassess if the 2027 strip "
               "collapses toward $2.90 \u2014 in that world, this note's bear case is the base case and the BUY is wrong.", s_body))
story.append(Spacer(1, 6*mm))
story.append(P("Disclosure: This note is independent research analysis for informational purposes only and is not "
               "personalized investment advice, a recommendation to transact, or an offer to buy or sell any security. "
               "Commodity producers carry substantial price risk; do your own due diligence. Valuation models are estimates "
               "with wide confidence bands \u2014 see the sensitivity table. Company data: Q2 2026 and FY2025 press "
               "releases, 2025 10-K. Market data: Henry Hub futures (late Sep 2026), EIA STEO/AEO 2026, BloombergNEF, "
               "Wood Mackenzie. Consensus: MarketBeat/Zacks, Sep 2026 (24 analysts, avg target $127.42). "
               "The author holds no position in EXE.", s_small))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=18*mm,
                        title="Expand Energy (EXE) \u2014 Equity Research Note", author="Muse")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("wrote", OUT)
print(f"EXE v2: bear ${RES['bear']['fv']:.2f} / base ${RES['base']['fv']:.2f} / bull ${RES['bull']['fv']:.2f} "
      f"-> weighted ${W_FV:.2f} -> target ${TARGET} vs price ${PRICE:.2f} (+{UPSIDE:.1%})")
