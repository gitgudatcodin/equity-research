"""Polished note build: JD (JD.com, Inc.). Re-runnable via template.build_note."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

data = {
    "ticker": "JD",
    "company": "JD.com, Inc.",
    "exchange": "NASDAQ / HK: 9618",
    "sector": "Consumer Discretionary — Internet Retail",
    "verdict": "BUY",
    "fair_value": 55.00,
    "price": 25.78,
    "risk": "High",
    "headline": "A Fortress Balance Sheet Priced for Ruin — China's Best Retailer for Free",
    "ceo": "Sandy Xu",
    "hq": "Beijing, China",
    "snapshot": [
        ("Market cap", "~$32.2 bn (1.248 bn ADSs × $25.78)"),
        ("Net financial assets", "~$35.8 bn — exceeds market cap"),
        ("Implied operating EV", "Negative (~−$3.6 bn)"),
        ("TTM revenue", "RMB 1,313.5 bn (~$182 bn)"),
        ("TTM non-GAAP EPS", "$2.57 / ADS (P/E 10.0x)"),
        ("Ex-cash P/E", "~4.0x on TTM earnings"),
        ("Dividend (FY2025)", "$1.00 / ADS (~3.9% yield)"),
        ("52-week range", "~$24.51 – $36.86"),
        ("Buybacks 2025", "$3.0 bn (6.3% of shares) + $1.4 bn dividend"),
        ("Next catalyst", "Q3 2026 earnings (Nov 12) + 11.11 festival"),
    ],
    "thesis": [
        "JD.com is China's most logistics-moated retailer: a direct-sales (1P) e-commerce business built "
        "on a proprietary nationwide fulfillment network that delivers same-day and next-day at a scale no "
        "competitor has replicated. The investment case is straightforward and, in our judgment, "
        "underappreciated: JD's moat is physical — warehouses, delivery stations, and a supply chain that "
        "took two decades and enormous capital to build — and physical moats do not erode the way digital "
        "ones do. At $25.78 the shares trade as though Chinese consumption is in permanent decline and JD "
        "is a melting legacy retailer. We see a business generating prodigious operating cash flow, "
        "returning capital through buybacks, and priced at a multiple that assumes the bear case on China "
        "as the permanent state of the world.",
        "Our judgment on the forward trajectory centers on two underappreciated drivers. First, JD's "
        "supply-chain capability is being extended into new categories of demand — instant retail and "
        "on-demand delivery, where JD's fulfillment density is a genuine structural advantage over "
        "marketplace-only competitors. The economics of delivering in under an hour favor the operator that "
        "already has inventory positioned within kilometers of the customer; that is JD. Second, the 1P "
        "model gives JD a quality and authenticity guarantee that matters more, not less, as Chinese "
        "consumers become more discerning — counterfeit and quality concerns structurally favor the "
        "retailer that takes title to the goods it sells. These are durable advantages compounding quietly "
        "while the market debates macro headlines.",
        "We price the China risk explicitly rather than embedding it in pessimism: a 250bp country-risk "
        "premium in the discount rate, regional peer benchmarking, and a bear case at $35.50 that assumes "
        "a prolonged consumption downturn and continued competitive intensity. Even so, the "
        "probability-weighted math supports a $57.50 fair value, and our $55.00 target — a modest haircut "
        "for the wide outcome range in Chinese equities — still implies +113% upside from $25.78. The base "
        "case ($50.67) requires nothing heroic: mid-single-digit revenue growth, stable 1P margins, and "
        "continued capital returns. The bull case ($93.16) assumes consumption normalization plus "
        "successful scaling of instant retail. This is a bet that China's largest quality retailer, bought "
        "at a distressed multiple with the sovereign risk transparently priced, compounds through the cycle.",
        "The starkest framing: at $25.78, JD's $32.2 billion market cap is worth less than its $35.8 "
        "billion of net financial assets — cash, short-term investments and investment securities less debt, "
        "per its own June 30, 2026 balance sheet. The implied enterprise value of the entire operating "
        "business — RMB 1.3 trillion of revenue, record retail operating margins, a logistics arm growing "
        "24–26% — is negative. The market is not pricing in slow growth; it is pricing in permanent value "
        "destruction. Any outcome better than 'burn forever' is upside, and the burn is already inflecting: "
        "the food-delivery loss was cut by more than half in Q2 2026 as the subsidy war de-escalates "
        "under regulatory pressure.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("You are buying the balance sheet at a discount. ",
         "Net financial assets of ~RMB 257.5 billion exceed the entire market capitalization; strip out "
         "net cash and you pay ~4x trailing non-GAAP earnings for the operating company — the cheapest "
         "stub in Chinese large-cap tech."),
        ("The furnace is cooling. ",
         "New Businesses torched RMB 46.6 billion of operating losses in 2025, mostly food-delivery "
         "subsidies; the Q2 2026 loss narrowed sharply as regulators declared the delivery war should "
         "end. Loss normalization is the single biggest earnings lever."),
        ("Capital returns are the compounding engine. ",
         "$3.0 billion of buybacks in 2025 (6.3% of shares) plus a $1.00/ADS dividend, with $1.4 billion "
         "remaining on the authorization — management is converting the cash pile into per-share value "
         "while the stock languishes."),
    ],
    "business": [
        "JD.com, founded by Richard Qiangdong Liu in 1998 (online since 2004; Nasdaq-listed 2014; Hong "
        "Kong secondary listing 9618 in 2020), is China's largest private enterprise by revenue and its "
        "second/third-largest e-commerce platform. The strategy that built JD — own the inventory, own the "
        "logistics — remains its defining difference versus asset-light marketplaces: JD operates ~3,600 "
        "warehouses and a self-built last-mile network covering nearly all of China's counties, which is "
        "why '211' same-/next-day delivery is a brand promise, not a slogan.",
        "The core is the 1P retail business — JD buys inventory and sells it directly, guaranteeing "
        "authenticity — complemented by a third-party marketplace, and powered by JD Logistics, the "
        "integrated supply chain and fulfillment arm with the country's most extensive self-operated "
        "warehouse and delivery network. The group also includes JD Health and JD Industrials (listed "
        "December 2025). Revenue is diversified across electronics, home appliances, general merchandise, "
        "and fast-moving consumer goods, with a customer base of several hundred million annual active "
        "users skewed toward quality-conscious urban consumers — and quarterly and annual active customers "
        "both grew over 20% YoY in Q1 2026, to a record.",
        "The business model differs fundamentally from marketplace peers: JD accepts lower gross margins "
        "on 1P sales in exchange for control over pricing, fulfillment speed, and authenticity, and "
        "monetizes the infrastructure through scale, advertising and logistics services sold to third "
        "parties. This capital intensity was long criticized; it is now the moat. Replicating JD's "
        "fulfillment density would require a competitor to spend tens of billions of yuan and a decade of "
        "operating losses — a check no rational entrant writes against an incumbent already earning "
        "returns on the installed base.",
    ],
    "segment_table": {
        "headers": ["Segment", "Q2'26 revenue (YoY)", "Q2'26 operating income", "What it does"],
        "rows": [
            ["JD Retail", "RMB 295.4 bn (−4.7%)", "RMB 13.5 bn (4.6% margin)",
             "Core 1P direct sales + 3P marketplace; gross margin 18.5% (+1.3 ppt YoY)"],
            ["JD Logistics", "RMB 64.1 bn (+24.3%)", "RMB 2.3 bn non-GAAP (3.5%)",
             "Integrated supply chain for 80k external customers; H1'26 adj. op. profit +39.9%"],
            ["New Businesses", "RMB 7.3 bn", "RMB −9.9 bn (narrowing)",
             "Food delivery, Jingxi, property, overseas — the 2025 furnace, now cooling"],
        ],
        "footnote": "Q2 2026 per company press release (Aug 13, 2026). New Businesses revenue reflects the Q1'26 reclassification of on-demand delivery into Logistics.",
    },
    "business_bullets": [
        ("The owned supply chain. ",
         "~3,600 warehouses, self-operated last-mile, 90%+ of orders same-/next-day. A 20-year capex moat "
         "that cannot be replicated with subsidies."),
        ("Authenticity and big-ticket trust. ",
         "The 1P model makes JD the default for electronics, appliances, and luxury — appliance market "
         "share grew across all major categories in Q2'26."),
        ("The 3P/advertising mix shift. ",
         "Marketplace & marketing revenue +8.3% in Q2 — the highest-margin line, driving record 4.6–5.6% "
         "retail operating margins."),
        ("Logistics as a second engine. ",
         "80,000 external supply-chain customers; automation (Super Brain LLM, robotics) is structural "
         "cost-down, widening the cost gap versus SF Holding and Cainiao."),
    ],
    "outlook": [
        "Our forward view is that JD enters a harvest phase on its logistics investments while planting "
        "the next growth driver in instant retail. We expect the core 1P business to grow roughly in line "
        "with a normalizing Chinese consumption environment — not the boom years, but a durable "
        "mid-single-digit trajectory — with margin expansion coming from scale, advertising attach, and "
        "supply-chain efficiency rather than from price increases. We haircut the most optimistic margin "
        "guidance and assume JD continues to invest a portion of gross profit back into price "
        "competitiveness, which is the correct long-run strategy even if it frustrates near-term margin "
        "expansion.",
        "Instant retail and on-demand delivery is the initiative we watch most closely, and our judgment "
        "is more constructive than the market's. Skeptics see a costly subsidy war with Meituan; we see JD "
        "deploying an existing asset — inventory positioned near customers — into a use case with "
        "structurally better unit economics for JD than for a pure delivery platform that must build supply "
        "from scratch. We model this business reaching contribution-positive on a longer timeline than "
        "management suggests, with meaningful investment drag in the early years, but we assign real "
        "terminal value to a scaled instant-retail franchise because the logistics advantage is genuine and "
        "durable. The falsifiable core of the whole note: if New Businesses losses do not keep narrowing "
        "quarter over quarter, the base case is wrong and the bear owns the stock.",
        "Capital allocation is a quiet pillar of the thesis. JD has been repurchasing shares aggressively, "
        "and at current prices each retired share is retired at a multiple of earnings that makes the "
        "buyback one of the highest-return investments available to the company. We expect buybacks to "
        "continue and to be a material contributor to per-share value compounding; the dividend, while "
        "modest, signals the transition from pure growth to a balanced return profile. Our bear case "
        "assumes consumption stays soft, competition stays intense, and instant retail burns cash longer "
        "than expected — and still values the shares at $35.50, 38% above today's price, which tells you "
        "how much pessimism is already in the quote.",
    ],
    "financials": [
        "The P&L tells a J-curve story: 2025 was the investment year — revenue +13.0% to RMB 1,309.1 "
        "billion, but non-GAAP net income halved to RMB 27.0 billion and free cash flow collapsed to RMB "
        "6.5 billion as food-delivery subsidies peaked. 2026 is the repair year: Q1 revenue +4.9% with a "
        "41% EPS beat, and Q2 — despite the first revenue decline since listing (−2.9%, on the 2025 "
        "trade-in high base) — delivered a striking margin recovery, with operating income swinging to RMB "
        "4.5 billion from a RMB 0.9 billion loss.",
        "The fortress balance sheet: at June 30, 2026 JD held RMB 89.1 billion of cash, RMB 132.6 billion "
        "of short-term investments, RMB 58.0 billion of equity investees and RMB 38.4 billion of marketable "
        "securities — RMB 331.5 billion of financial assets against roughly RMB 74 billion of "
        "interest-bearing debt, for net financial assets of ~RMB 257.5 billion. Current ratio 1.14x; "
        "debt-to-equity 0.19x. On peers (Oct 2, 2026): Pinduoduo ~6.3x forward P/E, Alibaba ~11.7x, Tencent "
        "~11.9x, Meituan ~14.9x — JD at ~10.0x TTM / ~7.6x FY26E is the cheapest on an ex-cash basis (~4.0x).",
    ],
    "fin_table": {
        "headers": ["RMB bn", "2023", "2024", "2025", "H1 2026"],
        "rows": [
            ["Revenue", "1,084.7", "1,158.8", "1,309.1", "662.1"],
            ["YoY growth", "+3.7%", "+6.8%", "+13.0%", "+0.7%"],
            ["Non-GAAP net income", "35.2", "47.8", "27.0", "16.3"],
            ["Non-GAAP net margin", "3.2%", "4.1%", "2.1%", "2.5%"],
            ["Free cash flow", "40.7", "43.7", "6.5", "—"],
        ],
        "footnote": "Sources: JD.com press releases (FY2025 Mar 5, 2026; Q2'26 Aug 13, 2026).",
    },
    "moat": [
        ("The owned supply chain. ",
         "~3,600 warehouses and self-operated last-mile covering nearly all of China's counties — a "
         "20-year capex moat that cannot be replicated with subsidies."),
        ("Authenticity as a business model. ",
         "The 1P model — JD takes title to the goods — makes it the default for big-ticket and luxury, "
         "where counterfeit concerns structurally favor the retailer that owns the inventory."),
        ("Logistics sold to third parties. ",
         "JD Logistics monetizes the network externally (80k customers, +24–26% growth), turning a cost "
         "center into a second engine with expanding margins."),
        ("The moat's tax is the burn. ",
         "New Businesses incinerated RMB 46.6 billion in 2025; the moat is real but management's "
         "willingness to spend the fortress balance sheet on subsidy wars is the recurring risk."),
    ],
    "valuation_method": "10-year scenario FCF DCF",
    "valuation_intro": [
        "We value JD on a probability-weighted scenario DCF over a 10-year horizon, off TTM revenue of RMB "
        "1,313.5 billion, with a 250bp China country-risk premium in the discount rate in all scenarios and "
        "benchmarking against regional peers facing similar risks. Discount rates: base 12.5% (10% standard "
        "plus the country premium, explicitly pricing VIE/regulatory/ADR risk on a net-cash structure), "
        "bear 15.0%, bull 11.0%. Terminal growth is capped at 2.5% on normalized mid-cycle margins. Net "
        "financial assets of RMB 257.5 billion are added to enterprise value; 1.248 billion ADSs; RMB/USD "
        "~7.2. No input is taken from management guidance at face value — margin recovery paths are "
        "anchored to the pre-2025 (2023–2024) margin record, not to promises.",
        "The bear case ($35.50) assumes prolonged soft consumption, sustained competitive intensity from "
        "Pinduoduo and Alibaba, and a longer, costlier ramp in instant retail. The base case ($50.67) "
        "assumes mid-single-digit revenue growth, stable 1P economics with gradual margin expansion from "
        "scale and advertising, and continued share repurchases. The bull case ($93.16) assumes consumption "
        "normalization, successful scaling of instant retail into a profitable franchise, and a re-rating as "
        "the market recognizes the durability of the logistics moat.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 35.50,
            "assumptions": "Prolonged soft consumption; sustained competitive intensity; longer, costlier instant-retail ramp",
            "rev_cagr": "+1.8%", "margin_end": "−0.8%",
            "discount": 0.15, "terminal_g": 0.025, "tv_share": 0.70,
            "pv_explicit": 10.72, "pv_terminal": 24.78, "cashflow_unit": "$/sh",
        },
        "base": {
            "fair_value": 50.67,
            "assumptions": "Mid-single-digit growth; stable 1P economics; gradual margin expansion; buybacks continue",
            "rev_cagr": "+4.5%", "margin_end": "2.8%",
            "discount": 0.125, "terminal_g": 0.025, "tv_share": 0.75,
            "pv_explicit": 12.92, "pv_terminal": 37.75, "cashflow_unit": "$/sh",
        },
        "bull": {
            "fair_value": 93.16,
            "assumptions": "Consumption normalization; instant retail scales profitably; logistics moat re-rated",
            "rev_cagr": "+6.2%", "margin_end": "3.5%",
            "discount": 0.11, "terminal_g": 0.025, "tv_share": 0.76,
            "pv_explicit": 22.64, "pv_terminal": 70.52, "cashflow_unit": "$/sh",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "scenario_note": "Probability-weighted fair value is $57.50; our $55.00 target applies a modest haircut to reflect the wide outcome range in Chinese equities. Terminal-year margins are FCF margins.",
    "risks": [
        ("New-business burn re-accelerates — the thesis risk. ",
         "If the delivery truce breaks and subsidies re-escalate — or Joybuy Europe (the €2.2 bn Ceconomy "
         "acquisition) becomes a second furnace — the cash pile stops compounding per-share value."),
        ("Chinese consumer weakness. ",
         "Retail sales posted their first monthly decline since the pandemic in May 2026; Q2's −2.9% "
         "revenue print shows JD is not immune."),
        ("Competitive re-escalation. ",
         "PDD, Alibaba, and Douyin are rational today; Chinese e-commerce has a long history of "
         "irrational tomorrows."),
        ("Regulatory & geopolitical. ",
         "SAMR fines are a recurring cost of doing business; VIE structure and delisting risk persist by "
         "statute; US tariffs raise import costs."),
        ("Capital-return reversal. ",
         "A buyback or dividend cut would signal that management itself expects the burn to persist — and "
         "remove the one mechanism converting cash into per-share value."),
    ],
    "falsification": (
        "Downgrade to HOLD if food-delivery losses re-accelerate (the subsidy truce breaks), Q3 shows JD "
        "Retail margins rolling over, or buybacks/dividends are cut. Two consecutive quarters of declining "
        "annual active users would indicate share loss beyond cyclical softness; sustained 1P gross-margin "
        "erosion not explained by deliberate price investment would signal structural pricing-power loss. "
        "Raise conviction if New Businesses reaches breakeven ahead of schedule, the buyback authorization "
        "is upsized, or Joybuy shows early traction."
    ),
    "charts": {
        "scenario": {"bear": 35.50, "base": 50.67, "bull": 93.16,
                     "weighted": 57.50, "price": 25.78},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [1046.2, 1084.7, 1158.8, 1309.1],
            "fcf_hist": [34.9, 39.5, 44.3, 4.8],
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": [1368.0, 1429.6, 1493.9, 1561.1, 1631.4, 1704.8, 1781.5, 1861.7, 1945.5, 2033.0, 2124.5],
            "fcf_proj": [23.3, 25.7, 28.4, 31.2, 34.3, 37.5, 41.0, 44.7, 48.6, 52.9, 59.5],
            "unit": "RMB bn", "fcf_label": "FCF",
            "note": "History: company filings (RMB bn). Projections: illustrative base-case paths — revenue at "
                    "the 4.5% scenario CAGR; FCF margin recovering 1.7% → 2.8% as the delivery burn fades.",
        },
        "composition": {
            "bear": {"pv_explicit": 10.72, "pv_terminal": 24.78},
            "base": {"pv_explicit": 12.92, "pv_terminal": 37.75},
            "bull": {"pv_explicit": 22.64, "pv_terminal": 70.52},
            "unit": "$/sh",
        },
        "extra": {
            "type": "pie",
            "title": "Q2'26 revenue mix",
            "labels": ["JD Retail", "JD Logistics", "New Businesses"],
            "values": [81, 17, 2],
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "JD-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
