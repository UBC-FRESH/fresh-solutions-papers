# Paper 2 evidence release candidate

Status: public release candidate `p14-evidence-rc7`; DOI pending.

## Verification

- `bash paper2/replay_all.sh` under `QAPLIB_ROOT`/`TSPLIB_ROOT`:
  deep, expanded, broad, BLS, and generic-tabu incumbents replay exactly.
- `paper2/evidence/manifest-v0.1.0-candidate.json` hashes match.
- 25 `esc8` parse-error records are skipped, not counted as evidence.
- Five `brazil58` cap hits are reported as cap hits.

## Assets

- `paper2/paper2-manuscript.pdf`
- `paper2/paper2-manuscript.tex`
- `paper2/figures/`
- `paper2/references.bib`
- `paper2/evidence/`
- `paper2/*.py` runners and replay scripts
- `paper2/submission/paper2-sn-jnl.tex` (JoH variant)

## Approval-gated actions

Visibility, tag, release, DOI, merge, and submission require explicit PI approval.
