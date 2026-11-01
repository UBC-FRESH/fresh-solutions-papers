# P10.6 applied case plan: TSA24 even-flow harvest scheduling

Status: active — publication permission not established
Date: 2026-11-01
Issue: #37

## Candidate case

**TSA24 / Prince George Timber Supply Area, even-flow harvest scheduling.**

- Instance: compiled TSA24 landscape, 208,255 blocks, 20 periods, 200-year horizon.
- Target: even flow within ±1% and linear harvest minimum 70,000,000 m³ per 10-year period
  (7.0M m³/year, slightly above the 2025 AAC 6,917,231 in the target file).
- Objective: weighted goal-programming penalty over flow and level targets.
- Current records: `ws4-tsa24-gpu-ga-1000-r7` and `ws4-tsa24-gpu-ga-10000-r7`.

This is a real timber-supply decision problem reconstructed from the local FEMIC/WS4 fixture, not a
synthetic toy instance.

## Decision and outcome

The decision is a block/treatment schedule. The measurable outcomes are:

- per-period harvest volume;
- flow deviation from the ±1% band;
- minimum-level shortfall;
- weighted objective (sum of penalties);
- feasible schedule and exact replay;
- search and wall time;
- schedule SHA-256.

The 10,000-generation record already gives a point estimate for these metrics, but it is not yet a
partner decision or a published applied result.

## Baseline

The matched baseline is the 1,000-generation same-engine record. The 10,000-generation record is the
current optimized point. There is no independent solver baseline; the case may not claim one.

## Data provenance and permission

- Local path: `/srv/shared-data/gep/ws4/femic/external/femic-tsa24-instance`.
- Target/provenance: `config/ws4/targets/evenflow_tsa24.yaml`; source data derived through FEMIC.
- Licence: **not established** in the compiled fixture.
- Publication permission: **not established**.
- Partner: **not named**.

**Stop condition:** no paper, public case study, or partner-impact claim until the data owner confirms
redistribution and publication permission.

## Case-study plan

1. Establish the data licence and permission, or replace the fixture with a public/partner-approved
   instance.
2. Freeze the target file and instance hash.
3. Run the 1,000/10,000-generation comparison and multi-seed sensitivity if permitted.
4. Extract per-period harvest and target residuals from the exact CPU evaluator.
5. Write a case report with the decision, metrics, baseline, limitations, and provenance.
6. Obtain maintainer and data-owner approval before publication.

## Current status

Selection and metrics are defined. Permission, partner confirmation, multi-seed runs, and the case
report are not complete. P10.6 remains open.
