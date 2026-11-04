# Autonomous remediation closeout

Status: non-gated remediation completed; approval-gated items remain
Date: 2026-11-03
Branch: `feature/p12-paper2-q1`
PR: #77

## Completed

### Paper 1

- Replaced the false cell-separable delta with the target-level/period-vector identity.
- Removed the unsupported CPU-refinement claim from the 100k evidence.
- Corrected campaign wall, realized level, level-term range, CPU limit/commit, artifact size, and
  public-release wording.
- Added 40 references, 5 figures (4 evidence figures plus architecture), keywords, and a 20-page,
  8,014-word manuscript.
- Added the Lockwood correction: **Carey Lockwood and Tom Moore**.
- Added `LICENSE`, `LICENSING.md`, and `paper/replay_all.sh`.

### Paper 2

- Added the 20-instance expanded QAP panel: 100/100 patience stops, 100/100 exact replays, mean
  0.274%, worst 1.583%, 37/100 optima.
- Added SciPy FAQ on the same panel: mean 25.44%, median 2.55%, worst 246.34%.
- Added 5 figures, 42 references, keywords, and a 22-page, 8,544-word manuscript.
- Added the evidence validator, canonical broad summary, campaign provenance sidecar, and
  convergence-record stamping.
- Corrected the 10k `tai25a` value, `esc8` count, 20-kick wording, TSP kick-cap label, Or-opt labels,
  spatial-adapter claims, QAP double count, and license/availability statements.
- Added `replay_all.sh`, container recipe, and approval-gate report.

## Not completed / explicitly blocked

- **20-instance expanded TSP panel**: attempted at 10k, 2k, and 500 kicks; the last tasks became
  pathologically slow. No final file is claimed. The paper uses the four-instance 10k convergence
  panel plus the 78-instance broad panel, and does not claim a 20-instance TSP convergence panel.
- **Public evidence release and license/visibility**: requires explicit maintainer approval.
- **Merge of PR #77**: requires phase-closeout approval.
- **Paper 1 architecture ablation / matched CPU-GA**: not run; the paper explicitly removes the
  causal speed claim and reports the diagnostic subset only.
- **Third-party adapter / portability experiment**: not done; the paper removes the false third-adapter
  claim and states the gap.

## Current manuscript state

- Paper 1: 20 pages, 8,014 source words, 40 references, 5 figures; builds clean.
- Paper 2: 22 pages, 8,544 source words, 42 references, 5 figures; builds clean.
- `paper2/check_evidence.py`: passes, replays 40 QAP + 20 TSP convergence incumbents and checks
  the 20-instance QAP panel, broad records, and summary.
- Dashboard: green.
- PR #77: green, mergeable, not merged.

## Honest verdict

Both papers are substantially stronger than at the start of the audit, but neither is submission-ready.
Paper 1 remains limited by the missing matched architecture/CPU experiment and the private paper-specific
evidence. Paper 2 remains limited by the TSP panel breadth, the lack of a published QAP baseline, the
uneven per-record metadata, and the private evidence release. The approval-gated release is the remaining
external dependency.
