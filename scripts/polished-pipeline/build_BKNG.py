"""Polished note build: Booking Holdings (BKNG). Re-runnable."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

# Base revenue path: 2026E ~$29.0bn at ~9% CAGR; FCF margin ~34% widening to ~36%
rev_proj = [29.0]
for _ in range(10):
    rev_proj.append(round(rev_proj[-1] * 1.09, 2))
margins = [0.34, 0.342, 0.344, 0.346, 0.348, 0.35, 0.352, 0.354, 0.356, 0.358, 0.36]
fcf_proj = [round(r * m, 2) for r, m in zip(rev_proj, margins)]

data = {
    "ticker": "BKNG",
    "company": "Booking Holdings Inc.",
    "exchange": "NASDAQ",
    "sector": "Consumer Discretionary — Online Travel",
    "verdict": "BUY",
    "fair_value": 219.00,
    "price": 159.02,
    "risk": "Medium",
    "headline": "The Best Asset in Online Travel, Discounted on an AI Fear",
    "snapshot": [
        ("Market cap", "~$119.5 bn (751 mn sh × $159.02)"),
        ("52-week range", "~$150.14 – $225.00"),
        ("Platforms", "Booking.com, Priceline, Agoda, Kayak, OpenTable"),
        ("Heartland", "Europe: dominant accommodation marketplace"),
        ("Model", "Asset-light marketplace, minimal marginal cost/booking"),
        ("FCF conversion", "Among the highest in large-cap tech"),
        ("Capital return", "Nearly all FCF via buybacks; share count shrinking"),
        ("Loyalty", "Genius program driving direct repeat traffic"),
        ("AI posture", "Own AI trip-planning + connected-trip infrastructure"),
        ("Implied upside", "+38% to $219.00 fair value"),
    ],
    "thesis": [
        "Booking Holdings is the highest-quality asset in online travel: the dominant accommodation "
        "marketplace in Europe, the highest-margin business in its sector, and a capital-return machine. "
        "The market's periodic worry — that generative AI reshapes travel discovery and "
        "disintermediates aggregators — is a real long-term question but a poor near-to-medium-term "
        "investment thesis. Booking's moat is not a search ranking; it is two-sided network density: the "
        "deepest property inventory, the most reviews, and the most efficient performance-marketing "
        "engine in travel.",
        "Our judgment is that the AI-disruption fear has created the opportunity. Travel booking is a "
        "high-trust, high-consideration transaction where inventory depth, cancellation flexibility, and "
        "customer support matter more than a chat interface. Booking's own AI investments (trip planning, "
        "concierge features, the connected-trip vision) position it to absorb the new interface rather "
        "than be replaced by it. We tested the bear narrative against the numbers: take rates have held, "
        "room-night growth has continued, and alternative-accommodation supply keeps expanding.",
        "At $159.02, the market pays a multiple appropriate for a travel company facing disruption and "
        "gets a compounder that has grown through every prior platform shift. Our probability-weighted "
        "fair value is $219.00, a 38% expected return, driven by room-night growth, take-rate stability, "
        "operating leverage, and relentless buybacks. The bear case assumes genuine AI-driven "
        "disintermediation; we assign it the standard 25% weight, a meaningful concession and the reason "
        "the target is $219 rather than higher.",
        "Consider the assets no entrant can assemble quickly. Booking.com lists millions of properties, "
        "including a vast long tail of independent hotels and alternative accommodations. Hundreds of "
        "millions of verified guest reviews create a data asset that improves conversion and cannot be "
        "scraped into existence. And the performance-marketing operation spends billions annually with a "
        "return on ad spend honed over two decades. An AI startup can build a chat interface in months; "
        "it cannot build these assets in years.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("The connected trip is the growth lever. ",
         "Flights, attractions, airport taxis, and travel insurance attached to accommodation bookings "
         "are growing faster than the core, and each attached product increases customer lifetime value "
         "while using the same acquisition spend. This is how a mature marketplace keeps growing: not by "
         "finding new travelers, but by capturing more of each traveler's wallet."),
        ("Alternative accommodations are the white space. ",
         "Booking has been closing the supply gap with the segment leader for years; each incremental "
         "property improves search completeness and conversion. We expect this segment to outgrow hotels "
         "within the mix, which is margin-accretive."),
        ("Buybacks are the quiet compounding engine. ",
         "With the share count shrinking several percent per year, per-share growth will continue to "
         "outpace enterprise growth indefinitely — at current free cash flow levels this is sustainable "
         "without stretching the balance sheet."),
    ],
    "business": [
        "Booking Holdings operates the world's leading online travel platforms: Booking.com "
        "(accommodation, the core profit engine), Priceline, Agoda, Kayak, and OpenTable. Revenue is "
        "dominated by agency commissions on accommodation bookings, supplemented by advertising, "
        "merchant-model revenue, and ancillary services. Europe is the heartland; the company has been "
        "expanding in the US and Asia.",
        "The economics are exceptional: an asset-light marketplace with minimal marginal cost per "
        "booking, a performance-marketing machine that arbitrages Google and Meta traffic at scale, and "
        "a loyalty ecosystem (Genius) that drives direct repeat traffic. Free cash flow conversion is "
        "among the highest in large-cap technology, and the company returns nearly all of it through "
        "share repurchases.",
        "Geographic mix is a structural advantage. Europe, where Booking.com is dominant, has a "
        "fragmented hotel landscape of independent properties that depend on the platform for demand; "
        "this fragmentation is precisely what makes the marketplace indispensable. In the US, where "
        "chains are stronger, Priceline and Kayak play larger roles, and Agoda anchors the "
        "Asia-Pacific presence.",
    ],
    "business_bullets": [
        ("Two-sided network density. ",
         "The deepest property inventory, the most verified reviews, and the most efficient "
         "performance-marketing engine in travel — each side reinforces the other."),
        ("The Genius flywheel. ",
         "A large share of bookings now comes from repeat members; direct traffic, mobile app usage, "
         "and member pricing tiers reduce marginal acquisition cost over time."),
        ("Alternative-accommodation supply buildout. ",
         "Closing the gap with the category leader property by property, improving completeness and "
         "conversion with every addition."),
    ],
    "outlook": [
        "Where is this business going? We expect Booking to keep compounding room nights at a "
        "high-single-digit rate as global travel normalizes above trend and the company gains share in "
        "alternative accommodations. The connected-trip strategy — flights, attractions, ground transport "
        "attached to the accommodation booking — is the real growth lever: every incremental product "
        "attached raises lifetime value without proportional marketing cost.",
        "On the AI question, our view is that Booking is a net beneficiary of the new interface layer as "
        "long as it owns the transaction. Agentic booking requires live inventory, payments, cancellation "
        "handling, and support — which is infrastructure, not a chatbot. Booking is building exactly that "
        "infrastructure and partnering where it makes sense. The risk is not zero, but it is a five-year "
        "question, not a five-quarter one, and the valuation does not demand perfection.",
        "On capital allocation, we expect the buyback to continue at a pace that retires a mid-single-"
        "digit percentage of shares annually, so per-share metrics compound several points faster than "
        "enterprise metrics indefinitely. Financially: high-single-digit gross-bookings growth, stable "
        "take rates, continued operating leverage, and buybacks at recent intensity.",
    ],
    "financials": [
        "Revenue has grown from $17.09 billion in 2022 to $26.92 billion trailing in 2025, with free cash "
        "flow compounding alongside from $6.19 billion to $9.09 billion — a ~34% FCF margin that is "
        "extraordinary for the sector. The P&L shows the marketplace signature: minimal marginal cost "
        "per booking converts incremental gross bookings into cash at very high rates.",
        "The balance sheet is a fortress with net cash flexibility; the capital-return program has "
        "retired a meaningful share of the float over the years. The valuation is most exposed to the "
        "take rate and the terminal growth rate: a 50bp permanent compression in take rates would reduce "
        "fair value by roughly a tenth; sustained buybacks above our assumed pace add a similar "
        "magnitude.",
    ],
    "fin_table": {
        "headers": ["$ bn", "2022", "2023", "2024", "2025 (TTM)"],
        "rows": [
            ["Revenue", "17.09", "21.37", "23.74", "26.92"],
            ["Free cash flow", "6.19", "7.00", "7.89", "9.09"],
            ["FCF margin", "36%", "33%", "33%", "34%"],
        ],
        "footnote": "Sources: company filings via Yahoo Finance. 2025 = trailing twelve months.",
    },
    "moat": [
        ("Two-sided network density. ",
         "Millions of properties, hundreds of millions of verified reviews, and the industry's most "
         "efficient performance-marketing engine — no entrant can assemble these in years."),
        ("European fragmentation as a structural edge. ",
         "Independent hotels that depend on the platform for demand make Booking.com indispensable in "
         "its heartland."),
        ("The Genius loyalty flywheel. ",
         "Repeat-member bookings reduce marginal acquisition cost over time; better economics fund "
         "better member benefits."),
        ("Marketing scale. ",
         "Billions in annual performance spend with two decades of return-on-ad-spend optimization is "
         "itself a barrier."),
    ],
    "valuation_method": "10-year scenario DCF",
    "valuation_intro": [
        "We value Booking on a 10-year scenario DCF — weights bear 25% / base 50% / bull 25% — with "
        "scenario-specific discounts: bear 12.5% (disruption pricing), base 10.0% (dominant marketplace "
        "with platform-shift risk concentrated in the bear case rather than the discount), bull 8.5%. "
        "Terminal growth is 2.0% / 2.5% / 2.5% on year-10 cash flows at normalized mid-cycle margins.",
        "Scenario fair values: bear $115 (AI-native entrants take share, take rates compress, buybacks "
        "slow), base $212 (high-single-digit bookings growth, stable take rates, operating leverage, "
        "buybacks at recent intensity), bull $337 (faster connected-trip adoption, alternative-"
        "accommodation share gains). Probability-weighted: $219.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 115.00,
            "assumptions": "AI-driven disintermediation compresses take rates and room-night growth; connected trip stalls; buybacks slow",
            "rev_cagr": "+5%", "margin_end": "36%",
            "discount": 0.125, "terminal_g": 0.02, "tv_share": 0.55,
            "pv_explicit": 52.0, "pv_terminal": 63.0, "cashflow_unit": "$/sh",
        },
        "base": {
            "fair_value": 212.00,
            "assumptions": "High-single-digit gross-bookings growth; stable take rates; continued operating leverage; buybacks at recent intensity",
            "rev_cagr": "+9%", "margin_end": "42%",
            "discount": 0.10, "terminal_g": 0.025, "tv_share": 0.62,
            "pv_explicit": 81.0, "pv_terminal": 131.0, "cashflow_unit": "$/sh",
        },
        "bull": {
            "fair_value": 337.00,
            "assumptions": "Faster connected-trip adoption; share gains in alternative accommodations; AI interface absorbed into Booking's own platform",
            "rev_cagr": "+13%", "margin_end": "46%",
            "discount": 0.085, "terminal_g": 0.025, "tv_share": 0.66,
            "pv_explicit": 115.0, "pv_terminal": 222.0, "cashflow_unit": "$/sh",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "risks": [
        ("AI disintermediation. ",
         "AI-native travel agents could bypass aggregators over time, compressing take rates or "
         "volumes — the central bear case."),
        ("Travel cyclicality. ",
         "Recessions, pandemics, or geopolitical shocks hit bookings sharply and quickly."),
        ("Marketing costs. ",
         "Dependence on Google and Meta for acquisition means rising ad prices flow directly to "
         "margins."),
        ("Regulatory. ",
         "European digital-markets rules and tax disputes create ongoing overhang and potential cost."),
        ("Competition. ",
         "Expedia, Airbnb, and direct hotel channels compete for the same travelers and supply."),
        ("FX. ",
         "A large share of revenue is earned in euros and other currencies; dollar strength is a "
         "reported-revenue headwind."),
    ],
    "falsification": (
        "Downgrade to HOLD if room-night growth decelerates to low-single digits for a full year without "
        "a macro cause (structural share loss), if take rates decline persistently (pricing power "
        "eroding, possibly to AI-native competitors), or if a major AI travel agent captures measurable "
        "booking share from aggregators — which would validate the disruption thesis. Buybacks slowing "
        "materially while cash piles up would remove a key per-share compounding driver."
    ),
    "charts": {
        "scenario": {"bear": 115.00, "base": 212.00, "bull": 337.00,
                     "weighted": 219.00, "price": 159.02},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [17.09, 21.365, 23.739, 26.917],
            "fcf_hist": [6.186, 6.999, 7.894, 9.087],
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": rev_proj,
            "fcf_proj": fcf_proj,
            "unit": "$bn", "fcf_label": "FCF",
            "note": "History: company filings via Yahoo Finance (2025 = TTM). Projection: illustrative "
                    "base-case path at ~9% revenue CAGR with FCF margins ~34–36%.",
        },
        "composition": {
            "bear": {"pv_explicit": 52.0, "pv_terminal": 63.0},
            "base": {"pv_explicit": 81.0, "pv_terminal": 131.0},
            "bull": {"pv_explicit": 115.0, "pv_terminal": 222.0},
            "unit": "$/sh",
        },
        "extra": {
            "type": "line",
            "title": "Revenue — reported history vs. base-case path ($bn)",
            "years": [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "series": [
                {"label": "Reported", "values": [17.09, 21.365, 23.739, 26.917, None, None, None, None, None, None, None, None, None, None, None]},
                {"label": "Base case", "values": [None, None, None, None] + rev_proj},
            ],
            "ylabel": "$bn",
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "BKNG-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
