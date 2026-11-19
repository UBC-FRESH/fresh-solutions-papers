# P13 publication-hardening plan

Status: active
Date: 2026-11-08
Phase identifier: P13
Branch: `feature/p13-publication-hardening`
Parent issue: TBD

## Objective

Maximise the probability that both papers survive peer review, not that they are submitted quickly.
The plan is evidence-first: every workstream either adds a missing comparison, closes a reproducibility
gap, or removes a claim a reviewer can falsify. No effort budget is set; a workstream closes only when
its acceptance test passes.

Targets:

- **Paper 1:** Environmental Modelling & Software, as an architecture/reproducibility paper. SoftwareX
  or JORS is the fallback if the architecture experiment fails or the paper is intentionally narrowed.
- **Paper 2:** Journal of Heuristics, as a reproducible benchmark-harness and framework-use paper.
  SoftwareX/JORS is the fallback. **COR is not a target** unless P13.2 and P13.3 produce a genuine
  methodological contribution.

## Inputs read

- `AGENTS.md`
- `ROADMAP.md`
- `CHANGE_LOG.md`
- `notes/reports/antagonistic-review-2026-11-03` (subagent review, retained in the conversation record)
- `notes/reports/claim-to-evidence-matrix-2026-11-03.md`
- `notes/reports/autonomous-remediation-closeout-2026-11-03.md`
- `notes/reports/paper2-framework-use-results.md`
- `notes/reports/paper2-tsp-convergence-protocol.md`
- `notes/reports/serious-budget-policy.md`
- `notes/reports/manuscript-plan-2026-11-03.md`

## Risk register

| ID | Risk | Evidence today | Required mitigation | Acceptance |
| --- | --- | --- | --- | --- |
| R1 | TSP 20-instance panel incomplete | 4-instance 10k panel; 78-instance broad panel; expanded attempts stalled | Diagnose and fix `tsp_lk` runtime; checkpointing; rerun serious panel | Complete panel with stop reasons and exact replay |
| R2 | QAP baseline is weak | SciPy FAQ only | Independent published-style baseline (BLS/Ro-TS) on same panel | Matched table; no straw man |
| R3 | Framework-use is narrow | Resident-state wrapper only | Generic engine tabu/LNS layer through adapters | Headline result through generic layer |
| R4 | Portability rests on two adapters | QAP and TSP | Third problem family / independent adapter | Third adapter, no engine changes |
| R5 | Paper 1 architecture claim untested | 5,000-block diagnostic only | CPU batch vs GPU batch; cache vs search; full-instance where feasible | Controlled ablation or explicit software-paper reframe |
| R6 | Paper 1 baseline weak | Single-seed CPU-SA | Tuned CPU-SA/GA; greedy/random; reduced MIP bound if feasible | Independent comparison |
| R7 | Evidence not public | Repo private; paper evidence pending | Public artifact/DOI/container, clean replay | Public URL and one-command replay |
| R8 | Metadata uneven | Sidecar plus partial stamping | Per-record schema and validator across publication records | Validator fails on missing fields |
| R9 | Panels/stopping weak | 20 QAP; 4 deep TSP | Sensitivity: seeds, patience, targets, instance families | Conclusion-change table |
| R10 | Reviewer objections unaddressed | One prior review | New independent antagonistic review after evidence | Objections closed or scoped |
| R11 | Journal fit risk | Paper 2 JoH; Paper 1 EMS | Target-specific package and cover letter | Editor checklist |
| R12 | Claim drift | Prior P0 fixes | Claim-to-evidence sweep before submission | No unbacked claim |

## Workstreams

### P13.1 — TSP runtime fix and 20-instance convergence panel

Why: the TSP panel is the most concrete incomplete evidence item, and the last tasks reveal a runtime
pathology that must be understood rather than hidden.

Deliverables:

- Profiling records for `tsp_lk` by instance/seed/kick/pass/exchange test.
- A fix for the pathological case, or a bounded search that reports cap hits.
- Checkpointed runner that writes each result.
- 20-instance × 5-seed panel at a declared serious budget.
- Per-run stop reason, actual kicks, wall/CPU time, exact replay.
- Paper 2 table generated from the new evidence.

Acceptance:

- Every run has a declared stop reason.
- Every incumbent replays exactly.
- Cap hits are reported separately and are not called convergence.
- No claim of a 20-instance convergence panel until the file exists.

### P13.2 — Independent QAP baseline

Why: SciPy FAQ is not a credible independent QAP baseline for a heuristics journal.

Deliverables:

- A published-style baseline: Breakout Local Search or Ro-TS (preferred).
- Same 20-instance panel, seeds, budget, and stopping rule.
- Full distribution and wall/CPU time.
- A fair comparison, including cases where the baseline wins.

Acceptance:

- Baseline code, runner, evidence, replay, and table.
- No “state-of-the-art” claim unless the comparison supports it.

### P13.3 — Generic engine tabu/LNS layer

Why: the current framework result is state management, not a generic search result.

