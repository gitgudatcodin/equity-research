"""Build 8 standalone equity research PDFs (wave 6). Zero self-reference rule enforced by pre-build grep."""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note
from pypdf import PdfReader

BANNED = ["old target", "previous note", "previous report", "prior report",
          "as we wrote", "prior methodology", "v2", "rebuild", "rebuilt",
          "addenda", "version", "upgraded", "downgraded", "was previously", "formerly"]

def check_banned(text, label):
    low = text.lower()
    for b in BANNED:
        if re.search(r"\b" + re.escape(b) + r"s?\b", low):
            raise SystemExit("BANNED PHRASE %r found in %s" % (b, label))

def meth(horizon_years, base_rate, extra=""):
    t = ("Our valuation is a probability-weighted scenario DCF. We model bear, base, and bull "
         "cases over an explicit forecast horizon \u2014 10 years for most businesses, 15 years for "
         "businesses meeting our compounder-quality criteria (10+ years of ROIC above 15%, stable "
         "or expanding gross margins, free-cash-flow conversion above 80%, all verified from "
         "history, never projected) \u2014 weighted 25% / 50% / 25%. Discount rates are "
         "scenario-specific: the base rate reflects fundamental business risk (9% for stable "
         "franchises, 10% standard, 12% or higher for speculative situations; 8\u20138.5% for "
         "compounder-quality businesses whose predictable cash flows genuinely lower risk); the "
         "bear case adds 250bp, the bull case subtracts 150bp (floor 8%). Terminal value assumes "
         "no more than 2.5% perpetual growth (3.0% for compounder-quality businesses) applied to "
         "normalized mid-cycle margins \u2014 never peak margins \u2014 and any terminal value "
         "exceeding 70% of enterprise value is haircut and disclosed. Bear cases are required to "
         "be genuinely adverse and to sit below the current price. Management guidance is never "
         "accepted at face value; it is independently tested and haircut where evidence warrants. "
         "For international businesses we add an explicit country-risk premium to the discount "
         "rate and benchmark multiples against regional peers facing similar risks, never US peers "
         "alone; structural risks (e.g. VIE structures, regulatory confiscation) are modeled in "
         "cash flows and the bear case.")
    t += " We value this business over a %d-year horizon at a %s base discount rate." % (horizon_years, base_rate)
    if extra:
        t += " " + extra
    return t

MELI_EXTRA = ("For this business we add an explicit 200bp country-risk premium to the discount "
              "rate, reflecting Latin American macroeconomic, currency, and regulatory risk, and "
              "we benchmark multiples against regional peers facing similar risks, never US peers alone.")

# ---------------------------------------------------------------- NFLX
nflx = dict(
    ticker="NFLX", company="Netflix, Inc.", verdict="SELL",
    target="$48.00", price="$67.06", upside="-28%",
    sections=[
        ("Investment Thesis", [
            ("p", "Netflix is a superb operating business selling at a price that assumes it is an "
             "unstoppable compounding machine. With more than 300 million paid memberships, global "
             "scale, and genuine free-cash-flow generation, the company has earned its place as the "
             "winner of the streaming wars. The problem is not the business. The problem is what the "
             "share price demands the business must still become: at $67.06, the market is paying for "
             "a decade of uninterrupted, high-margin growth that the engagement data no longer supports."),
            ("p", "The decisive fact is the divergence between content spending and engagement. View "
             "hours grew only about 2% in the first half of 2026 while the content budget keeps "
             "rising. Each marginal dollar of content is buying less viewing \u2014 the signature of a "
             "mature platform, not a growth compounder. The paid-sharing lift from the password-sharing "
             "crackdown, which powered the last leg of subscriber growth, was a one-time step-up in the "
             "paying base, not a repeatable engine. With engagement flat, the company has leaned on "
             "repeated price increases to drive revenue, and price hikes on flat engagement face hard "
             "limits: churn and piracy."),
            ("p", "Earnings quality deserves equal skepticism. Netflix carries roughly $33.8 billion of "
             "content assets on amortization schedules that are inherently judgmental \u2014 management "
             "decides, within wide latitude, how fast capitalized content costs flow through the income "
             "statement. Reported margins are therefore softer than they appear. Free cash flow tells a "
             "cleaner story, but 2026 cash flow is flattered by a one-time $2.8 billion Warner Bros. "
             "Discovery termination fee that does not recur; normalized free cash flow is about $10.3 "
             "billion, a materially lower base from which the market's growth expectations must be met."),
            ("p", "Our probability-weighted fair value is $48.00, 28% below the current price. The "
             "asymmetry is stark: even our bull case, at $78.79, barely clears today's price, while our "
             "bear case sits at $20.14. When the entire plausible upside is a few percent and the "
             "downside is measured in halves, the correct posture is to sell. SELL."),
        ]),
        ("Business Overview", [
            ("p", "Netflix is the world's largest subscription video streaming service, operating in "
             "more than 190 countries with a content library spanning licensed programming and a large "
             "and growing slate of original films and series. Revenue comes primarily from monthly "
             "membership fees across ad-free tiers, supplemented by a lower-priced advertising-supported "
             "tier launched in late 2022 and a nascent games initiative."),
            ("p", "The company's moat rests on scale: a global subscriber base amortizes content costs "
             "that regional competitors cannot match, and its recommendation and personalization systems "
             "benefit from the largest viewing dataset in the industry. The ad-supported tier adds a "
             "second revenue stream with structurally higher incremental margins, since advertising "
             "revenue requires no additional content spend."),
            ("p", "Competition for attention is broader than the traditional streaming set. YouTube, "
             "TikTok, and gaming compete for the same leisure hours, and several of these competitors "
             "acquire their content effectively for free through user generation. Netflix must pay cash "
             "for every hour it hopes its subscribers will watch."),
        ]),
        ("Forward Outlook", [
            ("p", "Our judgment is that Netflix is entering a structurally slower phase that the market "
             "has not yet priced. The subscriber base in developed markets is approaching saturation; "
             "future net additions will skew toward lower-ARPU regions and the ad tier, which dilutes "
             "average revenue per member even as headline subscriber counts grow. Management will "
             "continue to raise prices to manufacture revenue growth, but each increase on flat "
             "engagement raises churn risk and pushes marginal viewers toward piracy or free alternatives."),
            ("p", "The advertising tier is the most credible growth lever, and we expect it to scale "
             "meaningfully over the next three years. But it is a lower-ARPU, cyclically exposed revenue "
             "stream, and its growth partly cannibalizes full-price subscriptions as existing members "
             "trade down. Net-net, we see revenue growing at a mid-single-digit rate \u2014 respectable "
             "for a mature media business, but incompatible with a growth multiple."),
            ("p", "Longer term, the content-cost treadmill only steepens. Sports rights, live events, and "
             "gaming are logical adjacencies, but each carries the same economics: large upfront cash "
             "outlays for uncertain engagement returns. The era in which Netflix could outspend "
             "competitors into submission is ending, because the spending no longer reliably converts "
             "into viewing. A mature, cash-generative media utility is a fine business to own \u2014 at a "
             "utility-like multiple, which $67.06 is not."),
        ]),
        ("Valuation", [
            ("p", "We value Netflix on a 10-year scenario DCF at a 10% base discount rate, with terminal "
             "value computed on normalized 23% free-cash-flow margins \u2014 deliberately not peak "
             "margins. Base-case revenue compounds at 6.0% annually, and 2026 free cash flow is "
             "normalized to $10.3 billion with the one-time $2.8 billion Warner Bros. Discovery "
             "termination fee stripped out, since it does not recur."),
            ("table", (["Scenario", "Fair value", "What it assumes"], [
                ["Bear", "$20.14", "Revenue growth stalls near 3%; engagement declines as price hikes drive churn and piracy; FCF margins compress to the mid-teens; 12.5% discount rate"],
                ["Base", "$45.57", "6.0% revenue CAGR; normalized 2026 FCF of $10.3B; 10% discount rate; terminal value on normalized 23% FCF margins"],
                ["Bull", "$78.79", "Ad tier scales with accretive ARPU; pricing power holds without churn; margins expand; 8.5% discount rate"],
            ])),
            ("p", "Weighting the scenarios 25% / 50% / 25% gives a probability-weighted fair value of "
             "$47.52, which we round to our $48.00 target. Note the skew: even the bull case ($78.79) "
             "barely clears the current $67.06 price, while the bear case implies a two-thirds loss. "
             "There is almost no compensation here for the risk being taken."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Engagement deterioration: if view hours decline outright, the pricing-power thesis collapses and churn accelerates.",
                "Content amortization judgment: the $33.8 billion content asset balance rests on management's amortization schedules; faster write-downs would reveal lower true margins.",
                "Competition for attention from free platforms (YouTube, TikTok) that do not bear content cash costs.",
                "Ad-market cyclicality: a recession would hit the ad tier just as it becomes material to growth.",
                "Currency headwinds: a majority of members are outside the US, and dollar strength mechanically depresses reported growth.",
                "Regulatory risk: content quotas, taxation of digital services, and data rules across 190+ jurisdictions.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Sustained double-digit view-hour growth on a rising content budget \u2014 evidence the marginal content dollar is working again.",
                "A price increase cycle with no measurable uptick in churn, proving genuine pricing power on flat engagement.",
                "Free-cash-flow conversion structurally above 60% of operating income for two consecutive years.",
                "The ad tier demonstrating accretive blended ARPU rather than cannibalization of full-price plans.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", meth(10, "10%")),
        ]),
    ],
)

