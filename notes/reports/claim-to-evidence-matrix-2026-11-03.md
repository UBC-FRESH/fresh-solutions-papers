# Claim-to-evidence matrix

Status: current after P12.4
Date: 2026-11-03

## Paper 1

| Claim | Evidence | Status | Residual risk |
| --- | --- | --- | --- |
| 458,708 compiled blocks; 208,255 operable | TSA24 artifact and compiled data | Verified | None |
| 100k seed-7 objective 517.862; flow 2.721; level 515.141 | `evidence/ws4-tsa24-gpu-ga-100000-r7/record.json` | Verified | None |
| Five seeds 512.574–518.621; mean 515.682 | five 100k records | Verified | None |
| Realized level 51.21–52.49M | five records | Verified | None |
| GPU 100k campaign is GPU-GA with exact CPU replay | record algorithm and counters | Verified | No CPU-refinement arm |
| CPU-SA 335,044,976.675435; 31.25 min; 204,413 blocks | CPU-SA record | Verified | Not equal-work |
| 5,000-block ablation 2,005× | ablation evidence | Verified | Subset only |
| Architecture causes speed/quality | no matched ablation | **Not claimed** | Must stay out of claims |
| Schedules/replay public | papers repo private | **Blocked** | Release approval required |

## Paper 2

| Claim | Evidence | Status | Residual risk |
| --- | --- | --- | --- |
| QAP framework path exact on 40 runs | `framework-use.json`; validator | Verified | Small panel |
| CPU overhead 1.239 (1.168–1.310) | framework analysis | Verified | Pure-Python baseline |
| 20-instance QAP panel; 100/100 patience; mean 0.274% | `qap-expanded-100k.json` | Verified | Not state-of-the-art baseline |
| SciPy expanded mean 25.44%; median 2.55% | `qap-scipy-expanded.json` | Verified | Not equal-time |
| TSP 4-instance 10k campaign; 20/20 optima | `tsp-convergence-10k.json`; replay | Verified | Small panel |
| TSP actual work 1,000–1,380 kicks | records | Verified | Label must say cap |
| TSP 20-instance expanded panel | `tsp-expanded-2k.json` if complete | Pending | Not yet claimed |
| Broad runner reproduces summary | `broad_summary.py`; canonical regenerated summary | Verified | Per-record metadata uneven |
| Applied TSA24 is a Fresh Solutions adapter | no adapter exists | **Not claimed** | Separate WS4 case |
| Papers repo is public/MIT | private, no public release | **Blocked** | Approval required |
| All records contain solver/hardware/CPU/replay | partial; sidecar | **Not claimed** | Release blocker |

## Rules

- A claim with “blocked” or “pending” does not enter the manuscript as a completed result.
- A claim with “not claimed” must not appear in an abstract, conclusion, or response to reviewers.
- Every numeric claim is regenerated from evidence or marked as a limitation.