Deliverables:

- A generic tabu or large-neighbourhood search layer that uses only adapter operations.
- QAP and TSP runs through the generic layer.
- Quality/time comparison against the adapter-specific modules.
- A negative result is acceptable and must be reported.

Acceptance:

- One headline path goes through the generic engine.
- Exact replay and same stopping rules.
- Claim language matches the result.

### P13.4 — Third adapter / portability experiment

Why: two adapters by the same author do not establish portability.

Deliverables:

- A third public problem adapter, preferably written from the contract by a separate subagent.
- A small reference run and exact replay.
- A note on what the engine did not need to change.

Acceptance:

- Third adapter works under the same contract.
- Claims about “third-party” or “portability” are supported or removed.

### P13.5 — Paper 1 architecture ablation

Why: the architecture claim is not separated from the GPU/implementation effect.

Deliverables:

- CPU batched evaluator over the same sparse effect table.
- GPU vs CPU at the same population/generation count.
- Cache-load vs search.
- Effect table vs direct evaluator on a full or clearly bounded instance.
- Matched CPU-GA/SA at equal work and equal wall time.

Acceptance:

- A controlled table that supports or falsifies the architecture claim.
- If it fails, retitle/reframe Paper 1 and remove the causal claim.

### P13.6 — Paper 1 independent search baseline

Why: the current CPU-SA is untuned and single-seed.

Deliverables:

- Tuned CPU-SA with five seeds and a stated configuration.
- Greedy target-following and random feasible baselines.
- Reduced TSA24 MIP or CP-SAT bound on a subsample if feasible.
- A clear statement of what each baseline does and does not establish.

Acceptance:

- The GPU result is compared to an independent method, not only the initial seed.
- Reduced-instance results are labelled as such.

### P13.7 — Public artifact, container, and evidence schema

Why: a private artifact and optional replay gate are submission blockers.

Deliverables:

- Public repository/Zenodo release with DOI and license.
- One-command replay from a clean checkout/container.
- Per-record schema with solver commit, hardware, software, seed, budget, stop reason, exact replay,
  CPU/wall time, assignment hash.
- Validator that fails on missing fields.
- Tables regenerated in CI.

Acceptance:

- A reviewer can clone, run one command, and reproduce every table.
- No release/tag without maintainer approval.

### P13.8 — Sensitivity and statistical analysis

Why: reviewers will attack small panels, stopping rules, and target weights.

Deliverables:

- Seed-count sensitivity: 5/10/20.
- Patience sensitivity: QAP 50k/100k/200k; TSP 200/1000/5000 where feasible.
- Target-weight and level-aspiration sensitivity for TSA24.
- Bootstrap confidence intervals, paired differences, performance profiles, cap-hit rates.
- A table of what would change the conclusion.

Acceptance:

- Every headline conclusion has a sensitivity check.
- Negative or unstable results are retained.

### P13.9 — Independent antagonistic review and claim audit

Why: a second adversarial pass after new evidence is cheaper than a desk rejection.

Deliverables:

- Three independent subagent reviews: Paper 1 modelling/EMS, Paper 2 methods/JoH, reproducibility.
- A claim-to-evidence matrix with every claim linked to a file.
- A response letter that closes or scopes every objection.

Acceptance:

- No unresolved high-severity objection without an explicit scope statement.
- All numbers regenerate from evidence.

### P13.10 — Journal package and submission readiness

Why: fit and presentation decide desk rejection before methods are read.

Deliverables:

- Target-specific class file and metadata.
- 40–60 references, 5+ figures, cover letter, highlights, keywords.
- Author/affiliation/corresponding-author details approved by the PI.
- Final PDFs, clean build, artifact DOI, reviewer checklist.
- Submission only after maintainer approval.

Acceptance:

- Editor checklist passes.
- Public artifact resolves.
- No tag/release/submission without explicit approval.

## Sequencing

1. P13.1 TSP runtime and panel.
2. P13.2 independent QAP baseline.
3. P13.3 generic engine layer.
4. P13.4 third adapter.
5. P13.5/P13.6 Paper 1 experiments.
6. P13.7 public artifact and schema.
7. P13.8 sensitivity/statistics.
8. P13.9 independent review.
9. P13.10 journal package.

P13.7 and P13.8 can run alongside experiments. P13.9 is a gate, not a paper-writing task.

## Definition of done

- Every workstream issue closed with evidence.
- Both papers have a target-specific package and a clean build.
- The public artifact is available with DOI and license.
- The independent review has no unresolved high-severity objection.
- The PI has approved release and submission.

## Approval gates

The agent will not perform any of the following without explicit approval:

- repository visibility/settings change;
- tag or release;
- parent-phase close;
- manuscript submission.

## Reporting

- Update `ROADMAP.md`, `CHANGE_LOG.md`, and the relevant issue at each milestone.
- Write a short report in `notes/reports/` at each closeout.
- Run `python scripts/dashboard.py` before reporting a code/evidence milestone.
