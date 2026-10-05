"""Sample build: WYNN polished note end-to-end via template.build_note."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

data = {
    "ticker": "WYNN",
    "company": "Wynn Resorts, Limited",
    "exchange": "NASDAQ",
    "sector": "Consumer Discretionary — Casinos & Gaming",
    "verdict": "BUY",
    "fair_value": 153.00,
    "price": 75.88,
    "risk": "High",
    "headline": "The Capex Wall Is Ending; the Market Is Pricing the Bear Case",
    "ceo": "Craig Billings",
    "hq": "Las Vegas, Nevada",
    "snapshot": [
        ("Market cap", "~$7.8 bn (103 mn sh × $75.88)"),
        ("Enterprise value", "~$17.6 bn"),
        ("Net debt", "~$8.5–9.2 bn; leverage ~4–4.4x EBITDAR"),
        ("52-week range", "~$75.75 – $134.72"),
        ("2026E revenue / EBITDAR", "$7.5 bn / $2.27 bn"),
        ("Dividend", "$0.25/share quarterly (maintained)"),
        ("Buyback authorization", "$326 mn remaining (mid-2026)"),
        ("Next catalyst", "Wynn Al Marjan Island opening, Sep 2027"),
        ("Sell-side view", "JPMorgan assigns ~$0 value to UAE (Sep 2026)"),
        ("Macau concession", "10-year license to end-2032; no renewal risk"),
    ],
    "thesis": [
        "Wynn is trading like a company whose biggest growth project will never pay off. "
        "At $75.88, the equity is priced within shouting distance of our bear case ($52.08) — "
        "which assumes Macau revenue declines early in the forecast, the UAE project arrives "
        "late and small (a 58% haircut to company guidance, delayed to mid-2028), a $300 million "
        "equity call on cost overruns, and a punitive 14.5% discount rate. The market is pricing "
        "roughly the bear case as the expected outcome. That is the mispricing.",
        "Our 10-year scenario DCF says even the base case — discounted at 12%, with the UAE "
        "contribution haircut 25% below management's own guide, and roughly $110 million a year "
        "of Wynn Macau minority leakage priced in every year — is worth $140.13. The weighted "
        "fair value (bear 25% / base 50% / bull 25%) is $153, +101.6% above the current price. "
        "The math works because of a single, highly visible inflection: Wynn's capex wall ends. "
        "Our model has free cash flow to equity inflecting from roughly $110 million in 2027 to "
        "$1.0–2.3 billion per year from 2029, as the UAE and Enclave build programs complete and "
        "the assets start spinning cash. Right now investors are capitalizing the capex-heavy "
        "trough as if it were permanent; within three years the same company could be distributing "
        "double-digit percentages of its current market cap annually.",
        "The valuation is deliberately hardened against optimism. The scenario DCF runs ten "
        "years so the UAE and Enclave economics actually appear in the numbers. Terminal growth "
        "is capped at 2.5% on normalized mid-cycle margins — never peak margins. Each scenario "
        "carries its own discount rate: 14.5% for the bear's distress pricing, 12% for the base, "
        "10.5% for the bull. There is no multiple overrule and no anchoring to management's guide "
        "numbers: project economics are haircut, not guided. The target is the weighted DCF: $153. "
        "The rating is BUY.",
        "The bear case is genuinely priced in, so the asymmetry favors holders. At $75.88, even a "
        "mild derisking — the UAE opens on time, Macau gross gaming revenue merely stabilizes — "
        "forces the price toward the $140 base case. The core business is not broken: Wynn Las Vegas "
        "set a record monthly EBITDAR in May 2026, group EBITDAR annualizes above $2.2 billion, and "
        "Las Vegas margins run 35%+. The stock's 37% one-year decline is a narrative discount — Macau "
        "softness and headlines around the UAE budget — not an operating collapse.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("The capex wall is the story, and it has a calendar. ",
         "Wynn Al Marjan Island (40%-owned, the UAE's only licensed integrated resort, on a "
         "15-year exclusive renewable license) opens September 2027; the $900–950 million Enclave "
         "tower at Wynn Palace follows in early 2029. After that, Wynn is a harvest machine: two "
         "flagship growth assets fully built, with the base business alone throwing off over $2 "
         "billion of FCFE in our 2036 base year."),
        ("Investors currently assign the UAE project roughly zero value. ",
         "It is a $5.1 billion project, 67% spent or contracted, tower topped out, 22,000 workers "
         "on site, company-guided at $390–570 million of stabilized property EBITDA. We haircut "
         "that guide 25% and still get $144 million of annual Wynn-side EBITDA from 2031. Zero is "
         "not a haircut; it is a refusal to do the arithmetic."),
        ("Leverage is the reason this is a High-risk BUY, not a slam dunk. ",
         "Equity value here is levered to the timing of cash flows, which is precisely why the "
         "capex wall ending matters so much: the $900 million-plus of 2027–28 growth capex is the "
         "entire reason the price is $75.88, and it is a two-year problem with a known end date."),
    ],
    "business": [
        "Wynn Resorts operates ultra-luxury integrated resorts — the company claims more Forbes "
        "Travel Guide Five-Star Awards than any other independent hotel company in 2026. The "
        "operating footprint is four properties: Wynn Las Vegas / Encore (4,748 rooms, the "
        "highest-margin segment at roughly 35% EBITDAR), Encore Boston Harbor (a stable regional "
        "cash cow at roughly 28% margins), and Wynn Macau and Wynn Palace (the Cotai flagship). A "
        "fifth property, the Wynn Mayfair private members' club in London, was acquired in June 2025; "
        "it is immaterial to earnings but useful as a European and Middle East feeder for the UAE "
        "resort. The WynnBET/iGaming operation was effectively wound down in 2023–24.",
        "The FY2025 mix (company-reported): revenue $7.14 billion, Adjusted Property EBITDAR "
        "$2.22 billion at a 31.2% margin. Macau was roughly 52% of revenue and 49% of EBITDAR — "
        "the single largest driver of both earnings and volatility. Wynn's Macau market share has "
        "recovered to about 13% of gross gaming revenue (3Q25), skewed toward premium-mass and VIP. "
        "The 10-year gaming concession signed in December 2022 runs to end-2032, so there is no "
        "near-term renewal risk.",
        "Two growth assets are under construction — and both are in the valuation, with haircuts, "
        "not with management's numbers.",
    ],
    "business_bullets": [
        ("Wynn Al Marjan Island, Ras Al Khaimah (40% joint venture). ",
         "$5.1 billion budget (raised $600 million in August 2026 on conflict-related logistics "
         "costs), 1,530 rooms, 275 tables, 2,000+ machines, and the first and only UAE gaming "
         "license (15-year exclusive, renewable). Opening September 2027; the company guides "
         "$390–570 million of stabilized property EBITDA on roughly $1.33 billion of base-case "
         "gross gaming revenue. Our model takes a 25% haircut to the guide — 40% of $360 million "
         "projected EBITDA, or $144 million of annual Wynn-side EBITDA from 2031 — and still spends "
         "the remaining roughly $550 million of Wynn's equity share over 2027–28."),
        ("The Enclave at Wynn Palace. ",
         "A $900–950 million all-suite tower (432 suites, no gaming) fulfilling non-gaming "
         "concession commitments; opens early 2029. The company guides roughly $400 million of "
         "revenue and $150–175 million of EBITDA. We haircut to $320 million of revenue and $120 "
         "million of EBITDA — still a 12%+ yield on cost."),
        ("Spending the last of the wall. ",
         "Remaining equity for the UAE (roughly $550 million) and the Enclave (roughly $925 million "
         "total) flows out over 2027–28; then growth capex collapses to maintenance of roughly "
         "$400–478 million per year."),
        ("Terming out the 2027–29 maturity wall. ",
         "$2.86 billion due in 2027 and $2.54 billion in 2028 (including the Wynn Macau converts "
         "puttable March 2027); a $900 million 2035 senior-notes offering launched in September 2026 "
         "extends duration."),
        ("Returning cash while it builds. ",
         "The $0.25/share quarterly dividend was maintained through 2026; $129 million of buybacks "
         "were executed in H1 2026 with $326 million of authorization remaining at mid-year."),
        ("Exited distractions. ",
         "The $12 billion Hudson Yards New York casino bid was withdrawn in May 2025; capital is "
         "now concentrated on the UAE, the Enclave, and buybacks."),
    ],
    "outlook": [
        "The next three years are a two-act story: finish spending, then harvest. Through 2028, "
        "Wynn remains a construction company that happens to own casinos — roughly $1.5 billion of "
        "remaining growth equity flows out the door, free cash flow to equity stays thin, and the "
        "stock will trade on construction milestones and Macau monthly prints. The key markers are "
        "binary and observable: the Al Marjan tower opening on schedule in September 2027, the "
        "Enclave topping out for its early-2029 opening, and the 2027–28 refinancings pricing at "
        "non-distressed spreads.",
        "From 2029, the business model flips. With both growth assets open and growth capex collapsed "
        "to maintenance, base-case FCFE runs $1.0–2.3 billion a year against a $7.8 billion market "
        "cap — a 13–30% free-cash-flow yield on today's price. That cash has three competing uses: "
        "deleveraging from 4–4.4x toward 3x, the maintained $0.25 quarterly dividend, and buybacks "
        "against the remaining $326 million authorization and whatever follows. Management's revealed "
        "preference — returning cash while building, exiting the Hudson Yards distraction — suggests "
        "shareholders, not empire-building, get the harvest.",
        "The two swing factors over the horizon are Macau mix and the UAE ramp. In Macau, Wynn's "
        "13% gross-gaming-revenue share skewed to premium-mass is the highest-margin exposure of "
        "any concessionaire; every point of share regained toward the 2019 level of 14.6% falls "
        "through at 30%+ margins. In the UAE, the range of outcomes is genuinely wide — a licensed "
        "monopoly in a wealthy catchment with no competing supply — which is why the note haircuts "
        "the guide 25% in the base case and 58% in the bear case rather than picking a point estimate. "
        "Even the haircut case adds $144 million of annual Wynn-side EBITDA from 2031; the market's "
        "implied zero is the single largest gap between price and value in the note.",
    ],
    "financials": [
        "Total debt was roughly $10.6 billion at mid-2026 (about $10.72 billion including lease "
        "liabilities) against cash of roughly $1.57 billion — net debt of $8.5–9.2 billion on "
        "management's definition, putting net leverage at roughly 4–4.4x EBITDAR. Interest runs "
        "about $600 million per year in our model. The 2027–29 maturity wall ($2.86 billion / "
        "$2.54 billion / $1.79 billion) is being addressed through the 2035 notes offering, but "
        "refinancing happens at today's wider spreads — our bear case prices exactly that. "
        "Leverage is the constraint on the whole call: equity value is levered to the timing of "
        "cash flows, which is why the capex wall ending matters so much.",
        "The FCFE bridge is explicit. Our 10-year construction per year: EBITDAR minus corporate "
        "costs, interest, tax, maintenance capex, UAE equity capex, Enclave capex, other growth "
        "capex, and Wynn Macau minority leakage (roughly $110 million per year, growing). Base-case "
        "FCFE runs $110 million (2027) → $417 million (2028) → $1,011 million (2029) and compounds "
        "to $2.3 billion by 2036. The $900 million-plus of 2027–28 growth capex is the entire reason "
        "the price is $75.88; it is also a two-year problem with a known end date.",
    ],
    "fin_table": {
        "headers": ["$ mn", "FY2024", "FY2025", "Q2'26", "H1'26"],
        "rows": [
            ["Operating revenue", "7,128", "7,138", "1,861", "3,723"],
            ["YoY growth", "—", "+0.1%", "+6.9%", "—"],
            ["Adj. Property EBITDAR", "2,365", "2,224", "568", "1,131"],
            ["EBITDAR margin", "33.2%", "31.2%", "30.5%", "30.4%"],
            ["Net income (attrib.)", "501", "327", "140", "261"],
            ["Diluted EPS", "$4.35", "$3.14", "$1.32", "—"],
            ["Operating cash flow", "1,426", "1,353", "—", "—"],
            ["Free cash flow", "1,006", "692", "—", "—"],
        ],
        "footnote": "Sources: company 10-K, earnings releases (Aug 4, 2026), 10-Q filings. — = not disclosed quarterly.",
    },
    "moat": [
        ("The luxury brand is the moat. ",
         "Wynn's Five-Star positioning commands the industry's highest average daily rates and "
         "gaming yields; Las Vegas EBITDAR margins (35%) are the portfolio's best. Luxury "
         "customers are the least price-sensitive segment of a cyclical industry — a durable, "
         "if not impregnable, advantage."),
        ("A genuine regulatory moat in the UAE. ",
         "Wynn holds the UAE's only commercial gaming license — 15-year exclusive, renewable, "
         "for Ras Al Khaimah. MGM has formally applied and analysts expect up to four integrated "
         "resorts eventually, but Wynn expects to be 'the only one for quite some time.' A license "
         "monopoly in a $3–5 billion-plus gross-gaming-revenue market is the closest thing to a "
         "moat this industry offers."),
        ("Macau is the moat's weak link. ",
         "Six concessionaires compete for the same premium-mass pool; Wynn's roughly 13% gross "
         "gaming revenue share is below its 2019 level of 14.6%. Premium positioning wins margin "
         "but amplifies VIP volatility — the segment that whipsaws on China macro headlines."),
        ("Las Vegas: share of a premium niche. ",
         "MGM and Caesars dominate the Strip by scale; Wynn wins the ultra-luxury sliver. That "
         "works while visitation holds; Strip visitation fell 6% in 2025 before the 2026 recovery."),
    ],
    "valuation_method": "10-year scenario FCFE DCF",
    "valuation_intro": [
        "We value Wynn on a 10-year scenario free-cash-flow-to-equity DCF — weights bear 25% / "
        "base 50% / bull 25% — with scenario-specific discounts: bear 14.5% (base + 250bp, "
        "distress pricing: derated terminal, refinancing at wider spreads, deferred maintenance), "
        "base 12.0% (levered equity with two development projects), bull 10.5% (base − 150bp). "
        "Terminal growth is 1.0% / 2.0% / 2.5% on year-10 FCFE computed at normalized mid-cycle "
        "EBITDAR margins (28% / 31% / 32%) — never peak margins.",
        "Project economics are haircut, not guided: the UAE at 25% below company guide, the Enclave "
        "at 20% below, and Wynn Macau minority leakage of roughly $110 million per year priced "
        "through the whole forecast. Verified diluted share count: 102.97 million.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 52.08,
            "assumptions": "Macau revenue declines in 2027–28; UAE opens mid-2028 with economics 58% below guide; $300M equity call on overruns; refinancing at wider spreads",
            "rev_cagr": "+2.5%", "margin_end": "28%",
            "discount": 0.145, "terminal_g": 0.01, "tv_share": 0.48,
            "pv_explicit": 2788, "pv_terminal": 2575, "cashflow_unit": "$mn",
        },
        "base": {
            "fair_value": 140.13,
            "assumptions": "Capex wall ends on schedule; UAE opens Sep 2027 at 25% below guide ($144M/yr Wynn-side EBITDA from 2031); Enclave early 2029 at 20% below guide; Macau stabilizes",
            "rev_cagr": "+4.6%", "margin_end": "31%",
            "discount": 0.12, "terminal_g": 0.02, "tv_share": 0.53,
            "pv_explicit": 6829, "pv_terminal": 7600, "cashflow_unit": "$mn",
        },
        "bull": {
            "fair_value": 277.74,
            "assumptions": "UAE ramps to guide; Macau premium-mass share gains continue; Enclave yields above 12% on cost; leverage falls below 3x by 2030 enabling large buybacks",
            "rev_cagr": "+7.3%", "margin_end": "32%",
            "discount": 0.105, "terminal_g": 0.025, "tv_share": 0.59,
            "pv_explicit": 11811, "pv_terminal": 16788, "cashflow_unit": "$mn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "risks": [
        ("UAE execution and timing. ",
         "Construction delays or a slow ramp in a first-of-its-kind gaming jurisdiction would "
         "defer the cash-flow inflection the whole call rests on; conflict-related logistics "
         "costs have already added $600 million to the budget."),
        ("Leverage and refinancing. ",
         "Roughly $5.4 billion matures in 2027–28; punitive refinancing terms would divert cash "
         "from the inflection to creditors. The bear case prices exactly this."),
        ("Macau concentration. ",
         "Roughly half of revenue and EBITDAR sits in Macau; license conditions, table "
         "allocations, and government policy can move earnings faster than any model."),
        ("US–China tensions. ",
         "Geopolitical friction can hit Macau visitation and sentiment independent of Wynn's "
         "execution, and it colors how the market prices the equity's China exposure."),
    ],
    "falsification": (
        "Downgrade to HOLD if Macau gross gaming revenue declines through Q4 2026 (breaking the "
        "base case's core-revenue path from the inside), combined with UAE capex rising above $7.5 "
        "billion or the opening pushed past September 2027 — either development outcome invalidates "
        "the capex-wall-ending thesis the whole call rests on. Separately, a failed refinancing of "
        "the 2027 maturities at anything approaching distress pricing would force a re-underwrite "
        "of the entire capital structure. We watch: Macau GGR prints, UAE construction milestones "
        "and budget updates, and the pricing on the 2027–28 refinancings."
    ),
    "charts": {
        "scenario": {"bear": 52.08, "base": 140.13, "bull": 277.74,
                     "weighted": 153.00, "price": 75.88},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [3.757, 6.532, 7.128, 7.138],
            "fcf_hist": [-0.384, 0.794, 1.004, 0.692],
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": [7.5, 7.650, 7.956, 8.394, 8.463, 9.037, 9.582, 10.142, 10.665, 11.198, 11.742],
            "fcf_proj": [None, 0.110, 0.417, 1.011, 1.228, 1.501, 1.705, 1.868, 2.014, 2.162, 2.314],
            "unit": "$bn", "fcf_label": "FCFE",
            "note": "History: company filings (FCF = operating cash flow less capex). "
                    "Projection: base-case FCFE from the scenario DCF; 2026E revenue per company outlook.",
        },
        "composition": {
            "bear": {"pv_explicit": 2788, "pv_terminal": 2575},
            "base": {"pv_explicit": 6829, "pv_terminal": 7600},
            "bull": {"pv_explicit": 11811, "pv_terminal": 16788},
            "unit": "$mn",
        },
        "extra": {
            "type": "line",
            "title": "Adjusted property EBITDAR margin — history vs. base case",
            "years": [2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "series": [{"label": "EBITDAR margin",
                        "values": [33.2, 31.2, 30.3, 29.8, 30.8, 32.6, 32.3, 33.4, 33.8, 33.6, 33.5, 33.4, 33.2]}],
            "ylabel": "%",
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "samples",
                   "WYNN-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
