# QAP multi-start tabu — large tail

Status: pilot evidence, not converged
Date: 2026-11-02
Solver: Fresh Solutions main `ba3e3b7` (multi-start tabu support)

## Protocol

- Four QAPLIB instances with `n > 100`: `esc128`, `tai150b`, `tai256c`, `tho150`.
- Five random starts per instance, tabu patience 10,000, 600-second safety cap.
- No 30-second cap. Every run hit the safety cap, so none is called converged.

## Results

| Instance | Identity-start gap | Best multi-start gap | Mean multi-start gap |
| --- | ---: | ---: | ---: |
| esc128 | 15.62% | 0.000% | 1.250% |
| tai150b | 5.94% | 2.549% | 3.498% |
| tai256c | 66.76% | 0.350% | 0.413% |
| tho150 | 6.23% | 1.264% | 1.789% |

Identity-start values are the converged-panel cap hits from
`broad-converged-summary.json`. Multi-start improves every large instance, but
all five starts hit the 600-second cap. This is a portfolio-improvement result,
not a large-QAP convergence claim.

## Boundary

- Multi-start tabu is still robust tabu; no new heuristic.
- 600-second cap hits are not converged.
- The next requirement is either a longer convergence budget or a stronger
  large-QAP refinement; do not claim resolved large QAP.

## Files

- `paper2/evidence/qap-multistart.json`
- `paper2/run_qap_multistart.py`
