"""APH polished note. Research analysis, not investment advice.

Scenario numbers: authoritative Addendum-C model
(~/workspace/your_files/aph-equity-research/valuation_output.json).
Bear $10.36 / base $65.56 / bull $170.70 -> shown $10/$66/$171, weighted $78.05 -> $78 target.
Discounts: bear 11.5% / base 9.0% / bull 8.0%; terminal g 1.5%/2.5%/2.5%.
History: yfinance annuals. Projection: base-case model series (FY2027-2036).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

data = {
    "ticker": "APH",
    "company": "Amphenol Corporation",
    "exchange": "NYSE",
    "sector": "Electronic Components — Connectivity Solutions",
    "verdict": "REDUCE",
    "fair_value": 78.00,
    "price": 86.96,
    "risk": "Medium",
    "headline": "AI's Indispensable Plumber — at a Price That Leaves No Room for Friction",
    "ceo": "Adam Norwitt",
    "hq": "Wallingford, Connecticut",
    "snapshot": [
        ("Market cap", "~$224 bn (2.58 bn sh × $86.96)"),
        ("Net debt", "~$8.5 bn (~0.9x leverage, post-CommScope)"),
        ("52-week range", "~$58.67 – $89.26"),
        ("Q1 FY27 revenue / growth", "$8.5 bn / +39% YoY (June 2026)"),
        ("IT datacom (AI)", "$6.1 bn (+66% YoY); ~70% of mix on FY26E path"),
        ("Book-to-bill", "~1.41x (orders $12.0B vs sales $8.5B)"),
        ("FY2026E guide", "Revenue $29.1 bn (+26%); FCF margin 13.5%"),
        ("AI interconnect ramp", "1.6T optical (2027); 6.4T copper (2028)"),
        ("Next catalyst", "Q2 FY27 results; AI order-book linearity"),
    ],
    "thesis": [
        "Amphenol is the indispensable plumber of the AI build-out, and the stock is priced as though "
        "indispensability were the same as pricing power without limit. It is not. The company's high-density, "
        "high-speed interconnect — the copper and optical nervous system inside every AI rack — is genuinely "
        "world-class, and the numbers prove it: IT datacom revenue of $6.1 billion in Q1 FY27, up 66% "
        "year over year, with orders of $12.0 billion against $8.5 billion of sales, a 1.41x book-to-bill that "
        "is the strongest demand signal in the company's history. When hyperscalers cannot ship AI capacity "
        "without Amphenol connectors, the next two years are contracted. That is why our FY2026–27 "
        "assumptions track the demand signal, not a haircut of it.",
        "But this note is a REDUCE, and the reason is arithmetic, not narrative. At $86.96 the stock is priced "
        "for the AI supercycle to compound at roughly our bull-case pace — IT datacom growing at a 30%+ "
        "compounded rate through the decade while legacy automotive and industrial demand merely holds — with "
        "no allowance for the cyclicality that has defined this industry for forty years. Our scenarios are "
        "$10 / $66 / $171, weighted to a $78 target, 10.3% below the quote. The base case ($65.56) is already "
        "generous: 11.1% revenue CAGR for a decade, free-cash-flow margins gliding to 15.5%, a 9.0% discount "
        "rate that credits the franchise's through-cycle resilience. Even that generous path is worth less "
        "than the current price.",
        "The bear case ($10.36) deserves a hearing because it is how connector cycles actually end. Amphenol's "
        "history is a series of sharp AI/data-center-adjacent ramps followed by inventory corrections — and the "
        "current cycle has every marker of a pre-build: book-to-bill at 1.41x, customers double-ordering "
        "against 2027–28 capacity, and IT datacom at 70% of the revenue mix, up from 43% just a year ago. When "
        "the hyperscaler capex wave crests — and it will, because no build-out in history has compounded at "
        "30%+ indefinitely — the correction runs through the suppliers first. Bear assumes revenue falls ~20% "
        "in 2028–29 as the order book normalizes, FCF margins compress to 13.5%, and the multiple derates to a "
        "cyclical trough. That is not a prediction; it is the base rate for this industry.",
        "Our forward judgment: Amphenol will be a larger, more AI-centric, and structurally better business in "
        "five years — the 1.6T optical and 6.4T copper transitions extend the technology lead, and the "
        "CommScope acquisition diversifies the mix. But the stock at $86.96 is not pricing the business; it is "
        "pricing the cycle at its peak and calling it permanent. REDUCE: take profits into the strength, and "
        "revisit when the inevitable digestion arrives.",
    ],
    "thesis_subhead": "Why the demand is contracted — and why the price still fails",
    "thesis_bullets": [
        ("The order book is the thesis. ",
         "Q1 FY27: orders $12.0B vs sales $8.5B (1.41x book-to-bill), IT datacom $6.1B (+66%). Customers are "
         "committing capital against 2027–28 capacity; the FY2026 guide ($29.1B, +26%) is covered by "
         "contracted demand, not hope."),
        ("The technology roadmap extends the lead. ",
         "1.6T optical interconnect in 2027 and 6.4T copper in 2028 keep Amphenol ahead of the bandwidth "
         "curve that AI racks demand — the moat is engineering cadence, not patents alone."),
        ("But 70% mix concentration is a cycle amplifier. ",
         "IT datacom went from 43% of revenue to ~70% in one year. When the cycle turns, the same mix that "
         "drove the re-rating drives the de-rating."),
        ("The price requires the bull case. ",
         "Our base case grants an 11.1% revenue CAGR for a decade and is worth $65.56. The market at "
         "$86.96 is paying roughly halfway between our base and our bull ($170.70)."),
    ],
    "business": [
        "Amphenol (founded 1932) is the world's largest manufacturer of interconnect products — connectors, "
        "cable assemblies, sensors, and antennas — selling into IT datacom, automotive, industrial, mobile "
        "devices, and defense. The business model is decentralized entrepreneurship: dozens of operating units "
        "run with unusual autonomy, acquisitions are integrated aggressively, and capital allocation has been "
        "among the best in industrials for two decades. Fiscal 2025 produced revenue of $23.09 billion with "
        "free cash flow of $4.38 billion — a 19.0% FCF margin that is the envy of the sector.",
        "The IT datacom segment — high-speed interconnect for data centers, and therefore for AI — is now the "
        "company. From 43% of revenue in FY2025, it is on a path to roughly 70% of the FY2026 mix, growing 66% "
        "year over year in Q1 FY27. Amphenol's high-density copper and optical interconnect is the standard "
        "inside hyperscale AI racks; the 1.6T optical generation (2027) and 6.4T copper (2028) extend a lead "
        "that competitors chase but have not closed. The CommScope acquisition (closed 2025) added broadband "
        "and outdoor wireless exposure, diversifying the non-AI base.",
        "The forward picture is a two-speed company: an AI interconnect business growing at 30%+ compounded "
        "rates with expanding margins, stapled to a legacy industrial/automotive connector business growing "
        "low-single-digits at best. The mix shift is margin-accretive — IT datacom carries the best margins in "
        "the portfolio — which is why consolidated FCF margins glide from ~14% toward 15.5% in our base case "
        "even as the legacy businesses tread water. The risk is that the mix shift is also cycle-amplifying: "
        "at 70% of revenue, IT datacom's cyclicality is Amphenol's cyclicality.",
    ],
    "business_bullets": [
        ("IT datacom: the AI standard. ",
         "$6.1B in Q1 FY27 (+66% YoY); the interconnect inside hyperscale AI racks. 1.6T optical (2027) and "
         "6.4T copper (2028) extend the bandwidth lead."),
        ("CommScope acquisition. ",
         "Broadband and outdoor wireless exposure diversifies the non-AI base; integration is the "
         "near-term execution watch item."),
        ("Decentralized operating model. ",
         "Dozens of autonomous units with aggressive acquisition integration — the cultural engine behind "
         "two decades of best-in-class capital allocation."),
        ("Legacy segments: ballast, not growth. ",
         "Automotive, industrial, and mobile-device interconnect grow low-single-digits at best; their role "
         "is cash generation, not expansion."),
    ],
    "outlook": [
        "The next two years are contracted. FY2026E revenue of $29.1 billion (+26%) sits beneath a $12.0 "
        "billion quarterly order book, and FY2027E at $43.9 billion in our base case reflects the continued "
        "AI-rack ramp plus the full CommScope contribution. IT datacom grows through 2028–29 on the 1.6T "
        "optical and 6.4T copper transitions. This is the easy part of the call — the demand is visible, the "
        "technology lead is real, and the book-to-bill confirms it.",
        "The hard part is 2029–2032, and it is where our REDUCE lives. Connector cycles end in inventory "
        "corrections: customers double-order in the ramp, the order book normalizes, and revenue falls 15–25% "
        "before the next wave. Our base case assumes Amphenol navigates this with unusual grace — revenue CAGR "
        "of 11.1% for the decade, no down year worse than flat, FCF margins gliding to 15.5% — because the "
        "decentralized model has historically managed cycles better than peers. Even with that grace, the "
        "decade is worth $65.56. The bull case ($170.70) assumes the AI cycle does not correct at all — 19.2% "
        "revenue CAGR, 17% terminal FCF margins, the order book compounding indefinitely. That is the case the "
        "price is closest to.",
        "What would change the call: if IT datacom orders re-accelerate into 2027 with book-to-bill holding "
        "above 1.3x — evidence the wave is bigger than the current order book — we would revisit toward the "
        "bull. If book-to-bill falls below 1.0 for two quarters or IT datacom revenue declines sequentially, "
        "the bear case ($10.36) becomes the working assumption and the REDUCE hardens. Watch Q2 FY27: order "
        "linearity and any commentary on customer inventory are the numbers that matter.",
    ],
    "financials": [
        "Cash generation is elite: FY2025 free cash flow of $4.38 billion on $23.09 billion of revenue — a "
        "19.0% margin — and the model has FY2026E FCF margins at 13.5% (diluted by CommScope integration and "
        "working-capital absorption in the ramp) before gliding to 15.5% in the base case. Revenue history "
        "shows the cycle plainly: $12.62B (2022), $12.55B (2023, flat), $15.22B (2024, +21%), $23.09B (2025, "
        "+52%) — the AI ramp is visible as a step-change, and step-changes in connectors have always been "
        "followed by digestion.",
        "The balance sheet absorbed CommScope without strain: net debt of roughly $8.5 billion is about 0.9x "
        "leverage — comfortable for a business with this cash conversion. The share count of ~2.58 billion "
        "(post-split) means the $78 target implies roughly $201 billion of equity value against our base-case "
        "EV of $182.4 billion. Capital allocation remains the quiet strength: the acquisition program has "
        "compounded per-share value for two decades, and the dividend grows steadily.",
    ],
    "fin_table": {
        "headers": ["$ bn", "FY2022", "FY2023", "FY2024", "FY2025"],
        "rows": [
            ["Revenue", "12.62", "12.55", "15.22", "23.09"],
            ["YoY growth", "—", "−1%", "+21%", "+52%"],
            ["IT datacom mix", "—", "—", "~38%", "~43%"],
            ["Free cash flow", "1.79", "2.16", "2.15", "4.38"],
            ["FCF margin", "14.2%", "17.2%", "14.1%", "19.0%"],
            ["Q1 FY27 (Jun 2026)", "Revenue $8.5B (+39%)", "IT datacom $6.1B (+66%)", "Orders $12.0B", "B2B 1.41x"],
        ],
        "footnote": "Sources: company releases; annuals via yfinance. FY2026E guide: revenue $29.1B (+26%), "
                    "FCF margin 13.5%.",
    },
    "moat": [
        ("Engineering cadence at the bandwidth frontier. ",
         "1.6T optical (2027) and 6.4T copper (2028) keep Amphenol one generation ahead of the AI rack's "
         "bandwidth demands — the moat is the roadmap, executed."),
        ("Design-in lock-in. ",
         "Interconnect is designed into customer platforms years ahead of production; qualification cycles "
         "are long and switching costs are real once a standard is set."),
        ("The decentralized acquisition machine. ",
         "Two decades of best-in-class capital allocation — buying niche interconnect leaders and "
         "integrating them into the autonomous-unit model — compounds per-share value through cycles."),
        ("The moat's limit is the cycle. ",
         "No engineering lead prevents an inventory correction: when hyperscalers pause, orders stop "
         "regardless of technology position, and 70% mix concentration amplifies the hit."),
    ],
    "valuation_method": "10-year scenario DCF (FY2027–FY2036)",
    "valuation_intro": [
        "We value Amphenol on a 10-year explicit DCF of free cash flow (FY2027–FY2036), weights bear 25% / "
        "base 50% / bull 25%. Scenario discounts: base 9.0% (franchise resilience through cycles, customer "
        "concentration, cyclicality), bear 11.5% (base + 250bp), bull 8.0% (base − 100bp). Terminal growth "
        "1.5% / 2.5% / 2.5% on year-10 FCF at the scenario's terminal margin (13.5% / 15.5% / 17%) — "
        "through-cycle levels, never peaks. Revenue CAGRs: bear 1.2% (with a 2028–29 correction), base "
        "11.1%, bull 19.2%. Equity = firm EV − ~$8.5B net debt, over ~2.58B shares. Terminal value is "
        "39–70% of EV across scenarios — within discipline, no haircut required.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 10.36,
            "assumptions": "The AI order book normalizes: revenue falls ~20% across 2028–29 as customers work through double-ordered inventory; FCF margins compress to 13.5%; the multiple derates to a cyclical trough",
            "rev_cagr": "+1.2%", "margin_end": "13.5%",
            "discount": 0.115, "terminal_g": 0.015, "tv_share": 0.394,
            "pv_explicit": 24.33, "pv_terminal": 15.80, "cashflow_unit": "$bn",
        },
        "base": {
            "fair_value": 65.56,
            "assumptions": "Amphenol navigates the cycle with unusual grace: 11.1% revenue CAGR, no down year worse than flat; IT datacom compounds on the 1.6T/6.4T transitions; FCF margins glide to 15.5%",
            "rev_cagr": "+11.1%", "margin_end": "15.5%",
            "discount": 0.09, "terminal_g": 0.025, "tv_share": 0.598,
            "pv_explicit": 73.34, "pv_terminal": 109.10, "cashflow_unit": "$bn",
        },
        "bull": {
            "fair_value": 170.70,
            "assumptions": "The AI cycle does not correct: 19.2% revenue CAGR for a decade; IT datacom compounds indefinitely on successive bandwidth generations; 17% terminal FCF margins",
            "rev_cagr": "+19.2%", "margin_end": "17%",
            "discount": 0.08, "terminal_g": 0.025, "tv_share": 0.700,
            "pv_explicit": 136.24, "pv_terminal": 317.29, "cashflow_unit": "$bn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "0.25×$10.36 + 0.50×$65.56 + 0.25×$170.70 = $78.05 → $78 target. "
                     "Bear meets all hurt conditions (revenue decline years, margin compression, 25%+ derating).",
    "risks": [
        ("Inventory correction (the #1 risk). ",
         "1.41x book-to-bill and 70% AI mix are classic pre-build markers; when hyperscalers pause, "
         "supplier orders stop first and hardest."),
        ("Customer concentration. ",
         "A handful of hyperscalers and their ODMs drive the IT datacom wave; design losses or "
         "in-sourcing at any one of them is material."),
        ("Mix concentration amplifies the cycle. ",
         "IT datacom at ~70% of revenue means Amphenol's cyclicality is now the AI cycle's cyclicality."),
        ("Legacy segment drag. ",
         "Automotive and industrial connector demand is soft; a deeper industrial recession would "
         "pressure the non-AI base."),
        ("Integration risk. ",
         "CommScope is the largest acquisition in company history; synergy delivery is the near-term "
         "execution watch item."),
        ("Valuation. ",
         "At $86.96 the stock prices roughly the bull case — any disappointment in the order book "
         "reprices sharply toward the base ($65.56)."),
    ],
    "falsification": (
        "The base case's order-book assumption would be withdrawn if book-to-bill falls below 1.0 for two "
        "consecutive quarters or if IT datacom revenue declines sequentially — at that point the bear case "
        "($10.36) becomes the working assumption and the REDUCE hardens. Conversely, if orders "
        "re-accelerate into 2027 with book-to-bill holding above 1.3x, the wave is bigger than the current "
        "book and we would revisit toward the bull. Watch Q2 FY27: order linearity and any commentary on "
        "customer inventory are the numbers that matter."
    ),
    "methodology": [
        "We value the business on a 10-year explicit DCF of free cash flow (bear 25% / base 50% / bull 25%). "
        "Revenue follows the scenario path (bear 1.2% / base 11.1% / bull 19.2% 10-year CAGR, including a "
        "2028–29 correction in the bear case); free-cash-flow margin glides to the scenario's terminal margin "
        "(13.5% / 15.5% / 17%) over the horizon. Discount rates: base 9.0%, bear +250bp (11.5%), bull "
        "−100bp (8.0%). Terminal growth (1.5% / 2.5% / 2.5%) applies to year-10 FCF at the scenario's "
        "terminal margin. Equity = firm EV − net debt; divided by diluted shares. Bear cases must be "
        "genuinely adverse and sit below the current price. The published target is the probability-weighted "
        "fair value, stated as a 12-month horizon reference.",
        "Risk ratings (Low / Medium / Medium-High / High) combine business-model volatility, the balance "
        "sheet, and the valuation. This note is independent research-style analysis for informational purposes "
        "only and is not investment advice. Financial figures are drawn from company releases and SEC filings; "
        "market data as of October 2, 2026. Projections and the price target are the author's estimates and "
        "involve uncertainty. Past performance does not predict future results.",
    ],
    "charts": {
        "scenario": {"bear": 10.36, "base": 65.56, "bull": 170.70, "weighted": 78.05, "price": 86.96},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [12.62, 12.55, 15.22, 23.09],
            "fcf_hist": [1.79, 2.16, 2.15, 4.38],
            "years_proj": [2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": [43.87, 52.80, 62.40, 70.50, 77.20, 83.00, 88.20, 93.10, 97.60, 102.29],
            "fcf_proj": [6.53, 8.07, 9.74, 11.13, 12.26, 13.24, 14.09, 14.89, 15.61, 16.38],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via yfinance. Projection: base-case series from the scenario "
                    "DCF (FY2026E anchor $29.1B revenue; 11.1% 10-yr CAGR; FCF margin gliding to 15.5%).",
        },
        "composition": {
            "bear": {"pv_explicit": 24.33, "pv_terminal": 15.80},
            "base": {"pv_explicit": 73.34, "pv_terminal": 109.10},
            "bull": {"pv_explicit": 136.24, "pv_terminal": 317.29},
            "unit": "$bn",
        },
        "extra": {
            "type": "pie",
            "title": "FY2025 revenue mix — IT datacom vs. rest",
            "labels": ["IT datacom (AI)", "Automotive", "Industrial", "Mobile devices & other"],
            "values": [43, 20, 22, 15],
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "APH-equity-research-note-polished.pdf")
build_note(data, out)
print("built:", out)
