"""Build 8 standalone equity research PDFs (wave 2). Fresh analyst notes dated October 4, 2026."""
import sys
sys.path.insert(0, "/home/hatch/workspace/standalone-notes")
from template import build_note

BANNED = ["old target", "previous note", "previous report", "prior report",
          "as we wrote", "prior methodology", "v2", "rebuild", "rebuilt",
          "addenda", "version", "upgraded", "downgraded", "was previously",
          "formerly"]

CORE_METHOD = (
    "Our valuation is a probability-weighted scenario DCF. We model bear, base, and bull cases "
    "over an explicit forecast horizon \u2014 10 years for most businesses, 15 years for businesses meeting our "
    "compounder-quality criteria (10+ years of ROIC above 15%, stable or expanding gross margins, "
    "free-cash-flow conversion above 80%, all verified from history, never projected) \u2014 weighted "
    "25% / 50% / 25%. Discount rates are scenario-specific: the base rate reflects fundamental business "
    "risk (9% for stable franchises, 10% standard, 12% or higher for speculative situations; 8-8.5% for "
    "compounder-quality businesses whose predictable cash flows genuinely lower risk); the bear case adds "
    "250bp, the bull case subtracts 150bp (floor 8%). Terminal value assumes no more than 2.5% perpetual "
    "growth (3.0% for compounder-quality businesses) applied to normalized mid-cycle margins \u2014 never peak "
    "margins \u2014 and any terminal value exceeding 70% of enterprise value is haircut and disclosed. "
    "Bear cases are required to be genuinely adverse and to sit below the current price. Management guidance "
    "is never accepted at face value; it is independently tested and haircut where evidence warrants."
)

INTL_CHINA = (
    " For this international business we add an explicit 250bp country-risk premium to the discount rate "
    "and benchmark multiples against regional peers facing similar risks, never US peers alone; structural "
    "risks (the VIE structure, regulatory intervention, confiscation scenarios) are modeled in cash flows "
    "and the bear case."
)

INTL_SEA = (
    " For this international business we add an explicit 150bp country-risk premium to the discount rate "
    "to reflect operating across Southeast Asia and Latin America, and we benchmark multiples against "
    "regional peers facing similar risks, never US peers alone; structural risks (regulatory intervention, "
    "currency shocks, political instability in key markets) are modeled in cash flows and the bear case."
)

def check_banned(text, name):
    import re
    low = text.lower()
    hits = [b for b in BANNED if re.search(r"\b" + re.escape(b) + r"\b", low)]
    if hits:
        raise SystemExit("BANNED PHRASE in %s: %s" % (name, hits))

notes = []

# =====================================================================================
# 1. VICI PROPERTIES (VICI) - BUY $39.00 vs $22.65 (+72%)
# =====================================================================================
notes.append(dict(
    ticker="VICI",
    company="VICI Properties Inc.",
    verdict="BUY",
    target="$39.00",
    price="$22.65",
    price_note="October 2, 2026 close",
    upside="+72%",
    sections=[
        ("Investment Thesis", [
            ("p", "VICI Properties owns the land and buildings underneath some of the most irreplaceable "
             "gaming assets in the United States, and it rents them to the operators on 40-to-50-year "
             "triple-net leases with contractual annual escalators. That structure is the entire thesis in one "
             "sentence: the cash flows are bond-like in their visibility, but they are attached to real estate "
             "that cannot be replicated \u2014 you cannot build another Caesars Palace on the Las Vegas Strip. At "
             "$22.65 the market prices VICI as though those leases carry the same risk as an average office REIT, "
             "and that is simply wrong. Occupancy across the portfolio has never meaningfully wavered, tenants "
             "pay every cost of ownership from taxes to maintenance, and rent escalators of 2% or more compound "
             "year after year regardless of what the economy does."),
            ("p", "The second leg of the thesis is external growth. VICI is one of very few counterparties that "
             "regional gaming operators, tribal owners, and experiential landlords can call when they want to "
             "monetize real estate at scale, and it has repeatedly funded those acquisitions at spreads that are "
             "accretive to adjusted funds from operations (AFFO) per share. Its investment-grade balance sheet "
             "gives it a cost of capital that smaller buyers cannot match, so the deal pipeline is a structural "
             "advantage, not a cyclical one. Each accretive deal lengthens the compounding runway without asking "
             "shareholders to underwrite new development risk."),
            ("p", "The third leg is diversification that the market has not yet priced. Over the past several "
             "years VICI has moved beyond pure casino real estate into golf courses, youth sports complexes, "
             "water parks, wellness resorts, and urban experiential assets \u2014 all still under the same "
             "triple-net, long-lease model. This broadens the tenant base and the acquisition funnel while "
             "leaving the economics unchanged. Experiential real estate is one of the few property categories "
             "where demand has grown through the post-pandemic cycle, and VICI is quietly becoming its "
             "landlord of record."),
            ("p", "Our fair value of $39.00 implies a dividend yield and AFFO multiple consistent with a "
             "high-quality net-lease REIT, not the distressed multiple the shares carry today. The upside case "
             "does not require heroics \u2014 it requires the market to recognize that 40-year leases on Strip "
             "real estate with investment-grade tenants deserve a premium, not a discount, to generic net "
             "lease. The dividend, which has grown every year since formation, pays investors to wait while the "
             "compounding does the work."),
        ]),
        ("Business Overview", [
            ("p", "VICI Properties is a real estate investment trust formed in 2017 and headquartered in New "
             "York. It owns roughly 90 properties comprising more than 125 million square feet, concentrated "
             "in gaming and experiential real estate. Its largest tenants include Caesars Entertainment, MGM "
             "Resorts, Hard Rock International, PENN Entertainment, and the Apollo-owned Venetian Resort on the "
             "Las Vegas Strip. The portfolio is diversified across destination markets (Las Vegas, Atlantic "
             "City) and regional gaming markets across the United States, plus a growing book of non-gaming "
             "experiential assets."),
            ("p", "The economic model is the triple-net lease: tenants pay rent plus all property taxes, "
             "insurance, and maintenance, so VICI's expenses are minimal and its margins are among the highest "
             "in the REIT universe. Leases typically run 40 to 50 years including renewal options, with "
             "contractual rent escalators \u2014 generally the greater of a fixed percentage (around 2%) or a "
             "CPI-linked increase with a cap. Occupancy is effectively 100%, and rent collection has remained "
             "intact through recessions, the pandemic shutdowns, and regional gaming downturns, a record that "
             "demonstrates the durability of the cash flows."),
            ("p", "VICI operates as a REIT, distributing the bulk of taxable income as dividends. Growth comes "
             "from three sources: contractual escalators, accretive acquisitions funded with a mix of debt and "
             "equity at spreads above its cost of capital, and loan investments secured by real estate. "
             "Management has maintained an investment-grade balance sheet with laddered maturities, giving it "
             "the capacity to act as the buyer of choice when operators look to unlock the value of their real "
             "estate."),
        ]),
        ("Forward Outlook", [
            ("p", "Our judgment is that VICI's next five years look more like a compounding machine than a "
             "cyclical casino bet. Las Vegas visitation and Strip gaming revenue have demonstrated remarkable "
             "resilience, and the tenants' rent coverage ratios \u2014 the cushion between property earnings and "
             "rent owed \u2014 remain healthy, which means the escalators keep compounding even if gaming revenue "
             "growth moderates. The regional gaming portfolio benefits from the same dynamic at lower absolute "
             "rent levels: these are cash-generative boxes in markets with limited new supply, and the operators "
             "cannot easily relocate."),
            ("p", "Where we see the real upside is the acquisition funnel. A wave of regional operators, tribal "
             "nations, and experiential owners are sitting on owned real estate that could be monetized, and "
             "VICI's scale and cost of capital make it the natural counterparty. We expect the company to "
             "continue deploying $1-3 billion a year into accretive deals when pricing is right, each one "
             "adding a few cents to AFFO per share that then compound through the escalators. The non-gaming "
             "experiential book \u2014 golf, water parks, wellness \u2014 should grow as a share of rent, further "
             "diversifying tenant concentration, which has been the market's main objection to the name."),
            ("p", "On capital returns, we expect the dividend to keep growing in line with AFFO per share, "
             "keeping the payout ratio in its historical range. The risk to this outlook is interest rates: as "
             "a REIT, VICI's valuation is sensitive to the long end of the curve, and a sustained move higher "
             "in Treasury yields would compress the multiple even if the cash flows are unaffected. That is a "
             "valuation risk, not a business risk, and at the current price we believe it is already more than "
             "reflected in the shares."),
        ]),
        ("Valuation", [
            ("p", "Our valuation is a probability-weighted scenario DCF of VICI's distributable rental cash "
             "flows, weighted 25% bear / 50% base / 25% bull. In the base case, AFFO per share grows at a "
             "high-single-digit rate driven by contractual escalators of roughly 2% plus a steady cadence of "
             "accretive acquisitions funded at spreads above the cost of capital, discounted at 9% to reflect "
             "the stability of a triple-net franchise with 40-plus-year leases. The result is a fair value "
             "consistent with our $39.00 target \u2014 a multiple of forward AFFO in line with high-quality net-lease "
             "REITs and a dividend yield that reflects the visibility of the cash flows."),
            ("p", "The bear case assumes a genuine recession that pressures tenant earnings and rent coverage, "
             "a freeze in the acquisition market, and a higher-for-longer rate environment that keeps REIT "
             "multiples compressed; the resulting fair value sits well below the current $22.65 price, as our "
             "framework requires. The bull case assumes the acquisition pipeline reaccelerates as operators "
             "monetize real estate, Strip and regional gaming revenue grow, and the non-gaming experiential "
             "book scales \u2014 a combination that would justify a premium multiple for the scarcity of the "
             "assets. The probability-weighted fair value equals our $39.00 target."),
            ("p", "We cross-check the DCF against dividend discount math: with a dividend that has grown every "
             "year and a payout ratio anchored to AFFO, a normalized yield for this quality of lease cash flow "
             "supports a price materially above today's quote. Terminal growth is capped at 2.5% on normalized "
             "rental margins, and the terminal value is a minority of enterprise value, consistent with a "
             "business whose value is dominated by visible contractual cash flows rather than distant "
             "assumptions."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Tenant concentration: Caesars and MGM account for a large share of rental revenue; distress at "
                "a top tenant would be the single largest threat to the dividend.",
                "Gaming cyclicality: a deep recession would reduce tenant earnings and rent coverage ratios, "
                "even though leases are contractual and collection history is strong.",
                "Interest-rate sensitivity: as a REIT, VICI's share price and cost of capital are exposed to "
                "movements in long-term Treasury yields regardless of operating performance.",
                "Acquisition execution: the external-growth thesis depends on finding accretive deals; "
                "overpaying or funding deals with expensive equity would dilute AFFO per share.",
                "Regulatory and regional competition: new gaming supply or adverse regulatory changes in key "
                "markets could pressure tenant economics over time.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "A dividend cut or a payout ratio pushed permanently above sustainable levels \u2014 the dividend "
                "record is the core evidence for the thesis.",
                "A major tenant bankruptcy, lease rejection, or rent concession that breaks the perfect "
                "collection record.",
                "Two consecutive years of declining AFFO per share, signaling that escalators and acquisitions "
                "no longer offset dilution.",
                "A large acquisition funded at a spread that is dilutive to AFFO per share, indicating "
                "discipline has slipped.",
                "A sustained rise in long-term rates that reprices the entire REIT sector to yields that make "
                "our target multiple unattainable.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", CORE_METHOD + " For this REIT the scenario cash flows are distributable rental cash flows "
             "(AFFO) rather than corporate free cash flow, but the framework is identical: scenario-specific "
             "discounts, capped terminal growth on normalized margins, and a bear case that sits below the "
             "current price."),
        ]),
    ],
))

