# FRESH Solutions Papers

Public release status: **P14 release candidate 8** (`p14-evidence-rc10`); DOI pending. The repository
contains the working manuscripts and target-journal drafts, evidence, replay scripts, and release
metadata. Sole author: Gregory Paradis, UBC FRESH Lab, University of British Columbia.

A two-paper research programme on compiled spatial optimisation, GPU hybrid metaheuristics, and
reproducible benchmark reproduction.

The programme has two outputs:

1. **Compiled spatial optimisation** — the architecture and forestry benchmark evidence.
2. **FRESH Solutions** — a general hybrid metaheuristic engine tested beyond forestry.

The general solver lives in the `fresh-solutions/` git submodule:
<https://github.com/UBC-FRESH/fresh-solutions>.

## Status

Phase 0 (bootstrap) is planned. `ROADMAP.md` lists the phases, and the GitHub issues carry the live
status.

## Research thesis

The claimed contribution is a **system architecture pattern**:

- compile the model into a stable, sparse representation;
- keep exact resident state and compact candidate/effect indexes;
- separate exact CPU moves from batched GPU population evaluation;
- use weighted goal programming with inspectable aspirations;
- replay every elite schedule against the exact evaluator.

The benchmark wins are evidence for that pattern, not the pattern itself.

## Repository map

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Operating contract for coding agents |
| `ROADMAP.md` | Plan of record and issue tracker map |
| `CHANGE_LOG.md` | Dated narrative of changes |
| `notes/design/programme.md` | Full two-paper research plan |
| `notes/reference/benchmark-corpus.md` | Literature and benchmark availability matrix |
| `notes/reports/` | Evidence and close-out reports |
| `fresh-solutions/` | General solver submodule |
| `docs/` | Documentation site |
| `scripts/check_workflow.py` | Workflow validator |

## Quick start

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m ruff check .
python -m pytest
sphinx-build -b html docs _build/html -W
python scripts/check_workflow.py
git submodule update --init --recursive
```
