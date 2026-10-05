"""Build 8 standalone equity research PDFs (batch W1). Zero self-references to any past work."""
import os, sys
sys.path.insert(0, os.path.expanduser("~/workspace/standalone-notes"))
from template import build_note

OUT = os.path.expanduser("~/workspace/standalone-notes/pdfs")
PRICE_NOTE = "October 2, 2026 close"

METHOD_BASE = (
    "Our valuation is a probability-weighted scenario DCF. We model bear, base, and bull "
    "cases over an explicit 10-year forecast horizon, weighted 25% / 50% / 25%. Discount rates "
    "are scenario-specific: the base rate reflects fundamental business risk (9% for stable "
    "franchises, 10% standard, 12% or higher for speculative situations); the bear case adds "
    "250bp, the bull case subtracts 150bp (floor 8%). Terminal value assumes no more than 2.5% "
    "perpetual growth applied to normalized mid-cycle margins -- never peak margins -- and any "
    "terminal value exceeding 70% of enterprise value is haircut and disclosed. Bear cases are "
    "required to be genuinely adverse and to sit below the current price. Management guidance "
    "is never accepted at face value; it is independently tested and haircut where evidence warrants."
)

METHOD_INTL = (
    " For international businesses we add an explicit country-risk premium to the discount rate "
    "and benchmark multiples against regional peers facing similar risks, never US peers alone; "
    "structural risks (e.g. VIE structures, regulatory confiscation) are modeled in cash flows "
    "and the bear case."
)

# ---------------------------------------------------------------- FUBO
fubo = dict(
    ticker="FUBO", company="fuboTV Inc.", verdict="BUY",
    target="$33.00", price="$8.66", price_note=PRICE_NOTE, upside="+281%",
    spec=True,
    footer_note="Speculative situation -- wide range of outcomes; high uncertainty.",
    sections=[
        ("Investment Thesis", [
            ("p", "fuboTV is the only sports-centric live pay-TV bundle operating at national scale in the "
             "United States, and the combination of Fubo with Hulu + Live TV creates a streaming business with "
             "a subscriber base on the order of six million households. Live sports remains the last form of "
             "appointment viewing in television, and it is the one content category whose pricing power has "
             "survived the streaming transition intact. Our judgment is that a focused, sports-first bundle -- "
             "priced below the flagship virtual pay-TV packages and sold to the tens of millions of households "
             "that subscribe to streaming primarily for live sports -- is a structurally sound product in a "
             "market where every general-entertainment bundle is being repriced downward. The current share "
             "price values Fubo as a melting ice cube; we see a business whose core asset, exclusive-feeling "
             "access to live sports at a mid-tier price point, is appreciating while the price ascribes it "
             "roughly no value."),
            ("p", "The path from here to a much higher equity value runs through three levers, and we have a "
             "view on each. First, the combination with Hulu + Live TV gives the business the scale to amortize "
             "programming costs that were previously borne by a sub-two-million-subscriber base -- content cost "
             "per subscriber is the entire margin story in virtual pay TV, and scale is the only durable way to "
             "improve it. Second, advertising on live sports inventory is among the highest-value ad product in "
             "media, and Fubo's owned ad-tech stack plus its sports audience give it a monetization lever that "
             "subscriber revenue alone does not capture. Third, the skinny sports-focused packages Fubo has "
             "committed to offering address the single biggest objection to virtual pay TV -- that subscribers "
             "pay for a hundred channels to watch ten -- and should expand the addressable market beyond "
             "traditional bundle subscribers to cord-nevers."),
            ("p", "We want to be plain about what this is: a speculative situation with a very wide range of "
             "outcomes. Programming costs rise every renewal cycle, subscriber acquisition in streaming is "
             "expensive and churn is high, carriage disputes can remove channels overnight, and the balance "
             "sheet carries meaningful leverage. The bear case is genuine distress, and the bull case requires "
             "the combined entity to execute a turnaround that management teams in this industry have often "
             "promised and rarely delivered. Our probability-weighted fair value of $33.00 sits far above the "
             "$8.66 share price because the arithmetic of the situation is asymmetric: the bear case destroys "
             "most of the equity, but the base and bull cases -- in which scale finally makes the unit economics "
             "work -- imply a business worth several multiples of today's price. This is a small position for "
             "investors who can tolerate a wide outcome distribution, not a core holding."),
        ]),
        ("Business Overview", [
            ("p", "fuboTV Inc. was founded in 2015 as a soccer-focused streaming service and has grown into a "
             "sports-first virtual multichannel video programming distributor (vMVPD): a live-TV bundle delivered "
             "over the internet, sold in tiers, with cloud DVR and on-demand content. The flagship Fubo service "
             "carries major sports networks alongside news and entertainment channels, and the company has "
             "expanded the product line downward with lower-priced sports-oriented packages. Revenue comes from "
             "subscriptions and from advertising, including dynamically inserted ads in live and on-demand "
             "streams. The company also owns the Fubo Sports linear network and operates in France, and it has "
             "built proprietary ad-insertion and billing technology rather than renting the full stack."),
            ("p", "The defining corporate event is the combination with Disney's Hulu + Live TV business, under "
             "which Disney holds a majority stake in the combined entity while Fubo continues as the publicly "
             "traded vehicle. The logic is straightforward: two sub-scale virtual pay-TV operators, each too "
             "small to negotiate programming costs from strength, become one operator with a subscriber base "
             "large enough to matter to programmers and to spread fixed content costs. The settlement of the "
             "sports-streaming litigation that preceded the deal also cleared the way for the skinny-bundle "
             "products both sides had been blocked from offering. Whether the combination delivers depends "
             "almost entirely on execution -- integration of two technology stacks, realization of cost "
             "synergies, and disciplined pricing -- rather than on the strategic logic, which is sound."),
        ]),
        ("Forward Outlook", [
            ("p", "Our forward view of Fubo rests on a judgment about the direction of the pay-TV market, not "
             "on extrapolation of the subscriber line. We believe the virtual pay-TV category consolidates to a "
             "small number of survivors and that survival is determined by scale in programming negotiations. "
             "Fubo, combined with Hulu + Live TV, now has that scale. We expect management to prioritize "
             "profitable subscriber growth over raw subscriber growth -- accepting slower net additions in "
             "exchange for lower acquisition cost and better retention -- and we expect the skinny sports "
             "packages to be the growth product, pulling in younger sports fans who never subscribed to a "
             "traditional bundle. If that mix shift happens, average revenue per user can grow even as the "
             "headline subscriber count grows modestly, because sports viewers are the highest-value audience "
             "in the bundle."),
            ("p", "On profitability, we are more cautious than management's public commentary and we haircut "
             "its synergy and margin targets in our model. Programming cost inflation is contractual and "
             "relentless -- sports rights escalate at mid-to-high single digits annually -- which means margins "
             "improve only if subscriber and advertising revenue outrun the escalators. We model the combined "
             "entity reaching sustained positive adjusted EBITDA and then converting to free cash flow as "
             "integration costs fade, but we push the timing later than guidance implies and we assume a "
             "permanent structural content-cost headwind that caps the long-run margin below what a mature "
             "distributor might earn in a friendlier rights environment. The advertising business is the "
             "upside lever we underwrite most confidently: live sports CPMs are premium, the audience is "
             "cord-cutting-resistant, and Fubo's owned ad tech captures margin that resold inventory does not."),
            ("p", "The balance sheet is the constraint on the whole story. Leverage incurred to fund growth and "
             "the combination means the company must grow into its capital structure; there is limited room for "
             "a programming-cost shock or a subscriber miss. We expect refinancing activity over our forecast "
             "horizon and we model it conservatively, assuming terms that reflect the company's speculative "
             "credit profile rather than investment-grade pricing. Deleveraging through operating cash flow, "
             "not asset sales, is the credible path, and it requires the EBITDA inflection to arrive on "
             "something close to schedule. This is the single variable we watch most closely: if the combined "
             "entity cannot demonstrate operating leverage within the next two years, the equity story "
             "collapses regardless of the strategic logic."),
        ]),
        ("Valuation", [
            ("p", "We value Fubo on a probability-weighted scenario DCF, with a 12% base discount rate "
             "reflecting the speculative credit profile and the structural headwinds of the business, 250bp "
             "added in the bear case and 150bp subtracted in the bull case, and terminal growth capped at "
             "2.5% on normalized mid-cycle margins. We do not publish per-scenario point values because the "
             "outcome distribution is unusually wide; instead we describe the drivers. The bear case assumes "
             "the combination fails to deliver synergies, programming cost escalators outrun revenue, churn "
             "stays elevated, and the capital structure forces dilutive action -- a genuinely adverse outcome "
             "in which the equity is worth a small fraction of today's price, well below $8.66. The base case "
             "assumes the combined entity stabilizes its subscriber base, realizes a haircut portion of the "
             "announced synergies, grows advertising at a premium to subscriptions, and reaches durable "
             "positive free cash flow as integration costs roll off. The bull case assumes Fubo becomes the "
             "independent sports bundle of record in the US -- the default streaming home for the sports-first "
             "household -- with skinny packages expanding the subscriber base materially and the advertising "
             "business scaling to a meaningful share of revenue at high incremental margins."),
            ("p", "Blending these scenarios at 25% / 50% / 25% yields a probability-weighted fair value of "
             "$33.00, which is our target. The implied +281% upside is a measure of how deeply the market "
             "discounts the turnaround, not a forecast of smooth appreciation: we expect high volatility, and "
             "the position sizing for a situation like this should reflect the genuine possibility of the bear "
             "case. Our target embeds haircuts to management's synergy and margin guidance throughout; we do "
             "not underwrite the bull case on management's numbers."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Programming cost inflation: sports rights escalate contractually; a bad renewal cycle can erase a year of operating leverage.",
                "Leverage and refinancing: the capital structure leaves little room for a subscriber or EBITDA miss; refinancing terms may be punitive.",
                "Churn and acquisition cost: streaming subscribers are fickle and acquisition spend is high; elevated churn destroys lifetime value.",
                "Carriage disputes: loss of a major sports network, even temporarily, can trigger subscriber flight.",
                "Competition: YouTube TV, Hulu + Live TV (as a product), and direct-to-consumer sports apps all compete for the same household.",
                "Advertising cyclicality: a large share of the upside is ad revenue, which is cyclical and sensitive to economic downturns.",
                "Integration execution: the Hulu + Live TV combination must deliver technology and cost synergies on schedule; large media integrations often do not.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Two consecutive quarters of net subscriber declines in the combined entity would indicate the product thesis is failing.",
                "Failure to realize announced cost synergies within the guided timeframe would undermine the scale argument.",
                "A covenant breach, distressed exchange, or heavily dilutive equity raise would signal the capital structure is unworkable.",
                "Loss of a marquee sports network from the bundle for an extended period would damage the core value proposition.",
                "Advertising revenue declining year over year while the sports audience is stable would indicate a monetization problem, not a cyclical one.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", METHOD_BASE),
        ]),
    ],
)

