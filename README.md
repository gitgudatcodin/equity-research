# Equity Research Methodology — How These Notes Are Built

This document describes the actual process used to produce the 56 equity research notes
in this library (October 2026). It is grounded in the build scripts
(`<company>-equity-research/build_note.py`, `model.json`) and the notes themselves —
not a textbook. If a step here isn't visible in the scripts or notes, it isn't claimed.

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

A screener hit is only a candidate. The recurring pattern across the library: a quality
franchise **trading at a discount on a fixable or misunderstood problem** — or, on the
short side, a good business whose price already assumes perfection. Names that have run
past any defensible fair value are not chased. One-line triage applies throughout:
candidate, caution, or fails-the-screens.

---

## 2. Business analysis: moat, industry, management

Each note answers three questions in order:

1. **Is there a moat, and what kind?** Sources of advantage are named specifically —
   network effects, scale and distribution, switching costs, brand, regulatory licenses
   and concessions. Moat width is asserted with evidence (market share, retention,
   pricing power, ROIC history), never assumed from brand alone.
2. **Is the industry structure attractive?** Notes map the competitive set explicitly
   and ask whether the market is pricing a real structural threat or a
   cyclical/misunderstood one — and, for the SELLs, whether the price is ignoring a
   structural threat that is real.
3. **Can management execute?** Capital allocation track record is checked — M&A history,
   buybacks, balance-sheet discipline. Where management credibility is thin, the
   valuation demands a bigger discount. Guidance is treated as a ceiling to be
   verified, never a floor to be trusted (see §4).

---

## 3. Financial analysis: SEC filings first

The hierarchy of evidence is fixed and visible in the scripts:

- **SEC EDGAR filings first.** Company facts come from 10-K/10-Q XBRL pulls and filed
  statements. GAAP numbers anchor everything; adjusted metrics are flagged as non-GAAP
  with a pointer to company reconciliations.
- **Revenue quality:** recurring vs transactional mix, growth durability, customer and
  geographic concentration.
- **Margins:** gross/operating margin trajectory and the path to normalization. The
  terminal margin used in valuation is the *normalized mid-cycle* margin — never the
  peak. Capitalizing a one-time margin expansion as a perpetuity is explicitly
  forbidden (see §4).
- **Free cash flow:** the honesty metric. Where earnings and cash diverge —
  acquisitive names, amortization-heavy names, banks — FCF (or an owner-earnings proxy
  for lenders) is preferred over EPS, and one-time items are stripped out of the base
  year before any compounding begins.
- **Leverage:** net debt is subtracted in every DCF equity bridge and stress-tested
  against maturity walls.
- **Red flags:** aggressive accounting, deteriorating accruals, one-time gains passed
  off as earnings quality, unverifiable claims. The rule applied throughout:
  **what cannot be verified is excluded from the valuation and disclosed**, never
  quietly modeled.

---

## 4. Valuation: scenario DCF with hardened assumptions

The DCF is the anchor. Multiples are cross-checks, never the target — a target that
equals the market's multiple is a price, not a value.

**Scenario structure.** Each company is valued under three 10-year scenarios — bear,
base, bull — probability-weighted 25/50/25. The published fair value *is* the weighted
DCF. Departures require a written, falsifiable justification; "the multiple looks
cheap" is not one.

**Discount rates, per scenario:**

| Scenario | Rate |
|----------|------|
| Base — stable business | 9% |
| Base — standard | 10% |
| Base — speculative | 12% |
| Bear | base + 250bp |
| Bull | base − 150bp, floored at 8% |

The tier reflects fundamental risk (leverage, cyclicality, concentration, moat
durability), not price volatility.

**Terminal-value discipline.** Terminal growth is capped at 2.5% and applied to
normalized mid-cycle margins. If the terminal year accounts for more than 70% of
enterprise value, the model takes a haircut and discloses it.

**Bear cases must hurt.** A bear case that sits above the current price is not a bear
case. Every bear scenario is genuinely painful, sits below the quote, and gets its
full 25% weight.

**No management anchoring.** Guidance enters the model only with independent supporting
evidence, and even then at a haircut. The base case is the analyst's judgment of the
most likely path — not management's plan with a trim.

