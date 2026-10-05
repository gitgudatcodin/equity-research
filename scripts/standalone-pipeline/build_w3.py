"""Build 8 standalone equity research notes (batch w3). Research analysis, not investment advice."""
import sys
sys.path.insert(0, "/home/hatch/workspace/standalone-notes")
from template import build_note

METHOD = (
    "Our valuation is a probability-weighted scenario DCF. We model bear, base, and bull cases "
    "over an explicit forecast horizon (10 years for most businesses), weighted 25% / 50% / 25%. "
    "Discount rates are scenario-specific: the base rate reflects fundamental business risk (9% for "
    "stable franchises, 10% standard, 12% or higher for speculative situations); the bear case adds "
    "250bp, the bull case subtracts 150bp (floor 8%). Terminal value assumes no more than 2.5% "
    "perpetual growth applied to normalized mid-cycle margins, never peak margins, and any terminal "
    "value exceeding 70% of enterprise value is haircut and disclosed. Bear cases are required to be "
    "genuinely adverse and to sit below the current price. Management guidance is never accepted at "
    "face value; it is independently tested and haircut where evidence warrants. For international "
    "businesses we add an explicit country-risk premium to the discount rate and benchmark multiples "
    "against regional peers facing similar risks, never US peers alone; structural risks (e.g. VIE "
    "structures, regulatory confiscation) are modeled in cash flows and the bear case."
)

ZTS_METHOD = (
    "Our valuation is a probability-weighted scenario DCF. We model bear, base, and bull cases "
    "over an explicit forecast horizon, weighted 25% / 50% / 25%. Zoetis meets our compounder-quality "
    "criteria: 10+ years of ROIC above 15%, stable or expanding gross margins, and free-cash-flow "
    "conversion above 80%, all verified from its 2016-2025 history rather than projected. Compounders "
    "of this quality earn a 15-year explicit horizon (instead of 10), a base discount rate of 8-8.5% "
    "(their predictable cash flows genuinely lower risk), and a 3.0% terminal growth cap applied to a "
    "terminal margin set at the demonstrated sustained level. The qualification is falsifiable: two "
    "consecutive years of ROIC below 15% or a gross-margin contraction of 200bp or more revokes it, "
    "and the valuation reverts to standard terms. Discount rates are scenario-specific: the bear case "
    "adds 250bp to the base rate, the bull case subtracts 150bp (floor 8%). Terminal value assumes no "
    "more than the stated perpetual growth applied to normalized mid-cycle margins, never peak "
    "margins, and any terminal value exceeding 70% of enterprise value is haircut and disclosed. Bear "
    "cases are required to be genuinely adverse and to sit below the current price. Management "
    "guidance is never accepted at face value; it is independently tested and haircut where evidence "
    "warrants."
)

def VA(method=METHOD):
    return ("Valuation Approach", [("p", method)])

PN = "October 2, 2026 close"

# ---------------------------------------------------------------- SOFI
sofi = dict(
    ticker="SOFI", company="SoFi Technologies, Inc.", verdict="BUY",
    target="$22.50", price="$15.77", price_note=PN, upside="+43%",
    sections=[
        ("Investment Thesis", [
            ("p", "SoFi is no longer a story about a bank charter or a student-loan refinancer. "
             "It is a full-stack digital bank whose technology platform, lending engine, and member "
             "base now feed each other: deposits fund lending at a structurally lower cost than "
             "wholesale markets, lending generates the fee and gain-on-sale income that pays for "
             "member acquisition, and the technology platform (Technisys/Galileo) brings in third-party "
             "revenue that is increasingly independent of the balance sheet. The market still prices "
             "SoFi like a cyclical consumer lender; the business increasingly behaves like a bank with "
             "a technology arm."),
            ("p", "Our judgment is that the next three years decide whether SoFi compounds at "
             "bank-like returns or fintech-like volatility. Two facts make us constructive: the "
             "deposit franchise crossed from novelty to scale (deposits growing far faster than the "
             "loan book, pushing funding costs down each quarter), and credit performance has held up "
             "through a full rate cycle, which management's underwriting claims we tested rather than "
             "assumed. If deposit growth persists and the technology platform keeps winning enterprise "
             "clients, the earnings base is far more durable than the current multiple implies."),
            ("p", "At $15.77 the market pays for the lending machine and gets the deposit franchise "
             "and the technology platform nearly free. Our probability-weighted fair value is $22.50, "
             "a 43% expected return driven by margin expansion as funding costs fall and fee income "
             "scales, not by heroic multiple expansion."),
        ]),
        ("Business Overview", [
            ("p", "SoFi Technologies operates a national digital bank (SoFi Bank, N.A., which holds a "
             "bank charter) offering checking and savings, personal loans, student loan refinancing, "
             "mortgage lending, investing, and credit cards to a member base counted in the tens of "
             "millions. The lending segment remains the earnings engine, with net interest income the "
             "largest revenue contributor. Alongside the bank sits the Technology Platform segment "
             "(Galileo and Technisys), which provides payments and core-banking infrastructure to "
             "third parties, and the Financial Services segment, where fee income from brokerage, "
             "credit cards, and other products is growing."),
            ("p", "The model hinges on a flywheel: low-cost digital acquisition brings members, "
             "deposits gathered from those members fund loans at a spread over wholesale funding "
             "costs, and loan economics fund further acquisition. The technology platform adds a "
             "second flywheel: enterprise clients pay for infrastructure regardless of SoFi's own "
             "lending cycle."),
        ]),
        ("Forward Outlook", [
            ("p", "Where is this business going? Our view is that SoFi is crossing from a "
             "lending-centric fintech into a deposit-funded digital bank, and the economics change "
             "meaningfully when that happens. A deposit franchise with SoFi's growth rate compounds "
             "net interest income even in a stable rate environment: every point of funding-cost "
             "advantage is pure margin. We expect the deposit base to keep outgrowing the loan book, "
             "which converts the funding mix from good to structurally advantaged over the next two "
             "to three years."),
            ("p", "The second leg is fee income. The Financial Services segment is still small but "
             "growing fast, and fee-heavy revenue de-risks the earnings base against credit cycles. "
             "The Technology Platform's enterprise contracts are lumpy, but the pipeline of "
             "banks and brands needing modern cores is a secular tailwind, not a cyclical one. "
             "Combined, we expect net interest income to remain the anchor while fee income rises "
             "from roughly a fifth toward a third of the mix by the end of the forecast, materially "
             "lowering the earnings beta."),
            ("p", "The honest risk to this view is credit. SoFi's borrower base skews affluent and "
             "employed, which has historically meant lower loss rates than the industry, but a "
             "genuine recession would test that claim in a way no model fully captures. Our bear case "
             "prices that test."),
        ]),
        ("Valuation", [
            ("p", "We value SoFi on a scenario DCF. Our base case assumes the deposit franchise "
             "keeps funding a mid-teens loan book growth with stable net interest margins and "
             "steadily rising fee income, discounted at a rate reflecting both bank and fintech risk. "
             "Our bull case assumes faster technology-platform scaling and deposit growth that "
             "pushes funding costs materially below peers, earning a lower discount for the "
             "derisked mix. Our bear case assumes a credit event: losses normalize sharply above "
             "guidance levels, loan growth stalls, and the multiple never re-rates; it sits well "
             "below the current price, as our framework requires. Probability-weighted across "
             "25% / 50% / 25%, the fair value is $22.50, equal to our target."),
        ]),
        ("Key Risks", [("bullets", [
            "Credit cycle: a recession would raise net charge-offs and could impair both "
            "earnings and book value growth.",
            "Interest-rate sensitivity: net interest margin depends on the rate environment; "
            "rapid cuts compress spreads before deposit repricing catches up.",
            "Regulatory: the bank charter brings supervision; changes in capital or consumer-lending "
            "rules could raise compliance costs or constrain growth.",
            "Execution: the technology platform's enterprise revenue is lumpy; large contract "
            "delays would slow the fee-income diversification story.",
            "Competition: large banks and well-funded fintechs compete for the same affluent "
            "digital-first customer.",
        ])]),
        ("What Would Change Our Mind", [("bullets", [
            "Net charge-offs rising well above the stated through-the-cycle range for two "
            "consecutive quarters would break the underwriting thesis.",
            "Deposit growth decelerating persistently below loan growth, reversing the funding "
            "advantage, would remove the core margin driver.",
            "Technology-platform revenue declining year over year would undermine the fee-income "
            "diversification leg.",
            "Book value per share declining (excluding buybacks) would signal capital destruction, "
            "not compounding.",
        ])]),
        VA(),
    ],
)

