#!/usr/bin/env python3
"""Build the Comcast (CMCSA) equity research note PDF - v2 hardened rebuild, Oct 4 2026."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, HRFlowable)
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import VerticalBarChart

OUT = "/home/hatch/workspace/your_files/comcast-equity-research/comcast-equity-research-note.pdf"

NAVY = HexColor("#0F2A44"); ACCENT = HexColor("#0B6E4F"); GOLD = HexColor("#C9A227")
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
    canvas.drawString(18*mm, 12*mm, "Comcast Corporation (NASDAQ: CMCSA)  \u2014  Equity Research Note  \u2014  October 2026")
    canvas.drawRightString(W - 18*mm, 12*mm, f"Page {doc.page}")
    canvas.setStrokeColor(MGRAY); canvas.setLineWidth(0.5)
    canvas.line(18*mm, 14.5*mm, W - 18*mm, 14.5*mm)
    canvas.restoreState()

# ============ COVER ============
story.append(Spacer(1, 24*mm))
story.append(P("COMCAST CORPORATION (NASDAQ: CMCSA)", ParagraphStyle("x", parent=s_sub, fontName="Helvetica-Bold", fontSize=13, textColor=ACCENT, spaceAfter=2)))
story.append(P("Fairly Priced, Not Cheap<br/>The Re-Rating Is Priced In", s_title))
story.append(Spacer(1, 4*mm))
story.append(P("Equity Research Note  \u00b7  Communication Services \u2014 Cable & Media  \u00b7  October 4, 2026", s_sub))
story.append(Spacer(1, 8*mm))

rating_data = [
    [cell("Recommendation", s_theadL), cell("12-Mo. Price Target", s_thead), cell("Current Price", s_thead), cell("Implied Upside", s_thead), cell("Risk Rating", s_thead)],
    [Paragraph("<b><font color=\"#8A6D00\" size=\"13\">HOLD</font></b>", s_cellC),
     Paragraph("<b><font size=\"12\">$21</font></b>", s_cellC),
     Paragraph("<b>$21.57</b><br/><font size=\"7\" color=\"#5A6472\">Oct 2, 2026</font>", s_cellC),
     Paragraph("<b>\u22121% (+5% w/ dividend)</b>", s_cellC),
     Paragraph("<b>Medium-High</b><br/><font size=\"7\" color=\"#5A6472\">Beta 0.66</font>", s_cellC)],
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
    ["Market cap", "~$76.5 bn", "Shares (diluted)", "~3.54 bn"],
    ["Enterprise value", "~$159 bn", "52-week range", "$21.28 \u2013 $32.86"],
    ["Net debt (mid-2026)", "~$85 bn", "YTD / 1-yr return", "~-27% / -26%"],
    ["TTM adj. EBITDA", "~$34.4 bn", "2026E adj. EPS (cons.)", "~$3.50"],
    ["Normalized FCF", "~$15 bn", "Dividend yield", "6.1% ($1.32 annualized)"],
    ["Next catalyst", "Q3'26 results 10/22/26", "Spin close", "NBCU + Sky, ~mid-2027"],
]
sd = [[cell(r[0], s_cellB), cell(r[1], s_cell), cell(r[2], s_cellB), cell(r[3], s_cell)] for r in snap]
story.append(styled_table([[cell("Snapshot", s_theadL), cell("", s_thead), cell("", s_thead), cell("", s_thead)]] + sd,
               [38*mm, 42*mm, 42*mm, 48*mm], header_rows=1))
story.append(Spacer(1, 8*mm))
story.append(P("This note is independent research-style analysis for informational purposes only and is not investment advice. "
               "Figures are drawn from Comcast's SEC filings and earnings releases and market data as of October 2, 2026. "
               "Projections and the price target are the author's estimates. This note supersedes the September 28, 2026 "
               "edition (BUY, $40 target), which is withdrawn.", s_small))
story.append(PageBreak())

# ============ 1. INVESTMENT THESIS ============
story.append(P("1 &nbsp; Investment Thesis", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("We are downgrading Comcast from BUY to <b>HOLD</b> and cutting the target from $40 to <b>$21</b>. The September "
               "note's $40 target rested on a valuation stack that does not survive a red-team audit: a <b>flat 6.25% WACC</b> "
               "that the note itself admitted was subsidized by leverage that may not persist, a bear case ($21) that sat "
               "essentially <i>at</i> the market price, and a target blended from four models with hand-set weights and then "
               "haircut on judgment. Rebuilt under hardened rules \u2014 a 10-year scenario DCF, tiered discounts "
               "(base 10%, bear 12.5%, bull 8.5%), terminal growth capped at 2.5% \u2014 fair value is <b>$21.39, within 1% of "
               "the $21.57 quote</b>. The market already prices the stabilized-free-cash-flow base case. There is no margin "
               "of safety at this price, and the bear case ($1.03) is catastrophic: $85B of debt means the equity is a stub "
               "in any real decline scenario.", s_body))
story.append(P("What changed in our judgment, in plain terms. The old note asked the reader to underwrite the company 'like "
               "a utility with a catalyst.' A utility with 2.2x leverage, a shrinking core product, and a ratings review is not "
               "a utility \u2014 and pricing it at a utility's cost of capital (6.25%) was the load-bearing error. At a standard "
               "10% discount, the EV math is unforgiving: enterprise value $155.8B against $85B of net debt leaves equity "
               "worth $70B, or <b>$20.00 in the base case</b>. The bull case ($44.55) requires the broadband turnaround, the "
               "mobile conversion, Peacock sustaining profit, <i>and</i> a clean spin re-rating \u2014 all four, to get to a "
               "number the old note treated as the midpoint.", s_body))
story.append(P("Why not REDUCE? Two things keep this a HOLD rather than a sell. First, the base case is genuinely plausible: "
               "normalized free cash flow of ~$15B is real, the 6.1% dividend is covered ~8\u20139x by FCF, and the mid-2027 "
               "spin is a real catalyst that converts a conglomerate discount into two pure-plays. Second, the bear case is "
               "severe but not the modal outcome \u2014 wireless is adding a record ~450K lines a quarter and Peacock just "
               "posted its first profitable quarter. Holders are paid 6% to wait for the spin; new money has no edge at "
               "$21.57.", s_body))

story.append(P("Why own it (at the right price)", s_h2))
for b in [
    "<b>A ~20% free-cash-flow yield that is real.</b> Normalized FCF of ~$15B on a $76.5B market cap, after stripping the $2B one-time FY25 cash-tax benefit. The dividend ($1.32, 6.1%) is covered ~8\u20139x by FCF \u2014 the floor of the thesis.",
    "<b>Wireless is the offset that works.</b> Xfinity Mobile passed 10M lines with a record +448K net adds in Q2'26; wireless service revenue +14.2% to $1.0B/quarter. Convergence (cheap/free mobile) is the only proven broadband-churn reducer in the toolkit.",
    "<b>The spin is a genuine catalyst.</b> NBCU + Sky separation (~mid-2027) leaves a pure-play connectivity company (~40% EBITDA margins, 55%+ in business services) that the market prices at 6\u20137x EBITDA \u2014 versus 4.3x today \u2014 plus a separately-listed media asset with parks and studios the conglomerate multiple buries.",
    "<b>Peacock inflected.</b> First profitable quarter (+$189M EBITDA on $1.9B revenue, +54%) after >$11B of cumulative losses. The NBA/Olympics rights give it a live-sports funnel nobody else replicates.",
]:
    story.append(B(b))
story.append(P("Why the market should be nervous", s_h2))
for b in [
    "<b>The CFO just warned of 'no sign of easing' in broadband attrition.</b> Q2'26: AT&T; +646K, T-Mobile +520K, Verizon +348K net broadband adds vs Comcast \u2212167K. Fiber overbuilders and fixed wireless are taking 1M+ net adds a quarter industry-wide while cable loses share \u2014 and Comcast is defending with price cuts (broadband ARPU \u22123.8% YoY) that compress the very margins the thesis needs.",
    "<b>$85B of debt makes the equity a stub in the bear case.</b> Our bear DCF is $1.03/share \u2014 not a typo. At 12.5% discount with FCF declining ~4.5%/yr and \u22122% terminal growth, EV falls to $88.7B and the debt consumes nearly all of it. Leverage cuts both ways; the old note's 6.25% WACC assumed it only cuts one way.",
    "<b>The spin's economics are TBD.</b> The debt split, each company's dividend policy, and standalone NBCU economics are unknown; a bad split (too much debt on RemainCo, dividend rebase) unwinds the re-rating. Buybacks stay paused until close \u2014 removing price support.",
    "<b>Ratings on review.</b> Moody's (A3) and S&amp;P; (A\u2212) both have the company on review since the spin announcement. A downgrade raises funding costs on a ~$90B debt stack.",
]:
    story.append(B(b))

# ============ 2. BUSINESS ============
story.append(P("2 &nbsp; Business Overview", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Comcast is the largest U.S. residential broadband provider, mid-way through a two-step breakup. On January 2, "
               "2026 it completed the tax-free spin of its legacy cable networks into Versant Media Group. On June 29, 2026 it "
               "announced a second tax-free separation: NBCUniversal + Sky into a standalone public company (target close "
               "~mid-2027). Post-deals, Comcast becomes a pure-play connectivity company (Xfinity broadband/wireless/"
               "business services, ~65M U.S. homes and businesses passed); the spun media company keeps Universal Pictures, "
               "NBC/Telemundo/Bravo, Peacock, the theme parks including Epic Universe, Sky, and a sports-rights stack "
               "(NFL, NBA, Olympics) through 2032\u20132036.", s_body))
story.append(P("Segment economics (2025, recast ex-Versant): Connectivity &amp; Platforms is the profit engine at 86.6% of "
               "adjusted EBITDA with ~40% margins \u2014 residential C&amp;P; $70.7B revenue at 37.7% EBITDA margin, "
               "business services $10.2B at 55.9% (the highest-margin, fastest-growing piece, staying in RemainCo). Media "
               "($27.1B, 11.8%), Studios ($11.3B, 9.7%), Parks ($9.8B, 31.3% \u2014 Epic Universe opened May 2025, drove "
               "FY25 parks EBITDA +4.5%). Consolidated: $123.7B revenue, $37.4B adjusted EBITDA (30.2%). Q2'26: revenue "
               "$29.94B (\u22121.2%), EBITDA $8.90B (\u221213.4%) \u2014 beat consensus on both, but the trajectory is "
               "deteriorating at the core.", s_body))
story.append(P("The product battleground in brief", s_h2))
for b in [
    "<b>Xfinity Internet (crown jewel, under attack).</b> ~28.5M domestic residential broadband subs. Since June 2025: everyday-pricing tiers, 5-year price lock, free Xfinity Mobile line for a year \u2014 an explicit trade of ARPU for retention. Net losses narrowed (Q2'26 \u2212167K vs \u2212201K) but the CFO warned of no easing in Q3. DOCSIS 4.0 upgrade economics (<$200/home vs $500\u20131,000 fiber) are a cost story, not a growth story.",
    "<b>Xfinity Mobile (the offset).</b> 10.19M lines, record +448K adds in Q2'26; only ~7% penetrated of the addressable base. H2 2026 test: ~1M+ free-year promo lines must convert to paying.",
    "<b>Peacock (inflection).</b> 48M paid subs, first profitable quarter. Rides with the spun NBCU.",
    "<b>Parks &amp; studios (mispriced inside the conglomerate).</b> Universal #1 studio in 2026 (>$5B global box office); Epic Universe ramping. Both ride with the spun NBCU at higher multiples than 4.3x.",
]:
    story.append(B(b))

# ============ 3. FINANCIALS ============
story.append(P("3 &nbsp; Financial Situation", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("Revenue has been flat for three years (~$122\u2013124B) while the mix deteriorates at the core. Two adjustments "
               "matter: FY2025 GAAP net income ($20.0B) includes a $9.4B pre-tax Hulu-sale gain, and FY2025 free cash flow "
               "($19.2B, a record) includes a ~$2.0B one-time cash-tax benefit that will not recur. Use adjusted EBITDA "
               "(~$37.4B FY2025; TTM ~$34.4B) and normalized FCF (~$15B) as the analytical base.", s_body))
fin = [
    [cell("$ mn", s_theadL), cell("FY2022", s_thead), cell("FY2023", s_thead), cell("FY2024", s_thead), cell("FY2025", s_thead), cell("TTM", s_thead)],
    [cell("Revenue", s_cellB), cell("121,427", s_cellR), cell("121,572", s_cellR), cell("123,731", s_cellR), cell("123,707", s_cellR), cell("124,905", s_cellR)],
    [cell("Adjusted EBITDA", s_cell), cell("36,459", s_cellR), cell("37,633", s_cellR), cell("38,069", s_cellR), cell("37,384", s_cellR), cell("34,398", s_cellR)],
    [cell("Adj. EBITDA margin", s_cell), cell("30.0%", s_cellR), cell("31.0%", s_cellR), cell("30.8%", s_cellR), cell("30.2%", s_cellR), cell("27.5%", s_cellR)],
    [cell("Adjusted EPS", s_cell), cell("$3.64", s_cellR), cell("$3.98", s_cellR), cell("$4.33", s_cellR), cell("$4.31", s_cellR), cell("$3.79", s_cellR)],
    [cell("Free cash flow", s_cell), cell("12,646", s_cellR), cell("12,962", s_cellR), cell("12,543", s_cellR), cell("19,235*", s_cellR), cell("17,774*", s_cellR)],
]
story.append(styled_table(fin, [44*mm, 26*mm, 26*mm, 26*mm, 26*mm, 26*mm]))
story.append(P("*FY25/TMM include ~$2.0B one-time cash-tax benefit. Sources: company releases; yfinance.", s_small))
story.append(P("Balance sheet: ~$90.4B total debt, ~$7.7B cash \u2192 ~$83\u201385B net debt at mid-2026; net leverage ~2.2x "
               "adjusted EBITDA; interest coverage ~8.5x; A3/A\u2212 both on review since the spin announcement; maturities "
               "long-dated to 2055. Dividend $1.32 annualized (6.1% yield), 17 straight increases through Jan 2025, held flat "
               "in Jan 2026 \u2014 payout ~31% of FY25 adjusted EPS and ~8\u20139% of normalized FCF. Buybacks paused "
               "June 29, 2026 pending separation ($7.2B in 2025).", s_body))

# ============ 4. VALUATION ============
story.append(P("4 &nbsp; Valuation \u2014 Hardened 10-Year DCF, Fair Value $21", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
story.append(P("The September note valued Comcast on four blended lenses with a flat 6.25% WACC \u2014 a cost of capital the "
               "note itself flagged as subsidized by leverage that may not persist. The rebuild values the firm on a single "
               "hardened 10-year free-cash-flow DCF, weights bear 25% / base 50% / bull 25%, and prices risk through "
               "scenario-specific discounts rather than a leverage-flattered WACC: <b>base 10.0%</b> (standard tier \u2014 "
               "declining core, 2.2x leverage, spin execution risk; this is not a stable compounder), <b>bear 12.5%</b> "
               "(base + 250bp), <b>bull 8.5%</b> (base \u2013 150bp). Terminal growth is <b>+1.5% / \u22122.0% / +2.0%</b> on "
               "year-10 FCF at normalized mid-cycle margins (12.1% base, never peak). Net debt $85B; 3.539B shares. No "
               "multiple overrule, no lens-blending, no judgment haircut: the target <i>is</i> the weighted DCF.", s_body))
story.append(Spacer(1, 3*mm))
story.append(P("Scenario DCF (10-year FCFF, 2027\u20132036):", s_h2))
dcf = [
    [cell("Scenario", s_theadL), cell("2027\u201336 rev CAGR", s_thead), cell("FCF path ($B)", s_thead), cell("FCF mgn yr-10", s_thead), cell("Discount / term. g", s_thead), cell("Fair value", s_thead)],
    [cell("Bear", s_cellB), cell("\u22121.2%", s_cellC), cell("14.5 \u2192 9.6", s_cellR), cell("8.9%", s_cellR), cell("12.5% / \u22122.0%", s_cellR), cell("$1.03", s_cellBR)],
    [cell("Base", s_cellB), cell("0.0%", s_cellC), cell("14.7 \u2192 14.6", s_cellR), cell("12.1%", s_cellR), cell("10.0% / +1.5%", s_cellR), cell("$20.00", s_cellBR)],
    [cell("Bull", s_cellB), cell("+1.2%", s_cellC), cell("15.4 \u2192 19.0", s_cellR), cell("14.0%", s_cellR), cell("8.5% / +2.0%", s_cellR), cell("$44.55", s_cellBR)],
    [cell("Probability-weighted (25/50/25) \u2192 <b>$21 target</b>", s_cellB), cell("", s_cellC), cell("", s_cellR), cell("", s_cellR), cell("", s_cellR), cell("$21", s_cellBR)],
]
story.append(styled_table(dcf, [52*mm, 24*mm, 26*mm, 24*mm, 30*mm, 24*mm]))

d2 = Drawing(430, 185)
d2.add(String(215, 173, "Scenario fair values vs. current price ($)", fontName="Helvetica-Bold", fontSize=10, textAnchor="middle", fillColor=NAVY))
bc2 = VerticalBarChart(); bc2.x = 45; bc2.y = 30; bc2.height = 115; bc2.width = 340
bc2.data = [[1, 20, 45, 21, 22]]
bc2.strokeColor = None; bc2.barLabels.nudge = 8; bc2.barLabelFormat = "%d"
bc2.bars[0].fillColor = ACCENT
bc2.categoryAxis.categoryNames = ["Bear", "Base", "Bull", "Wtd. avg", "Price"]
bc2.valueAxis.valueMin = 0; bc2.valueAxis.valueMax = 50; bc2.valueAxis.valueStep = 10
bc2.valueAxis.labels.fontSize = 7; bc2.categoryAxis.labels.fontSize = 8
d2.add(bc2)
story.append(d2)

story.append(P("The bear case is genuinely severe \u2014 and it must be. If broadband losses don't stabilize (the CFO's own "
               "warning), FCF declines ~4.5%/yr to $9.6B by 2036 with \u22122% terminal decline; at a 12.5% discount the "
               "firm is worth $88.7B and the $85B debt stack consumes nearly all of it. Bear fair value <b>$1.03</b>: revenue "
               "declines (\u22121.2% CAGR), FCF margin compresses 320bp vs base (12.1% \u2192 8.9%), and the derating is "
               "95% \u2014 all three hurt conditions met, and far below the $21.57 quote. The base case requires only that "
               "FCF <i>stops shrinking</i> \u2014 mobile (+448K record adds), a profitable Peacock, and Epic Universe "
               "offsetting broadband ARPU erosion \u2014 and it is worth <b>$20.00</b>. The bull case ($44.55) needs the "
               "turnaround, the mobile conversion, sustained Peacock profit, <i>and</i> a clean spin re-rating.", s_body))
story.append(P("Why the old $40 is withdrawn. Three leaks, now closed: (1) the 6.25% WACC was flat across scenarios and "
               "explicitly leverage-subsidized \u2014 at a 10% cost of capital the base-case EV is $155.8B, not $287B; "
               "terminal value is 43% of base EV (no TV-dependence haircut needed, but the old model's low discount hid "
               "how much value sat in the terminal); (2) the old bear ($21) sat at the market price \u2014 a bear that "
               "doesn't hurt is a base case in disguise; (3) the target was a 45/25/20/10 blend of DCF, SOTP, multiples and "
               "DDM with hand-set weights, then haircut $44.50 \u2192 $40 on judgment. The hardened rule is one model, "
               "one weighting, no overrule. <b>Price target: $21</b> (0.25\u00d7$1.03 + 0.50\u00d7$20.00 + 0.25\u00d7$44.55 "
               "= $21.39, rounded). Implied return \u22120.8% price, ~+5% with the dividend.", s_body))
story.append(P("What would falsify the HOLD: broadband net losses stabilizing below \u2212100K/quarter for two quarters "
               "would argue the base case deserves a lower discount (the turnaround de-risked) \u2014 as would a spin "
               "filing that cleanly allocates debt and preserves the dividend, which would move us back toward BUY. "
               "Conversely, losses re-accelerating past \u2212250K/quarter pushes fair value toward the bear case and "
               "the rating to REDUCE.", s_body))

story.append(P("5 &nbsp; Key Risks", s_h1))
story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=6))
for b in [
    "<b>Broadband competition (high).</b> Fiber + fixed wireless taking 1M+ net adds/quarter industry-wide; Comcast defending with ARPU-dilutive pricing. If Q3\u2013Q4'26 losses don't stabilize, the trough-multiple thesis breaks.",
    "<b>Split execution (medium-high).</b> Debt allocation, dividend policies, standalone NBCU economics all TBD; tax-free status constrains M&amp;A; for a year post-close.",
    "<b>Leverage (medium).</b> ~2.2x net debt/EBITDA; both ratings on review; a downgrade raises funding costs on a ~$90B stack.",
    "<b>Sports-rights &amp; content costs (medium).</b> NBA ~$2.5B/season with expected early-year losses; Olympics through 2036 a $10B+ commitment \u2014 burdening consolidated FCF until the split.",
    "<b>Video &amp; programming (medium, fading).</b> Cord-cutting continues; largely margin-accretive and partly spun away with Versant.",
    "<b>Cyclicality (low-medium).</b> Parks and advertising are discretionary; Orlando softened in summer 2026.",
]:
    story.append(B(b))

story.append(P("Recommendation", s_h2))
story.append(P("<b>HOLD, $21 target (\u22120.8% price; ~+5% with dividend).</b> The September note's BUY rested on a "
               "leverage-subsidized 6.25% WACC and a four-lens blend; rebuilt under hardened rules, fair value is $21.39 "
               "against a $21.57 quote \u2014 the market already prices the stabilized-FCF base case. The 6.1% dividend "
               "(covered ~8\u20139x by FCF) pays holders to wait for the mid-2027 spin, but new money has no margin of "
               "safety and the bear case ($1.03) is a reminder of what $85B of debt does in a real decline. We would "
               "upgrade to BUY below ~$17 (where the base case offers 20%+ upside) or on evidence the broadband "
               "turnaround is real; we would cut to REDUCE if quarterly losses re-accelerate past \u2212250K. "
               "<b>Falsification:</b> two quarters of broadband losses under \u2212100K, or a spin filing that cleanly "
               "allocates debt and preserves the dividend, would argue the base case deserves a lower discount \u2014 and "
               "a higher rating.", s_body))
story.append(Spacer(1, 6*mm))
story.append(P("Methodology &amp; sources. Valuation as of October 4, 2026; share price $21.57 (10/2/26 close). Model: 10-year "
               "scenario FCFF DCF, weights bear 25% / base 50% / bull 25%; discounts base 10.0% (standard tier) / bear 12.5% / "
               "bull 8.5%; terminal growth +1.5% / \u22122.0% / +2.0% on year-10 FCF at normalized mid-cycle margins. "
               "Net debt $85B (mid-2026); 3.539B diluted shares. Bear case meets all three hurt conditions (revenue decline, "
               "\u2265300bp margin compression, \u226525% derating) and sits below the current price. Terminal value is "
               "43% of base-case EV (no haircut required). Segment and KPI data from Comcast Q1/Q2 2026 earnings releases "
               "and FY2025 10-K; market data via Yahoo Finance. This note is research analysis for informational purposes "
               "and is not personalized investment advice. Equity investing involves risk of loss. The author holds no "
               "position in CMCSA at the time of writing.", s_small))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=18*mm,
                        title="Comcast (CMCSA) \u2014 Equity Research Note", author="Muse")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("wrote", OUT)
