#!/usr/bin/env python3
"""Standalone equity research PDFs, batch w5: HD, SHOP, SPGI, CDNS, CELH, VST, AXP, NVDA.

Each note is written as a fresh analyst report dated October 4, 2026.
Business facts grounded in company filings and 2026 reporting; prices are
the fixed October 2, 2026 closes from the brief. Targets are authoritative.
"""
import sys
sys.path.insert(0, "/home/hatch/workspace/standalone-notes")
from template import build_note

OUT = "/home/hatch/workspace/standalone-notes/pdfs"

METHODOLOGY_STANDARD = (
    "Our valuation is a probability-weighted scenario DCF. We model bear, base, and bull "
    "cases over an explicit 10-year forecast horizon, weighted 25% / 50% / 25%. Discount "
    "rates are scenario-specific: the base rate reflects fundamental business risk (9% for "
    "stable franchises, 10% standard, 12% or higher for speculative situations); the bear case "
    "adds 250bp, the bull case subtracts 150bp (floor 8%). Terminal value assumes no more than "
    "2.5% perpetual growth applied to normalized mid-cycle margins - never peak margins - and "
    "any terminal value exceeding 70% of enterprise value is haircut and disclosed. Bear cases "
    "are required to be genuinely adverse and to sit below the current price. Management "
    "guidance is never accepted at face value; it is independently tested and haircut where "
    "evidence warrants."
)

METHODOLOGY_COMPOUNDER_HD = (
    "Our valuation is a probability-weighted scenario DCF. Home Depot meets our compounder-quality "
    "criteria, verified from history rather than projected: a 16-year streak (2010-2025) of return "
    "on invested capital above 15%, stable-to-expanding gross margins across the cycle, and "
    "free-cash-flow conversion above 80%. This qualification is not permanent: if ROIC were to fall "
    "below 15% for consecutive fiscal years, if gross margins compressed on a structural rather "
    "than cyclical basis, or if FCF conversion dropped below 80% over a multi-year window, the "
    "qualification would be revoked and the business re-valued at the standard 10% discount rate "
    "over a 10-year horizon. Under the qualification we model bear, base, and bull cases over an "
    "explicit 15-year forecast horizon, weighted 25% / 50% / 25%, with a base discount rate of 8-8.5% "
    "reflecting the genuinely lower risk of predictable cash flows. The bear case adds 250bp and the "
    "bull case subtracts 150bp (floor 8%). Terminal value assumes no more than 3.0% perpetual growth "
    "applied to a demonstrated sustained margin level - not a peak - and any terminal value exceeding "
    "70% of enterprise value is haircut and disclosed. Bear cases are required to be genuinely adverse "
    "and to sit below the current price. Management guidance is never accepted at face value; it is "
    "independently tested and haircut where evidence warrants."
)

METHODOLOGY_COMPOUNDER_CDNS = (
    "Our valuation is a probability-weighted scenario DCF. Cadence meets our compounder-quality "
    "criteria, verified from history rather than projected: a 15-year streak (2011-2025) of return "
    "on invested capital above 15%, stable-to-expanding gross margins across the cycle, and "
    "free-cash-flow conversion above 80%. This qualification is not permanent: if ROIC were to fall "
    "below 15% for consecutive fiscal years, if gross margins compressed on a structural rather "
    "than cyclical basis, or if FCF conversion dropped below 80% over a multi-year window, the "
    "qualification would be revoked and the business re-valued at the standard 10% discount rate "
    "over a 10-year horizon. Under the qualification we model bear, base, and bull cases over an "
    "explicit 15-year forecast horizon, weighted 25% / 50% / 25%, with a base discount rate of 8-8.5% "
    "reflecting the genuinely lower risk of predictable cash flows. The bear case adds 250bp and the "
    "bull case subtracts 150bp (floor 8%). Terminal value assumes no more than 3.0% perpetual growth "
    "applied to a demonstrated sustained margin level - not a peak - and any terminal value exceeding "
    "70% of enterprise value is haircut and disclosed. Bear cases are required to be genuinely adverse "
    "and to sit below the current price. Management guidance is never accepted at face value; it is "
    "independently tested and haircut where evidence warrants."
)

# ---------------------------------------------------------------- HD
hd = {
    "ticker": "HD",
    "company": "The Home Depot, Inc.",
    "verdict": "HOLD",
    "target": "$268.00",
    "price": "$282.85",
    "price_note": "October 2, 2026 close",
    "upside": "-5%",
    "sections": [
        ("Investment Thesis", [
            ("p", "Home Depot is the best home-improvement retailer in the world, and the stock is priced as though that statement alone settles the investment question. It does not. A 16-year streak of returns on invested capital above 15%, gross margins that have held at roughly 33% through every housing cycle of the last decade and a half, and free-cash-flow conversion above 80% make this one of the highest-quality businesses in American retail. Quality of that order deserves a premium multiple. It does not deserve the assumption that the cycle cooperates."),
            ("p", "The cycle is not cooperating. Existing-home turnover sits near historic lows, roughly 3% of the housing stock, with 30-year mortgage rates still near 6.6%. Management itself describes a frozen housing market. When homes do not change hands, the move-driven big-ticket projects - kitchens, additions, full renovations - that carry the highest tickets and the best margins simply do not get scheduled. Homeowners are healthy and spending, but they are spending on smaller maintenance and repair jobs while deferring the large discretionary work. The second quarter of fiscal 2026 delivered a four-year high in comparable sales and a genuine beat, and management reaffirmed rather than raised full-year guidance - comps flat to up 2%, total sales growth 2.5% to 4.5%, adjusted EPS growth of flat to 4% off a $14.69 baseline. The reaffirmation is the honest tell: the company does not trust the housing market to deliver a second-half acceleration, and neither should investors."),
            ("p", "Our judgment is that Home Depot's long-term economics are intact and underappreciated in the bearish narrative, but the next twelve months belong to the cycle, not to the franchise. The pro-customer pivot - roughly half of revenue, the $18.25 billion SRS Distribution acquisition, GMS, and a stated addressable pro market of around $700 billion - is the right strategic answer to a world in which the DIY homeowner defers. It will, however, take years to build the full capability to win that share, as management concedes, and the acquired businesses carry lower margins than the core retail box. We value the company on a probability-weighted scenario DCF that gives the 15-year compounder-quality treatment its history has earned, and the answer is fair value of $268 against a $282.85 price. That is a HOLD: a superb business at a full price, with the upside reserved for the eventual housing-turnover recovery, which remains a 2027-or-later story."),
            ("p", "The asymmetry matters. The bear case - housing stays frozen for two more years, big-ticket comps stay negative, and the pro build-out dilutes margins longer than expected - would take the stock well below our target. The bull case - mortgage rates break below 6% and turnover normalizes - produces mid-teens upside. But at this price investors are paying for an earnings recovery that management's own guidance says is not yet visible. We would add on genuine weakness; at $282.85 we wait."),
        ]),
        ("Business Overview", [
            ("p", "The Home Depot is the world's largest home-improvement retailer, operating roughly 2,360 stores across the United States, Canada, and Mexico. The business serves two customer types: the do-it-yourself homeowner and the professional contractor - the pro. Pros now account for roughly half of revenue, a deliberate and growing mix, and they are served through dedicated pro desks, direct fulfillment, and a trade distribution network built up through acquisitions."),
            ("p", "Fiscal 2025 (ended February 1, 2026) produced net sales of $164.7 billion, up 3.2%, with comparable sales of 0.3% and diluted earnings per share of $14.23 on a GAAP basis ($14.69 adjusted). Gross margin ran at approximately 33.1%, and operating margin guidance for fiscal 2026 sits at 12.4% to 12.6% - compressed relative to history by the mix shift toward the acquired distribution businesses and by continued investment in the pro ecosystem. Return on invested capital, which has exceeded 15% every year since 2010, was 25.4% in the first quarter of fiscal 2026. The company paid about $2.3 billion in dividends in that quarter alone and continues an aggressive, decades-long capital-return program funded by genuinely prodigious cash generation."),
            ("p", "The strategic centerpiece is the pro pivot. The March 2024 acquisition of SRS Distribution for $18.25 billion gave Home Depot a serious position in specialty trade distribution - roofing, pool, and landscaping supply - and the subsequent acquisition of GMS extended that reach. The company is adding 40 to 50 new SRS branches a year, opened 12 new stores in the first quarter of fiscal 2026, and points to a total pro addressable market of roughly $700 billion. The logic is sound: pro demand is steadier than DIY through cycles, pros buy on a recurring job-driven cadence, and Home Depot's scale in procurement and logistics gives it structural advantages over fragmented regional distributors. But it is a multi-year build, the acquired revenue carries thinner margins than the core box, and the balance sheet now carries the leverage those acquisitions required."),
        ]),
        ("Forward Outlook", [
            ("p", "Our base expectation is that fiscal 2026 and 2027 are transition years, not recovery years. The housing lock-in - tens of millions of homeowners holding mortgages at 3-4% who cannot afford to move at 6.6% rates - is a structural feature of this cycle, not a sentiment blip. Until turnover normalizes, big-ticket comps stay soft and the company's growth comes from market-share gains in a weak market, new stores and branches, and the acquired SRS/GMS revenue layering in. That is a recipe for low-single-digit sales growth and flat-to-modestly-up earnings, which is exactly what guidance describes. We take management at its word when it refuses to raise the guide after a strong quarter."),
            ("p", "Where we differ from the more bearish camp is on the durability of the franchise through this trough. Home Depot is taking share - its on-shelf availability, supply chain, and pro capabilities widen the gap with weaker competitors precisely when the market is weakest. The pro pivot is not a defensive crouch; it is an offensive build of the industry's best distribution platform for contractors, and the $700 billion addressable market means even modest share gains compound into very large revenue. Gross margin stability near 33% through this softness is the empirical proof that pricing power is intact. When turnover eventually normalizes - our working assumption is a gradual thaw beginning in 2027, not a snap-back - the operating leverage on the other side is real, and the pro business will be a larger, stickier, more recurring portion of the mix."),
            ("p", "The honest risk to this outlook is duration. A frozen housing market can stay frozen longer than equity investors' patience, and every quarter of flat comps is a quarter in which the market questions whether the multiple is earned. Tariff-related cost pressures - visible in the IEEPA tariff refunds embedded in fiscal 2026 guidance, which are offsetting unplanned fuel and input costs - are a reminder that the cost structure is not immune to policy shocks. Our judgment: the business will be larger and better in five years; the stock, at 19-20x earnings on trough-adjacent EPS, offers little compensation for the wait."),
        ]),
        ("Valuation", [
            ("p", "Home Depot qualifies for our compounder-quality treatment: 16 consecutive years of ROIC above 15% (2010-2025), stable-to-expanding gross margins, and free-cash-flow conversion above 80%, all verified from reported history. We therefore model a 15-year explicit horizon at an 8-8.5% base discount rate, with terminal growth capped at 3.0% applied to a demonstrated sustained margin - not a cyclical peak. The bear case adds 250bp, the bull case subtracts 150bp with an 8% floor, and the three scenarios are weighted 25% / 50% / 25%."),
            ("p", "The bear case assumes the housing freeze extends through 2028: existing-home turnover stays near 3%, big-ticket comps remain negative, SRS organic growth disappoints, and the pro build-out dilutes consolidated margins for longer than guided. Earnings power in this scenario sits well below the current price, as a bear case must. The base case assumes a gradual turnover thaw from 2027, low-single-digit comp growth through the explicit period, pro revenue compounding as the trade-distribution platform scales, and operating margins recovering toward the mid-teens as mix and leverage normalize - with no heroics on the multiple. The bull case assumes mortgage rates break durably below 6% by 2027, turnover normalizes faster, big-ticket deferred demand releases in a wave, and the pro platform captures share faster than our base assumption."),
            ("p", "The probability-weighted fair value is $268.00, our target, against the October 2, 2026 close of $282.85 - implying about 5% downside. The valuation says what the business says: this is a wonderful company whose economics are temporarily masked by the cycle, and the market has already paid for the recovery before it has arrived. We would become buyers on a genuine washout toward the bear-case zone; at current levels the risk-reward is balanced to mildly negative."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Housing-cycle duration: existing-home turnover could remain depressed well beyond 2027 if mortgage rates stay elevated, pushing the big-ticket recovery - and the earnings leverage that comes with it - further out.",
                "Pro-build execution: the SRS and GMS integrations, plus 40-50 new branches a year, must deliver mid-single-digit organic growth at acceptable margins; the acquired distribution businesses are structurally lower-margin than the core box.",
                "Tariff and input-cost pressure: fiscal 2026 guidance leans on IEEPA tariff refunds to offset unplanned fuel and product input costs - a one-time offset against a recurring cost risk if trade policy tightens further.",
                "Leverage: the balance sheet carries the debt taken on for SRS and GMS; a prolonged soft patch would slow deleveraging and constrain buyback capacity.",
                "DIY demand softness: consumer confidence is fragile and discretionary spending on large projects is the first thing deferred in a downturn; a consumer recession would hit comps harder than the base case assumes.",
                "Competitive response: Lowe's and the independent pro dealers are not standing still, and share gains claimed in a weak market need Lowe's own results to confirm them.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "A decisive turn in housing turnover - existing-home sales rising on a sustained basis with mortgage rates breaking below 6% - would pull forward the big-ticket recovery and justify a higher multiple on the earnings power we model.",
                "SRS delivering sustained high-single-digit organic growth with margins converging toward the core box would validate the pro-platform thesis ahead of our timeline.",
                "A sharp selloff on cyclical fears (toward $230 or below) with fundamentals intact would flip the risk-reward to positive and move us to BUY.",
                "Conversely, ROIC falling below 15% for consecutive years, structural gross-margin compression, or FCF conversion dropping below 80% over a multi-year window would revoke the compounder-quality assumptions and force a lower fair value.",
                "Evidence that the pro pivot is destroying rather than creating value - persistent margin dilution with no share gains - would undermine the central strategic thesis.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", METHODOLOGY_COMPOUNDER_HD),
        ]),
    ],
}

