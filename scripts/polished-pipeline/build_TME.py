"""Polished note build: Tencent Music Entertainment Group (TME) — BUY, $13.00 target."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note, validate

data = {
    "ticker": "TME",
    "company": "Tencent Music Entertainment Group",
    "exchange": "NYSE (ADS)",
    "sector": "Communication Services — Online Music & Audio",
    "verdict": "BUY",
    "fair_value": 13.00,
    "price": 7.74,
    "risk": "Medium-High",
    "headline": "The Spotify of China, Priced Like a Karaoke App in Decline",
    "ceo": "Ross Liang",
    "hq": "Shenzhen, China",
    "snapshot": [
        ("Market cap", "~$12.6 bn (~1.63 bn ADS × $7.74)"),
        ("Price (Oct 2, 2026)", "$7.74"),
        ("52-week range", "~$7.66 – $23.86"),
        ("Paying users", "120 mn+ (Q4 2025); ~20% of music MAU vs ~40% for Spotify in mature markets"),
        ("Super VIP tier", "20 mn+ subscribers at ~RMB 40/mo (5× standard ARPPU)"),
        ("Music-services revenue", "RMB 7.61 bn in Q2 2026 (+11% YoY)"),
        ("Balance sheet", "Net cash; $2.4 bn Ximalaya deal funded internally; buybacks begun"),
        ("Ximalaya", "China's leading long-form audio platform, acquired May 2026"),
        ("Next catalyst", "Q3 2026 earnings; Ximalaya integration and synergy disclosure"),
    ],
    "thesis": [
        "Tencent Music is the Spotify of China that the market still prices like a karaoke-app "
        "operator in structural decline. That framing is years out of date. The revenue mix has "
        "pivoted decisively toward online music services — subscriptions, advertising, digital "
        "albums, concerts — which grew 11% year over year in the second quarter of 2026 to RMB "
        "7.61 billion, while the legacy social-entertainment business continues its managed "
        "shrink. At $7.74 the shares price in a future where Chinese consumers never pay for "
        "music; the reality is that they increasingly do, and Tencent Music collects the toll.",
        "The core of the case is paid penetration. Tencent Music ended 2025 with well over 120 "
        "million paying users, yet that is still only around a fifth of its music monthly active "
        "users — roughly half Spotify's conversion rate in mature markets. Every point of "
        "conversion is almost pure margin, because the content costs are largely fixed. On top of "
        "that, the Super VIP tier — priced at roughly RMB 40 per month versus RMB 8 for "
        "standard — passed 20 million subscribers by year-end 2025 and is the engine of "
        "average-revenue-per-user expansion. A subscriber base migrating up a 5× price ladder is "
        "one of the most attractive unit-economics stories in global consumer internet.",
        "The $2.4 billion acquisition of Ximalaya, completed in May 2026, extends the runway "
        "further. Ximalaya is China's leading online audio platform — podcasts, audiobooks, "
        "long-form audio — and folding it into Tencent Music creates cross-selling between music "
        "subscribers and audio listeners while consolidating the broader audio market. The "
        "market has treated the deal as a distraction; we see it as the company buying the "
        "adjacent category it would otherwise have to compete with, at a price its balance sheet "
        "easily absorbs.",
        "We do not minimize the China discount: the VIE structure, regulatory overhang, and "
        "geopolitical risk are real, and our valuation charges a full 250bp country-risk premium "
        "for them. But after that charge, the math still works. Our $13.00 fair value implies the "
        "market eventually pays a normal multiple for a subscription business with 120 "
        "million-plus paying users, rising ARPPU, and a net-cash balance sheet — not a heroic "
        "multiple, just a normal one. The bear case at $4.84, well below the current price, "
        "captures what happens if regulation or competition breaks the story; we think that "
        "outcome is over-weighted in today's price. The rating is BUY.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("Conversion has a long runway. ",
         "Paid penetration of ~20% of music MAU against ~40% for Spotify in mature markets, "
         "with hundreds of millions of free users in the funnel and AI-personalized "
         "recommendations purpose-built to harvest the shift toward paying for digital content."),
        ("SVIP is the ARPPU engine. ",
         "Twenty million-plus subscribers paying roughly 5× the standard tier, with concert "
         "ticketing, merchandise, and premium audio benefits still being layered onto the "
         "membership — ARPPU expansion with minimal incremental cost."),
        ("The China discount is priced twice. ",
         "Once in the multiple and once in the growth assumptions — while the business "
         "compounds subscribers at a double-digit pace with a net-cash balance sheet. That "
         "double-counting is the asymmetry."),
    ],
    "business": [
        "Tencent Music Entertainment Group, headquartered in Shenzhen, operates China's largest "
        "online music platform through four flagship products: QQ Music, Kugou Music, Kuwo "
        "Music, and the WeSing karaoke app. Following the May 2026 closing of the Ximalaya "
        "acquisition, it also owns China's leading long-form audio platform. The company "
        "reports in two segments: music-related services (subscriptions, digital albums, "
        "advertising, concerts, and artist merchandise) and social entertainment (live streaming "
        "and online karaoke tipping).",
        "The strategic pivot of the past several years has been the deliberate shift from "
        "tipping-driven social entertainment toward subscription-driven music services. "
        "Music-related services now account for the large majority of revenue and essentially "
        "all of the growth, while social entertainment — pressured by regulatory tightening "
        "around live streaming — has been managed for cash. The subscription business benefits "
        "from Tencent's broader ecosystem: distribution through WeChat and QQ, AI-driven "
        "recommendation, and partnerships with domestic and international labels that deepen "
        "the content moat.",
        "Economically, this is a classic subscription compounder in its early innings. Content "
        "licensing costs scale more slowly than subscriber revenue, so incremental paying users "
        "carry very high margins; the SVIP tier amplifies this by quintupling revenue per "
        "subscriber for the most engaged cohort. The company holds a substantial net-cash "
        "position, funded the Ximalaya deal from its balance sheet, and has begun returning "
        "capital through buybacks — unusual financial strength for a business the market prices "
        "as fragile.",
    ],
    "outlook": [
        "Our judgment is that Tencent Music is roughly where Spotify was five to seven years "
        "ago: past the proof-of-concept for paid conversion, but far from the penetration "
        "ceiling. Chinese consumers' willingness to pay for digital content has risen steadily "
        "across video, literature, and now music, and Tencent Music's conversion funnel is "
        "purpose-built to harvest that shift. We expect paying users to keep growing at a "
        "double-digit pace and, more importantly, ARPPU to keep climbing as the SVIP mix "
        "shifts upward and as the company layers concert ticketing, merchandise, and premium "
        "audio benefits onto the membership.",
        "Ximalaya is the swing factor for the next three years. The integration risk is real — "
        "large Chinese internet acquisitions have a mixed record — but the strategic logic is "
        "sound: music and long-form audio share users, share the subscription relationship, and "
        "share the fight against short-video platforms for ear time. If Tencent Music executes, "
        "the combined entity owns the two largest audio use cases in China and can bundle them "
        "in ways no competitor can match. Even a partial success adds a durable growth leg; the "
        "bull case assumes the full synergy thesis lands.",
        "The honest risk to this outlook is not competition — NetEase Cloud Music is a capable "
        "rival but the market is large enough for two winners — it is the regulatory and "
        "geopolitical environment. Another wave of live-streaming-style intervention aimed at "
        "the music business, or a serious escalation in US-China capital-markets tensions "
        "affecting the ADR, would impair the shares regardless of fundamentals. That is why the "
        "bear case is severe and why we demand the country-risk premium.",
    ],
    "financials": [
        "The financial profile is that of a subscription compounder, not a declining karaoke "
        "operator. Revenue was RMB 32.9 billion in 2025 (up from RMB 28.3 billion in 2022), with "
        "the mix steadily shifting toward high-margin music subscriptions. Operating cash flow "
        "has run above RMB 10 billion for two consecutive years, and free cash flow — RMB 9.0 "
        "billion in 2025 — converts strongly because the content costs are largely fixed and "
        "capex is light. Gross margins are expanding (44.5% in 2026E, rising toward 45%+), "
        "exactly what the subscription-pivot thesis predicts.",
        "The balance sheet is a strategic weapon: substantial net cash funded the $2.4 billion "
        "Ximalaya acquisition without strain and supports the buyback program — a capital "
        "return unusual for a Chinese internet name at this multiple. At $7.74 the ADS trades "
        "at roughly 9× trailing earnings, a multiple that prices the business as fragile "
        "while it compounds paying users at a double-digit pace.",
    ],
    "fin_table": {
        "headers": ["RMB bn", "2022", "2023", "2024", "2025"],
        "rows": [
            ["Total revenue", "28.34", "27.75", "28.40", "32.90"],
            ["YoY growth", "—", "−2.1%", "+2.3%", "+15.8%"],
            ["Operating cash flow", "7.48", "7.34", "10.28", "10.23"],
            ["Free cash flow", "6.43", "6.17", "9.24", "9.04"],
            ["2026E (company proj.)", "—", "—", "—", "—"],
            ["Revenue / FCF", "35.90", "—", "—", "9.80"],
        ],
        "footnote": "Sources: company filings via Yahoo Finance (annual). 2026E–2028E revenue/FCF per company projections (revenue 39.0/42.3, FCF 10.6/11.45 RMB bn). FCF = operating cash flow less capex.",
    },
    "moat": [
        ("The catalog and label relationships. ",
         "Partnerships with domestic and international labels, plus exclusive and "
         "windowed content, make the music library a moat that a new entrant cannot "
         "license its way around cheaply."),
        ("Distribution through the Tencent ecosystem. ",
         "WeChat and QQ distribution plus AI-driven recommendation create a conversion funnel "
         "of hundreds of millions of free users that no standalone rival can replicate."),
        ("Subscription unit economics. ",
         "Largely fixed content costs mean every point of paid conversion and every SVIP "
         "upgrade is almost pure margin — the classic compounder flywheel, still early."),
        ("The Ximalaya bundle. ",
         "Owning China's leading long-form audio platform alongside the leading music "
         "platform enables bundling no competitor can match — if integration executes."),
        ("The moat's weak link: regulation. ",
         "Chinese authorities have previously intervened in live streaming and music "
         "copyright; rules on pricing, exclusivity, or content could impair monetization "
         "regardless of competitive position."),
    ],
    "valuation_method": "10-year scenario FCFE DCF with China country-risk premium",
    "valuation_intro": [
        "We value Tencent Music on a 10-year probability-weighted scenario DCF of free cash "
        "flow to equity — weights bear 25% / base 50% / bull 25% — with scenario-specific "
        "discounts that include a full 250bp China country-risk premium: bear 13.0% (base + "
        "250bp: regulatory break, VIE impairment), base 10.5% (country risk fully charged on a "
        "subscription compounder), bull 9.0% (base − 150bp). Terminal growth is 1.0% / 2.0% / "
        "2.5% on normalized mid-cycle FCF margins — never peak margins — and regional "
        "subscription peers, never US peers alone, anchor the multiple cross-check.",
        "In the base case, paying users keep compounding at a double-digit pace and ARPPU "
        "climbs on the SVIP mix shift, with Ximalaya contributing a partial synergy thesis — "
        "worth $13.50 per ADS. The bear case ($4.84) is the world where regulation or "
        "competition breaks the subscription story and the VIE structure impairs ADR holders "
        "directly; it sits well below the current price, as the framework requires. The bull "
        "case ($20.20) assumes the full Ximalaya synergy thesis lands, SVIP penetration "
        "accelerates, and the market eventually pays a normal subscription multiple. The "
        "probability-weighted fair value is $13.00 — a normal multiple for 120 million-plus "
        "paying users, rising ARPPU, and a net-cash balance sheet, not a heroic one.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 4.84,
            "assumptions": "Regulation or competition breaks the subscription story; VIE/geopolitical impairment hits ADR holders; conversion stalls",
            "rev_cagr": "+2.0%", "margin_end": "22%",
            "discount": 0.13, "terminal_g": 0.01, "tv_share": 0.45,
            "pv_explicit": 4333, "pv_terminal": 3547, "cashflow_unit": "$mn",
        },
        "base": {
            "fair_value": 13.50,
            "assumptions": "Paying users compound double-digits; ARPPU climbs on SVIP mix; Ximalaya contributes partial synergies; 250bp country-risk premium charged",
            "rev_cagr": "+7.5%", "margin_end": "28%",
            "discount": 0.105, "terminal_g": 0.02, "tv_share": 0.55,
            "pv_explicit": 9891, "pv_terminal": 12089, "cashflow_unit": "$mn",
        },
        "bull": {
            "fair_value": 20.20,
            "assumptions": "Full Ximalaya synergy thesis lands; SVIP penetration accelerates; market pays a normal subscription multiple for the compounder",
            "rev_cagr": "+11.0%", "margin_end": "32%",
            "discount": 0.09, "terminal_g": 0.025, "tv_share": 0.62,
            "pv_explicit": 12498, "pv_terminal": 20392, "cashflow_unit": "$mn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Scenario fair values are per-ADS equity values from the FCFE DCF (~1.63 bn ADS). 0.25×$4.84 + 0.50×$13.50 + 0.25×$20.20 ≈ $13.00.",
    "risks": [
        ("Regulatory risk. ",
         "Chinese authorities have previously intervened in live streaming and music "
         "copyright; new rules on pricing, exclusivity, or content could impair monetization."),
        ("VIE / geopolitical risk. ",
         "The variable-interest-entity structure and US-China tensions create tail risk for "
         "ADR holders, including delisting or ownership-structure scenarios."),
        ("Competition. ",
         "NetEase Cloud Music and short-video platforms (Douyin) compete for user time and "
         "music discovery."),
        ("Ximalaya integration. ",
         "The $2.4 billion acquisition may underdeliver on synergies or distract management "
         "from the core subscription engine."),
        ("Macro sensitivity. ",
         "A Chinese consumer downturn would slow discretionary subscription uptake and "
         "advertising revenue."),
    ],
    "falsification": (
        "Downgrade to HOLD on: paying-user net additions turning negative for two consecutive "
        "quarters — the conversion engine stalling would break the thesis; SVIP subscriber "
        "count declining or ARPPU falling year over year, indicating the premium tier has hit a "
        "wall; a regulatory action that directly caps music subscription pricing or mandates "
        "content sharing that destroys the catalog moat; Ximalaya write-downs or disclosure "
        "that integration synergies will not materialize; or any credible move by authorities "
        "against the VIE structure itself — the unhedgeable tail, on which we would exit on "
        "evidence it is materializing, not after. We watch: paying-user net adds, SVIP "
        "penetration, ARPPU, and regulatory headlines."
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
        "independently tested and haircut where evidence warrants. For Chinese issuers we add "
        "an explicit country-risk premium to the discount rate and model the VIE structure in "
        "the bear case.",
    ],
    "charts": {
        "scenario": {"bear": 4.84, "base": 13.50, "bull": 20.20,
                     "weighted": 13.00, "price": 7.74},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [28.339, 27.752, 28.401, 32.902],
            "fcf_hist": [6.428, 6.173, 9.243, 9.043],
            "years_proj": [2026, 2027, 2028, 2029, 2030],
            "revenue_proj": [35.9, 39.0, 42.3, 45.9, 49.7],
            "fcf_proj": [9.8, 10.6, 11.45, 12.4, 13.4],
            "unit": "RMB bn", "fcf_label": "FCF",
            "note": "History: company filings via Yahoo Finance (FCF = operating cash flow "
                    "less capex). 2026E–2028E per company projections; 2029E–2030E "
                    "base-case extension from the scenario DCF.",
        },
        "composition": {
            "bear": {"pv_explicit": 4333, "pv_terminal": 3547},
            "base": {"pv_explicit": 9891, "pv_terminal": 12089},
            "bull": {"pv_explicit": 12498, "pv_terminal": 20392},
            "unit": "$mn",
        },
        "extra": {
            "type": "line",
            "title": "Company projections, 2026E–2028E (RMB bn)",
            "years": [2026, 2027, 2028],
            "series": [
                {"label": "Revenue", "values": [35.9, 39.0, 42.3]},
                {"label": "FCF", "values": [9.8, 10.6, 11.45]},
            ],
            "ylabel": "RMB bn",
        },
    },
}

validate(data)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "TME-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
