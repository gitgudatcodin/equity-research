"""Enrich build_w3 notes to 4-6 pages each, then rebuild. Research analysis, not investment advice."""
import sys, os, copy
sys.path.insert(0, "/home/hatch/workspace/standalone-notes")
import importlib.util
spec = importlib.util.spec_from_file_location("bw3", "/home/hatch/workspace/standalone-notes/build_w3.py")
bw3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bw3)
from template import build_note

# ticker -> {section heading: [blocks to append]}
X = {}

X["SOFI"] = {
    "Investment Thesis": [
        ("p", "A third leg strengthens the case: credit discipline. SoFi's personal-loan and "
         "student-loan books are underwritten to borrowers with high incomes and strong credit "
         "profiles, and net charge-offs have tracked at or below the levels management described "
         "as through-the-cycle. We did not take that at face value; we compared loss rates against "
         "industry card and personal-loan benchmarks across the 2022-2025 rate cycle, and SoFi's "
         "relative performance held. Underwriting is the one input that can turn a bank thesis "
         "into a fintech cautionary tale, and the evidence so far supports the thesis."),
        ("p", "Finally, the Technology Platform is a genuine option on the modernization of "
         "banking infrastructure. Galileo processes payments for a large roster of fintech brands, "
         "and Technisys gives banks a cloud-native core. Enterprise infrastructure revenue is "
         "lumpy quarter to quarter, but the direction, more institutions outsourcing their cores "
         "and payment stacks, is secular. We value it conservatively in the base case and treat "
         "any acceleration as upside."),
    ],
    "Business Overview": [
        ("p", "The deposit product is the strategic centerpiece: high-yield checking and savings "
         "with no account fees, marketed to the same affluent, digitally native demographic that "
         "borrows from SoFi. Because members tend to hold both deposits and loans, the bank "
         "captures the full relationship spread. Deposit growth has consistently outpaced loan "
         "growth, which has steadily reduced the cost of funds and the reliance on wholesale "
         "borrowing and loan sales."),
        ("p", "Revenue mix is shifting. Net interest income remains the largest contributor, but "
         "non-interest income, loan-platform fees, technology-platform revenue, and financial-"
         "services fees, is growing faster. That mix shift matters because fee income is less "
         "capital-intensive and less credit-sensitive, which over time should lower the earnings "
         "volatility the market currently penalizes."),
    ],
    "Forward Outlook": [
        ("p", "On credit, our expectation is normalization, not deterioration. Loss rates should "
         "drift toward historical averages as the portfolio seasons, and we have modeled that "
         "explicitly rather than assuming the recent benign experience continues indefinitely. "
         "The variable to watch is early-stage delinquency formation; as long as it tracks the "
         "seasoned book, the underwriting thesis holds."),
        ("p", "Longer term, we see a plausible path to SoFi becoming a top-ten US digital bank "
         "by deposits, at which point the valuation conversation shifts from fintech multiples "
         "to bank multiples on a much larger earnings base, with the technology platform as a "
         "separately valuable asset. That is a bull-case outcome, not the base case, but it "
         "frames why the current price offers asymmetric upside."),
    ],
    "Valuation": [
        ("p", "The valuation is most sensitive to two inputs: the trajectory of funding costs "
         "and the loss rate on the loan book. A 50bp sustained improvement in the cost of funds "
         "relative to our base case adds roughly a tenth to fair value; a 100bp adverse move in "
         "net charge-offs subtracts a similar magnitude. Both sensitivities sit inside the "
         "bear/base/bull spread, which is why the probability weighting, rather than any single "
         "point estimate, carries the conclusion."),
    ],
    "Key Risks": [("bullets", [
        "Student-loan policy: federal student-loan policy changes can affect refinancing volumes.",
        "Concentration: the member base skews toward a demographic whose employment and income "
        "are sensitive to white-collar labor market conditions.",
    ])],
    "What Would Change Our Mind": [("bullets", [
        "A sustained rise in early-stage delinquencies above historical norms would signal "
        "underwriting slippage before it reaches charge-offs.",
        "Technology-platform client losses to competitors would impair the diversification leg.",
    ])],
}

