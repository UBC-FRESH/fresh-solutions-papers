# Paper 1

Working manuscript (LaTeX): `paper1-manuscript.tex`

Compiled PDF: `paper1-manuscript.pdf` — 20 pages, 8,387 source words, 40 references, 2 figures.

Bibliography: `paper/references.bib`

Compile with `make` in `paper/` or `latexmk -pdf paper1-manuscript.tex`.

Target: **SoftwareX, Original Software Publication**. The target-specific 4,000-word draft is
`paper/submission/softwarex/paper1-softwarex.tex` (10 pages, 3,754 counted words). Fallback: **JORS**
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

- SoftwareX target draft is the current submission candidate.
- Public TSA24 artifact and public evidence capsule are available.
- The 248x factorized result is not part of the current SoftwareX manuscript.
- Still open for submission: DOI/Zenodo, tested container, and final PI approval.
