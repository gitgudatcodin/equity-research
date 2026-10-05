"""Polished note build: SoFi Technologies (SOFI). Re-runnable."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_note

data = {
    "ticker": "SOFI",
    "company": "SoFi Technologies, Inc.",
    "exchange": "NASDAQ",
    "sector": "Financials — Digital Banking & Fintech",
    "verdict": "BUY",
    "fair_value": 22.50,
    "price": 15.77,
    "risk": "Medium-High",
    "headline": "A Deposit-Funded Digital Bank Priced Like a Cyclical Lender",
    "snapshot": [
        ("Market cap", "~$20.4 bn (1.29 bn sh × $15.77)"),
        ("52-week range", "~$14.88 – $32.73"),
        ("Bank charter", "SoFi Bank, N.A. (national bank)"),
        ("Member base", "Tens of millions of members"),
        ("2026E revenue", "~$4.2 bn (net interest income dominant)"),
        ("Funding mix", "Deposits growing faster than the loan book"),
        ("Technology platform", "Galileo + Technisys enterprise revenue"),
        ("Credit", "Net charge-offs at or below through-cycle levels"),
        ("Next catalyst", "Deposit-cost inflection + fee-income scaling"),
        ("Implied upside", "+43% to $22.50 fair value"),
    ],
    "thesis": [
        "SoFi is no longer a story about a bank charter or a student-loan refinancer. It is a "
        "full-stack digital bank whose technology platform, lending engine, and member base now "
        "feed each other: deposits fund lending at a structurally lower cost than wholesale markets, "
        "lending generates the fee and gain-on-sale income that pays for member acquisition, and the "
        "technology platform brings in third-party revenue that is increasingly independent of the "
        "balance sheet. The market still prices SoFi like a cyclical consumer lender; the business "
        "increasingly behaves like a bank with a technology arm.",
        "Our judgment is that the next three years decide whether SoFi compounds at bank-like returns "
        "or fintech-like volatility. Two facts make us constructive: the deposit franchise crossed from "
        "novelty to scale — deposits growing far faster than the loan book, pushing funding costs down "
        "each quarter — and credit performance has held up through a full rate cycle, which we tested "
        "against industry benchmarks rather than taking management's underwriting claims at face value. "
        "If deposit growth persists and the technology platform keeps winning enterprise clients, the "
        "earnings base is far more durable than the current multiple implies.",
        "At $15.77 the market pays for the lending machine and gets the deposit franchise and the "
        "technology platform nearly free. Our probability-weighted fair value is $22.50, a 43% expected "
        "return driven by margin expansion as funding costs fall and fee income scales, not by heroic "
        "multiple expansion. The bear case prices a genuine credit event and sits well below today's "
        "price, as the framework requires.",
        "The third leg is credit discipline. SoFi's personal-loan and student-loan books are "
        "underwritten to high-income, strong-credit borrowers, and net charge-offs have tracked at or "
        "below stated through-the-cycle levels. We compared loss rates against industry card and "
        "personal-loan benchmarks across the 2022–2025 rate cycle, and SoFi's relative performance "
        "held. Underwriting is the one input that can turn a bank thesis into a fintech cautionary tale, "
        "and the evidence so far supports the thesis.",
    ],
    "thesis_subhead": "Why the market will care (eventually)",
    "thesis_bullets": [
        ("The deposit flywheel is the margin engine. ",
         "Every point of funding-cost advantage over wholesale markets is pure net interest margin. "
         "Deposit growth has consistently outpaced loan growth, steadily reducing the cost of funds "
         "and the reliance on wholesale borrowing and loan sales — a structural advantage that "
         "compounds as the base scales."),
        ("Fee income de-risks the earnings base. ",
         "Loan-platform fees, technology-platform revenue, and financial-services fees are growing "
         "faster than net interest income, moving from roughly a fifth toward a third of the mix. "
         "Fee income is less capital-intensive and less credit-sensitive, which over time should "
         "lower the earnings volatility the market currently penalizes."),
        ("The technology platform is a free option. ",
         "Galileo processes payments for a large roster of fintech brands and Technisys gives banks a "
         "cloud-native core; enterprise infrastructure revenue is lumpy but the outsourcing trend is "
         "secular. We value it conservatively in the base case and treat acceleration as upside."),
    ],
    "business": [
        "SoFi Technologies operates a national digital bank (SoFi Bank, N.A.) offering checking and "
        "savings, personal loans, student loan refinancing, mortgage lending, investing, and credit "
        "cards to a member base counted in the tens of millions. The lending segment remains the "
        "earnings engine, with net interest income the largest revenue contributor. Alongside the bank "
        "sit the Technology Platform segment (Galileo and Technisys), which provides payments and "
        "core-banking infrastructure to third parties, and the Financial Services segment, where fee "
        "income from brokerage, credit cards, and other products is growing fast.",
        "The model hinges on a flywheel: low-cost digital acquisition brings members, deposits gathered "
        "from those members fund loans at a spread over wholesale funding costs, and loan economics "
        "fund further acquisition. The technology platform adds a second flywheel: enterprise clients "
        "pay for infrastructure regardless of SoFi's own lending cycle. Revenue mix is shifting toward "
        "fee income, which matters because fee income is less capital-intensive and less "
        "credit-sensitive.",
    ],
    "business_bullets": [
        ("The deposit product is the strategic centerpiece. ",
         "High-yield checking and savings with no account fees, marketed to the same affluent, "
         "digitally native demographic that borrows from SoFi. Because members tend to hold both "
         "deposits and loans, the bank captures the full relationship spread."),
        ("A bank charter changes the unit economics. ",
         "As a chartered bank, SoFi funds at deposit rates rather than wholesale rates and retains "
         "the spread that previously leaked to funding partners — the mechanical source of the "
         "margin expansion we underwrite."),
        ("Enterprise infrastructure as a second business. ",
         "Galileo's payments processing and Technisys's cloud-native core banking give SoFi revenue "
         "that does not depend on its own balance sheet or the credit cycle."),
    ],
    "outlook": [
        "Where is this business going? Our view is that SoFi is crossing from a lending-centric fintech "
        "into a deposit-funded digital bank, and the economics change meaningfully when that happens. "
        "A deposit franchise with SoFi's growth rate compounds net interest income even in a stable rate "
        "environment. We expect the deposit base to keep outgrowing the loan book, converting the "
        "funding mix from good to structurally advantaged over the next two to three years.",
        "The second leg is fee income. The Financial Services segment is still small but growing fast, "
        "and fee-heavy revenue de-risks the earnings base against credit cycles. Combined, we expect "
        "net interest income to remain the anchor while fee income rises toward a third of the mix by "
        "the end of the forecast, materially lowering the earnings beta.",
        "The honest risk to this view is credit. SoFi's borrower base skews affluent and employed, which "
        "has historically meant lower loss rates than the industry, but a genuine recession would test "
        "that claim in a way no model fully captures. Our bear case prices that test. On credit, our "
        "expectation is normalization, not deterioration: loss rates should drift toward historical "
        "averages as the portfolio seasons, and we have modeled that explicitly. The variable to watch "
        "is early-stage delinquency formation.",
        "Longer term, we see a plausible path to SoFi becoming a top-ten US digital bank by deposits, at "
        "which point the valuation conversation shifts from fintech multiples to bank multiples on a much "
        "larger earnings base, with the technology platform as a separately valuable asset. That is a "
        "bull-case outcome, not the base case, but it frames why the current price offers asymmetric "
        "upside.",
    ],
    "financials": [
        "Revenue has compounded from $1.57 billion in 2022 to $3.61 billion on a trailing basis in 2025, "
        "a trajectory driven by loan growth funded increasingly by deposits rather than wholesale "
        "markets. Net income turned positive in 2024 (~$0.50 billion) after the investment phase, and "
        "the trajectory chart below shows net income as the cash-flow proxy: for a bank, reported free "
        "cash flow is dominated by loan-book growth and is not the right compounding metric.",
        "The balance sheet is that of a growing bank: deposits fund the loan book, capital ratios are "
        "managed against growth, and the key operating metrics are net interest margin, the cost of "
        "deposits, and net charge-offs — all of which have moved in the right direction through the "
        "rate cycle.",
    ],
    "fin_table": {
        "headers": ["$ bn", "2022", "2023", "2024", "2025 (TTM)"],
        "rows": [
            ["Total revenue", "1.57", "2.11", "2.61", "3.61"],
            ["Net income", "−0.32", "−0.30", "0.50", "0.48"],
        ],
        "footnote": "Sources: company filings via Yahoo Finance. 2025 = trailing twelve months.",
    },
    "moat": [
        ("The deposit franchise is the moat. ",
         "A self-funded deposit base at national scale is the hardest thing in banking to build and "
         "the most defensible: it lowers funding costs structurally and cannot be replicated quickly "
         "by wholesale-funded competitors."),
        ("Full-relationship capture. ",
         "Members who hold both deposits and loans give SoFi the complete spread plus fee income, "
         "with cross-sell economics that single-product lenders cannot match."),
        ("The charter as a barrier. ",
         "The national bank charter is a regulatory moat: it took years to obtain and lets SoFi keep "
         "the economics that non-bank fintechs surrender to partner banks."),
        ("Technology platform optionality. ",
         "Galileo and Technisys give SoFi a second, balance-sheet-light business with enterprise "
         "relationships across the fintech ecosystem."),
    ],
    "valuation_method": "10-year scenario DCF (equity)",
    "valuation_intro": [
        "We value SoFi on a 10-year scenario equity DCF — weights bear 25% / base 50% / bull 25% — "
        "with scenario-specific discounts: bear 14.0% (credit-event pricing), base 11.5% (bank-plus-"
        "fintech risk), bull 10.0% (derisked mix). Terminal growth is 2.0% / 2.5% / 2.5% on year-10 "
        "earnings at normalized mid-cycle margins — never peak margins. The technology platform is "
        "valued conservatively inside the cash flows in the base case.",
        "The valuation is most sensitive to two inputs: the trajectory of funding costs and the loss "
        "rate on the loan book. A 50bp sustained improvement in the cost of funds adds roughly a tenth "
        "to fair value; a 100bp adverse move in net charge-offs subtracts a similar magnitude. Both "
        "sensitivities sit inside the bear/base/bull spread.",
    ],
    "scenarios": {
        "bear": {
            "fair_value": 12.00,
            "assumptions": "Credit event: net charge-offs normalize sharply above guidance, loan growth stalls, deposit growth slows, funding-cost advantage never materializes",
            "rev_cagr": "+5%", "margin_end": "16%",
            "discount": 0.14, "terminal_g": 0.02, "tv_share": 0.42,
            "pv_explicit": 7.0, "pv_terminal": 5.0, "cashflow_unit": "$/sh",
        },
        "base": {
            "fair_value": 22.00,
            "assumptions": "Deposit franchise keeps funding mid-teens loan growth; funding costs fall steadily; fee income rises toward a third of the mix; credit normalizes, not deteriorates",
            "rev_cagr": "+13%", "margin_end": "24%",
            "discount": 0.115, "terminal_g": 0.025, "tv_share": 0.52,
            "pv_explicit": 10.5, "pv_terminal": 11.5, "cashflow_unit": "$/sh",
        },
        "bull": {
            "fair_value": 34.00,
            "assumptions": "Technology platform scales faster; deposit growth pushes funding costs materially below peers; path toward top-ten digital bank by deposits opens",
            "rev_cagr": "+20%", "margin_end": "30%",
            "discount": 0.10, "terminal_g": 0.025, "tv_share": 0.58,
            "pv_explicit": 15.0, "pv_terminal": 19.0, "cashflow_unit": "$/sh",
        },
    },
    "weights": {"bear": 0.25, "base": 0.5, "bull": 0.25},
    "risks": [
        ("Credit cycle. ",
         "A recession would raise net charge-offs and could impair both earnings and book value "
         "growth — the single largest risk to the thesis."),
        ("Interest-rate sensitivity. ",
         "Net interest margin depends on the rate environment; rapid cuts compress spreads before "
         "deposit repricing catches up."),
        ("Regulatory. ",
         "The bank charter brings supervision; changes in capital or consumer-lending rules could "
         "raise compliance costs or constrain growth."),
        ("Execution on the technology platform. ",
         "Enterprise revenue is lumpy; large contract delays would slow the fee-income "
         "diversification story."),
        ("Competition. ",
         "Large banks and well-funded fintechs compete for the same affluent digital-first customer."),
        ("Student-loan policy. ",
         "Federal student-loan policy changes can affect refinancing volumes."),
    ],
    "falsification": (
        "Downgrade to HOLD if net charge-offs rise well above the stated through-the-cycle range for "
        "two consecutive quarters (breaking the underwriting thesis), or if deposit growth decelerates "
        "persistently below loan growth, reversing the funding advantage that drives the margin call. "
        "Technology-platform revenue declining year over year, or book value per share declining "
        "excluding buybacks, would each independently force a re-underwrite. We watch early-stage "
        "delinquency formation as the leading indicator."
    ),
    "charts": {
        "scenario": {"bear": 12.00, "base": 22.00, "bull": 34.00,
                     "weighted": 22.50, "price": 15.77},
        "trajectory": {
            "years_hist": [2022, 2023, 2024, 2025],
            "revenue_hist": [1.574, 2.108, 2.612, 3.613],
            "fcf_hist": [-0.320, -0.301, 0.499, 0.481],
            "years_proj": [2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036],
            "revenue_proj": [4.15, 4.69, 5.30, 5.99, 6.77, 7.65, 8.64, 9.77, 11.04, 12.47, 14.09],
            "fcf_proj": [0.62, 0.80, 1.01, 1.26, 1.55, 1.90, 2.31, 2.78, 3.29, 3.74, 4.23],
            "unit": "$bn", "fcf_label": "Net income",
            "note": "History: company filings via Yahoo Finance (2025 = TTM). Net income used as "
                    "the compounding metric — reported free cash flow is dominated by loan-book "
                    "growth for a bank. Projection: illustrative base-case path at ~13% revenue "
                    "CAGR with margins expanding toward 24%.",
        },
        "composition": {
            "bear": {"pv_explicit": 7.0, "pv_terminal": 5.0},
            "base": {"pv_explicit": 10.5, "pv_terminal": 11.5},
            "bull": {"pv_explicit": 15.0, "pv_terminal": 19.0},
            "unit": "$/sh",
        },
        "extra": {
            "type": "pie",
            "title": "Revenue mix direction — net interest income vs. fee income",
            "labels": ["Net interest income", "Fee / platform income"],
            "values": [78, 22],
        },
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                   "SOFI-equity-research-note-polished.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
build_note(data, out)
print("built:", out)