# ---------------------------------------------------------------- SHOP
shop = {
    "ticker": "SHOP",
    "company": "Shopify Inc.",
    "verdict": "HOLD",
    "target": "$137.00",
    "price": "$151.39",
    "price_note": "October 2, 2026 close",
    "upside": "-10%",
    "sections": [
        ("Investment Thesis", [
            ("p", "Shopify is executing at a level that few large-cap software companies can match. Five consecutive quarters of 30%+ growth across GMV, revenue, gross profit, operating income, and free cash flow is a genuine rarity at this scale: second-quarter 2026 revenue of $3.58 billion grew 33.7%, GMV reached $115.6 billion up 31.6%, and free-cash-flow margin hit 18%. The business has compounded from a toolkit for small merchants into the operating system for independent commerce - payments penetration at 68% of GMV, Shop Pay past $400 billion in lifetime volume, enterprise logos like Guess, Avon, Arhaus, and e.l.f. Cosmetics migrating onto Shopify Plus, B2B GMV up 76%, international GMV up 37%. This is a superb company, and the market knows it."),
            ("p", "Knowing it is the problem. At $151.39, the stock prices a long runway of 25%+ growth with continued margin expansion, and that is a demanding setup for a business whose core economics are still tethered to the volume of stuff sold through its merchants' storefronts. Shopify's take rate expands as payments penetration rises and as merchants adopt more financial services, but the merchant-solutions engine is fundamentally a toll on GMV growth - and GMV growth is ultimately a function of consumer spending, e-commerce penetration, and competitive share. The agentic-commerce narrative - Sidekick, Catalog, AI-driven storefronts, 36,000 Sidekick-enabled apps - is real product progress, but it is not yet a monetized revenue stream, and we are skeptical that AI assistants disintermediate checkout in ways that accrue to Shopify rather than to the model providers."),
            ("p", "Our judgment is that Shopify's fair value, on a probability-weighted scenario DCF, is $137 - about 10% below the current price. The base case gives the company full credit for durable mid-20s revenue growth, continued take-rate expansion as payments penetration marches toward the 70s, and operating margins that keep expanding as the post-logistics-divestiture cost structure scales. The bear case, which sits below the price as it must, contemplates GMV deceleration as e-commerce penetration growth normalizes, take-rate expansion stalling as large enterprise merchants negotiate economics, and the AI-commerce surface monetizing slower than hoped. We rate the stock HOLD: we would not sell a compounder of this quality into strength, but we cannot recommend buying a 30% grower at a price that assumes the growth never moderates."),
        ]),
        ("Business Overview", [
            ("p", "Shopify provides the commerce platform on which millions of merchants in more than 175 countries run their businesses - online storefronts, point-of-sale, B2B wholesale, and increasingly the financial services layered on top. Revenue comes in two streams. Subscription Solutions ($802 million in Q2 2026, up 22.3%) is the SaaS rent merchants pay for the platform, with monthly recurring revenue of $221 million growing 19% and Shopify Plus accounting for about a third of MRR. Merchant Solutions ($2.78 billion, up 37.4%, now 78% of revenue) is the larger and faster-growing stream: payments processing, currency conversion, Shop Pay, capital lending, and partner referrals - effectively a take rate on the GMV flowing through the platform."),
            ("p", "The flywheel is straightforward and powerful. More merchants and more GMV widen the base on which Shopify earns payments and financial-services revenue; rising payments penetration (68% of GMV in Q2 2026, up from 60% in early 2024) mechanically expands the take rate; the resulting cash funds product investment that attracts larger merchants. Full-year 2025 revenue was $11.6 billion, up 30%, on GMV of $378 billion, up 29%. The company is solidly profitable on a GAAP basis, generates strong free cash flow, and carries a fortress balance sheet. Retention among scaled merchants is excellent - 92% for merchants doing over $1 million in GMV, 97% above $10 million."),
            ("p", "The frontier of the story is upmarket and international. Enterprise migrations - Guess, Avon, Fred Segal, Holt Renfrew, Country Road, Aritzia, Claire's, Suitsupply named in recent quarters - validate Shopify Plus as a legitimate enterprise commerce platform, not just an SMB tool. International GMV grew 37% in Q2 2026, Shopify Payments is now in 40 countries, and offline (POS) GMV grew 32%. The newest vector is agentic commerce: Sidekick daily active merchants up 3.6x year over year, nearly 34 million Sidekick conversations handled in the quarter, and a product catalog of over a billion items positioned as the structured data layer that AI shopping agents will need."),
        ]),
        ("Forward Outlook", [
            ("p", "Our forward view is that Shopify keeps growing fast but the rate of growth moderates from the mid-30s toward the low-20s over the next several years, and the market's implicit forecast does not yet allow for that moderation. The mechanics are arithmetic: GMV of $378 billion in 2025 growing at 30% adds more than $110 billion of incremental volume a year, and sustaining that percentage growth requires the company to keep finding new GMV pools - enterprise, B2B, international, offline - faster than the core matures. It is doing exactly that today, which is why the numbers are so strong, but each successive pool is harder-won and lower-take-rate than the last."),
            ("p", "On the positive side, we believe the payments-led take-rate expansion has further to run. Payments penetration at 68% still has headroom toward the levels seen in mature markets, Shop Pay's 53% growth shows the consumer wallet product compounding, and the capital-lending book ($2.18 billion with manageable delinquency migration) is an underappreciated high-return asset. The enterprise migration is early - the named wins are real but small relative to the opportunity - and international remains under-penetrated. If agentic commerce becomes a genuine transaction channel rather than a discovery layer, Shopify's billion-product catalog is the best-structured inventory feed in the industry, and the company would be a natural toll collector."),
            ("p", "Our skepticism concentrates on two points. First, the AI-commerce monetization path is unproven: an AI agent that comparison-shops across merchants compresses rather than expands take rates, and the value could accrue to the agent operator. Second, Shopify's valuation leaves no room for the law of large numbers. A 30% grower at this price must remain a 25%+ grower for the better part of a decade to earn its multiple; the history of platform companies says the deceleration arrives sooner and faster than bulls expect. We admire the execution enormously. We simply cannot underwrite the price."),
        ]),
        ("Valuation", [
            ("p", "We value Shopify on a probability-weighted scenario DCF over an explicit 10-year horizon, weighted 25% / 50% / 25%, with a standard 10% base discount rate reflecting the combination of a strong competitive position and the inherent cyclicality of a GMV-tethered business. The bear case adds 250bp, the bull case subtracts 150bp with an 8% floor. Terminal growth is capped at 2.5% on normalized mid-cycle margins, and terminal value is haircut where it exceeds 70% of enterprise value."),
            ("p", "The bear case, which sits below the current price, assumes GMV growth decelerates into the mid-teens as e-commerce penetration gains slow, take-rate expansion stalls as enterprise mix dilutes the blended rate and large merchants negotiate, and agentic commerce monetizes slowly - leaving revenue growth in the low teens by the end of the decade with margins expanding less than the market expects. The base case credits the company with mid-20s revenue growth moderating to the high teens, payments penetration rising into the mid-70s, continued operating leverage toward best-in-class SaaS margins, and a durable moat in the independent-commerce ecosystem. The bull case assumes the enterprise migration and international expansion together sustain 25%+ growth for most of the decade, agentic commerce becomes a real transaction toll, and Shopify emerges as the default infrastructure for AI-mediated shopping."),
            ("p", "The probability-weighted fair value is $137.00, our target, against the October 2, 2026 close of $151.39 - about 10% downside. The message of the valuation is not that Shopify is a bad business; it is one of the best. It is that the market has already capitalized a decade of excellent execution, and excellent execution from here is the base case, not the upside."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "GMV deceleration: e-commerce penetration growth is normalizing; a consumer slowdown or share loss would hit the merchant-solutions take rate directly, since 78% of revenue is volume-tethered.",
                "Take-rate pressure: as enterprise merchants become a larger share of GMV, their negotiating leverage on payments and subscription economics could stall or reverse the take-rate expansion the valuation depends on.",
                "Agentic-commerce disintermediation: if AI shopping agents become the customer interface, the checkout toll could compress or migrate to the agent operator rather than the platform.",
                "Competition: entrenched enterprise platforms, payment processors building commerce tooling, and marketplace giants all contest pieces of the stack.",
                "Valuation: the stock embeds a long runway of 25%+ growth; any sustained deceleration would likely re-rate the multiple, not just the growth rate.",
                "International execution: payments expansion across 40 countries brings regulatory, fraud, and localization complexity that has tripped up fintech expanders before.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Evidence that agentic commerce is a monetizable transaction channel - measurable GMV and take rate flowing through AI-driven surfaces - would raise the terminal growth and duration assumptions materially.",
                "Sustained 30%+ revenue growth with expanding margins for another two to three years would prove the law of large numbers wrong and justify a higher fair value.",
                "A meaningful pullback (toward $110-115) on sentiment rather than fundamentals would flip the risk-reward and move us to BUY.",
                "Conversely, GMV growth decelerating into the teens while the multiple holds would confirm the overvaluation thesis and could move us to REDUCE.",
                "Deterioration in merchant retention among scaled cohorts (below 90% for $1M+ GMV merchants) would signal the moat is weakening.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", METHODOLOGY_STANDARD),
        ]),
    ],
}

