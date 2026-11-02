# Antagonistic audit — UBC-FRESH programme, 2026-11-02

> **Post-audit correction (2026-11-02):** Critical finding C1 is withdrawn. The audit
> treated the harvest-level residual as a failure without reading the WS4/TSA24
> scenario documentation. The 70M level targets are **deliberate, unattainable
> pull-up aspirations**; the dominant even-flow target selects the maximum even-flow
> level. The 517.86 penalty is therefore the expected weighted compromise, not a
> metric artifact. See `ws4/notes/design/weighted-goal-programming-aspirations.md`,
> `ws4/docs/howto/even-flow.rst`, and `ws4/docs/concepts/the-objective.rst`. The
> “near-zero” and “3.3 million times” phrasing is still wrong and must be removed,
> but the result itself is valid under the scenario design.

Status: read-only audit
Auditor: independent subagent
Scope: `fresh-solutions-papers`, `fresh-solutions`, `ws4` / `ws4-gpu`, the public
`femic-tsa24-instance` artifact, and the GitHub issue/PR/release state.
Constraint: no code, data, issue, PR, tag, release, or setting was changed. The only
file created is this report.

## Method and material inspected

I checked the actual repositories rather than the summaries:

- `fresh-solutions-papers` at `main` = `32d2aab` (clean), submodule
  `fresh-solutions` = `1affc14` (`v0.8.0`);
- `fresh-solutions` at `main` = `1affc14` (`v0.8.0`), tags `v0.1.0`–`v0.8.0`;
- `ws4` public repository; GPU evidence code at `f60ce64` on
  `origin/feature/gpu-acceleration`, CPU-SA at `f23d450` on `main`;
- `femic-tsa24-instance` release `ws4-tsa24-evenflow-v1`, asset
  `ws4-tsa24-evenflow-v1.tar.gz` (4,660,158 bytes), downloaded and manifest-checked;
- all `evidence/*/record.json`, all `paper2/evidence/*` summaries, the two drafts,
  the claims audit, close-outs, roadmaps, changelogs, workflows, and source.

Commands run included `git status`, `git log`, `git ls-tree`, `git show`, `gh issue
list`, `gh pr list`, `gh pr view`, `gh release list`, the repository validators, the
full test suites, and independent replay of the evidence assignments.

Test/gate state observed:

```text
fresh-solutions-papers: 154 passed, 99.53% coverage (gate 95%)
fresh-solutions:       201 passed, 95.02% coverage (gate 95%)
mypy (papers):          Success, no issues in 14 source files
mypy (solver):          Success, no issues in 39 source files
ruff/format:            pass in both repositories
check_workflow.py:      0 errors, 3 recommended-file warnings (papers)
check_workflow.py:      0 errors, 0 warnings (solver)
all 11 Paper 1 records: VALID under scripts/check_benchmark_record.py
paper/tables/evidence.md regenerates byte-identically
```

Those green gates do **not** establish the scientific claims. The most important
findings below are about what the records mean, not whether the YAML/JSON parses.

---

# 1. Executive verdict

**Neither paper is submission-ready.** Paper 1 is defensible as an
architecture/reproducibility paper after removing its “near-zero”/“3.3 million
times” framing; its maximum even-flow result is valid under the documented
scenario design. Paper 2 is closer to an honest internal draft, but its central
“framework” thesis is not supported by its own strongest experiments.

What is defensible today:

- The evidence harness exists and is mostly reproducible at the level of
  “assignment + exact evaluator”: all 11 Paper 1 records replay numerically; the
  Paper 2 QAP/LK assignments I re-ran replay exactly.
- The QAP/TSP benchmark bookkeeping is better than the average internal project:
  budgets, seeds, known optima, stop reasons, and assignments are mostly present.
- The programme is candid in several places: both drafts are marked not
  submission-ready, the LKH boundary is correctly labelled external, the
  same-engine baseline is correctly labelled non-independent, and large-TSP
  failure is disclosed.
- The TSA24 release exists, is public, is 4.5 MB, and its SHA-256 manifest verifies.

What is not defensible:

- **Paper 1’s 517.86 headline is a metric artifact.** It is 99.5% harvest-level
  shortfall, not a near-zero solution. The model’s level target is 70,000,000
  m³/period; the 100k schedule realizes roughly 51–52M m³/period. The
  “3.3 million times lower” and “near-zero” language hides this. I recomputed the
  objective terms; see Critical C1.
- **Paper 1 has no controlled baseline and no independent model baseline.** The
  CPU-SA number is a single, untuned, non-equal-work run of the same WS4 codebase;
  it cannot support “orders of magnitude stronger”.
- **Paper 2’s broad 1,060-run panel cannot be regenerated from the repository.**
  The runner is missing, the README points at deleted evidence files, and the
  raw bundle contains 25 error records. See Critical C2.
- **Paper 2’s strongest results bypass the framework thesis.** `run_qap_tabu`
  and `run_tsp_lk` are standalone search loops in `adapters/`; they do not use
  the generic engine contract that the paper claims as the contribution. The
  “graph colouring public adapter” does not exist as a public-library adapter.
  See Critical C3.
- **The workflow is not in the state the roadmap claims.** P10 was closed and its
  PR merged, then 14 more PRs and five solver releases were merged/created without
  a new parent phase or the required named approval. The roadmap still says P10
  is `pr-open`. See Critical C4.
- **The public TSA24 artifact is accessible but not openly licensed and is not
  GPU-self-contained.** The repository has no `LICENSE`; the effect table and
  caches are excluded; the artifact does not pin the WS4 GPU commit or give the
  exact rebuild command. See High H5.

Minimum defensible claims today:

- Paper 1: a **systems/reproducibility case study** of a compiled-state
  architecture on a public TSA24 dataset, with exact numerical replay, a
  same-engine scaling curve, and an explicitly weak/uncontrolled CPU-SA
  comparator. It can say “the architecture makes this instance exact and
  replayable at this scale”. It cannot say “near-zero”, “orders of magnitude
  stronger”, “full 208k landscape”, or “competitive”.
- Paper 2: a **reproducible benchmark harness and adapter contract** with two
  reference QAP/TSP modules, one of which is an external LKH comparison. It can
  say “we provide a replayable harness and show QAP/TSP reference results on
  selected public instances”. It cannot say “general framework” or “adapter-level
  application” as a proven thesis until a headline result is produced through the
  generic contract.

---

# 2. Severity-ranked findings

## Critical

### C1. [WITHDRAWN] Paper 1’s 100k headline: level residual is intentional; “near-zero”/“3.3 million times” is still wrong

Evidence:

- `paper/paper1-draft.md:16-20` reports 517.8619818205188 as the 100k result and
  calls the CPU-SA baseline “independent”; `:131-149` reports the numbers and the
  3.3M×/16,600× comparisons; `:182` calls it “near-zero objective”.
- `evidence/ws4-tsa24-gpu-ga-100000-r7/record.json` records
  `result.target_penalties.total = 517.8619818205188`; the record has **no
  per-target breakdown**.
- I replayed the schedules with the pinned evaluator and decomposed
  `IncrementalObjective._terms()`:
  - 1,000 generations: total 8,588,725.37; flow term 8,588,225.55; level terms
    499.82;
  - 10,000 generations: total 76,540.74; flow term 76,026.91; level terms 513.83;
  - 100,000 generations: total 517.86; flow term **2.72**; level terms
    **515.14**;
  - CPU-SA: total 335,044,976.68; flow term 335,044,373.52; level terms 603.15.
- The target file (`config/ws4/targets/evenflow_tsa24.yaml`) sets a linear
  minimum of 70,000,000 m³ per 10-year period and an even-flow band of ±1%.
  The 100k schedule realizes roughly 51.4–52.4M m³/period and its flow maximum is
  1.014%, slightly outside the ±1% band. The level shortfall is ~25% below the
  stated aspiration, and it accounts for ~99.5% of the final objective.

**Withdrawn as a correctness finding.** The scenario documentation is explicit:
the 70M level targets are deliberately unattainable aspirations that pull harvest
upward; the weight-10,000 even-flow target selects the flattest profile at the
resulting maximum sustainable level. The 515-level / 2.72-flow split is the
intended behavior, not evidence that the result is invalid.

What remains valid from this finding:

- The paper must report the residual split and realized level (about 51.3–52.4M
  m³/period) rather than calling 517.86 “near-zero.”
- The paper’s §3 promise of “per-target residuals” is still not met by the
  records; the residual table should be added.
- The 3.3M×/16,600× phrasing should be removed as a headline; it compares
  penalties dominated by different terms, not target-quality improvements.
- No definitive proof of maximum even-flow is possible without an exact MIP; the
  paper must state that limitation.

What would be required:

- A per-period flow and level residual table for every record;
- a statement whether 70M is feasible or an aspiration;
- a decision to keep the penalty objective and report the floor, or to redefine
  the benchmark (e.g., maximize volume subject to even flow);
- removal of “near-zero” and the 3.3M×/16,600× framing unless accompanied by
  “relative to a seed whose penalty is dominated by the same flow term”.

### C2. Paper 2’s broad QAP/TSP evidence cannot be regenerated; the runner is absent and the documentation points at deleted files

Evidence:

- `paper2/benchmarks/README.md:27-28` points to
  `paper2/evidence/broad-suite-v051.json.gz` and
  `broad-suite-v051-summary.json`. Those files were deleted in `bf3a3c3`; the
  current files are `broad-converged.json.gz` and
  `broad-converged-summary.json` (`paper2/evidence/`).
- `paper2/evidence/broad-converged.json.gz` contains **1,085 records**: 390 TSP
  + 695 QAP. 25 of those QAP records are error records (`{"error": "ValueError:
  QAPLIB instance has the wrong number of entries"}` for `esc8b`–`esc8f`), so
  the actual successful campaign is 1,060 runs (390 TSP + 670 QAP).
- `notes/reports/broad-converged-v060.md:11` says “**1,085** scheduled runs;
  25 `esc8` parser errors”, which double-counts the errors as runs.
- There is **no committed runner** for the broad panel. A repository-wide search
  of `paper2/*.py` finds `run_converged.py` (8 cases), `run_multiseed.py` (8
  cases), `run_qap_tabu.py` (4 QAP cases), `run_tsp_lk.py` (4 TSP cases), and
  no script that generates `broad-converged.json.gz` or its summary. The only
  committed scripts that reference `/srv/.../bench-inventory` are the LKH and
  SciPy-large scripts (`paper2/run_lkh_large.py:21`,
  `paper2/run_qap_scipy_large.py:21`), not the broad panel.