# ---------------------------------------------------------------- AMZN
amzn = dict(
    ticker="AMZN", company="Amazon.com, Inc.", verdict="REDUCE",
    target="$173.00", price="$251.52", upside="-31%",
    sections=[
        ("Investment Thesis", [
            ("p", "Amazon owns two of the best businesses built in the last thirty years: AWS, the "
             "dominant cloud infrastructure franchise, and a retail operation whose logistics network "
             "constitutes a nearly unassailable moat. Advertising, the third leg, is a high-margin "
             "compounder growing from the traffic the other two create. We have no quarrel with the "
             "quality of these assets. Our quarrel is with the price: at $251.52, the market is paying "
             "for AWS reacceleration, retail margin expansion, and advertising scale all arriving "
             "together, on schedule, without friction."),
            ("p", "AWS is the crux. Cloud growth has settled into the high teens, and the incremental "
             "revenue dollar is more contested than ever: Microsoft and Google compete aggressively on "
             "price and bundle AI tooling, while the largest customers are designing their own silicon "
             "and negotiating ever-larger discounts. AWS remains the leader, but leadership in a "
             "maturing market earns a maturing multiple, and the current price assumes the hypergrowth "
             "era resumes."),
            ("p", "Retail, for all its scale, remains a structurally low-margin business. Automation and "
             "advertising attach have lifted North American margins, but the international segment still "
             "earns little, and the next leg of efficiency requires capital spending that depresses free "
             "cash flow today for uncertain returns tomorrow. Project Kuiper \u2014 the satellite "
             "broadband constellation \u2014 is a genuine capital sink with a decade-long payback, and "
             "it sits inside the valuation at full optimism."),
            ("p", "The arithmetic of the current price is worth stating plainly. Amazon's market "
             "capitalization near $2.6 trillion prices the company at a multiple of free cash flow "
             "that only makes sense if AWS margins never compress, retail earns software-like returns, "
             "and advertising growth never decelerates. Each of those assumptions is individually "
             "optimistic; jointly, they leave no margin for the ordinary disappointments \u2014 a delayed "
             "enterprise migration cycle, a cloud price war, a consumer slowdown \u2014 that periodically "
             "visit even the best businesses."),
            ("p", "Our probability-weighted fair value is $173.00, 31% below the current price. We rate "
             "the shares REDUCE rather than SELL because the underlying franchises are exceptional and "
             "deserve some representation \u2014 but at this price the expected return is negative, and "
             "capital has better risk-adjusted homes."),
        ]),
        ("Business Overview", [
            ("p", "Amazon operates three segments. North America and International retail comprise the "
             "e-commerce marketplace, first-party sales, Prime subscriptions, and the physical store "
             "footprint led by Whole Foods. AWS provides compute, storage, databases, and AI services to "
             "enterprises and startups globally. Advertising \u2014 reported within the retail segments "
             "\u2014 sells sponsored placements to merchants and brands, and has become one of the "
             "highest-margin revenue streams in the company."),
            ("p", "The flywheel is well understood: Prime membership drives retail frequency, retail "
             "traffic feeds the advertising business, and AWS funds the capital intensity of the whole "
             "enterprise. Few companies in history have combined this scale with this many simultaneous "
             "reinvestment opportunities."),
        ]),
        ("Forward Outlook", [
            ("p", "Advertising deserves emphasis as the swing factor in our valuation. It is Amazon's "
             "highest-margin growth engine and the least appreciated source of operating leverage: "
             "every incremental ad dollar carries minimal cost. We model it compounding at a premium "
             "to retail for the full horizon. But advertising is also the most cyclically exposed leg "
             "\u2014 brand budgets are cut early in downturns \u2014 and its growth rate must eventually "
             "converge toward e-commerce growth as penetration saturates. Our base case assumes a "
             "graceful deceleration; the market assumes none."),
            ("p", "Our judgment is that the next three years are heavy-investment years with uncertain "
             "payoff timing. AI-related capital expenditure \u2014 data centers, custom Trainium chips, "
             "power procurement \u2014 will run at record levels, and while some of this spending clearly "
             "earns high returns, the aggregate return on the AI capex wave will not be known until the "
             "capacity is absorbed. Markets are currently capitalizing the spending as if the returns are "
             "assured."),
            ("p", "In retail, we expect steady but unspectacular progress: low-single-digit unit growth, "
             "continued automation gains, and advertising growth gradually decelerating as the base "
             "compounds. Kuiper will consume billions before generating meaningful revenue, and "
             "regulatory scrutiny of marketplace practices remains a live overhang in both the US and "
             "Europe. The business will be larger and more profitable in five years \u2014 our dispute "
             "is with the multiple the market applies to that future today."),
            ("p", "Longer term, the question is whether AWS can defend its margins as AI workloads "
             "commoditize inference. History suggests infrastructure margins compress as technology "
             "standardizes; AWS's scale and enterprise entrenchment argue for a slower fade than "
             "skeptics expect. Either way, the current price leaves no room for the fade at all."),
        ]),
        ("Valuation", [
            ("p", "We value Amazon on a 10-year scenario DCF at a 10% base discount rate. Our bear case "
             "assumes AWS share loss to Azure and GCP with sustained price competition, retail margins "
             "compressing as wage and logistics costs outrun automation gains, and Kuiper becoming a "
             "multi-year drag on free cash flow. The base case assumes AWS growth in the mid-teens with "
             "gradual margin normalization, retail margins grinding modestly higher, and advertising "
             "continuing to compound at a premium to retail growth. The bull case assumes an AI workload "
             "supercycle that reaccelerates AWS into the mid-20s, retail operating margins reaching "
             "double digits, and advertising becoming a $100 billion-plus high-margin engine."),
            ("p", "Probability-weighting the scenarios 25% / 50% / 25% produces a fair value of $173.00, "
             "our target. The bear case sits well below the current price, reflecting how much of the "
             "valuation rests on everything going right simultaneously across three distinct businesses."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "AWS deceleration: a sharper-than-expected slowdown in cloud growth would remove the primary engine of profit expansion.",
                "AI capex returns: record data-center spending may earn sub-par returns if capacity outruns demand.",
                "Retail margin pressure from wage inflation, fuel costs, and competitive discounting.",
                "Kuiper capital intensity with uncertain commercial returns.",
                "Antitrust and regulatory action in the US and EU targeting marketplace or cloud practices.",
                "Advertising cyclicality in an economic downturn.",
                "Prime membership saturation in developed markets limiting the frequency flywheel.",
                "Trainium and custom-silicon bets underdelivering against entrenched merchant-chip ecosystems, stranding AI capex.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "AWS reaccelerating above 20% growth for four consecutive quarters with stable margins.",
                "Retail operating margins sustainably above 8% in North America, proving structural leverage.",
                "Kuiper reaching cash-flow breakeven ahead of plan, removing the capital-sink overhang.",
                "A 20%+ decline in the share price with no deterioration in AWS or advertising fundamentals.",
                "Advertising sustaining 20%+ growth for two consecutive years while AWS margins expand \u2014 evidence of operating leverage the market is right to pay for.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", meth(10, "10%")),
        ]),
    ],
)

