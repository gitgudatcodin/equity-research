"""Polished note: RGTI (Rigetti Computing) — SELL, FV $5.00, price $15.25 (Oct 2, 2026).

Sources: standalone PDF (valuation + prose) and valuation_output_v2.json
(scenario FVs bear $0.00 / base $3.52 / bull $13.33; WACC 18.5%/16%/14.5%;
terminal g 0%/1.0%/2.5%; norm FCF margins 12%/20%/25%; rev CAGRs
15%/58.8%/70.3%; base TV 79% of EV).
Weighted model value $5.09 -> $5.00 target (library). History: yfinance
annuals (FY2022–FY2025). Composition: base from the model's stated TV share
(79% of EV); bull TV derived from the model's own bull parameters
(rev2035 $5,000 mn x 25% FCF margin, 14.5% discount, 2.5% terminal g);
bear floored at $0 (limited liability) per the model.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

# Composition ($mn): base equity 3.52 x 400 = 1,408; EV 867 (less $541 net cash);
#   TV 79% -> pv_terminal 685, pv_explicit 182.
# bull equity 13.33 x 380 = 5,065; EV 4,524; Gordon terminal on bull params:
#   5,000 x 25% x 1.025 / (0.145-0.025) / 1.145^10 = 2,775 -> tv 61%.
# bear: floored at $0 (limited liability) — no composition.

data = {
    "ticker": "RGTI",
    "company": "Rigetti Computing, Inc.",
    "exchange": "NASDAQ",
    "sector": "Technology — Quantum Computing",
    "verdict": "SELL",
    "fair_value": 5.00,
    "price": 15.25,
    "risk": "High",
    "headline": "A Pre-Revenue Science Project at a Multi-Billion-Dollar Valuation",
    "hq": "Berkeley, California",
    "snapshot": [
        ("Market cap", "~$5.2 bn (341.5 mn sh x $15.25)"),
        ("Net cash", "~$541 mn"),
        ("52-week range", "~$12.53 - $58.15"),
        ("TTM revenue", "~$13 mn (mostly research contracts)"),
        ("Annual burn", "~$70-80 mn"),
        ("EV / TTM sales", "~350x"),
        ("Next catalyst", "Technical milestones; financing windows"),
    ],
    "thesis": [
        "Let us be plain: Rigetti Computing is a pre-revenue science project trading at a "
        "multi-billion-dollar valuation. The company generates on the order of $10-15 million in annual "
        "revenue — mostly government research contracts, not commercial product sales — while burning "
        "$70-80 million a year pursuing superconducting quantum computers. At $15.25, the market "
        "capitalization prices a future in which fault-tolerant quantum computing arrives, Rigetti wins a "
        "meaningful share of it, and today's shareholders are not diluted into irrelevance along the way. "
        "We assign low probability to all three happening together. Our fair value is $5.00, implying 67% "
        "downside. This is a speculative SELL: position sizing should reflect binary risk.",
        "This is not a judgment on the physics. Superconducting qubits are a legitimate path to quantum "
        "computing, Rigetti operates its own fabrication facility (Fab-1), and the technical team has real "
        "credentials. It is a judgment on the timeline and the capital structure. Useful, fault-tolerant "
        "quantum computing — the kind that generates commercial revenue rather than research grants — is "
        "widely estimated at 5 to 15 years away, and the field is crowded with better-funded competitors: "
        "IBM and Google with effectively infinite R&D budgets, IonQ and D-Wave with their own public "
        "currencies. Breakthroughs in quantum error correction accrue to the field, not to any single "
        "small company.",
        "The nearer-term math is unforgiving. At the current burn rate, Rigetti must return to capital "
        "markets repeatedly, and each raise — typically via at-the-market offerings into retail enthusiasm — "
        "dilutes existing holders. The stock has become a trading vehicle for quantum narrative momentum "
        "rather than a claim on discounted cash flows, because there are no cash flows to discount. Our "
        "$5.00 fair value reflects the option value of the intellectual property, the talent, and the cash "
        "on hand, heavily discounted for the dilution required to survive to the end of the decade. At a "
        "$70-80 million annual burn, five more years of development implies $350-400 million of additional "
        "capital — roughly a doubling of the share count at current prices. Per-share option value decays "
        "with every offering; that decay is the core of our SELL.",
        "Stated in venture-capital terms, since that is what this is: at $15.25, Rigetti's enterprise value "
        "exceeds $4 billion — a late-stage private valuation for a company with $10-15 million of contract "
        "revenue and no product-market fit. Venture investors pay such prices with liquidation preferences, "
        "anti-dilution protection, and board control; public shareholders get none of those, only the "
        "dilution. The quantum-computing field will likely produce enormous value over the next two "
        "decades; the question is how much of it accrues to today's common shareholders after the "
        "intervening financings, and our answer is: far less than $15 per share.",
    ],
    "thesis_subhead": "The three paths from here",
    "thesis_bullets": [
        ("Dilutive survival (our base case, highest weight). ",
         "The company raises repeatedly at the mercy of sentiment, and per-share value decays regardless "
         "of technical progress. Steady technical progress preserves strategic IP value; dilution brings "
         "per-share fair value to $3.52 in the model's base case."),
        ("Acquisition by a hyperscaler or defense prime (the genuine bull case). ",
         "Quantum talent and IP have strategic value — but for pre-revenue companies, takeouts typically "
         "occur at modest premiums. The market is pricing the acquisition as the expected outcome rather "
         "than the optimistic one."),
        ("Technical failure or funding exhaustion (the bear case). ",
         "Funding dries up or progress stalls; the equity retains only nominal IP value near $1, floored "
         "at $0 by limited liability."),
    ],
    "business": [
        "Rigetti Computing, Inc., founded in 2013 and headquartered in Berkeley, California, develops "
        "superconducting quantum processors and offers quantum-computing-as-a-service through cloud "
        "partners. The company operates Fab-1, a dedicated quantum-chip fabrication facility, and sells "
        "its Novera line of quantum processing units alongside research collaborations. Reported revenue "
        "is minimal and contract-based; the company is pre-profitability by a wide margin and funds "
        "operations through equity raises.",
        "The competitive set spans IBM, Google, IonQ, D-Wave, and a deep bench of venture-backed startups "
        "pursuing trapped-ion, neutral-atom, and photonic approaches. Government research funding — a key "
        "revenue source — is subject to budget and policy shifts, and narrative-driven volatility means "
        "the shares trade on quantum sentiment, enabling sharp drawdowns unrelated to fundamentals.",
    ],
    "business_bullets": [
        ("Fab-1 is a real asset. ",
         "A dedicated quantum-chip fab is genuinely scarce infrastructure — it is the core of the "
         "strategic/IP value in our $5.00."),
        ("Novera QPUs and cloud access are real products with negligible revenue. ",
         "Commercial traction is measured in research contracts, not product-market fit."),
        ("The financing cycle is the business model for now. ",
         "Quantum stocks trade on narrative momentum — government announcements, technical milestones, "
         "quantum-advantage headlines — and management rationally exploits these windows with "
         "at-the-market offerings. Each raise funds 12-18 months of burn and permanently increases the "
         "share count."),
    ],
    "outlook": [
        "Our judgment is that the next several years bring technical milestones, not commercial ones. "
        "Qubit counts will rise, fidelities will improve, and error-correction demonstrations will make "
        "headlines — and none of it will produce material product revenue before the end of the decade. "
        "That is the normal path of deep-tech commercialization, and it is fatal to equity value when the "
        "starting valuation assumes the end state.",
        "Investors should understand they are underwriting years of dilution for a lottery ticket — and "
        "lottery tickets should not cost $15. We would not own this equity at any price above our $5.00 "
        "target; the risk is not volatility, it is permanent dilution.",
    ],
    "financials": [
        "Revenue has drifted from $13.1 million in FY2022 to $7.1 million in FY2025 — the wrong direction, "
        "though at this scale the absolute numbers barely matter. What matters is the burn: free cash flow "
        "of negative $77 million in FY2025 against net cash of ~$541 million, implying roughly seven years "
        "of runway at the current burn — except the burn rises as technical ambitions scale, and the "
        "company's history is to raise well before the cash runs out.",
        "Net losses have widened from $72 million (FY2022) to $216 million (FY2025). With 341.5 million "
        "pro-forma shares outstanding and effective share counts of 380-520 million across our scenarios, "
        "the capitalization table — not the technology — is the binding constraint on per-share value.",
    ],
    "fin_table": {
        "headers": ["$ mn", "FY2023", "FY2024", "FY2025"],
        "rows": [
            ["Revenue", "12.0", "10.8", "7.1"],
            ["Free cash flow", "-60", "-62", "-77"],
            ["Net income", "-75", "-201", "-216"],
            ["Net cash (mid-2026)", "—", "—", "541"],
        ],
        "footnote": "Source: company filings via yfinance; net cash per the valuation model (mid-2026). "
                    "Fiscal year ends Dec 31.",
    },
    "moat": [
        ("Fab-1 and superconducting-qubit know-how. ",
         "A dedicated fab and a real technical team are genuine assets — the foundation of the IP/talent "
         "option value in our fair value."),
        ("No moat against better-funded competitors. ",
         "IBM and Google spend more on quantum in a quarter than Rigetti's entire market history of "
         "raises; breakthroughs in error correction accrue to the field."),
        ("No moat against the modality bet. ",
         "Superconducting qubits may lose to trapped-ion, neutral-atom, or photonic approaches — a "
         "technical risk no balance sheet can hedge."),
        ("The public currency is a wasting asset. ",
         "ATM offerings into retail enthusiasm fund the burn but permanently impair per-share value; the "
         "stock needs ever-larger narratives to sustain the price on an ever-larger share base."),
    ],
    "valuation_method": "Scenario option-value framework (pre-revenue)",
    "valuation_intro": [
        "Traditional DCF is not meaningful for a pre-revenue company with no line of sight to positive "
        "cash flow; we value Rigetti on an option-value framework with scenario weights. The model applies "
        "a Gordon terminal on normalized mid-cycle FCF margins (12% / 20% / 25%) with speculative discount "
        "rates — bear 18.5%, base 16.0%, bull 14.5% — and terminal growth of 0% / 1.0% / 2.5%. Effective "
        "share counts of 520 / 400 / 380 million reflect the dilution required in each scenario.",
        "In the bear case, funding dries up or technical progress stalls and the equity retains only "
        "nominal IP value, floored at $0 by limited liability. In the base case, Rigetti survives to "
        "decade-end with steady technical progress ($2.0 billion of 2035 revenue at a 58.8% CAGR), and "
        "dilution brings per-share fair value to $3.52. In the bull case, quantum advantage arrives "
        "~2029-30 and Rigetti takes meaningful share — $13.33. Weighting 25% / 50% / 25% gives $5.09, "
        "rounded to our $5.00 target. Note the model's own caveat: even after haircutting terminal growth, "
        "the base-case terminal value is 79% of enterprise value — structural to pre-revenue quantum — "
        "which is disclosed, not hidden.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 0.00,
            "assumptions": "Funding dries up or technical progress stalls; dilutive raises continue; "
                           "revenue peaks at $90 mn in 2029 then declines; equity floored at $0 "
                           "(limited liability)",
            "rev_cagr": "+15%", "margin_end": "12%",
            "discount": 0.185, "terminal_g": 0.0, "tv_share": 0.0,
            "pv_explicit": 0, "pv_terminal": 0, "cashflow_unit": "$mn",
        },
        "base": {
            "fair_value": 3.52,
            "assumptions": "Survives to decade-end with steady technical progress; 2035 revenue "
                           "$2.0 bn; IP and talent hold strategic value; dilution to 400 mn shares",
            "rev_cagr": "+58.8%", "margin_end": "20%",
            "discount": 0.16, "terminal_g": 0.01, "tv_share": 0.79,
            "pv_explicit": 182, "pv_terminal": 685, "cashflow_unit": "$mn",
        },
        "bull": {
            "fair_value": 13.33,
            "assumptions": "Quantum advantage ~2029-30; Rigetti takes meaningful share; 2035 revenue "
                           "$5.0 bn; strategic acquirer pays a premium for the platform",
            "rev_cagr": "+70.3%", "margin_end": "25%",
            "discount": 0.145, "terminal_g": 0.025, "tv_share": 0.61,
            "pv_explicit": 1749, "pv_terminal": 2775, "cashflow_unit": "$mn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Scenario FVs from the note's option-value model (bear $0.00 / base $3.52 / bull "
                     "$13.33); weighted $5.09, rounded to the $5.00 target. Base-case terminal value is "
                     "79% of EV (disclosed). Bear case floored at $0 by limited liability.",
    "risks": [
        ("Repeated dilutive equity raises are near-certain. ",
         "Per-share value can fall even if the technology succeeds."),
        ("Technical risk. ",
         "Superconducting qubits may lose to trapped-ion, neutral-atom, or photonic approaches."),
        ("Competition. ",
         "IBM, Google, and well-funded startups with vastly greater resources."),
        ("Government funding dependence. ",
         "A key revenue source, subject to budget and policy shifts."),
        ("Narrative-driven volatility. ",
         "The shares trade on quantum sentiment, enabling sharp drawdowns unrelated to fundamentals."),
    ],
    "falsification": (
        "Upgrade on demonstrated quantum advantage on a commercially relevant problem with third-party "
        "verification — not a press release; non-dilutive funding at scale (a major strategic investment "
        "or government program removing the financing overhang); a credible path to product revenue — "
        "signed commercial contracts, not research grants — within three years; or acquisition interest at "
        "a premium validating the IP's strategic value."
    ),
    "charts": {
        "scenario": {"bear": 0.00, "base": 3.52, "bull": 13.33,
                     "weighted": 5.00, "price": 15.25},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [0.0131, 0.0120, 0.0108, 0.0071],
            "fcf_hist": [-0.085, -0.060, -0.062, -0.077],
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": [0.021, 0.034, 0.054, 0.085, 0.135, 0.214, 0.340, 0.540, 0.858, 1.362, 2.000],
            "fcf_proj": [-0.08, -0.09, -0.10, -0.10, -0.08, -0.05, -0.02, 0.00, 0.05, 0.12, 0.20],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via yfinance (FY ends Dec 31). Projection: base-case "
                    "revenue path from this note's option-value model (58.8% CAGR to $2.0 bn in 2035); "
                    "FCF stays negative until late decade — the dilution runway.",
        },
        "composition": {
            "bear": {"pv_explicit": 0, "pv_terminal": 0},
            "base": {"pv_explicit": 182, "pv_terminal": 685},
            "bull": {"pv_explicit": 1749, "pv_terminal": 2775},
            "unit": "$mn",
        },
        "extra": {
            "type": "line",
            "title": "Revenue — three scenario paths to 2035 ($mn)",
            "years": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035],
            "series": [
                {"label": "Bear (+15% CAGR)",
                 "values": [15.4, 17.7, 20.3, 23.4, 26.9, 30.9, 35.5, 40.9, 47.0, 54.0]},
                {"label": "Base (+58.8% CAGR)",
                 "values": [21.2, 33.7, 53.5, 84.9, 134.9, 214.2, 340.1, 540.1, 857.7, 1362.0]},
                {"label": "Bull (+70.3% CAGR)",
                 "values": [22.7, 38.7, 65.9, 112.3, 191.2, 325.7, 554.6, 944.5, 1608.5, 2739.3]},
            ],
            "ylabel": "$mn",
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "RGTI-equity-research-note-polished.pdf")
build_note(data, out)
print("built:", out)
