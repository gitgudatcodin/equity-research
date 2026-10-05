#!/usr/bin/env python3
"""Build valuations.xlsx — consolidated valuation workbook across 18 equity research notes (Sep 2026).

Sheets:
  1. Summary        — ticker, company, verdict, target, report price, upside, risk, methods
  2. DCF detail     — discount-rate / terminal-growth assumptions and scenario values
  3. Multiples detail — relative-valuation methods, benchmarks, implied values
  4. Notes          — missing inputs, estimates, data limitations, exclusions

All figures are extracted from the notes as written. Absent figures are left blank
(with 'n/a' notes), never invented.
"""
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

OUT = "/home/hatch/workspace/your_files/research-valuations/valuations.xlsx"

NAVY = "0F2A44"; LGRAY = "F2F4F7"; WHITE = "FFFFFF"
ACCENT = "0E7C3E"; RED = "B42318"
THIN = Side(style="thin", color="D9DEE5")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
HEAD_FILL = PatternFill("solid", fgColor=NAVY)
HEAD_FONT = Font(bold=True, color=WHITE, size=10)
TITLE_FONT = Font(bold=True, color=NAVY, size=13)
SUB_FONT = Font(color="5A6472", size=9, italic=True)
BAND1 = PatternFill("solid", fgColor=WHITE)
BAND2 = PatternFill("solid", fgColor=LGRAY)
WRAP = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(horizontal="center", vertical="top", wrap_text=True)

# ---------------------------------------------------------------- summary data
# ticker, company, verdict, target, target_type, report_price, price_date, upside, risk, methods_used
SUMMARY = [
    ("DKNG", "DraftKings Inc.", "BUY", 36.00, "12-month target", 21.75, "Sep 19, 2026", "+65%", "High",
     "Scenario-weighted DCF (primary); multiples cross-check (EV/Rev, EV/EBITDA, P/E)"),
    ("GRAB", "Grab Holdings Ltd.", "BUY", 6.00, "12-month target", 2.79, "Sep 18, 2026", "+115%", "High",
     "DCF (primary, scenario-weighted); peer multiples; SOTP cross-check"),
    ("BKNG", "Booking Holdings Inc.", "BUY", 222.00, "12-month target", 167.90, "Sep 18, 2026", "+32%", "Med-High",
     "Scenario-weighted DCF (primary); P/E, EV/EBITDA, PEG, FCF-yield cross-checks"),
    ("ADBE", "Adobe Inc.", "BUY", 465, "12-month target", 248.92, "Sep 18, 2026", "+87%", "n/a — no explicit label in note (note advises sizing at half position)",
     "Scenario-weighted DCF; reverse DCF; FY2027E EPS multiple; target bridge 70% DCF / 30% EPS multiple"),
    ("MCD", "McDonald's Corp.", "BUY", 300.00, "12-month target", 236.50, "Sep 25, 2026", "+27%", "Medium",
     "Blended: DCF 40% + forward P/E 30% + EV/EBITDA 20% + DDM 10%"),
    ("SOFI", "SoFi Technologies Inc.", "BUY", 23.50, "12-month target", 16.58, "Sep 25, 2026", "+42%", "High",
     "Scenario-weighted earnings-power DCF (primary); peer multiples; SOTP cross-check"),
    ("NFLX", "Netflix Inc.", "BUY", 90, "fair value", 71.79, "Sep 18, 2026", "+25%", "Medium",
     "Blended fair value: DCF 40% + P/E 25% + EV/operating income 20% + FCF yield 15%"),
    ("NKE", "Nike Inc.", "BUY", 46.00, "12-month target", 35.56, "Sep 18, 2026", "+29%", "High",
     "Scenario-weighted DCF blended with own-history & peer multiples; analyst-consensus cross-check"),
    ("PYPL", "PayPal Holdings Inc.", "BUY", 65.00, "12-month target (fair value $70)", 52.41, "Sep 18, 2026", "+24% to target / +34% to FV", "High",
     "Method blend (FV $70): FY26 P/E 25% + normalized P/FCF 30% + txn-margin$ 20% + DCF 25%; $65 target is FV with risk haircut"),
    ("ZTS", "Zoetis Inc.", "BUY", 108, "12-month target", 71.40, "Sep 19, 2026", "+51%", "High",
     "Base DCF 50% + relative P/E 30% + scenario-weighted DCF 20%; two-stage DDM as floor only"),
    ("CELH", "Celsius Holdings Inc.", "BUY", 38.00, "12-month target", 28.02, "Sep 18, 2026", "+36%", "High",
     "DCF + EV/EBITDA multiples vs Monster + PEG cross-check; scenario-weighted ($37.25 → $38)"),
    ("FI", "Fiserv Inc.", "BUY", 85, "12-month target", 47.19, "Sep 19, 2026", "+80%", "Speculative / High",
     "Blended: DCF 30% + forward P/E 30% + EV/EBITDA 25% + FCF-yield 15%"),
    ("BULL", "Webull Corp.", "HOLD", 9.10, "fair value", 8.25, "Sep 19, 2026", "+10%", "n/a — no explicit label in note",
     "50/50 blend: 2027E P/E + EV/Sales incl. net cash; no DCF (brokerage cash flows unreliable)"),
    ("META", "Meta Platforms Inc.", "BUY", 780, "12-month target (blended FV $765)", 665.75, "Sep 18, 2026", "+17%", "n/a — note says 'asymmetric, but not low risk'",
     "Blended FV $765: DCF 40% + relative multiples 35% + SOTP 25%; reverse-DCF sanity check"),
    ("WYNN", "Wynn Resorts Ltd.", "HOLD", 90.00, "12-month target (blended FV $88)", 81.68, "Sep 18, 2026", "+10%", "n/a — speculative buy only below $75",
     "Trading multiple ($88) + SOTP ($89) + FCFE ($87); bear/base/bull scenarios 25/50/25"),
    ("TTD", "The Trade Desk Inc.", "HOLD", 16.00, "fair value", 13.92, "Sep 18, 2026", "+15%", "Very high",
     "Fair value anchored to Morningstar's published estimate; no proprietary DCF or multiples model"),
    ("AMD", "Advanced Micro Devices Inc.", "HOLD", 520, "12-month target (blended FV ~$500)", 559.82, "Sep 19, 2026", "n/a — price above target at note time", "High",
     "Base DCF + bull case + reverse DCF (sanity check on embedded growth)"),
    ("FIS", "Fidelity National Info. Svcs.", "BUY", 49.50, "12-month target", 35.41, "Sep 25, 2026", "+40%", "High",
     "Scenario-weighted FCF DCF (primary); peer multiples; dividend & FCF-yield cross-checks"),
]
SUMMARY_COLS = ["Ticker", "Company", "Verdict", "Target ($)", "Target type", "Report price ($)",
                "Price date", "Implied upside", "Risk rating", "Valuation methods used"]