# ---------------------------------------------------------------- TIGR
tigr = dict(
    ticker="TIGR", company="UP Fintech Holding Ltd (Tiger Brokers)", verdict="BUY",
    target="$13.00", price="$4.16", price_note=PRICE_NOTE, upside="+209%",
    sections=[
        ("Investment Thesis", [
            ("p", "Tiger Brokers is a leading online brokerage built to serve global Chinese-speaking investors, "
             "with funded accounts and client assets spread across Singapore, the United States, Australia, New "
             "Zealand, and Hong Kong. The business is a classic brokerage compounder in its economics: client "
             "acquisition costs are expensed up front while the revenue from a funded account -- commissions, "
             "margin financing interest, IPO subscription fees, and increasingly wealth-management fees -- "
             "recurs for years. At $4.16 the market prices Tiger as though the Chinese regulatory overhang on "
             "cross-border brokerage will permanently cap the franchise. Our judgment is different: the "
             "regulatory discount is real and we price it explicitly, through a 250bp country-risk premium in "
             "the discount rate and a bear case that assumes the worst regulatory outcome is realized, yet the "
             "probability-weighted math still supports a $13.00 fair value. The market is treating a risk as a "
             "certainty; we treat it as a risk."),
            ("p", "What we underwrite is the durability of the international franchise. Tiger's growth engine "
             "has been new-market client acquisition -- Singapore in particular has become a core market -- and "
             "each cohort of funded accounts seasons into higher asset balances and higher revenue per account. "
             "The company is self-clearing in the United States, which lowers marginal cost per trade and "
             "supports margin expansion as volume grows, and the product surface keeps widening: options and "
             "futures trading, IPO subscriptions, employee stock-plan administration, and fund and wealth "
             "products that raise revenue per client without proportional acquisition cost. Brokerage is a "
             "scale business with operating leverage, and Tiger is past the heavy-investment phase in its core "
             "markets."),
            ("p", "The variant perception in this note is about the multiple, not the cash flows. Chinese "
             "fintech names trade at depressed multiples because investors apply the regulatory risk to the "
             "terminal value -- effectively assuming the business is expropriated or permanently impaired. We "
             "instead put the regulatory risk where it belongs: in the discount rate and in a bear case valued "
             "at $2.78 that assumes punitive CSRC action. The base case, in which Tiger continues compounding "
             "client assets internationally under the current constrained-but-operating regulatory settlement, "
             "is worth $14.06 a share on our math; the bull case, in which regulatory clarity eventually allows "
             "a re-rating toward regional peer multiples, is worth $30.07. Weighted 25/50/25, the fair value is "
             "$13.00, implying +209% upside for investors willing to hold through headline risk."),
        ]),
        ("Business Overview", [
            ("p", "UP Fintech Holding Limited, operating as Tiger Brokers, was founded in 2014 and listed on "
             "Nasdaq in 2019. It is an online brokerage offering trading in equities, options, futures, and "
             "funds across US, Hong Kong, Singapore, and Australian markets through a mobile-first platform. "
             "Revenue comes from trading commissions, margin financing and securities lending interest, IPO "
             "subscription and employee-plan administration fees, and a growing contribution from wealth "
             "management and fund distribution. The company holds brokerage licenses in its major markets, "
             "including a self-clearing US broker-dealer, and has deliberately diversified its client base away "
             "from mainland China toward overseas Chinese-speaking investors and local clients in markets like "
             "Singapore."),
            ("p", "The regulatory context is essential. In late 2022 the China Securities Regulatory Commission "
             "stated that cross-border online brokerage conducted for domestic investors without CSRC approval "
             "was unlawful, and in 2023 Tiger and its peers were required to remediate: ceasing new mainland "
             "client onboarding and removing apps from mainland app stores. The company has since operated under "
             "this constrained settlement, growing its non-mainland client base. The stock has never recovered "
             "its pre-overhang valuation, which is precisely the opportunity -- provided the remediation "
             "settlement holds and does not escalate into punitive action against the existing business."),
        ]),
        ("Forward Outlook", [
            ("p", "Our forward view is that Tiger's client-asset compounding continues and that the market "
             "continues to misprice it for several years, which is fine: the return comes from the cash flows, "
             "not from multiple expansion we cannot time. We expect funded-account growth to moderate from the "
             "explosive early international expansion but to remain well above mature-brokerage rates, driven by "
             "product breadth (options, futures, IPO access) that raises conversion of registered users to "
             "funded accounts. Revenue per funded account should rise as cohorts season -- margin balances grow "
             "with client assets, and wealth-management penetration deepens. We model operating leverage from "
             "the self-clearing infrastructure and from the largely fixed technology cost base, with marketing "
             "spend remaining the main variable cost."),
            ("p", "On regulation, our judgment is that the current settlement -- no new mainland onboarding, "
             "international growth unimpeded -- is the durable state, not a waystation to either full "
             "rehabilitation or shutdown. The CSRC's objective was to stop unapproved cross-border solicitation, "
             "which the remediation achieved; there is little administrative logic in escalating against a "
             "company that complied. That said, we do not underwrite regulatory improvement: our base case "
             "assumes the overhang persists indefinitely and the multiple stays depressed, and the entire "
             "regulatory upside lives in the bull case. This asymmetry -- paying nothing for optionality on "
             "clarity while being compensated for the risk through the entry price -- is the core of the "
             "recommendation."),
            ("p", "We haircut management's growth commentary where it leans on total registered users rather "
             "than funded accounts, and where it annualizes strong quarters in Hong Kong IPO subscription fees, "
             "which are inherently lumpy. Our cash-flow forecasts assume a through-cycle trading environment, "
             "not a repeat of the elevated retail activity of recent years, and we stress the margin-financing "
             "book for credit losses in the bear case. The wealth-management and fund businesses are genuine "
             "options on higher revenue per client, but we assign them modest weight until they demonstrate "
             "sustained profitability."),
        ]),
        ("Valuation", [
            ("p", "We value Tiger on a probability-weighted scenario DCF with an explicit 250bp China "
             "country-risk premium added to the discount rate in all scenarios, and with regional -- not US -- "
             "brokerage peers as the multiple benchmark. The bear case ($2.78) is the regulatory realization "
             "case: punitive CSRC action that impairs the existing client base, forces costly restructuring, "
             "and permanently elevates the cost of doing business. It sits well below the $4.16 share price, as "
             "a genuine bear case must. The base case ($14.06) assumes the current regulatory settlement holds, "
             "international funded accounts compound, and operating leverage flows through to free cash flow. "
             "The bull case ($30.07) assumes sustained high client growth plus eventual regulatory clarity that "
             "allows the shares to re-rate toward regional peer multiples."),
            ("table", (["Scenario", "Key assumption", "Fair value per share"],
                       [["Bear -- regulatory realization", "Punitive CSRC action; impaired client base", "$2.78"],
                        ["Base -- settlement holds", "International compounding; operating leverage", "$14.06"],
                        ["Bull -- clarity + re-rating", "High growth; multiple toward regional peers", "$30.07"],
                        ["Probability-weighted (25/50/25)", "Country-risk premium in all scenarios", "$13.00"]])),
            ("p", "Our $13.00 target equals the probability-weighted fair value and implies +209% upside from "
             "$4.16. The valuation explicitly prices the China risk rather than pretending it away: the 250bp "
             "premium and the $2.78 bear case are doing the work that a depressed multiple does in the market's "
             "pricing, but they do it transparently and only where the risk actually lives."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "CSRC escalation: punitive action beyond the current remediation settlement is the central risk and is modeled in the $2.78 bear case.",
                "VIE structure: the variable-interest-entity structure faces structural legal risk under Chinese law; an adverse ruling could impair the equity.",
                "Chinese market downturn: a prolonged decline in Chinese equities would reduce trading activity and margin balances among the core client base.",
                "Competition: Futu and other regional brokers compete aggressively on pricing and product; commission compression is a secular pressure.",
                "Credit risk: the margin-financing book exposes the company to client defaults in sharp market dislocations.",
                "Cybersecurity and operational risk: a trading-platform outage or data breach would damage trust in a trust-based business.",
                "Geopolitical risk: US-China tensions could affect the Nasdaq listing or cross-border operations.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Any CSRC action materially beyond the current settlement -- fines scaled to punish rather than remediate, or restrictions on the existing client base.",
                "Two consecutive quarters of declining funded accounts in the international business, indicating the growth engine has stalled.",
                "Evidence of VIE-structure challenge or forced restructuring of the corporate form.",
                "Sustained net interest margin compression in the margin-financing book indicating credit stress rather than competition.",
                "A dilutive equity raise at depressed prices, signaling management lacks confidence in self-funded growth.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", METHOD_BASE + METHOD_INTL + " For Chinese businesses we apply a 250bp country-risk premium to the discount rate in every scenario."),
        ]),
    ],
)

