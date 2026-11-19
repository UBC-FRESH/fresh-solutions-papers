# P13.2 independent QAP baseline: Breakout Local Search

Status: complete, evidence committed
Date: 2026-11-08
Issue: #83
Branch: `feature/p13-publication-hardening`

## Summary

This task replaces the weak SciPy FAQ comparison with an independent
Breakout Local Search (BLS) baseline in the style of Benlic and Hao (2013). The
baseline runs on the same 20-instance QAPLIB panel, the same five seeds, and the
same declared move cap and patience as the robust tabu panel. All 100 runs
stopped on patience, no run hit the cap, and all 100 incumbents replay exactly
through the QAP adapter.

The baseline is credible rather than a straw man: it reaches the known optimum
on 76 of 100 runs and its five-seed mean gap is 0.116% overall. The comparison
with robust tabu is reported descriptively below; this note does **not** claim
state-of-the-art performance or that BLS beats robust tabu.

## Inputs read

- `AGENTS.md`
- `notes/plans/p13-publication-hardening-2026-11-08.md`
- `notes/issue-bodies/p13/02-qap-baseline.md`
- `notes/reports/serious-budget-policy.md`
- `paper2/run_qap_expanded.py`
- `fresh-solutions/fresh_solutions/adapters/qap.py`
- `fresh-solutions/fresh_solutions/adapters/qap_tabu.py`
- `paper2/evidence/qap-expanded-100k.json`
- `paper2/evidence/qap-expanded-100k-summary.json`
- Benlic, U., and Hao, J.-K. (2013), *Breakout Local Search for the quadratic
  assignment problem*, Applied Mathematics and Computation 219(9), 4800-4815
  (algorithm and parameter table).

## Implementation

Algorithm: `paper2/qap_bls.py`.

BLS alternates a best-improvement swap descent with an adaptive perturbation:

1. Descend to a local optimum with the best improving swap.
2. If the local optimum is a new best, reset the non-improvement counter
   `omega`; otherwise increment it when the local optimum differs from the
   previous one.
3. Set the jump magnitude `L`: reset to `L0` after escaping to a different local
   optimum, increment by one when the search returns to the same local optimum,
   and set to `LMax` after `T` consecutive non-improving local optima.
4. Apply `L` perturbation moves. The perturbation type is chosen from the
   published probabilities: directed (tabu-guided least-degrading swap),
   recency-based (least recently applied swap), or random. The directed tabu is
   on moves, not positions, and the tabu list is updated during descent too.
5. Repeat until the move cap or the non-improving move patience fires.

Parameter values follow the published defaults, with the instance-family
`L0` split:

| Parameter | Value used |
| --- | --- |
| `L0` | `0.05 n` for `tai` (type II); `0.15 n` for `bur` (type I) and `chr` (type III), floor of 2 |
| `LMax` | `rand[0.4 n, 0.6 n]`, drawn once per run from the seed |
| `T` | 2500 |
| `gamma` (move tenure) | `rand[0.9 n, 1.1 n]` per directed step |
| `P0` | 0.75 |
| `Q` | 0.7 |

Exactness. The gain matrix is initialised with the exact O(n) swap-delta
formula. Symmetric zero-diagonal instances use Taillard's O(n^2) update.
The `bur` family is asymmetric with a non-zero diagonal, so it uses an exact
O(n^2) correction for pairs outside the swapped pair; this path was checked by
random-walk comparison against exact re-evaluation before the panel. Every run
also re-evaluates the incumbent through `QuadraticAssignment.evaluate` and
raises if the delta-tracked objective disagrees.

The module keeps an exact pure-Python reference path for audit without Numba.
The committed evidence uses the Numba path (`engine: "numba"`).

## Panel and budget

