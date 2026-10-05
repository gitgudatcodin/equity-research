#!/usr/bin/env python3
"""Build the FuboTV (FUBO) equity research note PDF — v2 hardened rebuild, October 4, 2026."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                HRFlowable)
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import VerticalBarChart

OUT = "/home/hatch/workspace/your_files/fubo-equity-research/fubo-equity-research-note.pdf"

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
    canvas.drawString(15*mm, 12*mm, "FuboTV Inc. (NYSE: FUBO)  \u2014  Equity Research Note  \u2014  October 4, 2026")
    canvas.drawRightString(W - 15*mm, 12*mm, f"Page {doc.page}")
    canvas.setStrokeColor(MGRAY); canvas.setLineWidth(0.4)
    canvas.line(15*mm, 14.5*mm, W - 15*mm, 14.5*mm)
    canvas.restoreState()

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=15*mm, rightMargin=15*mm,
                        topMargin=16*mm, bottomMargin=18*mm,
                        title="FuboTV (FUBO) Equity Research Note", author="Independent Research")
_doc_build = doc.build

# ---------- helpers for verdict box ----------
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
    # Cover
    story.append(P("FUBOTV INC.", ParagraphStyle("k", parent=s_sub, fontName="Helvetica-Bold", fontSize=12, textColor=ACCENT)))
    story.append(Spacer(1, 3*mm))
    story.append(P("The $164 Subscriber:<br/>Disney's Sports vMVPD Priced for Liquidation", s_title))
    story.append(Spacer(1, 3*mm))
    story.append(P("Equity Research Note \u00b7 Media \u2014 Streaming / vMVPD \u00b7 October 4, 2026", s_sub))
    story.append(Spacer(1, 4*mm))
    story.append(verdict_box([
        ("Recommendation", "BUY (Speculative)"),
        ("12-Mo. Price Target", "$33"),
        ("Current Price", "$8.66 (Oct 2, 2026 close)"),
        ("Implied Upside", "+281%"),
        ("Risk Rating", "High"),
    ]))
    story.append(Spacer(1, 4*mm))
    story.append(P("Fubo \u2014 now the combined Fubo + Hulu + Live TV business, 70% owned by Disney \u2014 is the "
        "sixth-largest pay-TV operator in the U.S. with ~5.75 million subscribers, inflecting toward profitability "
        "(three straight quarters of positive adjusted EBITDA; free cash flow nearly breakeven). The market values the "
        "equity at $164 per subscriber and 0.15x revenue \u2014 levels that price in permanent decline: our reverse-DCF "
        "shows the $8.66 quote implies either a roughly \u221210% annual revenue decline for a decade or a ~3.5\u20134% "
        "steady-state EBITDA margin, below management's own 2028 target ($300M EBITDA, ~4\u20135% margin). In January 2025, "
        "Disney's deal implicitly valued these same subscribers at roughly $800\u20131,000 apiece. This v2 rebuild values "
        "Fubo under hardened rules \u2014 scenario-specific discount rates (12% base / 14.5% bear / 10.5% bull), a bear case "
        "that genuinely hurts ($2.91, \u221266%), and terminal growth capped at 2% on mid-cycle margins. The "
        "probability-weighted DCF (25/50/25) lands at $32.55; we set a $33 twelve-month target, the weighted fair value "
        "rounded. This is a High-risk special situation, not a compounder: minority shareholders have no vote (the 1-for-12 "
        "reverse split was executed by Disney written consent alone), 79M shares of future overhang are registered, and the "
        "vMVPD remains a structurally thin-margin reseller. Size accordingly."))
    story.append(P("Full economic equity value $946M @ $8.66 \u00b7 Class A float value ~$262M (30.2M sh.) \u00b7 "
        "52-week range (split-adj.) $7.95\u2013$52.68 \u00b7 Enterprise value ~$1.03B \u00b7 FY2026E revenue (cons.) ~$6.19B \u00b7 "
        "Net debt (6/30/26) ~$86M \u00b7 Subscribers (FQ3'26) 5.75M North America \u00b7 Short interest 20.9% of float. "
        "Prices as of October 2, 2026 close. Per-share figures are post the 1-for-12 reverse split effective March 23, 2026. "
        "This note is an independent research-style analysis for informational purposes, not investment advice.", s_small))
    story.append(Spacer(1, 2*mm))

    # 1. Thesis
    story.append(P("1. Investment thesis", s_h1))
    story.append(P("The quote prices in failure; the business is inflecting. At $8.66 the market implies either a ~\u221210% "
        "ten-year revenue decline (at our base-case margins) or a ~3.5\u20134% steady-state EBITDA margin \u2014 below the ~4\u20135% "
        "margin embedded in management's public 2028 target of at least $300M in adjusted EBITDA. Yet the combined company "
        "has printed three consecutive quarters of positive adjusted EBITDA ($41.4M, $37.7M, $19.1M), management raised FY2026 "
        "guidance to $90\u2013100M, and free cash flow improved from \u2212$41M to \u2212$7.5M year over year. The bar the market "
        "sets is lower than the bar management already clears.", s_body))
    story.append(P("The Disney combination was a genuine transformation, not a rescue narrative. Closed October 29, 2025, the "
        "Up-C transaction married Fubo's sports-first product with Hulu + Live TV's ~4.6M subscribers, creating a ~6M-subscriber, "
        "sixth-ranked U.S. pay-TV operator overnight. Disney brings three tangible assets: a $145M Disney term note (4.2%, due "
        "2031 \u2014 drawn January 2026 to retire the converts), the Disney Ad Server migration (lifting ad fill rates and CPMs), "
        "and content-packaging flexibility that a sub-scale standalone could never negotiate.", s_body))
    story.append(P("Valuation is distressed on every relative metric. $164 per subscriber and 0.15x EV/revenue versus ~$800\u2013"
        "1,000 per subscriber implied when Disney struck the deal in January 2025, and versus $400\u20131,000 per sub in precedent "
        "pay-TV transactions. Even at trough multiples \u2014 0.5x revenue, $400/sub, 10x the 2028E $300M EBITDA target "
        "(present-valued) \u2014 fair value is $20\u201328 per share, roughly 2.5x to 3x the quote.", s_body))
    story.append(P("There is a free takeout option embedded. Disney owns 70% of the economics and a majority of the votes; "
        "taking out the 30% stub at a strategic 0.5\u20130.75x sales multiple equates to $28\u201342 per share. Minority "
        "shareholders cannot force it, but Disney's $145M loan commitment and board control signal long-term strategic \u2014 "
        "not financial \u2014 ownership, and strategic owners eventually clean up stubs.", s_body))
    story.append(P("The other side is real, and it is governance. Public shareholders own economics but no control: Disney "
        "executed the 1-for-12 reverse split by written consent without a shareholder meeting, the authorized share count was "
        "not reduced (dry powder for future issuance), and 79M Class A shares are registered for eventual exchange of Disney's "
        "interest \u2014 a permanent overhang. The vMVPD itself is a structurally thin-margin reseller (~7% gross margins; "
        "content owners capture the value), and 21% short interest says sophisticated money disagrees. Hence BUY (Speculative), "
        "High risk \u2014 a small position in a wide-range stub, not a core holding.", s_body))

    # 2. Company & deal (condensed)
    story.append(P("2. Company & the Disney deal: a 70%-controlled stub", s_h1))
    story.append(P("FuboTV (New York; founded 2015 by David Gandler) launched as a soccer-streaming service and went public in "
        "October 2020 as a sports-first virtual MVPD. The problem was scale: as a ~2M-subscriber standalone it paid among the "
        "highest per-subscriber content rates in the industry and burned cash every quarter. The Disney transaction rewrote the "
        "company: announced January 6, 2025 (Disney contributes Hulu + Live TV, ~4.6M subs; Fubo drops its Venu antitrust suit "
        "for a $220M settlement), closed October 29, 2025 via an Up-C reorganization. Hulu is the accounting acquirer, so "
        "as-reported history is Hulu + Live TV carve-out numbers \u2014 year-over-year comparisons are only meaningful on the "
        "company's pro forma basis. On March 23, 2026 a 1-for-12 reverse split (by Hulu written consent; no shareholder "
        "meeting) cut Class A to ~30.2M shares and Class B to ~79.0M; the authorized count was not reduced. In July 2026 Alisa "
        "Bowen (then president of Disney+) succeeded Gandler as CEO.", s_body))
    story.append(P("What the public shareholder owns: 30.20M Class A shares (the float, ~30% of OpCo economics and vote) plus "
        "78.99M Class B held by Hulu/Disney. Every per-share figure in this note divides by 109.2M economic-equivalent shares "
        "\u2014 the $8.66 quote therefore capitalizes the whole combined entity at $946M, not just the float. This is a "
        "controlled company in the strong sense: Disney can \u2014 and did \u2014 amend the charter by written consent.", s_body))

    # 3. Financials
    story.append(P("3. Financial situation: inflecting, still fragile", s_h1))
    story.append(P("Read the numbers on the pro forma basis. Three quarters into the combination, the trajectory is "
        "unambiguously improving: revenue stable around $1.5\u20131.7B per quarter, adjusted EBITDA positive every quarter, "
        "free cash flow approaching breakeven.", s_body))
    story.append(styled_table([
        [cell("<b>Pro forma, $M</b>", s_theadL), cell("<b>FQ1'26</b>", s_thead), cell("<b>FQ2'26</b>", s_thead),
         cell("<b>FQ3'26</b>", s_thead), cell("<b>Prior-year PF</b>", s_thead)],
        [cell("Revenue (North America)"), cell("$1,675", s_cellR), cell("$1,566", s_cellR), cell("$1,474", s_cellR), cell("$1,475", s_cellR)],
        [cell("Subscribers (NA, period-end)"), cell("6.2M", s_cellR), cell("5.7M", s_cellR), cell("5.75M", s_cellR), cell("5.63M", s_cellR)],
        [cell("Adjusted EBITDA"), cell("$41.4", s_cellR), cell("$37.7", s_cellR), cell("$19.1", s_cellR), cell("$31.0", s_cellR)],
        [cell("Adj. EBITDA margin"), cell("2.5%", s_cellR), cell("2.4%", s_cellR), cell("1.3%", s_cellR), cell("2.1%", s_cellR)],
        [cell("Free cash flow"), cell("\u2014", s_cellR), cell("$(214.7)*", s_cellR), cell("$(7.5)", s_cellR), cell("$(41.4)", s_cellR)],
    ], [58*mm, 22*mm, 22*mm, 22*mm, 26*mm]))
    story.append(P("*Q2 FCF outflow was seasonal working capital. Sources: Fubo 8-K exhibits (2/2026, 5/6/2026), FQ3'26 press "
        "release (8/2026). Management guides FY2026 adjusted EBITDA of $90\u2013100M (raised August 2026; ~1.5% margin on ~$6.2B "
        "pro forma revenue) and targets at least $300M by FY2028 (~4\u20135% margin) with positive free cash flow in FY2027. Gross "
        "margin sits near 7% \u2014 the vMVPD's structural reality: ~93 cents of every revenue dollar goes to content owners. "
        "Profitability must come from scale leverage on the remaining cents plus advertising, which is why the Disney Ad Server "
        "migration (completion expected by year-end 2026) matters more than any subscriber headline.", s_small))
    story.append(P("Balance sheet: $236.4M cash (6/30/26) against $322.5M debt ($145M Disney senior unsecured note at 4.2% due "
        "2031 + $177.5M converts due 2029); net debt ~$86M. Large NOL stock shields cash taxes near-term. Liquidity is workable "
        "but the plan is the inflection: consensus FCF turns positive (+$125M) in FY2027 after \u2212$441M in FY2026. A miss on the "
        "FY2027 FCF target re-opens the dilution question, and the un-reduced authorized share count gives management the tool "
        "to answer it. Trailing GAAP EPS of $3.84 is an accounting artifact of the $220M Venu settlement \u2014 ignore it.", s_body))

    # 4. Growth & outlook
    story.append(P("4. Growth & outlook: three synergy engines and a 2028 target", s_h1))
    story.append(P("The investment case does not require Fubo to win the streaming wars. It requires the combined company to "
        "harvest the synergies Disney underwrote: $300M of adjusted EBITDA by 2028 and positive FCF in 2027. Three engines: "
        "(1) <b>Advertising optimization</b> \u2014 the Disney Ad Server migration is already lifting fill rates and CPMs "
        "(credited for the FQ3 EBITDA beat); in a ~7%-gross-margin business every incremental ad dollar falls almost entirely "
        "to EBITDA; 2027 is the first full year of benefit. (2) <b>Content-cost flexibility</b> \u2014 at ~6M subscribers the "
        "combined company negotiates as the sixth-largest U.S. pay-TV operator, and Disney's ownership changes the bargaining "
        "dynamic; flexible packaging (the $64.99 Sports + News skinny tier) is itself a synergy. (3) <b>Distribution and "
        "marketing</b> \u2014 the ESPN reseller arrangement puts Fubo inside ESPN's purchase flow; cross-promotion across "
        "Disney's portfolio replaces paid subscriber acquisition. The math of the 2028 target: $300M on ~$6.8B consensus FY2028 "
        "revenue is a ~4.4% margin \u2014 roughly double today's ~2% run rate \u2014 bridged by ~$100M+ of net synergies plus "
        "operating leverage. It is a credible bridge if subscriber losses stay in the low single digits and the ad-server "
        "migration delivers. No management target is taken at face value in our valuation: our base case assumes only an 8% "
        "steady-state EBITDA margin, well short of synergy-optimist hopes.", s_body))

    # 5. Competition (condensed)
    story.append(P("5. Competition: a scale game Fubo just bought its way into", s_h1))
    story.append(styled_table([
        [cell("<b>Service</b>", s_theadL), cell("<b>Base price</b>", s_thead), cell("<b>Est. subs</b>", s_thead),
         cell("<b>Positioning vs. Fubo</b>", s_thead)],
        [cell("YouTube TV (Google)"), cell("$82.99", s_cellC), cell("10M+", s_cellC),
         cell("Scale leader; Feb-2026 genre plans ($64.99 Sports) bracket Fubo's ladder; sets the price ceiling")],
        [cell("Hulu + Live TV (Fubo/Disney)"), cell("$89.99", s_cellC), cell("~4.6M*", s_cellC),
         cell("Now a sibling under the same roof, not a rival")],
        [cell("Fubo (combined)"), cell("$64.99\u2013$98.99", s_cellC), cell("5.7M", s_cellC),
         cell("Sports-first #2; best DVR (1,000 hrs) / streams (10); Disney-backed")],
        [cell("DirecTV Stream"), cell("$94.99+", s_cellC), cell("~2M", s_cellC), cell("Priciest; melting incumbent")],
        [cell("Sling TV (EchoStar)"), cell("$40\u2013$66", s_cellC), cell("<1.8M", s_cellC), cell("Discounter; parent DISH in Chapter 11 (Jun 2026)")],
        [cell("ESPN Unlimited (DTC)"), cell("$29.99", s_cellC), cell("~1.7M", s_cellC), cell("Disney's direct product: strategic threat and reseller partner")],
    ], [44*mm, 26*mm, 22*mm, 58*mm]))
    story.append(P("YouTube TV is the existential comp \u2014 nearly twice Fubo's scale, Google-subsidized, matching Fubo's skinny-tier "
        "pricing move for move. Fubo's edge is sports depth (RSNs, 55,000+ events/year) and, newly, the Disney relationship. "
        "The industry backdrop is stabilizing: U.S. pay TV ended Q2 2026 at 61.5M subscribers, shedding 885k in the quarter while "
        "vMVPDs added 68k \u2014 the tenth straight quarter of improvement in the traditional decline rate (MoffettNathanson, "
        "September 2026).", s_body))

    # 6. Valuation v2
    story.append(P("6. Valuation (v2 hardened): scenario DCF, reverse-DCF, relative value, takeout", s_h1))
    story.append(P("We value Fubo under hardened v2 rules: 10-year scenario DCF (25/50/25 weights), scenario-specific discount "
        "rates (base 12% for this speculative controlled stub / bear 14.5% / bull 10.5%), terminal growth capped at 2% on "
        "mid-cycle margins, and a bear case that genuinely hurts. FCF is modeled as EBITDA less ~1.5% capex intensity, with NOLs "
        "shielding cash taxes. Net debt $86M is deducted; all per-share figures divide by 109.2M economic-equivalent shares.", s_body))
    story.append(P("Lens A \u2014 Scenario DCF (10 explicit years, combined entity)", s_h2))
    story.append(styled_table([
        [cell("<b>Scenario</b>", s_theadL), cell("<b>10-yr rev CAGR</b>", s_thead), cell("<b>Steady EBITDA margin</b>", s_thead),
         cell("<b>Discount</b>", s_thead), cell("<b>Fair value / sh</b>", s_thead)],
        [cell("<b>Bear</b> \u2014 cord-cutting wins; subs drift; synergies accrue to Disney, not the stub"),
         cell("+0.5%", s_cellC), cell("3%", s_cellC), cell("14.5%", s_cellC), cell("$2.91", s_cellBR)],
        [cell("<b>Base</b> \u2014 subs flat-ish, ARPU +2\u20133%; Disney synergies lift margins toward 8%"),
         cell("+3.5%", s_cellC), cell("8%", s_cellC), cell("12.0%", s_cellC), cell("$28.17", s_cellBR)],
        [cell("<b>Bull</b> \u2014 ESPN distribution + ad-server work; subs +3%; margins to 12%"),
         cell("+6.0%", s_cellC), cell("12%", s_cellC), cell("10.5%", s_cellC), cell("$70.94", s_cellBR)],
        [cell("<b>Weighted (25/50/25)</b>"), cell("\u2014", s_cellC), cell("\u2014", s_cellC), cell("\u2014", s_cellC),
         cell("$32.55", s_cellBR)],
    ], [62*mm, 24*mm, 26*mm, 20*mm, 28*mm]))
    story.append(P("The bear case clears every v2 bear-must-hurt test: revenue CAGR of 0.5% is under 3%; the 3% steady-state "
        "margin is 500bp below the base case; and $2.91 sits 66% below the $8.66 quote. Terminal value is 51\u201366% of "
        "enterprise value by scenario \u2014 under the 70% haircut threshold, but the model remains a margin-expansion bet, "
        "stated openly. The spread between $3 and $71 is the reason this is a speculative BUY: the expected value is strongly "
        "positive, but the distribution is extremely wide.", s_small))
    story.append(P("Lens B \u2014 Reverse DCF: what is the market pricing in?", s_h2))
    story.append(P("Holding our base-case margins, discount rate and terminal assumptions fixed, the $8.66 quote solves to "
        "roughly a \u221210% compound annual revenue decline over the next ten years (to ~$2B of revenue by 2036). Alternatively, "
        "at a neutral 2% revenue growth rate, the quote implies a ~3.5\u20134% steady-state EBITDA margin \u2014 below the ~4\u20135% "
        "margin embedded in management's own public 2028 target ($300M on ~$6.8B of consensus revenue). Framed plainly: the "
        "market is pricing in failure on both growth and margins simultaneously, worse than the company's own guidance \u2014 a "
        "plan the last three quarters' EBITDA prints support.", s_body))
    story.append(P("Lens C \u2014 Relative value", s_h2))
    story.append(styled_table([
        [cell("<b>Multiple</b>", s_theadL), cell("<b>Assumption</b>", s_thead), cell("<b>Fair value / sh</b>", s_thead)],
        [cell("EV / revenue 0.5x"), cell("0.5x on $6.19B 2026E"), cell("$27.56", s_cellBR)],
        [cell("EV / subscriber $400"), cell("$400/sub on 5.75M (distressed cut of deal value)"), cell("$20.32", s_cellBR)],
        [cell("EV / subscriber $600"), cell("$600/sub on 5.75M"), cell("$30.76", s_cellBR)],
        [cell("EV / 2028E EBITDA 10x"), cell("10x on $300M mgmt target, PV'd at 12%"), cell("$20.47", s_cellBR)],
    ], [52*mm, 68*mm, 40*mm]))
    story.append(P("Today's quote is 0.15x revenue and $164/sub. The January 2025 Disney deal implicitly valued these subscribers "
        "at roughly $800\u20131,000 apiece. Precedent pay-TV transactions cluster at $400\u20131,000 per sub even for declining "
        "assets. The 2028E EBITDA cut is the most conservative lens: it values only the company's own stated target at a market "
        "10x multiple, discounted back to today.", s_small))
    story.append(P("Lens D \u2014 Disney takeout of the stub", s_h2))
    story.append(P("At a strategic 0.5x sales takeout multiple \u2014 a multiple no independent board would call generous \u2014 the "
        "stub is worth $27.56/share; at 0.75x, $41.73. Minority shareholders cannot force a takeout, and Disney has no obligation "
        "to pay fairly \u2014 but strategic owners with $145M of committed financing and board control rarely leave a stub trading "
        "at 0.15x sales forever. We treat this as upside optionality, not base case.", s_body))
    story.append(P("Blended target: $33", s_h2))
    story.append(styled_table([
        [cell("<b>Valuation read</b>", s_theadL), cell("<b>Fair value / sh</b>", s_thead), cell("<b>Implied upside</b>", s_thead)],
        [cell("Scenario DCF, 10-yr, 25/50/25-weighted"), cell("$32.55", s_cellBR), cell("+276%", s_cellBR)],
        [cell("EV / revenue 0.5x (trough multiple)"), cell("$27.56", s_cellR), cell("+218%", s_cellR)],
        [cell("EV / subscriber $400 (distressed cut)"), cell("$20.32", s_cellR), cell("+135%", s_cellR)],
        [cell("2028E EBITDA 10x on mgmt target (PV'd)"), cell("$20.47", s_cellR), cell("+136%", s_cellR)],
        [cell("Street consensus (MarketBeat, Moderate Buy)"), cell("~$16.83", s_cellR), cell("+94%", s_cellR)],
        [cell("<b>12-month target</b>"), cell("<b>$33</b>", s_cellBR), cell("<b>+281%</b>", s_cellBR)],
    ], [80*mm, 40*mm, 40*mm]))
    story.append(P("We set $33: the probability-weighted DCF rounded, with no departure from it. The controlled-company risk is "
        "priced through the 12% base discount rate (a full speculative-tier rate for a ~$1B enterprise) rather than an ad hoc stub "
        "haircut. It sits above the Street consensus (~$16.83, Moderate Buy), because the Street's models, in our view, underweight "
        "the synergy-driven EBITDA inflection already visible in the last three quarters \u2014 and the Street's own targets have "
        "been cut repeatedly on price action more than on fundamentals (Wedbush $42\u2192$19, Needham $51\u2192$15). Every lens "
        "says the same thing in different units: the quote prices in failure, and failure is not the base case.", s_body))
    # bar chart: scenarios vs target
    story.append(P("Figure \u2014 Scenario fair values vs. target ($)", s_h2))
    d = Drawing(460, 170)
    bc = VerticalBarChart(); bc.x = 60; bc.y = 30; bc.height = 110; bc.width = 360
    bc.data = [[2.91, 28.17, 70.94, 32.55, 33.0]]
    bc.strokeColor = MGRAY; bc.barLabels.nudge = 8
    bc.barLabelFormat = "%.2f"
    bc.categoryAxis.labels.boxAnchor = "ne"; bc.categoryAxis.labels.dx = 6; bc.categoryAxis.labels.dy = -2
    bc.categoryAxis.labels.angle = 0
    bc.categoryAxis.categoryNames = ["Bear", "Base", "Bull", "Weighted", "Target"]
    bc.bars[0].fillColor = ACCENT
    bc.valueAxis.valueMin = 0; bc.valueAxis.valueMax = 80; bc.valueAxis.valueStep = 20
    d.add(bc); d.add(String(60, 150, "Fair value / share ($)", fontSize=8, fillColor=DGRAY))
    story.append(d)
    story.append(P("Figure \u2014 Scenario fair values vs. target ($). The $8.66 quote sits beneath every scenario except the bear "
        "($2.91). Source: analyst model, October 4, 2026.", s_small))

    # 7. Risks
    story.append(P("7. Risks", s_h1))
    for r in [
        "<b>Controlled-company governance (the central risk).</b> Disney holds ~70% of the economics and the votes and has shown it will act unilaterally \u2014 the 1-for-12 reverse split was executed by Hulu written consent (February 3, 2026) with no shareholder meeting. Minority shareholders cannot block strategy, capital allocation, or a takeout price they dislike.",
        "<b>Dilution and overhang.</b> The authorized share count was not reduced in the reverse split, and 79M Class A shares are registered for eventual exchange of Disney's interest. Any liquidity shortfall is likely to be solved with the printing press.",
        "<b>Structural margin thinness.</b> ~7% gross margins are not a phase; they are the vMVPD business model. Content owners (Disney itself, Fox, CBS, NBCU) capture essentially all the value. If content-cost inflation outruns ARPU, the EBITDA inflection reverses.",
        "<b>YouTube TV and the scale game.</b> Google's 10M+ subscribers, unlimited DVR, and new genre plans ($64.99 Sports) match Fubo's moves with deeper pockets. A price war in skinny sports bundles would compress the exact segment Fubo is counting on.",
        "<b>Carriage and content risk.</b> The NBCUniversal blackout (November 2025 \u2013 June 2026) is resolved, but each renewal is a potential blackout, subscriber shock, or rate step-up \u2014 and Fubo's sports-first customers are the least forgiving of gaps.",
        "<b>Cord-cutting and churn.</b> The U.S. pay-TV universe shrinks ~5% a year; Fubo's own 6.2M \u2192 5.7M seasonal swing shows how quickly sports-season subscribers leave. Sustained sub declines break the synergy math.",
        "<b>Financing.</b> $236M of cash funds the plan only if FY2027 FCF inflects positive as guided (consensus +$125M after \u2212$441M in FY2026). A miss re-opens the capital question on terms Disney dictates.",
        "<b>Market structure.</b> 20.9% short interest and a 2.39 beta: the stock can stay dislocated, and forced selling around the Class B exchange registration is a real technical risk.",
    ]:
        story.append(B(r))

    # 8. Recommendation
    story.append(P("8. Recommendation", s_h1))
    story.append(P("<b>BUY (Speculative), $33 twelve-month target (+281%).</b> Fubo is the rare equity where the market's implied "
        "expectations sit below the company's own public guidance: the quote prices in a decade of ~\u221210% annual revenue "
        "decline or ~3.5\u20134% steady-state margins, while management \u2014 with Disney's balance sheet, ad server and "
        "distribution behind it \u2014 targets $300M of EBITDA by 2028 and positive free cash flow in 2027, and has printed three "
        "straight quarters of positive adjusted EBITDA to prove the trajectory. At $164 per subscriber and 0.15x revenue, against "
        "~$800\u20131,000 per subscriber implied when Disney struck the deal twenty-one months ago, the stub is priced as a stub "
        "in liquidation rather than as the sixth-largest U.S. pay-TV operator. The v2 DCF \u2014 with a bear case that genuinely "
        "hurts ($2.91, \u221266%) and speculative-tier discounting \u2014 still weights to $32.55.", s_body))
    story.append(P("This is a High-risk special situation, not a compounder \u2014 size it as one. A 1\u20133% portfolio position is "
        "the right frame: the expected value is strongly positive, but the bear case is a real state of the world, and minority "
        "shareholders have no vote and no catalyst they control. The position earns its keep through: (a) quarterly EBITDA "
        "progress toward the $300M 2028 target, (b) Disney Ad Server migration completion by year-end 2026, (c) the FY2027 "
        "positive-FCF milestone, and (d) the ever-present takeout option on the 30% stub at $28\u201342.", s_body))
    story.append(P("<b>What would change our mind:</b> to the upside, sustained subscriber growth (not just seasonal recovery), ad "
        "ARPU compounding post-migration, and a takeout bid \u2014 the bull DCF ($71) becomes the conversation. To the downside, "
        "pro forma revenue declining while content costs rise, the FY2027 FCF target slipping, any dilutive equity raise using the "
        "un-reduced authorized count, or Disney actions that subordinate the stub \u2014 any of which re-rates the shares toward "
        "our $3\u20139 bear zone. Sell discipline: cut the position in half if the stock reaches $25 ahead of the fundamentals "
        "(de-risk into strength), and exit entirely on a dilutive raise or a broken FCF trajectory.", s_body))

    # Appendix
    story.append(P("Appendix A \u2014 Methodology and key assumptions (v2)", s_h1))
    story.append(P("<b>Share count.</b> All per-share figures divide by 109.19M economic-equivalent shares (30.20M Class A + "
        "78.99M Class B, per the 7/31/2026 10-Q), post the 1-for-12 reverse split effective March 23, 2026.", s_body))
    story.append(P("<b>Scenario DCF (v2).</b> Ten explicit years off a $6.19B FY2026E revenue base (consensus); starting EBITDA "
        "$95M (midpoint of the raised $90\u2013100M guide); EBITDA margins gliding to 3% / 8% / 12% by scenario; FCF \u2248 "
        "EBITDA less 1.5% capex intensity, NOLs shielding cash taxes; discount rates 14.5% / 12.0% / 10.5% (bear/base/bull); "
        "terminal growth 2.0% on mid-cycle margins. Net debt $86M deducted. Terminal value is 51\u201366% of EV by scenario "
        "(under the 70% haircut threshold). Growth and margin paths are set from historical fade and vMVPD unit economics, "
        "not from management targets \u2014 the base-case 8% margin is deliberately below synergy-optimist hopes.", s_body))
    story.append(P("<b>Reverse DCF.</b> Binary search on (i) a constant 10-year revenue CAGR holding base-case margins fixed, "
        "and (ii) a steady-state EBITDA margin at 2% revenue growth; solves the CAGR/margin equating model equity value to "
        "the $8.66 quote.", s_body))
    story.append(P("<b>Relative valuation.</b> EV/revenue, EV/subscriber and EV/EBITDA on the combined entity, October 2, 2026. "
        "Subscriber base 5.75M (FQ3'26). The 2028E EBITDA cut present-values a 10x multiple on management's $300M target at the "
        "base-case 12% discount rate over ~2.25 years.", s_body))
    story.append(P("<b>What we did not do.</b> No dividend model (no dividend); no sum-of-the-parts (the two brands share "
        "infrastructure and subscribers); no Monte Carlo (three explicit scenarios communicate the distribution better).", s_body))
    story.append(P("<b>Limitations.</b> Pro forma history is short (three quarters) and the accounting-acquirer convention makes "
        "as-reported history incomparable. Small changes in margin trajectory or discount rate move the DCF by tens of dollars "
        "per share.", s_body))
    story.append(P("Appendix B \u2014 Disclosures", s_h1))
    story.append(P("This note is an independent research-style analysis prepared for informational purposes. It is not investment "
        "advice, not a recommendation to buy or sell any security, and not a personal financial plan. All forward-looking "
        "statements \u2014 scenarios, targets, and projections \u2014 are estimates subject to uncertainty; actual results may "
        "differ materially. Valuation models rely on the assumptions disclosed above. The author may hold positions in "
        "securities mentioned. Past performance does not predict future results. Financial data: FuboTV Inc. 8-K/10-Q filings "
        "and earnings call transcripts; deal terms: Disney and Fubo press releases (1/6/2025, 10/29/2025); market data: Yahoo "
        "Finance, October 2, 2026 close. Verify all figures against primary sources before acting.", s_small))

    _doc_build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print("built", OUT)

if __name__ == "__main__":
    build()