# ---------------------------------------------------------------- SPGI
spgi = {
    "ticker": "SPGI",
    "company": "S&P Global Inc.",
    "verdict": "REDUCE",
    "target": "$341.00",
    "price": "$386.27",
    "price_note": "October 2, 2026 close",
    "upside": "-12%",
    "sections": [
        ("Investment Thesis", [
            ("p", "S&P Global owns some of the finest tollbooths in global finance. The Ratings division - a regulated oligopoly shared with Moody's - just posted a record quarter with revenue up 17% and an adjusted operating margin of 68.5%. S&P Dow Jones Indices delivered its 13th consecutive record quarter, up 20%, riding ETF asset growth that compounds with equity markets. Adjusted operating margin for the whole company expanded to 54.3% in the second quarter of 2026. These are extraordinary economics, and the July 2026 spin-off of the Mobility division sharpens the portfolio around benchmarks and data. We do not dispute the quality. We dispute the price."),
            ("p", "The dispute is straightforward: at $386.27, S&P Global trades at roughly 22 times trailing earnings and a mid-20s multiple of the $17.50-$17.75 adjusted EPS guidance for 2026, for a business whose growth is mid-to-high single digits through the cycle and whose two crown jewels are deeply cyclical. Ratings transaction revenue - up 25% in the quarter - is a leveraged bet on debt issuance volumes, which are currently running hot: U.S. rated issuance up 26%, Europe up 12%, Asia up 49%. Issuance booms do not last; they are followed, with historical regularity, by issuance droughts. Indices revenue is a leveraged bet on equity market levels and ETF flows. Both engines are firing at once right now, which is exactly when cyclical businesses look cheapest on trailing numbers and are in fact most expensive on normalized earnings."),
            ("p", "Our judgment is that the market is capitalizing peak-cycle earnings at a structural-growth multiple. On a probability-weighted scenario DCF - 10-year horizon, 9% base discount rate reflecting the stability of the benchmark franchises, bear +250bp, bull -150bp - fair value is $341, about 12% below the current price. The base case gives full credit for the benchmark moats: Ratings growing with global debt markets, Indices compounding with ETF assets, Market Intelligence grinding out mid-single-digit growth, and margins staying in the low-50s. But it refuses to project the current issuance boom forward, and it haircuts terminal value where peak margins inflate it. We rate the stock REDUCE: a wonderful business at a price that assumes the cycle never turns. Investors who own it for the quality should understand they are paying a growth multiple for cyclical earnings."),
        ]),
        ("Business Overview", [
            ("p", "S&P Global is a financial-information and analytics company organized, following the July 2026 spin-off of Mobility into the independent Mobility Global, around four divisions: Ratings, S&P Dow Jones Indices, Market Intelligence, and Energy (the former Commodity Insights). The benchmark businesses - Ratings and Indices - are the profit engine: in the second quarter of 2026 they generated the overwhelming majority of operating profit on margins that most companies cannot approach."),
            ("p", "Ratings ($1.34 billion revenue in Q2 2026, up 17%) is one half of the global credit-ratings duopoly. Revenue splits between transaction fees tied to new debt issuance and stickier non-transaction revenue - surveillance, entity ratings, and data feeds. The division's operating margin approaches 70% because the marginal cost of rating one more bond is near zero and the regulatory barriers to entry are formidable. S&P Dow Jones Indices ($534 million, up 20%, its 13th straight record quarter) earns asset-based fees on ETFs and indexed products benchmarked to its indices - most famously the S&P 500 - plus licensing and data revenue. It is a royalty on the growth of passive investing."),
            ("p", "Market Intelligence ($1.29 billion, up 6-7%) sells data, research, and workflow tools - Capital IQ Pro, data feeds, and increasingly AI-enabled offerings, with management citing 500+ customers on LLM-ready APIs and MCP-connected solutions. Energy ($568 million, up low-single digits) provides commodity price assessments and analytics. The company returned capital aggressively, raising its 2026 buyback target to more than $7 billion, and pays a quarterly dividend. Trailing GAAP EPS is about $14.65, and the balance sheet is investment-grade with manageable leverage following the IHS Markit integration."),
        ]),
        ("Forward Outlook", [
            ("p", "Our forward view is that S&P Global's next three years look meaningfully worse than its last three, not because the moats are breached but because the cycle turns. Debt issuance is running at record levels partly because borrowers are pulling forward refinancing ahead of rate and policy uncertainty; the forward calendar cannot sustain 26% U.S. issuance growth indefinitely. When issuance normalizes - as it always does - Ratings transaction revenue, the highest-margin revenue in the company, decelerates sharply, and the operating leverage works in reverse. This is not a prediction of distress; it is the ordinary rhythm of a ratings cycle, and the stock's multiple does not discount it."),
            ("p", "The structural positives are real and we weight them fully. Passive investing's share of equity assets keeps rising, which compounds Indices revenue with a multi-decade tailwind. The Mobility spin-off leaves a cleaner, higher-margin portfolio. AI offerings in Market Intelligence - the LLM-ready APIs growing 5x in call volume - could reaccelerate a division that has grown in the mid-single digits and disappointed growth investors before. Management's capital allocation is shareholder-friendly: a $7 billion-plus buyback at these prices retires meaningful share count, and the dividend grows. Our base case assumes the company compounds revenue at 6-8% and EPS at a low-teens rate through buybacks and margin discipline - a perfectly good outcome that the current price already more than reflects."),
            ("p", "Where we are most cautious is the market's treatment of this business as a secular compounder deserving a 25x-plus multiple. It is a cyclical compounder: the compounding happens across cycles, but within a cycle the earnings are volatile and the multiple should reflect that. Buying S&P Global at peak issuance, peak ETF inflows, and peak margins is buying the top of all three cycles simultaneously. Our judgment: wait for the issuance drought, when the stock will be offered 20-30% lower on transiently depressed earnings, and buy the moat then."),
        ]),
        ("Valuation", [
            ("p", "We value S&P Global on a probability-weighted scenario DCF over an explicit 10-year horizon, weighted 25% / 50% / 25%. The base discount rate is 9%, reflecting the genuine stability of the benchmark franchises - a notch below our standard 10% because the duopoly and index-royalty economics are unusually defensible. The bear case adds 250bp, the bull case subtracts 150bp with an 8% floor. Terminal growth is capped at 2.5% on normalized mid-cycle margins - critically, not on today's 54%+ company margins or the 68.5% Ratings margin, which reflect peak-cycle issuance - and terminal value exceeding 70% of enterprise value is haircut and disclosed."),
            ("p", "The bear case, which sits below the current price, models a genuine issuance downturn: refinancing walls pass, rates stay higher for longer, transaction revenue contracts, and Ratings margins compress from the high-60s toward the high-50s; Indices revenue stalls in a flat equity market; Market Intelligence growth stays muted. The base case assumes issuance normalizes gradually rather than collapsing, Indices compounds with mid-single-digit ETF asset growth, Market Intelligence accelerates modestly on AI offerings, and company margins settle in the low-50s - still elite, but below today's peak. The bull case assumes the issuance boom extends, passive share gains accelerate, and AI data products open a genuinely new high-margin revenue stream."),
            ("p", "The probability-weighted fair value is $341.00, our target, against the October 2, 2026 close of $386.27 - about 12% downside. The valuation's message is that peak-cycle earnings capitalized at a structural multiple is the classic value trap for quality cyclicals, and S&P Global is exhibiting all the symptoms."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Issuance cyclicality: a sharp drop in global debt issuance would hit Ratings transaction revenue - the company's highest-margin line - and operating leverage would magnify the earnings decline.",
                "Equity-market dependence: Indices revenue is a royalty on asset levels; a sustained bear market in equities would stall the division's record run.",
                "Regulatory risk: credit ratings remain a regulated activity; adverse regulatory changes in the U.S. or EU could constrain pricing or liability.",
                "Market Intelligence execution: the division has a history of mid-single-digit growth that disappoints; the AI product push must convert pilots into revenue.",
                "Capital allocation at the top: the $7 billion-plus buyback retires fewer shares at $386 than it would in a downturn; aggressive repurchases at peak multiples destroy the per-share compounding the program is meant to create.",
                "Passive-concentration: the Indices moat depends on continued passive share gains; any structural shift in how investors allocate could slow the royalty.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "A genuine issuance downturn that takes the stock 20-30% lower on depressed earnings - without impairing the duopoly - would make the moat buyable at a cyclical multiple and move us to BUY.",
                "Evidence that Market Intelligence AI offerings are a real growth engine - sustained double-digit organic growth in the division - would raise our through-cycle growth assumption.",
                "A structural, defensible acceleration in Ratings non-transaction revenue (surveillance, data, analytics) that de-cyclicalizes the division would justify a higher multiple.",
                "Conversely, confirmation that issuance has peaked while the multiple stays elevated would strengthen the REDUCE thesis.",
                "Any regulatory action that impairs the ratings oligopoly economics would force a fundamental reassessment of the moat.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", METHODOLOGY_STANDARD),
        ]),
    ],
}

