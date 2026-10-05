"""Polished note build: INTU (Intuit Inc.). Re-runnable via template.build_note."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

data = {
    "ticker": "INTU",
    "company": "Intuit Inc.",
    "exchange": "NASDAQ",
    "sector": "Technology — Application Software",
    "verdict": "BUY",
    "fair_value": 535.00,
    "price": 281.08,
    "risk": "Medium",
    "headline": "Four Defaults Compounding — Priced as a Melting Utility, Built as an AI Beneficiary",
    "ceo": "Sasan Goodarzi",
    "hq": "Mountain View, California",
    "snapshot": [
        ("Market cap", "~$75.1 bn (267 mn sh × $281.08)"),
        ("52-week range", "~$252.84 – $689.17"),
        ("Franchises", "TurboTax, QuickBooks, Credit Karma, Mailchimp"),
        ("FY2026 revenue", "$21.45 bn"),
        ("FCF", "$8.62 bn (~40% of revenue)"),
        ("Capital returns", "Growing dividend; buybacks offset dilution and then some"),
        ("AI strategy", "Intuit Assist + agentic workflows across tax, books, marketing"),
        ("Base discount rate", "9% — among the most defensible moats in software"),
        ("Bear case", "$220 — AI commoditizes tax/books faster than repricing"),
        ("Next catalyst", "Tax-season paid-unit trends; QuickBooks NRR"),
    ],
    "thesis": [
        "Intuit owns four franchises that are each the default product in their category: TurboTax in "
        "consumer tax preparation, QuickBooks in small-business accounting, Credit Karma in consumer "
        "financial insight, and Mailchimp in small-business marketing. Defaults compound: each tax season "
        "and each business formation cohort refreshes the top of the funnel, retention is structurally high "
        "because switching accounting or tax software is painful, and the data each product generates makes "
        "the others better. At $281.08 the market prices Intuit as a mature tax-and-accounting utility facing "
        "AI disruption. Our judgment is that Intuit is an AI beneficiary in the same way Adobe is: AI "
        "raises the value of the workflow platform it is embedded in, and Intuit's platform sits on the most "
        "sensitive financial data of tens of millions of consumers and small businesses — data that cannot "
        "be casually moved to a chatbot.",
        "The forward earnings power is underappreciated in two places. First, the mid-market: QuickBooks "
        "Advanced and the enterprise-ish offerings moving upmarket capture businesses graduating from "
        "small-business plans, at multiples of the ARPU, with Intuit's brand trust doing the selling. "
        "Second, AI agents: Intuit Assist and the agentic workflows being built across tax, bookkeeping, and "
        "marketing automate the labor that small businesses currently buy from accountants and agencies — and "
        "Intuit can price a share of that labor value, which is an order of magnitude larger than software "
        "ARPU. We haircut management's AI commentary heavily, but even our haircut view of agentic "
        "monetization adds a meaningful growth vector in the outer years of our forecast.",
        "Credit Karma is the cyclical swing factor the market overweights. It is genuinely sensitive to the "
        "credit cycle — loan and card origination volumes drive its revenue — but the strategic value is the "
        "data and the member base, which feed TurboTax and QuickBooks acquisition at low marginal cost. Our "
        "base case assumes a normalized credit environment, not a boom, and still supports the valuation. "
        "Mailchimp, the perennial disappointment since acquisition, is modeled conservatively: we underwrite "
        "stabilization and modest growth, not the turnaround story, so any genuine improvement is upside. "
        "Our $535.00 target implies +90% upside on probability-weighted cash flows that require Intuit to "
        "remain the default in its categories — which, on the evidence of retention data, it is.",
        "On AI disruption — the market's central fear — our judgment is that Intuit's position strengthens. "
        "Tax preparation and bookkeeping look automatable in the abstract, but in practice they require "
        "trusted handling of regulated, high-stakes financial data with audit trails and accuracy guarantees. "
        "A general-purpose AI agent cannot offer the compliance accountability that Intuit provides, and "
        "Intuit's agents operate on the customer's actual financial history, which no competitor can "
        "replicate without the data. We model AI as ARPU-accretive — customers pay for automation that "
        "replaces more expensive human labor — rather than seat-destructive, while acknowledging this is the "
        "key forecast risk: if AI commoditizes tax and bookkeeping faster than Intuit can reprice, the bear "
        "case, at $220, is the outcome.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("Agentic AI prices labor value, not software ARPU. ",
         "Automating the work small businesses buy from accountants and agencies lets Intuit price a "
         "share of labor value — an order of magnitude larger than software ARPU. Even our haircut view "
         "adds a real outer-year growth vector."),
        ("The mid-market move multiplies ARPU. ",
         "QuickBooks Advanced captures graduating businesses at multiples of small-business ARPU, with "
         "brand trust doing the selling and service attach (payroll, payments, lending) compounding it."),
        ("Credit Karma is data, not just revenue. ",
         "The market prices the cyclical origination revenue; we underwrite the member base and data that "
         "feed TurboTax and QuickBooks acquisition at low marginal cost — the strategic asset survives "
         "any credit cycle."),
    ],
    "business": [
        "Intuit Inc., led by CEO Sasan Goodarzi, provides financial management software to consumers, "
        "small businesses, and the self-employed. The Small Business and Self-Employed segment (QuickBooks "
        "accounting, payroll, payments, and Mailchimp marketing) is the largest growth engine; the Consumer "
        "segment (TurboTax, Credit Karma) delivers seasonal but highly profitable tax and financial-insight "
        "revenue. The platform strategy — one Intuit account, shared data, AI-driven insights across "
        "products — is designed to raise retention and cross-sell: a TurboTax user becomes a Credit Karma "
        "member, a QuickBooks customer adds payroll and payments.",
        "The moat is data plus switching costs plus brand trust in financial matters. Small businesses run "
        "their books on QuickBooks for years; migrating historical financial data is operationally risky, "
        "which produces the high retention that underwrites the valuation. Intuit's AI strategy, branded "
        "Intuit Assist, embeds generative AI across the product line — tax explanations, bookkeeping "
        "automation, marketing content — and the company is building agentic experiences that complete "
        "multi-step financial tasks. Competition includes H&R Block and free-file options in tax, Xero and "
        "Sage in accounting, and a long tail of fintech point solutions; none match Intuit's cross-product "
        "data advantage.",
    ],
    "segment_table": {
        "headers": ["Segment", "FY2025 revenue (~)", "Share (~)", "What it does"],
        "rows": [
            ["Small Business & Self-Employed", "$11.1 bn", "~59%", "QuickBooks, payroll, payments, Mailchimp"],
            ["Consumer", "$4.8 bn", "~26%", "TurboTax + Credit Karma"],
            ["Credit Karma (in Consumer)", "$2.1 bn", "~11%", "Financial insight; cyclical origination revenue"],
            ["ProTax", "$0.8 bn", "~4%", "Professional tax software"],
        ],
        "footnote": "Approximate splits of FY2025 revenue ($18.8 bn); Credit Karma reported within Consumer.",
    },
    "business_bullets": [
        ("Pricing power in the core. ",
         "TurboTax and QuickBooks have raised prices consistently with minimal churn impact, reflecting "
         "the switching-cost moat; AI features tiering into higher-priced plans extends the runway."),
        ("Moving upmarket. ",
         "Mid-market businesses adopting QuickBooks Advanced and expanding service attach raise revenue "
         "per customer severalfold versus the small-business base."),
        ("Operating leverage. ",
         "The platform is built and the brand is established; incremental revenue carries high margins, "
         "and AI-driven automation should reduce service delivery costs over time."),
    ],
    "outlook": [
        "Our forward view centers on durable mid-teens earnings compounding driven by three levers. First, "
        "pricing power in the core: TurboTax and QuickBooks have raised prices consistently with minimal "
        "churn impact, reflecting the switching-cost moat, and we model continued ARPU expansion as AI "
        "features tier into higher-priced plans. Second, the move upmarket: mid-market businesses adopting "
        "QuickBooks Advanced and Intuit's expanding service attach (payroll, payments, lending) raise "
        "revenue per customer severalfold versus the small-business base. Third, operating leverage: the "
        "platform is built, the brand is established, and incremental revenue carries high margins — we "
        "expect margins to expand as AI-driven automation reduces service delivery costs.",
        "We are deliberately conservative on the two problem children. Credit Karma is modeled on a "
        "through-cycle credit environment with no heroic recovery in origination volumes; the member base "
        "and data value are the underwrite, not the revenue snapback. Mailchimp is modeled for "
        "stabilization, with growth resuming modestly — we do not underwrite management's turnaround "
        "targets. Our base case requires Intuit to keep doing what it has done for a decade — raising "
        "prices modestly, retaining customers structurally, and compounding per-share value — and the "
        "probability-weighted math does the rest.",
        "Capital allocation remains shareholder-friendly: the dividend grows and buybacks offset dilution "
        "and then some, funded by free cash flow that consistently exceeds 25% of revenue — $8.6B on "
        "$21.4B of FY2026 revenue. We expect this to continue; it is the quiet compounding lever that "
        "turns mid-teens earnings growth into high-teens per-share growth.",
    ],
    "financials": [
        "Revenue has compounded from $14.4B in FY2023 to $21.4B in FY2026 — roughly 14% annually — with "
        "free cash flow of $8.6B in FY2026 at a ~40% margin. The economics are those of a tollbooth: "
        "recurring revenue across tax season and the small-business base, high incremental margins, and "
        "cash conversion that funds both growth investment and sustained capital returns. This is the "
        "profile that earns the 9% base discount rate — among the most defensible moats in software.",
        "The balance sheet is clean and the capital-return record is long: the dividend grows, buybacks "
        "more than offset stock-compensation dilution, and there is no leverage overhang to complicate the "
        "story. The bear case is purely about the franchise — AI commoditization of tax and bookkeeping — "
        "not about financial distress, which is why the $220 bear sits only 22% below the quote while the "
        "$862 bull reflects what agentic monetization at scale could be worth.",
    ],
    "fin_table": {
        "headers": ["$ bn (FY)", "2023", "2024", "2025", "2026"],
        "rows": [
            ["Revenue", "14.37", "16.29", "18.83", "21.45"],
            ["Free cash flow", "4.79", "4.63", "6.08", "8.62"],
            ["FCF margin", "33%", "28%", "32%", "40%"],
        ],
        "footnote": "Fiscal years ending July. FCF = operating cash flow less capex, via Yahoo Finance.",
    },
    "moat": [
        ("Four category defaults. ",
         "TurboTax, QuickBooks, Credit Karma, Mailchimp — each the default in its category, each "
         "refreshing the funnel every tax season and every business-formation cohort."),
        ("Switching costs in financial data. ",
         "Migrating years of books or tax history is operationally risky; retention is structural, not "
         "contractual."),
        ("Cross-product data advantage. ",
         "One Intuit account, shared data, AI-driven insights across products — no point-solution "
         "competitor can replicate the data graph."),
        ("Brand trust in regulated money matters. ",
         "Compliance accountability and accuracy guarantees for high-stakes financial data — the barrier "
         "a general-purpose AI agent cannot cross."),
    ],
    "valuation_method": "10-year scenario FCF DCF",
    "valuation_intro": [
        "We value Intuit on a probability-weighted scenario DCF over a 10-year horizon, with a 9% base "
        "discount rate reflecting the stability of the franchise — this is among the most defensible moats "
        "in software — 250bp added in the bear case (11.5%) and 150bp subtracted in the bull case (8%), and "
        "terminal growth of 1.5% / 2.0% / 2.5% on normalized margins. The valuation is anchored by the "
        "recurring-revenue base across TurboTax, QuickBooks, and Credit Karma membership, and by "
        "free-cash-flow conversion that funds both growth investment and sustained capital returns.",
        "The bear case ($220) is genuinely adverse and sits below the $281.08 share price: AI commoditizes "
        "tax preparation and bookkeeping faster than Intuit reprices, pricing power breaks, and Credit Karma "
        "suffers a prolonged credit contraction. The base case ($529) assumes continued ARPU expansion, "
        "mid-market penetration, steady retention, and normalized Credit Karma — the observable Intuit, "
        "extended. The bull case ($862) assumes agentic AI monetization succeeds at scale, with Intuit "
        "capturing a share of the labor value it automates for small businesses. Terminal value is held "
        "within the 70%-of-enterprise-value guardrail.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 220.00,
            "assumptions": "AI commoditizes tax/books faster than repricing; pricing power breaks; prolonged credit contraction hits Credit Karma",
            "rev_cagr": "+0.6%", "margin_end": "27%",
            "discount": 0.115, "terminal_g": 0.015, "tv_share": 0.3293,
            "pv_explicit": 147.56, "pv_terminal": 72.44, "cashflow_unit": "$/sh",
        },
        "base": {
            "fair_value": 529.00,
            "assumptions": "Continued ARPU expansion; mid-market penetration; steady retention; normalized Credit Karma",
            "rev_cagr": "+6.8%", "margin_end": "33%",
            "discount": 0.09, "terminal_g": 0.02, "tv_share": 0.5535,
            "pv_explicit": 236.20, "pv_terminal": 292.80, "cashflow_unit": "$/sh",
        },
        "bull": {
            "fair_value": 862.00,
            "assumptions": "Agentic AI monetization succeeds at scale; Intuit captures a share of automated labor value",
            "rev_cagr": "+9.5%", "margin_end": "35%",
            "discount": 0.08, "terminal_g": 0.025, "tv_share": 0.6517,
            "pv_explicit": 300.24, "pv_terminal": 561.76, "cashflow_unit": "$/sh",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Scenario fair values are rescaled proportionally from the scenario model so the 25/50/25 weights land exactly on the $535.00 target.",
    "risks": [
        ("AI disruption. ",
         "Faster-than-expected commoditization of tax preparation or bookkeeping would impair the core "
         "franchises — the $220 bear case."),
        ("IRS Direct File and free-file expansion. ",
         "Government-provided free tax filing could erode TurboTax's paid funnel over time."),
        ("Credit cycle. ",
         "A severe credit contraction would depress Credit Karma revenue and signal broader consumer stress."),
        ("Small-business formation slowdown. ",
         "Fewer new businesses means a thinner top-of-funnel for QuickBooks."),
        ("Mailchimp underperformance. ",
         "Continued deterioration would force a writedown of the strategic rationale and management credibility."),
        ("Regulatory scrutiny. ",
         "Data privacy and fintech regulation could constrain cross-product data use, dulling the platform advantage."),
        ("Valuation sensitivity. ",
         "The shares have historically traded at premium multiples; multiple compression on any growth "
         "scare is a real drawdown risk."),
    ],
    "falsification": (
        "Downgrade on: two consecutive tax seasons of TurboTax paid-unit declines not explained by "
        "demographics, signaling franchise erosion; sustained QuickBooks subscriber churn elevation or net "
        "revenue retention decline in the small-business segment; evidence that AI-native tax or bookkeeping "
        "products are winning Intuit's core customers at scale; a major data breach or regulatory action "
        "restricting Intuit's use of cross-product financial data; or capital allocation drift — a large "
        "dilutive acquisition or a buyback halt while the shares are depressed."
    ),
    "charts": {
        "scenario": {"bear": 220.00, "base": 529.00, "bull": 862.00,
                     "weighted": 535.00, "price": 281.08},
        "trajectory": {
            "years_hist": [2023, 2024, 2025, 2026],
            "revenue_hist": [14.368, 16.285, 18.831, 21.448],
            "fcf_hist": [4.786, 4.634, 6.083, 8.617],
            "years_proj": [2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": [22.91, 24.46, 26.13, 27.90, 29.80, 31.83, 33.99, 36.30, 38.77, 41.41],
            "fcf_proj": [9.16, 9.79, 10.45, 11.16, 11.92, 12.73, 13.60, 14.52, 15.51, 16.56],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via Yahoo Finance (fiscal years ending July). Projections: "
                    "base-case revenue at the scenario's 6.8% 10-yr CAGR to the model's 2036 endpoint "
                    "($41.41 bn), with FCF at ~40% of revenue.",
        },
        "composition": {
            "bear": {"pv_explicit": 147.56, "pv_terminal": 72.44},
            "base": {"pv_explicit": 236.20, "pv_terminal": 292.80},
            "bull": {"pv_explicit": 300.24, "pv_terminal": 561.76},
            "unit": "$/sh",
        },
        "extra": {
            "type": "pie",
            "title": "FY2025 revenue mix (~)",
            "labels": ["Small Business & SE", "Consumer", "Credit Karma", "ProTax"],
            "values": [59, 26, 11, 4],
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "INTU-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
