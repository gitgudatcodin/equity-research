"""Wave 4: 8 standalone equity research notes (Oct 4, 2026). Research analysis, not investment advice."""
import os
import re
import sys

sys.path.insert(0, "/home/hatch/workspace/standalone-notes")
from template import build_note

OUT = "/home/hatch/workspace/standalone-notes/pdfs"

BANNED = [re.compile(r"\b" + re.escape(b) + r"\b", re.IGNORECASE) for b in
          ["old target", "previous note", "previous report", "prior report",
           "as we wrote", "prior methodology", "v2", "rebuild", "rebuilt",
           "addenda", "version", "upgraded", "downgraded", "was previously",
           "formerly"]]

BASE_APPROACH = (
    "Our valuation is a probability-weighted scenario DCF. We model bear, base, and bull "
    "cases over an explicit forecast horizon -- 10 years for most businesses -- weighted "
    "25% / 50% / 25%. Discount rates are scenario-specific: the base rate reflects "
    "fundamental business risk (9% for stable franchises, 10% standard, 12% or higher for "
    "speculative situations); the bear case adds 250bp, the bull case subtracts 150bp "
    "(floor 8%). Terminal value assumes no more than 2.5% perpetual growth applied to "
    "normalized mid-cycle margins -- never peak margins -- and any terminal value "
    "exceeding 70% of enterprise value is haircut and disclosed. Bear cases are required "
    "to be genuinely adverse and to sit below the current price. Management guidance is "
    "never accepted at face value; it is independently tested and haircut where evidence "
    "warrants."
)

INTL_BABA = (
    "For international businesses we add an explicit country-risk premium to the discount "
    "rate and benchmark multiples against regional peers facing similar risks, never US "
    "peers alone; structural risks are modeled in cash flows and the bear case. For "
    "Alibaba we add a 250bp China country-risk premium. The VIE structure -- through "
    "which ADR holders own contractual claims on the operating companies rather than "
    "direct equity -- is a structural risk we model explicitly: it features in the bear "
    "case, and we apply a dedicated investment haircut to the probability-weighted fair "
    "value to reflect that ADR holders' claim is contractual, not direct."
)

INTL_GRAB = (
    "For international businesses we add an explicit country-risk premium to the discount "
    "rate and benchmark multiples against regional peers facing similar risks, never US "
    "peers alone; structural risks are modeled in cash flows and the bear case. For Grab "
    "we add a 150bp Southeast Asia country-risk premium, calibrated to the demonstrated "
    "willingness of governments in the region to intervene directly in platform "
    "economics -- Indonesia's commission cap being the live example. The regulation is "
    "modeled explicitly in forecast cash flows and anchors the bear case; it is not "
    "treated as a disclosure item."
)

META_APPROACH = (
    "Our valuation is a probability-weighted scenario DCF. We model bear, base, and bull "
    "cases over an explicit forecast horizon, weighted 25% / 50% / 25%. Businesses meeting "
    "our compounder-quality criteria -- 10+ years of ROIC above 15%, stable or expanding "
    "gross margins, free-cash-flow conversion above 80%, all verified from history, never "
    "projected -- are modeled over a 15-year horizon with an 8-8.5% base discount and a "
    "3.0% terminal growth cap, because genuinely predictable cash flows carry genuinely "
    "lower risk; all other businesses use a 10-year horizon with a 9% (stable franchise), "
    "10% (standard), or 12%+ (speculative) base rate. The bear case adds 250bp, the bull "
    "case subtracts 150bp (floor 8%). Terminal value assumes no more than the applicable "
    "perpetual growth cap applied to normalized mid-cycle margins -- never peak margins "
    "-- and any terminal value exceeding 70% of enterprise value is haircut and disclosed. "
    "Bear cases are required to be genuinely adverse and to sit below the current price. "
    "Management guidance is never accepted at face value; it is independently tested and "
    "haircut where evidence warrants. We apply the compounder-quality treatment to Meta as "
    "a borderline qualifier, and we say so plainly: the Family of Apps meets the criteria "
    "on verified history, but the classification is a judgment call rather than a "
    "mechanical pass, and it is revoked -- reverting to the standard 10-year, 10% "
    "framework -- if ROIC falls below 15%, FCF conversion below 80%, or gross margins "
    "deteriorate. That falsification condition is stated in What Would Change Our Mind."
)


def check_banned(notes):
    bad = []
    def scan(obj, where):
        if isinstance(obj, str):
            for rx in BANNED:
                if rx.search(obj):
                    bad.append((where, rx.pattern))
        elif isinstance(obj, (list, tuple)):
            for i, x in enumerate(obj):
                scan(x, "%s[%d]" % (where, i))
        elif isinstance(obj, dict):
            for k, v in obj.items():
                scan(v, "%s.%s" % (where, k))
    for n in notes:
        scan(n, n["ticker"])
    return bad


notes = []

