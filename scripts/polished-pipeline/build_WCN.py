"""Polished note: WCN (Waste Connections) — SELL, FV $78.00, price $153.82 (Oct 2, 2026).

Sources: standalone PDF (valuation + prose). Scenario FVs from the standalone
valuation prose (bear: below $60; base: $78 at 25x normalized FCF; bull:
approaches $110), calibrated so 25/50/25 weights equal the $78.00 target.
History: yfinance annuals (FY2022–FY2025). Projection: base-case path implied
by this note's scenario model. Composition bars decompose each scenario's
equity value (FV x diluted shares + net debt) at the stated TV shares.
Risk rating assigned from substance: Medium (superb, non-cyclical business;
the risk is pure multiple compression, not operations).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

# Composition calibration: 251.6 mn diluted shares, net debt $9,538 mn.
# bear: 52 x 251.6 = 13,081 eq; EV 22,619; TV 55% -> 12,440 / 10,179
# base: 78 x 251.6 = 19,622 eq; EV 29,160; TV 65% -> 18,954 / 10,206
# bull: 104 x 251.6 = 26,163 eq; EV 35,701; TV 70% -> 24,991 / 10,710

data = {
    "ticker": "WCN",
    "company": "Waste Connections, Inc.",
    "exchange": "NYSE",
    "sector": "Industrials — Waste Management",
    "verdict": "SELL",
    "fair_value": 78.00,
    "price": 153.82,
    "risk": "Medium",
    "headline": "A Superb Business at an Impossible Multiple",
    "hq": "The Woodlands, Texas (domiciled in Ontario, Canada)",
    "snapshot": [
        ("Market cap", "~$39.0 bn (251.6 mn sh x $153.82)"),
        ("Net debt", "~$9.5 bn; modest for the sector"),
        ("52-week range", "~$146.89 - $179.74"),
        ("TTM revenue", "~$9.5 bn"),
        ("Price vs. FCF", "~40x free cash flow"),
        ("Adjusted EBITDA margin", "Low 30s — best in class"),
        ("Next catalyst", "Q4'26 pricing / acquisition update"),
    ],
    "thesis": [
        "Waste Connections is a superb business, and this is a valuation call, not a business-quality "
        "call. The company has spent two decades rolling up local solid-waste monopolies, pricing above "
        "inflation into captive commercial customers, and converting it all into prodigious free cash flow. "
        "It deserves a premium multiple. It does not deserve this multiple. At $153.82, the shares trade at "
        "roughly 40 times free cash flow — a price that demands a decade of flawless tuck-in acquisitions, "
        "uninterrupted above-inflation pricing, and zero regulatory friction. Our probability-weighted fair "
        "value is $78.00, implying 49% downside.",
        "Our core judgment is that the market is capitalizing peak conditions into perpetuity. Waste "
        "Connections' pricing power is real but not infinite: commercial customers eventually push back, "
        "municipal contracts re-bid, and the acquisition targets that built the empire are getting scarcer "
        "and pricier with every deal. The marginal acquisition multiple has crept up for years — recent deal "
        "multiples have drifted into the low teens from the historical 6-9x EBITDA — which means each "
        "incremental dollar of deployed capital earns a lower return. A roll-up works until the targets run "
        "out or get too expensive; we are closer to that point than the price admits.",
        "Consider the acquisition math directly. At 12-14x EBITDA paid, an acquisition must be flawless to "
        "earn its cost of capital — and the market capitalizes Waste Connections as though every future deal "
        "clears that bar. Roll-ups do not die dramatically; they fade into conglomerates trading at market "
        "multiples. We believe that fade has begun. Meanwhile the regulatory backdrop is quietly worsening: "
        "PFAS remediation obligations, methane-emission rules, and post-closure liabilities are real cash "
        "costs that the current multiple treats as footnotes.",
        "Note what our scenarios imply: even our bull case — which assumes the roll-up machine keeps "
        "humming, accretive deals and pricing surprise to the upside — sits nearly 30% below today's price. "
        "When the bull case is a loss, the price is wrong. Our 25x normalized free-cash-flow multiple in the "
        "base case is itself a premium — the broad market trades near 20x — and we grant it for moat "
        "quality and still arrive 49% below the price. We rate the shares SELL and would revisit only after "
        "a derating commensurate with a maturing roll-up.",
    ],
    "thesis_subhead": "The roll-up math is fading",
    "thesis_bullets": [
        ("Deal multiples paid have drifted into the low teens. ",
         "The remaining independent operators are smaller, more competitive to acquire, and increasingly "
         "aware of their scarcity value. Each incremental dollar of deployed capital earns a lower return — "
         "the roll-up's engine is running on thinner fuel."),
        ("Environmental capex is the underappreciated variable. ",
         "PFAS treatment at landfills and leachate systems, plus methane-capture investments, will absorb "
         "a growing share of operating cash flow over our forecast horizon. None of this impairs the moat, "
         "but it trims the growth rate at the margin — and at 40x free cash flow there is no margin for "
         "trimming."),
        ("Multiple compression needs no operational misstep. ",
         "A derating from ~40x to ~25x free cash flow can happen with the business executing flawlessly. "
         "That is the primary risk to the shares, and it is a 49% risk."),
    ],
    "business": [
        "Waste Connections, Inc., headquartered in The Woodlands, Texas (domiciled in Ontario, Canada), is "
        "the third-largest solid-waste company in North America, with roughly $9 billion in annual revenue. "
        "The strategy is deliberately contrarian: dominate secondary and exclusive markets where competition "
        "is thin, then vertically integrate collection into transfer stations and landfills. The company also "
        "operates a sizable exploration-and-production waste business (R360) serving oil and gas basins. "
        "Growth has come roughly half from pricing and half from acquisitions, with adjusted EBITDA margins "
        "in the low 30s — best in class among the public waste operators.",
        "The moat structure is genuinely exceptional: landfills are nearly impossible to permit in most "
        "jurisdictions, giving incumbents local monopolies with pricing power that has compounded for "
        "decades, and collection routes exhibit powerful density economics — each incremental stop on an "
        "existing route is nearly pure margin. This is why the business deserves a premium multiple in any "
        "rational framework. Our argument is purely about the price of that excellence.",
    ],
    "business_bullets": [
        ("The R360 energy-waste business adds hidden cyclicality. ",
         "Tying a portion of earnings to oilfield activity introduces a cyclicality the "
         "'recession-proof compounder' narrative ignores."),
        ("Municipal renewals are seeing more aggressive bidding. ",
         "Competitors are targeting Waste Connections' high margins at contract renewal — not fatal, but "
         "another trim to the growth rate at the margin."),
        ("Capital allocation is the swing factor. ",
         "As deal multiples rise, the hurdle for buybacks falls — but repurchasing shares at 40x free cash "
         "flow destroys value as surely as overpaying for deals. Our base case assumes acquisition "
         "discipline holds; the bear case assumes it doesn't."),
    ],
    "outlook": [
        "Our judgment is that Waste Connections keeps executing well operationally while the investment "
        "math deteriorates. Pricing should remain above inflation — the local-monopoly structure guarantees "
        "that — but the spread between price increases and cost inflation narrows as labor and regulatory "
        "costs accelerate. Acquisition-driven growth continues, but deal multiples paid stay elevated, "
        "compressing the return on each new tuck-in.",
        "A maturing compounder growing free cash flow per share at high-single digits cannot sustain a 40x "
        "multiple. Multiple compression, not business deterioration, is the risk — and it is the entire "
        "49% of downside in this note.",
    ],
    "financials": [
        "Revenue has compounded from $7.2 billion in FY2022 to $9.5 billion in FY2025, but free cash flow "
        "has barely moved — $1.11 billion to $1.22 billion — and the FCF margin has quietly eroded from "
        "15.4% to 12.9%. The business is growing its top line while converting less of it to cash, exactly "
        "what the maturing-roll-up thesis predicts: rising environmental capex and pricier deals absorbing "
        "the incremental dollar.",
        "Leverage is modest for the sector at ~$9.5 billion of net debt, and the balance sheet is not the "
        "problem. The problem is purely the price: ~40x free cash flow for high-single-digit FCF-per-share "
        "growth is a multiple that assumes the roll-up economics of 2015 persist indefinitely.",
    ],
    "fin_table": {
        "headers": ["$ bn", "FY2023", "FY2024", "FY2025"],
        "rows": [
            ["Revenue", "8.022", "8.920", "9.467"],
            ["Free cash flow", "1.193", "1.173", "1.220"],
            ["Net income", "0.763", "0.618", "1.077"],
        ],
        "footnote": "Source: company filings via yfinance; fiscal year ends Dec 31.",
    },
    "moat": [
        ("Landfills are the best local monopolies in American business. ",
         "Nearly impossible to permit in most jurisdictions; incumbents hold pricing power that has "
         "compounded for decades. This moat is real and durable."),
        ("Route density economics. ",
         "Collection routes exhibit powerful density: each incremental stop on an existing route is nearly "
         "pure margin, rewarding the disciplined tuck-in strategy."),
        ("Exclusive-market strategy. ",
         "Dominating secondary markets where competition is thin avoids the urban price wars that plague "
         "less disciplined operators."),
        ("Moats deserve 25x free cash flow, not 40x. ",
         "We grant a full premium multiple for moat quality in the base case — and still arrive 49% below "
         "the price. The moat is not in question; the price of admission is."),
    ],
    "valuation_method": "10-year scenario DCF",
    "valuation_intro": [
        "We value Waste Connections on a probability-weighted scenario DCF using a 9% base discount rate, "
        "reflecting the stability of the franchise (bear +250bp at 11.5%, bull floored at 8.0%), with an "
        "explicit country-risk assessment for the Canadian domicile (immaterial at these weights). Terminal "
        "growth is 1.5% / 2.0% / 2.5% on normalized cash flows.",
        "In the bear case, acquisition multiples paid stay high while pricing power fades, free-cash-flow "
        "growth slows to 3%, and the multiple compresses toward 20x — implying value below $60. In the "
        "base case, the company compounds free cash flow per share at roughly 7%, margins hold in the low "
        "30s, and a 25x multiple on normalized free cash flow — still a full premium to the market — "
        "supports our $78.00 target. In the bull case, accretive deals and pricing surprise to the upside "
        "and value approaches $110.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 52.00,
            "assumptions": "Acquisition multiples paid stay high while pricing power fades; FCF growth "
                           "slows to 3%; multiple compresses toward 20x",
            "rev_cagr": "+3%", "margin_end": "29%",
            "discount": 0.115, "terminal_g": 0.015, "tv_share": 0.55,
            "pv_explicit": 10179, "pv_terminal": 12440, "cashflow_unit": "$mn",
        },
        "base": {
            "fair_value": 78.00,
            "assumptions": "FCF per share compounds ~7%; EBITDA margins hold in the low 30s; 25x "
                           "normalized FCF multiple — a full premium to the market",
            "rev_cagr": "+6%", "margin_end": "32%",
            "discount": 0.09, "terminal_g": 0.02, "tv_share": 0.65,
            "pv_explicit": 10206, "pv_terminal": 18954, "cashflow_unit": "$mn",
        },
        "bull": {
            "fair_value": 104.00,
            "assumptions": "Accretive deals and pricing surprise to the upside; roll-up math holds "
                           "longer than we expect",
            "rev_cagr": "+9%", "margin_end": "34%",
            "discount": 0.08, "terminal_g": 0.025, "tv_share": 0.70,
            "pv_explicit": 10710, "pv_terminal": 24991, "cashflow_unit": "$mn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Scenario FVs calibrated from the note's valuation ranges (bear: below $60; base: "
                     "$78; bull: approaches $110); 0.25x$52 + 0.50x$78 + 0.25x$104 = $78.00. "
                     "Composition bars decompose each scenario's equity value (FV x 251.6 mn diluted shares, "
                     "plus $9.5 bn net debt) at the stated terminal-value shares.",
    "risks": [
        ("Multiple compression is the primary risk. ",
         "A derating from ~40x to ~25x free cash flow needs no operational misstep at all."),
        ("Acquisition indigestion or overpayment. ",
         "Quality targets are becoming scarcer and pricier; overpaying would impair the roll-up math "
         "directly."),
        ("Environmental regulation. ",
         "PFAS, methane, and other rules raising capex and post-closure liabilities beyond our provisions."),
        ("Commercial-volume recession. ",
         "Would hit the highest-margin collection revenue first."),
        ("Leverage. ",
         "Modest for the sector, but limits flexibility if credit conditions tighten."),
    ],
    "falsification": (
        "Upgrade on evidence that acquisition multiples paid are falling while returns on new deals stay "
        "above 15% — the roll-up math working again; sustained double-digit free-cash-flow-per-share growth "
        "for several years, validating the current multiple; or regulatory clarity on PFAS with costs coming "
        "in well below our provisions. A derating of the shares toward our $78 fair value would restore a "
        "reasonable risk/reward."
    ),
    "charts": {
        "scenario": {"bear": 52.00, "base": 78.00, "bull": 104.00,
                     "weighted": 78.00, "price": 153.82},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [7.212, 8.022, 8.920, 9.467],
            "fcf_hist": [1.110, 1.193, 1.173, 1.220],
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": [10.2, 11.0, 11.8, 12.6, 13.5, 14.4, 15.4, 16.4, 17.5, 18.6, 19.8],
            "fcf_proj": [1.35, 1.48, 1.62, 1.77, 1.93, 2.10, 2.29, 2.49, 2.71, 2.95, 3.21],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via yfinance (FY ends Dec 31). Projection: base-case path "
                    "from this note's scenario model — FCF per share compounds ~7%, margins hold in the "
                    "low 30s.",
        },
        "composition": {
            "bear": {"pv_explicit": 10179, "pv_terminal": 12440},
            "base": {"pv_explicit": 10206, "pv_terminal": 18954},
            "bull": {"pv_explicit": 10710, "pv_terminal": 24991},
            "unit": "$mn",
        },
        "extra": {
            "type": "line",
            "title": "FCF margin — the quiet erosion the 40x multiple ignores (%)",
            "years": [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "series": [
                {"label": "FCF margin — actual",
                 "values": [15.4, 14.9, 13.1, 12.9, None, None, None, None, None, None, None, None, None, None, None]},
                {"label": "FCF margin — base-case projection",
                 "values": [None, None, None, None, 13.2, 13.5, 13.7, 14.0, 14.3, 14.6, 14.8, 15.1, 15.5, 15.9, 16.2]},
            ],
            "ylabel": "%",
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "WCN-equity-research-note-polished.pdf")
build_note(data, out)
print("built:", out)
