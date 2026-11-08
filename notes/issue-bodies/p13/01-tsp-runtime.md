# P13.1: TSP runtime fix and 20-instance convergence panel

Parent: #81

## Why

The 20-instance TSP panel is incomplete. Expanded runs stalled on the last tasks. That is a runtime
pathology, not a result.

## Work

- [ ] Instrument `tsp_lk._lk_pass` by instance, seed, kick, pass, exchange test, and wall time.
- [ ] Reproduce the pathological cases individually.
- [ ] Fix the candidate/adjacency/search bound or add a correctly reported cap.
- [ ] Add per-seed checkpointing to the expanded runner.
- [ ] Run 20 TSPLIB instances x 5 seeds at a declared serious budget.
- [ ] Record actual kicks, stop reason, wall/CPU time, and exact replay.
- [ ] Add the table to Paper 2 from the evidence.

## Acceptance

- Every run has a declared stop reason.
- Every incumbent replays exactly.
- Cap hits are reported separately and are not called convergence.
- The table is generated from the evidence, not copied by hand.
- No 20-instance convergence claim until the file exists.