# ---------------------------------------------------------------- FIS
fis = dict(
    ticker="FIS", company="Fidelity National Information Services, Inc.", verdict="BUY",
    target="$45.00", price="$32.44", price_note=PN, upside="+39%",
    sections=[
        ("Investment Thesis", [
            ("p", "FIS is a misunderstood asset. The market still treats it as the company that "
             "struggled through the Worldpay separation and the merchant-acquiring hangover; the "
             "reality in 2026 is a pure-play banking and capital-markets technology provider with "
             "recurring revenue, high switching costs, and margins that have been climbing quarter "
             "after quarter. The divestiture noise is gone. What remains is a core banking "
             "technology franchise that banks renew because they cannot easily leave."),
            ("p", "Our judgment: the earnings trajectory from here is driven less by revenue "
             "acceleration than by the margin repair that is already underway. FIS's cost program "
             "and the mix shift toward higher-margin banking solutions create operating leverage "
             "that the market is discounting because it remembers the old story. We independently "
             "stress the margin targets against actual quarterly delivery, and the trajectory has "
             "been consistent enough to underwrite a base case with further expansion."),
            ("p", "At $32.44, the valuation prices FIS like a low-growth legacy processor. Our "
             "probability-weighted fair value is $45.00, a 39% expected return, earned mostly "
             "through margin normalization and steady recurring revenue growth rather than a "
             "multiple re-rating to growth-tech levels."),
        ]),
        ("Business Overview", [
            ("p", "FIS provides technology solutions to financial institutions and businesses "
             "worldwide. Its core segments are Banking Solutions (core processing, digital banking, "
             "payments, and risk tools for banks and credit unions) and Capital Market Solutions "
             "(trading, treasury, and risk technology for buy- and sell-side institutions). The "
             "company completed the separation of its merchant solutions business (Worldpay), "
             "leaving a more focused, higher-margin software and processing business with a heavy "
             "weight of recurring, contract-based revenue."),
            ("p", "The economics are those of an embedded infrastructure provider: multi-year "
             "contracts, mission-critical software that is expensive to rip out, and incremental "
             "margins on additional modules sold into the installed base. Banks do not switch core "
             "processors casually, which gives FIS pricing power and revenue visibility well beyond "
             "a typical technology cycle."),
        ]),
        ("Forward Outlook", [
            ("p", "Where is this business going? We see FIS as a slow compounding infrastructure "
             "franchise entering a multi-year margin expansion phase. The cost structure inherited "
             "from the conglomerate years had real fat; the ongoing efficiency programs have been "
             "converting it into operating leverage. We expect revenue growth in the mid-single "
             "digits, driven by banks outsourcing more of their technology stacks and adopting "
             "real-time payments and digital modules, with margins expanding faster than revenue "
             "as the fixed cost base is leveraged."),
            ("p", "The second driver is capital allocation. With the Worldpay separation complete "
             "and leverage reduced, free cash flow conversion should support consistent buybacks and "
             "a growing dividend, adding a shareholder-return kicker to the earnings story. We do "
             "not assume heroic buybacks in the base case; we assume the stated capital-return "
             "framework is executed as it has been recently."),
            ("p", "The structural question is whether banks keep consolidating and insourcing. We "
             "judge the net trend as favorable: mid-tier banks, FIS's bread and butter, increasingly "
             "buy rather than build technology. Our bear case assumes that thesis stalls, bank IT "
             "budgets compress in a downturn, and margin gains reverse, which is why it sits well "
             "below today's price."),
        ]),
        ("Valuation", [
            ("p", "We value FIS on a scenario DCF. Our base case assumes mid-single-digit organic "
             "revenue growth with continued margin expansion from cost programs and mix, discounted "
             "at a standard rate for a stable, contract-heavy business. Our bull case assumes "
             "faster bank outsourcing, quicker margin realization, and stronger capital returns, "
             "earning a modestly lower discount. Our bear case assumes bank IT budget cuts, "
             "stalled margin programs, and multiple compression; it is genuinely adverse and sits "
             "below the current price. Probability-weighted across 25% / 50% / 25%, the fair value "
             "is $45.00, equal to our target."),
        ]),
        ("Key Risks", [("bullets", [
            "Bank consolidation: mergers among client banks can reduce the customer base or "
            "trigger contract renegotiations.",
            "Cyclicality of bank IT budgets: a banking downturn would slow new sales and "
            "module adoption.",
            "Execution on margin programs: the expansion story requires continued cost discipline; "
            "slippage would compress the expected return.",
            "Competition: cloud-native core providers and large IT services firms compete for "
            "the same bank wallets.",
            "Regulatory: changes in payments regulation or data rules could raise compliance "
            "costs or alter pricing power.",
        ])]),
        ("What Would Change Our Mind", [("bullets", [
            "Organic revenue growth turning negative for two consecutive quarters would signal "
            "demand deterioration beyond cycle noise.",
            "Adjusted EBITDA margin declining year over year despite the cost programs would "
            "break the margin-repair thesis.",
            "Client retention falling materially below historical levels would indicate the "
             "switching-cost moat is weakening.",
            "Free cash flow conversion deteriorating structurally would undermine the capital-return "
            "story.",
        ])]),
        VA(),
    ],
)