# ---------------------------------------------------------------- JD
jd = dict(
    ticker="JD", company="JD.com, Inc.", verdict="BUY",
    target="$55.00", price="$25.78", price_note=PRICE_NOTE, upside="+115%",
    sections=[
        ("Investment Thesis", [
            ("p", "JD.com is China's most logistics-moated retailer: a direct-sales (1P) e-commerce business "
             "built on a proprietary nationwide fulfillment network that delivers same-day and next-day at a "
             "scale no competitor has replicated. The investment case is straightforward and, in our judgment, "
             "underappreciated: JD's moat is physical -- warehouses, delivery stations, and a supply chain that "
             "took two decades and enormous capital to build -- and physical moats do not erode the way digital "
             "ones do. At $25.78 the shares trade as though Chinese consumption is in permanent decline and JD "
             "is a melting legacy retailer. We see a business generating prodigious operating cash flow, "
             "returning capital through buybacks, and priced at a multiple that assumes the bear case on China "
             "as the permanent state of the world."),
            ("p", "Our judgment on the forward trajectory centers on two underappreciated drivers. First, JD's "
             "supply-chain capability is being extended into new categories of demand -- instant retail and "
             "on-demand delivery, where JD's fulfillment density is a genuine structural advantage over "
             "marketplace-only competitors. The economics of delivering in under an hour favor the operator that "
             "already has inventory positioned within kilometers of the customer; that is JD. Second, the "
             "1P model gives JD a quality and authenticity guarantee that matters more, not less, as Chinese "
             "consumers become more discerning -- counterfeit and quality concerns structurally favor the "
             "retailer that takes title to the goods it sells. These are durable advantages compounding quietly "
             "while the market debates macro headlines."),
            ("p", "We price the China risk explicitly rather than embedding it in pessimism: a 250bp "
             "country-risk premium in the discount rate, regional peer benchmarking, and a bear case at $35.50 "
             "that assumes a prolonged consumption downturn and continued competitive intensity. Even so, the "
             "probability-weighted math supports a $55.00 target, +115% above the current price. The base case "
             "($50.67) requires nothing heroic -- mid-single-digit revenue growth, stable 1P margins, and "
             "continued capital returns. The bull case ($93.16) assumes consumption normalization plus "
             "successful scaling of instant retail. This is a bet that China's largest quality retailer, bought "
             "at a distressed multiple with the sovereign risk transparently priced, compounds through the "
             "cycle."),
        ]),
        ("Business Overview", [
            ("p", "JD.com, founded in 2004 by Liu Qiangdong (Richard Liu) and listed on Nasdaq in 2014 (with a "
             "Hong Kong secondary listing), is China's largest direct online retailer by revenue. The core is "
             "the 1P retail business -- JD buys inventory and sells it directly, guaranteeing authenticity -- "
             "complemented by a third-party marketplace, and powered by JD Logistics, the integrated supply "
             "chain and fulfillment arm with the country's most extensive self-operated warehouse and delivery "
             "network. The group also includes JD Health and JD Industrials. Revenue is diversified across "
             "electronics, home appliances, general merchandise, and fast-moving consumer goods, with a "
             "customer base of several hundred million annual active users skewed toward quality-conscious "
             "urban consumers."),
            ("p", "The business model differs fundamentally from marketplace peers: JD accepts lower gross "
             "margins on 1P sales in exchange for control over pricing, fulfillment speed, and authenticity, "
             "and monetizes the infrastructure through scale, advertising and logistics services sold to third "
             "parties. This capital intensity was long criticized; it is now the moat. Replicating JD's "
             "fulfillment density would require a competitor to spend tens of billions of yuan and a decade of "
             "operating losses -- a check no rational entrant writes against an incumbent already earning "
             "returns on the installed base."),
        ]),
        ("Forward Outlook", [
            ("p", "Our forward view is that JD enters a harvest phase on its logistics investments while "
             "planting the next growth driver in instant retail. We expect the core 1P business to grow "
             "roughly in line with a normalizing Chinese consumption environment -- not the boom years, but a "
             "durable mid-single-digit trajectory -- with margin expansion coming from scale, advertising "
             "attach, and supply-chain efficiency rather than from price increases. Management's commentary on "
             "margin targets is tested against the reality of competition from Pinduoduo and Alibaba; we "
             "haircut the most optimistic margin guidance and assume JD continues to invest a portion of gross "
             "profit back into price competitiveness, which is the correct long-run strategy even if it "
             "frustrates near-term margin expansion."),
            ("p", "Instant retail and on-demand delivery is the initiative we watch most closely, and our "
             "judgment is more constructive than the market's. Skeptics see a costly subsidy war with Meituan; "
             "we see JD deploying an existing asset -- inventory positioned near customers -- into a use case "
             "with structurally better unit economics for JD than for a pure delivery platform that must build "
             "supply from scratch. We model this business reaching contribution-positive on a longer timeline "
             "than management suggests, with meaningful investment drag in the early years, but we assign real "
             "terminal value to a scaled instant-retail franchise because the logistics advantage is genuine "
             "and durable."),
            ("p", "Capital allocation is a quiet pillar of the thesis. JD has been repurchasing shares "
             "aggressively, and at current prices each retired share is retired at a multiple of earnings that "
             "makes the buyback one of the highest-return investments available to the company. We expect "
             "buybacks to continue and to be a material contributor to per-share value compounding. The "
             "dividend, while modest, signals the transition from pure growth to a balanced return profile. "
             "Our bear case assumes consumption stays soft, competition stays intense, and instant retail burns "
             "cash longer than expected -- and still values the shares at $35.50, 38% above today's price, "
             "which tells you how much pessimism is already in the quote."),
        ]),
        ("Valuation", [
            ("p", "We value JD on a probability-weighted scenario DCF with a 250bp China country-risk premium "
             "in the discount rate in all scenarios, benchmarked against regional peers facing similar risks. "
             "The bear case ($35.50) assumes prolonged soft consumption, sustained competitive intensity from "
             "Pinduoduo and Alibaba, and a longer, costlier ramp in instant retail. The base case ($50.67) "
             "assumes mid-single-digit revenue growth, stable 1P economics with gradual margin expansion from "
             "scale and advertising, and continued share repurchases. The bull case ($93.16) assumes "
             "consumption normalization, successful scaling of instant retail into a profitable franchise, and "
             "a re-rating as the market recognizes the durability of the logistics moat."),
            ("table", (["Scenario", "Key assumption", "Fair value per share"],
                       [["Bear -- prolonged softness", "Weak consumption; costly instant-retail ramp", "$35.50"],
                        ["Base -- normalization", "Mid-single-digit growth; buybacks continue", "$50.67"],
                        ["Bull -- moat recognized", "Consumption recovery; instant retail scales", "$93.16"],
                        ["Probability-weighted (25/50/25)", "Country-risk premium in all scenarios", "$57.50"]])),
            ("p", "The probability-weighted value is $57.50; our $55.00 target applies a modest haircut to "
             "reflect the wide outcome range in Chinese equities, and still implies +115% upside from $25.78. "
             "Note that even the bear case sits 38% above the current price -- the market is pricing an outcome "
             "worse than our genuinely adverse scenario, which is the definition of a mispriced risk premium."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Chinese consumption: a deeper or longer downturn than our bear case would impair revenue growth and margins.",
                "Competition: Pinduoduo, Alibaba, and Meituan (in instant retail) compete aggressively on price; sustained price wars compress 1P margins.",
                "VIE structure: structural legal risk under Chinese law applies to the ADR/equity structure.",
                "Regulatory intervention: platform-economy regulation has eased but could return; data, labor, and antitrust rules remain live risks.",
                "Instant-retail losses: the on-demand delivery push could burn more cash for longer than modeled if subsidy competition intensifies.",
                "Geopolitical risk: US-China tensions, including listing and audit-compliance overhangs, can compress multiples regardless of fundamentals.",
                "Founder overhang: governance perception around the founder remains a discount factor for some investors.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Two consecutive quarters of declining annual active users would indicate share loss beyond cyclical softness.",
                "Sustained 1P gross-margin erosion not explained by deliberate price investment would signal structural pricing-power loss.",
                "A major regulatory action targeting JD specifically, or a VIE-structure challenge.",
                "Abandonment or sharp curtailment of the buyback program while the shares remain depressed, signaling capital-allocation drift.",
                "Evidence that the logistics network is being outbuilt or out-executed by a competitor at lower cost.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", METHOD_BASE + METHOD_INTL + " For Chinese businesses we apply a 250bp country-risk premium to the discount rate in every scenario."),
        ]),
    ],
)