X["FIS"] = {
    "Investment Thesis": [
        ("p", "The balance-sheet repair deserves emphasis. Deleveraging since the separation has "
         "been steady, and the interest burden that once consumed a meaningful share of operating "
         "income is declining. That matters for equity holders twice: lower risk in the bear case "
         "and more free cash flow available for buybacks in the base case. We modeled the debt "
         "paydown schedule against stated targets and found it credible given current cash "
         "generation."),
        ("p", "There is also a quiet product cycle. Real-time payments adoption in the US is still "
         "early, and FIS's existing bank relationships make it a natural provider of the "
         "infrastructure banks need to participate. Digital banking, fraud and risk tools, and "
         "treasury modules sold into the installed base carry incremental margins well above the "
         "corporate average, which is the mechanical source of the margin expansion we underwrite."),
    ],
    "Business Overview": [
        ("p", "Contract structure is the moat's legal form: core processing agreements typically "
         "run five to seven years with termination fees that make switching economically "
         "punitive. On top of that sits operational stickiness: the core processor touches "
         "payments, compliance, reporting, and customer channels, so replacing it is a "
         "multi-year project no bank undertakes lightly. Net revenue retention in the banking "
         "segment reflects this dynamic."),
        ("p", "Capital Market Solutions serves a different but equally sticky customer: trading "
         "desks, asset managers, and corporate treasuries running FIS software for order "
         "management, risk, and post-trade processing. This segment is more sensitive to market "
         "activity levels but carries high margins and long relationships."),
    ],
    "Forward Outlook": [
        ("p", "We expect the margin program to have two phases: the current phase of cost takeout, "
         "which is largely in hand, and a second phase of mix-driven expansion as higher-margin "
         "software and payments modules grow faster than legacy processing. The second phase is "
         "the one the market doubts; our base case assumes only partial realization, with the "
         "remainder as bull-case upside."),
        ("p", "M&A optionality is a watch item rather than a thesis driver. FIS has a history of "
         "large deals, and the market will likely penalize any return to empire-building. Our "
         "valuation assumes tuck-in acquisitions only; a large dilutive deal would be a reason "
         "to revisit the call."),
    ],
    "Valuation": [
        ("p", "Key sensitivities: a one-point change in the organic growth rate moves fair value "
         "by roughly a tenth, while a 100bp change in the terminal margin assumption moves it "
         "by a similar order. The discount rate reflects a stable, contract-heavy business with "
         "some cyclical exposure to bank IT spending; we consider 10% appropriate and test the "
         "conclusion at higher rates in the bear case."),
    ],
    "Key Risks": [("bullets", [
        "Large-deal risk: a return to transformative M&A could destroy shareholder value and "
        "re-lever the balance sheet.",
        "Talent and execution: the margin program depends on sustained operational discipline "
        "across a large organization.",
    ])],
}

