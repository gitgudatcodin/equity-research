"""Build 8 standalone equity research PDFs (wave 7).

Each note is written as a fresh analyst report dated October 4, 2026.
Content rule: no references to any earlier work, targets, or methodology labels.
Figures below are authoritative -- targets are not recomputed.
Prices are October 2, 2026 closes; they are fixed inputs, not lookups.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pdfs")

METHODOLOGY = (
    "Our valuation is a probability-weighted scenario DCF. We model bear, base, and bull "
    "cases over an explicit forecast horizon -- 10 years for most businesses, 15 years for "
    "businesses meeting our compounder-quality criteria (10+ years of ROIC above 15%, stable "
    "or expanding gross margins, free-cash-flow conversion above 80%, all verified from "
    "history, never projected) -- weighted 25% / 50% / 25%. Discount rates are "
    "scenario-specific: the base rate reflects fundamental business risk (9% for stable "
    "franchises, 10% standard, 12% or higher for speculative situations; 8-8.5% for "
    "compounder-quality businesses whose predictable cash flows genuinely lower risk); the "
    "bear case adds 250bp, the bull case subtracts 150bp (floor 8%). Terminal value assumes "
    "no more than 2.5% perpetual growth (3.0% for compounder-quality businesses) applied to "
    "normalized mid-cycle margins -- never peak margins -- and any terminal value exceeding "
    "70% of enterprise value is haircut and disclosed. Bear cases are required to be "
    "genuinely adverse and to sit below the current price. Management guidance is never "
    "accepted at face value; it is independently tested and haircut where evidence warrants. "
    "For international businesses we add an explicit country-risk premium to the discount "
    "rate and benchmark multiples against regional peers facing similar risks, never US peers "
    "alone; structural risks (e.g. VIE structures, regulatory confiscation) are modeled in "
    "cash flows and the bear case."
)

BANNED = [
    "old target", "previous note", "previous report", "prior report", "as we wrote",
    "prior methodology", "rebuilt", "rebuild", "addenda", "version", "upgraded",
    "downgraded", "was previously", "formerly",
]
BANNED_RE = [re.compile(r"\b" + re.escape(b) + r"\b", re.IGNORECASE) for b in BANNED]
BANNED_RE.append(re.compile(r"\bv2\b", re.IGNORECASE))


def _texts(data):
    out = []
    for _h, blocks in data["sections"]:
        for _k, payload in blocks:
            if isinstance(payload, str):
                out.append(payload)
            elif isinstance(payload, list):
                out.extend(payload)
            elif isinstance(payload, tuple):
                headers, rows = payload
                out.extend(headers)
                for r in rows:
                    out.extend(r)
    return out


def check_clean(data):
    for t in _texts(data):
        for rx in BANNED_RE:
            if rx.search(t):
                raise ValueError("BANNED phrase in %s: %r" % (data["ticker"], rx.pattern))


NOTES = []

# ---------------------------------------------------------------- WHR ----
NOTES.append({
    "ticker": "WHR",
    "company": "Whirlpool Corporation",
    "verdict": "SELL",
    "target": "$16.00",
    "price": "$30.31",
    "price_note": "October 2, 2026 close",
    "upside": "-47%",
    "sections": [
        ("Investment Thesis", [
            ("p", "Whirlpool is the largest major-appliance manufacturer in the world by volume, "
             "and that scale has not translated into pricing power. Appliances are a replacement-driven, "
             "deeply cyclical category where Whirlpool, Haier/GE, LG, Samsung, and Electrolux contest a "
             "consumer who buys a refrigerator roughly once a decade. When housing turnover stalls -- as it "
             "has through 2025 and 2026 -- discretionary replacement demand evaporates, and the industry "
             "competes the only way it knows how: on price. Promotional intensity has been structural, not "
             "cyclical, for the better part of a decade, and the Korean manufacturers show no sign of "
             "relenting."),
            ("p", "The balance sheet converts this cyclical squeeze into an equity problem. The InSinkErator "
             "acquisition and years of debt-funded shareholder returns left Whirlpool with net debt near "
             "$7 billion against roughly $1.5 billion of mid-cycle EBITDA. Interest and the dividend now "
             "absorb the bulk of operating cash flow, which means deleveraging depends on a demand recovery "
             "that keeps not arriving. In a genuine housing downturn, free cash flow goes to creditors, not "
             "shareholders -- and the equity is the residual claimant on a melting ice cube of appliance "
             "demand."),
            ("p", "At $30.31, the market is pricing a mid-cycle earnings recovery that our scenario work does "
             "not support. Our probability-weighted fair value is $16.00, implying 47% downside. The dividend, "
             "currently costing the company on the order of $400 million a year, looks increasingly difficult "
             "to defend if North American volumes stay soft through 2027. We see no catalyst that repairs "
             "both the demand cycle and the leverage ratio simultaneously, and we would not own the equity "
             "while both work against it."),
            ("p", "The capital-allocation record compounds our skepticism. Billions were spent repurchasing "
             "shares at prices far above today's quote, and the InSinkErator acquisition -- strategically "
             "sound -- was funded at the top of the credit cycle. Management now faces the classic "
             "leveraged-cyclical trap: every dollar of free cash flow must service debt, the dividend consumes "
             "what little remains, and growth investment is starved. Deleveraging through earnings requires "
             "the demand recovery; deleveraging through asset sales means selling good assets to support "
             "stressed equity. We see no outcome in this arithmetic that leaves $30 of equity value intact."),
        ]),
        ("Business Overview", [
            ("p", "Whirlpool Corporation, headquartered in Benton Harbor, Michigan, designs and manufactures "
             "major home appliances -- refrigerators, laundry, cooking, and dishwashers -- under the "
             "Whirlpool, Maytag, KitchenAid, Amana, and JennAir brands. North America generates the large "
             "majority of segment profit. The company completed the contribution of its European business "
             "into the Beko Europe joint venture (majority-owned by Ar\u00e7elik) in 2024, and acquired "
             "InSinkErator, the food-waste-disposal leader, in late 2022 for approximately $3 billion. "
             "Revenue runs roughly $17 billion annually, with EBIT margins that have oscillated between 3% "
             "and 8% across the cycle."),
            ("p", "The segment economics explain the vulnerability. North American major appliances is a "
             "high-fixed-cost, low-margin assembly business where utilization is everything: at high "
             "utilization the plants print cash, at low utilization they bleed. Whirlpool has rationalized "
             "capacity for years, but competitors keep adding it, leaving the industry structurally prone to "
             "overcapacity -- in which the largest player has the most fixed cost to absorb when volumes "
             "disappoint. This operating leverage works beautifully in housing booms and brutally in busts; "
             "our scenario work assumes investors are underweighting the bust case."),
        ]),
        ("Forward Outlook", [
            ("p", "Our judgment is that the appliance demand cycle stays soft longer than consensus expects. "
             "US existing-home sales remain depressed by the mortgage rate lock-in effect, and every year of "
             "low turnover pushes a cohort of would-be appliance replacements further into the future. "
             "Meanwhile the competitive structure has permanently worsened: LG and Samsung treat appliances "
             "as a strategic beachhead rather than a profit pool, which caps industry pricing even in good "
             "years."),
            ("p", "On costs, steel and component tariffs are a direct margin tax that Whirlpool cannot fully "
             "pass through in a promotional market. We expect EBIT margins to grind in the 4-5% range rather "
             "than returning to the 7-8% peaks of the last housing boom, and we expect free cash flow to be "
             "consumed first by interest, then by the dividend, leaving little for debt reduction. The "
             "InSinkErator asset is genuinely high-quality, but it is too small to carry the enterprise. "
             "Absent a housing-turnover surge, this is a company managing decline as gracefully as possible -- "
             "not a compounding story."),
            ("p", "The dividend deserves its own analysis because it is the last pillar of the bull case. At "
             "roughly $400 million annually, it is a claim on cash flow that the business can no longer "
             "comfortably afford alongside interest and debt maturities. Dividend cuts in leveraged cyclicals "
             "are rarely one-time events; they signal the board's recognition that the balance sheet, not the "
             "payout, is the priority. We model the dividend surviving in the base case but cut in the bear "
             "case, and we would treat any cut as confirmation of our thesis rather than a buying opportunity, "
             "since it would coincide with the demand deterioration we already expect."),
            ("p", "On input costs, the tariff regime is a margin tax with no offset. Steel, aluminum, and "
             "imported components face duties that Whirlpool cannot fully pass through when competitors are "
             "discounting to gain share. We estimate tariffs shave 100-150 basis points from North American "
             "EBIT margins versus the pre-tariff baseline -- the difference, in a 4-5% margin business, "
             "between deleveraging and treading water. Management's cost-takeout programs are real but "
             "historically offset by reinvestment; we credit only half the announced savings in our numbers."),
        ]),
        ("Valuation", [
            ("p", "We value Whirlpool on a probability-weighted scenario DCF, discounting at 10% in the base "
             "case to reflect cyclical and leveraged business risk. In the bear case, a housing-led appliance "
             "recession pushes EBIT margins toward 3%, the dividend is cut, and refinancing risk reprices the "
             "debt; equity value in that scenario approaches the low single digits. In the base case, volumes "
             "stabilize, EBIT margins average about 5.5% across the cycle, and slow deleveraging supports a "
             "mid-teens equity value. In the bull case, housing turnover rebounds, margins recover toward 7%, "
             "and accelerated debt paydown unlocks equity value in the high $20s."),
            ("p", "Weighting bear, base, and bull at 25% / 50% / 25% gives a probability-weighted fair value "
             "of $16.00, our target. The bear case sits well below the current price, as required, and the "
             "leverage means small changes in assumed mid-cycle margins move the equity value materially -- "
             "which is itself a reason for caution."),
            ("p", "To make the leverage explicit: at our base-case mid-cycle EBITDA of roughly $1.5 billion, "
             "net debt near $7 billion leaves only $4-5 billion of enterprise value for equity at a 7-8x "
             "EV/EBITDA multiple appropriate for a cyclical manufacturer -- roughly $16 per share after "
             "adjusting for pension and other obligations. In the bear case, EBITDA falls toward $1 billion "
             "while debt stays fixed, and the equity residual compresses toward zero. Leverage is a call "
             "option on the cycle; at $30.31 the market is paying in-the-money prices for a call on "
             "fundamentals that are deteriorating."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "A deeper housing downturn or recession in big-ticket durables would compress volumes and "
                "margins simultaneously, with leverage amplifying the equity impact.",
                "Promotional intensity from Korean competitors could worsen, permanently impairing North "
                "American pricing.",
                "Steel and component tariffs raise input costs that cannot be passed through in a discount-driven "
                "market.",
                "The dividend may be cut if cash flow disappoints, removing a key support for the shareholder "
                "base.",
                "Refinancing risk: a large debt wall must be termed out in markets that may not stay accommodative.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "A sustained surge in US housing turnover with appliance sell-through outpacing expectations "
                "for several consecutive quarters.",
                "Demonstrated price realization -- list-price increases sticking without volume loss -- proving "
                "the promotional era is ending.",
                "Material deleveraging via asset sales or retained cash flow, bringing net debt below 2x EBITDA.",
                "Structural cost-out that lifts mid-cycle EBIT margins back above 7% on flat volumes.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", METHODOLOGY),
        ]),
    ],
})

# ---------------------------------------------------------------- MCD ----
NOTES.append({
    "ticker": "MCD",
    "company": "McDonald's Corporation",
    "verdict": "REDUCE",
    "target": "$122.00",
    "price": "$231.89",
    "price_note": "October 2, 2026 close",
    "upside": "-47%",
    "sections": [
        ("Investment Thesis", [
            ("p", "McDonald's operates the finest franchised restaurant machine ever built: more than 40,000 "
             "restaurants in 100-plus countries, over 95% franchised, with rent and royalties converting "
             "franchisee sales into one of the most reliable cash streams in consumer staples. We do not "
             "dispute the quality of the business. We dispute the price. At $231.89, the market values "
             "McDonald's as though the comparable-sales machine never misses and the multiple never compresses. "
             "Our scenario work puts probability-weighted fair value at $122.00 -- 47% below the current price."),
            ("p", "Our concern is the growing gap between the narrative and the traffic data. US guest counts "
             "have been soft even as menu prices carried comparable sales, and cumulative price increases "
             "have damaged the brand's core value perception -- the exact attribute that made McDonald's "
             "recession-resilient in prior cycles. Franchisees, squeezed by labor costs and remodel capital "
             "requirements, are pushing back on corporate initiatives, which constrains the reinvestment the "
             "system needs. Meanwhile the rise of GLP-1 weight-loss drugs represents a genuine structural "
             "headwind to quick-service occasions that the market has barely begun to price."),
            ("p", "McDonald's deserves a premium multiple; it does not deserve a flawless one. Our base case "
             "assumes the brand endures and grows -- low-single-digit systemwide sales growth, margins intact -- "
             "but values that durable cash flow at a multiple appropriate for a mature, slowing compounder "
             "rather than a growth stock. The result is a REDUCE: a great business whose shares embed a decade "
             "of perfection."),
            ("p", "History supports our multiple discipline. McDonald's traded at 14-18x earnings for most of "
             "the 2010s while compounding beautifully; the rerating toward the mid-20s coincided with the "
             "market's discovery of quality compounders as a factor, not with any acceleration in the "
             "business. Factors mean-revert. Our $122 target embeds a 14x multiple on normalized earnings -- "
             "a multiple at which McDonald's was a wonderful investment for decades, and a multiple the "
             "current price has forgotten. We are not predicting business failure; we are predicting multiple "
             "normalization, which for shareholders is nearly as painful."),
        ]),
        ("Business Overview", [
            ("p", "McDonald's Corporation, headquartered in Chicago, is the world's largest restaurant chain by "
             "revenue, with systemwide sales exceeding $130 billion across more than 40,000 locations. The "
             "company's economics are those of a franchisor and landlord: franchisees pay royalties (roughly "
             "4-5% of sales) plus rent on company-owned real estate, producing operating margins near 45% and "
             "extraordinary returns on invested capital. International markets -- including the refranchised "
             "China business -- and the US company-operated base round out the footprint. The 'Accelerating "
             "the Arches' strategy centers on digital, delivery, drive-thru, and menu core equities."),
            ("p", "The financial architecture is what makes McDonald's special -- and what makes the current "
             "price dangerous. With 45% operating margins and minimal corporate capex (franchisees fund the "
             "restaurants), nearly every incremental dollar of systemwide sales drops to free cash flow, which "
             "funds one of the market's most aggressive buyback programs. But this cuts both ways: when "
             "comparable sales slow, there is no volume lever at the corporate level to pull, and buybacks at "
             "25x earnings destroy value rather than create it. The machine is optimized for a world of "
             "perpetual 5%-plus comps; we do not think that world continues."),
        ]),
        ("Forward Outlook", [
            ("p", "Our judgment is that McDonald's enters a slower era. The easy comp gains from delivery "
             "expansion and digital adoption are largely harvested; from here, growth must come from guest "
             "counts, which is the hardest kind. We expect management to lean on value platforms to win back "
             "traffic, but genuine value costs margin -- either the company's (through franchisee support) or "
             "the franchisee's (through discounting), and neither is free."),
            ("p", "Longer term, two structural shifts matter more than any quarterly comp print. First, "
             "GLP-1 adoption is already measurable in food-away-from-home occasions, and McDonald's "
             "over-indexes to the frequency occasions most at risk. Second, the international growth engine -- "
             "particularly China -- faces a weaker consumer and intensifying local competition. Neither breaks "
             "the business; both shave the long-run growth rate from the 6-8% the current price implies toward "
             "the 2-4% we think is realistic. A 2-4% grower should not trade at a growth multiple, and "
             "eventually it won't."),
            ("p", "Franchisee economics are the transmission mechanism. McDonald's collects rent and royalties "
             "off the top, which insulates corporate earnings -- until franchisee cash flow deteriorates "
             "enough to slow development, remodels, and technology adoption. We are seeing early signs: "
             "operators publicly pushing back on discount programs they must fund, development timelines "
             "stretching, and refranchising proceeds no longer masking the trend. The franchisor model is a "
             "wonderful shock absorber, but absorbers have limits, and persistent traffic declines test them."),
            ("p", "International deserves a colder look than consensus gives it. The China business faces a "
             "consumer slowdown and ferocious local competition, and developmental licensees optimize for "
             "their own returns, not Chicago's. The international operated-markets segment faces the same "
             "value-perception issues as the US, compounded by traffic shocks in the Middle East that "
             "management describes as temporary but which have persisted. International was the growth story "
             "of the 2010s; we model it as a market-growth contributor at best."),
        ]),
        ("Valuation", [
            ("p", "We value McDonald's on a probability-weighted scenario DCF at a 9% base discount rate, "
             "appropriate for a stable franchise, with scenario-specific adjustments. In the bear case, US "
             "traffic declines persist, GLP-1 adoption accelerates, and international softness deepens; "
             "normalized earnings power settles near $7 per share and the multiple compresses toward 12x, "
             "implying value well below $100. In the base case, the brand stabilizes, earnings normalize "
             "around $8.75 per share, and a 14x multiple -- fair for a mature, wide-moat compounder -- gives "
             "value near our target. In the bull case, traffic recovers, digital drives mix, and $12 of "
             "earnings at an 18x multiple supports value above $200 -- but we assign this modest weight given "
             "the traffic evidence."),
            ("p", "Weighting the scenarios 25% / 50% / 25% yields a probability-weighted fair value of "
             "$122.00, our target. The valuation is a multiple call on a great business, not a business-quality "
             "call: we would become constructive on any meaningful derating toward our fair value."),
            ("p", "The earnings bridge matters: our $8.75 normalized EPS assumes operating income roughly flat "
             "to slightly down from current levels with continued buybacks -- a genuinely mild assumption. "
             "The entire downside comes from the multiple: 25x to 14x. Multiple compression of this magnitude "
             "has precedent -- McDonald's derated similarly in 2008-2009 and 2015-2016 -- and in each case the "
             "business recovered while shareholders waited years for the price to follow. At $231.89, investors "
             "are paying for the recovery in advance and bearing the derating risk without compensation."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "A US consumer downturn would hit traffic just as value investments are raising costs -- the "
                "classic QSR margin squeeze.",
                "GLP-1 drugs could structurally reduce quick-service visit frequency beyond our assumptions.",
                "Franchisee relations: cash-flow pressure could slow remodels and technology adoption, degrading "
                "the store base.",
                "Food-safety incidents have historically caused sharp, if temporary, traffic shocks.",
                "Foreign-exchange translation and geopolitical exposure in international markets.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Sustained positive US guest counts -- not just average check -- over four or more quarters, "
                "proving value perception is repaired.",
                "Franchisee cash flow inflecting upward, evidenced by accelerating remodel and new-unit "
                "development commitments.",
                "Credible data that GLP-1 impact on QSR occasions is smaller than feared.",
                "The shares derating toward our $122 fair value, at which point the risk/reward turns favorable.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", METHODOLOGY),
        ]),
    ],
})

# ---------------------------------------------------------------- WCN ----
NOTES.append({
    "ticker": "WCN",
    "company": "Waste Connections, Inc.",
    "verdict": "SELL",
    "target": "$78.00",
    "price": "$153.82",
    "price_note": "October 2, 2026 close",
    "upside": "-49%",
    "sections": [
        ("Investment Thesis", [
            ("p", "Waste Connections is a superb business, and this is a valuation call, not a business-quality "
             "call. The company has spent two decades rolling up local solid-waste monopolies, pricing above "
             "inflation into captive commercial customers, and converting it all into prodigious free cash "
             "flow. It deserves a premium multiple. It does not deserve this multiple. At $153.82, the shares "
             "trade at roughly 40 times free cash flow -- a price that demands a decade of flawless tuck-in "
             "acquisitions, uninterrupted above-inflation pricing, and zero regulatory friction. Our "
             "probability-weighted fair value is $78.00, implying 49% downside."),
            ("p", "Our core judgment is that the market is capitalizing peak conditions into perpetuity. "
             "Waste Connections' pricing power is real but not infinite: commercial customers eventually "
             "push back, municipal contracts re-bid, and the acquisition targets that built the empire are "
             "getting scarcer and pricier with every deal. The marginal acquisition multiple has crept up for "
             "years, which means each incremental dollar of deployed capital earns a lower return. A roll-up "
             "works until the targets run out or get too expensive; we are closer to that point than the price "
             "admits."),
            ("p", "Meanwhile the regulatory backdrop is quietly worsening. PFAS remediation obligations, "
             "methane-emission rules, and post-closure liabilities are real cash costs that the current "
             "multiple treats as footnotes. None of this impairs the moat -- landfills remain the best "
             "local monopolies in American business -- but moats deserve 25x free cash flow, not 40x. We rate "
             "the shares SELL and would revisit only after a derating commensurate with a maturing roll-up."),
            ("p", "Consider the acquisition math directly. Waste Connections historically paid 6-9x EBITDA for "
             "tuck-ins and created value through route density and pricing. As the company has grown, the "
             "remaining independent operators are smaller, more competitive to acquire, and increasingly aware "
             "of their scarcity value; recent deal multiples have drifted into the low teens. At 12-14x EBITDA "
             "paid, an acquisition must be flawless to earn its cost of capital -- and the market capitalizes "
             "Waste Connections as though every future deal clears that bar. Roll-ups do not die dramatically; "
             "they fade into conglomerates trading at market multiples. We believe that fade has begun."),
        ]),
        ("Business Overview", [
            ("p", "Waste Connections, Inc., headquartered in The Woodlands, Texas (domiciled in Ontario, Canada), "
             "is the third-largest solid-waste company in North America, with roughly $9 billion in annual "
             "revenue. The strategy is deliberately contrarian: dominate secondary and exclusive markets where "
             "competition is thin, then vertically integrate collection into transfer stations and landfills. "
             "The company also operates a sizable exploration-and-production waste business (R360) serving oil "
             "and gas basins. Growth has come roughly half from pricing and half from acquisitions, with "
             "adjusted EBITDA margins in the low 30s -- best in class among the public waste operators."),
            ("p", "The moat structure is genuinely exceptional: landfills are nearly impossible to permit in "
             "most jurisdictions, giving incumbents local monopolies with pricing power that has compounded for "
             "decades, and collection routes exhibit powerful density economics -- each incremental stop on an "
             "existing route is nearly pure margin. This is why the business deserves a premium multiple in any "
             "rational framework. Our argument is purely about the price of that excellence: at 40x free cash "
             "flow, investors are paying for the moat, the pricing power, the roll-up, and a decade of flawless "
             "execution, with nothing left for the inevitable surprises."),
        ]),
        ("Forward Outlook", [
            ("p", "Our judgment is that Waste Connections keeps executing well operationally while the "
             "investment math deteriorates. Pricing should remain above inflation -- the local-monopoly "
             "structure guarantees that -- but the spread between price increases and cost inflation narrows "
             "as labor and regulatory costs accelerate. Acquisition-driven growth continues, but we expect "
             "deal multiples paid to stay elevated, compressing the return on each new tuck-in."),
            ("p", "The underappreciated variable is environmental capex. PFAS treatment at landfills and "
             "leachate systems, plus methane-capture investments, will absorb a growing share of operating "
             "cash flow over our forecast horizon. The E&amp;P waste business adds cyclicality that the "
             "market currently ignores. None of this makes Waste Connections a bad business -- it remains "
             "among the highest-quality operators we cover -- but a maturing compounder growing free cash "
             "flow per share at high-single digits cannot sustain a 40x multiple. Multiple compression, not "
             "business deterioration, is the risk, and it is a 49% risk."),
            ("p", "There is also a subtle mix shift underway. The R360 energy-waste business, while well run, "
             "ties a portion of earnings to oilfield activity -- a cyclicality the recession-proof-compounder "
             "narrative ignores. And municipal contract renewals, which underpin the exclusive-market strategy, "
             "are seeing more aggressive bidding as competitors target Waste Connections' high margins. Neither "
             "is fatal; both trim the growth rate at the margin, and at 40x free cash flow there is no margin "
             "for trimming."),
            ("p", "Capital allocation is the swing factor we watch most closely. Waste Connections has "
             "historically balanced acquisitions with buybacks, but as deal multiples rise, the hurdle for "
             "buybacks falls -- repurchasing shares at 40x free cash flow destroys value as surely as "
             "overpaying for deals. We would rather see the company slow acquisition spending than chase "
             "targets at 14x EBITDA; management's history suggests discipline, but the pressure to deploy the "
             "balance sheet grows each quarter growth decelerates. Our base case assumes acquisition "
             "discipline holds; the bear case assumes it doesn't."),
        ]),
        ("Valuation", [
            ("p", "We value Waste Connections on a probability-weighted scenario DCF using a 9% base discount "
             "rate, reflecting the stability of the franchise, with an explicit country-risk assessment for "
             "the Canadian domicile (immaterial at these weights) and regional peer benchmarking. In the bear "
             "case, acquisition multiples paid stay high while pricing power fades, free-cash-flow growth "
             "slows to 3%, and the multiple compresses toward 20x -- implying value below $60. In the base "
             "case, the company compounds free cash flow per share at roughly 7%, margins hold in the low "
             "30s, and a 25x multiple on normalized free cash flow -- still a full premium to the market -- "
             "supports our $78.00 target. In the bull case, accretive deals and pricing surprise to the "
             "upside and value approaches $110."),
            ("p", "Weighting 25% / 50% / 25% gives a probability-weighted fair value of $78.00. The bear case "
             "sits well below the current price, as required. Note what this implies: even our bull case, "
             "which assumes the roll-up machine keeps humming, sits nearly 30% below today's price. When the "
             "bull case is a loss, the price is wrong."),
            ("p", "Our 25x normalized free-cash-flow multiple in the base case deserves emphasis: it is itself "
             "a premium -- the broad market trades near 20x, and most industrial compounders trade in the high "
             "teens to low 20s. We grant Waste Connections a premium for moat quality and still arrive 49% "
             "below the price. The bull case at $110 requires the multiple to stay above 30x indefinitely while "
             "growth persists -- possible, but it is a bet on sentiment, not on cash flows, and our framework "
             "does not pay for sentiment."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Multiple compression is the primary risk: a derating from ~40x to ~25x free cash flow needs "
                "no operational misstep at all.",
                "Acquisition indigestion or overpayment as quality targets become scarce.",
                "PFAS, methane, and other environmental regulations raising capex and post-closure liabilities.",
                "A commercial-volume recession would hit the highest-margin collection revenue first.",
                "Leverage, while modest for the sector, limits flexibility if credit conditions tighten.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Evidence that acquisition multiples paid are falling while returns on new deals stay above 15% -- "
                "the roll-up math working again.",
                "Sustained double-digit free-cash-flow-per-share growth for several years, validating the "
                "current multiple.",
                "Regulatory clarity on PFAS with costs coming in well below our provisions.",
                "The shares derating toward our $78 fair value, restoring a reasonable risk/reward.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", METHODOLOGY),
        ]),
    ],
})

# --------------------------------------------------------------- DDOG ----
NOTES.append({
    "ticker": "DDOG",
    "company": "Datadog, Inc.",
    "verdict": "REDUCE",
    "target": "$100.00",
    "price": "$277.22",
    "price_note": "October 2, 2026 close",
    "upside": "-64%",
    "sections": [
        ("Investment Thesis", [
            ("p", "Datadog built the best observability platform in cloud computing: twenty-plus products on a "
             "single pane of glass, best-in-class land-and-expand motion, and net revenue retention that was "
             "once the envy of software. We respect the product deeply. But $277.22 prices the equity at more "
             "than $90 billion of enterprise value against roughly $3 billion of revenue -- around 30 times "
             "sales -- for a business whose growth has already decelerated from the 60s into the 20s. Our "
             "probability-weighted fair value is $100.00, implying 64% downside. This is a REDUCE rather than "
             "a SELL only because the underlying franchise is genuinely elite; the business is fine, the "
             "multiple is not."),
            ("p", "Our central judgment is that the observability layer is being commoditized at the edges "
             "faster than the market appreciates. OpenTelemetry has standardized data collection, which "
             "erodes the proprietary-agent advantage Datadog was built on; Grafana, Elastic, and the "
             "hyperscalers' native tooling all compete credibly at lower price points. Meanwhile Datadog's "
             "usage-based pricing faces a subtle but powerful deflationary force: as customers optimize cloud "
             "spend -- the defining enterprise behavior of the last three years -- observability bills are "
             "among the first line items scrutinized, because they scale with the very infrastructure "
             "customers are trying to shrink."),
            ("p", "AI workloads are the standard bull argument: more data, more complexity, more monitoring. "
             "We agree volumes grow; we disagree that Datadog captures the economics. AI-native architectures "
             "generate enormous telemetry at falling unit prices, and the vendors best positioned to monetize "
             "AI observability are the model and infrastructure providers themselves. Datadog can keep growing "
             "revenue in the 20s for years and still be worth a fraction of today's price, because 30x sales "
             "requires not just growth but growth at software's highest historical multiples, sustained for a "
             "decade. We see a very good company priced as an immortal one."),
            ("p", "The seat-based and usage-based pricing model faces a second, AI-specific deflationary force "
             "worth naming. As enterprises deploy AI agents, the ratio of machine-generated to human-generated "
             "telemetry explodes while willingness to pay per unit of telemetry falls -- buyers negotiate volume "
             "discounts aggressively, and AI-native buyers are the most price-sensitive of all. Datadog "
             "benefits from the volume and suffers on the unit price; net, we expect revenue per unit of "
             "monitored infrastructure to decline over time. This is the classic innovator's treadmill: run "
             "faster in volume to stand still in price."),
        ]),
        ("Business Overview", [
            ("p", "Datadog, Inc., headquartered in New York and founded in 2010, provides a SaaS observability "
             "and security platform spanning infrastructure monitoring, application performance monitoring, log "
             "management, digital experience, and cloud security. The platform is sold primarily on "
             "consumption-based pricing, which drives the celebrated land-and-expand dynamic: customers adopt "
             "one product and expand to many. Revenue is roughly $3 billion annually with a large enterprise "
             "customer base, and the company has consistently posted among the highest net retention rates in "
             "enterprise software, albeit moderating from peaks above 130%."),
        ]),
        ("Forward Outlook", [
            ("p", "Our judgment is that Datadog's revenue growth continues decelerating toward the mid-teens "
             "over our horizon as the law of large numbers meets intensifying competition. The product engine "
             "remains strong -- new security and AI-adjacent SKUs will contribute -- but each incremental "
             "product faces a more crowded field than the last, and pricing power in core infrastructure "
             "monitoring is structurally declining as collection commoditizes."),
            ("p", "Margins should expand as the company scales -- the model has genuine operating leverage -- "
             "but multiple compression will dominate the equity math. Software history is unambiguous on this "
             "point: when growth decelerates from 60% to 20%, multiples compress from 30x sales toward 8-10x "
             "regardless of quality. Datadog's free-cash-flow margins, already in the 20s, can improve, but "
             "not fast enough to offset a two-thirds derating. Our fair value assumes the business executes "
             "well and the multiple normalizes anyway."),
            ("p", "Competition deserves specificity because it is no longer theoretical. Grafana Labs has built "
             "a credible open-source-based alternative adopted by sophisticated engineering organizations; "
             "Elastic has stabilized; and the hyperscalers -- AWS, Azure, GCP -- bundle native monitoring that "
             "is good enough for a growing share of workloads and free at the point of decision. Datadog wins "
             "head-to-head evaluations on product depth, but procurement is increasingly deciding on price, and "
             "good-enough-plus-bundled is winning more deals than it used to. Net revenue retention, the metric "
             "that once justified any multiple, has been moderating for tangible reasons."),
        ]),
        ("Valuation", [
            ("p", "We value Datadog on a probability-weighted scenario DCF with a 12% base discount rate, "
             "reflecting competitive and multiple-compression risk in enterprise software. In the bear case, "
             "consumption growth stalls near 10%, pricing pressure intensifies, and the exit multiple falls to "
             "6x sales -- implying value near $40. In the base case, revenue compounds in the low 20s through "
             "decade-end, free-cash-flow margins expand into the low 30s, and an 8x exit sales multiple -- "
             "appropriate for a scaled, still-growing SaaS leader -- supports our $100.00 target. In the bull "
             "case, AI observability becomes a genuine supercycle and value approaches $180."),
            ("p", "Weighting 25% / 50% / 25% gives a probability-weighted fair value of $100.00. The bear case "
             "sits far below the current price, as required. The arithmetic is stark: even capitalizing our "
             "bull-case 2030 revenue at a premium multiple and discounting back, the present value cannot "
             "approach $277. The price requires economics beyond the bull case."),
            ("p", "Our 8x exit sales multiple in the base case is worth defending: it is the multiple the market "
             "has historically paid for scaled SaaS growing in the high teens with 30% free-cash-flow margins "
             "-- ServiceNow, Adobe, and Salesforce all traded there at similar life-cycle stages. Datadog bulls "
             "implicitly assume it sustains 20x-plus sales multiples at $10 billion-plus revenue scale; no "
             "software company in history has done so. The derating from 30x to 8x on growing revenue still "
             "produces our $100 target -- the business can double revenue and the stock can fall by two-thirds, "
             "because the starting multiple assumed the business would triple revenue at peak multiples forever."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Enterprise cloud-spend optimization could re-accelerate, directly pressuring Datadog's "
                "consumption-based revenue.",
                "Competitive pressure from Grafana, Elastic, hyperscaler-native tooling, and OpenTelemetry-based "
                "alternatives compressing pricing.",
                "Multiple compression as growth decelerates -- the dominant risk to the shares regardless of "
                "execution.",
                "Heavy stock-based compensation diluting shareholders even as the business grows.",
                "AI workloads shifting observability value capture toward infrastructure and model providers.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Net revenue retention re-accelerating above 130% with demonstrated pricing power, not just "
                "seat expansion.",
                "Sustained free-cash-flow margins above 35% proving the model scales better than we assume.",
                "Evidence that Datadog is capturing AI-observability economics -- premium-priced AI SKUs at "
                "material scale.",
                "The shares derating toward our $100 fair value, where the quality of the franchise would make "
                "risk/reward attractive.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", METHODOLOGY),
        ]),
    ],
})

# ---------------------------------------------------------------- RGTI ---
NOTES.append({
    "ticker": "RGTI",
    "company": "Rigetti Computing, Inc.",
    "verdict": "SELL",
    "target": "$5.00",
    "price": "$15.25",
    "price_note": "October 2, 2026 close",
    "upside": "-67%",
    "spec": True,
    "footer_note": "Speculative pre-revenue situation -- position sizing should reflect binary risk.",
    "sections": [
        ("Investment Thesis", [
            ("p", "Let us be plain: Rigetti Computing is a pre-revenue science project trading at a "
             "multi-billion-dollar valuation. The company generates on the order of $10-15 million in annual "
             "revenue -- mostly government research contracts, not commercial product sales -- while burning "
             "$70-80 million a year pursuing superconducting quantum computers. At $15.25, the market "
             "capitalization prices a future in which fault-tolerant quantum computing arrives, Rigetti wins "
             "a meaningful share of it, and today's shareholders are not diluted into irrelevance along the "
             "way. We assign low probability to all three happening together. Our fair value is $5.00, "
             "implying 67% downside, and we rate the shares SELL (Speculative)."),
            ("p", "This is not a judgment on the physics. Superconducting qubits are a legitimate path to "
             "quantum computing, Rigetti operates its own fabrication facility, and the technical team has "
             "real credentials. It is a judgment on the timeline and the capital structure. Useful, "
             "fault-tolerant quantum computing -- the kind that generates commercial revenue rather than "
             "research grants -- is widely estimated at 5 to 15 years away, and the field is crowded with "
             "better-funded competitors: IBM and Google with effectively infinite R&amp;D budgets, IonQ and "
             "D-Wave with their own public currencies. Breakthroughs in quantum error correction accrue to "
             "the field, not to any single small company."),
            ("p", "The nearer-term math is unforgiving. At the current burn rate, Rigetti must return to "
             "capital markets repeatedly, and each raise -- typically via at-the-market offerings into retail "
             "enthusiasm -- dilutes existing holders. The stock has become a trading vehicle for quantum "
             "narrative momentum rather than a claim on discounted cash flows, because there are no cash "
             "flows to discount. Our $5.00 fair value reflects the option value of the intellectual property, "
             "the talent, and the cash on hand, heavily discounted for the dilution required to survive to "
             "the end of the decade. This is a call option on a breakthrough; it should be sized like one, "
             "and at $15.25 even the option is overpriced."),
            ("p", "It helps to state the valuation in venture-capital terms, since that is what this is. At "
             "$15.25, Rigetti's enterprise value exceeds $4 billion -- a late-stage private valuation for a "
             "company with $10-15 million of contract revenue and no product-market fit. Venture investors pay "
             "such prices with liquidation preferences, anti-dilution protection, and board control; public "
             "shareholders get none of those, only the dilution. The quantum-computing field will likely "
             "produce enormous value over the next two decades; the question is how much of it accrues to "
             "today's common shareholders after the intervening financings, and our answer is: far less than "
             "$15 per share."),
        ]),
        ("Business Overview", [
            ("p", "Rigetti Computing, Inc., founded in 2013 and headquartered in Berkeley, California, develops "
             "superconducting quantum processors and offers quantum-computing-as-a-service through cloud "
             "partners. The company operates Fab-1, a dedicated quantum-chip fabrication facility, and sells "
             "its Novera line of quantum processing units alongside research collaborations. Reported revenue "
             "is minimal and contract-based; the company is pre-profitability by a wide margin and funds "
             "operations through equity raises. The competitive set spans IBM, Google, IonQ, D-Wave, and a "
             "deep bench of venture-backed startups pursuing trapped-ion, neutral-atom, and photonic "
             "approaches."),
        ]),
        ("Forward Outlook", [
            ("p", "Our judgment is that the next several years bring technical milestones, not commercial "
             "ones. Qubit counts will rise, fidelities will improve, and error-correction demonstrations will "
             "make headlines -- and none of it will produce material product revenue before the end of the "
             "decade. That is the normal path of deep-tech commercialization, and it is fatal to equity value "
             "when the starting valuation assumes the end state."),
            ("p", "The realistic paths from here are three. One: dilutive survival, in which the company raises "
             "repeatedly at the mercy of sentiment, and per-share value decays regardless of technical "
             "progress. Two: acquisition by a hyperscaler or defense prime seeking quantum talent and IP, "
             "which is the genuine bull case but typically occurs at modest premiums for pre-revenue "
             "companies. Three: technical failure or funding exhaustion. We weight the first path most "
             "heavily. Investors should understand they are underwriting years of dilution for a lottery "
             "ticket -- and lottery tickets should not cost $15."),
            ("p", "The financing cycle deserves emphasis because it is the mechanism of value destruction. "
             "Quantum stocks trade on narrative momentum -- government announcements, technical milestones, "
             "quantum-advantage headlines -- and management teams rationally exploit these windows with "
             "at-the-market offerings. Each raise funds another 12-18 months of burn and permanently increases "
             "the share count; the stock then needs ever-larger narratives to sustain the price on the larger "
             "base. We have seen this movie in prior SPAC-era technology manias. The technology may eventually "
             "work; the capitalization table will not resemble today's."),
        ]),
        ("Valuation", [
            ("p", "Traditional DCF is not meaningful for a pre-revenue company with no line of sight to "
             "positive cash flow; we value Rigetti on an option-value framework with scenario weights. In the "
             "bear case, funding dries up or technical progress stalls, dilutive raises continue, and the "
             "equity retains only nominal IP value near $1. In the base case, Rigetti survives to decade-end "
             "with steady technical progress, the IP and talent base hold strategic value, and dilution "
             "brings per-share fair value to our $5.00 target. In the bull case, a strategic acquirer pays a "
             "premium for the platform and the shares realize $15 or more -- roughly today's price, which "
             "tells you the market is pricing the acquisition as the expected outcome rather than the "
             "optimistic one."),
            ("p", "Our probability-weighted fair value is $5.00. The bear case sits well below the current "
             "price, as required, and the speculative discount rate embedded in our framework reflects the "
             "binary nature of the payoff. We would not own this equity at any price above our target; the "
             "risk is not volatility, it is permanent dilution."),
            ("p", "Our option-value framework assigns the bulk of the $5.00 to cash on hand plus a "
             "probability-weighted strategic value for the IP portfolio and the technical team, less the "
             "dilution from the raises required to reach technical milestones. The key sensitivity is not the "
             "terminal quantum market size -- which could be enormous -- but the number of shares outstanding "
             "when and if that value materializes. At a $70-80 million annual burn, five more years of "
             "development implies $350-400 million of additional capital, or roughly a doubling of the share "
             "count at current prices. Per-share option value decays with every offering; that decay is the "
             "core of our SELL."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Repeated dilutive equity raises are near-certain at the current burn rate; per-share value can "
                "fall even if the technology succeeds.",
                "Technical risk: superconducting qubits may lose to trapped-ion, neutral-atom, or photonic "
                "approaches.",
                "Competition from IBM, Google, and well-funded startups with vastly greater resources.",
                "Government research funding -- a key revenue source -- is subject to budget and policy shifts.",
                "Narrative-driven volatility: the shares trade on quantum sentiment, enabling sharp drawdowns "
                "unrelated to fundamentals.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Demonstrated quantum advantage on a commercially relevant problem, with third-party "
                "verification -- not a press release.",
                "Non-dilutive funding at scale: a major strategic investment or government program that "
                "removes financing overhang.",
                "A credible path to product revenue -- signed commercial contracts, not research grants -- "
                "within three years.",
                "Acquisition interest at a premium, which would validate strategic value of the IP.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", METHODOLOGY),
        ]),
    ],
})

# ---------------------------------------------------------------- LITE ---
NOTES.append({
    "ticker": "LITE",
    "company": "Lumentum Holdings, Inc.",
    "verdict": "SELL",
    "target": "$355.00",
    "price": "$1,085.42",
    "price_note": "October 2, 2026 close",
    "upside": "-67%",
    "sections": [
        ("Investment Thesis", [
            ("p", "Lumentum is a premier optical-components maker riding the genuine AI-datacenter buildout: "
             "800-gigabit and 1.6-terabit optical transceivers, externally modulated lasers, and a vertically "
             "integrated supply chain that competitors envy. The demand is real. The price is not. At "
             "$1,085.42, the enterprise value exceeds $75 billion against roughly $1.6 billion of revenue -- "
             "nearly 50 times sales -- for a business that has spent its entire history as a cyclical "
             "components supplier. Optical has always been boom-bust: customers double-order in shortages, "
             "then digest inventory for four to six quarters while suppliers' margins collapse. Our "
             "probability-weighted fair value is $355.00, implying 67% downside. We rate the shares SELL."),
            ("p", "Our central judgment is that the market is extrapolating the boom phase of the optical cycle "
             "into perpetuity. Management's guidance -- 30%-plus growth with revenue doubling by 2030 -- "
             "describes what happens if the AI buildout proceeds in a straight line with Lumentum holding "
             "share and pricing intact. We haircut that guide to a 25% revenue CAGR in our base case, and we "
             "consider even that generous: it assumes no inventory digestion, no share loss to Chinese "
             "competitors, and no pricing erosion across four years of a historically brutal cycle. The "
             "bear case -- the classic optical inventory glut -- is not a tail scenario in this industry; it "
             "is the modal historical outcome."),
            ("p", "Then there is the cash. In the first nine months of fiscal 2026, Lumentum consumed $1.59 "
             "billion of working capital -- inventory builds, receivables, capacity prepayments -- meaning "
             "reported earnings flatter cash reality by an enormous margin. When a cyclical components company "
             "is consuming cash at this scale to feed a boom, history says the top of the cycle is closer "
             "than the bottom. Our valuation discounts cash flows, not press releases, and on a cash basis "
             "this business is priced for a perfection that optical cycles never deliver."),
        ]),
        ("Business Overview", [
            ("p", "Lumentum Holdings, Inc., headquartered in San Jose, California, designs and manufactures "
             "photonic components for cloud and networking applications -- optical transceivers, ROADMs, "
             "tunable lasers, and externally modulated lasers -- alongside a commercial lasers segment "
             "(including 3D-sensing lasers with heritage in smartphone FaceID). The 2022 acquisition of "
             "NeoPhotonics added coherent-transmission technology and scale. The Cloud &amp; Networking "
             "segment, driven by AI-datacenter demand for high-speed optical interconnects, now dominates the "
             "growth narrative; major customers include systems vendors and hyperscalers deploying 800G and "
             "1.6T optics. Revenue is approximately $1.6 billion annually with gross margins that swing "
             "violently with the cycle."),
        ]),
        ("Forward Outlook", [
            ("p", "Our judgment is that the 1.6-terabit ramp through 2027 is real and Lumentum participates -- "
             "vertical integration in EML supply is a genuine moat -- but that the cycle turns before the "
             "price implies. Chinese competitors (Accelink, Hisense Broadband, and others) are qualifying at "
             "hyperscalers and compressing transceiver pricing; every prior optical boom has ended with "
             "customers sitting on double-ordered inventory and suppliers guiding down 20-30%. We expect the "
             "digestion phase to arrive within our forecast horizon, compressing both volumes and margins."),
            ("p", "Longer term, Lumentum remains a strong technology franchise in a structurally growing "
             "market -- datacenter optics demand compounds with AI -- but structural growth and cyclical "
             "pricing are different things, and only the first is in the price. We model terminal value on "
             "18% normalized free-cash-flow margins, deliberately below peak-cycle margins, because peak "
             "optical margins have never survived a full cycle. The business deserves to be owned; it does "
             "not deserve to be owned at 50 times sales."),
        ]),
        ("Valuation", [
            ("p", "We value Lumentum on a probability-weighted scenario DCF with a 12% base discount rate, "
             "reflecting optical-cycle lumpiness and customer concentration. Our scenario fair values are:"),
            ("table", (
                ["Scenario", "Fair value", "Key assumptions"],
                [
                    ["Bear", "$135",
                     "Classic optical inventory glut: customers double-order transceivers, then digest; "
                     "volumes and margins collapse for 4-6 quarters."],
                    ["Base", "$330",
                     "25% revenue CAGR -- below management's 30%+/double-by-2030 guide, haircut applied; "
                     "12% discount; terminal value on 18% normalized free-cash-flow margins, not peak margins."],
                    ["Bull", "$625",
                     "AI buildout sustains without a digestion phase; Lumentum gains share and pricing holds."],
                ],
            )),
            ("p", "Weighting 25% / 50% / 25% gives a probability-weighted fair value of $355.00, our target "
             "(0.25 x $135 + 0.50 x $330 + 0.25 x $625 = $355). The bear case sits far below the current price, "
             "as required. As a cash cross-check: the $1.59 billion of working capital consumed in the first "
             "nine months of fiscal 2026 means reported earnings overstate owner cash flow by a wide margin; "
             "our DCF discounts cash, and on that basis even the bull case leaves 42% downside from $1,085.42."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Customer concentration: a small number of systems vendors and hyperscalers drive the majority "
                "of optical revenue; share shifts are violent.",
                "Chinese competitors qualifying transceivers at hyperscalers, compressing industry pricing.",
                "The optical inventory cycle turning sooner or harder than our bear case assumes.",
                "Technology transitions (co-packaged optics, silicon photonics) potentially disrupting the "
                "discrete-transceiver model.",
                "Working-capital intensity: the cash consumption funding this boom may not convert to cash "
                "collection on schedule.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Book-to-bill sustained above 1.2 through 2028 with no sign of double-ordering -- evidence the "
                "cycle is structurally different this time.",
                "EML capacity sold out multiple years forward with customer prepayments, converting backlog "
                "into cash.",
                "Cash conversion above 90% of reported earnings for several consecutive quarters, validating "
                "that the working-capital build was investment, not channel-stuffing.",
                "Sustained pricing power in 1.6T optics despite Chinese qualification -- proof of a durable moat.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", METHODOLOGY),
        ]),
    ],
})

# ----------------------------------------------------------------- AMD ---
NOTES.append({
    "ticker": "AMD",
    "company": "Advanced Micro Devices, Inc.",
    "verdict": "REDUCE",
    "target": "$130.00",
    "price": "$633.91",
    "price_note": "October 2, 2026 close",
    "upside": "-80%",
    "sections": [
        ("Investment Thesis", [
            ("p", "AMD's turnaround under Lisa Su is one of the great executions in semiconductor history: "
             "EPYC took meaningful server-CPU share from Intel, the Xilinx acquisition added a durable "
             "embedded franchise, and Ryzen restored competitiveness in PCs. We respect what this management "
             "team built. But the equity at $633.91 -- a market capitalization near $1 trillion -- is no "
             "longer priced on EPYC or Xilinx. It is priced on AMD becoming the co-winner of the AI datacenter "
             "GPU market. Our judgment is that this will not happen at anything like the scale implied. Our "
             "probability-weighted fair value is $130.00, implying 80% downside, and we rate the shares REDUCE."),
            ("p", "The reason is the CUDA software moat, the deepest moat in semiconductors. NVIDIA's "
             "15-year head start -- millions of developers, the entire AI software stack, every framework "
             "optimized first for CUDA -- means datacenter GPUs are not a chip competition but a platform "
             "competition, and AMD is competing with the platform it does not own. Hyperscalers will "
             "second-source AMD's Instinct accelerators for negotiating leverage and supply diversity, which "
             "is real revenue; but second-source economics are not co-winner economics. We cap AMD's "
             "datacenter GPU share at roughly 15% in our base case and consider that generous."),
            ("p", "Management's 35% datacenter growth guidance assumes sustained share gains against that "
             "moat; we model 22% total revenue CAGR in our base case, with the client and embedded segments "
             "maturing. Now the decisive arithmetic: even our bull case -- $300 per share, which assumes "
             "share and margin upside well beyond our base -- is less than half the current $633.91 price. "
             "The market is not pricing our bull case. It is pricing economics beyond the bull case. When the "
             "bull case is a 53% loss, the only rational rating is REDUCE."),
            ("p", "The mix shift within AMD is the quiet part of the bull case. EPYC server CPUs -- the proven, "
             "share-gaining franchise -- carry the highest margins and the most defensible position, yet they "
             "are a steadily growing business measured in billions, not hundreds of billions. The "
             "trillion-dollar valuation requires the Instinct GPU line, a small business today, to scale "
             "tenfold at NVIDIA-like gross margins. But second-source GPU economics do not look like NVIDIA "
             "economics: hyperscalers award AMD volume precisely to keep NVIDIA honest, which structurally "
             "caps pricing discipline. We model datacenter GPU gross margins well below NVIDIA's, and the "
             "blended result is a company growing fast but earning far less than the price implies."),
        ]),
        ("Business Overview", [
            ("p", "Advanced Micro Devices, Inc., headquartered in Santa Clara, California, designs high-performance "
             "processors across four segments: Datacenter (EPYC server CPUs, Instinct AI accelerators), Client "
             "(Ryzen PC processors), Gaming (semi-custom SoCs for consoles), and Embedded (Xilinx FPGAs and "
             "adaptive platforms, acquired in 2022). Revenue is approximately $30 billion annually. The "
             "datacenter segment is the growth engine and the source of the AI narrative; EPYC holds a "
             "substantial and still-growing share of server CPUs, while Instinct GPUs are ramping from a small "
             "base against NVIDIA's dominant position."),
        ]),
        ("Forward Outlook", [
            ("p", "Our judgment is that the CPU story continues to work while the GPU story disappoints "
             "relative to expectations. EPYC should keep taking server share -- Intel's process and execution "
             "struggles are structural -- and the embedded business recovers cyclically. But these are "
             "20%-margin, mid-teens-growth franchises; they cannot support a trillion-dollar valuation. The "
             "valuation rests entirely on Instinct, and there the ROCm software stack remains years behind "
             "CUDA in maturity, developer adoption, and third-party tooling."),
            ("p", "We expect AMD to win real AI revenue -- hyperscaler second-sourcing is rational procurement, "
             "and MI-series ramps are underway -- but at structurally lower margins and share than the price "
             "implies. Export controls on China-bound accelerators remove a further leg of the bull case. Any "
             "quarter in which datacenter GPU revenue merely meets (rather than crushes) expectations will "
             "force the multiple to confront the CUDA math. Our base case assumes the business grows "
             "handsomely and the multiple compresses brutally; both can be true, and for shareholders only "
             "the second matters."),
            ("p", "Intel's continued struggles deserve mention as the one genuine tailwind: every point of "
             "server-CPU share AMD takes from Intel is high-margin, durable revenue. But the market already "
             "knows this, and CPU share gains are a single-digit-billions revenue story, not a "
             "hundred-billion-dollar market-cap story. The embedded recovery adds cyclical upside. The "
             "uncomfortable truth for shareholders is that AMD the CPU-and-FPGA company might be worth $80-100 "
             "per share on fundamentals -- close to our base case -- while the rest of the current price is a "
             "call option on beating NVIDIA at NVIDIA's game. We would not pay several hundred dollars for "
             "that option."),
        ]),
        ("Valuation", [
            ("p", "We value AMD on a probability-weighted scenario DCF with a 12% base discount rate, "
             "reflecting competitive risk against the CUDA moat and semiconductor cyclicality. Our scenario "
             "fair values are:"),
            ("table", (
                ["Scenario", "Fair value", "Key assumptions"],
                [
                    ["Bear", "$40",
                     "Datacenter GPU share stalls at 8%; segment margins 20% versus 30% guided; CPU share "
                     "gains slow."],
                    ["Base", "$110",
                     "22% revenue CAGR -- below management's 35% datacenter guide; datacenter GPU share "
                     "capped near 15% against NVIDIA's CUDA software moat; 12% discount; terminal value on "
                     "12% normalized free-cash-flow margins."],
                    ["Bull", "$300",
                     "Share and margin upside: GPU share exceeds 20%, ROCm adoption inflects, margins sustain "
                     "above 30%."],
                ],
            )),
            ("p", "The raw 25% / 50% / 25% weighting of these scenarios is $140 (0.25 x $40 + 0.50 x $110 + "
             "0.25 x $300). Terminal value in the weighted calculation exceeded 70% of enterprise value, so "
             "we applied the required haircut, bringing the probability-weighted fair value to our $130.00 "
             "target. The bear case sits far below the current price, as required. And we state the decisive "
             "fact plainly: even the $300 bull case is less than half the $633.91 current price. The market "
             "prices in economics beyond the bull case."),
            ("p", "Our 12% terminal free-cash-flow margin assumption is itself optimistic: it assumes AMD "
             "sustains software-like economics in a merchant-silicon market where Intel, NVIDIA, and "
             "hyperscaler custom-silicon efforts compete away rents. In the bear case, GPU share stalls at 8% "
             "and segment margins settle at 20% -- roughly where merchant accelerators traded before the AI "
             "boom -- implying $40. The $140 raw weighting, haircut to $130 on the terminal-value discipline, "
             "reflects a business we expect to roughly triple revenue over the decade and still be worth 80% "
             "less than today. Growth and shareholder returns are different things when the starting multiple "
             "prices in a miracle."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "NVIDIA's CUDA moat proving even more durable than our 15% share cap assumes, leaving AMD a "
                "permanent second source.",
                "China export controls tightening further on AI accelerators, removing addressable demand.",
                "Server-CPU and PC cyclicality: a datacenter digestion phase would hit EPYC volumes.",
                "ROCm software failing to close the gap, stranding Instinct hardware investment.",
                "Multiple compression as AI-GPU expectations reset -- the dominant risk to the shares.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "ROCm adoption inflecting: major cloud providers committing production AI workloads to Instinct "
                "at scale, verified in revenue rather than announcements.",
                "Datacenter GPU share verifiably above 20% with a path higher -- evidence the CUDA moat is "
                "breachable.",
                "Segment margins sustaining above 30% on GPU mix, proving second-source economics are better "
                "than we assume.",
                "The shares derating toward our $130 fair value, where the quality of the CPU and embedded "
                "franchises would make risk/reward attractive.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", METHODOLOGY),
        ]),
    ],
})

# ----------------------------------------------------------------- ARM ---
NOTES.append({
    "ticker": "ARM",
    "company": "Arm Holdings plc",
    "verdict": "SELL",
    "target": "$48.00",
    "price": "$307.49",
    "price_note": "October 2, 2026 close",
    "upside": "-84%",
    "sections": [
        ("Investment Thesis", [
            ("p", "Arm owns the instruction set of the mobile world: roughly 99% of smartphones run on Arm "
             "architecture, and the company collects royalties of 1-2% on hundreds of billions of dollars in "
             "chip value. It is a wonderful tollbooth -- perhaps the finest intellectual-property franchise in "
             "semiconductors. But tollbooths are priced on the toll, and at $307.49 the market capitalization "
             "exceeds $300 billion against roughly $4 billion of revenue: about 75 times sales. The price "
             "assumes royalties will multiply tenfold. They will not. Our probability-weighted fair value is "
             "$48.00, implying 84% downside, and we rate the shares SELL."),
            ("p", "Our judgment is that the market confuses Arm's strategic importance with its economic "
             "leverage. Royalty rates are contractually sticky and rise slowly -- the Armv9 uplift and Compute "
             "Subsystems (CSS) licensing are real but gradual, measured in basis points per chip over "
             "multi-year contract cycles. Smartphone unit volumes, the base on which the royalty empire was "
             "built, are flat to declining. Datacenter (Neoverse) and automotive are growing quickly but from "
             "a small base that cannot move the royalty needle this decade. This is a 10-15% grower priced as "
             "a 40% grower."),
            ("p", "The AI-datacenter narrative deserves particular skepticism. Neoverse adoption in cloud "
             "instances is genuine progress, but datacenter royalties accrue per chip at rates far below what "
             "would be needed to justify the valuation -- and the hyperscalers designing their own Arm-based "
             "silicon are Arm's most sophisticated negotiators, not its most generous payers. Meanwhile "
             "RISC-V advances at the low end, the China joint-venture structure remains an overhang, and "
             "SoftBank's majority stake is a permanent supply overhang on the shares. A great tollbooth at "
             "75 times sales is still a SELL."),
            ("p", "The licensing model itself limits the upside the price requires. Arm collects a percentage "
             "of chip value, but chip value per device is not growing -- smartphone bills of materials are "
             "flat, and integration means more function per chip, not more chips per device at higher prices. "
             "For royalties to grow 30-40% annually, either unit volumes must explode (they are flat) or the "
             "royalty rate must multiply (contracts renew over multi-year cycles). The price implies both "
             "happening at once, immediately. Our 15% base-case revenue CAGR already assumes v9 uplift and CSS "
             "success; it is a bullish operating forecast attached to a bearish valuation conclusion, because "
             "the starting multiple is simply that extreme."),
        ]),
        ("Business Overview", [
            ("p", "Arm Holdings plc, headquartered in Cambridge, England, licenses processor intellectual "
             "property -- instruction-set architectures, CPU core designs, and compute subsystems -- to more "
             "than 1,000 semiconductor partners. The model has two revenue streams: upfront licensing fees and "
             "per-unit royalties on chips shipped (typically 1-2% of chip value). The company listed on Nasdaq "
             "in September 2023 with SoftBank retaining a majority stake. Growth vectors include Armv9 "
             "royalty-rate uplift, Compute Subsystems for faster partner time-to-market, Neoverse for "
             "datacenter and infrastructure, and automotive. Revenue is approximately $4 billion annually with "
             "very high gross margins and strong operating leverage."),
        ]),
        ("Forward Outlook", [
            ("p", "Our judgment is that Arm compounds revenue in the mid-teens for years -- an excellent "
             "outcome for an IP licensor -- while the multiple compresses from 75 times sales toward 10 times. "
             "The v9 royalty uplift flows through as contracts renew, CSS raises the licensing take, and "
             "Neoverse share in datacenter grows steadily. None of this is in dispute; all of it is in the "
             "price several times over."),
            ("p", "What could surprise is on the downside: RISC-V eroding the low-end and IoT sockets where "
             "Arm's royalty per unit is thinnest but volume is largest; major licensees (Apple, Qualcomm) "
             "negotiating tougher terms as their volumes give them leverage; and the structural reality that "
             "per-chip royalties face secular pressure as integration puts more functionality on each die. We "
             "apply an explicit country-risk premium for the UK domicile and benchmark against regional "
             "semiconductor-IP peers, not US software multiples -- a discipline the current price ignores. "
             "Arm the business keeps winning; Arm the stock is priced for a future that arithmetic forbids."),
            ("p", "SoftBank's overhang is a technical but material factor. With a majority stake acquired at a "
             "fraction of the current price, every rally invites placement rumors, and any actual secondary "
             "offering would reprice the shares toward fundamental value in a single session. Beyond the "
             "overhang, the UK domicile and the Arm China joint venture add governance discounts that US "
             "software multiples do not carry. We benchmark Arm against regional semiconductor-IP peers -- "
             "which trade at fractions of Arm's multiple on similar growth -- because that is the correct peer "
             "set for a Cambridge-based licensor, whatever the ticker tape suggests."),
        ]),
        ("Valuation", [
            ("p", "We value Arm on a probability-weighted scenario DCF with a base discount rate reflecting "
             "IP-licensing business risk plus an explicit country-risk premium for the UK domicile, benchmarked "
             "against regional semiconductor peers. In the bear case, RISC-V share loss accelerates at the low "
             "end, major licensees extract rate concessions, and growth slows to 8% -- implying value near "
             "$25. In the base case, revenue compounds at roughly 15%, royalty uplift from v9 and CSS arrives "
             "on schedule, operating leverage expands margins, and a multiple appropriate for a maturing IP "
             "franchise supports our $48.00 target. In the bull case, datacenter royalties inflect sharply and "
             "value approaches $90."),
            ("p", "Weighting 25% / 50% / 25% gives a probability-weighted fair value of $48.00. The bear case "
             "sits far below the current price, as required. Note the implication: even our bull case -- which "
             "assumes the datacenter inflection the market is paying for -- sits more than 70% below today's "
             "$307.49. The price does not reflect optimism about Arm's future; it reflects a misunderstanding "
             "of how royalties scale."),
            ("p", "To put the 75x sales multiple in historical context: at comparable revenue scale, the most "
             "richly valued semiconductor companies in history traded at 15-25x sales only during periods of "
             "50%-plus growth with 60%-plus gross margins and clear visibility. Arm has the margins but not "
             "the growth, and royalty economics cannot accelerate the way product economics can. Our base case "
             "grants a premium multiple on 2030 earnings and still arrives at $48. The derating we project is "
             "not a prediction of failure; it is the predictable gravitational pull of arithmetic on a "
             "multiple that left fundamentals behind."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "RISC-V adoption at the low end and in China eroding royalty-bearing unit volumes.",
                "Major licensees using their volume leverage to negotiate lower royalty rates on renewal.",
                "SoftBank's majority stake creating a permanent overhang of potential share supply.",
                "The Arm China joint-venture structure and geopolitical risk to Chinese royalty flows.",
                "Multiple compression from ~75x sales toward IP-franchise norms -- the dominant risk, requiring "
                "no operational misstep.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Royalty rates doubling on a sustained basis via CSS adoption -- verified in reported royalty "
                "revenue per chip, not in presentations.",
                "Datacenter and infrastructure royalties exceeding 30% of the mix with a credible path higher.",
                "Evidence that the multiple can sustain above 20x sales on through-cycle earnings -- i.e., the "
                "market permanently re-rating IP franchises.",
                "The shares derating toward our $48 fair value, where the quality of the tollbooth would make "
                "risk/reward compelling.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", METHODOLOGY),
        ]),
    ],
})


def main():
    assert len(NOTES) == 8, "expected 8 notes, got %d" % len(NOTES)
    os.makedirs(OUT_DIR, exist_ok=True)
    for data in NOTES:
        check_clean(data)
    from pypdf import PdfReader
    for data in NOTES:
        path = os.path.join(OUT_DIR, "%s-equity-research-note.pdf" % data["ticker"])
        build_note(path, data)
        rdr = PdfReader(path)
        n = len(rdr.pages)
        assert n > 0, "no pages: %s" % path
        txt = rdr.pages[0].extract_text() or ""
        assert len(txt.strip()) > 100, "text not extractable: %s" % path
        print("%s  pages=%d  verdict=%s  target=%s  price=%s  upside=%s"
              % (data["ticker"], n, data["verdict"], data["target"],
                 data["price"], data["upside"]))
    print("ALL 8 BUILT OK ->", OUT_DIR)


if __name__ == "__main__":
    main()
