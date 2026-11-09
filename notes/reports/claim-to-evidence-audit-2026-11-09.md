# Final claim-to-evidence audit

Date: 2026-11-09
Status: local audit complete; public release approval outstanding

## Paper 1

| Claim | Evidence | Status |
| --- | --- | --- |
| 100,000-generation five-seed TSA24 campaign, exact replay | `paper/evidence/ws4-tsa24-gpu-ga-100000-*`; `paper/replay_all.sh` | supported |
| Factorized 64-genome batch 248x; error 1.7e-6 | `paper/evidence/tsa24-factorized-ablation.json` | supported, batch scope stated |
| Matched 100-generation CPU 528.8 s vs CUDA 23.9 s; one seed; exact | `paper/evidence/tsa24-matched-search.json` | supported, no hardware/quality claim |
| CPU one-seed objective about 5% lower | matched-search JSON | supported |
| Target-variant screen 1.714e9 to 1,010 | `paper/evidence/tsa24-target-sensitivity.json` | supported, screen only |
| CPU-SA 335M time-limited | `evidence/ws4-tsa24-cpu-sa-100000-r7/record.json` | supported, weak comparator stated |

Open: public evidence release/DOI; tuned CPU-GA/full-campaign CPU comparison.

## Paper 2

| Claim | Evidence | Status |
| --- | --- | --- |
| Ten-seed QAP: tabu 0.301%, 73/200; BLS 0.096%, 161/200 | `qap-expanded-100k-10seed*`, `qap-bls-10seed*` | supported |
| BLS lower 120, higher 11, tied 69 | paired records | supported |
| Family-balanced means 0.298 vs 0.099 | summary records | supported |
| TSP expanded: 94/100 optima, 95/100 patience, 5 brazil58 cap hits | `tsp-expanded-10k*` | supported |
| Broad TSP 195 optima, no negative gaps | `broad-converged*` after GEO fix | supported |
| LKH 75/100, no negative gaps | `lkh-large*` after GEO fix | supported |
| Generic tabu QAP 3.848% vs 0.097%; TSP 127.978% vs 0.000% | `generic-tabu*` | supported, negative result |
| Framework-use overhead 1.24x, CI 1.17–1.31 | `framework-use*` | supported |

Open: public evidence release/DOI; per-record CPU time; third-party adapter absent and scoped as
future work; LKH is an external capability reference.

## Replay

`bash paper2/replay_all.sh` under `QAPLIB_ROOT`/`TSPLIB_ROOT`:

- 40 framework + 20 deep TSP + 1,060 broad QAP/TSP + 200 expanded QAP + 100 expanded TSP + 200 BLS
  + 40 generic incumbents exact.
- 25 `esc8` parse-error broad records skipped explicitly.
- 5/100 expanded TSP cap hits reported as cap hits.

No tag, release, visibility change, merge, or submission.
