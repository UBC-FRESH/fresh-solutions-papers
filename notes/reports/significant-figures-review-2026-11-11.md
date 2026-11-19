# Significant-figures review — 2026-11-11

Scope: Paper 1, Paper 2, tables, figure captions, and the EMS/JoH submission variants.

## Rule applied

Full precision remains in the evidence files. The manuscripts use:

- counts, seeds, budgets, iterations, blocks, runs: exact integers;
- optimality gaps: three decimal places in percentage points;
- exact campaign objectives and flow/level terms: six significant figures;
- screen and one-seed diagnostic objectives: three significant figures;
- times, ratios, and CPU overheads: three significant figures;
- p-values/residual exactness checks: two significant figures in scientific notation.

The rule is stated in each manuscript's methods/evidence-protocol section.

## Paper 1 changes

- Replaced 15-digit objectives and times with six-significant-figure campaign values and
  three-significant-figure timings, e.g. `1,722,140,000`, `8,588,730`, `76,540.7`, `517.862`,
  `9.38 s / 23.1 s`, `89.8 s / 157 s`, `856 s / 942 s`.
- CPU-SA comparator: `3.35045e8`, `1.88e3 s`, `31.3 min`.
- Evaluation-path ablation: `54.9 s`, `1.09 s`, `0.542 ms`, `2.00e3` factor, residual `3.7e-9`.
- Factorized batch: `23.1 s`, `0.0931 s`, `2.77`/`687` genomes/s, `1.71e-6`, `234 s`, `9.27 GB`.
- Matched search: `529 s` vs `23.9 s`, `22.2` ratio, `5%` objective difference, three-significant
  figure objectives.
- Target-variant screen: three-significant-figure objectives (`1.71e9` ... `1.01e3`).
- Figure cleanup from the concurrent Paper 1 commit preserved: three figures (architecture, scaling,
  matched search). Captions use the same rounded values as the text.

## Paper 2 changes

- Gaps remain at three decimal places; broad-panel worst gap changed from `36.4%` to `36.400%`.
- SciPy baseline changed to `25.440%`, `2.550%`, `246.340%`.
- Framework CPU overhead changed to `1.24` with CI `1.17--1.31`; per-instance ratios `1.17--1.33`.
- QAP mean wall times changed to `754`, `605`, `688`, `604` s.
- Applied TSA24 values changed to `8,588,730`, `76,540.7`, `3.35045e8`, `1.88e3 s`.
- Figures remain five; axes use full data, captions quote the text/table-rounded values.

## Verification

- Main PDFs: Paper 1 **21 pages, 8,574 words, 3 figures**; Paper 2 **24 pages, 9,357 words, 5 figures**.
- Journal variants: EMS **29 pages**; JoH **28 pages**.
- `pdftotext` checks find no stale long-precision values in either main PDF.
- `paper/release/manifest-v0.2.0-candidate.json` and
  `paper2/evidence/manifest-v0.1.0-candidate.json` hashes match.
- Local dashboard green.

Full-precision values are retained in the evidence; the papers report rounded values only.