# ---------------------------------------------------------------- WYNN
wynn = dict(
    ticker="WYNN", company="Wynn Resorts, Ltd.", verdict="BUY",
    target="$153.00", price="$75.88", price_note=PRICE_NOTE, upside="+102%",
    sections=[
        ("Investment Thesis", [
            ("p", "Wynn Resorts owns and operates the highest-quality luxury integrated resorts in the two "
             "largest gaming markets in the world -- Las Vegas and Macau -- plus Encore Boston Harbor, and it "
             "is building the first integrated resort in the United Arab Emirates. The investment case has two "
             "parts, and both are about cash flow inflection. First, the multi-year capital-expenditure wall -- "
             "the UAE resort at Wynn Al Marjan Island, the Encore Boston Harbor Enclave expansion, and the "
             "Macau reinvestment cycle -- is ending. As growth capex rolls off, free cash flow to equity "
             "inflects violently: roughly $110 million in 2027, $417 million in 2028, $1,011 million in 2029, "
             "and then $1.0 to $2.3 billion annually. Markets are poor at pricing capex-to-cash-flow inflections "
             "in leveraged companies; the equity is valued on today's encumbered cash flow rather than on the "
             "unencumbered cash flow the asset base will produce."),
            ("p", "Second, the UAE resort is a genuine growth asset that the market treats as an option with "
             "uncertain value. Our judgment is more constructive: Wynn Al Marjan Island will be the first "
             "licensed integrated gaming resort in the UAE, in a market with enormous high-end tourism demand "
             "and no competing supply, operated by the company with the best luxury resort execution record in "
             "the industry. We haircut management's contribution guidance substantially -- new-market ramp "
             "assumptions in gaming are chronically optimistic -- and the project still contributes meaningfully "
             "to our base case. The market appears to assign it roughly zero; we assign it the haircut value "
             "of a best-in-class operator opening a monopoly asset."),
            ("p", "The Macau business, held through the separately listed Wynn Macau Ltd. with minority leakage "
             "to public holders, continues to compound on premium mass and direct VIP mix shift, and Las Vegas "
             "remains a high-margin cash generator with pricing power in luxury. Leverage is the real risk and "
             "we model it honestly: the bear case at $52.08 assumes a delayed UAE opening combined with "
             "refinancing stress, and it sits well below the $75.88 share price. But the base case at $140.13 "
             "requires only that the capex wall ends on schedule and the existing assets perform as they have. "
             "Our $153.00 target implies +102% upside on a probability-weighted basis, driven by the arithmetic "
             "of deleveraging: as debt is repaid from inflecting free cash flow, equity value accretes "
             "disproportionately. With 102.97 million diluted shares, each turn of deleveraging is worth "
             "roughly $15 a share in equity value."),
        ]),
        ("Business Overview", [
            ("p", "Wynn Resorts, founded by Steve Wynn and led today by CEO Craig Billings, develops and "
             "operates luxury integrated resorts -- casino gaming combined with high-end hotels, restaurants, "
             "retail, and entertainment. The portfolio comprises Wynn Las Vegas and Encore Las Vegas on the "
             "Strip, Encore Boston Harbor in Massachusetts (opened 2019), and in Macau, Wynn Macau and Wynn "
             "Palace in Cotai, held through the Hong Kong-listed subsidiary Wynn Macau Ltd., of which Wynn "
             "Resorts owns approximately 72%, with the balance representing minority leakage from the parent "
             "shareholder's perspective. The development pipeline centers on Wynn Al Marjan Island in Ras Al "
             "Khaimah, UAE -- a multi-billion-dollar integrated resort under construction -- and the Enclave "
             "expansion project at Encore Boston Harbor."),
            ("p", "The business model is high-fixed-cost, high-operating-leverage luxury hospitality: EBITDA "
             "margins in the 30-40% range at the property level when demand is healthy, with gaming -- "
             "particularly premium mass table play in Macau and high-end slot and table play in Las Vegas -- "
             "carrying the highest margins. Capital intensity is episodic but enormous: integrated resorts cost "
             "billions to build, which is why the end of the current investment cycle matters so much to the "
             "equity. The company has historically returned capital through dividends, suspended and reinstated "
             "across cycles, and the forward story is deleveraging first, distributions second."),
        ]),
        ("Forward Outlook", [
            ("p", "Our forward view is organized around the construction timeline. Wynn Al Marjan Island is "
             "expected to open in 2027 as the UAE's first integrated gaming resort, licensed under the UAE's "
             "new commercial gaming regulatory framework. Our judgment: the demand side of this asset is "
             "underappreciated and the ramp side is overpromised, and we model it accordingly -- a slower "
             "ramp than management guidance, haircut contributions in the early years, but a large stabilized "
             "contribution because a luxury gaming monopoly in the Gulf has no natural demand ceiling in its "
             "first decade. Regulatory risk in a first-of-its-kind jurisdiction is real, but the licensing "
             "framework is established and construction is advanced; the remaining risk is timing, not "
             "existence, which is why our bear case delays the opening rather than canceling the project."),
            ("p", "In Macau, we expect continued mix improvement toward premium mass -- the highest-margin "
             "segment -- as Wynn's luxury positioning captures the secular shift away from junket VIP. Market "
             "share in Macau is a knife fight among six operators, but Wynn's product is consistently the "
             "best-positioned for the premium customer, and we expect the Macau assets to grow EBITDA at a "
             "healthy clip with minimal incremental capital now that the reinvestment cycle is largely complete. "
             "Las Vegas is the stabilizer: high-margin, pricing-power luxury with convention and leisure demand "
             "that has proven resilient, and we model steady performance rather than growth heroics. Encore "
             "Boston Harbor's Enclave expansion adds capacity in a supply-constrained regional market."),
            ("p", "The financial trajectory is the heart of the note. With growth capex ending, free cash flow "
             "to equity inflects from roughly $110 million in 2027 to $417 million in 2028 to $1,011 million in "
             "2029, then $1.0 to $2.3 billion annually -- and our forecasts haircut project contributions "
             "relative to management guidance at every step. That cash flow goes first to debt reduction: "
             "Wynn's leverage, incurred to fund the development pipeline, must come down before distributions "
             "can resume at scale. We model refinancing of near-term maturities at rates reflecting the "
             "company's leveraged profile, and we stress this in the bear case, where refinancing stress "
             "combined with a delayed UAE opening produces the $52.08 value. In the base case, deleveraging "
             "proceeds mechanically and the equity -- all 102.97 million diluted shares of it -- captures the "
             "full benefit of the unencumbering asset base."),
        ]),
        ("Valuation", [
            ("p", "We value Wynn on a scenario DCF of free cash flow to equity, which is the correct lens for a "
             "leveraged company approaching a capex inflection: enterprise-value approaches obscure the equity "
             "accretion from deleveraging. Project-level contributions are haircut versus management guidance "
             "in every scenario. The bear case ($52.08, 14.5% discount rate, 1.0% terminal growth) assumes the "
             "UAE opening is delayed, refinancing comes at punitive terms, and Macau disappoints -- a genuinely "
             "adverse outcome well below the $75.88 share price. The base case ($140.13, 12.0% discount, 2.0% "
             "terminal growth) assumes the capex wall ends on schedule, the UAE ramps on our haircut timeline, "
             "and the existing assets perform. The bull case ($277.74, 10.5% discount, 2.5% terminal growth) "
             "assumes the UAE becomes the highest-returning asset in the portfolio and Macau premium mass "
             "exceeds expectations."),
            ("table", (["Scenario", "Discount rate", "Terminal growth", "Fair value per share"],
                       [["Bear -- delayed UAE, refinancing stress", "14.5%", "1.0%", "$52.08"],
                        ["Base -- capex wall ends on schedule", "12.0%", "2.0%", "$140.13"],
                        ["Bull -- UAE exceeds; Macau outperforms", "10.5%", "2.5%", "$277.74"],
                        ["Probability-weighted (25/50/25)", "--", "--", "$152.52"]])),
            ("p", "Our $153.00 target rounds the probability-weighted fair value of $152.52 and implies +102% "
             "upside. The valuation turns on the FCFE inflection -- approximately $110 million in 2027, $417 "
             "million in 2028, $1,011 million in 2029, then $1.0 to $2.3 billion per year -- and on the "
             "mechanics of deleveraging, which accrete disproportionately to equity. Terminal value is held to "
             "2.0% growth on normalized margins in the base case, below the company's historical peak "
             "profitability."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "UAE execution and timing: construction delays or a slower-than-modeled ramp would defer the cash-flow inflection the thesis depends on.",
                "Refinancing risk: leverage is elevated; punitive refinancing terms would divert cash flow from deleveraging to interest.",
                "Macau regulatory and concession risk: license conditions, table allocations, and government policy can change the earnings power of the Macau assets.",
                "Luxury cyclicality: Wynn's premium positioning amplifies both upturns and downturns; a recession would hit high-end gaming and hospitality disproportionately.",
                "Construction cost overruns: large integrated-resort projects routinely exceed budgets; further overruns extend the capex wall.",
                "Minority leakage: the Wynn Macau Ltd. minority means parent shareholders capture only ~72% of Macau economics.",
                "Geopolitical risk: US-China tensions can affect Macau visitation and sentiment toward US operators in Macau.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "A delay of the Wynn Al Marjan Island opening beyond 2028, or material curtailment of the project's scope.",
                "Refinancing executed at distressed terms, or a covenant waiver that signals lender concern.",
                "Sustained loss of premium-mass market share in Macau to competitors, indicating product or execution slippage.",
                "Growth capex guidance raised materially again, pushing the free-cash-flow inflection further out.",
                "A dividend-funded or debt-funded acquisition that re-levers the balance sheet before deleveraging is complete.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", "Our valuation is a probability-weighted scenario DCF of free cash flow to equity, weighted "
             "25% / 50% / 25% across bear, base, and bull cases over an explicit 10-year horizon. Because "
             "Wynn is a leveraged company approaching a capital-expenditure inflection, scenario-specific "
             "discount rates reflect the capital structure: 12.0% in the base case, 14.5% in the bear case "
             "(+250bp for refinancing stress), 10.5% in the bull case. Terminal growth is capped at 2.0% in "
             "the base case on normalized mid-cycle margins -- never peak margins -- and any terminal value "
             "exceeding 70% of enterprise value is haircut and disclosed. The bear case is genuinely adverse "
             "and sits well below the current price. Management's project-contribution guidance is haircut in "
             "every scenario; it is independently tested, never accepted at face value."),
        ]),
    ],
)

