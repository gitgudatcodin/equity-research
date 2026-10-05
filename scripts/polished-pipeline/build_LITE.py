"""Polished note: LITE (Lumentum) — SELL, FV $255.00, price $1,085.42 (Oct 2, 2026).

Authoritative source: the current rich research note (addendum_c PDF) plus the
scenario model (lite_valuation_addendum_c.json): bear $85.60 / base $244.30 /
bull $447.40, weighted $255.40 -> $255 target. Discounts bear 14.5% / base
12.0% / bull 10.5%; terminal g 1.0% / 2.0% / 2.5%; rev CAGRs +4.3% / +12.1% /
+16.4%; yr-10 FCF margins 14% / 25% / 28%; TV/EV 25.6% / 41.3% / 50.2%.
Composition PV splits derived as TV-share x EV from the model. History:
yfinance annuals (FY2023–FY2026; fiscal year ends June 30). The pre-Addendum-C
standalone PDF ($355) is stale and was not used.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

# Composition ($mn) from the model: EV = equity - net cash ($2,588 mn).
# bear: EV 4,862; TV 25.6% -> pv_terminal 1,245, pv_explicit 3,617
# base: EV 18,665; TV 41.3% -> pv_terminal 7,709, pv_explicit 10,956
# bull: EV 36,333; TV 50.2% -> pv_terminal 18,239, pv_explicit 18,094

data = {
    "ticker": "LITE",
    "company": "Lumentum Holdings Inc.",
    "exchange": "NASDAQ",
    "sector": "Technology — Optical Components",
    "verdict": "SELL",
    "fair_value": 255.00,
    "price": 1085.42,
    "risk": "High",
    "headline": "Peak-Cycle Math at a Cyclical Peak",
    "hq": "San Jose, California",
    "snapshot": [
        ("Market cap", "~$94.4 bn (~87 mn dil. sh x $1,085.42)"),
        ("Enterprise value", "~$91.8 bn"),
        ("Net cash", "$2.588 bn (June 2026)"),
        ("52-week range", "~$147.81 - $1,091.61"),
        ("All-time high", "$1,085.75 (Oct 2, 2026)"),
        ("1-year return", "~+560%"),
        ("Q4 FY26 revenue", "$1.01 bn (+109% YoY)"),
        ("FQ1'27 revenue guide", "$1.225 - $1.275 bn"),
        ("Analyst consensus", "Moderate Buy; avg ~$1,073"),
        ("Next catalyst", "FQ1 FY27 results (Nov)"),
    ],
    "thesis": [
        "Lumentum qualifies for the hypergrowth-regime valuation framework this note uses — and this note "
        "gives it full credit. The demand evidence is verifiable, not narrative: pump lasers are effectively "
        "sold out despite rapid capacity expansion, with a fourfold shipment increase guided over coming "
        "quarters; pockets of supply-chain tightness capped shipments below total market demand in the June "
        "quarter; NVIDIA has made an ~$2 billion commitment to expand Lumentum's capacity and co-develop "
        "data-center optics; multiple long-term customer agreements underwrite the scale-across capex; and "
        "lead Tier-1 hyperscalers' custom AI cluster rollouts are driving the 800G-to-1.6T transition, with "
        "1.6T uptake expected to intensify from fiscal Q1 through calendar 2027. So years 1–3 run at or near "
        "the demand the evidence shows: FY2027 revenue of ~$5.8 billion, with no mechanical haircut.",
        "But Lumentum is the classic inventory-glut cyclical — customers double-order, then digest — and the "
        "framework concentrates all skepticism in the fade. That is the whole story of this note. Forward "
        "visibility ends in calendar 2027. Then comes digestion: in the base case a full down-cycle lands in "
        "FY2029–30 (revenue −11%, then −12%) before reaccelerating to a lower peak than the current cycle; in "
        "the bear case the digestion hits early and hard — FY2029 revenue collapses 28%, book-to-bill "
        "craters, EML prices reset as dual-sourcing bites, and free-cash-flow margins fall to 14%. Terminal "
        "value is computed on through-cycle margins (25% base, 28% bull, 14% bear) — never the 34–36% peaks "
        "the cycle is printing now.",
        "The arithmetic is unforgiving. Bear $86 / base $244 / bull $447, weighted (25/50/25) to $255 — "
        "76.5% below the $1,085.42 quote. Read that bull case twice: it assumes four to five years of "
        "runway, co-packaged optics shipping on schedule with a second hyperscaler win, and EML holding the "
        "200G/300G lanes against silicon photonics — flawless execution — and it is still 59% below the "
        "price. The $1,085 quote demands aspirational targets — a ~$2 billion quarterly run-rate, ~$40 of "
        "FY2028 EPS — as permanent through-cycle reality with no digestion, ever. That $40 of FY2028 EPS is "
        "~$3.5 billion of net income on ~87 million shares: roughly 45% net margins, sustained forever. No "
        "optical-component company has ever done that through a cycle.",
        "Note what the hypergrowth framework did here: it raised the near-term revenue path versus a "
        "mechanical haircut — and the fair value still lands three-quarters below the price, because the "
        "fade is the whole story and the price has no fade in it. Cross-check the street: the average "
        "analyst target (~$1,073) sits 4.2x our fair value; even the $1,220 high — 35x a $35 FY2028 EPS — "
        "capitalizes a peak-cycle earnings year at a growth multiple and calls it a target. That $35 is the "
        "top of the cycle talking. Sell into the euphoria; the digestion trade is a when, not an if.",
    ],
    "thesis_subhead": "Why the demand is real — and why the cycle always collects",
    "thesis_bullets": [
        ("The 1.6T transition runs through Lumentum's lasers. ",
         "Early 1.6T modules are heavily EML-based, and 1.6T requires 200G-per-lane EMLs — the component "
         "where Lumentum holds a near-monopoly. 200G EML products already exceed 25% of EML revenue; the "
         "company is on track for >50% EML unit growth by the December quarter."),
        ("Allocation is happening now. ",
         "Pump lasers effectively sold out; narrow-linewidth laser assemblies grew for a 10th straight "
         "quarter (+130% YoY); supply tightness capped June-quarter shipments below demand. Factories are "
         "executing against aggressive plans and still can't clear the order book."),
        ("Every optical cycle ends the same way. ",
         "Hyperscalers and module makers double-order in the ramp, build inventory, then stop ordering for "
         "2–4 quarters while they digest. Lumentum's own history — including the 2023 collapse — is the "
         "template. The June quarter's 109% growth is the ramp; the digestion is the bill."),
        ("1.6T economics invite competition. ",
         "Higher ASPs and 200G-lane leadership are exactly what pull in dual-sourcing and "
         "silicon-photonics alternatives. Early 1.6T is EML's window; the window is the asset, and windows "
         "close."),
    ],
    "business": [
        "Lumentum makes the light that moves AI data. Two product categories: Components — EML and "
        "continuous-wave lasers, pump lasers, narrow-linewidth laser assemblies — sold to transceiver and "
        "equipment makers; and Systems — cloud optical transceivers and optical circuit switches (OCS) — "
        "sold increasingly direct to hyperscalers. Cloud and AI infrastructure now account for the majority "
        "of revenue. The June quarter (Q4 FY2026) printed $1.01 billion of revenue (+109% YoY) and $3.23 of "
        "non-GAAP EPS (+267%), with record cloud transceiver shipments, record 100G/200G EML shipments, and "
        "the first production 1.6T shipments. The September-quarter guide is $1.225–$1.275 billion of "
        "revenue at 39.5–40.5% non-GAAP operating margin — past the company's target operating model more "
        "than a quarter ahead of schedule.",
        "Three growth vectors sit on top of the transceiver cycle. 1.6T: adoption intensifying from fiscal "
        "Q1 through calendar 2027, anchored by Tier-1 hyperscale custom AI clusters. Scale-across (OCS + "
        "high-power/pump lasers): OCS shipments doubled quarter-on-quarter with the first triple-digit OCS "
        "revenue quarter guided for September; ultra-high-power lasers targeted at ~$50 million of quarterly "
        "revenue by end of calendar 2026, with pump shipments guided up fourfold. Co-packaged optics: the "
        "generational bet — optical scale-up inside the rack replacing copper — with first shipments "
        "targeted for late 2027. The balance sheet was recapitalized mid-run: $2.7 billion of cash and "
        "short-term investments against $109.5 million of net debt; the convertible overhang equitized; a "
        "$7.2 billion one-time accounting charge — not an operating loss — cleared the decks. There is no "
        "refinancing wall. That matters for the bear case: the digestion destroys equity value, not the "
        "company.",
    ],
    "business_bullets": [
        ("Concentration cuts both ways. ",
         "A handful of Tier-1 hyperscalers drive the 1.6T transition; a single architecture decision (CPO "
         "timelines, lane-speed choices) reprices the whole franchise."),
        ("The convert exchange diluted holders ~7%. ",
         "$650 million of converts exchanged for ~5 million shares at elevated prices — a reminder that "
         "the capital structure flexes against shareholders when the stock runs."),
        ("CPO is the bull-case engine and a 2027 story at best. ",
         "Slips or qualification failures strand the growth narrative the price already owns."),
        ("At 156x trailing earnings the setup punishes any guide that is merely excellent. ",
         "The stock fell ~2% on the record June quarter — expectations, not results, are the risk."),
    ],
    "outlook": [
        "Forward visibility ends in calendar 2027. The base case prices the digestion honestly — a full "
        "down-cycle in FY2029–30 (−11%, then −12%) — then reaccelerates to a $9.4 billion FY2036 at 25% "
        "through-cycle FCF margins: a lower peak than the current cycle, which is what cycles do.",
        "The bull case — flawless CPO execution, second hyperscaler win, EML holding the lanes — is $447, "
        "still 59% below the quote. We revisit only on structural-cycle evidence: sustained >45% 200G EML "
        "share through FY2029 with stable ASPs (dual-sourcing disproven), or on-schedule CPO shipments with "
        "a second hyperscaler win.",
    ],
    "financials": [
        "Revenue collapsed from $1.77 billion in FY2023 to $1.36 billion in FY2024 — the last digestion — "
        "then inflected to $1.65 billion (FY2025) and $3.01 billion (FY2026): the current ramp in full. "
        "Free cash flow followed the cycle: +$51 million, −$112 million, −$105 million, +$300 million. "
        "FY2026 net income of −$6.9 billion is entirely the $7.2 billion one-time accounting charge, not an "
        "operating loss — the operating business printed record results.",
        "The balance sheet was recapitalized for the cycle: $2.7 billion of cash and short-term investments, "
        "$109.5 million of net debt, the convert overhang equitized. There is no refinancing wall to force "
        "selling into the digestion — which is why the bear case destroys equity value without destroying "
        "the company.",
    ],
    "fin_table": {
        "headers": ["$ bn", "FY2024", "FY2025", "FY2026"],
        "rows": [
            ["Revenue", "1.359", "1.645", "3.014"],
            ["Net income", "-0.546", "0.026", "-6.935"],
            ["Free cash flow", "-0.112", "-0.105", "0.300"],
        ],
        "footnote": "Source: company filings via yfinance; fiscal year ends June 30. FY2026 net income "
                    "includes a ~$7.2 bn one-time accounting charge — not an operating loss.",
    },
    "moat": [
        ("A near-monopoly in high-speed EMLs — for this window. ",
         "100G/200G-per-lane EML leadership plus deep indium-phosphide process know-how and entrenched "
         "Tier-1 hyperscaler qualification command pricing power during the ramp."),
        ("The moat is narrow and cycle-dependent. ",
         "Real advantages during the ramp; the threats arrive on schedule every cycle: Coherent in lasers "
         "and transceivers, Innolight and Zhongji Innolight in modules competing aggressively on price."),
        ("Silicon photonics is the structural threat. ",
         "The industry expects silicon photonics to dominate 1.6T over time as volumes scale and "
         "integration deepens. Early 1.6T is EML's window; windows close."),
        ("Dual-sourcing is not a risk to be modeled — it is the base case of every prior cycle. ",
         "Hyperscalers systematically second-source at volume; EML price resets are a when, not an if."),
    ],
    "valuation_method": "Hypergrowth-regime 10-year scenario FCFF DCF",
    "valuation_intro": [
        "A 10-year scenario free-cash-flow DCF (FY2027–FY2036; fiscal year ends June), weights bear 25% / "
        "base 50% / bull 25%. The company qualifies for hypergrowth-regime treatment on verifiable evidence "
        "— extended allocation (pump lasers sold out, shipments capped below demand), customer capacity "
        "commitments (NVIDIA's ~$2 billion, long-term scale-across agreements), and named hyperscaler "
        "capex driving the 800G-to-1.6T transition — so years 1–3 run at or near the demand evidence with "
        "no mechanical haircut. All skepticism is loaded into duration and fade: explicit "
        "supercycle-length assumptions per scenario, post-cycle margin compression, and terminal value on "
        "through-cycle FCF margins (never peak).",
        "Discounts: base 12% (cyclical optical = speculative tier), bear 14.5% (base + 250bp), bull 10.5% "
        "(base − 150bp); terminal growth 1.0% / 2.0% / 2.5%. Equity = firm EV plus $2.588 billion of net "
        "cash, over 87 million fully diluted shares. Terminal value is ≤50% of EV in every scenario (no "
        "haircut required).",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 86.00,
            "assumptions": "Digestion hits early FY28 (double-ordered 800G/EMLs); FY29 cliff −28% "
                           "revenue, book-to-bill collapse, EML price reset on dual-sourcing; "
                           "through-cycle FCF margins 14%",
            "rev_cagr": "+4.3%", "margin_end": "14%",
            "discount": 0.145, "terminal_g": 0.01, "tv_share": 0.256,
            "pv_explicit": 3617, "pv_terminal": 1245, "cashflow_unit": "$mn",
        },
        "base": {
            "fair_value": 244.00,
            "assumptions": "Hypergrowth FY27–28 per demand visibility; full down-cycle FY29–30 "
                           "(−11%, −12%); reacceleration to a lower peak; through-cycle FCF margins 25%",
            "rev_cagr": "+12.1%", "margin_end": "25%",
            "discount": 0.12, "terminal_g": 0.02, "tv_share": 0.413,
            "pv_explicit": 10956, "pv_terminal": 7709, "cashflow_unit": "$mn",
        },
        "bull": {
            "fair_value": 447.00,
            "assumptions": "4–5-year runway; CPO ships on schedule with a second hyperscaler win; EML "
                           "holds the 200G/300G lanes vs silicon photonics; through-cycle FCF margins 28%",
            "rev_cagr": "+16.4%", "margin_end": "28%",
            "discount": 0.105, "terminal_g": 0.025, "tv_share": 0.502,
            "pv_explicit": 18094, "pv_terminal": 18239, "cashflow_unit": "$mn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Scenario FVs from the note's model (bear $85.60 / base $244.30 / bull $447.40); "
                     "0.25x$86 + 0.50x$244 + 0.25x$447 = $255.40, rounded to the $255 target. PV splits "
                     "in $mn derived as TV-share x EV from the scenario DCF.",
    "risks": [
        ("Inventory digestion (the #1 risk). ",
         "Customers stop ordering for 2–4 quarters and work through double-ordered stock. It has happened "
         "every prior optical cycle, including 2023."),
        ("Dual-sourcing and silicon photonics. ",
         "Hyperscalers systematically second-source at volume; silicon photonics is expected to take share "
         "in 1.6T over time. Either compresses EML pricing faster than modeled."),
        ("Customer concentration. ",
         "A handful of Tier-1 hyperscalers drive the 1.6T transition; one architecture decision reprices "
         "the franchise."),
        ("CPO execution. ",
         "Co-packaged optics is the bull-case engine and a 2027 story at best; slips strand the growth "
         "narrative the price already owns."),
        ("Supply-chain whiplash. ",
         "Tightness today can invert to glut with one quarter's notice — the two states are adjacent in "
         "this industry, not opposite."),
    ],
    "falsification": (
        "The hypergrowth provision is revoked if book-to-bill prints below 1.0 for two consecutive "
        "quarters or lead times normalize (allocation ends): the model reverts to standard treatment and "
        "fair value falls further toward ~$180. The SELL itself is raised only on evidence the "
        "cycle is structurally different this time: sustained >45% 200G EML share through FY2029 with "
        "stable ASPs (dual-sourcing disproven), or on-schedule CPO shipments with a second hyperscaler win. "
        "Absent that, the digestion thesis stands."
    ),
    "charts": {
        "scenario": {"bear": 86.00, "base": 244.00, "bull": 447.00,
                     "weighted": 255.00, "price": 1085.42},
        "trajectory": {
            "years_hist": [2023, 2024, 2025, 2026],
            "revenue_hist": [1.767, 1.359, 1.645, 3.014],
            "fcf_hist": [0.051, -0.112, -0.105, 0.300],
            "years_proj": [2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": [5.8, 7.6, 6.8, 6.0, 6.6, 7.4, 8.0, 8.5, 9.0, 9.4],
            "fcf_proj": [1.39, 2.28, 2.18, 1.68, 1.58, 1.85, 2.08, 2.21, 2.34, 2.35],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via yfinance; fiscal year ends June 30. Projection: "
                    "base-case path from this note's scenario DCF — hypergrowth FY27–28, full "
                    "digestion FY29–30, reacceleration to a lower peak.",
        },
        "composition": {
            "bear": {"pv_explicit": 3617, "pv_terminal": 1245},
            "base": {"pv_explicit": 10956, "pv_terminal": 7709},
            "bull": {"pv_explicit": 18094, "pv_terminal": 18239},
            "unit": "$mn",
        },
        "extra": {
            "type": "line",
            "title": "Revenue — three scenario paths, FY27–FY36 ($bn)",
            "years": [2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "series": [
                {"label": "Bear — early digestion, FY29 cliff −28%",
                 "values": [5.5, 5.0, 3.6, 3.2, 3.4, 3.8, 4.1, 4.3, 4.5, 4.6]},
                {"label": "Base — digestion FY29–30, lower re-peak",
                 "values": [5.8, 7.6, 6.8, 6.0, 6.6, 7.4, 8.0, 8.5, 9.0, 9.4]},
                {"label": "Bull — 4–5 yr runway, CPO on schedule",
                 "values": [6.0, 8.2, 8.8, 9.4, 10.2, 11.0, 11.8, 12.6, 13.2, 13.8]},
            ],
            "ylabel": "$bn",
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "LITE-equity-research-note-polished.pdf")
build_note(data, out)
print("built:", out)