- The evidence records have no solver version, commit, hardware, or software
  fields. The draft claims “pinned solver version or commit”, “wall time and
  hardware context” (`paper2-draft.md:70-79`), but the records do not carry them.
- The paper’s broad claims (134 QAP instances, 78 TSP instances, 552/670
  patience runs, 183 optima, median 0%) are therefore **summary-only**. The
  per-run assignments replay, but the campaign cannot be rerun from the
  repository, and the summary is not independently derivable without the missing
  script and the `/srv/...` instance inventory.

Why this is critical:

- The broad panel is the main breadth evidence for Paper 2’s “applied
  metaheuristics” claim. If the runner is missing, a reviewer cannot inspect
  instance selection, budget handling, cap treatment, or summary computation.
- The 25 error records show the raw artifact was not filtered or schema-checked;
  the summary silently drops them. That is recoverable, but only if the runner
  and filter are committed.

### C3. Paper 2’s framework thesis is not tested by its strongest results; the “graph colouring public adapter” claim is false

Evidence:

- `paper2/paper2-draft.md:11-20` says Fresh Solutions is “an adapter-based
  framework that separates those concerns from the search engine” and that the
  contribution is “adapter-level application of known-good methods”.
- The headline QAP result is produced by `paper2/run_qap_tabu.py`, which calls
  `fresh_solutions.adapters.qap_tabu.run_qap_tabu`. That function maintains its
  own permutation, tabu matrix, and delta matrix
  (`fresh-solutions/fresh_solutions/adapters/qap_tabu.py:196-346`); it does not
  use `fresh_solutions.engine.run_local_search`, the adapter `apply`/`undo`
  contract, or the population/hybrid paths.
- The headline TSP result is produced by `paper2/run_tsp_lk.py`, which calls
  `fresh_solutions.adapters.tsp_lk.run_tsp_lk`. It maintains its own edge sets
  and double-bridge perturbations (`tsp_lk.py`), again outside the generic
  engine.
- The generic engine and population search are exercised by the older
  convergence evidence (`paper2/run_converged.py`), but those results are much
  weaker (QAP 5–9%, TSP 3.7–8.2% in P9) and are not the paper’s headline.
- `paper2-draft.md:36` claims “public-library adapters for QAP, TSP, and graph
  colouring”. The only graph-colouring code is `fresh_solutions/toy.py`, the
  contract toy adapter. It has no public instance, no benchmark evidence, and is
  not a public-library adapter. `fresh_solutions.adapters.__init__` exports QAP,
  TSP, QAP tabu, LK, and LKH, but no graph colouring.
- The solver’s own guide admits the strongest modules are adapter-specific:
  `docs/heuristic-progression.rst:110-114` says “The tabu module is
  adapter-specific. It is not a replacement for the generic engine” and (stale)
  “TSP remains Or-opt-only … Lin–Kernighan is not implemented.”

Why this is critical:

- The paper’s thesis is about the framework, but the evidence demonstrates two
  standalone heuristics plus an external solver. A hostile reviewer will say:
  “You have written a benchmark harness and two problem-specific implementations;
  where is the framework experiment?”
- Either the paper must be reframed as a benchmark-harness/tool paper, or at
  least one headline result must be implemented through the generic adapter and
  engine, with an overhead/benefit measurement.

### C4. Workflow: P10 was closed, then 14 PRs and five solver releases landed without a new phase or named approval; the roadmap still says `pr-open`

Evidence:

- Papers P10 parent issue #31 is `CLOSED` (2026-11-01T22:34:02Z); PR #39
  (“P10: competitive evidence…”) is `MERGED` at 2026-11-01T22:33:58Z.
- `fresh-solutions-papers/ROADMAP.md:30` and `:225` still say
  `pr-open`; `notes/issue-bodies/p10.md:2` says `Status: pr-open` and
  `:5` says “Pull request: not opened yet”.
- After P10 closed, the papers repo merged PRs #40–#53
  (2026-11-01T22:39 through 2026-11-02T17:27), including new branches
  `feature/claims-audit`, `feature/paper1-gpu-100k`, `feature/paper1-gpu-multiseed`,
  `feature/tsa24-public-artifact`, and so on. None has a new parent phase issue;
  none has a phase close-out; none uses the `feature/p<n>-…` convention.
- The solver P10 parent #28 is `CLOSED` (2026-11-01T22:35:50Z); PR #30 merged
  at 22:35:47. `fresh-solutions/ROADMAP.md:24` and `:215` still say `pr-open`.
- After the solver P10 close-out, releases `v0.5.0`, `v0.5.1`, `v0.6.0`,
  `v0.7.0`, and `v0.8.0` were published (2026-11-01T22:57 through 2026-11-02T07:41).
  `notes/reports/p10-7-competitive-closeout.md:51` says “No new tag or release in
  P10”; the solver P10.1 PR body explicitly says “Tagging `v0.5.0` requires
  separate maintainer approval.”
- No close-out names the exact approval command for those tags/releases, as
  `AGENTS.md` requires. The workflow audit’s D4 already disclosed this pattern
  for earlier tags; it has recurred after the remediation boundary.

Why this is critical:

- The repository’s own contract says one phase = one parent issue = one branch =
  one PR, and no tag/release without a named approval. The current state violates
  both. The roadmap’s `pr-open` status is false.
- This is not a cosmetic bookkeeping issue: the Paper 1 100k evidence, the public
  artifact, and both drafts were added after the phase that supposedly closed.
  A reviewer cannot tell which close-out approved which claim.

---

## High

### H1. The CPU-SA “independent baseline” is an untuned, non-equal-work comparator and is used to claim “orders of magnitude”

- `paper/paper1-draft.md:162-167` says “The GPU path is orders of magnitude
  stronger despite a shorter wall budget.”
- The CPU-SA record (`evidence/ws4-tsa24-cpu-sa-100000-r7/record.json`) is a
  single run, 100,000 iterations, 32 threads, default SA parameters, starting
  from `seed_oldest_first_tsa24.csv`; it scheduled 204,413 blocks, not 208,255.
  The GPU run evaluates a population of 64 for 100,000 generations = 6.4M genome
  evaluations; the CPU-SA evaluates 100,000 single proposals. These are not the
  same work.
- The CPU-SA is implemented in the same WS4 codebase and uses the same exact
  evaluator; it is a separate algorithm path, not an independent implementation.
- The wall time is 1,875.12 s, which is 31.25 min, not 30 min; the run log says
  `time_limit_reached True` and `iterations 100000`. The record/paper call it a
  “30-minute cap” and “time-limited, not converged”.
- It is a straw man for “orders of magnitude”. At best it shows that the GPU
  path’s batched search is more effective per wall-second on this instance; it
  does not isolate architecture from implementation, tuning, or move set.

### H2. The QAP “certified budget” rule is misapplied for `tai30a`: the table uses 40k although 10k passes the stated rule

- Policy: `notes/reports/serious-budget-policy.md:39-50` says a campaign is
  converged for reporting when a further doubling improves the five-seed mean by
  ≤0.10 percentage points, and “the selected budget is the smallest budget that
  passes the check after any failed doubling”.
- Evidence: `paper2/evidence/qap-tabu-stability-summary.json` shows
  `tai30a`: 10k mean 0.7919276009737392, 20k mean 0.6996137823915131,
  improvement **0.09231381858222609 points**, and
  `converged_for_reporting: true`. That is ≤0.10, so 10k is the smallest
  passing budget.
- The paper table (`paper2/paper2-draft.md:96-104`) and P10.2 close-out
  (`notes/reports/p10-2-qap-tabu-closeout.md:29-37`) use **40,000** for
  `tai30a`, arguing “20k→40k improved by 0.293 points, so 20k was not certified”.
  That ignores the 10k→20k pass.
- The result at 40k is 0.407%, versus 0.792% at 10k. The table therefore reports
  a better number from a larger budget than the policy allows. This is exactly
  the “selection of best results” failure the policy was written to prevent.

### H3. The validator is a hash/flag gate, not an exact-replay gate; `time_to_best` and `time_to_first_feasible` are wrong

- `scripts/check_benchmark_record.py:104-118` validates JSON schema, checks
  `result.exact_replay` is true, checks the schedule exists, and checks its
  SHA-256. It never re-evaluates the objective. A record with a valid schedule
  hash and a false objective would pass. The test fixture
  (`tests/test_benchmark_record.py:9-64`) writes a schedule with one row and an
  objective of 0.0; the test passes without any evaluator.
- `paper/paper1-draft.md:103-105` says “The validator rejects missing schedules,
  hash mismatches, and schema violations” — true — but the paper calls this an
  “exact replay” gate and says “a record with `exact_replay: false` is not
  evidence”. The actual objective replay is in ad-hoc `replay.py` scripts, not in
  the gate.
- `run.time_to_best_s` is not time-to-best. For `ws4-tsa24-gpu-ga-100000-r7`,
  the summary says `best_generation: 67253` out of 100,000 and
  `search_s: 856.096`; the record sets `time_to_best_s: 856.096` (the full
  search). The actual best-generation time is roughly 575 s. The same error
  affects r1–r5: best generations 78,145 / 89,894 / 99,007 / 91,482 / 48,379
  vs records reporting full search time. `paper/tables/evidence.md` labels this
  column “Best s”, so the table is mislabelled.
- `time_to_first_feasible_s` is set equal to the search elapsed for the GPU
  records (9.381, 89.782, 856.096) even though the initial seed is a valid
  feasible schedule and the paper admits first-feasible was not instrumented.
  The field is a placeholder, not a measurement.
- The 100k records r1–r5 have no `replay.py`/`replay.out` beside them; only
  r7 does. I independently replayed all five and they match, but the committed
  artifact does not contain the replay entry points.
- `paper1-draft.md:142` says “All schedules are schema-valid, hash-verified, and
  exactly replayed.” The first two are true; the third is true only after
  ad-hoc replay, not via the stated gate.

### H4. Paper 2 evidence has no per-record solver pin, hardware, or schema; the repository pin is v0.8.0 while the reports claim v0.3/v0.4/v0.6/v0.7

- `paper2/evidence/qap-tabu-converged.json` keys:
  `assignment, budget_iterations, evaluations, history, instance, iterations,
  known_optimum, objective, optimality_gap_percent, optimum_kind, seed,
  stop_reason, wall_seconds`. No solver version/commit, no hardware, no
  software.