# ---------------------------------------------------------------- VITL
vitl = dict(
    ticker="VITL", company="Vital Farms, Inc.", verdict="BUY",
    target="$12.50", price="$9.06", price_note=PN, upside="+38%",
    sections=[
        ("Investment Thesis", [
            ("p", "Vital Farms sells something simple: pasture-raised eggs and butter at a premium "
             "price, in a category where the conventional product has been commoditized and the "
             "premium shelf is still being built. The thesis is not that eggs are a growth category; "
             "it is that branded, credence-attribute food (pasture-raised, ethically sourced) "
             "commands durable shelf space and pricing power, and Vital Farms owns the leading brand "
             "in its aisle. Revenue growth has been consistently strong because distribution is "
             "still expanding and same-store velocity is high."),
            ("p", "Our judgment is that the market prices Vital Farms like a volatile food "
             "manufacturer exposed to commodity egg prices, when the business is really a branded "
             "consumer franchise with a supply-constrained moat. The pasture-raised standard is "
             "hard to scale quickly (it requires real pasture and real farm relationships), which "
             "limits copycats and supports the premium. We tested management's margin targets "
             "against the historical pattern of input-cost shocks and recovery; the brand has "
             "repeatedly taken price without losing volume, which is the signature of pricing power."),
            ("p", "At $9.06, the multiple embeds a reversion to commodity-like margins that the "
             "track record does not support. Our probability-weighted fair value is $12.50, a 38% "
             "expected return, driven by continued distribution gains and margin normalization "
             "toward the brand's demonstrated range."),
        ]),
        ("Business Overview", [
            ("p", "Vital Farms is a food company built around pasture-raised eggs and butter, sold "
             "primarily through grocery retail in the United States. The brand's core promise is "
             "ethical sourcing: hens raised on pasture with outdoor access, sourced from a network "
             "of family farms. Products command a significant price premium over conventional and "
             "even cage-free alternatives."),
            ("p", "The business model is asset-light on production (contract family farms supply "
             "the eggs) and brand-heavy on the demand side. Growth comes from two levers: expanding "
             "distribution into new doors and regions, and increasing velocity within existing "
             "stores as consumer awareness of the pasture-raised standard grows. Gross margins are "
             "meaningfully above conventional egg economics because the premium price more than "
             "offsets higher sourcing costs, though input and freight costs create quarterly "
             "volatility."),
        ]),
        ("Forward Outlook", [
            ("p", "Where is this business going? We expect Vital Farms to keep taking share of the "
             "premium egg aisle for years, because the category conversion (conventional to cage-free "
             "to pasture-raised) is still early and the company is the recognized standard-bearer. "
             "The farm network is the binding constraint: adding contracted family farms takes time, "
             "which caps near-term growth but also protects pricing, a trade we like."),
            ("p", "Butter and adjacent categories are the second act. The same brand equity and "
             "retail relationships that built the egg business apply to pasture-raised butter and "
             "emerging products. We do not assume these become large in the base case, but they "
             "extend the runway beyond eggs. The margin story is one of scale: as revenue grows "
             "against a relatively fixed corporate cost base, operating margins should expand, "
             "partially offset by continued investment in the farm network and brand."),
            ("p", "Our bear case assumes the premium tier saturates, private label undercuts the "
             "pasture-raised price point, and input cost inflation outruns pricing. That scenario is "
             "genuinely painful and sits below today's price, which is why we sized the position of "
             "our conviction accordingly: this is a real brand, but a small-cap food company with "
             "real commodity exposure."),
        ]),
        ("Valuation", [
            ("p", "We value Vital Farms on a scenario DCF. Our base case assumes continued "
             "double-digit revenue growth tapering as distribution matures, with margins recovering "
             "toward the demonstrated brand range, discounted at a rate reflecting small-cap and "
             "commodity-input risk. Our bull case assumes faster category conversion and successful "
             "adjacency expansion. Our bear case assumes premium-tier saturation, private-label "
             "erosion, and margin compression; it sits below the current price. Probability-weighted "
             "across 25% / 50% / 25%, the fair value is $12.50, equal to our target."),
        ]),
        ("Key Risks", [("bullets", [
            "Input costs: feed, freight, and packaging inflation can compress margins faster than "
            "pricing recovers them.",
            "Supply: avian influenza or farm-network disruptions could constrain the egg supply "
            "the growth story depends on.",
            "Competition: larger food companies or private label could attack the pasture-raised "
            "premium with lower prices.",
            "Category risk: if premium egg growth stalls, the valuation multiple compresses "
            "regardless of execution.",
            "Scale: as a small-cap, quarterly results are volatile and the stock can move "
            "sharply on short-term news.",
        ])]),
        ("What Would Change Our Mind", [("bullets", [
            "Market share losses in tracked channels to private label or branded competitors "
            "would signal the moat is weaker than believed.",
            "Gross margins settling durably below the mid-30s would suggest commodity dynamics "
            "are overwhelming brand pricing power.",
            "Distribution expansion stalling (door counts flat for several quarters) would "
            "remove the primary growth lever.",
            "A sustained shift in consumer spending away from premium food tiers would "
            "undermine the category thesis.",
        ])]),
        VA(),
    ],
)

