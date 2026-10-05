"""Polished note build: UiPath (PATH). Scenario numbers from the hardened
10-year scenario FCFF-DCF model (path-research/valuation_v2.py):
bear $6.79 / base $13.21 / bull $20.84, weighted $13.51 -> $13.50 target;
discounts 14.5%/12.0%/10.5%, terminal g 1.5%/2.5%/2.5%, TV/EV 28.9%/48.9%/58.5%.
PV composition and the base-case projection path are re-derived by running the
model's own parameters. History via yfinance.
Re-runnable: python3 build_PATH.py."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note
import runpy, io, contextlib

buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    ns = runpy.run_path(os.path.expanduser("~/workspace/path-research/valuation_v2.py"))

REV_27, FCFM_27 = ns["REV_27"], ns["FCFM_27"]
COMP = {}
for k, (g, m_end, wacc, tg, fv) in {
    "bear": (ns["bear_g"], 0.26, 0.145, 0.015, 6.79),
    "base": (ns["base_g"], 0.30, 0.120, 0.025, 13.21),
    "bull": (ns["bull_g"], 0.33, 0.105, 0.025, 20.84),
}.items():
    rev, pv, n = REV_27, 0.0, len(g)
    revp, fcfp = [], []
    for i, gr in enumerate(g):
        rev *= (1 + gr)
        m = FCFM_27 + (m_end - FCFM_27) * (i + 1) / n
        f = rev * m
        revp.append(rev); fcfp.append(f)
        t = i + 1
        pv += f / (1 + wacc) ** t
        if i == n - 1:
            pvtv = f * (1 + tg) / (wacc - tg) / (1 + wacc) ** t
    COMP[k] = {"expl": round(pv, 2), "tv": round(pvtv, 2),
               "revp": revp, "fcfp": fcfp, "fv": fv}

base_revp = [round(x, 2) for x in COMP["base"]["revp"]]
base_fcfp = [round(x, 2) for x in COMP["base"]["fcfp"]]

data = {
    "ticker": "PATH",
    "company": "UiPath, Inc.",
    "exchange": "NYSE",
    "sector": "Technology — Enterprise Software / Automation",
    "verdict": "HOLD",
    "fair_value": 13.50,
    "price": 13.12,
    "risk": "Medium-High",
    "headline": "Stabilization Is Not Reacceleration — Waiting for Proof",
    "ceo": "Daniel Dines",
    "hq": "New York, New York",
    "snapshot": [
        ("Market cap", "~$6.8 bn (at $13.12)"),
        ("Net cash", "~$1.33 bn (~$2.50/share; ~19% of mkt cap)"),
        ("52-week range", "~$9.20 – $19.84"),
        ("FY2026 revenue", "$1.61 bn (+13%)"),
        ("Q3 FY26 (Oct 2025)", "First GAAP-profitable Q3: $13 mn op. income"),
        ("Non-GAAP gross margin", "~85%"),
        ("FY27E revenue guide", "$1.789–1.794 bn (haircut in model)"),
        ("Index", "S&P MidCap 400 (added Dec 2025)"),
        ("Founder ownership", "Dines ~20%"),
        ("Next catalyst", "Q4 FY26 earnings; Maestro adoption data"),
    ],
    "thesis": [
        "The existential question that has hung over UiPath — do large language models make robotic "
        "process automation obsolete? — has been answered, at least for now: agents need a body. AI "
        "agents can reason and plan, but someone still has to click the buttons inside legacy "
        "enterprise systems, and UiPath's robots — now paired with Maestro, its orchestration layer "
        "for governing fleets of agents from any vendor — are the most deployed such body in the "
        "enterprise. Founder Daniel Dines returning as CEO in mid-2024 and the December 2025 "
        "inclusion in the S&P MidCap 400 mark the company's rehabilitation from its post-IPO "
        "wilderness.",
        "Our judgment: the agentic pivot is credible and the numbers are stabilizing, but "
        "stabilization is not reacceleration. The third quarter of fiscal 2026 (ended October 2025) "
        "delivered the company's first GAAP-profitable third quarter — $13 million of GAAP operating "
        "income on $411 million of revenue, up 16% year over year — with 85% non-GAAP gross margins "
        "and more than $1.7 billion of cash against no meaningful debt. That is a healthy software "
        "business. It is not yet a reaccelerating one, and 16% growth after the brutal deceleration "
        "of 2023–2024 deserves measured — not enthusiastic — interpretation.",
        "The competitive field is the most dangerous in enterprise software: Microsoft, OpenAI, and "
        "every hyperscaler are building agent orchestration natively into the platforms UiPath "
        "automates. UiPath's counter-thesis — that enterprises need a vendor-neutral governance layer "
        "with human-in-the-loop controls, audit trails, and cross-platform reach — is reasonable and "
        "early customer evidence (production agentic deployments at banks, insurers, and airlines) "
        "supports it. But reasonable is not proven. At $13.12 the market prices a successful-but-"
        "not-dominant agentic transition, which is roughly fair. Our 10-year scenario DCF values the "
        "equity at a probability-weighted $13.51 — bear $6.79 / base $13.21 / bull $20.84 — essentially "
        "the current price, which is why this is a HOLD and not a BUY. We wait for proof.",
        "The margin trajectory is the reward for patience if the pivot lands: FCF margins "
        "expanding from the mid-20s toward 30% on an 85% gross-margin base mean every point of "
        "revenue reacceleration converts almost fully to cash. UiPath does not need heroic "
        "growth to be worth materially more than $13 — it needs growth to stop decelerating. "
        "That asymmetry (margins doing the work that growth used to do) is what keeps this a "
        "HOLD rather than a SELL despite the platform risk: the business is healthy enough that "
        "time is an ally, provided the top line merely stabilizes.",
    ],
    "business": [
        "UiPath, founded in 2005 in Bucharest, Romania by Daniel Dines and Marius Tirca and now "
        "headquartered in New York, is the market leader in robotic process automation. Its platform "
        "spans Studio (development), Orchestrator (management), and attended and unattended robots "
        "that execute workflows across enterprise applications. The 2021 IPO was one of the largest "
        "US software listings ever, valuing the company above $35 billion; the subsequent years "
        "brought slowing growth, a cloud transition, and the 2024 leadership change that returned "
        "Dines to the CEO role.",
        "The current platform strategy is agentic automation: Maestro orchestrates AI agents built by "
        "UiPath, Microsoft, OpenAI, or customers themselves; Autopilot offers natural-language "
        "workflow creation; and new AI models let robots interpret user interfaces without underlying "
        "API access. The commercial thesis is 'agents decide, robots execute, humans handle "
        "exceptions' — with governance built in from the start, which is what regulated enterprises "
        "require before they scale agents.",
    ],
    "business_bullets": [
        ("One underappreciated asset: the installed base. ",
         "Tens of thousands of enterprise customers with UiPath robots already embedded in their "
         "processes are the natural distribution channel for Maestro. Selling orchestration to a "
         "customer that already trusts your robots is a fundamentally easier motion than selling it "
         "cold — and it is why we give the agentic pivot better odds than a standing start would "
         "deserve. The installed base does not guarantee the transition, but it meaningfully "
         "shortens the sales cycle for it."),
    ],
    "outlook": [
        "We see the next two years as a show-me period with a binary flavor. If Maestro becomes the "
        "enterprise standard for governing heterogeneous agent fleets — the Switzerland of agentic AI "
        "— UiPath has a genuine second act with pricing power and net-revenue-retention expansion. "
        "Early signs are directionally positive: the 2026 customer awards highlighted production-"
        "scale agentic deployments with measured (not projected) returns, and Maestro appeared "
        "across nearly every winning submission.",
        "The alternative is absorption: agentic workflows get built natively into Microsoft 365, "
        "Salesforce, and ServiceNow, and UiPath is left automating the shrinking residue of legacy "
        "processes. Our base case sits between these poles — high-single-digit revenue growth "
        "(~7.8% CAGR) with the fortress balance sheet funding R&D and opportunistic M&A — but we "
        "weight the absorption scenario materially (bear 25% at $6.79, with growth stalling to ~1% "
        "CAGR) because platform history favors the platforms. Capital allocation is straightforward "
        "and shareholder-friendly: no meaningful debt, a large cash balance, and buybacks offsetting "
        "dilution. The debate is entirely about the top line's second derivative, and on that the "
        "honest answer is that the data are promising but early.",
    ],
    "financials": [
        "The financial profile is a healthy software business in rehabilitation: 85% non-GAAP gross "
        "margins, FCF margins gliding from ~24% toward 30% in the base case, and $1.33 billion of net "
        "cash (~$2.50 a share, ~19% of market cap) against no meaningful debt. Revenue: $1.06B → "
        "$1.31B → $1.43B → $1.61B (FY23–FY26), with FCF of -$0.03B → $0.29B → $0.31B → $0.35B. The "
        "model uses a 12% base discount — the speculative/risky tier, not the standard 10% — because "
        "a former high-flyer derated on the existential AI-agent disruption debate has not earned "
        "steady-compounder risk pricing. SBC remains a real drag ($290.7M in FY26), and the model "
        "prices 3% annual share creep.",
        "Base-case economics: ~7.8% ten-year revenue CAGR (FY27E $1.79B haircut anchor, growth "
        "fading from 11% toward 5%), FCF margins 23.7%→30% by year 10, terminal growth 2.5%. The "
        "bear case (0.8% CAGR, margins compressing to 26%, terminal growth derated 40% to 1.5%) sits "
        "at $6.79 — 48% below the price, a genuinely adverse outcome. The bull ($20.84) assumes "
        "Maestro becomes the enterprise-standard agent governance layer with 11% sustained growth.",
    ],
    "moat": [
        ("The most deployed 'body' for enterprise agents. ",
         "UiPath's robots are embedded in tens of thousands of enterprises — the execution layer "
         "that AI agents need to touch legacy systems. Distribution is the moat's foundation."),
        ("Vendor-neutral governance positioning. ",
         "Maestro's pitch — govern agents from any vendor with human-in-the-loop controls and audit "
         "trails — is exactly what regulated enterprises require before scaling agents, and no "
         "hyperscaler can credibly offer neutrality."),
        ("Fortress balance sheet. ",
         "$1.33B net cash funds the agentic R&D transition and opportunistic M&A without dilution."),
        ("Counterweight: the platforms own the battlefield. ",
         "Microsoft, OpenAI, and the hyperscalers build orchestration natively into the platforms "
         "UiPath automates. History favors the platforms — hence the 12% discount and the "
         "materially-weighted bear case."),
    ],
    "risks": [
        ("Platform absorption. ",
         "Microsoft, OpenAI, and hyperscalers building native agent orchestration could marginalize "
         "a third-party layer — the $6.79 bear case."),
        ("Growth reacceleration is unproven. ",
         "16% is stabilization, and the agentic revenue contribution is still early."),
        ("Enterprise budget cyclicality. ",
         "Automation spending is deferrable in a downturn."),
        ("Seat-based pricing pressure. ",
         "Automation shifting toward consumption-based agent models compresses per-seat pricing."),
        ("Execution risk. ",
         "The product transition from deterministic RPA to agentic orchestration is still early."),
        ("Founder dependence. ",
         "Dines owns roughly 20% and the turnaround is closely tied to his leadership."),
    ],
    "falsification": "Two consecutive quarters of accelerating revenue growth with agentic products "
        "called out as the driver — the single most important proof point — plus evidence of Maestro "
        "standardization (large enterprises deploying it as the cross-vendor agent governance layer) "
        "and net revenue retention inflecting upward on agentic expansion, would move us toward BUY. "
        "Conversely, growth decelerating back toward 10%, a major platform competitor launching a "
        "directly comparable orchestration layer with rapid adoption, or a large dilutive acquisition, "
        "would move us toward REDUCE.",
    "valuation_method": "10-year scenario FCFF DCF",
    "valuation_intro": [
        "We value UiPath on a probability-weighted 10-year scenario DCF, weighted bear 25% / base "
        "50% / bull 25%, with scenario-specific discounts: bear 14.5% (base + 250bp), base 12.0% "
        "(the speculative/risky tier — a former high-flyer derated on the AI-agent disruption debate "
        "has not earned steady-compounder pricing), bull 10.5% (base – 150bp). Terminal growth is "
        "1.5% / 2.5% / 2.5% on year-10 FCF at normalized margins — never peak margins. Net cash of "
        "$1.325B is added in every scenario; bear-case dilution runs higher under stress. Terminal "
        "value is 29–59% of EV across scenarios, under the 70% guardrail.",
        "The base case assumes ~7.8% ten-year revenue CAGR with FCF margins expanding 23.7%→30% on "
        "the high gross-margin base. The bear assumes platform absorption: growth stalls to ~1% "
        "CAGR, pricing power erodes, margins compress 400bp below base, and the terminal multiple "
        "derates 40% — a genuinely adverse outcome at $6.79, well below the current $13.12 price. "
        "The bull assumes Maestro becomes the enterprise-standard agent governance layer with 11% "
        "sustained growth and 33% terminal FCF margins.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 6.79,
            "assumptions": "Platform absorption: AI agents and Microsoft bundling cannibalize "
                "task-level RPA; growth stalls to ~1% CAGR; margins compress 400bp below base; "
                "terminal growth derated 40%.",
            "rev_cagr": "+0.8%", "margin_end": "26%",
            "discount": 0.145, "terminal_g": 0.015, "tv_share": 0.29,
            "pv_explicit": COMP["bear"]["expl"],
            "pv_terminal": COMP["bear"]["tv"],
            "cashflow_unit": "$bn",
        },
        "base": {
            "fair_value": 13.21,
            "assumptions": "Agentic pivot credible but not dominant; ~7.8% revenue CAGR; FCF "
                "margins 23.7%→30%; fortress balance sheet funds the transition.",
            "rev_cagr": "+7.8%", "margin_end": "30%",
            "discount": 0.120, "terminal_g": 0.025, "tv_share": 0.49,
            "pv_explicit": COMP["base"]["expl"],
            "pv_terminal": COMP["base"]["tv"],
            "cashflow_unit": "$bn",
        },
        "bull": {
            "fair_value": 20.84,
            "assumptions": "Maestro becomes the enterprise-standard agent governance layer; 11% "
                "sustained growth; 33% terminal FCF margins; NRR expansion.",
            "rev_cagr": "+11.0%", "margin_end": "33%",
            "discount": 0.105, "terminal_g": 0.025, "tv_share": 0.59,
            "pv_explicit": COMP["bull"]["expl"],
            "pv_terminal": COMP["bull"]["tv"],
            "cashflow_unit": "$bn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Probability-weighted DCF value is $13.51 "
        "(0.25×$6.79 + 0.50×$13.21 + 0.25×$20.84), rounded to our $13.50 target — essentially the "
        "current price, which is why this is a HOLD. Composition is on an EV basis; $1.325B of net "
        "cash is added to reach equity fair value in every scenario.",
    "charts": {
        "scenario": {"bear": 6.79, "base": 13.21, "bull": 20.84,
                     "weighted": 13.50, "price": 13.12},
        "trajectory": {
            "years_hist": [2023, 2024, 2025, 2026],
            "revenue_hist": [1.06, 1.31, 1.43, 1.61],
            "fcf_hist": [-0.03, 0.29, 0.31, 0.35],
            "years_proj": list(range(2027, 2037)),
            "revenue_proj": base_revp,
            "fcf_proj": base_fcfp,
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: fiscal-year revenue and operating-CF-minus-capex (Yahoo; FY ends "
                "January). Projection: the model's base-case FY28–FY37 path (FY27E $1.79B anchor). "
                "Shaded = projection.",
        },
        "composition": {
            "bear": {"pv_explicit": COMP["bear"]["expl"],
                     "pv_terminal": COMP["bear"]["tv"]},
            "base": {"pv_explicit": COMP["base"]["expl"],
                     "pv_terminal": COMP["base"]["tv"]},
            "bull": {"pv_explicit": COMP["bull"]["expl"],
                     "pv_terminal": COMP["bull"]["tv"]},
            "unit": "$bn",
        },
        "extra": {
            "type": "line",
            "years": list(range(2027, 2037)),
            "series": [{"label": "Base-case FCF margin (%)",
                        "values": [round(100 * f / r, 1) for f, r in
                                   zip(base_fcfp, base_revp)]}],
            "ylabel": "%", "title": "Base-case FCF margin trajectory (%)",
        },
    },
}

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "output", "PATH-equity-research-note-polished.pdf")
    print(build_note(data, out))
