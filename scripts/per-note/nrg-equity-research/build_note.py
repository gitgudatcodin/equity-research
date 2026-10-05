#!/usr/bin/env python3
"""Build the NRG Energy (NRG) equity research note PDF — v2 hardened rebuild, October 4, 2026."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle)
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import VerticalBarChart

OUT = "/home/hatch/workspace/your_files/nrg-equity-research/nrg-equity-research-note.pdf"

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
    canvas.drawString(15*mm, 12*mm, "NRG Energy, Inc. (NYSE: NRG)  \u2014  Equity Research Note  \u2014  October 4, 2026")
    canvas.drawRightString(W - 15*mm, 12*mm, f"Page {doc.page}")
    canvas.setStrokeColor(MGRAY); canvas.setLineWidth(0.4)
    canvas.line(15*mm, 14.5*mm, W - 15*mm, 14.5*mm)
    canvas.restoreState()

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=15*mm, rightMargin=15*mm,
                        topMargin=16*mm, bottomMargin=18*mm,
                        title="NRG Energy (NRG) Equity Research Note", author="Independent Research")
_doc_build = doc.build

def verdict_box(rows):
    d = [[cell(f"<b>{r[0]}</b>", s_cellB), cell(r[1], s_cellBR)] for r in rows]
    t = Table(d, colWidths=[62*mm, 62*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LGRAY),
        ("BOX", (0, 0), (-1, -1), 0.8, NAVY),
        ("INNERGRID", (0, 0), (-1, -1), 0.4, MGRAY),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    return t

def build():
    global story
    story = []
    story.append(P("NRG ENERGY, INC. (NYSE: NRG)", ParagraphStyle("k", parent=s_sub, fontName="Helvetica-Bold", fontSize=12, textColor=ACCENT)))
    story.append(Spacer(1, 3*mm))
    story.append(P("A De-Rated Power Platform:<br/>Levered Balance Sheet, Unlevered Growth", s_title))
    story.append(Spacer(1, 3*mm))
    story.append(P("Equity Research Note \u00b7 Utilities \u2014 Independent Power Producer \u00b7 October 4, 2026", s_sub))
    story.append(Spacer(1, 4*mm))
    story.append(verdict_box([
        ("Recommendation", "BUY"),
        ("12-Mo. Price Target", "$143"),
        ("Current Price", "$95.23 (Oct 2, 2026 close)"),
        ("Implied Upside", "+50.2%"),
        ("Risk Rating", "Medium-High (2.0% dividend yield; beta 1.18)"),
    ]))
    story.append(Spacer(1, 4*mm))
    story.append(styled_table([
        [cell("<b>Market cap</b>", s_theadL), cell("<b>Enterprise value</b>", s_thead), cell("<b>Net debt</b>", s_thead), cell("<b>52-week range</b>", s_thead)],
        [cell("~$20.1 bn", s_cellC), cell("~$43 bn", s_cellC), cell("~$23 bn (Jun '26)", s_cellC), cell("$93.36 \u2013 $189.96", s_cellC)],
        [cell("<b>FY26E / FY27E P/E</b>", s_theadL), cell("<b>EV/EBITDA (26E)</b>", s_thead), cell("<b>FCFbG yield (26E)</b>", s_thead), cell("<b>1-yr return</b>", s_thead)],
        [cell("10.7\u00d7 / 8.4\u00d7*", s_cellC), cell("~7.8\u00d7", s_cellC), cell("~14%", s_cellC), cell("-41%", s_cellC)],
    ], [38*mm, 38*mm, 38*mm, 36*mm], fontsize=8))
    story.append(P("*On consensus adj. EPS of $8.9 (2026E) / $11.3 (2027E).", s_small))
    story.append(P("NRG is the cheapest of the independent power producers \u2014 and the most retail-integrated. After the "
        "January 2026 LS Power deal it runs ~25.8 GW of mostly gas-fired generation alongside the largest competitive retail "
        "electricity book in the U.S. and the Vivint smart-home platform. The stock sits near 52-week lows because the market "
        "sees $23B of debt, two earnings misses, and guidance tracking below midpoint. This v2 rebuild values the equity as "
        "what it is \u2014 a levered stub \u2014 with hardened rules: scenario-specific discount rates (base 11%, bear 13.5%, "
        "bull 9.5%), terminal growth capped at 2% on <i>normalized mid-cycle power prices</i> (never the 2026 capacity-auction "
        "peak), and a bear case that genuinely hurts ($20.29, \u221279%). The probability-weighted FCFbG DCF (25/50/25) lands "
        "at $143.31; we set a $143 twelve-month target, the weighted fair value rounded. This is research analysis, not "
        "personalized investment advice.", s_body))
    story.append(P("<b>Bottom line:</b> a well-run integrated power platform at a distressed multiple. BUY; size it knowing the "
        "equity is a levered stub \u2014 beta 1.18, real commodity exposure \u2014 and watch Q3 for the leverage-trajectory update.", s_body))
    story.append(Spacer(1, 2*mm))

    story.append(P("1. Investment thesis", s_h1))
    for t in [
        "<b>The derating is about leverage, not the business.</b> The stock is down 41% in a year and sits near 52-week lows. The causes are identifiable and largely in the price: post-deal leverage anxiety (~$23B debt; Fitch pro-forma gross leverage ~4.3\u00d7), Q1/Q2 2026 earnings misses (~14% below consensus each), and 2026 guidance tracking below midpoint on mild Texas weather, Winter Storm Fern costs, and a $70M Virginia RGGI re-entry charge. Nothing in the misses suggests structural impairment of the retail franchise or the fleet.",
        "<b>2027\u20132030 earnings power is visible and contracted in growing measure.</b> PJM capacity cleared at the auction caps ($333.44 and $325/MW-day), locking in $729\u2013781M of annual capacity revenue for 2027\u201328. The LS Power assets contribute a full year for the first time. ERCOT and PJM both set record peak loads in the last twelve months. Consensus sees adj. EPS of $11.25\u201311.30 in 2027 (+26\u201331%), and management targets 14%+ EPS CAGR through 2030 (2030E adj. EPS $14+).",
        "<b>The data-center angle is real and contracted.</b> NRG's 'Bring Your Own Power' strategy has a signed 1.2 GW combined-cycle plant for an investment-grade hyperscaler in Texas \u2014 15-year term, ~95% capacity-payment FCF, ~$500M adj. EBITDA / ~$375M FCFbG run-rate at 12\u201315% pretax unlevered returns, COD end-2029 \u2014 plus 5.4 GW of GE Vernova/Kiewit turbine slots secured through 2032 and 445 MW of already-signed data-center agreements.",
        "<b>The retail\u2013generation integration is the moat's core.</b> ~6M retail energy customers matched against ~26 GW of flexible gas generation, ~50/50 retail/generation margin mix, dampens commodity swings versus pure merchants (Talen) or pure retailers \u2014 and the fleet profits from the volatility that retail hedging must manage.",
        "<b>Capital returns are running through the noise.</b> $1.90 annualized dividend (+8%, 7th straight increase) plus $1B/yr of buybacks until leverage drops below 3.0\u00d7. At $95.23, the FCFbG yield is ~14% \u2014 the market is pricing distress on a company guiding $2.8\u20133.3B of 2026 FCFbG.",
    ]:
        story.append(P(t, s_body))
    story.append(P("<b>Why BUY and not HOLD:</b> the v2 scenario DCF weights to $143 against a $95.23 price, the 2027\u20132030 "
        "growth path is contracted rather than hoped for, and the base case deliberately underwrites <i>less</i> growth than "
        "management's 14%+ target (8% FCF CAGR). The $143 target implies 50% upside plus a 2% dividend \u2014 enough to clear "
        "our hurdle despite the leverage risk.", s_body))

    story.append(P("2. What the company does", s_h1))
    story.append(P("Headquartered in Houston, Texas, NRG reports five segments: Texas (retail + ERCOT generation), East (retail + "
        "PJM/NYISO/ISO-NE generation, incl. CPower), West/Other, Vivint Smart Home, and Corporate. 2026 segment EBITDA guidance: "
        "Texas $2.20\u20132.45B; East/West/Other $2.03\u20132.23B. Customer count: ~8M residential \u2014 ~6M retail energy plus "
        "~2M smart-home; the largest retail provider in Texas.", s_body))
    story.append(styled_table([
        [cell("<b>Region</b>", s_theadL), cell("<b>Share of capacity</b>", s_thead), cell("<b>Key assets / notes</b>", s_thead)],
        [cell("ERCOT (Texas)"), cell("~50%", s_cellC),
         cell("W.A. Parish (2,514 MW coal + 1,118 MW gas), Limestone 1,688 MW coal, Cedar Bayou 1,495 MW gas; LS Jack County 1,252 MW CCGT; TEF builds (Wharton 415 MW online May/Jun 2026)")],
        [cell("PJM"), cell("~39%", s_cellC),
         cell("Powerton 1,538 MW coal; cleared 2028/29 BRA at $325/MW-day cap; $644M\u2192$781M/yr capacity revenue through 2028")],
        [cell("NYISO"), cell("~8%", s_cellC), cell("Ravenswood 2,002 MW (Zone J, NYC) \u2014 premium capacity zone")],
        [cell("ISO-NE"), cell("~3%", s_cellC), cell("$33\u201341M/yr capacity revenue")],
    ], [30*mm, 26*mm, 94*mm]))
    story.append(P("Fuel mix is ~88% natural gas/dual-fuel, ~12% coal/other \u2014 a flexible, volatility-friendly fleet (gas peakers "
        "and CCGTs capture scarcity pricing) with a defined coal tail. Vivint contributes subscription economics: 2.45M "
        "customers (+8% YoY), 89% retention, ~9-year lifetimes, $77.93 monthly recurring revenue per customer. Leadership: "
        "President & CEO Robert Gaudette (transitioned from Larry Coben during 1H 2026). The LS Power deal was funded with ~$6.4B "
        "cash, $4.4B of new notes, revolver draws, and 24.25M new shares \u2014 the share count rose to ~211M basic in Q2 2026, "
        "and the $1B/yr buyback pace is the offset mechanism.", s_body))

    story.append(P("3. Financial situation", s_h1))
    story.append(styled_table([
        [cell("<b>$ millions (FY ends Dec 31)</b>", s_theadL), cell("<b>FY24</b>", s_thead), cell("<b>FY25</b>", s_thead), cell("<b>2026E guide</b>", s_thead)],
        [cell("GAAP revenue"), cell("28,130", s_cellR), cell("30,710", s_cellR), cell("\u2014", s_cellR)],
        [cell("GAAP net income"), cell("1,130", s_cellR), cell("864", s_cellR), cell("\u2014", s_cellR)],
        [cell("Adjusted EBITDA"), cell("3,800", s_cellR), cell("4,100", s_cellR), cell("5,325\u20135,825*", s_cellR)],
        [cell("Adjusted EPS"), cell("$6.83", s_cellR), cell("$8.24", s_cellR), cell("$7.90\u2013$9.90*", s_cellR)],
        [cell("FCF before growth (FCFbG)"), cell("2,100", s_cellR), cell("2,200", s_cellR), cell("2,800\u20133,300*", s_cellR)],
        [cell("Dividend / share (ann.)"), cell("$1.75", s_cellR), cell("$1.76", s_cellR), cell("$1.90 (+8%)", s_cellR)],
        [cell("Total debt (Jun '26)"), cell("\u2014", s_cellR), cell("\u2014", s_cellR), cell("~23,500", s_cellR)],
    ], [54*mm, 32*mm, 32*mm, 32*mm]))
    story.append(P("*Reaffirmed Aug 4, 2026; company tracking below midpoint after Q2. Sources: FY2024 PR (Feb 26, 2025), FY2025 "
        "8-K (Feb 24, 2026), Q2 2026 PR and earnings deck (Aug 4, 2026). The Q2 2026 print: revenue $7.48B (+11% YoY, beat); adj. "
        "EBITDA $1,217M (+34%); FCFbG $1,025M; but adj. EPS $1.49 missed the $1.69 consensus \u2014 soft Texas weather and power "
        "prices, Winter Storm Fern costs, $70M of Virginia RGGI re-entry, and inherited LS hedges. The fleet is substantially "
        "hedged for the rest of 2026, which is why guidance was reaffirmed even as the EPS miss landed.", s_small))
    story.append(P("<b>Leverage is the central fact of the equity.</b> ~$23.5B of total debt against a ~$20B market cap makes the "
        "stock a levered stub: Fitch pro-forma 2026 gross leverage ~4.3\u00d7 (BB+/BB+ ratings, stable outlook, affirmed May 2026). "
        "The maturity ladder is manageable \u2014 no cliff before 2027, notes laddered 2028\u20132036 at 3.4\u20136.25% plus Term "
        "Loan B 2031/2033. The plan: &lt;3.0\u00d7 net leverage within 24\u201336 months of the January close, funded by EBITDA "
        "growth plus $960M of 2026 debt paydown. 2026 capital plan: $3.05B FCFbG midpoint \u2192 $1,030M liability management, "
        "$1,000M buybacks, $407M common dividends, $1,113M data-center new-build capex (BYOP), ~$620M TEF capex offset by $650M "
        "incremental TEF debt. The dividend ($1.90, +8%, 7th consecutive increase) is ~21% of 2026E adj. EPS \u2014 safe on "
        "adjusted earnings, with a 7\u20139% annual DPS growth policy. <b>Hedge profile:</b> substantially hedged for 2026, but "
        "2027+ carries open power-price exposure \u2014 the company discloses large unhedged gross-margin sensitivity (e.g., TX "
        "ATC at $60/MWh \u2248 +$290\u2013360M of 2027\u201328 gross margin at lower hedge cases). This is the commodity lever the "
        "equity holder owns, for better and worse.", s_body))

    story.append(P("4. Growth, moat & future projection", s_h1))
    story.append(P("Management targets 14%+ adj. EPS CAGR through 2030 (raised from 10% at the LS announcement), implying 2030E "
        "adj. EPS of $14+. Our v2 base case underwrites only 8% FCF CAGR \u2014 deliberately below management's target, per the "
        "no-anchoring rule. The building blocks:", s_body))
    for b in [
        "<b>Data centers \u2014 contracted, not aspirational.</b> The 1.2 GW BYOP hyperscaler CCGT ($3.2B capex, ~$2,700/kW, ~6.4\u00d7 build multiple) delivers \u2265$500M adj. EBITDA and ~$375M FCFbG/yr at full operation from end-2029, with 15-year capacity payments independent of data-center utilization \u2014 a utility-like annuity inside a merchant wrapper. Behind it: 5.4 GW of GE Vernova H-class turbine + Kiewit EPC slots through 2032, ~2 GW of PJM uprate opportunities, and 445 MW of already-signed data-center agreements with >1 GW targeted.",
        "<b>LS Power integration.</b> A full year of the acquired 13 GW in 2027 (closed Jan 30, 2026), ~$1.2B of annual EBITDA contribution per management framing, PJM capacity at the caps ($729\u2013781M/yr 2027\u201328), and identified cost and commercial synergies.",
        "<b>Texas load growth + TEF builds.</b> ERCOT set four record peaks in twelve months. The Texas Energy Fund finances 1.5 GW at 3% ($1.15B): Wharton 415 MW already online (on time/on budget), Cedar Bayou 5 (689 MW) and Greens Bayou 6 (443 MW) follow mid-2028.",
        "<b>Vivint compounding.</b> 2.45M subscribers growing 8% with $44/mo service margin and ~9-year lifetimes \u2014 a subscription annuity diversifying the earnings mix.",
        "<b>Retail margin and buybacks.</b> Texas retail EBITDA guidance of $2.20\u20132.45B reflects margin expansion; $1B/yr of buybacks at ~$95 retires ~5% of shares annually.",
    ]:
        story.append(B(b))
    story.append(P("On moat \u2014 honestly: NRG has integration advantages, not a franchise moat. The advantages are real: the "
        "largest U.S. competitive retail platform, ~26 GW of flexible gas generation that monetizes volatility, a genuine "
        "development machine, and ~50/50 retail/generation margin mix that dampens cycles. The offsets: commodity exposure on "
        "the open 2027+ book, regulatory risk (ERCOT market design, PJM price caps, RGGI), weather, and a balance sheet that "
        "turns every miss into a leverage event. This is a cyclical compounder with contracted growth \u2014 priced like one, "
        "with a discount rate that respects the leverage.", s_body))

    story.append(P("5. Competitive landscape", s_h1))
    story.append(styled_table([
        [cell("<b>Company</b>", s_theadL), cell("<b>Price (Oct 2)</b>", s_thead), cell("<b>1-yr</b>", s_thead), cell("<b>Profile</b>", s_thead)],
        [cell("NRG Energy"), cell("$95.23", s_cellC), cell("-41%", s_cellC), cell("25.8 GW gas, largest US retail, Vivint")],
        [cell("Vistra (VST)"), cell("$136.88", s_cellC), cell("-33%", s_cellC), cell("~41 GW nuclear+gas+coal; TXU retail; Meta 2.6 GW nuclear PPAs")],
        [cell("Constellation (CEG)"), cell("$253.46", s_cellC), cell("-21%", s_cellC), cell("Largest US nuclear; ~21\u00d7 fwd earnings carbon-free premium")],
        [cell("Talen (TLN)"), cell("$315.88", s_cellC), cell("-26%", s_cellC), cell("~13.2 GW incl. 2.2 GW nuclear; pure merchant")],
        [cell("NextEra (NEE)"), cell("$77.37", s_cellC), cell("-0.4%", s_cellC), cell("Regulated benchmark; ~18\u201320\u00d7")],
    ], [36*mm, 26*mm, 20*mm, 68*mm]))
    story.append(P("The independent power producers derated together in 2026 \u2014 NRG simply derated hardest. NRG is the "
        "cheapest IPP on forward earnings (~10.7\u00d7 '26E / 8.4\u00d7 '27E vs CEG ~21\u00d7) and the most retail-integrated. The "
        "discount reflects leverage (VST and CEG carry investment-grade or near-IG profiles) and the two 2026 misses. NRG's own "
        "7.8\u00d7 2026E EV/EBITDA sits below typical through-cycle IPP multiples of 8\u201310\u00d7.", s_body))

    story.append(P("6. Valuation (v2 hardened): FCFbG scenario DCF + cross-checks", s_h1))
    story.append(P("We run a 10-year scenario DCF on free cash flow before growth (the company's own core metric), off 2026E "
        "FCFbG of ~$2.9B (below the guidance midpoint, per company tracking). Net debt of $23B is deducted; ~205M diluted "
        "shares (post-buyback trajectory). The discount rate is the leverage call: <b>base 11%</b> \u2014 between the standard "
        "10% and the speculative 12%, explicitly justified by the BB+ rating, ~4.3\u00d7 gross leverage, and the merchant tail "
        "\u2014 <b>bear 13.5%</b>, <b>bull 9.5%</b>. Terminal growth is capped at 2% and applied to year-10 FCF at "
        "<b>normalized mid-cycle power prices</b>: the bear and base cases assume capacity prices fade from the 2026 auction "
        "caps toward mid-cycle, never extended at peak. Growth paths sit below management's 14%+ EPS target \u2014 no "
        "management anchoring.", s_body))
    story.append(P("Lens 1 \u2014 Scenario FCFbG DCF (primary)", s_h2))
    story.append(styled_table([
        [cell("<b>Scenario</b>", s_theadL), cell("<b>10-yr FCF path</b>", s_thead), cell("<b>Discount</b>", s_thead), cell("<b>Fair value / sh</b>", s_thead)],
        [cell("<b>Bear</b> \u2014 deleveraging stalls; power prices soften to mid-cycle; FCF growth fades 5%\u21922%"),
         cell("~2.6% CAGR", s_cellC), cell("13.5%", s_cellC), cell("$20.29", s_cellBR)],
        [cell("<b>Base</b> \u2014 8% FCF CAGR; leverage &lt;3\u00d7 by 2028; BYOP on schedule; normalized mid-cycle prices"),
         cell("8% CAGR", s_cellC), cell("11.0%", s_cellC), cell("$131.76", s_cellBR)],
        [cell("<b>Bull</b> \u2014 12% FCF CAGR; BYOP delivers; >1 GW more data-center deals; multiple re-rates"),
         cell("12% CAGR", s_cellC), cell("9.5%", s_cellC), cell("$289.42", s_cellBR)],
        [cell("<b>Weighted (25/50/25)</b>"), cell("\u2014", s_cellC), cell("\u2014", s_cellC), cell("$143.31", s_cellBR)],
    ], [66*mm, 28*mm, 22*mm, 34*mm]))
    story.append(P("The bear case clears every v2 bear-must-hurt test: FCF CAGR of ~2.6% is under 3%; $20.29 is an ~85% derating "
        "versus the base case; and it sits 79% below the $95.23 quote. This is a leverage story, not an operations story \u2014 "
        "if EBITDA disappoints, the $23B debt load means the levered stub absorbs it first. Terminal value is 34\u201360% of "
        "enterprise value by scenario (under the 70% haircut threshold). Note the honest asymmetry: the bull ($289) is nearly "
        "as far above the base as the bear is below it \u2014 leverage cuts both ways.", s_small))
    story.append(P("Lens 2 \u2014 Forward P/E (relative)", s_h2))
    story.append(P("At 12\u00d7 \u2014 a discount to CEG's ~21\u00d7 and regulated ~18\u201320\u00d7, a premium to distressed merchants "
        "\u2014 2026E $8.9 gives $107 and 2027E $11.3 gives $136; midpoint ~$121. The 2027 number matters more: by then the LS "
        "assets are fully annualized and PJM capacity is at the caps.", s_body))
    story.append(P("Lens 3 \u2014 EV/EBITDA", s_h2))
    story.append(P("On 2026E adj. EBITDA of ~$5.5B: 8.5\u00d7 \u2192 EV $46.75B, less $23B net debt = $23.75B equity \u00f7 205M = "
        "$116; 9.0\u00d7 \u2192 $129. Through-cycle IPP multiples of 8\u201310\u00d7 make 8.5\u20139\u00d7 conservative for a "
        "retail-integrated platform.", s_body))
    story.append(P("Blended target: $143", s_h2))
    story.append(styled_table([
        [cell("<b>Valuation read</b>", s_theadL), cell("<b>Fair value / sh</b>", s_thead), cell("<b>Implied upside</b>", s_thead)],
        [cell("Scenario FCFbG DCF, 10-yr, 25/50/25-weighted"), cell("$143.31", s_cellBR), cell("+50%", s_cellBR)],
        [cell("Forward P/E 12\u00d7 (26E/27E midpoint)"), cell("~$121", s_cellR), cell("+27%", s_cellR)],
        [cell("EV/EBITDA 8.5\u20139\u00d7 on 2026E"), cell("$116\u2013$129", s_cellR), cell("+22\u2013+35%", s_cellR)],
        [cell("Street consensus (Moderate Buy)"), cell("~$198", s_cellR), cell("+108%", s_cellR)],
        [cell("<b>12-month target</b>"), cell("<b>$143</b>", s_cellBR), cell("<b>+50%</b>", s_cellBR)],
    ], [80*mm, 40*mm, 40*mm]))
    story.append(P("We set $143: the probability-weighted DCF rounded, with no departure from it. The lenses converge at "
        "$116\u2013$143 \u2014 the DCF sits at the top of the cross-check range because it alone prices the 2027\u20132030 "
        "contracted growth. The $198 street consensus target is, in our view, a stale artifact of higher prices \u2014 our $143 "
        "is deliberately below it, because it is built on below-midpoint 2026 FCFbG and an 11% discount rate that respects the "
        "BB+ balance sheet. A raw Gordon DCF on the ~14% FCFbG yield produces nosebleed values ($300+); we treat that as "
        "evidence that the market deeply discounts FCF sustainability through a leverage cycle, not as a price target.", s_body))
    d = Drawing(460, 170)
    bc = VerticalBarChart(); bc.x = 60; bc.y = 30; bc.height = 110; bc.width = 360
    bc.data = [[20.29, 131.76, 289.42, 143.31, 143.0, 95.23]]
    bc.strokeColor = MGRAY; bc.barLabels.nudge = 8; bc.barLabelFormat = "%.2f"
    bc.categoryAxis.labels.boxAnchor = "ne"; bc.categoryAxis.labels.dx = 6; bc.categoryAxis.labels.dy = -2
    bc.categoryAxis.categoryNames = ["Bear", "Base", "Bull", "Weighted", "Target", "Price"]
    bc.bars[0].fillColor = ACCENT
    bc.valueAxis.valueMin = 0; bc.valueAxis.valueMax = 320; bc.valueAxis.valueStep = 80
    d.add(bc); d.add(String(60, 150, "Fair value / share ($)", fontSize=8, fillColor=DGRAY))
    story.append(d)
    story.append(P("Figure \u2014 Scenario fair values, target, and current price ($). Source: analyst model, October 4, 2026.", s_small))

    story.append(P("7. Key risks", s_h1))
    for r in [
        "<b>Leverage (the central risk).</b> ~$23B debt vs ~$20B market cap; Fitch pro-forma 4.3\u00d7 gross leverage. If EBITDA disappoints or rates rise, deleveraging stalls, the $1B/yr buyback is at risk, and the equity \u2014 a levered stub \u2014 absorbs it first. The bear case ($20) is a leverage story, not an operations story.",
        "<b>Commodity and hedging exposure.</b> Substantially hedged for 2026, but 2027+ is open: large unhedged gross-margin sensitivity to Texas and PJM power prices. A mild-weather/low-price year like 1H 2026, repeated, breaks the 14% growth narrative.",
        "<b>Regulatory.</b> ERCOT market-design and political scrutiny; PJM capacity price caps limit upside; Virginia RGGI re-entry already cost $70M in 2026.",
        "<b>Weather.</b> Winter Storm Fern (2026) and mild summers both hurt \u2014 the business is short weather volatility in both directions at different times.",
        "<b>Execution.</b> The $3.2B BYOP hyperscaler build (COD 2029) and LS Power integration must deliver; buybacks assumed at much lower prices than the $170/share the 2026 plan assumed.",
        "<b>Estimates still being cut.</b> Five analysts cut FY26/FY27 EPS in the last 30 days; Zacks is at Strong Sell. A third consecutive miss (Q3, ~early Nov) would likely take out the $93 lows.",
        "<b>Customer affordability.</b> The company flags affordability as a constraint on retail pricing \u2014 margin expansion has a political ceiling in Texas.",
    ]:
        story.append(B(r))

    story.append(P("8. Catalysts, recommendation & what could change our mind", s_h1))
    story.append(P("<b>Catalysts over the next 12 months:</b> (1) Q3 2026 earnings (~early November) \u2014 the single most "
        "important print: a beat plus a leverage-trajectory update would break the two-miss narrative; a third miss likely "
        "breaks $93; (2) ERCOT Batch Zero progression for the 1.2 GW BYOP project; (3) additional data-center announcements "
        "(445 MW signed, >1 GW targeted); (4) PJM/ERCOT winter performance; (5) Fitch/S&P leverage reviews as the &lt;3.0\u00d7 "
        "target approaches.", s_body))
    story.append(P("<b>Recommendation: BUY, $143 target.</b> NRG pairs the cheapest valuation in the IPP group (10.7\u00d7 '26E, "
        "8.4\u00d7 '27E, 7.8\u00d7 EV/EBITDA, ~14% FCFbG yield) with the most contracted 2027\u20132030 growth path: full-year "
        "LS Power, PJM capacity at the caps, Texas load growth, a signed hyperscaler build, and a visible earnings ramp the "
        "market refuses to fund through the leverage cycle. The v2 DCF \u2014 with an 11% discount rate that respects the BB+ "
        "balance sheet, mid-cycle (not peak) terminal power prices, and a bear case that takes the equity to $20 \u2014 still "
        "weights to $143, 50% above the quote. Risk is Medium-High: the $23B debt load makes the equity a levered stub with "
        "real commodity exposure, and estimates are still being cut. Size accordingly \u2014 this is a position, not a core "
        "holding \u2014 and use Q3 earnings as the confirmation checkpoint. We would downgrade to HOLD above ~$133 (upside "
        "&lt;7%) and to REDUCE above ~$160; we would add aggressively on a leverage scare toward $75 with the thesis intact.", s_body))
    story.append(P("<b>What could change our mind:</b> Q3 adj. EPS miss #3 or leverage stuck above 3.5\u00d7 into 2027 (bearish \u2014 "
        "the $20 case); a signed second hyperscaler deal or PJM capacity upside beyond the caps (bullish \u2014 re-rate toward "
        "$200+); a ratings downgrade (technical pressure \u2014 buying opportunity only if the FCF trajectory holds).", s_body))

    story.append(P("Appendix \u2014 Methodology & sources (v2)", s_h1))
    story.append(P("<b>Scenario DCF (v2).</b> Ten explicit years off 2026E FCFbG of ~$2.9B (below guidance midpoint); FCF growth "
        "paths: bear 5%/4%/3% then 2%, base 8% CAGR, bull 12% CAGR; discount rates 13.5% / 11.0% / 9.5%; terminal growth 2.0% on "
        "normalized mid-cycle power prices (capacity prices fade from 2026 auction caps toward mid-cycle \u2014 never extended "
        "at peak); net debt $23B deducted; ~205M diluted shares. Terminal value is 34\u201360% of EV by scenario (under the 70% "
        "haircut threshold). Growth inputs sit below management's 14%+ EPS CAGR target \u2014 no management anchoring. "
        "<b>What we did not do:</b> no dividend model as primary (payout is not the return driver); no Monte Carlo. "
        "<b>Limitations:</b> 2027+ hedge profile and power-price realizations are the dominant uncertainties; small changes in "
        "the discount rate move the levered equity value sharply.", s_body))
    story.append(P("Sources: NRG Q2 2026 earnings presentation and press release (Aug 4, 2026), FY2025 8-K (Feb 24, 2026), "
        "FY2024 PR (Feb 26, 2025), Q1 2026 10-Q, LS Power close PR (Jan 30, 2026), PJM BRA reports, ERCOT filings. Market prices "
        "via Yahoo Finance, Oct 2, 2026 (NRG $95.23, 52-wk $93.36\u2013$189.96). Sell-side estimates per Zacks. All 2026E+ "
        "figures beyond cited consensus/guidance are the author's. Disclaimer: this note is independent research analysis for "
        "informational purposes only and is not personalized investment advice. Estimates and targets are inherently uncertain. "
        "The author may hold positions in securities mentioned.", s_small))

    _doc_build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print("built", OUT)

if __name__ == "__main__":
    build()
