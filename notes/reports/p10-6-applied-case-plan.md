# P10.6 applied case: TSA24 even-flow harvest scheduling

Status: complete
Date: 2026-11-01
Issue: #37

## Candidate case

**TSA24 / Prince George Timber Supply Area, even-flow harvest scheduling.**

- Instance: compiled TSA24 landscape, 208,255 blocks, 20 periods, 200-year horizon.
- Target: even flow within ±1% and linear harvest minimum 70,000,000 m³ per 10-year period
  (7.0M m³/year, slightly above the 2025 AAC 6,917,231 in the target file).
- Objective: weighted goal-programming penalty over flow and level targets.
- Records: `ws4-tsa24-gpu-ga-1000-r7` and `ws4-tsa24-gpu-ga-10000-r7`.

## Ownership and publication

- **Builder/owner:** UBC-FRESH Lab.
- **Public repository:** https://github.com/UBC-FRESH/femic-tsa24-instance
- **Visibility:** public.
- **Default branch:** `main`; the FEMIC submodule pins `aaba8f33`.
- **Description:** “FEMIC deployment instance for TSA24 (WBI birds AOI; femic#316)”.
- **Data:** fresh public BC data — VRI 2025, FADM boundaries, and SiteProd, with the
  public `femic-public-data` DataLad remote and public Arbutus S3 bucket
  `ubc-fresh-femic-tsa24-instance`.
- **Local compiled fixture:** `/srv/shared-data/gep/ws4/femic/external/femic-tsa24-instance`.
  It is the local WS4 build/target layer over that public instance.

### Licence nuance

The repository currently has no explicit `LICENSE` file, and the benchmark record’s
`instance.license` is `null`. The source data retains BC government licences and is not
redistributed as an unrestricted attachment. This is a metadata/attribution gap to fix; it is
**not** an external partner-permission blocker. UBC-FRESH owns the instance repository and
publishes the data path publicly.

## Decision and outcome

The decision is a block/treatment schedule. Measurable outcomes:

- per-period harvest volume;
- flow deviation from the ±1% band;
- minimum-level shortfall;
- weighted objective (sum of penalties);
- feasible schedule and exact replay;
- search and wall time;
- schedule SHA-256.

The 10,000-generation record gives a point estimate: objective 76,540.740733, exact replay, two
runs with the same schedule hash. It is a public-data case, not a partner-endorsed operational
decision.

## Baseline

The matched baseline is the 1,000-generation same-engine record. The 10,000-generation record is
the current optimized point. There is no independent solver baseline; the case may not claim one.

## Remaining limits

- Public-data reconstructable case, not a named partner deployment.
- No explicit repository LICENSE file; add attribution/licence metadata before publication.
- No independent landscape baseline.
- No partner-impact claim.

## Follow-up

The case can proceed as a public-data applied case. Add the attribution/licence metadata and keep
the “same-engine baseline” caveat in any paper table.