# ---------------------------------------------------------------- CDNS
cdns = {
    "ticker": "CDNS",
    "company": "Cadence Design Systems, Inc.",
    "verdict": "HOLD",
    "target": "$308.00",
    "price": "$351.35",
    "price_note": "October 2, 2026 close",
    "upside": "-12%",
    "sections": [
        ("Investment Thesis", [
            ("p", "Cadence is the purest software toll on the AI hardware buildout, and its business quality is beyond dispute: 15 consecutive years of return on invested capital above 15% (2011-2025), gross margins that have expanded steadily into the high-80s on the software mix, free-cash-flow conversion above 80%, and a record $8.1 billion backlog with $4.2 billion converting to revenue within twelve months. Second-quarter 2026 revenue grew 24.2% to $1.584 billion, non-GAAP operating margin hit 45.5%, and management raised full-year guidance to $6.26-$6.34 billion of revenue and $8.05-$8.15 of adjusted EPS. Every chip that matters - AI accelerators, hyperscaler silicon, leading-edge mobile - is designed on Cadence or Synopsys tools. This is a structural winner, and we treat it as one."),
            ("p", "But structural winners get priced as though structure means certainty, and the current price of $351.35 embeds a growth trajectory that the semiconductor cycle has never once delivered smoothly. Cadence's revenue is ultimately a function of semiconductor R&D spending, which is cyclical with a capital-S: customers' R&D budgets expand in booms and get scrutinized in downturns, EDA spending lags chip downturns by a few quarters, and the current AI-driven R&D supercycle is concentrating growth in a handful of hyperscaler and AI-accelerator customers whose spending plans can pivot. The stock has already corrected about 32% from its 52-week high of $416.69 - the market is telling you something about how it prices the cycle - and even after that correction, the multiple assumes the AI R&D boom extends deep into the decade."),
            ("p", "Our judgment, on a probability-weighted scenario DCF with the 15-year compounder-quality treatment the company's history has earned (8-8.5% base discount rate, 3.0% terminal growth cap on demonstrated sustained margins), is fair value of $308 - about 12% below the current price. The base case is genuinely bullish on the business: EDA grows as a share of semis R&D, agentic AI design tools (ChipStack, ViraStack, AuraStack) expand consumption of Cadence's engines rather than cannibalizing seats, the IP and System Design & Analysis businesses keep compounding at 30%+, and margins stay in the mid-40s. The bear case - which sits below the price, as required - models the R&D cycle turning: hyperscaler silicon programs pause, China export controls bite harder, and the multiple compresses as growth decelerates. We rate the stock HOLD: own the compounder, but do not chase it 12% above fair value into a cyclical peak in customer R&D spending."),
        ]),
        ("Business Overview", [
            ("p", "Cadence Design Systems is one of two dominant electronic design automation (EDA) vendors - the other being Synopsys - providing the software that the semiconductor industry uses to design, verify, and simulate chips and electronic systems. The product portfolio spans Core EDA (digital and custom/analog design, including the Virtuoso, Innovus, and Genus platforms), Functional Verification (the Palladium hardware emulation family), semiconductor IP (memory, interface, and connectivity blocks), and System Design & Analysis (multiphysics simulation for 3D-IC, thermal, and electromagnetic effects). Roughly three-quarters of revenue is recurring, and the backlog-driven model gives unusual forward visibility."),
            ("p", "The financial profile is elite-software economics. Second-quarter 2026 revenue of $1.584 billion grew 24.2% year over year, with Core EDA up 18%, IP up more than 40%, and System Design & Analysis up 37% (helped by the BETA CAE and Hexagon Design & Engineering acquisitions). Non-GAAP operating margin was 45.5%, free cash flow was $582 million in the quarter, and the company ended June with $1.44 billion in cash. Customers include Nvidia, Apple, and effectively every leading-edge chipmaker and systems company. The TSMC relationship deepened through 2026 with tool certifications across the A14 (1.4nm) and N2P nodes and expanded 3DFabric support - table stakes in the foundry-duopoly world, but Cadence holds its seat at the table."),
            ("p", "The strategic frontier is AI for design. Cadence's agentic tools - ChipStack, ViraStack, and the AuraStack 'super agent' launched in 2026 - let engineers describe design goals in plain language while the agents run hundreds of parallel iterations on Cadence's physically accurate engines. Management's disclosed insight is important: autonomous agents increase consumption of the underlying EDA engines rather than cannibalizing seat licenses, because every agent iteration burns compute on licensed solvers. If that dynamic holds, agentic AI is a demand accelerator for the core franchise, not a disruption of it. The offsetting overhangs: the Hexagon D&E integration is diluting near-term margins (roughly $0.28 of 2026 EPS impact), China export-control policy remains a swing factor for a meaningful revenue geography, and Synopsys - now larger after closing the Ansys acquisition in July 2025 - is a well-armed competitor across the full stack."),
        ]),
        ("Forward Outlook", [
            ("p", "Our forward view is that Cadence grows revenue in the mid-teens through the decade in the base case, driven by three durable forces: AI-accelerator and hyperscaler silicon programs expanding the leading-edge design-start pool, EDA's share of semiconductor R&D spend continuing its decades-long creep upward as complexity rises, and the IP and multiphysics businesses compounding faster than core EDA. The $8.1 billion backlog - more than a full year of revenue, with $4.2 billion converting in twelve months - underwrites the near term almost mechanically. This is why the business earns the compounder-quality assumptions: the revenue visibility is contractual, the switching costs are measured in years of methodology investment, and no startup is displacing a duopoly entrenched in every leading fab's reference flow."),
            ("p", "The cycle is the caveat, and it is a large one. Semiconductor R&D spending is growing at an extraordinary rate because a small number of very large customers are in an arms race; arms races end, pause, or consolidate. When they do, EDA feels it with a lag but feels it fully - design starts get pushed, IP licensing slows, and hardware emulation purchases defer. Our base case assumes the current R&D supercycle moderates rather than collapses, with growth stepping down from the 20%+ of 2026 toward the low teens by the end of the decade. We do not assume a semiconductor downturn in the base case, which is itself a generous assumption given the industry's history of one every few years."),
            ("p", "On agentic AI we take management's demand-accelerator claim seriously but haircut the monetization timeline. The mechanism - agents burning licensed solver compute - is economically sound, but pricing models for agent-driven consumption are still being invented, and customers will negotiate. The Hexagon integration should be accretive by 2027-2028 as cost synergies land and the multiphysics portfolio cross-sells into the core EDA installed base. Net: a business we would love to own at the right price, growing into a valuation that currently assumes the R&D cycle has been repealed."),
        ]),
        ("Valuation", [
            ("p", "Cadence qualifies for our compounder-quality treatment: 15 consecutive years of ROIC above 15% (2011-2025), stable-to-expanding gross margins, and free-cash-flow conversion above 80%, all verified from reported history. We therefore model a 15-year explicit horizon at an 8-8.5% base discount rate, with terminal growth capped at 3.0% applied to a demonstrated sustained margin - not a cyclical peak in customer R&D spending. The bear case adds 250bp, the bull case subtracts 150bp with an 8% floor, weighted 25% / 50% / 25%. Terminal value exceeding 70% of enterprise value is haircut and disclosed."),
            ("p", "The bear case, sitting below the current price, assumes the AI R&D supercycle rolls over: hyperscaler silicon programs consolidate, a semiconductor downturn arrives mid-decade, China revenue is impaired by export controls, and revenue growth falls to high-single digits with margins compressing as the Hexagon integration disappoints. The base case assumes mid-teens revenue growth moderating to low teens, non-GAAP operating margins sustained in the mid-40s, agentic tools expanding engine consumption as management describes, and the backlog converting on schedule. The bull case assumes the AI silicon buildout extends through the decade, Cadence's agentic platform becomes the industry-standard design cockpit with premium pricing, and EDA's share of R&D spend steps up structurally."),
            ("p", "The probability-weighted fair value is $308.00, our target, against the October 2, 2026 close of $351.35 - about 12% downside. The valuation respects the franchise fully - the 15-year horizon and 8-8.5% discount rate are the most favorable assumptions we grant any business - and still finds the price ahead of the fundamentals. The stock's own 32% drawdown from its high is the market's way of saying the cycle is being repriced; our work says the repricing is not finished."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Semiconductor R&D cyclicality: EDA revenue lags chip downturns but follows them; a pause in hyperscaler silicon spending would hit design starts, IP licensing, and hardware sales with a lag.",
                "Customer concentration: AI-accelerator and hyperscaler programs are a growing share of growth; consolidation or insourcing shifts by a few large customers would be material.",
                "China export controls: China is a meaningful revenue geography and policy is a swing factor outside the company's control.",
                "Hexagon integration: the Design & Engineering acquisition is diluting 2026 margins; synergy capture and cross-sell execution must deliver to justify the price paid.",
                "Synopsys competition: the Ansys combination makes the arch-rival larger and broader across simulation; share battles in verification and IP could pressure pricing.",
                "Agentic-AI monetization: if agent-driven consumption commoditizes solver pricing or shifts value to the agent layer, the demand-accelerator thesis weakens.",
                "Valuation: even after the drawdown, the multiple assumes a smooth continuation of 20%+ growth that the semiconductor cycle has never delivered.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "A deeper cyclical washout - the stock offered 20%+ below our fair value on a semiconductor downturn that leaves the duopoly intact - would make this a BUY; that is historically when Cadence should be bought.",
                "Proof that agentic tools are expanding per-customer spend at premium pricing (not just shifting seats to consumption) would raise our through-cycle growth rate.",
                "Sustained 20%+ revenue growth with 45%+ non-GAAP margins through an actual semiconductor downturn would prove the business has de-cyclicalized and justify a higher multiple.",
                "Conversely, ROIC falling below 15% for consecutive years, structural gross-margin compression, or FCF conversion dropping below 80% over a multi-year window would revoke the compounder-quality assumptions and lower fair value.",
                "Loss of the TSMC leading-node certification cadence or a major foundry reference-flow defection would impair the moat directly.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", METHODOLOGY_COMPOUNDER_CDNS),
        ]),
    ],
}

