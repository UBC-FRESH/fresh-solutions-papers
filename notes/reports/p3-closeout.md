# P3 close-out: Paper 1 benchmark evidence

Status: complete
Date: 2026-11-01
Issue: #10

## Result

P3 produced three replayable public/architecture records and a replay gate.

### Public baseline records

- FHOPS tiny7 SA, 200 iterations, seed 42:
  - objective **4295.774752**
  - exact replay 4295.774752
  - hard violations 0
- FHOPS small21 SA, 200 iterations, seed 42:
  - objective **15508.884819999994**
  - exact replay same
  - hard violations 0

### WS4 architecture record

- TSA24 compiled landscape, current even-flow target file
- WS4 GPU-GA, population 64, 1,000 generations, seed 7
- GPU objective **8588725.370498415**
- exact CPU replay **8588725.370498514**
- initial oldest-first seed objective **1722144291.336651**
- search elapsed **9.381 s**
- wall **23.13 s**
- 208,255 blocks
- schedule hash verified

The seed-to-GPU improvement is about **200× in objective**, but the seed is a starting point, not a
controlled best-baseline comparison. Do not present it as a benchmark win yet.

## Decisions

- Direct WS4/FHOPS adapter rejected as a problem-contract mismatch.
- FHOPS is a public baseline/reproducibility stack, not a WS4 architecture peer.
- Lockwood and Moore remains reconstructable/deferred because the original instance is unavailable.

## Verification

- Benchmark records validate against the schema.
- Schedule SHA-256 matches.
- Exact replay passes for all three records.
- Tests, Sphinx `-W`, and workflow validator pass.

## Limits

- The WS4 record uses a local reconstructable TSA24 fixture, not a public dataset.
- Time-to-first-feasible was not separately instrumented; search elapsed was used conservatively.
- The architecture result has no matched optimized baseline yet.
- FHOPS baselines are operational-planning results; they are not architecture comparisons.

## Recommendation

Close P3. P4 should freeze the evidence tables, write the architecture paper, and state the missing
matched-baseline limitation explicitly.
