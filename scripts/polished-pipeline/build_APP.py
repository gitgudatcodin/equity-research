"""Polished note build: AppLovin (APP). Scenario numbers from the hardened
10-year scenario FCFF-DCF model (applovin-research/dcf_v3_hardened.py):
bear $109.02 / base $322.92 / bull $577.10, weighted $332.99 -> $335 target.
PV composition re-derived by calling the model's own dcf() function.
History via yfinance. Re-runnable: python3 build_APP.py."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note
import runpy, io, contextlib

# --- Actual model outputs (no invented numbers) ---
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    ns = runpy.run_path(os.path.expanduser("~/workspace/applovin-research/dcf_v3_hardened.py"))
dcf, scen = ns["dcf"], ns["scen"]
model = {}
for k, kw in scen.items():
    v, revn, fcfp, pv_tv, ev, margins = dcf(**kw)
    model[k] = dict(fv=v, expl=ev - pv_tv, tv=pv_tv, fcfp=fcfp)

base_fcf = model["base"]["fcfp"]          # FY27-FY36 base-case FCF path ($M)
base_kw = scen["base"]
rev2026 = ns["rev2026"]
rev_base, rev = [], rev2026
for gr in base_kw["g"]:
    rev *= (1 + gr)
    rev_base.append(rev)

data = {
    "ticker": "APP",
    "company": "AppLovin Corporation",
    "exchange": "NASDAQ",
    "sector": "Technology — Advertising Technology",
    "verdict": "HOLD",
    "fair_value": 335.00,
    "price": 268.22,
    "risk": "High",
    "headline": "A Superb Engine Entering Its Hardest Test: the Open Market",
    "ceo": "Adam Foroughi",
    "hq": "Palo Alto, California",
    "snapshot": [
        ("Market cap", "~$90.1 bn (at $268.22)"),
        ("Net debt", "~$0.5 bn (excl. $500 mn Tripledot stake)"),
        ("52-week range", "~$266.84 – $738.01"),
        ("TTM revenue (2025)", "$5.48 bn"),
        ("TTM FCF", "~$3.94 bn"),
        ("Q3'26 guidance", "Revenue +46–48% at ~83% EBITDA margin"),
        ("2026E revenue (consensus)", "~$8.01 bn"),
        ("Overhangs", "Securities class action; Unity litigation"),
        ("Next catalyst", "Q3 2026 earnings"),
        ("Multiple check", "~12x FY26E EV/EBITDA; ~17x P/E"),
    ],
    "thesis": [
        "AppLovin owns one of the finest advertising engines ever built. AXON, the AI bidder at the "
        "heart of its software business, has delivered sustained 50%+ revenue growth at roughly 85% "
        "adjusted EBITDA margins — economics with almost no precedent in ad-tech. In June 2026 the "
        "company made the defining move of its history: it opened AXON to all advertisers through a "
        "global self-serve platform, ending the curated, referral-only era. The question now is whether "
        "AXON's legendary precision survives contact with the open market.",
        "Our judgment: the engine is real, but the self-serve era is a different business than the "
        "curated era, and the market has not yet priced that difference. Third-party checks show "
        "genuine adoption — pixels at roughly 5,500 merchants by early 2026, growing about 200 per "
        "week — yet the legitimate question, raised by skeptical channel checks, is whether "
        "installations convert into durable spend. E-commerce is now the swing factor: independent "
        "surveys credit AppLovin with about 11% of e-commerce ad volume by mid-2026, the largest share "
        "gain of any ad network, and a September 2026 study of 755 e-commerce brands found 2.9x lifetime "
        "ROAS on the platform. That is early but genuinely encouraging evidence — not yet a verdict.",
        "The overhangs, however, are non-trivial. A securities class action covering February through "
        "August 2026 alleges management overstated the pace of AI-model improvements and the readiness "
        "of its generative-AI video creative tool; a separate lawsuit against Unity over alleged misuse "
        "of MAX auction data adds headline risk. With third-quarter guidance calling for 46–48% revenue "
        "growth at ~83% EBITDA margins — numbers that must be hit to sustain the multiple — we see a "
        "balanced risk/reward at $268.22. HOLD. The path to materially higher prices requires proof that "
        "self-serve e-commerce advertisers spend and retain like gaming advertisers did.",
        "Our 10-year scenario DCF values the equity at a probability-weighted $333 — bear $109 / base "
        "$323 / bull $577 — rounded to our $335 target, +25% above the current price but with the "
        "bear case ($109) sitting 59% below it. That spread is the honest summary: this is a "
        "wonderful-asset, show-me-the-retention situation. The reverse DCF says the current price "
        "implies ~9% ten-year revenue CAGR on base-case economics — the market is already paying for "
        "a great deal of growth, leaving the margin of safety thin until retention is proven.",
    ],
    "business": [
        "AppLovin, based in Palo Alto, California, is an ad-tech company built around three assets: "
        "AXON, the AI engine that optimizes ad bidding and user acquisition; MAX, one of the largest "
        "mobile in-app mediation platforms, which supplies AXON with proprietary auction data; and "
        "AppDiscovery, its user acquisition suite for app developers. The company historically also "
        "operated a portfolio of owned mobile games, but the economic engine — and the investment "
        "story — is the software business, which converts the overwhelming majority of EBITDA to "
        "free cash flow.",
        "The strategic arc is expansion beyond mobile gaming, the vertical where AXON proved itself. "
        "E-commerce is the first new vertical at scale, with connected TV the next frontier. "
        "Generative-AI creative tools — interactive page and video ad generators — are meant to close "
        "the onboarding gap for smaller merchants, and the referral program is widening the funnel "
        "down-market. Whether the funnel converts is the central empirical question of 2026 and 2027. "
        "Capital allocation is a quiet strength: the business's cash conversion funds buybacks that "
        "have steadily reduced the share count, and that compounding matters more at today's price "
        "than it did at the December 2025 peak.",
    ],
    "business_bullets": [
        ("The self-serve pivot is the defining move. ",
         "Opening AXON to all advertisers in June 2026 trades curation for scale. The upside is a "
         "third performance-advertising pillar alongside Meta and Google; the risk is that open "
         "access commoditizes the signal."),
        ("Connected TV is the plausible second act. ",
         "The same AXON bidding intelligence applied to a larger, less mature inventory pool, where "
         "targeting precision is scarcer and therefore more valuable. We do not underwrite CTV in "
         "the base case — it is early — but it lengthens the growth runway if e-commerce adoption "
         "follows the gaming playbook."),
    ],
    "outlook": [
        "We expect the next eighteen months to be dominated by one metric: advertiser retention and "
        "spend expansion in the self-serve cohort. If the e-commerce ROAS advantage holds at scale, "
        "AppLovin has a credible path to becoming a third performance-advertising pillar alongside "
        "Meta and Google, with connected TV as a second act. Our base case assumes total revenue "
        "compounds ~11% over ten years (the post-divestiture software business, growing off the 2026 "
        "surge) with FCF margins gliding from the mid-60s to the high-50s — extraordinary, but a "
        "step down from the curated-era peak as the advertiser mix broadens.",
        "The bear case is that open access commoditizes the signal: more advertisers bidding on the "
        "same inventory compresses ROAS, smaller merchants churn, and growth decelerates toward "
        "stagnation while the multiple contracts. The class-action litigation is the wild card — even "
        "meritless suits consume management attention and can force disclosure that resets "
        "expectations. We haircut management's e-commerce ramp accordingly. The through-line of our "
        "outlook is patience with verification: the engine has earned the benefit of the doubt on "
        "technology, but the open-platform commercial model has not yet earned it on retention.",
    ],
    "financials": [
        "The financial profile is extraordinary and deteriorating-in-a-good-way: revenue grew from "
        "$1.84 billion in 2023 to $5.48 billion in 2025 while free cash flow went from $1.0 billion to "
        "$3.94 billion — FCF margins in the 60s–70s, a software business with ad-network growth. The "
        "model's base case has FCF margins fading from 66% to 58% over ten years as the advertiser "
        "base broadens and take-rates normalize; we do not assume peak margins in perpetuity.",
        "The balance sheet is clean: ~$462 million of net debt against ~$98.7 billion of base-case "
        "enterprise value, plus a $500 million placeholder for the 20% Tripledot stake. The "
        "multiples cross-check is instructive: ~12x FY26E EV/EBITDA and ~17x FY26E P/E are full but "
        "not absurd for these economics; 22x FY27E EPS or 15x FY27E EBITDA both point to ~$400, above "
        "our DCF target — the DCF is the more conservative anchor, and we keep it.",
    ],
    "moat": [
        ("AXON's data flywheel. ",
         "MAX mediation supplies proprietary auction data that improves AXON's bidding models; "
         "better bidding wins more advertisers, which feeds more auction data. This loop is the "
         "moat, and it is why the curated-era economics were so strong."),
        ("Scale in mobile gaming. ",
         "The largest share gains in e-commerce ad volume of any network by mid-2026 suggest the "
         "targeting advantage transfers across verticals — the core bull thesis."),
        ("Cash conversion. ",
         "Mid-60s FCF margins fund buybacks and R&D without leverage, a structural advantage over "
         "ad-tech peers that must choose between growth and balance-sheet repair."),
        ("Vulnerability: the moat is data-depth, not switching cost. ",
         "If open access degrades signal quality — more advertisers on the same inventory — the "
         "flywheel can run in reverse. Unity's MAX auction is the live competitive test."),
    ],
    "risks": [
        ("Self-serve dilution. ",
         "Open access may compress ROAS and churn smaller advertisers, undermining the growth "
         "narrative — the central risk of the note."),
        ("Securities class action (Feb–Aug 2026 class period). ",
         "Alleges overstated AI-model progress and video-tool readiness; headline and financial risk."),
        ("Unity litigation. ",
         "Alleged MAX auction-data misuse; competitive and reputational overhang."),
        ("Expectations risk. ",
         "46–48% guided revenue growth leaves little room for a miss at the current multiple."),
        ("Customer concentration. ",
         "Mobile gaming advertisers still dominate during the transition to e-commerce."),
        ("Privacy and platform risk. ",
         "Changes to mobile OS attribution (Apple, Google) could impair targeting efficacy."),
    ],
    "falsification": "Two consecutive quarters of self-serve advertiser cohorts showing gaming-like "
        "retention and spend expansion — the single most important proof point — plus independent ROAS "
        "studies at larger scale confirming the early 2.9x lifetime figure, would move us toward BUY. "
        "Conversely, a guided growth deceleration into the teens, or evidence that pixel installs are "
        "not converting to spend, would move us toward REDUCE. Resolution of the class action without "
        "material damages or adverse disclosure removes an overhang; connected TV contributing a "
        "visible second growth leg adds one.",
    "valuation_method": "10-year scenario FCFF DCF",
    "valuation_intro": [
        "We value AppLovin on a probability-weighted 10-year scenario DCF (FY27–FY36), weighted bear "
        "25% / base 50% / bull 25%, with scenario-specific discount rates: bear 14.5% (base + 250bp), "
        "base 12.0% (the speculative tier — ad-tech cyclicality, litigation, unproven self-serve "
        "retention), bull 10.5% (base – 150bp). Terminal growth is 1.5% / 2.5% / 2.5% on year-10 FCF "
        "at normalized margins — never peak margins. Terminal value is 26–56% of EV across scenarios, "
        "under the 70% guardrail.",
        "The base case assumes the post-surge business mean-reverts gracefully: ~11% ten-year revenue "
        "CAGR off the 2026 base, FCF margins gliding 66%→58%. The bear assumes Unity takes share via "
        "MAX auctions, the AXON cadence stalls, and the e-commerce pixel proves a false start — "
        "growth collapses to ~1% CAGR and margins compress to 50%. The bull assumes AXON 3.0 ships, "
        "creative unlocks, e-commerce onboarding proves real, and connected TV works: 15.5% CAGR, "
        "margins holding in the 60s.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 109.02,
            "assumptions": "Unity takes share via MAX auctions, AXON cadence stalls, e-commerce "
                "pixel is a false start; growth collapses and FCF margins compress to 50%.",
            "rev_cagr": "+0.7%", "margin_end": "50%",
            "discount": 0.145, "terminal_g": 0.015, "tv_share": 0.26,
            "pv_explicit": round(model["bear"]["expl"], 1),
            "pv_terminal": round(model["bear"]["tv"], 1),
            "cashflow_unit": "$mn",
        },
        "base": {
            "fair_value": 322.92,
            "assumptions": "Post-surge mean reversion; take-rate fades but AXON stays best-in-class; "
                "FCF margins glide 66%→58% as the advertiser base broadens.",
            "rev_cagr": "+11.0%", "margin_end": "58%",
            "discount": 0.120, "terminal_g": 0.025, "tv_share": 0.46,
            "pv_explicit": round(model["base"]["expl"], 1),
            "pv_terminal": round(model["base"]["tv"], 1),
            "cashflow_unit": "$mn",
        },
        "bull": {
            "fair_value": 577.10,
            "assumptions": "AXON 3.0 ships, creative unlocked, e-commerce onboarding real, connected "
                "TV works; durable 15.5% growth with margins holding in the 60s.",
            "rev_cagr": "+15.5%", "margin_end": "62%",
            "discount": 0.105, "terminal_g": 0.025, "tv_share": 0.56,
            "pv_explicit": round(model["bull"]["expl"], 1),
            "pv_terminal": round(model["bull"]["tv"], 1),
            "cashflow_unit": "$mn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Probability-weighted DCF value is $332.99 "
        "(0.25×$109.02 + 0.50×$322.92 + 0.25×$577.10), rounded to our $335 target. Composition is on "
        "an EV basis; the bridge to equity is ~$462M of net debt less the $500M Tripledot stake.",
    "charts": {
        "scenario": {"bear": 109.02, "base": 322.92, "bull": 577.10,
                     "weighted": 335.00, "price": 268.22},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [2.82, 1.84, 3.22, 5.48],
            "fcf_hist": [0.41, 1.00, 2.07, 3.94],
            "years_proj": list(range(2026, 2037)),
            "revenue_proj": [round(rev2026 / 1000, 2)] + [round(x / 1000, 2) for x in rev_base],
            "fcf_proj": [None] + [round(x / 1000, 2) for x in base_fcf],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: revenue and operating-CF-minus-capex (Yahoo). Projection: the model's "
                "base-case FY27–FY36 FCF path (FY26 revenue anchor shown). Shaded = projection.",
        },
        "composition": {
            "bear": {"pv_explicit": round(model["bear"]["expl"], 1),
                     "pv_terminal": round(model["bear"]["tv"], 1)},
            "base": {"pv_explicit": round(model["base"]["expl"], 1),
                     "pv_terminal": round(model["base"]["tv"], 1)},
            "bull": {"pv_explicit": round(model["bull"]["expl"], 1),
                     "pv_terminal": round(model["bull"]["tv"], 1)},
            "unit": "$mn",
        },
    },
}

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "output", "APP-equity-research-note-polished.pdf")
    print(build_note(data, out))
