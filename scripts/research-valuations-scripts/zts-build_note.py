#!/usr/bin/env python3
"""Build the Zoetis equity research note PDF."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, KeepTogether, HRFlowable)
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.lib import colors

OUT = "/home/hatch/workspace/your_files/zoetis-equity-research/zoetis-equity-research-note.pdf"

NAVY = HexColor("#0F2A44"); ACCENT = HexColor("#1E7B34"); GOLD = HexColor("#C9A227")
LGRAY = HexColor("#F2F4F7"); MGRAY = HexColor("#D9DEE5"); DGRAY = HexColor("#5A6472")
RED = HexColor("#B42318"); BLUE = HexColor("#1D4ED8"); TEAL = HexColor("#0E7490")

s_title = ParagraphStyle("t", fontName="Helvetica-Bold", fontSize=25, leading=29, textColor=NAVY)
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
s_cellCB = ParagraphStyle("ccb", parent=s_cellB, alignment=TA_CENTER)
s_thead = ParagraphStyle("th", parent=s_cell, fontName="Helvetica-Bold", textColor=white, alignment=TA_CENTER, fontSize=8)
s_theadL = ParagraphStyle("thl", parent=s_thead, alignment=TA_LEFT)
s_fn = ParagraphStyle("fn", fontName="Helvetica", fontSize=7.5, leading=10.5, textColor=DGRAY, alignment=TA_LEFT, spaceAfter=2)

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
def hr(): return HRFlowable(width="100%", thickness=0.6, color=MGRAY, spaceAfter=6, spaceBefore=6)

story = []
W, H = A4

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7); canvas.setFillColor(DGRAY)
    canvas.drawString(18*mm, 12*mm, "Zoetis Inc. (NYSE: ZTS)  \u2014  Equity Research Note  \u2014  September 2026")
    canvas.drawRightString(W - 18*mm, 12*mm, f"Page {doc.page}")
    canvas.setStrokeColor(MGRAY); canvas.setLineWidth(0.5)
    canvas.line(18*mm, 14.5*mm, W - 18*mm, 14.5*mm)
    canvas.restoreState()

# ================= COVER =================
story.append(Spacer(1, 24*mm))
story.append(P("ZOETIS INC. (NYSE: ZTS)", ParagraphStyle("x", parent=s_sub, fontName="Helvetica-Bold", fontSize=13, textColor=ACCENT, spaceAfter=2)))
story.append(P("De-rated to Value Territory:<br/>A Quality Franchise Priced for Decline", s_title))
story.append(Spacer(1, 4*mm))
story.append(P("Equity Research Note  \u00b7  Healthcare \u2014 Animal Health  \u00b7  September 19, 2026", s_sub))
story.append(Spacer(1, 7*mm))

rating_data = [
    [cell("Recommendation", s_theadL), cell("12-Mo. Price Target", s_thead), cell("Current Price", s_thead), cell("Implied Upside", s_thead), cell("Risk Rating", s_thead)],
    [Paragraph("<b><font color=\"#1E7B34\" size=\"13\">BUY</font></b>", s_cellC),
     Paragraph("<b><font size=\"12\">$108.00</font></b>", s_cellC),
     Paragraph("<b>$71.40</b><br/><font size=\"7\" color=\"#5A6472\">Sep 19, 2026</font>", s_cellC),
     Paragraph("<b><font color=\"#1E7B34\">+51%</font></b>", s_cellC),
     Paragraph("<b>High</b><br/><font size=\"7\" color=\"#5A6472\">Beta ~0.70</font>", s_cellC)],
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
story.append(Spacer(1, 7*mm))

snap = [
    ["Market cap", "$30.2 bn", "Shares out. (diluted)", "~423 mn"],
    ["Enterprise value", "~$36.9 bn", "52-week range", "$71.00 \u2013 $149.54"],
    ["Net debt / EBITDA", "~$6.7 bn / ~1.7x", "YTD / 1-yr return", "-43% / -51%"],
    ["2026E revenue (guide)", "$9.12 \u2013 $9.32 bn", "2026E adj. EPS (guide)", "$6.15 \u2013 $6.25"],
    ["Trailing P/E / EV/EBITDA", "11.9x / 9.4x", "FCF yield / Div. yield", "7.6% / 3.0%"],
    ["Consensus rating", "Hold", "Consensus price target", "~$101 \u2013 $107"],
]
rows = []
for r in snap:
    rows.append([cell(r[0], s_cellB), cell(r[1], s_cellR), cell(r[2], s_cellB), cell(r[3], s_cellR)])
story.append(styled_table(rows, [34*mm, 46*mm, 34*mm, 46*mm], header_rows=0))
story.append(Spacer(1, 6*mm))
story.append(P("Thesis in one paragraph: The world\u2019s largest animal-health company has lost half its market value on two guidance cuts, a soft U.S. companion-animal market, and a Librela safety overhang \u2014 yet it still earns 38% operating margins, converts a quarter of revenue to free cash flow, and holds a pipeline of 12+ potential $100M blockbusters. At 12x trailing earnings with a 7.6% free-cash-flow yield, the market prices Zoetis as a declining asset; we see a temporarily impaired compounder whose 3-month OA-pain antibodies, long-acting Cytopoint, and diagnostics push can re-accelerate growth from 2027. Our scenario-weighted DCF gives $112; blended with relative multiples, our target is $108 (+51%).", s_body))
story.append(Spacer(1, 4*mm))
story.append(P("<b>Key risks to the call:</b> Librela safety scrutiny (FDA/EMA) and the related class action; U.S. companion-animal demand not recovering; branded JAK-inhibitor entrants taking more dermatology share; a third guidance cut.", s_small))

# ================= 1. INVESTMENT THESIS =================
story.append(P("1. Investment Thesis", s_h1))
story.append(hr())
story.append(P("<b>Why the stock is hated.</b> Zoetis cut full-year 2026 guidance twice (May and August): revenue guidance fell from $9.83\u2013$10.03 bn to $9.12\u2013$9.32 bn and adjusted EPS from $7.00\u2013$7.10 to $6.15\u2013$6.25, implying an <i>organic decline</i> of 1\u20133%. The U.S. companion-animal business fell 11% in both Q1 and Q2 2026 as vet-clinic visits declined, pet owners pushed back on prices, and new branded JAK inhibitors (Elanco\u2019s Zenrelia, Merck\u2019s Numelvi) attacked the Apoquel dermatology franchise. On top of that sits the Librela overhang: an FDA \u201cDear Veterinarian\u201d letter (Dec 2024), U.S. label updates with a mandatory client information sheet (Feb 2025), a UK label update flagging bone/joint findings (Jun 2026), an in-depth EMA review, and a securities class action filed after May\u2019s 21.5% plunge. Consensus collapsed from \u201cModerate Buy\u201d with a ~$153 target to \u201cHold\u201d with ~$101\u2013$107.", s_body))
story.append(P("<b>Why we disagree with the price, not the facts.</b> Every one of those headwinds is real \u2014 and priced. What the price misses:", s_body))
story.append(B("Franchise economics are intact. <b>37.8% GAAP operating margin (FY2025), ~72% gross margin, ~24% FCF margin, ~78% ROE.</b> These are software-like economics with a manufacturing moat behind them. The 2026 earnings hole is demand/mix, not structural margin collapse."))
story.append(B("<b>Multiple compression is extreme.</b> Zoetis traded at 25\u201335x forward earnings for most of the last decade. At 11.5x forward and 9.4x EV/EBITDA, it is cheaper than Elanco on a quality-adjusted basis and in line with generic-pharma multiples \u2014 for a company that has grown revenue at a ~9% CAGR since its 2013 spin-off."))
story.append(B("The OA-pain franchise is being reinvented, not abandoned. <b>Lenivia and Portela \u2014 the first 3-month anti-NGF antibodies \u2014 were approved in Canada and the EU in Q4 2025 and launched in 2026.</b> Monthly Librela\u2019s dosing burden and safety noise are precisely what a longer-acting successor addresses; the installed base of ~21M+ doses is the launchpad."))
story.append(B("<b>The pipeline is the deepest in company history:</b> 12+ candidates each with $100M+ potential across obesity, oncology, chronic kidney disease, cardiology and anxiety; a major-market approval targeted every year; long-acting Cytopoint expected in the U.S. by end-2026; Simparica DUO in 2027."))
story.append(B("<b>Capital returns are aggressive at the lows.</b> The $6B buyback program has $1.3B remaining; 11M shares were retired in H1 2026 (~$1.16B) at an average ~$105. The dividend was raised for the 13th straight year to $2.12 annualized (3.0% yield, ~35% payout). Management is buying its own dip."))
story.append(P("<b>Variant view vs. consensus:</b> sell-side models extrapolate 2026\u2019s U.S. companion-animal weakness indefinitely. We model a cyclical trough: U.S. revenue back to low-single-digit growth in 2027 as price-sensitivity laps, the retail-channel strategy beds in, and new launches contribute. That single assumption \u2014 normalization, not heroics \u2014 bridges most of the gap between $71 and our $108 target.", s_body))

# ================= 2. COMPANY OVERVIEW =================
story.append(P("2. Company Overview", s_h1))
story.append(hr())
story.append(P("Zoetis is the world\u2019s largest animal-health company (~18% global share), discovering, developing, manufacturing and commercializing medicines, vaccines and diagnostics for companion animals (dogs, cats, horses) and livestock (cattle, swine, poultry, fish, sheep). It markets directly in ~45 countries and sells in 100+. Born as Pfizer\u2019s animal-health division (1952), it IPO\u2019d at $26 in February 2013 \u2014 the largest U.S. IPO since Facebook \u2014 with Pfizer fully exiting by June 2013. HQ: Parsippany, NJ. Employees: ~14,500. CEO Kristin Peck (since 2020).", s_body))
story.append(P("Revenue mix (FY2025, $9,467M)", s_h2))
mix = [
    [cell("Segment", s_theadL), cell("Revenue ($M)", s_thead), cell("% of total", s_thead), cell("2025 growth", s_thead)],
    [cell("Companion animal"), cell("$6,587", s_cellR), cell("69.6%", s_cellR), cell("+5%", s_cellR)],
    [cell("Livestock"), cell("$2,764", s_cellR), cell("29.2%", s_cellR), cell("\u22125% rep. / +8% organic*", s_cellR)],
    [cell("Contract mfg / human health"), cell("$116", s_cellR), cell("1.2%", s_cellR), cell("\u2014", s_cellR)],
    [cell("<b>United States</b>", s_cellB), cell("<b>$5,097</b>", s_cellBR), cell("<b>53.8%</b>", s_cellBR), cell("83% companion / 17% livestock", s_cellR)],
    [cell("<b>International</b>", s_cellB), cell("<b>$4,254</b>", s_cellBR), cell("<b>44.9%</b>", s_cellBR), cell("56% companion / 44% livestock", s_cellR)],
]
story.append(styled_table(mix, [62*mm, 34*mm, 34*mm, 50*mm]))
story.append(P("* Livestock reported decline reflects the MFA divestiture; organic operational growth was +8%. Species split: dogs &amp; cats $6,283M; cattle $1,492M; poultry $432M; swine $466M; fish $286M; horses $304M. Source: Zoetis Q4/FY2025 press release (BusinessWire, 2/12/2026).", s_fn))

# ================= 3. FINANCIALS =================
story.append(P("3. Financial Review", s_h1))
story.append(hr())
story.append(P("A decade of compounding, then a 2026 air pocket. Revenue grew at ~9% CAGR from the 2013 spin-off through 2025; adjusted EPS compounded faster (~12%) on buybacks. FY2025 still printed record results \u2014 $9.47B revenue, 37.8% operating margin, $6.41 adjusted EPS \u2014 before U.S. companion-animal demand rolled over in 2026.", s_body))
fin = [
    [cell("$M except EPS", s_theadL), cell("FY2024", s_thead), cell("FY2025", s_thead), cell("FY2026E (guide mid)", s_thead)],
    [cell("Revenue"), cell("$9,256", s_cellR), cell("$9,467", s_cellR), cell("$9,220", s_cellR)],
    [cell("Revenue growth (organic operational)"), cell("+11%", s_cellR), cell("+6%", s_cellR), cell("\u22122%", s_cellR)],
    [cell("GAAP operating income"), cell("$3,358", s_cellR), cell("$3,582", s_cellR), cell("~$3,300", s_cellR)],
    [cell("GAAP operating margin"), cell("36.3%", s_cellR), cell("37.8%", s_cellR), cell("~36%", s_cellR)],
    [cell("Net income (GAAP)"), cell("$2,486", s_cellR), cell("$2,673", s_cellR), cell("\u2014", s_cellR)],
    [cell("Diluted EPS (GAAP)"), cell("$5.47", s_cellR), cell("$6.02", s_cellR), cell("\u2014", s_cellR)],
    [cell("Adjusted diluted EPS"), cell("$5.92", s_cellR), cell("$6.41", s_cellR), cell("$6.20", s_cellR)],
    [cell("Free cash flow"), cell("~$2,320", s_cellR), cell("$2,300", s_cellR), cell("~$2,050", s_cellR)],
    [cell("R&D / SG&A (% of revenue)"), cell("7.4% / 25.0%", s_cellR), cell("7.4% / 25.1%", s_cellR), cell("~7.5% / ~25%", s_cellR)],
    [cell("Dividend per share"), cell("$1.73", s_cellR), cell("$2.00", s_cellR), cell("$2.12", s_cellR)],
]
story.append(styled_table(fin, [62*mm, 38*mm, 38*mm, 42*mm]))
story.append(P("Sources: Zoetis 10-K (FY2025), Q4/FY2025 and Q2 2026 press releases; FY2026E per Aug-2026 guidance midpoints, FCF estimated.", s_fn))
story.append(P("The quarter that broke the multiple", s_h2))
story.append(P("<b>Q2 2026 (Aug 6):</b> revenue $2,468M, flat y/y (\u22121% organic); adjusted EPS $1.87 (+5% reported, +4% organic) \u2014 a 1% EPS beat on a 1.5% revenue miss. The U.S. fell 7% (companion animal \u221211%: dermatology and Simparica Trio pressured by price sensitivity and competition; Cerenia/Convenia generic erosion; lower Librela sales) while U.S. livestock surged 23% on cattle and poultry. Margins compressed (operating margin 37.4% vs 39.1% PY). <b>Q1 2026 (May 7)</b> was worse: revenue $2.26B (+3%, miss), adjusted EPS $1.53 (miss), U.S. companion \u221211% \u2014 and the stock fell 21.5% in a day.", s_body))
story.append(P("Guidance cuts \u2014 twice in three months", s_h2))
gc = [
    [cell("", s_theadL), cell("Feb 2026 (initial)", s_thead), cell("May 2026 (Q1)", s_thead), cell("Aug 2026 (Q2, current)", s_thead)],
    [cell("Revenue"), cell("$9.83\u2013$10.03B", s_cellC), cell("$9.68\u2013$9.96B", s_cellC), cell("<b>$9.12\u2013$9.32B</b>", s_cellCB)],
    [cell("Organic operational growth"), cell("+3% to +5%", s_cellC), cell("cut", s_cellC), cell("<b>\u22123% to \u22121%</b>", s_cellCB)],
    [cell("Adjusted diluted EPS"), cell("$7.00\u2013$7.10", s_cellC), cell("$6.85\u2013$7.00", s_cellC), cell("<b>$6.15\u2013$6.25</b>", s_cellCB)],
]
story.append(styled_table(gc, [52*mm, 42*mm, 42*mm, 44*mm]))
story.append(P("Midpoint revenue cut: \u22127.1%. Midpoint adj. EPS cut: \u221212%. Price contribution assumption trimmed to 1\u20132%. CFO (Sep 2026): assumptions tracking; next update in November. The bar is now low \u2014 and beatable.", s_fn))
story.append(P("Dividend &amp; balance sheet", s_h2))
story.append(P("The dividend was raised 6% in Dec 2025 to <b>$0.53/quarter ($2.12 annualized)</b> \u2014 the <b>13th consecutive annual increase</b>, with a 5-year annualized growth rate near 20%. At $71.40 the yield is <b>~3.0%</b> on a conservative <b>~35% payout ratio</b>; there is ample room to keep raising through the trough. Balance sheet: ~$2.5B cash against ~$9.0B long-term debt (including $2.0B of 0.25% converts due 2029 issued Dec 2025 to fund buybacks); net debt/EBITDA ~1.7x; ratings A3 (Moody\u2019s) / BBB+ (S&amp;P), both stable. The <b>$6B buyback program has $1.3B remaining</b>; 11.0M shares were retired in H1 2026 for $1.16B, cutting diluted shares 6.2% y/y. Five-year EPS CAGR (9.2%) has run well ahead of revenue CAGR (6.3%) \u2014 buybacks are a structural EPS driver.", s_body))

# revenue chart
story.append(P("Revenue &amp; adjusted EPS trajectory ($M / $)", s_h2))
d = Drawing(180*mm, 62*mm)
bc = VerticalBarChart()
bc.x = 12*mm; bc.y = 10*mm; bc.height = 44*mm; bc.width = 150*mm
bc.data = [[8080, 8544, 9256, 9467, 9220]]
bc.categoryAxis.categoryNames = ["2022", "2023", "2024", "2025", "2026E"]
bc.categoryAxis.labels.fontSize = 8; bc.valueAxis.labels.fontSize = 7
bc.valueAxis.valueMin = 0; bc.valueAxis.valueMax = 11000
bc.bars[0].fillColor = TEAL
bc.barLabels.fontSize = 7; bc.barLabelFormat = "%d"
d.add(bc)
story.append(d)
story.append(P("Revenue: $8,080M (2022) \u2192 $8,544M (2023) \u2192 $9,256M (2024) \u2192 $9,467M (2025) \u2192 ~$9,220M (2026E guide mid). Adj. EPS: $4.96 \u2192 $5.32 \u2192 $5.92 \u2192 $6.41 \u2192 $6.20E. Sources: company filings; 2026E per guidance.", s_fn))

# ================= 4. PRODUCTS =================
story.append(P("4. Product Portfolio Evaluation", s_h1))
story.append(hr())
story.append(P("We score each franchise on growth, defensibility, and LOE risk. The portfolio\u2019s center of gravity is shifting from small-molecule dermatology/parasiticides toward monoclonal antibodies and diagnostics \u2014 higher-moat, higher-duration assets.", s_body))
prod = [
    [cell("Franchise (molecule)", s_theadL), cell("FY2025 sales", s_thead), cell("Growth", s_thead), cell("Assessment", s_thead)],
    [cell("<b>Dermatology:</b> Apoquel (oclacitinib) + Cytopoint (lokivetmab)"), cell("$1,743M", s_cellR), cell("+6%", s_cellR), cell("Crown jewel under siege. Apoquel holds ~87% U.S. share but faces its first real branded JAK competition (Zenrelia, Numelvi). CEO guides first LOE to <b>2032</b> (ex-chewable) \u2014 far better than feared. Long-acting Cytopoint expected in U.S. by end-2026.", s_cell)],
    [cell("<b>OA-pain mAbs:</b> Librela (bedinvetmab, dogs) + Solensia (frunevetmab, cats)"), cell("$568M", s_cellR), cell("\u22122%", s_cellR), cell("The controversy. Librela $423M (\u22125%) with U.S. declines on safety scrutiny; Solensia intl +19%. No mAb competitor exists. <b>Lenivia/Portela (3-month dosing)</b> launched in Canada/EU 2026 \u2014 the franchise\u2019s second act.", s_cell)],
    [cell("<b>Parasiticides:</b> Simparica franchise / Simparica Trio"), cell("$1,504M / $1,194M", s_cellR), cell("+11% / +12%", s_cellR), cell("Strongest grower. U.S. share leader (~2x #2); share slipped ~1pt in Q2 2026. Threat is branded (BI\u2019s NexGard \u20ac1.4B), not generic \u2014 no disclosed generic filing. Simparica DUO (2027) extends the line.", s_cell)],
    [cell("<b>Anti-infectives / other:</b> Draxxin, Convenia, Cerenia, ProHeart, Revolution"), cell("n/d individually", s_cellR), cell("mixed", s_cellR), cell("Cerenia and Convenia already face U.S. generics (flagged in Q2 PR) \u2014 contained, legacy drag. ProHeart grew in Q4 2025. Convenia reformulation due 2028\u201329.", s_cell)],
    [cell("<b>Diagnostics:</b> Vetscan, Imagyst, Opticell + VitalRADS/VPG"), cell("$104M qtr (+12%)", s_cellR), cell("+12%", s_cellR), cell("Small but strategic. Acquisitions of VitalRADS (Jul 2026) and Veterinary Pathology Group (Nov 2025) push Zoetis beyond in-vitro into imaging interpretation vs. IDEXX.", s_cell)],
]
story.append(styled_table(prod, [52*mm, 30*mm, 22*mm, 76*mm]))
story.append(P("Sales per Zoetis FY2025 earnings slides. n/d = not disclosed.", s_fn))
story.append(P("Librela safety: separating signal from noise", s_h2))
story.append(P("The facts, in order: FDA \u201cDear Veterinarian\u201d letter (Dec 2024) citing 3,600+ adverse-event reports; U.S. label update plus mandatory Client Information Sheet (Feb 2025); EMA in-depth review launched (late 2025); UK label update adding very-rare bone/joint findings (Jun 2026); a 2026 JAVMA review flagging rapidly progressive OA; FDA draft mAb safety guidance (Sep 2026). Against this: 21M+ doses distributed, side effects described by Zoetis as rare, and the CMO publicly standing behind the product. Our read: the safety cloud caps Librela\u2019s monthly-injectable trajectory, but it does not strand the franchise \u2014 the 3-month successors were designed for exactly this moment. The residual tail risk is the class action and any EMA restriction; both are 2027 stories, and both are in the price at 12x earnings.", s_body))

# ================= 5. PIPELINE =================
story.append(P("5. Pipeline &amp; Growth Drivers", s_h1))
story.append(hr())
story.append(P("R&amp;D runs ~$700M/year (~7% of sales) \u2014 the largest absolute budget in animal health \u2014 and management targets a significant approval in a major market <i>every year</i>. More than 12 candidates are each credited with $100M+ potential across five new therapeutic frontiers (obesity, oncology, chronic kidney disease, cardiology, anxiety) where Zoetis today has minimal presence: pure whitespace.", s_body))
pipe = [
    [cell("Window", s_theadL), cell("Expected approvals / launches", s_thead)],
    [cell("<b>2026</b>"), cell("Long-acting OA mAbs <b>Lenivia/Portela</b> (achieved \u2014 launched Canada/EU); <b>long-acting Cytopoint</b> U.S.; next-gen chemistry Dx; HVT-ND poultry vaccine", s_cell)],
    [cell("<b>2027</b>"), cell("Renal mAb therapy; <b>Simparica DUO</b>; needle-free swine vaccines; DNA vaccine", s_cell)],
    [cell("<b>2028\u20132029</b>"), cell("Dermatology mAb; oncology mAbs 1 &amp; 2; Convenia reformulation; parasite vaccines", s_cell)],
    [cell("<b>2030+</b>"), cell("Obesity therapeutic; anxiety therapeutic; cardiology solution; long-acting parasiticide; oral vaccines", s_cell)],
]
story.append(styled_table(pipe, [28*mm, 152*mm]))
story.append(P("Per Zoetis Corporate Overview (Apr 2026). Beyond the pipeline, three structural drivers: (1) <b>emerging markets</b> \u2014 Simparica Trio launched in Brazil; China is 72% companion-animal mix; (2) <b>diagnostics</b> \u2014 moving up the value chain into imaging/teleradiology; (3) <b>livestock recovery</b> \u2014 U.S. livestock +23% in Q2 2026 on cattle/poultry, plus H5N2 and screwworm vaccine optionality. The global animal-health market is growing ~6\u201311% annually depending on scope; Zoetis at ~18% share has the distribution to take more than its share.", s_fn))

# ================= 6. COMPETITION =================
story.append(P("6. Competitive Landscape", s_h1))
story.append(hr())
comp = [
    [cell("Company", s_theadL), cell("2025 AH sales", s_thead), cell("Growth", s_thead), cell("Key brands / threat", s_thead)],
    [cell("<b>Zoetis</b>"), cell("$9,467M", s_cellR), cell("+2% (+6% organic)", s_cellR), cell("Simparica, Apoquel/Cytopoint, Librela \u2014 #1 globally (~18% share)", s_cell)],
    [cell("<b>Merck Animal Health</b>"), cell("$6,354M", s_cellR), cell("+8%", s_cellR), cell("Bravecto; <b>Numelvi</b> (new JAK vs Apoquel). Gaining in companion (+2%).", s_cell)],
    [cell("<b>Boehringer Ingelheim AH</b>"), cell("\u20ac4.9B", s_cellR), cell("+6.5%", s_cellR), cell("<b>NexGard \u20ac1.4B (+8.5%)</b> \u2014 top parasiticide brand vs Simparica", s_cell)],
    [cell("<b>Elanco</b>"), cell("$4,715M", s_cellR), cell("+6%", s_cellR), cell("<b>Zenrelia</b> (new JAK vs Apoquel); GAAP net loss \u2014 financially stretched rival", s_cell)],
    [cell("<b>IDEXX</b> (diagnostics)"), cell("diagnostics leader", s_cellR), cell("\u2014", s_cellR), cell("Owns the vet \u2018diagnostic desktop\u2019; Zoetis attacking via Imagyst/Opticell/VitalRADS", s_cell)],
    [cell("<b>Dechra / Virbac / Ceva</b>"), cell("mid-tier", s_cellR), cell("\u2014", s_cellR), cell("Niche companion/pharma and vaccine players; Dechra EQT-owned", s_cell)],
]
story.append(styled_table(comp, [44*mm, 30*mm, 32*mm, 74*mm]))
story.append(P("The competitive map favors Zoetis\u2019 moat more than the stock suggests: its two most direct attackers in dermatology (Elanco, loss-making; Merck AH, a division) lack Zoetis\u2019 field force and mAb manufacturing scale, and in parasiticides the fight is brand-vs-brand where Zoetis still leads the U.S. 2-to-1. The structural threat is channel, not product: Chewy/retail and pet-owner price sensitivity are disintermediating the clinic \u2014 Zoetis\u2019 home field. Management\u2019s affordability and loyalty programs are the right response, but this is the variable to watch.", s_body))

# ================= 7. MOAT & RISKS =================
story.append(P("7. Moat &amp; Risks", s_h1))
story.append(hr())
story.append(P("Moat \u2014 wide, in our view", s_h2))
story.append(B("<b>Veterinarian embeddedness.</b> Decades-deep field force and clinic-workflow integration create high switching costs; vets prescribe what they trust with patients they see repeatedly."))
story.append(B("<b>Biologics manufacturing.</b> ~29 facilities in 11 countries; mAb and vaccine capacity is a genuine barrier \u2014 Elanco cannot replicate it on its balance sheet."))
story.append(B("<b>R&amp;D scale + distribution.</b> ~$700M annual R&amp;D and direct presence in ~45 countries let Zoetis out-develop and out-launch every rival."))
story.append(B("<b>Portfolio breadth.</b> No single product exceeds ~18% of revenue; LOE events (Cerenia, Convenia) have been absorbed without derailing the P&amp;L."))
story.append(P("Risks \u2014 in order of stock relevance", s_h2))
story.append(B("<b>1. Librela safety/regulatory tail.</b> EMA review outcome, further label tightening, and the securities class action. A restrictive EMA decision would re-rate the OA franchise lower."))
story.append(B("<b>2. U.S. companion-animal demand.</b> Two quarters of \u221211% U.S. companion declines. If clinic visits and price sensitivity are structural (channel shift to retail), our 2027 normalization thesis fails."))
story.append(B("<b>3. Dermatology share loss.</b> Apoquel at ~87% U.S. share with two new JAK entrants; faster-than-modeled erosion hits the highest-margin franchise."))
story.append(B("<b>4. Execution on guidance.</b> A third cut would destroy the \u2018low bar\u2019 argument and likely take the stock to the $50s."))
story.append(B("<b>5. FX, livestock cyclicality, China</b> \u2014 45% of revenue is international; protein cycles and geopolitics are perennial swing factors."))

# ================= 8. VALUATION =================
story.append(P("8. Valuation", s_h1))
story.append(hr())
story.append(P("We triangulate fair value with three lenses: a scenario-weighted DCF (primary), relative multiples, and a dividend-discount cross-check.", s_body))
story.append(P("A. Discounted cash flow \u2014 scenario-weighted: $112", s_h2))
story.append(P("<b>WACC 7.5%:</b> cost of equity 7.9% (4.25% risk-free + 0.70 beta \u00d7 5.25% ERP); after-tax cost of debt 4.3% (A3/BBB+); target weights 87% equity / 13% debt (net debt ~$6.7B). Terminal growth 2.5% \u2014 well below the ~6%+ animal-health market growth, i.e., we assume share/margin fade, not compounding glory.", s_body))
dcf = [
    [cell("Scenario (weight)", s_theadL), cell("Revenue 2030", s_thead), cell("FCF 2030", s_thead), cell("WACC / g", s_thead), cell("Equity value / share", s_thead)],
    [cell("<b>Bear (30%)</b> \u2014 U.S. demand stays soft; Librela restricted; 2\u20134% growth"), cell("$10.5B", s_cellR), cell("$2.26B", s_cellR), cell("8.0% / 2.0%", s_cellR), cell("<b>$66</b>", s_cellBR)],
    [cell("<b>Base (45%)</b> \u2014 normalization from 2027; pipeline delivers; 5\u20136.5% growth"), cell("$11.6B", s_cellR), cell("$3.02B", s_cellR), cell("7.5% / 2.5%", s_cellR), cell("<b>$110</b>", s_cellBR)],
    [cell("<b>Bull (25%)</b> \u2014 OA franchise re-accelerates; obesity/oncology options hit; 8\u20139% growth"), cell("$12.9B", s_cellR), cell("$3.62B", s_cellR), cell("7.0% / 3.0%", s_cellR), cell("<b>$169</b>", s_cellBR)],
    [cell("<b>Probability-weighted DCF</b>", s_cellB), cell("", s_cellR), cell("", s_cellR), cell("", s_cellR), cell("<b>$112</b>", s_cellBR)],
]
story.append(styled_table(dcf, [72*mm, 26*mm, 26*mm, 28*mm, 28*mm]))
story.append(P("Base case detail: revenue $9.22B (2026E) \u2192 $9.68B \u2192 $10.26B \u2192 $10.93B \u2192 $11.64B; FCF $2.05B \u2192 $2.35B \u2192 $2.57B \u2192 $2.79B \u2192 $3.02B (FCF margin recovering to ~26% on mix and operating leverage); net debt $6.7B; ~423M diluted shares. Even the bear case ($66) is only 8% below today\u2019s price \u2014 the downside is substantially in the price.", s_fn))
# DCF scenario bar chart
story.append(P("DCF scenario values vs. current price ($)", s_h2))
d2 = Drawing(180*mm, 62*mm)
bc2 = VerticalBarChart()
bc2.x = 12*mm; bc2.y = 10*mm; bc2.height = 44*mm; bc2.width = 150*mm
bc2.data = [[71.4, 66, 110, 112, 169]]
bc2.categoryAxis.categoryNames = ["Current", "Bear", "Base", "Weighted", "Bull"]
bc2.categoryAxis.labels.fontSize = 8; bc2.valueAxis.labels.fontSize = 7
bc2.valueAxis.valueMin = 0; bc2.valueAxis.valueMax = 190
bc2.bars[0].fillColor = TEAL
bc2.barLabels.fontSize = 7; bc2.barLabelFormat = "%d"
d2.add(bc2)
story.append(d2)
story.append(P("B. Relative multiples \u2014 $100\u2013$114 range", s_h2))
story.append(P("Zoetis at 11.5x forward earnings trades at a ~60% discount to its own 10-year average (~28x) and roughly in line with diversified pharma \u2014 an absurd peer group for a 38%-margin animal-health leader. On 2027E adjusted EPS of ~$6.70 (revenue $9.68B, ~38% operating margin, continued buybacks): <b>15x \u2192 $100; 16x \u2192 $107; 17x \u2192 $114</b>. We use $107 (16x \u2014 still a 40%+ discount to history, appropriate for the overhang). Cross-check on EV/EBITDA: 2027E EBITDA ~$3.96B at 12\u201313x \u2192 $96\u2013$106 per share. IDEXX, the closest quality comp, trades ~28x forward \u2014 the quality gap does not justify Zoetis at value multiples.", s_body))
story.append(P("C. Dividend discount cross-check \u2014 $80\u2013$95", s_h2))
story.append(P("Two-stage DDM: $2.12 dividend growing 10% for 5 years (payout has headroom at 35%; 5-yr historical growth ~20%), then 4\u20135% terminal, 8% discount rate \u2192 <b>$80\u2013$95</b>. The DDM deliberately understates value here \u2014 Zoetis returns most cash via buybacks ($1.16B in H1 2026 alone), which the DDM ignores \u2014 so we treat it as a floor, not a target.", s_body))
story.append(P("Football field &amp; target derivation", s_h2))
ff = [
    [cell("Method", s_theadL), cell("Value", s_thead), cell("Weight in target", s_thead)],
    [cell("DCF \u2014 base case"), cell("$110", s_cellR), cell("50%", s_cellR)],
    [cell("Relative P/E (16x 2027E)"), cell("$107", s_cellR), cell("30%", s_cellR)],
    [cell("Scenario-weighted DCF"), cell("$112", s_cellR), cell("20%", s_cellR)],
    [cell("<b>Blended fair value \u2192 12-mo. target</b>", s_cellB), cell("<b>$108</b>", s_cellBR), cell("<b>100%</b>", s_cellBR)],
]
story.append(styled_table(ff, [70*mm, 55*mm, 55*mm]))
story.append(P("Blended: 0.50\u00d7110 + 0.30\u00d7107 + 0.20\u00d7112 = <b>$108</b>. Upside from $71.40: <b>+51%</b>. For context, the sell-side consensus target sits at ~$101\u2013$107 (Hold) \u2014 our target is at the top of the Street, but our <i>rating</i> differs because the Street\u2019s Hold embeds a multiple the business no longer deserves.", s_fn))

# ================= 9. RECOMMENDATION =================
story.append(P("9. Recommendation", s_h1))
story.append(hr())
story.append(P("<b>BUY \u2014 12-month target $108 (+51%), High risk.</b> This is a classic fallen-quality setup: a wide-moat compounder (38% operating margins, 78% ROE, 13 straight dividend raises) trading at 12x earnings and a 7.6% FCF yield because two quarters of U.S. weakness and a safety controversy broke the growth narrative. The controversy is real but contained \u2014 and the pipeline (3-month OA antibodies launched, long-acting Cytopoint by year-end, renal mAb and Simparica DUO in 2027, obesity/oncology beyond) gives Zoetis more shots on goal than at any point in its listed history. Downside is cushioned: even our bear case ($66) sits 8% below the current price, and the 3.0% dividend pays you to wait.", s_body))
story.append(P("Position sizing &amp; catalysts", s_h2))
story.append(B("<b>Size it as a starter, not a full position:</b> 1/3 to 1/2 of a full weight initially. Add on (a) Q3 results / November guidance update confirming stabilization, (b) U.S. long-acting Cytopoint approval, or (c) EMA review resolution. Cut on a third guidance cut or restrictive EMA action."))
story.append(B("<b>Catalysts (next 12 months):</b> Q3 2026 print + guidance update (Nov 2026); long-acting Cytopoint U.S. approval (by end-2026); Lenivia/Portela early launch reads in Canada/EU; EMA CVMP review conclusion; evidence of U.S. clinic-visit stabilization."))
story.append(B("<b>What would change our mind:</b> structural \u2014 not cyclical \u2014 U.S. companion demand (persistent double-digit declines into 2027); Apoquel share collapsing below ~70%; balance-sheet stress forcing the buyback/dividend to pause."))
story.append(P("Risks to the call are detailed in Section 7; the single largest is a third guidance cut, which would likely take the stock toward the $50s and invalidate the trough thesis.", s_small))
story.append(Spacer(1, 4*mm))
story.append(P("Sources &amp; methodology", s_h2))
story.append(P("Company: Zoetis Q4/FY2025 press release (BusinessWire 2/12/2026); Q2 2026 press release (BusinessWire 8/6/2026); Q2 2026 10-Q; FY2025 10-K; FY2025 earnings slides; Corporate Overview (Apr 2026); management commentary Sep 2026. Regulatory: FDA CVM, EMA/CVMP, UK VMD, JAVMA review. Market data: quote/market data Sep 19, 2026; consensus via MarketBeat/transcriptdaily; analyst actions via Zacks, StockStory, Piper Sandler, JPMorgan, TD Cowen, Stifel. Valuation estimates and scenarios are the author\u2019s. <b>This note is for informational purposes only and is not investment advice, an offer, or a recommendation to buy or sell any security. Investing involves risk, including loss of principal.</b>", s_fn))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm,
                        topMargin=16*mm, bottomMargin=18*mm,
                        title="Zoetis Inc. (ZTS) \u2014 Equity Research Note",
                        author="Muse")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("WROTE", OUT)