# ---------------------------------------------------------------- BABA
notes.append({
    "ticker": "BABA",
    "company": "Alibaba Group Holding Limited",
    "verdict": "HOLD",
    "target": "$132.00",
    "price": "$105.85",
    "price_note": "October 2, 2026 close",
    "upside": "+25%",
    "sections": [
        ("Investment Thesis", [
            ("p", "Alibaba is two businesses in one security: a slow-growing but enormously "
             "cash-generative Chinese commerce franchise anchored by Taobao and Tmall, and an "
             "AI-cloud growth engine that just printed its fastest growth in 22 quarters. In the "
             "June quarter, AI Cloud and Compute revenue rose 45% year over year to RMB48.4 "
             "billion, with AI-related products compounding at triple-digit rates for a twelfth "
             "straight quarter and now representing about 35% of external cloud revenue. The "
             "investment debate is whether this cloud reacceleration is a genuine multi-year "
             "S-curve or a capex front-running exercise that shareholders pay for before the "
             "revenue fully catches up."),
            ("p", "Our judgment: the cloud growth is real -- external customer cloud revenue "
             "grew at the same 45%, and cloud adjusted EBITA more than doubled with margins "
             "expanding to roughly 12% -- but the cost of that growth is severe. Capital "
             "expenditure jumped 75% to RMB67.7 billion in the June quarter, free cash flow "
             "swung to a RMB44.7 billion outflow, and group net income fell 75%. Management "
             "expects AI-related spending to break even in about three years; we haircut that "
             "timeline materially. The 20-gigawatt global data-center ambition announced at "
             "Apsara in September 2026 and the in-house Zhenwu V900 accelerator slated for "
             "Q1 2027 show strategic coherence -- Alibaba is building the full AI stack from "
             "silicon to models -- but the undisclosed current gigawatt base makes the cost "
             "trajectory genuinely hard to model, and that opacity is a discount, not a "
             "neutral."),
            ("p", "Commerce remains the ballast: group revenue of RMB269 billion in the June "
             "quarter, up 9%, was the fastest in three years, and the buyback continues to "
             "retire shares. But ADR holders must confront the structure: the VIE arrangement "
             "means a contractual claim, not direct ownership, and we apply an explicit "
             "investment haircut for it on top of a 250bp China country-risk premium. At "
             "$105.85 the market offers a fair price for a genuinely bifurcated story -- real "
             "AI-cloud option value, capped by governance and sovereign risk. HOLD. We would "
             "need the stock materially below $100, or verifiable evidence that AI capex is "
             "converting into cash flow rather than consuming it, to turn more constructive."),
        ]),
        ("Business Overview", [
            ("p", "Alibaba Group, headquartered in Hangzhou, China, is the country's largest "
             "e-commerce and cloud company. The commerce business centers on Taobao (consumer "
             "marketplace) and Tmall (brand flagship platform), supplemented by international "
             "commerce -- AliExpress, Lazada, and Trendyol -- plus Cainiao logistics and a "
             "digital media portfolio. The cloud business, renamed AI Cloud and Compute, is "
             "China's largest public cloud and the engine of the current investment story, "
             "with the Qwen family of large language models and the T-Head semiconductor unit "
             "rounding out a full-stack AI strategy."),
            ("p", "US investors access Alibaba through American Depositary Receipts. The "
             "operating assets in China are held through a variable interest entity (VIE) "
             "structure: ADR holders own shares in a Cayman Islands holding company with "
             "contractual -- not direct equity -- claims on the Chinese operating entities. "
             "This is a legal fact of the investment, and our valuation treats it as one: "
             "the VIE appears in cash-flow modeling, anchors part of the bear case, and "
             "carries a dedicated investment haircut."),
        ]),
        ("Forward Outlook", [
            ("p", "The next three years will be decided in the data centers, not the "
             "marketplaces. If AI-related products sustain triple-digit growth and cloud "
             "EBITA margins march from ~12% toward 20%+, Alibaba owns a genuine second growth "
             "engine with AWS-like economics -- and the in-house silicon (Zhenwu V900) plus "
             "the 20GW buildout are exactly the moves a serious contender makes. Our base "
             "case assumes cloud revenue compounds above 20% with gradual margin "
             "normalization; our skepticism concentrates on the capex duration and the "
             "payback period, which management's three-year breakeven claim understates, in "
             "our judgment."),
            ("p", "Commerce we model as a mid-single-digit grower with take-rate stability: "
             "Taobao/Tmall face relentless competition from Pinduoduo and Douyin, but the "
             "franchise's scale, logistics integration, and merchant ecosystem make "
             "share losses gradual rather than sudden. International commerce is the "
             "higher-growth, lower-margin offset."),
            ("p", "The geopolitical vector is the swing factor no model fully captures. US "
             "export controls on advanced accelerators are precisely the gap Alibaba's "
             "in-house chips are designed to fill; further tightening would slow the AI "
             "buildout, while any easing would be a material positive. We do not forecast "
             "policy; we price the risk at 250bp and size the bear case accordingly."),
        ]),
        ("Valuation", [
            ("p", "We value Alibaba on a probability-weighted scenario DCF with a 250bp China "
             "country-risk premium in the discount rate and an explicit VIE investment "
             "haircut applied to the weighted fair value."),
            ("table", (["Scenario", "Fair value", "Key assumptions"], [
                ["Bear", "$45",
                 "AI-cloud growth stalls under export controls; capex overbuild with weak "
                 "payback; commerce share losses accelerate; regulatory escalation; VIE "
                 "discount widens sharply."],
                ["Base", "$115",
                 "Commerce grows mid-single digits with stable take rates; cloud compounds "
                 "above 20% with EBITA margins normalizing toward 20%; buyback continues; "
                 "AI capex payback lands later than management claims but lands."],
                ["Bull", "$275",
                 "AI Cloud becomes an AWS-scale franchise with 25%+ margins; commerce "
                 "take rates expand on AI-driven monetization; geopolitical overhang "
                 "eases; VIE concerns fade as cash returns compound."],
            ])),
            ("p", "The 25% / 50% / 25% probability-weighted combination of these scenarios, "
             "after the VIE investment haircut, anchors our $132.00 target. The bear case at "
             "$45 sits well below the current $105.85 price, as our framework requires: a "
             "genuinely adverse outcome for this name is a severe one, reflecting how much "
             "of the equity value rests on assumptions about Chinese regulatory stability and "
             "AI-capex payback that could both disappoint at once."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "VIE structure: ADR holders' claim is contractual; any adverse legal or "
                "regulatory ruling on VIE enforceability would impair value directly.",
                "US-China technology decoupling: tighter export controls on accelerators "
                "and manufacturing equipment would slow the AI-cloud buildout.",
                "Capex overbuild: RMB67.7 billion of quarterly capex with negative free "
                "cash flow; if AI demand disappoints, the spending is sunk.",
                "Commerce competition: Pinduoduo and Douyin continue to take share and "
                "pressure take rates in core Chinese retail.",
                "Domestic regulatory risk: the post-2020 crackdown demonstrated Beijing's "
                "willingness to intervene; fintech, data, and platform regulation remain "
                "live risks.",
                "AI monetization timing: twelve quarters of triple-digit AI-product "
                "growth is real, but enterprise AI budgets in China could normalize "
                "faster than capacity comes online.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Sustained positive free cash flow alongside 30%+ cloud growth -- proof "
                "the AI capex is converting, not just consuming.",
                "Cloud adjusted EBITA margins crossing 20% on a sustained basis.",
                "A credible legal or structural resolution clarifying VIE enforceability "
                "for ADR holders.",
                "Commerce take-rate expansion or demonstrable share stabilization "
                "against Pinduoduo and Douyin.",
                "Material easing of US export controls on AI accelerators.",
                "Conversely, a further leg down in commerce growth combined with "
                "widening FCF outflows would move us toward REDUCE.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", BASE_APPROACH),
            ("p", INTL_BABA),
        ]),
    ],
})

