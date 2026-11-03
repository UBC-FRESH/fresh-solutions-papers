# Paper 1 archive and reproduction procedure

Status: P4.4
Date: 2026-11-01

## Artifact contents

- `paper/paper1-draft.md` — evidence-constrained draft.
- `paper/tables/evidence.md` — generated table.
- `evidence/*/record.json` — schema-valid records.
- `evidence/*/schedule.csv` or `assignments.csv` — serialized schedules.
- `evidence/*/replay.py` — exact replay entry points.
- `scripts/check_benchmark_record.py` — schema/hash/exact-replay gate.
- `scripts/build_evidence_tables.py` — table generator.
- `fresh-solutions/` — solver contracts submodule.

## Reproduction

```bash
python -m pytest
python -m sphinx -W -b html docs _build/html
python scripts/check_workflow.py
python scripts/build_evidence_tables.py --evidence evidence --out paper/tables/evidence.md
for record in evidence/*/record.json; do python scripts/check_benchmark_record.py "$record"; done
```

FHOPS replay needs the pinned FHOPS checkout:

```bash
PYTHONPATH=$FHOPS_ROOT/src \
  python evidence/fhops-tiny7-sa-200-r42/replay.py
PYTHONPATH=$FHOPS_ROOT/src \
  python evidence/fhops-small21-sa-200-r42/replay.py
```

WS4 replay needs the WS4 GPU checkout:

```bash
PYTHONPATH=$WS4_GPU_ROOT \
  python evidence/ws4-tsa24-gpu-ga-1000-r7/replay.py
```

## Known archive gaps

1. TSA24 is a local reconstructable fixture, not a public dataset.
2. FHOPS commit is recorded in the records; the full dependency environment is not containerized yet.
3. The WS4 GPU checkout has uncommitted launch-optimization work; preserve the patch before publication.
4. No matched optimized landscape baseline exists.
5. No release tag yet; P5 owns the public release.
