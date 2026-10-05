"""Polished note: Amazon (AMZN) — REDUCE, fair value $173.00.

Valuation: 10-year scenario DCF (bear $58.69 / base $171.68 / bull $290.42,
weighted $173.12 -> $173 target) from the current valuation model:
discounts 11.5%/9%/8%; terminal growth 1.5%/1.8%/0.5% (haircut where disclosed);
revenue CAGRs 8%/10%/13%; exit operating margins 13.5%/16.5%/18.5%.
Composition uses the model's explicit-period PVs and terminal-value shares of EV.
History: company filings via Yahoo Finance (Oct 2026). Trajectory projection:
base-case path at the scenario's 10% revenue CAGR with FCF margins gliding to
the model's year-10 level. All prose is fresh October 4, 2026 analysis.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note, validate

data = {
    "ticker": "AMZN",
    "company": "Amazon.com, Inc.",
    "exchange": "NASDAQ",
    "sector": "Consumer Discretionary — Internet Retail / Cloud",
    "verdict": "REDUCE",
    "fair_value": 173.00,
    "price": 251.52,
    "risk": "Medium",
    "headline": "Two of the best businesses of the last thirty years — at a price that needs all three engines firing at once",
    "ceo": "Andy Jassy",
    "hq": "Seattle, Washington",
    "snapshot": [
        ("Market cap", "~$2.71 tn (10.9 bn sh × $251.52)"),
        ("52-week range", "~$196 – $287"),
        ("Price / fair value", "$251.52 / $173.00"),
        ("Implied downside", "−31%"),
        ("2025 revenue", "$716.9 bn"),
        ("Segment revenue mix (2026E)", "AWS ~$151 bn; advertising ~$76 bn; N. America ~$405 bn; Intl ~$144 bn"),
        ("Net debt / strategic stakes", "~$35 bn / ~$100 bn"),
        ("2025 operating cash flow / capex", "$139.5 bn / $131.8 bn"),
        ("AI capex cycle", "Record data-center, Trainium, and power-procurement spend"),
        ("Next catalyst", "AWS growth reacceleration prints; Q4 holiday retail; Kuiper milestones"),
    ],
    "thesis": [
        "Amazon owns two of the best businesses built in the last thirty years: AWS, the "
        "dominant cloud infrastructure franchise, and a retail operation whose logistics "
        "network constitutes a nearly unassailable moat. Advertising, the third leg, is a "
        "high-margin compounder growing from the traffic the other two create. We have no "
        "quarrel with the quality of these assets. Our quarrel is with the price: at "
        "$251.52, the market is paying for AWS reacceleration, retail margin expansion, and "
        "advertising scale all arriving together, on schedule, without friction.",
        "AWS is the crux. Cloud growth has settled into the high teens, and the incremental "
        "revenue dollar is more contested than ever: Microsoft and Google compete aggressively "
        "on price and bundle AI tooling, while the largest customers are designing their own "
        "silicon and negotiating ever-larger discounts. AWS remains the leader, but leadership "
        "in a maturing market earns a maturing multiple, and the current price assumes the "
        "hypergrowth era resumes.",
        "Retail, for all its scale, remains a structurally low-margin business. Automation "
        "and advertising attach have lifted North American margins, but the international "
        "segment still earns little, and the next leg of efficiency requires capital spending "
        "that depresses free cash flow today for uncertain returns tomorrow. Project Kuiper "
        "— the satellite broadband constellation — is a genuine capital sink with a "
        "decade-long payback, and it sits inside the valuation at full optimism.",
        "The arithmetic of the current price is worth stating plainly. Amazon's market "
        "capitalization near $2.7 trillion prices the company at a multiple of free cash flow "
        "that only makes sense if AWS margins never compress, retail earns software-like "
        "returns, and advertising growth never decelerates. Each of those assumptions is "
        "individually optimistic; jointly, they leave no margin for the ordinary "
        "disappointments — a delayed enterprise migration cycle, a cloud price war, a "
        "consumer slowdown — that periodically visit even the best businesses. Our "
        "probability-weighted fair value is $173.00, 31% below the current price. We rate "
        "the shares REDUCE rather than SELL because the underlying franchises are exceptional "
        "and deserve some representation — but at this price the expected return is "
        "negative, and capital has better risk-adjusted homes.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("AWS is priced for reacceleration that the competitive facts do not support. ",
         "High-teens cloud growth with Azure and GCP discounting aggressively, customers "
         "building their own silicon, and AI workloads commoditizing inference over time — "
         "the price assumes the hypergrowth era resumes; our base case assumes mid-teens "
         "growth with gradual margin normalization."),
        ("The AI capex wave is being capitalized as if returns were assured. ",
         "Record data-center, Trainium, and power-procurement spending will run for years "
         "before the aggregate return is known. Our bear case — AI digestion, AWS share "
         "loss, capex staying elevated — is worth $58.69, and it sits far below the price, "
         "as required."),
        ("Advertising is the swing factor, and it is the most cyclical leg. ",
         "The highest-margin growth engine is also the first budget cut in a downturn, and "
         "its growth must eventually converge toward e-commerce growth as penetration "
         "saturates. Our base case assumes a graceful deceleration; the market assumes none."),
    ],
    "business": [
        "Amazon operates three segments. North America and International retail comprise "
        "the e-commerce marketplace, first-party sales, Prime subscriptions, and the "
        "physical store footprint led by Whole Foods. AWS provides compute, storage, "
        "databases, and AI services to enterprises and startups globally. Advertising — "
        "reported within the retail segments — sells sponsored placements to merchants and "
        "brands, and has become one of the highest-margin revenue streams in the company.",
        "The flywheel is well understood: Prime membership drives retail frequency, retail "
        "traffic feeds the advertising business, and AWS funds the capital intensity of the "
        "whole enterprise. Few companies in history have combined this scale with this many "
        "simultaneous reinvestment opportunities — which is also why the capital allocation "
        "question (how much of the AI buildout earns its cost of capital) matters more here "
        "than at almost any other company.",
    ],
    "business_bullets": [
        ("AWS: the profit engine under siege. ",
         "Roughly $151 billion of high-margin revenue growing in the high teens — still the "
         "leader, but the incremental dollar is contested by Azure and GCP on price and "
         "bundled AI tooling, and the largest customers are designing their own silicon."),
        ("Advertising: the highest-margin compounder. ",
         "Roughly $76 billion of revenue growing at a premium to retail, with minimal "
         "incremental cost per dollar — and the most cyclically exposed leg of the "
         "business, since brand budgets are cut early in downturns."),
        ("Retail: scale moat, thin margins. ",
         "The North America logistics network is nearly unassailable; international still "
         "earns little. The next leg of efficiency requires capex that depresses free cash "
         "flow today for uncertain returns tomorrow."),
        ("Kuiper: the capital sink inside the valuation. ",
         "The satellite broadband constellation will consume billions before generating "
         "meaningful revenue, on a decade-long payback — carried at full optimism in the "
         "current price."),
    ],
    "outlook": [
        "Advertising deserves emphasis as the swing factor in our valuation. It is Amazon's "
        "highest-margin growth engine and the least appreciated source of operating "
        "leverage: every incremental ad dollar carries minimal cost. We model it compounding "
        "at a premium to retail for the full horizon. But advertising is also the most "
        "cyclically exposed leg — brand budgets are cut early in downturns — and its growth "
        "rate must eventually converge toward e-commerce growth as penetration saturates. "
        "Our base case assumes a graceful deceleration; the market assumes none.",
        "Our judgment is that the next three years are heavy-investment years with uncertain "
        "payoff timing. AI-related capital expenditure — data centers, custom Trainium "
        "chips, power procurement — will run at record levels, and while some of this "
        "spending clearly earns high returns, the aggregate return on the AI capex wave "
        "will not be known until the capacity is absorbed. Markets are currently "
        "capitalizing the spending as if the returns are assured.",
        "In retail, we expect steady but unspectacular progress: low-single-digit unit "
        "growth, continued automation gains, and advertising growth gradually decelerating "
        "as the base compounds. Kuiper will consume billions before generating meaningful "
        "revenue, and regulatory scrutiny of marketplace practices remains a live overhang "
        "in both the US and Europe. The business will be larger and more profitable in five "
        "years — our dispute is with the multiple the market applies to that future today. "
        "Longer term, the question is whether AWS can defend its margins as AI workloads "
        "commoditize inference. History suggests infrastructure margins compress as "
        "technology standardizes; AWS's scale and enterprise entrenchment argue for a "
        "slower fade than skeptics expect. Either way, the current price leaves no room "
        "for the fade at all.",
    ],
    "financials": [
        "Revenue grew from $514 billion in 2022 to $717 billion in 2025, but free cash flow "
        "has not followed: operating cash flow of $139.5 billion in 2025 was nearly consumed "
        "by $131.8 billion of capex, leaving just $7.7 billion of free cash flow. That is "
        "the AI buildout in one line — the company is reinvesting essentially all of its "
        "operating cash generation into data centers, custom silicon, and logistics. The "
        "bull case says this capex earns high returns; our model haircuts terminal growth "
        "where the buildout looks most aggressive and refuses to assume the returns.",
        "The scenario economics: our bear case ($58.69) assumes AI capex digestion, AWS "
        "ceding share with sustained price competition, retail margins compressing as wage "
        "and logistics costs outrun automation gains, and Kuiper becoming a multi-year drag "
        "on free cash flow — an 8% revenue CAGR to $1.76 trillion in 2036 with exit operating "
        "margins of 13.5% at an 11.5% discount rate. The base case ($171.68) assumes the AI "
        "buildout sustains on a fade curve, AWS holding ~26–28% share, capex normalizing — "
        "10% CAGR to $2.11 trillion, 16.5% exit margins, 9% discount. The bull ($290.42) "
        "assumes an AI workload supercycle reaccelerating AWS into the mid-20s and "
        "advertising becoming a $200 billion-plus engine — 13% CAGR, 18.5% exit margins, 8% "
        "discount. Terminal growth of 1.5–1.8% (0.5% in the bull, haircut) is applied to "
        "mid-cycle, not peak, cash flows.",
    ],
    "fin_table": {
        "headers": ["$bn", "2022", "2023", "2024", "2025"],
        "rows": [
            ["Revenue", "514.0", "574.8", "638.0", "716.9"],
            ["YoY growth", "—", "+11.8%", "+11.0%", "+12.4%"],
            ["Operating cash flow", "46.8", "85.0", "115.9", "139.5"],
            ["Capital expenditures", "63.7", "52.7", "83.0", "131.8"],
            ["Free cash flow (OCF − capex)", "-16.9", "32.2", "32.9", "7.7"],
            ["Net debt / strategic stakes", "—", "—", "—", "~35 / ~100"],
        ],
        "footnote": "Company filings via Yahoo Finance. 2025 capex of $131.8 bn — the AI "
                    "buildout — consumed nearly all of operating cash flow.",
    },
    "moat": [
        ("AWS: scale and entrenchment, but a maturing multiple. ",
         "The largest cloud infrastructure base with deep enterprise entrenchment — but "
         "leadership in a maturing market earns a maturing multiple, and the largest "
         "customers are actively designing around AWS with their own silicon."),
        ("The logistics network is nearly unassailable. ",
         "Nobody can replicate the North America fulfillment footprint at comparable "
         "unit economics. It is a genuine moat — over a structurally low-margin business."),
        ("Advertising compounds off captive traffic. ",
         "Sponsored placements monetize purchase intent Amazon already owns; minimal "
         "incremental cost per ad dollar. The moat is distribution, and it is widening — "
         "until penetration saturates and growth converges to e-commerce."),
        ("Custom silicon as a cost moat — if it works. ",
         "Trainium and in-house chips could structurally lower AI capex intensity. If they "
         "underdeliver against entrenched merchant-chip ecosystems, the AI capex is "
         "stranded at full cost."),
    ],
    "valuation_method": "10-year scenario DCF",
    "valuation_intro": [
        "We value Amazon on a 10-year scenario DCF, weighted 25% / 50% / 25%. Discount "
        "rates are scenario-specific: base 9%, bear 11.5% (base + 250bp), bull 8% (base − "
        "150bp, at the 8% floor). Terminal growth is 1.8% in the base case and 1.5% in the "
        "bear case, haircut to 0.5% in the bull case where the AI supercycle assumptions "
        "are most aggressive — applied to mid-cycle, not peak, cash flows. Revenue CAGRs "
        "are 8% / 10% / 13% across bear / base / bull, with exit operating margins of "
        "13.5% / 16.5% / 18.5%.",
        "The scenario fair values are $58.69 (bear) / $171.68 (base) / $290.42 (bull), "
        "weighting to $173.12 — our $173.00 target, 31% below the $251.52 close. The bear "
        "case sits far below the current price, reflecting how much of the valuation rests "
        "on everything going right simultaneously across three distinct businesses. "
        "Terminal value is 64–70% of enterprise value across scenarios — at the top of the "
        "range, reflecting a mega-cap compounder valuation, disclosed here.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 58.69,
            "assumptions": ("AI digestion; AWS cedes share with sustained price "
                            "competition; capex stays elevated; retail margins compress; "
                            "Kuiper a multi-year drag on free cash flow."),
            "rev_cagr": "+8.0%", "margin_end": "13.5%",
            "discount": 0.115, "terminal_g": 0.015, "tv_share": 0.638,
            "pv_explicit": 208.0, "pv_terminal": 366.7, "cashflow_unit": "$bn",
        },
        "base": {
            "fair_value": 171.68,
            "assumptions": ("AI buildout sustains on a fade curve; AWS holds ~26–28% "
                            "share; capex normalizes; advertising compounds at a premium "
                            "to retail with graceful deceleration."),
            "rev_cagr": "+10.0%", "margin_end": "16.5%",
            "discount": 0.09, "terminal_g": 0.018, "tv_share": 0.699,
            "pv_explicit": 543.8, "pv_terminal": 1262.6, "cashflow_unit": "$bn",
        },
        "bull": {
            "fair_value": 290.42,
            "assumptions": ("AI workload supercycle reaccelerates AWS into the mid-20s; "
                            "retail operating margins reach double digits; custom silicon "
                            "cuts capex intensity; advertising becomes a $200B+ engine."),
            "rev_cagr": "+13.0%", "margin_end": "18.5%",
            "discount": 0.08, "terminal_g": 0.005, "tv_share": 0.698,
            "pv_explicit": 936.9, "pv_terminal": 2164.2, "cashflow_unit": "$bn",
        },
    },
    "scenario_note": "Terminal growth is haircut in the bull case (0.5%) where the AI "
                     "supercycle assumptions are most aggressive. Composition uses the "
                     "model's explicit-period PVs and terminal-value shares of EV.",
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "risks": [
        ("AWS deceleration. ",
         "A sharper-than-expected slowdown in cloud growth would remove the primary "
         "engine of profit expansion."),
        ("AI capex returns. ",
         "Record data-center spending may earn sub-par returns if capacity outruns demand."),
        ("Retail margin pressure. ",
         "Wage inflation, fuel costs, and competitive discounting against automation gains."),
        ("Kuiper capital intensity. ",
         "Billions consumed before meaningful revenue, on a decade-long payback with "
         "uncertain commercial returns."),
        ("Antitrust and regulatory action. ",
         "US and EU scrutiny of marketplace and cloud practices remains a live overhang."),
        ("Advertising cyclicality. ",
         "Brand budgets are cut early in downturns — the highest-margin leg is the most "
         "cyclical."),
        ("Prime saturation. ",
         "Membership saturation in developed markets limits the frequency flywheel."),
        ("Custom-silicon execution. ",
         "Trainium underdelivering against entrenched merchant-chip ecosystems would "
         "strand AI capex at full cost."),
    ],
    "falsification": (
        "AWS reaccelerating above 20% growth for four consecutive quarters with stable "
        "margins would force us to revisit the maturing-cloud thesis — the single most "
        "important falsifier. Retail operating margins sustainably above 8% in North "
        "America would prove structural leverage we do not currently grant. Kuiper "
        "reaching cash-flow breakeven ahead of plan would remove the capital-sink "
        "overhang. Advertising sustaining 20%+ growth for two consecutive years while AWS "
        "margins expand would be evidence of operating leverage the market is right to pay "
        "for. And a 20%+ decline in the share price with no deterioration in AWS or "
        "advertising fundamentals would mechanically repair the expected return. We watch: "
        "AWS growth and margin prints, capex intensity versus operating cash flow, "
        "advertising growth versus e-commerce growth, and Kuiper's cash burn."
    ),
    "methodology": [
        "We value Amazon on a 10-year scenario discounted-cash-flow framework, "
        "probability-weighted 25% / 50% / 25%. The base discount rate is 9%, reflecting a "
        "dominant mega-cap franchise with real cyclicality in two of its three engines; "
        "the bear case adds 250 basis points (11.5%) and the bull case subtracts 150 basis "
        "points (8%, at the floor). Terminal growth is capped at 2.5% and haircut where the "
        "scenario's assumptions are most aggressive (0.5% in the bull case), applied to "
        "mid-cycle — never peak — cash flows.",
        "Management guidance and segment narratives are never accepted at face value: AWS "
        "share, retail margin, and advertising trajectories are independently set per "
        "scenario, and Kuiper is carried as a multi-year drag in the bear case rather than "
        "wished away. The bear case is required to be genuinely adverse and to sit below "
        "the current price — at $58.69, it does. Terminal-value shares of enterprise value "
        "are disclosed for every scenario.",
        "We cross-check the DCF against sum-of-the-parts (AWS, advertising, retail "
        "segments), trading multiples, and reverse-DCF implied growth. The published "
        "target is the probability-weighted fair value, stated as a 12-month horizon "
        "reference. Risk ratings (Low / Medium / Medium-High / High) combine business "
        "volatility, balance-sheet strength, and valuation; Medium here reflects "
        "exceptional franchises priced for simultaneous perfection.",
    ],
    "charts": {
        "scenario": {"bear": 58.69, "base": 171.68, "bull": 290.42,
                     "weighted": 173.00, "price": 251.52},
        "trajectory": {
            # history: filings via Yahoo Finance (OCF - capex)
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [513.98, 574.78, 637.96, 716.92],
            "fcf_hist": [-16.90, 32.22, 32.88, 7.69],
            # base-case projection: 10% revenue CAGR; FCF margin gliding 4% -> 10%
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": [789.0, 868.0, 955.0, 1050.0, 1155.0, 1271.0, 1398.0, 1538.0, 1691.0, 1861.0, 2047.0],
            "fcf_proj": [31.6, 39.9, 49.7, 60.9, 73.9, 89.0, 106.2, 126.1, 148.8, 174.9, 204.7],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via Yahoo Finance (FCF = operating cash flow "
                    "less capex; 2025 FCF collapsed to $7.7B on $131.8B of AI capex). "
                    "Projection: base-case path — revenue at the scenario's 10% CAGR from "
                    "2026E ~$789B; FCF margins gliding 4% to 10% (year-10 FCF ~$205B vs. "
                    "the model's $211B mid-cycle figure).",
        },
        "composition": {
            "bear": {"pv_explicit": 208.0, "pv_terminal": 366.7},
            "base": {"pv_explicit": 543.8, "pv_terminal": 1262.6},
            "bull": {"pv_explicit": 936.9, "pv_terminal": 2164.2},
            "unit": "$bn",
        },
        "extra": {
            "type": "pie",
            "title": "Revenue mix by segment, 2026E (~$776 bn)",
            "labels": ["N. America ex-ads", "AWS", "International ex-ads", "Advertising"],
            "values": [405.0, 151.0, 144.0, 76.0],
        },
    },
}

validate(data)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "AMZN-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
