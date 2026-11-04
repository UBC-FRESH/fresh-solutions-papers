# Paper 1

Working manuscript (LaTeX): `paper1-manuscript.tex`

Compiled PDF: `paper1-manuscript.pdf` — 20 pages, 8,014 source words, 40 references, 5 figures.

Bibliography: `paper/references.bib`

Compile with `make` in `paper/` or `latexmk -pdf paper1-manuscript.tex`.

Target: **Environmental Modelling & Software**, as an architecture/reproducibility paper. The
`elsarticle` class and journal-specific author metadata are not yet applied. Fallback: SoftwareX/JORS
only if the paper is intentionally a tool/software paper. CJFR/Forest Science are not recommended
without a real spatial/forestry experiment.

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
- Public TSA24 artifact: available.
- Paper-specific schedules and replay scripts: retained in the project evidence repository; public
  release remains pending approval.
- Still open for submission: matched architecture ablation or explicit software-paper reframe,
  matched CPU-GA/CPU-SA, EMS formatting, and final claim audit.
