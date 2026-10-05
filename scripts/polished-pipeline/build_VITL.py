"""Polished note build: Vital Farms (VITL). Scenario numbers from the valuation model (valuation_output_v2.json). Re-runnable."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

# Base-case FCF series ($mn, 2027-2036) and scenario PVs from valuation_output_v2.json
FCF_BASE = [-70.2, -8.3, 27.6, 55.5, 70.9, 81.2, 85.4, 88.9, 91.7, 93.8]
FCF_BEAR = [-78.0, -15.9, 4.0, 16.6, 25.8, 31.2, 32.0, 32.9, 33.6, 34.1]
FCF_BULL = [-55.3, 8.9, 47.7, 75.6, 96.2, 114.8, 123.9, 130.9, 136.5, 140.0]

# Base revenue path: 2026E ~$0.90bn, then model revenue CAGR 6.2%
rev_proj = [0.90]
for _ in range(10):
    rev_proj.append(round(rev_proj[-1] * 1.062, 3))

data = {
    "ticker": "VITL",
    "company": "Vital Farms, Inc.",
    "exchange": "NASDAQ",
    "sector": "Consumer Staples — Packaged Foods",
    "verdict": "BUY",
    "fair_value": 12.50,
    "price": 9.06,
    "risk": "Medium-High",
    "headline": "A Branded Franchise Priced Like a Commodity Egg Producer",
    "snapshot": [
        ("Market cap", "~$0.39 bn (42.9 mn sh × $9.06)"),
        ("52-week range", "~$7.95 – $45.16"),
        ("Category", "Pasture-raised eggs + butter, US grocery"),
        ("Model", "Asset-light: contract family-farm network"),
        ("Distribution", "Large majority of US food-retail doors"),
        ("Velocity", "Among the highest in the egg category"),
        ("Gross margin", "Mid-30s demonstrated brand range"),
        ("Shares (diluted)", "~42.9 mn"),
        ("Net debt", "~$9 mn (effectively unlevered)"),
        ("Implied upside", "+38% to $12.50 fair value"),
    ],
    "thesis": [
        "Vital Farms sells something simple: pasture-raised eggs and butter at a premium price, in a "
        "category where the conventional product has been commoditized and the premium shelf is still "
        "being built. The thesis is not that eggs are a growth category; it is that branded, "
        "credence-attribute food (pasture-raised, ethically sourced) commands durable shelf space and "
        "pricing power, and Vital Farms owns the leading brand in its aisle. Revenue growth has been "
        "consistently strong because distribution is still expanding and same-store velocity is high.",
        "Our judgment is that the market prices Vital Farms like a volatile food manufacturer exposed "
        "to commodity egg prices, when the business is really a branded consumer franchise with a "
        "supply-constrained moat. The pasture-raised standard is hard to scale quickly — it requires "
        "real pasture and real farm relationships — which limits copycats and supports the premium. "
        "We tested the margin targets against the historical pattern of input-cost shocks and recovery; "
        "the brand has repeatedly taken price without losing volume, which is the signature of pricing "
        "power.",
        "At $9.06, the multiple embeds a reversion to commodity-like margins that the track record does "
        "not support. Our probability-weighted fair value is $12.50, a 38% expected return, driven by "
        "continued distribution gains and margin normalization toward the brand's demonstrated range. "
        "The bear case — premium-tier saturation, private-label erosion, margin compression — is "
        "genuinely painful and sits well below today's price.",
        "We also like the capital-light structure. Because production is contracted rather than owned, "
        "growth does not require building plants; the company's capital goes to brand, distribution, and "
        "the supply-chain team that manages the farm network. Returns on invested capital are therefore "
        "high for a food company, and the business can scale revenue without a commensurate scale in "
        "fixed assets.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("The farm network is a supply-constrained moat. ",
         "Bringing a new farm into the network — converting pasture, building houses, certifying "
         "standards — takes the better part of a year. Supply cannot respond quickly to demand "
         "spikes, which functions as a moat: no competitor can flood the pasture-raised shelf on "
         "short notice, and first-mover relationships with the best operators are hard to replicate."),
        ("Pricing power is demonstrated, not asserted. ",
         "Through input-cost shocks the brand has repeatedly taken price without losing volume. "
         "That is the empirical signature of a franchise, and it is what the current multiple refuses "
         "to pay for."),
        ("Butter is the second act. ",
         "The same playbook — pasture-raised positioning, premium pricing, the same retail buyer "
         "relationships — applied to butter demonstrates that the brand equity transfers beyond eggs, "
         "extending the growth runway. We do not assume it becomes large in the base case."),
    ],
    "business": [
        "Vital Farms is a food company built around pasture-raised eggs and butter, sold primarily "
        "through grocery retail in the United States. The brand's core promise is ethical sourcing: hens "
        "raised on pasture with outdoor access, sourced from a network of hundreds of family farms. "
        "Products command a significant price premium over conventional and even cage-free alternatives.",
        "The business model is asset-light on production (contract family farms supply the eggs) and "
        "brand-heavy on the demand side. Growth comes from two levers: expanding distribution into new "
        "doors and regions, and increasing velocity within existing stores as consumer awareness of the "
        "pasture-raised standard grows. Gross margins are meaningfully above conventional egg economics "
        "because the premium price more than offsets higher sourcing costs, though input and freight "
        "costs create quarterly volatility.",
        "Distribution is concentrated in the natural and conventional grocery channels, with the brand now "
        "present in a large majority of US food retail doors. Velocity — units sold per store per week — "
        "is among the highest in the egg category, which is why retailers keep expanding shelf "
        "allocation: Vital Farms turns the premium egg set faster than slower-moving alternatives.",
    ],
    "business_bullets": [
        ("The butter business applies the same playbook to a second category. ",
         "Pasture-raised positioning, premium pricing, and the same retail buyer relationships. It is "
         "smaller and earlier-stage, but it proves the brand equity transfers beyond eggs."),
        ("Retailers are partners, not just customers. ",
         "High velocity per store-week makes Vital Farms a productive use of premium shelf space, "
         "which is why door counts and shelf allocation have kept expanding."),
        ("Effectively unlevered. ",
         "Net debt of roughly $9 million against a $390 million market cap — the balance sheet is a "
         "non-issue and all of the risk sits in the operating story."),
    ],
    "outlook": [
        "Where is this business going? We expect Vital Farms to keep taking share of the premium egg "
        "aisle for years, because the category conversion (conventional to cage-free to pasture-raised) "
        "is still early and the company is the recognized standard-bearer. The farm network is the "
        "binding constraint: adding contracted family farms takes time, which caps near-term growth but "
        "also protects pricing — a trade we like.",
        "The central question for the next five years is how large the pasture-raised segment can become. "
        "Our base case assumes the premium tier continues to take share from conventional and cage-free, "
        "supported by retailer commitments to cage-free sourcing that push consumers up the welfare "
        "ladder. If pasture-raised reaches even a mid-single-digit share of the total egg market, Vital "
        "Farms' revenue more than doubles from current levels. We model revenue growth moderating from "
        "current elevated rates to a sustainable high-single-digit pace as distribution matures, with "
        "gross margins recovering to the mid-30s range the brand has demonstrated.",
        "Margins should benefit from scale in two ways: fixed corporate costs spread over a larger "
        "revenue base, and improved logistics density as volumes grow in existing regions. Offsetting "
        "this, the company will keep investing in the farm network and in brand marketing, so we model "
        "gradual rather than dramatic operating leverage. Butter and adjacent categories extend the "
        "runway beyond eggs.",
        "Our bear case assumes the premium tier saturates, private label undercuts the pasture-raised "
        "price point, and input cost inflation outruns pricing. Because this is a small-cap with "
        "commodity exposure, we use a discount rate at the higher end of our standard range (12% base); "
        "the bear case adds further stress to both growth and margins.",
    ],
    "financials": [
        "Revenue has compounded from $0.36 billion in 2022 to $0.76 billion on a trailing basis in 2025, "
        "roughly doubling in three years on distribution expansion and velocity. Net income has scaled "
        "from near zero to $66 million trailing. Free cash flow is lumpy year to year — negative in "
        "farm-network investment years — because growth capital goes into the supply chain rather than "
        "plants.",
        "The P&L signature is that of a brand, not a commodity producer: gross margins in the mid-30s "
        "through input-cost volatility, with pricing taken to recover shocks. The valuation hinges on "
        "the terminal margin and the duration of high growth; our base case assumes margins recover to "
        "the demonstrated brand range rather than reverting to commodity economics.",
    ],
    "fin_table": {
        "headers": ["$ mn", "2022", "2023", "2024", "2025 (TTM)"],
        "rows": [
            ["Revenue", "362", "472", "606", "759"],
            ["Net income", "1", "26", "53", "66"],
            ["Free cash flow", "−19", "39", "36", "−48"],
        ],
        "footnote": "Sources: company filings via Yahoo Finance. 2025 = trailing twelve months.",
    },
    "moat": [
        ("The pasture standard is a supply moat. ",
         "Real pasture and real farm relationships cannot be scaled quickly; the year-long lead time to "
         "bring a farm into the network caps both Vital Farms' growth and every competitor's."),
        ("Brand ownership of the premium shelf. ",
         "The recognized standard-bearer in pasture-raised, with the highest velocity in the category — "
         "retailers allocate shelf to what turns."),
        ("Demonstrated pricing power. ",
         "Repeated price increases through input-cost shocks without volume loss — the empirical "
         "signature of a franchise."),
        ("Capital-light scaling. ",
         "Contracted production means revenue can scale without commensurate fixed-asset investment, "
         "keeping returns on capital high for a food company."),
    ],
    "valuation_method": "10-year scenario FCF DCF",
    "valuation_intro": [
        "We value Vital Farms on a 10-year scenario free-cash-flow DCF — weights bear 25% / base 50% / "
        "bull 25% — with scenario-specific discounts: bear 14.5%, base 12.0% (higher end of the standard "
        "range for a small-cap with commodity-input exposure), bull 10.5%. Terminal growth is 1.0% / "
        "2.5% / 2.5% on year-10 free cash flow at normalized mid-cycle margins. Net debt is only "
        "~$9 million on 42.9 million diluted shares, so enterprise and equity value are nearly identical.",
        "Scenario fair values: bear $1.36 (premium-tier saturation, private-label erosion, margin "
        "compression), base $12.15 (6.2% revenue CAGR, 7.0% year-10 FCF margin), bull $24.32 (10.9% "
        "revenue CAGR, faster category conversion and adjacency success). Probability-weighted: $12.50.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 1.36,
            "assumptions": "Premium tier saturates; private label undercuts the pasture-raised price point; input-cost inflation outruns pricing; margins compress to commodity levels",
            "rev_cagr": "+2.5%", "margin_end": "3.5%",
            "discount": 0.145, "terminal_g": 0.01, "tv_share": 0.98,
            "pv_explicit": 1.3, "pv_terminal": 65.9, "cashflow_unit": "$mn",
        },
        "base": {
            "fair_value": 12.15,
            "assumptions": "Distribution-led double-digit growth tapering to high-single digits; gross margins recover to mid-30s brand range; year-10 FCF margin 7.0%",
            "rev_cagr": "+6.2%", "margin_end": "7.0%",
            "discount": 0.12, "terminal_g": 0.025, "tv_share": 0.614,
            "pv_explicit": 204.8, "pv_terminal": 325.9, "cashflow_unit": "$mn",
        },
        "bull": {
            "fair_value": 24.32,
            "assumptions": "Faster category conversion to pasture-raised; butter and adjacencies scale; pricing power fully sustained; 10.9% revenue CAGR",
            "rev_cagr": "+10.9%", "margin_end": "7.0%",
            "discount": 0.105, "terminal_g": 0.025, "tv_share": 0.627,
            "pv_explicit": 392.4, "pv_terminal": 660.9, "cashflow_unit": "$mn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "risks": [
        ("Input costs. ",
         "Feed, freight, and packaging inflation can compress margins faster than pricing recovers "
         "them."),
        ("Supply. ",
         "Avian influenza or farm-network disruptions could constrain the egg supply the growth story "
         "depends on."),
        ("Competition. ",
         "Larger food companies or private label could attack the pasture-raised premium with lower "
         "prices."),
        ("Category risk. ",
         "If premium egg growth stalls, the multiple compresses regardless of execution."),
        ("Scale and concentration. ",
         "As a small-cap, quarterly results are volatile; a small number of large grocery retailers "
         "represent a significant share of sales."),
        ("Brand risk. ",
         "The ethical-sourcing promise is the brand; any supply-chain controversy would damage it "
         "disproportionately."),
    ],
    "falsification": (
        "Downgrade to HOLD if the brand loses market share in tracked channels to private label or "
        "branded competitors, if gross margins settle durably below the mid-30s (commodity dynamics "
        "overwhelming brand pricing power), or if distribution expansion stalls with door counts flat "
        "for several quarters. A sustained consumer shift away from premium food tiers would undermine "
        "the category thesis itself."
    ),
    "charts": {
        "scenario": {"bear": 1.36, "base": 12.15, "bull": 24.32,
                     "weighted": 12.50, "price": 9.06},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [0.362, 0.472, 0.606, 0.759],
            "fcf_hist": [-0.019, 0.039, 0.036, -0.048],
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": rev_proj,
            "fcf_proj": [None] + [round(f / 1000, 3) for f in FCF_BASE],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via Yahoo Finance (2025 = TTM). Projection: base-case "
                    "model FCF series ($mn→$bn); revenue path at the model's 6.2% CAGR from ~$0.90bn "
                    "2026E.",
        },
        "composition": {
            "bear": {"pv_explicit": 1.3, "pv_terminal": 65.9},
            "base": {"pv_explicit": 204.8, "pv_terminal": 325.9},
            "bull": {"pv_explicit": 392.4, "pv_terminal": 660.9},
            "unit": "$mn",
        },
        "extra": {
            "type": "line",
            "title": "Scenario free-cash-flow paths ($mn)",
            "years": [2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "series": [
                {"label": "Bear", "values": FCF_BEAR},
                {"label": "Base", "values": FCF_BASE},
                {"label": "Bull", "values": FCF_BULL},
            ],
            "ylabel": "$mn",
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "VITL-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
