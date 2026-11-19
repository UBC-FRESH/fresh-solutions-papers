# Paper 2 evidence release candidate

Status: public release candidate `p14-evidence-rc20`; DOI pending.

## Verification

- `bash paper2/replay_all.sh` under `QAPLIB_ROOT`/`TSPLIB_ROOT`:
  deep, expanded, broad, BLS, and generic-tabu incumbents replay exactly.
- `paper2/evidence/manifest-v0.1.0-candidate.json` hashes match.
- 25 `esc8` parse-error records are skipped, not counted as evidence.
- Five `brazil58` cap hits are reported as cap hits.

## Assets

- `paper2/submission/jors/paper2-jors.pdf`
- `paper2/submission/jors/paper2-jors.tex`
- `paper2/submission/jors/paper2-jors-supplement.pdf`
- `paper2/evidence/`
- `paper2/*.py` runners and replay scripts
- `paper2/submission/jors/paper2-jors-supplement.tex`
- `paper2/submission/jors/README.md`, `cover-letter.md`

## Approval-gated actions

Visibility, tag, release, DOI, merge, and submission require explicit PI approval.
