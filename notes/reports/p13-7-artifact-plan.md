# P13.7 artifact and release plan

Status: prepared, approval-gated
Date: 2026-11-09
Issue: #88

## What exists

- `paper/evidence/` — factorized CPU/GPU ablation records.
- `paper2/evidence/` — framework-use, QAP expanded, BLS (5 and 10 seed), generic-tabu,
  TSP deep and expanded panels, broad panel, LKH provenance.
- `paper/release/manifest-v0.2.0-candidate.json`
- `paper2/evidence/manifest-v0.1.0-candidate.json`
- `paper/replay_all.sh`
- `paper2/replay_all.sh`
- `container/Dockerfile` and `container/requirements-evidence.txt`

## Evidence validation

`bash paper2/replay_all.sh` passes:

- 40 QAP framework incumbents exact.
- 20 TSP deep-panel incumbents exact.
- 1,085 broad records and 7 summary rows validated.
- 20 large-QAP records exact.
- 100 BLS records exact.
- 40 generic-tabu records exact.
- 5/100 expanded-TSP cap hits reported as cap hits, not convergence.

## Per-record schema

Convergence records carry solver commit, seed, budget, stop reason, objective, assignment,
exact-replay status, and wall/CPU time where measured. Broad records carry campaign-level solver
commit and provenance but not CPU/hardware per row. The campaign provenance sidecar is
`paper2/evidence/provenance-2026-11-03.json`.

Known gap: per-record CPU time and hardware are not uniform. The manuscript says so. This remains a
release blocker for a "complete schema" claim.

## Release assets

- source archive with both manuscripts, figures, references, runners, replay scripts, and evidence;
- PDFs;
- `LICENSE`, `LICENSING.md`;
- public TSA24 artifact reference;
- container recipe (untested in this session);
- SHA-256 manifests.

## Approval-gated commands

Repository visibility:

```bash
gh repo edit UBC-FRESH/fresh-solutions-papers --visibility public
```

Paper 1 release:

```bash
gh release create paper1-evidence-v0.3.0 \
  --repo UBC-FRESH/fresh-solutions-papers \
  --title "Paper 1 evidence v0.3.0" \
  --notes-file paper/release/paper1-evidence-v0.1.0.md
```

Paper 2 release:

```bash
gh release create paper2-evidence-v0.2.0 \
  --repo UBC-FRESH/fresh-solutions-papers \
  --title "Paper 2 evidence v0.2.0" \
  --notes-file notes/reports/evidence-release-candidates.md
```

A DOI via Zenodo requires an external account/release action; not performed.

## Container

The Dockerfile clones Fresh Solutions at `7d3c831`, installs evidence dependencies, and runs
`paper2/replay_all.sh`. Docker/Apptainer is not installed in this session, so the image is **untested**.

## Gate

No visibility change, tag, release, DOI, or submission until the PI approves each named action.
