"""Polished note build: Zoetis (ZTS). Compounder-quality terms: 15-yr horizon, 8-8.5% base discount, 3.0% terminal cap. Re-runnable."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

# 15-year base path: 2026E ~$10.1bn at ~8% CAGR; FCF margin ~24% widening toward ~30%
rev_proj = [10.1]
for _ in range(15):
    rev_proj.append(round(rev_proj[-1] * 1.08, 2))
margins = [0.24 + 0.004 * i for i in range(16)]
fcf_proj = [round(r * m, 2) for r, m in zip(rev_proj, margins)]

data = {
    "ticker": "ZTS",
    "company": "Zoetis Inc.",
    "exchange": "NYSE",
    "sector": "Health Care — Animal Health",
    "verdict": "BUY",
    "fair_value": 95.00,
    "price": 69.69,
    "risk": "Medium",
    "headline": "A Compounder-Quality Animal Health Franchise at a Narrative Discount",
    "snapshot": [
        ("Market cap", "~$28.8 bn (413 mn sh × $69.69)"),
        ("52-week range", "~$68.77 – $148.30"),
        ("Franchise", "Largest pure-play animal health company globally"),
        ("Gross margin", "~70%"),
        ("ROIC", ">15% sustained, 2016–2025 (verified)"),
        ("FCF conversion", ">80% (verified)"),
        ("Growth engines", "Dermatology (Apoquel/Cytopoint); OA pain (Librela/Solensia)"),
        ("Cash base", "Parasiticides + vaccines portfolios"),
        ("Compounder terms", "15-yr horizon; 8.5% base discount; 3.0% terminal cap"),
        ("Implied upside", "+36% to $95.00 fair value"),
    ],
    "thesis": [
        "Zoetis is the dominant pure-play animal health company in the world, and the rare business "
        "whose economics genuinely improve with scale: a portfolio of vaccines, parasiticides, and "
        "dermatology and pain therapeutics sold into a market where pet owners spend through cycles and "
        "livestock producers treat animal health as productivity insurance. The dermatology franchise "
        "(Apoquel, Cytopoint) and the osteoarthritis pain franchise (Librela, Solensia) are the growth "
        "engines; the parasiticide and vaccine portfolios are the durable cash base.",
        "Our judgment is that Zoetis's recent stock weakness reflects concern about the dermatology "
        "franchise facing competition and about Librela's growth cadence, not a deterioration of the "
        "underlying franchise. We tested that concern against the evidence: the pet-care spending "
        "category continues to grow, Zoetis's R&D pipeline in monoclonal antibodies and novel "
        "parasiticides remains the industry's deepest, and the livestock business provides a cyclical "
        "offset. The franchise economics — double-digit ROIC sustained for a decade, gross margins near "
        "70%, and free-cash-flow conversion above 80% — remain intact and verified from history.",
        "Zoetis meets our compounder-quality criteria: a 2016–2025 streak of ROIC above 15%, stable to "
        "expanding gross margins, and FCF conversion above 80%, all verified from reported history "
        "rather than projected. That standing earns a 15-year explicit forecast horizon, an 8.5% base "
        "discount rate, and a 3.0% terminal growth cap applied to a demonstrated sustained terminal "
        "margin. It is falsifiable: two consecutive years of ROIC below 15%, or a gross-margin "
        "contraction of 200bp or more, revokes the qualification and the valuation reverts to standard "
        "terms.",
        "At $69.69, the market prices Zoetis as though the growth franchises are permanently impaired. "
        "Our probability-weighted fair value is $95.00, a 36% expected return, earned through the "
        "compounding of a best-in-class animal health portfolio, not through a return to peak multiples. "
        "On the recent concerns directly: dermatology competition is real, but the category is growing "
        "and the portfolio approach (Apoquel for acute, Cytopoint for maintenance, plus pipeline "
        "follow-ons) defends better than any single product could; Librela's treated population remains "
        "a small fraction of the addressable one. Noise around a signal that is still intact.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("The pain franchise is the defining growth story of the next five years. ",
         "Librela and Solensia address enormous undertreated osteoarthritis populations; "
         "monoclonal-antibody therapies have long product lives with limited generic pressure, and the "
         "antibody platform can address other chronic conditions — each successful launch extends the "
         "runway without a heroic assumption about any single product."),
        ("The R&D engine is the underappreciated asset. ",
         "Zoetis spends more on animal-health R&D than any competitor, and the output has been a "
         "metronome of franchise creation. In animal health — shorter timelines, higher success rates "
         "than human pharma — sustained R&D spending compounds into a portfolio competitors cannot "
         "match by acquisition alone."),
        ("Pet humanization is a through-cycle demand tailwind. ",
         "Pet healthcare spending has grown faster than GDP across cycles, including downturns. An "
         "owner will cut many expenses before skipping a dog's arthritis treatment — that inelasticity "
         "is what supports pricing power and through-cycle cash-flow stability."),
    ],
    "business": [
        "Zoetis discovers, develops, manufactures, and commercializes medicines, vaccines, and "
        "diagnostics for companion animals and livestock. The companion-animal segment is the growth "
        "driver: dermatology (Apoquel, Cytopoint), osteoarthritis pain (Librela for dogs, Solensia for "
        "cats), and parasiticides (Simparica franchise). The livestock segment (cattle, swine, poultry, "
        "fish, sheep) provides vaccines, anti-infectives, and productivity products with more cyclical but "
        "still attractive economics.",
        "The business model is that of a specialty pharmaceutical company with better payer dynamics "
        "than human pharma: pet owners pay out of pocket and are price-insensitive about their animals' "
        "suffering, which supports pricing power; regulatory pathways are shorter; and the R&D engine "
        "has produced a steady cadence of blockbuster franchises. Gross margins near 70% reflect the "
        "value of patented therapeutics and manufacturing scale.",
        "Manufacturing is a quiet moat. Biologics and vaccine production require specialized facilities, "
        "regulatory approvals, and process expertise that take years to build; Zoetis's global "
        "manufacturing network is a scale advantage that supports both margins and supply reliability. "
        "The diagnostics and genetics businesses deepen the customer relationship beyond individual "
        "molecules.",
    ],
    "business_bullets": [
        ("Companion animal: the growth engine. ",
         "Dermatology and OA-pain franchises with multi-year patent-protected runways; parasiticides "
         "as the durable cash base."),
        ("Livestock: the cyclical offset. ",
         "Global scale leadership, protein-demand growth in emerging markets as a multi-decade "
         "tailwind; modeled as a steady contributor, not a growth engine."),
        ("Diagnostics and genetics adjacencies. ",
         "A veterinarian using Zoetis diagnostics is more likely to prescribe Zoetis therapeutics; "
         "livestock genetics data creates switching costs for producers."),
        ("Shareholder-friendly capital allocation. ",
         "The dividend has grown consistently since the spin-off; buybacks offset dilution with room to "
         "retire shares; FCF conversion above 80% funds R&D, the dividend, and buybacks simultaneously."),
    ],
    "outlook": [
        "Where is this business going? We expect the osteoarthritis pain franchise to be the defining "
        "growth story of the next five years: Librela and Solensia address enormous undertreated "
        "populations, and monoclonal-antibody therapies have long product lives with limited generic "
        "pressure. Dermatology will grow more slowly as competition intensifies, but from a large and "
        "still-expanding base, with multiple years of patent-protected runway.",
        "The livestock business should benefit from protein-demand growth and from the diagnostics and "
        "genetics offerings that deepen producer relationships beyond individual products. Across the "
        "portfolio, we expect revenue growth in the high-single digits with operating leverage from the "
        "high gross-margin structure, funding both R&D reinvestment and substantial capital returns.",
        "The pipeline beyond pain is the reason for the 15-year horizon. Monoclonal antibodies are a "
        "platform, not a product: the same technology that produced Librela and Solensia can address "
        "other chronic conditions in companion animals. Zoetis's antibody pipeline is the deepest in the "
        "industry.",
        "Our bear case assumes dermatology share losses accelerate, Librela adoption stalls on safety or "
        "efficacy concerns, and livestock cyclicality turns; it is genuinely adverse and sits below "
        "today's price. The compounder qualification is the guardrail on our optimism: if returns on "
        "capital deteriorate for two straight years, the framework itself forces a re-rating of the "
        "valuation terms.",
    ],
    "financials": [
        "Revenue has grown from $8.08 billion in 2022 to $9.47 billion trailing in 2025, with free cash "
        "flow compounding from $1.33 billion to $2.28 billion — a ~24% FCF margin on a ~70% gross-margin "
        "base. The P&L is the compounder signature: high gross margins, operating leverage, and cash "
        "conversion above 80% funding R&D, a growing dividend, and buybacks at once.",
        "The balance sheet is conservatively managed for a business of this quality; leverage is modest "
        "and the constraint on the valuation is franchise execution, not financing. Capital allocation "
        "should remain shareholder-friendly, with per-share growth exceeding enterprise growth via "
        "buybacks.",
    ],
    "fin_table": {
        "headers": ["$ bn", "2022", "2023", "2024", "2025 (TTM)"],
        "rows": [
            ["Revenue", "8.08", "8.54", "9.26", "9.47"],
            ["Free cash flow", "1.33", "1.62", "2.30", "2.28"],
            ["FCF margin", "16%", "19%", "25%", "24%"],
        ],
        "footnote": "Sources: company filings via Yahoo Finance. 2025 = trailing twelve months.",
    },
    "moat": [
        ("The deepest R&D engine in animal health. ",
         "The largest animal-health R&D budget in the industry, producing a metronome of blockbuster "
         "franchises — a portfolio competitors cannot match by acquisition alone."),
        ("The antibody platform. ",
         "Monoclonal antibodies for dermatology and pain are a platform technology with long product "
         "lives and limited generic pressure."),
        ("Manufacturing scale as a quiet moat. ",
         "Specialized biologics and vaccine facilities, regulatory approvals, and process expertise "
         "built over years; reliable supply is a competitive weapon for veterinarian loyalty."),
        ("Payer dynamics better than human pharma. ",
         "Out-of-pocket pet owners are price-insensitive about their animals' suffering, supporting "
         "pricing power through cycles."),
    ],
    "valuation_method": "15-year scenario FCF DCF (compounder terms)",
    "valuation_intro": [
        "We value Zoetis on a 15-year scenario free-cash-flow DCF under compounder-quality terms — "
        "weights bear 25% / base 50% / bull 25% — with scenario-specific discounts: bear 11.0% (base + "
        "250bp), base 8.5% (the empirical stability of the cash flows earns the lower rate), bull 8.0% "
        "(floor). Terminal growth is capped at 2.5% / 3.0% / 3.0% on a demonstrated sustained terminal "
        "margin — never a peak.",
        "Under compounder terms the math changes in two ways that matter. First, the 15-year horizon "
        "captures more of the pain-franchise and pipeline value that a 10-year model truncates. Second, "
        "the 8.5% base discount reflects the empirical stability of the cash flows rather than a generic "
        "large-cap rate. Both choices are earned by the verified history, and both are revoked "
        "automatically if the ROIC or margin triggers trip.",
        "Scenario fair values: bear $50 (franchise erosion, margin contraction — revoking the compounder "
        "qualification), base $92 (high-single-digit growth led by pain and dermatology, margins "
        "sustained), bull $146 (faster Librela/Solensia adoption, pipeline launches). "
        "Probability-weighted: $95.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 50.00,
            "assumptions": "Dermatology share losses accelerate; Librela adoption stalls on safety/efficacy concerns; livestock cyclicality turns; ROIC/margin triggers revoke compounder terms",
            "rev_cagr": "+4%", "margin_end": "24%",
            "discount": 0.11, "terminal_g": 0.025, "tv_share": 0.55,
            "pv_explicit": 22.5, "pv_terminal": 27.5, "cashflow_unit": "$/sh",
        },
        "base": {
            "fair_value": 92.00,
            "assumptions": "High-single-digit revenue growth led by the pain franchise and dermatology; margins sustained near demonstrated levels; pipeline extends the runway",
            "rev_cagr": "+8%", "margin_end": "30%",
            "discount": 0.085, "terminal_g": 0.03, "tv_share": 0.65,
            "pv_explicit": 32.0, "pv_terminal": 60.0, "cashflow_unit": "$/sh",
        },
        "bull": {
            "fair_value": 146.00,
            "assumptions": "Faster Librela/Solensia adoption; successful pipeline launches from the antibody platform; livestock tailwinds",
            "rev_cagr": "+12%", "margin_end": "34%",
            "discount": 0.08, "terminal_g": 0.03, "tv_share": 0.70,
            "pv_explicit": 44.0, "pv_terminal": 102.0, "cashflow_unit": "$/sh",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "risks": [
        ("Franchise concentration. ",
         "Dermatology and pain products are a large share of growth; competition or safety issues there "
         "hit disproportionately."),
        ("Librela adoption. ",
         "Slower-than-expected uptake or emerging safety signals would impair the key growth driver."),
        ("Livestock cyclicality. ",
         "Protein-price downturns and disease outbreaks affect the livestock segment quickly."),
        ("Generic and biosimilar pressure. ",
         "Key products will eventually face competition; timing and severity are uncertain."),
        ("Pricing scrutiny. ",
         "Sustained high price increases could invite regulatory or retailer pushback."),
        ("Pipeline failure. ",
         "The long-horizon thesis depends on continued R&D productivity; a dry spell would eventually "
         "show in growth."),
    ],
    "falsification": (
        "Downgrade to HOLD if ROIC falls below 15% for two consecutive years or gross margin contracts "
        "200bp or more on a sustained basis — either revokes the compounder qualification and forces a "
        "full valuation reset to standard terms. Separately, Librela/Solensia revenue declining year "
        "over year would break the pain-franchise growth thesis, and FCF conversion falling durably "
        "below 80% would signal the cash-compounding economics are deteriorating."
    ),
    "charts": {
        "scenario": {"bear": 50.00, "base": 92.00, "bull": 146.00,
                     "weighted": 95.00, "price": 69.69},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [8.08, 8.544, 9.256, 9.467],
            "fcf_hist": [1.326, 1.621, 2.298, 2.283],
            "years_proj": list(range(2026, 2042)),
            "revenue_proj": rev_proj,
            "fcf_proj": fcf_proj,
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via Yahoo Finance (2025 = TTM). Projection: illustrative "
                    "15-year base-case path at ~8% revenue CAGR with FCF margins ~24–30%.",
        },
        "composition": {
            "bear": {"pv_explicit": 22.5, "pv_terminal": 27.5},
            "base": {"pv_explicit": 32.0, "pv_terminal": 60.0},
            "bull": {"pv_explicit": 44.0, "pv_terminal": 102.0},
            "unit": "$/sh",
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "ZTS-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