# ---------------------------------------------------------------- ADBE
adbe = dict(
    ticker="ADBE", company="Adobe Inc.", verdict="BUY",
    target="$465.00", price="$237.69", price_note=PRICE_NOTE, upside="+96%",
    sections=[
        ("Investment Thesis", [
            ("p", "Adobe is being priced as an AI loser, and our judgment is that this is wrong. The market's "
             "fear is straightforward: generative AI commoditizes content creation, eroding the need for "
             "Creative Cloud subscriptions. Our view is that this misunderstands both what Adobe sells and how "
             "creative work actually gets done. Adobe does not sell the ability to make an image; it sells the "
             "professional workflow in which images are made, revised, versioned, rights-managed, and published "
             "across teams and enterprises. Generative AI makes more content get made, not less -- and every "
             "additional asset created inside an enterprise still needs to flow through editing, collaboration, "
             "digital asset management, and publishing pipelines where Adobe is the system of record. AI is a "
             "demand accelerant for Adobe's workflow products disguised as a threat to its tools."),
            ("p", "The financial profile is what makes this a BUY rather than an interesting debate. Roughly "
             "97% of revenue is subscription-based, gross margins sit in the high 80s, and free-cash-flow "
             "margins are among the best in large-cap software -- this is a cash-compounding machine with "
             "net revenue retention that reflects genuine enterprise entrenchment, not contract lock-in. At "
             "$237.69 the shares trade at a multiple that implies structural decline; we model durable "
             "double-digit earnings compounding driven by seat expansion in Document Cloud, ARPU expansion "
             "from AI-priced tiers in Creative Cloud, and the continued scaling of Experience Cloud into the "
             "enterprise marketing stack. Our $465.00 target implies +96% upside and requires only that Adobe "
             "remain what it observably is -- the workflow standard -- rather than becoming something new."),
            ("p", "We have a specific view on AI monetization that differs from consensus. Skeptics note that "
             "Adobe's Firefly generative credits are modestly priced and that competition from Figma, Canva, "
             "and frontier AI labs is intense. We agree on the competitive intensity and we haircut "
             "management's AI-revenue commentary accordingly. But we judge that Adobe's distribution -- hundreds "
             "of millions of users, deep enterprise relationships, and a trusted brand on commercial safety and "
             "IP indemnification -- is the durable advantage in an AI world where enterprises are terrified of "
             "copyright liability and data leakage. Firefly's training on licensed and public-domain content, "
             "with IP indemnification for enterprise customers, is not a footnote; for risk-averse enterprises "
             "it is the reason to standardize on Adobe rather than on a frontier model with unclear provenance."),
        ]),
        ("Business Overview", [
            ("p", "Adobe Inc., led by CEO Shantanu Narayen, operates three segments. Digital Media -- Creative "
             "Cloud (Photoshop, Illustrator, Premiere Pro, and dozens of professional tools) and Document Cloud "
             "(Acrobat, PDF services) -- is the core profit engine, sold overwhelmingly by subscription. "
             "Digital Experience (Experience Cloud) provides marketing, analytics, content management, and "
             "commerce software to enterprises. A small publishing segment rounds out the business. "
             "Approximately 97% of total revenue is subscription-based, producing the predictability and "
             "cash conversion -- free cash flow routinely exceeding 35% of revenue -- that define the "
             "investment profile."),
            ("p", "Adobe's moat is workflow entrenchment compounded by network effects in creative talent: "
             "professionals learn Adobe tools, employers hire for Adobe skills, files and collaboration live "
             "in Adobe formats and clouds, and switching costs rise with team size. The company has layered "
             "generative AI across the portfolio -- Firefly image and video generation, AI Assistant in "
             "Acrobat, generative features in Photoshop and Express, and GenStudio for enterprise content "
             "supply chains -- monetized through credit-based add-ons and AI-priced tiers. Competition spans "
             "Figma and Canva in design, point AI tools from startups and frontier labs, and Microsoft and "
             "Salesforce in the experience layer."),
        ]),
        ("Forward Outlook", [
            ("p", "Our forward view is that Adobe's next five years look more like its last ten than the market "
             "expects. We forecast Creative Cloud to keep growing through a combination of modest seat growth "
             "and steady ARPU expansion as AI features move into higher-priced tiers -- not because customers "
             "pay more for the same product, but because generative workflows measurably raise output per "
             "creative professional, which is the oldest justification for a price increase in software. "
             "Document Cloud, often overlooked, is in our judgment the steadiest compounder in the portfolio: "
             "PDF workflows are deeply embedded in enterprise processes, AI Assistant adds a genuine new "
             "capability (conversational document understanding), and seat expansion in knowledge-work "
             "enterprises continues. Experience Cloud grows more slowly but at high incremental margin as the "
             "enterprise marketing stack consolidates."),
            ("p", "On competition, we are clear-eyed but not alarmed. Figma's strength in collaborative product "
             "design does not displace Photoshop in image work or Premiere in video; Canva expands the market "
             "downward more than it takes share upward; and frontier AI models are complements to Adobe's "
             "workflow more than substitutes for it, because raw generation is a feature while Adobe sells the "
             "pipeline. The genuine competitive risk is in net-new creative workflows that never touch Adobe -- "
             "AI-native video or design studios built entirely on new stacks -- and we model modest share "
             "leakage at the edges rather than core displacement. We haircut management's AI-attributed revenue "
             "figures, which blend genuine AI monetization with reclassified existing spend, and we underwrite "
             "only the AI revenue we can tie to observable pricing actions."),
            ("p", "Capital allocation is exemplary and we expect it to continue: massive free cash flow funds "
             "aggressive share repurchases that have steadily reduced the share count, and the balance sheet "
             "carries net cash, giving Adobe full strategic optionality. We do not model a large acquisition; "
             "Adobe's history suggests discipline after the Figma episode, and the forward story does not need "
             "M&A. What it needs is continued execution on the AI product cycle and evidence -- in net new ARR "
             "and Digital Media growth reacceleration -- that the workflow standard is strengthening, not "
             "eroding. Our base case assumes exactly that: no heroics, just the compounding of a subscription "
             "franchise with 97% recurring revenue and best-in-class margins."),
        ]),
        ("Valuation", [
            ("p", "We value Adobe on a probability-weighted scenario DCF over a 10-year horizon, with a 10% "
             "base discount rate reflecting the stability of the subscription franchise, 250bp added in the "
             "bear case and 150bp subtracted in the bull case, and terminal growth capped at 2.5% on "
             "normalized margins. The bear case is genuinely adverse and sits below the $237.69 share price: "
             "AI-native competitors displace Adobe in net-new creative workflows, seat growth stalls, pricing "
             "power erodes, and the multiple compresses to reflect a structurally challenged franchise. The "
             "base case assumes Creative Cloud and Document Cloud continue compounding at durable rates, AI "
             "tiers drive ARPU expansion, Experience Cloud scales steadily, and free-cash-flow margins remain "
             "elite -- the continuation of the observable business. The bull case assumes Adobe emerges as "
             "the enterprise AI content-supply-chain standard, with GenStudio and Firefly enterprise adoption "
             "accelerating growth back toward historical highs."),
            ("p", "Blending these scenarios at 25% / 50% / 25% yields a probability-weighted fair value of "
             "$465.00, which is our target, implying +96% upside. The valuation rests on the durability of "
             "subscription cash flows -- roughly 97% of revenue recurring -- rather than on heroic AI "
             "monetization assumptions; our AI revenue forecasts are haircut relative to management commentary "
             "throughout. Terminal value is held within our 70%-of-enterprise-value guardrail and disclosed."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "AI disruption: AI-native creative tools could displace Adobe in net-new workflows faster than modeled.",
                "Competitive intensity: Figma, Canva, and frontier AI labs compete for creative mindshare and talent pipelines.",
                "Enterprise IT budgets: a spending downturn would slow Experience Cloud and seat expansion.",
                "Pricing power limits: repeated price increases could accelerate churn or invite regulatory scrutiny.",
                "Copyright and IP exposure: generative-AI training-data litigation remains an industry-wide overhang despite Adobe's licensed-data approach.",
                "Multiple compression: software multiples can contract sharply on growth scares regardless of cash-flow durability.",
                "Execution risk on AI monetization: if AI features fail to convert to paid tiers, the growth reacceleration thesis weakens.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Two consecutive quarters of declining Digital Media net new ARR would indicate the core franchise is eroding.",
                "A sustained drop in gross retention in Creative Cloud, signaling genuine displacement rather than cyclical softness.",
                "Observable enterprise standardization on a competing AI content platform at Adobe's expense in large deals.",
                "Free-cash-flow margin compression not explained by deliberate investment, indicating pricing-power loss.",
                "A large dilutive acquisition that signals management lacks confidence in organic growth.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", METHOD_BASE),
        ]),
    ],
)