X["VITL"] = {
    "Investment Thesis": [
        ("p", "The farm network is the part of the story most investors underweight. Vital Farms "
         "contracts with hundreds of family farms, and bringing a new farm into the network, "
         "converting pasture, building houses, certifying standards, takes the better part of a "
         "year. That lead time means supply cannot respond quickly to demand spikes, which "
         "sounds like a constraint but functions as a moat: no competitor can flood the "
         "pasture-raised shelf on short notice, and Vital Farms' first-mover relationships with "
         "the best operators are hard to replicate."),
        ("p", "We also like the capital-light structure. Because production is contracted rather "
         "than owned, growth does not require building plants; the company's capital goes to "
         "brand, distribution, and the supply-chain team that manages the farm network. Returns "
         "on invested capital are therefore high for a food company, and the business can scale "
         "revenue without a commensurate scale in fixed assets."),
    ],
    "Business Overview": [
        ("p", "Distribution is concentrated in the natural and conventional grocery channels, "
         "with the brand now present in a large majority of US food retail doors. Velocity, "
         "units sold per store per week, is among the highest in the egg category, which is why "
         "retailers keep expanding shelf allocation: Vital Farms turns the premium egg set "
         "faster than slower-moving alternatives, making it a productive use of shelf space."),
        ("p", "The butter business applies the same playbook to a second category: pasture-"
         "raised positioning, premium pricing, and the same retail buyer relationships. It is "
         "smaller and earlier-stage, but it demonstrates that the brand equity transfers beyond "
         "eggs, which extends the growth runway."),
    ],
    "Forward Outlook": [
        ("p", "The central question for the next five years is how large the pasture-raised "
         "segment can become. Our base case assumes the premium tier continues to take share "
         "from conventional and cage-free, supported by retailer commitments to cage-free "
         "sourcing that push consumers up the welfare ladder. If pasture-raised reaches even a "
         "mid-single-digit share of the total egg market, Vital Farms' revenue more than "
         "doubles from current levels."),
        ("p", "Margins should benefit from scale in two ways: fixed corporate costs spread over "
         "a larger revenue base, and improved logistics density as volumes grow in existing "
         "regions. Offsetting this, the company will keep investing in the farm network and in "
         "brand marketing, so we model gradual rather than dramatic operating leverage."),
    ],
    "Valuation": [
        ("p", "The valuation hinges on the terminal margin and the duration of high growth. Our "
         "base case assumes revenue growth moderates from current elevated rates to a "
         "sustainable high-single-digit pace as distribution matures, with gross margins "
         "recovering to the mid-30s range the brand has demonstrated. Because this is a "
         "small-cap with commodity exposure, we use a discount rate at the higher end of our "
         "standard range; the bear case adds further stress to both growth and margins."),
    ],
    "Key Risks": [("bullets", [
        "Customer concentration: a small number of large grocery retailers represent a "
        "significant share of sales.",
        "Brand risk: the ethical-sourcing promise is the brand; any supply-chain controversy "
        "would damage it disproportionately.",
    ])],
}

X["BKNG"] = {
    "Investment Thesis": [
        ("p", "Consider the numbers behind the moat. Booking.com lists millions of properties, "
         "including a vast long tail of independent hotels and alternative accommodations that "
         "no new entrant can assemble quickly. Hundreds of millions of verified guest reviews "
         "create a data asset that improves conversion and cannot be scraped into existence. "
         "And the performance-marketing operation spends billions annually with a return on ad "
         "spend honed over two decades. An AI startup can build a chat interface in months; it "
         "cannot build these assets in years."),
        ("p", "The connected-trip strategy deserves more credit than it gets. Flights, "
         "attractions, airport taxis, and travel insurance attached to accommodation bookings "
         "are growing faster than the core, and each attached product increases customer "
         "lifetime value while using the same acquisition spend. This is how a mature "
         "marketplace keeps growing: not by finding new travelers, but by capturing more of "
         "each traveler's wallet."),
    ],
    "Business Overview": [
        ("p", "Geographic mix is a structural advantage. Europe, where Booking.com is "
         "dominant, has a fragmented hotel landscape of independent properties that depend "
         "on the platform for demand; this fragmentation is precisely what makes the "
         "marketplace indispensable. In the US, where chains are stronger, Priceline and Kayak "
         "play larger roles, and Agoda anchors the Asia-Pacific presence."),
        ("p", "The Genius loyalty program now counts a large share of bookings from repeat "
         "members, which reduces marginal acquisition cost over time. Direct traffic, mobile "
         "app usage, and member pricing tiers form a flywheel: better economics fund better "
         "member benefits, which drive more direct bookings."),
    ],
    "Forward Outlook": [
        ("p", "Alternative accommodations remain the largest white space. Booking has been "
         "closing the supply gap with the segment leader for several years, and each "
         "incremental property added improves search completeness and conversion. We expect "
         "this segment to outgrow hotels within the mix, which is margin-accretive because "
         "alternative-accommodation economics are attractive and growing from a smaller base."),
        ("p", "On capital allocation, we expect the buyback to continue at a pace that retires "
         "a mid-single-digit percentage of shares annually. At current free cash flow levels, "
         "this is sustainable without stretching the balance sheet, and it means per-share "
         "metrics will compound several points faster than enterprise metrics indefinitely."),
        ("p", "The AI interface shift is the swing factor for the terminal value. Our base case "
         "assumes Booking successfully integrates AI trip planning and agentic booking into its "
         "own platform, neutralizing the threat. The bear case assumes a genuine "
         "disintermediation event; we assign it the standard 25% weight, which is a meaningful "
         "concession to the risk and the reason the target is $219 rather than higher."),
    ],
    "Valuation": [
        ("p", "Sensitivities: the valuation is most exposed to the take rate and the terminal "
         "growth rate. A 50bp permanent compression in take rates would reduce fair value by "
         "roughly a tenth; conversely, sustained buybacks above our assumed pace add a similar "
         "magnitude. The discount rate reflects a dominant but potentially disrupted "
         "marketplace; we use a standard rate with the disruption risk concentrated in the "
         "bear case rather than the discount."),
    ],
    "Key Risks": [("bullets", [
        "FX: a large share of revenue is earned in euros and other currencies; dollar "
        "strength is a reported-revenue headwind.",
        "Alternative-accommodation competition: the segment leader remains formidable and "
        "could defend share aggressively.",
    ])],
}

