# P13: Publication hardening for both papers

## Goal

Turn both drafts into submission-grade papers by adding the missing evidence, independent baselines,
ablation, portability, public artifact, sensitivity analysis, and a second independent review. This
phase is explicitly not effort-bounded; tasks close only when their acceptance tests pass.

## Plan of record

`notes/plans/p13-publication-hardening-2026-11-08.md`

## Targets

- Paper 1: Environmental Modelling & Software (architecture/reproducibility scope); SoftwareX/JORS
  fallback.
- Paper 2: Journal of Heuristics; SoftwareX/JORS fallback. COR only if P13.2/P13.3 produce a genuine
  methodological contribution.

## Workstreams

- [ ] P13.1 TSP runtime fix and 20-instance convergence panel (#82)
- [ ] P13.2 Independent QAP baseline (#83)
- [ ] P13.3 Generic engine tabu/LNS layer (#84)
- [ ] P13.4 Third adapter and portability (#85)
- [ ] P13.5 Paper 1 architecture ablation (#86)
- [ ] P13.6 Paper 1 independent search baseline (#87)
- [ ] P13.7 Public artifact, container, and evidence schema (#88)
- [ ] P13.8 Sensitivity and statistical analysis (#89)
- [ ] P13.9 Independent antagonistic review and claim audit (#90)
- [ ] P13.10 Journal package and submission readiness (#91)

## Acceptance criteria

- Every task issue is closed with evidence and a dashboard/CI result.
- Every headline claim maps to a file and regenerates from the committed runner.
- Both papers have a target-specific package and a clean build.
- The public artifact resolves and one-command replay works.
- The independent review has no unresolved high-severity objection.
- No tag, release, visibility change, or submission without explicit PI approval.

## Non-goals

- No new paper spin-off.
- No state-of-the-art claim without a matching baseline.
- No “converged” label for a cap hit.
- No private artifact presented as public.
