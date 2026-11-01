# P2 close-out: architecture and benchmark contracts

Status: complete
Date: 2026-11-01
Issue: #8

## Result

P2 froze the architecture and the benchmark contracts. No benchmark was run.

Deliverables:

- `notes/design/compiled-state-architecture.md` — architecture claim, layers, cache identity, hybrid
  search, adapter boundary, and replay gate.
- `notes/design/benchmark-adapter-contract.md` — required adapter surface and evidence rules.
- `notes/design/replay-and-feasibility.md` — exact replay procedure, tolerances, and the distinction
  between hard feasibility and weighted goal residuals.
- Cross-references to `schemas/benchmark-record.schema.json` and the Fresh Solutions adapter protocol.

## Key decisions

1. The architecture pattern is the contribution; benchmark results are evidence.
2. Effect-table cache identity is dataset + candidates + target-cell geometry + horizon/period width +
   extra rows + format version.
3. Weight, priority, normalization, and aspiration changes do not rebuild the effect table.
4. A benchmark record is invalid unless the serialized schedule replays exactly.
5. Hard feasibility is separate from target residual performance.

## Verification

- Sphinx HTML with `-W`: pass.
- Workflow validator: 0 errors.
- P1 benchmark schema remains the machine-readable evidence contract.

## Limits

The replay procedure is a contract, not yet a harness implementation. P3 must implement and test the
harness against the first reconstructed instance.

## Recommendation

Close P2. Start P3 after the maintainer approves the P3 parent issue.
