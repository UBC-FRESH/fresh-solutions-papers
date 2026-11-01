# P10.5 close-out: same-engine landscape scaling baseline

Status: complete with limitation
Date: 2026-11-01
Issue: #36
Record: `evidence/ws4-tsa24-gpu-ga-10000-r7/record.json`

## Recommendation

Close P10.5. Paper 1 now has a matched, optimized, non-seed landscape baseline. It is a **same-engine
scaling baseline**, not an independent solver, and the paper must say so.

## Acceptance

- Select baseline method and budget: **met** (WS4 GPU-GA, 10,000 generations, 10× the 1,000-generation
  record; seed and instance fixed).
- Run on the frozen TSA24 target set: **met**.
- Record time-to-quality and exact replay: **met**.
- Replace the seed-only comparison in Paper 1 evidence: **met**; the draft now reports both budgets and
  labels the comparison as same-engine.

## Results

| Record | Generations | Objective | Exact replay | Search s | Wall s |
| --- | ---: | ---: | --- | ---: | ---: |
| `ws4-tsa24-gpu-ga-1000-r7` | 1,000 | 8,588,725.370498 | yes | 9.381 | 23.130 |
| `ws4-tsa24-gpu-ga-10000-r7` | 10,000 | 76,540.740733 | yes | 89.782 | 157.338 |

The 10× budget run is about 112× lower in objective. Two independent runs produced the same schedule
SHA-256 (`cd430e634b35b320ee404ba75fecb739afa2f585daaee041af97ff6172a914b8`).

## Gate evidence

- `python scripts/check_benchmark_record.py evidence/ws4-tsa24-gpu-ga-10000-r7/record.json`
  reports `VALID`.
- Exact replay via `evidence/ws4-tsa24-gpu-ga-10000-r7/replay.py`.
- Evidence table regenerated with four records.

## Limits

- Same engine, same seed, same instance; this is budget scaling, not method independence.
- TSA24 is reconstructable, not public.
- Time-to-first-feasible is not separately instrumented; search elapsed is reported conservatively.
- The TSA24 landscape still lacks a public independent baseline; Paper 1 remains not submission-ready.

## Follow-up

P10.6 selects an applied case. P10.7 must keep this limitation in the evidence close-out.
