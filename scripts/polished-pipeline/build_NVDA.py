"""NVDA polished note. Research analysis, not investment advice.

Scenario numbers: authoritative Addendum-C model (model.json + addendum_c PDF).
Bear $55.56 / base $223.62 / bull $390.70 -> shown rounded $56/$224/$391, weighted $223.38 -> $223 target.
History: yfinance annuals (fiscal year ends January). Projection: base-case model series.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

data = {
    "ticker": "NVDA",
    "company": "NVIDIA Corporation",
    "exchange": "NASDAQ",
    "sector": "Semiconductors — AI Compute Platforms",
    "verdict": "HOLD",
    "fair_value": 223.00,
    "price": 233.95,
    "risk": "Med-High",
    "headline": "The AI Factory Is Real — but the Price Already Owns the Duration",
    "ceo": "Jensen Huang",
    "hq": "Santa Clara, California",
    "snapshot": [
        ("Market cap", "~$5.65 tn (24.1 bn sh × $233.95)"),
        ("Net liquid cash", "~$18.2 bn ($22.4B cash + $34.1B marketable securities − $38.4B debt)"),
        ("52-week range", "~$164.27 – $237.88"),
        ("Q2 FY27 revenue / Data Center", "$96.2 bn (+106% YoY) / $89.0 bn (+117%)"),
        ("Gross / net margin (Q2 FY27)", "75.0% / 62.0%"),
        ("Q3 FY27 guide", "$108 bn (±2%), gross margin 74%"),
        ("FY28 guide (first ever)", "+~70% revenue YoY (~$670B), supply-constrained"),
        ("Buyback authorization", "$235 bn through FY28 ($150B top-up)"),
        ("Street consensus target", "~$323 (48 Buy / 4 Hold)"),
        ("Next catalyst", "Q3 FY27 results (November 2026); Rubin ramp linearity"),
    ],
    "thesis": [
        "Our view of the business: NVIDIA is the one company in this AI cycle whose demand visibility is "
        "contractual rather than aspirational. In August 2026 the company issued its first-ever full-year revenue "
        "guide — fiscal 2028 (ending January 2028) up roughly 70% year over year, to about $670 billion — and "
        "management was explicit that the number is supply-constrained: real demand runs hotter than the guide, "
        "and supply is what determines the 70%. When a company guiding to ~$670 billion tells you demand is "
        "running ahead of what it can ship, the next four quarters are a capacity-allocation problem, not a "
        "forecast to be haircut. That is why our 2027–28 assumptions track guidance rather than sitting below it.",
        "But this note is not a victory lap, and the call is not about the next four quarters. The entire call is "
        "duration and fade. Our base case grants the supercycle through 2030 — the Rubin and Rubin Ultra waves, "
        "Vera Rubin in full production since March 2026 and on pace for the fastest ramp in company history, "
        "sovereign AI putting a demand floor beneath the hyperscalers — then fades growth into the single digits "
        "with free-cash-flow margins normalizing to a through-cycle 48%, far below today's 60%-plus net margins. "
        "The market at $233.95 is paying for something close to that. Our scenarios are $56 / $224 / $391, "
        "weighted to a $223 target, 4.7% below the quote. The business is exceptional, the cycle is real, and the "
        "price is roughly fair. HOLD.",
        "The bear case deserves emphasis because it is the scenario the price ignores. It is the honest version of "
        "2029–30: the 2026–28 pre-build — top-5 hyperscaler capex near $800 billion in 2026 and about $1.3 trillion "
        "in 2027 — overshoots, book-to-bill drops below 1.0, the inventory pre-build (raw materials up 71% "
        "quarter over quarter, 119 days of inventory) becomes a glut, revenue falls about 17% in FY29 and "
        "another 7% in FY30, and FCF margins compress 900 basis points versus base as price cuts clear the "
        "channel. Bear $56 — far below the price, as a bear case must be. Every compute build-out in history has "
        "ended in digestion; this one has all the signature markers of a top. Skepticism belongs in duration and "
        "fade, not in the next four quarters — and the price currently assigns the fade roughly zero weight.",
        "The forward judgment that matters: NVIDIA's product is no longer the GPU but the gigawatt-scale AI "
        "factory — compute, networking, and software sold as an integrated stack at roughly $40 billion of "
        "revenue opportunity per gigawatt of data-center capacity. That full-stack economics is why margins are "
        "extraordinary and why the franchise is so defensible. But it is also why the cycle will be so punishing "
        "when it turns: the same customers buying the factory today can defer the next factory tomorrow. We "
        "would own this business at a price that compensates for the fade arriving early. At $233.95, against a "
        "$323 Street consensus that prices roughly our bull case as the expected outcome, there is no margin of "
        "safety. Own it if you own the duration call; otherwise wait for the digestion scare.",
    ],
    "thesis_subhead": "Why the demand is contracted, not extrapolated",
    "thesis_bullets": [
        ("A 70% FY28 guide that is explicitly supply-capped. ",
         "Q2 FY27 revenue $96.22 billion (+106%), data center $89.0 billion (+117%), GAAP gross margin 75.0%; "
         "Q3 guided to $108 billion (±2%) at 74% gross margin — and the first-ever full-year guide of ~70% FY28 "
         "growth, with customer forecasts pointing to demand roughly doubling. Wall Street had been near 45%."),
        ("$279 billion of supply commitments and rising prices. ",
         "TrendForce reports NVIDIA's supply commitments have soared to ~$279 billion as memory costs surge; "
         "the company has notified its largest customers of price increases exceeding 15% on AI server systems "
         "(Vera Rubin and Grace Blackwell configurations) hitting systems shipped in early 2027. Allocation, not "
         "discounting."),
        ("Memory and foundry are hard constraints through 2028. ",
         "HBM is reported sold out for all of 2026, with SK Hynix warning the shortfall could stretch toward "
         "the end of the decade; Blackwell PRO lead times run 3–7 months; TSMC N3 capacity is near full "
         "utilization through at least 2027. The company itself cautions that supply constraints persist through "
         "fiscal 2028."),
        ("Named multi-year deployments. ",
         "Amazon has committed to deploying 2 million NVIDIA GPUs through 2029; Anthropic locked in a 2.5GW "
         "commitment; Rubin NVL72 racks are already delivering to Google Cloud, Microsoft, and Oracle, with "
         "systems up at CoreWeave and Nebius."),
        ("Sovereign AI is a second demand curve. ",
         "Saudi Arabia's HUMAIN ($10 billion partnership, part of a $100 billion AI ecosystem), the UK's £18 "
         "billion compute program, South Korea's 260,000-Blackwell build-out — nations treating compute as "
         "strategic infrastructure put a floor under demand independent of Silicon Valley capex cycles."),
        ("$40 billion per gigawatt. ",
         "In the Rubin generation the revenue opportunity per gigawatt of data-center capacity expands to "
         "~$40 billion, because the sale is the full AI factory — GPU, CPU, networking, inference silicon — not "
         "the chip. Networking has grown from under 9% to ~18% of data center revenue in a year."),
    ],
    "business": [
        "NVIDIA (founded 1993) has completed its transformation from chipmaker to AI-factory platform. The "
        "product is the gigawatt-scale data center, sold as an integrated stack: compute (Blackwell Ultra today, "
        "Vera Rubin ramping), CPU (Vera/Grace), networking (InfiniBand and Spectrum-X Ethernet, now ~18% of "
        "data center revenue), and the CUDA software ecosystem. Q2 FY27 (ended July 26, 2026): revenue $96.22 "
        "billion (+106% YoY), data center $89.0 billion (+117% YoY) on the Blackwell Ultra ramp, GAAP gross margin "
        "75.0%, net margin 62.0%, diluted EPS $2.46. Vera Rubin entered full production in March 2026 and is on "
        "pace for the fastest product ramp in company history, with NVL72 systems delivering to Google Cloud, "
        "Microsoft Azure, Oracle Cloud, CoreWeave, and Nebius — meaning NVIDIA is currently running two product "
        "cycles simultaneously.",
        "The forward picture: Q3 FY27 guided to $108 billion (±2%, gross margin 74.0%, excluding any China "
        "data-center revenue); FY28 guided to ~70% revenue growth (~$670 billion) on supply that management says "
        "cannot meet demand; a $150 billion buyback top-up taking remaining authorization to $235 billion through "
        "FY28; and a balance sheet with $56.6 billion of liquid resources against $38.4 billion of debt — plus "
        "$42.8 billion of marketable equity securities and $51.2 billion of non-marketable stakes in AI labs and "
        "partners. The open question for the decade is not whether the next two years are sold (they are, several "
        "times over) but how long the build-out lasts and what the business earns when the factories are built. "
        "Our judgment: supercycle through 2030, then a long fade — with a genuine 2029–30 digestion cliff as "
        "the live alternative.",
    ],
    "business_bullets": [
        ("Two product cycles running at once. ",
         "Blackwell Ultra is the current revenue engine while Vera Rubin ramps as the fastest product launch "
         "in company history; Rubin Ultra follows. Execution cadence is itself a competitive moat."),
        ("Networking is becoming the lock-in layer. ",
         "InfiniBand and Spectrum-X Ethernet now approach a fifth of data-center revenue; the rack-scale "
         "system, not the chip, is what customers buy — and what competitors cannot replicate."),
        ("Cash return is aggressive. ",
         "A $150 billion buyback top-up (authorization $235 billion through FY28) retires meaningful share "
         "count even at these prices; scenario-specific diluted shares in our model run 24.3 / 23.5 / 22.8 "
         "billion across bear/base/bull."),
    ],
    "outlook": [
        "The next two years are sold. FY2027E revenue anchors at $396 billion (Q2 actual plus Q3 guidance "
        "annualized against the FY28 guide), and FY28 at $673 billion is management's own ~70% guide — "
        "supply-constrained, with demand running higher — followed by +26% and +18% as the Rubin generation "
        "scales and the $40-billion-per-gigawatt full-stack mix builds. The duration judgment is what separates "
        "the scenarios: the base case runs the supercycle through 2030 (Rubin + Rubin Ultra waves, sovereign AI "
        "as a floor), then fades from 2031 as the installed base digests — growth stepping down through the "
        "high single digits to ~3.5%, FCF margins normalizing to a through-cycle 48%, well below today's 60%-plus "
        "net margins and above any historical semiconductor norm. Result: $224.",
        "The bull case ($391) extends the supercycle through 2032 — sovereign AI compounds, the full-stack "
        "$40B/GW economics hold, growth stays double-digit into the early 2030s with 50% through-cycle FCF "
        "margins. The bear case ($56) is the 2029–30 digestion cliff: the 2026–28 pre-build overshoots, "
        "book-to-bill drops below 1.0, revenue falls ~17% in FY29 and another 7% in FY30, FCF margins compress "
        "900bp versus base as price cuts clear the glut, and terminal growth is 1.5%. The market's $233.95 "
        "assigns the bear roughly zero weight; we carry it at 25%.",
        "What would change the call: evidence the wave is bigger than contracted — book-to-bill sustained above "
        "1.5 with lead times extending into 2028 — pushes toward the bull. Conversely, if book-to-bill falls "
        "below 1.0 for two consecutive quarters or lead times normalize, the contracted-demand assumption behind "
        "the 2027–28 numbers is withdrawn, the bear becomes the base, and this note becomes a SELL. Watch Q3 "
        "FY27 (November): DSO normalization and Rubin shipment linearity are the two numbers that matter.",
    ],
    "financials": [
        "Cash conversion is deteriorating at the peak — the single most important financial tell in the note. "
        "Receivables rose 54.9% quarter over quarter against revenue up 17.9%; days sales outstanding expanded to "
        "~60 days. Q2 free cash flow was $21.3 billion on $96.2 billion of revenue (22%), because working capital "
        "is absorbing the ramp. $36.9 billion of newly-appearing restricted cash is opaque. If customers are being "
        "financed to take supply, the demand signal is softer than the revenue line — and the digestion cliff, "
        "when it comes, will arrive through the receivables book first.",
        "Margin pressure is guided, not hypothetical. Gross margin bottoms at 71–72% in Q4 FY27 and settles at "
        "72–73% in FY28 on memory pricing — the announced price increases only partly offset. The 75% print is "
        "the peak, and our terminal margins assume the market knows it. On the balance sheet, $94 billion of "
        "equity positions in other companies — many of them NVIDIA's own customers (AI labs, infrastructure "
        "financiers) — is vendor-financing-style circular exposure: it flatters both revenue and the investment "
        "book, and in a downturn the two unwind together.",
    ],
    "fin_table": {
        "headers": ["", "Q2 FY27", "Q1 FY27", "FY2026"],
        "rows": [
            ["Revenue ($bn)", "96.22", "—", "215.94"],
            ["Data Center ($bn)", "89.0", "—", "—"],
            ["YoY growth", "+106%", "—", "+114%"],
            ["GAAP gross margin", "75.0%", "—", "71.1%"],
            ["Net margin", "62.0%", "—", "55.6%"],
            ["Diluted EPS", "$2.46", "—", "—"],
            ["Free cash flow ($bn)", "21.3", "—", "96.7"],
            ["Q3 FY27 guide", "$108 bn (±2%)", "74% GM", "—"],
        ],
        "footnote": "Sources: company earnings releases (Aug 2026), SEC filings; FY2026 via yfinance annuals. "
                    "FY2027E revenue anchor $396B (Q2 actual + Q3 guide run-rate).",
    },
    "moat": [
        ("The full stack is the moat. ",
         "CUDA's 20-year software ecosystem, the networking layer that locks racks together, and a "
         "one-generation lead in execution — no competitor ships a comparable rack-scale system at volume. "
         "The $40B-per-gigawatt sale is a systems sale, and the system is the moat."),
        ("AMD is now a contracted second source. ",
         "AMD's MI450/Helios is contracted at three frontier labs plus Oracle. It does not threaten 2027–28 "
         "volumes, but it caps the merchant-GPU share of each incremental data-center dollar — the fade "
         "mechanism in miniature."),
        ("Custom silicon attacks from the side. ",
         "Broadcom's 10GW custom-silicon partnership with OpenAI, and hyperscaler ASICs (Google TPU v7, "
         "Amazon Trainium, Microsoft Maia) absorbing inference workloads internally, steadily erode the "
         "'NVIDIA tax' the hyperscalers are explicitly trying to reduce."),
        ("Export controls ceded China. ",
         "China data-center revenue is effectively excluded from guidance entirely; policy can tighten "
         "further. DOJ/EU antitrust scrutiny of the networking lock-in is a live overhang — a forced "
         "unbundling would compress the full-stack economics."),
    ],
    "valuation_method": "10-year scenario FCFF DCF (FY2027–FY2037)",
    "valuation_intro": [
        "We value NVIDIA on a 10-year explicit free-cash-flow-to-firm DCF (FY2027–FY2037; fiscal year ends "
        "January), weights bear 25% / base 50% / bull 25%. Scenario discounts: base 12.0% (cycle concentration, "
        "customer concentration, geopolitical and antitrust overhangs), bear 14.5% (base + 250bp), bull 10.5% "
        "(base − 150bp). Terminal growth 1.5% / 2.5% / 2.5% on year-10 FCF at normalized through-cycle margins "
        "(never peak). Equity = firm EV + ~$18.2 billion net liquid cash ($22.4B cash + $34.1B marketable debt "
        "securities less $38.4B debt; restricted cash and equity stakes excluded), over scenario-specific diluted "
        "shares (24.3B / 23.5B / 22.8B — buybacks continue in base/bull, pause in bear). FY2027E revenue anchor: "
        "$396B (Q2 $96.22B, Q3 guide $108B). Terminal value is 39–56% of EV across scenarios — within discipline, "
        "no haircut required.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 56,
            "assumptions": "2026–28 pre-build overshoots; book-to-bill below 1.0; revenue −17% in FY29, −7% in FY30; FCF margins compress 900bp vs base as price cuts clear the glut",
            "rev_cagr": "+5.2%", "margin_end": "39%",
            "discount": 0.145, "terminal_g": 0.015, "tv_share": 0.387,
            "pv_explicit": 816.86, "pv_terminal": 514.96, "cashflow_unit": "$bn",
        },
        "base": {
            "fair_value": 224,
            "assumptions": "Supercycle through 2030 (Rubin + Rubin Ultra, sovereign AI floor); FY28 $673B per the guide; growth fades from 2031, FCF margins normalize to 48% through-cycle",
            "rev_cagr": "+14.4%", "margin_end": "48%",
            "discount": 0.12, "terminal_g": 0.025, "tv_share": 0.485,
            "pv_explicit": 2699.05, "pv_terminal": 2537.91, "cashflow_unit": "$bn",
        },
        "bull": {
            "fair_value": 391,
            "assumptions": "Supercycle through 2032; sovereign AI compounds; $40B/GW full-stack economics hold; double-digit growth into the early 2030s at 50% through-cycle FCF margins",
            "rev_cagr": "+18.2%", "margin_end": "50%",
            "discount": 0.105, "terminal_g": 0.025, "tv_share": 0.558,
            "pv_explicit": 3933.06, "pv_terminal": 4956.79, "cashflow_unit": "$bn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Model detail: $55.56 / $223.62 / $390.70 → $56 / $224 / $391 rounded; "
                     "weighted 0.25×$56 + 0.50×$224 + 0.25×$391 = $223.38 → $223 target.",
    "risks": [
        ("The digestion cliff (the #1 risk). ",
         "$1.3T of 2027 hyperscaler capex, 119 days of inventory, raw materials tripling YoY — the "
         "top-of-cycle signature. When the pre-build overshoots, the correction is violent (bear: −17% FY29 "
         "revenue)."),
        ("Cash conversion at the peak. ",
         "DSO expanding to ~60 days, receivables +54.9% QoQ vs revenue +17.9%; Q2 FCF only 22% of revenue. "
         "If customers are being financed to take supply, the demand signal is softer than the revenue line."),
        ("$94B of circular exposure. ",
         "Equity stakes in customers and infrastructure financiers unwind together with demand in a downturn."),
        ("Margin compression is guided. ",
         "Gross margin bottoming 71–72% in Q4 FY27 on memory pricing; the 75% print is the peak."),
        ("Customer and geographic concentration. ",
         "A handful of hyperscalers; China data-center revenue excluded entirely; export policy can tighten "
         "further."),
        ("Substitution. ",
         "Hyperscaler ASICs and Broadcom/OpenAI custom silicon erode the merchant-GPU share of each new "
         "data-center dollar."),
        ("Antitrust. ",
         "DOJ/EU scrutiny of networking lock-in; a forced unbundling would compress the $40B/GW "
         "full-stack economics."),
        ("Power. ",
         "Gigawatt-scale data centers face grid and permitting constraints that can push deployments right "
         "regardless of chip supply."),
    ],
    "falsification": (
        "The contracted-demand assumption behind the 2027–28 numbers would be withdrawn if book-to-bill "
        "falls below 1.0 for two consecutive quarters or if lead times normalize — at that point the bear case "
        "becomes the base case and this HOLD becomes a SELL. Conversely, book-to-bill sustained above 1.5 with "
        "lead times extending into 2028 validates the bull duration and we would revisit to the upside. "
        "Watch Q3 FY27 (November): DSO normalization and Rubin shipment linearity are the two numbers that matter."
    ),
    "charts": {
        "scenario": {"bear": 56, "base": 224, "bull": 391, "weighted": 223, "price": 233.95},
        "trajectory": {
            "years_hist": [2023, 2024, 2025, 2026],
            "revenue_hist": [26.97, 60.92, 130.5, 215.94],
            "fcf_hist": [3.81, 27.02, 60.85, 96.68],
            "years_proj": [2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037],
            "revenue_proj": [396, 673, 850, 1000, 1120, 1220, 1300, 1365, 1420, 1470, 1522],
            "fcf_proj": [138.6, 242.28, 323.0, 400.0, 470.4, 536.8, 585.0, 627.9, 667.4, 698.25, 730.56],
            "unit": "$bn", "fcf_label": "FCFF",
            "note": "History: company filings via yfinance (fiscal years end January; shown by calendar year). "
                    "Projection: base-case FCFF from the scenario DCF; FY2027E $396B anchors on Q2 actual + "
                    "Q3 $108B guidance run-rate.",
        },
        "composition": {
            "bear": {"pv_explicit": 816.86, "pv_terminal": 514.96},
            "base": {"pv_explicit": 2699.05, "pv_terminal": 2537.91},
            "bull": {"pv_explicit": 3933.06, "pv_terminal": 4956.79},
            "unit": "$bn",
        },
        "extra": {
            "type": "line",
            "title": "Profitability — gross vs. net margin (actual)",
            "years": [2023, 2024, 2025, 2026],
            "series": [
                {"label": "Gross margin", "values": [56.9, 72.7, 75.0, 71.1]},
                {"label": "Net margin", "values": [16.2, 48.8, 55.8, 55.6]},
            ],
            "ylabel": "%",
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "NVDA-equity-research-note-polished.pdf")
build_note(data, out)
print("built:", out)