# ---------------------------------------------------------------- APP
notes.append({
    "ticker": "APP",
    "company": "AppLovin Corporation",
    "verdict": "HOLD",
    "target": "$335.00",
    "price": "$268.22",
    "price_note": "October 2, 2026 close",
    "upside": "+25%",
    "sections": [
        ("Investment Thesis", [
            ("p", "AppLovin owns one of the finest advertising engines ever built. AXON, the "
             "AI bidder at the heart of its software business, has delivered sustained "
             "50%+ revenue growth at roughly 85% adjusted EBITDA margins -- economics that "
             "have almost no precedent in ad-tech. In June 2026 the company made the defining "
             "move of its history: it opened AXON to all advertisers through a global "
             "self-serve platform, ending the curated, referral-only era. The question now is "
             "whether AXON's legendary precision survives contact with the open market."),
            ("p", "Our judgment: the engine is real, but the self-serve era is a different "
             "business than the curated era, and the market has not yet priced that "
             "difference. Third-party checks show genuine adoption -- pixels at roughly "
             "5,500 merchants by early 2026, growing about 200 per week -- yet the legitimate "
             "question, raised by skeptical channel checks, is whether installations convert "
             "into durable spend. E-commerce is now the swing factor: independent surveys "
             "credit AppLovin with about 11% of e-commerce ad volume by mid-2026, the "
             "largest share gain of any ad network, and a September 2026 study of 755 "
             "e-commerce brands found 2.9x lifetime ROAS on the platform. That is early but "
             "genuinely encouraging evidence -- not yet a verdict."),
            ("p", "The overhangs, however, are non-trivial. A securities class action "
             "covering February through August 2026 alleges management overstated the pace "
             "of AI-model improvements and the readiness of its generative-AI video creative "
             "tool; a separate lawsuit against Unity over alleged misuse of MAX auction data "
             "adds headline risk. With third-quarter guidance calling for 46-48% revenue "
             "growth at ~83% EBITDA margins -- numbers that must be hit to sustain the "
             "multiple -- we see a balanced risk/reward at $268.22. HOLD. The path to "
             "materially higher prices requires proof that self-serve e-commerce "
             "advertisers spend and retain like gaming advertisers did."),
        ]),
        ("Business Overview", [
            ("p", "AppLovin, based in Palo Alto, California, is an ad-tech company built "
             "around three assets: AXON, the AI engine that optimizes ad bidding and user "
             "acquisition; MAX, one of the largest mobile in-app mediation platforms, which "
             "supplies AXON with proprietary auction data; and AppDiscovery, its user "
             "acquisition suite for app developers. The company historically also operated a "
             "portfolio of owned mobile games, but the economic engine -- and the investment "
             "story -- is the software business."),
            ("p", "The strategic arc is expansion beyond mobile gaming, the vertical where "
             "AXON proved itself. E-commerce is the first new vertical at scale, with "
             "connected TV the next frontier. Generative-AI creative tools -- interactive "
             "page and video ad generators -- are meant to close the onboarding gap for "
             "smaller merchants, and the referral program is widening the funnel "
             "down-market. Whether the funnel converts is the central empirical question of "
             "2026 and 2027."),
        ]),
        ("Forward Outlook", [
            ("p", "We expect the next eighteen months to be dominated by one metric: "
             "advertiser retention and spend expansion in the self-serve cohort. If the "
             "e-commerce ROAS advantage holds at scale, AppLovin has a credible path to "
             "becoming a third performance-advertising pillar alongside Meta and Google, "
             "with connected TV as a second act. Our base case assumes software revenue "
             "compounds in the mid-20s percent range with EBITDA margins sustained in the "
             "high 70s to low 80s -- extraordinary, but a step down from the curated-era "
             "peak as the advertiser mix broadens."),
            ("p", "The bear case is that open access commoditizes the signal: more "
             "advertisers bidding on the same inventory compresses ROAS, smaller merchants "
             "churn, and growth decelerates toward the high teens while the multiple "
             "contracts. The class-action litigation is the wild card -- even meritless "
             "suits consume management attention and can force disclosure that resets "
             "expectations. We haircut management's e-commerce ramp accordingly."),
            ("p", "Capital allocation is a quiet strength: the business converts the "
             "overwhelming majority of EBITDA to free cash flow, funding buybacks that "
             "have steadily reduced the share count. That compounding matters more at "
             "today's price than it did at the December 2025 peak."),
            ("p", "Connected TV is the plausible second act beyond e-commerce: the same "
             "AXON bidding intelligence applied to a larger, less mature inventory pool, "
             "where targeting precision is scarcer and therefore more valuable. We do "
             "not underwrite CTV in the base case -- it is early -- but its presence "
             "lengthens the growth runway if e-commerce adoption follows the gaming "
             "playbook. The through-line of our outlook is patience with verification: "
             "the engine has earned the benefit of the doubt on technology, but the "
             "open-platform commercial model has not yet earned it on retention."),
        ]),
        ("Valuation", [
            ("p", "We value AppLovin on a probability-weighted scenario DCF. The base case "
             "assumes software revenue compounds in the mid-20s percent range over the "
             "explicit horizon with adjusted EBITDA margins sustained in the high 70s to "
             "low 80s, normalizing gradually as the advertiser base broadens -- we do not "
             "assume peak margins in perpetuity. The bear case assumes self-serve "
             "dilution: e-commerce adoption stalls, ROAS compresses, growth decelerates "
             "into the teens, and litigation imposes real cost. The bull case assumes AXON "
             "becomes a top-three performance advertising platform with durable 30%+ "
             "growth and connected TV contributing a second leg. Terminal growth is "
             "capped at 2.5% on normalized margins, and the 25% / 50% / 25% weighted fair "
             "value equals our $335.00 target. The bear case sits well below the current "
             "$268.22 price: if the market concludes the curated-era economics do not "
             "transfer to the open platform, the derating would be severe."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Self-serve dilution: open access may compress ROAS and churn smaller "
                "advertisers, undermining the growth narrative.",
                "Securities class action (Feb-Aug 2026 class period) alleging overstated "
                "AI-model progress and video-tool readiness; headline and financial risk.",
                "Unity litigation over alleged MAX auction-data misuse; competitive and "
                "reputational overhang.",
                "Customer concentration in mobile gaming advertisers during the "
                "transition to e-commerce.",
                "Privacy and platform risk: changes to mobile OS attribution (Apple, "
                "Google) could impair targeting efficacy.",
                "Expectations risk: 46-48% guided revenue growth leaves little room for "
                "a miss at the current multiple.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Two consecutive quarters of self-serve advertiser cohorts showing "
                "gaming-like retention and spend expansion -- the single most important "
                "proof point.",
                "Independent ROAS studies at larger scale confirming the early 2.9x "
                "lifetime figure.",
                "Resolution of the class action without material damages or adverse "
                "disclosure.",
                "Connected TV contributing a visible second growth leg.",
                "Conversely, a guided growth deceleration into the teens, or evidence "
                "that pixel installs are not converting to spend, would move us toward "
                "REDUCE.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", BASE_APPROACH),
        ]),
    ],
})

# ---------------------------------------------------------------- BULL
notes.append({
    "ticker": "BULL",
    "company": "Webull Corporation",
    "verdict": "BUY",
    "target": "$9.00",
    "price": "$7.34",
    "price_note": "October 2, 2026 close",
    "upside": "+23%",
    "sections": [
        ("Investment Thesis", [
            ("p", "Webull went public through a SPAC merger with SK Growth Opportunities in "
             "April 2025, and the stock did what SPAC stocks do: it spiked toward $80 within "
             "days on a $37 billion implied valuation, then spent the next sixteen months "
             "falling roughly 90% as the market priced it as a broken deal rather than a "
             "business. Our judgment is that the market is still pricing the deal, not the "
             "business. The second quarter of 2026 was the best in company history: record "
             "revenue, a $34.7 million pretax profit, and revenue growth that led scaled US "
             "retail brokers."),
            ("p", "The business underneath the chart is a genuinely global retail brokerage: "
             "more than 23 million registered users and 50 million-plus app downloads across "
             "14 markets, served through licensed local broker-dealers, with commission-free "
             "trading in stocks, ETFs, options, and -- relaunched -- crypto. Monetization "
             "runs through payment for order flow, margin lending, securities lending, and a "
             "$40-per-year premium tier. At roughly 5.5 to 6 times trailing sales, Webull "
             "trades at about a third of Robinhood's multiple while growing revenue faster. "
             "That gap, in our view, reflects SPAC stigma and post-listing selling overhangs "
             "more than fundamentals."),
            ("p", "The risks are real and, we believe, priced in: payment-for-order-flow "
             "faces perennial regulatory scrutiny, retail trading volumes are cyclical, "
             "competition with Robinhood and incumbents is fierce, and the company's "
             "Chinese origins still invite questions -- mitigated by US re-domiciling and a "
             "St. Petersburg, Florida headquarters. But at $7.34 the market capitalizes "
             "Webull as if international expansion and the crypto relaunch add nothing. We "
             "see 23% upside to our $9.00 fair value, with a path to considerably more if the "
             "company strings together two or three clean quarters and the SPAC discount "
             "decays. BUY."),
        ]),
        ("Business Overview", [
            ("p", "Webull was founded in 2016 by Wang Anquan, a former Alibaba executive, "
             "with early backing from Chinese technology investors including Xiaomi. It "
             "launched in the United States in 2018, gained traction during the 2020-2021 "
             "retail trading wave, and -- to address US-China regulatory concerns -- "
             "separated from its Chinese parent, re-domiciled in the US, and established "
             "headquarters first in New York and now in St. Petersburg, Florida. The April "
             "2025 business combination with SK Growth Opportunities, a SPAC affiliated "
             "with South Korea's SK Group, brought Webull to Nasdaq under the ticker BULL."),
            ("p", "The platform differentiates on depth rather than simplicity: professional-"
             "grade charting, extended-hours trading, and advanced order types aimed at "
             "active self-directed investors, contrasting with simpler competitor apps. "
             "Geographic diversification is the strategic edge -- 14 markets across North "
             "America, Asia-Pacific, Europe, and Latin America -- giving Webull growth "
             "avenues beyond the saturated US retail brokerage market."),
        ]),
        ("Forward Outlook", [
            ("p", "We see three compounding growth levers. First, international markets: "
             "Webull's licensed footprint in Asia-Pacific and Latin America addresses "
             "retail-investor populations that are earlier in their adoption curve than "
             "the US, and early coverage suggests analysts expect 25%+ annual revenue "
             "growth through 2027. Second, the crypto trading relaunch captures a "
             "high-margin, high-engagement product that competitors monetize aggressively. "
             "Third, conversion: with 23 million-plus registered users against a much "
             "smaller funded-account base (4.3 million funded accounts at the end of "
             "2023), each point of conversion is operating leverage."),
            ("p", "Profitability inflection is the story of 2026. The Q2 pretax profit of "
             "$34.7 million, on record revenue, suggests the business has crossed from "
             "growth-at-all-costs into scalable economics -- payment for order flow and "
             "margin interest scale with volumes while the technology platform cost base "
             "grows more slowly. Our base case assumes this operating leverage continues "
             "and international markets contribute an increasing share of funded-account "
             "growth."),
            ("p", "The key variable we watch is not user growth but funded-account and "
             "asset growth: registered users are vanity, assets are revenue. Continued "
             "progress there, plus clean quarterly prints that bury the SPAC narrative, "
             "is what closes the valuation gap to Robinhood."),
        ]),
        ("Valuation", [
            ("p", "We value Webull on a probability-weighted scenario DCF with a 12% base "
             "discount rate, reflecting its short public history, post-SPAC overhang, and "
             "regulatory exposure -- a speculative-situations rate, not a mature-brokerage "
             "one. The base case assumes revenue compounds above 20% through the explicit "
             "horizon as international markets and crypto scale, with pretax margins "
             "expanding as the platform leverages its fixed technology base. The bear case "
             "assumes payment-for-order-flow restrictions, a retail-trading downturn, and "
             "stalled international conversion -- a genuinely adverse outcome that sits "
             "well below the current $7.34 price. The bull case assumes Webull closes a "
             "meaningful portion of the Robinhood multiple gap as clean quarters "
             "accumulate. The 25% / 50% / 25% weighted fair value equals our $9.00 "
             "target. Terminal growth is capped at 2.5% on normalized margins."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Payment-for-order-flow regulation: SEC or international restrictions "
                "would directly impair the core revenue model.",
                "Retail trading cyclicality: volumes and new-account growth mean-revert "
                "in weak markets.",
                "Competition: Robinhood, eToro, and incumbent brokers compete "
                "aggressively on product and pricing.",
                "Post-SPAC selling overhang: insider and early-holder selling pressure "
                "can persist independent of fundamentals.",
                "International regulatory complexity: 14 licensed markets means 14 "
                "regulatory regimes and compliance burdens.",
                "Crypto volatility: the relaunched crypto offering adds a cyclical, "
                "reputationally sensitive revenue stream.",
                "Governance overhang: Chinese origins continue to invite scrutiny "
                "despite US re-domiciling.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Funded-account and customer-asset growth stalling for two consecutive "
                "quarters -- the leading indicator we trust most.",
                "Any regulatory move restricting payment for order flow in the US or a "
                "major international market.",
                "A return to sustained pretax losses, breaking the operating-leverage "
                "narrative.",
                "Evidence that international expansion is failing to convert registered "
                "users into funded accounts.",
                "A governance or fraud event of any kind -- an immediate thesis break.",
                "To the upside: three consecutive clean quarters with accelerating "
                "funded-account growth would justify revisiting fair value materially "
                "higher.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", BASE_APPROACH),
            ("p", "For Webull we apply a 12% base discount rate -- the speculative-"
             "situations end of our framework -- reflecting its sixteen months as a "
             "public company, the post-SPAC selling overhang, and payment-for-order-flow "
             "regulatory exposure. The bear case adds 250bp to this rate and the bull "
             "case subtracts 150bp, consistent with the framework above."),
        ]),
    ],
})