- `paper2/evidence/tsp-lk.json` keys similarly omit solver version/hardware.
- `paper2/README.md:6` says “Evidence release: Fresh Solutions v0.8.0”, `:10`
  says the evidence uses v0.3.0 and v0.4.0, and `:40` describes the QAP table as
  v0.4.0. The actual papers submodule is pinned to `1affc14` (v0.8.0)
  (`git ls-tree HEAD fresh-solutions`). A third party checking out the papers
  repo gets v0.8.0, not v0.4.0; the QAP v0.4.0 result cannot be regenerated
  without manually checking out a different solver commit, which is not recorded
  in any evidence file.
- The broad panel report says v0.6.0, LKH v0.7.0, large QAP v0.8.0; none of
  those pins is in the evidence files.
- The paper’s own evidence protocol (`paper2-draft.md:70-79`) requires pinned
  version/commit, hardware, and replay; the files do not meet it.

### H5. The public TSA24 artifact is accessible but not openly licensed, and it is not self-contained for GPU reproduction

- `gh api repos/UBC-FRESH/femic-tsa24-instance --jq .license` returns `null`;
  the repository has no `LICENSE` file. The release README says only “Source data
  retains BC government licences. This artifact is a derived benchmark bundle.”
  The Paper 1 records set `instance.license: null`.
- Without a license, “public” means “viewable”, not “reusable”. A journal or a
  third party cannot safely redistribute or build on it.
- The release contains `compiled/` (12 Parquet tables), `evenflow_tsa24.yaml`,
  `seed_oldest_first_tsa24.csv`, README, and manifest. It does **not** contain
  `runtime/gpu-effects/effects-lean.pt` (1.4 GB) or `runtime/gpu-cache/*`
  (2.0 GB); the README says rebuild them with “WS4 GPU tooling”.
- The artifact README does not name the WS4 commit (`f60ce64`), the branch
  (`feature/gpu-acceleration`), the exact `gpu-run` command, the table build
  command, or the cache build command. A third party cannot reproduce the 100k
  run from the artifact alone without reverse-engineering the WS4 CLI.
- The GPU code is public only on `origin/feature/gpu-acceleration`; the default
  `ws4` branch is CPU. `ws4-gpu` is a worktree of `ws4` at a later commit, not a
  separate public repository (`gh repo view UBC-FRESH/ws4-gpu` fails).
- The artifact is 4.5 MB; the caches are 3.4 GB. That is a legitimate size
  trade-off, but then the artifact must include a build recipe and pinned code.

### H6. The large-QAP “portfolio improvement” is not supported as stated; the SciPy comparison mixes best-of-five with mean

- `paper2/paper2-draft.md:114-128` says “This is a portfolio improvement over
  identity-start tabu.”
- Broad identity-start evidence (`paper2/evidence/broad-converged.json.gz`,
  QAP `n>100` records, 600 s cap) versus the multi-start evidence
  (`qap-multistart-converged.jsonl`, no cap):
  - `esc128`: identity 0.000% on 4/5 seeds, one 6.25%; multi-start best 0.000%,
    **mean 1.250%** — the mean is worse.
  - `tai150b`: identity 1.714–2.163%; multi-start best 2.008%, **mean 2.976%** —
    the mean is worse.
  - `tai256c`: identity 0.452% all seeds; multi-start best 0.350%, mean 0.413% —
    better.
  - `tho150`: identity 1.850–2.097%; multi-start best 0.166%, mean 0.507% —
    better.
  So the claim is true for 2/4 instances by mean, and “best of five” is
  mechanically expected to beat one start. The comparison also changes solver
  version (v0.6.0 identity vs v0.8.0 delta-matrix), start policy, and cap, so it
  does not isolate “portfolio”.
- SciPy comparison: `paper2-draft.md:124-128` says SciPy wins `tai150b`
  “(1.861% vs 2.008%)” and Fresh wins `tho150` “(0.166% vs 1.523%)”. The first
  is SciPy **mean** vs Fresh **best**; the second is Fresh **best** vs SciPy
  **mean**. The honest mean-vs-mean comparison is Fresh 2.976% vs SciPy 1.861%
  for `tai150b`, and Fresh 0.507% vs SciPy 1.523% for `tho150`. Use one statistic
  consistently and report all three.
- The SciPy baseline is only `method="faq"`, `maxiter=10000`, five seeds (same
  result each seed). It is a weak baseline; there is no published QAP heuristic
  or QAPLIB BKS comparison. The paper admits “mixed”, but the bar is too low for
  a competitive claim.

### H7. Paper 2’s abstract conflates a 4-instance ILK experiment with the 78-instance broad panel

- `paper2/paper2-draft.md:15-18` says “iterated Lin–Kernighan reaches a median
  gap of 0% on the converged TSP subset”.
- The ILK experiment (`paper2/evidence/tsp-lk.json`) is **4 instances**
  (`berlin52`, `kroA100`, `kroB100`, `ch150`); it reports 0% on three and 0.383%
  on `ch150`.
- The 78-instance broad panel’s “converged TSP subset” (`tsp`, 236 patience
  runs) has median 0%, mean 0.100%, but that panel is not the ILK experiment;
  the broad panel report says “nearest-neighbour start, iterated LK” but its
  runner is missing (C2), and the committed `run_converged.py` uses the generic
  population/SA path, not `run_tsp_lk`.
- The 4-instance ILK result is valid on its own; the abstract’s “converged TSP
  subset” implies the 78-instance panel. That is an overclaim.

### H8. Absolute `/srv/shared-data/...` paths are in tracked evidence, scripts, and reports, defeating third-party reproducibility and violating public-safety intent

Examples:

- `evidence/ws4-tsa24-gpu-ga-100000-r7/replay.py:13`:
  `INSTANCE = Path("/srv/shared-data/gep/ws4/femic/external/femic-tsa24-instance")`
- `evidence/ws4-tsa24-gpu-ga-10000-r7/summary.json:2-23` and the 100k summary:
  absolute `cache_dir`, `dataset`, `out_dir`, `table`, `targets`.
- `evidence/fhops-tiny7-sa-200-r42/replay.py:21`: absolute FHOPS path.
- `paper2/run_qap_scipy_large.py:21`: absolute QAPLIB root.
- `paper2/run_lkh_large.py:21`: absolute TSPLIB root.
- `notes/design/paper1-archive.md:30-39`: absolute FHOPS/WS4 replay commands.
- `notes/reports/p10-6-applied-case-plan.md:27`: absolute local fixture path.

`AGENTS.md` says “Keep raw transcripts, credentials, private data, and personal
paths out of tracked files” and “Use placeholders, repository-relative paths, or
environment variables in examples.” `check_workflow.py` only rejects `/home/` and
`/Users/`, not `/srv/`, so the validator reports green. The evidence is not
portable: a reader cannot run any replay script without creating the same
`/srv/shared-data/gep/ws4` tree.

### H9. The optional Numba path is excluded from type and coverage gates, yet it is the default accelerated path used for the headline large-QAP evidence

- `fresh-solutions/pyproject.toml:52-54` sets
  `module = ["fresh_solutions.adapters.qap_tabu_numba"]` with
  `ignore_errors = true`.
- `pyproject.toml:64-68` omits `fresh_solutions/adapters/qap_tabu_numba.py`
  from coverage.
- `qap_tabu.py:346-356` imports `qap_tabu_numba` whenever `accelerated=True`
  (the default) and uses `run_accelerated_numba` for symmetric zero-diagonal
  instances. The large-QAP v0.8.0 evidence is symmetric (or uses the general
  Numba path for `tai150b`), so the headline results run through code that no
  strict type check or coverage gate sees.
- `RELEASE_NOTES.md` (v0.8.0) admits “The Numba path is optional and excluded
  from the default type/coverage gate.” That is honest, but the paper does not
  state that the large-QAP campaign requires it, nor record the Numba version.
  Without Numba, the pure-Python `_run_accelerated` or the O(n³) reference path
  may not finish the same budget; the 468 s `tai256c` patience result is
  hardware/implementation dependent.
- I ran a parity check on small random symmetric QAPs (60 runs) comparing the
  Numba path to the reference; it matched. That reduces, but does not remove,
  the risk: the excluded module is the one that produced the numbers.

### H10. Stale, contradictory documentation is widespread enough to mislead a new reader or reviewer

- `fresh-solutions/README.md:17`: “P6 maintenance is complete … v0.2.0 is the
  current release.” Actual: v0.8.0.
- `fresh-solutions/docs/heuristic-progression.rst:114`: “TSP remains
  Or-opt-only … Lin–Kernighan is not implemented.” Actual: LK/ILK shipped in
  v0.5.0 and is a headline Paper 2 result.
- `fresh-solutions-papers/README.md:16`: “Phase 0 (bootstrap) is planned.”
  Actual: all ten phases are closed/merged.
- `fresh-solutions-papers/ROADMAP.md:30,225` and solver `ROADMAP.md:24,215`:
  P10 `pr-open`; actual P10 issues/PRs closed/merged.
- `notes/reports/paper1-gpu-100k.md:33` and
  `notes/reports/p10-5-baseline-closeout.md:42`: “TSA24 is reconstructable, not
  a public benchmark.” Actual: public release `ws4-tsa24-evenflow-v1` and
  current records say `availability: public`.
- `notes/design/paper1-archive.md:45`: same stale “local reconstructable
  fixture” claim; `:42` says “The WS4 GPU checkout has uncommitted
  launch-optimization work; preserve the patch before publication.”
- `paper2/README.md:6,10,40`: “Evidence release v0.8.0”, “using v0.3.0, the
  v0.4.0 QAP”, and “QAP robust tabu — v0.4.0”; the submodule is v0.8.0.
- `paper2/benchmarks/README.md:27-28`: references deleted
  `broad-suite-v051` files.
- `docs/heuristic-progression.rst` also omits QAP tabu and LK from the API
  index (`docs/api/index.rst` has no `qap-tabu` page), while the package exports
  them.

### H11. There is no current evidence release/tag for either paper; the only Paper 1 release is the pre-100k v0.1.0

- Papers tags: only `paper1-evidence-v0.1.0` (`git tag -l`). `gh release list`
  shows only “Paper 1 evidence artifact v0.1.0” (2026-11-01).
- The v0.1.0 manifest (`paper/release/manifest.json`) hashes only three records
  (FHOPS tiny7/small21, TSA24 1k) and still says
  `known_limits: ["tsa24 is reconstructable, not public", ...]`.
- The current draft cites 11 records, including 100k/CPU-SA and a public
  artifact published after v0.1.0. The manifest’s file hashes for
  `paper/paper1-draft.md` and `paper/tables/evidence.md` are from v0.1.0 and do
  not match current files; the manifest itself was not updated.
- There is no `paper2-evidence-v…` tag/release at all. `paper2/README.md:6`
  calls the solver release v0.8.0 the “Evidence release”, but that is a solver
  tag, not a frozen papers artifact.

