# P13.7: Public artifact, container, and evidence schema

Parent: #81

## Why

A private artifact and optional replay gate are submission blockers.

## Work

- [ ] Define the per-record schema: solver commit, hardware, software, seed, budget, stop reason,
  exact replay, CPU/wall time, assignment hash.
- [ ] Make the validator fail on missing fields.
- [ ] Add one-command replay and a clean-checkout/container test.
- [ ] Prepare public release/Zenodo metadata.
- [ ] Prepare the exact visibility/release commands for PI approval.

## Acceptance

- Reviewer can clone, run one command, and reproduce every table.
- No tag/release/visibility change without explicit approval.
- Schema and manifest agree.
