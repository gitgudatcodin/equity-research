"""Polished note build: Webull (BULL). Scenario numbers from the hardened
10-year scenario FCFE-DCF model (bull-rebuild/bull_dcf_v2.py): bear $4.95 /
base $8.78 / bull $13.12, weighted $8.91 -> $9 target. History via yfinance.
Re-runnable: python3 build_BULL.py (from ~/workspace/polished-notes)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

# Base-case projection path (model): 2025A $571M; 2026E $790M; 2027E $950M;
# 2028E $1,090M; growth fading 12/10/8/6/5/4/3% to 2035 $1,729M.
# Adjusted net income (FCFE proxy): 84.2 / ~115 / ~152 / ~191, margin -> 18%.
rev_proj = [790, 950, 1090]
g = [0.12, 0.10, 0.08, 0.06, 0.05, 0.04, 0.03]
r = 1090.0
for x in g:
    r *= (1 + x)
    rev_proj.append(round(r, 1))
mgn = [0.145, 0.160, 0.175, 0.176, 0.177, 0.178, 0.179, 0.180, 0.180, 0.180]
# 2026E/2027E/2028E from the model (~115/~152/~191); thereafter revenue x margin.
ni_proj = [115.0, 152.0, 191.0] + \
    [round(rv * m, 1) for rv, m in zip(rev_proj[3:], mgn[3:])]

data = {
    "ticker": "BULL",
    "company": "Webull Corporation",
    "exchange": "NASDAQ",
    "sector": "Financials — Capital Markets / Online Brokerage",
    "verdict": "BUY",
    "fair_value": 9.00,
    "price": 7.34,
    "risk": "Medium-High",
    "headline": "Cash Is the Floor, the Business Is Nearly Free",
    "ceo": "Anquan Wang",
    "hq": "St. Petersburg, Florida",
    "snapshot": [
        ("Market cap", "~$3.5 bn (at $7.34)"),
        ("Net cash (Jun 2026)", "~$1.85 bn (~$3.89/share)"),
        ("Enterprise value", "~$1.6 bn"),
        ("52-week range", "~$4.50 – $14.51"),
        ("2025 revenue / adj. net income", "$571 mn / $84.2 mn"),
        ("Q2 2026", "Record revenue; $34.7 mn pretax profit"),
        ("Revenue model", "PFOF + net interest + subscriptions"),
        ("Footprint", "40+ markets; 20M+ registered users"),
        ("Listed", "April 2025 (SPAC merger)"),
        ("Next catalyst", "Q3 2026 earnings"),
    ],
    "thesis": [
        "The arithmetic of Webull at $7.34 is almost insultingly simple. The company sits on roughly "
        "$1.85 billion of net cash against a ~$3.5 billion market capitalization. Subtract the cash and "
        "the market values the entire operating franchise — a profitable brokerage doing $571 million of "
        "2025 revenue across 40-plus markets, one of the top retail options-trading platforms in the US — "
        "at about $3.45 a share, or $1.6 billion. That is under 3x revenue for the operating company, "
        "cash-adjusted. Our mid-cycle base case values the operating business alone at $4.89 a share "
        "($8.78 fair value minus $3.89 of cash). Investors are being offered the business for less than "
        "a deliberately harsh mid-cycle DCF says it is worth, with the cash truncating the left tail.",
        "Why is it this cheap? The reason is legible and it is exactly one thing: payment for order flow "
        "is the regulatory target. The EU has already banned it, the SEC has kept reform on the table "
        "for years, and 2026's trading-volume boom will normalize, because retail volumes always do. "
        "Our bear case models precisely that future — US take-rates compressed ~30%, European economics "
        "dead, revenue crawling at a 2.5% CAGR to $730 million by 2035, marketing staying intense, the "
        "governance discount persisting — and the equity is still worth $4.95, with roughly three-quarters "
        "of that being touchable cash. The base case asks for no heroics: an 11.9% revenue CAGR fading "
        "to single digits, adjusted-net margins settling at a mid-cycle 18%, self-clearing savings "
        "offsetting marketing intensity. That is $8.78, and the probability-weighted math is $8.91, "
        "rounded to our $9 target.",
        "The forward-looking judgment: Webull's international footprint is the underpriced asset. "
        "Forty-plus markets means the growth story is not hostage to US regulation alone — if US "
        "payment for order flow is gutted, the user-acquisition machine across the UK, Europe, "
        "Asia-Pacific, and Latin America keeps compounding, and self-clearing grinds unit costs down "
        "everywhere. The base case does not need the US to stay perfect; it needs the company to keep "
        "adding users and monetizing them internationally while the cash pile grows. That is a "
        "reasonable ask for $3.45 a share of operating value.",
        "At roughly 5.5 to 6 times trailing sales, Webull trades at about a third of Robinhood's "
        "multiple while growing revenue faster. That gap reflects SPAC stigma and post-listing selling "
        "overhangs more than fundamentals: the stock spiked toward $80 within days of the April 2025 "
        "listing on a $37 billion implied valuation, then fell roughly 90% as the market priced it as "
        "a broken deal rather than a business. The second quarter of 2026 was the best in company "
        "history — record revenue, a $34.7 million pretax profit, and revenue growth leading scaled US "
        "retail brokers. Two or three more clean quarters, and the SPAC discount has no reason to "
        "persist. BUY.",
    ],
    "thesis_subhead": "Why own it",
    "thesis_bullets": [
        ("Cash is the floor, not the thesis. ",
         "$1.85 billion of net cash — ~44% of base-case fair value — near-zero debt, and ~$5 million "
         "of annual maintenance capex. Adjusted net income is, for practical purposes, owner earnings, "
         "which is why the model discounts it directly as free cash flow to equity."),
        ("A real, profitable business at scale. ",
         "$571 million of 2025 revenue and $84.2 million of adjusted net income (~15% margin), "
         "growing — not a concept stock burning cash to buy users."),
        ("The international option. ",
         "40-plus countries. If US payment for order flow is regulated away, the non-US growth engine "
         "is already built and compounding — the exact offset the bear case requires."),
        ("Self-clearing as a margin lever. ",
         "Clearing-cost takeout drops straight to the bottom line and scales with volume; the "
         "structural offset to marketing intensity in the base case."),
    ],
    "business": [
        "Webull Corporation, founded in 2016 by Anquan Wang (a former Alibaba executive) and "
        "headquartered in St. Petersburg, Florida, operates a commission-free, mobile-first trading "
        "platform aimed at self-directed retail investors. It launched in the United States in 2018, "
        "gained traction during the 2020–2021 retail trading wave, and — to address US-China regulatory "
        "concerns — separated from its Chinese parent, re-domiciled in the US, and went public in April "
        "2025 via a SPAC merger with SK Growth Opportunities Corp, listing on Nasdaq under ticker BULL.",
        "The platform differentiates on depth rather than simplicity: professional-grade charting, "
        "extended-hours trading, advanced order types, and paper-trading tools aimed at active "
        "self-directed investors — the highest-turnover, highest take-rate segment of the retail "
        "market. The footprint is the differentiator versus US-centric peers: licensed operations in "
        "40-plus markets spanning North America, Europe, Asia-Pacific, Latin America, and the Middle "
        "East, with 20 million-plus registered users globally. Revenue comes from four streams: payment "
        "for order flow (the dominant transaction line, especially options), net interest income on "
        "customer cash balances and securities lending, subscriptions (premium tiers with Level 2 data "
        "and margin-rate discounts), and relaunched crypto trading. The company is migrating toward "
        "self-clearing, which removes per-trade clearing fees and is the main structural margin lever "
        "over the model horizon.",
    ],
    "business_bullets": [
        ("Three compounding growth levers. ",
         "International markets (retail-investor populations earlier in their adoption curve than the "
         "US; analysts expect 25%+ annual revenue growth through 2027); the crypto trading relaunch "
         "(a high-margin, high-engagement product competitors monetize aggressively); and conversion — "
         "with 20 million-plus registered users against a much smaller funded-account base, each point "
         "of conversion is operating leverage."),
        ("Competitive position. ",
         "Webull sits between Robinhood (the larger US retail brand, similar PFOF dependence) and the "
         "incumbents (Schwab/Fidelity, scale and banking attach) on one side, and eToro/Interactive "
         "Brokers on international/social and pro-sumer axes on the other. Its edge is product depth "
         "for active traders plus a genuine multi-region footprint few retail brokerages have built."),
    ],
    "outlook": [
        "Profitability inflection is the story of 2026. The Q2 pretax profit of $34.7 million, on record "
        "revenue, suggests the business has crossed from growth-at-all-costs into scalable economics — "
        "payment for order flow and margin interest scale with volumes while the technology platform "
        "cost base grows more slowly. Our base case assumes this operating leverage continues and "
        "international markets contribute an increasing share of funded-account growth.",
        "The key variable we watch is not user growth but funded-account and asset growth: registered "
        "users are vanity, assets are revenue. Continued progress there, plus clean quarterly prints "
        "that bury the SPAC narrative, is what closes the valuation gap to Robinhood. Our model has "
        "2026 revenue of ~$790 million (+38% on the volume boom) fading toward single-digit growth by "
        "the early 2030s, with adjusted-net margins gliding to a normalized mid-cycle 18% — never "
        "peak-cycle margins.",
    ],
    "financials": [
        "Four revenue streams, two of them cyclical. Payment for order flow and crypto scale with "
        "retail trading volumes (the 2026 boom flatters both); net interest income scales with rates "
        "and customer cash balances; subscriptions are the only genuinely recurring line and the "
        "smallest. This is why the model treats reported operating cash flow with suspicion — brokerage "
        "free cash flow is polluted by customer and clearing-balance movements — and discounts "
        "adjusted net income as the FCFE proxy instead. The firm is net-cash with near-zero debt and "
        "~$5 million of annual maintenance capex, so adjusted net income is, for practical purposes, "
        "cash owner earnings.",
        "The base-case financial path (2025 actual, 2026+ projected): revenue $571M → ~$790M → ~$950M "
        "→ ~$1,090M (2025A–2028E), with revenue growth fading from the 2026 volume boom toward single "
        "digits by the early 2030s and margins gliding to a normalized mid-cycle 18%. The bear case "
        "models PFOF compression plus volume normalization explicitly — revenue crawling at 2.5% CAGR "
        "to $730 million by 2035 — and still yields $4.95, because the cash floor does the work.",
    ],
    "fin_table": {
        "headers": ["$ mn", "2025A", "2026E", "2027E", "2028E"],
        "rows": [
            ["Revenue", "571", "790", "950", "1,090"],
            ["Revenue growth", "—", "+38%", "+20%", "+15%"],
            ["Adjusted net income", "84.2", "~115", "~152", "~191"],
            ["Adjusted net margin", "14.7%", "14.5%", "16.0%", "17.5%"],
        ],
        "footnote": "2025 figures are company-reported. 2026+ are base-case model projections, not guidance.",
    },
    "moat": [
        ("Multi-region licensed footprint. ",
         "Licensed broker-dealer operations in 40-plus markets are expensive and slow to replicate; "
         "they give Webull growth avenues beyond the saturated US retail brokerage market and a "
         "natural hedge against US-centric regulation."),
        ("Active-trader product depth. ",
         "Extended-hours trading, deep options analytics, and paper trading create switching costs "
         "for the highest-turnover retail segment — the segment with the best unit economics."),
        ("Self-clearing cost structure. ",
         "Migrating clearing in-house removes per-trade third-party fees; the savings scale with "
         "volume and drop straight to the bottom line."),
        ("Balance-sheet optionality. ",
         "$1.85 billion of net cash funds international expansion and share repurchases without "
         "dilution — a luxury most growth brokerages do not have."),
    ],
    "risks": [
        ("US payment-for-order-flow ban or severe take-rate compression. ",
         "The single thesis-breaking risk. The EU ban is the template; if the SEC bans PFOF or "
         "take-rates compress ≥30% with no international offset, 2027 revenue falls below ~$700M and "
         "the bear case ($4.95) becomes the base — downgrade to REDUCE on confirmation."),
        ("Volume normalization. ",
         "Retail trading volumes are among the most cyclical series in finance. A quiet 2027–28 "
         "compresses PFOF and crypto revenue simultaneously; the model assumes the 2026 boom fades, "
         "but a deeper trough hits the base case."),
        ("Customer-acquisition intensity. ",
         "Retail brokerages rent growth with marketing spend. A CAC arms race against Robinhood and "
         "the incumbents keeps margins below the bull path; the base case assumes self-clearing "
         "savings only offset this drag."),
        ("Governance and track-record discount. ",
         "Short public history (listed April 2025), founder control, and SPAC provenance keep a "
         "structural discount in the multiple — priced in via the 12% base discount, but capable of "
         "widening on any misstep."),
        ("Regulatory contagion beyond PFOF. ",
         "Leverage caps, gamification scrutiny, and adjacent rules in the UK/EU could raise "
         "compliance costs or constrain the product in Webull's growth markets."),
    ],
    "falsification": "The BUY breaks if US payment for order flow is banned, or take-rates compress by "
        "≥30% with no international offset — operationalized as 2027 revenue below ~$700M. That outcome "
        "converts the bear case into the expected value and the $9 target with it; the rating would move "
        "to REDUCE/SELL on confirmation. Short of that, volume softness or margin pressure is already "
        "priced into the $4.95 bear that the weighted target absorbs. To the upside, three consecutive "
        "clean quarters with accelerating funded-account growth would justify revisiting fair value "
        "materially higher.",
    "valuation_method": "10-year scenario FCFE DCF (adjusted net income ≈ FCFE)",
    "valuation_intro": [
        "We value Webull on a 10-year scenario DCF on adjusted net income ≈ FCFE, weighted bear 25% / "
        "base 50% / bull 25%, with scenario-specific discounts: bear 14.5% (base + 250bp), base 12.0% "
        "(the speculative tier — PFOF regulatory overhang, volume cyclicality, governance discount), "
        "bull 10.5% (base – 150bp). Terminal growth is 1.0% / 2.0% / 2.5% on year-10 earnings at "
        "normalized mid-cycle margins (14% / 18% / 20%) — never peak margins. Net cash of $1,847M is "
        "added to enterprise value in all scenarios; bear-case share count is 500M (dilution under "
        "stress) versus 475M in base/bull. Terminal value is 31–55% of EV across scenarios — no "
        "TV-dependence haircut needed.",
        "What the price implies: at $7.34, the market values the operating business at ~$3.45 a share "
        "ex-cash — below the operating value of the base case ($8.78 − $3.89 cash = $4.89 a share). "
        "The market prices the operating business as though the PFOF bear case is the expected "
        "outcome, while paying nothing for the international growth option or self-clearing leverage. "
        "That asymmetry is the BUY.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 4.95,
            "assumptions": "US take-rates compressed ~30%, European PFOF economics dead, revenue "
                "crawling at 2.5% CAGR to $730M by 2035, marketing stays intense, governance "
                "discount persists.",
            "rev_cagr": "+2.5%", "margin_end": "14%",
            "discount": 0.145, "terminal_g": 0.010, "tv_share": 0.31,
            "pv_explicit": 430.0, "pv_terminal": 197.0, "cashflow_unit": "$mn",
        },
        "base": {
            "fair_value": 8.78,
            "assumptions": "11.9% revenue CAGR fading to single digits, adjusted-net margins settling "
                "at a mid-cycle 18%, self-clearing savings offsetting marketing intensity.",
            "rev_cagr": "+11.9%", "margin_end": "18%",
            "discount": 0.120, "terminal_g": 0.020, "tv_share": 0.45,
            "pv_explicit": 1281.0, "pv_terminal": 1040.0, "cashflow_unit": "$mn",
        },
        "bull": {
            "fair_value": 13.12,
            "assumptions": "Webull closes a meaningful portion of the Robinhood multiple gap as clean "
                "quarters accumulate; international conversion and crypto scale together.",
            "rev_cagr": "+16.1%", "margin_end": "20%",
            "discount": 0.105, "terminal_g": 0.025, "tv_share": 0.55,
            "pv_explicit": 1981.0, "pv_terminal": 2406.0, "cashflow_unit": "$mn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Probability-weighted DCF value is $8.91 (0.25×$4.95 + 0.50×$8.78 + 0.25×$13.12), "
        "rounded to our $9 target. Composition is on an EV basis; $1,847M of net cash is added to "
        "reach equity fair value in every scenario.",
    "charts": {
        "scenario": {"bear": 4.95, "base": 8.78, "bull": 13.12, "weighted": 9.00, "price": 7.34},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [0.39, 0.39, 0.39, 0.57],
            "fcf_hist": [-0.06, 0.47, 0.18, 0.56],
            "years_proj": list(range(2026, 2036)),
            "revenue_proj": [round(x / 1000, 3) for x in rev_proj],
            "fcf_proj": [round(x / 1000, 3) for x in ni_proj],
            "unit": "$bn", "fcf_label": "Adj. net income (≈FCFE)",
            "note": "History: revenue and operating-CF-minus-capex (Yahoo). Projection: base-case "
                "adjusted net income, the series the DCF discounts as FCFE. Shaded = projection.",
        },
        "composition": {
            "bear": {"pv_explicit": 430.0, "pv_terminal": 197.0},
            "base": {"pv_explicit": 1281.0, "pv_terminal": 1040.0},
            "bull": {"pv_explicit": 1981.0, "pv_terminal": 2406.0},
            "unit": "$mn",
        },
    },
}

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "output", "BULL-equity-research-note-polished.pdf")
    print(build_note(data, out))