X["ZTS"] = {
    "Investment Thesis": [
        ("p", "The R&D engine is the underappreciated asset. Zoetis spends more on animal-health "
         "R&D than any competitor, and the output, monoclonal antibodies for dermatology and "
         "pain, novel parasiticides, poultry vaccines, diagnostics, has been a metronome of "
         "franchise creation. In animal health, where development timelines are shorter and "
         "success rates higher than in human pharma, sustained R&D spending compounds into a "
         "portfolio that competitors cannot match by acquisition alone."),
        ("p", "Pet humanization is the demand tailwind that makes the economics work. Pet owners "
         "increasingly treat animals as family members, and spending on pet healthcare has grown "
         "faster than GDP across cycles, including downturns. This is not a discretionary "
         "category in the way investors sometimes assume: an owner will cut many expenses before "
         "skipping a dog's arthritis treatment. That inelasticity is what supports Zoetis's "
         "pricing power and the through-cycle stability of its cash flows."),
        ("p", "On the recent concerns directly: dermatology competition is real, but the "
         "category is growing and Zoetis's portfolio approach (Apoquel for acute, Cytopoint for "
         "maintenance, plus pipeline follow-ons) defends better than any single product could. "
         "Librela's launch cadence has been debated quarter to quarter, but the treated "
         "population remains a small fraction of the addressable one. We see noise around a "
         "signal that is still intact."),
    ],
    "Business Overview": [
        ("p", "Manufacturing is a quiet moat. Biologics and vaccine production require "
         "specialized facilities, regulatory approvals, and process expertise that take years "
         "to build; Zoetis's global manufacturing network is a scale advantage that supports "
         "both margins and supply reliability. In a business where product shortages directly "
         "cost veterinarian loyalty, reliable supply is a competitive weapon."),
        ("p", "The diagnostics and genetics businesses, though smaller, deepen the customer "
         "relationship: a veterinarian using Zoetis diagnostics is more likely to prescribe "
         "Zoetis therapeutics, and livestock genetics data creates switching costs for "
         "producers. These adjacencies grow the share of wallet beyond individual molecules."),
    ],
    "Forward Outlook": [
        ("p", "The pipeline beyond pain is the reason for the 15-year horizon. Monoclonal "
         "antibodies are a platform, not a product: the same technology that produced Librela "
         "and Solensia can address other chronic conditions in companion animals. Zoetis's "
         "antibody pipeline is the deepest in the industry, and each successful launch extends "
         "the growth runway without requiring a heroic assumption about any single product."),
        ("p", "Livestock deserves a balanced view. It is cyclical and lower-margin than "
         "companion animal, but it is also a scale business where Zoetis is the global leader, "
         "and protein demand growth in emerging markets is a multi-decade tailwind. We model "
         "it as a steady contributor rather than a growth engine, which is appropriately "
         "conservative given the cyclicality."),
        ("p", "Capital allocation should remain shareholder-friendly: the dividend has grown "
         "consistently since the spin-off, and buybacks offset dilution with room to retire "
         "shares. With FCF conversion above 80%, the company can fund R&D, the dividend, and "
         "buybacks simultaneously, which is the practical meaning of the compounder "
         "qualification."),
    ],
    "Valuation": [
        ("p", "Under compounder terms, the valuation math changes in two ways that matter. "
         "First, the 15-year horizon captures more of the pain-franchise and pipeline value "
         "that a 10-year model truncates. Second, the 8-8.5% base discount reflects the "
         "empirical stability of the cash flows rather than a generic large-cap rate. Both "
         "choices are earned by the verified history, and both are revoked automatically if "
         "the ROIC or margin triggers trip. The terminal growth cap of 3.0% is applied to a "
         "margin set at the demonstrated sustained level, not a peak."),
    ],
    "Key Risks": [("bullets", [
        "Pipeline failure: the long-horizon thesis depends on continued R&D productivity; a "
        "dry spell would eventually show in growth.",
        "Veterinarian consolidation: corporate practice groups gaining share could pressure "
        "pricing over time.",
    ])],
}

