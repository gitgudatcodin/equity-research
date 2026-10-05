"""SPGI polished note. Research analysis, not investment advice.

Scenario numbers: authoritative hardened re-run (~/workspace/spgi-research/spgi_v2_hardened_model.py),
same numbers as the published standalone note.
Bear $118.34 / base $321.46 / bull $601.51, weighted $341.29 -> $341 target.
History: yfinance annuals. Projection: base-case model series (FY2027-2035).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

data = {
    "ticker": "SPGI",
    "company": "S&P Global Inc.",
    "exchange": "NYSE",
    "sector": "Financials — Data, Ratings & Indices",
    "verdict": "REDUCE",
    "fair_value": 341.00,
    "price": 386.27,
    "risk": "Medium",
    "headline": "The Credit Cycle's Toll Collector — Paid in Full Before the Cycle Turns",
    "ceo": "Martina Cheung",
    "hq": "New York, New York",
    "snapshot": [
        ("Market cap", "~$114 bn (~295M sh × $386.27)"),
        ("Net debt", "~$13 bn"),
        ("52-week range", "~$361.03 – $522.47"),
        ("Q2'26 revenue / growth", "$4.66 bn / +10% YoY"),
        ("Division revenue (Q2'26)", "Ratings $1.34B (+17%); Indices $534M (+20%); MI $1.29B; Energy $568M"),
        ("Ratings margin", "~60%+ (the profit engine)"),
        ("Adjusted operating margin", "~50% (FY2025)"),
        ("Dividend / buyback", "$3.64 annual ($0.91/qtr); ~$1B buybacks/yr"),
        ("Debt wall", "2026–2027 refinancing at higher rates"),
        ("Next catalyst", "Q3'26 results; debt-issuance / refinancing cycle prints"),
    ],
    "thesis": [
        "S&P Global is the credit cycle's toll collector. Ratings — the business of stamping investment-grade "
        "judgment on the world's debt — is a legal near-duopoly with ~60% margins, and Indices owns the "
        "benchmarks (S&P 500, Dow Jones) against which trillions are measured. These are among the finest "
        "franchises in financial data. They are also among the most cyclical franchises in financial data, "
        "because the toll collector's revenue depends on traffic: when corporations issue debt, Ratings prints "
        "money; when they do not, it does not. Q2 2026 showed the machine at full song — revenue $4.66 billion "
        "up 10%, Ratings up 17%, Indices up 20% — and the stock at $386.27 is priced as though the song plays "
        "indefinitely. It does not.",
        "Our judgment, and the reason this is a REDUCE, is that the credit cycle is the business and the "
        "credit cycle is late. Debt issuance has been pulled forward by borrowers racing to lock in rates; the "
        "refinancing wall of 2026–27 is real but finite; and the operating leverage that made Ratings' 17% "
        "growth so profitable works in both directions. When issuance normalizes — as it always does — revenue "
        "growth falls to the low single digits and the margin structure, built for growth, becomes the "
        "headwind. Our scenarios are $118 / $321 / $602, weighted to a $341 target, 11.7% below the quote. "
        "The base case ($321.46) already assumes a soft landing: 5.9% revenue CAGR for a decade, margins "
        "expanding to 41%, no recession in the explicit period. Even that benign path is worth less than the "
        "current price.",
        "The bear case ($118.34) is the credit-cycle turn that the price assigns zero probability. A "
        "recession or even a sharp issuance pause: Ratings revenue falls double-digits, Market Intelligence "
        "sees subscription churn as banks cut data budgets, and the 2026–27 debt refinancing lands at higher "
        "rates against lower earnings. Revenue compounds at just 2.3% for the decade with margins compressing "
        "to 33%. This is not a stress-test fantasy — it is approximately what the last two credit contractions "
        "looked like for this business. At $386.27, investors are paying a growth multiple for a cyclical "
        "franchise at the top of its cycle.",
        "The forward view that matters: S&P Global's franchises are permanent — the world will always need "
        "ratings and benchmarks — but their earnings are cyclical, and the market is currently pricing "
        "permanence into cyclical earnings. We would own this business at a price that compensates for the "
        "issuance cycle turning. That price is around $341, not $386. REDUCE into the strength; the toll "
        "collector's best buying opportunities have always come when the traffic stops.",
    ],
    "thesis_subhead": "Why the franchises are permanent and the earnings are not",
    "thesis_bullets": [
        ("Ratings at +17% is the cycle, not the franchise. ",
         "Q2'26 Ratings revenue $1.34B (+17%) on pulled-forward issuance; Indices $534M (+20%) on market "
         "levels. Both are cyclical peaks dressed as growth — the franchise didn't get 17% better, the "
         "traffic did."),
        ("Operating leverage cuts both ways. ",
         "~50% adjusted operating margins and ~60% Ratings margins mean revenue deceleration flows "
         "disproportionately to the bottom line. The base case assumes it doesn't have to."),
        ("The refinancing wall is finite. ",
         "2026–27 maturities support issuance near-term; beyond that, the pull-forward becomes the "
         "air pocket."),
        ("The price is the bull case. ",
         "Our bull ($601.51) assumes 8.9% revenue CAGR with no cycle. The market at $386.27 sits well "
         "above our base ($321.46) — paying for permanence in cyclical earnings."),
    ],
    "business": [
        "S&P Global (origins 1860; modern form since the 2016 McGraw-Hill split) is the world's leading "
        "provider of credit ratings, benchmarks, and financial data. Four divisions: Ratings (~30% of revenue, "
        "~60%+ margins — the profit engine), Market Intelligence ($1.29B quarterly revenue — desktop data, "
        "credit analytics, and research subscriptions), S&P Dow Jones Indices ($534M, +20% — the S&P 500 and "
        "Dow Jones benchmarks, licensed to the ETF industry), and Commodity Insights / Energy ($568M — "
        "Platts benchmarks and energy data). Adjusted operating margin is ~50%, among the highest of any "
        "large-cap financial franchise.",
        "The business model is subscription and transaction: Market Intelligence and Indices are largely "
        "recurring (sticky, priced on assets and seats), while Ratings is transaction-driven — issuers pay "
        "per deal, which makes it the cyclical swing factor. In 2025 revenue reached $15.34 billion with free "
        "cash flow of $5.46 billion (35.6% margin). Capital return is steady: a $3.64 annual dividend and "
        "roughly $1 billion a year in buybacks.",
        "The forward picture is a franchise portfolio at peak cyclical earnings. Ratings benefits from the "
        "2026–27 refinancing wall; Indices benefits from elevated equity markets and ETF asset growth; Market "
        "Intelligence benefits from bank data budgets that are currently expanding. All three tailwinds are "
        "cyclical. The structural story — data and benchmarks compounding with financial-market activity over "
        "decades — is real and is why the terminal value in our model is large. But the next three years are "
        "about where we are in the credit cycle, and our judgment is: late.",
    ],
    "business_bullets": [
        ("Ratings (~30% of revenue, ~60%+ margin). ",
         "The credit-rating duopoly with Moody's; transaction-driven, the cyclical swing factor, the "
         "profit engine at peak."),
        ("Market Intelligence ($1.29B/qtr). ",
         "Desktop data and credit analytics subscriptions; sticky but exposed to bank budget cuts in a "
         "downturn."),
        ("S&P Dow Jones Indices ($534M, +20%). ",
         "The S&P 500 benchmark licensed to the ETF industry; revenue scales with market levels and "
         "asset flows — a second cyclical lever."),
        ("Commodity Insights / Energy ($568M). ",
         "Platts benchmarks; steadier, smaller, and strategically peripheral."),
    ],
    "outlook": [
        "The next two years are strong by construction. The 2026–27 debt refinancing wall supports Ratings "
        "issuance; elevated equity markets support Indices licensing; and bank data budgets remain expansive. "
        "Our base case runs revenue from $15.5 billion in FY2026 to $25.7 billion by 2035 — a 5.9% CAGR — "
        "with free-cash-flow margins expanding to 41% as the mix shifts toward the higher-margin divisions. "
        "That is a benign decade: no recession in the explicit period, issuance normalizing gently rather "
        "than collapsing. It is worth $321.46.",
        "The judgment call is what happens when the issuance cycle turns, because it always does. The bear "
        "case ($118.34) models the turn arriving within the explicit period: Ratings revenue falls "
        "double-digits, Market Intelligence churns as banks cut budgets, the 2026–27 refinancing lands at "
        "higher rates against lower earnings, and revenue compounds at just 2.3% with margins compressing to "
        "33%. The last two credit contractions produced approximately this shape. The bull case ($601.51) "
        "assumes the cycle never turns — 8.9% revenue CAGR, 44% terminal margins, issuance compounding "
        "indefinitely. At $386.27 the market is priced meaningfully above our base and well on the way to "
        "the bull.",
        "What would change the call: a genuine credit contraction — issuance falling 20%+ year over year, "
        "spreads blowing out — would validate the bear and we would look to buy the franchise at cyclical "
        "prices. Conversely, if the refinancing wall extends into 2028–29 with issuance holding at current "
        "levels, the benign path lengthens and the base case becomes conservative. Watch: monthly "
        "investment-grade and high-yield issuance volumes, credit spreads, and any bank commentary on data "
        "budgets.",
    ],
    "financials": [
        "The margin structure is the story: ~50% adjusted operating margins, ~60%+ in Ratings, converting to "
        "a 35.6% free-cash-flow margin in FY2025 ($5.46B on $15.34B). Our model has FY2026E FCF at $6.25 "
        "billion, expanding to $10.54 billion by 2035 as margins reach 41%. This is a business that converts "
        "incremental revenue to cash at extraordinary rates — which is precisely why a revenue deceleration "
        "is so punishing: the operating leverage is symmetric.",
        "The balance sheet carries ~$13 billion of net debt against a ~$114 billion market cap — manageable, "
        "but the 2026–27 refinancing wall means a meaningful portion reprices at higher rates even as "
        "earnings face cyclical pressure in our bear case. The dividend ($3.64 annual) and ~$1B annual "
        "buybacks are well covered in the base case and would come under review in a genuine downturn — "
        "which is itself a signal to watch.",
    ],
    "fin_table": {
        "headers": ["$ bn", "FY2022", "FY2023", "FY2024", "FY2025"],
        "rows": [
            ["Revenue", "11.18", "12.50", "14.21", "15.34"],
            ["YoY growth", "—", "+12%", "+14%", "+8%"],
            ["Adj. operating margin", "—", "—", "~49%", "~50%"],
            ["Free cash flow", "2.51", "3.57", "5.57", "5.46"],
            ["FCF margin", "22.4%", "28.6%", "39.2%", "35.6%"],
            ["Q2'26: Ratings / Indices", "$1.34B (+17%)", "$534M (+20%)", "MI $1.29B", "Energy $568M"],
        ],
        "footnote": "Sources: company releases; annuals via yfinance. FY2026E: revenue $15.5B, FCF $6.25B "
                    "(model anchors).",
    },
    "moat": [
        ("The ratings duopoly. ",
         "S&P and Moody's are embedded in debt covenants, regulation, and investment mandates worldwide. "
         "Displacing a rating agency is a decades-long project; the NRSRO designation is a regulatory moat."),
        ("Benchmark ownership. ",
         "The S&P 500 is the benchmark against which the world's capital is measured; licensing it to the "
         "ETF industry is a royalty on global equity markets."),
        ("Data integration. ",
         "Market Intelligence's desktop and analytics are embedded in bank and fund workflows; switching "
         "costs are real, if not insurmountable."),
        ("The moat does not cover the cycle. ",
         "No moat protects a transaction business from a transaction drought. The franchises are "
         "permanent; the earnings are cyclical — and the market is pricing the former into the latter."),
    ],
    "valuation_method": "10-year scenario DCF (FY2026–FY2035)",
    "valuation_intro": [
        "We value S&P Global on a 10-year explicit DCF of free cash flow (FY2026–FY2035), weights bear 25% / "
        "base 50% / bull 25%. Scenario discounts: base 9.5% (elite franchises, cyclical earnings, "
        "regulatory exposure), bear 12.0% (base + 250bp), bull 8.0% (base − 150bp). Terminal growth "
        "1.25% / 2.25% / 2.50% on year-10 FCF at the scenario's terminal margin (33% / 41% / 44%) — "
        "through-cycle levels, never peaks. Revenue CAGRs: bear 2.3% (credit-cycle turn in the explicit "
        "period), base 5.9%, bull 8.9%. Equity = firm EV − ~$13B net debt, over ~295M shares. Terminal value "
        "is 38–65% of EV across scenarios — within discipline, no haircut required.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 118.34,
            "assumptions": "The credit cycle turns: Ratings revenue falls double-digits, MI churns on bank budget cuts, the 2026–27 refinancing lands at higher rates against lower earnings; 2.3% revenue CAGR, margins to 33%",
            "rev_cagr": "+2.3%", "margin_end": "33%",
            "discount": 0.12, "terminal_g": 0.0125, "tv_share": 0.383,
            "pv_explicit": 29.24, "pv_terminal": 18.14, "cashflow_unit": "$bn",
        },
        "base": {
            "fair_value": 321.46,
            "assumptions": "Soft landing: 5.9% revenue CAGR, no recession in the explicit period, issuance normalizes gently; margins expand to 41% on mix shift to the higher-margin divisions",
            "rev_cagr": "+5.9%", "margin_end": "41%",
            "discount": 0.095, "terminal_g": 0.0225, "tv_share": 0.525,
            "pv_explicit": 50.92, "pv_terminal": 56.34, "cashflow_unit": "$bn",
        },
        "bull": {
            "fair_value": 601.51,
            "assumptions": "The cycle never turns: 8.9% revenue CAGR, issuance compounds indefinitely, 44% terminal margins; the refinancing wall extends into 2028–29",
            "rev_cagr": "+8.9%", "margin_end": "44%",
            "discount": 0.08, "terminal_g": 0.025, "tv_share": 0.649,
            "pv_explicit": 66.55, "pv_terminal": 123.28, "cashflow_unit": "$bn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "0.25×$118.34 + 0.50×$321.46 + 0.25×$601.51 = $341.29 → $341 target. "
                     "Bear meets all hurt conditions (issuance collapse, margin compression, 25%+ derating).",
    "risks": [
        ("Credit-cycle turn (the #1 risk). ",
         "Ratings is transaction-driven; an issuance pause or recession cuts the highest-margin revenue "
         "first and the operating leverage amplifies it."),
        ("Pulled-forward issuance. ",
         "Borrowers racing to lock in rates have borrowed from future quarters; the air pocket follows "
         "the wall."),
        ("Refinancing at higher rates. ",
         "The 2026–27 debt wall reprices against potentially lower earnings in a downturn — a double hit."),
        ("Regulatory / political risk. ",
         "Rating agencies are perennial political targets; adverse regulation of the issuer-pays model "
         "would strike at the franchise's core."),
        ("Passive and private-credit disintermediation. ",
         "If private credit continues taking share from public debt markets, the rated-issuance universe "
         "grows more slowly than credit itself."),
        ("Valuation. ",
         "At $386.27 the stock sits well above our $321.46 base — a growth multiple on cyclical peak "
         "earnings."),
    ],
    "falsification": (
        "The base case's soft-landing assumption would be withdrawn if investment-grade or high-yield "
        "issuance falls 20%+ year over year for two consecutive quarters, or if credit spreads blow out — "
        "at that point the bear case ($118.34) becomes the working assumption and we would look to buy the "
        "franchise at cyclical prices. Conversely, if the refinancing wall extends into 2028–29 with "
        "issuance holding at current levels, the benign path lengthens and the base case becomes "
        "conservative. Watch: monthly issuance volumes, credit spreads, bank data-budget commentary."
    ),
    "methodology": [
        "We value the business on a 10-year explicit DCF of free cash flow (bear 25% / base 50% / bull 25%). "
        "Revenue follows the scenario path (bear 2.3% / base 5.9% / bull 8.9% 10-year CAGR, with a "
        "credit-cycle turn in the bear case); free-cash-flow margin moves to the scenario's terminal margin "
        "(33% / 41% / 44%) over the horizon. Discount rates: base 9.5%, bear +250bp (12.0%), bull −150bp "
        "(8.0%). Terminal growth (1.25% / 2.25% / 2.50%) applies to year-10 FCF at the scenario's terminal "
        "margin. Equity = firm EV − net debt; divided by diluted shares. Bear cases must be genuinely "
        "adverse and sit below the current price. The published target is the probability-weighted fair "
        "value, stated as a 12-month horizon reference.",
        "Risk ratings (Low / Medium / Medium-High / High) combine business-model volatility, the balance "
        "sheet, and the valuation. This note is independent research-style analysis for informational purposes "
        "only and is not investment advice. Financial figures are drawn from company releases and SEC filings; "
        "market data as of October 2, 2026. Projections and the price target are the author's estimates and "
        "involve uncertainty. Past performance does not predict future results.",
    ],
    "charts": {
        "scenario": {"bear": 118.34, "base": 321.46, "bull": 601.51, "weighted": 341.29, "price": 386.27},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [11.18, 12.50, 14.21, 15.34],
            "fcf_hist": [2.51, 3.57, 5.57, 5.46],
            "years_proj": [2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035],
            "revenue_proj": [16.60, 17.76, 18.83, 19.96, 21.16, 22.21, 23.32, 24.49, 25.71],
            "fcf_proj": [6.77, 7.32, 7.81, 8.28, 8.76, 9.17, 9.61, 10.07, 10.54],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via yfinance. Projection: base-case series from the scenario "
                    "DCF (FY2026E anchor $15.5B revenue; 5.9% 10-yr CAGR; FCF margin to 41%).",
        },
        "composition": {
            "bear": {"pv_explicit": 29.24, "pv_terminal": 18.14},
            "base": {"pv_explicit": 50.92, "pv_terminal": 56.34},
            "bull": {"pv_explicit": 66.55, "pv_terminal": 123.28},
            "unit": "$bn",
        },
        "extra": {
            "type": "pie",
            "title": "Q2'26 revenue by division ($4.66B total)",
            "labels": ["Ratings", "Market Intelligence", "Indices", "Energy / Commodity Insights"],
            "values": [1.34, 1.29, 0.53, 0.57],
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "SPGI-equity-research-note-polished.pdf")
build_note(data, out)
print("built:", out)
