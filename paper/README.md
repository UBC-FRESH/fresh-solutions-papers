# Paper 1

Working manuscript (LaTeX): `paper1-manuscript.tex`

Markdown working copy: `paper1-manuscript.md`

Bibliography: `paper/references.bib`

Compile with `pdflatex`/`bibtex` twice; the target journal class is not yet applied.

Draft: `paper1-draft.md`

Evidence table: `paper/tables/evidence.md`

Regenerate the table:

```bash
python scripts/build_evidence_tables.py --evidence evidence --out paper/tables/evidence.md
```

Validate every record:

```bash
for record in evidence/*/record.json; do python scripts/check_benchmark_record.py "$record"; done
```

The draft is evidence-constrained. Do not add a claim that is not backed by a schema-valid, exactly
replayed record.