### H12. LKH evidence lacks the external solver version, binary hash, and exact invocation; the binary is not present now

- `paper2/evidence/lkh-large.json` records only `"backend": "LKH-3 external"`.
  No LKH version, no binary SHA-256, no compiler/OS, no parameter file, no
  `LKH_BINARY` path.
- `paper2/run_lkh_large.py:21` hardcodes the TSPLIB root and uses
  `os.environ["LKH_BINARY"]`; the runner records wall time but not the command.
- `which LKH` returns nothing in the current environment; I could not rerun the
  100 LKH runs. The 71/100 optimum and 0.092% mean are therefore summary-only
  and depend on an unpinned external binary.
- The paper’s boundary (“external, research-use, not bundled”) is correct, but
  an external baseline still needs a version and reproducible invocation.

---

## Medium

### M1. “208,255 blocks” is the operable/candidate subset of a 458,708-block compiled dataset; “full instance” is ambiguous

- The release `compiled/blocks.parquet` has **458,708 unique block_ids**
  (I read it with `pyarrow.parquet`). The schedule has **208,255 unique
  block_ids**; the record sets `variables: 208255`; the GPU run log says
  `blocks 208255`.
- WS4’s `Optimizer.candidates()` filters to blocks whose selected fragment track
  has treatments (`engine.py:587-620`), so 208,255 is the number of decision
  blocks. That is a legitimate search universe, but the draft says “208,255-block
  TSA24 landscape” and “full 208,255-block instance”, which a reader will
  interpret as the whole compiled dataset. Say “208,255 operable/candidate
  blocks out of 458,708 compiled blocks” in the abstract, table caption, and
  artifact README.

### M2. The broad panel count is double-counted and the README points at removed files

- `notes/reports/broad-converged-v060.md:11` says “1,085 scheduled runs; 25
  `esc8` parser errors.” 78×5 + 134×5 = 1,060 successful runs; 1,060 + 25 error
  records = 1,085 raw records. Say “1,060 successful runs + 25 parse failures”.
- `paper2/benchmarks/README.md:27-28` points at deleted
  `broad-suite-v051` files. The current summary is
  `broad-converged-summary.json`; the current raw bundle is
  `broad-converged.json.gz`.
- The draft does not mention the 25 error records at all; the claims audit says
  “134 parseable” without noting that the raw artifact contains 139 QAP names.

### M3. The 100k campaign wall time and CPU-SA cap are slightly inconsistent with the underlying summaries

- Paper says five-seed campaign took `4,004.77 s`; the five record walls sum to
  3,995.906 s and `summary.json total_s` is 3,995.906. The 4,004.77 figure
  includes about 9 s of unstated overhead.
- 100k r7 record wall 941.51 s; summary total 932.211 s.
- CPU-SA record wall 1,875.12 s (31.25 min) versus a stated 30-minute cap; the
  run log says `time_limit_reached True` and exactly 100,000 iterations. Either
  the cap is 31.25 min or the iteration budget was the effective stop; state
  which.

### M4. The 100k repeat/identity claims lack the second artifact

- `evidence/ws4-tsa24-gpu-ga-100000-r7/README.md:9` says “Schedules: identical
  across repeated runs”; the record directory contains one schedule and one
  hash. There is no second schedule, second hash, or second summary in the
  evidence.
- The 10k repeat claim is supported only by `summary.json` (`out_dir` name
  `...repeat`) and the record note; the original schedule is not preserved.
- If “deterministic” is a claim, keep the repeat schedule/hash or a signed
  transcript.

### M5. Per-target residuals are promised but absent; the schema allows only a flat numeric map

- `paper1-draft.md:99-102` promises “per-target residuals”; every TSA24 record’s
  `result.target_penalties` contains only `total` and `initial_seed_objective`
  (e.g., `evidence/ws4-tsa24-gpu-ga-100000-r7/record.json:43-46`).
- The schema (`schemas/benchmark-record.schema.json:74`) permits
  `additionalProperties: number` but does not require named flow/level terms.
  The evidence contract is therefore weaker than the paper says.
- This is the same gap that hides C1.

### M6. Core adapter tests are thin relative to the claims; the LK double-bridge test is nearly tautological

- Solver coverage: `_permutation.py` 84%, `qap.py` 82%, `tsp.py` 89%,
  `tsp_lk.py` 90%, despite the overall 95.02% gate. The QAP/TSP modules are the
  scientific core.
- `tests/test_tsp_lk.py:107-114` asserts
  `_tour_edges(kicked) == _tour_edges(tour) or kicked != tour`. The second
  disjunct is true for almost any nontrivial perturbation; the test does not
  assert that the double bridge preserves the tour edge set (which is the actual
  invariant) or produces the expected four-segment reconnection.
- There is no test that `run_tsp_lk` reaches a known optimum on a nontrivial
  instance; the tests use a 6-city line and a 3-city case. The evidence campaign
  is the only real quality test.
- `test_qap_tabu_accelerated_matches_reference` is good but small; the
  excluded Numba path has only indirect parity coverage.
- The QAP parser’s `esc8` failure is a known bug (extra header token) with no
  regression test; the broad panel simply records five parse errors.

### M7. QAP instance selection is broad but shallow at the large end; the “134 parseable” panel is dominated by n≤100

- Broad QAP: 130 instances at n≤100, 4 at 100<n≤300 (`esc128`, `tai150b`,
  `tai256c`, `tho150`). The paper’s large-QAP table is exactly those four.
- QAPLIB’s harder/larger entries (`tai100a/b` at n=100, `sko100*`, `wil100`,
  etc.) are at the boundary; there is no n between 100 and 128 and no
  n>256. The “broad QAP” claim is true for small instances but not for the
  competitive QAP tail.
- The QAP “median 0%” over 552 converged runs is dominated by easy small
  instances; it is not evidence of competitive QAP quality. The paper does say
  the median is not the tail, but the abstract leads with median 0%.

### M8. The SciPy FAQ baseline is weak and the comparison is not budget-matched; the paper says so but still uses it as the only independent QAP baseline

- `paper2/run_qap_scipy_baseline.py` and `run_qap_scipy_large.py` use only
  `method="faq"`, `maxiter=10000`; no `2opt` refinement, no published QAP
  heuristic, no QAPLIB BKS comparison.
- SciPy returns the same assignment for all five seeds on the small and large
  panels (zero variance), so the “five seeds” is cosmetic.
- The tabu runs take 2–139 s on small instances and 80–428 s on large; SciPy
  takes milliseconds. The paper labels this “time-quality”, but the wall-time
  gap is so large that the comparison mostly says “a fast approximate method is
  fast and approximate”. A serious QAP baseline (e.g., published robust tabu,
  breakout local search, or a budget-matched SciPy 2opt) is needed.

### M9. The LKH large-tail comparison is capability-only and uses a different budget; that is disclosed, but the paper still needs a matched statement

- LKH runs one run per seed with a 600 s timeout; internal LK runs are
  patience-stopped/capped. The paper says “not a matched budget comparison” and
  “capability, not equal-time”; good.
- But the abstract says “external LKH remains substantially stronger on large
  TSP” without the budget caveat. Add “at this budget and configuration” or
  report a matched-time comparison.
- The LKH mean wall 4.88 s is suspiciously low for 318–1000-city instances; it
  is plausible for LKH, but without a version/hash it cannot be checked.

### M10. Paper 2 instance documentation is incomplete and the evidence bundle does not include the 78/134 instance files

- `paper2/instances/README.md` documents only `tai12a`, `berlin52`, `tai20a`,
  `kroA100`; it omits `tai25a`, `tai30a`, `kroB100`, `ch150`, which are used in
  the headline tables.
- The broad panel’s 78 TSP and 134 QAP files live under
  `/srv/.../tmp/bench-inventory`; the repository contains only 8 instance files.
  The manifest lists names/known values but not the data or a download script.
- The `paper2/benchmarks/manifest.json` pins mirror commits (good), but the
  README’s “Full records” link is stale and there is no script to fetch/pin the
  corpus.

### M11. Paper 1 release manifest is stale and the current draft is not the released draft

- `paper/release/manifest.json` hashes `paper/paper1-draft.md` at
  `b8601d47…`; the current draft is different (it includes 100k, CPU-SA, public
  artifact). The manifest’s `known_limits` still says TSA24 reconstructable.
- The tag `paper1-evidence-v0.1.0` is a historical artifact; that is fine, but
  the repository must either (a) create a new evidence tag for the current
  claims, or (b) stop citing the current draft as if it were released.

### M12. The Paper 1 “FHOPS” citation and record metadata are incomplete

- `evidence/fhops-tiny7-sa-200-r42/record.json:5-8` sets `doi: null` and cites
  “SoftwareX 36” without the DOI; Crossref resolves
  `10.1016/j.softx.2026.103147` for the FHOPS paper. Fill the DOI or mark it
  unverified.
- The FHOPS baseline is correctly labelled “not an architecture comparison”, so
  this is metadata hygiene, not a claim failure.

### M13. QAP tabu API documentation is missing; the progression guide is stale in the opposite direction

- `fresh-solutions/docs/api/index.rst` lists `contracts`, `engine`, `search`,
  `benchmarks`, `lkh`, `tsp-lk`; no `qap-tabu` page, even though
  `QapTabuConfig`/`run_qap_tabu` are public exports.
- `docs/heuristic-progression.rst:114` says LK is not implemented; it should
  describe the v0.5+ ILK stage and its extra-budget caveat.
- This matters because the README/RTFM surface is the public claim surface for
  the solver.

### M14. Solver version/citation metadata has small inconsistencies

- `fresh-solutions/CITATION.cff` says `date-released: 2026-11-01`; v0.8.0 was
  released 2026-11-02. The `version: 0.8.0` is correct.
- `fresh-solutions/README.md` is stale (see H10).
- The release notes are cumulative but the README status is not generated from
  them, so they diverge.

---

## Low

- **L1.** `paper2/evidence/broad-converged.json.gz` raw QAP names include
  `esc8b`–`esc8f` with `error` fields; the summary filters them. A reader who
  opens the raw file sees 139 QAP names while the paper says 134. Add a manifest
  field `parse_failures: 5` and keep the error records in a separate file.
- **L2.** The Paper 1 evidence table column “Best s” is populated from
  `time_to_best_s`; because that field is wrong (H3), the column is wrong.
- **L3.** `paper1-draft.md` date is 2026-11-01 but the content includes
  2026-11-02 evidence and the public artifact published 2026-11-02; update the
  date/status line.