# ---------------------------------------------------------------- AVGO
avgo = dict(
    ticker="AVGO", company="Broadcom Inc.", verdict="REDUCE",
    target="$240.00", price="$355.14", upside="-32%",
    sections=[
        ("Investment Thesis", [
            ("p", "Broadcom has executed one of the most successful roll-up strategies in technology "
             "history: acquiring entrenched semiconductor and infrastructure-software franchises, "
             "extracting costs with unusual discipline, and returning the proceeds to shareholders. The "
             "company sits at the center of the two most powerful enterprise-technology trends of the "
             "decade \u2014 AI networking, where its Ethernet portfolio is the connective tissue of AI "
             "clusters, and custom AI accelerators, where its co-design programs with hyperscalers offer "
             "an alternative to merchant GPUs. This is a genuinely advantaged position."),
            ("p", "It is also a cyclically peak position being priced as a permanent plateau. At $355.14, "
             "the market assumes the AI infrastructure buildout continues without a digestion phase, "
             "that hyperscaler capital spending grows indefinitely, and that custom-silicon programs \u2014 "
             "which belong to the customers, not to Broadcom \u2014 are never delayed, cancelled, or "
             "insourced. Semiconductor history is unambiguous on this point: every capex supercycle in "
             "the industry's history has been followed by a digestion period in which orders fall faster "
             "than anyone models. The current price contains no digestion."),
            ("p", "The VMware leg adds a second source of fragility. The acquisition thesis rests on "
             "raising prices on a locked-in enterprise installed base, and early results have validated "
             "the pricing power. But aggressive price increases on mission-critical virtualization "
             "software are accelerating customer evaluations of alternatives \u2014 open-source "
             "hypervisors, public-cloud migration, and competing platforms. Pricing power extracted too "
             "fast converts a durable annuity into a melting ice cube."),
            ("p", "Leverage is the quiet amplifier the bull case ignores. Broadcom's acquisition model "
             "was built on cheap debt and acquired cash flows; with rates structurally higher and the "
             "VMware deal already digested, the next leg of the playbook \u2014 another transformational "
             "deal \u2014 is harder to finance and harder to find. What remains is an operating company "
             "that must grow organically in cyclical end markets, a much less forgiving setup than the "
             "serial-acquirer narrative the multiple still reflects."),
            ("p", "Our probability-weighted fair value is $240.00, 32% below the current price. Broadcom's "
             "management and franchise quality keep us at REDUCE rather than SELL \u2014 this is a "
             "business we would be enthusiastic owners of at the right price. $355.14 is not the right "
             "price."),
        ]),
        ("Business Overview", [
            ("p", "Broadcom operates two segments. Semiconductor Solutions designs chips for networking "
             "(Ethernet switching and routing, optical interconnects), broadband, storage, and wireless, "
             "plus custom AI accelerators co-developed with large hyperscale customers. Infrastructure "
             "Software, transformed by the VMware acquisition, sells virtualization, cloud-management, "
             "and mainframe software to enterprises on subscription and license terms."),
            ("p", "The business model is acquisition-led: Broadcom buys mature franchises with strong "
             "market positions, consolidates operations aggressively, and harvests the cash flows. The "
             "company carries significant debt from this strategy, serviced by the very cash flows the "
             "acquisitions generate \u2014 a structure that works brilliantly until organic growth "
             "falters."),
        ]),
        ("Forward Outlook", [
            ("p", "We should also note the geopolitical dimension. Export controls on advanced "
             "semiconductors have already shrunk the addressable market for high-end networking and "
             "compute silicon in China, and the ratchet only moves in one direction. Broadcom's China "
             "exposure is manageable today, but each successive restriction removes a slice of the "
             "growth the current multiple assumes, while domestic Chinese competitors fill the vacuum "
             "behind protective policy."),
            ("p", "Our judgment is that AI networking demand remains strong through the current cluster "
             "buildout, but the slope of growth from here is flatter and lumpier than consensus assumes. "
             "Hyperscaler capex is already at historic highs as a share of revenue; the next phase of AI "
             "investment will be gated by power availability, not chip supply, and power constraints "
             "slow deployments in ways that hit component suppliers first. Customer concentration is "
             "extreme \u2014 a handful of hyperscalers drive the AI revenue \u2014 so any single "
             "customer's pause becomes Broadcom's air pocket."),
            ("p", "On custom silicon, we are structurally cautious about valuing customer-owned programs "
             "as if they were Broadcom-owned annuities. These engagements are lumpy, competitively "
             "re-bid, and subject to the customer's make-vs-buy calculus shifting with each generation. "
             "The economics are attractive while they last; the duration is the question the price "
             "ignores."),
            ("p", "VMware will continue to generate prodigious cash in the near term as contracts renew at "
             "higher prices. But we expect the renewal data over the next two years to show rising "
             "attrition at the margin and longer sales cycles, as CIOs who accepted the first price "
             "increase shop alternatives before the second. The market currently models the VMware "
             "annuity as perpetual; we model it as decaying, and the difference is most of our "
             "valuation gap."),
        ]),
        ("Valuation", [
            ("p", "We value Broadcom on a 10-year scenario DCF at a 10% base discount rate. Our bear case "
             "assumes an AI capex digestion in which networking orders fall sharply for 18\u201324 months, "
             "a major custom-silicon program is delayed or lost, and VMware attrition accelerates as "
             "customers migrate off the platform \u2014 with leverage amplifying the equity downside. "
             "The base case assumes AI networking grows through the cycle with one moderate digestion "
             "period, custom silicon contributes lumpy but positive growth, and VMware renewals hold with "
             "gradual price normalization. The bull case assumes the AI buildout extends without "
             "interruption, Ethernet takes dominant share of AI fabrics, and VMware pricing power proves "
             "fully durable."),
            ("p", "Probability-weighting the scenarios 25% / 50% / 25% produces a fair value of $240.00, "
             "our target. The valuation is highly sensitive to the timing of the semiconductor cycle \u2014 "
             "precisely the variable the current price assumes away."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Semiconductor cyclicality: an AI capex digestion would hit orders and multiples simultaneously.",
                "Hyperscaler concentration: a pause or cancellation by one or two large customers is material.",
                "Custom-silicon programs are customer-owned; they can be re-bid, delayed, or insourced.",
                "VMware customer attrition accelerating under aggressive pricing.",
                "Leverage: debt taken on for acquisitions amplifies downside if cash flows falter.",
                "US\u2013China technology restrictions affecting the addressable market for networking chips.",
                "Debt refinancing risk if credit conditions tighten while organic growth slows.",
                "Key-person and integration risk as the acquisition cadence that defined the culture slows.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Evidence that AI networking demand is genuinely non-cyclical: multi-year take-or-pay contracts replacing spot orders.",
                "VMware renewal rates holding above 95% through two full price-increase cycles.",
                "Deleveraging to below 2x net debt/EBITDA, reducing the fragility of the capital structure.",
                "A 25%+ share-price decline with AI order books still intact.",
                "Net leverage falling below 2x net debt/EBITDA combined with two consecutive years of double-digit organic growth \u2014 proof the model works without the next deal.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", meth(10, "10%")),
        ]),
    ],
)

