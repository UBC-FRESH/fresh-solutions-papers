# Broad QAP/TSP benchmark panel

Status: convergence panel, not publication evidence.

## Sources

- TSPLIB mirror: `https://github.com/mastqe/tsplib` at
  `775541365dc3f7f3cd6faa8d0e206036d2c45e0e`
- QAPLIB mirror: `https://github.com/didoudiaz/QAP-instances` at
  `3cfd4f2bf82782e6c02fe4a79397e02f8ef54b14`

TSPLIB has 111 symmetric TSP files. This panel includes the 78 with `n <= 1000`;
the 33 larger instances are excluded because the adapter stores dense matrices.
QAPLIB has 139 canonical `.dat` files; 134 parse with FRESH Solutions v0.9.3.
Five `esc8` variants carry an extra header token and are recorded as parser gaps.

## Protocol

- Five seeds (`1..5`).
- TSP: nearest-neighbour initial tour, then iterated Lin–Kernighan with 16
  candidates, depth 4, 100-kick patience.
- QAP: robust tabu, 10,000-iteration patience.
- A 600-second safety cap is used only for oversized runs; cap hits are
  reported as non-converged, not counted as patience stops.
- Every run records objective, known optimum/best-known value, gap, wall time,
  stop reason, and assignment.
- Full records: `paper2/evidence/broad-converged.json.gz`.
- Summary: `paper2/evidence/broad-converged-summary.json`.
- Successful runs: 1,060; parse-error records: 25 (`esc8b`–`esc8f`).

The 600-second cap is a safety limit, not a convergence claim. See
`notes/reports/broad-converged-v060.md`.

## Reproduce

Clone the two mirrors at the pinned commits, then point the runner at them:

```bash
export TSPLIB_ROOT=/path/to/tsplib
export QAPLIB_ROOT=/path/to/QAP-instances/QAPLIB
export TSPLIB_COMMIT=775541365dc3f7f3cd6faa8d0e206036d2c45e0e
export QAPLIB_COMMIT=3cfd4f2bf82782e6c02fe4a79397e02f8ef54b14
export FRESH_SOLUTIONS_VERSION=v0.9.3
export FRESH_SOLUTIONS_COMMIT=1affc14
python paper2/run_broad_converged.py --workers 24
```

The runner writes solver/corpus provenance, successful records, and parse errors
separately in the summary. It requires `numpy`, `scipy`, and the optional
`numba` extra for the accelerated QAP path.

## External LKH tail

`paper2/run_lkh_large.py` runs a user-supplied LKH binary on the `300<n<=1000`
tail. LKH is not bundled. Results: 100 runs, 71 optimum, mean gap 0.092%,
median 0%, worst 1.930%. See `notes/reports/lkh-tail-v070.md`.

## QAP multi-start tail

`paper2/run_qap_multistart.py` runs five random starts on the four QAPLIB
instances with `n>100`. With delta-matrix tabu updates and no time cap, all 20
runs stopped on patience; best gaps are 0.00/2.008/0.350/0.166%. See
`notes/reports/qap-multistart-v080.md`.