# ---------------------------------------------------------------- CELH
celh = {
    "ticker": "CELH",
    "company": "Celsius Holdings, Inc.",
    "verdict": "REDUCE",
    "target": "$23.00",
    "price": "$26.75",
    "price_note": "October 2, 2026 close",
    "upside": "-14%",
    "sections": [
        ("Investment Thesis", [
            ("p", "Celsius Holdings has assembled, by acquisition, the number-three energy-drink portfolio in America: roughly 21% of U.S. ready-to-drink energy dollar share across CELSIUS, Alani Nu, and Rockstar, behind only Red Bull and Monster. The Alani Nu deal - $1.8 billion gross, closed April 2025 - looks genuinely inspired in hindsight: the brand did over $1 billion of revenue in 2025, grew retail sales more than 100% in early 2026, and was bought for less than 2x sales. PepsiCo deepened its partnership with a $585 million preferred investment taking its stake to about 11%, designated Celsius its strategic energy lead in the U.S., and handed over Rockstar's U.S. and Canada rights. Full-year 2025 revenue hit $2.52 billion, up 85.5%, with adjusted EBITDA of $619.6 million up 142%. The transformation from a single-brand growth story into a scaled energy platform is real, and the operating leverage is showing."),
            ("p", "The problem is what the market is paying for the transformation, and what it is assuming about the parts. Strip out the acquisition math and the picture is a three-brand portfolio moving in three different directions: Alani Nu surging at roughly 9% share, the namesake CELSIUS brand growing retail sales at just 6-13% - the slowest horse in the stable - and Rockstar declining 9-13% and needing, by management's own framing, a 'stabilization year.' The second quarter of 2026 is the first quarter that fully laps the Alani Nu deal, which is why reported growth steps down from triple digits to roughly 20%: the rollup reveal. From here, Celsius must grow the way beverage companies actually grow - by selling more cans of the brands it owns, in categories where Red Bull and Monster do not yield shelf space willingly - while digesting integration costs that pushed Q4 2025 gross margin to 47.4% and a balance sheet carrying acquisition debt."),
            ("p", "Our judgment is that the current price of $26.75 capitalizes flawless execution of a multi-brand turnaround in the most competitive beverage category in America, and flawless is not the base case. On a probability-weighted scenario DCF - 10-year horizon, 12% base discount rate reflecting the speculative combination of acquisition integration risk, category concentration, and a still-unproven multi-brand playbook - fair value is $23, about 14% below the price. The bear case, which sits below the price as required, is genuinely adverse: the CELSIUS brand stalls as better-for-you energy matures, Alani Nu's torrid growth normalizes faster than expected, Rockstar's turnaround fails, promotional intensity compresses category margins, and the leverage from the deal spree constrains flexibility. We rate the stock REDUCE. Alani Nu was a great deal; the stock price assumes several more of them, already executed, already integrated, already paid for."),
        ]),
        ("Business Overview", [
            ("p", "Celsius Holdings is a functional-beverage company built around the energy-drink category. The flagship CELSIUS brand pioneered 'better-for-you' energy - thermogenic, fitness-positioned, sugar-free formulations - and rode the health-and-wellness wave to become a top-five U.S. energy brand. Alani Nu, acquired in April 2025, is a female-skewing, flavor-innovation-driven brand with a powerful influencer-born community that has become the growth engine of the portfolio. Rockstar Energy's U.S. and Canada rights, acquired from PepsiCo in August 2025, add a legacy mainstream brand in decline that management must stabilize and reposition."),
            ("p", "Distribution is the strategic moat, such as it is: PepsiCo is the company's distribution partner and, following the $585 million preferred investment, an ~11% shareholder with a board nominee. Celsius is PepsiCo's designated energy category captain in the U.S., which means preferential shelf, cooler, and promotional treatment across the Pepsi bottler network - an enormous structural advantage for a company that spent its early years fighting for distribution. The combined portfolio held about 20.8% U.S. dollar share in the 13 weeks ended late September 2025. First-quarter 2026 revenue was $782.6 million, up 138% year over year, with $747.3 million in North America and international up 55% albeit from a small base."),
            ("p", "The financial shape is that of a rollup in mid-integration. Full-year 2025 gross margin was 50.4% but the fourth quarter dipped to 47.4% on integration costs and tariffs; management guides a recovery to the low-50s across 2026, paced to the second half. GAAP earnings are obscured by one-time items - $327.5 million of distributor termination fees to move Alani Nu into PepsiCo's network (economically real, paid once) plus acquisition costs - while adjusted EBITDA of $619.6 million at a 24.6% margin shows the underlying cash engine. The company repurchased $40 million of stock in late 2025 with $260 million of authorization remaining, paid down about $200 million of debt, and pays no dividend - capital priority is M&A and buybacks."),
        ]),
        ("Forward Outlook", [
            ("p", "Our forward view is that 2026-2027 is the prove-it period, and the burden of proof is heavier than the stock price suggests. The good news first: Alani Nu's momentum is real and durable enough to carry the portfolio's growth for the next two years, the PepsiCo distribution machine is still in the early innings of what it can do for shelf presence and in-store execution, and the $50 million of integration synergies already captured show management can operate a multi-brand portfolio. International - the U.K., Australia, and other developed energy markets - is a genuine multi-billion-dollar whitespace where the better-for-you positioning travels well."),
            ("p", "The concerns are structural, not quarterly. First, the namesake CELSIUS brand - still the majority of revenue - is growing retail sales at 6-13% while the category's growth concentrates in Alani Nu's flavor-innovation lane; a flagship growing at half the portfolio rate is a brand-health question, not a blip, and management's pivot to 'portfolio framing' when asked about cannibalization did not answer the question. Second, Rockstar is a turnaround inside a growth story, and turnarounds consume management attention disproportionately to their revenue. Third, the energy category is brutally promotional - Red Bull and Monster have deeper pockets and longer relationships - and Celsius's gross-margin recovery to the low-50s assumes a promotional environment that cooperates. Fourth, the balance sheet, while de-risking, still reflects a company that spent $1.8 billion in eighteen months; the next acquisition cannot be funded as easily as the last ones were."),
            ("p", "Our judgment on the trajectory: revenue compounds in the mid-teens as Alani Nu scales and international builds, but the margin path is bumpier than guidance implies and the multiple compresses as the market stops valuing Celsius as a single high-growth brand and starts valuing it as what it is - a mid-teens-growing beverage consolidator with a turnaround project attached. That re-rating is the core of our REDUCE thesis: the business can execute well and the stock can still fall, because the price was set for a different company than the one that now exists."),
        ]),
        ("Valuation", [
            ("p", "We value Celsius on a probability-weighted scenario DCF over an explicit 10-year horizon, weighted 25% / 50% / 25%, with a 12% base discount rate - our speculative-tier rate, reflecting acquisition-integration risk, single-category concentration, the unproven multi-brand playbook, and balance-sheet leverage from the deal spree. The bear case adds 250bp, the bull case subtracts 150bp with an 8% floor. Terminal growth is capped at 2.5% on normalized mid-cycle margins, and terminal value exceeding 70% of enterprise value is haircut and disclosed."),
            ("p", "The bear case, sitting below the current price, is genuinely adverse: CELSIUS brand growth stalls in the low-single digits as better-for-you energy matures, Alani Nu's growth normalizes to category rates faster than expected, the Rockstar turnaround fails and the brand becomes a stranded asset, promotional intensity compresses gross margins back toward the mid-40s, and leverage constrains strategic flexibility. The base case assumes Alani Nu compounds at high rates for several more years before normalizing, CELSIUS reaccelerates modestly on innovation (including the fizz-free platform), Rockstar stabilizes but does not return to growth, gross margins recover to the low-50s by 2027, and international becomes a meaningful contributor late in the decade. The bull case assumes the PepsiCo partnership delivers share gains beyond our base case, the portfolio takes sustained share from Red Bull and Monster, and Celsius becomes the acquirer of choice for emerging functional brands at accretive multiples."),
            ("p", "The probability-weighted fair value is $23.00, our target, against the October 2, 2026 close of $26.75 - about 14% downside. The valuation says the Alani Nu deal, good as it was, is fully in the price - and the market is additionally paying for a Rockstar turnaround and a CELSIUS reacceleration that have not happened yet."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Brand concentration in transition: the CELSIUS flagship is the slowest-growing brand in the portfolio; if its deceleration continues, the growth story narrows to a single brand.",
                "Alani Nu normalization: triple-digit retail growth cannot persist; the speed and shape of the deceleration is the single largest swing factor in the model.",
                "Rockstar turnaround failure: a declining legacy brand can consume management attention and trade spend disproportionate to its revenue contribution.",
                "Promotional intensity: Red Bull and Monster compete aggressively on price and placement; category promo pressure could derail the gross-margin recovery to the low-50s.",
                "PepsiCo dependence: distribution, category captaincy, and a major shareholding concentrate strategic risk in one partner whose priorities could shift.",
                "Leverage and M&A hangover: the balance sheet still reflects $1.8 billion of deal spending; further large acquisitions would strain flexibility.",
                "Valuation: the stock prices flawless multi-brand execution; any stumble reprices the growth multiple, not just the growth rate.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "The CELSIUS brand reaccelerating to sustained double-digit retail growth on its own - not as a portfolio average - would retire our central brand-health concern.",
                "Rockstar returning to positive retail growth would prove the multi-brand turnaround playbook and raise through-cycle growth assumptions.",
                "Gross margins reaching and holding the low-50s on a clean (non-integration) basis would validate the earnings power the bull case assumes.",
                "A pullback toward $18-19 on integration noise rather than brand deterioration would make the risk-reward positive and move us to HOLD or BUY.",
                "Conversely, evidence of CELSIUS-to-Alani Nu cannibalization in scanner data, or Alani Nu growth collapsing toward category rates within a year, would deepen the REDUCE thesis.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", METHODOLOGY_STANDARD),
        ]),
    ],
}