# ---------------------------------------------------------------- MELI
meli = dict(
    ticker="MELI", company="MercadoLibre, Inc.", verdict="REDUCE",
    target="$1,119.00", price="$1,696.56", upside="-34%",
    sections=[
        ("Investment Thesis", [
            ("p", "Let us be explicit about what this call is and is not. The business thesis on "
             "MercadoLibre is intact: the company is the dominant e-commerce platform in Latin America, "
             "its Mercado Pago fintech ecosystem is one of the finest financial-inclusion stories in "
             "emerging markets, and its logistics network constitutes a deepening moat. Management "
             "execution has been excellent across cycles. Nothing in this report disputes any of that."),
            ("p", "This is a cost-of-capital call, not a business call. MercadoLibre's cash flows are "
             "generated in Argentina, Brazil, Mexico, and other Latin American economies \u2014 economies "
             "with histories of currency devaluation, inflation spikes, capital controls, and political "
             "upheaval. A valuation that discounts those cash flows at something close to a US "
             "risk-free-plus-equity-premium rate is simply mispriced risk. We add an explicit 200 basis "
             "point country-risk premium to the discount rate, and we benchmark multiples against "
             "regional peers facing similar risks, not against US e-commerce and fintech names."),
            ("p", "At $1,696.56, the market is valuing MercadoLibre as though Latin American risk had "
             "been repealed \u2014 as though the Argentine peso, Brazilian real, and Mexican policy "
             "environment were Connecticut. They are not. When the appropriate discount rate is applied "
             "to this genuinely excellent business, fair value is $1,119.00, 34% below the current "
             "price. The repricing we expect is the market rediscovering the country-risk premium, "
             "not the business deteriorating."),
            ("p", "We rate the shares REDUCE rather than SELL because the franchise quality is real and "
             "an investor with a very long horizon and high risk tolerance may reasonably choose to "
             "hold through the repricing. But fresh capital at this price is paying US-multiple prices "
             "for EM-risk cash flows, and that arithmetic does not work."),
        ]),
        ("Business Overview", [
            ("p", "MercadoLibre operates Latin America's largest e-commerce marketplace, with leading "
             "positions in Brazil, Argentina, and Mexico, supported by Mercado Envios, its proprietary "
             "logistics network. Mercado Pago began as the marketplace's payments arm and has grown into "
             "a full fintech ecosystem: digital wallets, QR payments, credit cards, consumer and "
             "merchant credit, and asset management products, serving tens of millions of users, many "
             "of whom had no prior access to formal financial services."),
            ("p", "The strategic logic is powerful: commerce generates payments volume, payments data "
             "underwrites credit, and credit deepens both commerce and payments engagement. Few "
             "companies globally have executed this flywheel as effectively in as difficult an "
             "operating environment."),
        ]),
        ("Forward Outlook", [
            ("p", "Operationally, we expect continued strong execution. E-commerce penetration in Latin "
             "America remains well below US and Chinese levels, leaving a long runway for share gains as "
             "logistics improve. Mercado Pago's credit portfolio is the highest-growth and highest-risk "
             "engine: underwriting millions of thin-file borrowers with proprietary data is a genuine "
             "competitive advantage, but credit is where emerging-market downturns bite first and "
             "hardest, and loss rates will spike in the next regional slowdown."),
            ("p", "Argentina deserves special attention. Economic stabilization under reformist policy "
             "could surprise positively and would be a meaningful tailwind; a return to populist "
             "intervention, capital controls, or peso collapse would impair a significant earnings "
             "stream. Our base case assumes neither miracle nor disaster \u2014 merely the historical "
             "base rate of Argentine volatility, which is itself a cost."),
            ("p", "Competition is intensifying: global platforms and well-funded regional challengers are "
             "contesting both commerce and fintech in Brazil and Mexico. MercadoLibre's scale and "
             "ecosystem integration are formidable defenses, but defense is not free \u2014 promotional "
             "intensity and logistics investment will weigh on incremental margins even as the "
             "franchise strengthens. The business will almost certainly be larger and more profitable "
             "in five years. Our target reflects what those cash flows are worth to a "
             "dollar-based investor who must be compensated for Latin American risk."),
        ]),
        ("Valuation", [
            ("p", "We value MercadoLibre on a 10-year scenario DCF. The critical input is the discount "
             "rate: we add an explicit 200bp country-risk premium to our standard base rate, reflecting "
             "currency, inflation, and regulatory risk across the company's Latin American footprint. "
             "This single adjustment \u2014 not any change in our view of the business \u2014 drives the "
             "majority of the gap between our fair value and the current price."),
            ("p", "Our bear case models a regional downturn combining Brazilian recession, Argentine "
             "policy reversal, and a spike in Mercado Pago credit losses, with sustained currency "
             "depreciation impairing dollar-reported earnings. The base case assumes continued "
             "operational excellence \u2014 commerce share gains, fintech scaling, gradual margin "
             "expansion \u2014 discounted at the country-risk-adjusted rate. The bull case assumes "
             "Argentine stabilization, benign credit performance, and successful defense of market "
             "share against global competitors."),
            ("p", "Probability-weighting the scenarios 25% / 50% / 25% produces a fair value of "
             "$1,119.00, our target. An investor who believes Latin American country risk should "
             "command no premium will find our target too low; we consider that belief the central "
             "mispricing in the shares today."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Currency devaluation across the real, peso, and other regional currencies directly reduces dollar-reported earnings.",
                "Argentine political and policy risk: capital controls or interventionist policy would impair a major earnings stream.",
                "Mercado Pago credit losses spiking in a regional downturn; thin-file lending has limited through-cycle history.",
                "Intensifying competition in Brazilian and Mexican e-commerce and fintech from global and regional players.",
                "Regulatory risk: fintech licensing, interest-rate caps, or payments regulation in key markets.",
                "Country-risk repricing: if the market continues to ignore EM risk, the shares can stay expensive longer than fundamentals justify.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Structural, durable Argentine macroeconomic stabilization that justifies narrowing the country-risk premium.",
                "Mercado Pago credit demonstrating through-cycle loss rates comparable to developed-market underwriting.",
                "Sustained local-currency growth with stable or strengthening FX \u2014 evidence the risk premium is excessive.",
                "The shares repricing to our target without business deterioration, restoring a fair risk-adjusted expected return.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", meth(10, "10% plus a 200bp country-risk premium", MELI_EXTRA)),
        ]),
    ],
)

