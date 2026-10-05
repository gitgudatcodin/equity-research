"""VST polished note. Research analysis, not investment advice.

Scenario numbers: authoritative v2 model (~/workspace/vst-research/valuation_v2_output.json + valuation_v2.py).
Bear $26.1 / base $123.6 / bull $212.2, weighted 121.5 -> $120 target.
Discounts: 12.5%/10%/8.5%; term g 1.5%/2.5%/2.0%; TV/EV 32.7%/47.4%/54.7%.
History: yfinance annuals. Projection: base-case model series (FY2027-2035).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

data = {
    "ticker": "VST",
    "company": "Vistra Corp.",
    "exchange": "NYSE",
    "sector": "Utilities — Independent Power Producer",
    "verdict": "REDUCE",
    "fair_value": 120.00,
    "price": 140.02,
    "risk": "Medium-High",
    "headline": "The Data-Center Power Trade — Priced for PPAs That Haven't Been Signed",
    "ceo": "Jim Burke",
    "hq": "Irving, Texas",
    "snapshot": [
        ("Market cap", "~$47 bn (~335M sh × $140.02)"),
        ("Net debt", "~$19 bn (Energy Harbor leverage)"),
        ("Enterprise value", "~$66 bn"),
        ("52-week range", "~$132.66 – $217.10"),
        ("Generation fleet", "~41 GW (nuclear, gas, coal, solar)"),
        ("Energy Harbor", "Acquired 2024 — nuclear baseload core"),
        ("Data-center angle", "Hyperscaler PPAs; PJM capacity prices surging"),
        ("Dividend / buyback", "Growing dividend; large buyback program"),
        ("Next catalyst", "Q3'26 results; new PPA announcements; PJM auction"),
    ],
    "thesis": [
        "Vistra is the purest public play on the AI era's most binding constraint — electricity. The "
        "company's ~41-gigawatt fleet, anchored by the Energy Harbor nuclear assets acquired in 2024, sells "
        "baseload power into markets where data-center demand is growing faster than new supply can be "
        "permitted and built. Hyperscalers are signing long-term power purchase agreements at prices that "
        "would have been unthinkable three years ago, and PJM capacity auction prices have surged on the "
        "same supply-demand imbalance. The strategic position is genuinely excellent. The stock at $140.02 "
        "is priced as though the excellent position were already fully contracted. It is not.",
        "Our judgment, and the reason this is a REDUCE, is that the market has capitalized a PPA pipeline "
        "that exists mostly in press releases. The data-center power thesis requires three things to "
        "compound for a decade: hyperscaler demand growing as projected, Vistra capturing a "
        "disproportionate share of the incremental contracting, and realized power prices holding at "
        "elevated levels rather than mean-reverting as new supply eventually arrives. All three are "
        "plausible; none is contracted. Our scenarios are $26 / $124 / $212, weighted to a $120 target, "
        "14.3% below the quote. The base case ($123.6) already assumes the good version: 3.0% revenue CAGR, "
        "data-center PPAs layering in through the decade, FCF margins holding in the low-20s. Even that "
        "good version is worth less than the current price.",
        "The bear case ($26.1) is the merchant-power cycle that the AI narrative has buried. Independent "
        "power producers are cyclical: when power prices fall — a mild winter, a demand disappointment, new "
        "supply clearing — revenue and margins compress simultaneously, and the ~$19 billion of net debt "
        "from the Energy Harbor acquisition turns operating leverage into financial leverage. Bear assumes "
        "0.5% revenue CAGR, power prices normalizing, and the data-center premium evaporating. This is not "
        "a stress-test invention; it is what merchant power has done in every prior cycle. At $140.02, "
        "investors are paying a growth multiple for a cyclical merchant generator at peak narrative.",
        "The forward view that matters: Vistra's nuclear baseload is a genuinely scarce, genuinely valuable "
        "asset in an electricity-short decade, and the company will likely sign meaningful data-center PPAs. "
        "But scarcity value accrues over decades, and the stock is pricing a decade of it in the next twelve "
        "months. We would own this fleet at a price that compensates for merchant cyclicality. That price "
        "is around $120, not $140. REDUCE into the AI-power enthusiasm; the electrons are real, the "
        "capitalization is premature.",
    ],
    "thesis_subhead": "Why the electrons are real and the price is premature",
    "thesis_bullets": [
        ("The fleet is genuinely scarce. ",
         "~41 GW anchored by Energy Harbor nuclear — baseload that cannot be built new on any relevant "
         "timeline. In an electricity-short decade, that scarcity has real option value."),
        ("But PPAs are announcements, not annuities. ",
         "The data-center power thesis requires a decade of hyperscaler contracting at elevated prices. "
         "Signed, long-tenor PPAs at attractive economics are the validation — and most of the "
         "pipeline is not yet signed."),
        ("Merchant cyclicality is the base rate. ",
         "Independent power producers are cyclical; ~$19B of net debt turns a power-price downturn "
         "into an equity event. The AI narrative does not repeal the merchant cycle."),
        ("The price is the bull case. ",
         "Our base case grants the good version — 3.0% CAGR, PPAs layering in — and is worth $123.6. "
         "The market at $140.02 is paying for the bull's $212.2 world."),
    ],
    "business": [
        "Vistra (Irving, Texas) is one of the largest independent power producers in the United States, "
        "operating ~41 gigawatts of generation — nuclear, natural gas, coal, and solar — plus a large retail "
        "electricity business (TXU Energy and others). The 2024 acquisition of Energy Harbor added "
        "~4 GW of nuclear baseload (including the Davis-Besse and Perry plants), transforming the fleet's "
        "carbon and cost profile and positioning the company as the natural counterparty for hyperscalers "
        "seeking clean, firm power.",
        "Fiscal 2025 produced revenue of $17.74 billion with free cash flow of $1.32 billion — the FCF "
        "number depressed by working capital and capex timing, a reminder of the business's lumpiness. "
        "Revenue history shows the merchant volatility plainly: $13.73B (2022), $14.78B (2023), $17.22B "
        "(2024, Energy Harbor), $17.74B (2025); free cash flow swung from −$0.82B to +$3.78B to +$2.48B to "
        "+$1.32B over the same period. This is not a steady-eddie utility; it is a merchant generator with "
        "a retail hedge.",
        "The forward picture is the data-center contracting story. Hyperscalers need firm, clean power on "
        "timelines that new build cannot meet; Vistra's nuclear and gas fleet can. Each long-term PPA signed "
        "at premium economics converts merchant volatility into contracted cash flow — the bull case's "
        "mechanism. But the conversion is gradual, the competition for hyperscaler contracts is intense "
        "(Constellation, Talen, and regulated utilities all bid), and realized economics depend on power "
        "prices that are currently elevated by the same imbalance the PPAs would lock in.",
    ],
    "business_bullets": [
        ("~41 GW fleet, nuclear-anchored. ",
         "Energy Harbor (2024) added ~4 GW of nuclear baseload — the scarce asset in the AI-power "
         "story; clean, firm, and unbuildable on relevant timelines."),
        ("Retail hedge (TXU Energy). ",
         "The retail book dampens merchant volatility but does not eliminate it — wholesale price "
         "swings still flow through."),
        ("Data-center PPA pipeline. ",
         "Hyperscaler contracting is the growth story; signed long-tenor PPAs at premium economics "
         "are the validation metric."),
        ("~$19B net debt. ",
         "Energy Harbor leverage turns the merchant cycle into a financial-leverage story on the "
         "downside."),
    ],
    "outlook": [
        "The next two years are about PPA announcements. Our base case runs revenue from $21.1 billion in "
        "FY2026 to $27.3 billion by 2035 — a 3.0% CAGR — with free cash flow compounding from $4.8 billion "
        "to $6.0 billion as data-center contracts layer in and margins hold in the low-20s. The near-term "
        "earnings are supported by elevated power prices and strong PJM capacity prices; the question is "
        "entirely about duration.",
        "The judgment call is whether the electricity shortage is a decade or a cycle. The bull case "
        "($212.2) assumes a decade: 4.1% revenue CAGR, hyperscaler demand compounding, Vistra capturing "
        "disproportionate share, power prices holding elevated indefinitely. Our view is more measured: "
        "electricity demand from data centers is real and durable, but new supply — gas turbines, "
        "uprates, batteries, and eventually new nuclear — does arrive, and power prices mean-revert. The "
        "bear case ($26.1) models the reversion arriving early: 0.5% revenue CAGR, the data-center premium "
        "evaporating, and $19 billion of debt amplifying the downside. Merchant power's history says the "
        "bear case is the base rate; the AI narrative says this time is different. We split the difference "
        "at 25% — and the price assigns it zero.",
        "What would change the call: signed, long-tenor PPAs at premium economics — actual contracts, not "
        "MOUs — would validate the bull's conversion thesis and we would revisit upward. A power-price "
        "normalization (mild weather, demand disappointment, supply clearing) would validate the bear and "
        "we would look to buy the fleet at cyclical prices. Watch: PPA announcements with disclosed "
        "tenor and pricing, PJM capacity auction results, and forward power curves.",
    ],
    "financials": [
        "The financial signature is merchant lumpiness: revenue $13.73B → $14.78B → $17.22B → $17.74B "
        "(2022–2025) looks steady, but free cash flow swung from −$0.82B to +$3.78B to +$2.48B to +$1.32B — "
        "the business converts unevenly and invests heavily. Our model normalizes this: FY2026E FCF of "
        "$4.77 billion on $21.09 billion of revenue (22.6% margin), compounding to $6.01 billion by 2035 "
        "as the PPA book builds. The base case assumes the lumpiness dampens; the bear case assumes it "
        "does not.",
        "The balance sheet is the risk: ~$19 billion of net debt against a ~$47 billion market cap — "
        "roughly 29% of enterprise value. In the base case the debt amortizes against contracted cash "
        "flows; in the bear case it is the mechanism that turns a power-price downturn into an equity "
        "event. The dividend is growing and the buyback program is large, but both are subordinate to "
        "deleveraging if the cycle turns. This is a Medium-High risk rating earned by leverage on top of "
        "merchant cyclicality.",
    ],
    "fin_table": {
        "headers": ["$ bn", "FY2022", "FY2023", "FY2024", "FY2025"],
        "rows": [
            ["Revenue", "13.73", "14.78", "17.22", "17.74"],
            ["YoY growth", "—", "+8%", "+17%*", "+3%"],
            ["Free cash flow", "−0.82", "3.78", "2.48", "1.32"],
            ["FCF margin", "−6.0%", "25.6%", "14.4%", "7.4%"],
            ["Net debt", "—", "—", "~$19", "~$19"],
        ],
        "footnote": "Sources: company filings; annuals via yfinance. *FY2024 includes the Energy Harbor "
                    "acquisition. FY2026E: $21.1B revenue, $4.8B FCF (model anchors).",
    },
    "moat": [
        ("Nuclear baseload scarcity. ",
         "Energy Harbor's reactors are clean, firm power that cannot be replicated on hyperscaler "
         "timelines — the structural asset in the AI-power story."),
        ("Scale and retail integration. ",
         "~41 GW of diversified generation plus the TXU retail book gives Vistra load-matching and "
         "hedging capabilities smaller IPPs cannot replicate."),
        ("The moat's limit is the commodity. ",
         "Electrons are fungible; in a power-price downturn, even nuclear fleets earn less. Scarcity "
         "value is real but cyclical."),
        ("Leverage as anti-moat. ",
         "~$19B of net debt means the equity's downside in a merchant downturn is amplified — the "
         "capital structure works against shareholders when the moat is tested."),
    ],
    "valuation_method": "10-year scenario DCF (FY2026–FY2035)",
    "valuation_intro": [
        "We value Vistra on a 10-year explicit DCF of free cash flow (FY2026–FY2035), weights bear 25% / "
        "base 50% / bull 25%. Scenario discounts: base 10.0% (contracted-cash-flow growth, merchant "
        "cyclicality, leverage), bear 12.5% (base + 250bp), bull 8.5% (base − 150bp). Terminal growth "
        "1.5% / 2.5% / 2.0% on year-10 FCF at through-cycle margins (19% / 22% / 24%) — never peaks. "
        "Revenue CAGRs: bear 0.5% (power-price normalization), base 3.0%, bull 4.1%. Equity = firm EV − "
        "~$19B net debt (EVs: $30.7B / $63.5B / $93.2B), over ~335M shares. Terminal value is 33–55% of "
        "EV across scenarios — within discipline, no haircut required.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 26.10,
            "assumptions": "Merchant-power reversion: power prices normalize, the data-center premium evaporates; 0.5% revenue CAGR; FCF margins compress to 19%; $19B of debt amplifies the equity downside",
            "rev_cagr": "+0.5%", "margin_end": "19%",
            "discount": 0.125, "terminal_g": 0.015, "tv_share": 0.327,
            "pv_explicit": 20.70, "pv_terminal": 10.04, "cashflow_unit": "$bn",
        },
        "base": {
            "fair_value": 123.60,
            "assumptions": "The good version: 3.0% revenue CAGR; data-center PPAs layer in through the decade; FCF margins hold in the low-20s; debt amortizes against contracted cash flows",
            "rev_cagr": "+3.0%", "margin_end": "22%",
            "discount": 0.10, "terminal_g": 0.025, "tv_share": 0.474,
            "pv_explicit": 33.42, "pv_terminal": 30.06, "cashflow_unit": "$bn",
        },
        "bull": {
            "fair_value": 212.20,
            "assumptions": "The electricity shortage is a decade: 4.1% revenue CAGR; hyperscaler demand compounds; Vistra captures disproportionate PPA share; power prices hold elevated; 24% terminal FCF margins",
            "rev_cagr": "+4.1%", "margin_end": "24%",
            "discount": 0.085, "terminal_g": 0.02, "tv_share": 0.547,
            "pv_explicit": 42.22, "pv_terminal": 51.00, "cashflow_unit": "$bn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "0.25×$26.1 + 0.50×$123.6 + 0.25×$212.2 = $121.5 → $120 target (rounded to the "
                     "published fair value). Bear meets all hurt conditions (price normalization, margin "
                     "compression, 25%+ derating).",
    "risks": [
        ("Power-price normalization (the #1 risk). ",
         "Merchant revenue follows power prices; a mild demand outcome or new supply clearing "
         "compresses revenue and margins simultaneously."),
        ("Leverage. ",
         "~$19B of net debt turns a merchant downturn into an equity event; deleveraging depends on "
         "the contracted cash flows materializing."),
        ("PPA execution. ",
         "The pipeline is mostly announcements; competition from Constellation, Talen, and regulated "
         "utilities is intense, and realized economics are unproven at scale."),
        ("New supply. ",
         "Gas turbines, uprates, batteries, and eventually new nuclear do arrive — the shortage is "
         "real but not permanent."),
        ("Regulatory / political. ",
         "Power markets are politically sensitive; capacity-market rule changes or price interventions "
         "can move economics quickly."),
        ("Retail margin pressure. ",
         "The TXU book hedges wholesale exposure but faces its own competitive and bad-debt dynamics."),
        ("Valuation. ",
         "At $140.02 the stock prices the bull case — any PPA disappointment or power-price softness "
         "reprices toward the base ($123.6)."),
    ],
    "falsification": (
        "The base case's PPA-conversion assumption would be withdrawn if no material long-tenor PPAs are "
        "signed over the next two quarters, or if forward power curves fall 20%+ — at that point the bear "
        "case ($26.1) becomes the working assumption. Conversely, signed long-tenor PPAs at disclosed "
        "premium economics would validate the bull path and we would revisit upward. Watch: PPA "
        "announcements (tenor and pricing disclosed), PJM capacity auction results, forward power curves."
    ),
    "methodology": [
        "We value the business on a 10-year explicit DCF of free cash flow (bear 25% / base 50% / bull 25%). "
        "Revenue follows the scenario path (bear 0.5% / base 3.0% / bull 4.1% 10-year CAGR, with "
        "power-price normalization in the bear case); free-cash-flow margin moves to the scenario's "
        "through-cycle margin (19% / 22% / 24%) over the horizon. Discount rates: base 10.0%, bear +250bp "
        "(12.5%), bull −150bp (8.5%). Terminal growth (1.5% / 2.5% / 2.0%) applies to year-10 FCF at the "
        "scenario's through-cycle margin. Equity = firm EV − ~$19B net debt; divided by ~335M shares. Bear "
        "cases must be genuinely adverse and sit below the current price. The published target is the "
        "probability-weighted fair value, stated as a 12-month horizon reference.",
        "Risk ratings (Low / Medium / Medium-High / High) combine business-model volatility, the balance "
        "sheet, and the valuation. This note is independent research-style analysis for informational purposes "
        "only and is not investment advice. Financial figures are drawn from company releases and SEC filings; "
        "market data as of October 2, 2026. Projections and the price target are the author's estimates and "
        "involve uncertainty. Past performance does not predict future results.",
    ],
    "charts": {
        "scenario": {"bear": 26.1, "base": 123.6, "bull": 212.2, "weighted": 121.5, "price": 140.02},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [13.73, 14.78, 17.22, 17.74],
            "fcf_hist": [-0.82, 3.78, 2.48, 1.32],
            "years_proj": [2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035],
            "revenue_proj": [21.93, 22.70, 23.50, 24.20, 24.93, 25.55, 26.19, 26.71, 27.25],
            "fcf_proj": [5.03, 5.27, 5.45, 5.62, 5.71, 5.78, 5.85, 5.96, 6.01],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via yfinance (note the merchant lumpiness in FCF). "
                    "Projection: base-case series from the scenario DCF (FY2026E anchor $21.1B revenue; "
                    "3.0% 10-yr CAGR; FCF margin in the low-20s).",
        },
        "composition": {
            "bear": {"pv_explicit": 20.70, "pv_terminal": 10.04},
            "base": {"pv_explicit": 33.42, "pv_terminal": 30.06},
            "bull": {"pv_explicit": 42.22, "pv_terminal": 51.00},
            "unit": "$bn",
        },
        "extra": {
            "type": "line",
            "title": "FCF margin — history vs. base-case normalization",
            "years": [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035],
            "series": [{"label": "FCF margin",
                        "values": [-6.0, 25.6, 14.4, 7.4, 22.6, 22.9, 23.2, 23.2, 23.2, 22.9, 22.6, 22.3, 22.3, 22.1]}],
            "ylabel": "%",
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "VST-equity-research-note-polished.pdf")
build_note(data, out)
print("built:", out)
