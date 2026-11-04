# Paper 2 TSP convergence protocol

Status: P12.1 secondary protocol
Date: 2026-11-03
Issue: #76

## Problem

The existing TSP ILK result uses 20 double-bridge kicks. That is a short
quality-at-additional-cost experiment, not a convergence test. It cannot support a Q1 TSP search
claim.

## Campaign

- Instances: `berlin52`, `kroA100`, `kroB100`, `ch150`.
- Starts: the existing converged Or-opt tours, one per seed.
- Seeds: 1 through 5.
- Candidate count: 16; maximum LK depth 4.
- Kick cap: 100,000.
- Patience: 1,000 kicks without a new best tour.
- No wall-clock cap in the publication-facing run.

## Reporting

- A run is plateau-stopped only when `stop_reason == "patience"`.
- A run that reaches 100,000 kicks is reported as `max_kicks` and is not convergence evidence.
- Report mean, median, best, and worst gap, wall time, kicks, accepted kicks, and exact replay.
- If any run hits the cap, the TSP claim is restricted to the plateau-stopped subset and the cap hits
  are reported.
- The 20-kick ILK table remains a separate short-budget result and must not be merged with this one.

## Acceptance

- All five seeds per instance replay exactly.
- At least one full instance has five plateau-stopped seeds before any TSP convergence sentence is
  written.
- If the campaign is too slow or does not plateau, TSP remains a reference-adapter/replay result,
  not a Q1 search result.