# ---------------------------------------------------------------- BKNG
bkng = dict(
    ticker="BKNG", company="Booking Holdings Inc.", verdict="BUY",
    target="$219.00", price="$159.02", price_note=PN, upside="+38%",
    sections=[
        ("Investment Thesis", [
            ("p", "Booking Holdings is the highest-quality asset in online travel: the dominant "
             "accommodation marketplace in Europe, the highest-margin business in its sector, and a "
             "capital-return machine. The market's periodic worry, that generative AI reshapes "
             "travel discovery and disintermediates aggregators, is a real long-term question but "
             "a poor near-to-medium-term investment thesis. Booking's moat is not a search ranking; "
             "it is two-sided network density: the deepest property inventory, the most reviews, "
             "and the most efficient performance-marketing engine in travel."),
            ("p", "Our judgment is that the AI-disruption fear has created the opportunity. Travel "
             "booking is a high-trust, high-consideration transaction where inventory depth, "
             "cancellation flexibility, and customer support matter more than a chat interface. "
             "Booking's own AI investments (trip planning, concierge features, the connected-trip "
             "vision) position it to absorb the new interface rather than be replaced by it. We "
             "tested the bear narrative against the numbers: take rates have held, room-night "
             "growth has continued, and alternative-accommodation supply keeps expanding."),
            ("p", "At $159.02, the market pays a multiple appropriate for a travel company facing "
             "disruption and gets a compounder that has grown through every prior platform shift. "
             "Our probability-weighted fair value is $219.00, a 38% expected return, driven by "
             "room-night growth, take-rate stability, operating leverage, and relentless buybacks."),
        ]),
        ("Business Overview", [
            ("p", "Booking Holdings operates the world's leading online travel platforms: "
             "Booking.com (accommodation, the core profit engine), Priceline, Agoda, Kayak, and "
             "OpenTable. Revenue is dominated by agency commissions on accommodation bookings, "
             "supplemented by advertising, merchant-model revenue, and ancillary services. Europe "
             "is the heartland; the company has been expanding in the US and Asia."),
            ("p", "The economics are exceptional: an asset-light marketplace with minimal "
             "marginal cost per booking, a performance-marketing machine that arbitrages Google "
             "and Meta traffic at scale, and a loyalty ecosystem (Genius) that drives direct "
             "repeat traffic. Free cash flow conversion is among the highest in large-cap "
             "technology, and the company returns nearly all of it through share repurchases."),
        ]),
        ("Forward Outlook", [
            ("p", "Where is this business going? We expect Booking to keep compounding room nights "
             "at a high-single-digit rate as global travel normalizes above trend and the company "
             "gains share in alternative accommodations, where its supply buildout is still "
             "closing the gap with the category leader. The connected-trip strategy (flights, "
             "attractions, ground transport attached to the accommodation booking) is the real "
             "growth lever: every incremental product attached to a booking raises lifetime value "
             "without proportional marketing cost."),
            ("p", "On the AI question, our view is that Booking is a net beneficiary of the new "
             "interface layer as long as it owns the transaction. Agentic booking requires live "
             "inventory, payments, cancellation handling, and support, which is infrastructure, "
             "not a chatbot. Booking is building exactly that infrastructure and partnering where "
             "it makes sense. The risk is not zero, but it is a five-year question, not a "
             "five-quarter one, and the valuation does not demand perfection."),
            ("p", "Capital return remains the quiet compounding engine: with the share count "
             "shrinking several percent per year, per-share growth will continue to outpace "
             "enterprise growth. Our bear case assumes AI-native entrants do take share, take "
             "rates compress, and buybacks slow; it is genuinely adverse and sits below today's "
             "price."),
        ]),
        ("Valuation", [
            ("p", "We value Booking on a scenario DCF. Our base case assumes high-single-digit "
             "gross-bookings growth, stable take rates, and continued operating leverage with "
             "buybacks at recent intensity, discounted at a rate appropriate for a dominant "
             "marketplace with platform-shift risk. Our bull case assumes faster connected-trip "
             "adoption and share gains in alternative accommodations. Our bear case assumes "
             "AI-driven disintermediation compresses take rates and growth; it sits below the "
             "current price. Probability-weighted across 25% / 50% / 25%, the fair value is "
             "$219.00, equal to our target."),
        ]),
        ("Key Risks", [("bullets", [
            "AI disintermediation: AI-native travel agents could bypass aggregators over time, "
            "compressing take rates or volumes.",
            "Travel cyclicality: recessions, pandemics, or geopolitical shocks hit bookings "
            "sharply and quickly.",
            "Marketing costs: dependence on Google and Meta for acquisition means rising ad "
            "prices flow directly to margins.",
            "Regulatory: European digital-markets rules and tax disputes create ongoing "
            "overhang and potential cost.",
            "Competition: Expedia, Airbnb, and direct hotel channels compete for the same "
            "travelers and supply.",
        ])]),
        ("What Would Change Our Mind", [("bullets", [
            "Room-night growth decelerating to low-single digits for a full year without a "
            "macro cause would signal structural share loss.",
            "Take rates declining persistently would indicate pricing power is eroding, "
            "possibly to AI-native competitors.",
            "A major AI travel agent capturing measurable booking share from aggregators "
            "would validate the disruption thesis.",
            "Buybacks slowing materially while cash piles up would remove a key per-share "
            "compounding driver.",
        ])]),
        VA(),
    ],
)

