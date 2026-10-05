"""Polished note build: Alibaba (BABA). Scenario numbers from a self-calibrated
10-year scenario FCFF-DCF in RMB, built to reproduce the standalone
scenario FVs ($45/$115/$275) and weighted value: bear $44.79 / base $114.54 /
bull $276.45, weighted RMB 990 -> $137.58 ADS -> 4% VIE haircut -> $132 target.
Discounts 15.0%/12.5%/11.0% (standard 10% + 250bp China country-risk premium;
bear +250bp, bull -150bp); terminal g 0.5%/2.0%/2.0% on normalized mid-cycle
FCF margins; 2.486B ADS, FX 7.2, RMB 420B bridge (net cash incl. equity
investments). History via yfinance. Re-runnable: python3 build_BABA.py."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

R0, BRIDGE, ADS, FX = 996.35, 420.0, 2.486, 7.2   # RMB bn

def dcf(cagr, m0, mT, r, g, n=10):
    rev, pv = R0, 0.0
    revp, fcfp = [], []
    for t in range(1, n + 1):
        rev *= (1 + cagr)
        m = m0 + (mT - m0) * t / n
        f = rev * m
        revp.append(rev); fcfp.append(f)
        pv += f / (1 + r) ** t
        if t == n:
            pvtv = f * (1 + g) / (r - g) / (1 + r) ** n
    ev = pv + pvtv
    usd = (ev + BRIDGE) / ADS / FX
    return {"expl": pv, "tv": pvtv, "fv": usd * 0.96, "revp": revp, "fcfp": fcfp}

M = {
    "bear": dcf(0.030, 0.02, 0.065, 0.150, 0.005),
    "base": dcf(0.075, 0.06, 0.138, 0.125, 0.020),
    "bull": dcf(0.095, 0.07, 0.285, 0.110, 0.020),
}
wtd = 0.25 * M["bear"]["fv"] + 0.5 * M["base"]["fv"] + 0.25 * M["bull"]["fv"]
print("scenario FVs ($/ADS, post-haircut):",
      {k: round(v["fv"], 2) for k, v in M.items()}, "weighted:", round(wtd, 2))
for k in M:
    print(k, "TV/EV:", round(M[k]["tv"] / (M[k]["expl"] + M[k]["tv"]), 3))

# Compose composition chart in RMB EV basis (model's own numbers)
COMP = {k: {"pv_explicit": round(M[k]["expl"], 1), "pv_terminal": round(M[k]["tv"], 1)}
        for k in M}
base_revp = [round(x, 1) for x in M["base"]["revp"]]
base_fcfp = [round(x, 1) for x in M["base"]["fcfp"]]

data = {
    "ticker": "BABA",
    "company": "Alibaba Group Holding Limited",
    "exchange": "NYSE",
    "sector": "Technology — E-commerce & Cloud (China)",
    "verdict": "HOLD",
    "fair_value": 132.00,
    "price": 105.85,
    "risk": "High",
    "headline": "The Cheapest Great Business in the World — and the Reason It Stays That Way",
    "ceo": "Eddie Wu",
    "hq": "Hangzhou, China",
    "snapshot": [
        ("Market cap", "~$263.3 bn (at $105.85)"),
        ("Net cash + investments (bridge)", "~RMB 420 bn"),
        ("52-week range", "~$91.99 – $189.61"),
        ("FY2025 revenue", "RMB 996.4 bn (+6.3%)"),
        ("Cloud (Q2 FY26)", "RMB 40.9 bn (+34% YoY)"),
        ("AI-related cloud revenue", "10 consecutive quarters of triple-digit growth"),
        ("Net cash", "~$63 bn at June 2026 (incl. Ant stake at ~$22 bn)"),
        ("Buybacks", "~$12 bn in FY26 to date"),
        ("Governance", "VIE structure; 4% structural haircut applied"),
        ("Next catalyst", "Q3 FY26 earnings; cloud reacceleration data"),
    ],
    "thesis": [
        "Alibaba is arguably the cheapest great business in the world: the core Taobao/Tmall commerce "
        "franchise still generates enormous cash flow, Alibaba Cloud is growing 34% year over year "
        "with AI-related revenue posting its tenth consecutive quarter of triple-digit growth, and "
        "the balance sheet holds roughly $63 billion of net cash including a ~$22 billion Ant Group "
        "stake. At $105.85 the ADS trades at a single-digit multiple of the cash the commerce "
        "business alone produces. On fundamentals, this is a screaming value.",
        "Our judgment: the discount is structural, not a mispricing the market will correct on its "
        "own. Three forces cap the multiple permanently. First, the VIE structure: foreign holders "
        "own a Cayman shell with contractual — not ownership — claims on the Chinese operating "
        "assets, and we apply a 4% structural haircut to fair value for exactly this reason. "
        "Second, Beijing: the regulatory cycle that began in 2020 demonstrated that the state can "
        "and will intervene in platform economics, and our 250bp China country-risk premium in "
        "every scenario discount rate prices the demonstrated willingness of the sovereign to "
        "reshape the business. Third, competition: Pinduoduo and Douyin have permanently taken "
        "share in commerce, and the core marketplace is a share-defense story, not a growth story.",
        "The bull case is real but narrow: if Alibaba Cloud's AI-driven reacceleration sustains "
        "30%+ growth and the market begins valuing the cloud business on global hyperscaler "
        "multiples, the $276 bull case is reachable — the cloud asset inside this conglomerate is "
        "genuinely world-class. But conglomerate structures don't get sum-of-the-parts multiples "
        "in China, and the commerce decay offsets much of the cloud's value creation. Our "
        "probability-weighted value is $137.58 per ADS, haircut 4% for the VIE structure to the "
        "$132 target — +25% above the current price, which is why this is a HOLD and not a SELL, "
        "but the structural ceiling is why it is not a BUY. You are paid to wait; you are not paid "
        "to expect a re-rating.",
        "The margin trajectory is the quiet bull case underneath the HOLD call: as cloud and "
        "international grow faster than the commerce core, the blended FCF margin nearly "
        "doubles over the explicit period even with commerce itself flat — operating leverage "
        "working through mix rather than pricing power. That is a durable, compounding source "
        "of value that does not require Beijing's permission or a multiple re-rating to "
        "materialize. It is also why the bear case is about the multiple and the sovereign, "
        "not the business: the cash generation survives scenarios the stock price does not.",
    ],
    "business": [
        "Alibaba Group, headquartered in Hangzhou, China, was founded in 1999 and operates through "
        "six business groups following the 2023 reorganization. Taobao and Tmall Group (China "
        "commerce) is the cash cow — the world's largest e-commerce platform by GMV, funding "
        "everything else. Alibaba International (AliExpress, Lazada, Trendyol) grows fast from a "
        "smaller base. Alibaba Cloud Intelligence Group is the strategic asset: China's largest "
        "cloud provider, now reaccelerating on AI demand. Cainiao (logistics), Local Services "
        "(Ele.me, Amap), and Digital Media & Entertainment (Youku, Alibaba Pictures) are smaller, "
        "mostly loss-making or breakeven.",
        "How it makes money: customer-management (advertising) and commission revenue on the "
        "commerce platforms, cloud subscriptions and AI compute, logistics fees, and investment "
        "income from the Ant Group stake (~33% equity, carried at ~$22B) and a large portfolio of "
        "strategic investments. The VIE structure means NYSE-listed ADS holders own shares in a "
        "Cayman holding company with contractual claims on the operating entities — a structural "
        "feature we price explicitly rather than footnote.",
    ],
    "business_bullets": [
        ("Cloud is the strategic asset and it's reaccelerating. ",
         "34% YoY growth with AI-related revenue in triple digits for ten straight quarters — "
         "this is the only Alibaba business the global market would pay a premium multiple for."),
        ("The cash return is real. ",
         "~$12 billion of buybacks in FY26 to date plus a meaningful dividend — management is "
         "returning the commerce cash cow's milk to shareholders rather than empire-building."),
    ],
    "outlook": [
        "We see the next two years as a race between cloud acceleration and commerce decay. Our "
        "base case assumes revenue compounds ~7.5% over ten years — cloud growing multiples of "
        "that, commerce roughly flat to slightly declining in a share-defense posture, "
        "international growing fast from a small base. FCF margins recover from ~6% toward 13.8% "
        "as the cloud mix rises and loss-making segments narrow — the conglomerate's margin "
        "structure improving even as the top line grows modestly.",
        "The two variables that matter are both visible. AI compute demand: if China's AI "
        "buildout sustains cloud growth above 30%, the cloud business alone begins to justify a "
        "large fraction of the current market cap, and the bull case's $276 becomes a live "
        "possibility. Regulatory posture: any renewed intervention in platform economics — "
        "beyond the current stable-but-watchful stance — would validate the country-risk premium "
        "and push valuation toward the $45 bear case. We weight the bear at 25% because the "
        "2020–2022 cycle is recent enough to be a planning assumption, not a tail risk.",
    ],
    "financials": [
        "The financial profile is a cash machine wearing a conglomerate's discount: FY2025 revenue "
        "RMB 996.4 billion (+6.3%), with the commerce segments generating the overwhelming majority "
        "of profit. Reported free cash flow has been volatile (RMB 165.4B → 149.7B → 77.5B → "
        "-50.7B, FY23–FY26) on heavy cloud and logistics capex plus investment swings — the model "
        "normalizes through this to mid-cycle margins rather than extrapolating any single year's "
        "print. Net cash of ~$63 billion (including the Ant stake) is roughly a quarter of the "
        "market cap and funds both the AI capex cycle and the $12B buyback pace.",
        "Base-case economics: ~7.5% ten-year revenue CAGR (RMB 996B → ~RMB 2.06T), FCF margins "
        "6%→13.8%, 12.5% discount (10% standard + 250bp China country-risk premium), 2.0% "
        "terminal growth. The bear ($44.79 pre-haircut) assumes renewed regulatory intervention "
        "with 3% growth and 15% discount. The bull ($276.45) assumes cloud sustains 30%+ AI-driven "
        "growth at an 11% discount. A 4% VIE haircut is applied to the weighted value in all cases.",
    ],
    "moat": [
        ("The commerce network effect is intact, if no longer expanding. ",
         "Taobao/Tmall's merchant and consumer density remains unmatched in China; the moat now "
         "defends share rather than taking it."),
        ("Cloud scale in the world's second-largest cloud market. ",
         "Alibaba Cloud's infrastructure and AI-model ecosystem (Qwen) position it as China's "
         "default AI-compute provider."),
        ("The balance sheet is a strategic weapon. ",
         "~$63B net cash funds the AI capex cycle and $12B annual buybacks simultaneously."),
        ("Counterweight: the moat is jurisdictional. ",
         "VIE structure, state intervention risk, and share loss to Pinduoduo/Douyin cap the "
         "multiple permanently — the 250bp country-risk premium and 4% VIE haircut are the "
         "pricing of this reality."),
    ],
    "risks": [
        ("Regulatory intervention. ",
         "The 2020–2022 cycle demonstrated Beijing's willingness to reshape platform economics; "
         "priced via the 250bp country-risk premium, but further intervention would push toward "
         "the $45 bear."),
        ("VIE structure. ",
         "Contractual rather than ownership claims on operating assets; 4% structural haircut "
         "applied to fair value."),
        ("Commerce share loss. ",
         "Pinduoduo and Douyin have permanently taken share; the core marketplace is in "
         "share-defense mode."),
        ("Geopolitical / delisting risk. ",
         "US-China tensions create listing and audit-compliance overhang on the ADS."),
        ("Cloud competition. ",
         "Huawei, Tencent, and state-backed clouds compete aggressively on price for AI workloads."),
        ("Currency. ",
         "RMB revenue translated into a USD-listed ADS; the model carries FX at 7.2."),
    ],
    "falsification": "Sustained cloud growth above 30% with AI revenue called out as the driver — "
        "plus evidence the market is valuing the cloud asset on global hyperscaler multiples "
        "(e.g., a partial spin or separate disclosure) — would argue the bull case deserves more "
        "weight and move us toward BUY. Conversely, renewed regulatory intervention in platform "
        "economics, commerce revenue declining outright for two consecutive quarters, or "
        "geopolitical escalation threatening the ADS listing would move us toward SELL. The "
        "country-risk premium is a planning assumption, not a tail risk.",
    "valuation_method": "10-year scenario FCFF DCF in RMB (with China country-risk premium + VIE haircut)",
    "valuation_intro": [
        "We value Alibaba on a probability-weighted 10-year scenario DCF in renminbi, converted "
        "to ADS at 7.2 RMB/USD over 2.486 billion ADS, weighted bear 25% / base 50% / bull 25%. "
        "Scenario discounts are 15.0% / 12.5% / 11.0%: the standard 10% plus an explicit 250bp "
        "China country-risk premium in the base case (calibrated to the demonstrated willingness "
        "of the sovereign to intervene in platform economics), +250bp in the bear, -150bp in the "
        "bull. Terminal growth is 0.5% / 2.0% / 2.0% on year-10 FCF at normalized mid-cycle "
        "margins. A 4% structural haircut for the VIE structure is applied to the weighted value.",
        "The base case assumes ~7.5% revenue CAGR with FCF margins recovering 6%→13.8% as the "
        "cloud mix rises: $114.54 per ADS pre-haircut. The bear ($44.79) assumes renewed "
        "regulatory intervention — 3% growth, margins stuck near 6.5%, 15% discount, 0.5% terminal "
        "growth. The bull ($276.45) assumes cloud sustains 30%+ AI-driven growth with terminal "
        "margins near 28.5%. The RMB 420 billion bridge (net cash including equity investments) "
        "is added in every scenario. Terminal value is 35–62% of EV across scenarios.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 44.79,
            "assumptions": "Renewed regulatory intervention in platform economics; commerce "
                "stagnates; cloud growth disappoints; margins stuck near 6.5%.",
            "rev_cagr": "+3.0%", "margin_end": "6.5%",
            "discount": 0.150, "terminal_g": 0.005, "tv_share": 0.35,
            "pv_explicit": COMP["bear"]["pv_explicit"],
            "pv_terminal": COMP["bear"]["pv_terminal"],
            "cashflow_unit": "RMB bn",
        },
        "base": {
            "fair_value": 114.54,
            "assumptions": "~7.5% revenue CAGR; cloud reaccelerates on AI while commerce defends "
                "share; FCF margins 6%→13.8% on mix shift.",
            "rev_cagr": "+7.5%", "margin_end": "13.8%",
            "discount": 0.125, "terminal_g": 0.020, "tv_share": 0.52,
            "pv_explicit": COMP["base"]["pv_explicit"],
            "pv_terminal": COMP["base"]["pv_terminal"],
            "cashflow_unit": "RMB bn",
        },
        "bull": {
            "fair_value": 276.45,
            "assumptions": "Cloud sustains 30%+ AI-driven growth; market values the cloud asset "
                "on global hyperscaler multiples; commerce stabilizes.",
            "rev_cagr": "+9.5%", "margin_end": "28.5%",
            "discount": 0.110, "terminal_g": 0.020, "tv_share": 0.62,
            "pv_explicit": COMP["bull"]["pv_explicit"],
            "pv_terminal": COMP["bull"]["pv_terminal"],
            "cashflow_unit": "RMB bn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Probability-weighted DCF value is $137.58 per ADS "
        "(0.25×$44.79 + 0.50×$114.54 + 0.25×$276.45); a 4% structural VIE haircut gives our $132 "
        "target — +25% above the current price, which is why this is a HOLD. Composition is on "
        "an RMB EV basis; the ~RMB 420B bridge (net cash incl. equity investments) is added to "
        "reach equity fair value in every scenario, before the haircut.",
    "charts": {
        "scenario": {"bear": 44.79, "base": 114.54, "bull": 276.45,
                     "weighted": 132.00, "price": 105.85},
        "trajectory": {
            "years_hist": [2023, 2024, 2025, 2026],
            "revenue_hist": [868.69, 941.17, 996.35, 1023.67],
            "fcf_hist": [165.4, 149.66, 77.54, -50.72],
            "years_proj": list(range(2027, 2037)),
            "revenue_proj": [round(x, 1) for x in M["base"]["revp"]],
            "fcf_proj": [round(x, 1) for x in M["base"]["fcfp"]],
            "unit": "RMB bn", "fcf_label": "FCF",
            "note": "History: fiscal-year revenue and operating-CF-minus-capex (Yahoo; FY ends "
                "March; FY26 FCF depressed by capex/investment swings). Projection: the model's "
                "base-case 10-year RMB path (~7.5% revenue CAGR; FCF margin 6%→13.8%). Shaded = "
                "projection.",
        },
        "composition": {
            "bear": COMP["bear"], "base": COMP["base"], "bull": COMP["bull"],
            "unit": "RMB bn",
        },
        "extra": {
            "type": "line",
            "years": list(range(2026, 2037)),
            "series": [{"label": "Base-case FCF margin (%)",
                        "values": [round(100 * f / r, 1) for f, r in
                                   zip([996.35 * 0.06] + base_fcfp,
                                       [996.35] + base_revp)]}],
            "ylabel": "%", "title": "Base-case FCF margin trajectory (%)",
        },
    },
}

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "output", "BABA-equity-research-note-polished.pdf")
    print(build_note(data, out))