# ---------------------------------------------------------------- META
notes.append({
    "ticker": "META",
    "company": "Meta Platforms, Inc.",
    "verdict": "HOLD",
    "target": "$880.00",
    "price": "$728.08",
    "price_note": "October 2, 2026 close",
    "upside": "+21%",
    "footer_note": "Borderline compounder-quality treatment -- see Valuation Approach.",
    "sections": [
        ("Investment Thesis", [
            ("p", "Meta's advertising business is in the best shape it has been in years. "
             "Revenue grew 33% in the first quarter of 2026 ($56.3 billion) and 28% in the "
             "second ($60.8 billion), operating margins sit near 40%, and 3.56 billion "
             "people use the Family of Apps daily. AI is compounding the ad engine "
             "directly: Advantage+ tooling has lifted advertiser ROI by roughly a third, "
             "and Reels watch time is up more than 30% year over year, unlocking "
             "substantial new inventory. This is one of the great cash machines in "
             "corporate history, and the market knows it."),
            ("p", "But the 2026 story is not the ad business -- it is the capex. Management "
             "guided full-year 2026 capital expenditure of $130-145 billion, roughly double "
             "2025's $72 billion, to fund the superintelligence push: Meta "
             "Superintelligence Labs, the Muse Spark initiative, and custom silicon with "
             "Broadcom to reduce Nvidia dependence. Second-quarter free cash flow collapsed "
             "to $784 million from $8.55 billion a year earlier. Meanwhile Reality Labs "
             "lost $4.6 billion in Q2 alone, with 2026 losses expected to match 2025's "
             "~$19 billion. Our judgment: the ad strength justifies a premium multiple, "
             "but shareholders are funding two moonshots -- superintelligence and Reality "
             "Labs -- from the same cash cow, and the market is right to demand proof of "
             "return before re-rating."),
            ("p", "That tension is why we treat Meta as a borderline compounder-quality "
             "business: a decade-plus record of ROIC well above 15%, stable gross margins, "
             "and free-cash-flow conversion above 80% -- all verified from history -- earns "
             "an extended 15-year horizon and an 8-8.5% base discount rather than the "
             "standard 10%. We call it borderline deliberately, and the treatment is "
             "revoked the moment the numbers stop qualifying. At $728.08, roughly 20x "
             "forward earnings, the stock prices neither the ad strength blindly nor the "
             "spend fearfully. It needs evidence the $130 billion-plus capex converts into "
             "revenue -- agentic ad tools, subscriptions, or a neocloud business -- before "
             "it earns a higher multiple. HOLD."),
        ]),
        ("Business Overview", [
            ("p", "Meta Platforms, headquartered in Menlo Park, California, operates two "
             "segments. Family of Apps -- Facebook, Instagram, WhatsApp, and Messenger -- "
             "generates more than 99% of revenue, almost entirely from advertising, and "
             "reaches 3.56 billion daily active users. Reality Labs houses the Quest VR "
             "headsets and the Ray-Ban Meta AI glasses, contributing under 1% of revenue "
             "while absorbing multi-billion-dollar annual operating losses as the company "
             "bets on AI-powered wearables and the long-term computing platform."),
            ("p", "The strategic pivot of 2025-2026 is the AI infrastructure buildout. "
             "Meta is deploying one of the largest GPU fleets in the world, developing "
             "custom accelerators, and reorganizing AI research under Meta "
             "Superintelligence Labs. A nascent subscription business built around AI "
             "features is the first attempt at a non-advertising revenue line of "
             "consequence."),
        ]),
        ("Forward Outlook", [
            ("p", "Our forward view centers on a single question: does the capex convert? "
             "The leading indicators are encouraging -- AI-driven ad performance gains are "
             "showing up in pricing power (ad prices up double digits alongside impression "
             "growth), and agentic ad tools could automate campaign management for "
             "millions of small advertisers, deepening the moat. Our base case assumes ad "
             "revenue compounds in the mid-teens with gradual margin recovery as the 2026 "
             "capex wave crests and utilization rises from 2027."),
            ("p", "Reality Labs we model as a contained drag, not a turnaround: glasses "
             "unit economics are improving (sales reportedly tripled), but the division "
             "remains years from breakeven and we assign it minimal terminal value. The "
             "superintelligence spend is the genuine uncertainty -- if personal "
             "superintelligence becomes a monetizable product (subscriptions, developer "
             "platform, neocloud), the bull case is very large; if it follows the "
             "metaverse trajectory, it is a multi-year margin tax. We weight the former "
             "modestly and demand evidence."),
            ("p", "Regulation remains a structural headwind: EU data and ad-targeting "
             "rules (including less-personalized-ads requirements), youth-safety "
             "litigation, and ongoing antitrust scrutiny all carry real -- if currently "
             "unquantified -- cost and constraint risk. We model a persistent regulatory "
             "drag in European monetization rather than a single event."),
        ]),
        ("Valuation", [
            ("p", "We value Meta on a probability-weighted scenario DCF using the "
             "borderline compounder-quality treatment described in Valuation Approach: a "
             "15-year explicit horizon, an 8-8.5% base discount, and a 3.0% terminal "
             "growth cap, applied to normalized mid-cycle margins. The base case assumes "
             "Family of Apps ad revenue compounds in the mid-teens, capex intensity "
             "normalizes after the 2026 build, and Reality Labs losses stabilize without "
             "a path to profitability. The bear case assumes ad growth stalls under "
             "macro or regulatory pressure while superintelligence spending continues -- "
             "a genuinely adverse combination that sits well below the current $728.08 "
             "price. The bull case assumes the AI capex converts: agentic ad tools and "
             "subscriptions add new high-margin revenue lines and the multiple "
             "re-rates. The 25% / 50% / 25% weighted fair value equals our $880.00 "
             "target. If the compounder qualification is revoked, fair value under the "
             "standard framework would be materially lower -- which is why the "
             "falsification triggers below are explicit."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Capex overbuild: $130-145 billion of 2026 spending with uncertain "
                "payback; echoes of the metaverse overspend are legitimate.",
                "Reality Labs: ~$19 billion of annual losses with no clear path to "
                "profitability; a permanent margin tax if wearables do not scale.",
                "Ad cyclicality: nearly all revenue is advertising; a macro downturn "
                "hits revenue and the multiple simultaneously.",
                "Regulation: EU targeting restrictions, youth-safety litigation, and "
                "antitrust actions could structurally impair monetization.",
                "AI execution: Llama and superintelligence efforts face formidable "
                "competition; delays would strand capital.",
                "Capital allocation: the dual moonshot funding model concentrates "
                "risk in management's judgment.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Compounder falsification -- any of: ROIC falling below 15%, "
                "free-cash-flow conversion below 80%, or gross-margin deterioration on a "
                "sustained basis. Any one revokes the borderline treatment.",
                "Reality Labs losses accelerating beyond the ~$19 billion annual run "
                "rate without a credible revenue path.",
                "Evidence the AI capex is converting: agentic ad tools or subscriptions "
                "contributing visible, growing revenue -- would support a higher "
                "valuation.",
                "A sustained ad-revenue deceleration into single digits, which would "
                "undermine the quality thesis entirely.",
                "A major adverse regulatory ruling (EU targeting, US antitrust) with "
                "quantified earnings impact.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", META_APPROACH),
        ]),
    ],
})

