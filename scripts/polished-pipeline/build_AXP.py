"""Polished note: American Express (AXP) — REDUCE, fair value $250.00.

Valuation: 10-year scenario DCF on per-share total shareholder distributions
(dividends + net buybacks) — the correct cash-flow-to-equity for a lender.
Scenario FVs / PV splits recomputed from the hardened distribution model
(discounts 12.5%/10%/8.5%; terminal growth 1.75%/2.5%/2.5%).
History: company filings via Yahoo Finance (Oct 2026). Trajectory projection:
base-case distribution path from the model; revenue grown at the base-case
EPS CAGR. All prose is fresh October 4, 2026 analysis.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note, validate

# --- model-derived scenario numbers (distribution DCF, per-share $) ---
# bear: recession 2027-28, EPS -40%/-5%, buybacks suspended, 60% payout after
# base: ~8.6% EPS CAGR fading, 68% total payout; bull: ~11.4% EPS CAGR, 68% payout
SCEN = {
    "bear": dict(fv=77.36, pv_expl=42.91, pv_tv=34.45, tv=0.445,
                 disc=0.125, gt=0.0175, cagr="+1.1%",
                 assumptions=("Credit-cycle turn: billed business stalls, net write-offs rise "
                               "toward 3%+, provisions rise $2-3B annually, buybacks suspended "
                               "through 2028, card-fee growth decelerates to mid-single digits, "
                               "multiple compresses to 12-13x normalized earnings.")),
    "base": dict(fv=260.55, pv_expl=116.11, pv_tv=144.44, tv=0.554,
                 disc=0.10, gt=0.025, cagr="+8.6%",
                 assumptions=("Billed business compounds at high-single digits, card fees grow "
                               "double digits for several more years before moderating, credit "
                               "normalizes only mildly, expenses track revenue, buyback retires "
                               "2-3% of shares annually at a 68% total payout.")),
    "bull": dict(fv=410.48, pv_expl=143.24, pv_tv=267.24, tv=0.651,
                 disc=0.085, gt=0.025, cagr="+11.4%",
                 assumptions=("Affluent-spend flywheel sustains double-digit billed-business "
                               "growth, international becomes a second engine, credit stays "
                               "pristine, and the market permanently awards a premium-network "
                               "multiple on a 68% total payout.")),
}

data = {
    "ticker": "AXP",
    "company": "American Express Company",
    "exchange": "NYSE",
    "sector": "Financial Services — Credit Services",
    "verdict": "REDUCE",
    "fair_value": 250.00,
    "price": 302.78,
    "risk": "Medium",
    "headline": "A superb franchise at a price that assumes the credit cycle has been repealed",
    "ceo": "Stephen Squeri",
    "hq": "New York, New York",
    "snapshot": [
        ("Market cap", "~$204 bn (0.68 bn sh × $302.78)"),
        ("52-week range", "~$291 – $387"),
        ("Price / fair value", "$302.78 / $250.00"),
        ("Implied downside", "−17%"),
        ("2025 revenue, net of interest expense", "$72.2 bn"),
        ("2026E diluted EPS guidance", "$17.30 – $17.90 (~17–18x the $302.78 price)"),
        ("Return on equity", "36–38%"),
        ("Credit quality (Q2 2026)", "Net write-offs 2.0%; delinquencies 1.2%"),
        ("Capital strength / return", "CET1 10.4%; $2.9 bn returned in Q2 2026 ($2.2 bn buybacks)"),
        ("Next catalyst", "Holiday billed-business prints; 2027 guidance (January 2027)"),
    ],
    "thesis": [
        "American Express is executing superbly. Second-quarter 2026 revenue net of interest "
        "expense grew 10% to $19.64 billion, billed business accelerated 9% on an FX-adjusted "
        "basis — the fastest pace in three years — net card fees climbed 15% to a record $2.9 "
        "billion for the 32nd consecutive quarter of double-digit growth, and diluted EPS rose "
        "11% to $4.53. Credit quality is pristine: net write-offs flat at 2.0%, delinquencies at "
        "1.2%, and a $1.1 billion provision that actually declined on a reserve release. "
        "Management raised full-year revenue growth guidance to 10% while holding EPS guidance "
        "at $17.30–$17.90. Return on equity runs at 36–38%. By every operating measure, this is "
        "a premium franchise performing at a premium level.",
        "And the market has noticed — which is precisely the problem. At $302.78, American "
        "Express trades at roughly 17–18 times the $17.30–$17.90 EPS guidance for a business "
        "whose through-cycle revenue growth is high-single digits and whose earnings are, at "
        "bottom, a leveraged bet on affluent consumer spending and benign credit. The "
        "premium-spend flywheel — acquire affluent cardmembers, monetize through discount "
        "revenue and rising annual fees, reinvest in rewards and the Platinum refresh — is "
        "working beautifully right now because the affluent consumer is employed, spending, and "
        "current on payments. Every one of those conditions is cyclical. The reserve release "
        "flattered the quarter; the 32 quarters of double-digit fee growth are a triumph of "
        "compounding that gets harder, not easier, with each successive quarter; and the 12% "
        "expense growth — driven by engagement costs and the Platinum refresh — shows how "
        "expensive it is to keep the flywheel spinning.",
        "Our judgment, on a probability-weighted scenario DCF over a 10-year horizon, is fair "
        "value of $250 — about 17% below the current price. The base case gives Amex full "
        "credit for the franchise: billed business compounding at high-single digits, card fees "
        "growing double digits for several more years before normalizing, credit staying near "
        "current benign levels through the explicit period, and the buyback continuing to "
        "retire 2–3% of shares annually. But it refuses to capitalize today's pristine credit "
        "and peak affluent spending as permanent, and the bear case — which sits below the "
        "price, as required — models what Amex shareholders have lived through before: a "
        "consumer downturn where billed business stalls, provisions rise by billions, and the "
        "multiple compresses from premium to merely good. We rate the stock REDUCE. This is a "
        "wonderful company at a price that assumes the credit cycle has been repealed.",
        "The forward question is not whether Amex is well run — it is superbly run — but what "
        "the next leg of the cycle does to a 17–18x multiple. Amex has traded at 10–12x "
        "earnings in softer environments within recent memory. The normalization mechanics are "
        "ordinary, not catastrophic: net card-fee growth faces the arithmetic of a larger "
        "base and the limits of annual-fee pricing power; the reserve release that flattered "
        "2026 provisions reverses when credit normalizes, and provisions rising by even $1–2 "
        "billion annually is a meaningful EPS headwind; expense growth in the low teens means "
        "operating leverage is thinner than the revenue line suggests. None of this impairs "
        "the franchise. All of it reprices the multiple — and the distance from 17–18x to "
        "12–13x is the downside the REDUCE rating is meant to capture.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("The price capitalizes peak-cycle credit as permanent. ",
         "Net write-offs at 2.0% and delinquencies at 1.2% are cyclical lows, and the 2026 "
         "provision benefited from a reserve release. A lender's earnings at the benign end of "
         "the credit cycle deserve a premium to banks — not immunity from the cycle."),
        ("The fee-forward mix shift is real de-risking, but it is already in the price. ",
         "Thirty-two straight quarters of double-digit card-fee growth have steadily moved the "
         "revenue mix toward recurring, high-margin annual fees that do not disappear in a "
         "spending downturn. That structural improvement is genuine — and the market has "
         "already paid for all of it, and then some."),
        ("International is the underappreciated leg — and the reason this is REDUCE, not SELL. ",
         "International Card Services posted 20% billed-business growth in Q1 2026, with years "
         "of runway. The franchise deserves representation in a portfolio; it simply does not "
         "deserve 17–18x peak earnings."),
    ],
    "business": [
        "American Express operates a closed-loop payments network — it is simultaneously the "
        "card issuer, the network, and (largely) the acquirer — which gives it data, economics, "
        "and customer relationships that the open-loop networks (Visa, Mastercard) do not have. "
        "Revenue comes from discount revenue (the merchant fee on billed business), net card "
        "fees (annual fees, now a $2.9 billion quarterly run-rate business growing 15%), and "
        "net interest income on revolving card balances ($4.6 billion in Q2 2026, up 11%). The "
        "customer base skews affluent: premium card products (Platinum, Gold, Centurion), heavy "
        "travel-and-entertainment exposure (T&E billed business up 10% in the quarter), and "
        "small-business and corporate cards.",
        "The economics are among the best in financial services. Cards-in-force reached 155.1 "
        "million, up 4%; network volumes were $516.8 billion in the quarter, up 9%; and the "
        "Common Equity Tier 1 ratio of 10.4% with $45.2 billion of cash supports both growth "
        "investment and capital return — $2.9 billion returned in Q2 2026 alone ($2.2 billion "
        "of buybacks at an average price of $315.77, plus dividends). The fee-forward strategy "
        "is deliberate: annual fees are recurring, high-margin, and less cyclical than "
        "spend-based revenue.",
    ],
    "business_bullets": [
        ("The affluent-spend flywheel. ",
         "Acquire premium cardmembers, monetize through discount revenue and rising annual "
         "fees, reinvest in rewards and card refreshes. The Platinum refresh cycle is currently "
         "driving acquisition and engagement — at 12% expense growth, the cost of keeping the "
         "wheel turning."),
        ("Closed-loop underwriting advantage. ",
         "Amex underwrites its own cardmembers, which is why its credit performance is "
         "structurally better than monolines' — 2.0% net write-offs versus multiples of that at "
         "subprime lenders. This advantage persists through cycles; it does not eliminate them."),
        ("International acceptance and billed business. ",
         "International Card Services grew billed business 20% in Q1 2026 — the clearest "
         "second engine in the portfolio, with years of runway in markets where Amex "
         "acceptance is still expanding."),
        ("Capital return as a core output. ",
         "With a 10.4% CET1 ratio, Amex returned $2.9 billion in a single quarter. Our "
         "valuation models 68% of earnings returned annually (dividends plus net buybacks) — "
         "the correct cash-flow-to-equity for a lender."),
    ],
    "outlook": [
        "Our forward view is that Amex's operating momentum persists through 2027 — the "
        "affluent consumer is in good shape, the Platinum refresh cycle is driving acquisition "
        "and engagement, and billed business should keep growing at high-single digits — but "
        "that the market is extrapolating a cyclical peak. The specific mechanics of the coming "
        "normalization: net card-fee growth, after 32 quarters of double-digit gains, faces "
        "the arithmetic of a larger base and the limits of annual-fee pricing power; the "
        "reserve release that flattered 2026 provisions reverses when credit normalizes, and "
        "provisions rising by even $1–2 billion annually is a meaningful EPS headwind; and "
        "expense growth in the low teens — the cost of acquiring and engaging premium "
        "cardmembers — means operating leverage is thinner than the revenue line suggests.",
        "We are constructive on the structural elements. The fee-forward mix shift genuinely "
        "de-risks the model: every point of revenue mix that moves from discount revenue to "
        "card fees is a point of revenue that does not disappear in a spending downturn. "
        "International — 20% billed-business growth in International Card Services — remains "
        "an underappreciated growth vector with years of runway. The closed-loop data "
        "advantage in underwriting should let Amex navigate a credit turn better than "
        "competitors, which is cold comfort for the stock price but real for the franchise. "
        "Our base case has EPS compounding at roughly 8–9% through the decade — an excellent "
        "outcome for a financial company, and one the current price more than discounts.",
        "The scenario that worries us is not a 2008-style crisis but an ordinary "
        "affluent-consumer slowdown: billed business growth halving, delinquencies ticking up "
        "from 1.2%, provisions rising again, and the market deciding that 17–18x earnings was "
        "a peak-cycle multiple for what is ultimately a consumer-credit business with a great "
        "brand. Our judgment: the franchise deserves a premium to banks, not immunity from "
        "the credit cycle.",
    ],
    "financials": [
        "Revenue net of interest expense grew from $60.5 billion in 2023 to $72.2 billion in "
        "2025, a two-year run of roughly 9% annual growth, with Q2 2026 up 10% to $19.64 "
        "billion. The mix is improving in the right direction: net card fees at a $2.9 billion "
        "quarterly run rate (+15%, the 32nd straight double-digit quarter) are the highest-"
        "quality dollars in the P&L, and net interest income of $4.6 billion (+11%) shows the "
        "revolving book growing alongside spend. But 12% expense growth is outrunning the "
        "revenue line — engagement marketing and the Platinum refresh are expensive — so "
        "operating leverage is modest despite the top-line strength.",
        "Credit is the swing factor and it is currently at the benign end. Net write-offs of "
        "2.0% and delinquencies of 1.2% are cyclical lows; the $1.1 billion Q2 provision "
        "declined on a reserve release, which flatters the earnings run rate. Our bear case "
        "models the normalization Amex shareholders have seen before: a genuine recession "
        "path with EPS falling 40% in 2027 and 5% in 2028 (2020 showed EPS can fall 53% in a "
        "single year when provisions triple), buybacks suspended through 2028, and the "
        "payout falling back to a leaner 60%. The balance sheet can absorb this — CET1 of "
        "10.4% and $45.2 billion of cash — but the multiple cannot absorb it at 17–18x, which "
        "is the entire point of the REDUCE.",
    ],
    "fin_table": {
        "headers": ["", "2023", "2024", "2025", "Q2 2026"],
        "rows": [
            ["Revenue, net of interest expense ($bn)", "60.5", "66.0", "72.2", "19.6"],
            ["YoY growth", "—", "+9.0%", "+9.5%", "+10%"],
            ["Net card fees ($bn, quarter)", "—", "—", "—", "2.9"],
            ["Net interest income ($bn, quarter)", "—", "—", "—", "4.6"],
            ["Net write-offs", "—", "—", "—", "2.0%"],
            ["Delinquency rate", "—", "—", "—", "1.2%"],
            ["Return on equity", "—", "—", "—", "36–38%"],
            ["Distributions: div + buybacks ($bn)", "5.4", "8.0", "8.1", "2.9"],
        ],
        "footnote": "Annual revenue from company filings via Yahoo Finance; quarterly figures "
                    "from the Q2 2026 release. Distributions = cash dividends paid + share "
                    "repurchases (cash-flow statement). — = not disclosed in that period.",
    },
    "moat": [
        ("The closed loop is the moat. ",
         "Issuing, network, and acquiring in one house gives Amex proprietary spend data that "
         "open-loop networks never see — the foundation of its underwriting edge and its "
         "fraud performance. Competitors cannot replicate the data asset without replicating "
         "the business model."),
        ("The affluent franchise is self-reinforcing. ",
         "Premium cardmembers spend more per card, default less, and pay annual fees for the "
         "privilege — 155.1 million cards-in-force and rising average proprietary spend. "
         "Chase and Citi now contest the tier aggressively, so the moat requires constant "
         "reinvestment (the 12% expense growth is the toll)."),
        ("Fee-forward mix de-risks the cycle. ",
         "Thirty-two quarters of double-digit card-fee growth have built a $2.9 billion "
         "quarterly annuity of high-margin, recurring revenue that does not vanish when "
         "spending pauses. This is a genuine structural improvement — and the main reason "
         "the through-cycle multiple deserves a premium to banks."),
        ("The moat's weak link is the interface. ",
         "Digital wallets, buy-now-pay-later, and alternative rails compete for the "
         "transaction interface, particularly with younger affluent cohorts. Acceptance parity "
         "in the US is effectively complete, which removes an old objection but also an old "
         "growth lever."),
    ],
    "valuation_method": "10-year scenario distribution DCF (dividends + net buybacks)",
    "valuation_intro": [
        "We value American Express on a 10-year scenario DCF of per-share total shareholder "
        "distributions — dividends plus net buybacks — the correct cash-flow-to-equity for a "
        "lender, weighted 25% / 50% / 25%. Discount rates are scenario-specific: base 10% "
        "(high-quality financial, but with genuine credit-cycle exposure), bear 12.5% (base + "
        "250bp, distress pricing), bull 8.5% (base − 150bp, above the 8% floor). Terminal "
        "growth is 2.5% in base and bull and 1.75% in the bear, applied to year-10 "
        "distributions at normalized mid-cycle credit costs — never today's 2.0% write-off "
        "rate and reserve-release-assisted provisions.",
        "The scenario FVs are $77.36 (bear) / $260.55 (base) / $410.48 (bull), weighting to "
        "$252.23 — our $250 target, about 17% below the $302.78 close. The bear case is a "
        "genuine recession path: EPS falls 40% in 2027 and 5% in 2028 as provisions spike, "
        "buybacks are suspended through 2028 (the 2020 playbook), and the payout resumes at a "
        "leaner 60%. The base case fades EPS growth from the realized 11.5% (2019–25) to a "
        "10-year CAGR of about 8.6% with a constant 68% total payout. Terminal value is "
        "45–65% of equity value across scenarios — inside the 70% guardrail, disclosed here.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 77.36,
            "assumptions": SCEN["bear"]["assumptions"],
            "rev_cagr": SCEN["bear"]["cagr"], "margin_end": "n/a (payout DCF)",
            "discount": SCEN["bear"]["disc"], "terminal_g": SCEN["bear"]["gt"],
            "tv_share": SCEN["bear"]["tv"],
            "pv_explicit": SCEN["bear"]["pv_expl"], "pv_terminal": SCEN["bear"]["pv_tv"],
            "cashflow_unit": "$/sh",
        },
        "base": {
            "fair_value": 260.55,
            "assumptions": SCEN["base"]["assumptions"],
            "rev_cagr": SCEN["base"]["cagr"], "margin_end": "n/a (payout DCF)",
            "discount": SCEN["base"]["disc"], "terminal_g": SCEN["base"]["gt"],
            "tv_share": SCEN["base"]["tv"],
            "pv_explicit": SCEN["base"]["pv_expl"], "pv_terminal": SCEN["base"]["pv_tv"],
            "cashflow_unit": "$/sh",
        },
        "bull": {
            "fair_value": 410.48,
            "assumptions": SCEN["bull"]["assumptions"],
            "rev_cagr": SCEN["bull"]["cagr"], "margin_end": "n/a (payout DCF)",
            "discount": SCEN["bull"]["disc"], "terminal_g": SCEN["bull"]["gt"],
            "tv_share": SCEN["bull"]["tv"],
            "pv_explicit": SCEN["bull"]["pv_expl"], "pv_terminal": SCEN["bull"]["pv_tv"],
            "cashflow_unit": "$/sh",
        },
    },
    "scenario_note": "AXP is valued on per-share shareholder distributions (dividends + net "
                     "buybacks); the 'Rev CAGR' column shows each scenario's 10-year EPS CAGR, "
                     "and composition is in $/share. Payout: 68% of earnings in base and bull "
                     "(60% post-recession in the bear).",
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "risks": [
        ("Credit-cycle turn. ",
         "Write-offs at 2.0% and delinquencies at 1.2% are cyclical lows; normalization would "
         "push provisions up by billions and hit EPS directly — 2020 showed EPS can fall 53% "
         "in a single year when provisions triple."),
        ("Affluent-spending slowdown. ",
         "Billed business is concentrated in discretionary and T&E; the affluent cohort is "
         "the most exposed to asset-price and employment shocks."),
        ("Fee-growth arithmetic. ",
         "Thirty-two quarters of double-digit card-fee growth gets harder against a larger "
         "base; annual-fee pricing power has limits, and Chase/Citi contest the premium tier."),
        ("Expense intensity. ",
         "12% expense growth to acquire and engage premium cardmembers compresses operating "
         "leverage if revenue growth moderates."),
        ("Multiple compression. ",
         "17–18x earnings is a peak-cycle multiple for a consumer-credit business; re-rating "
         "to historical mid-cycle multiples implies 20%+ downside without any fundamental "
         "impairment."),
        ("Disintermediation. ",
         "Digital wallets, buy-now-pay-later, and alternative rails compete for the "
         "transaction interface, particularly with younger affluent cohorts."),
    ],
    "falsification": (
        "A genuine credit scare or consumer slowdown that takes the stock 20–25% lower while "
        "the franchise and underwriting advantage remain intact would make this a BUY — Amex "
        "should be bought when credit fear peaks, not at the top of the credit cycle. "
        "Sustained double-digit card-fee growth with stable credit through an actual economic "
        "slowdown would prove the fee-forward model has structurally de-risked earnings and "
        "justify a higher multiple. Evidence that international billed business is becoming a "
        "second double-digit growth engine at scale would raise through-cycle growth "
        "assumptions. Conversely, delinquencies inflecting upward while the multiple holds "
        "would confirm the peak-cycle thesis and deepen the REDUCE view. A structural loss of "
        "pricing power on annual fees, or share loss in premium acquisition to fintech "
        "competitors, would impair the flywheel thesis. We watch: monthly billed-business "
        "prints, delinquency and write-off trends, card-fee growth versus the 32-quarter "
        "streak, and expense growth relative to revenue."
    ),
    "methodology": [
        "We value American Express on a 10-year scenario discounted-cash-flow framework "
        "built on per-share total shareholder distributions — dividends plus net buybacks — "
        "which is the correct cash-flow-to-equity for a lender whose reported operating cash "
        "flow is polluted by credit-book working capital. Bear, base, and bull scenarios "
        "carry scenario-specific discount rates (12.5% / 10.0% / 8.5%) and terminal growth "
        "assumptions (1.75% / 2.5% / 2.5%), probability-weighted 25% / 50% / 25%.",
        "The bear case is required to be genuinely adverse and to sit below the current "
        "price: it models an actual earnings trough (EPS −40% in 2027, −5% in 2028) with "
        "buybacks suspended through 2028, the 2020 playbook. Terminal value is computed on "
        "year-10 distributions at normalized mid-cycle credit costs — never on today's "
        "2.0% write-off rate or reserve-release-assisted provisions — and any terminal value "
        "exceeding 70% of equity value is haircut and disclosed.",
        "We cross-check the DCF against trading multiples and the payout-implied yield. The "
        "published target is the probability-weighted fair value, stated as a 12-month "
        "horizon reference. Risk ratings (Low / Medium / Medium-High / High) combine business "
        "volatility, balance-sheet strength, and valuation; Medium here reflects a superb "
        "franchise whose earnings remain cyclically exposed and whose multiple is full.",
    ],
    "charts": {
        "scenario": {"bear": 77.36, "base": 260.55, "bull": 410.48,
                     "weighted": 250.00, "price": 302.78},
        "trajectory": {
            # history: revenue (filings via Yahoo Finance); distributions = div + buybacks ($bn)
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [52.86, 60.52, 65.95, 72.23],
            "fcf_hist": [5.06, 5.43, 8.02, 8.08],
            # base-case projection: revenue at base EPS CAGR 8.6%; distributions = 68% payout path
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": [79.0, 85.8, 93.2, 101.2, 109.9, 119.4, 129.6, 140.8, 152.9, 166.0, 180.3],
            "fcf_proj": [8.2, 9.1, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.1, 17.3, 18.6],
            "unit": "$bn", "fcf_label": "Distributions",
            "note": "History: revenue net of interest expense from filings via Yahoo Finance; "
                    "'Distributions' = cash dividends paid + share repurchases (cash-flow "
                    "statement) — the cash-flow-to-equity used in the valuation. Projection: "
                    "base-case path (revenue at ~8.6% CAGR; distributions at 68% payout of "
                    "modeled EPS). 2026E revenue ~$79B annualized from Q2 2026.",
        },
        "composition": {
            "bear": {"pv_explicit": 42.91, "pv_terminal": 34.45},
            "base": {"pv_explicit": 116.11, "pv_terminal": 144.44},
            "bull": {"pv_explicit": 143.24, "pv_terminal": 267.24},
            "unit": "$/sh",
        },
        "extra": {
            "type": "pie",
            "title": "Revenue mix, 2026E annualized (~$79 bn)",
            "labels": ["Discount revenue", "Net card fees", "Net interest income"],
            "values": [48.9, 11.6, 18.4],
        },
    },
}

validate(data)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "AXP-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
