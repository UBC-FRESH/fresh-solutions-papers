# Broad QAP/TSP benchmark panel

Status: pilot campaign, not publication evidence.

## Sources

- TSPLIB mirror: `https://github.com/mastqe/tsplib` at
  `775541365dc3f7f3cd6faa8d0e206036d2c45e0e`
- QAPLIB mirror: `https://github.com/didoudiaz/QAP-instances` at
  `3cfd4f2bf82782e6c02fe4a79397e02f8ef54b14`

TSPLIB has 111 symmetric TSP files. This panel includes the 78 with `n <= 1000`;
the 33 larger instances are excluded because the adapter stores dense matrices.
QAPLIB has 139 canonical `.dat` files; 134 parse with v0.5.1. Five `esc8` variants
carry an extra header token and are recorded as parser gaps.

## Protocol

- Five seeds (`1..5`).
- TSP: nearest-neighbour initial tour, then iterated Lin–Kernighan with 16
  candidates, depth 4, 20 kicks, 30-second cap.
- QAP: robust tabu, 100,000 iteration ceiling, 30-second cap.
- Every run records objective, known optimum/best-known value, gap, wall time,
  stop reason, and assignment.
- Full records: `paper2/evidence/broad-suite-v051.json.gz`.
- Summary: `paper2/evidence/broad-suite-v051-summary.json`.

The 30-second cap is a declared pilot budget, not a converged-evidence claim.