# ---------------------------------------------------------------- ZTS (compounder)
zts = dict(
    ticker="ZTS", company="Zoetis Inc.", verdict="BUY",
    target="$95.00", price="$69.69", price_note=PN, upside="+36%",
    sections=[
        ("Investment Thesis", [
            ("p", "Zoetis is the dominant pure-play animal health company in the world, and the "
             "rare business whose economics genuinely improve with scale: a portfolio of "
             "vaccines, parasiticides, and dermatology and pain therapeutics sold into a market "
             "where pet owners spend through cycles and livestock producers treat animal health as "
             "productivity insurance. The dermatology franchise (Apoquel, Cytopoint) and the "
             "osteoarthritis pain franchise (Librela, Solensia) are the growth engines; the "
             "parasiticide and vaccine portfolios are the durable cash base."),
            ("p", "Our judgment is that Zoetis's recent stock weakness reflects concern about the "
             "dermatology franchise facing competition and about Librela's growth cadence, not a "
             "deterioration of the underlying franchise. We tested that concern against the "
             "evidence: the pet-care spending category continues to grow, Zoetis's R&D pipeline in "
             "monoclonal antibodies and novel parasiticides remains the industry's deepest, and "
             "the livestock business provides a cyclical offset. The franchise economics, "
             "double-digit ROIC sustained for a decade, gross margins near 70%, and free-cash-flow "
             "conversion above 80%, remain intact and verified from history."),
            ("p", "Zoetis meets our compounder-quality criteria: a 2016-2025 streak of ROIC above "
             "15%, stable to expanding gross margins, and FCF conversion above 80%, all verified "
             "from reported history rather than projected. That standing earns a 15-year explicit "
             "forecast horizon, an 8-8.5% base discount rate, and a 3.0% terminal growth cap "
             "applied to a demonstrated sustained terminal margin. It is falsifiable: two "
             "consecutive years of ROIC below 15%, or a gross-margin contraction of 200bp or more, "
             "revokes the qualification and the valuation reverts to standard terms."),
            ("p", "At $69.69, the market prices Zoetis as though the growth franchises are "
             "permanently impaired. Our probability-weighted fair value is $95.00, a 36% expected "
             "return, earned through the compounding of a best-in-class animal health portfolio, "
             "not through a return to peak multiples."),
        ]),
        ("Business Overview", [
            ("p", "Zoetis discovers, develops, manufactures, and commercializes medicines, "
             "vaccines, and diagnostics for companion animals and livestock. The companion-animal "
             "segment is the growth driver: dermatology (Apoquel, Cytopoint), osteoarthritis pain "
             "(Librela for dogs, Solensia for cats), and parasiticides (Simparica franchise). The "
             "livestock segment (cattle, swine, poultry, fish, sheep) provides vaccines, "
             "anti-infectives, and productivity products with more cyclical but still attractive "
             "economics."),
            ("p", "The business model is that of a specialty pharmaceutical company with better "
             "payer dynamics than human pharma: pet owners pay out of pocket and are "
             "price-insensitive about their animals' suffering, which supports pricing power; "
             "regulatory pathways are shorter; and the R&D engine has produced a steady cadence of "
             "blockbuster franchises. Gross margins near 70% reflect the value of patented "
             "therapeutics and manufacturing scale."),
        ]),
        ("Forward Outlook", [
            ("p", "Where is this business going? We expect the osteoarthritis pain franchise to be "
             "the defining growth story of the next five years: Librela and Solensia address "
             "enormous undertreated populations, and monoclonal-antibody therapies have long "
             "product lives with limited generic pressure. Dermatology will grow more slowly as "
             "competition intensifies, but from a large and still-expanding base; the franchise "
             "has multiple years of patent-protected runway."),
            ("p", "The livestock business should benefit from protein-demand growth and from "
             "Zoetis's diagnostics and genetics offerings, which deepen the relationship with "
             "producers beyond individual products. Across the portfolio, we expect revenue "
             "growth in the high-single digits with operating leverage from the high gross-margin "
             "structure, funding both R&D reinvestment and substantial capital returns."),
            ("p", "Our bear case assumes dermatology share losses accelerate, Librela adoption "
             "stalls on safety or efficacy concerns, and livestock cyclicality turns; it is "
             "genuinely adverse and sits below today's price. The compounder qualification "
             "described above is the guardrail on our optimism: if the returns on capital "
             "deteriorate for two straight years, the framework itself forces a re-rating of the "
             "valuation terms."),
        ]),
        ("Valuation", [
            ("p", "We value Zoetis on a scenario DCF under compounder-quality terms. Our base "
             "case assumes high-single-digit revenue growth led by the pain franchise and "
             "dermatology, with margins sustained near demonstrated levels, discounted at 8-8.5% "
             "over a 15-year explicit horizon. Our bull case assumes faster Librela/Solensia "
             "adoption and successful pipeline launches. Our bear case assumes franchise erosion "
             "and margin contraction; it sits below the current price and would, if realized "
             "through the ROIC and margin triggers, revoke the compounder qualification. Terminal "
             "growth is capped at 3.0% on a demonstrated sustained margin. Probability-weighted "
             "across 25% / 50% / 25%, the fair value is $95.00, equal to our target."),
        ]),
        ("Key Risks", [("bullets", [
            "Franchise concentration: dermatology and pain products are a large share of growth; "
            "competition or safety issues there hit disproportionately.",
            "Librela adoption: slower-than-expected uptake or emerging safety signals would "
            "impair the key growth driver.",
            "Livestock cyclicality: protein-price downturns and disease outbreaks affect the "
            "livestock segment quickly.",
            "Generic and biosimilar pressure: key products will eventually face competition; "
            "the timing and severity are uncertain.",
            "Pricing scrutiny: sustained high price increases could invite regulatory or "
            "retailer pushback.",
        ])]),
        ("What Would Change Our Mind", [("bullets", [
            "ROIC falling below 15% for two consecutive years would revoke the compounder "
            "qualification and force a full valuation reset.",
            "A gross-margin contraction of 200bp or more on a sustained basis would do the same.",
            "Librela/Solensia revenue declining year over year would break the pain-franchise "
            "growth thesis.",
            "FCF conversion falling durably below 80% would signal the cash-compounding "
            "economics are deteriorating.",
        ])]),
        VA(ZTS_METHOD),
    ],
)