SUMMARY_WIDTHS = [8, 24, 9, 11, 22, 13, 14, 18, 20, 52]

# ---------------------------------------------------------------- DCF detail
# ticker, cash_flow_measure, horizon/other, wacc_bear, wacc_base, wacc_bull,
# g_bear, g_base, g_bull, val_bear, val_base, val_bull, weights, weighted, notes
DCF = [
    ("DKNG", "FCF ≈ adj. EBITDA − capex − cash taxes − WC investment", "Net debt ~$1.0B; ~496.5M shares",
     "12.0%", "11.0%", "10.0%", "2.0%", "3.0%", "3.5%", 16, 36, 55, "25/50/25", 35.75,
     "Weighted DCF rounds to $36 target"),
    ("GRAB", "Adjusted FCF; 2026–35 revenue $4.13B→$14.8B (base), FCF margin 11%→18%",
     "Pro forma net cash $3.5B ($5.0B reported − $1.49B Atome)",
     "12.0%", "11.0%", "10.0%", "2.5%", "3.5%", "4.0%", 3.12, 6.00, 9.65, "25/50/25", 6.19,
     "Target $6.00 set at base case, below $6.19 weighted"),
    ("BKNG", "FCF: FY25 $9.1B → 2030 $16.3B (base)", "Net debt ~$3.0B; ~816M shares post-split",
     "12.0%", "10.5%", "10.0%", "2.0%", "3.0%", "3.5%", 121, 222, 290, "20/50/30", 222.00,
     "Weighted value exactly matches $222 target"),
    ("ADBE", "FCF: FY26 base $10.4B; bear −3%/yr; base +11/10/9/8/7%; bull +12/12/11/10/9%",
     "Net debt ~$1B; ~395M shares",
     "11.0%", "10.5%", "9.5%", "1.0%", "3.5%", "4.0%", 222, 490, 663, "25/50/25", 466,
     "Weighted ≈$466; target $465 via 70% DCF / 30% EPS-multiple bridge"),
    ("MCD", "FCF: 2026E $7.6B → 2030E $9.9B", "Net debt $39.2B; ~710M shares; CAPM WACC 5.8% (β 0.45, rf 4%, ERP 5%) → used 6.5%",
     "sensitivity", "6.5%", "sensitivity", "2%", "3%", "4%", None, 295, None, "base", 295,
     "Base $295 is 40% of target; sensitivity grid WACC 6–8% × g 2–4%"),
    ("SOFI", "Adjusted net income as proxy for FCFE (minimal divs; buybacks ≈ SBC)", "2026–35; 2026E adj. NI ~$825M anchors guidance",
     "13.5%", "12.0%", "10.5%", "2.5%", "3.5%", "4.0%", 12.80, 22.31, 37.01, "25/50/25", 23.61,
     "Cost of equity (not WACC) — bank valued on earnings; SOTP cross-check $22.36"),
    ("NFLX", "Explicit 2027–31 FCF", "Net debt $5.3B; 4.164B post-split shares",
     "9.5%", "8.5%", "8.0%", "3.0%", "3.5%", "3.5%", 53, None, 114, None, None,
     "DCF is 40% of $88.7 weighted FV (with P/E 25%, EV/OI 20%, FCF yield 15%)"),
    ("NKE", "Unlevered FCF FY27–30 (bear 1.8/2.0/2.1/2.2; base 2.6/3.3/4.0/4.6; bull 3.0/3.9/4.8/5.6 $B)",
     "WACC 8.5% base (CoE 9.1%: β 1.06, rf 4.3%, ERP 4.5%)",
     "9.5%", "8.5%", "8.0%", "2.5%", "2.75%", "3.0%", 20, 48, 67, "25/55/20", 45,
     "Weighted ≈$45; $46 target blends DCF with multiples & consensus"),
    ("PYPL", "FCF from $5.6B start, 1–3% near-term growth", "Cost of equity 11% (not WACC)",
     None, "11.0%", None, None, "2.0%", None, None, None, 77, "method 25%", 77,
     "Equity DCF $77 is 25% of method blend; sensitivity table in note"),
    ("ZTS", "FCF explicit 2027–30", "WACC 7.5% (CoE 7.9%: rf 4.25%+0.70×5.25%; AT debt 4.3%; 87/13); net debt ~$6.7B; ~423M sh",
     "8.0%", "7.5%", "7.0%", "2.0%", "2.5%", "3.0%", 66, 110, 169, "30/45/25", 112,
     "Weighted $112 is 20% of target; base $110 is 50%; DDM $80–95 floor excluded from blend"),
    ("CELH", "FCF FY27–31: 450/540/615/675/725 $M", "EV $11.2B − net debt $54M − $1.76B PepsiCo preferred; 260M shares; WACC 9.0% (CoE 9.3%: rf 4.3%, β 1.0, ERP 5.0%; ~99% equity)",
     None, "9.0%", None, None, "3.5%", None, None, None, 36, "single base", 36,
     "Sensitivity: WACC 8–11% × g 2.5–4.0% → $21–$54; base scenario $37 = blend of DCF $36 + 14× EBITDA $39"),
    ("FI", "FCF $3.8B → $4.85B", "$75B EV − $26.5B net debt; bear DCF: WACC 9%, g 1% → ~$40",
     None, "8.0%", None, None, "2.0%", None, 40, 92, None, "DCF 30%", 92,
     "DCF value $92 is 30% of $85 blended target"),
    ("BULL", "n/a — no DCF built", "Brokerage cash flows distorted by customer/clearing movements; normalized owner earnings not verified",
     None, None, None, None, None, None, None, None, None, None, None,
     "Valuation is pure multiples blend (see Multiples sheet)"),
    ("META", "EPS owner-earnings proxy: 2027E $35.0, 18% CAGR to 2031 ($67.8)", "Cost of equity (not WACC)",
     "11%", "10%", "9%", "3%", "3%", "3%", 677, 782, 923, "DCF 40%", 782,
     "DCF $782 = 40% of $765 blended FV; base-vs-bull WACC sensitivities shown"),
    ("WYNN", "FCFE 2026–30: $720M/$680M/$850M/$950M/$1.0B", "Cost of equity 11.5% (not WACC)",
     None, "11.5%", None, None, "2.5%", None, None, None, 87, "FCFE 1/3", 87,
     "FCFE $87 averaged with $88 trading multiple and $89 SOTP; bear $55 / base $89 / bull $123 scenarios (25/50/25 → $89)"),
    ("TTD", "n/a — no proprietary DCF built", "Fair value anchored to Morningstar's published $16 estimate",
     None, None, None, None, None, None, None, None, None, None, None,
     "See Notes sheet"),
    ("AMD", "Base-case FCF (AI-server upside in bull)", "n/a",
     None, "11.0%", None, None, "4.0%", None, None, None, 368, None, 368,
     "Bull $768 (20%+ AI GPU share); reverse DCF implies ~34% annual FCF growth for 10 years"),
    ("FIS", "FCF from $2.20B 2026E base, 10-yr, Gordon TV", "Net debt $16.2B (post-TSYS)",
     "10.0%", "9.0%", "8.5%", "2.0%", "2.5%", "3.0%", 26.16, 49.94, 72.60, "25/50/25", 49.66,
     "Weighted $49.66; target $49.50; bear: integration stumbles, ~2.5% FCF CAGR"),
]
DCF_COLS = ["Ticker", "Cash-flow measure", "Capital / horizon detail", "WACC bear", "WACC base", "WACC bull",
            "Terminal g bear", "Terminal g base", "Terminal g bull", "Bear value ($)", "Base value ($)",
            "Bull value ($)", "Weights (bear/base/bull)", "Weighted value ($)", "Notes"]
