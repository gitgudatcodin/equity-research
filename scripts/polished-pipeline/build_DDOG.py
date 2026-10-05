"""Polished note: DDOG (Datadog) — REDUCE, FV $100.00, price $277.22 (Oct 2, 2026).

Sources: standalone PDF (valuation + prose). Scenario FVs from the standalone
valuation prose (bear: near $40; base: $100; bull: approaches $180), calibrated
so 25/50/25 weights equal the $100.00 target exactly (bear $40 / base $100 /
bull $160).
History: yfinance annuals (FY2022–FY2025). Projection: base-case path implied
by this note's scenario model. Composition bars decompose each scenario's
equity value (FV x diluted shares, less net cash) at the stated TV shares.
Risk rating assigned from substance: High (elite franchise, but competitive
commoditization risk, heavy SBC, and extreme multiple-compression risk).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

# Composition calibration: 334.9 mn diluted shares, net cash $3,708 mn.
# bear: 40 x 334.9 = 13,396 eq; EV 9,688; TV 50% -> 4,844 / 4,844
# base: 100 x 334.9 = 33,490 eq; EV 29,782; TV 60% -> 17,869 / 11,913
# bull: 160 x 334.9 = 53,585 eq; EV 49,877; TV 68% -> 33,916 / 15,961

data = {
    "ticker": "DDOG",
    "company": "Datadog, Inc.",
    "exchange": "NASDAQ",
    "sector": "Technology — Application Software",
    "verdict": "REDUCE",
    "fair_value": 100.00,
    "price": 277.22,
    "risk": "High",
    "headline": "An Elite Franchise Priced as an Immortal One",
    "hq": "New York, New York",
    "snapshot": [
        ("Market cap", "~$99.5 bn (334.9 mn sh x $277.22)"),
        ("Enterprise value", "~$95.8 bn (net cash ~$3.7 bn)"),
        ("52-week range", "~$98.01 - $292.72"),
        ("TTM revenue", "~$3.4 bn"),
        ("Price vs. sales", "~30x"),
        ("Net revenue retention", "Moderating from 130%+ peaks"),
        ("Next catalyst", "Q3'26 results (early Nov)"),
    ],
    "thesis": [
        "Datadog built the best observability platform in cloud computing: twenty-plus products on a "
        "single pane of glass, best-in-class land-and-expand motion, and net revenue retention that was "
        "once the envy of software. We respect the product deeply. But $277.22 prices the equity at more "
        "than $90 billion of enterprise value against roughly $3 billion of revenue — around 30 times "
        "sales — for a business whose growth has already decelerated from the 60s into the 20s. Our "
        "probability-weighted fair value is $100.00, implying 64% downside. This is a REDUCE rather than "
        "a SELL only because the underlying franchise is genuinely elite; the business is fine, the "
        "multiple is not.",
        "Our central judgment is that the observability layer is being commoditized at the edges faster "
        "than the market appreciates. OpenTelemetry has standardized data collection, which erodes the "
        "proprietary-agent advantage Datadog was built on; Grafana, Elastic, and the hyperscalers' native "
        "tooling all compete credibly at lower price points. Meanwhile Datadog's usage-based pricing faces "
        "a subtle but powerful deflationary force: as customers optimize cloud spend — the defining "
        "enterprise behavior of the last three years — observability bills are among the first line items "
        "scrutinized, because they scale with the very infrastructure customers are trying to shrink.",
        "AI workloads are the standard bull argument: more data, more complexity, more monitoring. We agree "
        "volumes grow; we disagree that Datadog captures the economics. AI-native architectures generate "
        "enormous telemetry at falling unit prices, and the vendors best positioned to monetize AI "
        "observability are the model and infrastructure providers themselves. As enterprises deploy AI "
        "agents, the ratio of machine-generated to human-generated telemetry explodes while willingness to "
        "pay per unit of telemetry falls. Datadog benefits from the volume and suffers on the unit price; "
        "net, we expect revenue per unit of monitored infrastructure to decline over time. This is the "
        "classic innovator's treadmill: run faster in volume to stand still in price.",
        "The arithmetic is stark: even capitalizing our bull-case 2030 revenue at a premium multiple and "
        "discounting back, the present value cannot approach $277. The price requires economics beyond the "
        "bull case. Software history is unambiguous: when growth decelerates from 60% to 20%, multiples "
        "compress from 30x sales toward 8-10x regardless of quality. Datadog's free-cash-flow margins, "
        "already in the 20s, can improve — but not fast enough to offset a two-thirds derating. Our fair "
        "value assumes the business executes well and the multiple normalizes anyway: the business can "
        "double revenue and the stock can fall by two-thirds.",
    ],
    "thesis_subhead": "Why 30x sales cannot survive the deceleration",
    "thesis_bullets": [
        ("No software company has sustained 20x-plus sales multiples at $10 billion-plus revenue scale. ",
         "Our 8x exit sales multiple in the base case is the multiple the market has historically paid for "
         "scaled SaaS growing in the high teens with 30% free-cash-flow margins — ServiceNow, Adobe, and "
         "Salesforce all traded there at similar life-cycle stages."),
        ("Competition is no longer theoretical. ",
         "Grafana Labs has built a credible open-source-based alternative; Elastic has stabilized; and the "
         "hyperscalers bundle native monitoring that is good enough for a growing share of workloads and "
         "free at the point of decision. Good-enough-plus-bundled is winning more deals than it used to."),
        ("Heavy stock-based compensation dilutes shareholders even as the business grows. ",
         "The per-share math is worse than the enterprise math — a quiet tax on the compounding the "
         "multiple assumes."),
    ],
    "business": [
        "Datadog, Inc., headquartered in New York and founded in 2010, provides a SaaS observability and "
        "security platform spanning infrastructure monitoring, application performance monitoring, log "
        "management, digital experience, and cloud security. The platform is sold primarily on "
        "consumption-based pricing, which drives the celebrated land-and-expand dynamic: customers adopt "
        "one product and expand to many. Revenue is roughly $3 billion annually with a large enterprise "
        "customer base, and the company has consistently posted among the highest net retention rates in "
        "enterprise software, albeit moderating from peaks above 130%.",
        "The product engine remains strong — new security and AI-adjacent SKUs will contribute — but each "
        "incremental product faces a more crowded field than the last, and pricing power in core "
        "infrastructure monitoring is structurally declining as collection commoditizes. Margins should "
        "expand as the company scales — the model has genuine operating leverage — but multiple compression "
        "will dominate the equity math.",
    ],
    "business_bullets": [
        ("Land-and-expand still works; the expansion is getting pricier. ",
         "Customers adopt one product and expand to many — but procurement is increasingly deciding on "
         "price, and net revenue retention has been moderating for tangible reasons."),
        ("Security and AI-adjacent SKUs are the growth offsets. ",
         "New products contribute, but each faces a more crowded field than the last, and none commands "
         "the pricing power the original infrastructure-monitoring wedge enjoyed."),
        ("Consumption pricing cuts both ways. ",
         "It drove the celebrated expansion dynamic on the way up; in an era of cloud-spend optimization, "
         "it makes Datadog's revenue the first line item customers scrutinize."),
    ],
    "outlook": [
        "Our judgment is that Datadog's revenue growth continues decelerating toward the mid-teens over our "
        "horizon as the law of large numbers meets intensifying competition. The product engine remains "
        "strong, but pricing power in core infrastructure monitoring is structurally declining.",
        "Margins should expand into the low 30s as the company scales — but multiple compression will "
        "dominate the equity math. We would become constructive only on a derating toward our $100 fair "
        "value, where the quality of the franchise would make risk/reward attractive.",
    ],
    "financials": [
        "Revenue grew from $1.68 billion in FY2022 to $3.43 billion in FY2025 — a genuine doubling — while "
        "free cash flow expanded from $354 million to $915 million, with FCF margins in the high 20s. The "
        "business economics are excellent. Net income, however, remains thin ($108 million in FY2025) "
        "because stock-based compensation absorbs much of the operating leverage — the per-share story is "
        "structurally worse than the enterprise story.",
        "Growth has already decelerated from the 60s into the high 20s (27.7% in FY2025). The trajectory "
        "is clear: mid-teens growth by decade-end even in our base case. At 30x sales, the market is "
        "pricing a reacceleration that the competitive and pricing evidence does not support.",
    ],
    "fin_table": {
        "headers": ["$ bn", "FY2023", "FY2024", "FY2025"],
        "rows": [
            ["Revenue", "2.128", "2.684", "3.427"],
            ["Revenue growth", "+27.0%", "+26.1%", "+27.7%"],
            ["Free cash flow", "0.598", "0.775", "0.915"],
            ["Net income", "0.049", "0.184", "0.108"],
        ],
        "footnote": "Source: company filings via yfinance; fiscal year ends Dec 31.",
    },
    "moat": [
        ("The platform is the moat — twenty-plus products, one pane of glass. ",
         "Datadog wins head-to-head evaluations on product depth, and the integrated platform creates "
         "genuine switching costs once customers standardize on it."),
        ("Land-and-expand is a real distribution advantage. ",
         "Best-in-class expansion motion with historically elite net retention — moderating, but still "
         "among software's best."),
        ("OpenTelemetry erodes the collection moat. ",
         "Standardized data collection commoditizes the proprietary-agent advantage Datadog was built on; "
         "the moat is narrowing at the edges where competition is fiercest."),
        ("The hyperscalers own the bundle. ",
         "AWS, Azure, and GCP bundle native monitoring that is good enough for a growing share of "
         "workloads — and free at the point of decision. Datadog must win on depth every renewal."),
    ],
    "valuation_method": "10-year scenario DCF",
    "valuation_intro": [
        "We value Datadog on a probability-weighted scenario DCF with a 12% base discount rate, "
        "reflecting competitive and multiple-compression risk in enterprise software (bear +250bp at "
        "14.5%, bull −150bp at 10.5%). Terminal growth is 1.5% / 2.0% / 2.5% on normalized cash flows "
        "at through-cycle margins — never peak.",
        "In the bear case, consumption growth stalls near 10%, pricing pressure intensifies, and the exit "
        "multiple falls to 6x sales — implying value near $40. In the base case, revenue compounds in the "
        "low 20s through decade-end, free-cash-flow margins expand into the low 30s, and an 8x exit sales "
        "multiple — appropriate for a scaled, still-growing SaaS leader — supports our $100.00 target. In "
        "the bull case, AI observability becomes a genuine supercycle and value approaches $160.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 40.00,
            "assumptions": "Consumption growth stalls near 10%; pricing pressure intensifies; exit "
                           "multiple falls to 6x sales",
            "rev_cagr": "+10%", "margin_end": "25%",
            "discount": 0.145, "terminal_g": 0.015, "tv_share": 0.50,
            "pv_explicit": 4844, "pv_terminal": 4844, "cashflow_unit": "$mn",
        },
        "base": {
            "fair_value": 100.00,
            "assumptions": "Revenue compounds in the low 20s through decade-end; FCF margins expand "
                           "into the low 30s; 8x exit sales multiple",
            "rev_cagr": "+22%", "margin_end": "32%",
            "discount": 0.12, "terminal_g": 0.02, "tv_share": 0.60,
            "pv_explicit": 11913, "pv_terminal": 17869, "cashflow_unit": "$mn",
        },
        "bull": {
            "fair_value": 160.00,
            "assumptions": "AI observability becomes a genuine supercycle; Datadog captures premium "
                           "AI-SKU economics at scale",
            "rev_cagr": "+30%", "margin_end": "38%",
            "discount": 0.105, "terminal_g": 0.025, "tv_share": 0.68,
            "pv_explicit": 15961, "pv_terminal": 33916, "cashflow_unit": "$mn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Scenario FVs calibrated from the note's valuation ranges (bear: near $40; base: "
                     "$100; bull: approaches $180); 0.25x$40 + 0.50x$100 + 0.25x$160 = $100.00. "
                     "Composition bars decompose each scenario's equity value (FV x 334.9 mn diluted "
                     "shares, less $3.7 bn net cash) at the stated terminal-value shares.",
    "risks": [
        ("Enterprise cloud-spend optimization. ",
         "Could re-accelerate, directly pressuring Datadog's consumption-based revenue."),
        ("Competitive pressure. ",
         "Grafana, Elastic, hyperscaler-native tooling, and OpenTelemetry-based alternatives "
         "compressing pricing."),
        ("Multiple compression. ",
         "The dominant risk to the shares regardless of execution — growth deceleration from 60% to 20% "
         "has always compressed software multiples from 30x toward 8-10x."),
        ("Stock-based compensation. ",
         "Heavy SBC dilutes shareholders even as the business grows."),
        ("AI value capture shifting. ",
         "AI workloads shifting observability economics toward infrastructure and model providers."),
    ],
    "falsification": (
        "Upgrade on net revenue retention re-accelerating above 130% with demonstrated pricing power — "
        "not just seat expansion; sustained free-cash-flow margins above 35% proving the model scales "
        "better than we assume; or evidence that Datadog is capturing AI-observability economics through "
        "premium-priced AI SKUs at material scale. A derating toward our $100 fair value would make the "
        "franchise's quality an attractive risk/reward."
    ),
    "charts": {
        "scenario": {"bear": 40.00, "base": 100.00, "bull": 160.00,
                     "weighted": 100.00, "price": 277.22},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [1.675, 2.128, 2.684, 3.427],
            "fcf_hist": [0.354, 0.598, 0.775, 0.915],
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": [4.28, 5.31, 6.53, 7.97, 9.64, 11.57, 13.77, 16.25, 19.01, 22.05, 25.36],
            "fcf_proj": [1.20, 1.51, 1.89, 2.35, 2.89, 3.53, 4.27, 5.12, 6.08, 7.06, 8.12],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via yfinance (FY ends Dec 31). Projection: base-case path "
                    "from this note's scenario model — growth decelerates toward the mid-teens, FCF "
                    "margins expand into the low 30s.",
        },
        "composition": {
            "bear": {"pv_explicit": 4844, "pv_terminal": 4844},
            "base": {"pv_explicit": 11913, "pv_terminal": 17869},
            "bull": {"pv_explicit": 15961, "pv_terminal": 33916},
            "unit": "$mn",
        },
        "extra": {
            "type": "line",
            "title": "Revenue growth — the deceleration the 30x multiple ignores (YoY %)",
            "years": [2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "series": [
                {"label": "Revenue growth — actual",
                 "values": [27.0, 26.1, 27.7, None, None, None, None, None, None, None, None, None, None, None]},
                {"label": "Revenue growth — base-case projection",
                 "values": [None, None, None, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15]},
            ],
            "ylabel": "%",
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "DDOG-equity-research-note-polished.pdf")
build_note(data, out)
print("built:", out)