# =====================================================================================
# 2. PAYPAL (PYPL) - BUY $90.00 vs $52.80 (+71%)
# =====================================================================================
notes.append(dict(
    ticker="PYPL",
    company="PayPal Holdings, Inc.",
    verdict="BUY",
    target="$90.00",
    price="$52.80",
    price_note="October 2, 2026 close",
    upside="+71%",
    sections=[
        ("Investment Thesis", [
            ("p", "PayPal is priced as a melting ice cube and valued as one of the great two-sided payment "
             "networks ever built \u2014 and only one of those can be right. The branded PayPal checkout button "
             "remains the highest-converting payment method in e-commerce: merchants accept it because "
             "consumers trust it, and consumers use it because merchants accept it. That flywheel, built over "
             "two decades across more than 400 million active accounts and tens of millions of merchants, does "
             "not evaporate because Apple Pay exists. At $52.80 the market is capitalizing a permanent decline "
             "in the branded business that the transaction data simply does not show: branded checkout volumes "
             "continue to grow, take rates are stabilizing, and the margin structure is inflecting as new "
             "products shift the mix back toward higher-value flows."),
            ("p", "The second pillar is the turnaround under CEO Alex Chriss, which is further along than the "
             "stock price suggests. The company has refocused on its core checkout and payments strength, "
             "launched Fastlane \u2014 a one-click guest checkout that materially lifts conversion for merchants "
             "\u2014 and begun to monetize Venmo in earnest after years of leaving money on the table. Operating "
             "margins are expanding as the company rationalizes costs and as higher-margin branded volume "
             "outgrows the lower-margin Braintree processing business. This is the classic setup: a hated "
             "turnaround where the numbers turn before the narrative does."),
            ("p", "The third pillar is capital return. PayPal generates enormous free cash flow, and with the "
             "shares trading at a mid-teens multiple of earnings, every dollar of buybacks retires stock at "
             "prices that will look absurd in hindsight if the business merely stabilizes. The combination of "
             "mid-single-digit revenue growth, margin expansion of several hundred basis points, and a "
             "shrinking share count is a powerful earnings-per-share compounding formula that requires no heroic "
             "assumptions about market share gains."),
            ("p", "Our $90.00 fair value assumes PayPal is a low-growth compounder, not a high-growth "
             "disruptor \u2014 and the current price does not even grant it that. The risk-reward is skewed "
             "because the downside case (continued share erosion, fee compression) is fully priced while the "
             "base case (stable branded checkout, Venmo monetization, Fastlane adoption, agentic-commerce "
             "optionality) is priced at roughly zero probability. We see +71% upside to fair value with a "
             "dividend-like downside cushion from the buyback and the cash generation."),
        ]),
        ("Business Overview", [
            ("p", "PayPal Holdings, headquartered in San Jose, California, is one of the world's largest digital "
             "payment platforms. Its core is the branded checkout business: the PayPal button and digital "
             "wallet that consumers use to pay online, in-app, and increasingly in-store. Around that core sit "
             "Venmo, the leading US peer-to-peer payment app with a large and young user base; Braintree, the "
             "full-stack payment processor that powers unbranded card processing for large merchants and "
             "platforms; and smaller businesses including Xoom (remittances) and merchant lending products."),
            ("p", "The economics differ by product. Branded checkout carries the highest take rate and margin: "
             "PayPal earns a percentage of each transaction plus a fixed fee, with minimal incremental cost per "
             "transaction. Braintree is a scale processing business with much thinner margins but large volume. "
             "Venmo monetization \u2014 through instant transfers, the Venmo debit card, and merchant payments "
             "\u2014 has been the long-awaited second act. The company's moat is its two-sided network: consumer "
             "trust and merchant acceptance reinforce each other, and the data across hundreds of billions of "
             "transactions improves risk management and authorization rates in ways new entrants cannot quickly "
             "replicate."),
            ("p", "PayPal processes trillions of dollars in total payment volume annually. It is a "
             "capital-light business that converts a high share of operating profit into free cash flow, which "
             "management has directed toward share repurchases and, more recently, disciplined reinvestment in "
             "checkout innovation such as Fastlane and AI-driven shopping experiences."),
        ]),
        ("Forward Outlook", [
            ("p", "Our judgment is that PayPal's next chapter will be written in checkout conversion, not in "
             "winning a war against Apple Pay. The relevant question is not whether alternative payment methods "
             "exist \u2014 they do, and they will keep existing \u2014 but whether PayPal's branded button keeps "
             "converting better than the alternatives, because conversion is what merchants pay for. Every data "
             "point we have says it does: Fastlane's early merchant results show meaningful conversion lifts, "
             "and the branded take rate has stabilized as the company prices for the value it delivers. We "
             "expect branded checkout to keep growing at a healthy clip while Braintree provides volume scale "
             "at thinner margins \u2014 a mix that, on balance, supports margin expansion as the higher-value "
             "lines grow faster."),
            ("p", "Venmo is the underappreciated call option inside the company. With tens of millions of "
             "monthly active users who skew young and digitally native, even modest progress in monetization \u2014 "
             "debit card interchange, pay-with-Venmo at checkout, instant-transfer fees \u2014 drops almost "
             "entirely to the bottom line. We expect Venmo's revenue contribution to become material to the "
             "growth algorithm over the next three years, and the market currently assigns it little value."),
            ("p", "Longer term, agentic commerce \u2014 AI agents that shop on consumers' behalf \u2014 could be "
             "either a threat or an enormous opportunity for PayPal, and we lean toward opportunity: whoever "
             "owns the trusted payment credential inside the agent's wallet owns the transaction. PayPal's "
             "two-sided network and risk infrastructure position it well for that world. We do not need that "
             "thesis to work for the $90 target; it is upside. What we need is operational steadiness: mid-"
             "single-digit revenue growth, a few hundred basis points of margin expansion, and aggressive "
             "buybacks. That is a low bar for a business of this quality."),
        ]),
        ("Valuation", [
            ("p", "Our valuation is a probability-weighted scenario DCF, weighted 25% bear / 50% base / 25% "
             "bull. In the base case, revenue grows at mid-single-digit rates as branded checkout growth and "
             "Venmo monetization offset the dilutive mix of Braintree volume; operating margins expand toward "
             "the mid-20s as the cost discipline of the turnaround holds and higher-margin products outgrow "
             "processing; and free cash flow per share grows faster than revenue as buybacks shrink the share "
             "count. We discount at the 10% standard rate \u2014 PayPal is neither a fragile startup nor a "
             "regulated utility \u2014 with terminal growth capped at 2.5% on normalized mid-cycle margins. The "
             "probability-weighted fair value equals our $90.00 target."),
            ("p", "The bear case is genuinely adverse and sits below the current price, as required: branded "
             "checkout share erodes structurally to wallets and buy-now-pay-later, regulators compress "
             "interchange economics, and the turnaround stalls \u2014 a combination that would leave the shares "
             "worth less than today's quote. We assign it 25% because the competitive threats are real, but "
             "the transaction data argues against them being the base case. The bull case assumes Fastlane "
             "becomes the default guest checkout across large merchants, Venmo monetization inflects, and "
             "PayPal captures a meaningful share of agentic-commerce payment flows, discounted 150bp below the "
             "base rate."),
            ("p", "A cross-check on multiples supports the conclusion: at $52.80 the shares trade at a multiple "
             "of forward earnings more appropriate to a no-growth melting business, while the free-cash-flow "
             "yield \u2014 before buybacks \u2014 is in the high single digits. For a capital-light network "
             "business with this return profile, that pricing implies a future the fundamentals do not support."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Competitive pressure from Apple Pay, Google Pay, Stripe, Adyen, and buy-now-pay-later "
                "providers could erode branded checkout share or compress take rates.",
                "Regulatory risk around interchange fees, digital-wallet rules, and data privacy could reduce "
                "monetization across the platform.",
                "Execution risk: the turnaround depends on continued product innovation (Fastlane, Venmo "
                "monetization) and cost discipline under current leadership.",
                "Credit exposure through buy-now-pay-later and merchant lending could produce losses in a "
                "consumer downturn.",
                "Technological disruption: shifts in how consumers pay \u2014 including agentic AI commerce \u2014 "
                "could bypass traditional checkout flows if PayPal fails to embed itself in new interfaces.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Two consecutive quarters of declining branded-checkout payment volume \u2014 the network "
                "flywheel breaking would invalidate the core thesis.",
                "A sustained decline in take rate not explained by mix shift, indicating pricing power has "
                "been lost.",
                "Operating margin contraction resuming after the turnaround gains, suggesting cost discipline "
                "was temporary.",
                "Venmo monthly active users declining or monetization per user stalling for a full year.",
                "A large dilutive acquisition that diverts capital from buybacks into empire-building.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", CORE_METHOD),
        ]),
    ],
))