DCF_WIDTHS = [7, 40, 40, 10, 10, 10, 11, 11, 11, 11, 11, 11, 16, 13, 42]

# ---------------------------------------------------------------- multiples
# ticker, method, multiple_used, benchmark, implied_value, notes
MULT = [
    ("DKNG", "EV/Revenue", "2.8× 2026E revenue (target-implied; 1.75× today)", "Susquehanna sales framework ~3.6×; scaled platforms higher", None, "Target-implied multiple, not an independent estimate"),
    ("DKNG", "EV/EBITDA", "~23.5× 2026E adj. EBITDA", "13× on 2028E adj. EBITDA ~$1.9B → EV $24.7B (~2× upside)", None, ""),
    ("DKNG", "P/E", "~28× 2027E adj. EPS ~$1.30", "Growth-adjusted context", None, "28× ≈ $36 implied"),
    ("GRAB", "EV/Revenue", "peer set", "Uber 2.4×; DoorDash 4.1×; Sea n/a rev", None, "Grab cheapest on sales & EBITDA despite 22%+ rev growth, 44–48% EBITDA growth"),
    ("GRAB", "EV/EBITDA", "peer set", "Uber ~14×; DoorDash ~45–50×; Sea ~24.5×", None, ""),
    ("GRAB", "SOTP", "segment lens", "n/a", 5.65, "Cross-check vs $6.00 target"),
    ("BKNG", "P/E", "21.3× 2026E adj. EPS ~$10.42 (16.0× today)", "Own 5-yr 20–25×; peers 22–35×", None, "Target-implied"),
    ("BKNG", "EV/EBITDA", "15.0× 2027E (12.8× TTM today)", "Own 3-yr avg 16–17.5×; peer avg ~14.7×", None, "Target-implied"),
    ("BKNG", "PEG", "1.6× (1.2× today)", "n/a", None, ""),
    ("BKNG", "FCF yield", "5.8% (8.0% today)", "n/a", None, ""),
    ("ADBE", "P/E", "17× FY27E non-GAAP EPS $27.40", "n/a", 466, "30% of target bridge (70% DCF)"),
    ("ADBE", "Reverse DCF", "implied ~0.1% annual FCF growth (5-yr path, 0% terminal)", "n/a", None, "Expectations bar is low"),
    ("MCD", "Forward P/E", "22× 2027E EPS $13.89 (range 20×–24×)", "Peers YUM/DOM 21–22×; own history ~24×", 306, "30% of target; range $278–$333"),
    ("MCD", "EV/EBITDA", "16.5× 2027E EBITDA ~$15.9B", "YUM 16.4×; Domino's 16.8×; RBI 13.8×; own 18–19×", 314, "20% of target"),
    ("MCD", "DDM (Gordon)", "$7.72 div, 6% perpetual growth, 9% required", "n/a", 273, "10% of target"),
    ("SOFI", "P/E (peer)", "~28× 2026E adj. EPS $0.60; 2.3× tangible book", "Robinhood 52.4×; Block 129.2×; Affirm 12.5×; Upstart 38.4×; Ally 9.1×", None, "Discount to peers despite faster growth"),
    ("SOFI", "SOTP", "Lending 10× contrib. profit; FinSvcs 12×; Tech 9× sales", "n/a", 22.36, "Lending $16.0B + FinSvcs $10.3B + Tech $3.0B; 1.31B shares"),
    ("NFLX", "P/E", "25× forward EPS", "n/a", None, "25% of $88.7 weighted FV"),
    ("NFLX", "EV/Operating income", "20×", "n/a", None, "20% of $88.7 weighted FV"),
    ("NFLX", "FCF yield", "4.25%", "n/a", None, "15% of $88.7 weighted FV"),
    ("NKE", "P/E (own history)", "~17× TTM GAAP EPS (own 5-yr avg 28.4×)", "FY27E consensus: ~18–21× by vintage", None, "Optically cheap on GAAP"),
    ("NKE", "EV/EBITDA", "~9× vs own history 12–18×", "Peers ~12–18× range", None, ""),
    ("NKE", "P/E (scenario framing)", "24× FY28E EPS $2.70", "n/a", 65, "Frames bull case; 20–24× supports $44–$52"),
    ("PYPL", "P/E", "11.5× FY26E EPS $5.38", "n/a", 62, "25% of FV $70 method blend"),
    ("PYPL", "P/FCF (normalized)", "10× ($6.0B / 855M shares)", "n/a", 70, "30% of FV $70 method blend"),
    ("PYPL", "Transaction-margin $", "3.5× $15.6B + net cash", "n/a", 66, "20% of FV $70 method blend"),
    ("ZTS", "P/E (relative)", "16× 2027E adj. EPS ~$6.70 (range 15×–17×)", "Own 10-yr avg 28×; IDEXX 28×; peers 17–19×", 107, "30% of target; range $100–$114"),
    ("ZTS", "EV/EBITDA", "12–13× 2027E EBITDA ~$3.96B", "n/a", "96–106", "Cross-check"),
    ("ZTS", "DDM (two-stage)", "$2.12 div, 10% 5-yr then 4–5%, 8% discount", "n/a", "80–95", "Floor only — excluded from target blend"),
    ("CELH", "EV/EBITDA", "14× FY27E EBITDA $852M (12×–16× range)", "Monster ~25×; KO ~21×; PEP ~12×; KDP ~15–18×", 39, "Midpoint; 45–60% discount to Monster; 50% of base scenario $37"),
    ("CELH", "PEG", "~0.8–1.0 (19× fwd P/E ÷ 20–24% EPS CAGR)", "Monster PEG ~3×", None, "Cheap on growth-adjusted basis"),
    ("FI", "Forward P/E", "11× 2027E EPS $8.15", "Own 5-yr median 15.2×", 90, "30% of target; bear DCF ~$40 at 9%/1%"),
    ("FI", "EV/EBITDA", "7.5× ($8.9B EBITDA)", "n/a", 76, "25% of target"),
    ("FI", "FCF yield", "10% required equity yield on $3.9–4.1B FCF", "n/a", "73–77", "15% of target"),
    ("BULL", "P/E", "28× 2027E EPS $0.30", "growth-broker peer context; Street $11 cross-check", 8.40, "50% of $9.10 FV; ~492M shares"),
    ("BULL", "EV/Sales", "3.0× 2027E revenue $984.2M + ~$1.85B net cash", "n/a", 9.77, "50% of $9.10 FV"),
    ("META", "P/E", "24× 2027E EPS $35.0", "n/a", 840, "Composite midpoint with EV/EBITDA lens ≈$795 = 35% of FV"),
    ("META", "EV/EBITDA", "13–14× Dec-2026 EBITDA $143.4B − ~$22B net debt", "n/a", "727–786", "Composite midpoint ≈$795"),
    ("META", "SOTP", "FoA NOPAT ~$82B × 21× + $50B RL option + $6.6B net cash", "n/a", "~700–703", "25% of FV; RL valued as option"),
    ("WYNN", "EV/EBITDAR", "8.0× normalized $2.30B − $8.75B net debt, ~110M sh", "~7.8× est. TTM", 88, "FV component; debt-heavy capital structure"),
    ("WYNN", "SOTP", "9× Las Vegas / 8× Macau / 7× Boston + UAE/Enclave NPV − debt − $0.5B reserve", "n/a", 89, "FV component"),
    ("TTD", "n/a", "Peer P/E figures conflicted across providers — not used", "Morningstar FV $16 anchor", None, "No proprietary multiples model"),
    ("AMD", "Reverse DCF only", "Market implies ~34% annual FCF growth for 10 years", "n/a", None, "Valued for near-perfection; target $520 below spot $559.82"),
    ("FIS", "P/E (peer)", "7.0–8.5× 2027E adj. EPS ~$6.63 (5.7× 2026E today)", "Fiserv 8.7×; GPN 6.3×; Adyen ~24×", "46.41–56.35", "Cross-check; DCF is primary"),
    ("FIS", "EV/EBITDA", "~6.1× vs Adyen ~20×", "Adyen ~20×", None, "Cross-check"),
    ("FIS", "Dividend / FCF yield", "5.0% div yield; ~12% FCF yield", "n/a", None, "Cross-check"),
]
MULT_COLS = ["Ticker", "Method", "Multiple / input used", "Peer / benchmark context", "Implied value ($)", "Notes"]
MULT_WIDTHS = [7, 20, 44, 40, 14, 40]

