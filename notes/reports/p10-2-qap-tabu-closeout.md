# P10.2 close-out: QAP competitive neighborhood

Status: complete
Date: 2026-11-01
Issue: #33
Solver pin: Fresh Solutions `v0.4.0` (`260e789`)

## Recommendation

Close P10.2. QAP now has a competitive neighborhood with a certified budget ladder and exact replay.
This is not a global-optimality claim.

## Acceptance

- QAP mean gap improves materially against the 5–9% swap plateau: **met**.
- Every reported assignment replays exactly: **met** (20/20).
- Reproducible from a pinned release: **met** (`v0.4.0`).

## Certified evidence

The selected budget is the smallest budget whose next doubling improves the five-seed mean gap by
≤0.10 percentage points, or where every seed reaches the known optimum.

| Instance | Certified budget | Mean gap | Median gap | Worst gap | Larger check | Larger mean |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| tai12a | 10,000 | 0.000% | 0.000% | 0.000% | optimum on all seeds | — |
| tai20a | 10,000 | 0.403% | 0.470% | 0.470% | 20,000 | 0.370% |
| tai25a | 20,000 | 0.685% | 0.850% | 0.850% | 40,000 | 0.592% |
| tai30a | 40,000 | 0.407% | 0.407% | 0.678% | 80,000 | 0.348% |

Budget-ladder details:

- `tai25a`: 10k→20k improved by 0.102 points, so 10k was not certified; 20k→40k improved by
  0.092 points, so 20k is certified.
- `tai30a`: 20k→40k improved by 0.293 points, so 20k was not certified; 40k→80k improved by
  0.059 points, so 40k is certified.

The larger-budget values are retained in evidence but are not substituted into the headline table.

## Independent baseline

SciPy `quadratic_assignment` (`method="faq"`, `maxiter=10000`, SciPy 1.18.1) was run on the same
instances and five seeds. It is an independent implementation, but the budget is **not** equivalent to
tabu iterations.

| Instance | SciPy FAQ mean gap | Tabu mean gap | SciPy mean wall (s) | Tabu mean wall (s) |
| --- | ---: | ---: | ---: | ---: |
| tai12a | 9.026% | 0.000% | 0.001 | 2.21 |
| tai20a | 4.642% | 0.403% | 0.002 | 10.21 |
| tai25a | 4.474% | 0.685% | 0.003 | 39.98 |
| tai30a | 2.289% | 0.407% | 0.005 | 138.84 |

The baseline is much faster and much worse in quality. The comparison supports a quality claim at a
stated time cost, not a claim of dominating every solver on every budget. SciPy FAQ returned the same
assignment on all five seeds for each instance, so its five-seed spread is zero.

## Replay

`PYTHONPATH=fresh-solutions python paper2/replay_qap_tabu.py --input qap-tabu-converged.json`

`PYTHONPATH=fresh-solutions python paper2/replay_qap_tabu.py --input qap-scipy-faq.json`

Result: **20/20 tabu replays and 20/20 baseline replays exact**.

## Evidence files

- `paper2/evidence/qap-tabu.json` — 10k per-run records
- `paper2/evidence/qap-tabu-20k.json` — 20k records
- `paper2/evidence/qap-tabu-40k.json` — 40k records for tai25a/tai30a
- `paper2/evidence/qap-tabu-80k.json` — 80k records for tai30a
- `paper2/evidence/qap-tabu-converged.json` — certified per-run records
- `paper2/evidence/qap-tabu-converged-summary.json` — certified summary
- `paper2/evidence/qap-tabu-*-stability-summary.json` — doubling checks

## Limits

- Robust tabu is a QAP-specific adapter module, not a generic engine change.
- The certification rule checks one doubling; it is a stopping rule, not a convergence proof.
- The independent baseline is not budget-matched; it is a time-quality comparison.
- These results do not establish state-of-the-art QAP performance.