# ---------------------------------------------------------------- GRAB
notes.append({
    "ticker": "GRAB",
    "company": "Grab Holdings Limited",
    "verdict": "HOLD",
    "target": "$3.40",
    "price": "$3.08",
    "price_note": "October 2, 2026 close",
    "upside": "+10%",
    "footer_note": "Fragile HOLD -- the thesis stands or falls on Indonesia's regulatory trajectory.",
    "sections": [
        ("Investment Thesis", [
            ("p", "Grab is Southeast Asia's dominant super-app -- ride-hailing, food and "
             "grocery delivery, and a fast-growing fintech arm spanning payments, lending, "
             "and digital banking -- with the region's best network density and a genuine, "
             "demonstrated path to sustained profitability. The operating business has "
             "arguably never looked better: deliveries and mobility growing, margins "
             "expanding, and a strong balance sheet funding the fintech buildout. On "
             "operations alone, this would be a constructive story."),
            ("p", "But Indonesia -- Grab's largest market -- just rewrote the unit "
             "economics by decree. Presidential Regulation No. 27/2026 caps platform "
             "commissions at 8% of fare, down from 20%, for two-wheel drivers effective "
             "July 1, 2026, and layers on mandatory social-security contributions. We "
             "model this explicitly in forecast cash flows: it is an estimated $35-40 "
             "million of annualized EBITDA removed from mobility alone, and the true "
             "risk is contagion -- extension to food delivery, to four-wheel drivers, "
             "and to other markets where gig-worker politics are heating up. This is not "
             "a footnote to the thesis; it is the thesis. A government has demonstrated "
             "it will cap the take rate, which caps the terminal margin the entire "
             "investment case rests on."),
            ("p", "At $3.08 the stock prices in much of the damage, and Grab's regional "
             "diversification plus fintech growth keep us from walking away -- hence "
             "HOLD, not SELL. But we flag plainly that this is a fragile HOLD: our "
             "$3.40 target assumes the cap stays contained to Indonesian two-wheel "
             "mobility. Any extension of the cap regime, and the bear case ($1.50) "
             "becomes the operative valuation. We add a 150bp Southeast Asia "
             "country-risk premium to the discount rate to reflect exactly this kind of "
             "sovereign intervention risk."),
        ]),
        ("Business Overview", [
            ("p", "Grab Holdings, headquartered in Singapore and listed on Nasdaq, operates "
             "the leading super-app across eight Southeast Asian countries. The business "
             "has three segments: Deliveries (food, grocery, and parcels), Mobility "
             "(ride-hailing across two- and four-wheel), and Financial Services "
             "(GrabPay, lending, and digital banking ventures including GXBank). "
             "Indonesia is the largest single market and the regulatory epicenter."),
            ("p", "Governance is a structural feature investors must price: Grab is a "
             "Cayman-incorporated foreign private issuer with a dual-class structure, "
             "and a 2026 shareholder vote doubled Class B super-voting rights, "
             "concentrating roughly three-quarters of voting power with co-founder and "
             "CEO Anthony Tan on a small single-digit economic stake. Minority holders "
             "have essentially no mechanism to influence strategy or M&A. We treat this "
             "as a durable governance discount embedded in the required return, not a "
             "temporary overhang."),
        ]),
        ("Forward Outlook", [
            ("p", "Our forward view is two-track. On operations: fintech is the margin "
             "engine -- lending and payments attached to the region's largest consumer "
             "transaction network should compound at high rates with improving credit "
             "performance, and deliveries continues to take share with rationalizing "
             "incentives. Mobility, the historical core, is now a regulated utility in "
             "its largest market: we model Indonesian two-wheel take rates at the "
             "capped 8% in perpetuity and assume no recovery."),
            ("p", "On regulation: the base case assumes containment. The Indonesian cap "
             "applies to two-wheel mobility; food delivery and four-wheel remain "
             "uncapped, and other governments observe rather than imitate. This is a "
             "judgment, not a forecast -- Vietnam's competition commission is already "
             "probing platform commissions, and Singapore and Malaysia have passed "
             "platform-worker laws adding social-security costs. The direction of "
             "travel across the region is toward more intervention, not less, which is "
             "why the country-risk premium stays in the discount rate permanently."),
            ("p", "Consolidation optionality -- most obviously a combination with GoTo, "
             "Grab's Indonesian rival -- is real but we exclude it from the base case "
             "entirely and treat it as bull-case optionality only. The thesis must "
             "stand on the standalone business under the capped regime; it barely "
             "does, which is the honest summary of this note."),
        ]),
        ("Valuation", [
            ("p", "We value Grab on a probability-weighted scenario DCF with a 150bp "
             "Southeast Asia country-risk premium in the discount rate. Indonesia's "
             "commission cap is modeled explicitly in forecast cash flows -- it is the "
             "central variable, not a sensitivity."),
            ("table", (["Scenario", "Fair value", "Key assumptions"], [
                ["Bear", "$1.50",
                 "Commission cap extends to food delivery and four-wheel drivers in "
                 "Indonesia and spreads to a second market; take-rate ceiling becomes "
                 "permanent across mobility; fintech credit losses rise; governance "
                 "discount widens."],
                ["Base", "$3.00",
                 "Cap contained to Indonesian two-wheel mobility at 8%; fintech "
                 "scales with controlled credit costs; deliveries margins expand; "
                 "regional regulation stabilizes at current levels."],
                ["Bull", "$6.00",
                 "Regulatory environment stabilizes with no further intervention; "
                 "fintech lending reaches profitable scale; regional consolidation "
                 "(e.g., GoTo) delivers synergies; take-rate recovery in uncapped "
                 "segments."],
            ])),
            ("p", "The 25% / 50% / 25% probability-weighted combination is $3.375, which "
             "rounds to our $3.40 target. The bear case at $1.50 sits well below the "
             "current $3.08 price, as required: a genuinely adverse regulatory outcome "
             "for this name is a severe one, because the sovereign has already shown "
             "its hand. The narrow spread between price and target is the market's "
             "verdict on regulatory risk -- we agree with the market's caution, but "
             "find the current price modestly too pessimistic on containment."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Regulatory contagion: extension of Indonesia's 8% cap to food delivery, "
                "four-wheel drivers, or other countries would invalidate the base case.",
                "Gig-worker reclassification: platform-worker laws across the region are "
                "adding social-security and insurance costs structurally.",
                "Competition: GoTo in Indonesia and Sea Limited regionally compete "
                "aggressively on incentives and pricing.",
                "Fintech credit risk: lending growth in underbanked markets carries "
                "cyclical and underwriting risk; losses could surprise.",
                "Governance: dual-class control concentration leaves minority holders "
                "with no influence over strategy or M&A.",
                "Foreign exchange: multi-currency Southeast Asian revenue translated "
                "into a USD listing.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Any extension of the commission-cap regime -- to delivery, to "
                "four-wheel, or to another country -- would move us to SELL; the "
                "containment assumption is load-bearing.",
                "Fintech credit losses exceeding through-the-cycle assumptions would "
                "undermine the margin-engine thesis.",
                "Sustained user or transaction decline in the core Indonesian market.",
                "To the upside: credible regulatory stabilization plus demonstrated "
                "take-rate recovery in uncapped segments would justify a more "
                "constructive stance; a value-accretive regional consolidation would "
                "be assessed on its own terms.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", BASE_APPROACH),
            ("p", INTL_GRAB),
        ]),
    ],
})

