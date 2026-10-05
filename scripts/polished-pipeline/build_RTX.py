"""Polished note: RTX Corporation (RTX) — SELL, fair value $120.00.

Scenario numbers are from the current 10-year scenario DCF model
(valuation_v2.json): bear $32.0 / base $126.0 / bull $190.0, weighted 25/50/25
to $118.0, rounded to the $120 target. Discounts 11.5%/9%/8%; terminal growth
1.75%/2.5%/2.5%; revenue CAGR 1.9%/5.7%/6.9%; year-10 FCF margins 7.0%/10.5%/
11.5%; terminal-value share of EV 39.2%/58.3%/64.6% on EV of $72.4B/$199.2B/
$285.4B. Composition PVs reconcile exactly to those model outputs.
History: company filings via Yahoo Finance (Oct 2026); the base-case
projection series is from the model (revenue $99.0B->$187.7B, FCF $7.5B->
$19.7B over ten years). All prose is fresh October 4, 2026 analysis.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note, validate

data = {
    "ticker": "RTX",
    "company": "RTX Corporation",
    "exchange": "NYSE",
    "sector": "Industrials — Aerospace & Defense",
    "verdict": "SELL",
    "fair_value": 120.00,
    "price": 184.68,
    "risk": "Medium",
    "headline": "The recovery is real — and fully priced",
    "ceo": "Chris Calio",
    "hq": "Arlington, Virginia",
    "snapshot": [
        ("Market cap", "~$249 bn (1.35 bn sh × $184.68)"),
        ("52-week range", "~$156 – $227"),
        ("Price / fair value", "$184.68 / $120.00"),
        ("Implied downside", "−35.0%"),
        ("Backlog", "$241 bn (company-disclosed)"),
        ("FQ2 FY26 revenue / adj. EPS", "$23.0 bn (+12%) / $1.78 (+27%)"),
        ("Full-year guide (raised)", "Adj. EPS $6.10–$6.25; sales $86.5–$87.5 bn"),
        ("Commercial growth drivers", "Pratt GTF shipments +25–30% in FY26; defense book-to-bill 1.2x"),
        ("Tariff drag (est.)", "~$1.0 bn gross impact (mitigated via pricing/supply actions)"),
        ("Next catalyst", "FQ3 FY26 earnings (late October)"),
        ("Sell-side view", "Mixed: Buy 12 / Hold 13 / Sell 0"),
    ],
    "thesis": [
        "RTX is executing its recovery well — FQ2 2026 beat on revenue (+12% to $23.0B), "
        "adjusted EPS (+27% to $1.78), and free cash flow, the full-year guide was raised "
        "again, and the $241B backlog is the largest in company history. None of that is "
        "in dispute. What is in dispute is whether any of it justifies $184.68 a share, "
        "and our answer is no: the scenario DCF lands at $120 — bear $32, base $126, bull "
        "$190 — with 35% downside even in a base case that assumes demand normalization, "
        "a full aftermarket recovery, and defense budgets sustained by the NATO 5% "
        "spending pledge. The recovery is real. It is also fully priced.",
        "The core of the SELL is the structure of the cash flows, not the headline "
        "growth. Commercial aerospace profits arrive through two channels with very "
        "different economics: original-equipment engine sales, which are sold near "
        "cost (and sometimes below it) to win the 30-year aftermarket annuity, and "
        "aftermarket parts and services, where the margins live. As GTF and other new-"
        "engine shipments ramp 25–30% in FY2026, the OE mix drags on reported margins "
        "while the aftermarket that would offset it is still normalizing — flight hours "
        "have normalized, but shop-visit economics on the newest engine generations take "
        "years to mature. Our base case assumes that recovery completes; the valuation "
        "still doesn't clear the quote.",
        "Meanwhile the defense side — roughly half the portfolio through Raytheon — "
        "grows on budgets, not on moats, and the risks to the downside are "
        "structurally underpriced. The GTF powdered-metal issue remains a live "
        "execution overhang with fleet-management costs still being recognized; the "
        "IAM labor situation is unresolved; a ~$1.0B gross tariff impact is being "
        "'mitigated' through pricing that customers can only absorb for so long; and "
        "the balance sheet carries $32B of net debt against a $10.9B pension deficit "
        "with interest coverage of 1.8x. In the bear case — protracted aftermarket "
        "weakness, defense spending cuts, GTF overhang — fair value is $32. The bull "
        "case ($190, sustained double-digit aftermarket growth and elevated defense "
        "budgets) barely clears the current quote. When the bull case is the price, "
        "there is no margin of safety left to buy. SELL.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("OE mix is the margin story the headline hides. ",
         "New-engine shipments ramping 25–30% are sold at thin or negative margins to "
         "win decades of aftermarket annuities. The P&L absorbs the dilution now; the "
         "payback arrives years later — a timing mismatch the current multiple ignores."),
        ("The GTF powdered-metal issue is not closed. ",
         "Fleet-management costs and shop-visit capacity constraints continue to absorb "
         "cash and management attention. Engine programs at this scale do not have "
         "clean endings."),
        ("Defense growth is budget growth. ",
         "The NATO 5% pledge and a 1.2x book-to-bill support the bull case — but budgets "
         "are political, cyclical, and currently at historic highs. The bear case prices "
         "what happens when they normalize."),
    ],
    "business": [
        "RTX is the world's largest aerospace-and-defense company by revenue, organized "
        "in three segments. Collins Aerospace (avionics, interiors, mission systems) is "
        "the broadest commercial aftermarket franchise in the industry. Pratt & Whitney "
        "builds the Geared Turbofan (GTF) engine family powering the A320neo — the "
        "growth engine of the portfolio and its largest execution risk. Raytheon "
        "(missiles, air defense including Patriot, radars, space systems) is the defense "
        "half, levered to US and allied defense budgets.",
        "The business model is the classic aerospace razor-and-blade: engines and "
        "systems are sold at thin margins to secure decades of high-margin aftermarket "
        "parts, repairs, and overhauls. That model is currently in its most dilutive "
        "phase — record new-engine deliveries depressing near-term margins while the "
        "aftermarket annuities they secure mature years later. Collins' aftermarket "
        "exposure (roughly two-thirds of its profit) is the highest-quality earnings "
        "stream in the portfolio; Raytheon's are the most politically determined.",
        "Capital allocation is straightforward: the dividend and buyback are funded from "
        "free cash flow after the pension and debt service. The balance sheet is the "
        "constraint — $32B of net debt and a $10.9B pension deficit leave limited room "
        "for the kind of large capital returns that support the multiple at cyclical "
        "peaks.",
    ],
    "business_bullets": [
        ("Pratt & Whitney GTF: growth engine and overhang. ",
         "Shipments up 25–30% in FY2026; the powdered-metal fleet-management issue "
         "continues to consume cash and shop capacity. The aftermarket annuity is real — "
         "it just matures years after the OE dilution."),
        ("Collins aftermarket: the quality compounder. ",
         "Avionics, interiors, and mission systems with ~2/3 of profit from aftermarket "
         "— the most defensible, highest-margin earnings in the company."),
        ("Raytheon: budget beta. ",
         "Patriot, missiles, and radars ride allied rearmament (NATO 5% pledge, 1.2x "
         "book-to-bill). Growth is real; the multiple on budget-driven earnings should "
         "not be a growth multiple."),
        ("The installed base is the moat; the cycle is the limit. ",
         "Certification barriers and 30-year service relationships lock in the "
         "aftermarket — but every one of those annuities was sold during an upcycle, "
         "and shop-visit economics are only as good as flight hours."),
    ],
    "outlook": [
        "The next two years are underwritten by the backlog: $241B of contracted work, "
        "commercial deliveries ramping, and defense book-to-bill at 1.2x. Our base case "
        "assumes demand normalization completes — aftermarket fully recovered, commercial "
        "OE deliveries growing, defense budgets sustained — with revenue compounding at "
        "5.7% for ten years (from $88.6B in FY2025 toward ~$188B) and free-cash-flow "
        "margins expanding from today's ~8% to 10.5% at year ten as the OE mix "
        "normalizes and GTF aftermarket matures. Even under those friendly assumptions, "
        "fair value is $126 — 32% below the quote.",
        "The bull case ($190) requires sustained double-digit aftermarket growth, the "
        "engine production ramp executing cleanly, and defense budgets staying elevated "
        "on the NATO pledge through the decade — 6.9% revenue CAGR, 11.5% FCF margins. "
        "It barely clears $184.68. The bear case ($32) is the cycle turning: protracted "
        "aftermarket weakness as flight-hour growth stalls, defense spending cuts after "
        "the rearmament surge, and the GTF overhang proving larger than reserved — 1.9% "
        "CAGR, 7.0% FCF margins, a 1.75% terminal growth rate on derated earnings.",
        "Watch the falsification markers: sustained book-to-bill above 1.0 in both "
        "commercial and defense, expanding segment margins (proof the OE mix drag is "
        "abating), management confirming the 2026 free-cash-flow outlook, GTF "
        "aftermarket profitability normalizing, no material labor disruption, and "
        "continued geopolitical support for defense budgets. If those all print "
        "together for several quarters, the SELL is wrong and the bull case takes over. "
        "Today, the price assumes they already have.",
    ],
    "financials": [
        "FQ2 2026 was a genuine beat: revenue $23.0B (+12%), adjusted EPS $1.78 (+27%), "
        "free cash flow $1.9B, with the full-year guide raised to adjusted EPS of "
        "$6.10–$6.25 on sales of $86.5–$87.5B. Annual revenue has grown from $67.1B in "
        "FY2022 to $88.6B in FY2025; free cash flow (operating cash flow less capex) "
        "reached $7.45B in FY2025 after dipping to $3.92B in FY2024 on working-capital "
        "and program timing. The trajectory from here is margin-led: our base case "
        "expands FCF margins from ~8% toward 10.5% over ten years.",
        "The balance sheet is the quiet constraint on the bull case. Net debt of $32.0B "
        "sits against a $10.9B pension deficit with interest coverage of just 1.8x — "
        "thin for a cyclical industrial at what may be peak defense budgets. Valuation "
        "composition reflects the quality of the out-years: terminal value is 58% of "
        "base-case enterprise value ($199.2B), 65% in the bull ($285.4B), and only 39% "
        "in the bear ($72.4B). More than half the base-case value lives in the "
        "terminal year — appropriate for an annuity business, but it means the $184.68 "
        "price is a bet on the perpetuity, not the next three years.",
    ],
    "fin_table": {
        "headers": ["", "FY2022", "FY2023", "FY2024", "FY2025", "FQ2 FY26"],
        "rows": [
            ["Revenue ($bn)", "67.1", "68.9", "80.7", "88.6", "23.0"],
            ["Free cash flow ($bn)", "4.40", "4.71", "3.92", "7.45", "1.9"],
            ["FCF margin", "6.6%", "6.8%", "4.9%", "8.4%", "—"],
            ["Backlog ($bn)", "—", "—", "—", "—", "241"],
            ["Net debt ($bn) / pension deficit ($bn)", "—", "—", "—", "32.0 / 10.9", "—"],
        ],
        "footnote": "Annual figures from company filings via Yahoo Finance (FCF = "
                    "operating cash flow less capex). FQ2 FY26 and backlog from the "
                    "July 2026 earnings release. Balance-sheet figures as of mid-2026.",
    },
    "moat": [
        ("Certification and installed-base lock-in. ",
         "Engines and avionics certified on airframes for 30+ years; switching an "
         "installed fleet is economically prohibitive. The aftermarket annuity is the "
         "moat."),
        ("Duopoly structures in the key franchises. ",
         "GTF/LEAP split the narrowbody engine market; Patriot dominates its air-defense "
         "segment. Competitors exist but cannot displace installed positions."),
        ("Scale in aftermarket services. ",
         "The global MRO network and parts distribution create density advantages new "
         "entrants cannot replicate quickly."),
        ("The moat's limits: the mirror duopoly and program risk. ",
         "GE/Safran match Pratt engine-for-engine; defense contracts re-compete on "
         "politics as much as performance; and single programs (GTF powdered metal) can "
         "absorb billions. The moat protects the franchise — it does not protect the "
         "multiple."),
    ],
    "valuation_method": "10-year scenario DCF",
    "valuation_intro": [
        "We value RTX on a 10-year scenario discounted-cash-flow framework, weighted "
        "25% / 50% / 25%. Discount rates are scenario-specific — bear 11.5%, base 9%, "
        "bull 8% — reflecting a cyclical industrial with defense-budget exposure, "
        "program execution risk (GTF), labor overhang, and a levered balance sheet "
        "($32B net debt, $10.9B pension deficit, 1.8x interest coverage). Terminal "
        "growth is 1.75% in the bear case and 2.5% in the base and bull cases, applied "
        "to year-10 free cash flow at normalized margins — never peak margins.",
        "Scenario fair values: $32.0 (bear — protracted aftermarket weakness, defense "
        "spending cuts, GTF overhang; 1.9% revenue CAGR, 7.0% year-10 FCF margins) / "
        "$126.0 (base — demand normalization, aftermarket recovery, sustained defense "
        "budgets; 5.7% CAGR, 10.5% margins) / $190.0 (bull — sustained double-digit "
        "aftermarket growth, clean engine ramp, elevated defense budgets; 6.9% CAGR, "
        "11.5% margins). The probability-weighted value is $118.0; our published "
        "target rounds to $120 — 35.0% below the $184.68 quote. Terminal value is 58% "
        "of base-case EV: more than half the value sits in the perpetuity, which is "
        "exactly what the current price is paying for.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 32.00,
            "assumptions": ("Protracted aftermarket weakness; defense spending cuts "
                            "after the rearmament surge; GTF overhang larger than "
                            "reserved; 1.9% revenue CAGR; 7.0% year-10 FCF margin."),
            "rev_cagr": "+1.9%", "margin_end": "7.0%",
            "discount": 0.115, "terminal_g": 0.0175, "tv_share": 0.392,
            "pv_explicit": 44.02, "pv_terminal": 28.38, "cashflow_unit": "$bn",
        },
        "base": {
            "fair_value": 126.00,
            "assumptions": ("Demand normalization completes; aftermarket fully "
                            "recovered; commercial OE deliveries grow; defense budgets "
                            "sustained; 5.7% revenue CAGR; 10.5% year-10 FCF margin."),
            "rev_cagr": "+5.7%", "margin_end": "10.5%",
            "discount": 0.09, "terminal_g": 0.025, "tv_share": 0.583,
            "pv_explicit": 83.07, "pv_terminal": 116.13, "cashflow_unit": "$bn",
        },
        "bull": {
            "fair_value": 190.00,
            "assumptions": ("Sustained double-digit aftermarket growth; clean engine "
                            "production ramp; defense budgets elevated on NATO pledge; "
                            "6.9% revenue CAGR; 11.5% year-10 FCF margin."),
            "rev_cagr": "+6.9%", "margin_end": "11.5%",
            "discount": 0.08, "terminal_g": 0.025, "tv_share": 0.646,
            "pv_explicit": 101.03, "pv_terminal": 184.37, "cashflow_unit": "$bn",
        },
    },
    "scenario_note": "Composition PVs reconcile to the model's enterprise values "
                     "($72.4B / $199.2B / $285.4B) via the stated terminal-value shares "
                     "(39.2% / 58.3% / 64.6%).",
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "risks": [
        ("Commercial cycle (High). ",
         "Aftermarket profits track flight hours and shop visits; a demand downturn "
         "hits the highest-margin earnings first while OE commitments continue."),
        ("GTF program execution (High). ",
         "The powdered-metal fleet-management issue continues to absorb cash and shop "
         "capacity; further findings would extend the overhang."),
        ("Defense budget normalization (Medium-High). ",
         "Roughly half the portfolio grows on budgets at historic highs; the NATO 5% "
         "pledge is political, not contracted."),
        ("Labor (Medium). ",
         "The IAM situation is unresolved; aerospace labor actions have historically "
         "cost quarters of delivery and margin."),
        ("Tariffs and supply chain (Medium). ",
         "~$1.0B gross tariff impact being mitigated through pricing — absorption "
         "capacity is finite, and rare-earth/export-control exposure sits in missile "
         "components."),
        ("Balance sheet (Medium). ",
         "$32B net debt, $10.9B pension deficit, 1.8x interest coverage — thin for a "
         "cyclical at potential peak budgets; limits capital returns that support the "
         "multiple."),
    ],
    "falsification": (
        "We would revisit the SELL if, over several consecutive quarters: book-to-bill "
        "holds above 1.0 in both commercial and defense, segment margins expand "
        "(evidence the OE mix drag is abating), management confirms the 2026 "
        "free-cash-flow outlook, GTF aftermarket profitability normalizes with the "
        "fleet-management issue demonstrably behind, no material labor disruption "
        "occurs, and geopolitical developments continue to support defense budgets. "
        "That combination is the bull case ($190), and it would have to arrive together "
        "— a single strong quarter on backlog conversion alone does not change the "
        "valuation math. We watch: book-to-bill by segment, OE vs. aftermarket margin "
        "mix, GTF shop-visit economics, labor negotiations, and defense appropriations."
    ),
    "methodology": [
        "We value RTX on a 10-year scenario discounted-cash-flow framework. Revenue "
        "compounds from the current base under scenario-specific CAGRs (1.9% bear, "
        "5.7% base, 6.9% bull); free-cash-flow margins glide from current levels to "
        "scenario terminal margins (7.0% / 10.5% / 11.5%) as the OE mix normalizes and "
        "aftermarket matures. Scenarios are probability-weighted 25% / 50% / 25%.",
        "Discount rates are scenario-specific — 11.5% bear, 9% base, 8% bull — and "
        "terminal growth is 1.75% (bear) / 2.5% (base, bull), applied to year-10 free "
        "cash flow at normalized margins. The bear case is required to be genuinely "
        "adverse and to sit below the current price; terminal value exceeding 70% of "
        "enterprise value is haircut and disclosed (58% base, 65% bull, 39% bear — no "
        "haircut required). We cross-check against trough-cycle earnings multiples.",
        "The published target is the probability-weighted fair value rounded to a "
        "round number ($118.0 → $120), stated as a 12-month horizon reference. Risk "
        "ratings (Low / Medium / Medium-High / High) combine business volatility, "
        "balance-sheet strength, and valuation; Medium here reflects the annuity-like "
        "installed base against cyclical, budget-driven, and program-concentrated "
        "earnings.",
    ],
    "charts": {
        "scenario": {"bear": 32.00, "base": 126.00, "bull": 190.00,
                     "weighted": 120.00, "price": 184.68},
        "trajectory": {
            # history: filings via Yahoo Finance; FCF = OCF - capex
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [67.07, 68.92, 80.74, 88.60],
            "fcf_hist": [4.40, 4.71, 3.92, 7.45],
            # base-case projection from the model
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035],
            "revenue_proj": [99.0, 108.1, 117.5, 127.2, 136.8, 147.0, 157.2, 168.0, 178.2, 187.7],
            "fcf_proj": [7.5, 9.2, 10.6, 11.9, 13.0, 14.2, 15.4, 16.6, 17.9, 19.7],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via Yahoo Finance (FCF = operating cash "
                    "flow less capex). Projection: base-case model path — revenue "
                    "compounding at 5.7% with FCF margins expanding toward 10.5% as the "
                    "OE mix normalizes and GTF aftermarket matures.",
        },
        "composition": {
            "bear": {"pv_explicit": 44.02, "pv_terminal": 28.38},
            "base": {"pv_explicit": 83.07, "pv_terminal": 116.13},
            "bull": {"pv_explicit": 101.03, "pv_terminal": 184.37},
            "unit": "$bn",
        },
        "extra": {
            "type": "line",
            "title": "Free-cash-flow margin: history and base-case path",
            "years": [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035],
            "series": [{"label": "FCF margin (%)",
                        "values": [6.6, 6.8, 4.9, 8.4, 7.6, 8.5, 9.0, 9.4, 9.5, 9.7, 9.8, 9.9, 10.1, 10.5]}],
            "ylabel": "%",
            "note": "The margin-led recovery: FCF margins expanding from ~8% toward "
                    "10.5% as the OE mix normalizes. History from filings; projection "
                    "from the base-case model.",
        },
    },
}

validate(data)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "RTX-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
