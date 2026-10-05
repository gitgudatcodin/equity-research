"""CDNS polished note. Research analysis, not investment advice.

Scenario numbers: authoritative compounder-quality override rebuild
(~/workspace/compounder-screen/rebuild.py engine, master addenda PDF):
bear $65.10 / base $339.37 / bull $488.36, weighted $308.05 -> $308 target.
15-yr explicit base/bull (10-yr bear), 8.0% base discount (strongest band), term g cap 3.0%.
History: yfinance annuals. Projection: base-case model series (FY2027-2041, chart to 2036).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

base_rev_15 = [7.06, 7.90, 8.85, 9.91, 11.10, 12.44, 13.93, 15.60, 17.47, 19.57,
               21.56, 23.37, 24.92, 26.11, 26.90]
base_fcf_15 = [2.16, 2.43, 2.74, 3.08, 3.47, 3.90, 4.39, 4.95, 5.56, 6.26,
               6.90, 7.48, 7.97, 8.36, 8.61]

data = {
    "ticker": "CDNS",
    "company": "Cadence Design Systems, Inc.",
    "exchange": "NASDAQ",
    "sector": "Technology — EDA & Systems Design Software",
    "verdict": "HOLD",
    "fair_value": 308.00,
    "price": 351.35,
    "risk": "Medium",
    "headline": "The Picks and Shovels of the Chip Supercycle — at a Supercycle Price",
    "ceo": "Anirudh Devgan",
    "hq": "San Jose, California",
    "snapshot": [
        ("Market cap", "~$97 bn (0.275 bn sh × $351.35)"),
        ("Net debt", "~$1.1 bn (enterprise value ≈ $98 bn)"),
        ("52-week range", "~$262.75 – $416.69"),
        ("Gross margin", "~88% (FY2025); FCF margin ~30%"),
        ("Revenue mix", "Design IP ~13%; EDA software the rest"),
        ("Design IP growth", "+42% YoY (FY2025)"),
        ("OpenAI contract", "$200M compute commitment (strategic, not revenue)"),
        ("Backlog", "~$7.6 bn"),
        ("Next catalyst", "Q1'26 results; EDA license-renewal linearity"),
    ],
    "thesis": [
        "Cadence sells the picks and shovels of the semiconductor supercycle — the electronic design "
        "automation software without which no chip gets built — and it sells them with the economics of a "
        "monopoly: ~88% gross margins, ~30% free-cash-flow margins, a ~$7.6 billion backlog, and a "
        "two-player market shared with Synopsys. Every AI accelerator, every custom-silicon program at the "
        "hyperscalers, every automotive chip pays the EDA toll. The business is, on a through-cycle basis, "
        "one of the finest software franchises ever built. The stock at $351.35 is priced as though the "
        "supercycle's growth rate were the through-cycle growth rate. It is not.",
        "Our judgment, and the reason this is a HOLD rather than a buy, is duration versus price. The "
        "base case ($339.37) grants a 12.0% revenue CAGR for a decade — EDA growing with R&D budgets, design "
        "IP compounding at high-teens rates on the AI custom-silicon wave, margins gliding to a 32% "
        "through-cycle FCF level — and it is still worth less than the current quote. The market is paying "
        "for something between our base and our bull ($488.36): 15%+ revenue compounding for a decade with "
        "35% terminal FCF margins. That is the AI-supercycle-permanent case, and it requires believing that "
        "chip R&D intensity never mean-reverts.",
        "The falsification-relevant question is what EDA demand looks like when the AI capex wave crests. "
        "History is instructive: EDA revenue is tied to semiconductor R&D headcount and design starts, not "
        "to chip unit volumes — which makes it steadier than the semis themselves, but not immune. In a "
        "design-start downturn, license renewals get renegotiated, IP royalties fall with chip shipments, "
        "and the 30%-margin machine shows its operating leverage. Our bear case ($65.10) models exactly "
        "that: 2.0% revenue CAGR for a decade, margins compressing to 24% as pricing power meets a buyer's "
        "market. It is a genuine washout — and it is the scenario the price assigns zero weight.",
        "The forward view: Cadence will be a larger, more IP-weighted, and structurally better business in "
        "five years — design IP at 13% of revenue growing 42% is the future mix, and the AI custom-silicon "
        "wave (including the strategic OpenAI relationship) extends the runway. We would own this franchise "
        "at a price that compensates for the cycle. That price is around $308, not $351. HOLD: a superb "
        "business at a full price, with the upside reserved for the bull case that the market has already "
        "half-priced.",
    ],
    "thesis_bullets": [
        ("The tollbooth is real. ",
         "~88% gross margins, ~30% FCF margins, ~$7.6B backlog, a duopoly with Synopsys — every AI chip "
         "pays the EDA toll. This is the highest-quality software economics in the semiconductor "
         "ecosystem."),
        ("Design IP is the growth engine. ",
         "13% of revenue growing 42% YoY — the AI custom-silicon wave (hyperscaler ASICs, OpenAI "
         "relationship) turns Cadence from a tools vendor into an IP participant."),
        ("But the price is the supercycle-permanent case. ",
         "Our base case grants 12% revenue CAGR for a decade and is worth $339.37. The market at $351.35 "
         "is paying for the bull case's 15% CAGR — growth that assumes chip R&D intensity never "
         "mean-reverts."),
    ],
    "business": [
        "Cadence (founded 1988) provides the software, hardware emulation, and intellectual property used to "
        "design semiconductors and electronic systems. The core EDA business — digital and custom/analog "
        "design tools, verification, and Palladium/ZeBu hardware emulation — is sold primarily as "
        "multi-year term licenses to every major chipmaker and systems company in the world. Design IP "
        "(~13% of revenue) licenses interface, memory, and processor IP blocks that customers integrate "
        "into their chips — the fastest-growing segment at +42% in FY2025, riding the AI custom-silicon wave.",
        "Fiscal 2025 produced revenue of $5.3 billion with free cash flow of $1.59 billion — a 30.0% FCF "
        "margin on ~88% gross margins. The backlog of ~$7.6 billion provides unusual forward visibility for "
        "a software business. The competitive structure is a duopoly with Synopsys; Siemens EDA is a distant "
        "third. Customer concentration is real — a handful of large chipmakers and hyperscalers drive "
        "disproportionate revenue — but the switching costs are among the highest in enterprise software: "
        "ripping out a design flow mid-program is effectively unthinkable.",
        "The forward picture is a mix shift toward IP and systems. Design IP's 42% growth rate will not "
        "persist indefinitely, but the structural driver — hyperscalers and AI labs designing their own "
        "silicon rather than buying merchant chips — has years to run. The strategic relationship with "
        "OpenAI (a $200 million compute commitment, not revenue) signals where the industry's center of "
        "gravity is moving: toward the AI labs as the defining customers of the next decade. Cadence's "
        "position as the design platform for that silicon is the bull case's foundation — and the reason the "
        "bear case's 2% CAGR would require a genuine design-start recession.",
    ],
    "business_bullets": [
        ("Core EDA: the duopoly toll. ",
         "Digital/custom design tools and hardware emulation sold as multi-year term licenses; ~$7.6B "
         "backlog; switching costs among the highest in enterprise software."),
        ("Design IP (~13%, +42% YoY). ",
         "Interface, memory, and processor IP for the custom-silicon wave — the growth engine and the "
         "future mix."),
        ("The OpenAI relationship. ",
         "A $200M compute commitment (strategic, not revenue) that positions Cadence at the AI labs — "
         "the defining customers of the next decade's silicon."),
        ("Customer concentration. ",
         "A handful of large chipmakers and hyperscalers drive disproportionate revenue — the "
         "franchise's structural vulnerability."),
    ],
    "outlook": [
        "The next three years are strong by construction. The AI custom-silicon wave — hyperscaler ASICs, "
        "AI-lab silicon, automotive compute — drives design starts and IP licensing; the backlog converts "
        "to revenue on multi-year ramps; and EDA pricing holds because the tools are mission-critical to "
        "programs worth billions. Our base case runs revenue from $6.3 billion (FY2026E) to $26.9 billion "
        "by 2041 — a 12.0% 10-year CAGR — with FCF margins gliding from 30.5% to a 32% through-cycle level. "
        "That is an optimistic decade for a tools business, and it is worth $339.37.",
        "The judgment call is the terminal growth rate of chip R&D intensity. The bull case ($488.36) "
        "assumes 15.0% revenue CAGR — EDA growing faster than semiconductor R&D for a decade, design IP "
        "compounding at high-teens rates indefinitely, 35% terminal FCF margins. That requires the AI "
        "supercycle's design intensity to be the new normal rather than a wave. Our view is more measured: "
        "design intensity is genuinely elevated by AI, but the history of semiconductors is waves, and "
        "waves crest. The bear case ($65.10) — 2.0% CAGR, 24% margins, a design-start recession — is what "
        "the price refuses to contemplate.",
        "What would change the call: sustained design-IP growth above 30% with expanding backlog would "
        "validate the bull's mix-shift thesis. A design-start downturn — license renewals renegotiated "
        "down, IP royalties falling with chip shipments — would validate the bear and we would look to buy "
        "the franchise at cyclical prices. Watch: quarterly backlog linearity, design-IP growth "
        "deceleration, and hyperscaler capex commentary.",
    ],
    "financials": [
        "The margin structure is extraordinary and stable: ~88% gross margins, ~30% FCF margins, with our "
        "model gliding from 30.5% to a 32% through-cycle terminal level in the base case. FY2025 free cash "
        "flow of $1.59 billion on $5.3 billion of revenue; our FY2026E anchor is $6.3 billion of revenue. "
        "Revenue history shows the compounding: $3.56B (2022), $4.09B (2023), $4.64B (2024), $5.30B (2025) — "
        "steady mid-teens growth with none of the cyclicality of the chipmakers themselves. That steadiness "
        "is the franchise's signature and the reason the market pays up.",
        "The balance sheet is clean: ~$1.1 billion of net debt against a ~$97 billion market cap — "
        "effectively unlevered. Capital return is modest relative to cash generation; the company's "
        "preference has been reinvestment in R&D and tuck-in IP acquisitions. At 0.275 billion shares, our "
        "$308 target implies roughly $85 billion of equity value against a base-case EV of $94.6 billion.",
    ],
    "fin_table": {
        "headers": ["$ bn", "FY2022", "FY2023", "FY2024", "FY2025"],
        "rows": [
            ["Revenue", "3.56", "4.09", "4.64", "5.30"],
            ["YoY growth", "—", "+15%", "+13%", "+14%"],
            ["Gross margin", "—", "—", "~87%", "~88%"],
            ["Free cash flow", "1.12", "1.25", "1.12", "1.59"],
            ["FCF margin", "31.5%", "30.6%", "24.1%", "30.0%"],
            ["Design IP / growth", "—", "—", "~12%", "~13% / +42%"],
        ],
        "footnote": "Sources: company releases; annuals via yfinance. FY2026E: $6.3B revenue (model anchor); "
                    "backlog ~$7.6B.",
    },
    "moat": [
        ("The duopoly. ",
         "Cadence and Synopsys split the EDA market; Siemens EDA is a distant third. The tools are "
         "mission-critical to multi-billion-dollar chip programs — customers do not switch to save "
         "license fees."),
        ("Switching costs. ",
         "Ripping out a design flow mid-program is effectively unthinkable; design teams, scripts, and "
         "IP are all flow-specific. Renewal rates are the envy of enterprise software."),
        ("The IP flywheel. ",
         "Design IP licensed into customer chips creates royalty streams and deepens the design-win "
         "relationship — the fastest-growing, highest-leverage part of the mix."),
        ("The moat's boundary is design starts. ",
         "In a design-start recession, even unswitchable customers renegotiate renewals and delay new "
         "licenses. The tollbooth still collects, but the traffic thins."),
    ],
    "valuation_method": "15-year scenario FCF DCF (compounder-quality override)",
    "valuation_intro": [
        "Cadence meets our compounder-quality criteria — sustained ROIC above 15%, stable-to-expanding "
        "gross margins (~88%), and free-cash-flow conversion above 80%, verified from reported history — so "
        "we model a 15-year explicit horizon (10-year bear) at an 8.0% base discount rate (strongest band), "
        "with terminal growth capped at 3.0% applied to demonstrated sustained FCF margins (24% / 32% / "
        "35% — not cyclical peaks). The bear case adds 250bp (10.5%), the bull case subtracts 150bp with an "
        "8% floor (binds at 8.0%), and the three scenarios are weighted 25% / 50% / 25%. Revenue grows at "
        "the scenario CAGR for years 1–10 (+2.0% / +12.0% / +15.0%), fading to terminal growth over years "
        "11–15; FCF margin glides from 30.5% to the terminal margin over 10 years. Net debt $1.1B, 0.2754B "
        "shares. Terminal value is 40–62% of EV across scenarios — no haircut required.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 65.10,
            "assumptions": "A design-start recession: license renewals renegotiated down, IP royalties fall with chip shipments; 2.0% revenue CAGR for a decade; FCF margins compress to 24% as pricing power meets a buyer's market",
            "rev_cagr": "+2.0%", "margin_end": "24%",
            "discount": 0.105, "terminal_g": 0.015, "tv_share": 0.402,
            "pv_explicit": 11.39, "pv_terminal": 7.66, "cashflow_unit": "$bn",
        },
        "base": {
            "fair_value": 339.37,
            "assumptions": "The AI custom-silicon wave sustains elevated design intensity: 12.0% revenue CAGR; design IP compounds on hyperscaler/AI-lab silicon; FCF margins glide to a 32% through-cycle level",
            "rev_cagr": "+12.0%", "margin_end": "32%",
            "discount": 0.08, "terminal_g": 0.03, "tv_share": 0.591,
            "pv_explicit": 38.69, "pv_terminal": 55.89, "cashflow_unit": "$bn",
        },
        "bull": {
            "fair_value": 488.36,
            "assumptions": "The supercycle's design intensity is the new normal: 15.0% revenue CAGR for a decade; design IP compounds at high-teens rates indefinitely; 35% terminal FCF margins",
            "rev_cagr": "+15.0%", "margin_end": "35%",
            "discount": 0.08, "terminal_g": 0.03, "tv_share": 0.620,
            "pv_explicit": 51.49, "pv_terminal": 84.12, "cashflow_unit": "$bn",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "0.25×$65.10 + 0.50×$339.37 + 0.25×$488.36 = $308.05 → $308 target. "
                     "Bear meets all hurt conditions (design-start recession, margin compression, 25%+ derating).",
    "risks": [
        ("Design-start cyclicality. ",
         "EDA revenue follows semiconductor R&D headcount and design starts; a downturn means "
         "renegotiated renewals and delayed licenses — the bear case's mechanism."),
        ("Customer concentration. ",
         "A handful of large chipmakers and hyperscalers drive disproportionate revenue; share loss at "
         "any one of them is material."),
        ("Synopsys competition. ",
         "The duopoly is stable but not static; Ansys integration and AI-driven tooling could shift "
         "competitive dynamics."),
        ("AI-supercycle dependency. ",
         "Current growth rates assume elevated AI design intensity; if the capex wave crests, design "
         "starts follow with a lag."),
        ("Valuation. ",
         "At $351.35 the stock prices the bull case's permanence — any deceleration in design-IP growth "
         "or backlog reprices toward the base ($339.37)."),
    ],
    "falsification": (
        "The base case's design-intensity assumption would be withdrawn if the backlog declines for two "
        "consecutive quarters or if design-IP growth decelerates below 20% while license renewals are "
        "renegotiated down — at that point the bear case ($65.10) becomes the working assumption. "
        "Conversely, sustained design-IP growth above 30% with expanding backlog validates the bull path. "
        "Watch: quarterly backlog linearity, design-IP growth, hyperscaler capex commentary."
    ),
    "methodology": [
        "Cadence qualifies for the compounder-quality override: sustained ROIC above 15%, stable-to-expanding "
        "gross margins (~88%), and free-cash-flow conversion above 80%, verified from reported history. "
        "Qualifying businesses are valued on a 15-year explicit horizon (10-year bear) at an 8.0–8.5% base "
        "discount rate — the strongest band at 8.0% — with the bear case adding 250bp and the bull case "
        "subtracting 150bp (8% floor). Terminal growth is capped at 3.0% on demonstrated sustained margins, "
        "never peaks. Revenue compounds at the scenario CAGR for years 1–10, fading to terminal growth over "
        "years 11–15; FCF margin glides from the current level to the terminal margin over 10 years. "
        "Scenarios are weighted bear 25% / base 50% / bull 25%. If the qualification criteria fail over any "
        "multi-year window, the business is re-valued at the standard 10% discount over a 10-year horizon. "
        "Bear cases must be genuinely adverse and sit below the current price. The published target is the "
        "probability-weighted fair value, stated as a 12-month horizon reference.",
        "Risk ratings (Low / Medium / Medium-High / High) combine business-model volatility, the balance "
        "sheet, and the valuation. This note is independent research-style analysis for informational purposes "
        "only and is not investment advice. Financial figures are drawn from company releases and SEC filings; "
        "market data as of October 2, 2026. Projections and the price target are the author's estimates and "
        "involve uncertainty. Past performance does not predict future results.",
    ],
    "charts": {
        "scenario": {"bear": 65.10, "base": 339.37, "bull": 488.36, "weighted": 308.05, "price": 351.35},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [3.56, 4.09, 4.64, 5.30],
            "fcf_hist": [1.12, 1.25, 1.12, 1.59],
            "years_proj": [2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": base_rev_15[1:11],
            "fcf_proj": base_fcf_15[1:11],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via yfinance. Projection: base-case FCF from the 15-year "
                    "compounder DCF (shown FY2027–2036; the model runs to 2041, ending at $26.9B revenue / "
                    "$8.6B FCF).",
        },
        "composition": {
            "bear": {"pv_explicit": 11.39, "pv_terminal": 7.66},
            "base": {"pv_explicit": 38.69, "pv_terminal": 55.89},
            "bull": {"pv_explicit": 51.49, "pv_terminal": 84.12},
            "unit": "$bn",
        },
        "extra": {
            "type": "line",
            "title": "FCF margin — history vs. base-case glide path",
            "years": [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "series": [{"label": "FCF margin",
                        "values": [31.5, 30.6, 24.1, 30.0, 30.6, 30.8, 30.9, 31.1, 31.3, 31.4, 31.5, 31.7, 31.8, 32.0, 32.0]}],
            "ylabel": "%",
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "CDNS-equity-research-note-polished.pdf")
build_note(data, out)
print("built:", out)
