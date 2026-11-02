# Audit remediation plan

Status: active
Date: 2026-11-02
Source: `notes/reports/antagonistic-audit-2026-11-02.md`

## Already corrected in this batch

- Audit C1 withdrawn: the 70M level targets are deliberate maximum-even-flow
  aspirations, not a feasibility failure.
- Paper 1 now reports the level/flow split and the 51.3–52.4M m³/period realized
  level; “near-zero” and “3.3 million times” framing removed.
- QAP `tai30a` certified budget corrected to 10k under the 0.10-point policy;
  40k/80k retained only as larger checks.
- Paper 1 scope remains architecture/reproducibility; no competitive model claim.

## P0 — before any more paper prose

1. **Workflow reconciliation**
   - Record the post-P10 PRs/releases in a new parent phase or an explicit
     post-phase maintenance record.
   - Fix `ROADMAP.md`, `README.md`, `notes/issue-bodies/p10.md`, and stale
     release manifests.
   - Acceptance: roadmap and GitHub agree; no phase says `pr-open` after its
     issue/PR is closed; post-P10 changes have a parent/child or explicit
     maintenance record.

2. **Objective replay gate**
   - Extend `check_benchmark_record.py` to load the pinned evaluator and check the
     objective, not just the schedule hash and boolean.
   - Add a negative test with a correct hash and wrong objective.
   - Acceptance: the current 11 Paper 1 records pass; a wrong-objective fixture
     fails.

3. **Per-target residuals and timing**
   - Add flow/level residual fields and realized per-period values to TSA24
     records; replace the `time_to_best_s` placeholder with a measured or
     explicitly null value; fix `time_to_first_feasible_s`.
   - Acceptance: Paper 1 table explains 515.14 level / 2.72 flow and 51.3–52.4M
     realized level without a “near-zero” claim.

4. **Committed broad runner**
   - Add `paper2/run_broad_converged.py` with `TSPLIB_ROOT`/`QAPLIB_ROOT`,
     solver version/commit, hardware, Python/NumPy/Numba/SciPy versions, and
     separate parse-error records.
   - Acceptance: the runner reproduces the 1,060 successful records and 25
     `esc8` parse failures from the pinned corpus.

## P1 — paper claims

5. **Paper 2 reframe or framework experiment**
   - Either implement one headline result through the generic engine/adapter
     contract, or retitle/reframe as a benchmark harness + reference adapters.
   - Remove the graph-colouring public-adapter sentence unless a real public
     adapter is added.
   - Acceptance: paper title/abstract matches the evidence.

6. **Large-QAP comparison**
   - Report mean/median/worst consistently; do not compare Fresh best with SciPy
     mean.
   - Add SciPy 2-opt or a published QAP heuristic baseline, or label FAQ as a
     weak baseline only.
   - Acceptance: one statistic per comparison; no portfolio-improvement claim
     unless mean improves.

7. **TSP scope**
   - Either run ILK on the broad panel or restrict the abstract to the
     four-instance ILK result.
   - Acceptance: abstract scope matches evidence.

8. **Paper 1 artifact**
   - Add an explicit LICENSE or research-use/source-license statement.
   - Pin WS4 GPU commit/table/cache build commands; add asset SHA-256.
   - Acceptance: a third party can rebuild at least the 1k record from the
     artifact plus public code.

## P2 — hygiene

9. Replace absolute `/srv/...` paths with environment variables/repo-relative
   paths in tracked replay scripts and evidence.
10. Update stale READMEs, progression guide, roadmaps, and release notes.
11. Pin LKH version/binary hash/command or mark the LKH evidence illustrative.
12. Create a new Paper 1/Paper 2 evidence release only after the above and with
    named maintainer approval.

## Stop conditions

- If the broad runner cannot be recovered, restrict Paper 2 to the 8-instance
  convergence panel and 4-instance ILK panel.
- If no framework-use experiment is possible, submit Paper 2 as a tool/benchmark
  paper, not a methods paper.
- If no independent model baseline is available, Paper 1 remains an
  architecture/reproducibility paper.
- No tags, releases, merges, or settings changes without the approval steps in
  `AGENTS.md`.
