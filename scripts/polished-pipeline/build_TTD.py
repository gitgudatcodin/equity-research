"""Polished note build: TTD (The Trade Desk, Inc.). Re-runnable via template.build_note."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

data = {
    "ticker": "TTD",
    "company": "The Trade Desk, Inc.",
    "exchange": "NASDAQ",
    "sector": "Technology — Advertising Technology",
    "verdict": "BUY",
    "fair_value": 21.00,
    "price": 11.95,
    "risk": "Medium-High",
    "headline": "Priced for Obsolescence; the Bear Case Is Only $10.34",
    "ceo": "Jeff Green",
    "hq": "Ventura, California",
    "snapshot": [
        ("Market cap", "~$5.6 bn (~470 mn sh × $11.95)"),
        ("Enterprise value", "~$4.1 bn"),
        ("Net cash", "$1.49 bn ($3.16/sh); no funded debt"),
        ("52-week range", "~$11.77 – $56.39"),
        ("FY2025 revenue", "$2,896 mn (+18.5%)"),
        ("Q2'26 revenue", "$715 mn (+3% YoY); Q3 guide ≥$650 mn"),
        ("Take rate", "~21.6% (stable for years)"),
        ("Client retention", ">95%, 12 years running"),
        ("Joint business plans", "217 in Q2'26 (+38% YoY)"),
        ("Next catalyst", "Q3'26 earnings, ~early November"),
    ],
    "thesis": [
        "The Trade Desk is the leading independent demand-side platform for programmatic advertising, and "
        "independence is the entire investment thesis. The digital advertising market is bifurcating into "
        "walled gardens — Google, Meta, Amazon — where the platform grades its own homework, and the open "
        "internet, where advertisers need a neutral party to buy media objectively across publishers. The "
        "Trade Desk is that neutral party at scale, and its structural position improves as connected TV — "
        "the largest secular shift in media buying — moves more premium video inventory into programmatic "
        "channels. At $11.95 the shares price The Trade Desk as a growth-challenged ad-tech vendor; we see "
        "the default buying platform for the open internet, with a founder-led culture and a product cycle "
        "(Kokai) that is still early in its monetization.",
        "This is not a bet on The Trade Desk returning to 30% growth. It is a bet that the market has priced "
        "something worse than decline — obsolescence — and the business, cash flow, and balance sheet do not "
        "support that verdict. Q2 2026 revenue grew 3% against higher expectations and Q3 guidance implies "
        "~−12% YoY — ugly, but the causes are named and cyclical: CPG and autos, jointly ~25% of the "
        "business, were crushed by tariffs, input costs, and oil; management admitted execution shortfalls; "
        "and a fee dispute with Publicis, since settled, poisoned sentiment. Nothing in that list is a "
        "structural ruling that the independent DSP model is dead. To justify $11.95 in our framework, "
        "revenue must decline slightly for a decade at compressed 19% FCF margins — the market is "
        "underwriting permanent margin-compressed decline, contradicted by 12 years of >95% retention, "
        "joint business plans up 38% YoY, and $13.4B of gross spend still routing through the platform.",
        "The asymmetry is the whole pitch. Our harsh bear case — revenue declining slightly for a decade "
        "at 19% FCF margins, walled gardens enclosing CTV buying — lands at $10.34, only 13% below the "
        "quote, and $1.49B of net cash ($3.16/share, no funded debt) floors the downside at 26% of the "
        "market cap. The base case (4.2% revenue CAGR, 25% FCF margins — below historical 30%+ adjusted "
        "EBITDA margins) supports $20.12. That is ~$9 of weighted upside against ~$1.60 of harsh-bear "
        "downside. When the bear case needs a decade of decline to land 13% under the quote, the "
        "risk/reward is decisively asymmetric.",
        "Our judgment on the forward trajectory centers on CTV and retail media, the two highest-growth "
        "pools in programmatic. CTV advertising is migrating from direct sold deals to programmatic buying "
        "as measurement standardizes — $44B globally in 2025, heading toward $81B by 2030 — and The Trade "
        "Desk's integrations with the major streaming platforms position it to capture a disproportionate "
        "share. Kokai Zuma, the agentic AI platform launched in August 2026 with claimed 32% CPA "
        "improvements, and UID2 identity adopted across NBCUniversal, Disney, Roku, and Spotify are real "
        "forward assets the market is pricing at zero. We haircut management's Kokai commentary but "
        "underwrite steady adoption because the product demonstrably improves return on ad spend.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("The 2026 derating was earned, not arbitrary — and it overshot. ",
         "Growth deceleration fears and walled-garden noise cut the stock ~68% in a year. But the "
         "deceleration is cyclical and mix-related: tariffs crushed the two core verticals, and the "
         "Publicis dispute is settled. Cyclical verticals and one bad year are being priced as terminal "
         "decay."),
        ("Walled gardens' advance helps more than it hurts. ",
         "As Google, Meta, and Amazon capture larger shares of digital budgets, advertisers' need for an "
         "objective measurement and buying layer across the remaining open internet intensifies — nobody "
         "wants the referee to also own a team."),
        ("Buybacks at $12 are unmodeled upside. ",
         "Shares are modeled flat; $269M of authorization remained at mid-2026, and every dollar retired "
         "at these prices is ~75% accretion to the $21 target. The cash build makes further "
         "authorizations likely."),
    ],
    "business": [
        "The Trade Desk, founded in 2009 by CEO Jeff Green and listed on Nasdaq in 2016, operates a "
        "self-service, cloud-based demand-side platform that lets advertisers and agencies buy digital ad "
        "inventory programmatically across display, video, audio, and CTV. Revenue is a percentage of "
        "advertising spend flowing through the platform (take rate ~21.6% in 2025 on ~$13.4B of gross "
        "spend), plus data and platform fees, recognized net of media costs. The company does not own "
        "media — this is the point: unlike Google's DV360 or Amazon's DSP, The Trade Desk has no incentive "
        "to steer spending toward owned inventory, which is why the world's largest advertisers and agency "
        "holding companies trust it with objective buying decisions. Two agency holding companies route 30% "
        "of gross spend through the platform.",
        "The product engine is Kokai, the AI-driven platform generation embedding predictive models across "
        "media planning, audience targeting, and measurement — with Kokai Zuma (agentic AI, August 2026) "
        "claiming 26–32% CPA improvements and migration of the full client base substantially complete. The "
        "identity layer, UID2 — an open-source, privacy-conscious identifier built for the post-cookie "
        "internet, with The Trade Desk as sole protocol administrator — has gained broad industry adoption "
        "and deepens the data advantage as third-party cookies fade. Joint business plans, the "
        "deep-integration revenue tier, are up 38% YoY and growing 6x faster than the rest of the business, "
        "roughly half of revenue by CEO disclosure.",
        "Competition comes from walled-garden DSPs (Google DV360, Amazon), which bundle buying with owned "
        "inventory, and from smaller independent DSPs. The threat that matters is Amazon — marketplace plus "
        "behavioral data fused with a DSP and owned inventory, with agencies actively testing it and fee "
        "pressure on the take rate. Google's DV360 was not restricted by the September 2026 ad-tech "
        "antitrust remedies — a modest positive for the open internet, no structural help against DV360 "
        "itself.",
    ],
    "business_bullets": [
        ("Kokai / Kokai Zuma. ",
         "Agentic AI platform — Koa Assistant, forecasting, measurement, automated workflows; the product "
         "cycle that is still early in monetization."),
        ("UID2 / EUID identity. ",
         "Open-source hashed-email identity adopted by NBCUniversal, Paramount, Disney/Hulu, Roku (83.6M "
         "households), Spotify — the data moat for the post-cookie internet."),
        ("OpenPath + Ventura. ",
         "Direct buyer-to-publisher routing and the February 2026 smart-TV OS collaboration — optionality, "
         "not current revenue."),
        ("Retention as the moat's proof. ",
         ">95% client retention for 12 straight years; JBPs growing 6x faster than the rest of the "
         "business. Agencies vote with spend, and they keep voting for independence."),
    ],
    "outlook": [
        "Our forward view is that programmatic's share of total advertising keeps rising and The Trade "
        "Desk's share of programmatic keeps rising with it — a double compounding that the current price "
        "does not reflect. We model revenue growth reaccelerating as the cyclical ad-spend softness passes "
        "and as CTV programmatic penetration deepens: every major streamer expanding its ad tier adds "
        "premium supply that flows disproportionately through the independent platform advertisers trust "
        "for video. Kokai's AI capabilities should drive both higher win rates and higher take rates over "
        "time, as better targeting and measurement justify premium pricing.",
        "On the competitive front, our judgment is that the walled gardens' advance helps The Trade Desk "
        "more than it hurts — while acknowledging Amazon's DSP as a real competitor in "
        "retail-media-adjacent buying, where its structural conflict (steering spend to Amazon inventory) "
        "is exactly what drives sophisticated advertisers toward the independent alternative. UID2 adoption "
        "is the leading indicator we watch: broadening industry support for the open identifier entrenches "
        "The Trade Desk's data position regardless of cookie timelines. International revenue up ~30% "
        "year-to-date (China doubling) is the current growth engine alongside JBPs.",
        "We model the exceptional margin structure persisting: the platform's incremental economics are "
        "software-like, and management has demonstrated disciplined investment — growing headcount in "
        "product and go-to-market while holding adjusted EBITDA margins near 40%. Free cash flow funds "
        "buybacks that offset stock compensation, and the balance sheet carries net cash. Our bear case, "
        "which sits below $11.95 at $10.34, assumes walled gardens successfully enclose CTV buying, "
        "programmatic growth stalls, and take-rate compression arrives — a genuinely adverse outcome we "
        "assign 25% weight precisely because platform shifts in advertising have historically been "
        "unforgiving to losers.",
    ],
    "financials": [
        "The Trade Desk has grown revenue at 20%+ rates for most of its public life — $1,578M (2022) to "
        "$2,896M (2025) — while maintaining adjusted EBITDA margins in the 40% range and generating "
        "substantial free cash flow: a rare combination of growth and profitability in ad tech, funded "
        "organically without serial dilution. Gross margins run ~80%; GAAP operating margin expanded from "
        "7.2% (2022) to 20.4% (2025). H1 2026 shows the cyclical trough: revenue +6.9% YoY, adjusted "
        "EBITDA margin ~32% — the deceleration the market is pricing as permanent.",
        "Balance sheet (June 30, 2026): cash $1,123M plus short-term investments $362M = $1,485M liquid; "
        "no funded debt. Buybacks of $241M in H1 2026 ($269M authorization remaining) retired shares at "
        "depressed prices; diluted shares fell from 495.8M to 469.9M year over year. The cash floor is not "
        "a mood — it is $3.16 per share, liquid, and growing.",
    ],
    "fin_table": {
        "headers": ["$ mn", "2022", "2023", "2024", "2025", "H1'26"],
        "rows": [
            ["Revenue", "1,578", "1,946", "2,445", "2,896", "1,404"],
            ["Revenue growth", "+31.9%", "+23.3%", "+25.6%", "+18.5%", "+6.9%*"],
            ["Gross margin", "82.2%", "81.2%", "80.7%", "78.6%", "—"],
            ["Adj. EBITDA margin", "—", "—", "41%", "41%", "~32%**"],
            ["GAAP operating margin", "7.2%", "10.3%", "17.5%", "20.4%", "—"],
        ],
        "footnote": "*H1'26 vs H1'25. **Adj. EBITDA $447.4M on $1,403.9M revenue. Sources: company releases (2026).",
    },
    "moat": [
        ("Independence as the product. ",
         "No owned media means no incentive to steer spend — the structural reason the world's largest "
         "advertisers trust The Trade Desk with objective buying across the open internet."),
        ("Agency workflow integration. ",
         "A decade of embedded workflows, 217 joint business plans growing 6x faster than the rest of "
         "the business, and >95% retention for 12 years — switching costs measured in spend, not contracts."),
        ("Identity and data position. ",
         "UID2 adoption across tier-one CTV publishers plus the data marketplace make The Trade Desk the "
         "natural pipe connecting retail-media data to open-internet inventory."),
        ("Profitability as a weapon. ",
         "~40% adjusted EBITDA margins and $1.49B of net cash fund buybacks at trough prices and product "
         "investment through the cycle — while unprofitable independent rivals cannot."),
    ],
    "valuation_method": "10-year scenario FCF DCF",
    "valuation_intro": [
        "We value The Trade Desk on an explicit 3-scenario 10-year DCF: 25/50/25 probability weights, "
        "scenario-specific discounts (base 12%, bear +250bp to 14.5%, bull −150bp to 10.5%), terminal growth "
        "of 1.5% / 2.5% / 2.5% on normalized mid-cycle margins. The bear is required to hurt and to sit "
        "below the price — and it does, at $10.34. The target is the weighted DCF, with no analyst "
        "overrule: 0.25×$10.34 + 0.50×$20.12 + 0.25×$34.31 = $21.22, set as the $21 target.",
        "The base case (4.2% revenue CAGR, 25% FCF margins) assumes continued compounding of the "
        "independent leader in a growing market — below historical 30%+ adjusted EBITDA margins, a "
        "deliberate haircut. The bull case (8.2% revenue CAGR, 28% FCF margins) assumes The Trade Desk "
        "becomes the de facto operating system for open-internet advertising, with Kokai driving take-rate "
        "expansion and retail-media data flows accelerating growth above historical rates. Shares are "
        "modeled flat — continued buybacks at ~$12 are unmodeled upside.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 10.34,
            "assumptions": "Walled gardens enclose CTV buying; revenue declines slightly for a decade; take rates compress",
            "rev_cagr": "−0.3%", "margin_end": "19%",
            "discount": 0.145, "terminal_g": 0.015, "tv_share": 0.45,
            "pv_explicit": 5.69, "pv_terminal": 4.65, "cashflow_unit": "$/sh",
        },
        "base": {
            "fair_value": 20.12,
            "assumptions": "Continued compounding of the independent leader; CTV migration; UID2 entrenches data advantage",
            "rev_cagr": "+4.2%", "margin_end": "25%",
            "discount": 0.12, "terminal_g": 0.025, "tv_share": 0.55,
            "pv_explicit": 9.05, "pv_terminal": 11.07, "cashflow_unit": "$/sh",
        },
        "bull": {
            "fair_value": 34.31,
            "assumptions": "De facto OS for open-internet advertising; Kokai drives take-rate expansion; retail-media data accelerates growth",
            "rev_cagr": "+8.2%", "margin_end": "28%",
            "discount": 0.105, "terminal_g": 0.025, "tv_share": 0.62,
            "pv_explicit": 13.04, "pv_terminal": 21.27, "cashflow_unit": "$/sh",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "0.25×$10.34 + 0.50×$20.12 + 0.25×$34.31 = $21.22, set as the $21 target. Terminal-year margins are FCF margins.",
    "risks": [
        ("Walled-garden take-rate pressure. ",
         "Amazon DSP fuses marketplace/behavioral data with owned inventory; agencies are testing it and "
         "winning fee concessions. The 21.6% take rate is stable but not guaranteed."),
        ("Agency concentration. ",
         "Two holding companies represent 30% of 2025 gross platform spend. The settled Publicis fee "
         "dispute showed how fast one relationship can dent sentiment."),
        ("CPG/auto cyclicality (~25% of business). ",
         "Tariffs, input costs, and oil crushed the two core verticals in 2026. If these do not normalize, "
         "the 'cyclical' thesis fails and the bear's revenue decline is realized."),
        ("Kokai Zuma adoption and AI execution. ",
         "The bull case needs agentic AI to re-accelerate share; at least one buyer says TTD may still be "
         "catching up on AI features versus Google/Meta automation."),
        ("Identity fragmentation. ",
         "Open-internet targeting depends on the identity fabric; UID2 vs RampID vs Privacy Sandbox is "
         "unresolved, and adoption has not yet translated to measurable publisher revenue difference."),
        ("Key-person risk. ",
         "Founder-CEO Jeff Green is central to strategy, culture, and industry relationships."),
        ("Valuation sensitivity. ",
         "Growth-multiple compression on any deceleration scare can drive sharp drawdowns — the stock "
         "fell 25% after Q2 alone."),
    ],
    "falsification": (
        "This call is wrong if: the take rate breaks durably below ~19% while gross spend also declines — "
        "i.e., the walled gardens are taking spend, not just pressuring fees; two more quarters of "
        "double-digit YoY revenue decline with JBP growth decelerating below 15% — the 'cyclical' thesis "
        "fails and the decline is structural; net cash is deployed into defensive M&A at high multiples "
        "or a special dividend instead of buybacks at depressed prices — the cash floor is the core of the "
        "asymmetry; or UID2 is abandoned by a tier-one CTV publisher in favor of RampID or first-party stacks."
    ),
    "charts": {
        "scenario": {"bear": 10.34, "base": 20.12, "bull": 34.31,
                     "weighted": 21.22, "price": 11.95},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [1.578, 1.946, 2.445, 2.896],
            "fcf_hist": [0.457, 0.543, 0.632, 0.783],
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035],
            "revenue_proj": [3.018, 3.144, 3.276, 3.414, 3.557, 3.707, 3.862, 4.025, 4.194, 4.370],
            "fcf_proj": [0.754, 0.786, 0.819, 0.853, 0.889, 0.927, 0.966, 1.006, 1.048, 1.093],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via Yahoo Finance. Projections: illustrative base-case paths at "
                    "the scenario's 4.2% revenue CAGR with FCF at the 25% scenario margin.",
        },
        "composition": {
            "bear": {"pv_explicit": 5.69, "pv_terminal": 4.65},
            "base": {"pv_explicit": 9.05, "pv_terminal": 11.07},
            "bull": {"pv_explicit": 13.04, "pv_terminal": 21.27},
            "unit": "$/sh",
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "TTD-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
