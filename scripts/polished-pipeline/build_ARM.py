"""Polished note: ARM (Arm Holdings) — SELL, FV $48.00, price $307.49 (Oct 2, 2026).

Authoritative source: the current rich research note (addendum_c PDF) plus the
scenario model (valuation_output_v2.json): bear $17.12 / base $46.34 / bull
$82.73, weighted $48.13 -> $48 target. Discounts bear 14.5% / base 12.0% /
bull 10.5%; terminal g 1.0% / 2.0% / 2.5%; rev CAGRs +5.3% / +16.1% / +20.7%;
yr-10 FCF margins 25.2% / 30.0% / 31.0%. Composition ($B): bear from the
model's TV share (26.6%); base calibrated to the note's stated 56% of EV;
bull from the model's TV share (60.2%). History: yfinance annuals
(FY2023–FY2026; fiscal year ends March 31). The standalone PDF ($48) matches
but the addendum_c PDF is the authoritative source.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

# Composition ($B): ~1.03 bn diluted ADS, net cash $3.9 bn.
# bear: equity 17.12 x 1.03 = 17.63; EV 13.73; TV 26.6% -> 3.65 / 10.08
# base: equity 46.34 x 1.03 = 47.73; EV 43.83; TV 56% (per note) -> 24.54 / 19.29
# bull: equity 82.73 x 1.03 = 85.21; EV 81.31; TV 60.2% -> 48.95 / 32.36

data = {
    "ticker": "ARM",
    "company": "Arm Holdings plc",
    "exchange": "NASDAQ",
    "sector": "Technology — Semiconductors (IP Licensing)",
    "verdict": "SELL",
    "fair_value": 48.00,
    "price": 307.49,
    "risk": "High",
    "headline": "Wonderful Business, Bubble Price — the Royalty Machine at 52x Sales",
    "hq": "Cambridge, United Kingdom",
    "snapshot": [
        ("Market cap", "~$313.6 bn (~1.03 bn dil. ADS x $307.49)"),
        ("Enterprise value", "~$309.7 bn"),
        ("Net cash", "~$3.9 bn"),
        ("52-week range", "~$100.02 - $452.70"),
        ("YTD / 1-yr return", "+181% / +101%"),
        ("FY26 revenue / royalty / license", "$4.92 bn / $2.61 bn / $2.31 bn"),
        ("Trailing P/E", "~300x"),
        ("ACV / RPO", "$1.73 bn (+13%) / $2.07 bn (-7%)"),
        ("Beta", "3.78"),
        ("Next catalyst", "Q2 FYE27 (Nov 4); Qualcomm trial (Oct 5)"),
    ],
    "thesis": [
        "We rate Arm SELL with a $48 price target, −84.3% below the $307.49 quote. This is not a call on "
        "the business, which is wonderful — 98% gross margins, 350 billion chips shipped, the instruction "
        "set inside nearly every smartphone on earth, and now the CPU architecture of the hyperscalers' "
        "custom AI silicon. It is a call on the price. At $307.49 the market values Arm at roughly 52x "
        "forward sales and ~300x trailing earnings. Our 10-year scenario DCF — bear $17.12 / base $46.34 / "
        "bull $82.73, weighted 25/50/25 — says even the bull case sits 73% below the quote. "
        "Reverse-engineering the price: it demands roughly $290 billion of FYE36 revenue, about twelve "
        "times the company's own $25 billion FYE31 bull plan and nearly sixty times this year's revenue. "
        "No plausible operating outcome bridges that gap.",
        "The temptation is to grant Arm a hypergrowth pass: AI is real, data-center royalties more than "
        "doubled last quarter, and the new AGI CPU chip — co-developed with Meta — has demand exceeding "
        "supply. We tested that temptation against the demand evidence and it fails, for a structural "
        "reason: Arm is an IP licensor, not a shovel-seller. Royalty revenue is earned when customers ship "
        "chips; there is no contracted chip backlog, no allocation queue, no take-or-pay volume. Arm's own "
        "remaining performance obligations were $2.07 billion — about 4.4 months of guided revenue, down 7% "
        "year over year — and the company has stopped reporting the metric, calling it 'less relevant to "
        "our growth.' A hypergrowth regime requires verifiable contracted demand covering well over a year "
        "of revenue; Arm has roughly a third of a year, shrinking. So years 1–3 are modeled at scenario "
        "growth rates with full skepticism, not at guidance: base 16.1% CAGR, bull 20.7% (which already "
        "haircuts the $25 billion FYE31 plan by cutting its $15 billion CPU contribution to $8 billion).",
        "The chart is the whole argument: the current price is off the scale of every scenario. In the bear "
        "case — handset softness, RISC-V share loss, an adverse Qualcomm outcome — revenue compounds 5.3% "
        "to $9.4 billion and the equity is worth $17.12; the bear sits 94% below the quote, as the rules "
        "require a bear that hurts. In the base case — Neoverse/CSS mix drives 16.1% compounding to $24.9 "
        "billion of FYE36 revenue at 30% FCF margins — fair value is $46.34. In the bull case — 20.7% "
        "compounding to $36.8 billion, AGI CPU ramping to plan — $82.73. Terminal value is 56% of base-case "
        "EV (no haircut required). The weighted $48.13 rounds to the $48 target.",
        "Cross-checks confirm the direction. Reverse DCF: justifying $307.49 at a 12% discount requires "
        "roughly $290 billion of FYE36 revenue — growing at ~49% a year for a decade, a pace no IP licensor "
        "has ever sustained. Multiples: ~52x forward sales and ~300x trailing earnings price Arm as if "
        "royalties were software subscriptions; they are cyclical, per-unit, and hostage to other "
        "companies' shipment volumes. Arm is a wonderful business and a terrible stock at $307.49. Do not "
        "own this above $100.",
    ],
    "thesis_subhead": "Why the business is wonderful — and why the price is the problem",
    "thesis_bullets": [
        ("The royalty flywheel is the best in semiconductors. ",
         "License fees today become per-unit royalties for the 20-year life of a chip family. Armv9 and "
         "Compute Subsystems carry higher royalty rates per chip than v8, so mix — not just units — drives "
         "royalty growth. Q1 FYE27: royalty revenue +22% to $715 million, license +23% to $574 million, "
         "both quarterly records."),
        ("Data center is genuinely inflecting. ",
         "Data-center royalty revenue more than doubled year over year as Arm Neoverse adoption accelerated. "
         "The hyperscalers' custom CPUs — AWS Graviton, Google Axion, Microsoft Cobalt — are Arm-based, and "
         "the AGI CPU co-developed with Meta carries more than $2 billion of customer demand across "
         "FYE27–28."),
        ("The Qualcomm trial starts October 5 — a live binary. ",
         "Qualcomm, one of Arm's largest royalty payers, alleges Arm breached its architecture license "
         "agreement; Arm disputes it. An adverse outcome threatens both a major royalty stream and the "
         "pricing power of the ALA program itself. This binary is unpriced at 300x earnings — and a "
         "favorable outcome is the clearest near-term upside risk to this SELL."),
        ("RISC-V is a slow bleed, not a sudden death. ",
         "The open ISA keeps winning sockets at the low end and in China, capping Arm's pricing power "
         "exactly where unit growth is fastest."),
    ],
    "business": [
        "Arm Holdings (founded 1990, Cambridge, UK; re-listed on Nasdaq in September 2023; "
        "majority-owned by SoftBank) does not sell chips. It licenses processor IP — CPU designs, the Arm "
        "instruction-set architecture, and increasingly full Compute Subsystems — to ~1,000 semiconductor "
        "partners, collecting an upfront license fee and then a per-unit royalty on substantially every chip "
        "shipped with Arm technology inside. Two revenue lines: royalty revenue ($2.613 billion in FY2026), "
        "driven by chip volumes and the mix shift to higher-rate Armv9/CSS designs; and license and other "
        "revenue ($2.307 billion in FY2026), driven by new architecture licenses and backlog conversion. "
        "Annualized contract value was $1.73 billion, +13% year over year.",
        "Fiscal 2026 (ended March 31, 2026) was a record: $4.92 billion of revenue, +23% year over year, "
        "non-GAAP diluted EPS of $1.77, non-GAAP free cash flow of $882 million. Q1 FYE27 (June quarter) set "
        "another record at $1.289 billion (+22%), with non-GAAP operating margin near 41%. The strategic "
        "pivot underway is from pure IP to production silicon: the AGI CPU, Arm's first own chip for cloud "
        "AI data centers, co-developed with Meta, with demand 'much higher than supply.' What Arm is not: "
        "it has no fabs, no chip inventory, and no order backlog in the semiconductor sense. Royalty revenue "
        "lags the capex cycle by design — Arm collects its few-dollars-per-socket royalty when the custom "
        "CPUs beside NVIDIA's and Broadcom's accelerators ship. Leverage to the AI buildout is real but "
        "derivative and lagged.",
    ],
    "business_bullets": [
        ("350 billion chips shipped; the ecosystem moat is unassailable. ",
         "Cumulative Arm-based shipments passed 350 billion in March 2026. Software toolchains, foundry "
         "enablement, and two decades of design wins compound into switching costs no open ISA can "
         "replicate quickly."),
        ("Fortress balance sheet, 98% gross margins. ",
         "~$3.9 billion of cash and short-term investments, negligible debt, GAAP gross margin 97.9%."),
        ("The x86 duopoly still owns the socket Arm is attacking. ",
         "Neoverse's share gains are real but start from a small base; Intel and AMD are counter-attacking "
         "with custom-silicon programs of their own."),
        ("SoftBank overhang and Arm China. ",
         "Majority ownership and the related-party China structure remain governance discounts the market "
         "applies intermittently — and with a beta of 3.78, this stock falls 3–4x as fast as the market "
         "when AI sentiment wobbles."),
    ],
    "outlook": [
        "Data-center royalties should keep compounding as Neoverse/CSS mix improves take rates, and the AGI "
        "CPU moves Arm from licensing IP to participating in production silicon economics. Our base case "
        "compounds revenue 16.1% to $24.9 billion by FYE36 at 30% FCF margins — a genuinely strong decade "
        "for an IP licensor.",
        "But none of it is contracted, and the price demands a decade of 49% annual revenue growth that no "
        "IP licensor has ever delivered. We revisit only on a decisive Qualcomm victory that reprices ALA "
        "royalty rates structurally upward, or a derating toward the base case.",
    ],
    "financials": [
        "Revenue grew from $2.68 billion in FY2023 to $4.92 billion in FY2026 — an 83% increase in three "
        "years — while net income rose from $524 million to $904 million. Free cash flow, however, is lumpy "
        "($646 million, $947 million, $158 million, $949 million), reflecting the working-capital and "
        "investment rhythms of the licensing model rather than any deterioration.",
        "The P&L quality is exceptional — 97.9% gross margins, ~41% non-GAAP operating margin even while "
        "R&D investment runs +33% — which is precisely why the business deserves admiration and the stock "
        "deserves a SELL. At 300x trailing earnings, every dollar of royalty is priced as though it were "
        "already collected for the next decade.",
    ],
    "fin_table": {
        "headers": ["$ bn", "FY2024", "FY2025", "FY2026"],
        "rows": [
            ["Revenue", "3.233", "4.007", "4.920"],
            ["Royalty revenue", "—", "—", "2.613"],
            ["License & other", "—", "—", "2.307"],
            ["Net income", "0.306", "0.792", "0.904"],
            ["Free cash flow", "0.947", "0.158", "0.949"],
        ],
        "footnote": "Source: company filings via yfinance; fiscal year ends March 31. Royalty/license "
                    "split per FY2026 20-F.",
    },
    "moat": [
        ("Wide in mobile/embedded — ecosystem, toolchains, 350-billion-unit installed base. ",
         "Switching costs no open ISA can replicate quickly; this is the durable core of the franchise."),
        ("Narrowing at the edges. ",
         "RISC-V and in-house ISAs compete exactly where the marginal unit growth lives — embedded, IoT, "
         "and China — capping take-rate expansion."),
        ("A complement, not a competitor, to NVIDIA. ",
         "In AI accelerators Arm rides alongside someone else's cycle — leverage to the AI buildout that "
         "is real but derivative, lagged, and hostage to another company's shipment volumes."),
        ("The moat does not justify 52x sales. ",
         "Wide moats command premium multiples; ~52x forward sales and ~300x trailing earnings price a "
         "scarcity premium on 'AI CPU exposure' with no earnings anchor."),
    ],
    "valuation_method": "10-year scenario FCFF DCF",
    "valuation_intro": [
        "Ten-year explicit free-cash-flow DCF, weights bear 25% / base 50% / bull 25%. The discount "
        "structure is priced for the risk: base 12.0% (beta 3.78, the Qualcomm litigation binary, RISC-V "
        "encroachment, SoftBank/Arm-China related parties), bear 14.5% (base + 250bp), bull 10.5% "
        "(base − 150bp). Terminal growth is capped at 1.0% / 2.0% / 2.5% on year-10 free cash flow at "
        "normalized margins — never peak margins. Equity = firm EV plus $3.9 billion of net cash, over "
        "~1.03 billion diluted ADS.",
        "Crucially, the model grants no hypergrowth exemption: the demand evidence does not support it "
        "(RPO of $2.07 billion is ~4.4 months of guided revenue, down 7% year over year, and the company "
        "has discontinued the disclosure), so years 1–3 grow at scenario rates with full skepticism, and "
        "the bull case already haircuts the $25 billion FYE31 plan. The bear case meets the hurt conditions "
        "and sits 94% below the current price.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 17.12,
            "assumptions": "Handset softness; RISC-V share gains; adverse Qualcomm outcome weakens ALA "
                           "pricing; revenue peaks in FY33 then declines; FCF margin 25% at yr-10",
            "rev_cagr": "+5.3%", "margin_end": "25%",
            "discount": 0.145, "terminal_g": 0.01, "tv_share": 0.266,
            "pv_explicit": 10.08, "pv_terminal": 3.65, "cashflow_unit": "$B",
        },
        "base": {
            "fair_value": 46.34,
            "assumptions": "Neoverse/CSS mix compounds ~20% early, fading to ~9% by yr-10; CPU a modest "
                           "second vector; FYE36 revenue $24.9 bn at 30% FCF margins",
            "rev_cagr": "+16.1%", "margin_end": "30%",
            "discount": 0.12, "terminal_g": 0.02, "tv_share": 0.56,
            "pv_explicit": 19.29, "pv_terminal": 24.54, "cashflow_unit": "$B",
        },
        "bull": {
            "fair_value": 82.73,
            "assumptions": "Haircut of the company plan (~$17 bn by FYE31), then fades to 9%; AGI CPU "
                           "ramps to plan; FYE36 revenue $36.8 bn at 31% FCF margins",
            "rev_cagr": "+20.7%", "margin_end": "31%",
            "discount": 0.105, "terminal_g": 0.025, "tv_share": 0.602,
            "pv_explicit": 32.36, "pv_terminal": 48.95, "cashflow_unit": "$B",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Scenario FVs from the note's model (bear $17.12 / base $46.34 / bull $82.73); "
                     "weighted $48.13, rounded to the $48 target. PV splits in $B; base-case terminal "
                     "value is 56% of EV (no haircut required).",
    "risks": [
        ("Qualcomm litigation (trial begins October 5, 2026). ",
         "An adverse ruling could impair a top royalty stream and reset ALA pricing power downward; a "
         "favorable one is the clearest near-term upside catalyst and the main risk to this SELL."),
        ("RISC-V encroachment. ",
         "Royalty-free ISAs keep winning embedded, IoT, and China sockets — the highest-unit-growth "
         "segments — pressuring Arm's take rate over time."),
        ("Handset cycle. ",
         "Smartphones remain the largest royalty base; elevated memory prices are pressuring device "
         "volumes and near-term royalty growth."),
        ("AI-sentiment beta. ",
         "At beta 3.78 and 300x earnings, any wobble in AI capex sentiment reprices the stock violently."),
        ("Production-silicon execution. ",
         "The AGI CPU moves Arm from licensing IP to competing with its own customers' chip programs; "
         "'demand exceeding supply' must convert to shipped, royalty-bearing volume."),
    ],
    "falsification": (
        "We would void the SELL on FYE36 revenue tracking at or above $24 billion with free-cash-flow "
        "margins at or above 34% — sustained top-of-bull execution for a decade — or a decisive Qualcomm "
        "victory that reprices ALA royalty rates structurally upward. Until the litigation resolves, there "
        "is no reason to pay 52x sales for a cyclical royalty stream."
    ),
    "charts": {
        "scenario": {"bear": 17.12, "base": 46.34, "bull": 82.73,
                     "weighted": 48.00, "price": 307.49},
        "trajectory": {
            "years_hist": [2023, 2024, 2025, 2026],
            "revenue_hist": [2.679, 3.233, 4.007, 4.920],
            "fcf_hist": [0.646, 0.947, 0.158, 0.949],
            "years_proj": [2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": [6.10, 7.50, 9.08, 10.80, 12.64, 14.54, 16.43, 18.24, 20.06, 21.86],
            "fcf_proj": [1.71, 2.25, 2.91, 3.67, 4.42, 5.23, 5.91, 6.20, 6.62, 7.00],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via yfinance; fiscal year ends March 31. Projection: "
                    "base-case path from this note's scenario DCF (16.1% revenue CAGR, FCF margins "
                    "normalizing to 30%).",
        },
        "composition": {
            "bear": {"pv_explicit": 10.08, "pv_terminal": 3.65},
            "base": {"pv_explicit": 19.29, "pv_terminal": 24.54},
            "bull": {"pv_explicit": 32.36, "pv_terminal": 48.95},
            "unit": "$B",
        },
        "extra": {
            "type": "line",
            "title": "Revenue — three scenario paths, FY27–FY36 ($bn)",
            "years": [2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "series": [
                {"label": "Bear — handset softness, adverse litigation",
                 "values": [5.81, 6.85, 7.67, 8.29, 8.70, 8.96, 9.05, 8.87, 8.60, 8.26]},
                {"label": "Base — Neoverse/CSS mix, 16.1% CAGR",
                 "values": [6.10, 7.50, 9.08, 10.80, 12.64, 14.54, 16.43, 18.24, 20.06, 21.86]},
                {"label": "Bull — haircut company plan, AGI CPU ramps",
                 "values": [6.30, 8.50, 11.05, 13.93, 16.99, 20.39, 23.65, 26.72, 29.66, 32.33]},
            ],
            "ylabel": "$bn",
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "ARM-equity-research-note-polished.pdf")
build_note(data, out)
print("built:", out)