X["EXE"] = {
    "Investment Thesis": [
        ("p", "The cost position is the core of the call. Expand's Marcellus and Haynesville "
         "acreage sits at the low end of the North American cost curve, which means the "
         "company generates free cash flow at gas prices where higher-cost producers merely "
         "survive. In a commodity business, being the low-cost producer is the entire "
         "strategy; everything else, hedging, marketing, capital returns, is execution "
         "against that advantage."),
        ("p", "LNG is the structural demand story that the spot market underappreciates. US LNG "
         "export capacity is growing substantially through the end of the decade, and each new "
         "train is a durable source of demand for Gulf Coast and Appalachian gas. Expand's "
         "Haynesville position is advantaged for Gulf Coast LNG, and its scale gives it "
         "marketing optionality, including exposure to international price linkages, that "
         "smaller producers cannot access."),
        ("p", "Management credibility on capital discipline is the third pillar, and it is "
         "recently earned: the combined company has held the line on maintenance production "
         "rather than chasing growth, even when prices spiked. We treat past discipline as "
         "evidence, not promise, and the base case assumes it continues; any deviation would "
         "be visible quickly in the capex and production data."),
    ],
    "Business Overview": [
        ("p", "The asset base is concentrated in two world-class plays. The Marcellus offers "
         "enormous, low-decline inventory with proximity to premium Northeast and "
         "Mid-Atlantic demand; the Haynesville offers high-rate wells with direct access to "
         "Gulf Coast LNG and industrial demand. Together they provide decades of drilling "
         "inventory at current activity levels, which removes the treadmill dynamic that "
         "plagues shorter-lived shale plays."),
        ("p", "The commercial structure includes a base dividend designed to be sustainable at "
         "low gas prices, supplemented by buybacks that flex with free cash flow. Hedging "
         "covers a portion of near-term production to protect the dividend; the company "
         "deliberately leaves upside exposure, which is the correct posture for a "
         "low-cost producer."),
    ],
    "Forward Outlook": [
        ("p", "Data-center power demand is an emerging call option on gas volumes. US "
         "electricity demand growth, driven by AI data centers and industrial reshoring, "
         "disproportionately benefits natural gas as the marginal source of new dispatchable "
         "power. Expand's basins are well positioned to serve this demand, and we expect "
         "behind-the-meter and utility contracts to become a visible part of the demand "
         "picture over the forecast."),
        ("p", "Consolidation optionality is the other long-term lever. As the largest gas "
         "producer, Expand is the natural consolidator of remaining high-quality private and "
         "public gas assets. Our base case assumes no major deals, but the balance sheet and "
         "equity currency give the company an acquisition option that smaller peers lack; "
         "disciplined deals would be accretive to the per-share thesis."),
        ("p", "On price decks: our base case uses a mid-cycle Henry Hub assumption consistent "
         "with the LNG and power-demand outlook, not a spike. The investment works at that "
         "deck because of the cost position and the capital-return framework; it does not "
         "require the investor to forecast commodity prices correctly, only to believe that "
         "structural demand supports mid-cycle pricing over time."),
    ],
    "Valuation": [
        ("p", "The valuation is, unavoidably, a function of the long-term gas price deck: a "
         "$0.50 move in the sustained Henry Hub assumption shifts fair value by roughly a "
         "sixth. That sensitivity is disclosed rather than hidden, and it is why the "
         "probability weighting matters: the bear case prices a genuinely weak gas "
         "environment, and the weighted result still offers 31% upside from $85.52."),
    ],
    "Key Risks": [("bullets", [
        "Inventory exhaustion: the decades-of-inventory claim depends on continued drilling "
        "productivity; degradation would raise long-term costs.",
        "Takeaway constraints: pipeline capacity limits in Appalachia can strand gas and "
        "depress regional realizations.",
    ])],
}

