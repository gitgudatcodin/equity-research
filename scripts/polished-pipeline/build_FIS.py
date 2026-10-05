"""Polished note build: Fidelity National Information Services (FIS). Re-runnable."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

data = {
    "ticker": "FIS",
    "company": "Fidelity National Information Services, Inc.",
    "exchange": "NYSE",
    "sector": "Technology — Financial Technology Infrastructure",
    "verdict": "BUY",
    "fair_value": 45.00,
    "price": 32.44,
    "risk": "Medium",
    "headline": "A Misunderstood Core-Banking Franchise Midway Through Margin Repair",
    "snapshot": [
        ("Market cap", "~$16.7 bn (516 mn sh × $32.44)"),
        ("52-week range", "~$32.10 – $69.14"),
        ("Segments", "Banking Solutions; Capital Market Solutions"),
        ("Revenue character", "Heavy recurring, contract-based"),
        ("Contract tenor", "Core processing 5–7 years with termination fees"),
        ("Leverage", "Deleveraging steadily since the separation"),
        ("Capital return", "Buybacks + growing dividend"),
        ("Product cycle", "Real-time payments, digital banking, fraud/risk modules"),
        ("Next catalyst", "Continued margin expansion + capital returns"),
        ("Implied upside", "+39% to $45.00 fair value"),
    ],
    "thesis": [
        "FIS is a misunderstood asset. The market still treats it as the company that struggled through "
        "the Worldpay separation and the merchant-acquiring hangover; the reality in 2026 is a pure-play "
        "banking and capital-markets technology provider with recurring revenue, high switching costs, "
        "and margins that have been climbing quarter after quarter. The divestiture noise is gone. What "
        "remains is a core banking technology franchise that banks renew because they cannot easily "
        "leave.",
        "Our judgment: the earnings trajectory from here is driven less by revenue acceleration than by "
        "the margin repair that is already underway. FIS's cost program and the mix shift toward "
        "higher-margin banking solutions create operating leverage that the market is discounting because "
        "it remembers the old story. We stress the margin targets against actual quarterly delivery, and "
        "the trajectory has been consistent enough to underwrite a base case with further expansion.",
        "At $32.44, the valuation prices FIS like a low-growth legacy processor. Our probability-weighted "
        "fair value is $45.00, a 39% expected return, earned mostly through margin normalization and "
        "steady recurring revenue growth rather than a multiple re-rating to growth-tech levels. The "
        "bear case — bank IT budget cuts and stalled margin programs — is genuinely adverse and sits "
        "well below today's price.",
        "The balance-sheet repair deserves emphasis. Deleveraging since the separation has been steady, "
        "and the interest burden that once consumed a meaningful share of operating income is declining. "
        "That matters for equity holders twice: lower risk in the bear case and more free cash flow "
        "available for buybacks in the base case. We modeled the debt paydown schedule against stated "
        "targets and found it credible given current cash generation.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("Margin repair is already in the numbers, not in the price. ",
         "The cost structure inherited from the conglomerate years had real fat; ongoing efficiency "
         "programs have been converting it into operating leverage. We expect two phases: the current "
         "cost takeout, largely in hand, and a second phase of mix-driven expansion as higher-margin "
         "software and payments modules outgrow legacy processing. The base case assumes only partial "
         "realization of phase two."),
        ("A quiet product cycle. ",
         "Real-time payments adoption in the US is still early, and FIS's existing bank relationships "
         "make it a natural infrastructure provider. Digital banking, fraud and risk tools, and treasury "
         "modules sold into the installed base carry incremental margins well above the corporate "
         "average — the mechanical source of the expansion we underwrite."),
        ("Capital allocation as a second engine. ",
         "With the separation complete and leverage reduced, free cash flow conversion should support "
         "consistent buybacks and a growing dividend, adding a shareholder-return kicker to the "
         "earnings story."),
    ],
    "business": [
        "FIS provides technology solutions to financial institutions and businesses worldwide. Its core "
        "segments are Banking Solutions (core processing, digital banking, payments, and risk tools for "
        "banks and credit unions) and Capital Market Solutions (trading, treasury, and risk technology "
        "for buy- and sell-side institutions). The company completed the separation of its merchant "
        "solutions business (Worldpay), leaving a more focused, higher-margin software and processing "
        "business with a heavy weight of recurring, contract-based revenue.",
        "The economics are those of an embedded infrastructure provider: multi-year contracts, "
        "mission-critical software that is expensive to rip out, and incremental margins on additional "
        "modules sold into the installed base. Banks do not switch core processors casually, which gives "
        "FIS pricing power and revenue visibility well beyond a typical technology cycle.",
        "Capital Market Solutions serves a different but equally sticky customer: trading desks, asset "
        "managers, and corporate treasuries running FIS software for order management, risk, and "
        "post-trade processing. This segment is more sensitive to market activity levels but carries high "
        "margins and long relationships.",
    ],
    "business_bullets": [
        ("Contract structure is the moat's legal form. ",
         "Core processing agreements typically run five to seven years with termination fees that make "
         "switching economically punitive — on top of operational stickiness, since the core processor "
         "touches payments, compliance, reporting, and customer channels."),
        ("The installed base is the distribution channel. ",
         "New modules (real-time payments, digital banking, fraud tools) sell into thousands of existing "
         "bank relationships at incremental margins well above the corporate average."),
        ("Post-separation focus. ",
         "With Worldpay gone, management attention and capital are concentrated on the banking and "
         "capital-markets franchises rather than a conglomerate portfolio."),
    ],
    "outlook": [
        "Where is this business going? We see FIS as a slow-compounding infrastructure franchise entering "
        "a multi-year margin expansion phase. We expect revenue growth in the mid-single digits, driven "
        "by banks outsourcing more of their technology stacks and adopting real-time payments and "
        "digital modules, with margins expanding faster than revenue as the fixed cost base is leveraged.",
        "The second driver is capital allocation. With leverage reduced, free cash flow conversion should "
        "support consistent buybacks and a growing dividend. We do not assume heroic buybacks in the "
        "base case; we assume the stated capital-return framework is executed as it has been recently.",
        "The structural question is whether banks keep consolidating and insourcing. We judge the net "
        "trend as favorable: mid-tier banks — FIS's bread and butter — increasingly buy rather than build "
        "technology. Our bear case assumes that thesis stalls, bank IT budgets compress in a downturn, "
        "and margin gains reverse.",
        "M&A optionality is a watch item rather than a thesis driver. FIS has a history of large deals, "
        "and the market will likely penalize any return to empire-building. Our valuation assumes "
        "tuck-in acquisitions only; a large dilutive deal would be a reason to revisit the call.",
    ],
    "financials": [
        "Revenue has grown steadily from $9.72 billion in 2022 to $10.68 billion on a trailing basis in "
        "2025 — modest top-line growth, exactly as a mature infrastructure franchise should show. The "
        "story is in the margins and the balance sheet: the cost programs are expanding operating "
        "leverage while deleveraging since the separation reduces the interest burden each year.",
        "Free cash flow has been lumpy through the separation years ($0.63 billion in 2022, $3.56 billion "
        "in 2023, $1.25 billion in 2024, $1.83 billion trailing in 2025), reflecting restructuring and "
        "divestiture effects. The base case assumes conversion normalizes as one-time items fade, "
        "funding the buyback and dividend framework.",
    ],
    "fin_table": {
        "headers": ["$ bn", "2022", "2023", "2024", "2025 (TTM)"],
        "rows": [
            ["Total revenue", "9.72", "9.83", "10.13", "10.68"],
            ["Free cash flow", "0.63", "3.56", "1.25", "1.83"],
        ],
        "footnote": "Sources: company filings via Yahoo Finance. 2025 = trailing twelve months; FCF lumpy on separation effects.",
    },
    "moat": [
        ("Switching costs are the moat. ",
         "Core processing contracts run five to seven years with punitive termination fees, and "
         "replacing a core processor is a multi-year project no bank undertakes lightly."),
        ("Operational embeddedness. ",
         "The core processor touches payments, compliance, reporting, and customer channels — "
         "dislodging it means rewiring the bank."),
        ("Installed-base distribution. ",
         "Thousands of existing bank relationships give new modules a ready-made, high-incremental-"
         "margin channel that de-novo competitors cannot replicate."),
        ("Capital-markets stickiness. ",
         "Trading, treasury, and post-trade systems are deeply embedded in client workflows with long "
         "relationships and high margins."),
    ],
    "valuation_method": "10-year scenario DCF",
    "valuation_intro": [
        "We value FIS on a 10-year scenario DCF — weights bear 25% / base 50% / bull 25% — with "
        "scenario-specific discounts: bear 12.5% (base + 250bp), base 10.0% (standard tier for a "
        "stable, contract-heavy business with some cyclical exposure to bank IT spending), bull 8.5% "
        "(base − 150bp). Terminal growth is 1.5% / 2.0% / 2.0% on year-10 cash flows at normalized "
        "mid-cycle margins — never peak margins.",
        "Key sensitivities: a one-point change in the organic growth rate moves fair value by roughly a "
        "tenth, while a 100bp change in the terminal margin assumption moves it by a similar order. "
        "We consider 10% the appropriate base discount and test the conclusion at higher rates in the "
        "bear case.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 24.00,
            "assumptions": "Bank IT budget cuts in a downturn; margin programs stall and partially reverse; multiple compression on the legacy-processor narrative",
            "rev_cagr": "+2%", "margin_end": "36%",
            "discount": 0.125, "terminal_g": 0.015, "tv_share": 0.50,
            "pv_explicit": 12.0, "pv_terminal": 12.0, "cashflow_unit": "$/sh",
        },
        "base": {
            "fair_value": 44.00,
            "assumptions": "Mid-single-digit organic growth; continued margin expansion from cost programs and mix; stated capital-return framework executed",
            "rev_cagr": "+5%", "margin_end": "42%",
            "discount": 0.10, "terminal_g": 0.02, "tv_share": 0.58,
            "pv_explicit": 18.5, "pv_terminal": 25.5, "cashflow_unit": "$/sh",
        },
        "bull": {
            "fair_value": 68.00,
            "assumptions": "Faster bank outsourcing and real-time-payments adoption; full margin realization; stronger buybacks at the compressed multiple",
            "rev_cagr": "+8%", "margin_end": "46%",
            "discount": 0.085, "terminal_g": 0.02, "tv_share": 0.63,
            "pv_explicit": 25.0, "pv_terminal": 43.0, "cashflow_unit": "$/sh",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "risks": [
        ("Bank consolidation. ",
         "Mergers among client banks can reduce the customer base or trigger contract "
         "renegotiations."),
        ("Cyclicality of bank IT budgets. ",
         "A banking downturn would slow new sales and module adoption."),
        ("Execution on margin programs. ",
         "The expansion story requires continued cost discipline; slippage would compress the "
         "expected return."),
        ("Competition. ",
         "Cloud-native core providers and large IT services firms compete for the same bank wallets."),
        ("Regulatory. ",
         "Changes in payments regulation or data rules could raise compliance costs or alter pricing "
         "power."),
        ("Large-deal risk. ",
         "A return to transformative M&A could destroy shareholder value and re-lever the balance "
         "sheet."),
    ],
    "falsification": (
        "Downgrade to HOLD if organic revenue growth turns negative for two consecutive quarters "
        "(demand deterioration beyond cycle noise), or if adjusted EBITDA margin declines year over "
        "year despite the cost programs (breaking the margin-repair thesis). Client retention falling "
        "materially below historical levels, or free cash flow conversion deteriorating structurally, "
        "would each independently force a re-underwrite."
    ),
    "charts": {
        "scenario": {"bear": 24.00, "base": 44.00, "bull": 68.00,
                     "weighted": 45.00, "price": 32.44},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [9.72, 9.831, 10.127, 10.677],
            "fcf_hist": [0.626, 3.555, 1.254, 1.827],
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": [11.0, 11.55, 12.13, 12.73, 13.37, 14.04, 14.74, 15.48, 16.25, 17.06, 17.92],
            "fcf_proj": [1.98, 2.19, 2.43, 2.68, 2.95, 3.24, 3.55, 3.87, 4.22, 4.58, 5.02],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via Yahoo Finance (2025 = TTM; FCF lumpy on "
                    "separation effects). Projection: illustrative base-case path at ~5% revenue "
                    "CAGR with FCF margins expanding toward the high-20s.",
        },
        "composition": {
            "bear": {"pv_explicit": 12.0, "pv_terminal": 12.0},
            "base": {"pv_explicit": 18.5, "pv_terminal": 25.5},
            "bull": {"pv_explicit": 25.0, "pv_terminal": 43.0},
            "unit": "$/sh",
        },
        "extra": {
            "type": "line",
            "title": "Revenue — reported history vs. base-case path ($bn)",
            "years": [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "series": [
                {"label": "Reported", "values": [9.72, 9.831, 10.127, 10.677, None, None, None, None, None, None, None, None, None, None, None]},
                {"label": "Base case", "values": [None, None, None, None, 11.0, 11.55, 12.13, 12.73, 13.37, 14.04, 14.74, 15.48, 16.25, 17.06, 17.92]},
            ],
            "ylabel": "$bn",
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "FIS-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
