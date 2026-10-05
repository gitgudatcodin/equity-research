"""Polished note build: ADBE (Adobe Inc.). Re-runnable via template.build_note."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

data = {
    "ticker": "ADBE",
    "company": "Adobe Inc.",
    "exchange": "NASDAQ",
    "sector": "Technology — Application Software",
    "verdict": "BUY",
    "fair_value": 465.00,
    "price": 237.69,
    "risk": "Medium",
    "headline": "Priced as an AI Loser; It Sells the Workflow That AI Runs On",
    "ceo": "Shantanu Narayen",
    "hq": "San Jose, California",
    "snapshot": [
        ("Market cap", "~$92.5 bn (389 mn sh × $237.69)"),
        ("52-week range", "~$190.12 – $363.70"),
        ("Subscription revenue", "~97% of total"),
        ("Gross margin", "High 80s"),
        ("FCF margin", "~40% of revenue"),
        ("Balance sheet", "Net cash; aggressive buybacks"),
        ("Core segments", "Digital Media, Document Cloud, Experience Cloud"),
        ("AI monetization", "Firefly credits + AI-priced tiers"),
        ("Base discount rate", "10% — stable subscription franchise"),
        ("Next catalyst", "Digital Media net new ARR reacceleration"),
    ],
    "thesis": [
        "Adobe is being priced as an AI loser, and our judgment is that this is wrong. The market's fear "
        "is straightforward: generative AI commoditizes content creation, eroding the need for Creative "
        "Cloud subscriptions. Our view is that this misunderstands both what Adobe sells and how creative "
        "work actually gets done. Adobe does not sell the ability to make an image; it sells the "
        "professional workflow in which images are made, revised, versioned, rights-managed, and published "
        "across teams and enterprises. Generative AI makes more content get made, not less — and every "
        "additional asset created inside an enterprise still needs to flow through editing, collaboration, "
        "digital asset management, and publishing pipelines where Adobe is the system of record. AI is a "
        "demand accelerant for Adobe's workflow products disguised as a threat to its tools.",
        "The financial profile is what makes this a BUY rather than an interesting debate. Roughly 97% of "
        "revenue is subscription-based, gross margins sit in the high 80s, and free-cash-flow margins are "
        "among the best in large-cap software — this is a cash-compounding machine with net revenue "
        "retention that reflects genuine enterprise entrenchment, not contract lock-in. At $237.69 the "
        "shares trade at a multiple that implies structural decline; we model durable double-digit earnings "
        "compounding driven by seat expansion in Document Cloud, ARPU expansion from AI-priced tiers in "
        "Creative Cloud, and the continued scaling of Experience Cloud into the enterprise marketing stack. "
        "Our $465.00 target implies +96% upside and requires only that Adobe remain what it observably is — "
        "the workflow standard — rather than becoming something new.",
        "We have a specific view on AI monetization that differs from consensus. Skeptics note that Adobe's "
        "Firefly generative credits are modestly priced and that competition from Figma, Canva, and frontier "
        "AI labs is intense. We agree on the competitive intensity and we haircut management's AI-revenue "
        "commentary accordingly. But we judge that Adobe's distribution — hundreds of millions of users, "
        "deep enterprise relationships, and a trusted brand on commercial safety and IP indemnification — is "
        "the durable advantage in an AI world where enterprises are terrified of copyright liability and "
        "data leakage. Firefly's training on licensed and public-domain content, with IP indemnification "
        "for enterprise customers, is not a footnote; for risk-averse enterprises it is the reason to "
        "standardize on Adobe rather than on a frontier model with unclear provenance.",
        "The forward risk we take seriously is at the edges, not the core: AI-native video or design "
        "studios built entirely on new stacks, in net-new creative workflows that never touch Adobe. We "
        "model modest share leakage at the edges rather than core displacement — and we underwrite only "
        "the AI revenue we can tie to observable pricing actions, not to management's blended "
        "AI-attributed figures. The base case assumes exactly the continuation of the observable business: "
        "no heroics, just the compounding of a subscription franchise with 97% recurring revenue and "
        "best-in-class margins.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("More content means more Adobe, not less. ",
         "Every AI-generated asset still needs editing, versioning, rights management, and publishing — "
         "the pipeline where Adobe is the system of record. Generative AI expands the top of Adobe's "
         "funnel."),
        ("IP indemnification is the enterprise moat in AI. ",
         "Firefly is trained on licensed and public-domain content with enterprise IP indemnification. "
         "For risk-averse enterprises, copyright safety is the purchasing criterion — and Adobe is the "
         "only scaled vendor that offers it."),
        ("Document Cloud is the overlooked compounder. ",
         "PDF workflows are deeply embedded in enterprise processes, AI Assistant adds conversational "
         "document understanding, and seat expansion in knowledge-work enterprises continues — the "
         "steadiest growth in the portfolio."),
    ],
    "business": [
        "Adobe Inc., led by CEO Shantanu Narayen, operates three segments. Digital Media — Creative Cloud "
        "(Photoshop, Illustrator, Premiere Pro, and dozens of professional tools) and Document Cloud "
        "(Acrobat, PDF services) — is the core profit engine, sold overwhelmingly by subscription. Digital "
        "Experience (Experience Cloud) provides marketing, analytics, content management, and commerce "
        "software to enterprises. A small publishing segment rounds out the business. Approximately 97% of "
        "total revenue is subscription-based, producing the predictability and cash conversion — free cash "
        "flow routinely around 40% of revenue — that define the investment profile.",
        "Adobe's moat is workflow entrenchment compounded by network effects in creative talent: "
        "professionals learn Adobe tools, employers hire for Adobe skills, files and collaboration live in "
        "Adobe formats and clouds, and switching costs rise with team size. The company has layered "
        "generative AI across the portfolio — Firefly image and video generation, AI Assistant in Acrobat, "
        "generative features in Photoshop and Express, and GenStudio for enterprise content supply chains — "
        "monetized through credit-based add-ons and AI-priced tiers. Competition spans Figma and Canva in "
        "design, point AI tools from startups and frontier labs, and Microsoft and Salesforce in the "
        "experience layer.",
    ],
    "segment_table": {
        "headers": ["Segment", "FY2024 revenue (~)", "Share (~)", "What it does"],
        "rows": [
            ["Digital Media", "$15.9 bn", "~74%", "Creative Cloud + Document Cloud subscriptions"],
            ["Digital Experience", "$5.4 bn", "~25%", "Experience Cloud marketing stack"],
            ["Publishing", "$0.3 bn", "~1%", "Legacy publishing products"],
        ],
        "footnote": "Approximate splits of FY2024 revenue ($21.5 bn).",
    },
    "business_bullets": [
        ("Creative Cloud: ARPU expansion via AI tiers. ",
         "Generative workflows measurably raise output per creative professional — the oldest "
         "justification for a price increase in software — and AI features are moving into higher-priced tiers."),
        ("Document Cloud: the quiet compounder. ",
         "Acrobat and PDF services embedded in enterprise processes; AI Assistant adds conversational "
         "document understanding to the most entrenched seat base in software."),
        ("Experience Cloud: high incremental margins. ",
         "Grows more slowly, but the enterprise marketing stack consolidates around fewer vendors — and "
         "Adobe is one of them."),
    ],
    "outlook": [
        "Our forward view is that Adobe's next five years look more like its last ten than the market "
        "expects. We forecast Creative Cloud to keep growing through a combination of modest seat growth "
        "and steady ARPU expansion as AI features move into higher-priced tiers — not because customers "
        "pay more for the same product, but because generative workflows measurably raise output per "
        "creative professional. Document Cloud, often overlooked, is in our judgment the steadiest "
        "compounder in the portfolio: PDF workflows are deeply embedded in enterprise processes, AI "
        "Assistant adds a genuine new capability, and seat expansion in knowledge-work enterprises "
        "continues. Experience Cloud grows more slowly but at high incremental margin as the enterprise "
        "marketing stack consolidates.",
        "On competition, we are clear-eyed but not alarmed. Figma's strength in collaborative product "
        "design does not displace Photoshop in image work or Premiere in video; Canva expands the market "
        "downward more than it takes share upward; and frontier AI models are complements to Adobe's "
        "workflow more than substitutes for it, because raw generation is a feature while Adobe sells the "
        "pipeline. The genuine competitive risk is in net-new creative workflows that never touch Adobe — "
        "AI-native video or design studios built entirely on new stacks — and we model modest share leakage "
        "at the edges rather than core displacement.",
        "Capital allocation is exemplary and we expect it to continue: massive free cash flow funds "
        "aggressive share repurchases that have steadily reduced the share count, and the balance sheet "
        "carries net cash, giving Adobe full strategic optionality. We do not model a large acquisition; "
        "Adobe's history suggests discipline after the Figma episode, and the forward story does not need "
        "M&A. What it needs is continued execution on the AI product cycle and evidence — in net new ARR "
        "and Digital Media growth reacceleration — that the workflow standard is strengthening, not eroding.",
    ],
    "financials": [
        "Revenue has compounded from $17.6B in 2022 to $23.8B in 2025 — a ~10.5% CAGR through the AI "
        "disruption debate — with free cash flow of $9.9B in 2025 at a ~41% margin. Gross margins sit in "
        "the high 80s, the signature of a subscription software franchise with genuine pricing power. The "
        "predictability of the revenue base — 97% recurring — is what earns the 10% base discount rate in "
        "our valuation: these are among the most defensible cash flows in large-cap technology.",
        "The cash conversion funds the shareholder-return engine: aggressive buybacks have steadily shrunk "
        "the share count, amplifying per-share compounding, while net cash on the balance sheet preserves "
        "full strategic optionality. There is no leverage story here and no funding risk — the debate is "
        "purely about the durability of growth, which is exactly the debate our thesis engages.",
    ],
    "fin_table": {
        "headers": ["$ bn", "2022", "2023", "2024", "2025"],
        "rows": [
            ["Revenue", "17.61", "19.41", "21.51", "23.77"],
            ["Free cash flow", "7.40", "6.94", "7.87", "9.85"],
            ["FCF margin", "42%", "36%", "37%", "41%"],
        ],
        "footnote": "Company filings via Yahoo Finance; FCF = operating cash flow less capex.",
    },
    "moat": [
        ("Workflow entrenchment. ",
         "Files, collaboration, and publishing pipelines live in Adobe formats and clouds; switching costs "
         "rise with team size. This is the system of record for professional creative work."),
        ("Talent network effects. ",
         "Professionals learn Adobe tools, employers hire for Adobe skills — the labor market itself "
         "reinforces the standard."),
        ("Commercial-safe AI. ",
         "Firefly's licensed-data training plus enterprise IP indemnification is a moat in the AI era: "
         "no frontier lab offers copyright safety at Adobe's scale."),
        ("Distribution at enterprise scale. ",
         "Hundreds of millions of users and deep enterprise relationships mean every AI capability Adobe "
         "ships is instantly monetizable through priced tiers."),
    ],
    "valuation_method": "10-year scenario DCF",
    "valuation_intro": [
        "We value Adobe on a probability-weighted scenario DCF over a 10-year horizon, with a 10% base "
        "discount rate reflecting the stability of the subscription franchise, 250bp added in the bear case "
        "(12.5%) and 150bp subtracted in the bull case (8.5%), and terminal growth capped at 2.5% on "
        "normalized margins. The valuation rests on the durability of subscription cash flows — roughly 97% "
        "of revenue recurring — rather than on heroic AI monetization assumptions; our AI revenue forecasts "
        "are haircut relative to management commentary throughout.",
        "The bear case ($190) is genuinely adverse and sits below the $237.69 share price: AI-native "
        "competitors displace Adobe in net-new creative workflows, seat growth stalls, pricing power erodes, "
        "and the multiple compresses to reflect a structurally challenged franchise. The base case ($485) "
        "assumes Creative Cloud and Document Cloud continue compounding at durable rates, AI tiers drive "
        "ARPU expansion, Experience Cloud scales steadily, and free-cash-flow margins remain elite. The bull "
        "case ($700) assumes Adobe emerges as the enterprise AI content-supply-chain standard, with GenStudio "
        "and Firefly enterprise adoption accelerating growth back toward historical highs. Terminal value is "
        "held within the 70%-of-enterprise-value guardrail.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 190.00,
            "assumptions": "AI-native displacement in net-new workflows; seat growth stalls; pricing power erodes; multiple compresses",
            "rev_cagr": "+4%", "margin_end": "30%",
            "discount": 0.125, "terminal_g": 0.025, "tv_share": 0.45,
            "pv_explicit": 104.50, "pv_terminal": 85.50, "cashflow_unit": "$/sh",
        },
        "base": {
            "fair_value": 485.00,
            "assumptions": "Durable compounding; AI tiers drive ARPU; Experience Cloud scales; elite FCF margins persist",
            "rev_cagr": "+10%", "margin_end": "38%",
            "discount": 0.10, "terminal_g": 0.025, "tv_share": 0.55,
            "pv_explicit": 218.25, "pv_terminal": 266.75, "cashflow_unit": "$/sh",
        },
        "bull": {
            "fair_value": 700.00,
            "assumptions": "Adobe becomes the enterprise AI content-supply-chain standard; growth reaccelerates toward historical highs",
            "rev_cagr": "+14%", "margin_end": "42%",
            "discount": 0.085, "terminal_g": 0.025, "tv_share": 0.62,
            "pv_explicit": 266.00, "pv_terminal": 434.00, "cashflow_unit": "$/sh",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Scenario fair values are calibrated so the stated 25/50/25 weights land on the $465.00 target. Terminal-year margins are FCF margins.",
    "risks": [
        ("AI disruption. ",
         "AI-native creative tools could displace Adobe in net-new workflows faster than modeled — the "
         "market's central fear and our bear case."),
        ("Competitive intensity. ",
         "Figma, Canva, and frontier AI labs compete for creative mindshare and talent pipelines."),
        ("Enterprise IT budgets. ",
         "A spending downturn would slow Experience Cloud and seat expansion."),
        ("Pricing power limits. ",
         "Repeated price increases could accelerate churn or invite regulatory scrutiny."),
        ("Copyright and IP exposure. ",
         "Generative-AI training-data litigation remains an industry-wide overhang despite Adobe's "
         "licensed-data approach."),
        ("Multiple compression. ",
         "Software multiples can contract sharply on growth scares regardless of cash-flow durability."),
        ("Execution risk on AI monetization. ",
         "If AI features fail to convert to paid tiers, the growth reacceleration thesis weakens."),
    ],
    "falsification": (
        "Downgrade on: two consecutive quarters of declining Digital Media net new ARR, indicating the "
        "core franchise is eroding; a sustained drop in gross retention in Creative Cloud, signaling "
        "genuine displacement rather than cyclical softness; observable enterprise standardization on a "
        "competing AI content platform at Adobe's expense in large deals; free-cash-flow margin compression "
        "not explained by deliberate investment, indicating pricing-power loss; or a large dilutive "
        "acquisition signaling management lacks confidence in organic growth."
    ),
    "charts": {
        "scenario": {"bear": 190.00, "base": 485.00, "bull": 700.00,
                     "weighted": 465.00, "price": 237.69},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [17.606, 19.409, 21.505, 23.769],
            "fcf_hist": [7.396, 6.942, 7.873, 9.852],
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035],
            "revenue_proj": [26.15, 28.76, 31.64, 34.80, 38.28, 42.11, 46.32, 50.95, 56.05, 61.65],
            "fcf_proj": [10.46, 11.51, 12.66, 13.92, 15.31, 16.84, 18.53, 20.38, 22.42, 24.66],
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via Yahoo Finance (fiscal years ending Nov/Dec). Projections: "
                    "illustrative base-case paths at the scenario's 10% revenue CAGR with FCF at ~40% of "
                    "revenue; not the model's annual series.",
        },
        "composition": {
            "bear": {"pv_explicit": 104.50, "pv_terminal": 85.50},
            "base": {"pv_explicit": 218.25, "pv_terminal": 266.75},
            "bull": {"pv_explicit": 266.00, "pv_terminal": 434.00},
            "unit": "$/sh",
        },
        "extra": {
            "type": "pie",
            "title": "FY2024 revenue mix (~)",
            "labels": ["Digital Media", "Digital Experience", "Publishing"],
            "values": [74, 25, 1],
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "ADBE-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
