# Paper 2 claims audit

Status: internal audit
Date: 2026-11-02
Draft: `paper2/paper2-draft.md`

## Claim map

| Claim | Evidence | Status |
| --- | --- | --- |
| Adapter/replay framework is the contribution | `paper2/paper2-draft.md` architecture; contract tests | Supported |
| QAP certified means 0.000–0.685% | `qap-tabu-converged-summary.json` | Supported |
| QAP broad median 0%, mean 1.823% | `broad-converged-summary.json` | Supported; heavy tail disclosed |
| Large-QAP best 0.000–2.008% | `qap-multistart-converged.jsonl` | Supported |
| Large-QAP SciPy baseline is mixed | `qap-scipy-large-summary.json` | Supported; SciPy wins tai150b only |
| TSP ILK 0.000–0.383% | `tsp-lk-summary.json` | Supported; extra budget |
| LK kicks are material | `tsp-lk-ablation-summary.json` | Supported |
| Internal TSP is small/medium only | `broad-converged-summary.json` | Supported; 97/100 cap hits above n=300 |
| External LKH is strong on large TSP | `lkh-large-summary.json` | Supported; external, not bundled |
| TSA24 GPU-GA 100k is strong | `ws4-tsa24-gpu-ga-100000-*/record.json` | Supported; 5 seeds, exact replay |
| CPU-SA is an independent-search baseline | `ws4-tsa24-cpu-sa-100000-r7/record.json` | Supported; time-limited, not converged |
| TSA24 is public | `ws4-tsa24-evenflow-v1` release | Supported; frozen artifact |
| Universal small-gap performance | none | **Removed** |
| State-of-the-art QAP/TSP | none | **Removed** |
| Independent model landscape baseline | none | **Open** |
| Partner-endorsed applied impact | none | **Removed** |

## Corrections made

- Corrected the SciPy large-QAP comparison: SciPy wins `tai150b` only; Fresh
  tabu wins `esc128`, `tai256c`, and `tho150`.
- Replaced “TSA24 reconstructable” with the public frozen artifact.
- Added the 100k GPU-GA five-seed result.
- Replaced “large-QAP lacks an independent baseline” with “mixed SciPy baseline,
  no state-of-the-art claim.”

## Remaining submission blockers

- Paper 2 has no independent model baseline and no TSPLIB/QAPLIB-wide campaign.
- LKH is external and research-use; it cannot be presented as Fresh Solutions.
- The applied case is public-data, not partner-endorsed.
- The draft remains internal until the claims table is accepted.
