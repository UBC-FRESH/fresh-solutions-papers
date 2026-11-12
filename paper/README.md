# Paper 1

Working manuscript (LaTeX): `paper1-manuscript.tex`

Compiled PDF: `paper1-manuscript.pdf` — 20 pages, 8,387 source words, 40 references, 2 figures.

Bibliography: `paper/references.bib`

Compile with `make` in `paper/` or `latexmk -pdf paper1-manuscript.tex`.

Target: **SoftwareX, Original Software Publication**. The target-specific 4,000-word draft is
`paper/submission/softwarex/paper1-softwarex.tex` (10 pages, 3,977 counted words). Fallback: **JORS**
after a further cut. EMS is not a target for the current draft; it would require a new environmental
validation and a second landscape/spatial case.

Evidence table: `paper/tables/evidence.md`

Regenerate the figures:

```bash
python paper/make_figures.py
```

Regenerate the table:

```bash
python scripts/build_evidence_tables.py --evidence evidence --out paper/tables/evidence.md
```

Validate every record:

```bash
for record in evidence/*/record.json; do python scripts/check_benchmark_record.py "$record"; done
```

Current status:

- Claim corrections: non-separable even-flow delta, GPU-only 100k evidence wording, and stale numbers.
- Factorized batch ablation: CPU 23.124 s vs CUDA 0.0931 s (248x) for 64 genomes, max error 1.7e-6; batch only, not end-to-end search.
- Public TSA24 artifact: available.
- Paper-specific schedules and replay scripts: retained in the project evidence repository; public
  release remains pending approval.
- Still open for submission: matched architecture ablation or explicit software-paper reframe,
  matched CPU-GA/CPU-SA, EMS formatting, and final claim audit.
