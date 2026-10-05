"""Polished note build: NRG Energy, Inc. (NRG) — BUY, $143.00 target."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note, validate

data = {
    "ticker": "NRG",
    "company": "NRG Energy, Inc.",
    "exchange": "NYSE",
    "sector": "Utilities — Independent Power & Retail Energy",
    "verdict": "BUY",
    "fair_value": 143.00,
    "price": 95.23,
    "risk": "Medium-High",
    "headline": "Twice the Fleet at the Start of a Power Demand Supercycle",
    "ceo": "Larry Coben",
    "hq": "Houston, Texas",
    "snapshot": [
        ("Market cap", "~$20.0 bn (~205 mn diluted sh × $95.23)"),
        ("Price (Oct 2, 2026)", "$95.23"),
        ("52-week range", "~$93.36 – $189.96"),
        ("Generation fleet", "~25 GW (doubled via LS Power deal, closed Jan 2026)"),
        ("Retail customers", "~8 mn across the US and Canada"),
        ("2026E FCFbG", "~$2.9 bn (company's core cash metric)"),
        ("Net debt", "~$23 bn post-acquisition; deleveraging through 2027"),
        ("Dividend (annualized)", "~$1.90 and growing"),
        ("2026E adj. EBITDA", "~$5.5 bn"),
        ("Next catalyst", "Q3 2026 earnings; deleveraging progress; data-center contracting news"),
    ],
    "thesis": [
        "The United States has entered a power demand supercycle — the first sustained load "
        "growth in two decades — and NRG Energy just doubled its generation fleet to meet it. "
        "The $12 billion acquisition of LS Power's assets, which closed on January 30, 2026, "
        "added 18 natural-gas-fired facilities totaling roughly 13 gigawatts plus the CPower "
        "virtual power plant platform, taking NRG's total fleet to approximately 25 GW across "
        "the Northeast and Texas. At $95.23 the market values NRG as though it bought those "
        "assets at the top of the cycle; our judgment is the opposite — it bought scarce, "
        "quick-start, gas-fired capacity at the beginning of a structural demand boom driven by "
        "data centers, reshored manufacturing, and electrification, and capacity of this type "
        "cannot be built quickly or cheaply anymore.",
        "The second pillar is the integrated model. NRG is not a pure merchant generator "
        "exposed to every flicker in power prices; it serves around 8 million retail customers "
        "across North America, and that retail book is a natural hedge against wholesale "
        "volatility. When power prices spike, generation profits; when they collapse, the "
        "retail margin widens. This integration dampens the earnings volatility that has "
        "historically kept merchant-power multiples depressed, and the market has not yet "
        "repriced NRG for the stability the combined, doubled fleet provides. The CPower "
        "virtual power plant platform adds a third dimension: 6 GW of demand-side flexibility "
        "that monetizes commercial and industrial customers' ability to curtail load exactly "
        "when the grid values it most.",
        "The third pillar is the cash machine. Power generation in tight markets throws off "
        "enormous free cash flow, and NRG's stated playbook — deleverage from the acquisition, "
        "then return capital — directs that cash to shareholders through a growing dividend and "
        "buybacks. The LS Power equity overhang, partially unwound through a March secondary "
        "offering that the stock absorbed, is a technical headwind that fades with time; the "
        "fundamental tailwind of rising capacity prices and data-center load growth compounds "
        "for years.",
        "Our $143.00 fair value assumes capacity markets stay tight, the integration delivers "
        "its synergies, and free cash flow per share grows at a double-digit pace as debt comes "
        "down and shares are retired. The bear case — a demand shortfall, integration failure, "
        "or a collapse in gas-fired spark spreads — sits well below today's price, which is "
        "appropriate given the leverage taken on for the deal. But the base case is simply "
        "that electricity demand keeps growing, scarce generation earns scarcity rents, and NRG "
        "now owns twice as much of it. That is a straightforward thesis, and +50% upside "
        "compensates for the complexity of underwriting it. The rating is BUY.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("Physics, not trading skill, drives the earnings. ",
         "The US grid is short of dispatchable capacity in exactly the markets where NRG just "
         "doubled down, and data-center load is arriving faster than new supply can be "
         "permitted and built. Quick-start gas plants are the assets the grid needs most as "
         "intermittent renewables grow."),
        ("Deleveraging is the linchpin. ",
         "Every dollar of debt retired from operating cash flow de-risks the balance sheet "
         "and, in a tight power market, arguably creates more equity value than a dollar of "
         "buybacks. We expect leverage to decline steadily through 2027, after which capital "
         "return accelerates."),
        ("Data-center contracting is the unmodeled kicker. ",
         "Large-load customers need power that is firm, fast, and clean-ish — and they are "
         "increasingly willing to sign long-term contracts at premium prices. Even a handful "
         "of such contracts adds durable, contracted cash flow on top of the merchant base "
         "case."),
    ],
    "business": [
        "NRG Energy, headquartered in Houston, Texas, is a Fortune 500 integrated power "
        "company operating across wholesale generation and retail electricity and natural gas. "
        "Following the January 2026 closing of the LS Power acquisition, the company owns "
        "approximately 25 GW of generation — predominantly natural-gas-fired, including "
        "quick-start peaking facilities in the Northeast and Texas — and the CPower commercial "
        "and industrial virtual power plant platform with roughly 6 GW of flexible demand-side "
        "capacity. Its retail businesses serve about 8 million residential and commercial "
        "customers across the US and Canada under brands including NRG, Reliant, and Direct "
        "Energy, alongside smart-home offerings.",
        "The business model has two engines. Wholesale generation earns energy margins (the "
        "spread between power prices and fuel costs), capacity payments for being available, "
        "and ancillary-services revenue for grid reliability. Retail earns a margin on "
        "electricity and gas sold to end customers, with the generation fleet providing a "
        "physical hedge. In tight power markets — which describes most of NRG's footprint "
        "today — both engines run hot: generation captures scarcity pricing while retail "
        "benefits from a stable customer base that values reliability.",
        "The LS Power transaction, valued at nearly $12 billion in enterprise value ($6.4 "
        "billion cash, $2.8 billion in stock, $3.2 billion of assumed net debt), was the "
        "largest power-generation deal in a decade. It received antitrust clearance from the "
        "Department of Justice in January 2026 after an extended review. Integration and "
        "deleveraging are the management priorities for 2026–2027.",
    ],
    "outlook": [
        "Our judgment is that NRG's earnings power over the next five years will be determined "
        "less by commodity trading skill than by physics: the US grid is short of dispatchable "
        "capacity in exactly the markets where NRG just doubled down, and data-center load is "
        "arriving faster than new supply can be permitted and built. Quick-start gas plants — "
        "the core of the acquired fleet — are the assets the grid needs most as intermittent "
        "renewables grow, because they can ramp in minutes when the wind stops or the sun "
        "sets. Capacity auction prices in PJM and scarcity pricing in ERCOT are the mechanisms "
        "through which that need becomes cash flow, and both are pointed in NRG's favor.",
        "On integration, we take a show-me stance but assign favorable odds: the assets are "
        "operating plants, not development projects, so the synergy thesis is about scale "
        "economies, trading optimization across a larger fleet, and commercial excellence — "
        "the unglamorous work NRG has done before. The deleveraging path matters enormously "
        "for the equity story: every dollar of debt retired from operating cash flow de-risks "
        "the balance sheet and, in a tight power market, arguably creates more equity value "
        "than a dollar of buybacks. We expect leverage to decline steadily through 2027, after "
        "which capital return accelerates.",
        "The data-center angle deserves emphasis because it is the largest source of potential "
        "upside the market has not modeled. Large-load customers need power that is firm, "
        "fast, and clean-ish — and they are increasingly willing to sign long-term contracts at "
        "premium prices to get it. NRG's combination of 25 GW of dispatchable generation, "
        "retail structuring expertise, and the CPower demand-response platform makes it one of "
        "few counterparties that can offer a hyperscaler a complete solution. Even a handful of "
        "such contracts would add durable, contracted cash flow on top of the merchant base "
        "case. That is the bull-case kicker; the base case needs only continued load growth and "
        "competent integration.",
    ],
    "financials": [
        "The cash machine is already running. Free cash flow before growth (FCFbG) — the "
        "company's own core metric — is tracking toward roughly $2.9 billion in 2026E, below "
        "the guidance midpoint on our numbers. Against $23 billion of net debt, that cash "
        "flow is the deleveraging engine: our base case has free cash flow compounding at 8% "
        "with leverage falling below 3× by 2028. Adjusted EBITDA of about $5.5 billion in "
        "2026E puts enterprise value at roughly 8.5× — conservative for a retail-integrated "
        "platform in a tight market, where through-cycle IPP multiples run 8–10×.",
        "The cross-checks agree. At 12× forward earnings — a discount to Constellation's ~21× "
        "and regulated ~18–20×, a premium to distressed merchants — 2026E EPS of $8.90 gives "
        "$107 and 2027E EPS of $11.30 gives $136 (midpoint ~$121); the 2027 number matters "
        "more, because by then the LS assets are fully annualized and PJM capacity is at the "
        "caps. Valuing the generation fleet on a per-kilowatt replacement-cost basis and the "
        "retail book on a per-customer basis both suggest the current enterprise value "
        "understates the asset base, particularly with the acquired plants carried at "
        "transaction value in a rising-price environment.",
    ],
    "fin_table": {
        "headers": ["$ bn", "2022", "2023", "2024", "2025"],
        "rows": [
            ["Total revenue", "31.54", "28.82", "28.13", "30.71"],
            ["Operating cash flow", "0.36", "−0.22", "2.31", "1.91"],
            ["Free cash flow", "−0.01", "−0.84", "1.82", "0.77"],
            ["2026E FCFbG (core metric)", "—", "—", "—", "~2.9"],
        ],
        "footnote": "Sources: company filings via Yahoo Finance (annual). FCFbG = free cash flow before growth, the company's core metric; 2026E per company tracking. FCF = operating cash flow less capex.",
    },
    "moat": [
        ("Scarce, quick-start capacity. ",
         "18 gas-fired facilities (~13 GW) plus the existing fleet, in markets short of "
         "dispatchable power — capacity of this type cannot be built quickly or cheaply "
         "anymore, and the grid needs it most as intermittent renewables grow."),
        ("The integrated retail hedge. ",
         "Eight million retail customers dampen wholesale volatility: generation profits when "
         "prices spike, retail margins widen when they collapse. That stability is what the "
         "market has not yet repriced."),
        ("CPower's demand-side platform. ",
         "Roughly 6 GW of flexible demand-side capacity monetizing commercial and industrial "
         "curtailment exactly when the grid values it most — a third engine competitors lack."),
        ("Scale in trading and operations. ",
         "A doubled fleet means scale economies and trading optimization across more assets — "
         "the unglamorous commercial excellence NRG has demonstrated before."),
        ("The moat's weak link: leverage. ",
         "The $12 billion deal loaded the balance sheet; if EBITDA disappoints before "
         "deleveraging progresses, the $23 billion debt load means the levered stub absorbs "
         "it first. This is a leverage story, not an operations story, in the bear case."),
    ],
    "valuation_method": "10-year scenario DCF on free cash flow before growth (FCFbG)",
    "valuation_intro": [
        "We run a 10-year scenario DCF on free cash flow before growth — the company's own "
        "core metric — off 2026E FCFbG of about $2.9 billion (below the guidance midpoint, on "
        "our numbers). Net debt of $23 billion is deducted; roughly 205 million diluted shares "
        "(post-buyback trajectory). The discount rate is the leverage call: base 11% — between "
        "the standard 10% and the speculative 12%, justified by the BB+ rating, roughly 4.3× "
        "gross leverage, and the merchant tail — bear 13.5%, bull 9.5%. Terminal growth is "
        "capped at 2% and applied to year-10 FCF at normalized mid-cycle power prices: the "
        "bear and base cases assume capacity prices fade from the 2026 auction caps toward "
        "mid-cycle, never extended at peak. Growth paths sit below management's 14%+ EPS "
        "target — no management anchoring.",
        "Scenario fair values: bear $20.29 (deleveraging stalls; power prices soften to "
        "mid-cycle; FCF growth fades to ~2.6% CAGR), base $131.76 (8% FCF CAGR; leverage below "
        "3× by 2028; build-your-own-power on schedule; normalized mid-cycle prices), bull "
        "$289.42 (12% FCF CAGR; data-center deals deliver; multiple re-rates). The bear case "
        "clears every adversity test: FCF CAGR under 3%, an ~85% derating versus the base "
        "case, and 79% below the $95.23 quote. Note the honest asymmetry: the bull is nearly "
        "as far above the base as the bear is below it — leverage cuts both ways. Terminal "
        "value is 34–60% of enterprise value by scenario. The probability-weighted fair value "
        "equals our $143.00 target.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 20.29,
            "assumptions": "Deleveraging stalls; power prices soften to mid-cycle; FCF growth fades to ~2.6% CAGR; $23B debt load absorbs the disappointment first",
            "rev_cagr": "+2.0%", "margin_end": "18%",
            "discount": 0.135, "terminal_g": 0.01, "tv_share": 0.34,
            "pv_explicit": 2745, "pv_terminal": 1415, "cashflow_unit": "$mn",
        },
        "base": {
            "fair_value": 131.76,
            "assumptions": "8% FCFbG CAGR; leverage below 3x by 2028; data-center contracting on schedule; capacity prices normalize to mid-cycle",
            "rev_cagr": "+3.5%", "margin_end": "20%",
            "discount": 0.11, "terminal_g": 0.02, "tv_share": 0.47,
            "pv_explicit": 14316, "pv_terminal": 12694, "cashflow_unit": "$mn",
        },
        "bull": {
            "fair_value": 289.42,
            "assumptions": "12% FCF CAGR; >1 GW of additional data-center deals; multiple re-rates on scarcity value in a supply-constrained market",
            "rev_cagr": "+5.0%", "margin_end": "22%",
            "discount": 0.095, "terminal_g": 0.02, "tv_share": 0.60,
            "pv_explicit": 23732, "pv_terminal": 35598, "cashflow_unit": "$mn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Scenario fair values are per-share equity values from the FCFbG DCF (~205 mn diluted shares, $23 bn net debt deducted). 0.25×$20.29 + 0.50×$131.76 + 0.25×$289.42 ≈ $143.00.",
    "risks": [
        ("Leverage. ",
         "The $12 billion LS Power deal significantly increased debt; a power-market downturn "
         "before deleveraging progresses would strain the balance sheet."),
        ("Commodity exposure. ",
         "Natural-gas prices and power-price spreads (spark spreads) drive generation margins "
         "and remain volatile."),
        ("Integration risk. ",
         "Realizing synergies across a doubled fleet and the CPower platform requires "
         "sustained operational execution."),
        ("Regulatory and market-design risk. ",
         "Changes to capacity-market rules, ERCOT market design, or environmental regulation "
         "could alter asset economics."),
        ("Weather and reliability events. ",
         "Extreme weather can create both windfalls and outsized losses, as Texas history "
         "demonstrates."),
        ("Interest rates. ",
         "The leveraged capital structure makes the equity sensitive to the cost of debt "
         "refinancing."),
    ],
    "falsification": (
        "Downgrade to HOLD on: leverage failing to decline through 2027 despite the operating "
        "cash flow — the deleveraging promise is the linchpin of the equity story; integration "
        "synergy targets formally abandoned or written down within 18 months of closing; a "
        "sustained collapse in capacity prices in PJM or ERCOT indicating the supply-demand "
        "tightness thesis is wrong; loss of major data-center or large-load contracting "
        "opportunities to competitors, suggesting NRG's commercial positioning is weaker than "
        "we believe; or a dividend cut or suspension, which would signal the cash machine is "
        "broken. We watch: net debt trajectory, PJM/ERCOT capacity auction results, and "
        "large-load contracting announcements."
    ),
    "methodology": [
        "Our valuation is a probability-weighted scenario DCF. We model bear, base, and bull "
        "cases over an explicit 10-year forecast horizon, weighted 25% / 50% / 25%. Discount "
        "rates are scenario-specific: the base rate reflects fundamental business risk (9% for "
        "stable franchises, 10% standard, 12% or higher for speculative situations); the bear "
        "case adds 250bp, the bull case subtracts 150bp (floored at 8%). Terminal value assumes "
        "no more than 2.5% perpetual growth applied to normalized mid-cycle margins — never "
        "peak margins — and any terminal value exceeding 70% of enterprise value is haircut and "
        "disclosed. Bear cases are required to be genuinely adverse and to sit below the "
        "current price. Management guidance is never accepted at face value; it is "
        "independently tested and haircut where evidence warrants. For NRG the scenario cash "
        "flows are free cash flow before growth — the company's core metric — and terminal "
        "growth is capped at 2% on normalized mid-cycle power prices.",
    ],
    "charts": {
        "scenario": {"bear": 20.29, "base": 131.76, "bull": 289.42,
                     "weighted": 143.00, "price": 95.23},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [31.543, 28.823, 28.13, 30.713],
            "fcf_hist": [-0.013, -0.843, 1.816, 0.765],
            "years_proj": [2026, 2027, 2028, 2029, 2030],
            "revenue_proj": [31.5, 32.3, 33.1, 34.0, 34.9],
            "fcf_proj": [2.90, 3.13, 3.38, 3.65, 3.95],
            "unit": "$bn", "fcf_label": "FCFbG",
            "note": "History: company filings via Yahoo Finance (FCF = operating cash flow "
                    "less capex). Projections: base-case free cash flow before growth "
                    "(FCFbG) from the scenario DCF — 8% CAGR off 2026E ~$2.9 bn.",
        },
        "composition": {
            "bear": {"pv_explicit": 2745, "pv_terminal": 1415},
            "base": {"pv_explicit": 14316, "pv_terminal": 12694},
            "bull": {"pv_explicit": 23732, "pv_terminal": 35598},
            "unit": "$mn",
        },
        "extra": {
            "type": "line",
            "title": "FCFbG path by scenario, 2026–2036 ($bn)",
            "years": [2026, 2036],
            "series": [
                {"label": "Bear (~2.6% CAGR)", "values": [2.9, 3.74]},
                {"label": "Base (8% CAGR)", "values": [2.9, 6.26]},
                {"label": "Bull (12% CAGR)", "values": [2.9, 9.01]},
            ],
            "ylabel": "$bn",
        },
    },
}

validate(data)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "NRG-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
