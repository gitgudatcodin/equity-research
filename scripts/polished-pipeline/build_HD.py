"""HD polished note. Research analysis, not investment advice.

Scenario numbers: authoritative compounder-quality override rebuild
(~/workspace/compounder-screen/rebuild.py engine, master addenda PDF):
bear $58.75 / base $305.02 / bull $401.77, weighted $267.64 -> $268 target.
15-yr explicit base/bull (10-yr bear), 8.0% base discount (strongest band), term g cap 3.0%.
History: yfinance annuals (fiscal year ends January). Projection: base-case model series.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

# Base-case model series (15-yr, FY2027–FY2041) from the compounder engine; chart shows FY2027–2036
base_rev = [177.66, 185.12, 192.90, 201.00, 209.44, 218.24, 227.40, 236.95, 246.91, 257.28]
base_fcf = [15.89, 16.65, 17.45, 18.29, 19.17, 20.09, 21.06, 22.08, 23.15, 24.28]
# (engine full 15-yr series ends 2041 at rev $305.3B / FCF $29.0B; truncated at 10 shown for readability)

data = {
    "ticker": "HD",
    "company": "The Home Depot, Inc.",
    "exchange": "NYSE",
    "sector": "Consumer Discretionary — Home Improvement Retail",
    "verdict": "HOLD",
    "fair_value": 268.00,
    "price": 282.85,
    "risk": "Medium",
    "headline": "The Best Retailer in the World, Priced as Though the Cycle Cooperates",
    "ceo": "Ted Decker",
    "hq": "Atlanta, Georgia",
    "snapshot": [
        ("Market cap", "~$282 bn (0.998 bn sh × $282.85)"),
        ("Enterprise value", "~$345 bn"),
        ("Net debt", "~$61 bn (SRS/GMS acquisition leverage)"),
        ("52-week range", "~$277.15 – $397.63"),
        ("FY2025 sales / comps", "$164.7 bn (+3.2%) / +0.3%"),
        ("ROIC streak", ">15% every year since 2010 (16 years)"),
        ("Dividend", "$9.32/share annualized ($2.33/qtr, raised Feb 2026)"),
        ("FY2026E guide", "Comps flat to +2%; adj. EPS flat to +4% off $14.69"),
        ("Pro addressable market", "~$700 bn (SRS + GMS trade distribution)"),
        ("Next catalyst", "Q3 FY26 results; housing-turnover prints"),
    ],
    "thesis": [
        "Home Depot is the best home-improvement retailer in the world, and the stock is priced as though "
        "that statement alone settles the investment question. It does not. A 16-year streak of returns on "
        "invested capital above 15%, gross margins that have held near 33% through every housing cycle of the "
        "last decade and a half, and free-cash-flow conversion above 80% make this one of the highest-quality "
        "businesses in American retail. Quality of that order deserves a premium multiple. It does not deserve "
        "the assumption that the cycle cooperates.",
        "The cycle is not cooperating. Existing-home turnover sits near historic lows — roughly 3% of the "
        "housing stock — with 30-year mortgage rates still near 6.6%. Management itself describes a frozen "
        "housing market. When homes do not change hands, the move-driven big-ticket projects — kitchens, "
        "additions, full renovations — that carry the highest tickets and the best margins simply do not get "
        "scheduled. Homeowners are healthy and spending, but they are spending on smaller maintenance and "
        "repair jobs while deferring the large discretionary work. Q2 FY2026 delivered a four-year high in "
        "comparable sales and a genuine beat, and management reaffirmed rather than raised full-year guidance. "
        "The reaffirmation is the honest tell: the company does not trust the housing market to deliver a "
        "second-half acceleration, and neither should investors.",
        "Our judgment is that Home Depot's long-term economics are intact and underappreciated in the bearish "
        "narrative, but the next twelve months belong to the cycle, not to the franchise. We value the company "
        "on a 15-year scenario DCF that grants the compounder-quality treatment its history has earned — an 8.0% "
        "base discount rate (our strongest band), 3.0% terminal growth capped on demonstrated sustained margins, "
        "never peak margins — and the answer is fair value of $268 against a $282.85 price. The base case "
        "($305) assumes a gradual turnover thaw from 2027, low-single-digit comp growth, the pro platform "
        "scaling, and operating margins recovering toward the mid-teens — with no heroics on the multiple. That "
        "is a HOLD: a superb business at a full price, with the upside reserved for the eventual housing-turnover "
        "recovery, which remains a 2027-or-later story.",
        "The asymmetry matters. The bear case — housing stays frozen for two more years, big-ticket comps stay "
        "negative, the pro build-out dilutes margins longer than expected — is worth $58.75, a genuine "
        "washout. The bull case — mortgage rates break below 6% and turnover normalizes — is worth $401.77, "
        "mid-teens upside from here. At $282.85 investors are paying for an earnings recovery that management's "
        "own guidance says is not yet visible. We would become buyers on genuine weakness toward the bear-case "
        "zone; at current levels the risk-reward is balanced to mildly negative.",
    ],
    "thesis_bullets": [
        ("Quality is not the debate; the cycle is. ",
         "16 years of >15% ROIC, ~33% gross margins through every housing cycle, >80% FCF conversion — "
         "this is the strongest-band qualifier in our compounder framework, which is why the model grants it "
         "an 8.0% discount rate over 15 explicit years. The franchise is the reason the bear case is a "
         "buying opportunity, not an obituary."),
        ("The pro pivot is the right answer to a frozen DIY market. ",
         "Pros are roughly half of revenue; the $18.25 billion SRS Distribution acquisition (roofing, pool, "
         "landscaping supply) plus GMS gives Home Depot a serious position in specialty trade distribution "
         "against a ~$700 billion addressable market. Pro demand is steadier than DIY through cycles and "
         "buys on a recurring, job-driven cadence."),
        ("The honest tell is the guide. ",
         "A four-year high in comps, a genuine Q2 beat — and management reaffirmed rather than raised. "
         "When the best operator in retail refuses to extrapolate its own quarter, investors should not "
         "extrapolate it for them."),
    ],
    "business": [
        "The Home Depot is the world's largest home-improvement retailer, operating roughly 2,360 stores "
        "across the United States, Canada, and Mexico. The business serves two customer types: the "
        "do-it-yourself homeowner and the professional contractor — the pro. Pros now account for roughly half "
        "of revenue, a deliberate and growing mix, served through dedicated pro desks, direct fulfillment, and "
        "a trade distribution network built through acquisitions.",
        "Fiscal 2025 (ended February 1, 2026) produced net sales of $164.7 billion, up 3.2%, with comparable "
        "sales of 0.3% and diluted earnings per share of $14.23 GAAP ($14.69 adjusted). Gross margin ran at "
        "approximately 33.1%, and fiscal 2026 operating-margin guidance sits at 12.4% to 12.6% — compressed "
        "relative to history by the mix shift toward the acquired distribution businesses and continued "
        "investment in the pro ecosystem. Return on invested capital, above 15% every year since 2010, was "
        "25.4% in Q1 FY2026. The company paid about $2.3 billion in dividends in that quarter alone and "
        "continues a decades-long capital-return program funded by genuinely prodigious cash generation.",
        "The strategic centerpiece is the pro pivot. The March 2024 acquisition of SRS Distribution for "
        "$18.25 billion gave Home Depot a serious position in specialty trade distribution, and the subsequent "
        "GMS acquisition extended that reach. The company is adding 40 to 50 new SRS branches a year and "
        "points to a total pro addressable market of roughly $700 billion. The logic is sound: pro demand is "
        "steadier than DIY through cycles, and Home Depot's scale in procurement and logistics gives it "
        "structural advantages over fragmented regional distributors. But it is a multi-year build, the acquired "
        "revenue carries thinner margins than the core box, and the balance sheet now carries the leverage "
        "those acquisitions required.",
    ],
    "business_bullets": [
        ("SRS Distribution ($18.25B, Mar 2024). ",
         "Roofing, pool, and landscaping specialty distribution — the core of the pro build-out; 40–50 new "
         "branches a year."),
        ("GMS acquisition. ",
         "Extended specialty-distribution reach; the acquired revenue layers in at lower margins than the "
         "core retail box, diluting consolidated margins during the build phase."),
        ("Pro desks + direct fulfillment. ",
         "Dedicated pro infrastructure inside the store network converts job-driven contractor demand into "
         "recurring revenue — steadier than the DIY homeowner through housing cycles."),
        ("Capital return continues. ",
         "Decades-long dividend and buyback program funded by operating cash flow; the $9.32 annualized "
         "dividend yields ~3.3% at the current price."),
    ],
    "outlook": [
        "Our base expectation is that fiscal 2026 and 2027 are transition years, not recovery years. The "
        "housing lock-in — tens of millions of homeowners holding mortgages at 3–4% who cannot afford to move "
        "at 6.6% rates — is a structural feature of this cycle, not a sentiment blip. Until turnover normalizes, "
        "big-ticket comps stay soft and the company's growth comes from market-share gains in a weak market, "
        "new stores and branches, and the acquired SRS/GMS revenue layering in. That is a recipe for "
        "low-single-digit sales growth and flat-to-modestly-up earnings — exactly what guidance describes. We "
        "take management at its word when it refuses to raise the guide after a strong quarter.",
        "Where we differ from the more bearish camp is on the durability of the franchise through this trough. "
        "Home Depot is taking share — its on-shelf availability, supply chain, and pro capabilities widen the gap "
        "with weaker competitors precisely when the market is weakest. The pro pivot is not a defensive crouch; "
        "it is an offensive build of the industry's best distribution platform for contractors, and the $700 "
        "billion addressable market means even modest share gains compound into very large revenue. Gross "
        "margin stability near 33% through this softness is the empirical proof that pricing power is intact. "
        "When turnover eventually normalizes — our working assumption is a gradual thaw beginning in 2027, not "
        "a snap-back — the operating leverage on the other side is real, and the pro business will be a larger, "
        "stickier, more recurring portion of the mix.",
        "The honest risk to this outlook is duration. A frozen housing market can stay frozen longer than equity "
        "investors' patience, and every quarter of flat comps is a quarter in which the market questions whether "
        "the multiple is earned. Tariff-related cost pressures — visible in the IEEPA tariff refunds embedded in "
        "fiscal 2026 guidance, offsetting unplanned fuel and input costs — are a reminder that the cost structure "
        "is not immune to policy shocks. Our judgment: the business will be larger and better in five years; the "
        "stock, at 19–20x earnings on trough-adjacent EPS, offers little compensation for the wait.",
    ],
    "financials": [
        "The financial signature of the compounder case is cash conversion. Free-cash-flow conversion has run "
        "above 80% for years, and the terminal FCF margin in our model is a demonstrated sustained level — "
        "8.6–10.2% since 2015 (2025: 7.7%, depressed by SRS integration) — not a cyclical peak. Base-case FCF "
        "compounds from ~$15.9 billion in FY2027 to $29.0 billion by 2041 as revenue grows at a 4.2% 10-year CAGR "
        "and margins recover toward the mid-teens. The leverage is the constraint: ~$61 billion of net debt from "
        "the acquisition program, which is why the bear case — revenue declining at a 0.5% CAGR for a decade "
        "with margins compressing to 6.5% — is worth only $58.75.",
        "The dividend is the shareholder's compensation for patience: $9.32 annualized, a ~3.3% yield at the "
        "current price — the highest in years outside crisis periods. Buybacks have been paused since March 2024 "
        "as capital went to SRS/GMS; resumption is a 2027-or-later story tied to deleveraging progress.",
    ],
    "fin_table": {
        "headers": ["$ bn", "FY2023", "FY2024", "FY2025", "FY2026E guide"],
        "rows": [
            ["Net sales", "157.4", "152.7", "164.7", "+2.5% to +4.5%"],
            ["Comparable sales", "−3.2%", "−3.2%", "+0.3%", "flat to +2%"],
            ["Gross margin", "~33.0%", "~33.4%", "~33.1%", "—"],
            ["Operating margin", "14.2%", "13.5%", "13.0%", "12.4%–12.6%"],
            ["Adj. diluted EPS", "$15.11", "$15.11", "$14.69", "flat to +4%"],
            ["Free cash flow", "11.5", "18.0", "16.3", "—"],
            ["ROIC", ">15%", ">15%", ">15%", "—"],
        ],
        "footnote": "Sources: company 10-K and earnings releases; FY2023–25 annuals via yfinance (fiscal years end "
                    "January). 16 consecutive years of ROIC above 15% (2010–2025).",
    },
    "moat": [
        ("Scale procurement and logistics. ",
         "The world's largest home-improvement buyer extracts vendor terms no regional distributor can match; "
         "the supply chain delivered industry-best on-shelf availability through the softest demand in years."),
        ("The pro ecosystem is a share machine. ",
         "Pro desks, direct fulfillment, and now specialty trade distribution (SRS/GMS) make Home Depot the "
         "default supplier for contractors — a relationship moat that widens when weaker competitors retrench."),
        ("Pricing power, empirically demonstrated. ",
         "Gross margins near 33% through a multi-year demand trough is the proof; the business does not buy "
         "sales with margin."),
        ("The moat's weak link is the cycle itself. ",
         "No moat protects against deferred big-ticket demand: when turnover freezes, the highest-margin "
         "projects simply do not happen, and no amount of execution creates them."),
    ],
    "valuation_method": "15-year scenario FCFE DCF (compounder-quality override)",
    "valuation_intro": [
        "Home Depot meets our compounder-quality criteria — 16 consecutive years of ROIC above 15% "
        "(2010–2025), stable-to-expanding gross margins, and free-cash-flow conversion above 80%, all verified "
        "from reported history — so we model a 15-year explicit horizon (10-year bear) at an 8.0% base "
        "discount rate (strongest band), with terminal growth capped at 3.0% applied to demonstrated sustained "
        "FCF margins (6.5% / 9.5% / 10.5% — not cyclical peaks). The bear case adds 250bp (10.5%), the bull case "
        "subtracts 150bp with an 8% floor (binds at 8.0%), and the three scenarios are weighted 25% / 50% / 25%. "
        "Revenue grows at the scenario CAGR for years 1–10 (−0.5% / +4.2% / +5.8%), fading to terminal growth "
        "over years 11–15; FCF margin glides from 8.5% to the terminal margin over 10 years. Net debt $61.0B, "
        "0.998B shares. Terminal value is 37–54% of EV across scenarios — no haircut required.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 58.75,
            "assumptions": "Housing freeze extends through 2028: turnover near 3%, big-ticket comps negative, SRS organic growth disappoints, pro build-out dilutes margins longer than guided",
            "rev_cagr": "−0.5%", "margin_end": "6.5%",
            "discount": 0.105, "terminal_g": 0.015, "tv_share": 0.366,
            "pv_explicit": 75.83, "pv_terminal": 43.80, "cashflow_unit": "$bn",
        },
        "base": {
            "fair_value": 305.02,
            "assumptions": "Gradual turnover thaw from 2027; low-single-digit comp growth; pro revenue compounds as the trade-distribution platform scales; operating margins recover toward mid-teens — no multiple heroics",
            "rev_cagr": "+4.2%", "margin_end": "9.5%",
            "discount": 0.08, "terminal_g": 0.03, "tv_share": 0.515,
            "pv_explicit": 177.09, "pv_terminal": 188.32, "cashflow_unit": "$bn",
        },
        "bull": {
            "fair_value": 401.77,
            "assumptions": "Mortgage rates break durably below 6% by 2027; turnover normalizes faster; deferred big-ticket demand releases in a wave; pro platform captures share faster than base",
            "rev_cagr": "+5.8%", "margin_end": "10.5%",
            "discount": 0.08, "terminal_g": 0.03, "tv_share": 0.541,
            "pv_explicit": 211.99, "pv_terminal": 249.97, "cashflow_unit": "$bn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "0.25×$58.75 + 0.50×$305.02 + 0.25×$401.77 = $267.64 → $268 target. "
                     "Bear meets all hurt conditions (revenue decline, 300bp+ margin compression, 25%+ derating).",
    "risks": [
        ("Housing-freeze duration. ",
         "The lock-in effect (3–4% mortgages vs 6.6% market rates) can persist longer than equity patience; "
         "every flat-comp quarter re-opens the multiple debate."),
        ("Big-ticket deferral. ",
         "Kitchens, additions, and renovations are the highest-margin sales and the most deferrable — a "
         "structural mix headwind while turnover is frozen."),
        ("Pro-build execution. ",
         "SRS/GMS integration must deliver the distribution economics; the acquired revenue dilutes "
         "consolidated margins in the meantime."),
        ("Leverage. ",
         "~$61B of net debt from the acquisition program constrains capital return until deleveraging "
         "progresses; buybacks remain paused."),
        ("Tariff and input costs. ",
         "IEEPA tariff refunds in FY2026 guidance are offsetting unplanned fuel and input costs — policy "
         "shocks can move the cost structure faster than pricing."),
        ("Competition for the pro. ",
         "Specialty distributors and Lowe's pro push contest the $700B addressable market; share gains are "
         "assumed, not guaranteed."),
    ],
    "falsification": (
        "Downgrade to REDUCE if comps re-decelerate to flat/negative for two consecutive quarters combined "
        "with net debt/EBITDA failing to decline — that breaks the base case's core-revenue path from the "
        "inside. Conversely, a housing-turnover recovery or buyback resumption ahead of schedule would argue "
        "for the bull case ($401.77). We would become buyers on a genuine washout toward the bear-case zone "
        "($58.75). Watch: existing-home turnover prints, big-ticket comp trends, and SRS branch productivity."
    ),
    "methodology": [
        "Home Depot qualifies for the compounder-quality override: 16 consecutive years of ROIC above 15% "
        "(2010–2025), stable-to-expanding gross margins, and free-cash-flow conversion above 80%, verified "
        "from reported history. Qualifying businesses are valued on a 15-year explicit horizon (10-year bear) "
        "at an 8.0–8.5% base discount rate — the strongest band at 8.0% — with the bear case adding 250bp and "
        "the bull case subtracting 150bp (8% floor). Terminal growth is capped at 3.0% on demonstrated "
        "sustained margins, never peaks. Revenue compounds at the scenario CAGR for years 1–10, fading to "
        "terminal growth over years 11–15; FCF margin glides from the current level to the terminal margin over "
        "10 years. Scenarios are weighted bear 25% / base 50% / bull 25%. If the qualification criteria fail "
        "over any multi-year window, the business is re-valued at the standard 10% discount over a 10-year "
        "horizon. Bear cases must be genuinely adverse and sit below the current price. The published target "
        "is the probability-weighted fair value, stated as a 12-month horizon reference.",
        "Risk ratings (Low / Medium / Medium-High / High) combine business-model volatility, the balance "
        "sheet, and the valuation. This note is independent research-style analysis for informational purposes "
        "only and is not investment advice. Financial figures are drawn from company releases and SEC filings; "
        "market data as of October 2, 2026. Projections and the price target are the author's estimates and "
        "involve uncertainty. Past performance does not predict future results.",
    ],
    "charts": {
        "scenario": {"bear": 58.75, "base": 305.02, "bull": 401.77, "weighted": 267.64, "price": 282.85},
        "trajectory": {
            "years_hist": [2023, 2024, 2025, 2026],
            "revenue_hist": [157.40, 152.67, 159.51, 164.68],
            "fcf_hist": [11.50, 17.95, 16.32, 12.65],
            "years_proj": [2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": base_rev,
            "fcf_proj": base_fcf,
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via yfinance (fiscal years end January). Projection: base-case "
                    "FCF from the 15-year compounder DCF (shown FY2027–2036; the model runs to 2041, ending at "
                    "$305.3B revenue / $29.0B FCF).",
        },
        "composition": {
            "bear": {"pv_explicit": 75.83, "pv_terminal": 43.80},
            "base": {"pv_explicit": 177.09, "pv_terminal": 188.32},
            "bull": {"pv_explicit": 211.99, "pv_terminal": 249.97},
            "unit": "$bn",
        },
        "extra": {
            "type": "line",
            "title": "FCF margin — history vs. base-case glide path",
            "years": [2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "series": [{"label": "FCF margin",
                        "values": [7.3, 11.8, 10.2, 7.7, 8.9, 9.0, 9.0, 9.1, 9.2, 9.2, 9.3, 9.4, 9.4, 9.5]}],
            "ylabel": "%",
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "HD-equity-research-note-polished.pdf")
build_note(data, out)
print("built:", out)