- **L4.** `notes/reports/paper1-gpu-100k.md` still says “TSA24 is
  reconstructable, not a public benchmark” while the record says `public`; this
  is the most visible stale contradiction.
- **L5.** `paper2/README.md` says “DO NOT SUBMIT … smoke tests” at the top while
  the rest describes 1,085-run campaigns and headline tables; the status line
  and the body are from different stages.
- **L6.** `paper2/benchmarks/README.md` says “QAP: robust tabu, 10,000-iteration
  patience” but the large-QAP evidence uses `patience=10_000` with
  `iterations=1_000_000` and no cap; the general statement is fine, but the
  table should state the per-instance budget.
- **L7.** The artifact README says “self-contained WS4 compiled landscape” but
  the GPU path is not self-contained (H5); change “self-contained” to
  “CPU-self-contained; GPU requires the caches/effect table”.
- **L8.** `paper/release/clean-checkout.log` says “wrote
  paper/tables/evidence.md (3 records)”; the current table has 11 records. It
  is a historical log, but the repository does not label it as such.

---

# 3. Paper 1 — detailed assessment

## 3.1 Is the architecture/reproducibility scope coherent with the evidence?

Partially. The scope decision (`notes/reports/paper1-scope-decision.md`) is the
right response to the missing independent baseline: it explicitly says “no
competitive win without an independent model baseline.” But the draft still
leads with a competitive-sounding “3.3 million times lower” and “orders of
magnitude stronger”, and the abstract presents 517.86 without the level-target
residual. The scope and the prose are not yet aligned.

A coherent architecture/reproducibility paper can be written from the current
material if it does the following:

1. states that the contribution is the compiled-state/evidence architecture,
   not solver superiority;
2. reports the target residuals and explains the 70M/52M gap;
3. presents the 1k/10k/100k curve as same-engine scaling, not a win;
4. presents CPU-SA as an uncontrolled secondary comparator, not proof;
5. includes architecture ablations (cache load vs search, effect table vs
   direct evaluation, GPU vs CPU per evaluation);
6. pins and packages the artifact so a third party can rebuild the GPU table.

Without (2) and (5), the paper is a description of a system plus one scaling
curve, not an evaluation of the architecture.

## 3.2 Is the GPU-GA 100k five-seed result valid and correctly recorded?

The assignments are valid and replay numerically. The five objectives
(512.574–518.621), mean 515.682, median 515.938, and seed-7 517.862 are correct.
The schedules hash-match, and I replayed all five. The record does not establish
that 100k is converged: best generations are 48,379–99,007, and seed 3 improved
at generation 99,007. The paper does not claim convergence, so that is honest.

The recording is not fully correct:

- `time_to_best_s` is the full search time, not the best-generation time (H3);
- `time_to_first_feasible_s` is a placeholder;
- there is no per-target residual breakdown (M5);
- r1–r5 have no replay scripts (M4/H3);
- the repeat/identical-schedule claim lacks a second artifact (M4);
- the `target_penalties.total` is the objective, not a penalty decomposition;
- the 4,004.77 s campaign wall does not match the 3,995.906 s summary.

## 3.3 Is CPU-SA a genuinely independent-search baseline? What can/cannot be inferred?

It is a separate **algorithm path** in the same WS4 codebase, sharing the model,
target, evaluator, and hardware. It is not an independent implementation, and it
is not a controlled baseline. It is a single 100k-iteration SA chain with default
parameters, started from the oldest-first seed, on 204,413 scheduled blocks. The
GPU run is a population of 64 for 100k generations (6.4M genome evaluations).
The budgets are not comparable, and the SA was not tuned.

What can be inferred: the GPU path found a much lower penalty at a lower wall
time on this instance and seed. What cannot be inferred: that the architecture
is the cause, that CPU-SA is a strong baseline, or that the GPU path is
“orders of magnitude” better in general. A fair baseline would be a tuned CPU-SA
at the same wall/evaluation budget, and ideally a CPU-GA with the same
population/genetics, plus a per-evaluation throughput comparison.

## 3.4 Is TSA24 actually public now? Is the artifact complete enough for GPU reproduction?

It is publicly accessible: `gh release view ws4-tsa24-evenflow-v1` shows a
published, non-draft, non-prerelease asset; the manifest verifies. It is not
openly licensed (no `LICENSE`, `license: null`). “Public” in the paper should be
“publicly accessible, license pending” until the license is added.

The artifact is complete for CPU-SA reproduction (compiled data + target + seed +
manifest + README). It is **not** complete for GPU reproduction: the effect table
(1.4 GB), candidate cache (2.0 GB), simulator cache, and exact WS4 GPU commit are
excluded/unpinned. The README says rebuild with “WS4 GPU tooling” but does not
give the command, the branch, or the table-build parameters. A GPU-capable third
party can probably rebuild it, but not from the artifact alone and not without
expert knowledge.

## 3.5 Is the public artifact licensing/provenance sufficient?

No. The provenance text is a good start: UBC-FRESH owns the instance repository,
the source is public BC VRI/FADM/SiteProd, and the artifact is a derived bundle.
But there is no license for the derived bundle, and the source layers’ licenses
are not named (BC government licenses vary). A journal will require a data
availability statement and a license; a third party needs to know whether
redistribution and commercial use are allowed. Add a `LICENSE` (or a clear
“research use only, source data licenses apply” statement) before calling it a
public benchmark artifact.

## 3.6 What independent model baseline or public-instance comparison would be required?

At least one of:

1. **Same public instance, independent solver/model:** run an independent
   harvest-scheduling model/solver (e.g., a published MIP/CP formulation on a
   reduced TSA24, an open Woodstock/FSOS-class model, or a published
   Lockwood/Moore/Boston-Bettinger reconstruction) with the same objective and
   feasibility rules, and report gap/time.
2. **Published benchmark instance with known BKS:** reconstruct a published
   spatially explicit harvest-scheduling instance with a known optimum/BKS and
   compare.
3. **Strong same-model baseline:** a tuned CPU-SA and CPU-GA at matched
   wall/evaluation budgets, plus a per-evaluation throughput comparison. This is
   not an independent model, but it makes the architecture claim testable.
4. **Architecture ablation:** show that the compiled/effect-table path is faster
   than a direct evaluator at the same search, and that GPU population evaluation
   is faster than CPU batched evaluation at the same population/generation.

Without (1) or (2), the paper should be a systems/reproducibility paper and
should not use “competitive”, “orders of magnitude”, or “state-of-the-art”.

## 3.7 Is the paper plan realistic? What to remove/add

The current plan is realistic **only** as a systems/reproducibility paper. It is
not realistic as a competitive landscape-scheduling paper on the current
evidence. Remove:

- “3.3 million times” / “16,600 times” as headline framing;
- “near-zero objective” without the level residual;
- “orders of magnitude stronger” from the CPU-SA comparison;
- “full 208,255-block landscape” unless clarified as operable blocks;
- any implication that CPU-SA is an independent model baseline.

Add:

- per-period flow/level residuals and an explicit “target feasibility” table;
- a target-feasibility discussion (is 70M achievable? what is the maximum
  sustainable even-flow?);
- a CPU-SA/CPU-GA matched-budget experiment and a per-evaluation throughput
  table;
- an architecture ablation;
- a clean-room GPU reproduction recipe and a pinned WS4 commit;
- a license for the artifact;
- a new evidence tag/release for the current records.

---

# 4. Paper 2 — detailed assessment

## 4.1 Is the framework/methods thesis defensible at the current evidence level?

Not as written. The paper claims an adapter framework that separates problem
representation, exact state, and search. The generic engine and adapter contract
exist and are tested (`fresh_solutions/contracts.py`, `engine.py`,
`population.py`), but the strongest results are produced by two problem-specific
loops (`qap_tabu.py`, `tsp_lk.py`) that do not use the engine’s apply/undo or
population paths. The paper’s own guide says the tabu module is
“adapter-specific … not a replacement for the generic engine”
(`docs/heuristic-progression.rst:110-114`). The evidence therefore supports
“two reference implementations plus a harness”, not “a framework that makes
adapter-level application reproducible” as a tested thesis.

The paper can be defensible in one of two forms:

- **Tool/benchmark paper:** the contribution is the harness, the evidence
  protocol, and the two reference adapters; the results are case studies; the
  large-TSP boundary is explicit. This is the closest to the current evidence.
- **Methods paper:** at least one headline result must be implemented through
  the generic adapter/engine, with a controlled comparison (framework vs
  standalone), and a third public adapter (not just QAP/TSP) to support
  “general”.

## 4.2 Are the QAP/TSP comparisons and LKH boundary honest?

Mostly honest in tone, but the details are not all honest:

- The LKH boundary is correctly stated as external, not bundled, research-use,
  and not Fresh Solutions’ own heuristic. Good.
- The QAP “portfolio improvement” is overstated (H6).
- The SciPy comparison is mixed-statistic and weak (H6/M8).
- The certified budget is misapplied for `tai30a` (H2).
- The ILK abstract conflates 4 instances with 78 (H7).
- The broad panel cannot be regenerated (C2).
- The QAP/TSP evidence lacks hardware/version metadata (H4).

## 4.3 Does the broad panel support the claims or expose insufficient breadth/depth?

It exposes both breadth and shallow depth. 134 QAP + 78 TSP instances is a
credible breadth claim for a harness, but:

- only 4 QAP instances are n>100;
- only 20 TSP instances are n>300, and 97/100 of those runs hit the cap;
- the strongest TSP ILK result is 4 instances;
- the QAP median 0% is dominated by small/easy instances;
- there is no published QAP heuristic baseline, only SciPy FAQ;
- there is no runner, no hardware, and no schema for the 1,060 successful runs.

So the broad panel supports “the harness can run a broad public corpus and
report the tail honestly”, not “the solver is competitive across QAPLIB/TSPLIB”.

## 4.4 Is the LKH wrapper genuinely optional and not presented as Fresh Solutions’ own heuristic?

The wrapper is genuinely optional: `lkh.py` only invokes a user-supplied binary;
`pyproject.toml` has no LKH dependency; the binary is not bundled. The paper says
“optional external research-use software, not bundled and not claimed as Fresh
Solutions’ own heuristic” (`paper2-draft.md:158-161`), and the release notes say
the same. This is one of the honest parts.

Caveats: the evidence does not pin the LKH version/hash, and the `v0.7.0`
release notes are in the solver repo while the LKH evidence is in the papers
repo; a reader must connect two repositories. Add a `LKH_VERSION` and command to
the evidence.

## 4.5 What is missing for a credible submission, and what claims should be dropped?

Missing:

- a committed broad-panel runner, schema, and hardware/version metadata;
- a fixed QAP certification table that follows the policy;
- a stronger independent QAP baseline (published heuristic or SciPy 2opt at a
  matched budget);
- a framework-use experiment or a reframing as a tool paper;
- a third public adapter if “general framework” is claimed;
- a TSP ILK campaign on more than 4 instances, or a narrower abstract;
- an LKH version/hash/command;
- a license and a papers evidence tag.

Drop:

- “public-library adapters for … graph colouring” (toy only);
- “portfolio improvement” without the mean caveat;
- “certified” if the `tai30a` budget stays at 40k without explanation;
- “ILK median 0 on the converged TSP subset” (4-instance conflation);
- any “state-of-the-art”, “universal”, “converged” for cap hits, or “general
  framework” claim not backed by a generic-engine experiment.

---

# 5. Solver/software correctness

## 5.1 QAP tabu

What I checked:

- `_swap_delta` against full evaluation on 100 random asymmetric QAPs: exact
  (max error < 1e-9).
- Pure delta-matrix path vs reference on 100 random symmetric QAPs: exact
  objective/assignment match.
- Numba path vs reference on 60 random symmetric QAPs: exact match.
- `qap-multistart-converged.jsonl` all 20 assignments replay exactly against the
  QAPLIB files.

No algorithmic bug found in the delta update for the tested sizes. The code is
careful about the symmetric-zero-diagonal guard and uses a general Numba scan for
asymmetric instances.

Concerns:

- The Numba path is excluded from type/coverage gates (H9).
- `run_qap_tabu` defaults to `accelerated=True`; the “reference” path is only
  used when explicitly requested or when NumPy/Numba is absent. The paper should
  say which path produced the evidence.
- The tabu aspiration uses `candidate >= best_objective`; standard robust tabu
  usually allows a tabu move only if it strictly improves the best. This is a
  minor semantic difference, not a correctness bug, but it should be documented.
- The `max_seconds` check is once per iteration; for large `n`, an iteration can
  exceed the cap by a full O(n²) scan. The evidence uses no cap for the
  large-QAP campaign, so not a result issue.
- `qap_tabu_numba.py` imports `numba` at module import; if Numba is installed but
  broken, the `ImportError` catch may not catch e.g. `OSError`/`LLVMError`. The
  fallback is not robust to a partially installed optional dependency.
- The QAP parser does not handle the `esc8` extra header token (25 parse errors
  in the broad panel). This is a known gap, not fixed.

## 5.2 TSP LK

What I checked:

- LK finds the brute-force optimum on 20 random 5–8 city TSPs with
  `candidate_count=n-1`, `max_depth=4`, 20 kicks.
- The 20 evidence tours replay exactly.
- The double-bridge implementation preserves the permutation; the test for the
  edge-set invariant is weak (M6).

Concerns:

- The implementation is a candidate-list variable-depth sequential exchange
  with `max_depth=4`, not full Lin–Kernighan. The paper calls it
  “Lin–Kernighan”; that is acceptable only if it is described as a bounded
  LK-style implementation. The module docstring does say “sequential
  edge-exchange search,” but the paper should carry that qualifier.
- The LK pass is first-improvement and reconstructs the tour from an edge set;
  it is exact for the exchange it tests. I did not find an invalid-tour bug.
- The evidence is 4 instances. The abstract’s 78-instance implication is the
  problem (H7), not the code.
- The `search_seconds` field is measured inside `run_tsp_lk`; the evidence
  `wall_seconds` is measured outside. Both are present in `tsp-lk.json`; good.
- There is no test for `_tour_from_edges` rejecting a disconnected 2-regular
  graph, no test for candidate-list edge cases, and no test for `max_depth`
  semantics. The core search loop is under-tested relative to its role.

## 5.3 LKH wrapper

- The wrapper writes an explicit FULL_MATRIX TSPLIB file, calls the user binary,
  parses `TOUR_SECTION`, and re-evaluates exactly. The fake-backend tests cover
  success, missing binary, non-zero exit, and malformed tour.
- It does not record the LKH version/hash/command (H12).
- It does not wrap `FileNotFoundError` from reading a missing tour file; a
  backend that exits 0 without writing a tour raises `FileNotFoundError`, not
  `RuntimeError`. Minor.
- `LkhConfig()` default `binary="LKH"` ignores `LKH_BINARY`; only
  `run_lkh(config=None)` reads the env var. Minor API inconsistency.
- It uses `RUNS`/`SEED`, but does not set `MAX_TRIALS` or a time limit in the
  parameter file; the Python subprocess timeout is the only cap. The evidence
  uses 600 s; fine, but document it.

## 5.4 Tests, type checks, coverage

- Both repositories pass ruff, format, mypy strict, pytest, and the coverage
  gates. That is a real strength.
- The coverage gate is overall, not per-module; core adapters are 82–90%.
- The optional Numba module is entirely outside the gates (H9).
- The LK double-bridge test is weak (M6); the QAP parser `esc8` bug has no test.
- The papers validator tests prove schema/hash behavior, not objective replay
  (H3).

## 5.5 Version/tag/commit pinning

- `fresh-solutions` tags exist for v0.1.0–v0.8.0; `v0.8.0` points to `1affc14`
  (peeled), and the papers submodule is `1affc14`.
- Paper 1 records pin `ws4-gpu@f60ce64` and `ws4@f23d450`; both commits exist
  in the public `ws4` repository (f60ce64 on `origin/feature/gpu-acceleration`).
- Paper 2 evidence files do **not** pin their solver version; the reports carry
  the pins, the files do not (H4).
- The papers repo does not pin WS4 at all; only the record notes/URLs do.
- The TSA24 artifact is a separate release, not a submodule commit; the record
  notes the URL but not the asset SHA-256.

---

# 6. Evidence/reproducibility

## 6.1 What is reproducible today

- Paper 1: all 11 `record.json` files pass the schema/hash gate; the 1k, 10k,
  100k-r7, CPU-SA, FHOPS records have replay scripts; I replayed the 100k
  r1–r5 assignments and they match. The schedules are in-repo.
- Paper 2 QAP/LK: the 20 certified QAP records and 20 LK records replay exactly
  with `replay_qap_tabu.py` / `replay_tsp_lk.py`; the 20 multi-start QAP records
  replay exactly with a small ad-hoc script (no committed replay entry point).
- The QAPLIB/TSPLIB 8 instance files are in `paper2/instances`; the broad 212
  instances are not.

## 6.2 What is not reproducible

- The broad 1,060-run panel (missing runner, no hardware/version).
- The LKH 100-run panel (no version/hash, external binary absent).
- The QAP v0.4.0 certified campaign from the papers checkout (submodule is
  v0.8.0; no per-record pin).
- The GPU 100k campaign from the artifact alone (effect table/caches excluded,
  no pinned commit/command).
- The FHOPS records without the `/srv` FHOPS checkout (absolute path).
- The paper1 v0.1.0 release manifest does not describe the current evidence.

## 6.3 Evidence schema issues

- Paper 1 schema is well-formed but weak: `target_penalties` is an unconstrained
  numeric map; `time_to_first_feasible_s`/`time_to_best_s` are required but not
  semantically validated; `exact_replay` is a boolean, not a replay result;
  `deterministic` is a claim, not a check.
- Paper 2 evidence has no schema. The paper claims an evidence protocol; the
  files do not implement it.
- The validator’s name (`check_benchmark_record`) and docstring (“exact-replay
  schedule hash”) overstate what it does (H3).

## 6.4 Data roots and paths

- `/srv/shared-data/gep/ws4/...` appears in tracked evidence, scripts, and
  reports (H8). This is both a portability failure and a violation of the
  repository’s public-safety rule.
- The broad panel uses `/srv/.../tmp/bench-inventory`; no in-repo fetch/pin
  script.
- The artifact uses relative paths (good), but the replay scripts use absolute
  paths (bad).

## 6.5 Repository hygiene

- The papers repo is 32 MB of evidence, 36 MB `.git`; no LFS. The schedules are
  3.6 MB each; 8 schedules are ~28 MB. That is acceptable for a private papers
  repo but should be compressed or LFS if it goes public.
- No credentials/private data were found in tracked files (good), but absolute
  `/srv` paths and local fixture paths are present (H8).
- The TSA24 artifact is 4.5 MB and manifest-clean (good), but unlicensed (H5).
- `paper2/evidence/multiseed.json` is 6.9 MB and includes assignments; fine,
  but it is not schema-validated.

---

# 7. Workflow and operations

## 7.1 Roadmap / issue / PR consistency

Observed via `gh issue list` and `gh pr list`:

- Papers: all issues #1–#38 closed; all PRs #7–#53 merged; zero open issues/PRs.
- Solver: all issues #1–#29 closed; all PRs #6–#39 merged; zero open issues/PRs.
- Papers roadmap: P10 `pr-open`; solver roadmap: P10 `pr-open`.
- Papers README: “Phase 0 planned”; solver README: “v0.2.0 current”.
- `notes/issue-bodies/p10.md`: “Pull request: not opened yet”.

This is a direct contradiction. A new session following `AGENTS.md` (“read the
roadmap, then the latest changelog”) will be misinformed.

## 7.2 Phase/branch/PR discipline

- P10 papers: parent #31, children #32–#38, branch
  `feature/p10-competitive-benchmark`, PR #39. That part is compliant.
- P10 solver: parent #28, child #29, branch `feature/p10-tsp-lk`, PR #30. That
  part is compliant.
- After close-out: papers PRs #40–#53 and solver releases v0.5.0–v0.8.0 are
  **not** under a parent phase, child issue, or close-out. They use ad-hoc
  branches (`feature/paper1-gpu-100k`, `feature/claims-audit`,
  `feature/qap-delta-matrix`, `release/v0.8.0`). This violates the one-phase/
  one-branch/one-PR rule and the “phase ends with a close-out package” rule.
- `fresh-solutions-papers` feature branches remain on the remote after merge
  (e.g., `feature/claims-audit`, `feature/paper1-gpu-100k`), contrary to the
  close-out instruction to delete the feature branch. This is minor hygiene but
  part of the same drift.

## 7.3 Approval gates

- `AGENTS.md` requires an explicit approval naming each tag/release command.
- `notes/reports/p10-7-competitive-closeout.md:51` says “No new tag or release
  in P10.”
- The solver P10.1 PR body says “Tagging `v0.5.0` requires separate maintainer
  approval.”
- `gh release list` shows v0.5.0 (2026-11-01T22:57), v0.5.1 (23:27), v0.6.0
  (2026-11-02T03:03), v0.7.0 (06:21), v0.8.0 (07:41). No close-out names the
  approval commands. This is a recurrence of D4, not a new rule.
