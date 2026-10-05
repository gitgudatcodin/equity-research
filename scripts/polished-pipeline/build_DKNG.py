"""Polished note build: DraftKings Inc. (DKNG) — BUY, $27.00 target."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note, validate

data = {
    "ticker": "DKNG",
    "company": "DraftKings Inc.",
    "exchange": "NASDAQ",
    "sector": "Consumer Discretionary — Online Betting & Gaming",
    "verdict": "BUY",
    "fair_value": 27.00,
    "price": 18.59,
    "risk": "High",
    "headline": "The Sportsbook Obituary Is Premature; DKeX Is a Free Call Option",
    "ceo": "Jason Robins",
    "hq": "Boston, Massachusetts",
    "snapshot": [
        ("Market cap", "~$9.2 bn (~500 mn sh × $18.59)"),
        ("Price (Oct 2, 2026)", "$18.59"),
        ("52-week range", "~$18.52 – $36.98"),
        ("2026E adj. EBITDA", "~$1.0 bn (company target)"),
        ("Sportsbook handle", "+15% YoY as the NFL season kicked off"),
        ("DKeX", "Prediction-market exchange launched Jun 2026; live in 48 states"),
        ("iGaming", "Legal in a handful of states — the most profitable leg, mostly ahead"),
        ("2026 drawdown", "−39% YTD on prediction-market and regulatory fears"),
        ("Next catalyst", "Q3 2026 earnings; state legalization headlines; DKeX share data"),
    ],
    "thesis": [
        "DraftKings has fallen 39% in 2026 and now trades at $18.59 — pricing in the obituary "
        "of the American sportsbook at the hands of prediction markets. That obituary is "
        "premature. The core business — online sports betting and iGaming in licensed states "
        "— is on track to generate roughly $1 billion of adjusted EBITDA in 2026, sportsbook "
        "handle was growing 15% year over year as the NFL season kicked off, and the "
        "structural economics of mature-state sports betting keep improving as promotional "
        "intensity fades and hold percentages rise. The market has confused a real competitive "
        "question (what do Kalshi and Polymarket mean for the industry?) with a settled "
        "negative answer, and the resulting multiple prices the core franchise as though it is "
        "already in decline.",
        "Our judgment is that prediction markets are a threat to be managed, not a death "
        "sentence — and DraftKings is managing it better than the stock price suggests. In "
        "June 2026 the company launched DKeX, its own prediction-market exchange, which has "
        "since expanded to 48 states and is capturing share in the markets where it "
        "participates. That footprint matters enormously: prediction markets operate nationally "
        "under federal derivatives oversight, which means DraftKings can now acquire customers "
        "in states where sports betting remains illegal — California, Texas, Florida — and "
        "cross-sell them if and when those states legalize. The market values DKeX at zero; "
        "we see a free call option on the industry's fastest-growing segment, held by the "
        "operator with the best customer-acquisition machine in the business.",
        "The third leg is the legalization runway, which remains the most underappreciated "
        "source of compounding in the name. iGaming — far more profitable per user than "
        "sports betting — is legal in only a handful of states, and each new state that "
        "legalizes online casino is a step-change in DraftKings' earnings power. Sports "
        "betting still has large holdouts. Every year that passes without legalization is a "
        "year of deferred, not destroyed, value — and the prediction-market dynamic may "
        "actually accelerate the process by forcing states to confront the revenue they are "
        "leaving on the table.",
        "Our $27.00 fair value requires no heroics on prediction markets: it values the core "
        "sportsbook and iGaming business on its march toward mature-state margins, treats "
        "DKeX as a modest positive rather than the savior, and credits the legalization "
        "pipeline at a discount. The bear case — in which prediction markets structurally "
        "cannibalize the sportsbook and regulators pile on — sits below today's price, and we "
        "respect it; regulatory headlines have driven much of this year's decline. But at "
        "$18.59, the market is asking us to believe the bear case is the base case. The "
        "operating data says otherwise. The rating is BUY.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("The core is worth more than the market thinks. ",
         "Handle keeps growing at a mid-teens pace, hold keeps improving with product "
         "sophistication — live betting, same-game parlays, personalization — and the "
         "promotional arms race of the land-grab years is over. That alone, on reasonable "
         "multiples, supports a price well above $18.59."),
        ("DKeX at zero is the wrong number. ",
         "Months old, leveraging DraftKings' brand and enormous existing customer base at "
         "near-zero marginal acquisition cost, with a 48-state footprint giving DraftKings "
         "something it never had: a legal product in California and Texas."),
        ("Legalization is deferred, not destroyed, value. ",
         "iGaming's superior unit economics in each newly legalized state is a step-change "
         "the current price barely credits; regulatory friction is assumed in our target, "
         "not wished away."),
    ],
    "business": [
        "DraftKings Inc., headquartered in Boston, is one of the two dominant online sports "
        "betting operators in the United States alongside FanDuel, with a growing iGaming "
        "(online casino) business in states where it is legal. The company operates mobile "
        "sportsbooks in the majority of legal-betting states, digital casino products, the "
        "Jackpocket digital lottery courier acquired in 2024, and — since June 2026 — the "
        "DKeX prediction-market exchange, now live in 48 states. DraftKings also operates in "
        "Ontario and has exposure to international markets.",
        "The economics of the core business follow a well-understood maturation curve. New "
        "states lose money initially as operators spend heavily on promotions and customer "
        "acquisition; over two to four years, promotional intensity fades, the customer base "
        "seasons, hold percentages (the share of handle the operator keeps) improve with "
        "product sophistication — particularly same-game parlays — and the state flips to "
        "strong profitability. iGaming is structurally superior: higher hold, lower promotional "
        "intensity, and stickier customers. As the state mix matures and iGaming grows as a "
        "share of revenue, company-wide margins expand — the dynamic behind the roughly $1 "
        "billion 2026 adjusted EBITDA target.",
        "The prediction-market landscape adds a new dimension. Kalshi and Polymarket operate "
        "sports event contracts nationally under Commodity Futures Trading Commission "
        "oversight, competing with sportsbooks on pricing — recent data showed Kalshi's "
        "implied vig below both major sportsbooks for NFL Week 1 — while DraftKings' DKeX "
        "gives it a foothold in the same structure. The regulatory backdrop is fluid: court "
        "cases over states' authority to restrict prediction markets remain unresolved, with "
        "key deadlines extending into late 2026.",
    ],
    "outlook": [
        "Our forward view centers on a simple proposition: the sportsbook business that "
        "exists today is worth more than the market thinks, and everything else is "
        "optionality. Handle keeps growing at a mid-teens pace, the product keeps getting "
        "better at extracting hold — live betting, same-game parlays, and personalization all "
        "push in the same direction — and the promotional arms race of the land-grab years is "
        "over. As more states cross into maturity, the margin structure of the consolidated "
        "business should grind upward for years. That alone, on reasonable multiples, supports "
        "a price well above $18.59.",
        "On DKeX, we are deliberately measured. The early share data — roughly 3% of tracked "
        "NFL Week 1 prediction-market volume versus Kalshi's dominant share — shows how far "
        "the exchange has to go, and Kalshi's pricing advantage is real. But DKeX is months "
        "old, it leverages DraftKings' brand and its enormous existing customer base at "
        "near-zero marginal acquisition cost, and its 48-state footprint gives DraftKings "
        "something it never had: a legal product in California and Texas. Our base case "
        "assumes DKeX becomes a real but secondary business; our bull case assumes it "
        "captures a meaningful share of a large prediction-market TAM and becomes the "
        "customer-acquisition funnel for eventual sportsbook legalization in holdout states. "
        "Either way, the current price assigns it no value, which is the wrong number.",
        "The regulatory outlook is the swing factor we watch most closely. Adverse "
        "developments — state tax increases on sports betting, restrictions on prediction "
        "markets that strand DKeX, or federal intervention — would impair the thesis, and 2026 "
        "has supplied plenty of negative headlines, from the Brazil betting ban to "
        "congressional scrutiny. Our judgment is that the direction of travel still favors "
        "the legal industry: states need the tax revenue, consumers prefer regulated "
        "products, and prohibition has never worked in gambling. But we underwrite the target "
        "with regulatory friction assumed, not wished away.",
    ],
    "financials": [
        "The operating trajectory points the other way from the stock price. Revenue "
        "compounded from $2.24 billion in 2022 to $6.06 billion in 2025, and free cash flow "
        "inflected from negative $0.73 billion to positive $0.51 billion over the same period — "
        "the land-grab era's losses are behind it. The roughly $1 billion 2026 adjusted "
        "EBITDA target, against a ~$9 billion market cap, means the market capitalizes a "
        "profitable, growing earnings stream at a multiple that implies earnings have peaked.",
        "A cross-check on EV-to-forward-EBITDA supports the conclusion: the operating "
        "trajectory (15% handle growth, expanding hold, maturing states) points to growing, "
        "not peaking, earnings. Our DCF values the core sportsbook and iGaming business on "
        "its march toward mature-state margins — roughly $1 billion of 2026 EBITDA growing "
        "at double-digit rates — with DKeX as a modest positive and the legalization pipeline "
        "credited at a discount. Terminal growth is capped at 2.5% on normalized mid-cycle "
        "margins, and we do not assume prediction-market dominance in any scenario.",
    ],
    "fin_table": {
        "headers": ["$ bn", "2022", "2023", "2024", "2025"],
        "rows": [
            ["Total revenue", "2.24", "3.67", "4.77", "6.06"],
            ["YoY growth", "—", "+63.6%", "+30.0%", "+27.0%"],
            ["Operating cash flow", "−0.63", "−0.00", "0.42", "0.66"],
            ["Free cash flow", "−0.73", "−0.12", "0.30", "0.51"],
            ["2026E adj. EBITDA (target)", "—", "—", "—", "~1.0"],
        ],
        "footnote": "Sources: company filings via Yahoo Finance (annual). 2026E adjusted EBITDA per company target. FCF = operating cash flow less capex.",
    },
    "moat": [
        ("Scale and brand in a two-player market. ",
         "One of two dominant US online sportsbooks alongside FanDuel; the "
         "customer-acquisition machine and brand are the best in the business — the assets "
         "DKeX leverages at near-zero marginal cost."),
        ("The state-maturation curve. ",
         "Two to four years from launch to strong profitability per state, with hold "
         "improving on product sophistication; the growing base of mature states is a "
         "compounding earnings engine competitors cannot shortcut."),
        ("iGaming's structural superiority. ",
         "Higher hold, lower promotional intensity, stickier customers than sports betting — "
         "and legal in only a handful of states, so the highest-margin leg is mostly ahead."),
        ("DKeX's 48-state footprint. ",
         "A legal product in California, Texas, and Florida — states where sports betting "
         "remains illegal — creating a customer-acquisition funnel no sportsbook-only rival "
         "can match."),
        ("The moat's weak link: no pricing power against prediction markets. ",
         "Kalshi's implied vig undercut both major sportsbooks for NFL Week 1; if "
         "prediction markets structurally cannibalize handle, the maturation curve breaks — "
         "which is why mature-state handle is our downgrade tripwire."),
    ],
    "valuation_method": "10-year scenario FCF DCF (core sportsbook + DKeX option)",
    "valuation_intro": [
        "We value DraftKings on a 10-year probability-weighted scenario DCF of free cash "
        "flow — weights bear 25% / base 50% / bull 25% — discounted at 12% in the base case "
        "to reflect the speculative elements (regulatory uncertainty, the prediction-market "
        "competitive question) balanced against the demonstrated profitability of the core; "
        "bear 14.5% (base + 250bp), bull 10.5% (base − 150bp). Terminal growth is capped at "
        "2.5% on normalized mid-cycle margins, and we do not assume prediction-market "
        "dominance in any scenario.",
        "In the base case ($27.00), the core sportsbook and iGaming business grows handle "
        "and revenue at double-digit rates as states mature, adjusted EBITDA margins expand "
        "toward mature-state levels, DKeX contributes modestly, and the legalization pipeline "
        "adds states over time. The bear case ($12.00) is genuinely adverse and sits below "
        "the current price: prediction markets structurally cannibalize sportsbook handle, "
        "Kalshi's pricing advantage proves durable, states raise betting taxes, DKeX fails to "
        "gain traction, and the core business stagnates. The bull case ($42.00) assumes "
        "iGaming legalization accelerates across states, DKeX scales into a major "
        "prediction-market player and acquisition funnel, and mature-state margins reach "
        "their full potential. The probability-weighted fair value equals our $27.00 target.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 12.00,
            "assumptions": "Prediction markets structurally cannibalize sportsbook handle; Kalshi pricing advantage endures; states raise betting taxes; DKeX fails to scale",
            "rev_cagr": "+8.0%", "margin_end": "25%",
            "discount": 0.145, "terminal_g": 0.01, "tv_share": 0.40,
            "pv_explicit": 3600, "pv_terminal": 2400, "cashflow_unit": "$mn",
        },
        "base": {
            "fair_value": 27.00,
            "assumptions": "Handle and revenue grow double-digits as states mature; EBITDA margins expand toward mature-state levels; DKeX contributes modestly; legalization pipeline adds states",
            "rev_cagr": "+12.0%", "margin_end": "32%",
            "discount": 0.12, "terminal_g": 0.02, "tv_share": 0.52,
            "pv_explicit": 6480, "pv_terminal": 7020, "cashflow_unit": "$mn",
        },
        "bull": {
            "fair_value": 42.00,
            "assumptions": "iGaming legalization accelerates; DKeX scales into a major prediction-market player and acquisition funnel; mature-state margins reach full potential",
            "rev_cagr": "+17.0%", "margin_end": "38%",
            "discount": 0.105, "terminal_g": 0.025, "tv_share": 0.62,
            "pv_explicit": 7980, "pv_terminal": 13020, "cashflow_unit": "$mn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Scenario fair values are per-share equity values from the FCF DCF (~500 mn shares). 0.25×$12.00 + 0.50×$27.00 + 0.25×$42.00 = $27.00.",
    "risks": [
        ("Prediction-market competition. ",
         "Kalshi and Polymarket offer better pricing on straight bets and operate nationally; "
         "structural share loss from sportsbooks is the central risk."),
        ("Regulatory risk. ",
         "Unresolved court cases on prediction markets, potential state tax increases on "
         "sports betting, and federal scrutiny (including the congressional probe) could "
         "impair economics."),
        ("Promotional competition. ",
         "Rivalry with FanDuel and others could re-intensify, compressing margins."),
        ("DKeX execution. ",
         "The exchange is early-stage with small market share; failure to scale would strand "
         "the strategic rationale."),
        ("Responsible-gambling and reputational risk. ",
         "Scrutiny of AI-driven customer targeting could invite restrictive regulation."),
        ("International setbacks. ",
         "The Brazil betting ban demonstrates regulatory risk outside the US."),
    ],
    "falsification": (
        "Downgrade to HOLD on: sportsbook handle declining year over year in mature states "
        "for two consecutive quarters — evidence of structural cannibalization by prediction "
        "markets; adjusted EBITDA guidance cut materially below the roughly $1 billion 2026 "
        "target for non-regulatory reasons; DKeX shut down or withdrawn from major markets, "
        "eliminating the strategic option value; a federal or multi-state regulatory action "
        "that structurally raises the tax/fee burden on sports betting by a large margin; or "
        "market-share loss to FanDuel accelerating in head-to-head states, indicating "
        "competitive positioning — not just sector headwinds — is the problem. We watch: "
        "mature-state handle, hold percentages, DKeX volume share, and state tax headlines."
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
        "independently tested and haircut where evidence warrants. For DraftKings the base "
        "discount sits in the speculative tier to reflect regulatory uncertainty and the "
        "prediction-market competitive question.",
    ],
    "charts": {
        "scenario": {"bear": 12.00, "base": 27.00, "bull": 42.00,
                     "weighted": 27.00, "price": 18.59},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [2.24, 3.665, 4.768, 6.055],
            "fcf_hist": [-0.73, -0.115, 0.297, 0.509],
            "years_proj": [2026, 2027, 2028, 2029, 2030],
            "revenue_proj": [6.66, 7.33, 8.06, 8.87, 9.75],
            "fcf_proj": [0.62, 0.78, 0.95, 1.15, 1.38],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via Yahoo Finance (FCF = operating cash flow "
                    "less capex). Projections: base case — double-digit revenue growth as "
                    "states mature, FCF margins expanding toward mature-state levels.",
        },
        "composition": {
            "bear": {"pv_explicit": 3600, "pv_terminal": 2400},
            "base": {"pv_explicit": 6480, "pv_terminal": 7020},
            "bull": {"pv_explicit": 7980, "pv_terminal": 13020},
            "unit": "$mn",
        },
        "extra": {
            "type": "line",
            "title": "FCF margin — history vs. base case (%)",
            "years": [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030],
            "series": [{"label": "FCF margin",
                        "values": [-32.6, -3.1, 6.2, 8.4, 9.3, 10.6, 11.8, 13.0, 14.2]}],
            "ylabel": "%",
        },
    },
}

validate(data)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "DKNG-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
