# LKH large-TSP tail — v0.7.0

Status: external-backend evidence, not Fresh Solutions' own heuristic
Date: 2026-11-02
Backend: LKH-3 external binary (research-use software, not bundled)

## Protocol

- 20 TSPLIB instances with `300 < n <= 1000`.
- Five seeds (`1..5`), one LKH run per seed.
- Same 20 instances as the internal-LK `n>300` band.
- LKH binary supplied externally; Fresh Solutions only writes TSPLIB and parses the tour.
- Exact replay through the Fresh Solutions TSP adapter.

## Results

| Metric | LKH external | Internal ILK (same band) |
| --- | ---: | ---: |
| Runs | 100 | 100 |
| Patience/converged | 100 | 3 |
| Cap hits | 0 | 97 |
| Optimum runs | 71 | 1 |
| Mean gap | 0.092% | 4.170% |
| Median gap | 0.000% | 4.170% |
| Worst gap | 1.930% | 4.170% |
| Mean wall | 4.88 s | — |

The internal ILK numbers are the all-run band values from
`broad-converged-summary.json`; they are not a matched budget comparison. The
point is capability, not an equal-time win.

## Files

- `paper2/evidence/lkh-large.json`
- `paper2/evidence/lkh-large-summary.json`
- `paper2/run_lkh_large.py`

## Boundary

- LKH is Keld Helsgaun's external research solver. It is not bundled, not
  Apache-licensed, and not part of the Fresh Solutions heuristic claim.
- This establishes the large-TSP target and shows why the internal LK must be
  improved or clearly presented as a small/medium-instance method.