# ---------------------------------------------------------------- EXE
exe = dict(
    ticker="EXE", company="Expand Energy Corporation", verdict="BUY",
    target="$112.00", price="$85.52", price_note=PN, upside="+31%",
    sections=[
        ("Investment Thesis", [
            ("p", "Expand Energy, formed from the merger of Chesapeake and Southwestern, is now "
             "the largest natural gas producer in the United States, with premier acreage in the "
             "Marcellus, Haynesville, and other basins. The investment case is straightforward: "
             "scale lowers per-unit costs, a low-decline inventory supports decades of drilling, "
             "and the company's capital discipline (maintenance-mode production, free cash flow "
             "returned to shareholders) converts a commodity business into a cash machine across "
             "the cycle."),
            ("p", "Our judgment is that the market still prices Expand like the old Chesapeake, "
             "a leveraged gas-price lottery ticket, when the merged company is a different animal: "
             "lower leverage, lower breakevens, and a management team whose stated strategy is "
             "returns over growth. The structural demand story for US natural gas, LNG exports, "
             "power-generation demand including data centers, and industrial reshoring, provides a "
             "durable bid under volumes that the spot price does not fully reflect."),
            ("p", "At $85.52, the valuation embeds a gas-price deck well below what the forward "
             "curve and the structural demand picture support. Our probability-weighted fair value "
             "is $112.00, a 31% expected return, driven by free cash flow generation and the "
             "dividend-plus-buyback framework rather than a bet on a gas-price spike."),
        ]),
        ("Business Overview", [
            ("p", "Expand Energy is a natural gas exploration and production company created by "
             "the combination of Chesapeake Energy and Southwestern Energy. Its core operating "
             "areas are the Marcellus shale in Appalachia and the Haynesville shale in Louisiana "
             "and East Texas, among the lowest-cost natural gas basins in the world. The company "
             "also holds oil and liquids production that diversifies the revenue mix."),
            ("p", "The strategy is maintenance production with capital discipline: drill enough "
             "to hold volumes roughly flat, keep costs among the lowest in the industry, and "
             "return the resulting free cash flow to shareholders through a base dividend plus "
             "variable buybacks. Hedging smooths near-term price exposure. The merger synergies, "
             "operational (drilling and completion efficiencies, overhead reduction) and "
             "commercial (marketing scale, LNG optionality), are the near-term earnings driver."),
        ]),
        ("Forward Outlook", [
            ("p", "Where is this business going? We see Expand as the consolidator and low-cost "
             "anchor of US natural gas. The next three years should deliver the merger synergies "
             "in full, continued per-unit cost reduction from scale and longer laterals, and "
             "growing exposure to premium-priced demand: LNG export capacity additions and "
             "power demand growth both pull on exactly the basins Expand dominates."),
            ("p", "The capital framework is the compounding mechanism. At mid-cycle gas prices, "
             "the maintenance capex leaves substantial free cash flow; the base dividend is "
             "covered at low prices and buybacks accelerate when the stock trades below intrinsic "
             "value. We expect the share count to shrink meaningfully over the forecast, so "
             "per-share free cash flow grows faster than the commodity."),
            ("p", "Our bear case assumes a sustained gas-price collapse (oversupply, weak LNG "
             "demand, or a warm-winter glut), synergy shortfalls, and a dividend cut; it is "
             "genuinely adverse and sits below today's price. Gas is a commodity and this is a "
             "commodity equity; the margin of safety comes from the cost position and the "
             "balance sheet, not from price forecasting."),
        ]),
        ("Valuation", [
            ("p", "We value Expand on a scenario DCF tied to natural gas price decks. Our base "
             "case assumes mid-cycle gas pricing consistent with the structural demand picture, "
             "full realization of merger synergies, and the stated capital-return framework, "
             "discounted at a rate reflecting commodity E&P risk. Our bull case assumes stronger "
             "LNG-driven pricing and faster synergy capture. Our bear case assumes a prolonged "
             "price slump and synergy misses; it sits below the current price. Probability-weighted "
             "across 25% / 50% / 25%, the fair value is $112.00, equal to our target."),
        ]),
        ("Key Risks", [("bullets", [
            "Commodity price: natural gas prices are volatile; a sustained downturn impairs cash "
            "flow and the dividend.",
            "Merger integration: synergy targets may slip on operational or cultural friction.",
            "Regulatory: methane rules, permitting, and pipeline constraints can raise costs or "
            "limit growth.",
            "Hedging: the hedge book can create opportunity cost in a price spike and "
            "mark-to-market noise.",
            "Capital allocation: any return to growth-mode drilling at the expense of returns "
            "would break the thesis.",
        ])]),
        ("What Would Change Our Mind", [("bullets", [
            "A strategic pivot back to production growth at the expense of free cash flow would "
            "abandon the returns framework.",
            "Synergy realization falling well short of stated targets would undermine the merger "
            "economics.",
            "Leverage rising materially above the stated target range would recreate the old "
            "balance-sheet risk.",
            "A structural demand reversal (e.g., LNG project cancellations at scale) would "
            "impair the long-term price deck.",
        ])]),
        VA(),
    ],
)

