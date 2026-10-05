"""Polished note: Coinbase Global (COIN) — SELL, fair value $100.00.

Scenario numbers are from the current 10-year scenario DCF model
(valuation_output_v2.json): bear $46.90 / base $95.66 / bull $166.04,
weighted 25/50/25 to $101.07, rounded to the $100 target. WACC 14.5%/12%/
10.5%; terminal growth 1.5%/2.5%/2.5%; revenue CAGR 2.83%/8.48%/13.61%;
year-10 FCF margins 20%/26%/28%. DCF composition PVs are taken directly
from the model ($m): bear 3,825.1/2,540.0; base 10,870.7/9,393.5; bull
18,643.2/21,677.7 (terminal-value shares 39.9%/46.4%/53.8% of EV; equity =
EV + ~$7.0B net cash over ~285m diluted shares).
History: company filings via Yahoo Finance (Oct 2026; FCF = operating cash
flow less capex; capex undisclosed for 2024-25 and treated as negligible).
Trajectory projection: base-case path at 8.48% revenue CAGR with FCF margins
gliding 31.4% -> 26.0%. All prose is fresh October 4, 2026 analysis.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note, validate

data = {
    "ticker": "COIN",
    "company": "Coinbase Global, Inc.",
    "exchange": "NASDAQ",
    "sector": "Financials — Crypto Exchange & Digital-Asset Infrastructure",
    "verdict": "SELL",
    "fair_value": 100.00,
    "price": 183.00,
    "risk": "High",
    "headline": "The premier onshore exchange — capitalizing the mania as the run rate",
    "ceo": "Brian Armstrong",
    "hq": "Remote-first (no formal headquarters)",
    "snapshot": [
        ("Market cap", "~$52 bn (285 m diluted sh × $183.00)"),
        ("52-week range", "~$139 – $402"),
        ("Price / fair value", "$183.00 / $100.00"),
        ("Implied downside", "−45.4% — the widest in our coverage"),
        ("FY2025 revenue / FCF", "$7.18 bn / ~$2.3 bn"),
        ("Net cash", "~$7.0 bn"),
        ("Diluted shares", "~285 m"),
        ("Revenue character", "Retail trading volume: among the most cyclical streams in financial markets"),
        ("Next catalyst", "Q3 2026 earnings (late October)"),
        ("Sell-side view", "Mixed — bulls price regulatory clarity; bears price the cycle"),
    ],
    "thesis": [
        "Coinbase is the premier onshore crypto exchange: the most trusted brand in "
        "the industry, the custodian of choice for the spot bitcoin ETFs, and a genuine "
        "beneficiary of improving US regulatory clarity. These are real strategic "
        "assets, and in a bull market for digital assets the company's operating "
        "leverage is spectacular — incremental trading volume drops almost entirely "
        "to the bottom line. None of that is the SELL. The SELL is the price.",
        "The problem is that the operating leverage works in both directions, and "
        "crypto trading volume is among the most cyclical revenue streams in financial "
        "markets. Retail participation — the source of Coinbase's highest-margin take "
        "rates — surges during speculative manias and evaporates in drawdowns; history "
        "shows 50%+ volume contractions are routine, not tail events. At $183.00 the "
        "market is capitalizing elevated-cycle trading revenue as though the mania "
        "phase were the permanent run rate. Our probability-weighted fair value is "
        "$100.00 — bear $46.90, base $95.66, bull $166.04 — 45% below the quote, the "
        "widest downside in our coverage, reflecting the violence of crypto revenue "
        "cycles. Even the bull case ($166), which assumes sustained institutional "
        "adoption and growing subscription revenue, sits 9% below the current price.",
        "The structural pressures compound the cyclicality. Zero-commission crypto "
        "trading at traditional brokerages is compressing retail take rates across the "
        "industry; sophisticated volume increasingly migrates to venues competing on "
        "fractions of a basis point. Subscription and services revenue — staking, "
        "custody, USDC interest, Base sequencer fees — is growing and diversifying, but "
        "remains a minority of the total and is itself partly crypto-price-linked. "
        "And one consideration cuts against the entire bull thesis: Coinbase's "
        "valuation embeds the assumption that crypto's institutionalization accrues "
        "primarily to Coinbase. But institutionalization commoditizes access — ETFs, "
        "bank prime brokerage, and tokenized traditional assets all route around the "
        "retail exchange model. The more legitimate crypto becomes, the more "
        "competition Coinbase faces from institutions with lower cost structures and "
        "deeper distribution. Success of the asset class and success of this equity "
        "are diverging, and the price assumes they are the same trade. Regulatory "
        "clarity is a genuine long-term positive — but it is already in the price "
        "several times over. SELL.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("Operating leverage is symmetric. ",
         "The same cost structure that drops incremental volume to the bottom line in "
         "manias keeps the costs when volume falls 50%+. The earnings power the "
         "multiple prices is the top of the cycle, not the middle."),
        ("Take-rate compression is structural, not cyclical. ",
         "Zero-commission crypto at traditional brokerages resets the retail pricing "
         "anchor permanently. Every future mania will monetize at lower take rates "
         "than the last."),
        ("Institutionalization is a double-edged sword. ",
         "ETFs and bank prime brokerage legitimize the asset class while routing "
         "volume around the retail exchange. The more crypto wins, the more Coinbase "
         "competes with lower-cost incumbents."),
    ],
    "business": [
        "Coinbase operates the largest US crypto exchange across two customer "
        "segments: retail (the high-take-rate consumer platform) and institutional "
        "(Coinbase Prime, custody — including custody for the spot bitcoin ETFs — "
        "and advanced trading). Revenue splits into transaction revenue, which "
        "scales with trading volume and volatility, and subscription and services — "
        "staking rewards, custodial fees, USDC reserve interest, and Base sequencer "
        "fees — which is steadier but still partly linked to crypto prices and "
        "rates.",
        "The strategic assets are real: the most trusted onshore brand after a "
        "decade of offshore exchange failures, the ETF custody franchise, the USDC "
        "partnership economics, and Base — the leading Ethereum Layer-2 by activity — "
        "whose sequencer fees are a genuinely new, high-margin revenue line. The "
        "regulatory trajectory has also turned favorable: the end of regulation-by-"
        "enforcement and progress on market-structure legislation de-risk the "
        "operating environment that once threatened the business model itself.",
        "But the business remains, at its core, a volume-tax on speculation. "
        "Transaction revenue still dominates, retail take rates are multiples of "
        "institutional, and retail participation is the most sentiment-driven "
        "variable in financial markets. Diversification is progressing — it has not "
        "yet changed what the company fundamentally is.",
    ],
    "business_bullets": [
        ("Retail exchange: the profit engine and the cycle. ",
         "Highest-margin take rates in the industry, earned on the most sentiment-"
         "driven volume in financial markets. Spectacular in manias; evaporates in "
         "drawdowns."),
        ("Institutional & ETF custody: the trust moat. ",
         "Custodian of choice for spot bitcoin ETFs; Prime serves the institutional "
         "flow. Trust and compliance are the moat — but institutionalization invites "
         "bank prime-brokerage competition."),
        ("Subscription & services: growing, still a minority. ",
         "Staking, custody fees, USDC interest, Base sequencer fees — steadier, "
         "diversifying, but partly crypto-price- and rate-linked. Not yet the "
         "ballast the bull case needs."),
        ("Base: the genuine new asset. ",
         "A leading Ethereum Layer-2 with real sequencer-fee economics — the rare "
         "Coinbase revenue line that isn't a tax on trading volume."),
    ],
    "outlook": [
        "The cycle position is everything for this name. Crypto trading volume has "
        "been elevated, retail participation is strong, and the price action in "
        "digital assets supports the current revenue run rate. Our base case assumes "
        "that moderates rather than collapses: revenue compounds at 8.5% for ten "
        "years (from $7.18B toward ~$16B), free-cash-flow margins normalize from "
        "today's elevated ~32% toward 26% as take rates compress structurally, and "
        "subscription revenue keeps growing without ever becoming the majority. Fair "
        "value: $95.66. The current price needs the mania run rate to be permanent.",
        "The bull case ($166.04) is the institutionalization thesis fully realized: "
        "sustained institutional adoption, 13.6% revenue CAGR, 28% year-10 FCF "
        "margins, subscription revenue scaling — and it still doesn't clear $183. "
        "The bear case ($46.90) is the routine crypto winter: 50%+ volume "
        "contraction, retail gone, take rates compressed, 2.8% revenue CAGR and 20% "
        "FCF margins on a smaller base — a scenario the industry has produced "
        "multiple times per decade.",
        "The SELL would be wrong if retail take rates stabilize and grow (evidence "
        "the compression thesis is overstated), if subscription and services become "
        "the revenue majority and decouple from crypto prices, if Base sequencer "
        "fees scale into a material standalone profit pool, or if regulatory clarity "
        "drives sustained institutional volume that Coinbase captures in prime "
        "brokerage rather than losing to banks. Until then, the price is paying for "
        "the top of the cycle.",
    ],
    "financials": [
        "The financial history is the cyclicality thesis in numbers. Revenue was "
        "$3.19B in FY2022 (the last winter), $3.11B in FY2023, then $6.56B in FY2024 "
        "and $7.18B in FY2025 as the cycle turned — a near-doubling in two years on "
        "volume recovery. Free cash flow (operating cash flow less capex; capex "
        "undisclosed for 2024–25 and treated as negligible) swung from −$1.65B in "
        "FY2022 to +$3.0B in FY2024 and ~$2.3B in FY2025 — a $4.6B swing that "
        "demonstrates both the operating leverage and its symmetry.",
        "The balance sheet is a fortress: ~$7.0B of net cash, which is why equity "
        "value ($27.3B base case) exceeds enterprise value ($20.3B). That cash "
        "supports the valuation but doesn't change the earnings cyclicality — it "
        "just means the company survives winters comfortably. Terminal value is "
        "46% of base-case EV (54% bull, 40% bear): the out-years carry real weight, "
        "which is appropriate for a franchise asset but punishing if the terminal "
        "year is priced off mania earnings. Our terminal year uses normalized 26% "
        "FCF margins — deliberately below today's ~32%.",
    ],
    "fin_table": {
        "headers": ["$bn", "FY2022", "FY2023", "FY2024", "FY2025"],
        "rows": [
            ["Revenue", "3.19", "3.11", "6.56", "7.18"],
            ["Free cash flow (OCF − capex*)", "−1.65", "0.61", "3.00", "~2.30"],
            ["FCF margin", "−52%", "20%", "46%", "~32%"],
            ["Net cash", "—", "—", "—", "~7.0"],
        ],
        "footnote": "Company filings via Yahoo Finance. *Capex undisclosed for "
                    "2024–25 and treated as negligible (~$0.1B). The FY2022–FY2024 "
                    "revenue near-doubling and $4.6B FCF swing illustrate the "
                    "symmetric operating leverage.",
    },
    "moat": [
        ("Onshore trust after a decade of offshore failures. ",
         "The most trusted US brand in an industry defined by counterparty "
         "collapses — a genuine, hard-won asset that regulation now reinforces."),
        ("ETF custody franchise. ",
         "Custodian of choice for spot bitcoin ETFs: sticky, institutional, and "
         "reputationally self-reinforcing — the closest thing to an annuity in the "
         "business."),
        ("USDC economics and Base. ",
         "Reserve-interest income on the leading regulated stablecoin plus the "
         "leading Ethereum L2's sequencer fees — real, growing, non-transaction "
         "revenue lines."),
        ("The moat's limits: the volume tax and the commoditization paradox. ",
         "Trust doesn't prevent 50% volume drawdowns or take-rate compression — and "
         "institutionalization, the bull case's best argument, invites bank "
         "prime-brokerage competition with lower costs and deeper distribution. "
         "The moat protects the franchise; it doesn't repeal the cycle."),
    ],
    "valuation_method": "10-year scenario DCF",
    "valuation_intro": [
        "We value Coinbase on a 10-year scenario discounted-cash-flow framework, "
        "weighted 25% / 50% / 25%. Discount rates reflect a highly cyclical "
        "financial with crypto-volume beta: 12% base WACC, 14.5% bear (+250bp), "
        "10.5% bull (−150bp). Terminal growth is 1.5% (bear) / 2.5% (base, bull), "
        "applied to year-10 free cash flow at normalized margins (20% / 26% / 28%) "
        "— deliberately below today's elevated ~32%, because the terminal year must "
        "not be priced off mania earnings.",
        "Revenue compounds from the $7.18B FY2025 base at 2.83% (bear — the routine "
        "crypto winter) / 8.48% (base — moderation, not collapse) / 13.61% (bull — "
        "institutionalization fully realized). Scenario fair values: $46.90 / "
        "$95.66 / $166.04; the probability-weighted $101.07 rounds to our $100 "
        "target — 45.4% below the $183.00 close. Equity is EV plus ~$7.0B of net "
        "cash over ~285m diluted shares. Terminal value is 46% of base-case EV "
        "(54% bull, 40% bear) — no haircut required.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 46.90,
            "assumptions": ("Routine crypto winter: 50%+ volume contraction; retail "
                            "participation evaporates; 2.83% revenue CAGR; 20% "
                            "year-10 FCF margin; 14.5% WACC."),
            "rev_cagr": "+2.8%", "margin_end": "20%",
            "discount": 0.145, "terminal_g": 0.015, "tv_share": 0.399,
            "pv_explicit": 3825.1, "pv_terminal": 2540.0, "cashflow_unit": "$m",
        },
        "base": {
            "fair_value": 95.66,
            "assumptions": ("Cycle moderates without collapse: 8.48% revenue CAGR; "
                            "take-rate compression continues; FCF margins normalize "
                            "to 26%; 12% WACC."),
            "rev_cagr": "+8.5%", "margin_end": "26%",
            "discount": 0.12, "terminal_g": 0.025, "tv_share": 0.464,
            "pv_explicit": 10870.7, "pv_terminal": 9393.5, "cashflow_unit": "$m",
        },
        "bull": {
            "fair_value": 166.04,
            "assumptions": ("Institutionalization realized: 13.61% revenue CAGR; "
                            "subscription revenue scales; 28% year-10 FCF margin; "
                            "10.5% WACC."),
            "rev_cagr": "+13.6%", "margin_end": "28%",
            "discount": 0.105, "terminal_g": 0.025, "tv_share": 0.538,
            "pv_explicit": 18643.2, "pv_terminal": 21677.7, "cashflow_unit": "$m",
        },
    },
    "scenario_note": "Composition PVs are taken directly from the scenario DCF "
                     "model ($m); equity = EV + ~$7.0B net cash over ~285m diluted "
                     "shares.",
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "risks": [
        ("Volume cyclicality (High). ",
         "50%+ trading-volume contractions are routine, not tail events; retail "
         "participation — the highest-margin volume — evaporates in drawdowns."),
        ("Take-rate compression (High). ",
         "Zero-commission crypto at traditional brokerages resets the retail "
         "pricing anchor; sophisticated volume migrates to basis-point venues."),
        ("Commoditization via institutionalization (High). ",
         "ETFs, bank prime brokerage, and tokenized traditional assets route around "
         "the retail exchange model — success of the asset class and success of "
         "the equity are diverging."),
        ("Regulatory reversal (Medium). ",
         "Clarity has improved markedly, but crypto regulation remains political; "
         "adverse shifts would hit the onshore premium directly."),
        ("Crypto-price linkage of 'stable' revenue (Medium). ",
         "Staking, custody, and USDC income are steadier but still partly linked "
         "to asset prices and rates."),
        ("Competition (Medium). ",
         "Offshore venues on price, traditional brokers on distribution, banks on "
         "prime — attacked from every side of the cost curve."),
    ],
    "falsification": (
        "We would revisit the SELL if: retail take rates stabilize and grow "
        "(evidence the compression thesis is overstated); subscription and services "
        "become the revenue majority and demonstrably decouple from crypto prices; "
        "Base sequencer fees scale into a material standalone profit pool; or "
        "regulatory clarity drives sustained institutional volume that Coinbase "
        "captures in prime brokerage rather than ceding to banks. Any one of these "
        "would change the earnings durability the valuation assumes. We watch: "
        "blended take rates by quarter, subscription revenue as a share of total, "
        "Base fee trends, ETF custody mandates, and retail volume versus prior "
        "cycle peaks."
    ),
    "methodology": [
        "We value Coinbase on a 10-year scenario discounted-cash-flow framework, "
        "probability-weighted 25% / 50% / 25%. Revenue compounds from the current "
        "base under scenario CAGRs while free-cash-flow margins glide from current "
        "elevated levels to normalized scenario terminal margins — the terminal "
        "year is never priced off mania earnings.",
        "Discount rates are scenario-specific — 14.5% bear, 12% base, 10.5% bull — "
        "and terminal growth is 1.5% (bear) / 2.5% (base, bull) on year-10 free cash "
        "flow. The bear case is required to be genuinely adverse and to sit below "
        "the current price; terminal value exceeding 70% of enterprise value is "
        "haircut and disclosed (46% base, 54% bull, 40% bear — no haircut "
        "required). We cross-check against mid-cycle earnings power.",
        "The published target is the probability-weighted fair value rounded to a "
        "round number ($101.07 → $100), stated as a 12-month horizon reference. "
        "Risk ratings (Low / Medium / Medium-High / High) combine business "
        "volatility, balance-sheet strength, and valuation; High here reflects "
        "extreme revenue cyclicality and structural take-rate pressure against a "
        "strong net-cash balance sheet.",
    ],
    "charts": {
        "scenario": {"bear": 46.90, "base": 95.66, "bull": 166.04,
                     "weighted": 100.00, "price": 183.00},
        "trajectory": {
            # history: filings via Yahoo Finance; FCF = OCF - capex (capex n/a 2024-25)
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [3.19, 3.11, 6.56, 7.18],
            "fcf_hist": [-1.65, 0.61, 3.00, 2.30],
            # base-case projection: 8.48% revenue CAGR; FCF margins gliding 31.4% -> 26.0%
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035],
            "revenue_proj": [7.79, 8.45, 9.17, 9.94, 10.79, 11.70, 12.69, 13.77, 14.94, 16.20],
            "fcf_proj": [2.45, 2.60, 2.77, 2.94, 3.13, 3.32, 3.53, 3.75, 3.97, 4.21],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via Yahoo Finance (FCF = operating cash "
                    "flow less capex; capex undisclosed for 2024–25, treated as "
                    "negligible). Projection: base-case path — revenue at 8.48% CAGR "
                    "with FCF margins gliding from ~31% toward a normalized 26% as "
                    "take rates compress.",
        },
        "composition": {
            "bear": {"pv_explicit": 3825.1, "pv_terminal": 2540.0},
            "base": {"pv_explicit": 10870.7, "pv_terminal": 9393.5},
            "bull": {"pv_explicit": 18643.2, "pv_terminal": 21677.7},
            "unit": "$m",
        },
        "extra": {
            "type": "line",
            "title": "FCF margin: boom-bust history vs. base-case normalization",
            "years": [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035],
            "series": [{"label": "FCF margin, history",
                        "values": [-51.7, 19.6, 45.7, 32.0, None, None, None, None, None, None, None, None, None, None]},
                       {"label": "FCF margin, base case",
                        "values": [None, None, None, None, 31.4, 30.8, 30.2, 29.6, 29.0, 28.4, 27.8, 27.2, 26.6, 26.0]}],
            "ylabel": "%",
            "note": "The symmetric operating leverage: −52% to +46% FCF margins "
                    "across the last cycle. The base case normalizes to 26% — the "
                    "terminal year is never priced off mania earnings.",
        },
    },
}

validate(data)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "COIN-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