X["FISV"] = {
    "Investment Thesis": [
        ("p", "Start with what has not changed: Fiserv processes an enormous share of US "
         "financial transactions, serves thousands of financial institutions with core "
         "systems they cannot easily replace, and converts a high proportion of earnings to "
         "cash. Businesses like this do not become impaired in eighteen months; they get "
         "mispriced when growth wobbles and the narrative turns. The current price is a "
         "narrative discount on a durable franchise."),
        ("p", "Clover's distribution advantage is structural, not cyclical. Unlike "
         "direct-to-merchant competitors, Clover reaches small businesses through banks and "
         "ISOs that already own the merchant relationship, which lowers acquisition cost and "
         "improves retention. The integrated software suite (payments plus operating tools) "
         "raises switching costs with each module adopted. We track Clover volume growth "
         "against the industry as the cleanest competitive read, and it has held up."),
        ("p", "The efficiency program is the margin lever the market is ignoring. Fiserv has a "
         "long record of extracting cost synergies, and the current program targets the "
         "overhead accumulated through years of acquisitions. We underwrite only the "
         "announced, trackable savings in the base case; faster realization is bull-case "
         "upside."),
    ],
    "Business Overview": [
        ("p", "Merchant Solutions is the growth segment: Clover point-of-sale, e-commerce "
         "processing, and enterprise merchant acquiring. Clover's mix is diversified across "
         "verticals (retail, restaurant, services), which smooths vertical-specific cycles, "
         "and the international rollout, though early, opens a second growth vector."),
        ("p", "Financial Solutions is the stability segment: core account processing for banks "
         "and credit unions, digital banking platforms, electronic payments (including Zelle "
         "and bill pay infrastructure), and risk management. Client retention is extremely "
         "high, contracts are multi-year, and incremental modules carry high margins."),
    ],
    "Forward Outlook": [
        ("p", "We expect the merchant deceleration to prove temporary, driven by a "
         "normalization of small-business formation and spending rather than share loss. As "
         "those headwinds fade, Clover's volume growth should re-accelerate toward its "
         "historical premium to the industry. The international business is the upside "
         "surprise candidate: early results in Latin America and other markets suggest the "
         "playbook travels, though we model it conservatively."),
        ("p", "In Financial Solutions, the real-time payments wave (FedNow and RTP adoption) "
         "creates a multi-year module-adoption cycle across the installed base. Banks need "
         "the infrastructure regardless of the macro environment, and Fiserv's incumbent "
         "position makes it the default provider. This is slow, high-margin, highly visible "
         "growth, the ballast of the thesis."),
        ("p", "Capital allocation is the compounding kicker: with leverage now manageable, "
         "free cash flow should fund buybacks at a pace that retires a mid-single-digit "
         "percentage of shares annually, plus a growing dividend. Per-share growth will "
         "therefore exceed enterprise growth by several points, which is meaningful at a "
         "compressed multiple."),
    ],
    "Valuation": [
        ("p", "Sensitivities: the valuation turns most on the organic growth re-acceleration "
         "path and the terminal margin. If growth merely stabilizes at current levels "
         "without re-accelerating, fair value falls by roughly a fifth, which is essentially "
         "the bear case; our 50% weight on the base case reflects our judgment that "
         "re-acceleration is the more likely outcome given the competitive evidence."),
    ],
    "Key Risks": [("bullets", [
        "Fintech disruption: embedded finance and software-led payments could bypass "
        "traditional processors over time.",
        "Integration overhang: years of acquisitions leave complex systems; execution "
        "missteps can disrupt clients.",
    ])],
}

