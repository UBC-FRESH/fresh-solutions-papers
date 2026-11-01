# P10.3 close-out: Lin–Kernighan TSP neighborhood

Status: complete
Date: 2026-11-01
Issue: #34
Solver pin: Fresh Solutions `24dc60c` (P10.1)
Implementation: `fresh_solutions/adapters/tsp_lk.py`

## Recommendation

Close P10.3. The LK implementation produces a material improvement over the converged Or-opt tours,
with exact replay. The comparison is quality-at-additional-cost, not an equal-budget ablation.

## Implementation

- Candidate-list Lin–Kernighan sequential edge exchange.
- Exact tour reconstruction from alternating add/remove edges.
- Deterministic double-bridge kicks for iterated LK.
- Config: 16 candidates, depth 4, 20 kicks, 100 LK passes, seed per run.
- No randomized triple sampling; `tsp_three_opt.py` remains a rejected experiment.

## Results

Five seeds per instance, starting from the converged Or-opt assignment:

| Instance | Or-opt mean gap | LK mean gap | LK worst gap | LK mean wall (s) | Or-opt mean wall (s) |
| --- | ---: | ---: | ---: | ---: | ---: |
| berlin52 | 6.433% | **0.000%** | 0.000% | 12.18 | 5.02 |
| kroA100 | 7.323% | **0.000%** | 0.000% | 8.46 | 12.51 |
| kroB100 | 3.696% | **0.000%** | 0.000% | 11.67 | 12.81 |
| ch150 | 8.229% | **0.383%** | 0.475% | 11.59 | 29.34 |

- Three instances reach the known optimum on all five seeds.
- `ch150` mean gap is 0.383%; best seed 0.230%; worst 0.475%.
- Every recorded tour replays exactly: **20/20**.

## Acceptance

- Material improvement over 3.7–8.2%: **met**.
- Exact replay: **met**.
- Same budget rules: **not equal-budget**. The LK path receives additional local-search time; wall
  times are reported. The claim is time-quality, not equal-budget dominance.

## Kicks ablation

| Instance | LK-only mean gap | ILK-5 mean gap | ILK-20 mean gap |
| --- | ---: | ---: | ---: |
| berlin52 | 2.580% | 0.000% | 0.000% |
| kroA100 | 1.075% | 0.062% | 0.000% |
| kroB100 | 0.780% | 0.172% | 0.000% |
| ch150 | 2.203% | 0.558% | 0.383% |

The double-bridge kicks are a material part of the result, not a cosmetic restart.

## Evidence

- `paper2/evidence/tsp-lk-ablation.json`
- `paper2/evidence/tsp-lk-ablation-summary.json`
- `paper2/evidence/tsp-lk.json`
- `paper2/evidence/tsp-lk-summary.json`
- `paper2/run_tsp_lk.py`
- `paper2/replay_tsp_lk.py`

## Limits

- This is iterated Lin–Kernighan, not a new algorithm.
- No independent TSP solver baseline is included.
- The result is on four public TSPLIB instances, not a TSPLIB-wide campaign.
- No state-of-the-art claim.