# ---------------------------------------------------------------- RTX
rtx = dict(
    ticker="RTX", company="RTX Corporation", verdict="SELL",
    target="$120.00", price="$184.68", upside="-35%",
    sections=[
        ("Investment Thesis", [
            ("p", "RTX is priced as a clean aerospace compounder. It is not one \u2014 not yet. The "
             "company's three segments each carry a real business: Pratt & Whitney's geared turbofan "
             "(GTF) engine franchise, Collins Aerospace's avionics and interiors portfolio, and "
             "Raytheon's defense backlog. But the GTF powder-metal contamination issue has created a "
             "multi-year overhang of grounded aircraft, customer compensation, and cash costs that the "
             "current price treats as a footnote. It is the story."),
            ("p", "Consider what the GTF problem actually entails: hundreds of aircraft requiring "
             "accelerated engine inspections and shop visits, airlines demanding compensation for "
             "grounded fleets, and Pratt absorbing costs that flow directly against free cash flow for "
             "years. Management has laid out a resolution timeline extending well into the decade, and "
             "every quarter of delay compounds the liability. Aerospace investors have seen this film "
             "before \u2014 fleet issues are never resolved as fast or as cheaply as the initial "
             "guidance suggests."),
            ("p", "Meanwhile the defense leg, Raytheon, offers backlog but not margin comfort. Defense "
             "contracting is a cost-plus and fixed-price mix where program execution risk sits with the "
             "contractor; recent industry history is littered with charges on fixed-price development "
             "programs. Collins is the cleanest asset in the portfolio, but it cannot carry the "
             "valuation alone."),
            ("p", "There is also a subtler risk the price ignores: the reputational dimension with airline "
             "customers. Fleet groundings strain the most valuable relationships in commercial "
             "aerospace \u2014 the airlines whose future engine orders determine Pratt's installed base "
             "for decades. Competitors are actively courting frustrated GTF operators with alternative "
             "engine options on future airframes. Every quarter of disruption is a quarter in which the "
             "next decade's market share is being negotiated, and RTX is negotiating from weakness."),
            ("p", "At $184.68, the market is capitalizing a fully recovered, issue-free RTX. Our "
             "probability-weighted fair value is $120.00 \u2014 35% lower \u2014 reflecting the GTF cash "
             "drain, defense execution risk, and a discount rate appropriate for a business whose "
             "signature program is in remediation. Until the overhang clears, the shares are a sale. "
             "SELL."),
        ]),
        ("Business Overview", [
            ("p", "RTX Corporation, formed by the merger of Raytheon and United Technologies, operates "
             "three segments. Pratt & Whitney designs and manufactures aircraft engines, including the "
             "GTF engine family powering the Airbus A320neo. Collins Aerospace supplies avionics, "
             "interiors, and mission systems. Raytheon is one of the largest US defense contractors, "
             "producing missiles, air-defense systems including Patriot, and intelligence and space "
             "systems."),
            ("p", "The commercial aerospace businesses earn their best margins in the aftermarket \u2014 "
             "spare parts and maintenance on installed engines and systems \u2014 which makes fleet "
             "health central to profitability. The defense business earns steadier but lower margins on "
             "long government contracts."),
        ]),
        ("Forward Outlook", [
            ("p", "On defense, we are watchful rather than bearish on demand but cautious on "
             "profitability. The industry-wide shift toward fixed-price development contracts has "
             "transferred risk from governments to contractors, and recent years have produced "
             "multi-billion-dollar charges across the peer group. Raytheon's backlog is only as "
             "valuable as its execution; our base case assumes no major charges, but the base rate for "
             "large defense development programs counsels humility."),
            ("p", "Our judgment is that the GTF remediation dominates the investment horizon. The "
             "physics of the problem \u2014 inspecting and reworking a large installed fleet while "
             "maintaining new-engine deliveries \u2014 dictates a multi-year timeline regardless of "
             "management's determination. We expect compensation costs and working-capital absorption to "
             "depress free cash flow through at least 2028, with meaningful risk that the tail extends "
             "further if inspection findings broaden."),
            ("p", "The longer-term commercial outlook is genuinely attractive: global narrowbody fleets "
             "will fly for decades, and Pratt's installed base guarantees aftermarket annuities once "
             "the fleet is healthy. Defense demand is structurally supported by elevated geopolitical "
             "tension and replenishment needs. But both of these are 2030 stories being priced as 2026 "
             "stories."),
            ("p", "The critical question for the next two years is whether additional charges emerge \u2014 "
             "from expanded inspection scope, from fixed-price defense programs, or from customer "
             "settlements above reserved amounts. Our base case assumes the reserved amounts prove "
             "roughly adequate; our bear case, which we weight seriously, assumes they do not. Either "
             "way, the path to the market's implied valuation requires a spotless execution record from "
             "a company currently managing its largest operational crisis."),
        ]),
        ("Valuation", [
            ("p", "We value RTX on a 10-year scenario DCF at a 10% base discount rate. Our bear case "
             "assumes the GTF inspection scope widens, compensation and remediation costs exceed "
             "reserves materially, and a fixed-price defense program takes a significant charge \u2014 "
             "with free cash flow depressed for four or more years. The base case assumes remediation "
             "costs land near reserved amounts, the fleet returns to normal shop-visit cadence by the "
             "end of the decade, and defense executes without major charges. The bull case assumes "
             "faster-than-guided fleet recovery, no incremental charges, and defense margins expanding "
             "on favorable contract mix."),
            ("p", "Probability-weighting the scenarios 25% / 50% / 25% produces a fair value of $120.00, "
             "our target. The bear case sits far below the current price \u2014 appropriate for a "
             "business whose central program risk is both large and still being quantified."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "GTF remediation scope widening beyond current reserves, extending the cash drain.",
                "Airline customer compensation exceeding reserved amounts or triggering litigation.",
                "Fixed-price defense development programs generating charges on cost overruns.",
                "Commercial aerospace downturn reducing aftermarket flight hours and spare-parts demand.",
                "US defense budget pressure or program cancellations affecting Raytheon's backlog.",
                "Execution risk on the multi-year operational recovery across three segments.",
                "Market-share loss on future narrowbody engine competitions as airlines penalize GTF disruption.",
                "Pension and legacy-liability volatility affecting reported earnings.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "GTF fleet shop-visit backlog clearing ahead of schedule with costs tracking below reserves for four consecutive quarters.",
                "Pratt & Whitney free cash flow inflecting positively with the remediation substantially complete.",
                "A major fixed-price defense program completing development without charges, de-risking the contracting model.",
                "The shares declining toward our target while remediation milestones are demonstrably met.",
                "Pratt winning a major new airframe engine competition \u2014 evidence customer relationships survived the GTF episode intact.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", meth(10, "10%")),
        ]),
    ],
)

