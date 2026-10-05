# Build scripts — equity research notes

Every script used to build the 56-note equity research library (October 2026).
Regenerating a note is: `python build_<TICKER>.py` (polished pipeline) or
`python build_note.py` inside a per-note directory.

## What's here

- **`per-note/`** — the original per-note builders: `build_note.py` + `model.json`
  (+ `model_addendum_c.*` where the hypergrowth regime applied, `valuation_model.py`
  / `make_charts.py` for the oldest notes). 17 directories. `model.json` holds every
  valuation input — scenario growth rates, margins, discount rates, share counts.
- **`polished-pipeline/`** — the final rebuild that produced the 56 polished PDFs:
  `template.py` (shared house style + standalone-rule validator), `library.json`
  (authoritative 56-name record: verdicts, targets, scenarios), `build_<TICKER>.py`
  (56 per-note builders), `WORKER_GUIDE.md` (build spec).
- **`standalone-pipeline/`** — `build_w1.py` … `build_w7.py`, the intermediate
  standalone rebuild (superseded by the polished pipeline, kept for the record).
- **`valuation/`** — `VALUATION_REBUILD_V2_REPORT.md` (the v2 rebuild report),
  `wynn_dcf.py` (worked 10-year FCFE example), `build_master_pdf.py` (addenda
  master-PDF builder).
- **`research-valuations-scripts/`** — `build_workbook.py` and related scripts
  behind `research-valuations/valuations.xlsx`.

## Dependencies

reportlab, matplotlib, pypdf, yfinance, pandas, numpy.

```bash
pip install reportlab matplotlib pypdf yfinance pandas numpy
python polished-pipeline/build_NVDA.py   # → regenerates the NVDA note PDF
```

Research analysis, not investment advice.