# ---------------------------------------------------------------- PATH
notes.append({
    "ticker": "PATH",
    "company": "UiPath, Inc.",
    "verdict": "HOLD",
    "target": "$13.50",
    "price": "$13.12",
    "price_note": "October 2, 2026 close",
    "upside": "+3%",
    "sections": [
        ("Investment Thesis", [
            ("p", "The existential question that has hung over UiPath -- do large "
             "language models make robotic process automation obsolete? -- has been "
             "answered, at least for now: agents need a body. AI agents can reason and "
             "plan, but someone still has to click the buttons inside legacy enterprise "
             "systems, and UiPath's robots -- now paired with Maestro, its orchestration "
             "layer for governing fleets of agents from any vendor -- are the most "
             "deployed such body in the enterprise. Founder Daniel Dines returning as "
             "CEO in mid-2024 and the December 2025 inclusion in the S&P MidCap 400 "
             "mark the company's rehabilitation from its post-IPO wilderness."),
            ("p", "Our judgment: the agentic pivot is credible and the numbers are "
             "stabilizing, but stabilization is not reacceleration. The third quarter of "
             "fiscal 2026 (ended October 2025) delivered the company's first "
             "GAAP-profitable third quarter -- $13 million of GAAP operating income on "
             "$411 million of revenue, up 16% year over year -- with 85% non-GAAP gross "
             "margins and more than $1.7 billion of cash against no meaningful debt. "
             "That is a healthy software business. It is not yet a reaccelerating one, "
             "and 16% growth after the brutal deceleration of 2023-2024 deserves "
             "measured -- not enthusiastic -- interpretation."),
            ("p", "The competitive field is the most dangerous in enterprise software: "
             "Microsoft, OpenAI, and every hyperscaler are building agent orchestration "
             "natively into the platforms UiPath automates. UiPath's counter-thesis -- "
             "that enterprises need a vendor-neutral governance layer with "
             "human-in-the-loop controls, audit trails, and cross-platform reach -- is "
             "reasonable and early customer evidence (production agentic deployments at "
             "banks, insurers, and airlines) supports it. But reasonable is not proven. "
             "At $13.12 the market prices a successful-but-not-dominant agentic "
             "transition, which is roughly fair. We wait for proof. HOLD."),
        ]),
        ("Business Overview", [
            ("p", "UiPath, founded in 2005 in Bucharest, Romania by Daniel Dines and "
             "Marius Tirca and now headquartered in New York, is the market leader in "
             "robotic process automation. Its platform spans Studio (development), "
             "Orchestrator (management), and attended and unattended robots that "
             "execute workflows across enterprise applications. The 2021 IPO was one of "
             "the largest US software listings ever, valuing the company above $35 "
             "billion; the subsequent years brought slowing growth, a cloud transition, "
             "and the 2024 leadership change that returned Dines to the CEO role."),
            ("p", "The current platform strategy is agentic automation: Maestro "
             "orchestrates AI agents built by UiPath, Microsoft, OpenAI, or customers "
             "themselves; Autopilot offers natural-language workflow creation; and new "
             "AI models let robots interpret user interfaces without underlying API "
             "access. The commercial thesis is 'agents decide, robots execute, humans "
             "handle exceptions' -- with governance built in from the start, which is "
             "what regulated enterprises require before they scale agents."),
        ]),
        ("Forward Outlook", [
            ("p", "We see the next two years as a show-me period with a binary flavor. "
             "If Maestro becomes the enterprise standard for governing heterogeneous "
             "agent fleets -- the Switzerland of agentic AI -- UiPath has a genuine "
             "second act with pricing power and net-revenue-retention expansion. Early "
             "signs are directionally positive: the 2026 customer awards highlighted "
             "production-scale agentic deployments with measured (not projected) "
             "returns, and Maestro appeared across nearly every winning submission."),
            ("p", "The alternative is absorption: agentic workflows get built natively "
             "into Microsoft 365, Salesforce, and ServiceNow, and UiPath is left "
             "automating the shrinking residue of legacy processes. Our base case sits "
             "between these poles -- mid-teens revenue growth reaccelerating toward "
             "20% as agentic products scale, with the fortress balance sheet funding "
             "R&D and opportunistic M&A -- but we weight the absorption scenario "
             "materially because platform history favors the platforms."),
            ("p", "Capital allocation is straightforward and shareholder-friendly: no "
             "meaningful debt, a large cash balance, and buybacks offsetting dilution. "
             "The debate is entirely about the top line's second derivative, and on "
             "that the honest answer is that the data are promising but early."),
            ("p", "One underappreciated asset is the installed base itself: tens of "
             "thousands of enterprise customers with UiPath robots already embedded in "
             "their processes are the natural distribution channel for Maestro. "
             "Selling orchestration to a customer that already trusts your robots is "
             "a fundamentally easier motion than selling it cold -- and it is why we "
             "give the agentic pivot better odds than a standing start would deserve. "
             "The installed base does not guarantee the transition, but it "
             "meaningfully shortens the sales cycle for it."),
        ]),
        ("Valuation", [
            ("p", "We value UiPath on a probability-weighted scenario DCF at the standard "
             "10% base discount rate -- this is a real software business with 85% gross "
             "margins and a cash-rich balance sheet, but not a compounder-quality "
             "franchise on verified history, so no extended-horizon treatment applies. "
             "The base case assumes revenue growth reaccelerates from the mid-teens "
             "toward 20% as agentic products scale, with operating margins expanding "
             "on the high gross-margin base. The bear case assumes platform absorption: "
             "growth decelerates back toward 10%, pricing power erodes, and the "
             "multiple contracts -- a genuinely adverse outcome sitting well below the "
             "current $13.12 price. The bull case assumes Maestro becomes the "
             "enterprise-standard agent governance layer with 25%+ sustained growth. "
             "Terminal growth is capped at 2.5% on normalized margins, and the 25% / "
             "50% / 25% weighted fair value equals our $13.50 target -- essentially the "
             "current price, which is why this is a HOLD and not a BUY."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Platform absorption: Microsoft, OpenAI, and hyperscalers building "
                "native agent orchestration could marginalize a third-party layer.",
                "Growth reacceleration is unproven: 16% is stabilization, and the "
                "agentic revenue contribution is still early.",
                "Enterprise budget cyclicality: automation spending is deferrable in "
                "a downturn.",
                "Seat-based pricing pressure as automation shifts toward "
                "consumption-based agent models.",
                "Execution risk on the product transition from deterministic RPA to "
                "agentic orchestration.",
                "Founder dependence: Dines owns roughly 20% and the turnaround is "
                "closely tied to his leadership.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Two consecutive quarters of accelerating revenue growth with "
                "agentic products called out as the driver -- the single most "
                "important proof point.",
                "Evidence of Maestro standardization: large enterprises deploying it "
                "as the cross-vendor agent governance layer.",
                "Net revenue retention inflecting upward on agentic expansion.",
                "Conversely, growth decelerating back toward 10%, or a major "
                "platform competitor launching a directly comparable orchestration "
                "layer with rapid adoption, would move us toward REDUCE.",
                "A large dilutive acquisition would also force a reassessment.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", BASE_APPROACH),
        ]),
    ],
})

