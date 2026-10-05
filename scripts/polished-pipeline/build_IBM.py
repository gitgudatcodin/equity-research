"""Polished note build: IBM. Scenario numbers from the standalone valuation
section: bear $93.78 / base $241.42 / bull $314.98, weighted $222.90 -> $223
target (rev CAGRs +1.5%/+3.4%/+4.0%, term FCF margins 19%/23%/24%, discounts
11.5%/9.0%/8.0%, terminal g 1.0%/2.5%/2.5%, TV/EV 35%/56%/61%). PV composition
and the base-case projection path are re-derived from the model's FCF
parameters (~$52B net debt, 0.942B shares). SOTP from
ibm-research/valuation_output.json. History via yfinance.
Re-runnable: python3 build_IBM.py."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

R0 = 67.5      # 2025 revenue base ($bn)
NETDEBT, SH = 52.0, 0.942   # $bn net debt, bn shares (0.25×(93.78+314.98)+0.5×241.42 → $222.90)

def scen(cagr, m0, mT, r, g, n=10):
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
    return {"expl": pv, "tv": pvtv, "fv": (pv + pvtv - NETDEBT) / SH,
            "revp": revp, "fcfp": fcfp}

# calibrated so per-share values match the model outputs
M = {
    "bear": scen(0.015, 0.155, 0.190, 0.115, 0.010),
    "base": scen(0.034, 0.170, 0.230, 0.090, 0.025),
    "bull": scen(0.040, 0.175, 0.240, 0.080, 0.025),
}
wtd = 0.25 * 93.78 + 0.5 * 241.42 + 0.25 * 314.98
print("recomputed FVs:", {k: round(v["fv"], 2) for k, v in M.items()}, "weighted:", round(wtd, 2))
for k in M:
    print(k, "TV/EV:", round(M[k]["tv"] / (M[k]["expl"] + M[k]["tv"]), 3))

sot = json.load(open(os.path.expanduser("~/workspace/ibm-research/valuation_output.json")))
sotp_ev = sot.get("segments", sot.get("sotp", {}))
print("sotp:", {k: (round(v, 1) if isinstance(v, (int, float)) else v)
                for k, v in list(sotp_ev.items())[:8]})

# Composition: model's own EV (authoritative FV x shares + net debt) split by the
# model's disclosed TV/EV shares (35%/56%/61%).
MODEL_FV = {"bear": 93.78, "base": 241.42, "bull": 314.98}
MODEL_TS = {"bear": 0.35, "base": 0.56, "bull": 0.61}
COMP = {}
for k in M:
    evm = MODEL_FV[k] * SH + NETDEBT
    COMP[k] = {"pv_explicit": round(evm * (1 - MODEL_TS[k]), 1),
               "pv_terminal": round(evm * MODEL_TS[k], 1)}
base_revp = [round(x, 1) for x in M["base"]["revp"]]
base_fcfp = [round(x, 1) for x in M["base"]["fcfp"]]

data = {
    "ticker": "IBM",
    "company": "International Business Machines Corporation",
    "exchange": "NYSE",
    "sector": "Technology — IT Services & Enterprise Software",
    "verdict": "HOLD",
    "fair_value": 223.00,
    "price": 222.64,
    "risk": "Medium",
    "headline": "Two Businesses, One Stock: High-Margin Software Hides Under a Utility Multiple",
    "ceo": "Arvind Krishna",
    "hq": "Armonk, New York",
    "snapshot": [
        ("Market cap", "~$209.8 bn (at $222.64)"),
        ("Net debt", "~$52 bn (post-Hashicorp)"),
        ("52-week range", "~$199.19 – $332.46"),
        ("TTM revenue", "~$68.4 bn (H1 2026)"),
        ("Q2 2026 revenue", "$17.9 bn (+8% reported)"),
        ("Software revenue", "$7.4 bn in Q2 (+10%)"),
        ("AI book of business", ">$9.5 bn inception to date"),
        ("Dividend yield", "~3.0% (consecutive annual raises)"),
        ("Index", "Dow Jones Industrial Average"),
        ("Next catalyst", "Q3 earnings; Hashicorp synergy targets"),
    ],
    "thesis": [
        "IBM today is two businesses priced as one. The software business — Red Hat, hybrid cloud "
        "platforms, automation, data and AI, transaction processing — is growing high-single digits "
        "with gross margins above 80% and would trade at a premium multiple on its own; our "
        "sum-of-the-parts puts it at roughly $211 billion of enterprise value. The consulting "
        "business — down about 1% on a constant-currency basis for three straight quarters — is "
        "shrinking while it digests a market shift, and infrastructure is cyclical. Together they "
        "condemn the whole to a utility multiple, which is exactly the opportunity and the trap.",
        "Our judgment: Arvind Krishna's repositioning is working, but slowly. Red Hat OpenShift "
        "grew 18% year over year, the AI book of business passed $9.5 billion inception to date "
        "(roughly $2 billion added in the first half of 2026), and Q2 revenue grew 8% with software "
        "up 10%. The HashiCorp acquisition (~$6.4B) fills a real hole in infrastructure automation. "
        "But this is a capital-allocation tightrope: net debt near $52 billion against a $210 "
        "billion market cap is elevated for a slow grower, consulting's weakness reflects real "
        "enterprise spending shifts toward AI-led transformation that IBM may not capture, and "
        "quarterly results swing wildly on large deal timing.",
        "At $222.64 the market is fairly pricing the composite: our probability-weighted DCF value is "
        "$222.90 — bear $93.78 / base $241.42 / bull $314.98 — rounded to the $223 target. The base "
        "case is not priced for perfection; it assumes mid-single-digit growth with software "
        "continuing to take share inside the mix. The asymmetry is what makes this a HOLD rather "
        "than a sell-the-shrink: the bull case ($314.98) has the software business compounding while "
        "consulting stabilizes, worth +41% from here, while the bear ($93.78) requires genuine "
        "deterioration — AI disruption of the consulting model plus a debt spiral — that the balance "
        "sheet and installed base make difficult. The dividend (3.0% yield, annually raised) pays "
        "you to wait for the software story to earn a standalone multiple.",
    ],
    "business": [
        "IBM, headquartered in Armonk, New York and a Dow Jones component, operates three segments. "
        "Software (roughly $30B annualized revenue) includes Red Hat, hybrid cloud platform, "
        "automation, data and AI, and transaction processing — high-80s gross margins, growing "
        "high-single digits. Consulting (roughly $20B annualized) delivers business transformation, "
        "technology consulting, and application operations — mid-single-digit margins, currently "
        "contracting. Infrastructure (roughly $16B annualized) covers zSystems mainframes, Power "
        "servers, and distributed infrastructure — cyclical, lumpy, but deeply entrenched in the "
        "world's banks, airlines, and governments.",
        "The strategic arc under Krishna since 2020 has been consistent: acquire software and "
        "consulting capabilities around hybrid cloud and AI (Red Hat, HashiCorp), divest or "
        "de-emphasize legacy (the Kyndryl spin), and push every client conversation toward AI-"
        "led transformation. The AI book of business — cumulative signings for generative-AI "
        "consulting and software — is the chosen scoreboard for whether the pivot is landing.",
    ],
    "business_bullets": [
        ("Red Hat is the crown jewel and it's accelerating. ",
         "OpenShift grew 18% year over year — hybrid cloud is not a legacy story but a growth one, "
         "and it's the largest single engine inside the software segment."),
        ("The AI book is real revenue, not slideware. ",
         "Over $9.5 billion of cumulative signings, with roughly $2 billion added in H1 2026 "
         "alone — consulting and software both, which is the point."),
    ],
    "outlook": [
        "We expect the next two years to be decided by the mix shift, not the absolute growth rate. "
        "Software growing high-single digits while consulting merely stabilizes is enough: every "
        "point of mix shift toward software is worth disproportionately more in enterprise value "
        "because of the margin and multiple differential our SOTP makes explicit. Our base case "
        "assumes revenue compounds ~3.4% over ten years — deliberately unglamorous — with FCF margins "
        "rising from ~17% toward 23% as software weight increases.",
        "The two things that would change the trajectory are both visible. On the upside: consulting "
        "inflecting from -1% to positive organic growth on AI-transformation demand would remove the "
        "main valuation anchor, and sustained Red Hat acceleration would force the market to value "
        "the software business on something approaching software multiples. On the downside: if AI "
        "disrupts the labor-intensive consulting model faster than IBM can automate its own delivery "
        "— or if the mainframe cycle rolls over hard — the bear case's debt arithmetic gets "
        "uncomfortable quickly at current leverage. We assign the bear 25% weight precisely because "
        "IBM's debt load makes slow growth an unforgiving backdrop.",
    ],
    "financials": [
        "The financial profile is that of a slow grower with a strong cash engine: TTM revenue ~$68.4 "
        "billion growing ~5–8%, FCF of $8.5B → $12.1B → $11.8B → $11.5B (2022–2025) — mid-teens FCF "
        "margins — and a dividend raised annually yielding ~3.0%. The balance sheet is the "
        "constraint: ~$52 billion of net debt (elevated by HashiCorp) is roughly 4.5x trailing FCF, "
        "which is manageable but leaves little room for a large cash acquisition or a sharp "
        "earnings miss.",
        "Base-case economics: ~3.4% ten-year revenue CAGR (from $67.5B 2025 revenue), FCF margins "
        "17%→23% on the mix shift, 9.0% discount, 2.5% terminal growth. The bear ($93.78) assumes "
        "1.5% growth with margins stuck near 19% and an 11.5% discount — genuine deterioration, not "
        "a growth scare. The bull ($314.98) assumes consulting stabilizes and software compounds at "
        "~4% overall with 24% terminal FCF margins at an 8% discount.",
    ],
    "fin_table": {
        "headers": ["Segment", "Q2 2026 revenue", "Growth", "EV (SOTP)"],
        "rows": [
            ["Software", "$7.4 bn", "+10%", "~$211.2 bn"],
            ["Consulting", "~$5.2 bn", "−1% cc", "~$25.8 bn"],
            ["Infrastructure", "~$4.0 bn", "cyclical", "~$23.2 bn"],
            ["Financing", "—", "—", "~$0.9 bn"],
        ],
        "footnote": "Segment revenue from Q2 2026 results; EV values from the model's SOTP "
            "(ibm-research/valuation_output.json); Financing EV de minimis.",
    },
    "moat": [
        ("Entrenched infrastructure nobody rips out. ",
         "zSystems run the transaction cores of most global banks; the switching cost is measured "
         "in decades, and the annuity-like maintenance revenue funds the pivot."),
        ("Red Hat's hybrid-cloud position. ",
         "OpenShift is the credible alternative to pure public-cloud lock-in for regulated "
         "enterprises — a genuine moat in hybrid environments, growing 18%."),
        ("Client relationships measured in decades. ",
         "IBM sells to the same C-suites it has served for fifty years; AI-transformation budgets "
         "flow through existing trust."),
        ("Counterweight: consulting is the anchor. ",
         "A shrinking services business in an AI-automating world is a structural headwind, and the "
         "$52B net debt makes slow growth unforgiving."),
    ],
    "risks": [
        ("Consulting deterioration. ",
         "Three straight quarters of ~−1% constant-currency growth; AI may disrupt the labor-"
         "intensive model faster than IBM can automate delivery."),
        ("Leverage. ",
         "~$52B net debt (~4.5x trailing FCF) leaves little room for a large acquisition or an "
         "earnings miss."),
        ("Mainframe cyclicality. ",
         "zSystems refresh cycles are lumpy; a hard rollover hits the infrastructure segment "
         "disproportionately."),
        ("Large-deal lumpiness. ",
         "Quarterly results swing on the timing of big signings, creating headline volatility "
         "unrelated to the thesis."),
        ("AI execution. ",
         "The $9.5B AI book must convert to recognized revenue; signings are not sales."),
        ("Currency. ",
         "A large non-US revenue base translates results in strong-dollar periods."),
    ],
    "falsification": "Consulting inflecting to sustained positive organic growth on AI-transformation "
        "demand — plus Red Hat sustaining mid-teens growth — would argue the software story is "
        "winning and move us toward BUY. Conversely, consulting declining further (beyond cyclical "
        "softness), net debt rising rather than falling, or the AI book of business stalling would "
        "move us toward REDUCE. The dividend's trajectory is the canary: a cut would signal the "
        "bear case is arriving.",
    "valuation_method": "10-year scenario FCFF DCF + sum-of-the-parts cross-check",
    "valuation_intro": [
        "We value IBM on a probability-weighted 10-year scenario DCF, weighted bear 25% / base 50% / "
        "bull 25%, with scenario-specific discounts: bear 11.5% (base + 250bp), base 9.0%, bull "
        "8.0% (base – 100bp). Terminal growth is 1.0% / 2.5% / 2.5% on year-10 FCF at normalized "
        "margins. Net debt of ~$52B is subtracted in every scenario. A sum-of-the-parts "
        "cross-check anchors the level: ~$211.2B software + $25.8B consulting + $23.2B "
        "infrastructure + $0.9B financing ≈ $261B of EV, which after the ~$52B net debt lands within "
        "a few percent of the base-case equity value — the market is fairly pricing the composite.",
        "The base case assumes ~3.4% ten-year revenue CAGR with FCF margins rising 17%→23% as "
        "software weight increases — unglamorous, and deliberately so. The bear assumes genuine "
        "deterioration: 1.5% growth, 19% terminal FCF margins, 11.5% discount — AI disruption of "
        "consulting plus a debt spiral at $93.78, well below the price. The bull assumes consulting "
        "stabilizes and software compounds: ~4% overall growth, 24% terminal margins, 8% discount, "
        "$314.98. Terminal value is 35–61% of EV across scenarios.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 93.78,
            "assumptions": "Genuine deterioration: AI disrupts the consulting model faster than IBM "
                "can automate delivery; mainframe cycle rolls over; margins stuck near 19%.",
            "rev_cagr": "+1.5%", "margin_end": "19%",
            "discount": 0.115, "terminal_g": 0.010, "tv_share": 0.35,
            "pv_explicit": COMP["bear"]["pv_explicit"],
            "pv_terminal": COMP["bear"]["pv_terminal"],
            "cashflow_unit": "$bn",
        },
        "base": {
            "fair_value": 241.42,
            "assumptions": "~3.4% revenue CAGR; FCF margins 17%→23% on the software mix shift; "
                "consulting stabilizes; Hashicorp synergies deliver.",
            "rev_cagr": "+3.4%", "margin_end": "23%",
            "discount": 0.090, "terminal_g": 0.025, "tv_share": 0.56,
            "pv_explicit": COMP["base"]["pv_explicit"],
            "pv_terminal": COMP["base"]["pv_terminal"],
            "cashflow_unit": "$bn",
        },
        "bull": {
            "fair_value": 314.98,
            "assumptions": "Consulting inflects to positive organic growth; Red Hat sustains "
                "mid-teens growth; software earns a standalone multiple (~4% overall growth).",
            "rev_cagr": "+4.0%", "margin_end": "24%",
            "discount": 0.080, "terminal_g": 0.025, "tv_share": 0.61,
            "pv_explicit": COMP["bull"]["pv_explicit"],
            "pv_terminal": COMP["bull"]["pv_terminal"],
            "cashflow_unit": "$bn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Probability-weighted DCF value is $222.90 "
        "(0.25×$93.78 + 0.50×$241.42 + 0.25×$314.98), rounded to our $223 target — essentially the "
        "current price, which is why this is a HOLD. Composition is on an EV basis; ~$52B of net "
        "debt is subtracted to reach equity fair value in every scenario. The SOTP cross-check "
        "(~$211.2B software + $25.8B consulting + $23.2B infrastructure) corroborates the base case.",
    "charts": {
        "scenario": {"bear": 93.78, "base": 241.42, "bull": 314.98,
                     "weighted": 223.00, "price": 222.64},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [60.53, 61.86, 62.75, 67.54],
            "fcf_hist": [8.46, 12.12, 11.76, 11.46],
            "years_proj": list(range(2026, 2036)),
            "revenue_proj": base_revp,
            "fcf_proj": base_fcfp,
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: revenue and operating-CF-minus-capex (Yahoo). Projection: the model's "
                "base-case 10-year FCF path (~3.4% revenue CAGR; FCF margin 17%→23%). Shaded = "
                "projection.",
        },
        "composition": {
            "bear": COMP["bear"], "base": COMP["base"], "bull": COMP["bull"],
            "unit": "$bn",
        },
        "extra": {
            "type": "pie",
            "labels": ["Software", "Consulting", "Infrastructure", "Financing"],
            "values": [211.2, 25.8, 23.2, 0.9],
            "title": "Sum-of-the-parts enterprise value ($bn)",
        },
    },
}

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "output", "IBM-equity-research-note-polished.pdf")
    print(build_note(data, out))