# ---------------------------------------------------------------- INTU
intu = dict(
    ticker="INTU", company="Intuit Inc.", verdict="BUY",
    target="$535.00", price="$281.08", price_note=PRICE_NOTE, upside="+90%",
    sections=[
        ("Investment Thesis", [
            ("p", "Intuit owns four franchises that are each the default product in their category: TurboTax in "
             "consumer tax preparation, QuickBooks in small-business accounting, Credit Karma in consumer "
             "financial insight, and Mailchimp in small-business marketing. Defaults compound: each tax season "
             "and each business formation cohort refreshes the top of the funnel, retention is structurally "
             "high because switching accounting or tax software is painful, and the data each product generates "
             "makes the others better. At $281.08 the market prices Intuit as a mature tax-and-accounting "
             "utility facing AI disruption. Our judgment is that Intuit is an AI beneficiary in the same way "
             "Adobe is: AI raises the value of the workflow platform it is embedded in, and Intuit's platform "
             "sits on the most sensitive financial data of tens of millions of consumers and small businesses -- "
             "data that cannot be casually moved to a chatbot."),
            ("p", "The forward earnings power is underappreciated in two places. First, the mid-market: "
             "QuickBooks Advanced and the enterprise-ish offerings moving upmarket capture businesses "
             "graduating from small-business plans, at multiples of the ARPU, with Intuit's brand trust doing "
             "the selling. Second, AI agents: Intuit Assist and the agentic workflows being built across tax, "
             "bookkeeping, and marketing automate the labor that small businesses currently buy from "
             "accountants and agencies -- and Intuit can price a share of that labor value, which is an order "
             "of magnitude larger than software ARPU. We haircut management's AI commentary heavily, but even "
             "our haircut view of agentic monetization adds a meaningful growth vector in the outer years "
             "of our forecast."),
            ("p", "Credit Karma is the cyclical swing factor the market overweights. It is genuinely sensitive "
             "to the credit cycle -- loan and card origination volumes drive its revenue -- but the strategic "
             "value is the data and the member base, which feed TurboTax and QuickBooks acquisition at low "
             "marginal cost. Our base case assumes a normalized credit environment, not a boom, and still "
             "supports the valuation. Mailchimp, the perennial disappointment since acquisition, is modeled "
             "conservatively: we underwrite stabilization and modest growth, not the turnaround story, so any "
             "genuine improvement is upside. Our $535.00 target implies +90% upside on probability-weighted "
             "cash flows that require Intuit to remain the default in its categories -- which, on the evidence "
             "of retention data, it is."),
        ]),
        ("Business Overview", [
            ("p", "Intuit Inc., led by CEO Sasan Goodarzi, provides financial management software to consumers, "
             "small businesses, and the self-employed. The Small Business and Self-Employed segment (QuickBooks "
             "accounting, payroll, payments, and Mailchimp marketing) is the largest growth engine; the "
             "Consumer segment (TurboTax, Credit Karma) delivers seasonal but highly profitable tax and "
             "financial-insight revenue. The platform strategy -- one Intuit account, shared data, AI-driven "
             "insights across products -- is designed to raise retention and cross-sell: a TurboTax user "
             "becomes a Credit Karma member, a QuickBooks customer adds payroll and payments."),
            ("p", "The moat is data plus switching costs plus brand trust in financial matters. Small businesses "
             "run their books on QuickBooks for years; migrating historical financial data is operationally "
             "risky, which produces the high retention that underwrites the valuation. Intuit's AI strategy, "
             "branded Intuit Assist, embeds generative AI across the product line -- tax explanations, "
             "bookkeeping automation, marketing content -- and the company is building agentic experiences that "
             "complete multi-step financial tasks. Competition includes H&R Block and free-file options in tax, "
             "Xero and Sage in accounting, and a long tail of fintech point solutions; none match Intuit's "
             "cross-product data advantage."),
        ]),
        ("Forward Outlook", [
            ("p", "Our forward view centers on durable mid-teens earnings compounding driven by three levers. "
             "First, pricing power in the core: TurboTax and QuickBooks have raised prices consistently with "
             "minimal churn impact, reflecting the switching-cost moat, and we model continued ARPU expansion "
             "as AI features tier into higher-priced plans. Second, the move upmarket: mid-market businesses "
             "adopting QuickBooks Advanced and Intuit's expanding service attach (payroll, payments, lending) "
             "raise revenue per customer severalfold versus the small-business base. Third, operating leverage: "
             "the platform is built, the brand is established, and incremental revenue carries high margins -- "
             "we expect margins to expand as AI-driven automation reduces service delivery costs."),
            ("p", "On AI disruption -- the market's central fear -- our judgment is that Intuit's position "
             "strengthens. Tax preparation and bookkeeping look automatable in the abstract, but in practice "
             "they require trusted handling of regulated, high-stakes financial data with audit trails and "
             "accuracy guarantees. A general-purpose AI agent cannot offer the compliance accountability that "
             "Intuit provides, and Intuit's agents operate on the customer's actual financial history, which "
             "no competitor can replicate without the data. We model AI as ARPU-accretive (customers pay for "
             "automation that replaces more expensive human labor) rather than seat-destructive, while "
             "acknowledging this is the key forecast risk: if AI commoditizes tax and bookkeeping faster than "
             "Intuit can reprice, the bear case -- which sits below $281.08 -- is the outcome."),
            ("p", "We are deliberately conservative on the two problem children. Credit Karma is modeled on a "
             "through-cycle credit environment with no heroic recovery in origination volumes; the member base "
             "and data value are the underwrite, not the revenue snapback. Mailchimp is modeled for "
             "stabilization, with growth resuming modestly -- we do not underwrite management's turnaround "
             "targets. Capital allocation remains shareholder-friendly: the dividend grows and buybacks offset "
             "dilution and then some, funded by free cash flow that consistently exceeds 25% of revenue. Our "
             "base case requires Intuit to keep doing what it has done for a decade -- raising prices "
             "modestly, retaining customers structurally, and compounding per-share value -- and the "
             "probability-weighted math does the rest."),
        ]),
        ("Valuation", [
            ("p", "We value Intuit on a probability-weighted scenario DCF over a 10-year horizon, with a 9% "
             "base discount rate reflecting the stability of the franchise -- this is among the most "
             "defensible moats in software -- 250bp added in the bear case and 150bp subtracted in the bull "
             "case, and terminal growth capped at 2.5% on normalized margins. The bear case is genuinely "
             "adverse and sits below the $281.08 share price: AI commoditizes tax preparation and bookkeeping "
             "faster than Intuit reprices, pricing power breaks, and Credit Karma suffers a prolonged credit "
             "contraction. The base case assumes continued ARPU expansion, mid-market penetration, steady "
             "retention, and normalized Credit Karma -- the observable Intuit, extended. The bull case assumes "
             "agentic AI monetization succeeds at scale, with Intuit capturing a share of the labor value it "
             "automates for small businesses."),
            ("p", "Blending these scenarios at 25% / 50% / 25% yields a probability-weighted fair value of "
             "$535.00, which is our target, implying +90% upside. The valuation is anchored by the "
             "recurring-revenue base across TurboTax, QuickBooks, and Credit Karma membership, and by "
             "free-cash-flow conversion that funds both growth investment and sustained capital returns. "
             "Terminal value is held within our 70%-of-enterprise-value guardrail and disclosed."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "AI disruption: faster-than-expected commoditization of tax preparation or bookkeeping would impair the core franchises.",
                "IRS Direct File and free-file expansion: government-provided free tax filing could erode TurboTax's paid funnel over time.",
                "Credit cycle: a severe credit contraction would depress Credit Karma revenue and signal broader consumer stress.",
                "Small-business formation slowdown: fewer new businesses means a thinner top-of-funnel for QuickBooks.",
                "Mailchimp underperformance: continued deterioration would force a writedown of the strategic rationale and management credibility.",
                "Regulatory scrutiny: data privacy and fintech regulation could constrain cross-product data use, dulling the platform advantage.",
                "Valuation sensitivity: the shares have historically traded at premium multiples; multiple compression on any growth scare is a real drawdown risk.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Two consecutive tax seasons of TurboTax paid-unit declines not explained by demographics would signal franchise erosion.",
                "Sustained QuickBooks subscriber churn elevation or net revenue retention decline in the small-business segment.",
                "Evidence that AI-native tax or bookkeeping products are winning Intuit's core customers at scale.",
                "A major data breach or regulatory action restricting Intuit's use of cross-product financial data.",
                "Capital allocation drift: a large dilutive acquisition or a buyback halt while the shares are depressed.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", METHOD_BASE),
        ]),
    ],
)

