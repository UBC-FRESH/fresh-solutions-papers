# P5 close-out: release and reproducibility

Status: complete
Date: 2026-11-01
Issue: #21
Release: `paper1-evidence-v0.1.0`

## Result

The Paper 1 evidence artifact is frozen and verified from a clean checkout.

Deliverables:

- `paper/release/paper1-evidence-v0.1.0.md` — release notes and known gaps.
- `paper/release/manifest.json` — artifact and record hashes.
- `paper/release/clean-checkout.log` — clean-clone verification.
- GitHub tag/release `paper1-evidence-v0.1.0`.
- Attached source/evidence archive.

## Clean-checkout verification

- 154 tests passed.
- Sphinx `-W` passed.
- Workflow validator: 0 errors.
- All three benchmark records validated with exact replay.
- Evidence table regenerated.
- Submodule pinned to `58695d350fa5998a0e069e96e669cd3fa6870a9b`.

## Known gaps

- No matched optimized landscape baseline.
- TSA24 is a local reconstructable fixture.
- Time-to-first-feasible not separately instrumented.
- FHOPS is operational planning, not a direct architecture peer.
- Reference metadata needs final verification.
- No external peer review.

## Recommendation

The artifact is releasable as an internal evidence release. Do not submit Paper 1 until the matched-baseline
gap and reference verification are closed.
