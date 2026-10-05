"""Polished note build: Sea Limited (SE) — BUY, $149.00 target."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note, validate

data = {
    "ticker": "SE",
    "company": "Sea Limited",
    "exchange": "NYSE",
    "sector": "Technology — E-commerce, Gaming & Digital Financial Services",
    "verdict": "BUY",
    "fair_value": 149.00,
    "price": 95.19,
    "risk": "High",
    "headline": "Three Engines, One Flywheel — Priced as Though It Never Compounds",
    "ceo": "Forrest Li",
    "hq": "Singapore",
    "snapshot": [
        ("Market cap", "~$58.3 bn (~570 mn sh × $95.19)"),
        ("Price (Oct 2, 2026)", "$95.19"),
        ("52-week range", "~$77.05 – $193.48"),
        ("2025 revenue / growth", "~$22.9 bn (+36% YoY)"),
        ("2025 operating cash flow", "~$5.0 bn (vs −$1.1 bn in 2022)"),
        ("Segments", "Shopee (e-commerce) · Garena (gaming) · SeaMoney (fintech)"),
        ("Shopee take rate", "Well below global e-commerce peers — years of headroom"),
        ("Country-risk premium", "150bp charged on every scenario"),
        ("Next catalyst", "Q3 2026 earnings; SeaMoney loan-book and loss-rate disclosure"),
    ],
    "thesis": [
        "Sea Limited runs three businesses that each look mediocre in isolation and formidable "
        "in combination: Garena, the game publisher behind Free Fire; Shopee, the e-commerce "
        "marketplace leader across Southeast Asia, Taiwan, and Brazil; and SeaMoney, the "
        "digital financial services arm built on the transaction data of the other two. The "
        "market's enduring mistake with Sea is analyzing each segment against its worst "
        "comparable — Garena against aging game studios, Shopee against cash-burning "
        "marketplaces, SeaMoney against risky lenders — instead of pricing the flywheel. At "
        "$95.19 the shares embed the assumption that the flywheel never compounds; our work "
        "suggests it already is.",
        "Start with what changed: Sea is profitable now. The era of subsidized growth ended "
        "several years ago, and Shopee has demonstrated it can take share and make money at "
        "the same time, with logistics infrastructure — its own last-mile network across the "
        "region — as the moat that lets it do both. Take rates still sit well below global "
        "e-commerce peers, which means the monetization runway is measured in years, not "
        "quarters. Every point of take-rate expansion on Shopee's gross merchandise volume "
        "drops disproportionately to operating profit because the fulfillment network is "
        "already built.",
        "Garena, written off repeatedly since the post-pandemic gaming normalization, keeps "
        "generating the cash that funds everything else. Free Fire remains one of the "
        "most-played mobile games on earth, with particular strength in the emerging markets "
        "where Sea operates — the same markets where smartphone penetration and disposable "
        "income are still rising. The market treats Garena as a wasting asset; we treat it as a "
        "durable cash engine with new-title optionality that comes free with the shares.",
        "SeaMoney is the least understood and potentially the most valuable leg. Built on "
        "Shopee's transaction and logistics data, its lending products underwrite borrowers "
        "that traditional banks cannot see, and its payments products deepen the ecosystem "
        "lock-in. Fintech attached to commerce data has been the highest-return business model "
        "in emerging markets globally, and SeaMoney is still early in that journey. Our "
        "$149.00 fair value prices Shopee as a maturing regional champion with take-rate "
        "headroom, Garena as a durable cash cow, and SeaMoney as a fast-growing fintech — and "
        "charges a 150bp Southeast Asia country-risk premium for the privilege. The bear case "
        "at $75, below today's price, is the world where competition breaks all three engines "
        "at once; we consider that the tail, not the center. The rating is BUY.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("Take-rate expansion is the profit inflection. ",
         "Volume growth plus monetization expansion on an already-built logistics base is the "
         "classic e-commerce profit inflection — and Sea is in its early stages, with take rates "
         "grinding upward toward levels global peers sustain."),
        ("SeaMoney's underwriting is the data edge. ",
         "Lending decisions informed by real commerce and logistics behavior — not "
         "self-reported income — have produced loss rates the skeptics did not expect. If that "
         "continues, SeaMoney graduates from sidecar to core earnings driver and gets "
         "re-rated as a fintech."),
        ("The diversification is the downside protection. ",
         "Three engines across gaming, commerce, and fintech mean no single competitive or "
         "regulatory shock breaks the company — the bear case requires all three to misfire "
         "simultaneously, which is why we treat it as a tail."),
    ],
    "business": [
        "Sea Limited, headquartered in Singapore, operates three segments. Shopee is the "
        "leading e-commerce marketplace across Southeast Asia, Taiwan, and Brazil, with its own "
        "last-mile logistics network in core markets. Garena is the digital-entertainment arm, "
        "publisher of Free Fire — one of the most-played mobile games globally — plus a "
        "publishing pipeline for new titles. SeaMoney provides digital financial services: "
        "consumer and SME lending, mobile wallet payments, and related products, built on the "
        "transaction and logistics data generated by the other two segments.",
        "The flywheel logic: Garena's cash funded Shopee's land grab; Shopee's transaction "
        "volume feeds SeaMoney's underwriting data; SeaMoney's payments deepen lock-in across "
        "the ecosystem. The company reports in US dollars while operating across many emerging "
        "currencies, which adds translation volatility but also diversifies the economic base.",
        "The business model has matured from growth-at-all-costs to profitable compounding. "
        "Revenue was $22.9 billion in 2025, up 36% year over year, and operating cash flow "
        "inflected from negative $1.1 billion in 2022 to positive $5.0 billion in 2025. Shopee "
        "monetizes through take rates on gross merchandise volume that remain well below "
        "global peers; Garena monetizes through in-game purchases on a largely fixed cost "
        "base; SeaMoney monetizes through net interest and fee income on a growing loan book.",
    ],
    "outlook": [
        "Our judgment is that Shopee's next phase will be defined by monetization, not "
        "market-share warfare. The destructive subsidy battles of the past are over — every "
        "major regional player has learned that lesson — and Shopee's logistics moat means it "
        "can raise take rates gradually without losing sellers or buyers. We expect gross "
        "merchandise volume to keep growing at a healthy double-digit pace on the back of "
        "rising e-commerce penetration in Southeast Asia, while take rates grind upward. That "
        "combination — volume growth plus monetization expansion on a fixed logistics base — "
        "is the classic e-commerce profit inflection, and we believe Sea is in its early stages.",
        "For Garena, our view is deliberately unglamorous: Free Fire does not need to grow for "
        "the thesis to work; it needs to endure. Mobile gaming in emerging markets is supported "
        "by demographics — young populations, rising smartphone adoption, increasing spending "
        "power — and Free Fire's low device requirements make it the default game for exactly "
        "those users. New titles are genuine upside: Garena's publishing infrastructure means "
        "any hit scales quickly, but we underwrite the segment as a cash cow and treat hits as "
        "free options.",
        "SeaMoney is where our forward view is most optimistic and the market's is most "
        "skeptical. The bearish concern is credit quality — lending to thin-file borrowers in "
        "volatile economies. Our read of the data is that SeaMoney's underwriting, informed by "
        "real commerce and logistics behavior rather than self-reported income, has produced "
        "loss rates the skeptics did not expect, and the loan book keeps growing. If that "
        "continues, SeaMoney graduates over the next several years from sidecar to core "
        "earnings driver, and the market will be forced to value it as a fintech rather than "
        "as a cost center. That re-rating is a meaningful part of our bull case.",
    ],
    "financials": [
        "The financial transformation is the underappreciated story. Revenue compounded from "
        "$12.5 billion in 2022 to $22.9 billion in 2025 while the business flipped from cash "
        "burn to cash generation: operating cash flow went from negative $1.1 billion in 2022 "
        "to positive $5.0 billion in 2025, and free cash flow reached $4.5 billion. That is a "
        "$6 billion swing in operating cash flow in three years — the subsidy era is "
        "definitively over.",
        "The balance sheet funds the flywheel internally: Garena's cash generation means "
        "Shopee's logistics build and SeaMoney's loan-book growth do not depend on external "
        "capital. At $95.19 the shares trade at about 37× trailing earnings — optically full — "
        "but trailing earnings understate a business whose three segments are all still "
        "climbing their margin curves. Our DCF values the cash flows, not the multiple, and "
        "charges the 150bp country-risk premium on every scenario.",
    ],
    "fin_table": {
        "headers": ["$ bn", "2022", "2023", "2024", "2025"],
        "rows": [
            ["Total revenue", "12.45", "13.06", "16.82", "22.94"],
            ["YoY growth", "—", "+4.9%", "+28.7%", "+36.4%"],
            ["Operating cash flow", "−1.06", "2.08", "3.28", "5.03"],
            ["Free cash flow", "−2.03", "1.82", "2.96", "4.50"],
        ],
        "footnote": "Sources: company filings via Yahoo Finance (annual). FCF = operating cash flow less capex.",
    },
    "moat": [
        ("Shopee's logistics network is the moat. ",
         "Its own last-mile infrastructure across Southeast Asia lets Shopee take share and "
         "make money simultaneously — and raise take rates without losing sellers or buyers. "
         "Logistics is the hardest e-commerce asset to replicate in the region."),
        ("The flywheel across three segments. ",
         "Garena cash funds commerce; commerce data underwrites fintech; fintech payments "
         "deepen ecosystem lock-in. Each leg analyzed alone looks mediocre; combined, they "
         "compound."),
        ("Commerce-data underwriting. ",
         "SeaMoney lends against real transaction and logistics behavior, not self-reported "
         "income — a data edge traditional banks in these markets cannot see and fintech "
         "rivals cannot easily copy."),
        ("Free Fire's installed base. ",
         "One of the most-played mobile games on earth, with low device requirements "
         "perfectly matched to emerging-market demographics — a durable cash engine with "
         "free new-title optionality."),
        ("The moat's weak link: each engine has a predator. ",
         "TikTok Shop and Lazada in commerce, engagement decay in gaming, credit cycles in "
         "fintech — the diversification mitigates any single threat, but a synchronized "
         "regional shock would test all three at once."),
    ],
    "valuation_method": "10-year scenario FCF DCF with Southeast Asia country-risk premium",
    "valuation_intro": [
        "We value Sea on a 10-year probability-weighted scenario DCF of free cash flow — "
        "weights bear 25% / base 50% / bull 25% — with an explicit 150bp Southeast Asia "
        "country-risk premium added to the discount rate on every scenario: bear 14.5%, base "
        "12.0%, bull 10.5%. Terminal growth is 1.75% / 2.5% / 2.5% on normalized mid-cycle "
        "margins — we do not project peak e-commerce or gaming margins into perpetuity — and "
        "we benchmark multiples against regional e-commerce, gaming, and fintech peers facing "
        "similar emerging-market risks, never US peers alone. The terminal value is a minority "
        "of enterprise value, consistent with a business whose near-term cash generation is "
        "substantial and visible.",
        "Scenario-implied fair values: bear $75 (e-commerce price war resumes with TikTok "
        "Shop and Lazada; Free Fire declines steeply; SeaMoney credit losses spike; regional "
        "macro shock), base $141 (Shopee GMV grows double-digits with take-rate expansion; "
        "Garena cash flows endure; SeaMoney scales profitably; margins widen on logistics "
        "leverage), bull $256 (take rates normalize toward global peers; SeaMoney becomes a "
        "core fintech earnings engine; new Garena hit; market re-rates the flywheel). The "
        "probability-weighted fair value supports our $149.00 target — set conservatively "
        "inside the scenario range given the country-risk premium. The bear case at $75 sits "
        "below the current $95.19 price, as required: it is the world where all three engines "
        "misfire simultaneously, which we view as a genuine tail given the diversification "
        "across segments and geographies.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 75.00,
            "assumptions": "E-commerce price war resumes (TikTok Shop, Lazada); Free Fire declines steeply; SeaMoney credit losses spike; regional macro shock",
            "rev_cagr": "+5.0%", "margin_end": "17%",
            "discount": 0.145, "terminal_g": 0.0175, "tv_share": 0.342,
            "pv_explicit": 28157, "pv_terminal": 14593, "cashflow_unit": "$mn",
        },
        "base": {
            "fair_value": 141.00,
            "assumptions": "Shopee GMV grows double-digits with take-rate expansion; Garena cash flows endure; SeaMoney scales profitably; margins widen on logistics leverage",
            "rev_cagr": "+11.2%", "margin_end": "20%",
            "discount": 0.12, "terminal_g": 0.025, "tv_share": 0.491,
            "pv_explicit": 40908, "pv_terminal": 39462, "cashflow_unit": "$mn",
        },
        "bull": {
            "fair_value": 256.00,
            "assumptions": "Take rates normalize toward global peers; SeaMoney becomes a core fintech earnings engine; new Garena hit; market re-rates the flywheel",
            "rev_cagr": "+16.4%", "margin_end": "22%",
            "discount": 0.105, "terminal_g": 0.025, "tv_share": 0.59,
            "pv_explicit": 59827, "pv_terminal": 86093, "cashflow_unit": "$mn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Scenario fair values are per-share equity values from the FCF DCF (~570 mn shares), with the 150bp country-risk premium charged throughout. The $149.00 target is set conservatively inside the probability-weighted range.",
    "risks": [
        ("E-commerce competition. ",
         "TikTok Shop, Lazada (Alibaba), and local players could reignite subsidy wars or "
         "take share in key markets."),
        ("Gaming concentration. ",
         "Free Fire is a large share of Garena's profit; a sharp decline in engagement would "
         "reduce the cash engine funding the other segments."),
        ("SeaMoney credit risk. ",
         "Rapid loan-book growth among thin-file borrowers could produce unexpected losses "
         "in an economic downturn."),
        ("Regulatory and political risk. ",
         "Across Southeast Asia, Taiwan, and Latin America — including data, fintech "
         "licensing, and foreign-ownership rules."),
        ("Currency volatility. ",
         "Results are reported in US dollars while operations span many emerging-market "
         "currencies."),
    ],
    "falsification": (
        "Downgrade to HOLD on: Shopee losing market leadership in two or more core markets "
        "(Indonesia, Vietnam, Thailand) on both volume and profitability — the moat thesis "
        "breaking; take-rate expansion reversing for four consecutive quarters, indicating "
        "pricing power was illusory; SeaMoney non-performing loan ratios inflecting sharply "
        "upward with inadequate provisioning; Free Fire quarterly paying users declining more "
        "than 20% year over year with no pipeline title offsetting; or a regulatory event that "
        "structurally impairs one of the three segments (e.g., fintech license revocation in a "
        "major market). We watch: Shopee market share and take rate, SeaMoney NPL ratios, "
        "Free Fire engagement, and regional regulatory headlines."
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
        "independently tested and haircut where evidence warrants. For Sea we add an explicit "
        "150bp Southeast Asia country-risk premium to the discount rate and benchmark "
        "multiples against regional peers facing similar emerging-market risks.",
    ],
    "charts": {
        "scenario": {"bear": 75.00, "base": 141.00, "bull": 256.00,
                     "weighted": 149.00, "price": 95.19},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [12.45, 13.064, 16.82, 22.938],
            "fcf_hist": [-2.032, 1.822, 2.955, 4.501],
            "years_proj": [2026, 2027, 2028, 2029, 2030],
            "revenue_proj": [25.5, 28.4, 31.5, 35.1, 39.0],
            "fcf_proj": [4.70, 5.40, 6.20, 7.10, 8.05],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via Yahoo Finance (FCF = operating cash flow "
                    "less capex). Projections: base-case free cash flow from the scenario "
                    "DCF (~11% revenue CAGR, FCF margins widening on logistics leverage).",
        },
        "composition": {
            "bear": {"pv_explicit": 28157, "pv_terminal": 14593},
            "base": {"pv_explicit": 40908, "pv_terminal": 39462},
            "bull": {"pv_explicit": 59827, "pv_terminal": 86093},
            "unit": "$mn",
        },
        "extra": {
            "type": "line",
            "title": "2036 revenue by scenario — the monetization runway ($bn)",
            "years": [2026, 2036],
            "series": [
                {"label": "Bear", "values": [25.5, 51.2]},
                {"label": "Base", "values": [25.5, 91.2]},
                {"label": "Bull", "values": [25.5, 143.8]},
            ],
            "ylabel": "$bn",
        },
    },
}

validate(data)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "SE-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
