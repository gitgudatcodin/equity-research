"""Polished note: MercadoLibre (MELI) — REDUCE, fair value $1,119.00.

Authoritative scenario numbers are from the current research note's
international-framework valuation: bear $116.16 / base $1,106.57 /
bull $2,146.62, weighted to the $1,119 target. Every scenario discount rate
carries an explicit +200bp Latin America country-risk premium (ARS
hyperinflation history, BRL volatility, Brazil tax reform, Mexico policy
shifts; local-currency billing is a partial natural hedge, so the premium
sits below China's 250bp): 16.5%/14.0%/12.5%. Terminal growth 1.5%/2.5%/2.5%
on year-10 free cash flow at normalized mid-cycle net margins (7.5%/11%/
12.5%); the bear terminal is derated to force the case to hurt.
Owner earnings are modeled as 0.8x net income (adjusted FCF; reported FCF
includes the credit book). Composition PVs are derived from the note's own
disclosed terminal values, discount rates, net debt ($7.462B), and scenario
fair values (EV = equity + net debt; PV(terminal) = TV/(1+r)^10).
History: company filings via Yahoo Finance (Oct 2026). Trajectory projection:
base-case path at the scenario's 14.9% revenue CAGR with net margins gliding
6.0% -> 11.0% and FCF at 0.8x net income. All prose is fresh October 4, 2026
analysis.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note, validate

data = {
    "ticker": "MELI",
    "company": "MercadoLibre, Inc.",
    "exchange": "NASDAQ",
    "sector": "Consumer Cyclical — Internet Retail / Fintech",
    "verdict": "REDUCE",
    "fair_value": 1119.00,
    "price": 1696.56,
    "risk": "High",
    "headline": "Latin America's compounding machine: a great company at a demanding price",
    "ceo": "Marcos Galperin",
    "hq": "Montevideo, Uruguay",
    "snapshot": [
        ("Market cap", "~$86.0 bn (50.7 m sh × $1,696.56)"),
        ("52-week range", "~$1,495 – $2,549"),
        ("Price / fair value", "$1,696.56 / $1,119.00"),
        ("Implied downside", "−34.0%"),
        ("TTM revenue / net income", "$35.2 bn / $1.86 bn"),
        ("Gross / operating margin (FY25)", "44.5% / 11.1%"),
        ("TTM P/E / forward P/E / PEG", "46.2x / 30.9x / 0.95"),
        ("Net debt", "~$7.5 bn"),
        ("Sell-side view", "Average target ~$2,272 (25 analysts; range $1,750–$2,800)"),
        ("Next catalyst", "Q3 2026 print (early November) — the test of the reinvestment thesis"),
    ],
    "thesis": [
        "MercadoLibre is the highest-quality compounder we cover in emerging markets: 30 "
        "consecutive quarters of above-30% revenue growth, roughly 40% share of Brazilian "
        "e-commerce, a fintech (Mercado Pago) that crossed $100 billion of quarterly "
        "payment volume, a credit book growing 75% a year at a 21% net interest margin "
        "after losses, and an advertising business up 73% that just crossed 10% of Latin "
        "American digital ad spend. The stock is down 31% over twelve months — and yet, on "
        "our numbers, the rerating case is not yet there.",
        "We rate the shares REDUCE with fair value at $1,119: bear $116.16, base "
        "$1,106.57, bull $2,146.62, weighted 25/50/25. The business thesis is untouched — "
        "this is purely the cost of Latin American capital being repriced. The valuation "
        "applies an explicit +200bp Latin America country-risk premium to every scenario "
        "discount rate — ARS hyperinflation history, BRL volatility, Brazil tax reform, "
        "Mexico policy shifts; MercadoLibre bills and collects in local currency, a partial "
        "natural hedge, so the premium sits below the 250bp applied to China — taking "
        "rates to 16.5% / 14.0% / 12.5%. The premium is the entire verdict: without it, "
        "the same operating projections are worth far more; with it, the $1,696.56 price "
        "embeds roughly 18% ten-year growth with no margin of safety, and at a 14% base "
        "discount that growth is worth $1,107, not $1,697.",
        "The bull ($2,146.62) still clears the price — so this is REDUCE, not SELL: own "
        "less of it, do not own none of it. Thirty quarters above 30% growth, a fintech "
        "flywheel where payments data drives superior underwriting drives credit drives "
        "engagement, and an ads business that is the highest-margin incremental dollar in "
        "the company — this is arguably the best emerging-markets compounder in public "
        "markets, and a core EM-growth holding for patient capital. But 47x trailing "
        "earnings leaves no room for execution slips: FX shocks, credit-loss spikes, or "
        "Amazon/Shopee/Temu share pressure would all hit a multiple that assumes "
        "near-perfect execution. High risk reflects EM FX, a $16B+ credit book growing "
        "fast into a stressed Brazilian consumer (Selic 14%), Argentina macro, and "
        "regulatory overhang. Reduce into strength; accumulate only on weakness toward "
        "base-case DCF territory around $1,106.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("This is a capital-cost call, not a business call. ",
         "Nothing in the operating projections moved — only the discount rate. The "
         "disagreement with the Street (average target ~$2,272) is stated plainly: the "
         "Street prices Latin American capital at US rates; we charge an explicit 200bp "
         "for ARS hyperinflation history, BRL volatility, and regional policy risk."),
        ("The margin compression is investment, not decay. ",
         "Q2 2026 operating margin fell 550bps YoY to 6.7% on free-shipping expansion, "
         "credit-card rollout, 1P selection, cross-border, and MELI+. Management says "
         "margin would be 5–6 points higher without these outlays — we haircut that claim "
         "to roughly half and model it as deferred earnings, not eroded unit economics."),
        ("The credit book is the tripwire. ",
         "$16B+ growing 75% into a stressed Brazilian consumer, NPLs near historic lows "
         "today, provisions already doubling YoY in Q1 2026. A regional downturn hits "
         "earnings twice: higher losses and slower payment volume. Selic at 14% is the "
         "number to watch."),
    ],
    "business": [
        "MercadoLibre is the dominant Latin American e-commerce and fintech ecosystem: "
        "roughly 40% of Brazilian retail e-commerce and co-leader in Mexico, in markets "
        "where e-commerce penetration is still low-double-digits versus ~16% in the US. "
        "Mexico is the fastest-growing online retail market in the world (+20% in 2024). "
        "The commerce marketplace, logistics network (Mercado Envios), and fintech stack "
        "form a single flywheel: marketplace frequency drives ad and credit monetization, "
        "and fintech users transact at ~+90% payment volume per user versus "
        "fintech-only cohorts.",
        "Mercado Pago is a second engine that is no longer an accessory: 43% of revenue "
        "($4.4B in Q2 2026), $101B of quarterly total payment volume (+56% in USD, the "
        "first $100B+ quarter) on 5.2 billion transactions — and most of that volume is "
        "off-platform (wallet, QR, bill pay, transfers). It is an independent "
        "financial-services business with its own flywheel: payments data → superior "
        "underwriting → credit → engagement → more data. The credit portfolio is "
        "expanding fast at a 21% net interest margin after losses (recovered from 18%), "
        "with cards near historic lows.",
        "Advertising is the purest margin-accretive line: +73% growth, above 10% of Latin "
        "American digital ad spend, auction-priced — the highest-margin incremental dollar "
        "in the company, just getting started. MELI+ (the loyalty/subscription bundle) is "
        "early-stage but strategically load-bearing as the retention layer.",
    ],
    "business_bullets": [
        ("Commerce: share leader in under-penetrated markets. ",
         "~40% of Brazil e-commerce; co-leader in Mexico (85% combined seller share with "
         "Amazon). Low-double-digits online penetration is the multi-year runway."),
        ("Fintech: the independent second engine. ",
         "Mercado Pago at 43% of revenue, $101B quarterly TPV mostly off-platform, "
         "acquiring TPV $64B (+44%) with market-share gains — a payments business that "
         "would be a decacorn on its own."),
        ("Credit: the growth lever and the risk. ",
         "$16B+ book, +75% YoY, 21% NIMAL. Underwriting edge from payments data is real; "
         "so is the cyclicality of lending into a stressed consumer at Selic 14%."),
        ("Ads: the margin kicker. ",
         "+73% growth at >10% of LatAm digital ad spend. Every incremental ad dollar "
         "carries minimal cost — the same high-margin compounder Amazon's ad business "
         "became, earlier in its curve."),
    ],
    "outlook": [
        "The reinvestment cycle defines the next two years. Management is spending "
        "through the P&L — free shipping thresholds cut from R$79 to R$19 in Brazil, the "
        "credit-card rollout, 1P selection, cross-border, MELI+ — to win the share war "
        "against Amazon, Shopee, and Temu/Shein at the value tier. The -550bps of Q2 2026 "
        "margin compression is the cost of that fight, and our base case assumes the "
        "spending continues: net margin glides from ~6.0% toward 11% over ten years, "
        "capturing roughly half of management's claimed 5–6 points of 'deferred' "
        "operating margin — deliberate humility on timing.",
        "Our base case (~14.9% ten-year revenue CAGR, tracking below the 2026–28 "
        "consensus path of +22.4%) assumes consensus-like growth with a slower margin "
        "recovery — the explicit source of our below-Street fair value. Fintech "
        "compounds on payments-data underwriting, the credit book keeps growing at a "
        "21%+ NIMAL, and advertising scales toward the highest-margin line in the "
        "company. The Q3 2026 print (expected early November) is the key test: consensus "
        "expects earnings growth to re-accelerate in H2 2026 after Q2's −15.7% YoY "
        "decline, and evidence that the investment program bends back toward margin "
        "expansion without growth deceleration would argue the deferred margin is real.",
        "The bear case ($116.16) is a genuine LatAm crisis path: ARS/BRL devaluation "
        "running through the margin path, credit-book stress with NPLs inflecting up, "
        "repatriation and FX effects living in margin compression — 3.0% revenue CAGR, "
        "7.5% year-10 net margins, a 16.5% discount rate, and a terminal value derated "
        "27.6% to force the case to hurt. The bull ($2,146.62): share gains compound, "
        "credit NIMAL holds above 20% while the book keeps compounding, ads scale toward "
        "Amazon-like margins, and FX cooperates — 19.1% CAGR, 12.5% margins. The Street's "
        "$2,272 average lives in the bull's neighborhood; our disagreement is the cost "
        "of capital, not the business.",
    ],
    "financials": [
        "The financial profile is that of a hypergrowth compounder in a deliberate "
        "reinvestment cycle. Revenue grew 39% in FY2025 to $28.9B and accelerated to +50% "
        "in Q2 2026 — the fastest in four years and the 30th straight quarter above 30%. "
        "Net income compounded at ~61% from 2022–25 ($482M → $2.0B). The Q2 2026 earnings "
        "miss on net income (EPS $9.19, −10.9% YoY) is fully explained by the investment "
        "program: operating margin fell 550bps YoY while gross profit still grew "
        "strongly. Gross margin was 44.5% in FY2025 (47.7% TTM); operating margin "
        "compressed to 6.7% in the quarter.",
        "We value owner earnings, not reported free cash flow: reported FCF (~$10.8B in "
        "FY2025) is operating cash flow minus capex and includes the credit book — "
        "growing loans consume cash through operating cash flow, and shrinking them "
        "would release it. We therefore model adjusted free cash flow (the company's "
        "definition: $1.48B in FY2025) as 0.8x net income, trending up as the credit "
        "book matures. Net debt is $7.462B. Our DCF implies 19.8x forward EPS — well "
        "below the quote's 29.9x — and the reverse-DCF shows the $1,696.56 price embeds "
        "~18% ten-year revenue growth with no margin of safety.",
    ],
    "fin_table": {
        "headers": ["", "FY2022", "FY2023", "FY2024", "FY2025", "TTM"],
        "rows": [
            ["Revenue ($bn)", "10.78", "15.11", "20.78", "28.89", "35.18"],
            ["YoY growth", "—", "+40.1%", "+37.5%", "+39.1%", "+49.8%"],
            ["Gross margin", "—", "—", "—", "44.5%", "47.7%"],
            ["Operating income ($bn) / margin", "1.07 / 9.9%", "2.21 / 14.6%", "2.63 / 12.7%", "3.20 / 11.1%", "— / 6.7%*"],
            ["Net income ($bn) / margin", "0.48", "0.99", "1.91", "2.00 / 6.9%", "1.86"],
            ["Diluted EPS", "$9.57", "$19.46", "$37.55", "$39.33", "—"],
            ["Adjusted FCF = 0.8× net income ($bn)", "0.38", "0.79", "1.53", "1.60", "—"],
        ],
        "footnote": "Company Q2 2026 release, FY2025 10-K/filings. *Q2 2026 operating margin "
                    "(−550bps YoY) on the strategic investment program. TTM = Q3'25–Q2'26. "
                    "Reported FCF (~$10.8B FY2025) includes the credit book; the valuation "
                    "uses adjusted FCF (0.8× net income).",
    },
    "moat": [
        ("Two-sided network density in commerce. ",
         "~40% of Brazilian e-commerce and co-leadership in Mexico create the liquidity "
         "— buyers and sellers — that regional rivals cannot replicate market by market."),
        ("Payments data → underwriting edge. ",
         "Mercado Pago's mostly off-platform volume generates proprietary transaction "
         "data that feeds superior credit underwriting — a data moat that compounds with "
         "every transaction and that pure lenders cannot buy."),
        ("Logistics as the defensive wall. ",
         "Mercado Envios' fulfillment density defends against Shopee/Temu on delivery "
         "speed and cost — the unglamorous moat that wins low-ticket share wars."),
        ("The moat's weak links: FX and the credit cycle. ",
         "Reports in USD, earns in BRL/ARS/MXN — Argentina is hyperinflationary-accounting "
         "with the peso near ~1,485/USD. And the $16B+ credit book means the moat is "
         "levered to the Brazilian consumer. Neither is fixable by execution."),
    ],
    "valuation_method": "10-year scenario DCF with explicit LatAm country-risk premium",
    "valuation_intro": [
        "We value MercadoLibre on a 10-year scenario DCF of owner earnings — adjusted "
        "free cash flow modeled as 0.8x net income, trending up as the credit book "
        "matures — weighted 25% / 50% / 25%. The defining judgment is the discount "
        "rate: a 14% base = 4.5% US risk-free + 1.44 beta × 5.5% equity risk premium + "
        "an explicit ~2% Latin America country-risk premium (ARS hyperinflation "
        "history, BRL volatility, Brazil tax reform, Mexico policy shifts; partial "
        "natural hedge via local-currency billing keeps it below the 250bp charged on "
        "China). Scenario rates: bear 16.5% (base + 250bp), bull 12.5% (base − 150bp, "
        "bull floor above 8% given the speculative EM tier).",
        "Terminal growth is 1.5% (bear) / 2.5% (base and bull), applied to year-10 free "
        "cash flow at normalized mid-cycle net margins (7.5% bear, 11% base, 12.5% "
        "bull) — not depressed 2026 levels — and the bear terminal is derated 27.6% to "
        "force the case to hurt. Net debt is $7.462B. Scenario fair values: $116.16 / "
        "$1,106.57 / $2,146.62, weighting to $1,118.98 — our $1,119 target, 34.0% below "
        "the $1,696.56 close. Operating projections are unchanged from the "
        "US-anchored-rate model; the +200bp on every discount rate is the entire "
        "verdict change (bear $161.85 → $116.16; base $1,442.45 → $1,106.57; bull "
        "$2,893.95 → $2,146.62).",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 116.16,
            "assumptions": ("LatAm crisis: credit shock + FX drag; ARS/BRL devaluation "
                            "through the margin path; credit-book stress; 3.0% revenue "
                            "CAGR; 7.5% year-10 net margin; terminal derated 27.6%."),
            "rev_cagr": "+3.0%", "margin_end": "7.5%",
            "discount": 0.165, "terminal_g": 0.015, "tv_share": 0.360,
            "pv_explicit": 8.55, "pv_terminal": 4.80, "cashflow_unit": "$bn",
        },
        "base": {
            "fair_value": 1106.57,
            "assumptions": ("Consensus-trajectory growth with slower margin recovery; "
                            "net margin glides ~6.0% → 11% over ten years (roughly half "
                            "of management's claimed deferred margin); 14.9% revenue CAGR."),
            "rev_cagr": "+14.9%", "margin_end": "11.0%",
            "discount": 0.14, "terminal_g": 0.025, "tv_share": 0.570,
            "pv_explicit": 27.33, "pv_terminal": 36.23, "cashflow_unit": "$bn",
        },
        "bull": {
            "fair_value": 2146.62,
            "assumptions": ("Share gains + credit compounding + ads scaling; credit "
                            "NIMAL holds above 20%; ads approach Amazon-like margins; "
                            "FX cooperates; 19.1% revenue CAGR; 12.5% year-10 margin."),
            "rev_cagr": "+19.1%", "margin_end": "12.5%",
            "discount": 0.125, "terminal_g": 0.025, "tv_share": 0.685,
            "pv_explicit": 36.58, "pv_terminal": 79.71, "cashflow_unit": "$bn",
        },
    },
    "scenario_note": "Composition PVs are derived from the note's disclosed terminal "
                     "values, scenario discount rates, $7.462B net debt, and scenario "
                     "fair values (EV = equity + net debt; PV of terminal value = "
                     "TV/(1+r)^10); they sum to each scenario's enterprise value. The "
                     "bear terminal is derated 27.6%.",
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "risks": [
        ("FX and translation (High). ",
         "Reports in USD, earns in BRL/ARS/MXN. Argentina is hyperinflationary-accounting; "
         "the peso sits near ~1,485/USD with ~17% further depreciation expected in 2026. "
         "BRL volatility is the largest single translation driver of reported growth."),
        ("Credit quality (High). ",
         "A $16B+ book growing 75% into a stressed Brazilian consumer. NPLs near historic "
         "lows today (7.0% / 4.6% card) and NIMAL recovered to 21%, but provisions doubled "
         "YoY in Q1 2026 and neobank industry delinquency has nearly tripled since 2021."),
        ("Argentina macro (Medium-High). ",
         "Disinflation is real but poverty rose to 32.3% in H1 2026 and consumption is "
         "'challenging' per management — a weak backdrop for both GMV and credit."),
        ("Regulatory (Medium-High). ",
         "BCB scrutiny of fintech lending; Pix ecosystem changes; Mexico's 2026 tax reform "
         "(already a GMV headwind); Brazil's cross-border import-tax regime in flux; "
         "COFECE antitrust overhang in Mexico."),
        ("Competition (Medium-High). ",
         "Amazon (deeper pockets, Prime, logistics build-out), Shopee (price), Temu/Shein "
         "(cross-border), Nubank (fintech). The −550bps Q2 2026 margin compression is "
         "partly the cost of this fight."),
        ("Valuation / multiple (Medium). ",
         "47x trailing earnings and 31x forward leave no room for execution slips; the "
         "stock fell 31% in twelve months on far less than a thesis break."),
    ],
    "falsification": (
        "We would revisit the REDUCE — toward HOLD or BUY — on a pullback toward $1,106 "
        "(base-case DCF territory, ~35% below the current price), or on Q3/Q4 2026 prints "
        "showing the reinvestment cycle bending back toward margin expansion without "
        "growth deceleration — evidence the 5–6 points of 'deferred' operating margin are "
        "real and recoverable — or on Latin American macro stabilization (Selic easing, "
        "BRL strength) that would argue the 200bp country-risk premium is too punitive. "
        "We would cut to SELL if NPLs inflect upward with provisions accelerating, on "
        "Brazil import-tax or Pix-regulation shocks to the take rate, or on sustained "
        "share loss to Amazon/Shopee in Brazil/Mexico. We watch: the Q3 print's margin "
        "trajectory, NPL and provision trends, Selic and BRL moves, and the credit "
        "book's growth versus NIMAL."
    ),
    "methodology": [
        "We value MercadoLibre on a 10-year scenario discounted-cash-flow framework "
        "built on owner earnings — adjusted free cash flow modeled as 0.8x net income, "
        "trending up as the credit book matures — because reported free cash flow "
        "includes the credit book (growing loans consume cash through operating cash "
        "flow). Scenarios are probability-weighted 25% / 50% / 25% with "
        "scenario-specific discount rates.",
        "The discount rate carries an explicit Latin America country-risk premium of "
        "200 basis points on every scenario: 14% base = 4.5% US risk-free + 1.44 beta × "
        "5.5% equity risk premium + ~2% LatAm premium (ARS hyperinflation history, BRL "
        "volatility, Brazil tax reform, Mexico policy shifts; local-currency billing is a "
        "partial natural hedge, so the premium sits below China's 250bp). Bear 16.5% "
        "(base + 250bp); bull 12.5% (base − 150bp, floored above 8% for the speculative "
        "EM tier). Terminal growth is 1.5%/2.5%/2.5% on year-10 free cash flow at "
        "normalized mid-cycle net margins — never depressed 2026 levels — and the bear "
        "terminal is derated 27.6% to force the case to hurt.",
        "Management's claim of 5–6 points of 'deferred' operating margin is haircut to "
        "roughly half in our margin path; we never anchor to guidance (MELI issues none "
        "— scenarios are calibrated to third-party consensus). Regional fintech comps "
        "are disclosed as a cross-check but rejected as the wrong peer set (pure "
        "fintech, not commerce+fintech+logistics+credit). The published target is the "
        "probability-weighted fair value, stated as a 12-month horizon reference. Risk "
        "ratings combine business volatility, balance-sheet strength, and valuation; "
        "High here reflects EM FX, credit-book, and regulatory risk.",
    ],
    "charts": {
        "scenario": {"bear": 116.16, "base": 1106.57, "bull": 2146.62,
                     "weighted": 1119.00, "price": 1696.56},
        "trajectory": {
            # history: revenue from filings; adjusted FCF = 0.8 x net income
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [10.78, 15.11, 20.78, 28.89],
            "fcf_hist": [0.38, 0.79, 1.53, 1.60],
            # base-case projection: 14.9% revenue CAGR; net margin 6.0% -> 11.0%; FCF = 0.8 x NI
            "years_proj": [2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": [40.5, 46.6, 53.5, 61.5, 70.7, 81.2, 93.4, 107.3, 123.4, 141.8],
            "fcf_proj": [1.94, 2.45, 3.04, 3.77, 4.65, 5.70, 6.97, 8.49, 10.31, 12.48],
            "unit": "$bn", "fcf_label": "Adj. FCF",
            "note": "History: company filings via Yahoo Finance; 'Adj. FCF' = 0.8× net "
                    "income (owner earnings — reported OCF−capex of ~$10.8B in FY2025 "
                    "includes the credit book and is not the valuation cash flow). "
                    "Projection: base-case path — revenue at the scenario's 14.9% CAGR "
                    "from the $35.2B TTM base; net margins gliding 6.0% to 11.0%; "
                    "adjusted FCF at 0.8× net income (year-10: $12.5B).",
        },
        "composition": {
            "bear": {"pv_explicit": 8.55, "pv_terminal": 4.80},
            "base": {"pv_explicit": 27.33, "pv_terminal": 36.23},
            "bull": {"pv_explicit": 36.58, "pv_terminal": 79.71},
            "unit": "$bn",
        },
        "extra": {
            "type": "pie",
            "title": "Revenue mix, Q2 2026 (fintech vs. commerce)",
            "labels": ["Commerce & other", "Fintech (Mercado Pago)"],
            "values": [57.0, 43.0],
        },
    },
}

validate(data)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "MELI-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