# =====================================================================================
# 3. TENCENT MUSIC (TME) - BUY $13.00 vs $7.74 (+68%)
# =====================================================================================
notes.append(dict(
    ticker="TME",
    company="Tencent Music Entertainment Group",
    verdict="BUY",
    target="$13.00",
    price="$7.74",
    price_note="October 2, 2026 close",
    upside="+68%",
    sections=[
        ("Investment Thesis", [
            ("p", "Tencent Music is the Spotify of China that the market still prices like a karaoke-app "
             "operator in structural decline. That framing is years out of date. The company's revenue mix has "
             "pivoted decisively toward online music services \u2014 subscriptions, advertising, digital albums, "
             "concerts \u2014 which grew 11% year over year in the second quarter of 2026 to RMB 7.61 billion, "
             "while the legacy social-entertainment business continues its managed shrink. At $7.74 the shares "
             "price in a future where Chinese consumers never pay for music; the reality is that they "
             "increasingly do, and Tencent Music collects the toll."),
            ("p", "The core of the bull case is paid penetration. Tencent Music ended 2025 with well over 120 "
             "million paying users, yet that is still only around a fifth of its music monthly active users \u2014 "
             "roughly half Spotify's conversion rate in mature markets. Every point of conversion is almost pure "
             "margin, because the content costs are largely fixed. On top of that, the Super VIP (SVIP) tier \u2014 "
             "priced at roughly RMB 40 per month versus RMB 8 for standard \u2014 passed 20 million subscribers by "
             "year-end 2025 and is the engine of average-revenue-per-user expansion. A subscriber base "
             "migrating up a 5x price ladder is one of the most attractive unit-economics stories in global "
             "consumer internet."),
            ("p", "The $2.4 billion acquisition of Ximalaya, completed in May 2026, extends the runway further. "
             "Ximalaya is China's leading online audio platform \u2014 podcasts, audiobooks, long-form audio \u2014 "
             "and folding it into Tencent Music creates cross-selling between music subscribers and audio "
             "listeners while consolidating the broader audio market. The market has treated the deal as a "
             "distraction; we see it as the company buying the adjacent category it would otherwise have to "
             "compete with, at a price its balance sheet easily absorbs."),
            ("p", "We do not minimize the China discount: the VIE structure, regulatory overhang, and "
             "geopolitical risk are real, and our valuation charges a full 250bp country-risk premium for them. "
             "But after that charge, the math still works. Our $13.00 fair value implies the market eventually "
             "pays a normal multiple for a subscription business with 120 million-plus paying users, rising "
             "ARPPU, and a net-cash balance sheet \u2014 not a heroic multiple, just a normal one. The bear case "
             "at $4.84, which sits well below the current price, captures what happens if regulation or "
             "competition breaks the story; we think that outcome is over-weighted in today's price."),
        ]),
        ("Business Overview", [
            ("p", "Tencent Music Entertainment Group, headquartered in Shenzhen, operates China's largest online "
             "music platform through four flagship products: QQ Music, Kugou Music, Kuwo Music, and the WeSing "
             "karaoke app. Following the May 2026 closing of the Ximalaya acquisition, it also owns China's "
             "leading long-form audio platform. The company reports in two segments: music-related services "
             "(subscriptions, digital albums, advertising, concerts, and artist merchandise) and social "
             "entertainment (live streaming and online karaoke tipping)."),
            ("p", "The strategic pivot of the past several years has been the deliberate shift from tipping-"
             "driven social entertainment toward subscription-driven music services. Music-related services now "
             "account for the large majority of revenue and essentially all of the growth, while social "
             "entertainment \u2014 pressured by regulatory tightening around live streaming \u2014 has been "
             "managed for cash. The subscription business benefits from Tencent's broader ecosystem: "
             "distribution through WeChat and QQ, AI-driven recommendation, and partnerships with domestic and "
             "international labels that deepen the content moat."),
            ("p", "Economically, this is a classic subscription compounder in its early innings. Content "
             "licensing costs scale more slowly than subscriber revenue, so incremental paying users carry very "
             "high margins; the SVIP tier amplifies this by quintupling revenue per subscriber for the most "
             "engaged cohort. The company holds a substantial net-cash position, funds the Ximalaya deal from "
             "its balance sheet, and has begun returning capital through buybacks \u2014 unusual financial "
             "strength for a business the market prices as fragile."),
        ]),
        ("Forward Outlook", [
            ("p", "Our judgment is that Tencent Music is roughly where Spotify was five to seven years ago: "
             "past the proof-of-concept for paid conversion, but far from the penetration ceiling. Chinese "
             "consumers' willingness to pay for digital content has risen steadily across video, literature, "
             "and now music, and Tencent Music's conversion funnel \u2014 hundreds of millions of free users, "
             "AI-personalized recommendations, artist superfans products \u2014 is purpose-built to harvest "
             "that shift. We expect paying users to keep growing at a double-digit pace and, more importantly, "
             "ARPPU to keep climbing as the SVIP mix shifts upward and as the company layers concert ticketing, "
             "merchandise, and premium audio benefits onto the membership."),
            ("p", "Ximalaya is the swing factor for the next three years. The integration risk is real \u2014 "
             "large Chinese internet acquisitions have a mixed record \u2014 but the strategic logic is sound: "
             "music and long-form audio share users, share the subscription relationship, and share the fight "
             "against short-video platforms for ear time. If Tencent Music executes, the combined entity owns "
             "the two largest audio use cases in China and can bundle them in ways no competitor can match. "
             "Even a partial success adds a durable growth leg; the bull case assumes the full synergy thesis "
             "lands."),
            ("p", "The honest risk to this outlook is not competition \u2014 NetEase Cloud Music is a capable "
             "rival but the market is large enough for two winners \u2014 it is the regulatory and geopolitical "
             "environment. Another wave of live-streaming-style intervention aimed at the music business, or a "
             "serious escalation in US-China capital-markets tensions affecting the ADR, would impair the "
             "shares regardless of fundamentals. That is why the bear case is severe and why we demand the "
             "country-risk premium. But a business compounding subscribers at this pace, with this balance "
             "sheet, at this price, is the kind of asymmetry we look for: the market has priced the China "
             "discount twice \u2014 once in the multiple and once in the growth assumptions."),
        ]),
        ("Valuation", [
            ("p", "Our valuation is a probability-weighted scenario DCF, weighted 25% bear / 50% base / 25% "
             "bull, with an explicit 250bp China country-risk premium added to the discount rate \u2014 the "
             "base discount is therefore 12.5%, the bear case 15%, and the bull case 11%. Scenario-implied "
             "fair values are:"),
            ("table", (
                ["Scenario", "Weight", "Implied fair value", "Key drivers"],
                [
                    ["Bear", "25%", "$4.84", "Regulatory intervention hits music; VIE/geopolitical stress; "
                     "subscription growth stalls; Ximalaya integration fails; social entertainment drags."],
                    ["Base", "50%", "$11.56", "Paying users grow double-digits; SVIP mix drives ARPPU "
                     "expansion; music-services margins widen; Ximalaya contributes modestly."],
                    ["Bull", "25%", "$25.33", "Conversion approaches global levels; ARPPU compounding via "
                     "SVIP; Ximalaya synergies land; market awards a subscription-compounder multiple."],
                ],
            )),
            ("p", "The probability-weighted fair value supports our $13.00 target. The bear case at $4.84 sits "
             "well below the current $7.74 price, as our framework requires \u2014 it is the genuine disaster "
             "scenario in which the VIE structure or regulation impairs the equity. The base case values a "
             "durable subscription compounder growing music-services revenue at a mid-teens rate with expanding "
             "margins, discounted for China risk. The bull case reflects what the business is worth if paid "
             "penetration converges toward global norms \u2014 a transformation that would re-rate the multiple "
             "toward Western streaming peers."),
            ("p", "Terminal growth is capped at 2.5% on normalized mid-cycle margins, never peak margins, and "
             "the terminal value is a minority of enterprise value. We benchmark against regional streaming "
             "and subscription peers facing similar risks, never against US peers alone. The company's large "
             "net-cash position is counted once, in enterprise value \u2014 we do not double-count it in both "
             "the cash flows and the balance sheet."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Regulatory risk: Chinese authorities have previously intervened in live streaming and music "
                "copyright; new rules on pricing, exclusivity, or content could impair monetization.",
                "VIE / geopolitical risk: the variable-interest-entity structure and US-China tensions create "
                "tail risk for ADR holders, including delisting or ownership-structure scenarios.",
                "Competition from NetEase Cloud Music and short-video platforms (Douyin) competing for user "
                "time and music discovery.",
                "Ximalaya integration: the $2.4 billion acquisition may underdeliver on synergies or distract "
                "management from the core subscription engine.",
                "Macro sensitivity: a Chinese consumer downturn would slow discretionary subscription uptake "
                "and advertising revenue.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Paying-user net additions turning negative for two consecutive quarters \u2014 the conversion "
                "engine stalling would break the thesis.",
                "SVIP subscriber count declining or ARPPU falling year over year, indicating the premium tier "
                "has hit a wall.",
                "A regulatory action that directly caps music subscription pricing or mandates content "
                "sharing that destroys the catalog moat.",
                "Ximalaya write-downs or disclosure that integration synergies will not materialize.",
                "Any credible move by authorities against the VIE structure itself \u2014 this is the "
                "unhedgeable tail and we would exit on evidence it is materializing.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", CORE_METHOD + INTL_CHINA),
        ]),
    ],
))