- Instances: the same 20 names as `paper2/run_qap_expanded.py:INSTANCES`.
- Seeds: `1,2,3,4,5`.
- Start: the adapter's identity assignment, matching the robust tabu panel.
- Cap: 1,000,000 applied swaps (declared; no wall-clock cap).
- Patience: 100,000 applied swaps without a new best.
- A cap hit is reported as `max_moves` and is not called convergence.
- Hardware: Intel Xeon Gold 6254, 36 physical cores / 72 threads; 40 worker
  processes. Python 3.12.3, numpy 2.5.4, numba 0.68.0. CPU only; the GPU was
  not used.
- Unit of budget: one applied swap. Robust tabu counts one accepted move per
  iteration, so the move budgets are comparable. Mean applied moves were
  128,004 for BLS and 125,056 for robust tabu.

## Exact commands

```bash
export QAPLIB_ROOT=/path/to/QAPLIB
python paper2/run_qap_bls.py --no-resume --workers 40 \
  --moves 1000000 --patience 100000
```

The runner checkpoints every completed run in
`runtime/qap-bls-expanded.checkpoint.jsonl` and writes
`paper2/evidence/qap-bls-expanded.json` and
`paper2/evidence/qap-bls-expanded-summary.json`.

Replay:

```bash
export QAPLIB_ROOT=/path/to/QAPLIB
python paper2/replay_qap_bls.py
# 100/100 exact replays
```

Lint and format:

```bash
python -m ruff check paper2/qap_bls.py paper2/run_qap_bls.py \
  paper2/replay_qap_bls.py
python -m ruff format --check paper2/qap_bls.py paper2/run_qap_bls.py \
  paper2/replay_qap_bls.py
```

## Stop reasons and budget consumption

- `patience`: 100/100 runs.
- `max_moves` (cap hits): 0/100.
- Applied moves: minimum 100,056; median 113,713; maximum 322,705.
- Mean candidate evaluations: 48.3 million per run.
- Mean local optima visited: 20,893 (range 10,746 to 63,865).
- Strong perturbations: mean 2.93 per run (maximum 9).
- Perturbation mix over the panel: 79.8% directed, 14.1% recency-based, 6.1%
  random.
- Wall time: 11.5 s for the whole campaign on 40 workers; 217.6 s summed
  per-run wall time. Mean 2.18 s per run, maximum 8.88 s.
- CPU time: 215.4 s summed per-run process time.

No run is a screen: every run used the declared serious cap and patience.

## Gap distribution

| Instance | n | Type | Mean gap | Median gap | Worst gap | Optima | Stopped | Mean moves | Mean wall (s) |
| --- | ---: | :---: | ---: | ---: | ---: | ---: | :---: | ---: | ---: |
| tai12a | 12 | II | 0.000% | 0.000% | 0.000% | 5/5 | 5P/0C | 100,397 | 0.40 |
| tai20a | 20 | II | 0.000% | 0.000% | 0.000% | 5/5 | 5P/0C | 143,551 | 1.34 |
| tai25a | 25 | II | 0.000% | 0.000% | 0.000% | 5/5 | 5P/0C | 120,236 | 1.69 |
| tai30a | 30 | II | 0.157% | 0.000% | 0.391% | 3/5 | 5P/0C | 182,575 | 3.66 |
| tai35a | 35 | II | 0.403% | 0.320% | 0.649% | 0/5 | 5P/0C | 143,604 | 3.91 |
| tai40a | 40 | II | 0.389% | 0.375% | 0.644% | 0/5 | 5P/0C | 189,083 | 5.92 |
| tai50a | 50 | II | 0.756% | 0.724% | 1.013% | 0/5 | 5P/0C | 153,858 | 7.10 |
| bur26a | 26 | I | 0.000% | 0.000% | 0.000% | 5/5 | 5P/0C | 115,576 | 1.99 |
| bur26b | 26 | I | 0.000% | 0.000% | 0.000% | 5/5 | 5P/0C | 124,885 | 2.19 |
| bur26c | 26 | I | 0.000% | 0.000% | 0.000% | 5/5 | 5P/0C | 115,349 | 1.97 |
| bur26d | 26 | I | 0.000% | 0.000% | 0.000% | 5/5 | 5P/0C | 122,170 | 2.06 |
| bur26e | 26 | I | 0.000% | 0.000% | 0.000% | 5/5 | 5P/0C | 109,232 | 1.91 |
| bur26f | 26 | I | 0.000% | 0.000% | 0.000% | 5/5 | 5P/0C | 115,188 | 1.89 |
| bur26g | 26 | I | 0.000% | 0.000% | 0.000% | 5/5 | 5P/0C | 106,462 | 1.79 |
| bur26h | 26 | I | 0.000% | 0.000% | 0.000% | 5/5 | 5P/0C | 106,503 | 1.59 |
| chr12a | 12 | III | 0.000% | 0.000% | 0.000% | 5/5 | 5P/0C | 102,649 | 0.30 |
| chr15a | 15 | III | 0.000% | 0.000% | 0.000% | 5/5 | 5P/0C | 102,782 | 0.45 |
| chr18a | 18 | III | 0.000% | 0.000% | 0.000% | 5/5 | 5P/0C | 102,047 | 0.78 |
| chr20a | 20 | III | 0.420% | 0.182% | 1.369% | 0/5 | 5P/0C | 148,910 | 1.15 |
| chr22a | 22 | III | 0.188% | 0.000% | 0.617% | 3/5 | 5P/0C | 155,029 | 1.43 |