- The TSA24 public release `ws4-tsa24-evenflow-v1` was published 2026-11-02T16:46;
  no close-out names the approval for the public artifact/repo release.

## 7.4 Disclosed deviations and new ones

Disclosed (`notes/reports/workflow-conformance-audit.md`): D1 inline checklists,
D2 direct main commits, D3 missing close-out sections, D4 tag/release approval
gaps, D5 drafts before evidence, D6 ad-hoc P9. These are still visible in
history.

New/undisclosed:

- Post-P10 continuation without a parent phase/child issue/close-out (C4).
- Solver releases v0.5.0–v0.8.0 after P10 close-out without named approval
  (C4/H11).
- Current evidence/draft after the only Paper 1 tag, with a stale manifest
  (H11/M11).
- Absolute `/srv` paths in tracked evidence/scripts (H8).
- Stale roadmap/README statuses (H10).
- Claims audit marks “Supported” without schema-valid per-record evidence and
  without the missing broad runner (C2).

## 7.5 Are evidence files, manifests, data roots, and scripts third-party reproducible?

No, not end-to-end:

- Paper 1 assignments replay if you can reconstruct the `/srv` tree and the WS4
  code; the public artifact does not include the effect table/caches, and the
  replay scripts use absolute paths.
- Paper 2 QAP/LK assignments replay from the 8 in-repo instances; the broad
  panel and LKH do not.
- Manifests are inconsistent: Paper 1 manifest is v0.1.0; Paper 2 has no
  manifest of evidence files (only an instance manifest).
- Data roots are local absolute paths, not environment variables or relative
  paths.

---

# 8. Claim-by-claim table

Legend: **S** supported by a schema-valid/replayed record; **P** partially
supported (true number, but overstated/ambiguous/missing artifact); **U**
unsupported; **?** unknown/not verifiable from the repository.

| # | Claim (source) | Status | Basis / problem |
| --- | --- | --- | --- |
| 1 | Compiled-state architecture separates model, state, search (`paper1-draft.md:8-12`) | P | Design note and code exist; no architecture ablation; GPU result does not isolate the architecture. |
| 2 | 208,255-block TSA24 landscape (`paper1-draft.md:12,131`) | P | 208,255 operable blocks; compiled blocks.parquet has 458,708. Clarify. |
| 3 | 1k GPU objective 8,588,725.370498, exact replay (`paper1-draft.md:133-134`) | S | Record + replay.out; numeric match. |
| 4 | 10k GPU objective 76,540.740733 (`paper1-draft.md:135-136`) | S | Record + replay; exact within float64. |
| 5 | 100k GPU objective 517.8619818205188 (`paper1-draft.md:137-138`) | P | Numeric record/replay; 99.5% of it is unmet level target; “near-zero” unsupported. |
| 6 | Five-seed 100k 512.574–518.621, mean 515.682, median 515.938 (`paper1-draft.md:139-140`) | S | Records + our replay; arithmetic correct. |
| 7 | 100k is 3.3M× lower than initial seed (`paper1-draft.md:146`) | P | Arithmetic correct; metric artifact (flow-dominated); not a target-quality claim. |
| 8 | 100k is 16,600× lower than 1k (`paper1-draft.md:147`) | P | Arithmetic correct; same problem. |
| 9 | All schedules schema-valid, hash-verified, exactly replayed (`paper1-draft.md:142`) | P | Schema/hash yes; objective replay via ad-hoc scripts, not validator; r1–r5 lack replay scripts. |
| 10 | CPU-SA is an independent-search baseline (`abstract`, §4.3) | P | Separate algorithm path, same codebase/model/evaluator; untuned, non-equal-work; not independent model. |
| 11 | GPU path is orders of magnitude stronger (`paper1-draft.md:164`) | U | No controlled comparison; CPU-SA is a straw man. |
| 12 | TSA24 is public (`paper1-draft.md:19,181`) | P | Release exists and is public; no license; GPU artifact not self-contained. |
| 13 | Artifact complete enough for GPU reproduction (`notes/reports/tsa24-public-artifact.md`) | U | Effect table/caches excluded; no pinned commit/command. |
| 14 | No independent model baseline (`paper1-draft.md` limitations) | S | Honest; it is the central gap. |
| 15 | Paper 1 submission-ready | U | Status line says not; evidence also does not support it. |
| 16 | Fresh Solutions separates concerns from search engine (`paper2-draft.md:11-20`) | P | Contract/engine exist; headline QAP/TSP bypass them. |
| 17 | Exact resident state and reversible moves are the framework’s contribution (`paper2-draft.md:31-35`) | P | True for generic engine; QAP tabu maintains its own state; no framework experiment. |
| 18 | Public-library adapters for QAP, TSP, graph colouring (`paper2-draft.md:36`) | U | QAP/TSP yes; graph colouring is `toy.py`, not public-library. |
| 19 | QAP certified means 0.000–0.685% (`paper2-draft.md:94-105`) | P | Numbers supported; `tai30a` budget violates the stated rule. |
| 20 | QAP broad median 0%, mean 1.823%, 552/670 patience (`paper2-draft.md:109-112`) | P | Summary arithmetic supported; no runner/hardware/version; raw has 25 errors. |
| 21 | Large-QAP best 0.000–2.008%, 20/20 patience (`paper2-draft.md:114-122`) | S | Records replay; runner exists; no committed replay script for jsonl; means caveat below. |
| 22 | Multi-start is a portfolio improvement over identity-start (`paper2-draft.md:124`) | U | Mean worse on esc128/tai150b; 2/4 improvement; confounded version/cap/start. |
| 23 | SciPy FAQ mixed baseline (`paper2-draft.md:124-128`) | P | Numbers exist; best-vs-mean inconsistency; weak FAQ-only baseline. |
| 24 | ILK 0.000–0.383% on 4 instances (`paper2-draft.md:140-145`) | S | 20 records replay; 4-instance scope. |
| 25 | ILK median 0% on “converged TSP subset” (`paper2-draft.md:16-18`) | U | 4-instance ILK vs 78-instance broad subset conflation. |
| 26 | Kicks are material (`paper2-draft.md:147-149`) | S | Ablation records; not equal budget; disclosed. |
| 27 | Broad TSP 78, 236/390 patience, 183 optima (`paper2-draft.md:153-156`) | P | Summary supported; runner/hardware/version missing. |
| 28 | LKH 71/100 optima, mean 0.092% (`paper2-draft.md:158-160`) | P | Records exist; no LKH version/hash; binary absent. |
| 29 | LKH optional/external, not Fresh Solutions’ heuristic (`paper2-draft.md:158-161`) | S | Code/docs/release notes; not bundled. |
| 30 | Internal TSP is a small/medium solver (`paper2-draft.md:163-164`) | S | Broad evidence; 97/100 n>300 cap. |
| 31 | TSA24 applied case is public-data (`paper2-draft.md:166-175`) | P | Public release exists; no license; target residual issue (C1). |
| 32 | No partner-impact claim (`paper2-draft.md` limitations) | S | Honest. |
| 33 | Paper 2 submission-ready | U | Status line says internal; evidence gaps. |
| 34 | P10 is complete and merged | S | Issue #31/#28 closed, PRs #39/#30 merged. |
| 35 | One phase = one branch = one PR | U | Post-P10 PRs #40–#53 and releases. |
| 36 | Tags/releases had explicit named approval | U | No close-out names commands; v0.5–v0.8 after close-out. |
| 37 | Third party can reproduce the evidence | U | `/srv` paths, missing runner, mixed pins, excluded caches. |

---

# 9. Prioritized remediation plan

This is a recommendation only; the maintainer must approve any phase/tag/release.
Do not merge, tag, or release as part of the audit follow-up without the named
approval required by `AGENTS.md`.

## P0 — Stop the bleeding (before any more prose)

1. **Freeze claims.** Change both draft status lines to “internal, not
   submission-ready” (Paper 2 already; Paper 1 already). Remove the
   “3.3 million times”, “near-zero”, “orders of magnitude”, and “full 208k”
   phrases until C1/H1/M1 are resolved. Acceptance: a grep of both drafts finds
   no unsupported headline adjective without a linked residual table.
2. **Repair the workflow record.** Open a new parent phase (with maintainer
   approval) for all post-P10 work; add child issues for the already-merged
   PRs #40–#53 and solver releases v0.5.0–v0.8.0; update `ROADMAP.md`,
   `README.md`, `CHANGE_LOG.md`, and `notes/issue-bodies/p10.md` to the truth.
   Do not retroactively rewrite history; record the deviation. Acceptance:
   `ROADMAP.md` and GitHub agree; no phase is `pr-open` when its issue/PR is
   closed; every post-P10 change has a parent/child or an explicit “post-phase
   maintenance” issue.
3. **Fix the validator before adding records.** Add an objective replay hook to
   `check_benchmark_record` (or a new gate) that loads the schedule, calls the
   pinned evaluator, and fails on a mismatch. Add a negative test where the hash
   is correct but the objective is wrong. Acceptance: the dummy test record in
   `tests/test_benchmark_record.py` fails until it has a real evaluator; all 11
   current records pass.
4. **Add per-target residuals and correct timing.** For each TSA24 record,
   store flow term, level terms, per-period realized values, and the best
   generation. Recompute `time_to_best_s` from `best_generation`/`generations`
   or from an instrumented log; replace the `time_to_first_feasible_s`
   placeholder with a measured or explicitly null value (schema change).
   Acceptance: a table in the paper shows the residual decomposition; no
   “near-zero” claim survives without it.

## P1 — Paper 1 minimum defensible paper

5. **Target feasibility audit.** Determine whether 70,000,000 m³/period is
   achievable under the candidate set and even-flow band. If not, redefine the
   benchmark objective (e.g., maximize level subject to flow) or report the
   shortfall as the result. Acceptance: a written note with either a feasible
   schedule at 70M or a proof/argument that the target is infeasible; the paper’s
   title/abstract reflect the chosen objective.
6. **Matched CPU baseline.** Run (a) a tuned CPU-SA at the same wall budget
   (e.g., 941 s) and the same evaluation count, and (b) a CPU-GA with the same
   population/generations as the GPU-GA. Report mean/median/worst over five
   seeds. Acceptance: a table with equal-budget and equal-evaluation columns;
   the “orders of magnitude” claim is either supported by a controlled result or
   removed.