# ---------------------------------------------------------------- APH
aph = dict(
    ticker="APH", company="Amphenol Corporation", verdict="REDUCE",
    target="$55.53", price="$86.96", upside="-36%",
    sections=[
        ("Investment Thesis", [
            ("p", "Amphenol is one of the best-run industrial companies in the world. Its decentralized "
             "operating model, relentless cost discipline, and program of disciplined tuck-in "
             "acquisitions have compounded shareholder value for decades. The company's interconnect "
             "products are genuinely enabling the AI data-center buildout \u2014 high-speed connectors, "
             "cable assemblies, and sensors that carry the signals inside every AI cluster. We admire "
             "the business without reservation."),
            ("p", "We do not admire the price. At $86.96, the shares trade at a multiple that assumes "
             "the AI interconnect boom runs indefinitely at peak margins. Connectors are a cyclical "
             "business: Amphenol's own history shows clear cycles in which orders surge, capacity is "
             "added, and then digestion follows. The current order strength in data-center interconnects "
             "is real, but it is also precisely what cyclical peaks look like \u2014 customers "
             "double-ordering against long lead times, distributors building inventory, and every "
             "participant extrapolating the present."),
            ("p", "Outside the AI bright spot, the picture is less euphoric. Automotive and industrial "
             "end markets \u2014 historically the ballast of Amphenol's diversification \u2014 have been "
             "soft, and a recovery there is assumed rather than visible. The Carlisle Interconnect "
             "Technologies acquisition adds scale in harsh-environment interconnects but also adds "
             "integration risk and was priced at a full multiple."),
            ("p", "The multiple deserves one more look. Amphenol has historically traded at a premium to "
             "industrial peers \u2014 deservedly \u2014 but the current premium prices the company alongside "
             "secular-growth technology franchises rather than cyclical component manufacturers. "
             "Premiums expand late in cycles as growth investors discover quality cyclicals; they "
             "compress violently at the first sign of order deceleration. We are not predicting the "
             "timing of that compression, only noting that the compensation for bearing it has vanished."),
            ("p", "Our probability-weighted fair value is $55.53, 36% below the current price. This is a "
             "valuation call on a wonderful company: we rate the shares REDUCE because the expected "
             "return from here is firmly negative, while acknowledging that Amphenol's quality means the "
             "shares deserve a premium multiple \u2014 just not this one."),
        ]),
        ("Business Overview", [
            ("p", "Amphenol designs and manufactures electrical, electronic, and fiber-optic connectors, "
             "cable assemblies, and sensors sold into a diversified set of end markets: information "
             "technology and data communications, automotive, industrial, mobile devices, military, and "
             "commercial aerospace. No single customer or market dominates, which has historically "
             "smoothed cycles."),
            ("p", "Growth comes from two engines: organic design wins, where Amphenol's engineering "
             "proximity to customers wins interconnect content on new platforms, and acquisitions, where "
             "the company buys smaller connector manufacturers and applies its operating playbook. The "
             "model has produced decades of margin expansion and high returns on capital."),
            ("p", "The end-market mix is worth understanding because it determines how the cycle hits. "
             "Information technology and data communications \u2014 the AI-exposed leg \u2014 now drives "
             "the growth narrative, but automotive, industrial, and mobile devices still represent the "
             "bulk of unit volume and provide diversification when any single market pauses. Military "
             "and commercial aerospace contribute smaller, steadier streams with long qualification "
             "cycles that lock in share. This diversification is Amphenol's shock absorber; the question "
             "for valuation is how much of the current earnings power belongs to the absorber and how "
             "much belongs to the cyclical surge."),
        ]),
        ("Forward Outlook", [
            ("p", "M&A remains a genuine long-term value driver \u2014 Amphenol's acquisition track record "
             "is among the best in industrials \u2014 but deal math is less forgiving at today's multiples. "
             "The Carlisle Interconnect Technologies acquisition was strategically sound and priced for "
             "perfection; integrating a large deal while the cycle turns is the classic test of serial "
             "acquirers, and we will be watching organic growth excluding acquisitions as the cleanest "
             "signal of underlying demand."),
            ("p", "Our judgment is that AI data-center interconnect demand remains robust through the "
             "current build cycle, and Amphenol's content per rack continues to rise as speeds increase. "
             "But we expect the torrid growth rates of the last two years to moderate as hyperscaler "
             "capex growth decelerates and the initial cluster buildout passes its steepest phase. "
             "History suggests the digestion, when it comes, will be sharper than consensus models: "
             "lead times collapse, double orders cancel, and distributor inventory destocks all at once."),
            ("p", "The margin question is equally important. Current profitability benefits from a rich "
             "mix \u2014 high-speed data-center products at premium margins. As that mix normalizes, or "
             "as competitors add high-speed capacity and pricing pressure follows, margins should drift "
             "back toward historical norms. The market is capitalizing peak-mix margins as permanent; we "
             "apply terminal value to normalized mid-cycle margins, and the difference is substantial."),
            ("p", "Longer term, Amphenol remains a premier compounder that will continue to take share "
             "and make smart acquisitions. Our target implies a still-healthy multiple of normalized "
             "earnings \u2014 a recognition of quality. It simply does not imply the 40-times-plus "
             "multiple the market currently pays for cyclical peak earnings."),
        ]),
        ("Valuation", [
            ("p", "We value Amphenol on a 10-year scenario DCF at a 10% base discount rate, with terminal "
             "value on normalized mid-cycle margins rather than today's AI-enriched mix. Our bear case "
             "assumes a sharp interconnect digestion \u2014 order cancellations, distributor destocking, "
             "and margin reversion toward historical averages \u2014 coinciding with continued softness "
             "in automotive and industrial markets. The base case assumes data-center growth moderates "
             "to a sustainable pace, industrial markets recover gradually, and margins settle modestly "
             "above historical norms reflecting permanent mix improvement. The bull case assumes AI "
             "infrastructure spending sustains elevated growth for the full horizon with pricing power "
             "intact."),
            ("p", "Probability-weighting the scenarios 25% / 50% / 25% produces a fair value of $55.53, "
             "our target. The bear case sits well below the current price, reflecting how much of "
             "today's valuation depends on peak-cycle conditions persisting."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "AI interconnect digestion: a sharp order slowdown as hyperscaler capex decelerates.",
                "Margin reversion as high-speed product mix normalizes and competition intensifies.",
                "Continued softness in automotive and industrial end markets.",
                "Acquisition integration risk, including the large Carlisle Interconnect Technologies deal.",
                "Customer concentration in data-center interconnects rising as AI becomes a larger mix.",
                "Trade and tariff exposure across a global manufacturing footprint.",
                "Multiple compression as growth investors rotate out of a cyclical compounder at the first order deceleration.",
                "Raw-material cost inflation (copper, precious metals) pressuring connector margins.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Data-center interconnect orders demonstrating genuinely non-cyclical characteristics through a hyperscaler capex pause.",
                "Industrial and automotive markets inflecting to growth, restoring the diversified growth algorithm.",
                "Margins holding at current levels for two full years, evidencing permanent mix improvement.",
                "The shares declining toward our target with the operating business performing to plan.",
                "Amphenol sustaining double-digit organic growth through a full interconnect downcycle \u2014 evidence the AI content story is structural rather than cyclical.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", meth(10, "10%")),
        ]),
    ],
)

