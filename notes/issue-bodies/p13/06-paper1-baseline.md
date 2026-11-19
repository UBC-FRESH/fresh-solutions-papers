# P13.6: Paper 1 independent search baseline

Parent: #81

## Why

The current CPU-SA is untuned, single-seed, and not a controlled baseline.

## Work

- [ ] Tune CPU-SA on a small validation set; run five seeds.
- [ ] Add greedy target-following and random feasible baselines.
- [ ] If feasible, build a reduced TSA24 MIP/CP-SAT model and report an optimality gap on the
  reduced instance.
- [ ] Keep full-instance and reduced-instance claims separate.

## Acceptance

- The GPU result is compared with an independent method, not only the initial seed.
- Reduced-instance results are labelled as such.
- Exact replay for every reported schedule.
