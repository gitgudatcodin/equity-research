# Equity Research Methodology — How These Notes Are Built

This document describes the actual process used to produce the 18 equity research notes
in this library (September 2026). It is grounded in the build scripts in
[`scripts/`](./scripts/) and the notes themselves — not a textbook. If a step here isn't
visible in the scripts or notes, it isn't claimed.

> **Standing framing:** these notes are research analysis / research screens for
> informational purposes. Every note carries a disclaimer to that effect
> ("independent research-style analysis for informational purposes only and is not
> investment advice"; "projections are the author's estimates").

---

## 1. Idea generation and screening

Research starts from **quantitative screens**, not gut picks. The working idea pool comes
from internal screeners (the "Fallen Quality" and "Undiscovered Growth" engines in
`~/workspace/stock-monitor/`), which rank S&P 1500 names on value, quality, momentum and
growth factors against point-in-time price and SEC EDGAR fundamentals.

A screener hit is only a candidate. The recurring pattern across the 18 notes: a quality
franchise **trading near its 52-week low on a fixable or misunderstood problem** —
DKNG and BKNG on prediction-market fears, ADBE on AI-disruption pricing, MCD on a U.S.
execution miss, SOFI on a Fed-hike derating, FI/FIS on post-deal washed-out payments
multiples. Names already past their targets are dropped, not chased (AMD ran past its
$520 target to $630 → HOLD, "do-not-chase at 52-week highs"; WHR's distressed profile
earned a REDUCE). One-line triage applies throughout: candidate, caution, or
fails-the-screens.

---

## 2. Business analysis: moat, industry, management

Each note answers three questions in order:

1. **Is there a moat, and what kind?** Sources of advantage are named specifically —
   network effects (META's advertiser graph, Grab's driver/merchant networks), scale and
   distribution (MCD's 95% franchised system, CELH's PepsiCo distribution), switching
   costs (FIS/FI core banking platforms), brand and regulatory licenses (WYNN's gaming
   concessions). Moat width is asserted with evidence (market share, retention, pricing
   power), never assumed from brand alone.
2. **Is the industry structure attractive?** Notes map the competitive set explicitly
   (Grab vs Uber/DoorDash/Sea; DKNG vs FanDuel and prediction markets; FIS vs Fiserv,
   Global Payments, Adyen) and ask whether the market is pricing a real structural
   threat or a cyclical/misunderstood one.
3. **Can management execute?** Capital allocation track record is checked — M&A history
   (FIS's Worldpay write-down vs the TSYS swap), buybacks, insider signals. Where
   management credibility is thin, the valuation demands a bigger discount.

---

## 3. Financial analysis: SEC filings first

The hierarchy of evidence is fixed and visible in the scripts:

- **SEC EDGAR filings first.** Several notes pull XBRL `companyfacts` directly from
  EDGAR (FIS: revenue, net income, debt, cash, shares, segment facts from the 10-K/10-Qs).
  GAAP numbers anchor everything; adjusted metrics are flagged as non-GAAP with a
  pointer to company reconciliations.
- **Revenue quality:** recurring vs transactional mix (FIS: 90%+ recurring; MCD:
  royalty-driven franchised revenue), growth durability, and customer concentration
  (CELH's PepsiCo concentration).
- **Margins:** gross/operating margin trajectory and the path to normalization —
  Grab's adjusted-FCF margin 11%→18%, MCD's march to low-to-mid-50s operating margin by
  2030, DKNG's adjusted-EBITDA inflection.
- **Free cash flow:** the honesty metric. For acquisitive or amortization-heavy names
  (FIS: GAAP EPS ~$0.73 vs real cash generation) FCF — or an earnings proxy for banks
  (SOFI: adjusted net income ≈ FCFE given minimal dividends and buybacks ≈ SBC) — is
  preferred over EPS.
- **Leverage:** net debt is subtracted in every DCF equity bridge (MCD $39.2B,
  FIS $16.2B, WYNN $8.75B) and stress-tested against maturity walls (WYNN 2027–29).
- **Red flags:** aggressive accounting, deteriorating accruals, one-time gains passed
  off as earnings quality, and unverifiable claims. The rule applied in the scripts:
  **what cannot be verified is excluded from the valuation and disclosed**, never
  quietly modeled — e.g. FIS's Q1 2026 adjusted EPS and segment EBITDA splits, BULL's
  fully diluted share count, TTD's FY2025 FCF, META's Reality Labs unit metrics.

---

## 4. Valuation toolkit

No single method is trusted. Notes typically run **two to four lenses** and blend them:

- **DCF (usually primary).** Scenario-weighted: bear/base/bull cases with their own
  WACC (or cost of equity for banks/insurers) and terminal growth, weighted most often
  25/50/25 (NKE uses 25/55/20; BKNG 20/50/30). WACC is built, not guessed — CAPM with
  stated beta, risk-free rate and ERP (MCD: β 0.45, rf 4%, ERP 5% → 6.5% WACC; ZTS:
  7.5% from 87/13 capital structure). Terminal growth sits at 2–4%, near long-run
  nominal GDP. Sensitivity grids (WACC × g) are shown, e.g. MCD 6–8% × 2–4%.
- **Reverse DCF.** Used as an expectations check: what growth is the market price
  already implying? (ADBE: ~0.1% annual FCF growth; AMD: ~34% annual FCF growth for a
  decade — "valued for near-perfection".)
- **Relative multiples.** Forward P/E, EV/EBITDA, EV/Revenue and PEG against peers
  *and* the company's own history (NKE vs its 28.4× five-year average P/E; BKNG vs its
  20–25× history). Target-implied multiples are shown as a sanity check (DKNG target ≈
  2.8× 2026E revenue).
- **SOTP.** For sum-of-parts businesses: SOFI (Lending/FinSvcs/Tech Platform),
  META (Family of Apps + Reality Labs as an option + net cash), WYNN (Vegas/Macau/Boston
  at different multiples + UAE NPV).
- **DDM.** Only where dividends are the story (MCD, ZTS) — and sometimes deliberately
  excluded from the blend as a floor (ZTS's $80–95 DDM vs the $108 target).
- **Blending.** Weights are stated, not hidden: MCD 40/30/20/10, FI 30/30/25/15,
  BULL 50/50, PYPL 25/30/20/25. When a lens is unreliable, it is **dropped with a
  reason** (BULL: no DCF — brokerage cash flows distorted; TTD: no proprietary model —
  anchored to Morningstar's published fair value instead).

The **12-month target is not always the raw model output**: PYPL's $70 fair value takes
a risk haircut to a $65 target; META's $765 blended FV becomes a $780 target; GRAB's
$6.19 weighted DCF is rounded to a $6.00 target. Fair value vs target is labeled where
it differs.

---

## 5. Risk-rating framework

Risk ratings in the notes are **High / Med-High / Medium / Very high / Speculative** —
a qualitative judgment over the target horizon, driven by:

- **Business risk:** cyclicality, regulatory exposure, single-product or single-market
  concentration, balance-sheet leverage.
- **Thesis risk:** how much of the upside depends on one uncertain event (WYNN's UAE
  build, DKNG's prediction-market outcome, TTD's growth re-acceleration).
- **Drawdown risk:** ratings translate into position-sizing guidance, not just labels —
  SOFI (High): "size for a 30–40% drawdown scenario"; NKE (High): "small starter
  position now, with dry powder reserved"; ADBE: "start with a half position at most".

Higher upside targets systematically pair with higher risk ratings (GRAB +115%/High,
FI +80%/Speculative) — the rating prices the *path*, not just the destination. Where a
note carries no explicit label (ADBE, BULL, META, WYNN), the workbook says so rather
than back-filling one.

---

## 6. Verdict framework

- **BUY:** expected 12-month upside compensates the rated risk; thesis is that the
  market misprices a fixable problem. 12 of 18 notes.
- **HOLD:** fairly valued or fairly valued *for the risk* — upside exists but is thin
  relative to uncertainty (BULL +10%, WYNN +10%, TTD +15%), or the price has already
  run past fair value (AMD above its $520 target; META re-priced near target and
  treated as effectively HOLD).
- **REDUCE/SELL:** reserved for broken theses and value traps (WHR: distressed
  turnaround, REDUCE — outside this 18-note set but same framework).

A verdict is always paired with a **target, a report-date price, an upside %, a risk
rating, and a next catalyst** — the five fields on every note's cover box.

---

## 7. Limitations and biases

Stated plainly, as the notes themselves do:

- **Dated prices.** All 18 notes are priced September 18–26, 2026. Upsides are
  arithmetic on those snapshots, not live quotes — several notes (META, AMD) were
  explicitly re-priced days later as prices moved.
- **Estimates, labeled.** Out-year forecasts are the author's (or consensus-derived)
  estimates. The scripts tag estimated quarters/inputs inline (e.g. FIS Q4 2025 revenue,
  SOFI Q2 2025 deposits) and the workbook's Notes sheet collects every flagged item.
- **Stale consensus.** Peer multiples and "consensus" figures vary by provider and
  vintage; TTD's peer P/Es conflicted across providers and were excluded rather than
  averaged.
- **Survivorship and selection bias.** The idea pool comes from screens of current
  index constituents; the notes select washed-out quality names, which tilts the set
  toward turnaround stories that can keep falling.
- **No precision implied.** Scenario weights, method blends and terminal values are
  judgmental. The notes present ranges and sensitivities (DCF grids, bull/bear cases)
  precisely so the target is read as a central tendency, not a prediction.
- **Analyst bias.** The author builds the bull case they find convincing; the
  structural defense is the bear case being modeled and priced explicitly in every DCF.
