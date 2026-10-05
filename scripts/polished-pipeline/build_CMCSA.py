"""Polished note build: Comcast (CMCSA). Scenario numbers from the standalone
valuation section: bear $1.03 / base $20.00 / bull $44.55, weighted $21.39 ->
$21 target (rev CAGRs -1.2%/0.0%/+1.2%, term FCF margins 8.9%/12.1%/14.0%,
discounts 12.5%/10.0%/8.5%, terminal g -2.0%/+1.5%/+2.0%; TV 43% of EV in the
base case). PV composition uses the model's own EV (authoritative FV x shares
+ net debt) with TV shares re-derived from the model FCF-path parameters;
the base-case projection path is re-derived from those parameters (~$85B net
debt, 3.539B shares). Extra chart: post-Versant revenue mix pie (~$70B
connectivity, ~$54B content & experiences). History via yfinance.
Re-runnable: python3 build_CMCSA.py."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

R0 = 123.7     # 2025 revenue base ($bn)
NETDEBT, SH = 85.0, 3.539   # $bn net debt, bn shares

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
            "revp": revp, "fcfp": fcfp,
            "ts": pvtv / (pv + pvtv)}

# parameters chosen so the FCF path reproduces the model's revenue CAGRs,
# terminal FCF margins, and discount rates
M = {
    "bear": scen(-0.012, 0.080, 0.089, 0.125, -0.020),
    "base": scen(0.000, 0.110, 0.121, 0.100, 0.015),
    "bull": scen(0.012, 0.120, 0.140, 0.085, 0.020),
}
print("path TV/EV:", {k: round(v["ts"], 3) for k, v in M.items()})

# Composition: model's own EV (authoritative FV x shares + net debt) split by
# TV shares re-derived from the model's FCF-path parameters (base 43%
# disclosed, matches the re-derived base path share)
MODEL_FV = {"bear": 1.03, "base": 20.00, "bull": 44.55}
COMP = {}
for k in M:
    evm = MODEL_FV[k] * SH + NETDEBT
    COMP[k] = {"pv_explicit": round(evm * (1 - M[k]["ts"]), 1),
               "pv_terminal": round(evm * M[k]["ts"], 1)}

base_revp = [round(x, 1) for x in M["base"]["revp"]]
base_fcfp = [round(x, 1) for x in M["base"]["fcfp"]]

data = {
    "ticker": "CMCSA",
    "company": "Comcast Corporation",
    "exchange": "NASDAQ",
    "sector": "Communication Services — Telecom & Media",
    "verdict": "HOLD",
    "fair_value": 21.00,
    "price": 21.57,
    "risk": "Medium-High",
    "headline": "A 4.3% Dividend Yield Paid for by a Shrinking Business",
    "ceo": "Brian Roberts",
    "hq": "Philadelphia, Pennsylvania",
    "snapshot": [
        ("Market cap", "~$76.5 bn (at $21.57)"),
        ("Net debt", "~$85 bn (Versant spin adds ~$2.7B)"),
        ("52-week range", "~$21.28 – $32.86"),
        ("2025 revenue", "$123.7 bn (flat)"),
        ("Broadband subscribers", "~29.0 mn; −142k in Q2 2026"),
        ("Dividend yield", "~4.3% ($1.00 annualized)"),
        ("Buybacks", "$1.8 bn in H1 2026"),
        ("NBCUniversal / Studios", "$5.4 bn Studio revenue in 2025; Epic Universe opened"),
        ("Versant spin", "Completed; ~$2.7 bn distribution to Comcast"),
        ("Next catalyst", "Q3 2026 earnings; broadband subscriber trend"),
    ],
    "thesis": [
        "Comcast is a slow-motion transformation: a cable-broadband utility in structural subscriber "
        "decline — down about 1.6 million subscribers since 2023 — funding a media business that "
        "mostly offsets the decay. Total revenue has been flat at ~$124 billion for three years; "
        "broadband, once the growth engine, lost 142,000 subscribers in the second quarter of 2026 "
        "alone as fixed-wireless and fiber overbuilds took share. The question for investors is "
        "whether the sum of the parts — Connectivity & Platforms on one side, Content & Experiences "
        "on the other — is worth more than a 4.3% dividend yield on a melting ice cube.",
        "Our judgment: the dividend is the thesis, and it is covered — for now. Free cash flow of "
        "$19.2 billion in 2025 and roughly $6 billion in each of the first two quarters of 2026 "
        "covers the ~$4 billion annual dividend and $1.8 billion of first-half buybacks with room "
        "to spare. But the direction of travel is adverse: broadband subscriber losses are "
        "accelerating (not stabilizing), the advertising business is cyclical and structurally "
        "challenged in linear, and $85 billion of net debt against a $76 billion market cap means "
        "the equity is a levered claim on a no-growth business. Our bear case ($1.03) is not a "
        "model artifact — it is the arithmetic of a leveraged equity when revenue declines 1.2% "
        "annually and the terminal growth rate goes to -2%.",
        "The base case ($20.00) assumes Comcast manages the decline: broadband stabilizes at lower "
        "share, wireless and business services grow, and the content side (NBCU studios at $5.4B "
        "2025 revenue, Epic Universe's first full year) holds the line. At $21.57 the stock is "
        "pricing roughly that outcome — fairly, in our view, with a fat yield compensating for the "
        "leverage. Our probability-weighted value is $21.39, rounded to the $21 target. This is a "
        "HOLD for income-oriented investors who understand they own a declining asset being "
        "harvested, not a growth story. The dividend's coverage — not subscriber counts — is the "
        "metric that matters, and it is the falsification trigger we watch.",
    ],
    "business": [
        "Comcast, headquartered in Philadelphia and led by CEO Brian Roberts, is the largest US "
        "cable operator and a major media owner. Post the Versant spin-off, the company reports in "
        "two segments: Connectivity & Platforms (~$70 billion revenue: Xfinity broadband, video, "
        "wireless, and business services — the cash cow, but broadband subscribers are in structural "
        "decline) and Content & Experiences (~$54 billion: NBCUniversal studios, theme parks, "
        "Peacock streaming, and the remaining cable networks — growing modestly, cyclical, and "
        "capital-intensive).",
        "The Versant spin — cable networks including USA, CNBC, and MSNBC — was completed with a "
        "~$2.7 billion distribution to Comcast, removing a declining linear asset from the portfolio "
        "and simplifying the story to broadband-plus-content. The capital allocation is unambiguous: "
        "pay the dividend (raised annually, now $1.00 annualized), buy back stock opportunistically "
        "($1.8B in H1 2026), and deleverage slowly. There is no growth capex story here; the thesis "
        "is harvest and return.",
    ],
    "business_bullets": [
        ("Wireless is the one genuine growth line. ",
         "Xfinity Mobile is adding subscribers at a healthy clip on Verizon's network at minimal "
         "incremental capex — the bundle that slows broadband churn."),
        ("Epic Universe is a real asset. ",
         "The new Orlando theme park's first full year adds high-margin, non-cyclical-adjacent "
         "revenue to Content & Experiences."),
    ],
    "outlook": [
        "We expect the next two years to be a managed decline with two swing variables. Broadband "
        "subscriber losses: if the quarterly bleed stabilizes around -100k to -150k, the base case "
        "holds; if fixed-wireless acceleration pushes losses materially higher, the bear case's "
        "decline arithmetic starts to apply and the equity's leverage turns punitive. Content: "
        "Peacock's path to sustained profitability and the parks' performance are the offsets — "
        "neither is large enough to change the corporate growth rate, but both cushion the "
        "broadband decay.",
        "Capital allocation will dominate the equity story. With $85 billion of net debt, every "
        "dollar of FCF is contested between the dividend, buybacks, and deleveraging. Our base case "
        "assumes the dividend is maintained and slowly grown, buybacks continue at roughly the "
        "current pace, and leverage drifts down. A dividend cut — however unlikely management "
        "considers it — would be the single most damaging event for the equity, because the yield "
        "is the reason to own the stock. We assign the bear case 25% weight because the "
        "levered-equity arithmetic is unforgiving: small misses on revenue compound into large "
        "misses on equity value.",
        "On the content side, the offsets are real but bounded: Epic Universe contributes its "
        "first full year of high-margin attendance revenue, NBCU's studio slate ($5.4B 2025 "
        "revenue) remains a genuine franchise factory, and Peacock's losses have narrowed. None "
        "of these changes the corporate growth rate — they cushion the broadband decay and buy "
        "time for deleveraging. That is the bull case's honest shape: not a growth re-rating, "
        "but a slower harvest at a lower discount rate.",
    ],
    "financials": [
        "The financial profile is a flat top line with a strong but contested cash engine: revenue "
        "$121.4B → $121.6B → $123.7B → $123.7B (2022–2025), FCF $12.7B → $13.0B → $12.5B → $19.2B "
        "(2022–2025, 2025 boosted by working capital). FCF margins run 10–15%, and the model has "
        "base-case terminal FCF margins at 12.1% — this is a harvest story, and the model prices it "
        "as one. The balance sheet is the defining feature: ~$85 billion of net debt against a "
        "$76.5 billion market cap. The equity is a levered claim, which is why the valuation range "
        "is so wide ($1.03 to $44.55).",
        "Base-case economics: 0.0% ten-year revenue CAGR (flat — the honest number), FCF margins "
        "~11–12%, 10.0% discount, +1.5% terminal growth, TV 43% of EV. The bear (-1.2% revenue "
        "CAGR, 8.9% terminal FCF margins, 12.5% discount, -2.0% terminal growth) is the declining-"
        "utility death spiral at $1.03. The bull (+1.2% CAGR, 14.0% terminal margins, 8.5% "
        "discount, +2.0% terminal growth) assumes broadband stabilizes and content over-delivers at "
        "$44.55.",
"$44.55.",
        "The trajectory chart tells the harvest story visually: a flat revenue line with FCF "
        "oscillating in a band rather than compounding — this is what a no-growth cash cow looks "
        "like, and the model does not pretend otherwise. The investment question is never 'when "
        "does growth return' but 'how long does the harvest last,' and every input in the model — "
        "the 0.0% base revenue CAGR, the declining-perpetuity bear, the leverage — is chosen to "
        "keep that question front and center.",
    ],
    "moat": [
        ("The last-mile network is a real moat — in most of its footprint. ",
         "HFC and fiber plant with speeds competitors can't match without overbuilding; the "
         "problem is fixed-wireless doesn't need to match speeds to take price-sensitive subs."),
        ("Scale in content purchasing and production. ",
         "NBCU's studio and parks portfolio diversifies the revenue base beyond connectivity."),
        ("Bundle economics. ",
         "Mobile + broadband bundles reduce churn and raise lifetime value — the best defense "
         "against fixed-wireless."),
        ("Counterweight: the moat is defending a shrinking castle. ",
         "Broadband subscriber losses are structural, and $85B of net debt means the equity "
         "absorbs every miss."),
    ],
    "risks": [
        ("Broadband subscriber acceleration. ",
         "Losses of ~142k/quarter could worsen as fixed-wireless and fiber overbuilds expand — "
         "the load-bearing assumption of the base case."),
        ("Leverage. ",
         "~$85B net debt vs ~$76.5B market cap: the equity is a levered claim on a no-growth "
         "business; small revenue misses compound into large equity misses."),
        ("Linear advertising decline. ",
         "The remaining networks and broadcast face structural ad erosion."),
        ("Dividend coverage. ",
         "The 4.3% yield is the thesis; a cut would destroy the investment case."),
        ("Content cyclicality. ",
         "Studios and parks are economically sensitive and capital-intensive."),
        ("Regulatory. ",
         "Broadband is a politically sensitive utility; price regulation is a perennial risk."),
    ],
    "falsification": "The dividend's coverage is the metric that matters: FCF falling below ~1.3x the "
        "dividend on a sustained basis — or management signaling a cut — would move us to SELL, "
        "because the yield is the reason to own the stock. Broadband quarterly losses accelerating "
        "materially beyond the recent ~140k pace would move us toward REDUCE. To the upside: "
        "broadband losses stabilizing below ~75k/quarter with wireless continuing to scale, or "
        "leverage falling below 2.5x on sustained FCF, would argue the harvest is more durable "
        "than the bear case allows.",
    "valuation_method": "10-year scenario FCFF DCF (levered-equity framework)",
    "valuation_intro": [
        "We value Comcast on a probability-weighted 10-year scenario DCF, weighted bear 25% / base "
        "50% / bull 25%, with scenario-specific discounts: bear 12.5% (base + 250bp), base 10.0%, "
        "bull 8.5% (base – 150bp). Terminal growth is -2.0% / +1.5% / +2.0% — the bear case "
        "explicitly models a declining perpetuity, which is the honest treatment for a "
        "structurally shrinking business. Net debt of ~$85B is subtracted in every scenario; with "
        "the debt larger than the market cap, the equity is a levered claim and the valuation "
        "range is correspondingly wide.",
        "The base case assumes revenue flat at ~$124B (0.0% CAGR — the honest number), terminal "
        "FCF margins of 12.1%, and a 10% discount: a harvest story priced as one, at $20.00 with "
        "TV 43% of EV. The bear ($1.03) is the declining-utility death spiral: -1.2% revenue CAGR, "
        "8.9% terminal margins, -2.0% terminal growth — the arithmetic of leverage when the top "
        "line shrinks. The bull ($44.55) assumes broadband stabilizes, wireless scales, and "
        "content over-delivers. The wide range is the point: this equity is an option on the "
        "decline being managed.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 1.03,
            "assumptions": "Declining-utility death spiral: broadband losses accelerate, -1.2% "
                "revenue CAGR, 8.9% terminal FCF margins, -2.0% terminal growth; leverage turns "
                "punitive.",
            "rev_cagr": "-1.2%", "margin_end": "8.9%",
            "discount": 0.125, "terminal_g": -0.020, "tv_share": round(M["bear"]["ts"], 2),
            "pv_explicit": COMP["bear"]["pv_explicit"],
            "pv_terminal": COMP["bear"]["pv_terminal"],
            "cashflow_unit": "$bn",
        },
        "base": {
            "fair_value": 20.00,
            "assumptions": "Managed decline: revenue flat at ~$124B, broadband bleed contained, "
                "wireless and business services grow, content holds the line; dividend maintained.",
            "rev_cagr": "+0.0%", "margin_end": "12.1%",
            "discount": 0.100, "terminal_g": 0.015, "tv_share": 0.43,
            "pv_explicit": COMP["base"]["pv_explicit"],
            "pv_terminal": COMP["base"]["pv_terminal"],
            "cashflow_unit": "$bn",
        },
        "bull": {
            "fair_value": 44.55,
            "assumptions": "Broadband stabilizes, Xfinity Mobile scales, Epic Universe and "
                "Peacock over-deliver; leverage falls and the equity re-rates on the harvest.",
            "rev_cagr": "+1.2%", "margin_end": "14.0%",
            "discount": 0.085, "terminal_g": 0.020, "tv_share": round(M["bull"]["ts"], 2),
            "pv_explicit": COMP["bull"]["pv_explicit"],
            "pv_terminal": COMP["bull"]["pv_terminal"],
            "cashflow_unit": "$bn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Probability-weighted DCF value is $21.39 "
        "(0.25×$1.03 + 0.50×$20.00 + 0.25×$44.55), rounded to our $21 target — essentially the "
        "current price, which is why this is a HOLD. Composition is on an EV basis; ~$85B of net "
        "debt is subtracted to reach equity fair value in every scenario. The wide scenario "
        "range is the levered-equity arithmetic, not model noise.",
    "charts": {
        "scenario": {"bear": 1.03, "base": 20.00, "bull": 44.55,
                     "weighted": 21.00, "price": 21.57},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [121.43, 121.57, 123.73, 123.71],
            "fcf_hist": [12.65, 12.96, 12.54, 19.23],
            "years_proj": list(range(2026, 2036)),
            "revenue_proj": base_revp,
            "fcf_proj": base_fcfp,
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: revenue and operating-CF-minus-capex (Yahoo; 2025 FCF boosted by "
                "working capital). Projection: the model's base-case 10-year path (flat revenue; "
                "FCF margin ~11-12%). Shaded = projection.",
        },
        "composition": {
            "bear": COMP["bear"], "base": COMP["base"], "bull": COMP["bull"],
            "unit": "$bn",
        },
        "extra": {
            "type": "pie",
            "labels": ["Connectivity & Platforms", "Content & Experiences"],
            "values": [70.0, 54.0],
            "title": "Post-Versant revenue mix (~$bn)",
        },
    },
}

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "output", "CMCSA-equity-research-note-polished.pdf")
    print(build_note(data, out))