# ---------------------------------------------------------------- FISV
fisv = dict(
    ticker="FISV", company="Fiserv, Inc.", verdict="BUY",
    target="$58.00", price="$44.36", price_note=PN, upside="+31%",
    sections=[
        ("Investment Thesis", [
            ("p", "Fiserv is the quiet infrastructure of American small-business payments. Clover, "
             "its point-of-sale platform, continues to take share among small and mid-size "
             "merchants; the core-account processing business serves thousands of banks and credit "
             "unions that renew because switching is operationally painful. The stock's 2025-2026 "
             "weakness, driven by a growth deceleration and a CEO transition overhang, has "
             "compressed the multiple to a level that no longer reflects the durability of the "
             "franchise."),
            ("p", "Our judgment is that the deceleration is cyclical and mix-related, not "
             "structural. Clover's competitive position against Square, Toast, and Stripe Terminal "
             "remains strong on distribution (bank and ISO channels) and on integrated software "
             "depth; the core processing business is as sticky as it has ever been. We haircut "
             "management's growth targets where the evidence warrants, particularly on the pace "
             "of the Clover international rollout, but the base business earns its multiple."),
            ("p", "At $44.36, the market prices Fiserv like a melting legacy processor. Our "
             "probability-weighted fair value is $58.00, a 31% expected return, driven by "
             "re-accelerating organic growth, margin expansion from the efficiency programs, and "
             "continued buybacks shrinking the share count."),
        ]),
        ("Business Overview", [
            ("p", "Fiserv provides payments and financial-services technology. The Merchant "
             "Solutions segment (anchored by Clover) offers point-of-sale hardware, payment "
             "processing, and integrated business software to merchants of all sizes. The "
             "Financial Solutions segment provides core account processing, digital banking, "
             "payments, and risk tools to banks and credit unions. Revenue is heavily recurring, "
             "and client retention in core processing is among the highest in financial "
             "technology."),
            ("p", "The economics combine a growth engine (Clover, expanding internationally and "
             "upmarket) with a cash cow (core processing, high retention, incremental margins on "
             "cross-sold modules). Free cash flow conversion is strong, and the company has a "
             "long history of returning capital through buybacks."),
        ]),
        ("Forward Outlook", [
            ("p", "Where is this business going? We expect Clover to remain the growth engine: "
             "the US small-business digitization wave still has room, the ISO and bank referral "
             "channels give Clover distribution that pure-play competitors cannot easily "
             "replicate, and the software attach (inventory, payroll, lending) raises revenue per "
             "merchant each year. International expansion is the swing factor; we model it "
             "conservatively because cross-border payments rollouts have a history of slipping."),
            ("p", "The core processing business should grow in the low-to-mid single digits, "
             "driven by digital banking adoption and real-time payments modules sold into the "
             "installed base. Combined with the efficiency programs, this yields operating "
             "leverage: we expect margins to expand even as the company invests in Clover's "
             "growth. Capital allocation should remain buyback-heavy, compounding per-share "
             "results."),
            ("p", "Our bear case assumes Clover share losses to competitors, a deeper "
             "deceleration in the merchant segment, and stalled margin programs; it is genuinely "
             "adverse and sits below today's price. The key variable we watch is Clover's "
             "volume growth relative to the industry, the cleanest read on competitive position."),
        ]),
        ("Valuation", [
            ("p", "We value Fiserv on a scenario DCF. Our base case assumes organic growth "
             "re-accelerating to the high-single digits led by Clover, with margin expansion from "
             "efficiency programs and a steady buyback, discounted at a standard rate for a "
             "durable payments franchise. Our bull case assumes faster Clover international "
             "traction and stronger operating leverage. Our bear case assumes competitive share "
             "loss and growth stagnation; it sits below the current price. Probability-weighted "
             "across 25% / 50% / 25%, the fair value is $58.00, equal to our target."),
        ]),
        ("Key Risks", [("bullets", [
            "Competition: Square, Toast, Stripe, and Adyen compete aggressively for the same "
            "merchants, pressuring pricing and win rates.",
            "Growth deceleration: if the merchant slowdown proves structural rather than "
            "cyclical, the multiple may not recover.",
            "Execution: the CEO transition and efficiency programs introduce operational risk.",
            "Bank consolidation: mergers among financial-institution clients can reduce the "
            "customer base.",
            "Macro: consumer-spending weakness flows directly to payments volume.",
        ])]),
        ("What Would Change Our Mind", [("bullets", [
            "Clover volume growth trailing the industry for several consecutive quarters would "
            "signal competitive share loss.",
            "Organic revenue growth staying in the low-single digits beyond the current "
            "slowdown would indicate a structural problem.",
            "Margin contraction despite the efficiency programs would break the operating-"
            "leverage thesis.",
            "Client retention in core processing deteriorating would undermine the durability "
            "argument.",
        ])]),
        VA(),
    ],
)

