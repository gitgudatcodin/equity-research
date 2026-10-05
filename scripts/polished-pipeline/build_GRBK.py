"""Polished note: Green Brick Partners (GRBK) — SELL, fair value $41.00.

Scenario numbers are from the current 10-year scenario DCF model
(valuation_output_v2.json): bear $7.41 / base $41.10 / bull $74.58, weighted
25/50/25 to the $41 target. Discounts 14.5%/12%/10.5%; terminal growth
1.0%/2.5%/2.5%; revenue CAGR -0.5%/+5.0%/+7.0%; year-10 FCF margins
4.5%/8.5%/11.0%. DCF composition is derived from a stylized 10-year model
with those stated parameters (revenue from the FY2025 $2.04B base, FCF
margins gliding from the current ~10.3% to scenario terminal margins),
scaled so the composition sums exactly to each scenario's equity value at
43.0m diluted shares: bear PV-explicit $263m / PV-terminal $56m; base
$1,029m / $738m; bull $1,500m / $1,707m (terminal-value shares 17.6%/41.8%/
53.2%). Footnote discloses the derivation.
History: company filings via Yahoo Finance (Oct 2026; FCF = operating cash
flow less capex). Trajectory projection: base-case path at 5% revenue CAGR
with FCF margins gliding to 8.5%. All prose is fresh October 4, 2026
analysis.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note, validate

data = {
    "ticker": "GRBK",
    "company": "Green Brick Partners, Inc.",
    "exchange": "NYSE",
    "sector": "Consumer Cyclical — Residential Construction",
    "verdict": "SELL",
    "fair_value": 41.00,
    "price": 66.66,
    "risk": "High",
    "headline": "A well-managed builder priced as though the housing cycle had been abolished",
    "ceo": "James R. Brickman",
    "hq": "Plano, Texas",
    "snapshot": [
        ("Market cap", "~$2.9 bn (43.0 m sh × $66.66)"),
        ("52-week range", "~$60 – $83"),
        ("Price / fair value", "$66.66 / $41.00"),
        ("Implied downside", "−38.5%"),
        ("FY2025 revenue / net income", "$2.04 bn / $0.31 bn"),
        ("FY2024 net margin (cyclical peak)", "18.4%"),
        ("TTM P/E", "~10.7x — the classic peak-E trap"),
        ("Footprint", "Sunbelt: Dallas–Fort Worth, other Texas markets, Atlanta, Florida, Colorado"),
        ("Builder brands", "Trophy Signature, CB JENI, Normandy, Southgate, Centre Living, Providence Group, GHO"),
        ("Next catalyst", "Q3 2026 results (late October) — order rates and cancellation rates"),
    ],
    "thesis": [
        "Green Brick Partners is a well-managed Sunbelt homebuilder being valued as "
        "though the housing cycle had been abolished. The company has grown impressively "
        "— concentrated in Texas and other high-growth Sunbelt markets, with a land-light "
        "option model in several divisions and a deserved reputation for operational "
        "execution under co-founder and CEO James Brickman. But homebuilding is among "
        "the most cyclical industries in the economy, and Green Brick's current earnings "
        "reflect cyclical peak conditions: constrained resale supply, elevated prices, "
        "and margins fattened by years of underbuilding. On a through-cycle basis — "
        "normalizing margins to mid-cycle levels at a 12% discount rate appropriate for "
        "a leveraged cyclical — the shares are worth $41.00, 38.5% below the $66.66 "
        "quote. SELL.",
        "Those peak conditions are normalizing in real time. Affordability sits near "
        "historic lows: the combination of elevated home prices and mortgage rates has "
        "pushed the monthly payment on a median new home beyond the reach of the median "
        "household in Green Brick's core markets. Builders are responding the way they "
        "always do — incentives, rate buydowns, and price reductions that compress "
        "margins from both ends. Order rates are softening, cancellation rates are "
        "rising, and spec inventory is building. The 18.4% net margin of FY2024 was the "
        "top of the cycle, not the new normal; our base case glides free-cash-flow "
        "margins from today's ~10% toward 8.5% over ten years, and the bear case takes "
        "them to 4.5% — because that is what homebuilder margins do in downturns.",
        "The valuation math is unforgiving for cyclical peaks. At $66.66 the market "
        "pays a full multiple of earnings that are themselves at a cyclical high — the "
        "late-cycle trap of a low P/E on peak E (~10.7x trailing looks cheap until the E "
        "is cut in half). Investors sometimes argue that Green Brick's premium land "
        "positions and Texas footprint justify a premium multiple through the cycle. We "
        "agree the footprint is superior — which is exactly why the shares should be "
        "bought after the downturn impairs lesser builders, not before. Quality "
        "homebuilders outperform by surviving downturns with balance sheets intact and "
        "buying distressed land from failures; paying peak prices for that quality "
        "inverts the entire logic of cyclical investing. The business is good; the "
        "cycle is not. Investors are being paid nothing for the downside of owning a "
        "cyclical at the top, and the downside in homebuilding downturns is measured "
        "not in multiple compression but in land impairments and earnings collapses. "
        "SELL.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("Peak-E is the whole argument. ",
         "~10.7x trailing earnings looks like value until the earnings are the "
         "variable. In the last housing downturn, builder earnings didn't compress — "
         "they collapsed, and land impairments did the rest. The multiple is low "
         "because the earnings are high, not because the price is low."),
        ("The leading indicators are already rolling. ",
         "Softening order rates, rising cancellations, building spec inventory, and "
         "incentives/buydowns compressing margins from both ends — this is the "
         "standard sequence, and it is underway."),
        ("Land-light is a mitigant, not immunity. ",
         "The option model in several divisions limits impairment exposure — but "
         "option deposits get walked away from, counterparties fail, and earnings "
         "still fall when absorption slows. It softens the cycle; it doesn't abolish "
         "it."),
    ],
    "business": [
        "Green Brick Partners is a residential homebuilder focused on high-growth "
        "Sunbelt markets: principally the Dallas–Fort Worth metroplex along with other "
        "Texas markets, Atlanta, and select Southeast markets including Florida, with a "
        "non-controlling interest in a Colorado builder. The company builds "
        "single-family homes across move-up and luxury segments through seven "
        "subsidiary brands — Trophy Signature Homes, CB JENI Homes, Normandy Homes, "
        "Southgate Homes, Centre Living Homes, The Providence Group (Atlanta), and "
        "GHO Homes (Florida) — plus related title and mortgage platforms. Chairman "
        "David Einhorn co-founded the company; CEO James Brickman has run it since "
        "inception.",
        "The operating model blends traditional homebuilding with a land-light option "
        "strategy in several divisions: controlling lots through options rather than "
        "ownership, which reduces balance-sheet intensity and impairment exposure "
        "relative to land-heavy peers. The Texas concentration is both the strength "
        "and the concentration risk — DFW's population and job growth underwrite "
        "demand, but a Texas-centric downturn (energy, in-migration reversal) hits "
        "every division at once.",
        "This is a company we would want to own — after the cycle turns. The "
        "reputation for execution, the balance-sheet discipline, and the land-light "
        "model are exactly the attributes that let quality builders buy distressed "
        "land from failures in downturns. The SELL is a call on price and cycle "
        "position, not on management.",
    ],
    "business_bullets": [
        ("Seven brands, one Sunbelt footprint. ",
         "Trophy Signature (scaled from a 2018 start-up to a leading DFW builder), "
         "CB JENI, Normandy, Southgate, Centre Living, Providence Group (Atlanta), "
         "GHO (Florida) — diversified by brand, concentrated by geography."),
        ("Land-light option model. ",
         "Lot options rather than ownership in several divisions: less capital "
         "intensity, less impairment exposure — a genuine structural advantage that "
         "softens but does not abolish the cycle."),
        ("Texas concentration cuts both ways. ",
         "DFW and Texas job/population growth are the demand engine — and the "
         "correlated risk. A regional downturn impairs every division simultaneously."),
        ("The downturn playbook is the bull case — later. ",
         "Survive with the balance sheet intact, buy distressed land from failures. "
         "That logic requires buying after the impairment cycle, not before it."),
    ],
    "outlook": [
        "The cycle sequence from here is well established: incentives and rate buydowns "
        "compress gross margins first, then order rates soften, then cancellations "
        "rise, then spec inventory builds, then land gets impaired. Green Brick is in "
        "the early stages of that sequence now. Our base case assumes the "
        "normalization runs its course without a severe recession: revenue compounds "
        "at 5% for ten years (from $2.04B toward ~$3.3B) while free-cash-flow margins "
        "glide from today's ~10% to 8.5% — mid-cycle profitability for a well-run "
        "builder. Fair value: $41.10.",
        "The bear case ($7.41) is the full housing downturn: revenue shrinking 0.5% a "
        "year, FCF margins collapsing to 4.5%, a 14.5% discount rate for a leveraged "
        "cyclical in distress, and 1% terminal growth. The bull case ($74.58) "
        "requires the cycle to extend — rates falling back, affordability restored, "
        "7% revenue CAGR with 11% FCF margins — and even then offers only ~12% upside "
        "from $66.66. When the bull case is barely above the price, the risk-reward "
        "is fully inverted.",
        "The falsification markers are the cycle's own leading indicators: a "
        "sustained re-acceleration in net new orders with cancellation rates falling "
        "back to normal, spec inventory clearing without margin sacrifice, and "
        "mortgage rates declining enough to restore affordability in the core Texas "
        "markets. If absorptions recover and incentives roll off while margins hold, "
        "the peak-earnings thesis is wrong and the shares deserve a higher multiple. "
        "Until then, the cycle is doing what cycles do.",
    ],
    "financials": [
        "The financial profile is peak-cycle homebuilding. Revenue grew from $1.76B in "
        "FY2022 to $2.04B in FY2025; net income peaked at $0.38B in FY2024 (an 18.4% "
        "net margin — the cyclical top) and eased to $0.31B in FY2025. Free cash flow "
        "(operating cash flow less capex) has been lumpy — $0.09B, $0.20B, $0.03B, "
        "$0.21B across FY2022–25 — as land investment and working capital swing with "
        "the cycle. The ~10.7x trailing P/E is the trap: it prices peak earnings as "
        "permanent.",
        "Our scenario DCF discounts at 12% in the base case (14.5% bear, 10.5% bull) — "
        "a leveraged cyclical's cost of capital, not a growth company's. Terminal "
        "value is 42% of base-case enterprise value; only 18% in the bear case "
        "($319m equity value — the impairments-and-collapse path) and 53% in the bull. "
        "The composition reflects the call: most of the base-case value must come "
        "from the explicit ten-year cash flows because the terminal multiple on "
        "normalized mid-cycle earnings is modest. At 43.0m diluted shares, the "
        "probability-weighted $41 target sits 38.5% below the quote.",
    ],
    "fin_table": {
        "headers": ["$bn", "FY2022", "FY2023", "FY2024", "FY2025"],
        "rows": [
            ["Revenue", "1.76", "1.75", "2.06", "2.04"],
            ["Net income", "0.29", "0.28", "0.38", "0.31"],
            ["Net margin", "16.5%", "16.0%", "18.4%", "15.2%"],
            ["Free cash flow (OCF − capex)", "0.09", "0.20", "0.03", "0.21"],
            ["Diluted shares (m)", "~43", "~43", "~43", "43.0"],
        ],
        "footnote": "Company filings via Yahoo Finance. FY2024's 18.4% net margin "
                    "marks the cyclical peak; the valuation normalizes margins to "
                    "mid-cycle levels.",
    },
    "moat": [
        ("Sunbelt land positions in supply-constrained submarkets. ",
         "Premium DFW and Atlanta positions, partly controlled via options — "
         "genuinely superior footprint that compounds in upcycles and defends "
         "better in downturns."),
        ("Operator reputation and balance-sheet discipline. ",
         "A deserved reputation for execution and a land-light model that limits "
         "impairment exposure — the attributes that let quality builders buy "
         "distressed land from failures."),
        ("Scale economies in procurement and mortgage capture. ",
         "Seven brands' combined purchasing power and captive title/mortgage "
         "platforms add basis points competitors can't match."),
        ("The moat's limits: cyclicality dominates everything. ",
         "No land position or operator skill prevents earnings from collapsing in a "
         "housing downturn — and Texas concentration means the cycle hits every "
         "division at once. The moat determines who survives; it doesn't determine "
         "the price to pay at the top."),
    ],
    "valuation_method": "10-year scenario DCF (through-cycle normalization)",
    "valuation_intro": [
        "We value Green Brick on a 10-year scenario discounted-cash-flow framework, "
        "weighted 25% / 50% / 25%, built on through-cycle normalization — the "
        "correct lens for a cyclical at peak earnings. Revenue compounds from the "
        "FY2025 $2.04B base at −0.5% (bear) / +5.0% (base) / +7.0% (bull); "
        "free-cash-flow margins glide from the current ~10.3% to 4.5% / 8.5% / 11.0% "
        "at year ten. Discount rates are a cyclical's cost of capital: 12% base, "
        "14.5% bear (+250bp), 10.5% bull (−150bp). Terminal growth is 1.0% / 2.5% / "
        "2.5% on year-10 free cash flow at normalized mid-cycle margins.",
        "Scenario fair values: $7.41 (bear — full housing downturn, impairments, "
        "earnings collapse) / $41.10 (base — orderly normalization to mid-cycle "
        "profitability) / $74.58 (bull — cycle extends on falling rates, affordability "
        "restored). The probability-weighted value is $41.00 — our target, 38.5% "
        "below the $66.66 close. The DCF composition is derived from a stylized "
        "10-year model using these stated parameters, scaled to reconcile exactly to "
        "each scenario's equity value at 43.0m diluted shares; terminal value is "
        "17.6% / 41.8% / 53.2% of scenario equity value.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 7.41,
            "assumptions": ("Full housing downturn: revenue −0.5% CAGR; FCF margins "
                            "collapse to 4.5%; land impairments; 14.5% discount; 1.0% "
                            "terminal growth."),
            "rev_cagr": "−0.5%", "margin_end": "4.5%",
            "discount": 0.145, "terminal_g": 0.01, "tv_share": 0.176,
            "pv_explicit": 263.0, "pv_terminal": 56.0, "cashflow_unit": "$m",
        },
        "base": {
            "fair_value": 41.10,
            "assumptions": ("Orderly normalization to mid-cycle profitability: +5.0% "
                            "revenue CAGR; FCF margins glide ~10.3% → 8.5%; 12% "
                            "discount; 2.5% terminal growth."),
            "rev_cagr": "+5.0%", "margin_end": "8.5%",
            "discount": 0.12, "terminal_g": 0.025, "tv_share": 0.418,
            "pv_explicit": 1029.0, "pv_terminal": 738.0, "cashflow_unit": "$m",
        },
        "bull": {
            "fair_value": 74.58,
            "assumptions": ("Cycle extends: rates fall, affordability restored; +7.0% "
                            "revenue CAGR; FCF margins to 11.0%; 10.5% discount; 2.5% "
                            "terminal growth."),
            "rev_cagr": "+7.0%", "margin_end": "11.0%",
            "discount": 0.105, "terminal_g": 0.025, "tv_share": 0.532,
            "pv_explicit": 1500.0, "pv_terminal": 1707.0, "cashflow_unit": "$m",
        },
    },
    "scenario_note": "Composition PVs are derived from a stylized 10-year model "
                     "using the stated scenario parameters (revenue from the FY2025 "
                     "$2.04B base; FCF margins gliding from ~10.3% to scenario "
                     "terminal margins), scaled to reconcile exactly to each "
                     "scenario's equity value at 43.0m diluted shares.",
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "risks": [
        ("Housing cycle (High). ",
         "The #1 risk: affordability near historic lows, softening orders, rising "
         "cancellations, building spec inventory. Downturns bring land impairments "
         "and earnings collapses, not gentle multiple compression."),
        ("Texas concentration (High). ",
         "DFW and Texas markets dominate; a regional downturn (energy, in-migration "
         "reversal) impairs every division simultaneously."),
        ("Mortgage-rate sensitivity (High). ",
         "Elevated rates price the median household out of the median new home in "
         "core markets; further increases deepen the affordability crisis."),
        ("Margin compression (Medium-High). ",
         "Incentives, rate buydowns, and price reductions compress from both ends — "
         "already underway."),
        ("Land and option-counterparty risk (Medium). ",
         "The land-light model mitigates but doesn't eliminate exposure: option "
         "deposits are walked away from and counterparties can fail."),
        ("Execution on growth (Medium). ",
         "Seven brands and rapid scaling (Trophy Signature from 2018 start-up) "
         "require sustained operational excellence through a downturn."),
    ],
    "falsification": (
        "We would revisit the SELL if the cycle's leading indicators reverse "
        "together: net new orders re-accelerating with cancellation rates falling "
        "back to normal levels, spec inventory clearing without margin sacrifice, "
        "and mortgage rates declining enough to restore affordability in the core "
        "Texas markets — with gross margins holding as incentives roll off. That "
        "combination would mean peak earnings were not the peak, and the shares "
        "would deserve a higher multiple on durable earnings. We would cut the "
        "target further toward the bear case on evidence of land impairments, "
        "order cancellations spiking, or a Texas regional demand shock. We watch: "
        "monthly order and cancellation rates, spec inventory levels, incentive "
        "spend per closing, and DFW affordability metrics."
    ),
    "methodology": [
        "We value Green Brick on a 10-year scenario discounted-cash-flow framework, "
        "probability-weighted 25% / 50% / 25%, built on through-cycle normalization: "
        "revenue compounds from the current base under scenario CAGRs while "
        "free-cash-flow margins glide from current levels to scenario terminal "
        "margins (mid-cycle profitability, never peak margins). For cyclicals, "
        "anchoring the terminal year to peak earnings is the classic error; we "
        "anchor to mid-cycle.",
        "Discount rates are a leveraged cyclical's cost of capital — 12% base, "
        "14.5% bear (+250bp), 10.5% bull (−150bp) — and terminal growth is 1.0% "
        "(bear) / 2.5% (base, bull) on year-10 free cash flow. The bear case is "
        "required to be genuinely adverse and to sit below the current price; "
        "terminal value exceeding 70% of enterprise value is haircut and disclosed "
        "(41.8% base, 53.2% bull, 17.6% bear — no haircut required). The DCF "
        "composition is derived from a stylized model with the stated parameters, "
        "scaled to reconcile to scenario equity values.",
        "The published target is the probability-weighted fair value, stated as a "
        "12-month horizon reference. Risk ratings (Low / Medium / Medium-High / "
        "High) combine business volatility, balance-sheet strength, and valuation; "
        "High here reflects peak-cycle earnings, housing cyclicality, and Texas "
        "concentration.",
    ],
    "charts": {
        "scenario": {"bear": 7.41, "base": 41.10, "bull": 74.58,
                     "weighted": 41.00, "price": 66.66},
        "trajectory": {
            # history: filings via Yahoo Finance; FCF = OCF - capex
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [1.76, 1.75, 2.06, 2.04],
            "fcf_hist": [0.09, 0.20, 0.03, 0.21],
            # base-case projection: 5% revenue CAGR; FCF margins gliding ~10.3% -> 8.5%
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035],
            "revenue_proj": [2.14, 2.25, 2.36, 2.48, 2.60, 2.73, 2.87, 3.01, 3.17, 3.32],
            "fcf_proj": [0.22, 0.22, 0.23, 0.24, 0.24, 0.25, 0.26, 0.27, 0.27, 0.28],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via Yahoo Finance (FCF = operating cash "
                    "flow less capex). Projection: base-case path — revenue at 5% "
                    "CAGR with free-cash-flow margins gliding from ~10.3% toward "
                    "mid-cycle 8.5%.",
        },
        "composition": {
            "bear": {"pv_explicit": 263.0, "pv_terminal": 56.0},
            "base": {"pv_explicit": 1029.0, "pv_terminal": 738.0},
            "bull": {"pv_explicit": 1500.0, "pv_terminal": 1707.0},
            "unit": "$m",
        },
        "extra": {
            "type": "line",
            "title": "Margins: peak net income (history) vs. normalizing FCF (base case)",
            "years": [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035],
            "series": [{"label": "Net income margin (hist.)",
                        "values": [16.5, 16.0, 18.4, 15.2, None, None, None, None, None, None, None, None, None, None]},
                       {"label": "Base-case FCF margin (proj.)",
                        "values": [None, None, None, None, 10.1, 9.9, 9.8, 9.6, 9.4, 9.2, 9.0, 8.9, 8.7, 8.5]}],
            "ylabel": "%",
            "note": "FY2024's 18.4% net margin marks the cyclical peak; the base case "
                    "normalizes free-cash-flow margins toward mid-cycle 8.5%.",
        },
    },
}

validate(data)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "GRBK-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
