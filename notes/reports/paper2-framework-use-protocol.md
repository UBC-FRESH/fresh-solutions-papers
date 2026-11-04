# Paper 2 framework-use protocol

Status: P12.1 protocol, fixed before the final run
Date: 2026-11-03
Issue: #76

## Why this protocol exists

The first pilot used a fixed 10,000-iteration QAP budget and five seeds. That is a certification-style
check, not a per-run convergence test, and it is too weak for a Q1 framework-use claim. The first
generic-engine pilot also used a fixed 100,000-iteration simulated-annealing budget. Both are
internal pilots only and do not enter a paper table.

## Final comparison

The framework-use experiment compares two implementations of the same QAP robust-tabu trajectory:

1. **Standalone delta-matrix path**: the private-array `qap_tabu._run_accelerated` loop.
2. **Framework-managed path**: the same scan and tabu memory, but the incumbent is held in
   `ResidentAssignment` and every accepted move goes through adapter `apply` and exact `evaluate`.

The production `run_qap_tabu` path is also run to verify that the Numba-accelerated production path
finds the same objective.

## Instances and seeds

- `tai12a` (n=12, known optimum 224,416)
- `tai20a` (n=20, known optimum 703,482)
- `tai25a` (n=25, known optimum 1,167,256)
- `tai30a` (n=30, best known 1,818,146)
- Seeds 1 through 10 inclusive.

## Stopping rule

- Maximum budget: 1,000,000 tabu iterations.
- Per-run patience: 50,000 iterations without a new best objective.
- A run is **converged for this evidence** only when `stop_reason == "patience"`. This is a declared
  plateau rule, not a proof of global optimality.
- A run that reaches the maximum is reported as `max_iterations` and counted as non-converged.
- The paper must say “plateau-stopped” or “converged for this evidence”, never “proved optimal”.
- The two paths must report the same stop reason and iteration count; otherwise the comparison is
  invalid.

This is a stronger test than the earlier fixed 10k/20k/40k certification ladder. The 50,000-iteration
patience is five times the earlier broad-panel patience of 10,000 and is longer than the certified
80,000-iteration `tai30a` budget in stagnation length.

## Longer-patience sensitivity check

After the main campaign, run three seeds per instance with patience 100,000. If any objective differs
from the 50,000-patience result, the 50,000 evidence is not convergence-stable and the paper must use
the longer budget. The sensitivity check is recorded separately, not silently pooled.

## Reported quantities

- Per-run objective and optimality gap.
- Per-run stop reason and iteration count.
- Wall time for the standalone path, framework path, and production path.
- Framework wall-time ratio against the standalone pure-Python path.
- Exact replay through `QuadraticAssignment.evaluate`.
- Mean, median, best, and worst gap; all-patience and all-replay flags.
- Every cap hit and quality mismatch.

## TSP boundary

The TSP check in this experiment is an **exact-replay contract check** over the existing 20 recorded
ILK incumbents. It is not a new TSP convergence campaign and must not be described as one. A separate
TSP convergence experiment is required before any framework claim about TSP search.

## Prohibited claims

- “Converged” for a `max_iterations` stop.
- “Same quality” if any seed differs.
- “Low overhead” without the measured ratio and instance sizes.
- “Framework experiment” for the TSP replay-only check.
- State-of-the-art QAP performance.