# ---------------------------------------------------------------- TMUS
tmus = dict(
    ticker="TMUS", company="T-Mobile US, Inc.", verdict="BUY",
    target="$205.00", price="$163.64", price_note=PN, upside="+25%",
    sections=[
        ("Investment Thesis", [
            ("p", "T-Mobile is the best-run wireless carrier in the United States, and it is not "
             "close. The Sprint merger delivered the spectrum depth that now underwrites the "
             "industry's best 5G network; postpaid subscriber growth has led the industry for "
             "years; and the synergy realization is largely complete, which means the earnings "
             "story from here is straightforward operating leverage plus capital return. The "
             "market treats wireless as a zero-sum share-shift game; T-Mobile is the company "
             "doing the shifting."),
            ("p", "Our judgment is that the next leg of the story is the convergence of "
             "subscriber growth, ARPU stability, and a buyback program funded by prodigious free "
             "cash flow. T-Mobile's network advantage is durable because mid-band spectrum "
             "cannot be quickly replicated, and the company's brand and value positioning keep "
             "churn the lowest in the industry. We tested the growth assumptions against "
             "demographic and household-formation data rather than extrapolating the Sprint-era "
             "surge; even normalized, the subscriber trajectory supports the valuation."),
            ("p", "At $163.64, the valuation implies the growth premium fades quickly. Our "
             "probability-weighted fair value is $205.00, a 25% expected return, earned through "
             "continued subscriber gains, margin expansion, and one of the most aggressive "
             "buyback programs in large-cap telecom."),
        ]),
        ("Business Overview", [
            ("p", "T-Mobile US is the second-largest wireless carrier in the United States by "
             "subscribers, offering postpaid, prepaid (Metro), and wholesale wireless services, "
             "plus a fast-growing fixed-wireless home internet business. The 2020 acquisition of "
             "Sprint gave T-Mobile a deep mid-band spectrum portfolio (2.5 GHz) that powers its "
             "5G network, widely regarded as the fastest and most extensive in the country."),
            ("p", "The economics are those of a scale telecom: high fixed costs, very low marginal "
             "cost per subscriber, and therefore powerful operating leverage as the base grows. "
             "Churn is the key operating metric, and T-Mobile's is the industry's lowest. Free "
             "cash flow, now that merger integration spending is behind, funds dividends and "
             "large buybacks."),
        ]),
        ("Forward Outlook", [
            ("p", "Where is this business going? We expect T-Mobile to keep taking postpaid share "
             "for the next several years, driven by the network advantage and by segments where "
             "it is underpenetrated: smaller markets and rural coverage (where the spectrum "
             "depth now allows credible competition), business and government accounts, and "
             "fixed-wireless home internet, which monetizes excess network capacity at high "
             "incremental margins."),
            ("p", "The financial trajectory is operating leverage plus buybacks: revenue growth "
             "in the mid-single digits, EBITDA margins expanding as the subscriber base scales "
             "against a largely fixed cost base, and the share count shrinking several percent "
             "per year. We do not assume a price war ends or begins; we assume rational "
             "competition continues, which the industry's recent history supports."),
            ("p", "Our bear case assumes subscriber growth stalls, promotional intensity "
             "compresses ARPU, and the buyback slows; it is genuinely adverse and sits below "
             "today's price. Wireless is a mature industry and the upside is compounding, not "
             "transformation; the margin of safety is the network moat and the cash generation."),
        ]),
        ("Valuation", [
            ("p", "We value T-Mobile on a scenario DCF. Our base case assumes continued "
             "industry-leading postpaid net additions tapering to market growth, stable ARPU, "
             "margin expansion from operating leverage, and buybacks at recent intensity, "
             "discounted at a rate appropriate for a stable, cash-generative telecom leader. Our "
             "bull case assumes faster share gains in underpenetrated segments and stronger "
             "fixed-wireless growth. Our bear case assumes stalled subscriber growth and "
             "promotional pressure; it sits below the current price. Probability-weighted across "
             "25% / 50% / 25%, the fair value is $205.00, equal to our target."),
        ]),
        ("Key Risks", [("bullets", [
            "Competition: AT&T and Verizon can match promotions and network claims, and cable "
             "MVNOs compete aggressively on price.",
             "Saturation: the US wireless market is mature; long-term growth depends on share "
             "gains and ARPU, both of which can stall.",
             "Capital intensity: network leadership requires sustained capex; technology shifts "
             "(e.g., satellite) could alter the investment calculus.",
             "Regulatory: spectrum policy, merger scrutiny, and consumer-protection rules "
             "affect strategy and costs.",
            "Leverage: the balance sheet still carries merger-era debt; buyback capacity "
             "depends on continued deleveraging.",
        ])]),
        ("What Would Change Our Mind", [("bullets", [
            "Postpaid net additions turning negative for two consecutive quarters would signal "
            "the share-gain engine has stalled.",
            "Churn rising to parity with competitors would indicate the network and brand "
            "advantage is eroding.",
            "ARPU declining persistently under promotional pressure would break the revenue-"
            "quality thesis.",
            "Buybacks slowing materially while leverage stays elevated would remove a key "
            "per-share compounding driver.",
        ])]),
        VA(),
    ],
)

# ---------------------------------------------------------------- build
NOTES = [sofi, fis, vitl, bkng, zts, exe, fisv, tmus]

if __name__ == "__main__":
    import os
    outdir = "/home/hatch/workspace/standalone-notes/pdfs"
    os.makedirs(outdir, exist_ok=True)
    for n in NOTES:
        path = os.path.join(outdir, "%s-equity-research-note.pdf" % n["ticker"])
        build_note(path, n)
        print("built", path)
