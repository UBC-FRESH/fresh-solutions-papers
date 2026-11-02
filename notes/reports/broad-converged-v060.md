# Broad QAP/TSP convergence panel — v0.6.0

Status: convergence audit, not publication-ready
Date: 2026-11-02
Solver: Fresh Solutions `v0.6.0`

## Protocol

- **78** TSPLIB instances with `n <= 1000`, five seeds.
- **134** parseable QAPLIB instances, five seeds.
- **1,085** scheduled runs; 25 `esc8` parser errors; 33 TSP instances above
  `n=1000` excluded.
- TSP: nearest-neighbour start, iterated LK, 100-kick patience.
- QAP: robust tabu, 10,000-iteration patience.
- No 30-second cap. A **600-second safety cap** was used only for oversized
  runs; cap hits are reported separately and are **not** called converged.

## Results

| Family | Band | Instances | Runs | Patience stops | Cap hits | Optimum runs | All mean | Converged mean | Converged median | Converged worst |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TSP | all | 78 | 390 | 236 | 154 | 183 | 1.327% | 0.100% | 0.000% | 2.110% |
| TSP | n≤100 | 28 | 140 | 135 | 5 | 121 | 0.098% | 0.101% | 0.000% | 2.110% |
| TSP | 100<n≤300 | 30 | 150 | 98 | 52 | 61 | 0.579% | 0.087% | 0.000% | 1.021% |
| TSP | n>300 | 20 | 100 | 3 | 97 | 1 | 4.170% | 0.502% | 0.461% | 0.605% |
| QAP | all | 134 | 670 | 552 | 118 | 318 | 1.723% | 1.823% | 0.000% | 36.445% |
| QAP | n≤100 | 130 | 650 | 552 | 98 | 314 | 1.733% | 1.823% | 0.000% | 36.445% |
| QAP | 100<n≤300 | 4 | 20 | 0 | 20 | 4 | 1.399% | — | — | — |

## What this says

- Small and medium TSP converge strongly: 183/390 runs hit the known optimum;
  the converged subset has median 0% and mean 0.100%.
- QAP often hits the optimum, but its converged mean is pulled by a few bad
  outliers; median 0%, worst 36.4%.
- Large TSP does **not** converge under the safety cap: 97/100 runs hit the
  cap, and only one hit the optimum. The 0.502% mean is therefore a
  cap-selected subset, not a large-instance convergence claim.
- Large QAP is also unresolved: no `100<n<=300` run reached patience.

## Honest conclusion

The current LK is strong on small/medium TSP but not a large-instance
convergence solver. QAP tabu is strong on median but has a tail. The next
algorithmic work is large-TSP scaling — candidate lists alone are not enough;
this is the case for a proper LK/LKH-scale implementation or a better
large-instance construction/refinement path.

## LKH target

The external LKH backend is recorded separately in `lkh-tail-v070.md`: on the
same large-TSP band it reaches 71/100 optimum runs and a 0.092% mean gap. That
is the capability gap the internal ILK still has to close.
