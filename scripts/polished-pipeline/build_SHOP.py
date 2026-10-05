"""SHOP polished note. Research analysis, not investment advice.

Scenario numbers: authoritative v2 JSON (~/workspace/shop-research/valuation_output_v2.json).
Bear $23.3 / base $139.8 / bull $243.7, weighted $136.7 -> $137 target.
History: yfinance annuals. Projection: base-case growth/margin path off FY26E $15.3B.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

data = {
    "ticker": "SHOP",
    "company": "Shopify Inc.",
    "exchange": "NYSE",
    "sector": "Technology — E-Commerce Software & Payments",
    "verdict": "HOLD",
    "fair_value": 137.00,
    "price": 151.39,
    "risk": "Medium-High",
    "headline": "Commerce's Operating System — Owned by Giants, Priced for Perfection",
    "ceo": "Tobias Lütke",
    "hq": "Ottawa, Canada",
    "snapshot": [
        ("Market cap", "~$196 bn (1.296 bn sh × $151.39)"),
        ("Net cash", "~$4.77 bn (per model)"),
        ("52-week range", "~$94.00 – $182.19"),
        ("GMV / revenue attach", "$418 bn GMV; 2.74% blended attach"),
        ("Gross margin profile", "~48% overall; Merchant Solutions ~38%, Subscriptions ~77%"),
        ("Merchant Solutions", "~75% of revenue; Shop Pay ~70% of GMV"),
        ("Free cash flow margin", "~20% (FY2025)"),
        ("Q4'25 guide (Dec 5 print)", "Revenue +~29% YoY; GM 37.9% (MS) / 77.0% (Sub)"),
        ("AI shopping presence", "Integrated with ChatGPT, Gemini, Copilot agents"),
        ("Next catalyst", "Q4'25 earnings (December 2026); holiday GMV / attach print"),
    ],
    "thesis": [
        "Shopify has become the operating system of independent commerce. On $418 billion of gross merchandise "
        "volume the company extracts a 2.74% blended attach rate, and the machinery behind that take is "
        "genuinely impressive: merchant solutions are now roughly three-quarters of revenue, Shop Pay processes "
        "about 70% of GMV, and the gross-margin stack — ~38% on merchant solutions, ~77% on subscriptions — "
        "funds a free-cash-flow margin near 20% that most software companies would envy. The business earns its "
        "premium multiple. The stock does not earn the price it trades at.",
        "Our judgment, and the reason this is a HOLD at $151.39 rather than a buy, is that the current price "
        "demands flawless execution on two independent bets simultaneously. The first is that e-commerce "
        "penetration and Shopify's share of it compound at roughly 20% for a decade — a growth path that takes "
        "GMV from $418 billion toward the multi-trillion scale while the attach rate holds or rises. The second "
        "is that the margin expansion embedded in that growth — from ~20% free-cash-flow margins to a 23% "
        "through-cycle level — survives the pricing discipline the giant platforms are imposing. Both bets are "
        "plausible. Neither is certain. And the market is paying for both.",
        "The pressure on the attach rate is the structural story of this note. Shopify does not own its "
        "endpoints: distribution runs through Apple, Google, Meta, and Microsoft, which control the phones, the "
        "searches, and the feeds where discovery happens — and each takes its toll, most visibly the roughly 30% "
        "Apple extracts from App Store transactions, against which Shopify's own App Store keeps about 20%. As "
        "commerce migrates into agentic AI shopping — ChatGPT, Gemini, Copilot agents that transact on the "
        "shopper's behalf — the platform layer's leverage over the commerce layer grows, not shrinks. Shopify "
        "has integrated with these agents, which is the right move, but the tollbooth owner and the tollbooth "
        "tenant do not earn the same return. Our terminal assumption that the attach rate holds rather than "
        "compresses is a bet on Shopify's merchant-side leverage; it is one of the least certain numbers in the "
        "model.",
        "On a 10-year scenario DCF the numbers are $23.3 / $139.8 / $243.7, weighted to a $137 target — 9.5% "
        "below the quote. The base case is genuinely optimistic: 20.2% revenue CAGR for a decade, margins "
        "expanding to 23%, GMV attach preserved. Even that optimistic path is worth less than the current "
        "price. The upside case ($243.7) requires the bull version of everything — 23.9% CAGR, 28% margins, a "
        "lower 8.5% discount — and still only offers 61% upside from $151.39. We would buy this franchise at a "
        "price that compensates for the attach-rate uncertainty. That price is around $137, not $151.",
    ],
    "thesis_bullets": [
        ("$418B GMV at 2.74% attach is a real franchise. ",
         "Merchant solutions at ~75% of revenue and Shop Pay at ~70% of GMV show a platform that keeps "
         "deepening its wallet share per merchant — the economics work, today."),
        ("The tollbooth problem is structural. ",
         "Shopify rents its endpoints from Apple/Google/Meta/Microsoft; the ~30% Apple toll versus "
         "Shopify's ~20% App Store take is the template for how platform leverage flows. Agentic AI shopping "
         "strengthens the platforms, not the tenants."),
        ("The price requires two bets at once. ",
         "20%+ revenue CAGR for a decade AND preserved attach rates AND margin expansion — our base case "
         "grants all three and is still worth $139.8, below the $151.39 quote."),
    ],
    "business": [
        "Shopify provides the commerce infrastructure for millions of merchants: storefronts, checkout (Shop "
        "Pay), payments (Shopify Payments), shipping, capital, and the App Store ecosystem. Revenue splits "
        "into two streams. Merchant Solutions (~75% of revenue) is payments and transaction-adjacent services "
        "— it scales with GMV and carries a ~38% gross margin. Subscription Solutions (~25%) is the SaaS "
        "recurring core at ~77% gross margin. The blended gross margin is roughly 48%, and the business has "
        "reached a ~20% free-cash-flow margin — a genuinely software-grade profit profile on what is "
        "fundamentally a volume business.",
        "Growth has been re-accelerating: revenue growth hit 33% in Q3 2025, GMV growth 32% to $111.5 billion "
        "in the quarter, and Q4 2025 guidance (reported December 5, 2025) calls for roughly 29% revenue growth "
        "with gross margins of 37.9% on merchant solutions and 77.0% on subscriptions — the mix holding "
        "remarkably well. Management frames the opportunity as agentic AI commerce: Shopify is integrating "
        "with ChatGPT, Gemini, and Copilot shopping agents, positioning the platform as the checkout layer "
        "wherever agents transact. Enterprise merchant wins continue, and the App Store adds a second revenue "
        "engine on top of the GMV take.",
        "The forward question is whether the attach rate is the ceiling or the floor. Every percentage point of "
        "attach on $418 billion of GMV is $4.2 billion of revenue; holding 2.74% while GMV grows 20% annually is "
        "the entire base case. The platforms' leverage is the risk: as Apple, Google, Meta, and Microsoft "
        "interpose themselves between merchants and shoppers — now including AI agents — the take available "
        "to the commerce layer compresses at the margin. Shopify's counter is merchant indispensability: "
        "switching the operating system of your business is far harder than switching an ad channel.",
    ],
    "business_bullets": [
        ("Merchant Solutions (~75% of revenue, ~38% GM). ",
         "Payments and transaction services scaling with GMV; Shop Pay at ~70% of GMV is the moat's "
         "operational expression."),
        ("Subscriptions (~25% of revenue, ~77% GM). ",
         "The SaaS recurring core; high-margin ballast as transaction revenue cycles."),
        ("App Store (~20% take). ",
         "The ecosystem flywheel: third-party apps deepen merchant lock-in while Shopify clips the "
         "marketplace spread — though Apple's ~30% toll is the reminder of who owns the endpoint."),
        ("Agentic AI positioning. ",
         "Integrated with ChatGPT, Gemini, and Copilot shopping agents; the bet is that Shopify becomes "
         "the checkout layer wherever agents transact."),
    ],
    "outlook": [
        "The next two years are strong almost by construction. GMV growing in the low 30s, revenue guided to "
        "+29% in Q4 2025, and the merchant base expanding through enterprise wins gives Shopify one of the "
        "cleanest near-term growth profiles in large-cap software. Our base case runs revenue from $15.3 "
        "billion in FY2026 to $96.1 billion by 2036 — a 20.2% CAGR — with free-cash-flow margins expanding from "
        "14% to a 23% terminal level as the mix matures. That is an optimistic decade by any standard, and it "
        "is worth $139.8.",
        "The two judgment calls that determine whether the price is justified are the attach rate and the "
        "discount. On the attach rate, we hold 2.74% roughly flat through the decade — neither expanding on "
        "App Store leverage nor compressing under platform tolls. This is the single assumption we are least "
        "sure of, and it cuts both ways: AI-agent checkout could deepen Shopify's take per transaction if the "
        "platform becomes the trusted execution layer, or it could become another toll collected by the "
        "endpoint owners. On the discount, 10% base reflects a genuinely high-quality franchise with "
        "GMV-concentration and platform-dependency risk; the bull's 8.5% is the franchise-as-monopoly case.",
        "What would change the call: sustained GMV growth above 30% with attach expansion — the App Store and "
        "payments mix pushing blended take above 3% — would validate the bull path toward $243.7. Conversely, "
        "any quarter where GMV grows but revenue attach slips, or where a major platform tightens its commerce "
        "terms, validates the platform-leverage thesis and we would cut toward the bear ($23.3 — the case where "
        "the attach collapses and growth stalls). Watch Q4 2025 (December 2026): holiday GMV and the attach "
        "print are the numbers that matter.",
    ],
    "financials": [
        "The margin stack is the business: 38% gross on merchant solutions, 77% on subscriptions, blended ~48%, "
        "converting to ~20% free-cash-flow margins at scale. Our model has FY2026 owner FCF at $2.15 billion on "
        "$15.3 billion of revenue (~14%), expanding to $22.1 billion on $96.1 billion by 2036 (23%). This is a "
        "margin-expansion story as much as a growth story — and the expansion is assumed, not demonstrated: "
        "Shopify's cost structure must absorb payment processing costs, AI investment, and platform tolls while "
        "growing headcount-sensitive functions slower than GMV. The historical record is encouraging — margins "
        "have expanded from negative to ~20% — but the last five points of expansion are always the hardest.",
        "The balance sheet is a fortress: ~$4.77 billion of net cash (our model figure), no leverage constraint "
        "on the story, and the company's history of one-time gains (the Affirm/Doordash/Global-E stakes "
        "harvested in prior years) is a reminder that reported earnings periodically flatter. We value on "
        "owner free cash flow, not GAAP net income, precisely to exclude those.",
    ],
    "fin_table": {
        "headers": ["$ bn", "FY2022", "FY2023", "FY2024", "FY2025"],
        "rows": [
            ["Revenue", "5.60", "7.06", "8.88", "11.56"],
            ["YoY growth", "—", "+26%", "+26%", "+30%"],
            ["Gross margin", "—", "—", "~48%", "~48%"],
            ["Free cash flow", "−0.19", "0.91", "1.60", "2.01"],
            ["FCF margin", "−3%", "13%", "18%", "~20%"],
            ["GMV (annual est.)", "—", "—", "~$293", "$418"],
        ],
        "footnote": "Sources: company filings; annuals via yfinance. FY2026E: $15.3B revenue, $2.15B owner FCF "
                    "(model anchors).",
    },
    "moat": [
        ("The merchant operating system. ",
         "Millions of merchants run their business on Shopify; switching the OS of your company is "
         "prohibitively costly. Data, integrations, and workflows compound into real lock-in."),
        ("Shop Pay at 70% of GMV. ",
         "The highest-converting checkout on the internet is a network effect: more shoppers with Shop Pay "
         "accounts make Shop Pay more valuable to merchants, and vice versa."),
        ("The App Store ecosystem. ",
         "Third-party developers extend the platform in ways Shopify could never build alone — and Shopify "
         "clips ~20% while deepening merchant dependence."),
        ("The moat's boundary is the endpoint. ",
         "Shopify does not own the phone, the search, or the feed. Every platform toll — Apple's 30% is the "
         "template — is a tax on the franchise that Shopify cannot unilaterally resist."),
    ],
    "valuation_method": "10-year scenario DCF on owner free cash flow (FY2027–FY2036)",
    "valuation_intro": [
        "We value Shopify on a 10-year explicit DCF of owner free cash flow (FY2027–FY2036), weights bear 25% / "
        "base 50% / bull 25%. Scenario discounts: base 10.0% (high-quality franchise, GMV concentration, "
        "platform-dependency risk), bear 12.5% (base + 250bp), bull 8.5% (base − 150bp). Terminal growth "
        "1.5% / 2.5% / 1.0% on year-10 FCF at the scenario's terminal margin (15% / 23% / 28%) — no peak "
        "margins. Revenue grows along the scenario growth path (10-year CAGR: bear 2.9%, base 20.2%, bull "
        "23.9%); FCF margin glides from ~14% (FY2026) to the terminal margin. Equity = firm EV + $4.77B net "
        "cash, over 1.296B diluted shares. Terminal value is 34–70% of EV across scenarios — within "
        "discipline, no haircut required.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 23.30,
            "assumptions": "Platform tolls compress the attach rate; e-commerce growth normalizes; GMV CAGR stalls at 2.9%; FCF margins cap at 15% as costs absorb the platform taxes",
            "rev_cagr": "+2.9%", "margin_end": "15%",
            "discount": 0.125, "terminal_g": 0.015, "tv_share": 0.342,
            "pv_explicit": 16.73, "pv_terminal": 8.70, "cashflow_unit": "$bn",
        },
        "base": {
            "fair_value": 139.80,
            "assumptions": "GMV compounds ~20% for a decade with attach held at ~2.7%; FCF margins expand 14% to 23%; agentic AI commerce deepens rather than displaces the platform's take",
            "rev_cagr": "+20.2%", "margin_end": "23%",
            "discount": 0.10, "terminal_g": 0.025, "tv_share": 0.660,
            "pv_explicit": 59.98, "pv_terminal": 116.43, "cashflow_unit": "$bn",
        },
        "bull": {
            "fair_value": 243.70,
            "assumptions": "Franchise-as-monopoly: 23.9% revenue CAGR; attach expands above 3% on App Store/payments mix; 28% terminal FCF margins; AI-agent checkout deepens Shopify's per-transaction take",
            "rev_cagr": "+23.9%", "margin_end": "28%",
            "discount": 0.085, "terminal_g": 0.01, "tv_share": 0.697,
            "pv_explicit": 94.25, "pv_terminal": 216.82, "cashflow_unit": "$bn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "0.25×$23.3 + 0.50×$139.8 + 0.25×$243.7 = $136.7 → $137 target. "
                     "Bear meets all hurt conditions (revenue CAGR ~3%, margin compression, 25%+ derating).",
    "risks": [
        ("Platform leverage over the franchise. ",
         "Apple, Google, Meta, Microsoft own the endpoints; the ~30% App Store toll is the template. Agentic "
         "AI shopping strengthens the endpoint owners' hand, not Shopify's."),
        ("Attach-rate compression. ",
         "Every 10bp of attach on $418B GMV is ~$420M of revenue; competition or platform terms that "
         "compress the 2.74% take cut the model at the top line with no offsetting cost saving."),
        ("Growth expectations are extreme. ",
         "The price embeds a 20%+ revenue CAGR for a decade — the base case grants it and is still worth "
         "less than the quote. Any deceleration reprices sharply."),
        ("Take-rate sensitivity. ",
         "Merchant solutions is ~75% of revenue at ~38% gross margin; pricing pressure on payments "
         "processing flows directly to the bottom line."),
        ("Competition. ",
         "Amazon's Buy with Prime, BigCommerce/Adobe Commerce at the enterprise edge, and the platforms' "
         "own native checkout products all contest GMV share."),
        ("Cyclicality of GMV. ",
         "Consumer spending drives GMV; a demand slowdown hits the transaction-revenue majority first."),
    ],
    "falsification": (
        "The base case's attach-rate assumption would be withdrawn if blended attach slips for two "
        "consecutive quarters while GMV grows — that breaks the revenue path from the inside and we would "
        "cut toward the bear case. A major platform tightening commerce terms (higher tolls, mandatory native "
        "checkout) is a second falsification trigger. Conversely, attach expansion above 3% sustained over a "
        "year — via App Store and payments mix — validates the bull path. Watch Q4 2025 (December 2026): "
        "holiday GMV and the attach print are the numbers that matter."
    ),
    "methodology": [
        "We value the business on a 10-year explicit DCF of owner free cash flow (bear 25% / base 50% / "
        "bull 25%). Revenue follows the scenario growth path (bear 2.9% / base 20.2% / bull 23.9% 10-year "
        "CAGR); free-cash-flow margin glides from the current level to the scenario's terminal margin (15% / "
        "23% / 28%) over the horizon. Discount rates: base 10.0%, bear +250bp (12.5%), bull −150bp (8.5%). "
        "Terminal growth (1.5% / 2.5% / 1.0%) applies to year-10 FCF at the scenario's terminal margin. "
        "Equity = firm EV + net cash; divided by diluted shares. Bear cases must be genuinely adverse and sit "
        "below the current price. The published target is the probability-weighted fair value, stated as a "
        "12-month horizon reference.",
        "Risk ratings (Low / Medium / Medium-High / High) combine business-model volatility, the balance "
        "sheet, and the valuation. This note is independent research-style analysis for informational purposes "
        "only and is not investment advice. Financial figures are drawn from company releases and SEC filings; "
        "market data as of October 2, 2026. Projections and the price target are the author's estimates and "
        "involve uncertainty. Past performance does not predict future results.",
    ],
    "charts": {
        "scenario": {"bear": 23.3, "base": 139.8, "bull": 243.7, "weighted": 136.7, "price": 151.39},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [5.60, 7.06, 8.88, 11.56],
            "fcf_hist": [-0.19, 0.91, 1.60, 2.01],
            "years_proj": [2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": [19.43, 24.39, 30.24, 37.04, 44.82, 53.56, 63.20, 73.63, 84.68, 96.11],
            "fcf_proj": [3.01, 4.15, 5.59, 7.41, 9.41, 11.78, 14.38, 16.94, 19.48, 22.10],
            "unit": "$bn", "fcf_label": "Owner FCF",
            "note": "History: company filings via yfinance. Projection: base-case path off the $15.3B FY2026E "
                    "revenue anchor (20.2% 10-yr CAGR; FCF margin gliding 14% to 23%).",
        },
        "composition": {
            "bear": {"pv_explicit": 16.73, "pv_terminal": 8.70},
            "base": {"pv_explicit": 59.98, "pv_terminal": 116.43},
            "bull": {"pv_explicit": 94.25, "pv_terminal": 216.82},
            "unit": "$bn",
        },
        "extra": {
            "type": "line",
            "title": "Free-cash-flow margin — history vs. base-case path",
            "years": [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "series": [{"label": "FCF margin",
                        "values": [-3.4, 12.9, 18.0, 17.4, 14.1, 15.5, 17.0, 18.5, 20.0, 21.0, 22.0, 22.75, 23.0, 23.0, 23.0]}],
            "ylabel": "%",
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "SHOP-equity-research-note-polished.pdf")
build_note(data, out)
print("built:", out)