# ---------------------------------------------------------------- VST
vst = {
    "ticker": "VST",
    "company": "Vistra Corp.",
    "verdict": "REDUCE",
    "target": "$120.00",
    "price": "$140.02",
    "price_note": "October 2, 2026 close",
    "upside": "-14%",
    "sections": [
        ("Investment Thesis", [
            ("p", "Vistra is the best-positioned independent power producer in America for the AI electricity supercycle, and the market has spent two years repricing it as such. The facts are impressive: the second-largest competitive nuclear fleet in the U.S. at about 6.4 GW (Comanche Peak plus Beaver Valley, Davis-Besse, and Perry from the 2024 Energy Harbor acquisition), roughly 3.8 GW of nuclear capacity now contracted to hyperscalers - a 20-year PPA for up to 1.2 GW at Comanche Peak with AWS, 2.6 GW across three plants with Meta - a record 2025 with ongoing-operations adjusted EBITDA of $5.912 billion, 2026 guidance of $6.8-$7.6 billion, and a 2027 outlook of $7.6-$7.8 billion that excludes the pending 5,500 MW Cogentrix acquisition and the Meta contracts. Management has repurchased about 30% of shares outstanding since late 2021. This is a well-run company riding a genuine demand wave."),
            ("p", "Riding it is the operative phrase, because the stock at $140.02 is priced as though the wave never breaks. Independent power producers are merchant businesses: they sell into wholesale markets and through contracts, which means they have torque to rising power prices - and torque cuts both ways. The hyperscaler PPAs are real and long-dated, but they cover a fraction of the fleet; the rest of the earnings power is a bet on sustained tightness in power markets, on data-center load materializing on schedule, and on capacity prices staying elevated. The company carries around $19 billion of debt, plans about $3 billion of 2026 capex, and the latest reported quarter missed consensus on both earnings and revenue. The AI-power narrative is doing a great deal of work in this valuation - including the June 2026 Helix Digital Infrastructure venture with Nvidia and the Kuwait Investment Authority, which is strategic optionality, not cash flow."),
            ("p", "Our judgment, on a probability-weighted scenario DCF - 10-year horizon, 10% base discount rate reflecting merchant power-market exposure and leverage, bear +250bp, bull -150bp - is fair value of $120, about 14% below the current price. The base case respects the contracted cash flows: the AWS and Meta nuclear PPAs, the retail earnings stream from TXU, and a constructive but not heroic power-price environment. The bear case, which sits below the price as required, models what merchant generators have experienced in every prior cycle: data-center load arrives slower than announced, power prices mean-revert as new supply (including Vistra's own new gas builds) clears, capacity revenues normalize, and the leverage that amplified the upside amplifies the downside. We rate the stock REDUCE. The electrons are real; the price assumes they are all sold at peak-cycle economics forever."),
        ]),
        ("Business Overview", [
            ("p", "Vistra is an independent power producer (IPP) and retail electricity provider. Unlike regulated utilities, it earns no guaranteed return: its generation fleet sells power into competitive wholesale markets (ERCOT, PJM, and others) and through bilateral contracts, while its retail arm - anchored by TXU Energy in Texas - sells directly to residential and commercial customers. The integrated model (generation plus retail) provides a natural hedge: the retail book is effectively short power that the generation fleet is long, dampening merchant volatility while retaining upside to tight markets."),
            ("p", "The fleet is the strategic asset. Nuclear - about 6.4 GW across Comanche Peak in Texas and the three Energy Harbor plants in Ohio and Pennsylvania - is the crown jewel: carbon-free, baseload, 90%+ capacity factors, and suddenly the most coveted generation on the grid because hyperscalers will pay premiums for firm clean power. Around it sits a large natural-gas fleet (expanded in 2025 with ~2,600 MW across seven plants acquired from Lotus Infrastructure Partners), legacy coal in managed decline, and growing solar and battery storage. The pending Cogentrix acquisition would add another 5,500 MW of mostly gas-fired capacity."),
            ("p", "Financially, the company is in the strongest position in its history and also the most levered to the power-price cycle. 2025 ongoing-operations adjusted EBITDA was $5.912 billion, a record; 2026 guidance is $6.8-$7.6 billion with adjusted free cash flow before growth of $3.9-$4.7 billion - a double-digit FCF yield even at recent prices. The dividend is $0.92 per share (a sub-1% yield - this is not an income stock), and the buyback has retired roughly 30% of shares since November 2021 with $1.8 billion of authorization remaining. Debt of about $19 billion is the shadow over the story: manageable at current EBITDA, constraining if EBITDA reverts."),
        ]),
        ("Forward Outlook", [
            ("p", "Our forward view is that Vistra's contracted earnings - the nuclear PPAs with AWS and Meta, the retail book, the hedged portion of the gas fleet - compound reliably through the decade, and that this contracted base alone supports a solid mid-$100s valuation. The 20-year AWS contract at Comanche Peak and the Meta agreements are genuine derisking events: they convert merchant nuclear megawatts into bond-like cash flows at attractive economics, and there is a credible pipeline of additional hyperscaler deals for the remaining uncontracted nuclear capacity. The New Era 20-year PPA (200 MW from a Texas gas plant, starting 2027, plus a 5% project interest) shows the contracting playbook extending beyond nuclear. This is a better business than the Vistra of 2021, and the market is right to pay up for it."),
            ("p", "Where we part company with the bulls is on the uncontracted earnings - the merchant torque that the current price extrapolates indefinitely. Power markets are cyclical because supply responds to price: high power prices and capacity payments are already pulling new gas builds (including Vistra's own 860 MW in West Texas), battery storage, and demand-response into the market, and every megawatt of new supply is a future headwind to the spark spreads the bull case assumes. Data-center load forecasts, meanwhile, have a long history of arriving late and light relative to announcements; the 1.4 GW New Era campus, the Helix venture, and the broader AI-load pipeline are real options, not contracted EBITDA. Our base case assumes power markets stay constructive but normalize from today's tightness, with merchant EBITDA flattening late in the decade rather than compounding at the guided trajectory forever."),
            ("p", "The honest bull case for the stock from here requires one of two things: power prices structurally resetting higher for a decade (possible if load growth truly overwhelms supply additions, but a bet on persistent market tightness that history counsels against), or Vistra converting far more of its fleet to long-dated hyperscaler contracts at premium economics, effectively turning the merchant generator into a contracted infrastructure company. We assign real probability to further contracting - management's commercial team is demonstrably best-in-class at it - but the current price already assumes a great deal of it. Our judgment: own the contracted cash flows at the right price; at $140, you are paying for merchant earnings at peak-cycle multiples."),
        ]),
        ("Valuation", [
            ("p", "We value Vistra on a probability-weighted scenario DCF over an explicit 10-year horizon, weighted 25% / 50% / 25%, with a 10% base discount rate reflecting merchant power-market exposure, ~$19 billion of debt, and the inherent cyclicality of wholesale power - a full standard rate despite the nuclear fleet's quality, because leverage and merchant torque dominate the risk profile. The bear case adds 250bp, the bull case subtracts 150bp with an 8% floor. Terminal growth is capped at 2.5% on normalized mid-cycle power-market margins - not on today's elevated spark spreads and capacity prices - and terminal value exceeding 70% of enterprise value is haircut and disclosed."),
            ("p", "The bear case, sitting below the current price, models the merchant cycle turning: data-center load materializes at half the announced pace, new gas and storage supply clears the tightness in ERCOT and PJM, power and capacity prices mean-revert, uncontracted EBITDA falls 25-30% from peak, and leverage ratios deteriorate - the classic IPP downcycle. The base case assumes the AWS/Meta nuclear PPAs and retail earnings compound as contracted, merchant markets stay constructive but normalize gradually, the Cogentrix acquisition closes and integrates at guided economics, and free cash flow funds continued buybacks and deleveraging. The bull case assumes sustained power-market tightness through the decade, most remaining nuclear capacity contracted to hyperscalers at premium 20-year economics, and Vistra effectively completing the transition from merchant generator to contracted clean-power infrastructure."),
            ("p", "The probability-weighted fair value is $120.00, our target, against the October 2, 2026 close of $140.02 - about 14% downside. The valuation credits every contracted electron and still finds the market paying peak-cycle multiples for merchant earnings. In IPP investing, that has historically been the wrong side of the cycle to pay up."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Power-price mean reversion: merchant earnings are torque to wholesale prices; new supply (gas builds, storage, demand response) responding to today's tightness would compress spark spreads and capacity revenues.",
                "Data-center load shortfall: announced AI-load pipelines have a history of arriving late and light; slower-than-expected load growth undermines the demand thesis.",
                "Leverage: ~$19 billion of debt is manageable at $7B+ EBITDA but becomes constraining quickly if merchant EBITDA reverts toward historical norms.",
                "Regulatory and political risk: nuclear uprates, plant life extensions, and market-design changes (capacity market reforms in PJM, ERCOT evolution) are subject to political and regulatory decisions.",
                "Contract concentration: a small number of hyperscaler counterparties underpin the growth narrative; counterparty or project risk is concentrated.",
                "Retail margin pressure: the TXU book faces competitive and regulatory pressure in Texas retail markets; hedged margins can compress.",
                "Cogentrix integration: the 5,500 MW acquisition must deliver guided economics; large fleet integrations carry operational and market risk.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Contracting the bulk of remaining nuclear capacity to investment-grade hyperscalers at 15-20 year terms and premium economics would convert the merchant risk we are discounting into contracted cash flow and raise fair value materially.",
                "Structural, durable power-market tightness - load growth persistently outpacing supply additions for several years with data to prove it - would validate the bull-case power-price deck.",
                "A cyclical washout that takes the stock toward $90-100 on transiently weak power prices, with the nuclear fleet and contracts intact, would flip us to BUY - IPPs should be bought in the trough.",
                "Conversely, evidence that data-center load forecasts are being cut, or new supply clearing prices faster than expected, would deepen the REDUCE thesis.",
                "A debt-funded empire-building acquisition beyond Cogentrix, or suspension of the buyback to fund speculative development, would signal capital-allocation drift.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", METHODOLOGY_STANDARD),
        ]),
    ],
}