7. **Architecture ablation.** Measure cache load vs search, effect-table
   evaluation vs direct evaluator, and GPU vs CPU batched evaluation at the
   same population/generation. Acceptance: an ablation table with speed and
   objective; if the architecture effect is not measurable, downgrade the thesis
   to “engineering report”.
8. **Artifact and license.** Add a `LICENSE` (or a clear research-use/source-
   license statement) to `femic-tsa24-instance`; add the exact WS4 commit,
   branch, table-build command, cache-build command, and asset SHA-256 to the
   artifact README; either include a small effect-table slice or provide a
   build script with a checksum. Acceptance: a clean-room GPU-capable user can
   rebuild the 1k record from the artifact + public code; the license is
   explicit.
9. **Clean paths and pins.** Replace `/srv/...` with environment variables or
   repository-relative paths in every replay script and evidence JSON; add the
   WS4/TSA24 pins to the papers repo (e.g., a `provenance.json`). Acceptance:
   `grep -R "/srv/shared-data"` returns no tracked evidence/script; a clean
   checkout can run `--help`/replay with `WS4_ROOT`/`TSA24_ROOT`.
10. **New Paper 1 evidence release.** After 5–9, tag a new
    `paper1-evidence-v0.2.0` (with named maintainer approval) containing the
    current draft, records, manifest, and artifact reference. Acceptance: tag,
    release, clean-checkout log, all records valid, table regenerated.

**Stop conditions for Paper 1:**

- If no independent model baseline and no matched CPU baseline can be produced,
  do not submit a competitive paper; submit the systems/reproducibility paper
  with the architecture ablation and the target-feasibility audit.
- If the 70M target is infeasible and the objective is redefined, the paper’s
  headline must change; do not keep the old numbers as a “result” for the new
  objective.

## P2 — Paper 2 minimum defensible paper

11. **Commit the broad-panel runner and schema.** Recover/recreate the script
    that produced `broad-converged.json.gz`; parameterize the corpus root
    (`QAPLIB_ROOT`, `TSPLIB_ROOT`), record solver version/commit, hardware,
    Python/Numpy/Numba/SciPy versions, and a schema for every record. Re-run or
    at least re-summarize from the raw bundle. Acceptance:
    `python paper2/run_broad.py` reproduces the 1,060 successful records and the
    summary from the pinned corpus; 25 parse errors are isolated in a separate
    file with a documented parser gap.
12. **Fix the QAP certified table.** Apply the policy consistently: `tai30a`
    at 10k if 10k passes; otherwise change the policy and explain why the extra
    doubling is required. Acceptance: the table matches
    `qap-tabu-stability-summary.json` and the policy; no larger-budget
    substitution.
13. **Strengthen the QAP baseline.** Add SciPy `2opt` refinement or a published
    QAP heuristic at a stated budget; report mean/median/worst and wall. If only
    FAQ is available, label it “weak baseline” and do not draw a quality
    conclusion beyond “mixed”.
14. **Framework-use experiment or reframe.** Either (a) implement QAP tabu or
    TSP LK through the generic adapter/engine and measure overhead/replay, or
    (b) retitle/reframe as “a reproducible benchmark harness and adapter
    contract” and remove “framework” claims that the experiments do not test.
    Acceptance: at least one headline result produced by the generic engine, or
    a paper title/abstract that accurately says “harness + reference adapters”.
15. **Third public adapter or narrower claim.** If “general framework” remains,
    add a public graph-colouring/job-shop instance and replayable evidence.
    Otherwise delete “public-library adapters for graph colouring” and scope to
    QAP/TSP. Acceptance: a public instance, adapter, runner, schema record, and
    baseline, or the claim is gone.
16. **LKH metadata.** Record `LKH_VERSION`, binary SHA-256, command, parameter
    file, and a small rerun subset. Acceptance: an independent user with the
    same LKH version can reproduce 71/100 within the stated tolerance; otherwise
    mark the LKH evidence “illustrative, not reproducible”.
17. **TSP ILK breadth or narrower abstract.** Run ILK on the 78-instance panel
    (or a defined subset) with the same starts/budget, or restrict the abstract
    to the 4-instance result. Acceptance: the abstract’s scope matches the
    evidence table; no “converged TSP subset” conflation.
18. **Evidence release.** Tag a `paper2-evidence-v0.x` (with named approval) and
    update `paper2/README.md`, `paper2/benchmarks/README.md`, and the draft.
    Acceptance: tag + manifest + clean replay of the archived subset.

**Stop conditions for Paper 2:**

- If the broad runner cannot be recovered and the raw bundle cannot be
  re-summarized with provenance, restrict the paper to the 8-instance
  convergence panel and the 4-instance ILK panel; do not use the 78/134 claims.
- If no framework-use experiment is possible, submit a tool/benchmark paper, not
  a metaheuristics methods paper.
- If the LKH binary cannot be pinned, keep LKH as an “external capability
  reference” in the limitations, not a headline result.

## P3 — Abandon/defer

- **Abandon** the “3.3 million times” / “near-zero” framing permanently; it is
  not a target-quality statement.
- **Abandon** the “portfolio improvement over identity-start tabu” claim until a
  matched multi-start experiment exists.
- **Abandon** the “graph colouring public adapter” sentence unless a real
  public adapter is added.
- **Defer** any state-of-the-art or universal dominance claim; it is not
  supported and is not needed for either paper’s honest contribution.
- **Defer** a large-TSP internal solver claim; LKH is the correct boundary for
  now.
- **Do not** create new tags/releases, merge PRs, or change repository settings
  without the explicit approval required by `AGENTS.md`.

---

# 10. What a hostile reviewer will attack first

## Paper 1

1. **“Your 517.86 is not near zero; it is a 25% harvest-level shortfall.”**
   They will compute the target residuals (as I did) and ask why the objective
   is defined around an unmet 70M aspiration.
2. **“Your CPU-SA baseline is a straw man.”** They will note 100k single-chain
   proposals vs 6.4M genome evaluations, default parameters, same codebase, and
   a 31.25-minute run.
3. **“Your instance is 458,708 blocks, not 208,255.”** They will open
   `blocks.parquet` and ask what “full” means.
4. **“Your artifact is not reproducible.”** No license, no effect table/caches,
   no pinned WS4 commit/command; the replay scripts use `/srv` paths.
5. **“Your validator does not replay the objective.”** They will read
   `check_benchmark_record.py` and the dummy test.
6. **“Where is the architecture ablation?”** The paper asserts a causal
   architecture but only shows one GPU scaling curve.

## Paper 2

1. **“Your broad panel has no runner.”** They will search for the script and
   find only 8-instance runners and a stale README.
2. **“Your framework results do not use your framework.”** They will see
   `run_qap_tabu`/`run_tsp_lk` bypass the engine.
3. **“Your certified budget is not the smallest passing budget.”** They will
   compute `tai30a` 10k→20k = 0.0923 and see the table uses 40k.
4. **“Your SciPy baseline is weak and the comparison mixes best and mean.”**
   They will compare means and ask for a published QAP baseline.
5. **“Your ILK abstract claims 78 instances but the table has 4.”**
6. **“Your LKH number has no version/hash.”**
7. **“Your workflow closed P10 and then merged 14 PRs and five releases.”**

---

# 11. Uncertainties and things I could not verify

1. **GPU 100k rerun.** I did not rerun the 100k GPU campaign: the effect table
   (1.4 GB) and caches (2.0 GB) are excluded from the artifact, and a
   GPU-capable environment with the same device was not available. I relied on
   the stored schedules and the CPU evaluator.
2. **LKH 100-run rerun.** `LKH` is not installed in the current environment and
   the version/hash is not recorded. The 71/100 summary is unverified beyond the
   stored assignment/objective records.
3. **FHOPS commit.** The FHOPS working tree is owned by another user; `git`
   refused due to “dubious ownership”, so I could not inspect commit `135321b`
   directly. The FHOPS replay script ran and matched the record.
4. **TSA24 target feasibility.** I computed the residuals, but I did not prove
   whether 70M m³/period is infeasible or whether 52M is the maximum sustainable
   even-flow. That is a domain question for the forestry team.
5. **BC data licenses.** I did not audit the BC VRI/FADM/SiteProd license terms;
   the repository has no `LICENSE` and the artifact says only “source data
   retains BC government licences.” A lawyer/domain owner must confirm
   redistribution and reuse terms.
6. **GPU determinism across hardware.** The records claim determinism; I did not
   verify that the same seed produces the same schedule on a different GPU or
   PyTorch version. GPU reductions can be nondeterministic across devices.
7. **Broad panel script.** I could not find it in the current tree or in
   `git log --all --name-only`; it may exist outside the repository. I did not
   reconstruct it.
8. **SciPy FAQ domain on asymmetric QAP.** `tai150b` is asymmetric
   (`max |D - D^T| = 8097`); SciPy’s FAQ may still optimize the stated trace
   objective, but it is a weak baseline. I did not prove it is invalid; I only
   note that the comparison is not a strong QAP baseline.
9. **GitHub issue comments.** `gh issue view --comments` failed with a Projects
   (classic) deprecation error; I used `gh issue list` and `gh pr view` JSON.
   I did not read every issue comment.
10. **Approval history.** I did not find a maintainer approval for the post-P10
    releases/tags in the repository text or PR bodies. It may exist in a chat
    or a comment I could not read; the repository does not record it.
11. **Paper 1 v0.1.0 release asset.** I verified the tag/commit and manifest in
    the repository, but I did not download the release’s attached archive to
    compare its bytes with the current tree. The manifest’s file hashes are
    stale relative to the current draft/table.
12. **Current `ws4-gpu` worktree.** The worktree is at `e066a9c` with unrelated
    web changes; the evidence used a temporary copy at `f60ce64`. I did not
    audit the later `ws4` main for GPU regressions.

---

# 12. Bottom line

The programme has real engineering value: a working evidence harness, exact
assignment replay, a public TSA24 release, a broad public-corpus campaign (whose
runner is missing), and honest labelling in several places. It does not yet have
the scientific claims it is reaching for.

**Paper 1** should be a systems/reproducibility paper with a target-residual
audit, a matched CPU baseline, an architecture ablation, and a licensed,
GPU-rebuildable artifact. It should not be submitted as a competitive
landscape-scheduling paper on the current evidence.

**Paper 2** should be a benchmark-harness/tool paper or a narrower QAP/TSP
methods paper, with a committed broad runner, a corrected certified table, a
stronger independent baseline, and either a framework-use experiment or a
title that does not claim one.

**Workflow:** before either paper moves, the post-P10 phase/release drift and the
stale roadmap/README must be recorded and corrected under a new approved phase.
The scientific findings above are independent of that, but the governance issue
is the first thing a maintainer should see.