# ---------------------------------------------------------------- GRBK
grbk = dict(
    ticker="GRBK", company="Green Brick Partners, Inc.", verdict="SELL",
    target="$41.00", price="$66.66", upside="-39%",
    sections=[
        ("Investment Thesis", [
            ("p", "Green Brick Partners is a well-managed Sunbelt homebuilder being valued as though the "
             "housing cycle had been abolished. The company has grown impressively, concentrated in "
             "Texas and other high-growth Sunbelt markets, with a land-light option model in several "
             "divisions and a deserved reputation for operational execution. But homebuilding is among "
             "the most cyclical industries in the economy, and Green Brick's current earnings reflect "
             "cyclical peak conditions: constrained resale supply, elevated prices, and margins fattened "
             "by years of underbuilding."),
            ("p", "Those conditions are normalizing. Affordability sits near historic lows \u2014 the "
             "combination of elevated home prices and mortgage rates has pushed the monthly payment on "
             "a median new home beyond the reach of the median household in Green Brick's core markets. "
             "Builders are responding the way they always do: incentives, rate buydowns, and price "
             "reductions that compress margins from both ends. Order rates are softening, cancellation "
             "rates are rising, and spec inventory is building."),
            ("p", "The valuation math is unforgiving for cyclical peaks. At $66.66, the market pays a "
             "full multiple of earnings that are themselves at a cyclical high \u2014 the classic "
             "late-cycle trap of a low P/E on peak E. On a through-cycle basis, normalizing margins to "
             "mid-cycle levels and applying a discount rate appropriate for a leveraged cyclical "
             "(12%), the shares are worth $41.00, 39% below the current price. Homebuilders do not "
             "decline gracefully from peaks; earnings have further to fall than the price implies."),
            ("p", "Investors sometimes argue that Green Brick's premium land positions and Texas footprint "
             "justify a premium multiple through the cycle. We agree the footprint is superior \u2014 which "
             "is exactly why the shares should be bought after the downturn impairs lesser builders, not "
             "before. Quality homebuilders outperform by surviving downturns with balance sheets intact "
             "and buying distressed land from failures; paying peak prices for that quality inverts the "
             "entire logic of cyclical investing."),
            ("p", "We rate the shares SELL. The business is good; the cycle is not. Investors are being "
             "paid nothing for the downside of owning a cyclical at the top, and the downside in "
             "homebuilding downturns is measured not in multiple compression but in land impairments "
             "and earnings collapses. SELL."),
        ]),
        ("Business Overview", [
            ("p", "Green Brick Partners is a residential homebuilder focused on high-growth Sunbelt "
             "markets, principally the Dallas\u2013Fort Worth metroplex along with other Texas markets, "
             "Atlanta, and select Southeast markets. The company builds single-family homes across "
             "move-up and luxury price points, operating through subsidiary builders, and controls land "
             "through a mix of ownership and option contracts."),
            ("p", "The investment case for Green Brick has rested on superior market selection \u2014 "
             "building where population and job growth are strongest \u2014 and disciplined land "
             "underwriting. These are real advantages. They are also advantages that matter most in "
             "downturns, when land bought at peak prices across the industry must be written down; "
             "discipline is tested by the cycle, not exempt from it."),
        ]),
        ("Forward Outlook", [
            ("p", "The rental and build-to-rent channel warrants mention as a partial offset: "
             "institutional demand for single-family rentals has absorbed some new supply and could "
             "cushion order declines. But institutional buyers are the most price-sensitive marginal "
             "buyers in the market \u2014 they underwrite to cap rates, and higher rates have already "
             "thinned their bids. We model modest support from this channel, not salvation."),
            ("p", "Our judgment is that Green Brick is entering the difficult phase of the housing cycle. "
             "We expect net orders to decelerate through 2027 as affordability constraints bite, with "
             "the company increasingly reliant on incentives \u2014 mortgage rate buydowns, closing-cost "
             "credits, and outright price cuts \u2014 to maintain absorption pace. Each of these "
             "compresses gross margins, which we expect to retreat several hundred basis points from "
             "peak levels toward historical mid-cycle norms."),
            ("p", "The land book is the swing factor. Lots contracted or purchased at 2024\u20132025 "
             "prices embed peak land economics; if home prices soften even modestly, option deposits "
             "are abandoned and owned land faces impairment. Green Brick's underwriting has been "
             "better than most, but no underwriting survives a demand shock unscathed, and the "
             "balance sheet will absorb the cycle's costs before shareholders see the benefits of the "
             "next upturn."),
            ("p", "Longer term, the Sunbelt demographic thesis remains intact \u2014 people and jobs "
             "continue migrating to Green Brick's markets, which supports a strong recovery when "
             "affordability normalizes. But housing cycles run in years, not quarters, and the current "
             "price offers no compensation for waiting through the down leg. Our $41.00 target "
             "approximates through-cycle value; the path there is likely to be volatile."),
        ]),
        ("Valuation", [
            ("p", "We value Green Brick on a 10-year scenario DCF at a 12% base discount rate, "
             "appropriate for a leveraged cyclical business, with terminal value on normalized "
             "mid-cycle homebuilding margins \u2014 not today's elevated margins. Our bear case assumes "
             "a genuine housing downturn: orders fall sharply, margins compress toward trough levels, "
             "and land impairments destroy book value. The base case assumes a moderate correction \u2014 "
             "margins normalizing over three years, impairments limited to option walk-aways, and a "
             "recovery beginning late in the decade. The bull case assumes the soft landing: "
             "affordability improves via rate declines, demand holds, and margins stay above historical "
             "norms."),
            ("p", "Probability-weighting the scenarios 25% / 50% / 25% produces a fair value of $41.00, "
             "our target. The bear case sits far below the current price \u2014 the nature of "
             "late-cycle homebuilding, where peak earnings mask the leverage to a downturn."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Housing demand shock: further rate increases or recession would collapse order rates.",
                "Margin compression from incentives, buydowns, and price cuts as builders compete for scarce buyers.",
                "Land impairments if home prices soften on lots contracted at peak prices.",
                "Sunbelt supply response: competing builders adding inventory in Green Brick's core markets.",
                "Cancellation rates spiking, stranding spec inventory.",
                "Concentration in Texas markets amplifies exposure to regional economic shocks.",
                "Texas energy-sector downturn compounding a housing correction in Green Brick's core markets.",
                "Rising property taxes and insurance costs in Sunbelt markets further eroding affordability.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "A sustained decline in mortgage rates restoring affordability without a recession.",
                "Net orders reaccelerating for two consecutive quarters with stable or rising margins and no incremental incentives.",
                "Demonstrable land impairments already taken and reserved, clearing the balance-sheet overhang.",
                "The shares trading at or below tangible book value, pricing in the downturn we expect.",
                "Green Brick acquiring distressed land or a distressed competitor at trough prices \u2014 the classic quality-builder move that would signal the cycle has bottomed.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", meth(10, "12%")),
        ]),
    ],
)