# ---------------------------------------------------------------- AXP
axp = {
    "ticker": "AXP",
    "company": "American Express Company",
    "verdict": "REDUCE",
    "target": "$250.00",
    "price": "$302.78",
    "price_note": "October 2, 2026 close",
    "upside": "-17%",
    "sections": [
        ("Investment Thesis", [
            ("p", "American Express is executing superbly. Second-quarter 2026 revenue net of interest expense grew 10% to $19.64 billion, billed business accelerated 9% on an FX-adjusted basis - the fastest pace in three years - net card fees climbed 15% to a record $2.9 billion for the 32nd consecutive quarter of double-digit growth, and diluted EPS rose 11% to $4.53. Credit quality is pristine: net write-offs flat at 2.0%, delinquencies at 1.2%, and a $1.1 billion provision that actually declined on a reserve release. Management raised full-year revenue growth guidance to 10% while holding EPS guidance at $17.30-$17.90. Return on equity runs at 36-38%. By every operating measure, this is a premium franchise performing at a premium level."),
            ("p", "And the market has noticed - which is precisely the problem. At $302.78, American Express trades at roughly 17-18 times the $17.30-$17.90 EPS guidance for a business whose through-cycle revenue growth is high-single digits and whose earnings are, at bottom, a leveraged bet on affluent consumer spending and benign credit. The premium-spend flywheel - acquire affluent cardmembers, monetize through discount revenue and rising annual fees, reinvest in rewards and the Platinum refresh - is working beautifully right now because the affluent consumer is employed, spending, and current on payments. Every one of those conditions is cyclical. The reserve release flattered the quarter; the 32 quarters of double-digit fee growth are a triumph of compounding that gets harder, not easier, with each successive quarter; and the 12% expense growth - driven by engagement costs and the Platinum refresh - shows how expensive it is to keep the flywheel spinning."),
            ("p", "Our judgment, on a probability-weighted scenario DCF - 10-year horizon, 9% base discount rate reflecting the closed-loop network moat and affluent mix, bear +250bp, bull -150bp - is fair value of $250, about 17% below the current price. The base case gives Amex full credit for the franchise: billed business compounding at high-single digits, card fees growing double digits for several more years before normalizing, credit staying near current benign levels through the explicit period, and the buyback continuing to retire 2-3% of shares annually. But it refuses to capitalize today's pristine credit and peak affluent spending as permanent, and the bear case - which sits below the price, as required - models what Amex shareholders have lived through before: a consumer downturn where billed business stalls, provisions rise by billions, and the multiple compresses from premium to merely good. We rate the stock REDUCE. This is a wonderful company at a price that assumes the credit cycle has been repealed."),
        ]),
        ("Business Overview", [
            ("p", "American Express operates a closed-loop payments network - it is simultaneously the card issuer, the network, and (largely) the acquirer - which gives it data, economics, and customer relationships that the open-loop networks (Visa, Mastercard) do not have. Revenue comes from discount revenue (the merchant fee on billed business), net card fees (annual fees, now a $2.9 billion quarterly run-rate business growing 15%), and net interest income on revolving card balances ($4.6 billion in Q2 2026, up 11%). The customer base skews affluent: premium card products (Platinum, Gold, Centurion), heavy travel-and-entertainment exposure (T&E billed business up 10% in the quarter), and small-business and corporate cards."),
            ("p", "The economics are among the best in financial services. Cards-in-force reached 155.1 million, up 4%; network volumes were $516.8 billion in the quarter, up 9%; average proprietary basic cardmember spending keeps rising; and the Common Equity Tier 1 ratio of 10.4% with $45.2 billion of cash supports both growth investment and capital return - $2.9 billion returned in Q2 2026 alone ($2.2 billion of buybacks at an average price of $315.77, plus dividends). The fee-forward strategy is deliberate: annual fees are recurring, high-margin, and less cyclical than spend-based revenue, and 32 straight quarters of double-digit fee growth have steadily de-risked the revenue mix."),
            ("p", "The competitive position rests on the affluent-spend flywheel and the closed loop's data advantage in underwriting and fraud. Amex underwrites its own cardmembers, which is why its credit performance is structurally better than monolines' - 2.0% net write-offs versus multiples of that at subprime lenders. The risks to the moat are digital wallets and alternative payment rails disintermediating the card interface, fintechs competing for the affluent millennial cohort Amex covets, and the perennial merchant acceptance cost debate - though Amex's acceptance parity in the U.S. is now effectively complete."),
        ]),
        ("Forward Outlook", [
            ("p", "Our forward view is that Amex's operating momentum persists through 2027 - the affluent consumer is in good shape, the Platinum refresh cycle is driving acquisition and engagement, and billed business should keep growing at high-single digits - but that the market is extrapolating a cyclical peak. The specific mechanics of the coming normalization: net card-fee growth, after 32 quarters of double-digit gains, faces the arithmetic of a larger base and the limits of annual-fee pricing power; the reserve release that flattered 2026 provisions reverses when credit normalizes, and provisions rising by even $1-2 billion annually is a meaningful EPS headwind; and expense growth in the low teens - the cost of acquiring and engaging premium cardmembers - means operating leverage is thinner than the revenue line suggests."),
            ("p", "We are constructive on the structural elements. The fee-forward mix shift genuinely de-risks the model: every point of revenue mix that moves from discount revenue to card fees is a point of revenue that does not disappear in a spending downturn. International - 20% billed-business growth in International Card Services in Q1 2026 - remains an underappreciated growth vector with years of runway. The closed-loop data advantage in underwriting should let Amex navigate a credit turn better than competitors, which is cold comfort for the stock price but real for the franchise. Our base case has EPS compounding at roughly 10% through the decade - an excellent outcome for a financial company, and one the current price more than discounts."),
            ("p", "The scenario that worries us is not a 2008-style crisis but an ordinary affluent-consumer slowdown: billed business growth halving, delinquencies ticking up from 1.2%, provisions rising again, and the market deciding that 17-18x earnings was a peak-cycle multiple for what is ultimately a consumer-credit business with a great brand. Amex has traded at 10-12x earnings in softer environments within recent memory; the distance from there to here is the downside the REDUCE rating is meant to capture. Our judgment: the franchise deserves a premium to banks, not immunity from the credit cycle."),
        ]),
        ("Valuation", [
            ("p", "We value American Express on a probability-weighted scenario DCF over an explicit 10-year horizon, weighted 25% / 50% / 25%. The base discount rate is 9% - below our standard 10% to reflect the closed-loop moat, the affluent customer mix, and structurally superior credit performance, but well above a utility-like rate because this remains a consumer-credit business with cyclical earnings. The bear case adds 250bp, the bull case subtracts 150bp with an 8% floor. Terminal growth is capped at 2.5% on normalized mid-cycle credit costs and margins - not on today's 2.0% write-off rate and reserve-release-assisted provisions - and terminal value exceeding 70% of enterprise value is haircut and disclosed."),
            ("p", "The bear case, sitting below the current price, models an ordinary consumer-credit turn: billed business growth falls to low-single digits, net write-offs rise toward 3%+, provisions rise by $2-3 billion annually, card-fee growth decelerates to mid-single digits as acquisition slows, and the multiple compresses to 12-13x normalized earnings. The base case assumes billed business compounds at high-single digits, card fees grow double digits for several more years before moderating, credit stays near current levels with only mild normalization, expenses grow roughly in line with revenue, and the buyback retires 2-3% of shares annually. The bull case assumes the affluent-spend flywheel sustains double-digit billed-business growth, international becomes a second engine, credit stays pristine indefinitely, and the market permanently awards a premium-network multiple."),
            ("p", "The probability-weighted fair value is $250.00, our target, against the October 2, 2026 close of $302.78 - about 17% downside. The valuation's conclusion is that Amex is priced as a secular growth compounder when its earnings are those of a superbly managed cyclical - and superbly managed cyclicals should be bought in the downcycle, not at the top of the credit cycle."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Credit-cycle turn: write-offs at 2.0% and delinquencies at 1.2% are cyclical lows; normalization would push provisions up by billions and hit EPS directly.",
                "Affluent-spending slowdown: billed business is concentrated in discretionary and T&E spending by affluent consumers - the cohort most exposed to asset-price and employment shocks.",
                "Fee-growth arithmetic: 32 quarters of double-digit card-fee growth gets harder against a larger base; annual-fee pricing power has limits.",
                "Expense intensity: 12% expense growth to acquire and engage premium cardmembers compresses operating leverage if revenue growth moderates.",
                "Multiple compression: 17-18x earnings is a peak-cycle multiple for a consumer-credit business; re-rating to historical mid-cycle multiples implies 20%+ downside without any fundamental impairment.",
                "Disintermediation: digital wallets, buy-now-pay-later, and alternative rails compete for the transaction interface, particularly with younger affluent cohorts.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "A genuine credit scare or consumer slowdown that takes the stock 20-25% lower while the franchise and underwriting advantage remain intact would make this a BUY - Amex should be bought when credit fear peaks.",
                "Sustained double-digit card-fee growth with stable credit through an actual economic slowdown would prove the fee-forward model has structurally de-risked earnings and justify a higher multiple.",
                "Evidence that international billed business is becoming a second double-digit growth engine at scale would raise through-cycle growth assumptions.",
                "Conversely, delinquencies inflecting upward while the multiple holds would confirm the peak-cycle thesis and deepen the REDUCE view.",
                "A structural loss of pricing power on annual fees, or share loss in premium acquisition to fintech competitors, would impair the flywheel thesis.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", METHODOLOGY_STANDARD),
        ]),
    ],
}

