"""Polished note build: FUBO (fuboTV Inc.). Re-runnable via template.build_note."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

data = {
    "ticker": "FUBO",
    "company": "fuboTV Inc.",
    "exchange": "NYSE",
    "sector": "Communication Services — Streaming / vMVPD",
    "verdict": "BUY",
    "fair_value": 33.00,
    "price": 8.66,
    "risk": "High",
    "headline": "The $164 Subscriber: Disney's Sports Bundle Priced for Liquidation",
    "ceo": "Alisa Bowen",
    "hq": "New York, New York",
    "snapshot": [
        ("Market cap", "~$0.95 bn (109.2 mn econ. sh × $8.66)"),
        ("Enterprise value", "~$1.03 bn"),
        ("Net debt", "~$86 mn (6/30/26)"),
        ("52-week range", "~$7.95 – $52.68 (split-adjusted)"),
        ("Subscribers", "~5.75 mn North America (FQ3'26)"),
        ("FY2026E revenue", "~$6.19 bn (pro forma, combined)"),
        ("FY2026E adj. EBITDA guide", "$90–100 mn (raised Aug 2026)"),
        ("2028 target", "≥$300 mn adj. EBITDA; positive FCF in 2027"),
        ("Disney stake", "~70% of economics; controlled company"),
        ("Next catalyst", "Disney Ad Server migration completion, YE 2026"),
    ],
    "thesis": [
        "The quote prices in failure; the business is inflecting. At $8.66 the market implies either "
        "a roughly −10% ten-year revenue decline (at our base-case margins) or a ~3.5–4% steady-state "
        "EBITDA margin — below the ~4–5% margin embedded in management's own public 2028 target of at "
        "least $300 million of adjusted EBITDA. Yet the combined company has printed three consecutive "
        "quarters of positive adjusted EBITDA, raised its 2026 guidance, and brought free cash flow to "
        "near breakeven. The bar the market sets is lower than the bar management already clears. That "
        "gap is the opportunity.",
        "The Disney combination was a genuine transformation of the unit economics, not a rescue "
        "narrative. Closed in October 2025, it married Fubo's sports-first product with Hulu + Live TV's "
        "subscriber base, creating a ~6-million-subscriber, sixth-ranked U.S. pay-TV operator overnight. "
        "Disney brings three tangible assets beyond scale: committed financing, the Disney Ad Server "
        "migration that is already lifting ad fill rates and CPMs, and content-packaging flexibility a "
        "sub-scale standalone could never negotiate. Scale is the only durable way to improve content "
        "cost per subscriber in virtual pay TV, and Fubo just bought it.",
        "Our forward judgment is that the investment case does not require Fubo to win the streaming "
        "wars — it requires the combined company to harvest the synergies the combination underwrote. "
        "Three engines carry the 2028 target: advertising optimization, where every incremental ad dollar "
        "in a ~7%-gross-margin business falls almost entirely to EBITDA; content-cost flexibility from "
        "negotiating as a top-six operator with Disney's ownership changing the bargaining dynamic; and "
        "distribution inside ESPN's purchase flow replacing paid subscriber acquisition. We haircut "
        "management's synergy and margin targets throughout — our base case assumes only an 8% "
        "steady-state EBITDA margin — and the probability-weighted DCF still lands at $32.55, rounded to "
        "our $33 target.",
        "We want to be plain about what this is: a speculative situation with a very wide range of "
        "outcomes, and the governance is the central risk. Public shareholders own economics but no "
        "control — Disney executed the 1-for-12 reverse split by written consent without a shareholder "
        "meeting — and 79 million shares of future overhang are registered. There is also a free takeout "
        "option embedded: Disney owns 70% of the economics, and taking out the stub at a strategic "
        "0.5–0.75x sales multiple equates to roughly $28–42 per share. This is a small position for "
        "investors who can tolerate a wide outcome distribution, not a core holding.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("$164 per subscriber is a liquidation quote. ",
         "The equity is valued at roughly $164 per subscriber and 0.15x revenue, versus ~$800–1,000 "
         "per subscriber implied when Disney struck the deal in January 2025 and $400–1,000 per sub in "
         "precedent pay-TV transactions. Even at trough multiples — 0.5x revenue, $400 per sub, 10x the "
         "2028E EBITDA target present-valued — fair value is $20–28 per share, roughly 2.5x to 3x the quote."),
        ("The EBITDA inflection is already printing. ",
         "Three straight quarters of positive adjusted EBITDA ($41.4M, $37.7M, $19.1M), guidance raised "
         "to $90–100M for 2026, and free cash flow improved from −$41M to −$7.5M year over year. The "
         "market is underwriting a trajectory the reported numbers are already beating."),
        ("Advertising is the highest-leverage engine. ",
         "Live sports inventory commands premium CPMs, and the Disney Ad Server migration — complete by "
         "year-end 2026 — is credited for the FQ3 EBITDA beat. In a 7%-gross-margin business, the ad "
         "business is the margin story."),
    ],
    "business": [
        "FuboTV, founded in 2015 as a soccer-streaming service and public since October 2020, is a "
        "sports-first virtual multichannel video programming distributor (vMVPD): a live-TV bundle "
        "delivered over the internet, sold in tiers from a $64.99 sports-and-news skinny package to the "
        "full $98.99 bundle, with cloud DVR and on-demand content. Revenue comes from subscriptions and "
        "from advertising, including dynamically inserted ads in live and on-demand streams, on the "
        "company's proprietary ad-insertion and billing stack. The flagship service carries major sports "
        "networks alongside news and entertainment; the company also owns the Fubo Sports linear network "
        "and operates in France.",
        "The defining corporate event is the October 2025 combination with Disney's Hulu + Live TV "
        "business, structured as an Up-C reorganization in which Hulu is the accounting acquirer — so "
        "as-reported history is Hulu + Live TV carve-out numbers, and year-over-year comparisons are only "
        "meaningful on the company's pro forma basis. Disney holds roughly 70% of the economics and a "
        "majority of the votes through 79.0 million Class B shares; the public float is 30.2 million "
        "Class A shares after the March 2026 1-for-12 reverse split. The settlement of the sports-streaming "
        "litigation that preceded the deal cleared the way for the skinny-bundle products both sides had "
        "been blocked from offering.",
        "Whether the combination delivers depends almost entirely on execution — integration of two "
        "technology stacks, realization of cost synergies, and disciplined pricing — rather than on the "
        "strategic logic, which is sound: two sub-scale virtual pay-TV operators, each too small to "
        "negotiate programming costs from strength, become one operator large enough to matter to "
        "programmers.",
    ],
    "business_bullets": [
        ("Sixth-largest U.S. pay-TV operator. ",
         "~5.75 million North American subscribers at FQ3'26, behind only YouTube TV at 10M+. "
         "Sports depth — regional sports networks, 55,000+ events per year — plus the best DVR "
         "(1,000 hours) and stream count (10) in the category."),
        ("The Disney toolkit. ",
         "A $145M Disney term note (4.2%, due 2031) drawn to retire the converts; the Disney Ad Server "
         "migration lifting fill rates and CPMs; ESPN reseller placement inside ESPN's purchase flow; "
         "cross-promotion across Disney's portfolio replacing paid acquisition."),
        ("The skinny ladder. ",
         "A $64.99 sports-and-news tier brackets YouTube TV's genre plans and pulls in cord-nevers who "
         "never subscribed to a traditional bundle — the growth product, if churn can be contained."),
    ],
    "outlook": [
        "Our forward view rests on a judgment about the direction of the pay-TV market, not on "
        "extrapolation of the subscriber line: the virtual pay-TV category consolidates to a small number "
        "of survivors, and survival is determined by scale in programming negotiations. Fubo, combined "
        "with Hulu + Live TV, now has that scale. We expect management to prioritize profitable subscriber "
        "growth over raw subscriber growth — accepting slower net additions in exchange for lower "
        "acquisition cost and better retention — and we expect the skinny sports packages to be the growth "
        "product, pulling in younger sports fans. If that mix shift happens, ARPU can grow even as the "
        "headline subscriber count grows modestly, because sports viewers are the highest-value audience "
        "in the bundle.",
        "On profitability we are more cautious than management's public commentary and haircut its "
        "synergy and margin targets in our model. Programming cost inflation is contractual and relentless "
        "— sports rights escalate at mid-to-high single digits annually — so margins improve only if "
        "subscriber and advertising revenue outrun the escalators. We model the combined entity reaching "
        "sustained positive adjusted EBITDA and then converting to free cash flow as integration costs fade, "
        "but we push the timing later than guidance implies and assume a permanent structural content-cost "
        "headwind that caps the long-run margin below what a mature distributor might earn. The advertising "
        "business is the upside lever we underwrite most confidently: live sports CPMs are premium and "
        "Fubo's owned ad tech captures margin that resold inventory does not.",
        "The balance sheet is the constraint on the whole story. With $236M of cash against $322.5M of "
        "debt at mid-2026, the company must grow into its capital structure; there is limited room for a "
        "programming-cost shock or a subscriber miss. We model refinancing conservatively, at terms that "
        "reflect the speculative credit profile. Deleveraging through operating cash flow, not asset sales, "
        "is the credible path — and it requires the EBITDA inflection to arrive on something close to "
        "schedule. This is the single variable we watch most closely: if the combined entity cannot "
        "demonstrate operating leverage within the next two years, the equity story collapses regardless "
        "of the strategic logic.",
    ],
    "financials": [
        "Read the numbers on the pro forma basis. Three quarters into the combination, the trajectory is "
        "unambiguously improving: revenue stable around $1.5–1.7B per quarter, adjusted EBITDA positive "
        "every quarter ($41.4M, $37.7M, $19.1M), free cash flow approaching breakeven (−$7.5M in FQ3'26 "
        "versus −$41M a year earlier). Management guides FY2026 adjusted EBITDA of $90–100M — roughly a "
        "1.5% margin on ~$6.2B of pro forma revenue — and targets at least $300M by FY2028 (~4–5% margin) "
        "with positive free cash flow in FY2027. Gross margin sits near 7%: the vMVPD's structural reality, "
        "with ~93 cents of every revenue dollar going to content owners.",
        "Balance sheet: $236.4M cash at June 30, 2026 against $322.5M of debt — a $145M Disney senior "
        "unsecured note at 4.2% due 2031 plus $177.5M of converts due 2029 — for net debt of ~$86M. A large "
        "NOL stock shields cash taxes near-term. Liquidity is workable only if the plan delivers: consensus "
        "FCF turns positive (+$125M) in FY2027 after −$441M in FY2026. A miss on the FY2027 FCF target "
        "re-opens the dilution question, and the un-reduced authorized share count gives management the "
        "tool to answer it.",
    ],
    "fin_table": {
        "headers": ["$ mn (pro forma)", "FQ1'26", "FQ2'26", "FQ3'26"],
        "rows": [
            ["Revenue (North America)", "1,675", "1,566", "1,474"],
            ["Subscribers (NA, period-end)", "6.2M", "5.7M", "5.75M"],
            ["Adjusted EBITDA", "41.4", "37.7", "19.1"],
            ["Adj. EBITDA margin", "2.5%", "2.4%", "1.3%"],
            ["Free cash flow", "—", "−214.7*", "−7.5"],
        ],
        "footnote": "*FQ2 FCF outflow was seasonal working capital. Sources: Fubo 8-K exhibits and FQ3'26 press release (2026).",
    },
    "moat": [
        ("Sports depth at mid-tier pricing. ",
         "Regional sports networks and 55,000+ annual events in a $64.99–$98.99 ladder — the deepest "
         "sports lineup of any vMVPD, aimed at the tens of millions of households that subscribe to "
         "streaming primarily for live sports."),
        ("Scale just purchased. ",
         "Sixth-largest U.S. pay-TV operator overnight; programming-cost leverage is the entire margin "
         "story in virtual pay TV, and scale is the only durable way to improve it."),
        ("Owned ad tech on premium inventory. ",
         "Proprietary ad-insertion stack monetizing live sports audiences at premium CPMs, now amplified "
         "by the Disney Ad Server migration — margin that resold inventory does not capture."),
        ("The moat's limits are structural. ",
         "A ~7% gross margin means content owners capture essentially all the value; YouTube TV at 10M+ "
         "subscribers matches Fubo's skinny-tier pricing move for move with deeper pockets. This is a "
         "scale-and-execution story, not a compounder."),
    ],
    "valuation_method": "10-year scenario FCF DCF",
    "valuation_intro": [
        "We value Fubo on a 10-year scenario DCF off a $6.19B FY2026E revenue base (consensus), with "
        "starting EBITDA of $95M (midpoint of the raised $90–100M guide) and EBITDA margins gliding to "
        "3% / 8% / 12% by scenario — FCF modeled as EBITDA less ~1.5% capex intensity, with NOLs shielding "
        "cash taxes. Discount rates are scenario-specific: 12.0% base for this speculative controlled stub, "
        "14.5% bear, 10.5% bull; terminal growth capped at 2.0% on mid-cycle margins. Net debt of $86M is "
        "deducted; all per-share figures divide by 109.2M economic-equivalent shares (30.2M Class A + "
        "79.0M Class B). Terminal value is 35–65% of enterprise value by scenario, under the 70% guardrail.",
        "The bear case genuinely hurts: 0.5% revenue CAGR (under 3%), a 3% steady-state margin 500bp below "
        "the base case, and $2.91 per share — 66% below the quote. We do not underwrite management's "
        "synergy targets at face value: the base-case 8% margin is deliberately below synergy-optimist "
        "hopes, and the controlled-company risk is priced through the 12% base discount rate rather than "
        "an ad hoc stub haircut.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 2.91,
            "assumptions": "Cord-cutting wins; subs drift; synergies accrue to Disney, not the stub; dilutive action on the capital structure",
            "rev_cagr": "+0.5%", "margin_end": "3%",
            "discount": 0.145, "terminal_g": 0.02, "tv_share": 0.35,
            "pv_explicit": 1.89, "pv_terminal": 1.02, "cashflow_unit": "$/sh",
        },
        "base": {
            "fair_value": 28.17,
            "assumptions": "Subs flat-ish, ARPU +2–3%; Disney synergies lift margins toward 8%; ad-server migration delivers",
            "rev_cagr": "+3.5%", "margin_end": "8%",
            "discount": 0.12, "terminal_g": 0.02, "tv_share": 0.55,
            "pv_explicit": 12.68, "pv_terminal": 15.49, "cashflow_unit": "$/sh",
        },
        "bull": {
            "fair_value": 70.94,
            "assumptions": "ESPN distribution + ad-server work; subs +3%; skinny tiers expand the base; margins to 12%",
            "rev_cagr": "+6.0%", "margin_end": "12%",
            "discount": 0.105, "terminal_g": 0.02, "tv_share": 0.65,
            "pv_explicit": 24.83, "pv_terminal": 46.11, "cashflow_unit": "$/sh",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Probability-weighted fair value is $32.55; the $33.00 target is the weighted value rounded.",
    "risks": [
        ("Controlled-company governance — the central risk. ",
         "Disney holds ~70% of the economics and the votes and has shown it will act unilaterally. "
         "Minority shareholders cannot block strategy, capital allocation, or a takeout price they dislike."),
        ("Dilution and overhang. ",
         "The authorized share count was not reduced in the reverse split, and 79M Class A shares are "
         "registered for eventual exchange of Disney's interest. Any liquidity shortfall is likely to be "
         "solved with the printing press."),
        ("Structural margin thinness. ",
         "~7% gross margins are not a phase; they are the vMVPD business model. If content-cost inflation "
         "outruns ARPU, the EBITDA inflection reverses."),
        ("YouTube TV and the scale game. ",
         "Google's 10M+ subscribers and new genre plans match Fubo's moves with deeper pockets; a price "
         "war in skinny sports bundles would compress the exact segment Fubo is counting on."),
        ("Carriage and content risk. ",
         "Each renewal is a potential blackout, subscriber shock, or rate step-up — and sports-first "
         "customers are the least forgiving of gaps."),
        ("Cord-cutting and churn. ",
         "The U.S. pay-TV universe shrinks ~5% a year; sustained sub declines break the synergy math."),
        ("Financing. ",
         "$236M of cash funds the plan only if FY2027 FCF inflects positive as guided. A miss re-opens "
         "the capital question on terms Disney dictates."),
    ],
    "falsification": (
        "Downgrade on: two consecutive quarters of pro forma net subscriber declines (the product thesis "
        "failing); failure to realize announced cost synergies within the guided timeframe; the FY2027 "
        "positive-FCF target slipping; any dilutive equity raise using the un-reduced authorized count; or "
        "Disney actions that subordinate the stub — any of which re-rates the shares toward the $3–9 bear "
        "zone. Conversely, sustained subscriber growth, ad ARPU compounding post-migration, or a takeout "
        "bid would move the conversation toward the $71 bull case. Sell discipline: halve the position if "
        "the stock reaches $25 ahead of the fundamentals; exit entirely on a dilutive raise or a broken "
        "FCF trajectory."
    ),
    "charts": {
        "scenario": {"bear": 2.91, "base": 28.17, "bull": 70.94,
                     "weighted": 32.55, "price": 8.66},
        "trajectory": {
            "years_hist": [2021, 2022, 2023, 2024],
            "revenue_hist": [0.638, 1.009, 1.368, 1.623],
            "fcf_hist": [-0.203, -0.323, -0.200, -0.095],
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": [6.19, 6.41, 6.63, 6.86, 7.10, 7.35, 7.61, 7.88, 8.15, 8.44, 8.73],
            "fcf_proj": [-0.44, 0.125, 0.19, 0.24, 0.29, 0.33, 0.37, 0.40, 0.42, 0.44, 0.463],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: standalone Fubo as-reported (pre-combination). Projections: combined-entity "
                    "base case — revenue at the 3.5% scenario CAGR off the $6.19B FY2026E base; FCF turning "
                    "positive in 2027 per the guided inflection, compounding to the model's 2036 endpoint. "
                    "The 2025 gap reflects the accounting-acquirer changeover.",
        },
        "composition": {
            "bear": {"pv_explicit": 1.89, "pv_terminal": 1.02},
            "base": {"pv_explicit": 12.68, "pv_terminal": 15.49},
            "bull": {"pv_explicit": 24.83, "pv_terminal": 46.11},
            "unit": "$/sh",
        },
        "extra": {
            "type": "pie",
            "title": "Revenue mix, ~2024 (standalone Fubo)",
            "labels": ["Subscription", "Advertising"],
            "values": [88, 12],
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "FUBO-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