`5P/0C` means five patience stops and zero cap hits.

Overall over all 100 runs: mean gap 0.116%, median 0.000%, worst 1.369%,
76/100 known optima.

## Comparison with robust tabu

Reference: `paper2/evidence/qap-expanded-100k-summary.json` (same 20 instances,
seeds, cap, patience, and identity start). Tabu mean is the five-seed mean gap.
A negative delta means the BLS mean gap is lower.

| Instance | n | Tabu mean | BLS mean | Delta | Tabu worst | BLS worst | Tabu optima | BLS optima |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| tai12a | 12 | 0.000% | 0.000% | +0.000 | 0.000% | 0.000% | 5/5 | 5/5 |
| tai20a | 20 | 0.000% | 0.000% | +0.000 | 0.000% | 0.000% | 5/5 | 5/5 |
| tai25a | 25 | 0.073% | 0.000% | -0.073 | 0.366% | 0.000% | 4/5 | 5/5 |
| tai30a | 30 | 0.313% | 0.157% | -0.157 | 0.391% | 0.391% | 1/5 | 3/5 |
| tai35a | 35 | 0.664% | 0.403% | -0.261 | 1.051% | 0.649% | 0/5 | 0/5 |
| tai40a | 40 | 0.831% | 0.389% | -0.442 | 1.045% | 0.644% | 0/5 | 0/5 |
| tai50a | 50 | 1.264% | 0.756% | -0.508 | 1.583% | 1.013% | 0/5 | 0/5 |
| bur26a | 26 | 0.135% | 0.000% | -0.135 | 0.147% | 0.000% | 0/5 | 5/5 |
| bur26b | 26 | 0.565% | 0.000% | -0.565 | 0.565% | 0.000% | 0/5 | 5/5 |
| bur26c | 26 | 0.004% | 0.000% | -0.004 | 0.004% | 0.000% | 0/5 | 5/5 |
| bur26d | 26 | 0.042% | 0.000% | -0.042 | 0.043% | 0.000% | 0/5 | 5/5 |
| bur26e | 26 | 0.009% | 0.000% | -0.009 | 0.009% | 0.000% | 0/5 | 5/5 |
| bur26f | 26 | 0.225% | 0.000% | -0.225 | 0.542% | 0.000% | 0/5 | 5/5 |
| bur26g | 26 | 0.376% | 0.000% | -0.376 | 0.376% | 0.000% | 0/5 | 5/5 |
| bur26h | 26 | 0.368% | 0.000% | -0.368 | 0.368% | 0.000% | 0/5 | 5/5 |
| chr12a | 12 | 0.000% | 0.000% | +0.000 | 0.000% | 0.000% | 5/5 | 5/5 |
| chr15a | 15 | 0.000% | 0.000% | +0.000 | 0.000% | 0.000% | 5/5 | 5/5 |
| chr18a | 18 | 0.000% | 0.000% | +0.000 | 0.000% | 0.000% | 5/5 | 5/5 |
| chr20a | 20 | 0.602% | 0.420% | -0.182 | 1.460% | 1.369% | 2/5 | 0/5 |
| chr22a | 22 | 0.000% | 0.188% | +0.188 | 0.000% | 0.617% | 5/5 | 3/5 |

