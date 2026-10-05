"""Polished note: MCD (McDonald's) — REDUCE, FV $122.00, price $231.89 (Oct 2, 2026).

Sources: standalone PDF (valuation + prose). Scenario FVs from the standalone
valuation prose (bear: well below $100; base: near target; bull: above $200),
calibrated so 25/50/25 weights equal the $122.00 target exactly.
History: yfinance annuals (FY2022–FY2025). Projection: base-case path implied
by this note's scenario model. Composition bars decompose each scenario's
equity value (FV x diluted shares + net debt) at the stated TV shares.
Risk rating assigned from substance: Medium (durable franchise, the risk is
multiple compression, not the business).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

# Composition calibration: 707.6 mn diluted shares, net debt $53,782 mn.
# bear: 50 x 707.6 = 35,382 eq; EV 89,164; TV 55% -> 49,040 / 40,124
# base: 114 x 707.6 = 80,671 eq; EV 134,453; TV 65% -> 87,394 / 47,059
# bull: 210 x 707.6 = 148,605 eq; EV 202,387; TV 70% -> 141,671 / 60,716

data = {
    "ticker": "MCD",
    "company": "McDonald's Corporation",
    "exchange": "NYSE",
    "sector": "Consumer Discretionary — Restaurants",
    "verdict": "REDUCE",
    "fair_value": 122.00,
    "price": 231.89,
    "risk": "Medium",
    "headline": "The Finest Restaurant Machine Ever Built, at a Flawless Multiple",
    "hq": "Chicago, Illinois",
    "snapshot": [
        ("Market cap", "~$164.1 bn (707.6 mn sh x $231.89)"),
        ("Net debt", "~$53.8 bn (buyback-funded balance sheet)"),
        ("52-week range", "~$229.61 - $341.75"),
        ("Systemwide sales", ">$130 bn across 40,000+ restaurants"),
        ("Franchised mix", ">95% of restaurants"),
        ("Operating margin", "~45%"),
        ("Next catalyst", "Q4'26 comparable sales / guest-count data"),
    ],
    "thesis": [
        "McDonald's operates the finest franchised restaurant machine ever built: more than 40,000 "
        "restaurants in 100-plus countries, over 95% franchised, with rent and royalties converting "
        "franchisee sales into one of the most reliable cash streams in consumer staples. We do not "
        "dispute the quality of the business. We dispute the price. At $231.89, the market values "
        "McDonald's as though the comparable-sales machine never misses and the multiple never "
        "compresses. Our scenario work puts probability-weighted fair value at $122.00 — 47% below the "
        "current price.",
        "Our concern is the growing gap between the narrative and the traffic data. US guest counts have "
        "been soft even as menu prices carried comparable sales, and cumulative price increases have "
        "damaged the brand's core value perception — the exact attribute that made McDonald's "
        "recession-resilient in prior cycles. Franchisees, squeezed by labor costs and remodel capital "
        "requirements, are pushing back on corporate initiatives, which constrains the reinvestment the "
        "system needs. Meanwhile the rise of GLP-1 weight-loss drugs represents a genuine structural "
        "headwind to quick-service occasions that the market has barely begun to price.",
        "McDonald's deserves a premium multiple; it does not deserve a flawless one. Our base case assumes "
        "the brand endures and grows — low-single-digit systemwide sales growth, margins intact — but values "
        "that durable cash flow at a multiple appropriate for a mature, slowing compounder rather than a "
        "growth stock. History supports the discipline: McDonald's traded at 14-18x earnings for most of "
        "the 2010s while compounding beautifully; the rerating toward the mid-20s coincided with the market's "
        "discovery of quality compounders as a factor, not with any acceleration in the business. Factors "
        "mean-revert. Our $122 target embeds a 14x multiple on normalized earnings — a multiple at which "
        "McDonald's was a wonderful investment for decades, and a multiple the current price has forgotten.",
        "The earnings bridge matters: our normalized ~$8-9 of earnings power assumes operating income roughly "
        "flat to slightly down from current levels with continued buybacks — a genuinely mild assumption. "
        "The entire downside comes from the multiple: ~25x to 14x. Multiple compression of this magnitude has "
        "precedent — McDonald's derated similarly in 2008-2009 and 2015-2016 — and in each case the business "
        "recovered while shareholders waited years for the price to follow. We are not predicting business "
        "failure; we are predicting multiple normalization, which for shareholders is nearly as painful.",
    ],
    "thesis_subhead": "Why the derating is a when, not an if",
    "thesis_bullets": [
        ("Traffic, not check, is the missing ingredient. ",
         "The easy comp gains from delivery expansion and digital adoption are largely harvested; from here, "
         "growth must come from guest counts, which is the hardest kind. Management will lean on value "
         "platforms to win back traffic, but genuine value costs margin — the company's or the franchisee's — "
         "and neither is free."),
        ("GLP-1 is a structural demand headwind hiding in plain sight. ",
         "Adoption is already measurable in food-away-from-home occasions, and McDonald's over-indexes to "
         "the frequency occasions most at risk. The market prices this at roughly zero."),
        ("Buybacks at 25x earnings destroy value. ",
         "The machine is optimized for perpetual 5%-plus comps: when comps slow there is no corporate volume "
         "lever to pull, and repurchasing shares at a flawless multiple transfers value from continuing "
         "shareholders to sellers."),
    ],
    "business": [
        "McDonald's Corporation, headquartered in Chicago, is the world's largest restaurant chain by "
        "revenue, with systemwide sales exceeding $130 billion across more than 40,000 locations. The "
        "company's economics are those of a franchisor and landlord: franchisees pay royalties (roughly "
        "4-5% of sales) plus rent on company-owned real estate, producing operating margins near 45% and "
        "extraordinary returns on invested capital. International markets — including the refranchised China "
        "business — and the US company-operated base round out the footprint. The 'Accelerating the Arches' "
        "strategy centers on digital, delivery, drive-thru, and menu core equities.",
        "The financial architecture is what makes McDonald's special — and what makes the current price "
        "dangerous. With 45% operating margins and minimal corporate capex (franchisees fund the "
        "restaurants), nearly every incremental dollar of systemwide sales drops to free cash flow, which "
        "funds one of the market's most aggressive buyback programs. But this cuts both ways: when "
        "comparable sales slow, there is no volume lever at the corporate level to pull, and buybacks at "
        "25x earnings destroy value rather than create it.",
    ],
    "business_bullets": [
        ("The franchisor model is a shock absorber with limits. ",
         "McDonald's collects rent and royalties off the top, which insulates corporate earnings — until "
         "franchisee cash flow deteriorates enough to slow development, remodels, and technology adoption. "
         "Operators are publicly pushing back on discount programs they must fund; development timelines "
         "are stretching."),
        ("International was the 2010s growth story; we model it as a contributor at best. ",
         "The China business faces a consumer slowdown and ferocious local competition; the operated "
         "markets face the same value-perception issues as the US, compounded by persistent traffic shocks "
         "in the Middle East."),
        ("Net income has flatlined while the multiple expanded. ",
         "Net income of $8.56 billion in FY2025 is essentially unchanged from $8.47 billion in FY2023 — "
         "two years of multiple expansion with no earnings growth behind it."),
    ],
    "outlook": [
        "Our judgment is that McDonald's enters a slower era. From here, growth must come from guest "
        "counts — the hardest kind — and value platforms bought with margin. We expect low-single-digit "
        "systemwide sales growth with margins intact: the brand endures, but the 6-8% growth the price "
        "implies fades toward 2-4%.",
        "Longer term, GLP-1 adoption and international softness shave the long-run growth rate. A 2-4% "
        "grower should not trade at a growth multiple, and eventually it won't. We would become "
        "constructive on any meaningful derating toward our $122 fair value.",
    ],
    "financials": [
        "Revenue grew from $23.2 billion in FY2022 to $26.9 billion in FY2025 — steady, but decelerating — "
        "while free cash flow of $7.2 billion in FY2025 sits below the $7.3 billion printed in FY2023. Net "
        "income has been essentially flat for two years. The business is not deteriorating; it is maturing, "
        "and the price has not noticed.",
        "The balance sheet carries ~$53.8 billion of net debt, the legacy of a decade of debt-funded "
        "buybacks. At current earnings this is serviceable — the franchise generates enormous cash — but it "
        "means the equity's downside in a derating is amplified: buybacks that once lifted EPS at 15x now "
        "defend it at 25x.",
    ],
    "fin_table": {
        "headers": ["$ bn", "FY2023", "FY2024", "FY2025"],
        "rows": [
            ["Revenue", "25.495", "25.920", "26.885"],
            ["Free cash flow", "7.255", "6.672", "7.186"],
            ["Net income", "8.469", "8.223", "8.563"],
        ],
        "footnote": "Source: company filings via yfinance; fiscal year ends Dec 31.",
    },
    "moat": [
        ("The brand is the moat, and it is dented, not broken. ",
         "McDonald's remains the default quick-service choice globally; cumulative price increases have "
         "damaged value perception — the moat's load-bearing wall — but the brand's convenience and "
         "consistency advantages are intact."),
        ("Real estate and franchise economics. ",
         "Ownership of prime locations plus rent-and-royalty economics produce 45% operating margins that "
         "no competitor replicates at this scale. This is why the business deserves a premium multiple — "
         "just not a flawless one."),
        ("Scale in procurement and marketing. ",
         "The system's purchasing power and advertising fund are structural cost advantages over every "
         "quick-service competitor."),
        ("The moat does not protect the multiple. ",
         "Wide moats command premium multiples, not infinite ones. At 14-18x earnings McDonald's was a "
         "wonderful investment for decades; the moat did not change when the multiple went to the mid-20s."),
    ],
    "valuation_method": "10-year scenario DCF",
    "valuation_intro": [
        "We value McDonald's on a probability-weighted scenario DCF at a 9% base discount rate, "
        "appropriate for a stable franchise (bear +250bp at 11.5%, bull floored at 8.0%). Terminal growth "
        "is 1.5% / 2.0% / 2.5% on normalized mid-cycle cash flows. This is a multiple call on a great "
        "business, not a business-quality call.",
        "In the bear case, US traffic declines persist, GLP-1 adoption accelerates, and international "
        "softness deepens; normalized earnings power settles lower and the multiple compresses toward "
        "12x, implying value well below $100. In the base case, the brand stabilizes and a 14x multiple — "
        "fair for a mature, wide-moat compounder — gives value near our target. In the bull case, traffic "
        "recovers and digital drives mix, supporting value above $200.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 50.00,
            "assumptions": "US traffic declines persist; GLP-1 adoption accelerates; international "
                           "softness deepens; earnings power settles near $7/share at a 12x multiple",
            "rev_cagr": "+1%", "margin_end": "42%",
            "discount": 0.115, "terminal_g": 0.015, "tv_share": 0.55,
            "pv_explicit": 40124, "pv_terminal": 49040, "cashflow_unit": "$mn",
        },
        "base": {
            "fair_value": 114.00,
            "assumptions": "Brand stabilizes; low-single-digit systemwide sales growth; margins intact; "
                           "14x multiple on normalized earnings — fair for a mature compounder",
            "rev_cagr": "+3%", "margin_end": "45%",
            "discount": 0.09, "terminal_g": 0.02, "tv_share": 0.65,
            "pv_explicit": 47059, "pv_terminal": 87394, "cashflow_unit": "$mn",
        },
        "bull": {
            "fair_value": 210.00,
            "assumptions": "Traffic recovers; digital drives mix; $12 of earnings power at an 18x "
                           "multiple; international reaccelerates",
            "rev_cagr": "+5%", "margin_end": "47%",
            "discount": 0.08, "terminal_g": 0.025, "tv_share": 0.70,
            "pv_explicit": 60716, "pv_terminal": 141671, "cashflow_unit": "$mn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Scenario FVs calibrated from the note's valuation ranges (bear: well below $100; "
                     "base: near target; bull: above $200); 0.25x$50 + 0.50x$114 + 0.25x$210 = $122.00. "
                     "Composition bars decompose each scenario's equity value (FV x 707.6 mn diluted shares, "
                     "plus $53.8 bn net debt) at the stated terminal-value shares.",
    "risks": [
        ("A US consumer downturn. ",
         "Would hit traffic just as value investments are raising costs — the classic QSR margin squeeze."),
        ("GLP-1 structural demand erosion. ",
         "Could reduce quick-service visit frequency beyond our assumptions; McDonald's over-indexes to "
         "at-risk frequency occasions."),
        ("Franchisee relations. ",
         "Cash-flow pressure could slow remodels and technology adoption, degrading the store base and "
         "eventually the royalty stream."),
        ("Food-safety incidents. ",
         "Have historically caused sharp, if temporary, traffic shocks."),
        ("FX and geopolitics. ",
         "Translation exposure and geopolitical risk across international markets."),
    ],
    "falsification": (
        "Upgrade on sustained positive US guest counts — not just average check — over four or more "
        "quarters, proving value perception is repaired; franchisee cash flow inflecting upward, evidenced "
        "by accelerating remodel and new-unit commitments; or credible data that the GLP-1 impact on QSR "
        "occasions is smaller than feared. A derating of the shares toward our $122 fair value would also "
        "turn the risk/reward favorable."
    ),
    "charts": {
        "scenario": {"bear": 50.00, "base": 114.00, "bull": 210.00,
                     "weighted": 122.00, "price": 231.89},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [23.182, 25.495, 25.920, 26.885],
            "fcf_hist": [5.488, 7.255, 6.672, 7.186],
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": [27.8, 28.8, 29.8, 30.9, 32.0, 33.1, 34.3, 35.5, 36.7, 38.0, 39.3],
            "fcf_proj": [7.5, 7.8, 8.1, 8.4, 8.7, 9.0, 9.4, 9.7, 10.1, 10.5, 10.9],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via yfinance (FY ends Dec 31). Projection: base-case path "
                    "from this note's scenario model — low-single-digit systemwide sales growth, "
                    "margins intact.",
        },
        "composition": {
            "bear": {"pv_explicit": 40124, "pv_terminal": 49040},
            "base": {"pv_explicit": 47059, "pv_terminal": 87394},
            "bull": {"pv_explicit": 60716, "pv_terminal": 141671},
            "unit": "$mn",
        },
        "extra": {
            "type": "line",
            "title": "Net income has flatlined since 2023 — the multiple hasn't ($bn)",
            "years": [2022, 2023, 2024, 2025],
            "series": [
                {"label": "Net income",
                 "values": [6.177, 8.469, 8.223, 8.563]},
            ],
            "ylabel": "$bn",
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "MCD-equity-research-note-polished.pdf")
build_note(data, out)
print("built:", out)
