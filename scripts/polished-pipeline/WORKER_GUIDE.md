# Polished-notes rebuild — worker guide

7 workers × 8 notes each. All output is research analysis, not investment advice.

## Files here
- `template.py` — the ONLY way to build a note. `from template import build_note, validate`.
  Full data-dict schema is documented in its module docstring. Run `validate(data)`
  mentally via `build_note` — it raises on missing keys AND on banned language.
- `library.json` — authoritative per-name record: ticker, company, verdict,
  fair_value, price, risk_rating (null = assign from substance), data_sources,
  and per-name notes (stale-source warnings).
- `sources/` — durable PDF sources: `standalone/` (all 56, thin 4-page),
  `batch2/` (9 rich originals), `batch3/` (11 rich originals),
  `addendum_c/` (6 rich Addendum-C notes, authoritative for those names).
- `samples/WYNN-equity-research-note-polished.pdf` — the verified reference build.
- `build_sample_wynn.py` — how a worker script assembles `data` and calls `build_note`.

## Rules (non-negotiable)
1. Verdict / fair value / price in `library.json` are FINAL. Reproduce exactly.
2. No version labels in ANY output text: "v2", "addendum", "rebuild", "old note",
   "prior target", "previous note" are banned — `validate()` will raise.
   Every note reads as a fresh October 4, 2026 analyst note. Rewrite, don't copy,
   any source sentence that references report history.
3. Charts render ACTUAL numbers from `data` only. Never invent a series.
   If a chart input is missing, omit that chart (composition/trajectory/scenario
   are required — so go find the numbers; extra is optional).
4. `risk_rating` null in library.json → assign Low/Medium/Medium-High/High from
   the note's substance (leverage × cyclicality × valuation).
5. Historical financials for the trajectory chart: pull via yfinance
   (`Ticker(...).financials` / `.cashflow`, annual columns) or EDGAR when the
   name's JSON lacks history. Record what you substituted in your report.
6. Output path: `~/workspace/polished-notes/output/<TICKER>-equity-research-note-polished.pdf`
   (create `output/` when you start). Re-run `build_sample_wynn.py`-style scripts
   are re-runnable by design — keep your per-name build script next to the PDF.

## Data-source priority per name (see library.json `data_sources` + `notes`)
- 6 Addendum-C names (NVDA, AMD, AVGO, LITE, ARM, APH): the `addendum_c/` PDF is
  authoritative (rich, current FVs). Their `standalone/` PDFs are STALE — do not
  mine numbers from them. NVDA/AMD also have `model.json` + `model_addendum_c.py`
  with full scenario series.
- Names with `valuation_output_json`: mine scenario FVs, discounts, cash-flow
  series from there (schemas vary: `dcf_bear/base/bull`, `base/bull/bear`, or
  `dcf_10y` — inspect before mapping).
- Names with NO model/valuation JSON (27 names — listed in the parent report):
  mine scenario numbers from the `standalone/` PDF valuation section and prose
  from standalone + batch2/batch3 where available; history via yfinance.
- JD: batch3 PDF shows an older $65 target — authoritative FV is $55.

## Bar per note (matches the verified WYNN sample)
≥6 pages, 4 chart images embedded, verdict banner + cover table exact,
8 sections (thesis / business / outlook / financials / moat / valuation /
risks+falsification / methodology+disclaimer), page numbers + running head,
present-tense methodology, disclaimer footer.
