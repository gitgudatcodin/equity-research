"""CELH polished note. Research analysis, not investment advice.

Scenario numbers: authoritative hardened note (~/workspace/celsius-research-v2/build_note.py + batch2 PDF).
Bear $7.70 / base $22.90 / bull $38.48, weighted ~$23 -> $23 target.
Discounts: 14.5%/12%/10.5%; term g 1.0%/2.5%/2.5%; mid-cycle FCF margins 20.5%/24%/25%;
revenue CAGR 1.2%/5.5%/8.3%; $1.76B PepsiCo preferred + $54M net debt senior; ~260M shares.
PV split derived analytically (no scenario PV detail published): PV_TV = year-10 FCF
($3.3B FY26E anchor x (1+CAGR)^10 x mid-cycle margin) capitalized and discounted; PV_explicit = EV - PV_TV,
where EV = FV x 0.260B shares + $1.814B senior claims. TV shares 38.6%/60.5%/73.1% — what the published
params imply; derivation basis footnoted in the note.
History: yfinance annuals. Projection: base 5.5% CAGR off $3.3B anchor, 24% FCF margin.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

data = {
    "ticker": "CELH",
    "company": "Celsius Holdings, Inc.",
    "exchange": "NASDAQ",
    "sector": "Consumer Staples — Energy Drinks",
    "verdict": "REDUCE",
    "fair_value": 23.00,
    "price": 26.75,
    "risk": "High",
    "headline": "A Great Brand in a Brutal Category — at a Price That Forgets the Category",
    "ceo": "John Fieldly",
    "hq": "Boca Raton, Florida",
    "snapshot": [
        ("Market cap", "~$6.9 bn (260M sh × $26.75)"),
        ("Senior claims", "$1.76 bn PepsiCo preferred + $54M net debt"),
        ("52-week range", "~$23.56 – $66.74"),
        ("Revenue / growth", "$2.52 bn FY2025 (+85% YoY, incl. Alani Nu)"),
        ("Category", "US energy drinks — Monster/Red Bull duopoly"),
        ("PepsiCo role", "Preferred holder + distribution partner"),
        ("Alani Nu acquisition", "Closed 2025; integration in progress"),
        ("FCF margin (FY2025)", "~12.7% ($0.32B on $2.52B)"),
        ("Next catalyst", "Q3'26 results; Alani Nu synergy delivery"),
    ],
    "thesis": [
        "Celsius is a genuinely good brand in a genuinely brutal category. The energy-drink aisle is a "
        "duopoly — Monster and Red Bull — with a long graveyard of challengers that grew fast, spent faster, "
        "and faded. Celsius broke through where others died: functional positioning, a loyal core consumer, "
        "and the Alani Nu acquisition, which bought growth and a second brand engine in one move. FY2025 "
        "revenue of $2.52 billion, up 85%, is a real achievement. The stock at $26.75, off its highs but "
        "still rich, is priced as though the breakthrough were the same as the moat. It is not.",
        "Our judgment, and the reason this is a REDUCE with a High risk rating, is that the category "
        "economics are the binding constraint on the valuation, not the brand's momentum. Energy drinks are "
        "a marketing-spend arms race: slotting, sponsorships, and trade promotion are the price of shelf "
        "space, and the duopoly's scale advantages in distribution and media buying are structural. Celsius "
        "can grow revenue at 5–8% and still see margins compress if the promotional intensity rises — which "
        "is exactly what happens when a challenger reaches scale and the incumbents respond. Our scenarios "
        "are $7.70 / $22.90 / $38.48, weighted to a $23 target, 14.0% below the quote. The base case already "
        "assumes the good version: 5.5% revenue CAGR for a decade, mid-cycle FCF margins of 24%, Alani Nu "
        "integrated cleanly. Even that good version is worth less than the current price.",
        "The bear case ($7.70) is the category's base rate for challengers. Growth stalls to 1.2% as the "
        "core brand matures and Alani Nu's novelty fades; promotional spend ratchets to defend share; "
        "mid-cycle FCF margins settle at 20.5% — still respectable, but on a much smaller revenue base — "
        "and the $1.76 billion PepsiCo preferred plus $54 million of net debt sits senior to the equity in a "
        "downturn. The preferred is the quiet leverage in this story: it does not show up in net-debt "
        "screens, but it is a senior claim on a cyclical consumer business. In the bear case, the equity is "
        "worth $7.70 because the senior claims eat first.",
        "The forward view: Celsius will likely be a bigger brand in five years — the category is growing, "
        "the functional positioning has legs, and PepsiCo's distribution is a genuine asset. But the stock "
        "at $26.75 is pricing the bull case's 8.3% CAGR and 25% mid-cycle margins as the expected outcome, "
        "with no discount for the category's history of destroying challenger economics at scale. We would "
        "own this brand at a price that respects the aisle it fights in. That price is around $23, not $27. "
        "REDUCE.",
    ],
    "thesis_subhead": "Why the brand is real and the price is wrong",
    "thesis_bullets": [
        ("The breakthrough is real. ",
         "$2.52B revenue (+85% with Alani Nu), a loyal functional-energy consumer, PepsiCo distribution — "
         "Celsius did what most challengers never do: reach scale in a duopoly aisle."),
        ("The aisle is the constraint. ",
         "Monster/Red Bull scale advantages in distribution and media are structural; promotional "
         "intensity rises as challengers scale. Revenue can grow while economics compress."),
        ("The preferred is quiet leverage. ",
         "$1.76B of PepsiCo preferred sits senior to the equity — invisible in net-debt screens, "
         "decisive in a downturn."),
        ("The price is the bull case. ",
         "Our base case grants 5.5% CAGR and 24% mid-cycle margins and is worth $22.90. The market at "
         "$26.75 is paying for the bull's 8.3% CAGR — the outcome, not the expectation."),
    ],
    "business": [
        "Celsius Holdings (founded 2004, Boca Raton) makes functional energy drinks — the flagship Celsius "
        "brand positioned around fitness and wellness, and Alani Nu (acquired 2025), a fast-growing brand "
        "with strong appeal to younger female consumers. Distribution runs through the PepsiCo partnership "
        "(which also holds $1.76 billion of preferred equity), giving the brands national retail reach that "
        "an independent challenger could never build alone.",
        "Fiscal 2025 produced revenue of $2.52 billion, up 85% year over year — the Alani Nu acquisition "
        "doing heavy lifting — with free cash flow of $0.32 billion (12.7% margin). The growth history is "
        "explosive: $0.65B (2022), $1.32B (2023), $1.36B (2024), $2.52B (2025). But the 2024 plateau — "
        "revenue essentially flat at $1.36 billion — is the number the bulls skip: the core brand's growth "
        "stalled before Alani Nu arrived, a reminder that energy-drink growth comes in waves, not straight "
        "lines.",
        "The forward picture is a two-brand portfolio in a consolidating category. Alani Nu's integration "
        "is the near-term execution story: synergy delivery, distribution expansion, and brand investment "
        "without cannibalizing Celsius. PepsiCo's role is double-edged — unmatched distribution reach, but "
        "a $1.76 billion senior claim and a partner whose strategic priorities may not always align with "
        "Celsius shareholders'. The category grows mid-single-digits; Celsius's job is to take share "
        "profitably, which is harder than taking share.",
    ],
    "business_bullets": [
        ("Celsius: the flagship. ",
         "Functional-energy positioning, loyal fitness-adjacent consumer; growth stalled in 2024 before "
         "Alani Nu — the wave, not the line."),
        ("Alani Nu (acquired 2025). ",
         "Second brand engine with younger-female appeal; integration and synergy delivery are the "
         "near-term execution story."),
        ("PepsiCo partnership + preferred. ",
         "National distribution reach — and a $1.76B senior claim that eats first in any downturn."),
        ("The duopoly aisle. ",
         "Monster and Red Bull own the category's scale economics; every challenger fights uphill on "
         "slotting, sponsorship, and trade spend."),
    ],
    "outlook": [
        "The next two years are about Alani Nu digestion. FY2026E revenue anchors at $3.3 billion in our "
        "model, with the base case compounding at 5.5% to roughly $5.6 billion by 2036. The growth is "
        "back-half loaded on distribution expansion and international optionality; the near term is "
        "integration risk. Our base-case FCF margin glides to a 24% mid-cycle level — well above the 12.7% "
        "printed in FY2025 — which assumes promotional intensity stays rational and the mix shifts toward "
        "higher-margin channels. That is an optimistic margin path for a category this competitive.",
        "The judgment call is whether Celsius's economics scale or compress. The bull case ($38.48) assumes "
        "they scale: 8.3% revenue CAGR, 25% mid-cycle FCF margins, the two-brand portfolio taking durable "
        "share from the duopoly. Our view is more cautious: the history of challenger brands in this aisle "
        "is that scale invites competitive response, and competitive response costs margin. The bear case "
        "($7.70) — 1.2% CAGR, 20.5% mid-cycle margins, the preferred claim dominating a smaller equity "
        "value — is what the category does to challengers that stumble. At $26.75, the market is not "
        "discounting that possibility at all.",
        "What would change the call: Alani Nu synergy delivery ahead of plan with core-brand re-acceleration "
        "would validate the bull's share-gain thesis. A second year of core-brand stagnation, or promotional "
        "spend rising faster than revenue, would validate the bear and we would cut further. Watch Q3'26: "
        "Alani Nu integration metrics and the promotional-spend line are the numbers that matter.",
    ],
    "financials": [
        "The financial history is a step function: revenue $0.65B → $1.32B → $1.36B → $2.52B (2022–2025), "
        "with the 2024 flatline the most informative print — core-brand growth stalled before the "
        "acquisition. Free cash flow has been lumpy: $0.10B, $0.12B, $0.24B, $0.32B, with margins of 15.4%, "
        "9.1%, 17.6%, 12.7%. Our model assumes the business matures into a 24% mid-cycle FCF margin — a "
        "heroic assumption that does most of the valuation work, and the assumption we are least sure of.",
        "The capital structure is the hidden risk: $1.76 billion of PepsiCo preferred plus $54 million of "
        "net debt sits senior to ~260 million common shares. At our $23 target the equity is worth roughly "
        "$6.0 billion against $1.8 billion of senior claims — a 3.3x coverage that looks comfortable until "
        "growth stalls, at which point the preferred's seniority dominates the downside. This is a High "
        "risk rating earned by leverage structure as much as by category cyclicality.",
    ],
    "fin_table": {
        "headers": ["$ bn", "FY2022", "FY2023", "FY2024", "FY2025"],
        "rows": [
            ["Revenue", "0.65", "1.32", "1.36", "2.52"],
            ["YoY growth", "—", "+103%", "+3%", "+85%*"],
            ["Free cash flow", "0.10", "0.12", "0.24", "0.32"],
            ["FCF margin", "15.4%", "9.1%", "17.6%", "12.7%"],
        ],
        "footnote": "Sources: company filings; annuals via yfinance. *FY2025 includes the Alani Nu "
                    "acquisition. FY2026E: $3.3B revenue (model anchor).",
    },
    "moat": [
        ("Brand loyalty in a tribal category. ",
         "Energy-drink consumers are loyal to the point of identity; Celsius's functional positioning "
         "owns a distinct tribe. Alani Nu adds a second one."),
        ("PepsiCo distribution. ",
         "National retail reach that an independent could never build — the structural advantage that "
         "makes the scale story possible."),
        ("The moat's limit is the aisle. ",
         "Monster and Red Bull's scale in media buying, slotting, and sponsorship is structural; brand "
         "loyalty does not repeal the promotional arms race."),
        ("The preferred is anti-moat. ",
         "$1.76B of senior claims means equity holders are second in line — the capital structure "
         "works against shareholders precisely when the moat is tested."),
    ],
    "valuation_method": "10-year scenario DCF (FY2027–FY2036)",
    "valuation_intro": [
        "We value Celsius on a 10-year explicit DCF of free cash flow (FY2027–FY2036), weights bear 25% / "
        "base 50% / bull 25%. Scenario discounts: base 12.0% (challenger brand, category cyclicality, "
        "customer concentration via PepsiCo), bear 14.5% (base + 250bp), bull 10.5% (base − 150bp). "
        "Terminal growth 1.0% / 2.5% / 2.5% on year-10 FCF at the scenario's mid-cycle margin (20.5% / "
        "24% / 25%) — through-cycle levels, never peaks. Revenue CAGRs: bear 1.2%, base 5.5%, bull 8.3%, "
        "off a $3.3B FY2026E anchor. Equity = firm EV − $1.814B senior claims ($1.76B PepsiCo preferred + "
        "$54M net debt), over ~260M shares. Terminal value is 39–73% of EV across scenarios (bull 73% "
        "reflects the back-loaded growth profile); the composition below is derived analytically from the "
        "published scenario parameters — PV of the terminal value computed from year-10 FCF at the "
        "mid-cycle margin, with PV-explicit as the residual — since no scenario PV split was published.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 7.70,
            "assumptions": "The category's base rate for challengers: core brand matures, Alani Nu novelty fades; 1.2% revenue CAGR; promotional spend ratchets; mid-cycle FCF margins 20.5%; the preferred claim dominates a smaller equity value",
            "rev_cagr": "+1.2%", "margin_end": "20.5%",
            "discount": 0.145, "terminal_g": 0.01, "tv_share": 0.386,
            "pv_explicit": 2.34, "pv_terminal": 1.47, "cashflow_unit": "$bn",
        },
        "base": {
            "fair_value": 22.90,
            "assumptions": "The good version: 5.5% revenue CAGR; Alani Nu integrates cleanly; promotional intensity stays rational; mid-cycle FCF margins reach 24%",
            "rev_cagr": "+5.5%", "margin_end": "24%",
            "discount": 0.12, "terminal_g": 0.025, "tv_share": 0.605,
            "pv_explicit": 3.07, "pv_terminal": 4.70, "cashflow_unit": "$bn",
        },
        "bull": {
            "fair_value": 38.48,
            "assumptions": "Economics scale: 8.3% revenue CAGR; the two-brand portfolio takes durable share from the duopoly; 25% mid-cycle FCF margins",
            "rev_cagr": "+8.3%", "margin_end": "25%",
            "discount": 0.105, "terminal_g": 0.025, "tv_share": 0.731,
            "pv_explicit": 3.17, "pv_terminal": 8.65, "cashflow_unit": "$bn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "0.25×$7.70 + 0.50×$22.90 + 0.25×$38.48 = $23.00 → $23 target. "
                     "Bear meets all hurt conditions (growth stall, margin compression, 25%+ derating). "
                     "PV splits are derived analytically from the published scenario parameters (see "
                     "valuation method), not from a published model run.",
    "risks": [
        ("Category promotional arms race (the #1 risk). ",
         "Scale invites competitive response from Monster/Red Bull; defending share costs margin. "
         "Revenue can grow while economics compress."),
        ("Core-brand stagnation. ",
         "2024's flatline preceded Alani Nu; a second year of stagnation would break the growth narrative."),
        ("Alani Nu integration. ",
         "Synergy delivery, distribution expansion, and brand investment without cannibalizing Celsius — "
         "the near-term execution risk."),
        ("PepsiCo dependence. ",
         "Distribution partner and $1.76B senior claimant; strategic priorities may not align with "
         "common shareholders'."),
        ("Senior claims in a downturn. ",
         "$1.814B of preferred + net debt eats first; the equity's downside is amplified relative to "
         "the enterprise value."),
        ("Valuation. ",
         "At $26.75 the stock prices the bull case — any promotional or integration disappointment "
         "reprices toward the base ($22.90)."),
    ],
    "falsification": (
        "The base case's margin-expansion assumption would be withdrawn if promotional spend rises faster "
        "than revenue for two consecutive quarters, or if the core brand posts a second year of "
        "stagnation — at that point the bear case ($7.70) becomes the working assumption. Conversely, "
        "Alani Nu synergy delivery ahead of plan with core-brand re-acceleration validates the bull path. "
        "Watch Q3'26: Alani Nu integration metrics and the promotional-spend line are the numbers that matter."
    ),
    "methodology": [
        "We value the business on a 10-year explicit DCF of free cash flow (bear 25% / base 50% / bull 25%). "
        "Revenue follows the scenario path (bear 1.2% / base 5.5% / bull 8.3% 10-year CAGR off a $3.3B "
        "FY2026E anchor); free-cash-flow margin moves to the scenario's mid-cycle margin (20.5% / 24% / "
        "25%) over the horizon. Discount rates: base 12.0%, bear +250bp (14.5%), bull −150bp (10.5%). "
        "Terminal growth (1.0% / 2.5% / 2.5%) applies to year-10 FCF at the scenario's mid-cycle margin. "
        "Equity = firm EV − $1.814B senior claims ($1.76B PepsiCo preferred + $54M net debt); divided by "
        "~260M shares. The DCF composition chart is derived analytically from these published parameters "
        "(PV of terminal value from year-10 FCF; PV-explicit as the residual), since no scenario PV split "
        "was published. Bear cases must be genuinely adverse and sit below the current price. The published "
        "target is the probability-weighted fair value, stated as a 12-month horizon reference.",
        "Risk ratings (Low / Medium / Medium-High / High) combine business-model volatility, the balance "
        "sheet, and the valuation. This note is independent research-style analysis for informational purposes "
        "only and is not investment advice. Financial figures are drawn from company releases and SEC filings; "
        "market data as of October 2, 2026. Projections and the price target are the author's estimates and "
        "involve uncertainty. Past performance does not predict future results.",
    ],
    "charts": {
        "scenario": {"bear": 7.70, "base": 22.90, "bull": 38.48, "weighted": 23.00, "price": 26.75},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [0.65, 1.32, 1.36, 2.52],
            "fcf_hist": [0.10, 0.12, 0.24, 0.32],
            "years_proj": [2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": [3.48, 3.67, 3.87, 4.09, 4.31, 4.55, 4.80, 5.06, 5.34, 5.63],
            "fcf_proj": [0.84, 0.88, 0.93, 0.98, 1.03, 1.09, 1.15, 1.21, 1.28, 1.35],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via yfinance. Projection: base-case path off the $3.3B FY2026E "
                    "revenue anchor (5.5% 10-yr CAGR; FCF margin to a 24% mid-cycle level).",
        },
        "composition": {
            "bear": {"pv_explicit": 2.34, "pv_terminal": 1.47},
            "base": {"pv_explicit": 3.07, "pv_terminal": 4.70},
            "bull": {"pv_explicit": 3.17, "pv_terminal": 8.65},
            "unit": "$bn",
        },
        "extra": {
            "type": "line",
            "title": "FCF margin — history vs. base-case path to mid-cycle",
            "years": [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "series": [{"label": "FCF margin",
                        "values": [15.4, 9.1, 17.6, 12.7, 16.0, 18.0, 20.0, 21.5, 22.5, 23.0, 23.5, 24.0, 24.0, 24.0, 24.0]}],
            "ylabel": "%",
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "CELH-equity-research-note-polished.pdf")
build_note(data, out)
print("built:", out)
