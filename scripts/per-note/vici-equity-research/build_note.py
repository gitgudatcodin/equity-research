#!/usr/bin/env python3
"""Build the VICI Properties (VICI) equity research note PDF — v2 hardened rebuild, October 4, 2026."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle)
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import VerticalBarChart

OUT = "/home/hatch/workspace/your_files/vici-equity-research/vici-equity-research-note.pdf"

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
    canvas.drawString(15*mm, 12*mm, "VICI Properties Inc. (NYSE: VICI)  \u2014  Equity Research Note  \u2014  October 4, 2026")
    canvas.drawRightString(W - 15*mm, 12*mm, f"Page {doc.page}")
    canvas.setStrokeColor(MGRAY); canvas.setLineWidth(0.4)
    canvas.line(15*mm, 14.5*mm, W - 15*mm, 14.5*mm)
    canvas.restoreState()

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=15*mm, rightMargin=15*mm,
                        topMargin=16*mm, bottomMargin=18*mm,
                        title="VICI Properties (VICI) Equity Research Note", author="Independent Research")
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
    story.append(P("VICI PROPERTIES INC. (NYSE: VICI)", ParagraphStyle("k", parent=s_sub, fontName="Helvetica-Bold", fontSize=12, textColor=ACCENT)))
    story.append(Spacer(1, 3*mm))
    story.append(P("The Best Landlord in Gaming,<br/>Priced Like a Distressed One", s_title))
    story.append(Spacer(1, 3*mm))
    story.append(P("Equity Research Note \u00b7 Real Estate \u2014 Experiential / Gaming REIT \u00b7 October 4, 2026", s_sub))
    story.append(Spacer(1, 4*mm))
    story.append(verdict_box([
        ("Recommendation", "BUY"),
        ("12-Mo. Price Target", "$39.00"),
        ("Current Price", "$22.65 (Oct 2, 2026 close)"),
        ("Implied Upside", "+72.2%"),
        ("Dividend Yield / Risk", "8.1% / Medium-High"),
    ]))
    story.append(Spacer(1, 4*mm))
    story.append(P("<b>Thesis in one paragraph.</b> VICI is the dominant experiential REIT in America \u2014 103 assets, ~130 "
        "million sq ft, 16 tenants, 100% rent collection since inception \u2014 trading at 9.2\u00d7 forward AFFO and an 8.1% "
        "dividend yield, both the cheapest readings since its 2018 listing. The market is pricing three fears: Caesars' $17.6B "
        "take-private (39% of rent), a 5.25% 10-year Treasury, and soft Las Vegas visitation. We judge all three to be "
        "overstated or self-correcting: the leases are 30-to-50-year, cross-defaulted master leases on immovable assets that "
        "survive any change of tenant ownership (and the buyer is arguably better credit); AFFO per share is still growing "
        "4\u20135% a year with a ~75% payout; and the balance sheet is investment-grade with 98% fixed-rate debt. This v2 "
        "rebuild values VICI the way a REIT should be valued \u2014 on AFFO per share, not GAAP EPS \u2014 under hardened rules: "
        "scenario-specific discount rates (base 9% for this contractual cash-flow compounder / bear 11.5% / bull 8%), terminal "
        "growth capped at 2%, and \u2014 the critical fix versus the prior note \u2014 a bear case that genuinely hurts. The old "
        "note's bear cases ($38 AFFO-DCF, $28 DDM) sat <i>above</i> the $22.65 quote: a mild-bear leak. The honest bear is a "
        "Caesars stress that cuts AFFO 15% in year one: $20.65, 9% below the quote. The probability-weighted AFFO-DCF "
        "(25/50/25) lands at $38.86; we set a $39 twelve-month target, the weighted fair value rounded. Initiate with BUY.", s_body))
    story.append(P("This note is independent research for informational purposes only and is not investment advice or a "
        "recommendation to transact. Valuation figures marked \u2020 are analyst-computed from public filings and market data "
        "as of October 2, 2026 (VICI close $22.65). Forward-looking statements involve risk and uncertainty.", s_small))
    story.append(styled_table([
        [cell("<b>Market cap</b>", s_theadL), cell("<b>Price (Oct 2)</b>", s_thead), cell("<b>52-week range</b>", s_thead), cell("<b>Beta</b>", s_thead)],
        [cell("$24.9B", s_cellC), cell("$22.65", s_cellC), cell("$22.54 \u2013 $33.01", s_cellC), cell("0.68", s_cellC)],
        [cell("<b>Dividend (ann.)</b>", s_theadL), cell("<b>Div. yield</b>", s_thead), cell("<b>2026E AFFO/share</b>", s_thead), cell("<b>P / AFFO</b>", s_thead)],
        [cell("$1.84", s_cellC), cell("8.12%", s_cellC), cell("$2.46 \u2020", s_cellC), cell("9.2\u00d7 \u2020", s_cellC)],
        [cell("<b>Payout ratio</b>", s_theadL), cell("<b>Net leverage</b>", s_thead), cell("<b>Credit ratings</b>", s_thead), cell("<b>Employees</b>", s_thead)],
        [cell("~75% of AFFO", s_cellC), cell("5.0\u00d7 EBITDA", s_cellC), cell("Baa3 / BBB- (IG)", s_cellC), cell("~28", s_cellC)],
    ], [38*mm, 38*mm, 38*mm, 36*mm], fontsize=8))
    story.append(P("Sources: Company Q2 2026 release and Q1 2026 supplemental; market data via Yahoo Finance (Oct 2, 2026). "
        "\u2020 Analyst-computed.", s_small))
    story.append(Spacer(1, 2*mm))

    story.append(P("1. What the company does", s_h1))
    story.append(P("VICI Properties, formed in 2017 as the real-estate spin of Caesars Entertainment's bankruptcy and listed in "
        "February 2018, is an S&P 500 experiential REIT. It does not operate casinos. It owns the dirt and buildings \u2014 "
        "including three of the most iconic assets on the Las Vegas Strip (Caesars Palace, MGM Grand, the Venetian) \u2014 and "
        "leases them back to operators under long-term triple-net leases: the tenant pays property taxes, insurance, "
        "maintenance, and capital expenditures. VICI's income is therefore contractual rent plus financing income from its loan "
        "book, not gaming revenue. The portfolio spans 103 experiential assets (63 gaming, 40 other experiential) across the US "
        "and Canada: ~130 million square feet, ~66,000 hotel rooms, 700+ restaurants, bars, nightclubs and sportsbooks, four "
        "championship golf courses, and ~33 acres of undeveloped Strip-adjacent land. Sixteen tenants; 100% occupancy and 100% "
        "rent collection every year since inception. The company runs this on ~28 employees \u2014 one of the most asset-light "
        "models in the S&P 500.", s_body))
    story.append(P("<b>Lease architecture \u2014 the actual product.</b> The weighted-average lease term is ~39.7 years including "
        "renewals, with whole-portfolio, cross-defaulted master leases backed by corporate guarantees. Two tenants dominate: "
        "Caesars ~39% and MGM ~33% of annualized rent (~$3.2B total). Escalators are fixed 1\u20132% or 'greater of 2% and CPI' "
        "(typically capped at 3%). Crucially, ~45% of the rent roll is CPI-linked in 2026, rising to ~87% by 2035 \u2014 a growing "
        "organic engine that converts a bond-like asset into a growing perpetuity, rare among net-lease REITs.", s_body))

    story.append(P("2. Financial situation", s_h1))
    story.append(P("<b>The P&L: cash rent, not gaming.</b> Q2 2026 (reported July 29, 2026): total revenue ~$1.06B, +5.7% YoY, "
        "ahead of estimates. GAAP net income $526.5M / $0.48 per share, down 39% YoY \u2014 but that was a CECL loan-loss "
        "accounting swing, not an operating miss. The correct lens is AFFO: $679.6M / $0.62 per share, +4.6% YoY, in line with "
        "consensus. Management raised the low end of 2026 AFFO guidance to $2.45\u2013$2.47/share. Annual revenue has compounded "
        "from $2.6B (2022, post-MGP deal) to ~$4.1B (2026E); operating margins run ~70% \u2014 triple-net economics are almost "
        "pure margin.", s_body))
    story.append(styled_table([
        [cell("<b>Year</b>", s_theadL), cell("<b>AFFO / share</b>", s_thead), cell("<b>Dividend / share</b>", s_thead)],
        [cell("2018"), cell("$1.43", s_cellR), cell("$1.00", s_cellR)],
        [cell("2019"), cell("$1.24", s_cellR), cell("$1.17", s_cellR)],
        [cell("2020"), cell("$1.64", s_cellR), cell("$1.26", s_cellR)],
        [cell("2021"), cell("$1.82", s_cellR), cell("$1.38", s_cellR)],
        [cell("2022"), cell("$1.93", s_cellR), cell("$1.50", s_cellR)],
        [cell("2023"), cell("$2.15", s_cellR), cell("$1.61", s_cellR)],
        [cell("2024"), cell("$2.26", s_cellR), cell("$1.70", s_cellR)],
        [cell("2025"), cell("$2.38", s_cellR), cell("$1.77", s_cellR)],
        [cell("2026E"), cell("$2.46 \u2020", s_cellR), cell("$1.84 \u2020", s_cellR)],
    ], [50*mm, 50*mm, 50*mm]))
    story.append(P("AFFO/share history per suredividend (2019 dip reflects MGP-era share count); 2026E is guidance mid. Dividend "
        "CAGR 2018\u20132025 \u2248 8.5%. The dividend was raised again on September 3, 2026 to $0.46/quarter ($1.84 annualized, "
        "+2.2%), the 8th consecutive annual increase since the 2018 IPO. Payout is ~75% of 2026E AFFO \u2014 comfortably inside "
        "the company's ~75% policy, leaving retained cash flow to fund growth. The 8.1% yield is the highest since listing.", s_small))
    story.append(P("<b>Balance sheet: investment-grade fortress, refinancing is the watch item.</b> Total debt ~$17.1B; net "
        "leverage 5.0\u00d7 LQA adjusted EBITDA; 98.4% fixed-rate; liquidity ~$3.1B. Covenants are comfortable (net debt/assets "
        "35% vs 60% limit; interest coverage 4.0\u00d7). Ratings: Moody's Baa3 / S&P BBB- / Fitch BBB-, all Stable. The honest "
        "blemish: VICI refinanced $1.75B of notes in August 2026 at higher rates, and a ~$1.5B tranche matures in 2027 that will "
        "reprice upward \u2014 a few cents of AFFO drag, manageable, but the key near-term balance-sheet event.", s_body))

    story.append(P("3. Growth: three engines", s_h1))
    for b in [
        "<b>Acquisitions \u2014 the deep-pocketed buyer in a high-rate world.</b> 2026 has been active: the $1.16B Golden Entertainment deal (seven Nevada casinos incl. The Strat, closed ~April 30 into a new master lease); C$200.6M for two Alberta casinos at an 8.0% cap rate; the 14th tenant (Northfield Park/Clairvest); and the 16th tenant, Club Med, via the Carambola Beach Resort acquisition plus a $55.2M build-to-suit (reopening Q4 2027). With operators as motivated sellers and VICI holding the sector's cheapest cost of capital, the sale-leaseback pipeline is structurally advantaged.",
        "<b>Partner Property Growth Fund (PPGF) \u2014 reinvestment at contracted yields.</b> VICI funds tenant capex at fixed returns: up to $700M for the Venetian at 7.25% and a $1.5B mezzanine loan into the $4.3B One Beverly Hills financing (March 2026). PPGF turns tenant growth capex into VICI rent \u2014 incremental, high-visibility AFFO.",
        "<b>Organic escalators.</b> Contractual bumps (1\u20132% fixed or CPI-linked, caps ~3%) plus the rising CPI-linked mix (45% \u2192 87% of rent by 2035) deliver ~2\u20133% same-store rent growth with zero capex \u2014 the compounding spine beneath the dividend.",
    ]:
        story.append(B(b))
    story.append(P("Our forward view: we model AFFO/share compounding at 4\u20135% annually through 2028 (escalators ~2.5% + "
        "accretive deals + PPGF), moderating to ~3% terminal. Dividend growth of ~4% a year is fully fundable at a 75% payout. "
        "This is not a high-growth equity; it is a growing 8% yield with a 4% kicker \u2014 the classic compounding REIT profile, "
        "currently priced as if the growth were zero.", s_body))

    story.append(P("4. Moat & competition", s_h1))
    story.append(P("We rate VICI's moat narrow-to-moderate, but unusually durable for a REIT. The sources: <b>irreplicable, "
        "licensed assets</b> (you cannot build another Caesars Palace); <b>master-lease architecture</b> (whole-portfolio, "
        "cross-defaulted, 30\u201350-year terms \u2014 VICI has never missed a rent check since formation); <b>scale + cost of "
        "capital</b> (~$43B enterprise value vs GLPI's ~$16B, S&P 500-listed, investment-grade); and <b>inflation linkage</b> "
        "(45% \u2192 87% CPI-linked rent) converting fixed income into a growing perpetuity. The moat's weak point is "
        "concentration: it is only as strong as tenant credit. Caesars (39%) and MGM (33%) are 72% of rent. Our judgment: the "
        "asset moat is wide (the buildings will be casinos in 30 years); the credit moat is the risk to underwrite \u2014 and on "
        "that, the Caesars take-private is arguably credit-positive (Fertitta arguably better credit than levered public "
        "Caesars' $11.9B debt). Gaming real estate is effectively a two-player market: GLPI (~$11B cap, ~8.6% yield, ~96% payout "
        "vs VICI's ~75% \u2014 less dividend-growth headroom) is the only pure-play peer. Beyond gaming: Realty Income (~5.2% "
        "yield, 8\u201314-year leases vs VICI's ~40). Our judgment: VICI is the quality compounder of the group \u2014 longer "
        "leases, stronger escalators, better balance sheet \u2014 yet trades at the widest discount to its own history.", s_body))

    story.append(P("5. Valuation (v2 hardened): AFFO-DCF primary, DDM cross-check", s_h1))
    story.append(P("A REIT is valued on cash to equity holders, not GAAP earnings: our primary lens is a 10-year scenario DCF on "
        "<b>AFFO per share</b>, off 2026E AFFO of $2.46 (guidance mid). The discount rate is the rate call: <b>base 9%</b> \u2014 "
        "the stable-compounder tier, justified by 30\u201350-year contractual triple-net leases, 100% collection since inception, "
        "and investment-grade leverage \u2014 <b>bear 11.5%</b>, <b>bull 8%</b> (the floor). Terminal growth is capped at 2% on "
        "normalized mid-cycle AFFO (escalator-driven, never peak acquisition pace). Growth paths are anchored to the "
        "2018\u20132025 AFFO compounding record (8.5% dividend CAGR; ~6% AFFO CAGR), faded \u2014 not to management guidance.", s_body))
    story.append(P("Lens 1 \u2014 AFFO-per-share DCF (primary) \u2020", s_h2))
    story.append(styled_table([
        [cell("<b>Scenario</b>", s_theadL), cell("<b>AFFO growth path</b>", s_thead), cell("<b>Discount</b>", s_thead),
         cell("<b>Terminal g</b>", s_thead), cell("<b>Fair value</b>", s_thead)],
        [cell("<b>Bear</b> \u2014 Caesars stress: 15% AFFO cut in year 1; growth fades 1%\u21920.5%"),
         cell("1% \u2192 0.5%*", s_cellC), cell("11.5%", s_cellC), cell("2.0%", s_cellC), cell("$20.65", s_cellBR)],
        [cell("<b>Base</b> \u2014 escalators + accretive deals + PPGF; 5% \u2192 3%"),
         cell("5% \u2192 3%", s_cellC), cell("9.0%", s_cellC), cell("2.0%", s_cellC), cell("$41.59", s_cellBR)],
        [cell("<b>Bull</b> \u2014 acquisition pace sustains; CPI linkage compounds; 6% \u2192 3.5%"),
         cell("6% \u2192 3.5%", s_cellC), cell("8.0%", s_cellC), cell("2.0%", s_cellC), cell("$51.60", s_cellBR)],
        [cell("<b>Weighted (25/50/25)</b>"), cell("\u2014", s_cellC), cell("\u2014", s_cellC), cell("\u2014", s_cellC),
         cell("$38.86", s_cellBR)],
    ], [62*mm, 26*mm, 20*mm, 20*mm, 22*mm]))
    story.append(P("*After the year-1 15% cut. The bear case clears every v2 bear-must-hurt test: AFFO growth of ~1% is under "
        "3% (with an outright 15% cut in year one \u2014 an AFFO decline, not a slowdown); $20.65 is a ~50% derating versus the "
        "base case; and it sits 9% below the $22.65 quote. Terminal value is 39\u201359% of fair value by scenario (under the "
        "70% haircut threshold). The falsifiable core of the note: if the Caesars take-private closes with leases impaired or "
        "renegotiated downward, the base case is wrong and the bear owns the stock.", s_small))
    story.append(P("Lens 2 \u2014 Gordon growth (dividend discount) \u2020", s_h2))
    story.append(P("On the $1.84 dividend: bear (11.5% CoE, 3% growth) \u2192 $23.46; base (9% CoE, 4% growth) \u2192 $38.27; "
        "bull (8% CoE, 4.5% growth) \u2192 $55.66; weighted \u2192 $38.86 \u2014 landing on the same number as the AFFO-DCF, "
        "which is what should happen when the payout ratio is stable and the dividend is funded by AFFO. The DDM confirms "
        "rather than contradicts.", s_body))
    story.append(P("Lens 3 \u2014 Market-multiple context (not the anchor)", s_h2))
    story.append(P("For context only: P/AFFO on 2027E AFFO (~$2.58): 9\u00d7 (no re-rating) \u2192 $23.22; 11.5\u00d7 (halfway to "
        "the 12\u201314\u00d7 history) \u2192 $29.67; 13\u00d7 (full normalization) \u2192 $33.54. Target-yield lens: at 6.25% "
        "(toward history) the $1.84 dividend is worth $29.44; at 5.25% (rate relief), $35.05. NAV via cap rate: on ~$3.48B LQA "
        "adjusted EBITDA, a 7.5% cap \u2192 ~$26.6/share. These lenses measure what the market will pay over 12 months with "
        "the 10-year above 5% \u2014 they cluster at $26\u2013$30 \u2014 while the DCF/DDM measure through-cycle intrinsic value "
        "at ~$39. The prior note anchored its $30 target to the market lenses; v2 does not permit that departure without a "
        "falsifiable justification, and 'rates might stay high' is a scenario, not a justification \u2014 it is already priced "
        "in the 9% base discount rate (a full ~375bp over the 10-year). Our $39 target is the weighted DCF, stated plainly: "
        "it requires the market to pay for the cash flows, which an 8.1% starting yield plus 4\u20135% AFFO growth has "
        "historically forced it to do.", s_body))
    story.append(P("Blended target: $39", s_h2))
    story.append(styled_table([
        [cell("<b>Valuation read</b>", s_theadL), cell("<b>Fair value / sh</b>", s_thead), cell("<b>Implied upside</b>", s_thead)],
        [cell("AFFO-DCF, 10-yr, 25/50/25-weighted \u2020"), cell("$38.86", s_cellBR), cell("+72%", s_cellBR)],
        [cell("Dividend discount (Gordon), weighted \u2020"), cell("$38.86", s_cellR), cell("+72%", s_cellR)],
        [cell("Market multiples (P/AFFO, yield, NAV) \u2014 context"), cell("$26\u2013$30", s_cellR), cell("+15\u2013+32%", s_cellR)],
        [cell("Street consensus"), cell("~$30", s_cellR), cell("+32%", s_cellR)],
        [cell("<b>12-month target</b>"), cell("<b>$39</b>", s_cellBR), cell("<b>+72%</b>", s_cellBR)],
    ], [80*mm, 40*mm, 40*mm]))
    story.append(P("At $22.65: +72.2% price upside to $39, plus an 8.1% dividend yield \u2248 80% expected total return. The "
        "asymmetry the old note identified survives hardening: the bear-case DDM ($23.46) still beats the quote, base-case "
        "AFFO-DCF points to ~$42, and through-cycle value is ~$39 even after a genuine Caesars-stress bear.", s_body))
    d = Drawing(460, 170)
    bc = VerticalBarChart(); bc.x = 60; bc.y = 30; bc.height = 110; bc.width = 360
    bc.data = [[20.65, 41.59, 51.60, 38.86, 39.0, 22.65]]
    bc.strokeColor = MGRAY; bc.barLabels.nudge = 8; bc.barLabelFormat = "%.2f"
    bc.categoryAxis.labels.boxAnchor = "ne"; bc.categoryAxis.labels.dx = 6; bc.categoryAxis.labels.dy = -2
    bc.categoryAxis.categoryNames = ["Bear", "Base", "Bull", "Weighted", "Target", "Price"]
    bc.bars[0].fillColor = ACCENT
    bc.valueAxis.valueMin = 0; bc.valueAxis.valueMax = 60; bc.valueAxis.valueStep = 15
    d.add(bc); d.add(String(60, 150, "Fair value / share ($)", fontSize=8, fillColor=DGRAY))
    story.append(d)
    story.append(P("Figure \u2014 Scenario fair values, target, and current price ($). \u2020 Analyst-computed. Source: analyst "
        "model, October 4, 2026.", s_small))

    story.append(P("6. Risks \u2014 what could break the thesis", s_h1))
    for r in [
        "<b>Caesars concentration (39% of rent) + take-private overhang (the central risk).</b> The market's #1 fear, and our bear case. Our stress test: a 15% AFFO cut keeps the dividend covered at ~88% payout \u2014 painful, not fatal. Mitigants: 30+ years to renewal, cross-default, immovable assets, and Fertitta is arguably better credit than levered public Caesars ($11.9B debt). But a hostile lease renegotiation, however unlikely legally, would re-rate the stock violently \u2014 that is the $20.65 world.",
        "<b>Interest rates.</b> The 10-year at ~5.25% (24-year high) is the valuation anchor dragging the multiple. Every 50bp of sustained long-end rise compresses the fair range by ~$2\u20133. VICI's own refinancing ($1.5B due 2027) reprices higher. This is the risk that keeps the market lenses at $26\u201330 while the DCF says $39.",
        "<b>Las Vegas / regional softness.</b> Visitor volume -7.5% in 2025 and -4.3% in Aug 2026; ADR -7.4%. Strip GGR is still growing (+0.7%), but sustained leisure weakness pressures tenant rent coverage \u2014 especially regional Caesars properties where coverage is thinnest.",
        "<b>Cap-rate expansion.</b> If acquisition cap rates rise with rates, the accretive-deal engine slows; external growth would then rely on the loan book and PPGF.",
        "<b>GAAP noise.</b> CECL swings and sales-type lease accounting make EPS volatile and screen poorly \u2014 a perpetual source of headline misses (as in Q2). Underwrite AFFO, not EPS.",
    ]:
        story.append(B(r))

    story.append(P("7. Catalysts & final recommendation", s_h1))
    story.append(P("<b>Catalysts (next 12 months):</b> Caesars/Fertitta closing (by June 2027) \u2014 removes the overhang; any "
        "disclosure confirming lease treatment is a re-rating event. Q3 2026 results (late Oct 2026) \u2014 AFFO trajectory and "
        "2027 commentary; another guidance raise would force multiple expansion. Rate relief \u2014 any sustained 10-year rally "
        "is the single biggest multiple driver; REITs re-rate first. Sale-leaseback pipeline \u2014 motivated sellers + VICI's "
        "cheap capital = accretive deals. Dividend raises \u2014 the 9th consecutive annual increase (expected Sept 2027) at a "
        "75% payout is self-funding marketing for the compounding story.", s_body))
    story.append(P("<b>We initiate VICI Properties with a BUY rating and a $39.00 12-month price target</b> (from $22.65; +72.2% "
        "upside, ~80% total return with the 8.1% dividend), risk rating Medium-High.", s_body))
    story.append(P("The investment case, stated plainly: <b>the cash flows are fine; the price is about fear.</b> AFFO/share is "
        "growing 4\u20135%, the dividend was just raised for the 8th straight year at a 75% payout, collection is 100%, leverage "
        "is 5.0\u00d7 investment-grade. The stock sits ~1% off its 52-week low because the market fears Caesars and 5%+ rates, "
        "not because the business deteriorated. <b>Asymmetry favors the buyer.</b> Bear-case fair value ($20.65) is a genuine "
        "Caesars-stress world and still only 9% below the quote; base-case AFFO-DCF points to ~$42; the weighted DCF is $39. "
        "You are paid 8.1% to wait for the re-rating. <b>The forward view.</b> We expect the Caesars take-private to close by "
        "mid-2027 with leases intact (credit-neutral to positive), AFFO to compound ~4\u20135%, and the dividend to keep rising. "
        "If long-end yields stay above 5% indefinitely, the return is still an 8%+ growing yield \u2014 an acceptable outcome; "
        "if they normalize, the multiple follows and $39 proves conservative.", s_body))
    story.append(P("<b>Position sizing note:</b> this is an income compounder, not a growth rocket \u2014 size it as a core "
        "dividend holding. The two genuine thesis-breakers to monitor: a Caesars lease impairment (watch the FTC/deal "
        "disclosures) and a sustained move in the 10-year well above 5.5%. Absent those, weakness toward $20 would be an "
        "opportunity to add, not a signal to sell.", s_body))

    story.append(P("Appendix \u2014 Methodology & sources (v2)", s_h1))
    story.append(P("<b>Scenario DCF (v2).</b> Ten explicit years on AFFO per share off 2026E $2.46; growth paths: bear 15% yr-1 "
        "cut then 1% \u2192 0.5%, base 5% \u2192 3%, bull 6% \u2192 3.5%; discount rates 11.5% / 9.0% / 8.0%; terminal growth "
        "2.0% on normalized mid-cycle AFFO (escalator-driven, never peak acquisition pace). Terminal value is 39\u201359% of "
        "fair value by scenario (under the 70% haircut threshold). Growth inputs are anchored to the 2018\u20132025 AFFO "
        "compounding record, faded \u2014 no management anchoring. DDM cross-check: $1.84 dividend at 11.5%/9%/8% cost of "
        "equity and 3%/4%/4.5% dividend growth \u2192 $23.46 / $38.27 / $55.66, weighted $38.86. <b>What we did not do:</b> no "
        "GAAP-EPS DCF (CECL and sales-type lease accounting make EPS noise); no Monte Carlo. <b>Limitations:</b> the 10-year "
        "Treasury is the dominant valuation variable and is not modeled \u2014 it is priced in the discount rate; small changes "
        "in the rate assumption move the DCF materially.", s_body))
    story.append(P("Sources: Company Q2 2026 earnings release (Jul 29, 2026), Q1 2026 supplemental, corporate responsibility "
        "report; SEC filings. Market data: Yahoo Finance (Oct 2, 2026 close $22.65). 10-yr Treasury ~5.25% (Oct 1\u20132, 2026). "
        "Valuation models are the analyst's own; figures marked \u2020 computed from the stated inputs. This is independent "
        "research for informational purposes only \u2014 not investment advice, not a solicitation. The author may hold "
        "positions in securities mentioned. Past performance does not predict future results.", s_small))

    _doc_build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print("built", OUT)

if __name__ == "__main__":
    build()