# ---------------------------------------------------------------- notes
NOTES = [
    ("DKNG", "Estimates", "Out-year forecasts are author estimates; 2026–27 anchored to guidance/consensus. Target and valuation involve uncertainty."),
    ("GRAB", "Excluded from valuation", "Reported CEO share sale (Sep 8, 2026) was single-source and could not be fully verified — excluded."),
    ("GRAB", "Estimates", "Regulatory EBITDA-hit estimates (3–6%, ~10% if extended to four-wheelers) are third-party estimates, not modeled as a base case."),
    ("BKNG", "Estimates", "2026E figures are consensus/derived; adjusted EPS converted to post-split basis. Target involves uncertainty."),
    ("ADBE", "Estimates", "FY2027–FY2030 are analyst estimates; FY2026 anchored to company midpoint and a normalized $10.4B FCF base. Reverse-DCF path is stylized, not a forecast."),
    ("MCD", "Estimates", "2028E+ figures and margins are author estimates calibrated to the Sept 2026 Investor Day 2030 targets. Sensitivity range $212 (bear) to $365 (bull)."),
    ("SOFI", "Excluded from valuation", "Identity of departed Technology Platform executive, Q3 2025 segment splits beyond reported totals — could not be verified, excluded."),
    ("SOFI", "Estimates", "Q2 2025 deposit figure estimated from reported growth rates."),
    ("NFLX", "Estimates", "2026 revenue/margin/FCF use company guidance midpoints; forecasts beyond are author estimates."),
    ("NFLX", "Judgment", "Method weights (DCF 40 / P-E 25 / EV-OI 20 / FCF yield 15) are judgmental."),
    ("NKE", "Could not verify", "Exact FY2025 Greater China revenue base could not be independently verified."),
    ("NKE", "Estimates", "Valuation estimates and scenarios are the author's; consensus figures vary by provider/vintage."),
    ("PYPL", "Distinction", "Note distinguishes $70 fair value (method blend) from $65 12-month target (risk haircut). Scenario: bear $40 (25%) / base $70 (55%) / bull $95 (20%)."),
    ("ZTS", "Excluded from blend", "Two-stage DDM ($80–95) is a floor/cross-check only — not in the weighted target."),
    ("ZTS", "Estimates", "FY2026E per Aug-2026 guidance midpoints; forward FCF estimated."),
    ("CELH", "Assumption", "$1.76B PepsiCo preferred treated as debt-like in equity bridge. DCF sensitivity: WACC 8–11% × g 2.5–4.0% → $21–$54/share."),
    ("FI", "Estimates", "Figures are this note's estimates, not company guidance; 2027 EPS uses consensus."),
    ("BULL", "Could not verify", "Fully diluted share count, index-inclusion status, PIPE/warrant counts and precise Q2 funded accounts were not verified."),
    ("BULL", "Methodological", "No DCF by design: brokerage cash flows distorted by customer/clearing movements; normalized owner earnings not verified."),
    ("META", "Could not verify", "Quest units/Horizon metrics, Taiwan supply-chain exposure, remaining buyback authorization — not verified; 2028 revenue/EPS single-source."),
    ("META", "Distinction", "Blended fair value $765 vs 12-month target $780. Note: 'asymmetric, but not low risk' — no explicit risk label."),
    ("WYNN", "Could not verify", "Sept. 10, 2026 notes-offering terms not verified in an SEC filing for this note; precise ADR/RevPAR peer comps not verified."),
    ("WYNN", "Estimates", "Normalized $2.30B EBITDAR, ~110M shares, UAE/Enclave NPV are analytical estimates, not company guidance."),
    ("TTD", "Excluded from valuation", "FY2025 FCF was not reverified — excluded. Peer P/E figures conflicted across providers — not used."),
    ("TTD", "Methodological", "Fair value $16 is an analyst judgment anchored to Morningstar's September 2026 published estimate; no formal DCF/multiple model built."),
    ("AMD", "Estimates", "Scenario values are analyst estimates; reverse DCF is a sanity check on embedded growth expectations, not a forecast."),
    ("FIS", "Excluded from valuation", "Q1 2026 adjusted EPS and segment EBITDA splits beyond reported revenue could not be verified — excluded."),
    ("FIS", "Estimates", "Q4 2025 revenue estimated from full-year trajectory; post-deal share count estimated (~515M vs FY2025's 519M)."),
    ("FIS", "General", "Targets and valuations are analytical estimates, not company guidance; past performance does not predict future results."),
]
NOTES_COLS = ["Ticker", "Topic", "Note"]
NOTES_WIDTHS = [7, 22, 110]