X["TMUS"] = {
    "Investment Thesis": [
        ("p", "The spectrum advantage is the foundation everything else rests on. T-Mobile's "
         "mid-band holdings deliver a combination of speed and coverage that competitors "
         "cannot match without years of additional investment, and network quality is the "
         "primary driver of both gross additions and churn. Independent speed tests have "
         "consistently ranked T-Mobile first; that is not marketing, it is physics plus "
         "capital deployment."),
        ("p", "Fixed wireless is the growth vector the market still undervalues. Home internet "
         "over the 5G network monetizes excess capacity at very high incremental margins, "
         "and T-Mobile has scaled it to millions of subscribers faster than skeptics "
         "expected. The addressable market is large, the product keeps improving with "
         "network densification, and each subscriber adds revenue with minimal incremental "
         "cost."),
        ("p", "The capital-return program is the compounding engine. With merger integration "
         "spending complete and leverage declining, free cash flow supports buybacks at a "
         "scale that retires a high-single-digit percentage of shares in peak years. "
         "Combined with the dividend, total shareholder return from capital return alone is "
         "meaningful even before any growth."),
    ],
    "Business Overview": [
        ("p", "Postpaid phone is the core: the highest-value subscriber segment, where "
         "T-Mobile has led the industry in net additions for years. The value positioning, "
         "premium network at a discount to AT&T and Verizon pricing, continues to pull "
         "switchers, and the business-account segment, historically underpenetrated, is now "
         "a deliberate growth focus."),
        ("p", "Prepaid (Metro) serves the value-conscious segment with industry-leading "
         "economics, and the wholesale business monetizes network capacity through MVNO "
         "partnerships. Both are stable contributors that add scale without proportional "
         "cost."),
    ],
    "Forward Outlook": [
        ("p", "Rural and small-market expansion is the next share-gain frontier. T-Mobile's "
         "coverage investments have made it competitive in markets where it was historically "
         "weak, and the switcher pool there is large. We expect these markets to contribute "
         "an increasing share of net additions over the forecast, extending the growth "
         "runway beyond the already-penetrated urban base."),
        ("p", "On the technology front, network slicing and standalone 5G capabilities open "
         "enterprise use cases (private networks, IoT, low-latency applications) that carry "
         "higher ARPU than consumer lines. We do not underwrite large enterprise 5G revenue "
         "in the base case, but the optionality lengthens the growth duration."),
        ("p", "Financially, the trajectory is straightforward: mid-single-digit service "
         "revenue growth, EBITDA margins expanding as the base scales, capex intensity "
         "declining from merger-era peaks, and the resulting free cash flow funding "
         "dividends and buybacks. It is a compounding story, not a transformation story, "
         "and the valuation reflects that appropriately."),
    ],
    "Valuation": [
        ("p", "Sensitivities: the valuation is most sensitive to the long-term net-addition "
         "trajectory and the buyback pace. If net additions fade to market growth sooner "
         "than modeled, fair value declines by roughly a tenth; if buybacks run above our "
         "assumed pace, it rises similarly. The discount rate reflects a mature, "
         "cash-generative telecom with modest disruption risk."),
    ],
    "Key Risks": [("bullets", [
        "Price competition: a sustained price war would compress ARPU across the industry.",
        "Technology shift: satellite-to-phone services could alter competitive dynamics at "
        "the margin over time.",
    ])],
}

notes = {n["ticker"]: copy.deepcopy(n) for n in bw3.NOTES}
for t, secs in X.items():
    n = notes[t]
    for heading, blocks in n["sections"]:
        if heading in secs:
            blocks.extend(secs[heading])

outdir = "/home/hatch/workspace/standalone-notes/pdfs"
for t, n in notes.items():
    path = os.path.join(outdir, "%s-equity-research-note.pdf" % t)
    build_note(path, n)
    print("built", path)
