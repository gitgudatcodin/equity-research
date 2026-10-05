"""Polished note build: T-Mobile US (TMUS). Scenario numbers from the valuation model
(valuation_output_v2.json): bear $50.30 / base $216.30 / bull $338.20, weighted $205. Re-runnable."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

# Base-case path from the model: 2026E revenue $92.0B, growth path and FCF margins (2027-2036)
G = [5.5, 5.0, 4.5, 4.0, 3.5, 3.0, 2.8, 2.5, 2.2, 2.0]
M = [19.8, 20.0, 20.2, 20.4, 20.6, 20.7, 20.8, 20.9, 21.0, 21.0]
rev_proj = [92.0]
for g in G:
    rev_proj.append(round(rev_proj[-1] * (1 + g / 100), 2))
fcf_proj = [round(r * m / 100, 2) for r, m in zip(rev_proj[1:], M)]
fcf_proj = [18.0] + fcf_proj  # 2026E FCF $18.0B

data = {
    "ticker": "TMUS",
    "company": "T-Mobile US, Inc.",
    "exchange": "NASDAQ",
    "sector": "Communication Services — Wireless Telecom",
    "verdict": "BUY",
    "fair_value": 205.00,
    "price": 163.64,
    "risk": "Medium",
    "headline": "The Best-Run US Wireless Carrier, Compounding Through Buybacks",
    "snapshot": [
        ("Market cap", "~$175.5 bn (1.073 bn sh × $163.64)"),
        ("52-week range", "~$160.81 – $231.02"),
        ("Position", "#2 US wireless carrier by subscribers"),
        ("Network", "Deepest mid-band (2.5 GHz) 5G spectrum post-Sprint"),
        ("Churn", "Industry's lowest"),
        ("2026E revenue / FCF", "$92.0 bn / $18.0 bn (model inputs)"),
        ("Net debt", "~$83.5 bn (merger-era, declining)"),
        ("Capital return", "Buybacks retiring high-single-digit % of shares in peak years + dividend"),
        ("Growth vector", "Fixed-wireless home internet at high incremental margins"),
        ("Implied upside", "+25% to $205.00 fair value"),
    ],
    "thesis": [
        "T-Mobile is the best-run wireless carrier in the United States, and it is not close. The Sprint "
        "merger delivered the spectrum depth that now underwrites the industry's best 5G network; "
        "postpaid subscriber growth has led the industry for years; and the synergy realization is "
        "largely complete, which means the earnings story from here is straightforward operating "
        "leverage plus capital return. The market treats wireless as a zero-sum share-shift game; "
        "T-Mobile is the company doing the shifting.",
        "Our judgment is that the next leg of the story is the convergence of subscriber growth, ARPU "
        "stability, and a buyback program funded by prodigious free cash flow. T-Mobile's network "
        "advantage is durable because mid-band spectrum cannot be quickly replicated, and the company's "
        "brand and value positioning keep churn the lowest in the industry. We tested the growth "
        "assumptions against demographic and household-formation data rather than extrapolating the "
        "Sprint-era surge; even normalized, the subscriber trajectory supports the valuation.",
        "At $163.64, the valuation implies the growth premium fades quickly. Our probability-weighted "
        "fair value is $205.00, a 25% expected return, earned through continued subscriber gains, margin "
        "expansion, and one of the most aggressive buyback programs in large-cap telecom. The bear case "
        "— stalled subscriber growth and promotional pressure — is genuinely adverse and sits well below "
        "today's price.",
        "Fixed wireless is the growth vector the market still undervalues. Home internet over the 5G "
        "network monetizes excess capacity at very high incremental margins, and T-Mobile has scaled it "
        "to millions of subscribers faster than skeptics expected. The addressable market is large, the "
        "product keeps improving with network densification, and each subscriber adds revenue with "
        "minimal incremental cost.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("The spectrum advantage is physics, not marketing. ",
         "Mid-band holdings deliver a combination of speed and coverage that competitors cannot match "
         "without years of additional investment. Network quality is the primary driver of both gross "
         "additions and churn — and independent speed tests have consistently ranked T-Mobile first."),
        ("Operating leverage plus buybacks is the compounding formula. ",
         "Mid-single-digit service revenue growth against a largely fixed cost base, EBITDA margins "
         "expanding as the base scales, and the share count shrinking several percent per year. It is a "
         "compounding story, not a transformation story."),
        ("Underpenetrated segments extend the runway. ",
         "Smaller markets and rural coverage (where spectrum depth now allows credible competition), "
         "business and government accounts, and fixed wireless — the switcher pool in these segments "
         "is large and the share gains are still early."),
    ],
    "business": [
        "T-Mobile US is the second-largest wireless carrier in the United States by subscribers, "
        "offering postpaid, prepaid (Metro), and wholesale wireless services, plus a fast-growing "
        "fixed-wireless home internet business. The 2020 acquisition of Sprint gave T-Mobile a deep "
        "mid-band spectrum portfolio (2.5 GHz) that powers its 5G network, widely regarded as the "
        "fastest and most extensive in the country.",
        "The economics are those of a scale telecom: high fixed costs, very low marginal cost per "
        "subscriber, and therefore powerful operating leverage as the base grows. Churn is the key "
        "operating metric, and T-Mobile's is the industry's lowest. Free cash flow, now that merger "
        "integration spending is behind, funds dividends and large buybacks.",
        "Postpaid phone is the core: the highest-value subscriber segment, where T-Mobile has led the "
        "industry in net additions for years. The value positioning — premium network at a discount to "
        "AT&T and Verizon pricing — continues to pull switchers, and the business-account segment, "
        "historically underpenetrated, is now a deliberate growth focus. Prepaid (Metro) and wholesale "
        "add scale without proportional cost.",
    ],
    "business_bullets": [
        ("Postpaid: the share-gain engine. ",
         "Industry-leading net additions for years; value positioning keeps pulling switchers from the "
         "two larger carriers."),
        ("Fixed wireless: monetizing excess capacity. ",
         "Home internet over 5G at very high incremental margins, scaled to millions of subscribers; "
         "the product improves as the network densifies."),
        ("Enterprise optionality. ",
         "Network slicing and standalone 5G open private-network, IoT, and low-latency use cases at "
         "higher ARPU — not underwritten in the base case, but lengthening the growth duration."),
        ("The capital-return machine. ",
         "With integration spending complete and leverage declining, buybacks retire a high-single-digit "
         "percentage of shares in peak years; total shareholder return from capital return alone is "
         "meaningful before any growth."),
    ],
    "outlook": [
        "Where is this business going? We expect T-Mobile to keep taking postpaid share for the next "
        "several years, driven by the network advantage and by segments where it is underpenetrated: "
        "smaller markets and rural coverage, business and government accounts, and fixed-wireless home "
        "internet. We expect these markets to contribute an increasing share of net additions over the "
        "forecast.",
        "The financial trajectory is operating leverage plus buybacks: revenue growth in the "
        "mid-single digits (the model's base path runs 5.5% tapering to 2.0%), EBITDA margins expanding "
        "from ~40% as the subscriber base scales against a largely fixed cost base, and the share count "
        "shrinking several percent per year. We do not assume a price war ends or begins; we assume "
        "rational competition continues, which the industry's recent history supports.",
        "Capex intensity is declining from merger-era peaks, so the resulting free cash flow — $18 "
        "billion in 2026E rising toward ~21% margins — funds dividends and buybacks. Our bear case "
        "assumes subscriber growth stalls, promotional intensity compresses ARPU, and the buyback slows. "
        "Wireless is a mature industry and the upside is compounding, not transformation; the margin of "
        "safety is the network moat and the cash generation.",
    ],
    "financials": [
        "Revenue was $79.57 billion in 2022, $78.56 billion in 2023, $81.40 billion in 2024, and $88.31 "
        "billion trailing in 2025 — the growth re-accelerating as the Sprint integration completed. "
        "Free cash flow tells the merger story in one line: −$0.52 billion in 2022 (integration peak), "
        "$7.75 billion in 2023, $9.98 billion in 2024, $15.43 billion trailing in 2025. The harvest phase "
        "has begun.",
        "The balance sheet still carries ~$83.5 billion of merger-era net debt, which is why buyback "
        "capacity depends on continued deleveraging — and why the bear case stresses it. But the "
        "trajectory is one-directional: integration capex behind, leverage falling, FCF compounding.",
    ],
    "fin_table": {
        "headers": ["$ bn", "2022", "2023", "2024", "2025 (TTM)"],
        "rows": [
            ["Revenue", "79.57", "78.56", "81.40", "88.31"],
            ["Free cash flow", "−0.52", "7.75", "9.98", "15.43"],
        ],
        "footnote": "Sources: company filings via Yahoo Finance. 2025 = trailing twelve months.",
    },
    "moat": [
        ("Mid-band spectrum depth. ",
         "The Sprint-derived 2.5 GHz portfolio delivers speed plus coverage that competitors cannot "
         "replicate without years of investment — the foundation of the network advantage."),
        ("Lowest churn in the industry. ",
         "Network quality plus value positioning produce the industry's lowest churn, which compounds "
         "subscriber economics over time."),
        ("Scale operating leverage. ",
         "High fixed costs and near-zero marginal cost per subscriber convert base growth into margin "
         "expansion mechanically."),
        ("Fixed-wireless capacity monetization. ",
         "Excess network capacity sold as home internet at very high incremental margins — a growth "
         "vector competitors with thinner spectrum cannot match as efficiently."),
    ],
    "valuation_method": "10-year scenario FCF DCF",
    "valuation_intro": [
        "We value T-Mobile on a 10-year scenario free-cash-flow DCF — weights bear 25% / base 50% / "
        "bull 25% — with scenario-specific discounts: bear 11.5% (base + 250bp), base 9.0% (stable, "
        "cash-generative telecom leader), bull 8.0% (base − 150bp). Terminal growth is 1.0% / 2.0% / "
        "2.0% on year-10 free cash flow. Net debt of ~$83.5 billion is subtracted from enterprise value; "
        "1.073 billion diluted shares.",
        "Scenario fair values: bear $50.30 (stalled subscriber growth, promotional ARPU pressure, slower "
        "buybacks), base $216.30 (continued industry-leading net additions tapering to market growth, "
        "stable ARPU, 3.5% revenue CAGR, year-10 EBITDA margin 40.2%), bull $338.20 (faster share gains "
        "in underpenetrated segments, stronger fixed-wireless growth, 5.2% revenue CAGR). "
        "Probability-weighted: $205.",
        "Sensitivities: the valuation is most sensitive to the long-term net-addition trajectory and "
        "the buyback pace. If net additions fade to market growth sooner than modeled, fair value "
        "declines by roughly a tenth; if buybacks run above our assumed pace, it rises similarly.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 50.30,
            "assumptions": "Subscriber growth stalls; promotional intensity compresses ARPU; buyback slows while leverage stays elevated",
            "rev_cagr": "+0.5%", "margin_end": "35.0%",
            "discount": 0.115, "terminal_g": 0.01, "tv_share": 0.343,
            "pv_explicit": 90.3, "pv_terminal": 47.2, "cashflow_unit": "$B",
        },
        "base": {
            "fair_value": 216.30,
            "assumptions": "Continued industry-leading postpaid net additions tapering to market growth; stable ARPU; margin expansion from operating leverage; buybacks at recent intensity",
            "rev_cagr": "+3.5%", "margin_end": "40.2%",
            "discount": 0.09, "terminal_g": 0.02, "tv_share": 0.531,
            "pv_explicit": 148.0, "pv_terminal": 167.6, "cashflow_unit": "$B",
        },
        "bull": {
            "fair_value": 338.20,
            "assumptions": "Faster share gains in underpenetrated segments; stronger fixed-wireless growth; enterprise 5G optionality contributes",
            "rev_cagr": "+5.2%", "margin_end": "44.0%",
            "discount": 0.08, "terminal_g": 0.02, "tv_share": 0.581,
            "pv_explicit": 186.8, "pv_terminal": 259.6, "cashflow_unit": "$B",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "risks": [
        ("Competition. ",
         "AT&T and Verizon can match promotions and network claims; cable MVNOs compete aggressively "
         "on price."),
        ("Saturation. ",
         "The US wireless market is mature; long-term growth depends on share gains and ARPU, both of "
         "which can stall."),
        ("Capital intensity. ",
         "Network leadership requires sustained capex; technology shifts (e.g., satellite) could alter "
         "the investment calculus."),
        ("Regulatory. ",
         "Spectrum policy, merger scrutiny, and consumer-protection rules affect strategy and costs."),
        ("Leverage. ",
         "The balance sheet still carries merger-era debt; buyback capacity depends on continued "
         "deleveraging."),
        ("Price competition. ",
         "A sustained price war would compress ARPU across the industry."),
    ],
    "falsification": (
        "Downgrade to HOLD if postpaid net additions turn negative for two consecutive quarters "
        "(the share-gain engine stalled), if churn rises to parity with competitors (network and brand "
        "advantage eroding), or if ARPU declines persistently under promotional pressure. Buybacks "
        "slowing materially while leverage stays elevated would remove a key per-share compounding "
        "driver."
    ),
    "charts": {
        "scenario": {"bear": 50.30, "base": 216.30, "bull": 338.20,
                     "weighted": 205.00, "price": 163.64},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [79.571, 78.558, 81.4, 88.309],
            "fcf_hist": [-0.52, 7.748, 9.982, 15.427],
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": rev_proj,
            "fcf_proj": fcf_proj,
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via Yahoo Finance (2025 = TTM). Projection: model "
                    "base-case path — revenue growth 5.5% tapering to 2.0%, FCF margins ~20–21%.",
        },
        "composition": {
            "bear": {"pv_explicit": 90.3, "pv_terminal": 47.2},
            "base": {"pv_explicit": 148.0, "pv_terminal": 167.6},
            "bull": {"pv_explicit": 186.8, "pv_terminal": 259.6},
            "unit": "$B",
        },
        "extra": {
            "type": "line",
            "title": "Revenue growth path by scenario (% y/y)",
            "years": [2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "series": [
                {"label": "Bear", "values": [2.5, 1.5, 0.0, -1.5, -1.0, 0.0, 0.5, 1.0, 1.0, 1.5]},
                {"label": "Base", "values": G},
                {"label": "Bull", "values": [7.5, 7.0, 6.5, 6.0, 5.5, 5.0, 4.5, 4.0, 3.5, 3.0]},
            ],
            "ylabel": "%",
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "TMUS-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
print("rev_proj:", rev_proj)
print("fcf_proj:", fcf_proj)
