"""Polished note: AMD (Advanced Micro Devices) — REDUCE, FV $163.00, price $633.91
(Oct 2, 2026).

Authoritative source: the current rich research note (addendum_c PDF) plus the
scenario model (model_addendum_c.json): bear $34.11 / base $152.50 / bull
$311.94, weighted $162.76 -> $163 target. Discounts bear 14.5% / base 12.0% /
bull 10.5%; terminal g 0% / 2.0% / 2.0%; rev CAGRs +6.5% / +16.3% / +22.3%;
yr-10 FCF margins 13% / 18% / 22%; PV explicit/terminal ($B) from the model;
TV/EV 43% / 49% / 59%. History: yfinance annuals (FY2022–FY2025).
The pre-Addendum-C standalone PDF ($130) is stale and was not used.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

data = {
    "ticker": "AMD",
    "company": "Advanced Micro Devices, Inc.",
    "exchange": "NASDAQ",
    "sector": "Technology — Semiconductors (AI Accelerators & Server CPUs)",
    "verdict": "REDUCE",
    "fair_value": 163.00,
    "price": 633.91,
    "risk": "High",
    "headline": "Fourteen Gigawatts of Contracts, Priced for Forty",
    "hq": "Santa Clara, California",
    "snapshot": [
        ("Market cap", "~$1.03 tn (~1.66 bn dil. sh x $633.91)"),
        ("Enterprise value", "~$1.03 tn"),
        ("Net cash", "~$8.8 bn"),
        ("52-week range", "~$160.49 - $645.46"),
        ("TTM / forward P/E", "~161x / ~57x"),
        ("Q2'26 revenue / data center", "$11.54 bn / $6.72 bn (+107%)"),
        ("Q3'26 guide", "~$13.0 bn (+41% YoY)"),
        ("2027 data-center guide", "~$70 bn (~2x YoY)"),
        ("Contracted deployments", "~14 GW (OpenAI 6 / Meta 6 / Anthropic 2)"),
        ("Street consensus target", "~$620 (Buy)"),
        ("Next catalyst", "Q3 results (early Nov)"),
    ],
    "thesis": [
        "AMD has crossed the line from challenger narrative to contracted infrastructure supplier. "
        "Fourteen gigawatts of committed deployments across OpenAI (6GW), Meta (6GW), and Anthropic (2GW) "
        "— with warrants that only vest as silicon ships — turn the 2027 revenue ramp from a forecast into "
        "a delivery schedule. The strategic question is not whether AMD can sell the 2027 wave — it is sold — "
        "but what happens after the first wave is delivered. We see a genuine multi-year runway: hyperscaler "
        "capex near $800 billion in 2026 and headed toward $1.3 trillion in 2027, sovereign AI as a new "
        "customer class, and AMD establishing itself as the credible second source with double-digit "
        "AI-accelerator share. But the price has skipped the debate entirely.",
        "At $633.91, AMD is valued as if the supercycle never fades and AMD captures far more than "
        "double-digit share. The arithmetic is unforgiving: $634 implies roughly $1.3 trillion of "
        "mid-2030s revenue — a ~44% decade CAGR, about four to five times our bull case. Our three "
        "scenarios are $34 / $153 / $312, weighted to a $163 target, −74.3% against the quote. The business "
        "thesis is intact; the price is not. That is the entire note in two sentences, and the valuation "
        "section shows the work.",
        "What this note does differently from a standard DCF: near-term visibility is unusually high, "
        "because demand is contracted, not extrapolated. Our 2027–28 revenue assumptions track the stated "
        "targets — data center revenue doubling to ~$70 billion in 2027, with AI GPUs in the low $40 "
        "billions — rather than being mechanically haircut, because those targets are now backed by named, "
        "milestone-linked deployments: OpenAI's first gigawatt of MI450s deploying in H2 2026, Meta's on "
        "the same timeline, Anthropic's first gigawatt in H1 2027, Oracle's initial 50,000 MI450s starting "
        "Q3 2026, and a $1.2 billion Vultr Helios order deploying in Q4 2026. Demand evidence must be "
        "AMD-specific, not 'AI is hot' — and here it is: $29–30 billion of AMD's own supply purchase "
        "commitments, the largest TSMC allocation increase of any customer, and ~10% price increases on AI "
        "accelerators. Companies short on demand do not raise prices.",
        "All of the skepticism therefore concentrates where it belongs: in duration and fade. Our base case "
        "gives the hypergrowth phase through 2029 — the committed 14GW deploys through the 2030 milestone "
        "schedules — then fades growth into the single digits with through-cycle FCF margins of 18%. The "
        "bull case extends the supercycle through 2032 (sovereign AI plus an inference replacement cycle) "
        "with 22% terminal FCF margins — still only $312. The bear case is the honest version of 2028–29: "
        "the 2026–27 pre-build overshoots, book-to-bill collapses below 1.0, the $8.5 billion inventory "
        "build becomes a glut, revenue falls ~13% in 2029, and margins compress 500bp as price cuts clear "
        "the channel. Bear $34 — below the price, as a bear must be. REDUCE.",
    ],
    "thesis_subhead": "Why the demand is real — and why the price is wrong anyway",
    "thesis_bullets": [
        ("The demand evidence is verifiable, not narrative. ",
         "14GW contracted across three named counterparties; Oracle and Vultr diversifying the order book; "
         "seven of the world's top 10 AI companies now using Instinct GPUs; supply-side commitments "
         "matching demand. Q2 2026 printed $11.54 billion of revenue (+50% YoY) with data center at $6.72 "
         "billion (+107%)."),
        ("$634 prices ~5x the bull case. ",
         "Even giving AMD the supercycle through 2032 and 22% through-cycle FCF margins — a genuinely "
         "heroic outcome — fair value is $312, less than half the quote. The market is not pricing the "
         "contracted wave; it is pricing a second and third wave nobody has contracted."),
        ("320 million warrants are ~20% potential dilution. ",
         "The OpenAI and Meta warrants (160 million each at $0.01) are the price of the contracts. The "
         "dilution is real, becomes visible in 2027–28 financials, and our per-share values reflect "
         "scenario-specific vesting (1.70 / 1.80 / 1.95 billion shares)."),
        ("The cycle will turn. ",
         "Every semiconductor supercycle ends in a digestion phase. Our bear case prices it in 2028–29; "
         "the market prices no digestion at all."),
    ],
    "business": [
        "Advanced Micro Devices (founded 1969, Santa Clara) is a fabless semiconductor company whose "
        "center of gravity has shifted decisively to the data center. The Data Center segment — EPYC server "
        "CPUs and Instinct AI accelerators — did $6.72 billion in Q2 2026 (+107% YoY), 58% of total revenue, "
        "and is expected to roughly double to ~$70 billion in 2027, with AI GPUs in the low $40 billions and "
        "server CPUs most of the rest. The product engine is the Helios rack-scale AI platform: up to 72 "
        "Instinct MI400/MI450 accelerators paired with 6th-gen EPYC 'Venice' CPUs and Pensando networking — "
        "AMD's answer to NVIDIA's Vera Rubin, sold as a full system rather than merchant silicon. MI450 "
        "production shipments began in Q3 2026 with a sharp Q4 ramp; MI500 is in customer development for "
        "2027.",
        "The rest of the business — Client (Ryzen), Gaming (semi-custom), Embedded (Xilinx) — is roughly "
        "$20 billion of durable, slower-growing revenue that funds the AI build-out and provides ballast if "
        "the accelerator cycle turns. Balance sheet: ~$13.1 billion of cash and short-term investments "
        "against ~$4.3 billion of debt (~$8.8 billion net cash); no refinancing pressure. The P&L is "
        "inflecting: Q2 non-GAAP EPS of $1.66 versus $0.48 a year earlier, data center operating margin "
        "31.3%.",
    ],
    "business_bullets": [
        ("Customer concentration is extreme. ",
         "Three counterparties account for the 14GW. If any one of them pauses, the 2027 guide is at "
         "risk — two of the three CEOs publicly argued for slowing AI capability advancement this year."),
        ("Margins compress before they expand. ",
         "Gross margin edges lower in Q4 and through 2027 as MI450 ramps; rack-scale Helios is a "
         "lower-margin systems sale than merchant silicon. The Q2 FCF print ($1.6 billion) was flattered "
         "by a ~$2.4 billion payables stretch."),
        ("CUDA is still the moat AMD doesn't have. ",
         "ROCm is improving but the software gap is the reason AMD is the second source — and second "
         "sources get second-source economics when the cycle turns."),
        ("Competition sets the terms. ",
         "NVIDIA (>90% AI-accelerator share) defines the market; Broadcom's custom silicon with OpenAI "
         "attacks the same diversification budget; hyperscaler ASICs increasingly absorb inference "
         "workloads. AMD's moat is execution plus openness — loved in shortages, squeezed in gluts."),
    ],
    "outlook": [
        "The open question for the decade is not 2027 — that is contracted — but whether AMD converts a "
        "spectacular deployment wave into a durable franchise: double-digit AI-accelerator share, a closing "
        "ROCm gap, and server-CPU share gains compounding off a much higher base.",
        "Our duration judgment: hypergrowth through 2029 as the committed wave deploys, then fade from "
        "2030 as first-wave capacity digests. The bear case — the 2028–29 digestion cliff — is the honest "
        "version of what every prior semiconductor supercycle has delivered.",
    ],
    "financials": [
        "Revenue grew from $23.6 billion in FY2022 to $34.6 billion in FY2025, with free cash flow "
        "inflecting from $1.1 billion (FY2023) to $6.7 billion (FY2025) — the operating leverage of the "
        "data-center mix shift arriving. Net income of $4.3 billion in FY2025 is up 5x from FY2023. The "
        "business is performing; only the price is in question.",
        "The balance sheet is a fortress: ~$8.8 billion of net cash, no refinancing pressure, and "
        "supply-side commitments ($29–30 billion of purchase commitments) that match the contracted demand. "
        "The financial risk in this note is not distress — it is duration: how long the hypergrowth lasts "
        "before the digestion phase arrives.",
    ],
    "fin_table": {
        "headers": ["$ bn", "FY2024", "FY2025", "Q2'26"],
        "rows": [
            ["Revenue", "25.785", "34.639", "11.54"],
            ["Data center revenue", "—", "—", "6.72"],
            ["Net income", "1.641", "4.335", "—"],
            ["Free cash flow", "2.405", "6.735", "1.6"],
        ],
        "footnote": "Source: company filings via yfinance (FY ends Dec 31); Q2'26 per company release. "
                    "Q2 FCF flattered by a ~$2.4 bn payables stretch.",
    },
    "moat": [
        ("The credible-second-source position is the moat — and it is cyclical. ",
         "AMD is the only credible alternative to a single supplier the entire industry is desperate to "
         "diversify away from. That diversification bid is real, but second sources are loved in shortages "
         "and squeezed in gluts."),
        ("Rack-scale systems capability (ZT Systems). ",
         "Helios moves AMD up the stack from merchant silicon to full systems — higher content per "
         "deployment, but a new execution muscle with qualification risk."),
        ("Open ecosystem vs. CUDA lock-in. ",
         "An open Ethernet/software stack appeals to customers allergic to lock-in — a genuine "
         "differentiator that nonetheless loses to CUDA's installed base in a downturn."),
        ("No software moat. ",
         "ROCm is improving but the software gap is structural; AMD wins on openness and price, which "
         "compress first when the cycle turns."),
    ],
    "valuation_method": "10-year scenario FCFF DCF",
    "valuation_intro": [
        "We value AMD on a 10-year explicit free-cash-flow DCF (FY2026–2036), weights bear 25% / base 50% / "
        "bull 25%. Scenario discounts: base 12.0% (beta 2.55, extreme customer concentration, warrant "
        "overhang, cyclical semiconductors), bear 14.5% (base + 250bp), bull 10.5% (base − 150bp). Terminal "
        "growth 0% / 2.0% / 2.0% on year-10 FCF at normalized through-cycle margins (never peak). Equity = "
        "firm EV plus ~$8.8 billion net cash, over scenario-specific diluted shares (1.70 / 1.80 / 1.95 "
        "billion) reflecting warrant vesting that scales with deployment success. FY2026E revenue anchor: "
        "$48.5 billion.",
        "The base case is the contracted wave, priced honestly: 2027 revenue of $90 billion sits at the "
        "$70 billion data-center guide plus ~$20 billion for the rest of the business — no haircut, because "
        "14GW of named deployments and $29–30 billion of supply commitments are verifiable demand. Growth "
        "runs +31% (2028), +19% (2029), then fades from 2030. FCF margins build from ~10% to a "
        "through-cycle 18%. Result: $152.50 → $153. The bull ($311.94 → $312) extends the supercycle "
        "through 2032 and still lands at less than half the quote. Terminal value is 43–59% of EV across "
        "scenarios (no haircut required).",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 34.00,
            "assumptions": "2026–27 pre-build overshoots; book-to-bill below 1.0; $8.5 bn inventory "
                           "build becomes a glut; revenue falls ~13% in 2029; margins compress 500bp; "
                           "terminal growth 0%",
            "rev_cagr": "+6.5%", "margin_end": "13%",
            "discount": 0.145, "terminal_g": 0.0, "tv_share": 0.43,
            "pv_explicit": 28.12, "pv_terminal": 21.07, "cashflow_unit": "$B",
        },
        "base": {
            "fair_value": 153.00,
            "assumptions": "Contracted 14GW wave delivers; 2027 revenue $90 bn; hypergrowth through "
                           "2029, fade from 2030; through-cycle FCF margins 18%",
            "rev_cagr": "+16.3%", "margin_end": "18%",
            "discount": 0.12, "terminal_g": 0.02, "tv_share": 0.49,
            "pv_explicit": 135.64, "pv_terminal": 130.05, "cashflow_unit": "$B",
        },
        "bull": {
            "fair_value": 312.00,
            "assumptions": "Supercycle through 2032 — sovereign AI plus inference replacement cycle; "
                           "22% terminal FCF margins; still less than half the quote",
            "rev_cagr": "+22.3%", "margin_end": "22%",
            "discount": 0.105, "terminal_g": 0.02, "tv_share": 0.59,
            "pv_explicit": 247.36, "pv_terminal": 352.12, "cashflow_unit": "$B",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Scenario FVs from the note's model (bear $34.11 / base $152.50 / bull $311.94); "
                     "0.25x$34 + 0.50x$153 + 0.25x$312 = $162.76, rounded to the $163 target. PV splits "
                     "in $B from the scenario DCF.",
    "risks": [
        ("Customer concentration. ",
         "Three counterparties account for the 14GW; a pause by any one breaks the 2027 guide."),
        ("Warrant dilution (~20%). ",
         "320 million shares at $0.01 vesting on deployment and price milestones; visible in 2027–28 "
         "financials."),
        ("Execution on Helios/MI450. ",
         "Rack-scale systems are a new muscle; qualification slips or yield issues push the wave right."),
        ("CUDA/ROCm gap. ",
         "The software moat is NVIDIA's; AMD wins on openness and price, which compress first in a glut."),
        ("Cycle digestion. ",
         "$8.5 billion of inventory plus channel pre-building; if 2027 demand was pulled forward, "
         "2028–29 is the cliff."),
        ("Hyperscaler ASICs and export controls. ",
         "Custom silicon competes for the same diversification budget; export controls remain a "
         "geopolitical overhang."),
    ],
    "falsification": (
        "We would withdraw the REDUCE on sustained book-to-bill above 1.5 with lead times extending into "
        "2028 (evidence the wave is bigger than contracted), or year-10 revenue tracking toward $300 "
        "billion-plus with FCF margins above 20% — neither of which the current evidence supports. "
        "Conversely, if book-to-bill falls below 1.0 for two consecutive quarters or lead times normalize, "
        "the contracted-demand assumption is withdrawn and the bear case becomes the base case. Watch Q3 "
        "results (early November) and Q4 Helios shipment volumes against the $70 billion 2027 data-center "
        "guide."
    ),
    "charts": {
        "scenario": {"bear": 34.00, "base": 153.00, "bull": 312.00,
                     "weighted": 163.00, "price": 633.91},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [23.601, 22.680, 25.785, 34.639],
            "fcf_hist": [3.115, 1.121, 2.405, 6.735],
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": [48.5, 90.0, 118.0, 140.0, 157.0, 171.0, 184.0, 196.0, 205.0, 213.0, 220.0],
            "fcf_proj": [4.8, 10.8, 15.3, 19.6, 23.6, 26.5, 29.4, 32.3, 34.9, 37.3, 39.6],
            "unit": "$B", "fcf_label": "FCFF",
            "note": "History: company filings via yfinance (FY ends Dec 31). Projection: base-case FCFF "
                    "path from this note's scenario DCF — the contracted wave through 2029, fading "
                    "from 2030.",
        },
        "composition": {
            "bear": {"pv_explicit": 28.12, "pv_terminal": 21.07},
            "base": {"pv_explicit": 135.64, "pv_terminal": 130.05},
            "bull": {"pv_explicit": 247.36, "pv_terminal": 352.12},
            "unit": "$B",
        },
        "extra": {
            "type": "pie",
            "title": "2027E revenue mix — base case ($bn)",
            "labels": ["Data Center (~$70B guide)", "Client / Gaming / Embedded (~$20B)"],
            "values": [70, 20],
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "AMD-equity-research-note-polished.pdf")
build_note(data, out)
print("built:", out)
