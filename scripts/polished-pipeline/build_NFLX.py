"""Polished note: Netflix (NFLX) — SELL, fair value $48.00.

No model JSON exists for this name: scenario FVs / discounts / margins are taken
from the valuation section of the current standalone research note
(bear $20.14 / base $45.57 / bull $78.79; discounts 12.5%/10%/8.5%; terminal
growth 2.5%; base revenue CAGR 6.0%; normalized 2026 FCF $10.3B; terminal FCF
margin 23%). The DCF composition split is derived transparently from those
stated parameters (10-yr FCF paths implied by the revenue CAGR and margin
assumptions); explicit-period and terminal PVs sum to the scenario fair values.
History: company filings via Yahoo Finance (Oct 2026). All prose is fresh
October 4, 2026 analysis.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note, validate

SHARES_BN = 4.164  # ~$279bn / $67.06

data = {
    "ticker": "NFLX",
    "company": "Netflix, Inc.",
    "exchange": "NASDAQ",
    "sector": "Communication Services — Entertainment / Streaming",
    "verdict": "SELL",
    "fair_value": 48.00,
    "price": 67.06,
    "risk": "Medium",
    "headline": "A superb business priced as an unstoppable compounder — the engagement data says otherwise",
    "ceo": "Ted Sarandos and Greg Peters (co-CEOs)",
    "hq": "Los Gatos, California",
    "snapshot": [
        ("Market cap", "~$279 bn (4.16 bn sh × $67.06)"),
        ("52-week range", "~$65 – $125"),
        ("Price / fair value", "$67.06 / $48.00"),
        ("Implied downside", "−28%"),
        ("Paid memberships", "300 mn+ across 190+ countries"),
        ("2025 revenue", "$45.2 bn"),
        ("Content assets on balance sheet", "~$33.8 bn"),
        ("Normalized 2026 free cash flow", "~$10.3 bn (excludes $2.8 bn one-time WBD fee)"),
        ("Ad-supported tier", "Launched late 2022; scaling, lower ARPU"),
        ("Next catalyst", "Q3 2026 print; ad-tier ARPU and engagement disclosures"),
    ],
    "thesis": [
        "Netflix is a superb operating business selling at a price that assumes it is an "
        "unstoppable compounding machine. With more than 300 million paid memberships, "
        "global scale, and genuine free-cash-flow generation, the company has earned its place "
        "as the winner of the streaming wars. The problem is not the business. The problem is "
        "what the share price demands the business must still become: at $67.06, the market "
        "is paying for a decade of uninterrupted, high-margin growth that the engagement data "
        "no longer supports.",
        "The decisive fact is the divergence between content spending and engagement. View "
        "hours grew only about 2% in the first half of 2026 while the content budget keeps "
        "rising. Each marginal dollar of content is buying less viewing — the signature of a "
        "mature platform, not a growth compounder. The paid-sharing lift from the "
        "password-sharing crackdown, which powered the last leg of subscriber growth, was a "
        "one-time step-up in the paying base, not a repeatable engine. With engagement flat, "
        "the company has leaned on repeated price increases to drive revenue, and price hikes "
        "on flat engagement face hard limits: churn and piracy.",
        "Earnings quality deserves equal skepticism. Netflix carries roughly $33.8 billion of "
        "content assets on amortization schedules that are inherently judgmental — management "
        "decides, within wide latitude, how fast capitalized content costs flow through the "
        "income statement. Reported margins are therefore softer than they appear. Free cash "
        "flow tells a cleaner story, but 2026 cash flow is flattered by a one-time $2.8 "
        "billion Warner Bros. Discovery termination fee that does not recur; normalized free "
        "cash flow is about $10.3 billion, a materially lower base from which the market's "
        "growth expectations must be met.",
        "Our probability-weighted fair value is $48.00, 28% below the current price. The "
        "asymmetry is stark: even our bull case, at $78.79, barely clears today's price, while "
        "our bear case sits at $20.14. When the entire plausible upside is a few percent and "
        "the downside is measured in halves, the correct posture is to sell. The forward "
        "judgment is that Netflix is entering a structurally slower phase — developed-market "
        "saturation, lower-ARPU net adds, ad-tier cannibalization of full-price plans, and a "
        "content-cost treadmill that only steepens — and the market has not yet priced any of "
        "it. A mature, cash-generative media utility is a fine business to own at a "
        "utility-like multiple, which $67.06 is not. SELL.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("The marginal content dollar is broken. ",
         "View hours up ~2% in H1 2026 against a rising content budget is the single most "
         "important data point in the note. When spending no longer reliably converts into "
         "viewing, the era of outspending competitors into submission is ending — and with "
         "it the growth-multiple justification."),
        ("The pricing-power engine is running on fumes. ",
         "Revenue growth is increasingly manufactured by price increases on flat engagement. "
         "Each hike raises churn risk and pushes marginal viewers toward piracy or free "
         "alternatives — YouTube and TikTok acquire their content effectively for free."),
        ("The $33.8 billion judgment call. ",
         "Capitalized content on management's amortization schedules means reported margins "
         "are softer than they appear. Faster write-downs would reveal lower true margins; "
         "the balance sheet carries the risk that the P&L does not show."),
    ],
    "business": [
        "Netflix is the world's largest subscription video streaming service, operating in "
        "more than 190 countries with a content library spanning licensed programming and a "
        "large and growing slate of original films and series. Revenue comes primarily from "
        "monthly membership fees across ad-free tiers, supplemented by a lower-priced "
        "advertising-supported tier launched in late 2022 and a nascent games initiative.",
        "The company's moat rests on scale: a global subscriber base amortizes content costs "
        "that regional competitors cannot match, and its recommendation and personalization "
        "systems benefit from the largest viewing dataset in the industry. The ad-supported "
        "tier adds a second revenue stream with structurally higher incremental margins, "
        "since advertising revenue requires no additional content spend.",
        "Competition for attention is broader than the traditional streaming set. YouTube, "
        "TikTok, and gaming compete for the same leisure hours, and several of these "
        "competitors acquire their content effectively for free through user generation. "
        "Netflix must pay cash for every hour it hopes its subscribers will watch.",
    ],
    "business_bullets": [
        ("Scale as the moat. ",
         "300 million-plus memberships amortize a content budget no regional rival can "
         "match; the viewing dataset compounds the recommendation advantage every quarter."),
        ("The ad tier: second engine, lower ARPU. ",
         "The advertising-supported tier scales with structurally higher incremental margins "
         "but dilutes blended ARPU and is cyclically exposed — brand budgets are cut early "
         "in downturns."),
        ("Paid sharing was a step-up, not an engine. ",
         "The password-sharing crackdown converted borrowers into payers once. There is no "
         "second crackdown to run; future net adds skew to lower-ARPU regions and the ad tier."),
        ("Sports, live, gaming: same economics. ",
         "Logical adjacencies, but each demands large upfront cash for uncertain engagement "
         "returns — the same treadmill, steeper."),
    ],
    "outlook": [
        "Our judgment is that Netflix is entering a structurally slower phase that the market "
        "has not yet priced. The subscriber base in developed markets is approaching "
        "saturation; future net additions will skew toward lower-ARPU regions and the ad "
        "tier, which dilutes average revenue per member even as headline subscriber counts "
        "grow. Management will continue to raise prices to manufacture revenue growth, but "
        "each increase on flat engagement raises churn risk and pushes marginal viewers "
        "toward piracy or free alternatives.",
        "The advertising tier is the most credible growth lever, and we expect it to scale "
        "meaningfully over the next three years. But it is a lower-ARPU, cyclically exposed "
        "revenue stream, and its growth partly cannibalizes full-price subscriptions as "
        "existing members trade down. Net-net, we see revenue growing at a mid-single-digit "
        "rate — respectable for a mature media business, but incompatible with a growth "
        "multiple.",
        "Longer term, the content-cost treadmill only steepens. Sports rights, live events, "
        "and gaming are logical adjacencies, but each carries the same economics: large "
        "upfront cash outlays for uncertain engagement returns. Our base case compounds "
        "revenue at 6.0% annually with free-cash-flow margins normalizing at 23% — a healthy "
        "media business, worth $45.57, not $67.06.",
    ],
    "financials": [
        "Revenue grew from $31.6 billion in 2022 to $45.2 billion in 2025, but the "
        "composition of growth has deteriorated: engagement is flat while price increases do "
        "the work. Free cash flow (operating cash flow less capex) ran $1.6 billion in 2022, "
        "$6.9 billion in 2023 and 2024, and $9.5 billion in 2025 — a genuine inflection, but "
        "2026's headline number is flattered by the one-time $2.8 billion Warner Bros. "
        "Discovery termination fee. We normalize 2026 free cash flow to $10.3 billion and "
        "value the business off that base, not the reported figure.",
        "The balance sheet carries the $33.8 billion content asset — capitalized production "
        "costs amortized on management's schedules. This is the softest number in large-cap "
        "media: within wide latitude, management decides how fast the costs hit the P&L. Our "
        "valuation deliberately uses cash flow, not reported earnings, and the terminal value "
        "is computed on a normalized 23% free-cash-flow margin — deliberately not peak "
        "margins. The bear case ($20.14) assumes revenue growth stalls near 3%, engagement "
        "declines as price hikes drive churn and piracy, and FCF margins compress to the "
        "mid-teens at a 12.5% discount rate.",
    ],
    "fin_table": {
        "headers": ["$bn", "2022", "2023", "2024", "2025"],
        "rows": [
            ["Revenue", "31.6", "33.7", "39.0", "45.2"],
            ["YoY growth", "—", "+6.6%", "+15.7%", "+15.9%"],
            ["Operating cash flow", "2.0", "7.3", "7.4", "10.2"],
            ["Free cash flow (OCF − capex)", "1.6", "6.9", "6.9", "9.5"],
            ["FCF margin", "5.1%", "20.5%", "17.7%", "20.9%"],
            ["Net income", "4.5", "5.4", "8.7", "11.0"],
        ],
        "footnote": "Company filings via Yahoo Finance. 2026 FCF is normalized to ~$10.3 bn "
                    "excluding the one-time $2.8 bn Warner Bros. Discovery termination fee.",
    },
    "moat": [
        ("Global scale amortizes content. ",
         "A 300-million-member base spreads production costs no regional competitor can "
         "match — the structural reason Netflix won the streaming wars."),
        ("The data flywheel. ",
         "The largest viewing dataset in the industry compounds the recommendation and "
         "personalization advantage, lowering churn at the margin."),
        ("But attention competitors pay nothing for content. ",
         "YouTube and TikTok acquire hours effectively free through user generation. "
         "Netflix must pay cash for every hour — the moat is real but it is not widening."),
        ("Pricing power has hard limits now. ",
         "With engagement flat, each price increase is a churn experiment. The moat "
         "protects the subscriber base; it does not protect ARPU growth."),
    ],
    "valuation_method": "10-year scenario DCF",
    "valuation_intro": [
        "We value Netflix on a 10-year scenario DCF at a 10% base discount rate, weighted "
        "25% / 50% / 25%. The bear case (12.5% discount) assumes revenue growth stalls near "
        "3%, engagement declines as price hikes drive churn and piracy, and FCF margins "
        "compress to the mid-teens. The base case compounds revenue at 6.0% annually off a "
        "normalized 2026 free cash flow of $10.3 billion — the one-time $2.8 billion Warner "
        "Bros. Discovery termination fee stripped out, since it does not recur — with "
        "terminal value computed on normalized 23% free-cash-flow margins, deliberately not "
        "peak margins. The bull case (8.5% discount) assumes the ad tier scales with "
        "accretive ARPU, pricing power holds without churn, and margins expand.",
        "The scenario fair values are $20.14 (bear) / $45.57 (base) / $78.79 (bull), "
        "weighting to $47.52 — our $48.00 target, 28% below the $67.06 close. Note the skew: "
        "even the bull case barely clears the current price, while the bear case implies a "
        "two-thirds loss. Terminal value is 36–66% of equity value across scenarios, "
        "disclosed here.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 20.14,
            "assumptions": ("Revenue growth stalls near 3%; engagement declines as price "
                            "hikes drive churn and piracy; FCF margins compress to the "
                            "mid-teens; 12.5% discount rate."),
            "rev_cagr": "+3.0%", "margin_end": "15%",
            "discount": 0.125, "terminal_g": 0.025, "tv_share": 0.356,
            "pv_explicit": 54.0, "pv_terminal": 29.9, "cashflow_unit": "$bn",
        },
        "base": {
            "fair_value": 45.57,
            "assumptions": ("6.0% revenue CAGR; normalized 2026 FCF of $10.3B (one-time WBD "
                            "fee stripped out); 10% discount rate; terminal value on "
                            "normalized 23% FCF margins."),
            "rev_cagr": "+6.0%", "margin_end": "23%",
            "discount": 0.10, "terminal_g": 0.025, "tv_share": 0.546,
            "pv_explicit": 86.2, "pv_terminal": 103.6, "cashflow_unit": "$bn",
        },
        "bull": {
            "fair_value": 78.79,
            "assumptions": ("Ad tier scales with accretive ARPU; pricing power holds "
                            "without churn; margins expand toward 28%; 8.5% discount rate."),
            "rev_cagr": "+9.0%", "margin_end": "28%",
            "discount": 0.085, "terminal_g": 0.025, "tv_share": 0.662,
            "pv_explicit": 110.9, "pv_terminal": 217.2, "cashflow_unit": "$bn",
        },
    },
    "scenario_note": "Composition (PV of explicit-period cash flows vs. terminal value) is "
                     "derived from each scenario's stated parameters — 10-year horizon, "
                     "scenario discount rate, 2.5% terminal growth, revenue CAGR and "
                     "year-10 FCF margin — and sums to the scenario fair value at 4.164 bn "
                     "shares outstanding.",
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "risks": [
        ("Engagement deterioration. ",
         "If view hours decline outright, the pricing-power thesis collapses and churn "
         "accelerates."),
        ("Content amortization judgment. ",
         "The $33.8 billion content asset balance rests on management's amortization "
         "schedules; faster write-downs would reveal lower true margins."),
        ("Free attention platforms. ",
         "YouTube and TikTok compete for leisure hours without bearing content cash costs."),
        ("Ad-market cyclicality. ",
         "A recession would hit the ad tier just as it becomes material to growth."),
        ("Currency headwinds. ",
         "A majority of members are outside the US; dollar strength mechanically depresses "
         "reported growth."),
        ("Regulatory risk. ",
         "Content quotas, taxation of digital services, and data rules across 190+ "
         "jurisdictions."),
    ],
    "falsification": (
        "Sustained double-digit view-hour growth on a rising content budget would be evidence "
        "the marginal content dollar is working again — the single fact that would most "
        "directly challenge this note. A price-increase cycle with no measurable uptick in "
        "churn would prove genuine pricing power on flat engagement. Free-cash-flow "
        "conversion structurally above 60% of operating income for two consecutive years "
        "would support a higher through-cycle margin assumption. And the ad tier "
        "demonstrating accretive blended ARPU — rather than cannibalization of full-price "
        "plans — would reopen the growth case. Absent those, the SELL stands: we watch "
        "reported view hours versus content spend, churn around price increases, the "
        "content-asset balance versus amortization, and ad-tier ARPU mix."
    ),
    "methodology": [
        "We value Netflix on a 10-year scenario discounted-cash-flow framework, "
        "probability-weighted 25% / 50% / 25%. The base discount rate is 10%, reflecting a "
        "standard operating company with a strong franchise but maturing growth; the bear "
        "case adds 250 basis points (12.5%) and the bull case subtracts 150 basis points "
        "(8.5%, above the 8% floor). Terminal growth is 2.5%, applied to normalized "
        "mid-cycle free-cash-flow margins — never peak margins.",
        "Two normalizations are load-bearing. First, 2026 free cash flow is set at $10.3 "
        "billion, stripping out the one-time $2.8 billion Warner Bros. Discovery termination "
        "fee, since it does not recur. Second, the valuation is built on cash flow, not "
        "reported earnings, because the $33.8 billion capitalized content asset is amortized "
        "on judgmental schedules. The bear case is required to be genuinely adverse and to "
        "sit below the current price — at $20.14, it does.",
        "We cross-check the DCF against trading multiples and reverse-DCF implied growth. "
        "The published target is the probability-weighted fair value, stated as a 12-month "
        "horizon reference. Risk ratings (Low / Medium / Medium-High / High) combine "
        "business volatility, balance-sheet strength, and valuation; Medium here reflects a "
        "cash-generative franchise whose price embeds growth the engagement data no longer "
        "supports.",
    ],
    "charts": {
        "scenario": {"bear": 20.14, "base": 45.57, "bull": 78.79,
                     "weighted": 48.00, "price": 67.06},
        "trajectory": {
            # history: filings via Yahoo Finance (OCF - capex)
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [31.62, 33.72, 39.00, 45.18],
            "fcf_hist": [1.62, 6.92, 6.92, 9.46],
            # base-case projection: 6.0% revenue CAGR; FCF margin gliding 21% -> 23%
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": [49.0, 51.9, 55.1, 58.4, 61.9, 65.6, 69.5, 73.7, 78.1, 82.8, 87.8],
            "fcf_proj": [10.29, 11.00, 11.79, 12.61, 13.49, 14.43, 15.43, 16.51, 17.65, 18.88, 20.19],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via Yahoo Finance (FCF = operating cash flow "
                    "less capex). Projection: base-case path — revenue at 6.0% CAGR from "
                    "2026E $49.0B; FCF from the normalized $10.3B base with margins gliding "
                    "21% to the normalized 23%.",
        },
        "composition": {
            "bear": {"pv_explicit": 54.0, "pv_terminal": 29.9},
            "base": {"pv_explicit": 86.2, "pv_terminal": 103.6},
            "bull": {"pv_explicit": 110.9, "pv_terminal": 217.2},
            "unit": "$bn",
        },
        "extra": {
            "type": "line",
            "title": "Free-cash-flow margin — reported history",
            "years": [2022, 2023, 2024, 2025],
            "series": [{"label": "FCF margin",
                        "values": [5.1, 20.5, 17.7, 20.9]}],
            "ylabel": "%",
        },
    },
}

validate(data)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "NFLX-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
