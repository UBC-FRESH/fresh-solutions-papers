# FHOPS / WS4 comparison decision

Status: P3.5 decision
Date: 2026-11-01

## Decision

A direct WS4-to-FHOPS adapter is **rejected**. FHOPS remains a reproducible public baseline and
reproducibility stack, but it is not a like-for-like comparison for the WS4 Paper 1 architecture.

## Why

| Dimension | WS4 | FHOPS |
|---|---|---|
| Decision object | Landscape harvest schedule by block and period | Operational machine/block/day/shift assignment |
| Time unit | Annual simulation, multi-year accounting periods | Days and shifts |
| Spatial scope | Landscape-level spatial harvest structure | Harvesting operations and machine coordination |
| Objective | Weighted goal-programming landscape targets | Operational harvest cost/production/sequencing objective |
| Feasibility | Spatial/flow/locked target rules | Machine, landing, sequencing, calendar constraints |
| Architecture target | Compiled resident state + GPU hybrid metaheuristics | MIP and metaheuristic operations planning |

Mapping one onto the other would change the problem, objective, and feasibility contract. A wall-clock
comparison would be apples-to-oranges.

## Consequence

- FHOPS supplies **public baseline evidence** and a reproducibility model.
- FHOPS does not supply the WS4 architecture comparison.
- The architecture comparison must use a landscape harvest-scheduling instance with a comparable
  objective and constraints, or be presented as a separate operational-planning result.

## What would change the decision

A published FHOPS scenario with a landscape-level, multi-period harvest objective and a WS4-compatible
spatial constraint set. Until then, no direct adapter.
