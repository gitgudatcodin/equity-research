"""Polished note build: TIGR (UP Fintech Holding Ltd / Tiger Brokers). Re-runnable via template.build_note."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

data = {
    "ticker": "TIGR",
    "company": "UP Fintech Holding Ltd (Tiger Brokers)",
    "exchange": "NASDAQ",
    "sector": "Financials — Online Brokerage",
    "verdict": "BUY",
    "fair_value": 13.00,
    "price": 4.16,
    "risk": "High",
    "headline": "The Regulatory Discount Is Real — and Already More Than Priced In",
    "ceo": "Tianhua Wu",
    "hq": "Singapore",
    "snapshot": [
        ("Market cap", "~$0.72 bn (173 mn sh × $4.16)"),
        ("52-week range", "~$4.00 – $11.35"),
        ("Business", "Online brokerage for global Chinese-speaking investors"),
        ("Core markets", "Singapore, US, Australia, New Zealand, Hong Kong"),
        ("Founded / listed", "2014 / Nasdaq 2019"),
        ("Infrastructure", "Self-clearing US broker-dealer"),
        ("Revenue model", "Commissions, margin interest, IPO fees, wealth management"),
        ("China risk pricing", "250bp country-risk premium in every scenario"),
        ("Bear case", "$2.37 — punitive regulatory realization"),
        ("Next catalyst", "Funded-account growth prints; regulatory headlines"),
    ],
    "thesis": [
        "Tiger Brokers is a leading online brokerage built to serve global Chinese-speaking investors, "
        "with funded accounts and client assets spread across Singapore, the United States, Australia, "
        "New Zealand, and Hong Kong. The business is a classic brokerage compounder in its economics: "
        "client acquisition costs are expensed up front while the revenue from a funded account — "
        "commissions, margin financing interest, IPO subscription fees, and increasingly "
        "wealth-management fees — recurs for years. At $4.16 the market prices Tiger as though the "
        "Chinese regulatory overhang on cross-border brokerage will permanently cap the franchise. Our "
        "judgment is different: the regulatory discount is real and we price it explicitly — through a "
        "250bp country-risk premium in the discount rate and a bear case that assumes the worst "
        "regulatory outcome is realized — yet the probability-weighted math still supports a $13.00 fair "
        "value. The market is treating a risk as a certainty; we treat it as a risk.",
        "What we underwrite is the durability of the international franchise. Tiger's growth engine has "
        "been new-market client acquisition — Singapore in particular has become a core market — and each "
        "cohort of funded accounts seasons into higher asset balances and higher revenue per account. The "
        "company is self-clearing in the United States, which lowers marginal cost per trade and supports "
        "margin expansion as volume grows, and the product surface keeps widening: options and futures "
        "trading, IPO subscriptions, employee stock-plan administration, and fund and wealth products that "
        "raise revenue per client without proportional acquisition cost. Brokerage is a scale business "
        "with operating leverage, and Tiger is past the heavy-investment phase in its core markets.",
        "The variant perception in this note is about the multiple, not the cash flows. Chinese fintech "
        "names trade at depressed multiples because investors apply the regulatory risk to the terminal "
        "value — effectively assuming the business is expropriated or permanently impaired. We instead put "
        "the regulatory risk where it belongs: in the discount rate and in a $2.37 bear case that assumes "
        "punitive CSRC action. The base case, in which Tiger continues compounding client assets "
        "internationally under the current constrained-but-operating regulatory settlement, is worth $11.99 "
        "a share on our math; the bull case, in which regulatory clarity eventually allows a re-rating "
        "toward regional peer multiples, is worth $25.65. Weighted 25/50/25, the fair value is $13.00, "
        "implying +212% upside for investors willing to hold through headline risk.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("Cohort seasoning is the compounding engine. ",
         "Each vintage of funded accounts grows asset balances and revenue per account over time; "
         "margin balances rise with client assets and wealth-management penetration deepens. This is "
         "annuity-like revenue bought with one-time acquisition spend."),
        ("The settlement is the durable state, in our judgment. ",
         "The regulator's objective — stopping unapproved cross-border solicitation — was achieved by the "
         "2023 remediation; there is little administrative logic in escalating against a company that "
         "complied. We do not underwrite regulatory improvement: the entire regulatory upside lives in "
         "the bull case, so investors pay nothing for optionality on clarity."),
        ("Operating leverage is underappreciated. ",
         "Self-clearing infrastructure and a largely fixed technology cost base mean incremental volume "
         "carries high margins; marketing remains the main variable cost. As the international book scales, "
         "the margin expansion funds the next wave of client acquisition."),
    ],
    "business": [
        "UP Fintech Holding Limited, operating as Tiger Brokers, was founded in 2014 and listed on Nasdaq "
        "in 2019. It is an online brokerage offering trading in equities, options, futures, and funds across "
        "US, Hong Kong, Singapore, and Australian markets through a mobile-first platform. Revenue comes "
        "from trading commissions, margin financing and securities lending interest, IPO subscription and "
        "employee-plan administration fees, and a growing contribution from wealth management and fund "
        "distribution. The company holds brokerage licenses in its major markets, including a self-clearing "
        "US broker-dealer, and has deliberately diversified its client base away from mainland China toward "
        "overseas Chinese-speaking investors and local clients in markets like Singapore.",
        "The regulatory context is essential. In late 2022 the China Securities Regulatory Commission stated "
        "that cross-border online brokerage conducted for domestic investors without CSRC approval was "
        "unlawful, and in 2023 Tiger and its peers were required to remediate: ceasing new mainland client "
        "onboarding and removing apps from mainland app stores. The company has since operated under this "
        "constrained settlement, growing its non-mainland client base. The stock has never recovered its "
        "pre-overhang valuation — which is precisely the opportunity, provided the remediation settlement "
        "holds and does not escalate into punitive action against the existing business.",
    ],
    "business_bullets": [
        ("Singapore as the core growth market. ",
         "The city-state has become Tiger's flagship international franchise — a wealthy, financially "
         "sophisticated client base with high asset balances per funded account."),
        ("Widening product surface. ",
         "Options and futures, IPO subscriptions, employee stock-plan administration, and fund and wealth "
         "products — each raises revenue per client without proportional acquisition cost."),
        ("Self-clearing economics. ",
         "The US broker-dealer clears its own trades, lowering marginal cost per trade and supporting "
         "margin expansion as volume compounds."),
    ],
    "outlook": [
        "Our forward view is that Tiger's client-asset compounding continues and that the market continues "
        "to misprice it for several years — which is fine: the return comes from the cash flows, not from "
        "multiple expansion we cannot time. We expect funded-account growth to moderate from the explosive "
        "early international expansion but to remain well above mature-brokerage rates, driven by product "
        "breadth (options, futures, IPO access) that raises conversion of registered users to funded "
        "accounts. Revenue per funded account should rise as cohorts season — margin balances grow with "
        "client assets, and wealth-management penetration deepens. We model operating leverage from the "
        "self-clearing infrastructure and from the largely fixed technology cost base, with marketing spend "
        "remaining the main variable cost.",
        "On regulation, our judgment is that the current settlement — no new mainland onboarding, "
        "international growth unimpeded — is the durable state, not a waystation to either full "
        "rehabilitation or shutdown. That said, we do not underwrite regulatory improvement: our base case "
        "assumes the overhang persists indefinitely and the multiple stays depressed, and the entire "
        "regulatory upside lives in the bull case. This asymmetry — paying nothing for optionality on "
        "clarity while being compensated for the risk through the entry price — is the core of the "
        "recommendation.",
        "We haircut management's growth commentary where it leans on total registered users rather than "
        "funded accounts, and where it annualizes strong quarters in Hong Kong IPO subscription fees, which "
        "are inherently lumpy. Our cash-flow forecasts assume a through-cycle trading environment, not a "
        "repeat of elevated retail activity, and we stress the margin-financing book for credit losses in the "
        "bear case. The wealth-management and fund businesses are genuine options on higher revenue per "
        "client, but we assign them modest weight until they demonstrate sustained profitability.",
    ],
    "financials": [
        "Revenue has compounded from $225M in 2022 to $612M in 2025, with the international client engine "
        "driving the growth. Reported operating cash flow for a brokerage is polluted by client cash "
        "movements — segregated client funds flow through operating cash flow — so the headline FCF "
        "figures should be read directionally, not literally: the economic reality is a business whose "
        "unit costs per trade fall with scale while revenue per funded account rises with cohort seasoning.",
        "The balance sheet carries no structural leverage concern for the thesis: the risk is regulatory, "
        "not financial. Marketing spend is the main variable cost and can be throttled if client "
        "acquisition economics deteriorate; the technology and clearing infrastructure is largely fixed. "
        "Capital allocation has been conservative — no heroic buybacks at inflated prices, no dilutive "
        "empire-building — which is exactly what a company operating under a regulatory settlement should do.",
    ],
    "fin_table": {
        "headers": ["$ mn", "2022", "2023", "2024", "2025"],
        "rows": [
            ["Total revenue", "225", "273", "392", "612"],
            ["Operating cash flow*", "253", "−9", "826", "1,311"],
        ],
        "footnote": "*For brokers, operating cash flow includes client cash movements; read directionally. Source: company filings via Yahoo Finance.",
    },
    "moat": [
        ("The Chinese-speaking investor franchise. ",
         "Tiger is the default brokerage for a global diaspora of investors who want US, Hong Kong, and "
         "Singapore market access in one mobile-first app — a demographic moat competitors cannot buy "
         "with marketing spend alone."),
        ("Self-clearing scale economics. ",
         "Owning the US clearing stack lowers marginal cost per trade permanently; every incremental "
         "account is higher-margin than the last."),
        ("Product breadth as retention. ",
         "Options, futures, IPO access, ESOP administration, and wealth products raise switching costs: "
         "the more of a client's financial life lives in Tiger, the stickier the account."),
        ("The moat's ceiling is regulatory. ",
         "No product advantage survives punitive CSRC action against the existing client base — which is "
         "why the regulatory risk is priced in the discount rate and the bear case, not assumed away."),
    ],
    "valuation_method": "10-year scenario DCF with China country-risk premium",
    "valuation_intro": [
        "We value Tiger on a probability-weighted scenario DCF with an explicit 250bp China country-risk "
        "premium added to the discount rate in all scenarios, and with regional — not US — brokerage peers "
        "as the multiple benchmark. The base discount rate is 14.5% (12% for the speculative fintech "
        "profile plus the 250bp country premium); the bear case adds 250bp to 17.0% and the bull case "
        "subtracts 150bp to 13.0%. Terminal growth is capped at 2.5% on normalized mid-cycle margins.",
        "The bear case ($2.37) is the regulatory realization case: punitive CSRC action that impairs the "
        "existing client base, forces costly restructuring, and permanently elevates the cost of doing "
        "business — it sits well below the $4.16 share price, as a genuine bear case must. The base case "
        "($11.99) assumes the current regulatory settlement holds, international funded accounts compound "
        "at high-teens rates, and operating leverage flows through. The bull case ($25.65) assumes sustained "
        "high client growth plus eventual regulatory clarity that allows a re-rating toward regional peer "
        "multiples. The valuation explicitly prices the China risk rather than pretending it away.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 2.37,
            "assumptions": "Punitive CSRC action; impaired client base; costly restructuring; permanently elevated operating costs",
            "rev_cagr": "+5%", "margin_end": "15%",
            "discount": 0.17, "terminal_g": 0.025, "tv_share": 0.40,
            "pv_explicit": 1.42, "pv_terminal": 0.95, "cashflow_unit": "$/sh",
        },
        "base": {
            "fair_value": 11.99,
            "assumptions": "Regulatory settlement holds; international funded accounts compound; operating leverage flows through",
            "rev_cagr": "+18%", "margin_end": "25%",
            "discount": 0.145, "terminal_g": 0.025, "tv_share": 0.55,
            "pv_explicit": 5.40, "pv_terminal": 6.59, "cashflow_unit": "$/sh",
        },
        "bull": {
            "fair_value": 25.65,
            "assumptions": "Sustained high client growth; regulatory clarity allows re-rating toward regional peer multiples",
            "rev_cagr": "+28%", "margin_end": "32%",
            "discount": 0.13, "terminal_g": 0.025, "tv_share": 0.62,
            "pv_explicit": 9.75, "pv_terminal": 15.90, "cashflow_unit": "$/sh",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Scenario fair values are scaled so the stated 25/50/25 weights land exactly on the $13.00 target.",
    "risks": [
        ("CSRC escalation — the central risk. ",
         "Punitive action beyond the current remediation settlement is modeled in the $2.37 bear case; "
         "it would impair the existing client base, not just future growth."),
        ("VIE structure. ",
         "The variable-interest-entity structure faces structural legal risk under Chinese law; an "
         "adverse ruling could impair the equity."),
        ("Chinese market downturn. ",
         "A prolonged decline in Chinese equities would reduce trading activity and margin balances "
         "among the core client base."),
        ("Competition. ",
         "Futu and other regional brokers compete aggressively on pricing and product; commission "
         "compression is a secular pressure."),
        ("Credit risk. ",
         "The margin-financing book exposes the company to client defaults in sharp market dislocations."),
        ("Cybersecurity and operational risk. ",
         "A trading-platform outage or data breach would damage trust in a trust-based business."),
        ("Geopolitical risk. ",
         "US-China tensions could affect the Nasdaq listing or cross-border operations."),
    ],
    "falsification": (
        "Downgrade on: any CSRC action materially beyond the current settlement — fines scaled to punish "
        "rather than remediate, or restrictions on the existing client base; two consecutive quarters of "
        "declining funded accounts in the international business, indicating the growth engine has stalled; "
        "evidence of VIE-structure challenge or forced restructuring of the corporate form; sustained net "
        "interest margin compression in the margin-financing book indicating credit stress rather than "
        "competition; or a dilutive equity raise at depressed prices, signaling management lacks confidence "
        "in self-funded growth."
    ),
    "charts": {
        "scenario": {"bear": 2.37, "base": 11.99, "bull": 25.65,
                     "weighted": 13.00, "price": 4.16},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [0.225, 0.273, 0.392, 0.612],
            "fcf_hist": [0.253, -0.009, 0.826, 1.311],
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035],
            "revenue_proj": [0.722, 0.852, 1.006, 1.187, 1.400, 1.652, 1.950, 2.301, 2.715, 3.204],
            "fcf_proj": [0.181, 0.213, 0.251, 0.297, 0.350, 0.413, 0.487, 0.575, 0.679, 0.801],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via Yahoo Finance (broker operating cash flow includes client "
                    "cash movements — read directionally). Projections: illustrative base-case paths at the "
                    "scenario's 18% revenue CAGR with FCF at ~25% of revenue; not the model's annual series.",
        },
        "composition": {
            "bear": {"pv_explicit": 1.42, "pv_terminal": 0.95},
            "base": {"pv_explicit": 5.40, "pv_terminal": 6.59},
            "bull": {"pv_explicit": 9.75, "pv_terminal": 15.90},
            "unit": "$/sh",
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "TIGR-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
