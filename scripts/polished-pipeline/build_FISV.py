"""Polished note build: Fiserv (FISV). Scenario numbers from the authoritative
October 2026 hardened 10-year DCF: bear $13.50 / base $60.12 / bull $100.22, weighted $58.
Re-runnable."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

# DCF composition: net debt $25.3bn / 535mn sh = $47.29/sh of leverage per share
ND_PS = 25.3e9 / 535e6  # 47.29
def ev_split(fv, tv):
    ev = fv + ND_PS
    t = round(ev * tv, 2)
    return round(ev - t, 2), t

bear_e, bear_t = ev_split(13.50, 0.50)
base_e, base_t = ev_split(60.12, 0.58)
bull_e, bull_t = ev_split(100.22, 0.62)

# Base revenue path: 2026E ~$22.0bn at 4.5% CAGR; FCF margin ~20% toward 21.5%
rev_proj = [22.0]
for _ in range(10):
    rev_proj.append(round(rev_proj[-1] * 1.045, 2))
margins = [0.20 + 0.0015 * i for i in range(11)]
fcf_proj = [round(r * m, 2) for r, m in zip(rev_proj, margins)]

data = {
    "ticker": "FISV",
    "company": "Fiserv, Inc.",
    "exchange": "NASDAQ",
    "sector": "Technology — Payments & Financial Technology",
    "verdict": "BUY",
    "fair_value": 58.00,
    "price": 44.36,
    "risk": "High",
    "headline": "A Durable Payments Franchise at a Narrative Discount — a Speculative BUY",
    "snapshot": [
        ("Market cap", "~$23.7 bn (535 mn sh × $44.36)"),
        ("Enterprise value", "~$49 bn"),
        ("Net debt", "$25.3 bn (≈ market cap)"),
        ("52-week range", "~$43.87 – $128.78"),
        ("Segments", "Merchant Solutions (Clover); Financial Solutions"),
        ("Recurring revenue", "~84%"),
        ("FCF conversion", "~112%"),
        ("2027E FCF/share", "~$8.16 (base case)"),
        ("Overhangs", "Two guidance resets; CEO transition"),
        ("Implied upside", "+31% to $58.00 fair value"),
    ],
    "thesis": [
        "Fiserv is the quiet infrastructure of American small-business payments. Clover, its point-of-"
        "sale platform, continues to take share among small and mid-size merchants; the core-account "
        "processing business serves thousands of banks and credit unions that renew because switching "
        "is operationally painful. The stock's 2025–2026 weakness — driven by a growth deceleration "
        "and a CEO transition overhang — has compressed the multiple to a level that no longer reflects "
        "the durability of the franchise.",
        "Our judgment is that the deceleration is cyclical and mix-related, not structural. Clover's "
        "competitive position against Square, Toast, and Stripe Terminal remains strong on distribution "
        "(bank and ISO channels) and on integrated software depth; the core processing business is as "
        "sticky as it has ever been. We haircut the growth targets where the evidence warrants — "
        "particularly on the pace of the Clover international rollout — but the base business earns its "
        "multiple.",
        "At $44.36, the market prices roughly a 35–40% weight on the distress bear — a decade of "
        "shrinkage discounted like a failing credit, with almost nothing paid for the turnaround option. "
        "That is an odd price for a business generating $4 billion-plus of through-cycle free cash flow "
        "at 112% conversion with the best small-business acquiring asset in the industry. Our "
        "probability-weighted fair value is $58.00, a 31% expected return, driven by re-accelerating "
        "organic growth, margin expansion from the efficiency programs, and continued buybacks.",
        "Start with what has not changed: Fiserv processes an enormous share of US financial "
        "transactions, serves thousands of financial institutions with core systems they cannot easily "
        "replace, and converts a high proportion of earnings to cash. Businesses like this do not become "
        "impaired in eighteen months; they get mispriced when growth wobbles and the narrative turns. "
        "The current price is a narrative discount on a durable franchise — which is why this is a "
        "speculative BUY: the expected value compensates for a real left tail, but the left tail is "
        "real.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("Clover's distribution advantage is structural, not cyclical. ",
         "Unlike direct-to-merchant competitors, Clover reaches small businesses through banks and "
         "ISOs that already own the merchant relationship, which lowers acquisition cost and improves "
         "retention. The integrated software suite raises switching costs with each module adopted. "
         "Clover volume growth has held up against the industry — the cleanest competitive read."),
        ("The efficiency program is the margin lever the market is ignoring. ",
         "Fiserv has a long record of extracting cost synergies, and the current program targets the "
         "overhead accumulated through years of acquisitions. We underwrite only the announced, "
         "trackable savings in the base case; faster realization is bull-case upside."),
        ("The base case only needs 4.5% growth. ",
         "At a 12% discount against $25.3 billion of net debt, the base fair value of $60.12 is just "
         "7.4x 2027E FCF/share (~$8.16) — barely a 10% premium to the peer band, justified by 84% "
         "recurring revenue and 112% FCF conversion."),
    ],
    "business": [
        "Fiserv provides payments and financial-services technology. The Merchant Solutions segment "
        "(anchored by Clover) offers point-of-sale hardware, payment processing, and integrated "
        "business software to merchants of all sizes. The Financial Solutions segment provides core "
        "account processing, digital banking, payments, and risk tools to banks and credit unions. "
        "Revenue is heavily recurring (~84%), and client retention in core processing is among the "
        "highest in financial technology.",
        "The economics combine a growth engine (Clover, expanding internationally and upmarket) with a "
        "cash cow (core processing, high retention, incremental margins on cross-sold modules). Free "
        "cash flow conversion is strong (~112%), and the company has a long history of returning capital "
        "through buybacks.",
        "Merchant Solutions is the growth segment: Clover point-of-sale, e-commerce processing, and "
        "enterprise merchant acquiring, diversified across retail, restaurant, and services verticals. The "
        "international rollout, though early, opens a second growth vector. Financial Solutions is the "
        "stability segment: core account processing, digital banking, electronic payments (including "
        "Zelle and bill-pay infrastructure), and risk management — multi-year contracts, extremely high "
        "retention, high incremental margins.",
    ],
    "business_bullets": [
        ("Clover: the best SMB acquiring asset. ",
         "Distribution through banks and ISOs plus integrated software depth; the international "
         "rollout is the swing factor, modeled conservatively because cross-border payments rollouts "
         "have a history of slipping."),
        ("Core processing: the ballast. ",
         "The real-time payments wave (FedNow and RTP adoption) creates a multi-year module-adoption "
         "cycle across the installed base — slow, high-margin, highly visible growth."),
        ("Capital allocation as the compounding kicker. ",
         "With leverage now manageable, free cash flow should fund buybacks at a pace that retires a "
         "mid-single-digit percentage of shares annually, plus a growing dividend."),
    ],
    "outlook": [
        "Where is this business going? We expect Clover to remain the growth engine: the US "
        "small-business digitization wave still has room, the ISO and bank referral channels give Clover "
        "distribution that pure-play competitors cannot easily replicate, and the software attach "
        "(inventory, payroll, lending) raises revenue per merchant each year. We expect the merchant "
        "deceleration to prove temporary — a normalization of small-business formation and spending "
        "rather than share loss — with Clover's volume growth re-accelerating toward its historical "
        "premium to the industry as headwinds fade.",
        "The core processing business should grow in the low-to-mid single digits, driven by digital "
        "banking adoption and real-time payments modules sold into the installed base. Combined with "
        "the efficiency programs, this yields operating leverage: we expect margins to expand even as "
        "the company invests in Clover's growth. Capital allocation should remain buyback-heavy, "
        "compounding per-share results.",
        "The international business is the upside surprise candidate: early results in Latin America and "
        "other markets suggest the playbook travels, though we model it conservatively. Our bear case "
        "assumes Clover share losses to competitors, a deeper deceleration in the merchant segment, and "
        "stalled margin programs — a decade of −1% revenue compounding that leaves equity at $13.50, "
        "70% below the quote.",
    ],
    "financials": [
        "Revenue has grown from $17.74 billion in 2022 to $21.19 billion trailing in 2025, with free "
        "cash flow of $3.14 billion → $4.30 billion over the same period — through-cycle cash generation "
        "above $4 billion at ~112% conversion. The P&L through the wobble is the point: the franchise "
        "kept compounding cash while the narrative broke.",
        "The balance sheet is the constraint and the opportunity. Net debt of $25.3 billion is roughly "
        "equal to the market capitalization, which is why the base discount is a non-negotiable 12% and "
        "why FCF misses are equity disasters in the bear case. Against that, the bull case ($100.22) "
        "needs 6.5% compounding, margins recovering toward 23.5%, and the strategic review converting "
        "into actual de-levering.",
    ],
    "fin_table": {
        "headers": ["$ bn", "2022", "2023", "2024", "2025 (TTM)"],
        "rows": [
            ["Revenue", "17.74", "19.09", "20.46", "21.19"],
            ["Free cash flow", "3.14", "3.77", "5.06", "4.30"],
            ["Net debt", "—", "—", "—", "25.3"],
        ],
        "footnote": "Sources: company filings via Yahoo Finance (2025 = TTM); net debt per October 2026 note.",
    },
    "moat": [
        ("Clover's bank/ISO distribution. ",
         "Reaching merchants through banks and ISOs that own the relationship lowers acquisition cost "
         "and improves retention versus direct-to-merchant competitors."),
        ("Core-processing switching costs. ",
         "Multi-year contracts with extremely high retention; replacing core systems is operationally "
         "painful for banks."),
        ("Integrated software depth. ",
         "Payments plus operating tools raise switching costs with each module adopted and raise "
         "revenue per merchant each year."),
        ("Scale in payments. ",
         "An enormous share of US financial transactions flows across Fiserv rails — a data and "
         "scale advantage in fraud, risk, and authorization."),
    ],
    "valuation_method": "10-year scenario FCF DCF (leverage-aware)",
    "valuation_intro": [
        "We value Fiserv on a leverage-aware 10-year free-cash-flow DCF — weights bear 25% / base 50% "
        "/ bull 25% — with scenario-specific discounts: bear 14.5% (base + 250bp), base 12.0% "
        "(speculative: net debt ≈ market cap, two guidance resets, three CEOs since May 2025), bull "
        "10.5% (base − 150bp). Terminal growth is capped at 1.0% / 2.5% / 2.5% on year-10 FCF at "
        "normalized mid-cycle margins, never peak margins. $25.3 billion of net debt is subtracted from "
        "the levered enterprise value.",
        "Scenario fair values: bear $13.50 (−1.0% revenue CAGR, 18.0% year-10 FCF margin), base $60.12 "
        "(+4.5% revenue CAGR, 21.5% year-10 FCF margin), bull $100.22 (+6.5% revenue CAGR, 23.5% "
        "year-10 FCF margin). Probability-weighted: 0.25×$13.50 + 0.50×$60.12 + 0.25×$100.22 = $58.49, "
        "published as the $58 target.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 13.50,
            "assumptions": "Decade of −1% revenue compounding: legacy drag plus Clover stalling; leverage compounds through the downturn; equity disaster at 14.5%",
            "rev_cagr": "−1.0%", "margin_end": "18.0%",
            "discount": 0.145, "terminal_g": 0.01, "tv_share": 0.50,
            "pv_explicit": bear_e, "pv_terminal": bear_t, "cashflow_unit": "$/sh",
        },
        "base": {
            "fair_value": 60.12,
            "assumptions": "Organic growth re-accelerates to 4.5% led by Clover; margin expansion from efficiency programs; steady buybacks; 7.4x 2027E FCF/share",
            "rev_cagr": "+4.5%", "margin_end": "21.5%",
            "discount": 0.12, "terminal_g": 0.025, "tv_share": 0.58,
            "pv_explicit": base_e, "pv_terminal": base_t, "cashflow_unit": "$/sh",
        },
        "bull": {
            "fair_value": 100.22,
            "assumptions": "Faster Clover international traction; stronger operating leverage toward 23.5% FCF margin; strategic review converts into actual de-levering",
            "rev_cagr": "+6.5%", "margin_end": "23.5%",
            "discount": 0.105, "terminal_g": 0.025, "tv_share": 0.62,
            "pv_explicit": bull_e, "pv_terminal": bull_t, "cashflow_unit": "$/sh",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "risks": [
        ("A third guidance cut. ",
         "Two resets in ten months is already credibility-destroying; a third means the base case's "
         "4.5% revenue CAGR is fantasy and the bear's weight should rise toward 50%+."),
        ("Leverage compounding through a downturn. ",
         "Net debt ≈ market cap means FCF misses are equity disasters; a recession that stalls "
         "merchant volume flows straight to the $13.50 bear."),
        ("Clover competition. ",
         "Square, Toast, Stripe, and Adyen compete aggressively for the same merchants, pressuring "
         "pricing and win rates."),
        ("Execution. ",
         "The CEO transition and efficiency programs introduce operational risk."),
        ("Macro. ",
         "Consumer-spending weakness flows directly to payments volume."),
        ("Fintech disruption. ",
         "Embedded finance and software-led payments could bypass traditional processors over time."),
    ],
    "falsification": (
        "Downgrade to HOLD if Clover volume growth trails the industry for several consecutive quarters "
        "(competitive share loss), if organic revenue growth stays in the low-single digits beyond the "
        "current slowdown (structural problem), or if margins contract despite the efficiency programs "
        "(operating-leverage thesis broken). A third guidance cut, or client retention deteriorating in "
        "core processing, would each independently force a re-underwrite."
    ),
    "charts": {
        "scenario": {"bear": 13.50, "base": 60.12, "bull": 100.22,
                     "weighted": 58.00, "price": 44.36},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [17.737, 19.093, 20.456, 21.193],
            "fcf_hist": [3.139, 3.774, 5.062, 4.299],
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": rev_proj,
            "fcf_proj": fcf_proj,
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via Yahoo Finance (2025 = TTM). Projection: illustrative "
                    "base-case path at 4.5% revenue CAGR with FCF margins ~20–21.5%.",
        },
        "composition": {
            "bear": {"pv_explicit": bear_e, "pv_terminal": bear_t},
            "base": {"pv_explicit": base_e, "pv_terminal": base_t},
            "bull": {"pv_explicit": bull_e, "pv_terminal": bull_t},
            "unit": "$/sh",
        },
        "extra": {
            "type": "line",
            "title": "Revenue — reported history vs. base-case path ($bn)",
            "years": [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "series": [
                {"label": "Reported", "values": [17.737, 19.093, 20.456, 21.193, None, None, None, None, None, None, None, None, None, None, None]},
                {"label": "Base case", "values": [None, None, None, None] + rev_proj},
            ],
            "ylabel": "$bn",
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "FISV-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
