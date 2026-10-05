"""Polished note build: Expand Energy (EXE). Scenario numbers from the authoritative
October 2026 hardened 10-year DCF: bear $31.53 / base $111.16 / bull $195.75, weighted $112.
Re-runnable."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

# DCF composition from stated TV shares of EV (31/42/50%) and net debt $4.3bn / 231.5mn sh
ND_PS = 4.3e9 / 231.5e6  # 18.57
def ev_split(fv, tv):
    ev = fv + ND_PS
    t = round(ev * tv, 2)
    return round(ev - t, 2), t

bear_e, bear_t = ev_split(31.53, 0.31)
base_e, base_t = ev_split(111.16, 0.42)
bull_e, bull_t = ev_split(195.75, 0.50)

data = {
    "ticker": "EXE",
    "company": "Expand Energy Corporation",
    "exchange": "NASDAQ",
    "sector": "Energy — Natural Gas E&P",
    "verdict": "BUY",
    "fair_value": 112.00,
    "price": 85.52,
    "risk": "Medium-High",
    "headline": "The Low-Cost Anchor of US Natural Gas, Priced for Bear-Case Gas Forever",
    "hq": "Oklahoma City, Oklahoma",
    "snapshot": [
        ("Market cap", "~$19.8 bn (231.5 mn sh × $85.52)"),
        ("Enterprise value", "~$24.1 bn"),
        ("Net debt (pro forma)", "~$4.3 bn"),
        ("52-week range", "$83.25 – $126.62"),
        ("Production", "~7.5 Bcfe/d (92% natural gas)"),
        ("Proved reserves", "25.9 Tcfe"),
        ("Basins", "Haynesville; NE Appalachia; SW Appalachia"),
        ("Dividend", "$2.30/yr (~2.7% yield)"),
        ("Q2'26 adj. EBITDAX", "$1,183 mn (flat y/y despite lower gas)"),
        ("Implied upside", "+31% to $112.00 fair value"),
    ],
    "thesis": [
        "Expand Energy, formed from the merger of Chesapeake and Southwestern, is now the largest "
        "natural gas producer in the United States, with premier acreage in the Marcellus, Haynesville, "
        "and other basins. The investment case is straightforward: scale lowers per-unit costs, a "
        "low-decline inventory supports decades of drilling, and the company's capital discipline "
        "(maintenance-mode production, free cash flow returned to shareholders) converts a commodity "
        "business into a cash machine across the cycle.",
        "Our judgment is that the market still prices Expand like the old Chesapeake — a leveraged "
        "gas-price lottery ticket — when the merged company is a different animal: lower leverage, "
        "lower breakevens, and a management team whose stated strategy is returns over growth. The "
        "structural demand story for US natural gas — LNG exports, power-generation demand including "
        "data centers, and industrial reshoring — provides a durable bid under volumes that the spot "
        "price does not fully reflect.",
        "At $85.52, the stock is priced for bear-case gas, forever. The reverse DCF is blunt: at this "
        "price, enterprise value of ~$24.1 billion capitalized at the 10% base discount with 1.0% "
        "terminal growth implies roughly $2.1 billion of perpetual free cash flow — equivalent to a "
        "sustained ~$3.00 Henry Hub with zero terminal growth and no LNG or data-center uplift. Our "
        "probability-weighted fair value is $112.00, a 31% expected return, driven by free cash flow "
        "generation and the dividend-plus-buyback framework rather than a bet on a gas-price spike.",
        "The cost position is the core of the call. Expand's Marcellus and Haynesville acreage sits at "
        "the low end of the North American cost curve, which means the company generates free cash flow "
        "at gas prices where higher-cost producers merely survive. In a commodity business, being the "
        "low-cost producer is the entire strategy; everything else — hedging, marketing, capital "
        "returns — is execution against that advantage.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("LNG is the structural demand story the spot market underappreciates. ",
         "US LNG export capacity is growing substantially through the end of the decade, and each new "
         "train is a durable source of demand for Gulf Coast and Appalachian gas. Expand's Haynesville "
         "position is advantaged for Gulf Coast LNG, and its scale gives it marketing optionality — "
         "including exposure to international price linkages — that smaller producers cannot access."),
        ("The bear case is already in the price. ",
         "Our bear DCF ($31.53) is 63% below the price — a genuinely adverse decade of $2.90 gas — and "
         "the market price embeds roughly that outcome as the expectation. Any move toward the futures "
         "strip re-rates the equity; the asymmetry favors holders."),
        ("An underappreciated second product: gas marketing. ",
         "The $1.25 billion Twin Eagle acquisition added ~1,000 commercial customers and 44 Bcf of "
         "storage; management raised its marketing free-cash-flow target to $750 million per year. The "
         "strategy is evolving from pure producer to integrated gas marketer — capturing volatility and "
         "basis spreads that pure producers leave on the table."),
    ],
    "business": [
        "Expand Energy was created in October 2024 when Chesapeake Energy acquired Southwestern Energy "
        "for ~$7.4 billion, then rebranded — making it the largest independent US natural gas producer "
        "at roughly 7.5 Bcfe/d, 92% natural gas. The footprint spans three basins (proved reserves "
        "25.88 Tcfe): Haynesville (23% of reserves — the LNG-adjacent growth engine, with 75,000+ net "
        "Western Haynesville acres and 200+ potential locations); NE Appalachia (42% of reserves — the "
        "low-cost, basis-constrained base); SW Appalachia (35% of reserves, with an oil and NGL liquids "
        "kicker that lifts blended realizations).",
        "The strategy is maintenance production with capital discipline: drill enough to hold volumes "
        "roughly flat, keep costs among the lowest in the industry, and return the resulting free cash "
        "flow to shareholders through a base dividend plus variable buybacks. Hedging smooths near-term "
        "price exposure while deliberately leaving upside exposure — the correct posture for a low-cost "
        "producer. The merger synergies — operational (drilling and completion efficiencies, overhead "
        "reduction) and commercial (marketing scale, LNG optionality) — are the near-term earnings "
        "driver.",
        "The commercial structure includes a base dividend designed to be sustainable at low gas prices "
        "($2.30/year), supplemented by buybacks that flex with free cash flow. We expect the share "
        "count to shrink meaningfully over the forecast, so per-share free cash flow grows faster than "
        "the commodity.",
    ],
    "business_bullets": [
        ("Decades of low-decline inventory. ",
         "The Marcellus offers enormous, low-decline inventory near premium Northeast demand; the "
         "Haynesville offers high-rate wells with direct access to Gulf Coast LNG and industrial "
         "demand. Together they remove the treadmill dynamic that plagues shorter-lived shale plays."),
        ("Marketing and logistics as a growth vector. ",
         "Twin Eagle plus a 20-year, 1.15 Mtpa Delfin LNG supply agreement (targeted 2031): the "
         "company is building an integrated marketer, not just a producer."),
        ("Management credibility on discipline — recently earned. ",
         "The combined company has held the line on maintenance production rather than chasing "
         "growth, even when prices spiked. We treat past discipline as evidence, not promise; any "
         "deviation would be visible quickly in capex and production data."),
    ],
    "outlook": [
        "Where is this business going? We see Expand as the consolidator and low-cost anchor of US "
        "natural gas. The next three years should deliver the merger synergies in full, continued "
        "per-unit cost reduction from scale and longer laterals, and growing exposure to "
        "premium-priced demand: LNG export capacity additions and power demand growth both pull on "
        "exactly the basins Expand dominates.",
        "Data-center power demand is an emerging call option on gas volumes. US electricity demand "
        "growth, driven by AI data centers and industrial reshoring, disproportionately benefits natural "
        "gas as the marginal source of new dispatchable power. We expect behind-the-meter and utility "
        "contracts to become a visible part of the demand picture over the forecast.",
        "Consolidation optionality is the other long-term lever. As the largest gas producer, Expand is "
        "the natural consolidator of remaining high-quality gas assets; our base case assumes no major "
        "deals, but the balance sheet and equity currency give the company an acquisition option that "
        "smaller peers lack.",
        "On price decks: our base case uses a mid-cycle Henry Hub assumption consistent with the LNG "
        "and power-demand outlook ($3.10 rising toward $3.50), not a spike. The investment works at "
        "that deck because of the cost position and the capital-return framework — it does not require "
        "forecasting commodity prices correctly, only believing that structural demand supports "
        "mid-cycle pricing over time. Our bear case assumes gas stuck at ~$2.90 for the decade; a $0.50 "
        "move in the sustained Henry Hub assumption shifts fair value by roughly a sixth.",
    ],
    "financials": [
        "Q2 2026 (reported July 28, 2026): revenue $2.96 billion (−19.8% year over year on lower gas), "
        "adjusted EBITDAX $1.18 billion — flat year over year despite the price drop, which is the "
        "synergy story working — adjusted EPS $1.33 versus ~$1.35–1.41 consensus, operating cash flow "
        "$1.10 billion, capex ~$753 million, free cash flow ~$343 million. Production hit 7.48 Bcfe/d; "
        "realized gas was $2.42/Mcf. Q2 annualized FCF of ~$1.37 billion at ~$2.90 realized gas anchors "
        "the DCF's FCF path.",
        "The historical revenue series is merger-distorted (2024 reflects only the post-October combined "
        "company), so the trajectory chart below is best read from 2025 onward. Net debt of ~$4.3 "
        "billion pro forma is modest against ~$24 billion of enterprise value — the balance-sheet risk "
        "that defined the old Chesapeake is gone.",
    ],
    "fin_table": {
        "headers": ["$ bn", "2022*", "2023*", "2024*", "2025"],
        "rows": [
            ["Revenue", "11.44", "7.78", "4.22", "12.19"],
            ["Free cash flow", "2.30", "0.55", "0.01", "1.64"],
            ["Q2'26 annualized FCF", "—", "—", "—", "1.37"],
        ],
        "footnote": "*Pre-merger (Chesapeake standalone); merger with Southwestern closed Oct 2024. Sources: company filings via Yahoo Finance; Q2'26 company release.",
    },
    "moat": [
        ("Lowest-quartile cost position. ",
         "Marcellus and Haynesville acreage at the low end of the North American cost curve — free "
         "cash flow at gas prices where higher-cost producers merely survive."),
        ("Scale as the consolidator. ",
         "The largest US gas producer has the lowest per-unit overhead, the strongest marketing "
         "optionality, and the acquisition currency smaller peers lack."),
        ("Decades of inventory. ",
         "25.9 Tcfe of proved reserves removes the treadmill dynamic of shorter-lived shale plays."),
        ("The marketer's edge. ",
         "Storage, commercial customers, and LNG linkages capture volatility and basis spreads that "
         "pure producers leave on the table."),
    ],
    "valuation_method": "10-year scenario FCF DCF (gas-deck driven)",
    "valuation_intro": [
        "We value Expand on a 10-year scenario free-cash-flow DCF — weights bear 25% / base 50% / bull "
        "25% — with scenario-specific discounts: bear 12.5% (base + 250bp), base 10.0% (standard tier: "
        "cyclical commodity E&P with 92% gas exposure), bull 8.5% (base − 150bp). Terminal growth is "
        "0.0% / 1.0% / 1.5% — capped well under 2.5% because shale wells decline and reserves deplete; "
        "no perpetual growth is assumed for a depleting resource.",
        "Inputs are independently justified: the FCF path is anchored to Q2'26 annualized FCF ($1.37 "
        "billion at ~$2.90 realized gas), the company's own $/Mcf sensitivity (+$0.50/Mcfe ≈ +$1.37 "
        "billion revenue), the 2027 futures strip (~$3.27 rising toward ~$3.87), and mid-cycle "
        "normalization — never strip peaks. Year-10 FCF is set at mid-cycle margins, not the bull-case "
        "peak. No terminal-value haircut is needed: TV is 31–50% of EV across scenarios, well under the "
        "70% guardrail.",
        "Sensitivity read: at $3.00 sustained Henry Hub the stock is roughly fairly valued-to-cheap near "
        "$63; every sustained $0.25 above that is worth ~$29/share. Our $112 target sits between the "
        "$3.25 and $3.50 columns — it requires gas to normalize toward mid-cycle, not to boom.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 31.53,
            "assumptions": "Gas stuck ~$2.90 flat for the decade; 2036 FCF $1.45B (flat, CAGR 0%); synergy shortfalls; dividend at risk",
            "rev_cagr": "0%*", "margin_end": "FCF $1.45B",
            "discount": 0.125, "terminal_g": 0.00, "tv_share": 0.31,
            "pv_explicit": bear_e, "pv_terminal": bear_t, "cashflow_unit": "$/sh",
        },
        "base": {
            "fair_value": 111.16,
            "assumptions": "Strip → mid-cycle $3.50; full synergy realization; maintenance production; dividend + buyback framework; 2036 FCF $2.90B",
            "rev_cagr": "+7.8%*", "margin_end": "FCF $2.90B",
            "discount": 0.10, "terminal_g": 0.01, "tv_share": 0.42,
            "pv_explicit": base_e, "pv_terminal": base_t, "cashflow_unit": "$/sh",
        },
        "bull": {
            "fair_value": 195.75,
            "assumptions": "LNG boom: $3.50 → $4.25; faster synergy capture; marketing upside; 2036 FCF $3.90B",
            "rev_cagr": "+11.0%*", "margin_end": "FCF $3.90B",
            "discount": 0.085, "terminal_g": 0.015, "tv_share": 0.50,
            "pv_explicit": bull_e, "pv_terminal": bull_t, "cashflow_unit": "$/sh",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": (
        "*For EXE the 'Rev CAGR' column shows the FCF CAGR implied by each scenario's 2036 FCF versus "
        "Q2'26 annualized FCF ($1.37B); 'End margin' shows the scenario's 2036 FCF. The valuation is "
        "driven by the Henry Hub deck, not a revenue forecast."
    ),
    "risks": [
        ("Commodity leverage — the big one. ",
         "92% gas exposure means a sustained $0.50/Mcf move swings ~$1 billion of annual EBITDA on a "
         "~$20 billion market cap. Our bear DCF ($31.53) is 63% below the price."),
        ("Basis differentials. ",
         "NE Appalachia realized just $2.15/Mcf in Q2; Marcellus differentials can persist even if "
         "Henry Hub recovers."),
        ("Hedge drag. ",
         "Floors protect 2026, but collars cap upside if gas spikes; 2027 coverage is undisclosed."),
        ("Execution. ",
         "Interim CEO since early 2026; Twin Eagle integration and synergy targets are new."),
        ("Takeaway constraints. ",
         "Pipeline capacity limits in Appalachia can strand gas and depress regional realizations."),
        ("Capital allocation. ",
         "Any return to growth-mode drilling at the expense of returns would break the thesis."),
    ],
    "falsification": (
        "Downgrade to HOLD if the 2027 futures strip collapses back toward $2.90 and stays there — in "
        "which case this note's bear case ($31.53) becomes the base case — or if sustained Marcellus "
        "basis blowouts keep realized prices $0.75+ below Henry Hub regardless of the strip. A strategic "
        "pivot back to production growth at the expense of free cash flow, or leverage rising materially "
        "above the stated target range, would each independently force a re-underwrite. We watch: the "
        "futures strip, basis differentials, the 2027 hedge book, and synergy delivery."
    ),
    "charts": {
        "scenario": {"bear": 31.53, "base": 111.16, "bull": 195.75,
                     "weighted": 112.00, "price": 85.52},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [11.443, 7.775, 4.221, 12.189],
            "fcf_hist": [2.302, 0.551, 0.008, 1.644],
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": [None]*11,
            "fcf_proj": [1.37, 1.52, 1.68, 1.84, 2.0, 2.16, 2.32, 2.48, 2.63, 2.77, 2.90],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via Yahoo Finance (pre-merger years are Chesapeake "
                    "standalone; merger closed Oct 2024 — read from 2025). Projection: interpolated "
                    "base-case FCF path between Q2'26 annualized FCF ($1.37B) and the model's 2036 "
                    "FCF ($2.90B); the actual path follows the gas deck year by year.",
        },
        "composition": {
            "bear": {"pv_explicit": bear_e, "pv_terminal": bear_t},
            "base": {"pv_explicit": base_e, "pv_terminal": base_t},
            "bull": {"pv_explicit": bull_e, "pv_terminal": bull_t},
            "unit": "$/sh",
        },
        "extra": {
            "type": "line",
            "title": "Henry Hub price deck by scenario ($/MMBtu)",
            "years": [2026, 2027, 2028, 2029, 2030],
            "series": [
                {"label": "Bear (~$2.90 flat)", "values": [3.0, 3.0, 3.1, 3.2, 3.2]},
                {"label": "Base ($3.10 → $3.50)", "values": [3.1, 3.27, 3.6, 3.5, 3.5]},
                {"label": "Bull ($3.50 → $4.25)", "values": [3.3, 3.5, 3.87, 4.1, 4.25]},
            ],
            "ylabel": "$/MMBtu",
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "EXE-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
