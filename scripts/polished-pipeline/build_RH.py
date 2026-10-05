"""Polished note build: RH (RH) — BUY, $177.00 target."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note, validate

data = {
    "ticker": "RH",
    "company": "RH",
    "exchange": "NYSE",
    "sector": "Consumer Discretionary — Luxury Home Furnishings",
    "verdict": "BUY",
    "fair_value": 177.00,
    "price": 120.46,
    "risk": "High",
    "headline": "A Luxury Platform Priced as a Cyclical Furniture Stock",
    "ceo": "Gary Friedman",
    "hq": "Corte Madera, California",
    "snapshot": [
        ("Market cap", "~$2.3 bn (~18.9 mn sh × $120.46)"),
        ("Price (Oct 2, 2026)", "$120.46"),
        ("52-week range", "~$106.30 – $239.40"),
        ("Net financial debt", "~$2.26 bn (4.2× net debt/EBITDA)"),
        ("Book equity", "~$61 mn — the equity is a levered call option"),
        ("$2.5 bn maturity", "October 2028 — the refinancing watch item"),
        ("Galleries", "Design Galleries in the US + UK/Europe; hospitality (restaurants, guesthouses)"),
        ("Collections", "RH Interiors, Modern, Contemporary, Outdoor, Baby & Child, Teen"),
        ("Next catalyst", "Q3 2026 earnings; same-gallery sales; housing-turnover data"),
    ],
    "thesis": [
        "RH — the luxury home-furnishings company — is a different business than the furniture "
        "retailer the market thinks it is. Over the past decade it has transformed from a "
        "mall-based catalog company into a luxury ecosystem: massive design galleries that "
        "function as hospitality destinations, restaurants and wine bars inside the stores, "
        "guesthouses, and a product line that spans furniture, lighting, textiles, and "
        "outdoor. The gallery model does two things simultaneously: it justifies premium "
        "pricing through experience, and it concentrates demand into fewer, larger, more "
        "productive locations. At $120.46 the market prices RH as a cyclical furniture stock "
        "at the top of a housing cycle; we see a luxury platform still in the middle of its "
        "expansion.",
        "The core of the thesis is operating leverage on a revenue recovery. RH's cost "
        "structure carries significant fixed costs — the galleries, the supply chain, the "
        "design organization — which means that when revenue grows, a large share of the "
        "incremental dollar falls to operating profit. The past two years of housing-market "
        "softness have depressed revenue and made margins look structurally impaired; our "
        "judgment is that they are cyclically depressed. As housing turnover normalizes and "
        "the wealthy consumer — RH's customer — keeps spending, revenue reacceleration should "
        "drive margin expansion of several hundred basis points, a dynamic the current "
        "valuation barely credits.",
        "The longer-term leg is international and hospitality. RH's expansion into Europe — "
        "with galleries in England and on the continent — and its growing hospitality "
        "footprint extend the brand beyond American home furnishings into global luxury "
        "lifestyle. Luxury is the most durable category in consumer discretionary, and RH is "
        "one of very few American brands playing in it with an integrated physical "
        "experience. Each new gallery is a multi-year comp driver; each hospitality venue "
        "deepens the brand halo that supports pricing power.",
        "Founder-CEO Gary Friedman's capital allocation adds a final kicker: RH has "
        "repeatedly repurchased shares aggressively when the stock has been weak, shrinking "
        "the share count at prices that reward long-term holders. Our $177.00 fair value "
        "assumes a mid-cycle revenue base with normalized margins — not peak housing-boom "
        "economics — and values the international and hospitality options at a fraction of "
        "what they could become. The bear case, in which housing stays soft and gallery "
        "investments disappoint, sits below today's price; but the base case is simply that "
        "luxury demand mean-reverts and the operating leverage does the rest. The rating is "
        "BUY — sized for a High-risk, levered-equity call option.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("Fixed-cost leverage cuts both ways — and revenue is the lever. ",
         "Galleries, supply chain, and design are fixed costs; a return toward average "
         "housing turnover amplifies even a modest revenue recovery into substantial earnings "
         "growth. We do not need a housing boom."),
        ("The gallery maturation curve is embedded comp growth. ",
         "New galleries ramp over several years as local awareness builds and the hospitality "
         "components establish themselves — the recent cohort is still climbing that curve, "
         "which means growth requiring no new capital."),
        ("Luxury demand is the most durable in consumer discretionary. ",
         "RH's customer — the affluent homeowner — has proven resilient across cycles. As RH "
         "becomes less correlated with the furniture cycle and more with global luxury "
         "demand, the multiple should follow."),
    ],
    "business": [
        "RH, headquartered in Corte Madera, California, is a luxury home-furnishings company "
        "operating through collections including RH Interiors, RH Modern, RH Contemporary, RH "
        "Outdoor, RH Baby & Child, and RH Teen. Its defining strategic asset is the Design "
        "Gallery network: very large-format retail destinations — often 50,000-plus square "
        "feet across multiple levels — that combine fully furnished room installations with "
        "restaurants, wine bars, and rooftop hospitality spaces. The company has also expanded "
        "into hospitality proper with RH Guesthouses and a growing restaurant portfolio, and "
        "internationally with galleries in the United Kingdom and Europe.",
        "The economic model is luxury retail: high average order values, premium gross margins "
        "supported by brand and design differentiation, and a deliberately limited promotional "
        "posture. Revenue is driven by gallery productivity, new gallery openings, and the "
        "Sourcebook catalog circulation that still functions as a high-end direct-marketing "
        "engine. The fixed-cost base — gallery leases and staffing, the supply chain, product "
        "development — creates the operating leverage that defines the investment case in both "
        "directions.",
        "RH's customer is the affluent homeowner, a cohort whose spending has proven resilient "
        "across cycles relative to mass-market furniture retail. The company sources globally "
        "and sells primarily in North America, with international expansion representing the "
        "next leg of the growth algorithm. Capital allocation under founder leadership has "
        "favored share repurchases during periods of stock weakness alongside continued "
        "investment in the gallery and hospitality footprint.",
    ],
    "outlook": [
        "Our judgment is that RH's earnings over the next three to five years will be driven "
        "by three compounding forces. First, the housing cycle: existing-home sales have been "
        "depressed by elevated mortgage rates, and furniture demand correlates strongly with "
        "housing turnover. Any normalization — from lower rates, demographic household "
        "formation, or simply time — flows disproportionately to RH's bottom line because of "
        "the fixed-cost leverage. We do not need a housing boom; we need a return toward "
        "average turnover, and the operating leverage amplifies even a modest recovery into "
        "substantial earnings growth.",
        "Second, the gallery maturation curve. New galleries typically ramp over several "
        "years as local awareness builds and the hospitality components — which drive foot "
        "traffic far beyond furniture shoppers — establish themselves. The cohort of galleries "
        "opened in recent years is still climbing that curve, which means embedded comp "
        "growth that requires no new capital. International galleries extend this dynamic: if "
        "the European locations replicate even a portion of US gallery economics, they add a "
        "multi-year growth vector the market currently values at roughly zero.",
        "Third, brand extension into hospitality and adjacent luxury categories. The "
        "restaurants and guesthouses are not side projects — they are the mechanism by which "
        "RH converts furniture shoppers into luxury-lifestyle adherents, deepening the moat "
        "around pricing power. Our forward view is that RH slowly becomes less correlated "
        "with the furniture cycle and more correlated with global luxury demand, a transition "
        "that — if it continues — justifies a higher multiple than furniture retail has ever "
        "commanded. The risk is execution: galleries are capital-intensive, international "
        "expansion has humbled many retailers, and luxury positioning is fragile if quality or "
        "service slips. But the trajectory of the past decade argues the team knows how to "
        "build this.",
    ],
    "financials": [
        "Leverage makes this equity a call option, and the valuation is priced for it. Net "
        "financial debt of about $2.26 billion against 4.2× net debt/EBITDA, book equity of "
        "roughly $61 million, a $2.5 billion maturity in October 2028, and a beta of 1.86 — "
        "the capital structure is the reason the base discount rate is 12%, the speculative "
        "tier. In the bear case — housing frozen, tariffs lingering, gallery investments "
        "underwhelming — firm enterprise value of $2.0 billion against $2.26 billion of debt "
        "leaves the equity at roughly zero. That is the honest downside, and it sits below "
        "today's price as the framework requires.",
        "In the base case, revenue compounds 6.9% to about $7.1 billion, margins recover "
        "toward 20% EBITDA on the fixed-cost leverage, and free cash flow runs from $350 "
        "million toward $848 million — the firm is worth $5.9 billion and the equity $190.73 "
        "per share over 18.93 million shares. The spread is the story: 4.2× leverage means "
        "the equity captures a disproportionate share of any recovery, which is exactly what "
        "the probability-weighted $177.00 target prices.",
    ],
    "fin_table": {
        "headers": ["$ mn", "FY2023", "FY2024", "FY2025", "FY2026"],
        "rows": [
            ["Total revenue", "3,590", "3,029", "3,181", "3,440"],
            ["YoY growth", "—", "−15.6%", "+5.0%", "+8.1%"],
            ["Operating cash flow", "404", "202", "17", "452"],
            ["Free cash flow", "230", "−67", "−214", "249"],
            ["Base-case FCF path", "—", "—", "—", "350 → 848 (FY35)"],
        ],
        "footnote": "Sources: company filings via Yahoo Finance (fiscal years ending late January; FY2026 = year to Jan 2026). Base-case FCF path per the scenario DCF. FCF = operating cash flow less capex.",
    },
    "moat": [
        ("Brand + experience + ecosystem — narrow-to-moderate, widening. ",
         "Experiential flagships competitors cannot copy cheaply, membership economics, "
         "design IP, and hospitality that manufactures desire. The moat widens if the "
         "international and hospitality extensions execute."),
        ("The gallery as a hospitality destination. ",
         "Restaurants, wine bars, and rooftop spaces inside 50,000-plus-square-foot "
         "galleries drive foot traffic far beyond furniture shoppers and justify premium "
         "pricing through experience — a format mass retailers cannot replicate."),
        ("Affluent-customer resilience. ",
         "The wealthy homeowner cohort spends through cycles better than mass-market "
         "furniture buyers, dampening the cyclicality the market prices in."),
        ("Founder-led capital allocation. ",
         "Aggressive buybacks during stock weakness have repeatedly shrunk the share count "
         "at prices rewarding long-term holders — a genuine edge in a levered equity."),
        ("The moat's weak link: leverage and key-person risk. ",
         "4.2× net debt/EBITDA with a 2028 maturity wall means the equity absorbs any "
         "operating disappointment first; the strategy and brand vision are closely tied to "
         "founder-CEO Gary Friedman."),
    ],
    "valuation_method": "10-year scenario FCFF DCF (leverage-priced discounts)",
    "valuation_intro": [
        "We value RH on a 10-year scenario DCF of free cash flow to the firm — weights bear "
        "25% / base 50% / bull 25% — with scenario-specific discounts priced for the "
        "leverage: base 12.0% (speculative tier: 4.2× net debt/EBITDA, $61 million book "
        "equity, $2.5 billion maturity in October 2028, beta 1.86, single-key-man brand), "
        "bear 14.5% (base + 250bp), bull 10.5% (base − 150bp). Terminal growth is 1.0% / "
        "2.5% / 2.5% on year-10 FCF at normalized mid-cycle margins (11.9% base — well below "
        "the 27%+ FY21 peak; never peak margins). Equity equals firm enterprise value minus "
        "$2.26 billion of net financial debt, over 18.93 million shares.",
        "Scenario fair values: bear ~$0 (housing frozen to 2028, tariffs lingering, gallery "
        "investments underwhelming — revenue CAGR under 3%, FCF margins compressing to 5.4%, "
        "firm EV of $2.0 billion against $2.26 billion of debt leaves the equity at roughly "
        "zero), base $190.73 (gallery and hospitality investments work, housing normalizes, "
        "revenue compounds 6.9% to ~$7.1 billion, margins recover to 20% EBITDA), bull "
        "$325.96 (international and hospitality inflect; operating leverage runs full). The "
        "probability-weighted fair value is our $177.00 target. The spread is wider than a "
        "typical retail note because the leverage demands it: this equity is a call option, "
        "priced as one.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 0.00,
            "assumptions": "Housing frozen to 2028; tariffs linger; gallery investments underwhelm; firm EV $2.0B vs $2.26B debt leaves equity at ~$0",
            "rev_cagr": "+2.5%", "margin_end": "5.4%",
            "discount": 0.145, "terminal_g": 0.01, "tv_share": 0.55,
            "pv_explicit": 0, "pv_terminal": 0, "cashflow_unit": "$mn",
        },
        "base": {
            "fair_value": 190.73,
            "assumptions": "Gallery and hospitality investments work; housing normalizes; revenue compounds 6.9% to ~$7.1B; EBITDA margins recover to 20%",
            "rev_cagr": "+6.9%", "margin_end": "11.9%",
            "discount": 0.12, "terminal_g": 0.025, "tv_share": 0.62,
            "pv_explicit": 1372, "pv_terminal": 2238, "cashflow_unit": "$mn",
        },
        "bull": {
            "fair_value": 325.96,
            "assumptions": "International and hospitality inflect; operating leverage runs full; luxury multiple re-rating as furniture-cycle correlation fades",
            "rev_cagr": "+9.5%", "margin_end": "11.4%",
            "discount": 0.105, "terminal_g": 0.025, "tv_share": 0.68,
            "pv_explicit": 1974, "pv_terminal": 4196, "cashflow_unit": "$mn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Scenario fair values are per-share equity values (firm EV less $2.26 bn net debt, 18.93 mn shares). 0.25×$0 + 0.50×$190.73 + 0.25×$325.96 ≈ $177.00.",
    "risks": [
        ("Housing cyclicality. ",
         "Furniture demand is tightly linked to home sales and mortgage rates; a prolonged "
         "housing downturn would keep revenue and margins depressed."),
        ("Gallery expansion execution. ",
         "New galleries are capital-intensive and take years to mature; underperformance "
         "would strand capital."),
        ("International expansion risk. ",
         "European luxury consumers and operating environments differ from the US; "
         "replication is not guaranteed."),
        ("Key-person risk. ",
         "The strategy and brand vision are closely associated with founder-CEO Gary "
         "Friedman."),
        ("Tariff and supply-chain exposure. ",
         "Global sourcing makes margins sensitive to trade policy and freight costs."),
        ("Luxury positioning fragility. ",
         "Quality, service, or design missteps could erode the pricing power the entire "
         "model depends on."),
    ],
    "falsification": (
        "Downgrade to HOLD on: same-gallery sales declining for six consecutive quarters "
        "despite housing stabilization — the demand thesis breaking; operating margins "
        "failing to expand as revenue recovers, indicating the fixed-cost leverage story was "
        "wrong and costs are variable after all; international galleries generating "
        "sustainably negative four-wall economics after a reasonable ramp period; a strategic "
        "pivot away from luxury positioning toward promotional or mass-market offerings; or "
        "share repurchases continuing while gallery returns deteriorate — capital allocation "
        "masking a broken operating model. We watch: same-gallery sales, housing turnover, "
        "European gallery four-wall margins, and the October 2028 refinancing."
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
        "independently tested and haircut where evidence warrants. For RH the discount rates "
        "are priced for the leverage — the speculative tier — because the equity is a levered "
        "claim on the firm's cash flows.",
    ],
    "charts": {
        "scenario": {"bear": 0.00, "base": 190.73, "bull": 325.96,
                     "weighted": 177.00, "price": 120.46},
        "trajectory": {
            "years_hist": [2023, 2024, 2025, 2026],
            "revenue_hist": [3.59, 3.029, 3.181, 3.44],
            "fcf_hist": [0.23, -0.067, -0.029, 0.249],
            "years_proj": [2027, 2028, 2029, 2030, 2031],
            "revenue_proj": [3.68, 3.93, 4.20, 4.49, 4.80],
            "fcf_proj": [0.35, 0.40, 0.46, 0.52, 0.59],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via Yahoo Finance — fiscal years ending "
                    "late January (FY2026 = year to Jan 2026); FCF = operating cash flow "
                    "less capex. Projections: base case — 6.9% revenue CAGR, FCF path "
                    "$350M → $848M by FY35.",
        },
        "composition": {
            "bear": {"pv_explicit": 0, "pv_terminal": 0},
            "base": {"pv_explicit": 1372, "pv_terminal": 2238},
            "bull": {"pv_explicit": 1974, "pv_terminal": 4196},
            "unit": "$mn",
        },
        "extra": {
            "type": "line",
            "title": "Base-case FCF path by scenario, FY26–FY35 ($mn)",
            "years": [2026, 2035],
            "series": [
                {"label": "Bear ($340M → $253M)", "values": [340, 253]},
                {"label": "Base ($350M → $848M)", "values": [350, 848]},
                {"label": "Bull ($372M → $1,029M)", "values": [372, 1029]},
            ],
            "ylabel": "$mn",
        },
    },
}

validate(data)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "RH-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