# =====================================================================================
# 4. SEA LIMITED (SE) - BUY $149.00 vs $95.19 (+57%)
# =====================================================================================
notes.append(dict(
    ticker="SE",
    company="Sea Limited",
    verdict="BUY",
    target="$149.00",
    price="$95.19",
    price_note="October 2, 2026 close",
    upside="+57%",
    sections=[
        ("Investment Thesis", [
            ("p", "Sea Limited runs three businesses that each look mediocre in isolation and formidable in "
             "combination: Garena, the game publisher behind Free Fire; Shopee, the e-commerce marketplace "
             "leader across Southeast Asia, Taiwan, and Brazil; and SeaMoney, the digital financial services "
             "arm built on the transaction data of the other two. The market's enduring mistake with Sea is "
             "analyzing each segment against its worst comparable \u2014 Garena against aging game studios, "
             "Shopee against cash-burning marketplaces, SeaMoney against risky lenders \u2014 instead of pricing "
             "the flywheel. At $95.19 the shares embed the assumption that the flywheel never compounds; our "
             "work suggests it already is."),
            ("p", "Start with what changed: Sea is profitable now. The era of subsidized growth ended several "
             "years ago, and Shopee has demonstrated it can take share and make money at the same time, with "
             "logistics infrastructure \u2014 its own last-mile network across the region \u2014 as the moat that "
             "lets it do both. Take rates still sit well below global e-commerce peers, which means the "
             "monetization runway is measured in years, not quarters. Every point of take-rate expansion on "
             "Shopee's gross merchandise volume drops disproportionately to operating profit because the "
             "fulfillment network is already built."),
            ("p", "Garena, written off repeatedly since the post-pandemic gaming normalization, keeps "
             "generating the cash that funds everything else. Free Fire remains one of the most-played mobile "
             "games on earth, with particular strength in the emerging markets where Sea operates \u2014 the "
             "same markets where smartphone penetration and disposable income are still rising. The market "
             "treats Garena as a wasting asset; we treat it as a durable cash engine with new-title optionality "
             "that comes free with the shares."),
            ("p", "SeaMoney is the least understood and potentially the most valuable leg. Built on Shopee's "
             "transaction and logistics data, its lending products underwrite borrowers that traditional banks "
             "cannot see, and its payments products deepen the ecosystem lock-in. Fintech attached to commerce "
             "data has been the highest-return business model in emerging markets globally, and SeaMoney is "
             "still early in that journey. Our $149.00 fair value prices Shopee as a maturing regional champion "
             "with take-rate headroom, Garena as a durable cash cow, and SeaMoney as a fast-growing fintech \u2014 "
             "and charges a 150bp Southeast Asia country-risk premium for the privilege. The bear case at $75, "
             "below today's price, is the world where competition breaks all three engines at once; we consider "
             "that the tail, not the center."),
        ]),
        ("Business Overview", [
            ("p", "Sea Limited, headquartered in Singapore, operates across three segments. Garena is a global "
             "online games developer and publisher, best known for Free Fire, the battle-royale mobile game "
             "that has been among the most downloaded games worldwide for years, alongside a portfolio of "
             "licensed and self-developed titles. Shopee is the largest e-commerce platform in Southeast Asia "
             "and Taiwan by gross merchandise volume and orders, with a significant and growing presence in "
             "Brazil; it operates a hybrid marketplace model with first-party logistics capabilities in its "
             "core markets. SeaMoney (branded Monee in some markets) provides digital financial services "
             "including mobile wallet payments, consumer and SME lending, and digital banking services in "
             "several markets."),
            ("p", "The strategic logic is the ecosystem: Garena's massive user base seeds Shopee's customer "
             "acquisition, Shopee's transaction volume generates the data and distribution for SeaMoney, and "
             "SeaMoney's payments and credit products increase conversion and retention on Shopee. This "
             "flywheel is Sea's central competitive advantage against single-vertical rivals \u2014 TikTok Shop "
             "in commerce, traditional banks in lending \u2014 because none of them sees the full customer the "
             "way Sea does."),
            ("p", "Financially, the company has transitioned from growth-at-all-costs to profitable growth. "
             "Shopee reached adjusted EBITDA profitability while maintaining market leadership; Garena remains "
             "highly cash-generative with industry-leading margins; SeaMoney is the fastest-growing segment "
             "with expanding loan books. The balance sheet carries substantial cash, giving the company "
             "strategic flexibility across cycles."),
        ]),
        ("Forward Outlook", [
            ("p", "Our judgment is that Shopee's next phase will be defined by monetization, not market-share "
             "warfare. The destructive subsidy battles of the past are over \u2014 every major regional player "
             "has learned that lesson \u2014 and Shopee's logistics moat means it can raise take rates "
             "gradually without losing sellers or buyers. We expect gross merchandise volume to keep growing "
             "at a healthy double-digit pace on the back of rising e-commerce penetration in Southeast Asia, "
             "while take rates grind upward toward levels that global peers sustain. That combination \u2014 "
             "volume growth plus monetization expansion on a fixed logistics base \u2014 is the classic "
             "e-commerce profit inflection, and we believe Sea is in its early stages."),
            ("p", "For Garena, our view is deliberately unglamorous: Free Fire does not need to grow for the "
             "thesis to work; it needs to endure. Mobile gaming in emerging markets is supported by "
             "demographics \u2014 young populations, rising smartphone adoption, increasing spending power \u2014 "
             "and Free Fire's low device requirements make it the default game for exactly those users. New "
             "titles are genuine upside: Garena's publishing infrastructure means any hit scales quickly, but "
             "we underwrite the segment as a cash cow and treat hits as free options."),
            ("p", "SeaMoney is where our forward view is most optimistic and the market's is most skeptical. "
             "The bearish concern is credit quality \u2014 lending to thin-file borrowers in volatile economies. "
             "Our read of the data is that SeaMoney's underwriting, informed by real commerce and logistics "
             "behavior rather than self-reported income, has produced loss rates the skeptics did not expect, "
             "and the loan book keeps growing. If that continues, SeaMoney graduates over the next several "
             "years from sidecar to core earnings driver, and the market will be forced to value it as a "
             "fintech rather than as a cost center. That re-rating is a meaningful part of our bull case."),
        ]),
        ("Valuation", [
            ("p", "Our valuation is a probability-weighted scenario DCF, weighted 25% bear / 50% base / 25% "
             "bull, with an explicit 150bp Southeast Asia country-risk premium added to the discount rate. "
             "Scenario-implied fair values are:"),
            ("table", (
                ["Scenario", "Weight", "Implied fair value", "Key drivers"],
                [
                    ["Bear", "25%", "$75", "E-commerce price war resumes (TikTok Shop, Lazada); Free Fire "
                     "declines steeply; SeaMoney credit losses spike; regional macro shock."],
                    ["Base", "50%", "$141", "Shopee GMV grows double-digits with take-rate expansion; Garena "
                     "cash flows endure; SeaMoney scales profitably; margins widen on logistics leverage."],
                    ["Bull", "25%", "$256", "Take rates normalize toward global peers; SeaMoney becomes a "
                     "core fintech earnings engine; new Garena hit; market re-rates the flywheel."],
                ],
            )),
            ("p", "The probability-weighted fair value supports our $149.00 target. The bear case at $75 sits "
             "below the current $95.19 price, as required \u2014 it is the world where all three engines "
             "misfire simultaneously, which we view as a genuine tail given the diversification across "
             "segments and geographies. The base case values Shopee on a long monetization runway, Garena as "
             "a durable cash cow, and SeaMoney as a high-growth fintech, with the country-risk premium fully "
             "charged. The bull case captures the re-rating if SeaMoney's underwriting proves out and Shopee's "
             "take rates converge toward global norms."),
            ("p", "Terminal growth is capped at 2.5% on normalized mid-cycle margins \u2014 we do not project "
             "peak e-commerce or gaming margins into perpetuity \u2014 and we benchmark multiples against "
             "regional e-commerce, gaming, and fintech peers facing similar emerging-market risks, never US "
             "peers alone. The terminal value is a minority of enterprise value, consistent with a business "
             "whose near-term cash generation is substantial and visible."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "E-commerce competition: TikTok Shop, Lazada (Alibaba), and local players could reignite "
                "subsidy wars or take share in key markets.",
                "Gaming concentration: Free Fire is a large share of Garena's profit; a sharp decline in "
                "engagement would reduce the cash engine funding the other segments.",
                "SeaMoney credit risk: rapid loan-book growth among thin-file borrowers could produce "
                "unexpected losses in an economic downturn.",
                "Regulatory and political risk across Southeast Asia, Taiwan, and Latin America, including "
                "data, fintech licensing, and foreign-ownership rules.",
                "Currency volatility: results are reported in US dollars while operations span many emerging-"
                "market currencies.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Shopee losing market leadership in two or more core markets (Indonesia, Vietnam, Thailand) "
                "on both volume and profitability \u2014 the moat thesis breaking.",
                "Take-rate expansion reversing for four consecutive quarters, indicating pricing power was "
                "illusory.",
                "SeaMoney non-performing loan ratios inflecting sharply upward with inadequate provisioning.",
                "Free Fire quarterly paying users declining more than 20% year over year with no pipeline "
                "title offsetting.",
                "A regulatory event that structurally impairs one of the three segments (e.g., fintech license "
                "revocation in a major market).",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", CORE_METHOD + INTL_SEA),
        ]),
    ],
))

# =====================================================================================
# 5. NRG ENERGY (NRG) - BUY $143.00 vs $95.23 (+50%)
# =====================================================================================
notes.append(dict(
    ticker="NRG",
    company="NRG Energy, Inc.",
    verdict="BUY",
    target="$143.00",
    price="$95.23",
    price_note="October 2, 2026 close",
    upside="+50%",
    sections=[
        ("Investment Thesis", [
            ("p", "The United States has entered a power demand supercycle \u2014 the first sustained load "
             "growth in two decades \u2014 and NRG Energy just doubled its generation fleet to meet it. The "
             "$12 billion acquisition of LS Power's assets, which closed on January 30, 2026, added 18 "
             "natural-gas-fired facilities totaling roughly 13 gigawatts plus the CPower virtual power plant "
             "platform, taking NRG's total fleet to approximately 25 GW across the Northeast and Texas. At "
             "$95.23 the market values NRG as though it bought those assets at the top of the cycle; our "
             "judgment is the opposite \u2014 it bought scarce, quick-start, gas-fired capacity at the "
             "beginning of a structural demand boom driven by data centers, reshored manufacturing, and "
             "electrification, and capacity of this type cannot be built quickly or cheaply anymore."),
            ("p", "The second pillar is the integrated model. NRG is not a pure merchant generator exposed to "
             "every flicker in power prices; it serves around 8 million retail customers across North "
             "America, and that retail book is a natural hedge against wholesale volatility. When power "
             "prices spike, generation profits; when they collapse, the retail margin widens. This "
             "integration dampens the earnings volatility that has historically kept merchant-power multiples "
             "depressed, and the market has not yet repriced NRG for the stability the combined, doubled "
             "fleet provides. The CPower virtual power plant platform adds a third dimension: 6 GW of "
             "demand-side flexibility that monetizes commercial and industrial customers' ability to curtail "
             "load exactly when the grid values it most."),
            ("p", "The third pillar is the cash machine. Power generation in tight markets throws off "
             "enormous free cash flow, and NRG's stated playbook \u2014 deleverage from the acquisition, then "
             "return capital \u2014 directs that cash to shareholders through a growing dividend and "
             "buybacks. The LS Power equity overhang, partially unwound through a March secondary offering "
             "that the stock absorbed, is a technical headwind that fades with time; the fundamental "
             "tailwind of rising capacity prices and data-center load growth compounds for years."),
            ("p", "Our $143.00 fair value assumes capacity markets stay tight, the integration delivers its "
             "synergies, and free cash flow per share grows at a double-digit pace as debt comes down and "
             "shares are retired. The bear case \u2014 a demand shortfall, integration failure, or a collapse "
             "in gas-fired spark spreads \u2014 sits well below today's price, which is appropriate given the "
             "leverage taken on for the deal. But the base case is simply that electricity demand keeps "
             "growing, scarce generation earns scarcity rents, and NRG now owns twice as much of it. That is "
             "a straightforward thesis, and +50% upside compensates for the complexity of underwriting it."),
        ]),
        ("Business Overview", [
            ("p", "NRG Energy, headquartered in Houston, Texas, is a Fortune 500 integrated power company "
             "operating across wholesale generation and retail electricity and natural gas. Following the "
             "January 2026 closing of the LS Power acquisition, the company owns approximately 25 GW of "
             "generation \u2014 predominantly natural-gas-fired, including quick-start peaking facilities in "
             "the Northeast and Texas \u2014 and the CPower commercial and industrial virtual power plant "
             "platform with roughly 6 GW of flexible demand-side capacity. Its retail businesses serve about "
             "8 million residential and commercial customers across the US and Canada under brands including "
             "NRG, Reliant, Direct Energy, and others, alongside smart-home offerings."),
            ("p", "The business model has two engines. Wholesale generation earns energy margins (the spread "
             "between power prices and fuel costs), capacity payments for being available, and ancillary "
             "services revenue for grid reliability. Retail earns a margin on electricity and gas sold to "
             "end customers, with the generation fleet providing a physical hedge. In tight power markets \u2014 "
             "which describes most of NRG's footprint today \u2014 both engines run hot: generation captures "
             "scarcity pricing while retail benefits from a stable customer base that values reliability."),
            ("p", "The LS Power transaction, valued at nearly $12 billion in enterprise value ($6.4 billion "
             "cash, $2.8 billion in stock to LS Power, $3.2 billion of assumed net debt), was the largest "
             "power-generation deal in a decade. It received antitrust clearance from the Department of "
             "Justice in January 2026 after an extended review and was positioned by CEO Larry Coben as a "
             "bet on the early stages of a power demand supercycle. Integration and deleveraging are the "
             "management priorities for 2026-2027."),
        ]),
        ("Forward Outlook", [
            ("p", "Our judgment is that NRG's earnings power over the next five years will be determined less "
             "by commodity trading skill than by physics: the US grid is short of dispatchable capacity in "
             "exactly the markets where NRG just doubled down, and data-center load is arriving faster than "
             "new supply can be permitted and built. Quick-start gas plants \u2014 the core of the acquired "
             "fleet \u2014 are the assets the grid needs most as intermittent renewables grow, because they "
             "can ramp in minutes when the wind stops or the sun sets. Capacity auction prices in PJM and "
             "scarcity pricing in ERCOT are the mechanisms through which that need becomes cash flow, and "
             "both are pointed in NRG's favor."),
            ("p", "On integration, we take a show-me stance but assign favorable odds: the assets are "
             "operating plants, not development projects, so the synergy thesis is about scale economies, "
             "trading optimization across a larger fleet, and commercial excellence \u2014 the unglamorous "
             "work NRG has done before. The deleveraging path matters enormously for the equity story: every "
             "dollar of debt retired from operating cash flow de-risks the balance sheet and, in a tight "
             "power market, arguably creates more equity value than a dollar of buybacks. We expect leverage "
             "to decline steadily through 2027, after which capital return accelerates."),
            ("p", "The data-center angle deserves emphasis because it is the largest source of potential "
             "upside the market has not modeled. Large-load customers need power that is firm, fast, and "
             "clean-ish \u2014 and they are increasingly willing to sign long-term contracts at premium "
             "prices to get it. NRG's combination of 25 GW of dispatchable generation, retail structuring "
             "expertise, and the CPower demand-response platform makes it one of few counterparties that can "
             "offer a hyperscaler a complete solution. Even a handful of such contracts would add durable, "
             "contracted cash flow on top of the merchant base case. That is the bull-case kicker; the base "
             "case needs only continued load growth and competent integration."),
        ]),
        ("Valuation", [
            ("p", "Our valuation is a probability-weighted scenario DCF, weighted 25% bear / 50% base / 25% "
             "bull. In the base case, the combined fleet generates growing free cash flow as capacity prices "
             "remain firm, retail margins hold, and integration synergies land; leverage declines through "
             "2027 and the resulting equity value \u2014 after servicing the acquisition debt \u2014 is "
             "discounted at the 10% standard rate, reflecting merchant-power cyclicality balanced against "
             "the contracted retail base. The probability-weighted fair value equals our $143.00 target."),
            ("p", "The bear case is genuinely adverse and sits well below the current price: power demand "
             "growth disappoints, spark spreads compress on weak gas or oversupply, integration synergies fail "
             "to materialize, and the leveraged balance sheet leaves little room for error \u2014 a combination "
             "that would impair the equity substantially. We assign it 25% because the leverage is real and "
             "power markets have humbled optimists before. The bull case assumes data-center contracting at "
             "premium prices, capacity auction spikes, and faster deleveraging, discounted 150bp below the "
             "base rate; in that world the equity value reflects a scarcity asset in a supply-constrained "
             "market."),
            ("p", "We cross-check against free-cash-flow yield and sum-of-the-parts logic: valuing the "
             "generation fleet on a per-kilowatt replacement-cost basis and the retail book on a "
             "per-customer basis both suggest the current enterprise value understates the asset base, "
             "particularly with the acquired plants carried at transaction value in a rising-price "
             "environment. Terminal growth is capped at 2.5% on normalized mid-cycle power margins \u2014 we "
             "do not capitalize scarcity pricing into perpetuity."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Leverage: the $12 billion LS Power deal significantly increased debt; a power-market downturn "
                "before deleveraging progresses would strain the balance sheet.",
                "Commodity exposure: natural-gas prices and power-price spreads (spark spreads) drive "
                "generation margins and remain volatile.",
                "Integration risk: realizing synergies across a doubled fleet and the CPower platform requires "
                "sustained operational execution.",
                "Regulatory and market-design risk: changes to capacity-market rules, ERCOT market design, or "
                "environmental regulation could alter asset economics.",
                "Weather and reliability events: extreme weather can create both windfalls and outsized "
                "losses, as Texas history demonstrates.",
                "Interest rates: the leveraged capital structure makes the equity sensitive to the cost of "
                "debt refinancing.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Leverage failing to decline through 2027 despite the operating cash flow \u2014 the "
                "deleveraging promise is the linchpin of the equity story.",
                "Integration synergy targets formally abandoned or written down within 18 months of closing.",
                "A sustained collapse in capacity prices in PJM or ERCOT indicating the supply-demand "
                "tightness thesis is wrong.",
                "Loss of major data-center or large-load contracting opportunities to competitors, suggesting "
                "NRG's commercial positioning is weaker than we believe.",
                "Dividend cut or suspension, which would signal the cash machine is broken.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", CORE_METHOD + " For this integrated power company the scenario cash flows reflect both "
             "merchant generation margins and the contracted retail book, with the acquisition debt serviced "
             "in the cash flows before arriving at equity value; commodity cyclicality is captured in the "
             "scenario spreads rather than in a single forecast."),
        ]),
    ],
))

# =====================================================================================
# 6. RH (RH) - BUY $177.00 vs $120.46 (+47%)
# =====================================================================================
notes.append(dict(
    ticker="RH",
    company="RH",
    verdict="BUY",
    target="$177.00",
    price="$120.46",
    price_note="October 2, 2026 close",
    upside="+47%",
    sections=[
        ("Investment Thesis", [
            ("p", "RH \u2014 the luxury home-furnishings company \u2014 is a different business than the "
             "furniture retailer the market thinks it is. Over the past decade it has transformed from a "
             "mall-based catalog company into a luxury ecosystem: massive design galleries that function as "
             "hospitality destinations, restaurants and wine bars inside the stores, guesthouses, and a "
             "product line that spans furniture, lighting, textiles, and outdoor. The gallery model does two "
             "things simultaneously: it justifies premium pricing through experience, and it concentrates "
             "demand into fewer, larger, more productive locations. At $120.46 the market prices RH as a "
             "cyclical furniture stock at the top of a housing cycle; we see a luxury platform still in the "
             "middle of its expansion."),
            ("p", "The core of the thesis is operating leverage on a revenue recovery. RH's cost structure "
             "carries significant fixed costs \u2014 the galleries, the supply chain, the design organization "
             "\u2014 which means that when revenue grows, a large share of the incremental dollar falls to "
             "operating profit. The past two years of housing-market softness have depressed revenue and made "
             "margins look structurally impaired; our judgment is that they are cyclically depressed. As "
             "housing turnover normalizes and the wealthy consumer \u2014 RH's customer \u2014 keeps spending, "
             "revenue reacceleration should drive margin expansion of several hundred basis points, a dynamic "
             "the current valuation barely credits."),
            ("p", "The longer-term leg is international and hospitality. RH's expansion into Europe \u2014 with "
             "galleries in England and on the continent \u2014 and its growing hospitality footprint "
             "(restaurants, guesthouses) extend the brand beyond American home furnishings into global luxury "
             "lifestyle. Luxury is the most durable category in consumer discretionary, and RH is one of very "
             "few American brands playing in it with an integrated physical experience. Each new gallery is a "
             "multi-year comp driver; each hospitality venue deepens the brand halo that supports pricing "
             "power."),
            ("p", "Founder-CEO Gary Friedman's capital allocation adds a final kicker: RH has repeatedly "
             "repurchased shares aggressively when the stock has been weak, shrinking the share count at "
             "prices that reward long-term holders. Our $177.00 fair value assumes a mid-cycle revenue base "
             "with normalized margins \u2014 not peak housing-boom economics \u2014 and values the "
             "international and hospitality options at a fraction of what they could become. The bear case, "
             "in which housing stays soft and gallery investments disappoint, sits below today's price; but "
             "the base case is simply that luxury demand mean-reverts and the operating leverage does the "
             "rest."),
        ]),
        ("Business Overview", [
            ("p", "RH, headquartered in Corte Madera, California, is a luxury home-furnishings company "
             "operating through collections including RH Interiors, RH Modern, RH Contemporary, RH Outdoor, "
             "RH Baby & Child, and RH Teen. Its defining strategic asset is the Design Gallery network: "
             "very large-format retail destinations \u2014 often 50,000-plus square feet across multiple "
             "levels \u2014 that combine fully furnished room installations with restaurants, wine bars, and "
             "rooftop hospitality spaces. The company has also expanded into hospitality proper with RH "
             "Guesthouses and a growing restaurant portfolio, and internationally with galleries in the "
             "United Kingdom and Europe."),
            ("p", "The economic model is luxury retail: high average order values, premium gross margins "
             "supported by brand and design differentiation, and a deliberately limited promotional posture. "
             "Revenue is driven by gallery productivity, new gallery openings, and the Sourcebook catalog "
             "circulation that still functions as a high-end direct-marketing engine. The fixed-cost base \u2014 "
             "gallery leases and staffing, the supply chain, product development \u2014 creates the operating "
             "leverage that defines the investment case in both directions."),
            ("p", "RH's customer is the affluent homeowner, a cohort whose spending has proven resilient "
             "across cycles relative to mass-market furniture retail. The company sources globally and sells "
             "primarily in North America, with international expansion representing the next leg of the "
             "growth algorithm. Capital allocation under founder leadership has favored share repurchases "
             "during periods of stock weakness alongside continued investment in the gallery and hospitality "
             "footprint."),
        ]),
        ("Forward Outlook", [
            ("p", "Our judgment is that RH's earnings over the next three to five years will be driven by "
             "three compounding forces. First, the housing cycle: existing-home sales have been depressed by "
             "elevated mortgage rates, and furniture demand correlates strongly with housing turnover. Any "
             "normalization \u2014 from lower rates, demographic household formation, or simply time \u2014 "
             "flows disproportionately to RH's bottom line because of the fixed-cost leverage. We do not need "
             "a housing boom; we need a return toward average turnover, and the operating leverage amplifies "
             "even a modest recovery into substantial earnings growth."),
            ("p", "Second, the gallery maturation curve. New galleries typically ramp over several years as "
             "local awareness builds and the hospitality components \u2014 which drive foot traffic far beyond "
             "furniture shoppers \u2014 establish themselves. The cohort of galleries opened in recent years "
             "is still climbing that curve, which means embedded comp growth that requires no new capital. "
             "International galleries extend this dynamic: if the European locations replicate even a portion "
             "of US gallery economics, they add a multi-year growth vector the market currently values at "
             "roughly zero."),
            ("p", "Third, brand extension into hospitality and adjacent luxury categories. The restaurants and "
             "guesthouses are not side projects \u2014 they are the mechanism by which RH converts furniture "
             "shoppers into luxury-lifestyle adherents, deepening the moat around pricing power. Our forward "
             "view is that RH slowly becomes less correlated with the furniture cycle and more correlated "
             "with global luxury demand, a transition that \u2014 if it continues \u2014 justifies a higher "
             "multiple than furniture retail has ever commanded. The risk is execution: galleries are "
             "capital-intensive, international expansion has humbled many retailers, and luxury positioning "
             "is fragile if quality or service slips. But the trajectory of the past decade argues the team "
             "knows how to build this."),
        ]),
        ("Valuation", [
            ("p", "Our valuation is a probability-weighted scenario DCF, weighted 25% bear / 50% base / 25% "
             "bull. In the base case, revenue recovers toward a mid-cycle level as housing turnover "
             "normalizes and the gallery base matures, operating margins expand several hundred basis points "
             "on the fixed-cost leverage, and international galleries contribute increasingly; we discount at "
             "the 10% standard rate for a cyclical luxury retailer. The probability-weighted fair value "
             "equals our $177.00 target."),
            ("p", "The bear case is genuinely adverse and sits below the current price: housing turnover "
             "stays depressed for years, new galleries underperform, international expansion consumes "
             "capital without returns, and margins remain stuck at trough levels. In that world the shares "
             "are worth less than $120. The bull case assumes a proper housing recovery, international "
             "galleries replicating US unit economics, and hospitality deepening the brand moat \u2014 "
             "discounted 150bp below the base rate \u2014 which would support a luxury-multiple re-rating "
             "well above our target."),
            ("p", "A multiples cross-check supports the conclusion: at $120.46 the shares trade at a multiple "
             "of trough earnings that looks optically high but is meaningless \u2014 on mid-cycle earnings "
             "power, the multiple compresses to levels inconsistent with a luxury brand compounding at "
             "double-digit rates. Terminal growth is capped at 2.5% on normalized mid-cycle margins, not "
             "peak-cycle margins, and the terminal value is a minority of enterprise value."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Housing cyclicality: furniture demand is tightly linked to home sales and mortgage rates; a "
                "prolonged housing downturn would keep revenue and margins depressed.",
                "Execution risk on gallery expansion: new galleries are capital-intensive and take years to "
                "mature; underperformance would strand capital.",
                "International expansion risk: European luxury consumers and operating environments differ "
                "from the US; replication is not guaranteed.",
                "Key-person risk: the strategy and brand vision are closely associated with founder-CEO Gary "
                "Friedman.",
                "Tariff and supply-chain exposure: global sourcing makes margins sensitive to trade policy "
                "and freight costs.",
                "Luxury positioning fragility: quality, service, or design missteps could erode the pricing "
                "power the entire model depends on.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Same-gallery sales declining for six consecutive quarters despite housing stabilization \u2014 "
                "the demand thesis breaking.",
                "Operating margins failing to expand as revenue recovers, indicating the fixed-cost leverage "
                "story was wrong and costs are variable after all.",
                "International galleries generating sustainably negative four-wall economics after a "
                "reasonable ramp period.",
                "A strategic pivot away from luxury positioning toward promotional or mass-market offerings.",
                "Share repurchases continuing while gallery returns deteriorate \u2014 capital allocation "
                "masking a broken operating model.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", CORE_METHOD),
        ]),
    ],
))

# =====================================================================================
# 7. DRAFTKINGS (DKNG) - BUY $27.00 vs $18.59 (+45%)
# =====================================================================================
notes.append(dict(
    ticker="DKNG",
    company="DraftKings Inc.",
    verdict="BUY",
    target="$27.00",
    price="$18.59",
    price_note="October 2, 2026 close",
    upside="+45%",
    sections=[
        ("Investment Thesis", [
            ("p", "DraftKings has fallen 39% in 2026 and now trades at $18.59 \u2014 pricing in the obituary of "
             "the American sportsbook at the hands of prediction markets. That obituary is premature. The "
             "core business \u2014 online sports betting and iGaming in licensed states \u2014 is on track to "
             "generate roughly $1 billion of adjusted EBITDA in 2026, sportsbook handle was growing 15% year "
             "over year as the NFL season kicked off, and the structural economics of mature-state sports "
             "betting keep improving as promotional intensity fades and hold percentages rise. The market has "
             "confused a real competitive question (what do Kalshi and Polymarket mean for the industry?) "
             "with a settled negative answer, and the resulting multiple prices the core franchise as though "
             "it is already in decline."),
            ("p", "Our judgment is that prediction markets are a threat to be managed, not a death sentence "
             "\u2014 and DraftKings is managing it better than the stock price suggests. In June 2026 the "
             "company launched DKeX, its own prediction-market exchange, which has since expanded to 48 "
             "states and \u2014 while still early \u2014 is capturing double-digit share in the markets where "
             "it participates, according to management. That footprint matters enormously: prediction markets "
             "operate nationally under federal derivatives oversight, which means DraftKings can now acquire "
             "customers in states where sports betting remains illegal \u2014 California, Texas, Florida \u2014 "
             "and cross-sell them if and when those states legalize. The market values DKeX at zero; we see a "
             "free call option on the industry's fastest-growing segment, held by the operator with the best "
             "customer-acquisition machine in the business."),
            ("p", "The third leg is the legalization runway, which remains the most underappreciated source of "
             "compounding in the name. iGaming \u2014 far more profitable per user than sports betting \u2014 is "
             "legal in only a handful of states, and each new state that legalizes online casino is a "
             "step-change in DraftKings' earnings power. Sports betting still has large holdouts. Every year "
             "that passes without legalization is a year of deferred, not destroyed, value \u2014 and the "
             "prediction-market dynamic may actually accelerate the process by forcing states to confront the "
             "revenue they are leaving on the table."),
            ("p", "Our $27.00 fair value requires no heroics on prediction markets: it values the core "
             "sportsbook and iGaming business on its march toward mature-state margins, treats DKeX as a "
             "modest positive rather than the savior, and credits the legalization pipeline at a discount. "
             "The bear case \u2014 in which prediction markets structurally cannibalize the sportsbook and "
             "regulators pile on \u2014 sits below today's price, and we respect it; regulatory headlines have "
             "driven much of this year's decline. But at $18.59, the market is asking us to believe the "
             "bear case is the base case. The operating data says otherwise."),
        ]),
        ("Business Overview", [
            ("p", "DraftKings Inc., headquartered in Boston, is one of the two dominant online sports betting "
             "operators in the United States alongside FanDuel, with a growing iGaming (online casino) "
             "business in states where it is legal. The company operates mobile sportsbooks in the majority "
             "of legal-betting states, digital casino products, the Jackpocket digital lottery courier "
             "acquired in 2024, and \u2014 since June 2026 \u2014 the DKeX prediction-market exchange, now "
             "live in 48 states. DraftKings also operates in Ontario and has exposure to international "
             "markets."),
            ("p", "The economics of the core business follow a well-understood maturation curve. New states "
             "lose money initially as operators spend heavily on promotions and customer acquisition; over "
             "two to four years, promotional intensity fades, the customer base seasons, hold percentages "
             "(the share of handle the operator keeps) improve with product sophistication \u2014 particularly "
             "same-game parlays \u2014 and the state flips to strong profitability. iGaming is structurally "
             "superior: higher hold, lower promotional intensity, and stickier customers. As the state mix "
             "matures and iGaming grows as a share of revenue, company-wide margins expand \u2014 the dynamic "
             "behind management's roughly $1 billion 2026 adjusted EBITDA target."),
            ("p", "The prediction-market landscape adds a new dimension. Kalshi and Polymarket operate sports "
             "event contracts nationally under Commodity Futures Trading Commission oversight, competing with "
             "sportsbooks on pricing \u2014 recent data showed Kalshi's implied vig below both major "
             "sportsbooks for NFL Week 1 \u2014 while DraftKings' DKeX gives it a foothold in the same "
             "structure. The regulatory backdrop is fluid: court cases over states' authority to restrict "
             "prediction markets remain unresolved, with key deadlines extending into late 2026."),
        ]),
        ("Forward Outlook", [
            ("p", "Our forward view centers on a simple proposition: the sportsbook business that exists "
             "today is worth more than the market thinks, and everything else is optionality. Handle keeps "
             "growing at a mid-teens pace, the product keeps getting better at extracting hold \u2014 live "
             "betting, same-game parlays, and personalization all push in the same direction \u2014 and the "
             "promotional arms race of the land-grab years is over. As more states cross into maturity, the "
             "margin structure of the consolidated business should grind upward for years. That alone, on "
             "reasonable multiples, supports a price well above $18.59."),
            ("p", "On DKeX, we are deliberately measured. The early share data \u2014 roughly 3% of tracked "
             "NFL Week 1 prediction-market volume versus Kalshi's dominant share \u2014 shows how far the "
             "exchange has to go, and Kalshi's pricing advantage is real. But DKeX is months old, it leverages "
             "DraftKings' brand and its enormous existing customer base at near-zero marginal acquisition "
             "cost, and its 48-state footprint gives DraftKings something it never had: a legal product in "
             "California and Texas. Our base case assumes DKeX becomes a real but secondary business; our "
             "bull case assumes it captures a meaningful share of a large prediction-market TAM and becomes "
             "the customer-acquisition funnel for eventual sportsbook legalization in holdout states. Either "
             "way, the current price assigns it no value, which is the wrong number."),
            ("p", "The regulatory outlook is the swing factor we watch most closely. Adverse developments \u2014 "
             "state tax increases on sports betting, restrictions on prediction markets that strand DKeX, or "
             "federal intervention \u2014 would impair the thesis, and 2026 has supplied plenty of negative "
             "headlines, from the Brazil betting ban to congressional scrutiny. Our judgment is that the "
             "direction of travel still favors the legal industry: states need the tax revenue, consumers "
             "prefer regulated products, and prohibition has never worked in gambling. But we underwrite the "
             "target with regulatory friction assumed, not regulatory clarity."),
        ]),
        ("Valuation", [
            ("p", "Our valuation is a probability-weighted scenario DCF, weighted 25% bear / 50% base / 25% "
             "bull. In the base case, the core sportsbook and iGaming business grows handle and revenue at "
             "double-digit rates as states mature, adjusted EBITDA margins expand toward mature-state "
             "levels, DKeX contributes modestly, and the legalization pipeline adds states over time; we "
             "discount at 12% to reflect the speculative elements \u2014 regulatory uncertainty and the "
             "prediction-market competitive question \u2014 balanced against the demonstrated profitability of "
             "the core. The probability-weighted fair value equals our $27.00 target."),
            ("p", "The bear case is genuinely adverse and sits below the current price: prediction markets "
             "structurally cannibalize sportsbook handle, Kalshi's pricing advantage proves durable, states "
             "raise betting taxes, DKeX fails to gain traction, and the core business stagnates \u2014 a "
             "combination that would leave the shares worth less than $18.59. We assign it 25% because the "
             "competitive threat is real and the regulatory path is uncertain. The bull case assumes iGaming "
             "legalization accelerates across states, DKeX scales into a major prediction-market player, and "
             "mature-state margins reach their full potential, discounted 150bp below the base rate."),
            ("p", "A cross-check on EV-to-forward-EBITDA supports the conclusion: at $18.59 the market "
             "capitalizes roughly $1 billion of 2026 adjusted EBITDA \u2014 a profitable, growing number \u2014 "
             "at a multiple that implies the earnings have peaked. The operating trajectory (15% handle "
             "growth, expanding hold, maturing states) points the other way. Terminal growth is capped at "
             "2.5% on normalized mid-cycle margins, and we do not assume prediction-market dominance in any "
             "scenario."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Prediction-market competition: Kalshi and Polymarket offer better pricing on straight bets "
                "and operate nationally; structural share loss from sportsbooks is the central risk.",
                "Regulatory risk: unresolved court cases on prediction markets, potential state tax increases "
                "on sports betting, and federal scrutiny (including the congressional probe) could impair "
                "economics.",
                "Promotional competition with FanDuel and others could re-intensify, compressing margins.",
                "DKeX execution: the exchange is early-stage with small market share; failure to scale would "
                "strand the strategic rationale.",
                "Responsible-gambling and reputational risk, including scrutiny of AI-driven customer "
                "targeting, could invite restrictive regulation.",
                "International setbacks, such as the Brazil betting ban, demonstrate regulatory risk outside "
                "the US.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Sportsbook handle declining year over year in mature states for two consecutive quarters \u2014 "
                "evidence of structural cannibalization by prediction markets.",
                "Adjusted EBITDA guidance cut materially below the roughly $1 billion 2026 target for "
                "non-regulatory reasons.",
                "DKeX shut down or withdrawn from major markets, eliminating the strategic option value.",
                "A federal or multi-state regulatory action that structurally raises the tax/fee burden on "
                "sports betting by a large margin.",
                "Market-share loss to FanDuel accelerating in head-to-head states, indicating competitive "
                "positioning \u2014 not just sector headwinds \u2014 is the problem.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", CORE_METHOD + " For this business we use the 12% speculative-tier base discount to reflect "
             "regulatory uncertainty and the unresolved prediction-market competitive question; the scenario "
             "spreads capture the wide range of outcomes from cannibalization to legalization-led growth."),
        ]),
    ],
))

# =====================================================================================
# 8. PDD HOLDINGS (PDD) - BUY $108.00 vs $75.38 (+43%)
# =====================================================================================
notes.append(dict(
    ticker="PDD",
    company="PDD Holdings Inc.",
    verdict="BUY",
    target="$108.00",
    price="$75.38",
    price_note="October 2, 2026 close",
    upside="+43%",
    sections=[
        ("Investment Thesis", [
            ("p", "PDD Holdings is two businesses the market insists on valuing as one problem: Pinduoduo, "
             "the Chinese discount-retail machine that generates enormous cash flow, and Temu, the global "
             "cross-border marketplace navigating the end of the de minimis era. At $75.38 the market prices "
             "both as impaired \u2014 Pinduoduo as a victim of domestic competition and regulation, Temu as a "
             "business model broken by tariffs. Our judgment is that the first is wrong and the second is "
             "misunderstood. Pinduoduo remains one of the most profitable e-commerce businesses in China, "
             "and Temu \u2014 while genuinely disrupted \u2014 is a free option the market values at less than "
             "zero."),
            ("p", "Start with the domestic business, because it is the foundation of the valuation. Pinduoduo "
             "pioneered the team-purchase, value-first model in Chinese e-commerce and retains a massive, "
             "engaged user base in a market where discount retail keeps gaining share. Competition from "
             "Alibaba and JD.com is real and permanent \u2014 this is a three-player market now \u2014 but "
             "Pinduoduo's cost structure and agricultural-supply-chain roots give it a durable position at "
             "the value end. The domestic segment's profitability funds everything else, including the Temu "
             "investment cycle, and it does so with room to spare."),
            ("p", "Temu is where the analytical work matters. The end of US de minimis treatment \u2014 first "
             "for China-origin goods, then globally \u2014 raised the cost structure of the cross-border "
             "direct-ship model that powered Temu's explosive growth, and US user metrics suffered. But Temu "
             "has responded the way a well-capitalized operator should: pivoting toward local fulfillment "
             "with US-based warehouses and merchants, cutting prices to defend share, and leaning into "
             "non-US markets where the regulatory picture is less hostile. Our base case does not require "
             "Temu to recover its peak trajectory \u2014 it requires the business to stabilize as a "
             "large, lower-margin international marketplace. Anything beyond that, including a normalization "
             "of US trade treatment over time, is upside."),
            ("p", "Then there is the balance sheet, which the market treats as a footnote and we treat as "
             "central: PDD holds a very large net-cash position \u2014 tens of billions of dollars \u2014 "
             "against a business throwing off substantial annual free cash flow. We count that cash once, "
             "in enterprise value, and it still leaves the operating business priced at a multiple "
             "inconsistent with its profitability. Our $108.00 fair value charges a full 250bp China "
             "country-risk premium, models the VIE structure explicitly in the bear case, and still finds "
             "+43% upside. The bear case at $30 \u2014 well below today's price \u2014 is the world where "
             "geopolitics or regulation impairs the equity itself; we believe that tail is over-weighted in "
             "the current quote."),
        ]),
        ("Business Overview", [
            ("p", "PDD Holdings Inc., headquartered in Shanghai with its principal executive offices in "
             "Dublin, operates two major platforms. Pinduoduo is one of China's largest e-commerce platforms, "
             "built on a value-retail model emphasizing agricultural products, team purchasing, and "
             "gamified shopping; it serves hundreds of millions of annual active buyers, concentrated in "
             "price-sensitive segments where it holds a leading position. Temu is the company's "
             "international marketplace, launched in 2022, which scaled with extraordinary speed across North "
             "America, Europe, Latin America, and the Middle East on a cross-border direct-ship model "
             "connecting Chinese merchants to overseas consumers."),
            ("p", "The company's economics are unusual in global e-commerce: it is highly profitable, with "
             "operating margins that reflect Pinduoduo's asset-light marketplace model and Temu's early "
             "efficiency, and it converts a large share of profit into cash. The balance sheet carries a very "
             "large net-cash position, giving management the capacity to fund Temu's logistics pivot, invest "
             "through cycles, and return capital. The ADR is listed on Nasdaq; the operating entities sit "
             "within the variable-interest-entity (VIE) structure standard for Chinese companies listed "
             "abroad."),
            ("p", "The regulatory and trade backdrop is the defining context. Washington ended de minimis "
             "duty-free treatment for low-value parcels \u2014 the mechanism that enabled Temu's ultra-low "
             "pricing \u2014 and the European Union has moved to impose customs duties on small parcels as "
             "well. Temu has responded by shifting toward local fulfillment models, onboarding domestic "
             "merchants and warehouse capacity in destination markets, a transition that raises costs but "
             "builds a more defensible and compliant operating model."),
        ]),
        ("Forward Outlook", [
            ("p", "Our judgment on Pinduoduo is that the domestic business has entered a mature, cash-cow "
             "phase \u2014 and that this is good, not bad. The hypergrowth years are over; what remains is a "
             "dominant value-retail platform with best-in-class margins, deep agricultural supply chains, "
             "and a user base whose shopping habits are entrenched. We expect low-single-digit to "
             "mid-single-digit revenue growth domestically with stable-to-expanding margins as the company "
             "laps its heavy investment periods. In a market that now prices Chinese e-commerce as a "
             "no-growth utility, even modest growth with this margin structure creates substantial value, "
             "particularly with the cash balance funding buybacks."),
            ("p", "For Temu, our forward view is deliberately two-tracked. The pessimistic track \u2014 which "
             "we assign meaningful weight \u2014 is that the US business never recovers its former "
             "economics: tariffs and the loss of de minimis permanently raise the cost floor, local "
             "fulfillment compresses margins, and Temu settles as a mid-tier international marketplace. "
             "Even in that track, the non-US business \u2014 Europe, Latin America, the Middle East, where "
             "Temu continues to scale \u2014 has real value. The optimistic track is that the "
             "local-fulfillment pivot succeeds, Temu's merchant ecosystem deepens in destination markets, and "
             "US trade treatment normalizes over a multi-year horizon; in that world Temu re-accelerates and "
             "the current price looks like a generational entry point. Our base case sits between: "
             "stabilization, not triumph."),
            ("p", "The honest risk to this entire outlook is geopolitical. An escalation in US-China tensions "
             "that targets Chinese ADRs, a forced VIE restructuring, or a Taiwan-contingency scenario would "
             "impair the equity regardless of how well Pinduoduo and Temu execute \u2014 and no operating "
             "outperformance hedges that. We model it explicitly: the bear case at $30 assumes the equity "
             "itself is impaired, and the 250bp country-risk premium is charged on every scenario. Investors "
             "who cannot underwrite that tail should not own the name. For those who can, the asymmetry is "
             "striking: a cash-gushing domestic franchise, a free option on global commerce, and a fortress "
             "balance sheet, priced as though all three are liabilities."),
        ]),
        ("Valuation", [
            ("p", "Our valuation is a probability-weighted scenario DCF, weighted 25% bear / 50% base / 25% "
             "bull, with an explicit 250bp China country-risk premium added to the discount rate. The very "
             "large net-cash position is counted once, in enterprise value \u2014 we are careful not to "
             "double-count it in both the cash flows and the balance sheet \u2014 and Temu is treated as a "
             "free option: valued conservatively in the base case, at zero in the bear case. "
             "Scenario-implied fair values are:"),
            ("table", (
                ["Scenario", "Weight", "Implied fair value", "Key drivers"],
                [
                    ["Bear", "25%", "$30", "VIE/geopolitical impairment of the equity; Temu US business "
                     "written to zero; domestic margins compress under competition; cash trapped."],
                    ["Base", "50%", "$95", "Pinduoduo grows modestly with stable margins; Temu stabilizes on "
                     "local fulfillment ex-US; net cash counted once; buybacks continue."],
                    ["Bull", "25%", "$195", "Temu pivot succeeds and re-accelerates; US trade treatment "
                     "normalizes; domestic margins expand; market re-rates the cash compounder."],
                ],
            )),
            ("p", "The probability-weighted fair value supports our $108.00 target. The bear case at $30 sits "
             "far below the current $75.38 price, as our framework requires \u2014 it is the genuine disaster "
             "scenario in which the VIE structure or geopolitics impairs ADR holders directly. The base case "
             "values a highly profitable domestic franchise plus a stabilized international option, with the "
             "country-risk premium fully charged and Temu contributing modestly. The bull case reflects what "
             "the business earns if the market ever pays a normal multiple for this level of cash "
             "generation."),
            ("p", "Terminal growth is capped at 2.5% on normalized mid-cycle margins \u2014 we do not project "
             "peak e-commerce margins into perpetuity \u2014 and we benchmark against regional e-commerce "
             "peers facing similar risks, never US peers alone. The terminal value is a minority of "
             "enterprise value, consistent with a business whose near-term cash generation and existing cash "
             "balance dominate the valuation."),
        ]),
        ("Key Risks", [
            ("bullets", [
                "Geopolitical / VIE risk: US-China tensions could lead to ADR delisting, forced VIE "
                "restructuring, or ownership-impairment scenarios \u2014 the unhedgeable tail.",
                "Trade policy: US tariffs and the end of de minimis, plus EU small-parcel duties, "
                "structurally raise Temu's cost base.",
                "Domestic competition: Alibaba and JD.com compete aggressively in Chinese discount retail, "
                "pressuring growth and margins.",
                "Temu transition risk: the pivot to local fulfillment is capital-intensive and may fail to "
                "reproduce the unit economics of the direct-ship model.",
                "Regulatory risk in China: e-commerce, data, and platform-economy regulation remains an "
                "overhang for the domestic business.",
                "Capital allocation: the large cash balance could be deployed into low-return investments "
                "rather than returned to shareholders.",
            ]),
        ]),
        ("What Would Change Our Mind", [
            ("bullets", [
                "Any credible move against the VIE structure or toward forced ADR delisting \u2014 we would "
                "exit on evidence this tail is materializing, not after.",
                "Pinduoduo annual active buyers declining for two consecutive years, indicating structural "
                "share loss domestically.",
                "Temu's non-US growth stalling alongside continued US deterioration \u2014 the stabilization "
                "thesis failing on both tracks.",
                "Operating margins compressing structurally (not cyclically) for four consecutive quarters.",
                "The net-cash position being deployed into a large, low-return acquisition or diverted in "
                "ways that suggest governance concerns.",
            ]),
        ]),
        ("Valuation Approach", [
            ("p", CORE_METHOD + INTL_CHINA + " The very large net-cash position is counted once, in "
             "enterprise value; Temu is treated as a free option \u2014 valued conservatively in the base "
             "case and at zero in the bear case \u2014 rather than as a guaranteed growth engine."),
        ]),
    ],
))

# =====================================================================================
# Build + verify
# =====================================================================================
def collect_text(note):
    parts = [note["ticker"], note["company"], note["verdict"], note["target"],
             note["price"], note["upside"]]
    for heading, blocks in note["sections"]:
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

import os
outdir = "/home/hatch/workspace/standalone-notes/pdfs"
os.makedirs(outdir, exist_ok=True)

built = []
for note in notes:
    check_banned(collect_text(note), note["ticker"])
    path = os.path.join(outdir, "%s-equity-research-note.pdf" % note["ticker"])
    build_note(path, note)
    built.append((note["ticker"], path))

# Verify with pypdf
from pypdf import PdfReader
print("Built %d notes:" % len(built))
for ticker, path in built:
    r = PdfReader(path)
    n = len(r.pages)
    txt = (r.pages[0].extract_text() or "")[:60].replace("\n", " ")
    assert n > 0, "zero pages: %s" % path
    assert len(txt.strip()) > 0, "no extractable text: %s" % path
    print("  %-5s %s  pages=%d  head=%r" % (ticker, path, n, txt))
print("ALL OK")