Descriptive counts:

- Instance-mean delta: BLS lower on 14, higher on 1 (`chr22a`), equal on 5.
- Seed-level delta: BLS lower on 57, higher on 7, equal on 36.
- Overall mean gap: BLS 0.116%, robust tabu 0.274%.
- Overall median gap: BLS 0.000%, robust tabu 0.027%.
- Overall worst gap: BLS 1.369%, robust tabu 1.583%.
- Known optima: BLS 76/100, robust tabu 37/100.
- Summed per-run wall time: BLS 217.6 s, robust tabu 471.7 s.

These are descriptive differences from one 20-instance panel. They are **not** a
state-of-the-art claim, a significance test, or a claim that BLS beats robust
tabu. The instances are not independent (nine `bur` variants at n=26 dominate
the family-level average), the two solvers were run at different times, and
neither was tuned on this panel. The table is the fair comparison the issue
asked for: it shows both directions, including `chr22a` where the baseline is
worse.

## Reproducibility

- `python paper2/replay_qap_bls.py` reports `100/100 exact replays`.
- Re-running one run with the same instance and seed produced the same
  assignment, objective, and move count (`bur26b`, seed 4: objective 3,817,852,
  75,916 moves in both runs).
- Every evidence record stores the assignment, stored objective, adapter
  replay objective, `exact_replay`, moves, evaluations, stop reason, budget,
  and resolved BLS parameters.

## Limitations

- This is a reimplementation of the published BLS *design*, not the authors'
  code. It is not claimed to reproduce the paper's results or timings.
- The panel is limited to the 20 instances already used by the tabu panel. No
  larger QAPLIB tail, no `tai60a`/`tai80a`/`sko`/`nug` families, and no
  wall-clock-budgeted comparison.
- The stop rule is a declared move cap plus move patience. It differs from the
  paper's wall-clock stopping rule, so the budget is comparable to the tabu
  panel rather than to the published BLS experiments.
- The `L0` split follows the published type II versus type I/III guidance and
  the QAPLIB family labels; it was not tuned on this panel. A sensitivity study
  of `L0`, `T`, `LMax`, and patience is not part of this task.
- The `bur` instances need the general asymmetric delta update; the added
  correction is exact but raises the per-move constant relative to the
  symmetric Taillard path.
- The comparison is descriptive and single-panel. A paired bootstrap or
  multiple-panel test belongs in P13.8, not here.
- Timings come from one shared machine under varying load; summed CPU time is
  the more stable work measure. No GPU was used.
- The pure-Python reference path is an audit fallback. It produces a different
  RNG trajectory and is not used for the committed evidence.

## Files

- `paper2/qap_bls.py` - algorithm, typed helpers, exact delta update, replay
  check.
- `paper2/run_qap_bls.py` - parallel panel runner, checkpointing, evidence.
- `paper2/replay_qap_bls.py` - independent adapter replay.
- `paper2/evidence/qap-bls-expanded.json` - 100 per-run records.
- `paper2/evidence/qap-bls-expanded-summary.json` - 20 per-instance rows.

## Gates

- `python -m ruff check paper2/qap_bls.py paper2/run_qap_bls.py paper2/replay_qap_bls.py`: pass.
- `python -m ruff format --check paper2/qap_bls.py paper2/run_qap_bls.py paper2/replay_qap_bls.py`: pass.
- `python paper2/replay_qap_bls.py`: 100/100 exact replays.
- `python scripts/dashboard.py`: GREEN (lint, format, types, tests, validator, docs).