# ---------------------------------------------------------------- COIN
coin = dict(
    ticker="COIN", company="Coinbase Global, Inc.", verdict="SELL",
    target="$100.00", price="$183.00", upside="-45%",
    sections=[
        ("Investment Thesis", [
            ("p", "Coinbase is the premier onshore crypto exchange: the most trusted brand in the "
             "industry, the custodian of choice for the spot bitcoin ETFs, and a genuine beneficiary "
             "of improving US regulatory clarity. These are real strategic assets, and in a bull-market "
             "for digital assets the company's operating leverage is spectacular \u2014 incremental "
             "trading volume drops almost entirely to the bottom line."),
            ("p", "The problem is that the operating leverage works in both directions, and crypto "
             "trading volume is among the most cyclical revenue streams in financial markets. Retail "
             "participation \u2014 the source of Coinbase's highest-margin take rates \u2014 surges "
             "during speculative manias and evaporates in drawdowns; history shows 50%+ volume "
             "contractions are routine, not tail events. At $183.00, the market is capitalizing "
             "elevated-cycle trading revenue as though the mania phase were the permanent run rate."),
            ("p", "The structural pressures compound the cyclicality. Zero-commission crypto trading at "
             "traditional brokerages is compressing retail take rates across the industry; "
             "sophisticated volume increasingly migrates to venues competing on fractions of a basis "
             "point. Coinbase's subscription and services revenue \u2014 staking, custody, USDC interest, "
             "and Base sequencer fees \u2014 is growing and diversifying, but it remains a minority of "
             "the total and is itself partly crypto-price-linked."),
            ("p", "One more consideration: Coinbase's valuation embeds an assumption that crypto's "
             "institutionalization accrues primarily to Coinbase. But institutionalization commoditizes "
             "access \u2014 ETFs, bank prime brokerage, and tokenized traditional assets all route around "
             "the retail exchange model. The more legitimate crypto becomes, the more competition "
             "Coinbase faces from institutions with lower cost structures and deeper distribution. "
             "Success of the asset class and success of this equity are diverging, and the price assumes "
             "they are the same trade."),
            ("p", "Our probability-weighted fair value is $100.00, 45% below the current price \u2014 the "
             "widest downside in our coverage, reflecting the violence of crypto revenue cycles. "
             "Regulatory clarity is a genuine long-term positive, but it is already in the price several "
             "times over. Until the shares reflect mid-cycle rather than peak-cycle earnings power, "
             "they are a sale. SELL."),
        ]),
        ("Business Overview", [
            ("p", "Coinbase operates the largest US cryptocurrency exchange, serving retail traders "
             "through its consumer platform and institutions through Coinbase Prime, custody, and "
             "financing services. Transaction revenue \u2014 spreads and fees on trading \u2014 has "
             "historically driven the majority of revenue and virtually all of the earnings "
             "volatility. Subscription and services revenue includes staking rewards, custodial fees, "
             "interest on USDC reserves, and fees from the Base layer-2 network."),
            ("p", "The company's moat rests on regulatory compliance, brand trust earned by surviving "
             "multiple crypto winters without solvency questions, and its entrenched position in "
             "institutional custody infrastructure. These advantages are durable; they do not make "
             "revenue less cyclical."),
        ]),
        ("Forward Outlook", [
            ("p", "Base, the layer-2 network, is the most interesting long-term option in the portfolio: "
             "sequencer fees scale with onchain activity and carry software-like margins. We model it "
             "growing into a meaningful contributor by the end of the decade. But it is still small "
             "relative to transaction revenue, its economics depend on sustained onchain activity that "
             "has historically been as cyclical as trading, and monetization could attract exactly the "
             "regulatory scrutiny the industry is trying to escape."),
            ("p", "Our judgment is that crypto trading volumes are closer to a cyclical peak than a "
             "permanent plateau. The speculative fervor that drove record volumes is already cooling, "
             "and the pattern of prior cycles \u2014 euphoria, drawdown, dormancy \u2014 argues that the "
             "next 18 months bring materially lower retail participation. When volumes fall, they fall "
             "fast: Coinbase's cost base is largely fixed in the short term, so revenue declines "
             "translate almost one-for-one into earnings declines."),
            ("p", "Regulatory clarity in the US is the most constructive long-term development in the "
             "company's history, and we expect it to expand the addressable market over five years \u2014 "
             "more institutions, more products, more onchain activity on Base. But clarity also invites "
             "competition: every major brokerage and bank can now credibly offer crypto services, and "
             "their distribution advantages will pressure Coinbase's retail take rates structurally, "
             "not just cyclically."),
            ("p", "The subscription and services businesses deserve credit for compounding through "
             "cycles, and we model them growing steadily. They are not, however, large or stable "
             "enough to offset a halving of transaction revenue \u2014 which is what prior crypto "
             "winters delivered. Our valuation assumes mid-cycle volumes, and mid-cycle Coinbase earns "
             "far less than peak-cycle Coinbase. The market has not made that adjustment."),
        ]),
        ("Valuation", [
            ("p", "We value Coinbase on a 10-year scenario DCF at a 12% base discount rate, reflecting "
             "the speculative, highly cyclical nature of crypto-linked revenues, with terminal value on "
             "normalized mid-cycle margins \u2014 not the peak margins of a volume mania. Our bear case "
             "assumes a full crypto winter: trading volumes fall more than 50%, retail take rates "
             "compress under brokerage competition, and the company burns through the earnings cushion "
             "built during the boom. The base case assumes mid-cycle volumes with gradual growth in "
             "subscription and services providing a stabilizing floor. The bull case assumes sustained "
             "elevated crypto adoption, successful monetization of Base, and take-rate stability."),
            ("p", "Probability-weighting the scenarios 25% / 50% / 25% produces a fair value of $100.00, "
             "our target. The bear case sits dramatically below the current price \u2014 the honest "
             "reflection of a business whose revenue can halve in a year."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Crypto winter: a 50%+ contraction in trading volumes would collapse transaction revenue and earnings.",
                "Take-rate compression as zero-commission brokerages and banks compete for retail crypto flow.",
                "Crypto asset price declines directly reducing custody, staking, and USDC-reserve economics.",
                "Regulatory reversal or adverse rulemaking despite the current constructive direction.",
                "Security events: a major hack or outage would damage the trust-based moat.",
                "Concentration of profitability in the most cyclical revenue stream in financial services.",
                "Competition from banks and brokerages offering crypto custody and trading to their existing customer bases.",
                "Stablecoin regulation compressing USDC reserve economics, a key services-revenue contributor.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Subscription and services revenue exceeding 60% of total revenue for a full year, proving the business has genuinely diversified past volume cyclicality.",
                "Coinbase maintaining retail take rates through a full crypto drawdown, evidencing structural pricing power.",
                "Trading volumes stabilizing at mid-cycle levels with the shares priced accordingly.",
                "The shares declining toward our target while regulatory clarity continues to expand the institutional franchise.",
                "Base sequencer revenue reaching 15%+ of total revenue with stable unit economics \u2014 evidence of a genuine second engine.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", meth(10, "12%")),
        ]),
    ],
)

NOTES = [nflx, amzn, avgo, meli, rtx, aph, grbk, coin]

def all_text(d):
    parts = [d["ticker"], d["company"], d["verdict"], d["target"], d["price"], d["upside"]]
    for heading, blocks in d["sections"]:
        parts.append(heading)
        for kind, payload in blocks:
            if kind == "table":
                headers, rows = payload
                parts.extend(headers)
                for r in rows:
                    parts.extend(r)
            elif kind == "bullets":
                parts.extend(payload)
            else:
                parts.append(payload)
    return "\n".join(parts)

def main():
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pdfs")
    os.makedirs(outdir, exist_ok=True)
    for d in NOTES:
        check_banned(all_text(d), d["ticker"])
    print("banned-phrase check: clean for all 8 notes")
    for d in NOTES:
        path = os.path.join(outdir, "%s-equity-research-note.pdf" % d["ticker"])
        build_note(path, d)
        rdr = PdfReader(path)
        n = len(rdr.pages)
        assert n > 0, "no pages: %s" % d["ticker"]
        txt = "".join((p.extract_text() or "") for p in rdr.pages)
        assert len(txt) > 2000, "text extraction too short: %s" % d["ticker"]
        assert d["ticker"] in txt and d["target"] in txt and d["verdict"] in txt, "key fields missing: %s" % d["ticker"]
        print("%s: %d pages, %d chars extracted -- OK" % (d["ticker"], n, len(txt)))

if __name__ == "__main__":
    main()
