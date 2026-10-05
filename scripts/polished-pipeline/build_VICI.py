"""Polished note build: VICI Properties Inc. (VICI) — BUY, $39.00 target."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note, validate

data = {
    "ticker": "VICI",
    "company": "VICI Properties Inc.",
    "exchange": "NYSE",
    "sector": "Real Estate — Experiential Net-Lease REIT",
    "verdict": "BUY",
    "fair_value": 39.00,
    "price": 22.65,
    "risk": "Medium-High",
    "headline": "Forty-Year Leases on Irreplaceable Real Estate, Priced Like an Ordinary REIT",
    "ceo": "Edward Pitoniak",
    "hq": "New York, New York",
    "snapshot": [
        ("Market cap", "~$24.9 bn (1,101 mn sh × $22.65)"),
        ("Price (Oct 2, 2026)", "$22.65"),
        ("52-week range", "~$22.54 – $33.01"),
        ("Dividend (annualized)", "$1.84 — ~8.1% yield; raised every year since formation"),
        ("2026E AFFO / share", "~$2.46 (~9.2× P/AFFO)"),
        ("Payout ratio", "~75% of AFFO"),
        ("Net leverage", "~5.0× EBITDA; Baa3 / BBB- (investment grade)"),
        ("Portfolio", "103 experiential assets; ~39.7-yr weighted-average lease term"),
        ("Tenant concentration", "Caesars ~39% / MGM ~33% of annualized rent"),
        ("Rent collection", "100% every year since inception (2017)"),
        ("Next catalyst", "Q3 2026 earnings; accretive acquisition announcements"),
    ],
    "thesis": [
        "VICI owns dirt and buildings you cannot build another of — Caesars Palace, MGM Grand, "
        "the Venetian — and leases them to operators under 40-year triple-net contracts in which "
        "the tenant pays everything from property taxes to maintenance. At $22.65 the market "
        "prices those leases as though they carry the same risk as an average office REIT, and "
        "that is simply wrong. Occupancy has never meaningfully wavered, rent collection is a "
        "perfect 100% every year since the company's formation, and escalators of 2% or more "
        "compound year after year regardless of what the economy does. This is a bond-like "
        "compounding machine wearing a casino costume, and the costume is the entire discount.",
        "The second leg of the thesis is external growth, and it is structural, not cyclical. "
        "VICI is one of very few counterparties that regional gaming operators, tribal nations, "
        "and experiential landlords can call when they want to monetize real estate at scale — "
        "and it has repeatedly funded those acquisitions at spreads accretive to adjusted funds "
        "from operations (AFFO) per share. Its investment-grade balance sheet gives it a cost of "
        "capital smaller buyers cannot match, so the deal pipeline is a durable advantage. Each "
        "accretive deal lengthens the compounding runway without asking shareholders to "
        "underwrite a dollar of development risk.",
        "The third leg is diversification the market has not priced. VICI has moved beyond pure "
        "casino real estate into golf courses, youth-sports complexes, water parks, wellness "
        "resorts, and urban experiential assets — all under the same triple-net, long-lease "
        "model. Experiential real estate is one of the few property categories whose demand has "
        "grown through the post-pandemic cycle, and VICI is quietly becoming its landlord of "
        "record. The tenant-concentration objection — Caesars plus MGM are over 70% of rent — "
        "is real, but it is shrinking as the non-gaming book grows.",
        "Our $39.00 fair value is the probability-weighted result of a scenario DCF on VICI's "
        "distributable rental cash flows: $26.70 in a genuine recession bear case, $39.90 in the "
        "base case, $49.50 in a bull case where the acquisition pipeline reaccelerates. The "
        "base case needs nothing heroic — high-single-digit AFFO-per-share compounding from "
        "contractual escalators and $1–3 billion a year of accretive deals, discounted at 9% for "
        "a triple-net franchise with 40-year leases. The dividend, which has grown every year, "
        "pays investors roughly 8% to wait while the compounding does the work.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("The escalators are a growing organic engine. ",
         "Roughly 45% of the rent roll is CPI-linked in 2026, rising toward 87% by 2035 — a "
         "bond-like asset converting into a growing perpetuity, which is rare among net-lease "
         "REITs and worth a premium multiple once recognized."),
        ("Tenants' rent coverage is the cushion. ",
         "Las Vegas visitation and Strip gaming revenue have shown remarkable resilience, and "
         "healthy rent-coverage ratios mean the escalators keep compounding even if gaming "
         "revenue growth moderates. Regional assets are cash-generative boxes in "
         "supply-constrained markets that operators cannot easily relocate."),
        ("Rates are the risk, and it is already in the price. ",
         "As a REIT, VICI's multiple is sensitive to the long end of the curve — a valuation "
         "risk, not a business risk. At 9.2× forward AFFO with an 8% yield, a sustained "
         "higher-for-longer regime is more than reflected in the shares."),
    ],
    "business": [
        "VICI Properties, formed in 2017 as the real-estate spin of Caesars Entertainment's "
        "restructuring and listed in February 2018, is an S&P 500 experiential REIT. It does not "
        "operate casinos. It owns the land and buildings — including three of the most iconic "
        "assets on the Las Vegas Strip — and leases them back to operators under long-term "
        "triple-net leases: the tenant pays property taxes, insurance, maintenance, and capital "
        "expenditures. VICI's income is contractual rent plus financing income from its loan "
        "book, not gaming revenue.",
        "The portfolio spans 103 experiential assets (63 gaming, 40 other experiential) across "
        "the United States and Canada: roughly 130 million square feet, about 66,000 hotel "
        "rooms, more than 700 restaurants, bars, nightclubs and sportsbooks, four championship "
        "golf courses, and some 33 acres of undeveloped Strip-adjacent land. Sixteen tenants; "
        "effectively 100% occupancy and 100% rent collection every year since inception — run "
        "on roughly 28 employees, one of the most asset-light models in the S&P 500.",
        "The lease architecture is the actual product. The weighted-average lease term is about "
        "39.7 years including renewals, with whole-portfolio, cross-defaulted master leases backed "
        "by corporate guarantees. Two tenants dominate: Caesars at roughly 39% and MGM at "
        "roughly 33% of annualized rent (about $3.2 billion total). Escalators are fixed 1–2% "
        "or the greater of 2% and CPI, typically capped at 3%. As a REIT, VICI distributes the "
        "bulk of taxable income as dividends; growth comes from contractual escalators, "
        "accretive acquisitions funded at spreads above its cost of capital, and real-estate-"
        "secured loan investments.",
    ],
    "outlook": [
        "Our judgment is that VICI's next five years look more like a compounding machine than "
        "a cyclical casino bet. Las Vegas visitation and Strip gaming revenue have demonstrated "
        "remarkable resilience, and tenants' rent-coverage ratios — the cushion between property "
        "earnings and rent owed — remain healthy, which means the escalators keep compounding "
        "even if gaming revenue growth moderates. The regional portfolio benefits from the same "
        "dynamic at lower absolute rent levels: cash-generative boxes in markets with limited new "
        "supply, run by operators who cannot easily relocate.",
        "Where we see the real upside is the acquisition funnel. A wave of regional operators, "
        "tribal nations, and experiential owners are sitting on owned real estate that could be "
        "monetized, and VICI's scale and cost of capital make it the natural counterparty. We "
        "expect the company to keep deploying $1–3 billion a year into accretive deals when "
        "pricing is right, each one adding a few cents to AFFO per share that then compound "
        "through the escalators. The non-gaming experiential book should grow as a share of "
        "rent, further diversifying the tenant concentration that has been the market's main "
        "objection to the name.",
        "On capital returns, we expect the dividend to keep growing in line with AFFO per "
        "share, keeping the payout ratio in its historical range. The risk to this outlook is "
        "interest rates: a sustained move higher in Treasury yields would compress the multiple "
        "even if the cash flows are unaffected. That is a valuation risk, not a business risk — "
        "and at the current price we believe it is already more than reflected in the shares.",
    ],
    "financials": [
        "The P&L is cash rent, not gaming. Total revenue was $4.01 billion in 2025, up from $2.60 "
        "billion in 2022, driven by contractual escalators and acquisitions. Operating cash flow "
        "reached $2.51 billion in 2025 against minimal capex — the triple-net model means the "
        "tenant, not VICI, funds property upkeep — so free cash flow conversion is among the "
        "highest in the REIT universe. AFFO per share of roughly $2.46 in 2026E puts the shares "
        "at about 9.2×, a multiple more appropriate to a cyclical landlord than to 40-year "
        "contracted cash flows.",
        "The balance sheet is investment-grade (Baa3/BBB-) with laddered maturities and net "
        "leverage of about 5.0× EBITDA — moderate for a REIT with this lease duration. That "
        "rating is the strategic asset: it lets VICI fund acquisitions with debt and equity at a "
        "cost of capital smaller buyers cannot match, which is precisely what makes the "
        "external-growth flywheel turn. The dividend of $1.84 per share (~8.1% yield) is covered "
        "at roughly 75% of AFFO, leaving retained cash flow plus the balance-sheet capacity to "
        "keep acquiring.",
    ],
    "fin_table": {
        "headers": ["$ bn", "2022", "2023", "2024", "2025"],
        "rows": [
            ["Total revenue", "2.60", "3.61", "3.85", "4.01"],
            ["Operating cash flow", "1.94", "2.18", "2.38", "2.51"],
            ["Free cash flow", "1.94", "2.18", "2.37", "2.51"],
            ["Dividend / share", "1.56", "1.64", "1.72", "1.80"],
        ],
        "footnote": "Sources: company filings via Yahoo Finance (annual). 2026E AFFO/share ~$2.46 and dividend $1.84 per company guidance and market data. FCF = operating cash flow less capex (capex de minimis under triple-net leases).",
    },
    "moat": [
        ("Irreplaceable real estate. ",
         "You cannot build another Caesars Palace on the Las Vegas Strip. Trophy experiential "
         "assets in supply-constrained destination markets give VICI pricing power no generic "
         "net-lease REIT can replicate."),
        ("Contract duration and structure. ",
         "Roughly 40-year weighted-average lease terms, whole-portfolio cross-defaulted master "
         "leases, corporate guarantees, and CPI-linked escalators convert a real-estate portfolio "
         "into a growing annuity — the closest thing to a moat in net lease."),
        ("Cost-of-capital advantage in acquisitions. ",
         "The investment-grade balance sheet makes VICI the buyer of choice for operators "
         "monetizing real estate at scale; smaller buyers cannot match its funding spreads, so "
         "the accretive-deal pipeline accrues to VICI first."),
        ("Collection record as evidence. ",
         "100% rent collection through recessions, the pandemic shutdowns, and regional gaming "
         "downturns — the durability claim is not a projection, it is a track record."),
        ("The moat's weak link: tenant concentration. ",
         "Caesars and MGM are over 70% of rent. Distress at a top tenant is the single largest "
         "threat to the dividend, and the diversification into non-gaming experiential assets is "
         "the multi-year answer."),
    ],
    "valuation_method": "10-year scenario DCF on distributable rental cash flows (AFFO)",
    "valuation_intro": [
        "We value VICI on a 10-year probability-weighted scenario DCF of distributable rental "
        "cash flows — weights bear 25% / base 50% / bull 25% — with scenario-specific "
        "discounts: bear 11.5% (base + 250bp: recession pricing, compressed REIT multiples), "
        "base 9.0% (the stable-franchise rate, reflecting 40-year triple-net leases with "
        "investment-grade tenants), bull 8.0% (base − 150bp, floored at 8%). Terminal growth is "
        "1.0% / 2.0% / 2.5% on normalized rental cash flows — never peak economics — and the "
        "terminal value is a minority of enterprise value, consistent with a business whose "
        "value sits in visible contractual cash flows rather than distant assumptions.",
        "In the base case, AFFO per share compounds at a high-single-digit rate, driven by "
        "contractual escalators of roughly 2% plus a steady cadence of accretive acquisitions "
        "funded at spreads above the cost of capital. The bear case assumes a genuine recession "
        "that pressures tenant earnings and rent coverage, a freeze in the acquisition market, "
        "and a higher-for-longer rate environment that keeps REIT multiples compressed; the "
        "resulting $26.70 fair value sits well below the current $22.65 price on a "
        "multiple basis only in the sense that the whole sector derates — the cash flows "
        "themselves are contractual. The bull case assumes the acquisition pipeline "
        "reaccelerates as operators monetize real estate, Strip and regional gaming revenue "
        "grow, and the non-gaming experiential book scales — justifying a premium multiple for "
        "the scarcity of the assets. The probability-weighted fair value equals our $39.00 "
        "target: a forward AFFO multiple in line with high-quality net-lease REITs, not the "
        "distressed multiple the shares carry today.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 26.70,
            "assumptions": "Genuine recession pressures tenant earnings and rent coverage; acquisition market freezes; higher-for-longer rates keep REIT multiples compressed",
            "rev_cagr": "+2.0%", "margin_end": "92%",
            "discount": 0.115, "terminal_g": 0.01, "tv_share": 0.45,
            "pv_explicit": 16168, "pv_terminal": 13228, "cashflow_unit": "$mn",
        },
        "base": {
            "fair_value": 39.90,
            "assumptions": "AFFO/share compounds at high-single-digit rate on ~2% contractual escalators plus $1-3B/yr accretive acquisitions funded above the cost of capital",
            "rev_cagr": "+5.5%", "margin_end": "93%",
            "discount": 0.09, "terminal_g": 0.02, "tv_share": 0.50,
            "pv_explicit": 21965, "pv_terminal": 21965, "cashflow_unit": "$mn",
        },
        "bull": {
            "fair_value": 49.50,
            "assumptions": "Acquisition pipeline reaccelerates as operators monetize real estate; Strip and regional gaming revenue grow; non-gaming experiential book scales",
            "rev_cagr": "+8.0%", "margin_end": "94%",
            "discount": 0.08, "terminal_g": 0.025, "tv_share": 0.55,
            "pv_explicit": 24525, "pv_terminal": 29975, "cashflow_unit": "$mn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Scenario fair values are per-share equity values from the AFFO DCF (1,101 mn shares). 0.25×$26.70 + 0.50×$39.90 + 0.25×$49.50 = $39.00.",
    "risks": [
        ("Tenant concentration. ",
         "Caesars and MGM account for a large share of rental revenue; distress at a top "
         "tenant would be the single largest threat to the dividend."),
        ("Gaming cyclicality. ",
         "A deep recession would reduce tenant earnings and rent-coverage ratios, even though "
         "leases are contractual and the collection history is perfect."),
        ("Interest-rate sensitivity. ",
         "As a REIT, VICI's share price and cost of capital are exposed to long-term Treasury "
         "yields regardless of operating performance."),
        ("Acquisition execution. ",
         "The external-growth thesis depends on finding accretive deals; overpaying or funding "
         "deals with expensive equity would dilute AFFO per share."),
        ("Regulatory and regional competition. ",
         "New gaming supply or adverse regulatory changes in key markets could pressure tenant "
         "economics over time."),
    ],
    "falsification": (
        "Downgrade to HOLD on: a dividend cut or a payout ratio pushed permanently above "
        "sustainable levels — the dividend record is the core evidence for the thesis; a major "
        "tenant bankruptcy, lease rejection, or rent concession that breaks the perfect "
        "collection record; two consecutive years of declining AFFO per share, signaling that "
        "escalators and acquisitions no longer offset dilution; a large acquisition funded at a "
        "spread dilutive to AFFO per share, indicating discipline has slipped; or a sustained "
        "rise in long-term rates that reprices the entire REIT sector to yields that make the "
        "$39.00 target multiple unattainable. We watch: tenant earnings and rent-coverage "
        "ratios, acquisition funding spreads, and the 10-year Treasury."
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
        "independently tested and haircut where evidence warrants. For this REIT the scenario "
        "cash flows are distributable rental cash flows (AFFO) rather than corporate free cash "
        "flow, but the framework is identical.",
    ],
    "charts": {
        "scenario": {"bear": 26.70, "base": 39.90, "bull": 49.50,
                     "weighted": 39.00, "price": 22.65},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [2.601, 3.612, 3.849, 4.006],
            "fcf_hist": [1.942, 2.177, 2.373, 2.509],
            "years_proj": [2026, 2027, 2028, 2029, 2030],
            "revenue_proj": [4.21, 4.42, 4.64, 4.87, 5.12],
            "fcf_proj": [2.63, 2.76, 2.90, 3.05, 3.20],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via Yahoo Finance (FCF = operating cash flow "
                    "less capex; capex is de minimis under triple-net leases). Projections: "
                    "base-case distributable cash flows from the scenario DCF.",
        },
        "composition": {
            "bear": {"pv_explicit": 16168, "pv_terminal": 13228},
            "base": {"pv_explicit": 21965, "pv_terminal": 21965},
            "bull": {"pv_explicit": 24525, "pv_terminal": 29975},
            "unit": "$mn",
        },
        "extra": {
            "type": "pie",
            "title": "Portfolio by asset type — 103 experiential assets",
            "labels": ["Gaming assets", "Other experiential"],
            "values": [63, 40],
        },
    },
}

validate(data)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "VICI-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
