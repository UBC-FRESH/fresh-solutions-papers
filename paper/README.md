# Paper 1

Working manuscript: `paper1-manuscript.md`

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