# ---------------------------------------------------------------- IBM
notes.append({
    "ticker": "IBM",
    "company": "International Business Machines Corporation",
    "verdict": "HOLD",
    "target": "$223.00",
    "price": "$222.64",
    "price_note": "October 2, 2026 close",
    "upside": "+0%",
    "sections": [
        ("Investment Thesis", [
            ("p", "IBM's investment case has always been the software mix shift: Red "
             "Hat-led hybrid cloud compounding while the mainframe prints cash. The "
             "second quarter of 2026 broke the second half of that story. IBM Z revenue "
             "fell 42% as clients deferred purchases ahead of the z17 cycle and shifted "
             "spending toward supply-constrained servers and storage; management "
             "preannounced the shortfall on July 14, and the stock suffered its worst "
             "single-day decline in 115 years as a listed company. Full-year "
             "constant-currency revenue guidance was rebased from above 5% to 4-5%."),
            ("p", "Our judgment: the quarter was a genuine stumble, not a broken thesis. "
             "Red Hat revenue growth accelerated to 11%, data products grew 19%, "
             "distributed infrastructure grew 37% with roughly $500 million of backlog, "
             "and -- critically -- the z17 program is tracking at nearly 130% of the "
             "comparable z16 trajectory. Mainframe demand is deferred, not destroyed. "
             "Management reiterated free-cash-flow growth of about $1 billion for the "
             "year and operating pre-tax margin expansion of roughly 100 basis points. "
             "We haircut the second-half recovery narrative -- guidance credibility "
             "was dented and must be re-earned -- but we do not discard it."),
            ("p", "The balance sheet carries the acquisition strategy: total debt of $62 "
             "billion and net debt around $54 billion after $10.5 billion of "
             "year-to-date acquisition spending (HashiCorp, Confluent), against $8.2 "
             "billion of cash. The $1.69 quarterly dividend -- paid continuously since "
             "1916 -- remains well covered by $13 billion-plus of trailing free cash "
             "flow. At $222.64, more than 20% below where the year began, the stock "
             "trades at a discount that already reflects the credibility damage. Our "
             "$223.00 fair value says the market has it about right: a durable "
             "software franchise with a bruised multiple and a leveraged balance "
             "sheet. HOLD."),
        ]),
        ("Business Overview", [
            ("p", "IBM, headquartered in Armonk, New York, reports in three segments. "
             "Software ($7.8 billion of Q2 2026 revenue, up 5%) spans hybrid cloud "
             "platforms led by Red Hat (up 11%), data (up 19%), automation (up 4%), "
             "and transaction processing (down 8%) -- the last still coupled to the "
             "mainframe cycle. Consulting ($5.3 billion, roughly flat) covers strategy, "
             "technology implementation, and intelligent operations. Infrastructure "
             "($3.8 billion, down 7%) houses the IBM Z mainframe franchise and "
             "distributed infrastructure (Power and storage, up 37%). Software is "
             "roughly 80% recurring with $24.6 billion of annual recurring revenue, up "
             "8%."),
            ("p", "The strategic portfolio has been reshaped by acquisition: Red Hat "
             "(2019) anchored hybrid cloud, HashiCorp brought infrastructure "
             "automation, and Confluent (closed March 2026) added real-time data "
             "streaming for AI workloads. A $5 billion Lightwell software-security "
             "initiative and a planned $10 billion-plus quantum computing investment "
             "over five years round out the capital deployment."),
        ]),
        ("Forward Outlook", [
            ("p", "The second half of 2026 is the mainframe cycle's to win or lose. The "
             "z17 ramp -- tracking well ahead of z16 at the comparable point -- should "
             "drive a sharp Infrastructure rebound and pull transaction-processing "
             "software with it, since so much of IBM's software monetization remains "
             "coupled to mainframe capacity. Our base case assumes the cycle delivers "
             "but with less vigor than management's original framing; we model "
             "software growth of 6-8% for the year, in line with the rebased guide, "
             "rather than the acceleration previously implied."),
            ("p", "Red Hat is the durable compounder inside the conglomerate: OpenShift "
             "positioned for AI workloads, 11% growth reaccelerating, and the "
             "HashiCorp/Confluent integrations deepening the automation and data "
             "stack. Consulting's flat quarter is the soft spot -- the historical "
             "offset during software softness did not show up -- and its recovery is "
             "tied to enterprise AI-implementation demand materializing in 2027."),
            ("p", "Deleveraging is the quiet imperative. With $62 billion of debt, "
             "every quarter of $3 billion-plus free cash flow that goes to debt paydown "
             "rather than new deals improves the equity risk profile. We expect "
             "management to prioritize the balance sheet over further large "
             "acquisitions, and we would view a return to big-ticket M&A before "
             "leverage normalizes as a negative signal."),
            ("p", "Longer term, the question is what IBM looks like when the portfolio "
             "transformation is complete: a software-led company with 80%-plus "
             "recurring revenue, a consulting arm levered to AI implementation, and a "
             "mainframe franchise managed as a high-margin annuity rather than a "
             "growth engine. That company deserves a mid-teens multiple on "
             "through-cycle earnings. Getting there requires two things we have not "
             "yet seen together: a clean mainframe cycle and a consulting recovery. "
             "The second half of 2026 is the first real test of whether both can "
             "coincide -- and our HOLD reflects genuine uncertainty about the "
             "answer, not indifference to it."),
        ]),
        ("Valuation", [
            ("p", "We value IBM on a probability-weighted scenario DCF at a 9% base "
             "discount rate, the stable-franchise rate -- the software business's 80% "
             "recurring revenue and the mainframe's annuity-like installed base "
             "justify it, with the leveraged balance sheet and hardware cyclicality "
             "kept in view. The base case assumes software grows 6-8% with the z17 "
             "cycle delivering a second-half infrastructure rebound, free cash flow "
             "grows about $1 billion for the year, and the dividend is sustained. The "
             "bear case assumes the mainframe cycle disappoints, consulting stays "
             "flat, and leverage constrains capital returns -- a genuinely adverse "
             "outcome sitting well below the current $222.64 price. The bull case "
             "assumes Red Hat reaccelerates into the mid-teens on AI workloads and "
             "the z17 cycle exceeds the z16 trajectory. Terminal growth is capped at "
             "2.5% on normalized mid-cycle margins, and the 25% / 50% / 25% weighted "
             "fair value equals our $223.00 target -- the market price, which is "
             "precisely why this is a HOLD."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Mainframe cycle dependence: a large share of software monetization "
                "remains coupled to IBM Z capacity; cycle disappointments cascade.",
                "Guidance credibility: the July preannouncement damaged "
                "management's forecasting reputation; further misses would derate "
                "the stock structurally.",
                "Leverage: $62 billion of debt ($54 billion net) after heavy "
                "acquisition spending constrains flexibility.",
                "Consulting stagnation: flat revenue removes the historical offset "
                "during software softness.",
                "Competition: hyperscalers and pure-play software vendors contest "
                "every growth segment IBM is leaning on.",
                "Execution on large acquisitions: HashiCorp and Confluent must "
                "deliver the growth that justified their prices.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "A clean second half: z17-driven infrastructure rebound plus "
                "software growth at the high end of the 6-8% guide would restore "
                "credibility and justify a higher multiple.",
                "Red Hat growth sustaining above 12% on AI-workload demand.",
                "Visible deleveraging: net debt declining meaningfully quarter "
                "over quarter.",
                "Conversely, a second consecutive guidance cut, consulting revenue "
                "declining, or a large debt-funded acquisition would move us toward "
                "REDUCE.",
                "Dividend coverage coming under pressure would be an immediate "
                "negative reassessment trigger.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", BASE_APPROACH),
            ("p", "For IBM we apply the 9% stable-franchise base rate: the software "
             "segment's ~80% recurring revenue and the mainframe installed base's "
             "annuity-like economics support it. The leveraged balance sheet and "
             "hardware cyclicality are captured in the scenario design -- particularly "
             "the bear case -- rather than in a higher discount rate."),
        ]),
    ],
})

