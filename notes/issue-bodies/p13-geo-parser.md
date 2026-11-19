# P13.10: Fix TSPLIB GEO distance conversion

Parent: #40

## Problem

The GEO conversion in `fresh_solutions/adapters/tsp.py` uses the decimal degree as the base instead
of the integer degree. For `burma14`, the first edge is computed as 117 instead of the canonical 153,
and broad/LKH runs contain objectives below the published optimum.

## Scope

- Correct the GEO radians conversion.
- Add a known-distance regression test (`burma14` first edge = 153).
- Run the Fresh Solutions test suite and dashboard/quality gates.
- Publish a patch release/tag only after PI approval.
- Re-run the affected GEO broad TSP and LKH evidence in the papers repo after the fix.

## Acceptance

- The regression test fails on the old formula and passes on the fix.
- No GEO broad/LKH record reports a negative optimality gap.
- The papers repo reruns the affected panels and updates the claims.
