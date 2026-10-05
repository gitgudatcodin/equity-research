"""Polished note build: PayPal Holdings, Inc. (PYPL) — BUY, $90.00 target."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note, validate

data = {
    "ticker": "PYPL",
    "company": "PayPal Holdings, Inc.",
    "exchange": "NASDAQ",
    "sector": "Financials — Digital Payments",
    "verdict": "BUY",
    "fair_value": 90.00,
    "price": 52.80,
    "risk": "High",
    "headline": "Priced as a Melting Ice Cube; Valued as a Two-Sided Network",
    "ceo": "Alex Chriss",
    "hq": "San Jose, California",
    "snapshot": [
        ("Market cap", "~$45.2 bn (~855 mn sh × $52.80)"),
        ("Price (Oct 2, 2026)", "$52.80"),
        ("52-week range", "~$38.46 – $79.22"),
        ("TTM free cash flow", "~$5.6 bn (~10-12% FCF yield)"),
        ("Owner FCF multiple", "~9× (after ~$1B+/yr stock comp)"),
        ("Net cash", "~$0.3 bn (cash + investments ≈ debt; no leverage wall)"),
        ("Active accounts", "400 mn+ consumers; tens of millions of merchants"),
        ("Share count", "Falling sharply — buybacks retiring stock at single-digit multiples"),
        ("Next catalyst", "Q3 2026 earnings; Fastlane merchant adoption; Venmo monetization prints"),
    ],
    "thesis": [
        "PayPal is priced as a melting ice cube and valued as one of the great two-sided payment "
        "networks ever built — and only one of those can be right. The branded PayPal checkout "
        "button remains the highest-converting payment method in e-commerce: merchants accept "
        "it because consumers trust it, and consumers use it because merchants accept it. That "
        "flywheel, built over two decades across more than 400 million active accounts and tens "
        "of millions of merchants, does not evaporate because Apple Pay exists. At $52.80 the "
        "market is capitalizing a permanent decline in the branded business that the transaction "
        "data simply does not show: branded checkout volumes keep growing, take rates are "
        "stabilizing, and the margin structure is inflecting as new products shift the mix back "
        "toward higher-value flows.",
        "The second pillar is the turnaround under CEO Alex Chriss, which is further along than "
        "the stock price suggests. The company has refocused on its core checkout and payments "
        "strength, launched Fastlane — a one-click guest checkout that materially lifts "
        "conversion for merchants — and begun to monetize Venmo in earnest after years of "
        "leaving money on the table. Operating margins are expanding as the company rationalizes "
        "costs and as higher-margin branded volume outgrows the lower-margin Braintree "
        "processing business. This is the classic setup: a hated turnaround where the numbers "
        "turn before the narrative does.",
        "The third pillar is capital return. PayPal generates enormous free cash flow, and with "
        "the shares trading at a mid-teens multiple of earnings, every dollar of buybacks "
        "retires stock at prices that will look absurd in hindsight if the business merely "
        "stabilizes. The combination of mid-single-digit revenue growth, margin expansion of "
        "several hundred basis points, and a shrinking share count is a powerful earnings-per-"
        "share compounding formula that requires no heroic assumptions about market-share gains.",
        "Our $90.00 fair value assumes PayPal is a low-growth compounder, not a high-growth "
        "disruptor — and the current price does not even grant it that. The risk-reward is "
        "skewed because the downside case (continued share erosion, fee compression) is fully "
        "priced while the base case — stable branded checkout, Venmo monetization, Fastlane "
        "adoption, agentic-commerce optionality — is priced at roughly zero probability. We see "
        "+71% upside to fair value with a downside cushion from the buyback and the cash "
        "generation. The rating is BUY.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("Conversion is what merchants pay for. ",
         "The relevant question is not whether alternative payment methods exist — they do — "
         "but whether PayPal's branded button keeps converting better than the alternatives. "
         "Fastlane's early merchant results show meaningful conversion lifts, and the branded "
         "take rate has stabilized as the company prices for the value it delivers."),
        ("Venmo is a free call option inside the company. ",
         "Tens of millions of monthly active users who skew young and digitally native; even "
         "modest progress in monetization — debit-card interchange, pay-with-Venmo at checkout, "
         "instant-transfer fees — drops almost entirely to the bottom line. The market assigns "
         "it little value."),
        ("The bear case cannot get 20% below the quote. ",
         "We charge branded erosion, 400bp of margin compression, and a 12.5% discount rate in "
         "the bear case and still get $43.43 — 18% below $52.80, not a collapse. The asymmetry "
         "is the whole case."),
    ],
    "business": [
        "PayPal Holdings, headquartered in San Jose, California, is one of the world's largest "
        "digital payment platforms. Its core is the branded checkout business: the PayPal button "
        "and digital wallet that consumers use to pay online, in-app, and increasingly in-store. "
        "Around that core sit Venmo, the leading US peer-to-peer payment app with a large and "
        "young user base; Braintree, the full-stack payment processor that powers unbranded card "
        "processing for large merchants and platforms; and smaller businesses including Xoom "
        "(remittances) and merchant lending products.",
        "The economics differ by product. Branded checkout carries the highest take rate and "
        "margin: PayPal earns a percentage of each transaction plus a fixed fee, with minimal "
        "incremental cost per transaction. Braintree is a scale processing business with much "
        "thinner margins but large volume. Venmo monetization — through instant transfers, the "
        "Venmo debit card, and merchant payments — has been the long-awaited second act. The "
        "company's moat is its two-sided network: consumer trust and merchant acceptance "
        "reinforce each other, and the data across hundreds of billions of transactions improves "
        "risk management and authorization rates in ways new entrants cannot quickly replicate.",
        "PayPal processes trillions of dollars in total payment volume annually. It is a "
        "capital-light business that converts a high share of operating profit into free cash "
        "flow, which management has directed toward share repurchases and disciplined "
        "reinvestment in checkout innovation such as Fastlane and AI-driven shopping "
        "experiences.",
    ],
    "outlook": [
        "Our judgment is that PayPal's next chapter will be written in checkout conversion, not "
        "in winning a war against Apple Pay. Every data point we have says the branded button "
        "keeps converting better than the alternatives, because conversion is what merchants pay "
        "for. We expect branded checkout to keep growing at a healthy clip while Braintree "
        "provides volume scale at thinner margins — a mix that, on balance, supports margin "
        "expansion as the higher-value lines grow faster.",
        "Venmo is the underappreciated call option. With tens of millions of monthly active "
        "users who skew young and digitally native, even modest progress in monetization drops "
        "almost entirely to the bottom line. We expect Venmo's revenue contribution to become "
        "material to the growth algorithm over the next three years, and the market currently "
        "assigns it little value.",
        "Longer term, agentic commerce — AI agents that shop on consumers' behalf — could be "
        "either a threat or an enormous opportunity for PayPal, and we lean toward opportunity: "
        "whoever owns the trusted payment credential inside the agent's wallet owns the "
        "transaction. PayPal's two-sided network and risk infrastructure position it well for "
        "that world. We do not need that thesis to work for the $90 target; it is upside. What "
        "we need is operational steadiness: mid-single-digit revenue growth, a few hundred "
        "basis points of margin expansion, and aggressive buybacks. That is a low bar for a "
        "business of this quality.",
    ],
    "financials": [
        "Cash generation and buybacks create a valuation floor. TTM free cash flow of roughly "
        "$5.6 billion against a ~$45 billion market cap is a double-digit FCF yield — and owner "
        "free cash flow, after the roughly $1 billion-plus annual stock-compensation charge, "
        "still prices the equity at about 9×. The share count has fallen sharply as buybacks "
        "retire stock at single-digit multiples. That compounding only adds value while the "
        "franchise remains durable — which is exactly what our downgrade triggers police.",
        "The balance sheet (mid-2026): cash plus short-term investments and available-for-sale "
        "securities roughly offset total debt of about $13.4 billion, leaving near-zero net cash. "
        "Near-cash, not a war chest — but no leverage forcing the company's hand, and no "
        "refinancing wall in the thesis window. Revenue has compounded steadily ($27.5 billion "
        "in 2022 to $33.2 billion in 2025) while the mix shifts toward higher-margin branded "
        "flows, which is the mechanical driver of the margin expansion in our scenarios.",
    ],
    "fin_table": {
        "headers": ["$ bn", "2022", "2023", "2024", "2025"],
        "rows": [
            ["Total revenue", "27.52", "29.77", "31.80", "33.17"],
            ["YoY growth", "—", "+8.2%", "+6.8%", "+4.3%"],
            ["Operating cash flow", "5.81", "4.84", "7.45", "6.42"],
            ["Free cash flow", "5.11", "4.22", "6.77", "5.56"],
            ["Owner FCF (less SBC)", "~4.0", "~3.1", "~5.7", "~4.5"],
        ],
        "footnote": "Sources: company filings via Yahoo Finance (annual). Owner FCF deducts ~$1B+/yr stock-based compensation — the cash shareholders can actually spend.",
    },
    "moat": [
        ("The two-sided network is the moat. ",
         "Consumer trust and merchant acceptance reinforce each other across 400 million-plus "
         "accounts; the data across hundreds of billions of transactions improves authorization "
         "rates and risk management in ways new entrants cannot quickly replicate."),
        ("The branded button converts best. ",
         "Highest-converting checkout method in e-commerce — that conversion is what merchants "
         "pay for, and it is the source of the take-rate premium over unbranded processing."),
        ("Venmo's social graph. ",
         "The leading US P2P app with a young, digitally native user base — a distribution "
         "asset for the next wave of monetization that competitors cannot easily clone."),
        ("Scale in risk infrastructure. ",
         "Two decades of fraud and credit data across global corridors; agentic commerce will "
         "reward whoever owns the trusted credential, and PayPal is positioned for that world."),
        ("The moat's weak link: the button is optional. ",
         "Apple Pay, Google Pay, Stripe, Adyen, and buy-now-pay-later keep attacking the "
         "checkout; the moat holds only as long as conversion superiority does — which is why "
         "branded volume is our downgrade tripwire."),
    ],
    "valuation_method": "10-year scenario DCF on owner free cash flow (after stock comp)",
    "valuation_intro": [
        "We value PayPal on a 10-year scenario DCF at the firm level on owner free cash flow — "
        "free cash flow after deducting stock-based compensation, the only number shareholders "
        "can spend — weighted bear 25% / base 50% / bull 25%, with scenario-specific discounts: "
        "bear 12.5% (base + 250bp: branded erosion, margin compression), base 10.0% (standard "
        "tier: branded share loss, mix pressure, execution risk), bull 8.5% (base − 150bp). "
        "Terminal growth is 1.0% / 2.0% / 2.5% on normalized mid-cycle owner-FCF margins "
        "(11% / 15% / 16.5%), and the terminal value is 31–61% of enterprise value. Buybacks "
        "are not modeled as accretion (that would be circular); the share count is held at 855 "
        "million, which is conservative given the retirement pace.",
        "In the base case, revenue grows at 3.4% (2027–36) to $48.3 billion as branded checkout "
        "growth and Venmo monetization offset the dilutive mix of Braintree volume; operating "
        "margins expand toward the mid-20s as turnaround cost discipline holds and "
        "higher-margin products outgrow processing; and owner FCF per share grows faster than "
        "revenue as buybacks shrink the share count. The bear case ($43.43) is genuinely adverse "
        "and sits below the current price: branded share erodes structurally to wallets and "
        "buy-now-pay-later, regulators compress interchange economics, and the turnaround "
        "stalls. The bull case ($144.26) assumes Fastlane becomes the default guest checkout "
        "across large merchants, Venmo monetization inflects, and PayPal captures a meaningful "
        "share of agentic-commerce payment flows. A cross-check on multiples supports the "
        "conclusion: at $52.80 the shares trade at a multiple of forward earnings more "
        "appropriate to a no-growth melting business, while the owner-FCF yield is in the high "
        "single digits. For a capital-light network business with this return profile, that "
        "pricing implies a future the fundamentals do not support.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 43.43,
            "assumptions": "Branded checkout share erodes structurally to wallets and BNPL; regulators compress interchange; turnaround stalls; 400bp margin compression",
            "rev_cagr": "+1.0%", "margin_end": "11%",
            "discount": 0.125, "terminal_g": 0.01, "tv_share": 0.31,
            "pv_explicit": 25624, "pv_terminal": 11508, "cashflow_unit": "$mn",
        },
        "base": {
            "fair_value": 86.07,
            "assumptions": "3.4% revenue compounding; owner-FCF margins recover to 15%; branded growth + Venmo monetization offset Braintree mix; buybacks continue",
            "rev_cagr": "+3.4%", "margin_end": "15%",
            "discount": 0.10, "terminal_g": 0.02, "tv_share": 0.46,
            "pv_explicit": 39739, "pv_terminal": 33853, "cashflow_unit": "$mn",
        },
        "bull": {
            "fair_value": 144.26,
            "assumptions": "Fastlane becomes default guest checkout at large merchants; Venmo monetization inflects; PayPal captures agentic-commerce payment flows",
            "rev_cagr": "+5.7%", "margin_end": "16.5%",
            "discount": 0.085, "terminal_g": 0.025, "tv_share": 0.61,
            "pv_explicit": 48103, "pv_terminal": 75240, "cashflow_unit": "$mn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Scenario fair values are per-share equity values from the owner-FCF DCF (855 mn shares). 0.25×$43.43 + 0.50×$86.07 + 0.25×$144.26 ≈ $90.00.",
    "risks": [
        ("Competitive pressure. ",
         "Apple Pay, Google Pay, Stripe, Adyen, and buy-now-pay-later providers could erode "
         "branded checkout share or compress take rates."),
        ("Regulatory risk. ",
         "Interchange-fee rules, digital-wallet regulation, and data-privacy regimes could "
         "reduce monetization across the platform."),
        ("Execution risk. ",
         "The turnaround depends on continued product innovation (Fastlane, Venmo "
         "monetization) and cost discipline under current leadership."),
        ("Credit exposure. ",
         "Buy-now-pay-later and merchant lending could produce losses in a consumer downturn."),
        ("Technological disruption. ",
         "Shifts in how consumers pay — including agentic AI commerce — could bypass "
         "traditional checkout flows if PayPal fails to embed itself in new interfaces."),
    ],
    "falsification": (
        "Downgrade to HOLD on: two consecutive quarters of declining branded-checkout payment "
        "volume — the network flywheel breaking would invalidate the core thesis; a sustained "
        "decline in take rate not explained by mix shift, indicating pricing power has been lost; "
        "operating-margin contraction resuming after the turnaround gains, suggesting cost "
        "discipline was temporary; Venmo monthly active users declining or monetization per user "
        "stalling for a full year; or a large dilutive acquisition that diverts capital from "
        "buybacks into empire-building. We watch: branded TPV, take rate net of mix, Fastlane "
        "merchant adoption, and Venmo monetization per user."
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
        "independently tested and haircut where evidence warrants. For PayPal the scenario cash "
        "flows are owner free cash flow — after stock-based compensation — because that is the "
        "cash shareholders can actually spend.",
    ],
    "charts": {
        "scenario": {"bear": 43.43, "base": 86.07, "bull": 144.26,
                     "weighted": 90.00, "price": 52.80},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [27.518, 29.771, 31.797, 33.172],
            "fcf_hist": [4.01, 3.12, 5.67, 4.46],
            "years_proj": [2026, 2027, 2028, 2029, 2030],
            "revenue_proj": [34.30, 35.47, 36.67, 37.92, 39.21],
            "fcf_proj": [5.90, 6.20, 6.52, 6.85, 7.20],
            "unit": "$bn", "fcf_label": "Owner FCF",
            "note": "History: company filings via Yahoo Finance; FCF less ~$1B+/yr "
                    "stock-based compensation = owner FCF. Projections: base-case owner "
                    "FCF from the scenario DCF.",
        },
        "composition": {
            "bear": {"pv_explicit": 25624, "pv_terminal": 11508},
            "base": {"pv_explicit": 39739, "pv_terminal": 33853},
            "bull": {"pv_explicit": 48103, "pv_terminal": 75240},
            "unit": "$mn",
        },
        "extra": {
            "type": "line",
            "title": "2036 revenue by scenario — the compounding range ($bn)",
            "years": [2026, 2036],
            "series": [
                {"label": "Bear", "values": [34.3, 38.1]},
                {"label": "Base", "values": [34.3, 48.3]},
                {"label": "Bull", "values": [34.3, 60.3]},
            ],
            "ylabel": "$bn",
        },
    },
}

validate(data)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "PYPL-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