# ---------------------------------------------------------------- CMCSA
notes.append({
    "ticker": "CMCSA",
    "company": "Comcast Corporation",
    "verdict": "HOLD",
    "target": "$21.00",
    "price": "$21.57",
    "price_note": "October 2, 2026 close",
    "upside": "-3%",
    "sections": [
        ("Investment Thesis", [
            ("p", "Comcast spent a decade being valued as a melting ice cube attached to "
             "a good business. On January 2, 2026, it finally separated the two: the "
             "Versant Media Group spin-off -- most of NBCUniversal's cable networks "
             "including CNBC, USA Network, E!, Syfy, and Golf Channel, distributed "
             "1-for-25 to shareholders -- leaves Comcast as a connectivity company "
             "(broadband, wireless, business services) plus NBC, Telemundo, Peacock, "
             "the Universal studios, the theme parks, and Sky. The surgery was "
             "correct; it does not cure the patient."),
            ("p", "Our judgment: the remaining business is a cash machine with a "
             "shrinking core. Broadband -- the profit engine -- continues to lose "
             "subscribers to fiber overbuilders and fixed wireless, even as ARPU "
             "growth offsets some of the decline; video is in structural retreat; "
             "wireless is growing but low-margin. What Comcast undeniably has is "
             "cash: a forward P/E of 8-9x and a free-cash-flow yield above 10% on a "
             "connectivity franchise still generating on the order of $70 billion of "
             "annual revenue across 65 million homes and businesses. The dividend and "
             "buyback are well covered, Peacock's losses are narrowing, and the parks "
             "are a genuine growth asset."),
            ("p", "At $21.57 the stock is priced as a no-growth cash cow, and that is "
             "roughly what it is. Multiple expansion requires broadband subscriber "
             "stabilization -- evidence that the connectivity business can grow "
             "again, not just harvest ARPU -- and we do not see that evidence yet. "
             "Our $21.00 fair value implies modest downside from here: this is a HOLD "
             "for income-oriented holders, not a compounding story. The bull case "
             "needs the broadband base to stabilize and wireless bundling to "
             "demonstrate real churn benefits; until then, the market's skepticism "
             "is rational."),
        ]),
        ("Business Overview", [
            ("p", "Post-Versant, Comcast Corporation -- headquartered in Philadelphia -- "
             "is two things. Connectivity and Platforms: Xfinity residential and "
             "commercial broadband, video distribution, a growing wireless business "
             "built on an MVNO agreement, and business services -- the cash engine, "
             "reaching roughly 65 million homes and businesses. And Content and "
             "Experiences: the NBC broadcast network, Telemundo, the Bravo cable "
             "brand, Peacock streaming, Universal Pictures and Universal Television, "
             "Universal Destinations and Experiences (theme parks), and Sky in "
             "Europe."),
            ("p", "The Versant separation, completed January 2, 2026 as a tax-free "
             "distribution, removed the declining linear-network bundle -- USA, CNBC, "
             "the network now known as MS NOW, Oxygen, E!, Syfy, Golf Channel, plus "
             "digital assets including Fandango and Rotten Tomatoes -- along with "
             "about $3 billion of associated indebtedness, for which Comcast received "
             "a $2.25 billion cash distribution. Comcast retains no equity interest "
             "in Versant."),
        ]),
        ("Forward Outlook", [
            ("p", "The central operating question is the broadband subscriber line. "
             "Management's playbook -- ARPU growth through speed-tier upgrades and "
             "bundling, plus wireless attach to reduce churn -- can sustain cash flow "
             "for years even with modest subscriber losses, but the equity multiple "
             "will not expand while the base shrinks. We model continued low-single-"
             "digit subscriber declines with ARPU growth roughly offsetting, leaving "
             "connectivity revenue flat to slightly down -- a harvest profile, "
             "honestly described."),
            ("p", "Peacock is the swing asset on the content side: losses narrowing, "
             "scale approaching the point where the streaming business can stand on "
             "its own economics, though we assign it modest terminal value given the "
             "competitive intensity of streaming. The parks business -- Epic Universe "
             "now in its second full year -- is the clearest organic growth driver in "
             "the portfolio, and Sky's turnaround, while slow, removes a drag."),
            ("p", "Capital allocation is the shareholder proposition: with "
             "double-digit free-cash-flow yields, the combination of dividend growth "
             "and buybacks should deliver high-single-digit cash returns even without "
             "multiple expansion. That is an attractive holding proposition at the "
             "right price; at $21.57, with our fair value at $21.00, the price is "
             "roughly right already."),
            ("p", "There is a subtler bull case worth naming even though we do not "
             "underwrite it: the market may be underestimating how long a harvest "
             "profile can run. Cable broadband's high incremental margins mean that "
             "even flat revenue with disciplined capital spending throws off enormous "
             "cash for a very long time, and Comcast's scale advantages in network "
             "operations are real. If subscriber losses merely stabilize at a slower "
             "rate of decline -- not reverse, just decelerate -- the combination of "
             "a 10%+ FCF yield and buybacks compounds equity value faster than the "
             "current 8-9x P/E implies. We keep this as upside optionality rather "
             "than base case because hope is not a thesis, but it is the reason this "
             "name stays on the watchlist rather than in the discard pile."),
        ]),
        ("Valuation", [
            ("p", "We value Comcast on a probability-weighted scenario DCF at a 9% "
             "base discount rate, the stable-franchise rate -- the connectivity "
             "installed base and subscription economics justify it despite the "
             "subscriber declines. The base case assumes connectivity revenue flat "
             "to slightly down with ARPU offsetting subscriber losses, Peacock "
             "losses narrowing toward breakeven, parks growing, and free cash flow "
             "sustained at levels supporting the dividend and buyback. The bear case "
             "assumes accelerating broadband share loss to fiber and fixed wireless "
             "with ARPU growth faltering -- a genuinely adverse outcome sitting "
             "below the current $21.57 price. The bull case assumes subscriber "
             "stabilization and wireless bundling proving out, with modest multiple "
             "expansion. Terminal growth is capped at 2.5% on normalized margins, "
             "and the 25% / 50% / 25% weighted fair value equals our $21.00 target -- "
             "modestly below the current price, consistent with a HOLD rather than a "
             "BUY."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Broadband subscriber losses: fiber overbuild and fixed wireless "
                "continue to take share; ARPU offsets have limits.",
                "Video cord-cutting: structural decline in the remaining video "
                "business pressures revenue and margins.",
                "Wireless margin profile: growth in a low-margin MVNO business "
                "dilutes the connectivity margin mix.",
                "Peacock: streaming losses, while narrowing, still consume capital "
                "in a brutally competitive market.",
                "Sky: European operations face macro and competitive pressures.",
                "Capital intensity: network investment requirements compete with "
                "shareholder returns for free cash flow.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Two consecutive quarters of broadband subscriber stabilization or "
                "growth -- the single development that would unlock multiple "
                "expansion.",
                "Evidence that wireless bundling materially reduces churn and "
                "improves lifetime value.",
                "Peacock reaching sustained profitability ahead of expectations.",
                "Conversely, accelerating subscriber losses combined with ARPU "
                "growth stalling would move us toward REDUCE.",
                "A large debt-funded acquisition or a dividend cut would force an "
                "immediate reassessment.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", BASE_APPROACH),
        ]),
    ],
})


def main():
    bad = check_banned(notes)
    if bad:
        print("BANNED PHRASES FOUND:")
        for where, b in bad:
            print("  %s: %r" % (where, b))
        raise SystemExit(1)
    print("Banned-phrase check: clean (%d notes)" % len(notes))
    os.makedirs(OUT, exist_ok=True)
    from pypdf import PdfReader
    for n in notes:
        path = os.path.join(OUT, "%s-equity-research-note.pdf" % n["ticker"])
        build_note(path, n)
        r = PdfReader(path)
        pages = len(r.pages)
        text = "".join((p.extract_text() or "") for p in r.pages)
        assert pages > 0 and len(text) > 500, "verification failed for %s" % n["ticker"]
        print("%s: %d pages, %d chars extracted -- OK" % (n["ticker"], pages, len(text)))


if __name__ == "__main__":
    main()
