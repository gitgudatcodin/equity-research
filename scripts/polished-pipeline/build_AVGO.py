"""Polished note: Broadcom (AVGO) — REDUCE, fair value $235.00.

Authoritative scenario numbers are from the current hypergrowth-regime
research note and its segmented 10-year DCF model (FY2026E-FY2035):
bear $69.2 / base $233.9 / bull $402.1, weighted $234.8 -> $235 target.
The AI-exposed segment (~$58B FY2026) runs under the hypergrowth-regime
framework (years 1-3 at/near guidance on verifiable demand evidence;
skepticism loaded into supercycle duration and post-cycle fade); the non-AI
segment (~$48B: VMware + non-AI semis) is valued on standard ~5% growth at
~40% FCF margins. Discounts 12.5%/10%/8.5%; terminal growth 1%/2.5%/2.5%.
History: company filings via Yahoo Finance (Oct 2026). All prose is fresh
October 4, 2026 analysis.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note, validate

data = {
    "ticker": "AVGO",
    "company": "Broadcom Inc.",
    "exchange": "NASDAQ",
    "sector": "Technology — Semiconductors & Infrastructure Software",
    "verdict": "REDUCE",
    "fair_value": 235.00,
    "price": 355.14,
    "risk": "Medium-High",
    "headline": "The $73 billion backlog is real — and at this price, fully priced",
    "ceo": "Hock Tan",
    "hq": "Palo Alto, California",
    "snapshot": [
        ("Market cap", "~$1.70 tn (4.77 bn sh × $355.14)"),
        ("52-week range", "~$290 – $495"),
        ("Price / fair value", "$355.14 / $235.00"),
        ("Implied downside", "−33.9%"),
        ("Enterprise value / net debt", "~$1.73 tn / ~$35.4 bn"),
        ("FQ3 FY26 revenue", "$29.59 bn (+86% YoY)"),
        ("AI semiconductor revenue (FQ3)", "$16.7 bn (+221% YoY)"),
        ("Committed AI backlog", "~$73 bn (company-disclosed, ~18 months)"),
        ("Next catalyst", "FQ4 FY26 earnings (early December)"),
        ("Sell-side view", "Buy; average target ~$527"),
    ],
    "thesis": [
        "Broadcom's AI-exposed revenue — custom AI accelerators (XPUs) plus AI networking — "
        "qualifies for the hypergrowth-regime valuation framework this note uses: verifiable "
        "demand evidence, not narrative. Management discloses a committed AI backlog of "
        "about $73 billion, scheduled for delivery over roughly 18 months — more than 12 "
        "months of guided FY2026 AI revenue (~$58B). And hyperscaler capex commitments name "
        "the category explicitly: Google's TPU partnership running through 2031; Meta "
        "co-developing multiple MTIA generations with more than a gigawatt of custom "
        "silicon to start; Anthropic scaling from 1 gigawatt of Broadcom-designed silicon in "
        "2026 to 5 gigawatts in 2027 with line of sight to ten more in 2028; OpenAI's first "
        "custom chip, unveiled with Broadcom in June 2026, deploying by end of year. So "
        "years 1–3 of the AI segment run at or near management guidance in this note: "
        "FY2027 AI revenue of about $105B against management's line of sight to in excess "
        "of $100 billion, with no mechanical haircut.",
        "But the framework cuts both ways, and the market only prices one edge of it. "
        "Skepticism concentrates where it belongs: in supercycle duration and post-cycle "
        "fade. The $73B backlog and the gigawatt-scale commitments underwrite FY2027–FY2029 "
        "— they do not underwrite FY2035. After the supercycle, AI silicon is still "
        "silicon: in our base case AI-segment free-cash-flow margins compress from a ~45% "
        "peak to 38% through-cycle, and AI revenue growth fades to low-single digits by the "
        "early 2030s. The bear case models what this business structure demands — an abrupt "
        "cliff: book-to-bill collapsing, double-ordered XPUs being digested, a scale-back "
        "by the marginal customer (Anthropic), because custom AI silicon has no secondary "
        "market and no merchant outlet. There is no graceful mean-reversion for a "
        "six-customer franchise.",
        "One guardrail matters enormously: the hypergrowth treatment applies only to the "
        "AI-exposed segment (~$58B of FY2026 revenue). VMware — infrastructure software at "
        "a ~$29B run-rate, roughly a third of revenue — and the non-AI semiconductor lines "
        "are valued on standard 5%-ish growth with stable ~40% FCF margins. The headline "
        "AI numbers must not leak into the whole base. Run that way, the three scenarios "
        "are $69 / $234 / $402, weighted (25/50/25) to $235 — 33.9% below the $355.14 "
        "quote. Even with years 1–3 at guidance and a six-year bull runway, the price "
        "embeds a longer, fatter supercycle than the evidence supports. The $73B backlog "
        "is real. It is also, at this price, fully priced — the market is valuing it as if "
        "it were perpetual. REDUCE.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("The demand evidence is the strongest of any AI-infrastructure name we cover — and it has an expiry date. ",
         "A $73B committed backlog, six confirmed hyperscale XPU customers, and "
         "multi-generation co-development engagements are contracted engineering revenue "
         "with 18 months of visibility. That underwrites the ramp, not the decade: $73B "
         "over 18 months is ~2.5 quarters of FY2027 guided revenue."),
        ("Concentration is the load-bearing assumption. ",
         "The path from ~$58B to $100B+ of AI revenue runs through six customers, and the "
         "marginal one is Anthropic — a private company the holder cannot own and cannot "
         "diligence. Broadcom's own filings flag dependence on a limited number of "
         "significant customers."),
        ("VMware is the ballast that makes the cyclicality ownable. ",
         "~$29B run-rate software at ~78% operating margins funds the dividend, the "
         "deleveraging, and the R&D for the next XPU generation. The AI story gets the "
         "multiple; VMware pays for the optionality — and it gets no hypergrowth "
         "treatment, by rule."),
    ],
    "business": [
        "Broadcom reports two segments. Semiconductor Solutions (about two-thirds of "
        "revenue) spans custom AI accelerators (XPUs) co-designed with hyperscalers, AI "
        "Ethernet switching and routing (Tomahawk, Jericho), broadband, wireless "
        "connectivity, and storage/networking chips. Infrastructure Software is VMware — "
        "virtualization, private cloud, and mainframe/security software — acquired for $69B "
        "in November 2023 and converted to a subscription model at materially higher "
        "prices. This note values them separately: the semiconductor segment is split "
        "again into an AI-exposed portion (~$58B FY2026), which gets the hypergrowth-regime "
        "treatment, and a non-AI portion (~$48B including VMware), which does not.",
        "The AI franchise works like this: a hyperscaler brings a model architecture and a "
        "scale target; Broadcom co-designs the accelerator, the interconnect, and "
        "increasingly the rack-scale networking around it; TSMC fabricates; the customer "
        "commits to multi-generation roadmaps. Six such engagements are confirmed: Google "
        "(seven TPU generations, currently Ironwood, partnership through 2031), Meta (MTIA "
        "training and inference, >1GW to start), OpenAI (inference chip, deploying "
        "end-2026), Anthropic (1GW in 2026, 5GW in 2027, line of sight to 10 more in 2028 — "
        "set to become the largest XPU customer in 2027), ByteDance, and Fujitsu. The "
        "economics are exceptional while the cycle runs — ~45% FCF margins at peak — "
        "because the R&D is amortized over gigawatt-scale deployments and the customer "
        "funds the roadmap certainty.",
        "VMware, the second business, did $7.2B in FQ2 FY2026 (32% of revenue) at ~78% "
        "operating margins. The controversial post-acquisition price increases are largely "
        "through the base; growth has slowed to high single digits as the "
        "perpetual-to-subscription transition completes in late 2026.",
    ],
    "business_bullets": [
        ("Custom XPUs: six customers, gigawatt scale. ",
         "Co-designed accelerators for Google, Meta, OpenAI, Anthropic, ByteDance, and "
         "Fujitsu. Third-party estimates put Broadcom at ~60% of the custom AI ASIC market "
         "by 2027. TCO 30–50% lower than GPUs for fixed hyperscale workloads — against "
         "total inflexibility if model architectures shift."),
        ("AI networking: the stickiest layer. ",
         "Tomahawk 6 and the AI Ethernet switch backlog (over $10B) ride the same capex "
         "wave with less architectural risk than any single accelerator generation; the "
         "industry's migration toward open Ethernet standards is the structural tailwind."),
        ("VMware: the annuity. ",
         "~$29B run-rate infrastructure software at ~78% operating margins. The "
         "perpetual-to-subscription transition completes in late 2026; growth has slowed to "
         "high single digits — valued on standard growth, no hypergrowth treatment."),
        ("TSMC is the bottleneck Broadcom doesn't control. ",
         "Management says foundry capacity is constrained into next year. A large share of "
         "guided revenue is booked and waiting on foundry supply to convert on schedule."),
    ],
    "outlook": [
        "The next three years are underwritten by evidence: the $73B backlog plus named "
        "gigawatt-scale programs carry FY2027–FY2029 in every scenario — our base case has "
        "AI revenue at ~$105B in FY2027 (guidance, unhaircut), $140B in FY2028, $165B in "
        "FY2029. The debate is what happens after. In the base case the fade begins "
        "FY2030–32 as custom-silicon mix normalizes: AI revenue growth falls to low-single "
        "digits by the early 2030s and AI-segment FCF margins compress from the ~45% peak "
        "to 38% through-cycle. AI is ~60% of FY2035 revenue in the base case (vs ~54% in "
        "FY2026) — the franchise grows, but the supercycle ends.",
        "The bull case extends the runway to six full years (FY2027–32): Anthropic's 10GW "
        "line-of-sight converts, a seventh customer qualifies, TPU-through-2031 compounds — "
        "$312B of AI revenue in FY2035 and a $402 fair value that still offers only 13% "
        "upside from $355.14. The bear case is the cliff the structure demands: hypergrowth "
        "ends abruptly mid-FY2027, book-to-bill collapses, double-ordered XPUs digest "
        "through FY2028–29, Anthropic scales back — FY2035 AI revenue of $78B, FCF margins "
        "compressed to 30%, and a $69 fair value that is an 81% drawdown. A six-customer "
        "custom-silicon franchise has earned that drawdown before in prior cycles.",
        "Two tripwires govern the call. The hypergrowth framework is revoked for the AI "
        "segment — fair value falling toward ~$190 — if book-to-bill prints below 1.0 for "
        "two consecutive quarters or lead times normalize with no replacement bottleneck. "
        "The REDUCE is falsified upward if Anthropic's 10GW line-of-sight converts to firm "
        "multi-year purchase commitments with TSMC capacity resolved — that extends the "
        "bull duration and reprices the weighted average toward $300+.",
    ],
    "financials": [
        "FQ3 FY2026 revenue was $29.59 billion (+86% YoY) with AI semiconductor revenue of "
        "$16.7 billion (+221%) — operating costs barely moved on the ramp, the operating "
        "leverage of the custom-silicon model showing through. Annual revenue grew from "
        "$35.8 billion in FY2023 to $63.9 billion in FY2025, with free cash flow (operating "
        "cash flow less capex) of $26.9 billion in FY2025. The balance sheet carries ~$59 "
        "billion of gross debt against ~$24 billion of cash ($35.4 billion net debt); the "
        "VMware acquisition's amortization still depresses GAAP earnings, so the multiple "
        "debate is permanently fought on non-GAAP figures.",
        "The scenario DCF splits the firm in two. The AI segment (~$57.6B FY2026) runs the "
        "hypergrowth-regime framework: years 1–3 at/near guidance, all skepticism in "
        "duration and fade, terminal on through-cycle AI-segment FCF margins of 30%/38%/40% "
        "(never the ~45% peak). The non-AI segment (~$48.4B) grows at −1%/+5%/+7% across "
        "scenarios at stable ~40% FCF margins. Equity is firm EV minus $35.4B net debt over "
        "4.7736B diluted shares. Terminal value is 52% of base-case EV (no haircut "
        "required); 62% in the bull, 30% in the bear. Cross-check: 15x FY2028E non-GAAP "
        "EPS on trough-cycle earnings implies ~$210; the DCF sits above it because the DCF "
        "owns the supercycle cash flows directly rather than capitalizing a single year's "
        "earnings.",
    ],
    "fin_table": {
        "headers": ["$bn", "FY2023", "FY2024", "FY2025", "FQ3 FY26"],
        "rows": [
            ["Revenue", "35.8", "51.6", "63.9", "29.6"],
            ["AI semiconductor revenue", "—", "—", "—", "16.7"],
            ["Free cash flow (OCF − capex)", "17.6", "19.4", "26.9", "—"],
            ["Committed AI backlog", "—", "—", "—", "~73"],
            ["Gross debt / cash", "—", "—", "—", "~59 / ~24"],
        ],
        "footnote": "Annual figures from company filings via Yahoo Finance (fiscal years "
                    "end Oct/Nov). Quarterly figures from the FQ3 FY2026 release "
                    "(September 2026). — = not disclosed in that period.",
    },
    "moat": [
        ("Co-design entrenchment with six hyperscalers. ",
         "Multi-generation XPU roadmaps (Google through 2031, Meta MTIA, Anthropic to "
         "10GW) are engineering partnerships, not chip purchases — switching costs are "
         "measured in years and gigawatts."),
        ("AI Ethernet: the defensible layer. ",
         "Tomahawk 6 at 102.4 Tbps and a $10B+ AI Ethernet backlog ride the industry's "
         "migration to open standards — less architectural risk than any single "
         "accelerator generation, compounding across cycles."),
        ("VMware switching costs fund the optionality. ",
         "The controversial price increases monetize deep enterprise entrenchment; the "
         "~78%-margin annuity funds dividends, deleveraging, and next-generation XPU R&D."),
        ("The moat's limits: concentration and inflexibility. ",
         "Six customers, one foundry (TSMC), and silicon that cannot be repurposed if "
         "architectures shift — the customer owns the roadmap, Broadcom owns the "
         "execution risk. Marvell trails by a generation, but NVIDIA's CUDA ecosystem is "
         "the permanent alternative."),
    ],
    "valuation_method": "Segmented 10-year scenario DCF (hypergrowth-regime framework)",
    "valuation_intro": [
        "We value Broadcom on a segmented 10-year scenario DCF (FY2026E–FY2035), weighted "
        "25% / 50% / 25%. The AI-exposed segment (~$57.6B of FY2026 revenue) runs under "
        "the hypergrowth-regime framework: it qualifies on verifiable demand evidence "
        "(committed ~$73B backlog covering 12+ months of guided revenue; named hyperscaler "
        "capex commitments), so years 1–3 run at or near guidance with no mechanical "
        "haircut, and all skepticism is loaded into supercycle duration and post-cycle "
        "margin fade. The non-AI segment (~$48.4B: VMware plus non-AI semis) grows at "
        "−1%/+5%/+7% across scenarios at stable ~40% FCF margins — no hypergrowth "
        "treatment, by rule.",
        "Discounts: base 10% (beta 1.46, semi cyclicality, six-customer AI concentration, "
        "$59B of gross debt — but 46% FCF margins and a VMware annuity keep it out of the "
        "speculative tier), bear 12.5% (base + 250bp), bull 8.5% (base − 150bp). Terminal "
        "growth is 1.0%/2.5%/2.5% on year-10 FCF at through-cycle margins (AI segment "
        "30%/38%/40% — never the ~45% peak). Equity is firm EV minus $35.4B of net debt, "
        "over 4.7736B diluted shares. Scenario fair values: $69 / $234 / $402, weighting "
        "to $234.75 — our $235 target, 33.9% below the $355.14 quote. The net effect of "
        "the framework is a fair value essentially unchanged from a standard disciplined "
        "DCF — because the evidence supports the ramp but not the perpetuity the price "
        "implies.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 69.20,
            "assumptions": ("Hypergrowth ends abruptly mid-FY27: book-to-bill collapse, "
                            "double-ordered XPU digestion FY28–29, Anthropic scale-back; "
                            "AI-segment FCF margins compress 44% → 30%; terminal derated "
                            "to 1.0%."),
            "rev_cagr": "+1.6%", "margin_end": "34%",
            "discount": 0.125, "terminal_g": 0.01, "tv_share": 0.304,
            "pv_explicit": 254.4, "pv_terminal": 111.1, "cashflow_unit": "$bn",
        },
        "base": {
            "fair_value": 233.90,
            "assumptions": ("Hypergrowth FY27–29 (backlog + gigawatt commitments), fade "
                            "FY30–32 as custom-silicon mix normalizes; AI revenue "
                            "$105B → $140B → $165B; through-cycle AI FCF margins 38%."),
            "rev_cagr": "+12.1%", "margin_end": "39%",
            "discount": 0.10, "terminal_g": 0.025, "tv_share": 0.523,
            "pv_explicit": 549.4, "pv_terminal": 602.3, "cashflow_unit": "$bn",
        },
        "bull": {
            "fair_value": 402.10,
            "assumptions": ("Six-year runway FY27–32: Anthropic 10GW line-of-sight "
                            "converts, a 7th customer qualifies, TPU-through-2031 "
                            "compounds; AI-segment FCF margins 40% through-cycle."),
            "rev_cagr": "+15.9%", "margin_end": "40%",
            "discount": 0.085, "terminal_g": 0.025, "tv_share": 0.62,
            "pv_explicit": 742.9, "pv_terminal": 1212.0, "cashflow_unit": "$bn",
        },
    },
    "scenario_note": "Firm-level FCF margins at year 10; AI-segment through-cycle margins "
                     "are 30%/38%/40% (never the ~45% peak). Equity = firm EV − $35.4B net "
                     "debt, over 4.7736B diluted shares.",
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "risks": [
        ("Customer concentration (the #1 risk). ",
         "Six XPU customers; the marginal growth engine is Anthropic, a private company. "
         "A single program cancellation or architecture pivot removes tens of billions of "
         "forward revenue with no merchant offset."),
        ("TSMC capacity. ",
         "Broadcom doesn't fabricate. Capacity constrained into next year; guided revenue "
         "is booked but not yet converted."),
        ("Architecture inflexibility. ",
         "An XPU optimized for today's models cannot be repurposed. The customer owns the "
         "roadmap; Broadcom owns the execution risk."),
        ("VMware pricing exhaustion. ",
         "The perpetual-to-subscription transition completes in late 2026; software growth "
         "has slowed to high single digits. Further price increases risk accelerating "
         "defections to Nutanix or public cloud."),
        ("AI-capex digestion. ",
         "Hyperscaler capex is at historic highs; any pause — rates, power constraints, "
         "ROI questions — hits custom silicon first, the most discretionary layer of the "
         "stack."),
        ("Leverage and the non-GAAP gap. ",
         "$59B of gross debt; GAAP earnings remain depressed by acquisition amortization, "
         "so the valuation debate is permanently fought on adjusted numbers."),
    ],
    "falsification": (
        "The hypergrowth framework behind this valuation is revoked for the AI segment — "
        "fair value falling toward ~$190 on standard growth treatment — if book-to-bill "
        "falls below 1.0 for two consecutive quarters or lead times normalize with no "
        "replacement bottleneck (TSMC constraint clears). The REDUCE itself is falsified "
        "upward if Anthropic's 10GW line-of-sight converts to firm multi-year purchase "
        "commitments with TSMC capacity resolved — that extends the bull duration and "
        "reprices the weighted average toward $300+. We watch: book-to-bill and lead-time "
        "commentary each quarter, Anthropic's gigawatt conversion milestones, TSMC capacity "
        "statements, VMware's post-transition growth rate, and any seventh qualifying XPU "
        "customer."
    ),
    "methodology": [
        "We value Broadcom on a segmented 10-year scenario discounted-cash-flow "
        "framework (FY2026E–FY2035), probability-weighted 25% / 50% / 25%. The "
        "AI-exposed semiconductor segment is valued under a hypergrowth-regime "
        "framework: it qualifies only on verifiable demand evidence (committed backlog "
        "covering 12+ months of guided revenue; named hyperscaler capex commitments), in "
        "which case years 1–3 run at or near guidance with no mechanical haircut and all "
        "skepticism is formalized as explicit supercycle-duration assumptions and "
        "post-cycle margin compression per scenario. The non-AI segment (VMware plus "
        "non-AI semis) receives no hypergrowth treatment, by rule.",
        "Discount rates are scenario-specific: base 10%, bear 12.5% (base + 250bp), bull "
        "8.5% (base − 150bp). Terminal growth is 1.0%/2.5%/2.5%, applied to year-10 free "
        "cash flow at through-cycle margins — never peak margins. The bear case is "
        "required to be genuinely adverse and to sit below the current price; terminal "
        "value exceeding 70% of enterprise value is haircut and disclosed (52% base, 62% "
        "bull, 30% bear — no haircut required).",
        "We cross-check the DCF against trough-cycle earnings multiples and "
        "reverse-DCF implied growth. The published target is the probability-weighted "
        "fair value, stated as a 12-month horizon reference. Risk ratings (Low / Medium / "
        "Medium-High / High) combine business volatility, balance-sheet strength, and "
        "valuation; Medium-High here reflects six-customer concentration and foundry "
        "dependence against a genuine contracted backlog.",
    ],
    "charts": {
        "scenario": {"bear": 69.20, "base": 233.90, "bull": 402.10,
                     "weighted": 235.00, "price": 355.14},
        "trajectory": {
            # history: filings via Yahoo Finance (FY ends Oct/Nov; OCF - capex)
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [33.20, 35.82, 51.57, 63.89],
            "fcf_hist": [16.32, 17.64, 19.41, 26.92],
            # base-case projection: model series FY2026-FY2035
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035],
            "revenue_proj": [106.0, 155.8, 193.4, 221.0, 240.8, 256.8, 269.9, 280.1, 288.5, 297.1],
            "fcf_proj": [44.7, 67.6, 84.3, 95.0, 101.8, 106.6, 110.0, 112.0, 113.2, 114.4],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via Yahoo Finance (fiscal years; FCF = "
                    "operating cash flow less capex). Projection: base-case model series "
                    "FY2026E–FY2035 (firm revenue and free cash flow; AI segment ~54% of "
                    "FY2026 revenue, ~60% of FY2035).",
        },
        "composition": {
            "bear": {"pv_explicit": 254.4, "pv_terminal": 111.1},
            "base": {"pv_explicit": 549.4, "pv_terminal": 602.3},
            "bull": {"pv_explicit": 742.9, "pv_terminal": 1212.0},
            "unit": "$bn",
        },
        "extra": {
            "type": "pie",
            "title": "FY2026E revenue: AI-exposed vs. non-AI (~$106 bn)",
            "labels": ["AI-exposed semis", "Non-AI (VMware + other semis)"],
            "values": [57.6, 48.4],
        },
    },
}

validate(data)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "AVGO-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
