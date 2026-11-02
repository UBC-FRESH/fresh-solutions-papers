# Broad QAP/TSP panel — v0.5.1 pilot

Status: pilot evidence, not publication-ready
Date: 2026-11-02
Solver: Fresh Solutions `v0.5.1`

## Scope

- **78** TSPLIB instances with `n <= 1000`, five seeds.
- **134** parseable QAPLIB instances, five seeds.
- **1,085** runs total (some QAP errors remain; see below).
- TSP starts from a nearest-neighbour tour; QAP starts from identity.
- 30-second wall cap per run.

## Results

| Family | Band | Instances | Runs | Optimum runs | Mean gap | Median gap | P90 gap | Worst gap |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TSP | all | 78 | 390 | 108 | 4.663% | 0.497% | 17.011% | 32.087% |
| TSP | n<=100 | 28 | 140 | 88 | 0.156% | 0.000% | 0.497% | 2.110% |
| TSP | 100<n<=300 | 30 | 150 | 20 | 3.038% | 0.648% | 12.557% | 20.820% |
| TSP | n>300 | 20 | 100 | 0 | 13.409% | 14.527% | 21.078% | 32.087% |
| QAP | all | 134 | 670 | 311 | 2.447% | 0.067% | 7.468% | 66.764% |
| QAP | n<=100 | 130 | 650 | 311 | 1.794% | 0.022% | 6.614% | 30.477% |
| QAP | 100<n<=300 | 4 | 20 | 0 | 23.646% | 10.989% | 66.764% | 66.764% |

## Interpretation

This is a broad pilot, not a universal solver claim. Small TSP instances are strong:
88/140 runs hit the optimum, mean gap 0.156% at `n<=100`. QAP is strong through
`n<=100`: 311/650 runs hit the optimum, median gap 0.022%.

The large-instance tail is not small-gap. TSP `n>300` has median gap 14.5% under the
30-second cap, and QAP `100<n<=300` has median 11.0%. Those are real failures, not
noise to hide. More budget, better initial tours, or a stronger large-instance
neighbourhood is required before claiming broad competitiveness.

## Gaps and errors

- 33 TSPLIB instances with `n>1000` were excluded because the adapter stores a
  dense distance matrix.
- Five QAPLIB `esc8` variants failed to parse due to an extra header token.
- The 30-second cap is not a convergence proof.
- No independent solver baseline; known optimum/best-known values only.

## Next

1. Improve large-TSP initialization and neighbourhood scaling before raising the
   claim.
2. Fix the `esc8` QAPLIB header handling.
3. Add a stratified five-seed panel for the paper rather than reporting every
   available instance equally.
