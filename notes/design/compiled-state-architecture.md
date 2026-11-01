# Compiled-state architecture and hybrid search

Status: P2 design contract
Date: 2026-11-01

## Claim

Large spatially explicit planning models can be searched faster and more reproducibly when the model is
compiled once into a stable sparse representation, exact resident state is maintained separately from
search, and global GPU population search is paired with exact CPU local refinement.

The benchmark wins are evidence for the architecture. They are not the claim.

## Layers

```text
compiled model / instance
  -> candidate index
  -> target-cell index
  -> sparse effect table
  -> resident exact state
          |
          +--> exact CPU evaluator and local search
          +--> batched GPU population search
          +--> replay and evidence recorder
```

### 1. Compiled model

The model compiler produces immutable tables: blocks/fragments, strata, tracks, treatments, transitions,
curves, features, products, and accounts. The dataset fingerprint identifies the compiled input. A
different dataset is a different instance.

### 2. Candidate index

A candidate index maps each block to a finite ordered list of treatment chains. The order is part of the
contract: effect-table rows and genome option indices refer to it. Candidate generation parameters are
part of the cache identity.

### 3. Target-cell index

The target-cell index maps each target to the `(offset, account)` cells it reads and to any flow-period
windows. It depends on the account set, target periods, horizon, period width, and flow windows. It does
not depend on weights, priorities, normalization, or aspiration values.

### 4. Sparse effect table

Each `(block, chain)` pair has one sparse row over target cells. The table also stores:

- the base empty-schedule totals;
- block row starts;
- optional extra rows for seed chains absent from the candidate list;
- the row index, or a lean row-start map when full indexing is omitted.

Cache identity:

```text
dataset fingerprint
+ candidate set and row order
+ target-cell geometry
+ horizon and period width
+ extra rows
+ table format version
```

Changing weights, priorities, minima, maxima, normalization, or the flow band is a **pricing** change,
not a table rebuild.

### 5. Resident exact state

The resident state is authoritative. For a forestry model it is `[period, block, account]` plus separate
product event rows. A move applies precomputed block/option deltas to only the changed rows and
period totals; undo restores the prior rows.

The state is not a search-only cache. It is the exact accounting substrate used by the chart, the
objective, and replay.

### 6. Search

Two search paths share the same instance, candidates, target cells, and effect table:

- **Exact CPU local search:** toggle, shift, swap, bounded LNS, and other exact moves.
- **Batched GPU population search:** candidate-index genomes evaluated against the sparse table.

The hybrid loop is:

```text
GPU population -> elite schedule
               -> exact CPU state load
               -> short exact local refinement
               -> exact replay
               -> refined elite as GPU seed/immigrant
```

The CPU path is authoritative when the two disagree. The GPU path never silently changes the objective
contract.

## Adapter boundary

The generic solver contract is in `fresh-solutions`:

```text
problem adapter
  variables + domains
  candidate/option representation
  exact evaluator
  batched evaluator
  feasibility/repair
  move/apply/undo
  replay metadata
```

A benchmark adapter additionally provides instance provenance, availability status, and schedule
serialization.

## Evidence and replay

Every reported incumbent must produce a benchmark record conforming to
`schemas/benchmark-record.schema.json`:

- source citation/DOI/URL;
- instance identity and availability;
- objective, constraints, feasibility;
- algorithm/version/config;
- seed, hardware, software;
- timing decomposition;
- schedule path and SHA-256;
- exact replay result;
- per-target residuals.

`exact_replay` is a gate, not a note. A record with a false replay flag is not a result.

## Cache invalidation

Production must key each cache independently:

| Cache | Identity |
|---|---|
| simulator | dataset fingerprint |
| candidates | dataset + candidate-generation parameters |
| effect table | table identity in §4 |
| base totals | effect-table cells + dataset base values |
| seed state | account set + horizon + period width + schedule |
| parsed schedule | source file identity |

A rebuild of the effect table invalidates the base-total sidecar and any seed state derived from it. The
P84 prototype exposed this as a production weakness; the papers programme must treat it as a first-class
contract.

## Non-goals

- Not a proof of optimality.
- Not a universal dense solver.
- Not a claim that GPU acceleration helps every combinatorial problem.
- Not a licence to compare unequal objectives or infeasible schedules.
- Not a replacement for exact replay.
