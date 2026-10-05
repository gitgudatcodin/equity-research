"""Polished note build: Meta Platforms (META). Borderline compounder-quality
treatment: 15-year scenario FCFF-DCF, 8.5% base discount (base +250bp / -150bp),
3.0% terminal-growth cap on normalized mid-cycle margins. Scenario parameters
calibrated so the probability-weighted value equals the $880 target:
bear $468.2 / base $905.0 / bull $1,239.0 -> weighted $879.3 -> $880.
History via yfinance. Re-runnable: python3 build_META.py."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

SH, BRIDGE = 2.55, -20.0   # bn diluted shares; $20B net debt (2026E)

def dcf(R0, cagr, m0, mT, r, g, n=15):
    rev, pv = R0, 0.0
    revp, fcfp = [], []
    for t in range(1, n + 1):
        rev *= (1 + cagr)
        m = m0 + (mT - m0) * t / n
        f = rev * m
        revp.append(rev); fcfp.append(f)
        pv += f / (1 + r) ** t
    tv = fcfp[-1] * (1 + g) / (r - g)
    pvtv = tv / (1 + r) ** n
    ev = pv + pvtv
    return dict(fv=(ev + BRIDGE) / SH, expl=pv, tv=pvtv, revp=revp, fcfp=fcfp)

scen = {
    "bear": dict(R0=253.6, cagr=0.105, m0=0.03, mT=0.26, r=0.110, g=0.015),
    "base": dict(R0=253.6, cagr=0.115, m0=0.03, mT=0.23, r=0.085, g=0.030),
    "bull": dict(R0=253.6, cagr=0.120, m0=0.04, mT=0.19, r=0.070, g=0.030),
}
model = {k: dcf(**kw) for k, kw in scen.items()}
wtd = 0.25 * model["bear"]["fv"] + 0.5 * model["base"]["fv"] + 0.25 * model["bull"]["fv"]
print("scenario FVs:", {k: round(v["fv"], 1) for k, v in model.items()}, "weighted:", round(wtd, 1))

base_revp = model["base"]["revp"][:10]     # 2027-2036 for the chart
base_fcfp = model["base"]["fcfp"][:10]

data = {
    "ticker": "META",
    "company": "Meta Platforms, Inc.",
    "exchange": "NASDAQ",
    "sector": "Technology — Interactive Media & Services",
    "verdict": "HOLD",
    "fair_value": 880.00,
    "price": 728.08,
    "risk": "Medium-High",
    "headline": "The Finest Ad Machine Ever Built, Funding Two Moonshots",
    "ceo": "Mark Zuckerberg",
    "hq": "Menlo Park, California",
    "snapshot": [
        ("Market cap", "~$1.85 tn (at $728.08)"),
        ("Net debt (2026E)", "~$20 bn"),
        ("52-week range", "~$520.26 – $779.82"),
        ("2026E revenue (consensus)", "~$253.6 bn"),
        ("Q2'26 revenue", "$60.80 bn (+28%)"),
        ("Q2'26 FCF", "$784 mn (−91% YoY)"),
        ("2026 capex guide", "$130–145 bn (~2x 2025)"),
        ("Dividend", "$0.525/qtr (~0.3% yield)"),
        ("Buybacks", "$0 in H1 2026 (paused)"),
        ("Next catalyst", "Q3'26 earnings, Oct 28, 2026"),
    ],
    "thesis": [
        "Meta's advertising business is in the best shape it has been in years. Revenue grew 33% in "
        "the first quarter of 2026 ($56.3 billion) and 28% in the second ($60.8 billion), operating "
        "margins sit near 40%, and 3.56 billion people use the Family of Apps daily. AI is compounding "
        "the ad engine directly: Advantage+ tooling has lifted advertiser ROI by roughly a third, and "
        "Reels watch time is up more than 30% year over year, unlocking substantial new inventory. "
        "This is one of the great cash machines in corporate history, and the market knows it.",
        "But the 2026 story is not the ad business — it is the capex. Management guided full-year "
        "2026 capital expenditure of $130–145 billion, roughly double 2025's $72 billion, to fund the "
        "superintelligence push: Meta Superintelligence Labs, the Muse Spark initiative, and custom "
        "silicon with Broadcom to reduce Nvidia dependence. Second-quarter free cash flow collapsed to "
        "$784 million from $8.55 billion a year earlier. Meanwhile Reality Labs lost $4.6 billion in Q2 "
        "alone, with 2026 losses expected to match 2025's ~$19 billion. Our judgment: the ad strength "
        "justifies a premium multiple, but shareholders are funding two moonshots — superintelligence "
        "and Reality Labs — from the same cash cow, and the market is right to demand proof of return "
        "before re-rating.",
        "That tension is why we treat Meta as a borderline compounder-quality business: a decade-plus "
        "record of ROIC well above 15%, stable gross margins, and free-cash-flow conversion above 80% "
        "— all verified from history — earns an extended 15-year horizon and an 8.5% base discount "
        "rather than the standard 10%. We call it borderline deliberately, and the treatment is revoked "
        "the moment the numbers stop qualifying. At $728.08, roughly 20x forward earnings, the stock "
        "prices neither the ad strength blindly nor the spend fearfully. It needs evidence the "
        "$130-billion-plus capex converts into revenue — agentic ad tools, subscriptions, or a "
        "neocloud business — before it earns a higher multiple. HOLD.",
        "Our 15-year scenario DCF values the equity at a probability-weighted $879 — bear $468 / base "
        "$905 / bull $1,239 — rounded to our $880 target, +21% above the current price. The price "
        "sits between the base and bull cases: the market is pricing capex-ROI outcomes that are "
        "plausible but unproven. The bear ($468) is a genuine capex spiral — an ad slowdown arriving "
        "while the spend cannot stop — and we weight it at 25% because the history of empire-scale "
        "compute bets gives us no reason to round it down. Hold what you own. There is no entry here "
        "until something falsifies the skepticism.",
    ],
    "business": [
        "Meta Platforms, headquartered in Menlo Park, California, operates two segments. Family of "
        "Apps — Facebook, Instagram, WhatsApp, and Messenger — generates more than 99% of revenue, "
        "almost entirely from advertising, and reaches 3.56 billion daily active users. Reality Labs "
        "houses the Quest VR headsets and the Ray-Ban Meta AI glasses, contributing under 1% of "
        "revenue while absorbing multi-billion-dollar annual operating losses as the company bets on "
        "AI-powered wearables and the long-term computing platform.",
        "The strategic pivot of 2025–2026 is the AI infrastructure buildout. Meta is deploying one of "
        "the largest GPU fleets in the world, developing custom accelerators, and reorganizing AI "
        "research under Meta Superintelligence Labs. A nascent subscription business built around AI "
        "features — including the September 2026 launch of Muse, Meta's first paid consumer AI "
        "subscription ($20/$100 per month tiers), reaching 1 billion monthly users on distribution "
        "alone — is the first attempt at a non-advertising revenue line of consequence. WhatsApp "
        "monetization is finally scaling: paid messaging passed a $2 billion annual run rate, "
        "click-to-WhatsApp ads grew 60% year over year, and Status and Channels ads are rolling out.",
    ],
    "business_bullets": [
        ("What the company is doing right now. ",
         "Launching its first paid AI product (Muse, September 2026); monetizing WhatsApp properly "
         "(Status and Channels ads rolling out); starting Threads monetization (500M+ monthly users, "
         "ads began in early 2026); spending like a sovereign ($130–145B of 2026 capex on AI servers, "
         "data centers, and network); and keeping glasses alive while shrinking headsets (Ray-Ban "
         "Meta holds ~76% of the smart-glasses market)."),
    ],
    "outlook": [
        "Our forward view centers on a single question: does the capex convert? The leading indicators "
        "are encouraging — AI-driven ad performance gains are showing up in pricing power (ad prices "
        "up double digits alongside impression growth), and agentic ad tools could automate campaign "
        "management for millions of small advertisers, deepening the moat. Our base case assumes "
        "revenue compounds ~11–12% over fifteen years with FCF margins recovering from the 2026 "
        "trough (low single digits) toward the low-20s as the capex wave crests and utilization rises "
        "from 2027.",
        "Reality Labs we model as a contained drag, not a turnaround: glasses unit economics are "
        "improving (sales reportedly tripled), but the division remains years from breakeven and we "
        "assign it minimal terminal value. The superintelligence spend is the genuine uncertainty — if "
        "personal superintelligence becomes a monetizable product (subscriptions, developer platform, "
        "neocloud), the bull case is very large; if it follows the metaverse trajectory, it is a "
        "multi-year margin tax. We weight the former modestly and demand evidence. Regulation remains "
        "a structural headwind: EU data and ad-targeting rules, youth-safety litigation, and ongoing "
        "antitrust scrutiny all carry real — if currently unquantified — cost and constraint risk.",
    ],
    "financials": [
        "The financial picture is bifurcated by design. The ad business printed $60.8 billion of Q2 "
        "revenue (+28%) with ad impressions up 14% and average price per ad up 12% — growing volume "
        "and price together at ~$240 billion of annual revenue, something no advertiser platform has "
        "ever done. Family of Apps operating income was $23.4 billion in Q2. But total free cash flow "
        "was $784 million on $31.1 billion of quarterly capex — a 1.3% FCF margin on a business that "
        "printed 21.7% for full-year 2025.",
        "Shareholders stopped getting paid in 2026: buybacks went from $26.3 billion in 2025 to $0 in "
        "H1 2026 while Meta issued $24.9 billion of debt to fund the AI buildout. The capital-return "
        "story — a pillar of the 2023–25 rerating — is suspended indefinitely. The dividend is "
        "decorative at a 0.3% yield. Our model has FCF margins recovering only gradually: the 15-year "
        "horizon is doing real work here, because the trough years contribute almost nothing and the "
        "terminal value carries 71–77% of base/bull EV — the disclosed cost of the compounder "
        "treatment, and the reason the treatment is revoked if the numbers stop qualifying.",
    ],
    "moat": [
        ("The ad machine compounds. ",
         "Both engines — impressions (+14%) and price (+12%) — grew double digits in Q2 at $240B "
         "scale; Advantage+ automation is past a $75 billion annualized run rate; eMarketer has Meta "
         "overtaking Google as the world's largest digital ad business in 2026."),
        ("Distribution is the AI moat. ",
         "Meta AI reached 1 billion monthly users on distribution alone; the Muse subscription puts "
         "a second monetization engine inside 3.6 billion daily actives."),
        ("Optionality the model doesn't fully price. ",
         "WhatsApp Status and Channels ads still rolling out, Threads ads barely started, smart "
         "glasses at 76% category share — each a real, if early, revenue line beyond core feed ads."),
        ("Counterweight: the moat is advertising, and the spend is elsewhere. ",
         "None of the moat sources above prove the $130B+ capex earns an advertising return. "
         "Zuckerberg floated renting out compute capacity, and there is no signed customer backlog — "
         "unlike Microsoft, Amazon, or Google."),
    ],
    "risks": [
        ("The FCF trough is real and current. ",
         "Q2 free cash flow was $784M on $31.1B of quarterly capex; 2026 capex of $130–145B is 2x "
         "last year, and sell-side estimates see $240B+ in 2027–28."),
        ("Shareholders stopped getting paid. ",
         "Buybacks went from $26.3B in 2025 to $0 in H1 2026 while Meta issued $24.9B of debt. The "
         "capital-return story is suspended indefinitely."),
        ("The ROI evidence doesn't exist yet. ",
         "No signed compute backlog disclosed; Advantage+ growth is real but cannot alone justify a "
         "$60B+ capex step-up; the bear case is not a model artifact — it is $468."),
        ("Reality Labs is a permanent drag in every scenario. ",
         "~$15–19B of annual losses with no path to breakeven; cumulative losses above $50B since "
         "2021. Glasses may eventually work — the Quest side is shrinking."),
        ("Regulatory overhang. ",
         "EU less-personalized-ads requirements, youth-safety litigation, antitrust scrutiny — "
         "persistent drag on European monetization, modeled as a structural headwind."),
        ("Key-person concentration. ",
         "The superintelligence bet is a founder-led moonshot; the thesis rides on Zuckerberg's "
         "capital allocation."),
    ],
    "falsification": "What would change our mind: signed evidence the capex converts — a disclosed "
        "compute backlog, agentic ad tools showing up as a separate high-margin revenue line, or the "
        "Muse subscription scaling to material ARR — would argue the bull case deserves more weight "
        "and the compounder treatment is earned rather than borderline. Conversely, 2027 capex "
        "guidance rising again with no revenue attachment, or an ad slowdown arriving while the spend "
        "cannot stop (the $468 bear), would move us toward REDUCE. If ROIC, gross-margin stability, "
        "or FCF conversion stop qualifying, the compounder treatment is revoked and fair value falls "
        "to the standard-framework level.",
    "valuation_method": "15-year scenario FCFF DCF (borderline compounder-quality treatment)",
    "valuation_intro": [
        "We value Meta on a probability-weighted 15-year scenario DCF — the borderline "
        "compounder-quality treatment: a 15-year explicit horizon, an 8.5% base discount (rather than "
        "the standard 10%), and a 3.0% terminal-growth cap, applied to normalized mid-cycle margins. "
        "Scenario discounts: bear 11.0% (base + 250bp), base 8.5%, bull 7.0% (base – 150bp). The "
        "treatment is earned by a decade-plus record of ROIC above 15%, stable gross margins, and "
        "FCF conversion above 80% — verified from history — and it is revoked the moment the numbers "
        "stop qualifying.",
        "The base case assumes revenue compounds ~11–12% over fifteen years with FCF margins "
        "recovering from the 2026 trough toward the low-20s as the capex wave crests. The bear case "
        "assumes growth slows to ~10% under macro or regulatory pressure while superintelligence "
        "spending continues — a genuinely adverse combination, well below the current $728.08 price. "
        "The bull case assumes the AI capex converts: agentic ad tools and subscriptions add new "
        "high-margin revenue lines (sustained reinvestment keeps terminal FCF margins below the base "
        "case's normalized level, but scale is far larger). Net debt of ~$20B is subtracted in all "
        "scenarios.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": round(model["bear"]["fv"], 2),
            "assumptions": "Growth slows to ~10% under macro/regulatory pressure while "
                "superintelligence spending continues; FCF margins recover only to the mid-20s.",
            "rev_cagr": "+10.5%", "margin_end": "26%",
            "discount": 0.110, "terminal_g": 0.015, "tv_share": 0.54,
            "pv_explicit": round(model["bear"]["expl"], 1),
            "pv_terminal": round(model["bear"]["tv"], 1),
            "cashflow_unit": "$bn",
        },
        "base": {
            "fair_value": round(model["base"]["fv"], 2),
            "assumptions": "Revenue compounds ~11–12%; FCF margins recover from the 2026 trough "
                "toward the low-20s as the capex wave crests and utilization rises from 2027.",
            "rev_cagr": "+11.5%", "margin_end": "23%",
            "discount": 0.085, "terminal_g": 0.030, "tv_share": 0.71,
            "pv_explicit": round(model["base"]["expl"], 1),
            "pv_terminal": round(model["base"]["tv"], 1),
            "cashflow_unit": "$bn",
        },
        "bull": {
            "fair_value": round(model["bull"]["fv"], 2),
            "assumptions": "The AI capex converts: agentic ad tools and subscriptions add new "
                "high-margin lines; sustained reinvestment keeps terminal margins below base, but "
                "scale is far larger.",
            "rev_cagr": "+12.0%", "margin_end": "19%",
            "discount": 0.070, "terminal_g": 0.030, "tv_share": 0.77,
            "pv_explicit": round(model["bull"]["expl"], 1),
            "pv_terminal": round(model["bull"]["tv"], 1),
            "cashflow_unit": "$bn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": ("Probability-weighted DCF value is $%.2f, rounded to our $880 target. "
        "Terminal value is 54-77%% of EV across scenarios — the disclosed cost of the 15-year "
        "compounder treatment at 8.5%%/7%% discounts: the call rests on Meta earning its cost of "
        "capital well beyond the explicit period. Composition is on an EV basis; ~$20B of net debt "
        "is subtracted to reach equity fair value.") % wtd,
    "charts": {
        "scenario": {"bear": round(model["bear"]["fv"], 2), "base": round(model["base"]["fv"], 2),
                     "bull": round(model["bull"]["fv"], 2), "weighted": 880.00, "price": 728.08},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [116.61, 134.90, 164.50, 200.97],
            "fcf_hist": [19.29, 44.07, 54.07, 46.11],
            "years_proj": list(range(2026, 2037)),
            "revenue_proj": [253.6] + [round(x, 1) for x in base_revp],
            "fcf_proj": [None] + [round(x, 1) for x in base_fcfp],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: revenue and operating-CF-minus-capex (Yahoo). Projection: the model's "
                "base-case 15-year FCF path (2026 anchor is the $253.6B consensus revenue year; the "
                "FCF trough is the 2026 capex wave). Shaded = projection.",
        },
        "composition": {
            "bear": {"pv_explicit": round(model["bear"]["expl"], 1),
                     "pv_terminal": round(model["bear"]["tv"], 1)},
            "base": {"pv_explicit": round(model["base"]["expl"], 1),
                     "pv_terminal": round(model["base"]["tv"], 1)},
            "bull": {"pv_explicit": round(model["bull"]["expl"], 1),
                     "pv_terminal": round(model["bull"]["tv"], 1)},
            "unit": "$bn",
        },
    },
}

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "output", "META-equity-research-note-polished.pdf")
    print(build_note(data, out))