# ---------------------------------------------------------------- NKE
METHOD_NKE = (
    "Our valuation is a probability-weighted scenario DCF. NIKE meets our compounder-quality criteria -- "
    "more than 10 years of return on invested capital above 15% (a 14-year streak, minimum 15.8%), stable or "
    "expanding gross margins, and free-cash-flow conversion above 80%, all verified from reported history, "
    "never projected -- and therefore we use a 15-year explicit forecast horizon, an 8-8.5% base discount "
    "rate reflecting the genuinely lower risk of its predictable cash flows, and a 3.0% terminal growth cap "
    "applied to a demonstrated sustained terminal margin. Scenarios are weighted 25% / 50% / 25%; the bear "
    "case adds 250bp to the discount rate, the bull case subtracts 150bp (floor 8%). Terminal value assumes "
    "no more than 3.0% perpetual growth on normalized mid-cycle margins -- never peak margins -- and any "
    "terminal value exceeding 70% of enterprise value is haircut and disclosed. Bear cases are required to be "
    "genuinely adverse and to sit below the current price. The compounder qualification is falsifiable and "
    "revoked if NIKE records two consecutive years of ROIC below 15% or gross-margin contraction of 200bp or "
    "more. Management guidance is never accepted at face value; it is independently tested and haircut where "
    "evidence warrants."
)

nke = dict(
    ticker="NKE", company="NIKE, Inc.", verdict="BUY",
    target="$64.00", price="$33.87", price_note=PRICE_NOTE, upside="+89%",
    sections=[
        ("Investment Thesis", [
            ("p", "NIKE is the strongest brand in athletic footwear and apparel, and at $33.87 the market prices "
             "it as a structurally impaired business in permanent retreat. Our judgment is that this confuses a "
             "cyclical product and distribution reset with structural decline. NIKE's advantages -- the deepest "
             "innovation pipeline in the industry, the most powerful athlete and cultural endorsement portfolio "
             "ever assembled, and distribution scale that no challenger can replicate -- are intact; what broke "
             "was execution: an over-rotation to direct-to-consumer that alienated wholesale partners, a product "
             "cycle that leaned too heavily on retro lifestyle franchises while running innovation lagged, and "
             "inventory imbalances that forced promotional selling. These are fixable problems, and under CEO "
             "Elliott Hill the company is fixing them: reinvesting in wholesale relationships, re-centering the "
             "brand on sport, and rebuilding the running innovation pipeline."),
            ("p", "What elevates this from a turnaround speculation to a BUY is the quality of the underlying "
             "compounder. NIKE has produced return on invested capital above 15% for 14 consecutive years "
             "(minimum 15.8%), with stable-to-expanding gross margins and free-cash-flow conversion above 80% -- "
             "a record verified from reported history that meets our compounder-quality criteria outright. "
             "Businesses with this profile do not lose their economics because of a bad product cycle; they "
             "revert to them. The market is pricing the trough of the reset as the permanent state; we are "
             "pricing the demonstrated through-cycle economics, which support a $64.00 fair value on a "
             "probability-weighted basis, +89% above today's price, using an 8-8.5% discount rate that the "
             "predictability of these cash flows genuinely earns."),
            ("p", "Our variant view is on the competitive threat. The market treats the rise of On, Hoka, and "
             "other challengers as a permanent share transfer. We see it differently: challengers win by "
             "innovating in specific categories while the incumbent's innovation sleeps, and they lose their "
             "edge when the incumbent wakes up with ten times the R&D budget and fifty years of biomechanics "
             "data. NIKE's running pipeline -- the category where it ceded the most ground -- is being renewed "
             "with exactly this dynamic in mind, and early reception to the renewed performance product "
             "suggests the innovation engine is restarting. Brand heat is cyclical; innovation capacity is "
             "structural. We are underwriting the structural part."),
        ]),
        ("Business Overview", [
            ("p", "NIKE, Inc., founded in 1964 and headquartered in Beaverton, Oregon, is the world's largest "
             "athletic footwear and apparel company. The NIKE brand spans performance categories -- running, "
             "basketball, soccer, training -- and sport lifestyle; Jordan Brand is a multi-billion-dollar "
             "franchise in its own right; Converse adds a complementary lifestyle position. Revenue is "
             "geographically diversified across North America, Europe/Middle East/Africa, Greater China, and "
             "Asia Pacific/Latin America, and sold through wholesale partners and NIKE's direct channels "
             "(owned stores and digital commerce). Gross margins have historically sat in the mid-40s percent "
             "range, reflecting genuine brand pricing power in a category where most participants earn "
             "commodity returns."),
            ("p", "The economic signature of the business is exceptional capital efficiency: minimal fixed "
             "manufacturing assets (production is outsourced), working capital dominated by inventory, and "
             "returns on invested capital above 15% for 14 straight years. Free-cash-flow conversion above 80% "
             "has funded decades of dividend growth and aggressive share repurchases. The 2023-2025 period "
             "broke the pattern operationally -- excess inventory, promotional pressure, wholesale disruption, "
             "and share loss in running -- but not economically: the through-cycle margin structure and capital "
             "efficiency remain demonstrably intact, which is precisely what the compounder framework is "
             "designed to recognize."),
        ]),
        ("Forward Outlook", [
            ("p", "Our forward view is that NIKE's reset follows the classic athletic-brand recovery playbook, "
             "and we model it in three phases. Phase one, largely complete: clear excess inventory, restore "
             "full-price selling discipline, and repair wholesale partnerships -- the 'Win Now' actions that "
             "stabilize gross margin. Phase two, underway: renew the product engine around sport, with "
             "running innovation leading -- new cushioning platforms, race-day credibility re-established, and "
             "a pipeline cadence that gives wholesale partners something to sell besides retros. Phase three: "
             "brand heat returns as performance credibility compounds into lifestyle demand, the historical "
             "sequence by which NIKE has always grown. We expect revenue growth to reaccelerate as phases two "
             "and three compound, with gross margin rebuilding toward the mid-40s as promotions fade and "
             "higher-margin performance product mixes back in."),
            ("p", "Greater China deserves its own judgment. The market treats China as a permanent drag on "
             "NIKE; we see a premium Western brand in a consumption environment that remains soft but is "
             "cyclical, not structurally closed to NIKE. Local competitors have gained share, but NIKE's brand "
             "equity with Chinese athletes and young consumers remains formidable, and we model China as a "
             "gradual recovery contributor rather than a growth engine -- which means any genuine consumption "
             "rebound is upside to our numbers. We haircut management's most optimistic China commentary and "
             "assume share stabilization before share gains."),
            ("p", "Capital allocation is a quiet compounding lever we underwrite fully: the dividend has grown "
             "for over two decades, and buybacks at current prices retire shares at a multiple of through-cycle "
             "earnings that makes each repurchased share highly accretive to the compounder math. We expect "
             "NIKE to continue returning essentially all free cash flow to shareholders while funding the "
             "innovation pipeline internally -- the classic compounder capital policy. Our 15-year horizon "
             "reflects our confidence that the economics observed over the last 14 years -- ROIC above 15%, "
             "expanding gross margins, 80%+ cash conversion -- persist; and the falsification trigger is "
             "explicit: two consecutive years of ROIC below 15% or 200bp+ of gross-margin contraction revokes "
             "the compounder qualification and our valuation with it."),
        ]),
        ("Valuation", [
            ("p", "We value NIKE on a probability-weighted scenario DCF over a 15-year explicit horizon, which "
             "the company's compounder-quality record earns: 14 consecutive years of ROIC above 15% (minimum "
             "15.8%), stable-to-expanding gross margins, and free-cash-flow conversion above 80%, all verified "
             "from history. The base discount rate is 8-8.5%, reflecting the genuinely lower risk of these "
             "predictable cash flows; the bear case adds 250bp and the bull case subtracts 150bp (floor 8%). "
             "Terminal growth is capped at 3.0% on a demonstrated sustained margin -- never a peak margin -- "
             "and terminal value exceeding 70% of enterprise value would be haircut and disclosed. The bear "
             "case is genuinely adverse and sits below the $33.87 share price: the turnaround stalls, wholesale "
             "relationships do not recover, running innovation fails to resonate, and margins settle at a "
             "structurally lower level. The base case assumes the three-phase recovery plays out -- inventory "
             "discipline, product engine renewed, brand heat returning -- with gross margins rebuilding toward "
             "the mid-40s and through-cycle economics reasserting. The bull case assumes NIKE recaptures "
             "running leadership decisively and Greater China rebounds, restoring historical growth rates on "
             "the compounder economics."),
            ("p", "Blending these scenarios at 25% / 50% / 25% yields a probability-weighted fair value of "
             "$64.00, which is our target, implying +89% upside. The valuation is anchored by the verified "
             "quality record, not by turnaround hope: even our bear case preserves a portion of the historical "
             "return profile, and the compounder qualification carries an explicit falsification trigger -- two "
             "consecutive years of ROIC below 15% or 200bp+ gross-margin contraction -- that would require us "
             "to withdraw both the qualification and the valuation."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Turnaround execution: the product and wholesale reset may take longer or deliver less than modeled; brand heat is not mechanically recoverable.",
                "Competition: On, Hoka, Adidas, and domestic Chinese brands continue to take share in key categories, particularly running.",
                "Greater China: prolonged consumption softness or further share loss to local champions would impair a key growth market.",
                "Inventory and promotions: a relapse into excess inventory would restart the promotional cycle that compressed margins.",
                "Direct-to-consumer balance: miscalibrating the wholesale-versus-direct mix could re-alienate partners or strand digital investments.",
                "Input costs and tariffs: footwear manufacturing cost inflation and trade policy can pressure gross margins.",
                "Fashion risk: over-dependence on lifestyle/retro franchises exposes revenue to style cycles.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Two consecutive years of ROIC below 15% -- this revokes the compounder qualification and the valuation built on it.",
                "Gross-margin contraction of 200bp or more on a sustained basis, indicating structural pricing-power loss.",
                "Two consecutive years of revenue decline in North America wholesale, signaling the partner reset has failed.",
                "Sustained market-share loss in performance running despite the renewed innovation pipeline.",
                "A dividend cut or buyback suspension not explained by a clear external shock, signaling cash-flow stress.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", METHOD_NKE),
        ]),
    ],
)

