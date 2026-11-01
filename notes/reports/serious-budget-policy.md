# Serious-budget and convergence policy

Status: P10.4 policy
Date: 2026-11-01
Scope: publication-facing benchmark evidence for Paper 1 and Paper 2

## Purpose

A result may not be called publication-grade because it was long, short, or lucky. It must state its
budget, stopping reason, seed count, and whether more budget changed the conclusion.

This policy does not make a run globally optimal. It prevents smoke tests and unconverged runs from
being presented as competitive evidence.

## Minimum evidence

A publication-facing campaign requires:

1. a pinned Fresh Solutions release or commit;
2. the public instance and known optimum/best-known value;
3. at least five seeds;
4. a stated local-iteration or wall-clock budget per seed;
5. the full assignment or a replayable record;
6. an exact replay check (the stored assignment re-evaluates to the stored objective);
7. hardware and software provenance;
8. mean, median, worst, and best optimality gap, plus wall time.

## Serious-budget floor

A run is **serious** only if it is more than a harness smoke test:

- QAP robust tabu: at least 10,000 tabu iterations per seed; 20,000 for the budget-stability check.
- TSP outer search: at least 10,000 local iterations per round, patience 3, up to 30 rounds or
  500,000 evaluations.
- Any run below these floors is internal smoke testing and may not appear in a paper table.

## Convergence flag

A campaign is **converged for reporting** when all of the following hold:

- every seed stops for a declared reason (`patience`, `max_seconds`, or `max_iterations`);
- every assignment replays exactly;
- a further budget doubling improves the five-seed mean gap by no more than **0.10 percentage points**,
  or the known optimum is reached on every seed;
- the selected budget is the smallest budget that passes the check after any failed doubling;
- the result is not selected from a single lucky seed.

If a budget doubling improves the mean by more than 0.10 points, the smaller budget is **not
certified**; continue the ladder until a doubling passes. The projected publication table uses the
certified budget, not the best result from an arbitrarily larger run.

A single doubling is not proof of asymptotic convergence. It is the minimum stopping rule used here;
closer instances receive an extra doubling to detect delayed improvements.

## Reporting rule

Every table row states:

- solver version;
- instance/size and optimum kind;
- seeds and budget;
- stopping reason;
- gap distribution;
- wall time;
- replay result.

## Application status

- QAP 10k vs 20k stability check: see `paper2/evidence/qap-tabu-stability-summary.json`.
- TSP converged campaign: uses patience; remains internal until a matched baseline exists.
- Paper 1: the matched landscape baseline is P10.5; the seed-only comparison is not a baseline.
