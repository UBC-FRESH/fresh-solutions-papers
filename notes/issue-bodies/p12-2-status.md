# P12.2 status

The first P0 correction pass is complete and pushed to PR #77.

Corrected:

- Paper 1: non-separable even-flow delta identity; GPU-only 100k evidence wording; wall time
  3,995.906 s; realized level 51.21-52.49M; level term 499.8-517.3; CPU commit/31.25-minute wording;
  artifact size 4.66 MB; public-release wording for schedules/replay.
- Paper 2: 10k `tai25a` mean 0.786; 25 `esc8` parse-error records; 20-kick pilot 15/20 optima;
  TSP actual kicks 1,000-1,380 under a 10,000 cap; Or-opt labels replaced by generic local-search
  starts; spatial-adapter claims removed; QAP convergence/framework row merged; Apache-2.0 license
  statement corrected; campaign-level provenance sidecar added.
- Paper 2 now has 42 references and 19 pages / 8,153 source words.

Still blocked / not done:

- Public release and license for the paper-specific evidence.
- Per-record evidence schema and validator.
- Broad runner/summary reconciliation and broad replay.
- Paper 1 architecture ablation and matched CPU-GA.
- Third-party adapter or portability experiment.
- Journal-specific formatting, figures, and Paper 1 reference expansion.

No tag, release, visibility change, or submission action.