# ---------------------------------------------------------------- helpers
def add_sheet(wb, title, cols, widths, rows, intro):
    ws = wb.create_sheet(title)
    ws.sheet_view.showGridLines = False
    ws["A1"] = title
    ws["A1"].font = TITLE_FONT
    ws["A2"] = intro
    ws["A2"].font = SUB_FONT
    ws["A2"].alignment = Alignment(wrap_text=True)
    ws.row_dimensions[2].height = 34
    hdr_row = 4
    for c, (col, w) in enumerate(zip(cols, widths), start=1):
        cell = ws.cell(row=hdr_row, column=c, value=col)
        cell.font = HEAD_FONT
        cell.fill = HEAD_FILL
        cell.alignment = CENTER
        cell.border = BORDER
        ws.column_dimensions[get_column_letter(c)].width = w
    for r, row in enumerate(rows, start=hdr_row + 1):
        fill = BAND1 if r % 2 == 0 else BAND2
        for c, val in enumerate(row, start=1):
            cell = ws.cell(row=r, column=c, value=val)
            cell.fill = fill
            cell.border = BORDER
            cell.font = Font(size=10)
            cell.alignment = WRAP if c not in (1, 3) else CENTER
        ws.row_dimensions[r].height = 30
    ws.freeze_panes = "A5"
    ws.auto_filter.ref = f"A{hdr_row}:{get_column_letter(len(cols))}{hdr_row + len(rows)}"
    return ws