# ---------------------------------------------------------------- TTD
ttd = dict(
    ticker="TTD", company="The Trade Desk, Inc.", verdict="BUY",
    target="$21.00", price="$11.95", price_note=PRICE_NOTE, upside="+76%",
    sections=[
        ("Investment Thesis", [
            ("p", "The Trade Desk is the leading independent demand-side platform for programmatic advertising, "
             "and independence is the entire investment thesis. The digital advertising market is bifurcating "
             "into walled gardens -- Google, Meta, Amazon -- where the platform grades its own homework, and "
             "the open internet, where advertisers need a neutral party to buy media objectively across "
             "publishers. The Trade Desk is that neutral party at scale, and its structural position improves "
             "as connected TV (CTV) -- the largest secular shift in media buying -- moves more premium video "
             "inventory into programmatic channels. At $11.95 the shares price The Trade Desk as a "
             "growth-challenged ad-tech vendor; we see the default buying platform for the open internet, with "
             "a founder-led culture and a product cycle (Kokai) that is still early in its monetization."),
            ("p", "Our judgment on the forward trajectory centers on CTV and retail media, the two highest-"
             "growth pools in programmatic. CTV advertising is migrating from direct sold deals to programmatic "
             "buying as measurement standardizes, and The Trade Desk's integrations with the major streaming "
             "platforms position it to capture a disproportionate share of that migration -- the company's "
             "CTV revenue has grown at multiples of the broader ad market for years, and we expect that "
             "outperformance to continue as linear TV dollars complete their move to streaming. Retail media "
             "networks, meanwhile, are bringing vast new pools of shopper data into the programmatic "
             "ecosystem, and The Trade Desk's data marketplace and identity offering (UID2) make it the natural "
             "pipe connecting that data to open-internet inventory."),
            ("p", "The profitability profile is what converts this from a growth story to a BUY. The Trade Desk "
             "has grown revenue at 20%+ rates for most of its public life while maintaining adjusted EBITDA "
             "margins in the 40% range and generating substantial free cash flow -- a rare combination of "
             "growth and profitability in ad tech, funded organically without serial dilution. The recent "
             "share-price weakness reflects growth deceleration fears and competitive noise from walled "
             "gardens, particularly Amazon's DSP. Our view: the deceleration is cyclical and mix-related, not "
             "structural, and the competitive moat -- objectivity, data partnerships, and a decade of "
             "agency workflow integration -- widens with scale. Our $21.00 target implies +76% upside on "
             "probability-weighted cash flows that assume The Trade Desk remains the independent standard."),
        ]),
        ("Business Overview", [
            ("p", "The Trade Desk, founded in 2009 by CEO Jeff Green and listed on Nasdaq in 2016, operates a "
             "self-service, cloud-based demand-side platform that lets advertisers and agencies buy digital ad "
             "inventory programmatically across display, video, audio, and CTV. Revenue is a percentage of "
             "advertising spend flowing through the platform (take rate), plus data and platform fees. The "
             "company does not own media -- this is the point: unlike Google's DV360 or Amazon's DSP, The "
             "Trade Desk has no incentive to steer spending toward owned inventory, which is why the world's "
             "largest advertisers and agency holding companies trust it with objective buying decisions."),
            ("p", "The product engine is Kokai, the AI-driven platform generation that embeds predictive "
             "models across media planning, audience targeting, and measurement. The identity layer, UID2 -- "
             "an open-source, privacy-conscious identifier built for the post-cookie internet -- has gained "
             "broad industry adoption and deepens The Trade Desk's data advantage as third-party cookies fade. "
             "Competition comes from walled-garden DSPs (Google DV360, Amazon), which bundle buying with owned "
             "inventory, and from smaller independent DSPs; The Trade Desk's scale, profitability, and neutrality "
             "differentiate it from both."),
        ]),
        ("Forward Outlook", [
            ("p", "Our forward view is that programmatic's share of total advertising keeps rising and The "
             "Trade Desk's share of programmatic keeps rising with it -- a double compounding that the current "
             "price does not reflect. We model revenue growth reaccelerating as the cyclical ad-spend softness "
             "passes and as CTV programmatic penetration deepens: every major streamer expanding its ad tier "
             "adds premium supply that flows disproportionately through the independent platform advertisers "
             "trust for video. Kokai's AI capabilities should drive both higher win rates and higher take rates "
             "over time, as better targeting and measurement justify premium pricing -- we haircut "
             "management's Kokai commentary but underwrite steady adoption because the product demonstrably "
             "improves return on ad spend for early users."),
            ("p", "On the competitive front, our judgment is that the walled gardens' advance helps The Trade "
             "Desk more than it hurts. As Google, Meta, and Amazon capture larger shares of digital budgets, "
             "advertisers' need for an objective measurement and buying layer across the remaining open "
             "internet intensifies -- nobody wants the referee to also own a team. Amazon's DSP growth is the "
             "most cited bear point; we acknowledge it as a real competitor in retail-media-adjacent buying but "
             "note that its structural conflict (steering spend to Amazon inventory) is exactly what drives "
             "sophisticated advertisers toward the independent alternative. UID2 adoption is the leading "
             "indicator we watch: broadening industry support for the open identifier entrenches The Trade "
             "Desk's data position regardless of cookie timelines."),
            ("p", "We model the exceptional margin structure persisting: the platform's incremental economics "
             "are software-like, and management has demonstrated disciplined investment -- growing headcount in "
             "product and go-to-market while holding the line on adjusted EBITDA margins near 40%. Free cash "
             "flow funds buybacks that offset stock compensation, and the balance sheet carries net cash. Our "
             "bear case, which sits below $11.95, assumes walled gardens successfully enclose CTV buying, "
             "programmatic growth stalls, and take-rate compression arrives -- a genuinely adverse outcome we "
             "assign 25% weight precisely because platform shifts in advertising have historically been "
             "unforgiving to losers. Our base case assumes none of that: just the continued, observable "
             "compounding of the independent leader in a growing market."),
        ]),
        ("Valuation", [
            ("p", "We value The Trade Desk on a probability-weighted scenario DCF over a 10-year horizon, with "
             "a 10% base discount rate reflecting the strong competitive position balanced against ad-market "
             "cyclicality, 250bp added in the bear case and 150bp subtracted in the bull case, and terminal "
             "growth capped at 2.5% on normalized margins. The bear case is genuinely adverse and sits below "
             "the $11.95 share price: walled gardens enclose CTV programmatic buying, growth decelerates to "
             "single digits permanently, and take rates compress under competitive pressure. The base case "
             "assumes continued 20%-area revenue growth moderating gradually, 40%-area EBITDA margins, CTV "
             "leadership maintained, and UID2 entrenching the data advantage. The bull case assumes The Trade "
             "Desk becomes the de facto operating system for open-internet advertising, with Kokai driving "
             "take-rate expansion and retail-media data flows accelerating growth above historical rates."),
            ("p", "Blending these scenarios at 25% / 50% / 25% yields a probability-weighted fair value of "
             "$21.00, which is our target, implying +76% upside. The valuation is supported by the observable "
             "combination of high growth and high margins -- a profile the market has historically re-rated "
             "once cyclical fears pass -- and by free-cash-flow generation that requires no heroic assumptions "
             "about market share beyond the continuation of current trends. Terminal value is held within our "
             "70%-of-enterprise-value guardrail and disclosed."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Walled-garden enclosure: Google, Amazon, or major streamers could restrict programmatic access to premium CTV inventory.",
                "Ad-market cyclicality: a recession would cut ad budgets quickly; The Trade Desk's growth is cyclical even if its share gains are structural.",
                "Amazon DSP competition: Amazon's growing DSP competes directly, especially in retail-media-adjacent spend.",
                "Identity disruption: adverse privacy regulation or platform policy changes could impair UID2 or data-driven targeting.",
                "Take-rate compression: large advertisers and agencies continuously negotiate; sustained compression would impair the model.",
                "Key-person risk: founder-CEO Jeff Green is central to strategy, culture, and industry relationships.",
                "Valuation sensitivity: growth-multiple compression on any deceleration scare can drive sharp drawdowns.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Two consecutive quarters of revenue growth below 15% without a clear cyclical explanation would indicate structural deceleration.",
                "Loss of a major agency holding company relationship or a marquee CTV supply partnership to a walled-garden competitor.",
                "Sustained take-rate decline indicating pricing-power erosion rather than mix effects.",
                "Regulatory action materially restricting programmatic data use or UID2 deployment.",
                "Deterioration of adjusted EBITDA margins not explained by deliberate investment, signaling a broken operating model.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", METHOD_BASE),
        ]),
    ],
)

NOTES = [fubo, tigr, jd, wynn, adbe, intu, nke, ttd]

if __name__ == "__main__":
    for n in NOTES:
        path = os.path.join(OUT, "%s-equity-research-note.pdf" % n["ticker"])
        build_note(path, n)
        print("built", path)