**Reverse DCF as an expectations check.** Where useful, the notes ask what growth the
current price already implies. If the quote requires 25%+ annual growth for a decade
just to break even on value, that fact is stated plainly — the burden of proof is on
the bull case, not the model.

**Sensitivity.** WACC × terminal-growth grids are shown where they illuminate how much
of the target depends on the discount assumption rather than the business.

### 4a. Compounder-quality override

Quality earns better valuation, but only through demonstrated economics — never
narrative. All three required, verified from filings, never projected:

1. ROIC above 15% for 10+ consecutive years
2. Gross margins stable or expanding (pricing-power evidence)
3. FCF conversion above 80% on average

Qualifiers get an 8–8.5% base discount, a 15-year explicit horizon, and a 3.0%
terminal cap — duration rewarded through a longer forecast, not a fatter perpetuity.
Two consecutive years of ROIC below 15% or 200bp of gross-margin contraction revokes
the override.

### 4b. International framework

Three explicit adjustments, no hand-waving:

1. **Country-risk premium** in the discount rate — China +250bp (VIE/regulatory),
   Southeast Asia +150bp, Latin America +200bp. Documented as judgment, trued up
   annually.
2. **Regional peer comps, never US peers alone.**
3. **Structural risks in the cash flows** — VIE haircuts, repatriation, currency,
   confiscation — modeled in the bear case, not footnoted.

### 4c. Hypergrowth regime

For confirmed infrastructure buildouts, years 1–3 run at or near guidance *when
backlog, lead times, or prepayments verify demand* — the framework does not haircut
guidance where evidence is strongest. Skepticism moves to supercycle duration, the
post-cycle cliff, and terminal margins. Revoked if book-to-bill drops below 1.

---

## 5. Risk-rating framework

Risk ratings in the notes are **High / Medium / Speculative** (among others) — a
qualitative judgment over the target horizon, driven by:

- **Business risk:** cyclicality, regulatory exposure, single-product or single-market
  concentration, balance-sheet leverage.
- **Thesis risk:** how much of the upside depends on one uncertain event.
- **Drawdown risk:** ratings translate into position-sizing guidance, not just labels —
  size for the drawdown scenario the rating implies.

Higher upside targets systematically pair with higher risk ratings — the rating prices
the *path*, not just the destination.

---

## 6. Verdict framework

- **BUY:** expected 10-year value materially exceeds the price with compensation for
  the rated risk; the market misprices a fixable problem or undervalues a durable
  compounder. 25 of 56 notes.
- **HOLD:** fairly valued or fairly valued *for the risk* — upside exists but is thin
  relative to uncertainty, or the price sits near fair value. 11 of 56.
- **REDUCE:** expected value below the price by a margin that no longer compensates
  the risk; trim, don't necessarily exit. 11 of 56.
- **SELL:** expected value deeply below the price — typically where the quote prices
  perfection the business cannot deliver. 9 of 56.

A verdict is always paired with a **fair value, a report-date price, an implied
upside %, a risk rating, and falsification triggers** — what would change the call.
Upside % is arithmetic on the report-date snapshot (October 2, 2026 closes), not a
live quote.

---

## 7. Limitations and biases

Stated plainly, as the notes themselves do:

- **Dated prices.** All 56 notes are priced October 2, 2026. Upsides are arithmetic on
  that snapshot, not live quotes.
- **Estimates, labeled.** Out-year forecasts are the author's estimates. Inputs that
  are estimated rather than filed are flagged in `model.json`.
- **No precision implied.** Scenario weights and terminal values are judgmental. The
  notes present ranges, sensitivities, and full bear/base/bull spreads precisely so the
  target is read as a central tendency, not a prediction.
- **The growth skepticism cuts both ways.** The framework's terminal cap and
  fade assumptions would never have captured a true outlier compounding at 20%+ for
  fifteen years. That is accepted as the price of not overpaying for the other 99 —
  and Addendum 4c exists so genuine, evidence-backed hypergrowth is modeled rather
  than defined away.
- **Survivorship and selection bias.** The idea pool comes from screens of current
  index constituents; the library tilts toward situations with a clear, arguable
  mispricing, which is itself a selection.
- **Analyst bias.** The author builds the bull case they find convincing; the
  structural defense is the bear case being modeled, weighted at 25%, and priced
  explicitly in every DCF — plus falsification triggers that hand the reader the
  exact evidence that would overturn the call.
