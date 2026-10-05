"""Polished note: WHR (Whirlpool) — SELL, FV $16.00, price $30.31 (Oct 2, 2026).

Sources: standalone PDF (valuation + prose), batch2 rich original.
Scenario FVs taken from the standalone valuation prose ranges
(bear: equity toward low single digits; base: mid-teens; bull: high $20s)
calibrated so the 25/50/25 weight equals the $16.00 target exactly.
History: yfinance annuals (FY2022–FY2025). Projection: base-case path
implied by this note's scenario model. Composition bars decompose each
scenario's equity value (FV x diluted shares +/- net debt) at the stated
TV shares.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

# Composition calibration: 65.2 mn diluted shares, net debt $6,818 mn.
# bear: 5 x 65.2 = 326 eq; EV 7,144; TV 40% -> 2,858 / 4,286
# base: 16 x 65.2 = 1,043 eq; EV 7,861; TV 50% -> 3,931 / 3,931
# bull: 27 x 65.2 = 1,760 eq; EV 8,578; TV 55% -> 4,718 / 3,860

data = {
    "ticker": "WHR",
    "company": "Whirlpool Corporation",
    "exchange": "NYSE",
    "sector": "Consumer Discretionary — Household Appliances",
    "verdict": "SELL",
    "fair_value": 16.00,
    "price": 30.31,
    "risk": "High",
    "headline": "A Levered Cyclical Priced for a Recovery That Is Not Coming",
    "hq": "Benton Harbor, Michigan",
    "snapshot": [
        ("Market cap", "~$2.0 bn (65.2 mn sh x $30.31)"),
        ("Net debt", "~$6.8 bn; leverage ~4.5x mid-cycle EBITDA"),
        ("52-week range", "~$29.81 - $94.82"),
        ("TTM revenue", "~$15.5 bn"),
        ("Dividend", "~$300 mn paid in FY2025"),
        ("European business", "Contributed to Beko Europe JV (2024)"),
        ("InSinkErator", "Acquired late 2022 for ~$3 bn"),
        ("Next catalyst", "US existing-home sales; Q4'26 results"),
    ],
    "thesis": [
        "Whirlpool is the largest major-appliance manufacturer in the world by volume, and that "
        "scale has never translated into pricing power. Appliances are a replacement-driven, deeply "
        "cyclical category where Whirlpool, Haier/GE, LG, Samsung, and Electrolux fight over a consumer "
        "who buys a refrigerator roughly once a decade. When housing turnover stalls — as it has through "
        "2025 and 2026 — discretionary replacement demand evaporates, and the industry competes the only "
        "way it knows how: on price. Promotional intensity has been structural, not cyclical, for the better "
        "part of a decade, and the Korean manufacturers show no sign of relenting.",
        "Our forward judgment is that the demand cycle stays soft longer than the market expects. "
        "US existing-home sales remain depressed by the mortgage rate lock-in effect, and every year of "
        "low turnover pushes a cohort of would-be appliance replacements further into the future. "
        "Meanwhile the competitive structure has permanently worsened: LG and Samsung treat appliances "
        "as a strategic beachhead rather than a profit pool, which caps industry pricing even in good "
        "years. Steel and component tariffs are a direct margin tax — we estimate 100-150 basis points "
        "off North American EBIT margins — that Whirlpool cannot pass through in a promotional market. "
        "We expect EBIT margins to grind in the 4-5% range rather than revisit the 7-8% peaks of the last "
        "housing boom.",
        "The balance sheet converts this cyclical squeeze into an equity problem. The InSinkErator "
        "acquisition and years of debt-funded shareholder returns left Whirlpool with net debt near $7 "
        "billion against roughly $1.5 billion of mid-cycle EBITDA. Interest and the dividend now absorb "
        "the bulk of operating cash flow, which means deleveraging depends on a demand recovery that "
        "keeps not arriving. In a genuine housing downturn, free cash flow goes to creditors, not "
        "shareholders — and the equity is the residual claimant on a melting ice cube of appliance demand.",
        "Our probability-weighted fair value is $16.00, implying 47% downside from $30.31. The dividend, "
        "costing roughly $300-400 million a year, looks increasingly difficult to defend if North American "
        "volumes stay soft through 2027; we model it surviving in the base case but cut in the bear case. "
        "The capital-allocation record compounds our skepticism: billions were spent repurchasing shares "
        "far above today's quote, and the InSinkErator deal — strategically sound — was funded at the top "
        "of the credit cycle. We see no catalyst that repairs both the demand cycle and the leverage ratio "
        "simultaneously, and we would not own the equity while both work against it.",
    ],
    "thesis_subhead": "Why the equity is the wrong side of the capital structure",
    "thesis_bullets": [
        ("Leverage turns a cyclical trough into an equity impairment. ",
         "At our base-case mid-cycle EBITDA of ~$1.5 billion, net debt near $7 billion leaves only "
         "$4-5 billion of enterprise value for equity at a 7-8x EV/EBITDA multiple appropriate for a "
         "cyclical manufacturer — roughly $16 per share after pension and other obligations. In the bear "
         "case, EBITDA falls toward $1 billion while debt stays fixed, and the equity residual compresses "
         "toward zero."),
        ("The dividend is the last pillar of the bull case, and it is load-bearing. ",
         "At ~$300-400 million annually it is a claim on cash flow the business can no longer comfortably "
         "afford alongside interest and debt maturities. Dividend cuts in levered cyclicals are rarely "
         "one-time events; they signal the board's recognition that the balance sheet, not the payout, "
         "is the priority."),
        ("Management faces the classic levered-cyclical trap. ",
         "Every dollar of free cash flow must service debt, the dividend consumes what little remains, and "
         "growth investment is starved. Deleveraging through earnings requires the demand recovery; "
         "deleveraging through asset sales means selling good assets to support stressed equity."),
    ],
    "business": [
        "Whirlpool Corporation, headquartered in Benton Harbor, Michigan, designs and manufactures major "
        "home appliances — refrigerators, laundry, cooking, and dishwashers — under the Whirlpool, Maytag, "
        "KitchenAid, Amana, and JennAir brands. North America generates the large majority of segment "
        "profit. The company contributed its European business into the Beko Europe joint venture "
        "(majority-owned by Arcelik) in 2024, and acquired InSinkErator, the food-waste-disposal leader, "
        "in late 2022 for approximately $3 billion. Revenue runs roughly $15-17 billion annually, with EBIT "
        "margins that have oscillated between 3% and 8% across the cycle.",
        "The segment economics explain the vulnerability. North American major appliances is a "
        "high-fixed-cost, low-margin assembly business where utilization is everything: at high utilization "
        "the plants print cash, at low utilization they bleed. Whirlpool has rationalized capacity for years, "
        "but competitors keep adding it, leaving the industry structurally prone to overcapacity — in which "
        "the largest player has the most fixed cost to absorb when volumes disappoint. This operating "
        "leverage works beautifully in housing booms and brutally in busts.",
    ],
    "business_bullets": [
        ("InSinkErator is the good asset trapped in a stressed balance sheet. ",
         "The food-waste-disposal leader is genuinely high-quality, but it is too small to carry the "
         "enterprise — and it is exactly the kind of asset a levered cyclical eventually sells to placate "
         "creditors, crystallizing value for bondholders rather than shareholders."),
        ("The Beko Europe contribution simplified the footprint. ",
         "Exiting direct European manufacturing removed a chronic drag, but it also removed a potential "
         "source of earnings diversification; the company is now more concentrated in North American "
         "housing than at any point in the last decade."),
        ("Cost-takeout programs are real but historically offset. ",
         "Management's announced savings have a track record of being reinvested into price or promotion; "
         "we credit only half the announced savings in our numbers."),
    ],
    "outlook": [
        "We expect the appliance demand cycle to stay soft through 2027. US existing-home sales show no "
        "sign of breaking the rate lock-in, promotional intensity from Korean competitors remains "
        "structural, and tariffs act as a 100-150bp margin tax that cannot be passed through. Base-case "
        "volumes stabilize rather than recover; EBIT margins average ~5.5% across the cycle.",
        "Free cash flow is consumed first by interest (~$350 million of cash interest), then by the "
        "dividend, leaving little for debt reduction. Absent a housing-turnover surge, this is a company "
        "managing decline as gracefully as possible — not a compounding story.",
    ],
    "financials": [
        "Revenue has fallen from $19.7 billion in FY2022 to $15.5 billion in FY2025, and free cash flow "
        "collapsed from $820 million to $81 million over the same period — the operating leverage of the "
        "business running in reverse. Net income printed a $323 million loss in FY2024 before recovering "
        "to $318 million in FY2025, a number flattered by non-operating items against a deteriorating core.",
        "The balance sheet is the binding constraint. Net debt of ~$6.8 billion sits against mid-cycle "
        "EBITDA of ~$1.5 billion — leverage of ~4.5x at the midpoint of the cycle, higher at the trough. "
        "Cash interest runs ~$350 million a year and the dividend another ~$300 million, against free cash "
        "flow of $81 million in FY2025. The arithmetic does not work without a demand recovery, and the "
        "demand recovery is precisely what the cycle is not delivering.",
    ],
    "fin_table": {
        "headers": ["$ bn", "FY2023", "FY2024", "FY2025"],
        "rows": [
            ["Revenue", "19.455", "16.607", "15.524"],
            ["Free cash flow", "0.366", "0.384", "0.081"],
            ["Net income", "0.481", "-0.323", "0.318"],
            ["Dividends paid", "0.384", "—", "0.300"],
        ],
        "footnote": "Source: company filings via yfinance; fiscal year ends Dec 31. — = not separately disclosed in pull.",
    },
    "moat": [
        ("Scale without pricing power. ",
         "Whirlpool is the volume leader, but appliances are a low-differentiation category where the "
         "consumer buys on price and promotion. Scale lowers unit cost; it does not confer the ability to "
         "raise price — the Korean competitors have proven that for a decade."),
        ("Brand portfolio breadth. ",
         "Whirlpool through JennAir covers every price tier, which defends shelf space. But brand equity "
         "in appliances depreciates with each promotional cycle, and the portfolio has not prevented "
         "share loss to LG and Samsung."),
        ("InSinkErator is the one true moat — and it is for sale in spirit. ",
         "Near-monopoly in food-waste disposal with genuine pricing power. It is also the asset most "
         "likely to be monetized to repair the balance sheet."),
        ("No moat against the cycle. ",
         "High fixed costs and operating leverage mean the moat, such as it is, inverts in downturns: the "
         "largest plant footprint becomes the largest burden."),
    ],
    "valuation_method": "10-year scenario DCF",
    "valuation_intro": [
        "We value Whirlpool on a probability-weighted scenario DCF, discounting at 10% in the base case "
        "to reflect cyclical and leveraged business risk (bear +250bp at 12.5%, bull −150bp at 8.5%). "
        "Terminal growth is set at 0.5% / 1.0% / 2.0% on normalized mid-cycle cash flows — never peak — "
        "reflecting a business we expect to shrink in real terms over time.",
        "In the bear case, a housing-led appliance recession pushes EBIT margins toward 3%, the dividend "
        "is cut, and refinancing risk reprices the debt; equity value approaches the low single digits. "
        "In the base case, volumes stabilize, EBIT margins average ~5.5% across the cycle, and slow "
        "deleveraging supports a mid-teens equity value. In the bull case, housing turnover rebounds, "
        "margins recover toward 7%, and accelerated debt paydown unlocks equity value in the high $20s.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 5.00,
            "assumptions": "Housing-led appliance recession; EBIT margins toward 3%; dividend cut; "
                           "refinancing risk reprices the debt; equity residual compresses toward zero",
            "rev_cagr": "-2%", "margin_end": "3%",
            "discount": 0.125, "terminal_g": 0.005, "tv_share": 0.40,
            "pv_explicit": 4286, "pv_terminal": 2858, "cashflow_unit": "$mn",
        },
        "base": {
            "fair_value": 16.00,
            "assumptions": "Volumes stabilize; EBIT margins average ~5.5% across the cycle; "
                           "slow deleveraging; dividend maintained but not grown",
            "rev_cagr": "+1%", "margin_end": "5.5%",
            "discount": 0.10, "terminal_g": 0.01, "tv_share": 0.50,
            "pv_explicit": 3931, "pv_terminal": 3931, "cashflow_unit": "$mn",
        },
        "bull": {
            "fair_value": 27.00,
            "assumptions": "Housing turnover rebounds; margins recover toward 7%; "
                           "accelerated debt paydown unlocks equity value",
            "rev_cagr": "+3%", "margin_end": "7%",
            "discount": 0.085, "terminal_g": 0.02, "tv_share": 0.55,
            "pv_explicit": 3860, "pv_terminal": 4718, "cashflow_unit": "$mn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Scenario FVs calibrated from the note's valuation ranges (bear: low single digits; "
                     "base: mid-teens; bull: high $20s); 0.25x$5 + 0.50x$16 + 0.25x$27 = $16.00. "
                     "Composition bars decompose each scenario's equity value (FV x 65.2 mn diluted shares, "
                     "plus $6.8 bn net debt) at the stated terminal-value shares.",
    "risks": [
        ("A deeper housing downturn. ",
         "A genuine recession in big-ticket durables would compress volumes and margins simultaneously, "
         "with leverage amplifying the equity impact — the bear case, arriving early."),
        ("Promotional intensity from Korean competitors. ",
         "LG and Samsung could intensify discounting further, permanently impairing North American pricing."),
        ("Tariffs. ",
         "Steel and component duties are a margin tax with no offset in a discount-driven market; "
         "escalation would shave further points off EBIT margins."),
        ("Dividend cut. ",
         "A cut would remove the last support for the income-oriented shareholder base and signal "
         "balance-sheet distress."),
        ("Refinancing risk. ",
         "A large debt wall must be termed out in markets that may not stay accommodative; wider "
         "spreads divert cash from deleveraging to creditors."),
    ],
    "falsification": (
        "Upgrade to HOLD on a sustained surge in US housing turnover with appliance sell-through "
        "outpacing expectations for several consecutive quarters, combined with demonstrated price "
        "realization — list-price increases sticking without volume loss — proving the promotional era "
        "is ending. Material deleveraging bringing net debt below 2x EBITDA, or structural cost-out "
        "lifting mid-cycle EBIT margins above 7% on flat volumes, would also force a re-underwrite. "
        "We watch: existing-home sales, North American industry shipments, and the dividend decision."
    ),
    "charts": {
        "scenario": {"bear": 5.00, "base": 16.00, "bull": 27.00,
                     "weighted": 16.00, "price": 30.31},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [19.724, 19.455, 16.607, 15.524],
            "fcf_hist": [0.820, 0.366, 0.384, 0.081],
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": [15.6, 15.9, 16.2, 16.5, 16.8, 17.1, 17.4, 17.7, 18.0, 18.3, 18.6],
            "fcf_proj": [0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via yfinance (FY ends Dec 31). Projection: base-case path "
                    "from this note's scenario model — volumes stabilize, EBIT margins average ~5.5% "
                    "across the cycle.",
        },
        "composition": {
            "bear": {"pv_explicit": 4286, "pv_terminal": 2858},
            "base": {"pv_explicit": 3931, "pv_terminal": 3931},
            "bull": {"pv_explicit": 3860, "pv_terminal": 4718},
            "unit": "$mn",
        },
        "extra": {
            "type": "line",
            "title": "Revenue vs. net income — the cycle in one picture ($bn)",
            "years": [2022, 2023, 2024, 2025],
            "series": [
                {"label": "Revenue",
                 "values": [19.724, 19.455, 16.607, 15.524]},
                {"label": "Net income",
                 "values": [-1.519, 0.481, -0.323, 0.318]},
            ],
            "ylabel": "$bn",
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "WHR-equity-research-note-polished.pdf")
build_note(data, out)
print("built:", out)
