"""Polished note build: Grab (GRAB). Scenario numbers from the hardened 10-year
scenario FCFF-DCF model (workspace/grab-research/build_note.py): bear $1.36 /
base $3.37 / bull $5.43, weighted $3.38 -> $3.40 target; revenue CAGRs
2.4%/12.9%/16.4%, terminal FCF margins 6.5%/15%/18%, discounts
16.0%/13.5%/12.0% (incl. +150bp Southeast Asia country-risk premium),
terminal g 1.5%/2.5%/2.5%. EV splits from the scenario EV ($2.1B/$10.4B/$18.8B)
with TV shares derived from the model parameters. History via yfinance.
Re-runnable: python3 build_GRAB.py."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

# Composition: scenario EV from the model; TV share derived from the model's
# own parameters (smooth revenue CAGR + FCF-margin glide from ~0% to terminal).
def tv_share(cagr, mT, r, g, R0=3.37, n=10):
    rev, pv = R0, 0.0
    for t in range(1, n + 1):
        rev *= (1 + cagr)
        m = mT * t / n
        f = rev * m
        pv += f / (1 + r) ** t
        if t == n:
            pvtv = f * (1 + g) / (r - g) / (1 + r) ** n
    return pvtv / (pv + pvtv)

EV = {"bear": 2.1, "base": 10.4, "bull": 18.8}
TS = {"bear": tv_share(0.024, 0.065, 0.160, 0.015),
      "base": tv_share(0.129, 0.150, 0.135, 0.025),
      "bull": tv_share(0.164, 0.180, 0.120, 0.025)}
COMP = {k: {"pv_explicit": round(EV[k] * (1 - TS[k]), 2),
            "pv_terminal": round(EV[k] * TS[k], 2)} for k in EV}
print("TV shares:", {k: round(v, 3) for k, v in TS.items()})

# Base-case projection: revenue CAGR 12.9% from 2025 $3.37B; FCF margin glide 2%->15%.
rev_proj, r0 = [], 3.37
for t in range(1, 11):
    r0 *= 1.129
    rev_proj.append(round(r0, 2))
fcf_proj = [round(rv * (0.02 + (0.15 - 0.02) * (t + 1) / 10), 2)
            for t, rv in enumerate(rev_proj)]

data = {
    "ticker": "GRAB",
    "company": "Grab Holdings Limited",
    "exchange": "NASDAQ",
    "sector": "Technology — Internet Platforms / Super-App",
    "verdict": "HOLD",
    "fair_value": 3.40,
    "price": 3.08,
    "risk": "High",
    "headline": "Fragile HOLD — the Thesis Stands or Falls on Indonesia's Regulatory Trajectory",
    "ceo": "Anthony Tan",
    "hq": "Singapore",
    "snapshot": [
        ("Market cap", "~$12.6 bn (at $3.08)"),
        ("Net cash (pro forma)", "~$3.5 bn (~$1.13/share)"),
        ("52-week range", "~$2.74 – $6.60"),
        ("2025 revenue", "$3.37 bn (+22%)"),
        ("Adj. EBITDA guide (2026)", "$720–740 mn (+44–48%)"),
        ("Adj. EBITDA streak", "18 consecutive quarters of growth"),
        ("Valuation", "~1.9x FY26E revenue; ~10.4x FY26E adj. EBITDA"),
        ("Markets", "8 Southeast Asian countries"),
        ("Governance", "Dual-class; ~3/4 voting power with founder"),
        ("Next catalyst", "FinSvcs EBITDA inflection (expected H2 2026)"),
    ],
    "thesis": [
        "Grab is Southeast Asia's dominant super-app — ride-hailing, food and grocery delivery, and "
        "a fast-growing fintech arm spanning payments, lending, and digital banking — with the "
        "region's best network density and a genuine, demonstrated path to sustained profitability. "
        "The operating business has arguably never looked better: 18 consecutive quarters of "
        "adjusted-EBITDA growth, the first full-year GAAP profit in company history (FY2025, "
        "~$200M), guidance raised twice this year, and a net-cash balance sheet with $5.0 billion "
        "in the bank. On operations alone, this would be a constructive story.",
        "But Indonesia — Grab's largest market — just rewrote the unit economics by decree. "
        "Presidential Regulation No. 27/2026 caps platform commissions at 8% of fare, down from 20%, "
        "for two-wheel drivers effective July 1, 2026, and layers on mandatory social-security "
        "contributions. We model this explicitly in forecast cash flows: it is an estimated $35–40 "
        "million of annualized EBITDA removed from mobility alone, and the true risk is contagion — "
        "extension to food delivery, to four-wheel drivers, and to other markets where gig-worker "
        "politics are heating up. This is not a footnote to the thesis; it is the thesis. A government "
        "has demonstrated it will cap the take rate, which caps the terminal margin the entire "
        "investment case rests on.",
        "At $3.08 the stock prices in much of the damage — down 49% over the past year, trading at "
        "1.9x forward revenue and 10.4x forward adjusted EBITDA, cheaper than Uber and a fraction of "
        "DoorDash despite growing revenue 22%+ and adjusted EBITDA 44–48% — and Grab's regional "
        "diversification plus fintech growth keep us from walking away. Hence HOLD, not SELL. Our "
        "$3.40 target assumes the cap stays contained to Indonesian two-wheel mobility: the "
        "probability-weighted DCF is $3.38 (bear $1.36 / base $3.37 / bull $5.43), and any extension "
        "of the cap regime makes the $1.36 bear the operative valuation. We add a 150bp Southeast "
        "Asia country-risk premium to every scenario discount rate to reflect exactly this kind of "
        "sovereign intervention risk. This is the most fragile HOLD in our coverage: a quarter of "
        "adverse newsflow — Atome credit deterioration, a second commission-cap intervention — flips "
        "the verdict to REDUCE.",
    ],
    "business": [
        "Grab Holdings, headquartered in Singapore and listed on Nasdaq, operates the leading "
        "super-app across eight Southeast Asian countries. The business has three segments: "
        "Deliveries (GrabFood, GrabMart, GrabExpress — Q2 2026 GMV $4.25B, revenue $531M, +21% YoY, "
        "~12.5% revenue/GMV take rate, segment adjusted EBITDA $96M); Mobility (GrabCar, GrabBike — "
        "Q2 2026 GMV $2.21B, revenue $331M, +12% YoY, ~15.0% take rate, the highest-margin on-demand "
        "vertical); and Financial Services (GrabPay, lending, digital banking including GXBank — the "
        "margin engine of the forward story). Indonesia is the largest single market and the "
        "regulatory epicenter. GrabAds — advertising sold to merchants on the platform — reached 1.7% "
        "of Deliveries GMV in early 2025 and is a growing, high-margin contributor.",
        "How it makes money: commissions and take rates on every ride and delivery, advertising, and "
        "net interest/lending margins. The model is asset-light — no vehicle fleet, no restaurant "
        "kitchens, no bank branches. Governance is a structural feature investors must price: Grab is "
        "a Cayman-incorporated foreign private issuer with a dual-class structure, and a 2026 "
        "shareholder vote doubled Class B super-voting rights, concentrating roughly three-quarters "
        "of voting power with co-founder and CEO Anthony Tan on a small single-digit economic stake. "
        "Minority holders have essentially no mechanism to influence strategy or M&A. We treat this "
        "as a durable governance discount embedded in the required return, not a temporary overhang.",
    ],
    "business_bullets": [
        ("Profitability inflection is real and accelerating. ",
         "Adjusted EBITDA has grown 18 quarters in a row; FY2025 delivered the first full-year GAAP "
         "profit; adjusted EBITDA margin expanded from 12.6% (Q3 2024) to 16.9% (Q2 2026). FY2026 "
         "guidance was raised twice and now calls for $720–740M of adjusted EBITDA (+44–48%)."),
        ("Fintech is the margin engine. ",
         "Lending and payments attached to the region's largest consumer transaction network should "
         "compound at high rates with improving credit performance; FinSvcs EBITDA inflection is "
         "expected in H2 2026. The $1.49 billion Atome (BNPL) acquisition, closing Q3 2027, is the "
         "largest check management has ever written — and the largest new credit risk."),
    ],
    "outlook": [
        "Our forward view is two-track. On operations: fintech is the margin engine — lending and "
        "payments attached to the region's largest consumer transaction network should compound at "
        "high rates with improving credit performance, and deliveries continues to take share with "
        "rationalizing incentives. Mobility, the historical core, is now a regulated utility in its "
        "largest market: we model Indonesian two-wheel take rates at the capped 8% in perpetuity and "
        "assume no recovery.",
        "On regulation: the base case assumes containment. The Indonesian cap applies to two-wheel "
        "mobility; food delivery and four-wheel remain uncapped, and other governments observe rather "
        "than imitate. This is a judgment, not a forecast — Vietnam's competition commission is "
        "already probing platform commissions, and Singapore and Malaysia have passed platform-worker "
        "laws adding social-security costs. The direction of travel across the region is toward more "
        "intervention, not less, which is why the country-risk premium stays in the discount rate "
        "permanently. Consolidation optionality — most obviously a combination with GoTo, Grab's "
        "Indonesian rival — is real but we exclude it from the base case entirely and treat it as "
        "bull-case optionality only. The thesis must stand on the standalone business under the "
        "capped regime; it barely does, which is the honest summary of this note.",
    ],
    "financials": [
        "Revenue has grown 17–24% every quarter; GMV growth accelerated from 15% to 24%; adjusted "
        "EBITDA has risen for 18 straight quarters. The Q2 2026 GAAP profit of $235M is haircut for "
        "a $307M Superbank one-off (true operating profit ~$19M) — the model does not capitalize "
        "one-offs. Net cash is taken pro forma at $3.5B ($5.0B reported less the $1.49B Atome "
        "consideration), or ~$1.13 a share — a third of fair value, flooring the left tail.",
        "The model is a 10-year scenario DCF with no management anchoring — the $1.7B 2028 EBITDA "
        "target is management's, not ours. Revenue CAGRs of 2.4% / 12.9% / 16.4% (bear / base / "
        "bull); terminal FCF margins reset to 6.5% / 15% / 18% on normalized mid-cycle profitability; "
        "discount rates 16.0% / 13.5% / 12.0% — speculative-tier rates plus an explicit +150bp "
        "Southeast Asia country-risk premium calibrated to the demonstrated willingness of governments "
        "in the region to intervene directly in platform economics; terminal growth 1.5% / 2.5% / "
        "2.5%. Indonesia's 20%-to-8% commission cap is structural in the bear case.",
    ],
    "fin_table": {
        "headers": ["", "Q2 2026", "Q2 2025", "YoY"],
        "rows": [
            ["Deliveries revenue", "$531 mn", "—", "+21%"],
            ["Mobility revenue", "$331 mn", "—", "+12%"],
            ["Adjusted EBITDA (margin)", "$168 mn (16.9%)", "$109 mn (13.3%)", "+54%"],
        ],
        "footnote": "Segment figures from Q2 2026 earnings materials.",
    },
    "moat": [
        ("Regional scale + super-app density — a narrow moat. ",
         "Leadership positions are durable (multi-year #1 shares, driver and merchant networks that "
         "took a decade to build) but contestable at the margin by well-funded rivals — and regulators "
         "can redraw the economics overnight (see Indonesia)."),
        ("Network density. ",
         "The region's densest driver/merchant/consumer network lowers fulfillment cost per order and "
         "deepens the data advantage in dispatch and pricing."),
        ("GrabAds as a high-margin layer. ",
         "Ad revenue at 1.7% of Deliveries GMV and rising, at ~100% incremental margin, layered on "
         "existing GMV."),
        ("Cooling competitive temperature. ",
         "The subsidy wars of 2018–2022 have cooled into 'affordability initiatives' and tiered "
         "pricing — better for industry margins. Watch: Uber swallowing foodpanda's parent creates a "
         "formidable delivery competitor from 2027; Sea is out-executing in fintech (Monee's $11.1B "
         "loan book sets the benchmark Grab's digibanks are chasing)."),
    ],
    "risks": [
        ("Regulatory contagion. ",
         "Extension of Indonesia's 8% cap to food delivery, four-wheel drivers, or other countries "
         "would invalidate the base case — this is the load-bearing assumption."),
        ("Gig-worker reclassification. ",
         "Platform-worker laws across the region are adding social-security and insurance costs "
         "structurally."),
        ("Fintech credit risk. ",
         "Lending growth in underbanked markets carries cyclical and underwriting risk; the Atome "
         "acquisition concentrates it."),
        ("Competition. ",
         "GoTo in Indonesia and Sea Limited regionally compete aggressively on incentives and pricing."),
        ("Governance. ",
         "Dual-class control concentration leaves minority holders with no influence over strategy "
         "or M&A."),
        ("Foreign exchange. ",
         "Multi-currency Southeast Asian revenue translated into a USD listing."),
    ],
    "falsification": "Any extension of the commission-cap regime — to delivery, to four-wheel, or to "
        "another country — would move us to SELL; the containment assumption is load-bearing. "
        "Fintech credit losses exceeding through-the-cycle assumptions, or sustained user/transaction "
        "decline in the core Indonesian market, would move us toward REDUCE. To the upside: credible "
        "regulatory stabilization plus demonstrated take-rate recovery in uncapped segments, or a "
        "value-accretive regional consolidation assessed on its own terms, would justify a more "
        "constructive stance.",
    "valuation_method": "10-year scenario FCFF DCF (with Southeast Asia country-risk premium)",
    "valuation_intro": [
        "We value Grab on a 10-year scenario DCF, weighted bear 25% / base 50% / bull 25%, with an "
        "explicit +150bp Southeast Asia country-risk premium in every scenario discount rate — "
        "calibrated to the demonstrated willingness of governments in the region to intervene "
        "directly in platform economics, with Indonesia's commission cap as the live example. Rates: "
        "bear 16.0%, base 13.5%, bull 12.0%. Terminal growth 1.5% / 2.5% / 2.5% on year-10 FCF at "
        "normalized mid-cycle margins — never peak margins. Indonesia's commission cap is modeled "
        "explicitly in forecast cash flows; it is the central variable, not a sensitivity.",
        "The bear ($1.36) assumes the cap extends to food delivery and four-wheel in Indonesia and "
        "spreads to a second market, the take-rate ceiling becomes permanent, fintech credit losses "
        "rise, and the governance discount widens. The base ($3.37) assumes containment to "
        "Indonesian two-wheel at 8%, fintech scaling with controlled credit costs, deliveries margins "
        "expanding. The bull ($5.43) assumes regulatory stabilization, fintech reaching profitable "
        "scale, and regional consolidation delivering synergies. Pro-forma net cash of $3.5B (~$1.13 "
        "a share, a third of fair value) floors the left tail in every scenario.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 1.36,
            "assumptions": "Commission cap extends to food delivery and four-wheel in Indonesia and "
                "spreads to a second market; take-rate ceiling becomes permanent; fintech credit "
                "losses rise; governance discount widens.",
            "rev_cagr": "+2.4%", "margin_end": "6.5%",
            "discount": 0.160, "terminal_g": 0.015, "tv_share": round(TS["bear"], 2),
            "pv_explicit": COMP["bear"]["pv_explicit"],
            "pv_terminal": COMP["bear"]["pv_terminal"],
            "cashflow_unit": "$bn",
        },
        "base": {
            "fair_value": 3.37,
            "assumptions": "Cap contained to Indonesian two-wheel mobility at 8%; fintech scales with "
                "controlled credit costs; deliveries margins expand; regional regulation stabilizes.",
            "rev_cagr": "+12.9%", "margin_end": "15%",
            "discount": 0.135, "terminal_g": 0.025, "tv_share": round(TS["base"], 2),
            "pv_explicit": COMP["base"]["pv_explicit"],
            "pv_terminal": COMP["base"]["pv_terminal"],
            "cashflow_unit": "$bn",
        },
        "bull": {
            "fair_value": 5.43,
            "assumptions": "Regulatory environment stabilizes with no further intervention; fintech "
                "lending reaches profitable scale; regional consolidation delivers synergies.",
            "rev_cagr": "+16.4%", "margin_end": "18%",
            "discount": 0.120, "terminal_g": 0.025, "tv_share": round(TS["bull"], 2),
            "pv_explicit": COMP["bull"]["pv_explicit"],
            "pv_terminal": COMP["bull"]["pv_terminal"],
            "cashflow_unit": "$bn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Probability-weighted DCF value is $3.38 "
        "(0.25×$1.36 + 0.50×$3.37 + 0.25×$5.43), rounded to our $3.40 target. Composition is on an "
        "EV basis ($2.1B / $10.4B / $18.8B); $3.5B of pro-forma net cash is added to reach equity "
        "fair value in every scenario.",
    "charts": {
        "scenario": {"bear": 1.36, "base": 3.37, "bull": 5.43,
                     "weighted": 3.40, "price": 3.08},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [1.43, 2.36, 2.80, 3.37],
            "fcf_hist": [-0.87, -0.01, 0.74, -0.04],
            "years_proj": list(range(2026, 2036)),
            "revenue_proj": rev_proj,
            "fcf_proj": fcf_proj,
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: revenue and operating-CF-minus-capex (Yahoo). Projection: the model's "
                "base-case path (12.9% revenue CAGR; FCF margin gliding 2%→15%). Shaded = projection.",
        },
        "composition": {
            "bear": COMP["bear"], "base": COMP["base"], "bull": COMP["bull"],
            "unit": "$bn",
        },
    },
}

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "output", "GRAB-equity-research-note-polished.pdf")
    print(build_note(data, out))
