# P13.3: Generic engine tabu/LNS layer

Parent: #81

## Why

The current framework-use result manages state; it does not show a generic search layer.

## Work

- [ ] Add a generic tabu or large-neighbourhood layer that uses only adapter operations.
- [ ] Run QAP and TSP through the generic layer.
- [ ] Compare quality, wall/CPU time, and exact replay against adapter-specific modules.
- [ ] Report a negative result honestly if the generic layer is worse.
- [ ] Update the framework claim.

## Acceptance

- At least one headline path goes through the generic engine.
- Same seeds, budgets, and stopping rules.
- Exact replay.
- The paper no longer overstates the framework result.