# ---------------------------------------------------------------- NVDA
nvda = {
    "ticker": "NVDA",
    "company": "NVIDIA Corporation",
    "verdict": "REDUCE",
    "target": "$186.00",
    "price": "$233.95",
    "price_note": "October 2, 2026 close",
    "upside": "-21%",
    "sections": [
        ("Investment Thesis", [
            ("p", "NVIDIA is the defining company of the AI era, and the numbers are almost difficult to believe: second-quarter fiscal 2027 revenue of $96.2 billion, up 106% year over year; data-center revenue the overwhelming majority of the total; gross margins at 73.4%; Blackwell systems shipping at a pace management calls the fastest production ramp in semiconductor history; a $10 billion-plus investment web spanning OpenAI, Anthropic, and Intel; and sovereign AI programs across the U.K., Germany, South Korea, and the Gulf. The CUDA software moat - two decades of developer lock-in, libraries, and tooling - remains the deepest competitive advantage in technology. We do not question that NVIDIA is a great company. We question whether any company in history has been worth what the market currently says NVIDIA is worth."),
            ("p", "At $233.95, the stock prices a world in which AI capital expenditure grows more or less indefinitely, in which NVIDIA captures the dominant share of every layer of that spend - compute, networking (with data-center networking up 199% year over year), and increasingly the systems and cloud commitments themselves - and in which gross margins near 75% persist against the combined competitive response of the largest technology companies on earth. Each of those assumptions deserves scrutiny. Hyperscalers are designing their own silicon (Google's TPUs, Amazon's Trainium, Microsoft's Maia) precisely to reduce the NVIDIA tax; AMD and a funded startup ecosystem contest the merchant-silicon layer; China - historically a meaningful market - is constrained by export controls; and the $50 billion of manufacturing commitments and $26 billion of cloud commitments on the balance sheet show a company stretching its own capital to sustain the demand narrative. Capex supercycles in technology have a perfect historical record: every one of them has ended, and the companies priced as though they would not have been the worst investments of the subsequent decade."),
            ("p", "Our judgment, on a probability-weighted scenario DCF - 10-year horizon, 10% base discount rate reflecting technology cyclicality and customer concentration despite the moat, bear +250bp, bull -150bp - is fair value of $186, about 21% below the current price. The base case is not bearish on AI: it assumes data-center revenue keeps growing at very high rates for several more years before moderating, CUDA sustains pricing power, and NVIDIA remains the dominant AI compute supplier with margins settling in the 60s rather than the 70s. The bear case - which sits below the price, as required - is the capex-digestion scenario the market refuses to price: hyperscaler spending pauses after the buildout, custom silicon takes 15-20% share of AI compute, China revenue goes to zero, gross margins compress toward 60%, and the multiple compresses from growth-premium to semiconductor-cyclical. We rate the stock REDUCE. The AI revolution is real; revolutions do not repeal the business cycle, and this price assumes they do."),
        ]),
        ("Business Overview", [
            ("p", "NVIDIA designs accelerated-computing platforms: data-center GPUs and AI systems (the Blackwell and forthcoming Rubin architectures), networking (NVLink, InfiniBand, Spectrum-X Ethernet), the CUDA software stack, plus gaming, professional visualization, and automotive/robotics platforms. Data center is now roughly 90% of revenue - the company has, for economic purposes, become a picks-and-shovels monopoly on AI training and inference compute. Fiscal 2026 full-year revenue was $215.9 billion, up 65%; the first two quarters of fiscal 2027 have already delivered $177.8 billion combined, putting the company on a run-rate that would have been fantastical three years ago."),
            ("p", "The moat has three layers. First, CUDA: twenty years of software investment that makes NVIDIA's hardware the default target for AI developers, with switching costs measured in rewritten codebases and retrained teams. Second, systems: the shift from selling chips to selling rack-scale systems (GB200/G300 NVL72) with integrated networking raised the competitive bar from silicon design to full-stack systems engineering, where NVIDIA's lead is widest. Third, cadence: annual architecture releases (Blackwell to Rubin) keep competitors perpetually a generation behind. Gross margins above 73% and operating cash flow of $66.5 billion in nine months of fiscal 2026 are the financial expression of this dominance, funding $36.7 billion of buybacks and a fortress balance sheet with $60+ billion of liquidity against $8.5 billion of debt."),
            ("p", "The demand base is concentrated by any honest measure: a handful of hyperscalers (Microsoft, Google, Amazon, Oracle, Meta), xAI, sovereign buyers, and a growing enterprise tier account for the great majority of data-center revenue. Management discloses $500 billion-plus of AI chip bookings visibility through 2026 and describes cloud GPU supply as 'sold out.' The strategic investments - up to $10 billion in Anthropic, the OpenAI 10 GW partnership, $5 billion in Intel, sovereign programs - serve the dual purpose of expanding the ecosystem and, inevitably, of supporting the demand narrative on which the valuation depends."),
        ]),
        ("Forward Outlook", [
            ("p", "Our forward view separates the AI thesis, which we believe, from the NVIDIA-stock thesis at this price, which we do not. AI compute demand will grow enormously through the decade: training runs keep scaling, inference demand compounds with deployment, and sovereign programs add a durable new buyer class. NVIDIA will remain the largest beneficiary of that growth - CUDA's developer lock-in does not dissolve, the systems lead is real, and Rubin extends the roadmap. Our base case has data-center revenue roughly tripling from fiscal 2026 levels over the explicit period before growth moderates to single digits. That is a bullish forecast by any historical standard for a company already at $300 billion of run-rate revenue, and it still produces fair value 21% below the price."),
            ("p", "The risks to the demand trajectory are not about whether AI matters but about the shape of the spending curve. First, capex digestion: hyperscalers are simultaneously building for uncertain future demand, and the history of telecom, dot-com, and memory capex cycles says the pause, when it comes, is abrupt - 20-30% order cuts in a single year are the norm, not the exception. Second, substitution: every hyperscaler has an economic incentive to move inference - the larger long-term workload - to custom silicon, and Google's TPUs already demonstrate the model works at scale. Third, China: export controls have already removed a high-margin market, and further tightening is a one-way ratchet. Fourth, margins: 73%+ gross margins on merchant silicon are an invitation to competition that the entire industry is now RSVP-ing to, and systems-level competition (where NVIDIA bundles networking and software) only partly insulates the silicon margin."),
            ("p", "Our judgment on timing: the current fiscal year and next are likely to remain very strong - backlog, bookings, and sold-out supply see to that - which is why we rate the stock REDUCE rather than SELL. The asymmetry is in the out-years: the market prices a smooth, decade-long capex ramp, while the historical base rate for technology capex cycles says the smooth ramp is the least likely path. When the digestion comes - and 'when,' not 'if,' is the honest framing - the combination of decelerating growth and multiple compression is what produces 30-50% drawdowns in prior-cycle leaders. We would rather be early in recognizing the asymmetry than precise in timing the turn."),
        ]),
        ("Valuation", [
            ("p", "We value NVIDIA on a probability-weighted scenario DCF over an explicit 10-year horizon, weighted 25% / 50% / 25%. The base discount rate is 10% - our standard rate, reflecting that even the deepest moat in technology does not repeal cyclicality, customer concentration (a handful of hyperscalers drive the majority of data-center revenue), geopolitical exposure, and the inherent volatility of capex-driven demand. The bear case adds 250bp, the bull case subtracts 150bp with an 8% floor. Terminal growth is capped at 2.5% applied to normalized mid-cycle margins - emphatically not today's 73%+ gross margins, which reflect peak-cycle pricing power - and terminal value exceeding 70% of enterprise value is haircut and disclosed."),
            ("p", "The bear case, sitting below the current price, is the capex-digestion scenario: hyperscaler spending pauses for 18-24 months after the current buildout wave, custom silicon captures 15-20% of AI compute (concentrated in inference), China revenue goes to zero under tighter controls, gross margins compress from the 70s toward 60% as competition intensifies, revenue actually declines in the worst years of the explicit period, and the terminal multiple reflects a mature semiconductor cyclical rather than a growth franchise. The base case assumes AI compute demand grows enormously but with cyclical air pockets: data-center revenue roughly triples over the decade, CUDA sustains a pricing premium, margins settle in the 60s, and NVIDIA exits the period as the dominant but no longer monopolistic AI compute supplier. The bull case assumes the market's implicit forecast - uninterrupted 20%+ growth deep into the 2030s, sustained 70%+ gross margins, successful extension of the franchise into sovereign and enterprise AI at current economics."),
            ("p", "The probability-weighted fair value is $186.00, our target, against the October 2, 2026 close of $233.95 - about 21% downside. The valuation's message is the oldest one in growth investing: the business can be one of the great franchises of the era and the stock can still be 20% overvalued, because franchises are priced on fundamentals and this price is set by extrapolation."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Capex digestion: hyperscaler AI spending is cyclical; a pause after the current buildout wave would cut orders abruptly, and NVIDIA's revenue concentration makes the impact severe.",
                "Custom-silicon substitution: hyperscaler in-house chips (TPUs, Trainium, Maia) target exactly the high-volume inference workloads that underpin long-term demand.",
                "Customer concentration: a handful of hyperscalers and AI labs drive the majority of data-center revenue; capex decisions by 3-4 companies are the demand curve.",
                "China/export controls: further tightening would permanently remove a high-margin market; the ratchet moves one way.",
                "Margin compression: 73%+ gross margins attract the combined competitive response of the industry's largest R&D budgets; AMD, startups, and custom silicon all attack the margin stack.",
                "Multiple compression: the stock embeds a growth-franchise multiple; any sustained deceleration reprices it toward semiconductor-cyclical multiples - a double hit with earnings.",
                "Balance-sheet stretch: $50B+ of manufacturing commitments and large strategic investments show capital intensity rising with the narrative.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Evidence that AI capex is through-cycle rather than cyclical - hyperscalers sustaining 20%+ capex growth through an actual economic downturn - would retire our central cyclicality objection.",
                "Custom-silicon efforts stalling or being abandoned by major hyperscalers would extend the duration of NVIDIA's pricing power materially.",
                "A 25-30% drawdown on capex-digestion fears, with CUDA's moat and the roadmap intact, would make the risk-reward positive and move us to BUY - prior-cycle leaders should be bought in the digestion, not the euphoria.",
                "Sustained 70%+ gross margins with 25%+ growth through a full semiconductor downturn would prove the business has structurally de-cyclicalized.",
                "Conversely, hyperscaler capex guidance cuts, lengthening GPU lead times normalizing to availability, or book-to-bill falling below 1 would confirm the cycle is turning and deepen the REDUCE thesis.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", METHODOLOGY_STANDARD),
        ]),
    ],
}

NOTES = [hd, shop, spgi, cdns, celh, vst, axp, nvda]

if __name__ == "__main__":
    import os
    os.makedirs(OUT, exist_ok=True)
    for n in NOTES:
        path = os.path.join(OUT, "%s-equity-research-note.pdf" % n["ticker"])
        build_note(path, n)
        print("built", path)