def main():
    wb = Workbook()
    wb.remove(wb.active)
    add_sheet(wb, "Summary", SUMMARY_COLS, SUMMARY_WIDTHS, SUMMARY,
              "Verdict, target, report-date price, upside and risk rating for each of the 18 equity research notes (Sep 2026). "
              "All figures are extracted from the notes as written; missing items are blank with an 'n/a' note — never invented. "
              "This workbook is a research-analysis tool, not investment advice.")
    add_sheet(wb, "DCF detail", DCF_COLS, DCF_WIDTHS, DCF,
              "Discount-rate (WACC / cost of equity) and terminal-growth assumptions, scenario values and weights for every note "
              "that built a DCF. BULL and TTD have no DCF — see their rows and the Notes sheet for why.")
    add_sheet(wb, "Multiples detail", MULT_COLS, MULT_WIDTHS, MULT,
              "Every relative-valuation lens used in the 18 notes: the multiple applied, the peer/history benchmark behind it, "
              "and the implied value where the note stated one.")
    add_sheet(wb, "Notes", NOTES_COLS, NOTES_WIDTHS, NOTES,
              "Data limitations, estimates, unverifiable items excluded from valuation, and methodological caveats — one row per flag. "
              "Blank cells in the other sheets trace back to a row here.")
    wb.save(OUT)
    print(f"saved {OUT} ({os.path.getsize(OUT)/1024:.0f} KB)")

if __name__ == "__main__":
    main()
