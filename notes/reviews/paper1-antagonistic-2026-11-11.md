# Reviewer report — Paper 1

**Manuscript:** “Compiled landscape optimisation: exact resident state and GPU population search for harvest scheduling”
**Target venue:** Environmental Modelling & Software (EMS)
**Review copy:** `paper/paper1-manuscript.pdf` (21 pages, 3 figures, 5 tables)
**Journal variant:** `paper/submission/paper1-elsarticle.pdf` (29 pages; content identical apart from front matter and bibliography style)
**Review date:** 2026-11-11
**Reviewer stance:** independent, antagonistic Reviewer 2 / associate editor

**Recommendation:** **Reject**
**Prepared to review after revision:** **No** for this submission. I would consider a *new* submission only if the P0 items in this report are resolved and the paper is either reframed for a software/reproducibility venue or given a genuine environmental-modelling contribution.

---

## Overrides and scope of this review

- The EMS review form is not included in the submission materials. This report therefore uses the manuscript template headings supplied for the review, plus the requested risk table and P0/P1/P2 list.
- The main PDF (`paper/paper1-manuscript.pdf`, 21 pages) is the review copy. The EMS variant (`paper/submission/paper1-elsarticle.pdf`, 29 pages) was checked for content differences; a normalised diff of the two `.tex` files shows only front-matter, keyword, table-width, and bibliography-style differences. Formatting is not reviewed here.
- All substantive praise and criticism is tied to the submission materials. I use the tags below. I did not use external literature, and I did not import claims from outside the submission.
- Arithmetic was recomputed from the manuscript tables and the evidence records. SHA-256 hashes were recomputed for the manifest check. No manuscript or evidence file was edited. The only file created is this report.

### Evidence tag key

| Tag | Meaning |
|---|---|
| `MS pX` | Main manuscript PDF, page X |
| `SUB pX` | EMS journal variant PDF, page X |
| `Table N`, `Fig N` | Main manuscript table/figure |
| `EV <path>` | Evidence JSON or record in the repository |
| `NOTE <path>` | Notes report in the repository |
| `TEX <path>:line` | LaTeX source line |
| `MANIFEST` | `paper/release/manifest-v0.2.0-candidate.json` |

---

## Document inventory

| Material | Observation |
|---|---|
| `paper/paper1-manuscript.pdf` | 21 pages, 3 figures, 5 tables. SHA-256 matches `MANIFEST.pdf`. |
| `paper/paper1-manuscript.tex` | 61,789 bytes. SHA-256 matches `MANIFEST.manuscript`. |
| `paper/submission/paper1-elsarticle.pdf` | 29 pages. SHA-256 matches `MANIFEST.submission_pdf`. Content same as main PDF; placeholder author metadata (`SUB p1`; `TEX paper/submission/paper1-elsarticle.tex:20`). |
| `paper/evidence/tsa24-factorized-ablation.json` | 64-genome, 4-cell CPU/CUDA batch. **SHA-256 does not match `MANIFEST.factorized_ablation`** (manifest `9d788e…`; actual `e958a6…`). |
| `paper/evidence/tsa24-matched-search.json` | 1/10/100-generation CPU/CUDA search, one seed. |
| `paper/evidence/tsa24-target-sensitivity.json` | 1,000-iteration, five-target screen. |
| `paper/evidence/tsa24-factorized-cpu.json`, `…-gpu.json` | Component records; hashes match the manifest. |
| `paper/release/manifest-v0.2.0-candidate.json` | Status: “candidate; no tag/release created; public schedules/replay release pending.” One hash mismatch (above). |
| `evidence/ws4-tsa24-gpu-ga-100000-r1…r5`, `…r7` | 100,000-generation records. All record hashes match the manifest. |
| `evidence/ws4-tsa24-gpu-ga-1000-r7`, `…10000-r7` | Scaling records. Hashes match. |
| `evidence/ws4-tsa24-cpu-sa-100000-r7` | CPU-SA comparator. Hash matches. |
| `evidence/ws4-tsa24-eval-ablation.json` | 5,000-block, 50-move evaluation-path diagnostic. Hash matches. |
| `notes/reports/claim-to-evidence-audit-2026-11-09.md` | Claim audit; “public release approval outstanding.” |
| `notes/reports/significant-figures-review-2026-11-11.md` | Precision audit. Claims “hashes match”; this is false for the factorized ablation. |
| `notes/reports/p13-5-architecture.md` | Architecture-ablation close-out. |
| `notes/reports/p13-6-paper1-baselines.md` | Baseline close-out; “no improved independent CPU-search baseline.” |
| `notes/reports/p13-9-review-2026-11-09.md` | Internal re-review: “Paper 1 (EMS): not submission-ready… SoftwareX/JORS is the better fit.” |
| `notes/reports/p13-7-artifact-plan.md` | Artifact plan; “public evidence repo private”; release is approval-gated. |
| `notes/reports/p13-8-sensitivity.md` | “No target-weight sensitivity yet.” |
| `notes/reports/naming-convention.md` | FRESH naming audit (clean). |

---

## Evidence ledger (claim → evidence → status)

| Claim in the manuscript | Evidence tag | Status |
|---|---|---|
| 458,708 compiled blocks; 208,255 operable; 20 periods | `MS p4`; `EV evidence/ws4-tsa24-gpu-ga-100000-r1/record.json` (`instance.variables` = 208255) | Supported |
| Initial objective 1,722,140,000 | `MS p5`, `MS p11`; records `result.target_penalties.initial_seed_objective` = 1,722,144,291.34 | Supported to six significant figures |
| 1,000 generations: 8,588,730 in 9.38 s search / 23.1 s wall | `Table 2`; `EV …1000-r7` (9.3815 s, 23.13 s) | Supported; one seed |
| 10,000 generations: 76,540.7 in 89.8 s / 157 s | `Table 2`; `EV …10000-r7` (89.7816 s, 157.338 s) | Supported; one seed |
| 100,000 generations: 517.862 in 856 s / 942 s | `Table 2`; `EV …100000-r7` (856.096 s, 941.51 s) | Supported; one seed; timing differs from campaign runs |
| Five-seed campaign 512.574–518.621; mean 515.682; median 515.938 | `MS p12`, `Table 3`; records r1–r5 | Supported for seeds 1–5; table has six rows (seed 7 included) |
| Level term 515.141; realized level 51.34–52.38M | `Table 2`, `Table 3`; `EV …r7` | Numerically supported; functional form and units not stated |
| 248× factorized batch; max error 1.71e-6 | `Table 4`; `EV paper/evidence/tsa24-factorized-ablation.json` | Supported as a 64-genome/4-cell batch; manifest hash stale |
| 22.2× matched search; CPU objective 5% lower | `Table 5`; `EV paper/evidence/tsa24-matched-search.json` | Arithmetic supported; CUDA timing non-monotonic; one seed |
| 2.00e3 evaluation-path factor; residual 3.7e-9 | `MS p13`; `EV evidence/ws4-tsa24-eval-ablation.json` | Supported on a 5,000-block/50-move subset; `54.9` should be `54.8` |
| Target screen 1.71e9 → 1.01e3 | `Table 1`; `EV paper/evidence/tsa24-target-sensitivity.json` | Supported as a 1,000-iteration screen; not a converged comparison |
| CPU-SA 3.35045e8 in 1.88e3 s; 204,413 “operable blocks” | `MS p13`; `EV evidence/ws4-tsa24-cpu-sa-100000-r7/record.json`; `NOTE p13-6` | Numerically supported; “operable blocks” is a mislabel of “scheduled blocks” |
| Exact CPU replay | `MS p9`; records `result.exact_replay = true`; seed-7 device/replay difference 1.95e-13 | Supported numerically; not publicly replayable |
| Public release of schedules/replay | `MS p18`; `MANIFEST.status`; `NOTE p13-7` | **Not supported**; repository private, release pending |
| Manifest hashes match | `NOTE significant-figures-review-2026-11-11.md:46`; `MANIFEST.factorized_ablation` | **Not supported** for the factorized ablation |
| FRESH naming | `MS p1`, `MS p18`; `NOTE naming-convention.md` | Supported |
| 3 figures | `MS p1–21`; `NOTE significant-figures-review-2026-11-11.md:43` | Supported; but thin (see M9) |

---

## Confidential comments to the editor

**Recommendation: Reject for EMS.**

The manuscript is candid and technically careful in places, but it does not deliver an environmental-modelling contribution, and its central reproducibility claim is not met at review time. The paper-specific schedules and replay scripts are private (`MS p18`; `MANIFEST.status`; `NOTE notes/reports/p13-7-artifact-plan.md`), so a reader cannot replay any reported objective. The manifest hash for the factorized ablation is stale (`MANIFEST.factorized_ablation` = `9d788e…`; actual file = `e958a6…`), which contradicts the project’s own “hashes match” audit (`NOTE notes/reports/significant-figures-review-2026-11-11.md:46`). The CUDA search times in Table 5 decrease with more generations (41.7 s → 33.7 s → 23.9 s), a data-integrity issue that the “model/table overhead” explanation does not resolve (`MS p14`). The architecture claim is explicitly not separated from implementation effects (`MS p15`, `MS p17`), and there is no independent harvest-scheduling baseline (`MS p2`, `MS p17`). The paper’s own internal P13.9 review already concluded “not submission-ready” and “SoftwareX/JORS is the better fit” (`NOTE notes/reports/p13-9-review-2026-11-09.md:9-12`).

I would not send this out for a second EMS round in its current form. A new submission could be considered after (i) a public evidence release with a DOI and one-command replay; (ii) a controlled architecture/CPU ablation or an explicit removal of the architecture-performance claim; (iii) an independent baseline or a clear “no quality claim” reframing; and (iv) either an environmental validation/second landscape or a move to a software/reproducibility venue. The paper’s honesty about its limits is a credit, but honesty about missing evidence is not a substitute for the evidence.

---

# Comments to the authors

## Summary

The manuscript describes a compiled-state architecture for landscape harvest scheduling and evaluates it on one frozen TSA24/Prince George instance with a GPU population search and exact CPU replay. It is unusually candid about what it does not claim, and the numerical reporting is mostly internally consistent. However, it does not establish that the architecture causes the observed performance, has no independent harvest-scheduling baseline, and withholds the schedules and replay scripts that are the core of its reproducibility contribution. The environmental-modelling contribution is thin: there is no ecological validation, no management scenario, no spatial-constraint case, and no second landscape. The paper reads as a software/operations-research case study, not an EMS research article. I recommend reject for EMS; the work is a credible SoftwareX/JORS candidate only after a public release and a controlled ablation.

---

## What the manuscript does well

These are real strengths, not consolation prizes.

1. **The paper is explicit about its claim boundary.** The abstract says the contribution is “the architecture and its reproducibility contract” and disclaims an independent model comparison (`MS p1`); the introduction says the paper “does not make a competitive landscape claim” and that the CPU-SA comparison is “a weak, untuned secondary comparator” (`MS p2`); the results section says the campaign “does not establish that the GPU path is faster per unit of exact work than a tuned CPU implementation” and “does not establish that the architecture is the cause of the observed quality” (`MS p15`); the conclusion repeats the limits (`MS p17`). This is better practice than most submissions, and it makes the review tractable.

2. **The exact-replay records are well structured and numerically credible.** Each 100,000-generation record carries instance, algorithm, seed, hardware, software, wall/search time, schedule path, schedule SHA-256, exact-replay flag, and target penalties (`EV evidence/ws4-tsa24-gpu-ga-100000-r7/record.json`). For seed 7, the device objective is 517.8619818207143 and the exact CPU replay is 517.8619818205188, a difference of about 1.95e-13. The 10,000-generation record notes that two independent runs produced the identical schedule SHA-256 (`EV evidence/ws4-tsa24-gpu-ga-10000-r7/record.json`). The manuscript does not report the duplicate-run determinism check; it should, because it is stronger evidence than the current “exact replay” sentence.

3. **The tables’ arithmetic is consistent.** In Table 2, flow + level = objective for all three rows within rounding: 8,588,230 + 499.821 = 8,588,729.821 → 8,588,730; 76,026.9 + 513.832 = 76,540.732 → 76,540.7; 2.721 + 515.141 = 517.862 (`Table 2`). In Table 3, flow + level = objective for every row (`Table 3`). The five-seed mean (515.682) and median (515.938) are correct for seeds 1–5. The 248×, 22.2×, and 2.00e3 factors are arithmetically correct to the reported precision. I found no arithmetic errors in the table sums or ratios; the problems are definitional, statistical, and evidentiary (below).

4. **The paper labels its weaker evidence honestly.** The target screen is “screen only, not a converged comparison” (`Table 1`); the factorized batch is “batch evaluation only, not end-to-end search” (`Table 4`); the matched search is “not a hardware ranking” (`Table 5`); the 5,000-block ablation is a “diagnostic” (`MS p11`, `MS p13`). This is the right instinct.

5. **FRESH naming is consistent.** The lab is “UBC FRESH Lab” in the main manuscript and the journal variant (`MS p1`; `SUB p1`), and the naming audit reports no title-case lab reference (`NOTE notes/reports/naming-convention.md`). The package path `fresh-solutions/` is a code identifier, not prose. This is clean.

6. **Negative results are reported, not hidden.** The CPU objective is lower than the CUDA objective at 100 generations (`MS p14`, `Table 5`); the GPU is not shown to be faster per unit of exact work (`MS p15`); the CPU-SA comparator is weak (`MS p13`). This is a genuine credit.

---

## Major comments

### M1. The paper is a single-instance software case study, not an EMS contribution

**Claim.** The manuscript’s environmental-modelling content is the TSA24 landscape and a harvest-flow target. It reports no ecological process model, no validation against observed or policy benchmarks, no alternative management scenario, no spatial-constraint case, and no second landscape. The paper’s own scope statement concedes this.

**Evidence.** The abstract defines the contribution as “the architecture and its reproducibility contract” (`MS p1`). The introduction says “It does not make a competitive landscape claim… no independent harvest-scheduling model is available on the same instance” (`MS p2`). The related work is about spatial harvest scheduling with adjacency and opening-size restrictions (`MS p3`), but the reported run has “no hard spatial constraints” (`MS p2`, `MS p6`). The discussion says “The TSA24 case is a scenario configuration, not an official decision” and limits the operational claim to “the reproducibility of the computation, not the desirability of the result” (`MS p16`). The conclusion says the paper “cannot claim competitive landscape performance, state-of-the-art quality, or partner-endorsed operational impact” (`MS p17`). The only environmental quantities in the results are the flow and level terms and the realized harvest level (`Table 2`, `Table 3`); the reported objective does not use an ecological indicator, a habitat account, or a carbon account, and there is no validation.

**Why it matters.** EMS readers expect an environmental model, an environmental application with validation, or a software tool they can use. This paper is a software architecture case study with a forest-planning objective. The related work sets up the hard spatial-constraint literature, then the experiment removes the spatial constraints; the paper is therefore not testing the problem class it claims to address. The “environmental” content is the input data, not the contribution.

**Action.** Choose one of two paths. (a) Add a genuine environmental-modelling contribution: a second landscape; a management scenario with an ecological or policy interpretation; a validation/benchmark against an independent harvest-scheduling model or a documented policy target; and a spatial-constraint case with adjacency or opening-size rules. (b) Reframe for SoftwareX or JORS as a short software/reproducibility paper, with the architecture description, the public artifact, and the replay contract as the contribution. Do not submit the current version to EMS.

---

### M2. The architecture claim is not separated from GPU/implementation effects

**Claim.** The paper’s three speed numbers measure three different things, none of which isolates the architecture: 248× is a 64-genome, 4-cell batch; 22.2× is a one-seed, 100-generation device comparison on the same implementation; 2.00e3 is a 5,000-block, 50-move evaluation-path diagnostic. No experiment varies architecture while holding hardware, implementation, and work constant.

**Evidence.** The factorized batch is “64 genomes, four mixed target cells, 3 repeats; batch evaluation only, not end-to-end search” (`EV paper/evidence/tsa24-factorized-ablation.json`; `Table 4`). The matched search uses “the same `gpu-run` implementation” with `--device cpu` and `--device cuda`, population 64, seed 7, 1/10/100 generations; the CPU path is “a single torch device path, not a tuned multithreaded CPU-GA” (`MS p14`; `EV paper/evidence/tsa24-matched-search.json`). The evaluation-path ablation is a 5,000-block subset with 50 moves (`MS p11`, `MS p13`; `EV evidence/ws4-tsa24-eval-ablation.json`). The paper itself says “The reported campaign does not establish that the GPU path is faster per unit of exact work than a tuned CPU implementation, and it does not establish that the architecture is the cause of the observed quality” (`MS p15`), and that “a tuned CPU-GA and cache/search ablation at equal work are still required before the architecture claim can be separated from a local implementation-speed claim” (`MS p17`). The internal P13.5 close-out calls this a “controlled, scoped ablation,” but the factorized batch and matched search vary device/batch size, not architecture (`NOTE notes/reports/p13-5-architecture.md:12-20`).

**Why it matters.** The architecture is the paper’s central claim. The current evidence supports “this implementation runs on this instance,” not “the architecture causes the speed or the quality.” The 248× and 22.2× numbers are device/implementation effects; the 2.00e3 number is an evaluation-path effect on a 2.4% subset. None of them tests the architecture.

**Action.** Add a controlled architecture ablation: same code path, same hardware, same total work, with the architecture on/off — for example, dense vs sparse effect table; full re-evaluation vs resident-state delta; rebuild-per-move vs cached table. Add a tuned CPU baseline (multithreaded, same population/generation budget, same target) and report time-to-quality, not just wall time. If those experiments are not feasible, remove the architecture-performance claim and present the paper as a design description, with the 248×/22.2×/2.00e3 labeled as implementation microbenchmarks, not architecture evidence.

---

### M3. Statistical defensibility: one seed, no intervals, and a table that does not support its own statistics

**Claim.** The matched search and the 1,000/10,000-generation scaling are one-seed; the five-seed campaign has no standard deviation, confidence interval, or test; the five-seed table contains six rows, so a reader cannot reproduce the reported mean and median from the table.

**Evidence.** The matched-search scope says “one seed” (`Table 5` caption; `EV paper/evidence/tsa24-matched-search.json`). The 1,000- and 10,000-generation runs use seed 7 (`MS p11`). The five-seed campaign reports “the best seed is 512.574, the worst is 518.621, the mean is 515.682, and the median is 515.938” (`MS p12`), but Table 3 has six rows: seeds 1–5 and seed 7 (`Table 3`). I computed the six-row mean and median from the table: **516.045** and **516.234**, not 515.682 and 515.938. The paper says “All five schedules replay exactly” while the table shows six (`MS p12`; `Table 3`). The paper admits “the five-seed campaign is a small sample… the paper does not report a confidence interval for the mean or a test against a baseline” (`MS p16`). The paper cites Barr et al. [1995], Hooker [1995], and McGeoch [1996] on experimental reporting (`MS p3`) but does not follow their reporting discipline.

**Why it matters.** The “tightly clustered” claim and the 22.2× claim are not statistically supported. The seed table is the main evidence for the 100,000-generation result; if its summary statistics do not match the table, the reader cannot trust the surrounding claims. The one-seed matched search cannot support a general CPU/CUDA ratio.

**Action.**
- Report per-seed objective, flow, level, wall, and search time in Table 3, and either exclude seed 7 or label the table “five-seed campaign plus seed-7 reference.” If seed 7 is included, report the six-run mean/median (516.045/516.234) or state explicitly that the mean/median are five-seed statistics.
- Report the standard deviation and a 95% interval for the five seeds. My t-based calculation from `Table 3` is SD ≈ 2.23 and 95% CI ≈ 512.9–518.5; n=5, so this is descriptive, not a basis for a general claim.
- Repeat the matched CPU/CUDA comparison over at least 5–10 seeds at 100 generations and report the paired distribution and timing variance. Do not report “22.2×” as a single-seed point estimate without the distribution.
- Remove “tightly clustered” as a result or qualify it as a descriptive observation about this seed set. The table does not show a clean flow/level trade-off: seed 1 is worse on both components (flow 1.331, level 517.290) and seed 2 is better on both (0.000, 512.574), which is the opposite of a trade-off (`Table 3`).

---

### M4. The level term is misdescribed and its units are missing

**Claim.** The manuscript says “every period carries a linear harvest-level target with aspiration 70,000,000 m³ per 10-year period and weight 100” and that “every period has a downward gradient toward more harvest” (`MS p5`). The evidence records are consistent with a **mean-based, normalized** penalty, not a per-period linear penalty: for every seed, the level term equals `20 × 100 × (70,000,000 − realized_mean) / 70,000,000` to machine precision. The manuscript never states this normalization, and the reported level term is dimensionless, not m³.

**Evidence.** I recomputed the identity from the records:
- Seed 1: mean 51,894,835.4; `20 × 100 × (70,000,000 − 51,894,835.4)/70,000,000 = 517.2904166`; record level = 517.2904166207935 (`EV evidence/ws4-tsa24-gpu-ga-100000-r1/record.json`).
- Seed 2: mean 52,059,905.14709445; level = 512.5741386544443; the same identity holds.
- Seed 3: level = 515.9377174965076; seed 4: 514.7459645617461; seed 5: 516.4541810447618; seed 7: 515.1408610731742. The identity holds for all six.
- The record’s `realized_level_min_m3` and `realized_level_max_m3` vary widely (e.g., seed 1: 51.21–52.25M), but the level term depends on the mean, not the per-period values (`EV …r1`).
- A direct illustration: the 1,000-generation seed-7 schedule has a **higher** mean level (52,506,270.98 m³) and a **lower** level term (499.820829) than the 100,000-generation seed-7 schedule (mean 51,970,069.86; level 515.140861), even though its per-period range is much wider (42.09–60.54M vs 51.34–52.38M) (`EV evidence/ws4-tsa24-gpu-ga-1000-r7/record.json`, `…100000-r7`). Under the manuscript’s “every period carries a linear target” description, the wider, lower-minimum 1,000-generation profile should have a *higher* level penalty, not a lower one. The mean-based identity is the only way the records are consistent.

**Why it matters.** The objective is the central result. As written, it cannot be reproduced or interpreted. The “every period” claim is false: a schedule with one zero period and one very high period can have the same level penalty as a flat schedule, because the penalty uses the mean. The paper’s argument that the level aspiration prevents “periods that would otherwise be left underused” (`MS p5`) is not supported by the evidence. The reported “level term 515.141” is not 515 m³ of shortfall; it is roughly 20 × a percentage shortfall. A reader who compares it to the 70M aspiration will be misled by the units.

**Action.** Write the exact penalty equations, including the normalization (divide by the target or reference level), and state the units of every term. If the design is a mean-level penalty, say “the level term is a normalized penalty on the mean realized level, summed over 20 periods,” and remove “every period has a downward gradient.” If the design is per-period, the records are wrong and must be regenerated. Report the mean level and the per-period profile next to the level term. Also state whether the flow term is normalized and give the reference-period value; the manuscript says it “compares each period with the reference period” (`MS p5`) but never gives that value.

---

### M5. The 70M target, weights, and band are unjustified; the target screen is not a sensitivity analysis; there is one landscape

**Claim.** The values 70,000,000 m³, weight 100, ±1% band, and weight 10,000 are asserted, not justified. The 1,000-iteration screen is near the initial objective and under-budgeted; full-budget target sensitivity is future work. There is one landscape.

**Evidence.** The target values appear without provenance (`MS p5`, `MS p6`). The screen uses 1,000 SA iterations, seed 7, 8 threads (`Table 1`; `EV paper/evidence/tsa24-target-sensitivity.json`). For the main target, the screen objective is 1.7138e9 versus the initial 1.7221e9 — an improvement of about 0.48% — so the screen is essentially an initial-objective scale check, not a search result. The screen’s range is six orders of magnitude (1.71e9 to 1.01e3), which shows the objective scale is target-dependent, not that one target is better. The paper says “target-weight sensitivity at the full budget remains future work” (`MS p6`) and the internal note says “No target-weight sensitivity yet” (`NOTE notes/reports/p13-8-sensitivity.md:3`). The external validity section says “TSA24 is one landscape, one target construction, and one 20-period horizon” (`MS p16`).

**Why it matters.** The headline 517.862 is a weighted sum whose scale is set by the target. The screen shows a six-order-of-magnitude range but is not a converged comparison; it cannot tell the reader whether 517.862 is robust to the weights. Without justification for 70M/100/±1%/10,000, the result is arbitrary. Without a second landscape, the architecture claim is instance-specific.

**Action.**
- Justify the target values from the artifact or a policy/management source: why 70M, why weight 100, why ±1%, why weight 10,000. If 70M is the current allowable cut or a policy aspiration, say so and cite the artifact/source. If it is a synthetic pull-up value, say how it was chosen.
- Run a full-budget sensitivity (at least the level weight and the band; ideally the flow weight) and report the objective components, not just the total. The current 1,000-iteration screen is not enough.
- Add a second landscape or a stress instance with a different treatment vocabulary, candidate size, or horizon. If that is not possible, remove “architecture” as a general claim and call it a single-case design.
- Report the management interpretation of the 52M vs 70M gap. The paper says the 70M aspiration is “deliberately unattainable” (`MS p5`, `MS p17`), but it does not say what the gap means for a planner. A reader cannot tell whether 52M is a good outcome, a policy failure, or an artifact of the target.

---

### M6. The reproducibility/release contribution is not delivered, and the evidence process fails its own hash check

**Claim.** The paper’s third contribution is an exact replay contract, but the schedules and replay scripts are private; the code is on a feature branch and a non-main commit; the manifest hash for the factorized ablation is stale; and the audit that says “hashes match” is wrong.

**Evidence.**
- Abstract: “The frozen dataset, target, and seed are public; the paper-specific schedules and replay scripts are retained in the project evidence repository and are not yet publicly released” (`MS p1`).
- Data availability: “The paper-specific schedules and replay scripts are retained in the project evidence repository; a public evidence release remains pending maintainer approval” (`MS p18`).
- Manifest: “status: candidate; no tag/release created; public schedules/replay release pending” (`MANIFEST`); the artifact plan says “public evidence repo private” (`NOTE notes/reports/p13-7-artifact-plan.md:54`) and “No visibility change, tag, release, DOI, or submission until the PI approves…” (`NOTE …:84`).
- Code: GPU at `f60ce64` on `feature/gpu-acceleration`; CPU baseline at `f23d450`, “the record does not claim that commit is on main” (`MS p10`). No tagged release.
- Manifest hash: `MANIFEST.factorized_ablation.sha256 = 9d788e6e828a4ea631ae5af46bb9032322b1dcd310656a4f9096c2658c9bd6c9`; actual `sha256sum paper/evidence/tsa24-factorized-ablation.json` = `e958a621cd17dd4f8476bc3ea6ecedfd022cd2c0538bf19b8b8bab5cfee995e2`. The manifest hash matches the file at commit `24add97`, not the current file (the current file changed at `794855e`); the manifest was not updated. The significant-figures review says “`paper/release/manifest-v0.2.0-candidate.json` … hashes match” (`NOTE notes/reports/significant-figures-review-2026-11-11.md:46`), which is false for this file.
- The paper says “A record with a mismatched hash or objective is not evidence” (`MS p9`). By its own rule, the factorized-ablation evidence is currently not evidence until the manifest is fixed.
- The cover letter says “a reader can inspect, replay, and challenge every reported incumbent” (`paper/submission/cover-letter.md`), which contradicts the private evidence.
- The search operators and SA schedule are not described; the records’ `algorithm.config` contains population/generations/seed/targets but not selection/crossover/mutation/annealing parameters (`EV …r1`; `MS p6`, `MS p11`). The replay gate is “a separate program” (`MS p9`) but is not public.

**Why it matters.** The paper’s central claim is a reproducibility contract. If the schedules and replay scripts are private, the contract is a design, not a delivered result. The stale manifest is exactly the failure mode the paper claims to prevent. The missing search-operator description means even a reader with the code could not reproduce the search.

**Action.**
- Create a public tag/release (and a DOI) with the schedules, replay scripts, container/environment, and a one-command replay. Update the manifest and the audit note. If the release cannot be made before submission, remove the “reproducibility contract” contribution, the “reader can replay” language, and the “public frozen artifact” implication that the reported results are inspectable.
- Tag the code commits used for the GPU and CPU runs; do not rely on branch names or non-main commits. State the data and code licenses.
- Describe the GA operators and SA schedule in the methods (selection, crossover, mutation, acceptance, cooling, move probabilities). Add them to the record schema.
- Fix the factorized-ablation manifest hash and regenerate the audit. Add a hash check to the audit, not just a claim.
- Name the evidence repository and its access status in the Data availability statement; if it is private, say “private until release” explicitly.

---

### M7. The CUDA search-time data are non-monotonic and the explanation does not fit the reported build times

**Claim.** Table 5 reports CUDA search times that *decrease* with more generations: 41.7 s at 1 generation, 33.7 s at 10, 23.9 s at 100. CPU times increase: 26.2, 71.5, 529. The manuscript attributes the 1-generation slowness to “model/table overhead,” but the build times are reported separately and the 100-generation total is lower than the 1-generation total. The implied marginal CUDA search cost is negative.

**Evidence.** `Table 5`; `EV paper/evidence/tsa24-matched-search.json`:
- CUDA: build 79.694 s, search 41.655 s (1 gen); build 88.843, search 33.675 (10); build 70.684, search 23.866 (100).
- CPU: build 67.543, search 26.241 (1); build 63.205, search 71.485 (10); build 69.249, search 528.756 (100).
- The text says “At one generation the CUDA path is slower (41.7 s vs 26.2 s search), because model/table overhead dominates” (`MS p14`).
- If search time were cumulative, the 100-generation CUDA run should be at least the 1-generation run plus 99 generations of work; it is 17.8 s *shorter*. The 100-generation total (build + search = 94.6 s) is also shorter than the 1-generation total (121.4 s). A fixed overhead cannot explain a total that is lower for more work.
- Figure 3(a) shows the CUDA line decreasing from 1 to 100 generations; the visual is consistent with the table, which makes the anomaly visible to any reader (`Fig 3`).
- A separate consistency issue: the 100,000-generation seed-7 row in Table 2 is 856 s search / 942 s wall, but the five-seed campaign runs (seeds 1–5) are about 776 s search / 798 s wall and use about 9.0 GB, while seed 7 uses 8.26 GB (`EV evidence/ws4-tsa24-gpu-ga-100000-r1…r5`, `…r7`). The ~18% wall difference at the same budget and the memory difference are not explained; the scaling curve mixes a different run/configuration from the campaign. The manuscript says seed 7 “is retained as a reference run” (`MS p11`) but does not say why it is 18% slower.

**Why it matters.** Table 5 and Figure 3 are a central result. A non-monotonic timing curve with a negative marginal cost undermines the 22.2× claim and suggests the three CUDA runs are not comparable (different warm-up, JIT/capture, code state, or timer scope). The paper’s explanation is an inference, not evidence.

**Action.** Provide a timing breakdown for every cell: setup/cache load, JIT/capture, per-generation search, verification/replay. Rerun the six cells in one harness with the same warm-up and the same code commit. Report the per-generation slope and the raw timings. If the 1-generation run includes a one-time overhead that is not in `build_s`, say so and exclude it from the search-time comparison; if the runs used different code or hardware states, disclose and rerun. Do not report the 22.2× ratio until the timing is monotonic and explainable. For the seed-7/campaign difference, either use a campaign run for the 100k scaling row or explain the configuration/resource difference and report per-run memory.

---

### M8. There is no independent baseline, so “fast enough” and the quality of 517.862 are undefined

**Claim.** The paper has no independent harvest-scheduling model, no MIP/LP bound, and no standard heuristic baseline. The CPU-SA comparator is untuned, one seed, time-limited, not converged, and its “204,413 operable blocks” is a mislabel. The reader cannot judge whether 517.862 is good.

**Evidence.** The paper says “no independent harvest-scheduling model is available on the same instance” (`MS p2`) and repeats it in the limitations (`MS p17`). The CPU-SA is “untuned, single-seed, time-limited, and not equal-work” (`MS p17`); it “performs 100,000 single proposals, whereas the GPU-GA path evaluates a population of 64 for 100,000 generations (6.4 million genome evaluations)” (`MS p11`). The internal baseline note says “Scheduled blocks 204,413” and calls the 32-start result an “invalid comparator” (`NOTE notes/reports/p13-6-paper1-baselines.md:22-24`); the CPU-SA record’s `instance.variables` is 208,255 (`EV evidence/ws4-tsa24-cpu-sa-100000-r7/record.json`). The manuscript says “The CPU-SA run has 204,413 operable blocks in its schedule, while the GPU schedule has 208,255. The difference is small relative to the instance, but it means the two runs do not cover exactly the same decision set” (`MS p13`). The “operable blocks” wording is not supported: operable blocks are a property of the instance (208,255), and the empty chain is a valid decision (`MS p4`). The note calls 204,413 “scheduled blocks”; whether that is the count of non-empty chains or an incomplete schedule is not stated. The CPU-SA `result.feasible` and `exact_replay` are true, so the record treats the schedule as valid; the manuscript must say what 204,413 counts before inferring a different decision set.

**Why it matters.** The paper asks whether the architecture is “fast enough” (`MS p2`), but “enough” has no reference. A 100,000-generation run at 856 s is fast or slow only relative to a baseline. The CPU-SA comparator is not a baseline; the paper says so. Without a lower bound or an independent heuristic, the reader cannot tell whether 517.862 is near-optimal, mediocre, or meaningless under the target.

**Action.**
- Add at least one independent baseline on the same instance: an LP/MIP relaxation bound (even if not solved to optimality), a standard greedy/priority heuristic, or an independent harvest-scheduling implementation. Report the gap and time-to-quality.
- If no baseline is feasible, remove “fast enough” and the quality implications; present only the exact replay and cost measurements. Do not use the CPU-SA as a quality comparator.
- Correct the CPU-SA description: report “scheduled blocks” or “non-empty chains,” not “operable blocks”; remove the unsupported “different decision set” inference unless the authors can show the CPU-SA schedule omits blocks that the GPU schedule includes.
- Report the CPU-SA flow/level split and realized level range. The record has them (`EV …cpu-sa`: flow 335,044,373.5; level 603.15; realized 26.43–87.79M), and they show the CPU-SA profile is flow-dominated and highly uneven. That is more informative than the total alone.

---

### M9. The abstract, title, and figures overclaim relative to the body

**Claim.** The abstract leads with the 248× GPU speedup and the 517.862 objective; the title foregrounds “GPU population search”; the body says the GPU benefit is not established and the objective is dominated by a deliberately unattainable target. The abstract says “four concerns” while the introduction says “five layers.” The figures do not show the central “flat profile” result.

**Evidence.**
- Abstract: “A 1,000-generation GPU search reduces the weighted penalty from 1,722,140,000 to 8,588,730… a 100,000-generation, five-seed campaign reaches 512.574–518.621… A factorized 64-genome batch is 248 times faster on CUDA than on CPU…” (`MS p1`).
- Body: “The reported campaign does not establish that the GPU path is faster per unit of exact work than a tuned CPU implementation, and it does not establish that the architecture is the cause of the observed quality” (`MS p15`); “the CPU objective is about 5% lower” at 100 generations (`MS p14`); “the 70M level aspiration is deliberately unattainable” (`MS p17`).
- Title: “Compiled landscape optimisation: exact resident state and GPU population search for harvest scheduling” (`MS p1`). The GPU is a method, not a demonstrated benefit.
- Count mismatch: abstract “separates four concerns” (`MS p1`) vs introduction “The architecture has five layers” (`MS p2`); Figure 1 has four boxes (compiled model, candidate + effect index, exact resident state, GPU/CPU search) (`Fig 1`).
- Figure count: three figures. Figure 1 is a schematic; Figure 2 is a three-point scaling plot; Figure 3 is a two-panel, three-point matched search (`Fig 1`–`Fig 3`). There is no map of the TSA24 landscape, no 20-period flow/level profile, and no schedule visualization. The paper says the reader can “inspect the compromise” (`MS p5`), but Table 3 gives only per-seed ranges, not the 20-period profile.
- The abstract’s “four concerns” groups the candidate index and sparse effect table; the intro separates them. The figure follows the abstract, not the intro.

**Why it matters.** The abstract and title set expectations the body does not meet. EMS readers will judge the paper by the abstract, the figures, and the first page; the current first page sells a GPU speedup and a low objective, then the body withdraws both. The missing profile figure is a substantive evidence gap: the paper’s central claim is a flat harvest profile, but the reader never sees the profile.

**Action.**
- Rewrite the abstract to lead with the architecture and exact-replay contribution, the one-landscape scope, and the negative GPU result. Move the 248× and 517.862 numbers to the results, with their scopes, or state them in the abstract with the caveats in the same sentence.
- Retitle to remove the GPU emphasis unless the GPU benefit is demonstrated. A title such as “A compiled-state architecture and exact replay for landscape harvest scheduling” would match the evidence; the current title does not.
- Reconcile four vs five: either say “four concerns” in both places (and explain that the candidate index and effect table are one concern) or say “five layers” in both.
- Add a 20-period flow/level profile figure for the five seeds, with the 70M aspiration line and the ±1% band, and a landscape map or schedule figure. This is the single most useful addition for an EMS reader: it makes the “maximum even-flow” claim inspectable and shows what the search actually produced.
- Report the mean level (51.9–52.1M) in the abstract, not only the min–max range; the level penalty uses the mean (M4).

---

## Minor comments

### Abstract and front matter

1. `MS p1`: “four concerns” vs `MS p2` “five layers” — reconcile (M9).
2. `MS p1`: “The frozen dataset, target, and seed are public” — the schedules/replay are private (`MS p18`). Reword to “the dataset and target are public; the schedules and replay scripts are not yet released.”
3. `MS p1`: “248 times faster on CUDA than on CPU” — add “on a single-device, untuned CPU path” in the same sentence, or move the number out of the abstract. The current caveat arrives one sentence later.
4. `MS p1`: “the contribution is the architecture and its reproducibility contract” — the contract is not delivered (M6). Either deliver it or say “the architecture and a replay design.”
5. `MS p1`: the opening claim “Landscape forest planning models are difficult not because the objective is exotic, but because…” is asserted without a citation or evidence. Soften (“In our experience…”) or support it from the related work.
6. `MS p1`: “UBC FRESH Lab” is not expanded. The naming note says FRESH is an acronym (`NOTE notes/reports/naming-convention.md:3`); expand it at first use or add a footnote. Do not guess the expansion.
7. `SUB p1`; `TEX paper/submission/paper1-elsarticle.tex:20`: placeholder author (`UBC FRESH Lab`) and `author@example.invalid`. The submission README and editor checklist say the metadata is placeholders. This is a submission-readiness issue, not a content issue, but it must be fixed before any resubmission.
8. `paper/submission/highlights.md`: “22-fold CPU/CUDA search-time ratio” is ambiguous. Say “22-fold longer CPU search time at 100 generations” or “22-fold shorter CUDA search time.”
9. `paper/submission/cover-letter.md`: “a reader can inspect, replay, and challenge every reported incumbent” contradicts the private evidence (`MS p18`). Remove or qualify.

### Introduction, related work, and model

10. `MS p2`: “three contributions” — the second (“an exact replay contract… including a public frozen artifact”) is not delivered. Either deliver the public schedules/replay or rewrite the contribution.
11. `MS p3`: the related work cites Barr et al., Hooker, and McGeoch on experimental reporting, but the paper’s comparisons are one-seed and uncontrolled. Either follow the cited reporting discipline or explain why the case study is exempt.
12. `MS p3`: the related work is about spatial harvest scheduling with adjacency/opening-size constraints; the experiment has none (`MS p2`, `MS p6`). Add a paragraph explaining why the spatial-constraint literature is relevant to a run without spatial constraints, or move the spatial-constraint case from future work (`MS p17`) into the paper.
13. `MS p3`: “This is closest in spirit to the exact incremental evaluation used in move-based local search” — the manuscript does not compare the architecture to any existing incremental-evaluation implementation or to the WS4 baseline it extends. State what is new relative to prior software.
14. `MS p4`: “license terms” — the CPU-SA record’s `instance.license` is null (`EV evidence/ws4-tsa24-cpu-sa-100000-r7/record.json`). State the data and code licenses explicitly; do not rely on “license terms.”
15. `MS p5`: “every period carries a linear harvest-level target” and “every period has a downward gradient” — contradicted by the mean-based level term (M4). Correct.
16. `MS p5`: “a dominant even-flow target defines the shape” — in the final objective, the level term (515.141) dominates the flow term (2.721) (`Table 2`). Say “dominant in weight, not in final magnitude” or explain the scale.
17. `MS p5`: “The very large initial penalty is dominated by even-flow deviations” — the initial flow/level split is not reported. Report it, or remove the claim.
18. `MS p6`: “A 1,000-iteration screen… shows how strongly the target construction controls the objective scale” — the main target improves only ~0.48% from the initial objective (1.7221e9 → 1.7138e9; my calculation from `Table 1` and `MS p5`). The screen is near-initial; call it an initial-scale check, not a search result.
19. `MS p6`: the screen configuration (1,000 SA iterations, 8 threads) is only in the Table 1 caption and the evidence JSON; it is not in Methods 4.13 (`MS p11`). Add it to the methods.
20. `MS p6`: “target-weight sensitivity at the full budget remains future work” — for a paper whose result is a weighted objective, this is a major omission, not a future-work item (M5).

### Methods and evidence contract

21. `MS p7`: the candidate index size is not reported. The records give `options: 50,096,749` (`EV evidence/ws4-tsa24-gpu-ga-100000-r1/record.json`). Report the total and the per-block distribution; the “rich enough for non-trivial treatment scheduling” claim needs it.
22. `MS p8`: the full effect-table build time, size, and nonzero count are not reported. Only the factorized build (234 s; `MS p14`) is given. The architecture’s cost claim needs the full table’s numbers, not just the 4-cell microbenchmark.
23. `MS p9`: “A record with a mismatched hash or objective is not evidence” — the manifest’s factorized hash is stale (M6). Fix the manifest and add a hash check to the audit.
24. `MS p9`: “The replay gate is a separate program” — the gate is not public. State where it is and how a reader can run it.
25. `MS p10`: GPU code at `f60ce64` on `feature/gpu-acceleration`; CPU at `f23d450`, “not on main.” Use tags or releases, not branch names/non-main commits. A reader cannot rely on a branch that may be force-pushed or deleted.
26. `MS p10`: “the large GPU effect table and caches are not part of the 4.66 MB artifact” — the 4.66 MB figure is not explained in the manuscript. Say what the 4.66 MB contains (dataset? manifest?) and where the number comes from.
27. `MS p11`: “The 100,000-generation campaign uses seeds 1–5; seed 7 is retained as a reference run” — Table 3 includes seed 7 without a separator or footnote. Fix (M3).
28. `MS p11`: “A full-instance whole-schedule ablation is impractical” — the full-instance evaluation time is not reported. The 5,000-block cold evaluation is 54.8 s (`MS p13`; the manuscript says 54.9 s, see item 32); a full-instance number would make the 2.00e3 factor interpretable. Report it or explain why not.
29. `MS p11`: “the first 5,000 blocks of the recorded 100k schedule” — the selection is not random. State the ordering (block ID? spatial?) and why the subset is representative. A random sample would be more defensible.
30. `MS p11`: “each row is one seed” (Table 5 text) — the table rows are generations, not seeds; the run has one seed. Reword.
31. `MS p13`: “The CPU-SA run has 204,413 operable blocks” — the note says “Scheduled blocks 204,413” (`NOTE notes/reports/p13-6-paper1-baselines.md:22`); the record’s `variables` is 208,255. Correct the terminology and the “different decision set” inference (M8).
32. `MS p13`: “54.9 s” — the evidence value is 54.8465589 s; three significant figures = **54.8 s**, not 54.9 s (`EV evidence/ws4-tsa24-eval-ablation.json`; `NOTE notes/reports/significant-figures-review-2026-11-11.md:24` repeats the error). Fix.
33. `MS p13`: “a factor of 2.00 × 10^3” — the exact ratio is 2,004.75; three significant figures = 2.00e3 ✓. The text should say “about” (it does) and give the numerator/denominator definitions (warm whole-schedule move evaluation vs delta+apply, not cold full simulation).
34. `MS p14`: “The maximum absolute error against the exact evaluator is 1.71 × 10−6 on both paths” — if the CPU path is the exact evaluator, why is its error nonzero? Name the reference evaluator and give the relative error and the objective scale. The table’s “Max error” column has no units.
35. `MS p14`: “The CPU batch takes 23.1 s; the CUDA batch takes 0.0931 s” — the batch is 64 genomes and 4 cells. A batch-size sweep (64, 256, 1024) would show whether 248× is a small-batch artifact. The GPU peak is 9.27 GB; the CPU memory is not reported. Report both.
36. `MS p14`: “At one generation the CUDA path is slower… because model/table overhead dominates” — contradicted by the build times and the non-monotonic search times (M7). Remove the inference or support it with a breakdown.
37. `MS p14`: “the CPU objective is about 5% lower” — exact 5.1185%; the figure annotation says “5.0%” (`Fig 3`), which is wrong at one decimal place. Use 5.1% (per the numeric policy, `NOTE notes/reports/numeric-reporting-policy-2026-11-11.md:26-27`) or “about 5%.”
38. `MS p14`, `Table 5`: “0.63” for the 1-generation CPU/CUDA ratio — exact 0.62996; three significant figures = 0.630. Use 0.630.
39. `MS p14`, `Table 5`: the CUDA search times decrease with generations (41.7 → 33.7 → 23.9). This is the most serious data-integrity issue in the paper (M7). Do not publish the 22.2× ratio until it is explained.
40. `MS p16`: “The present experiments show that the combined path can reach a tight seed distribution” — the “combined path” includes the CPU-refinement handoff, which the abstract and Section 4.9 say is “designed but not measured” (`MS p1`, `MS p9`). The measured campaign is GPU search + CPU replay, not CPU refinement. Correct the discussion or measure the handoff.
41. `MS p17`: “An exact MIP proof is not practical at this scale” — no bound is attempted. Add a simple LP/greedy bound or say “no bound attempted”; the reader has no sense of optimality.
42. `MS p17`: “fast enough for a 100,000-generation GPU campaign” — “fast enough” is undefined without a baseline (M8). Remove or define.
43. `MS p18`: the Data availability URL wraps across a line in the PDF (`femic-tsa` / `24-instance`). Verify that it resolves and is not hyphenated; use `\url{}` consistently.
44. `MS p18`: “retained in the project evidence repository” — name the repository and its access status. If it is private, say “private until release.”
45. `TEX paper/experiments/run_matched_search.sh:2`: the comment says “Reproduce the TSA24 matched CPU/CUDA search rows in Table 3,” but the matched search is Table 5. Fix the reference.
46. `paper/tables/evidence.md`: the evidence table includes `fhops-small21` and `fhops-tiny7` records that are not in Paper 1, and it reports 10-decimal objectives. The manuscript says the table is “generated from the record files” (`MS p9`); either scope the table to Paper 1 or explain the extra rows. The manuscript’s tables are hand-rounded, so the “generated” claim is overstated.
47. `NOTE notes/reports/significant-figures-review-2026-11-11.md:46`: “hashes match” is false for `paper/evidence/tsa24-factorized-ablation.json` (M6). Fix the note; a reviewer should not have to catch this.
48. `NOTE notes/reports/significant-figures-review-2026-11-11.md:24`: “54.9 s” repeats the rounding error; the value is 54.8 s at three significant figures. Fix both the note and the manuscript.
49. `Table 2`, `Table 3`: the flow terms are under-reported relative to the stated six-significant-figure policy: 2.7211207 → 2.72112; 1.3310357 → 1.33104; 0.07592449 → 0.0759245. The level terms are six figures; the flow terms are four/two. Apply the policy consistently (`NOTE notes/reports/numeric-reporting-policy-2026-11-11.md:15-19`).
50. `Table 2`, `Table 3`, `Table 5`: the objective/flow/level columns do not state units. The numeric policy says “Tables state the relevant unit in the column header” (`NOTE notes/reports/numeric-reporting-policy-2026-11-11.md:31`). Add “penalty units (dimensionless)” or the correct unit; Table 4’s “Max error” has no unit.
51. `Table 1`: the caption says “1,000 SA iterations, seed 7, same start; screen only,” but the text does not give the initial objective for each target. Add the initial value and the improvement; otherwise the reader cannot tell the screen is near-initial.
52. `Table 3`: the title says “Five-seed 100,000-generation campaign” but the table has six rows. Retitle or separate seed 7 (M3).
53. `Table 4`: “Max error” is identical for CPU and CUDA (1.71e-6). Explain why the CPU path has nonzero error and identify the reference. Give the relative error.
54. `Table 5`: the caption says “The 100-generation CUDA run uses 22-fold less search time” — “22-fold less” is ambiguous; say “22.2 times shorter” or “the CPU search is 22.2 times longer.” The table’s “CPU/CUDA time” column is a ratio; label it “CPU/CUDA search-time ratio.”
55. `Fig 2`: a three-point log-log plot is a budget sweep, not a scaling law. The text calls it a “scaling curve” (`MS p12`); say “budget sweep” or add more budgets.
56. `Fig 3`: the annotation “CPU objective 5.0% lower at 100 generations” is wrong at one decimal (5.1%); it also ignores that the CPU is 8.2%/8.6% lower at 1/10 generations. Annotate all three or say “CPU lower at all budgets.”
57. `MS p1`, `Fig 1`: the architecture figure has four boxes; the intro says five layers. If the candidate index and effect table are separate layers, show five boxes; if they are one concern, say four consistently.

### Submission package

58. `SUB p1`; `TEX paper/submission/paper1-elsarticle.tex:20-22`: placeholder author and email; the editor checklist has unchecked author/CRediT/funding/competing-interest items (`paper/submission/editor-checklist.md`). Fix before resubmission.
59. `paper/submission/editor-checklist.md`: “40 references, 3 figures” — the reference count is at the lower end of the 40–60 range; the figure count is thin for a 21-page paper (M9). Not fatal, but consider adding the profile/map figures.
60. `paper/submission/README.md`: “29 pages, 11pt preprint” — the main PDF is 21 pages; the journal variant is 29. The content is the same. No action needed, but do not let the page count hide the thin evidence base.

---

## Risk table

| # | Risk | Likelihood | Impact | Evidence | Mitigation |
|---|---|---|---|---|---|
| R1 | Desk reject for EMS scope/fit: single-instance software case study, no environmental validation | High | Fatal | `MS p1`–`MS p2`, `MS p16`, `MS p17`; `NOTE p13-9` | Add an environmental validation/second landscape/spatial-constraint case, or reframe for SoftwareX/JORS |
| R2 | Reject for unsupported architecture claim: no controlled architecture ablation | High | Fatal | `MS p15`, `MS p17`; `Table 4`, `Table 5`; `NOTE p13-5` | Add architecture-on/off ablation and a tuned CPU baseline at equal work; or remove the performance claim |
| R3 | Reject for irreproducibility: schedules/replay private; no DOI | High | Fatal | `MS p1`, `MS p18`; `MANIFEST.status`; `NOTE p13-7` | Public tag/release/DOI + one-command replay; tag code; state licenses |
| R4 | Data-integrity challenge: CUDA search times decrease with more work | Medium–High | Major | `Table 5`; `EV paper/evidence/tsa24-matched-search.json`; `Fig 3` | Rerun all cells in one harness; report setup/JIT/per-generation breakdown; remove 22.2× until explained |
| R5 | Manifest/audit inconsistency: stale factorized hash; audit says hashes match | Certain | Major | `MANIFEST.factorized_ablation`; `sha256sum` of `paper/evidence/tsa24-factorized-ablation.json`; `NOTE significant-figures:46` | Regenerate manifest; fix audit; add hash check to the audit |
| R6 | Statistical challenge: one seed, no CI, six-row table under a five-seed title | High | Major | `Table 3`, `Table 5`; `MS p16`; my six-row mean 516.045/median 516.234 | Report per-seed values, SD/CI, paired seeds; fix the table title/rows |
| R7 | Objective-definition challenge: level term is mean-based/normalized but described as per-period linear | High | Major | `MS p5`; `EV …r1`–`…r7`; level = 20×100×(70M−mean)/70M | Write exact equations, units, normalization; correct the “every period” claim; report mean/profile |
| R8 | Target justification/sensitivity: 70M/100/±1%/10,000 unjustified; screen near-initial | High | Major | `MS p5`–`MS p6`; `Table 1`; `NOTE p13-8` | Justify from artifact/policy; full-budget sensitivity; report initial vs screen |
| R9 | No independent baseline; “fast enough” undefined; CPU-SA mislabeled | High | Major | `MS p2`, `MS p13`, `MS p17`; `NOTE p13-6:22`; CPU-SA record | Add LP/MIP bound or independent heuristic; correct CPU-SA terminology; drop “fast enough” |
| R10 | Single landscape; no spatial constraints; architecture may not generalize | High | Major | `MS p2`, `MS p6`, `MS p16`, `MS p17` | Second landscape/stress instance; adjacency/opening-size case |
| R11 | Abstract/title overclaim relative to body; four vs five layers; no profile figure | Medium | Moderate | `MS p1`–`MS p2`, `MS p15`; `Fig 1`–`Fig 3` | Rewrite abstract/title; reconcile; add 20-period profile and map |
| R12 | Submission package not ready: placeholder author/email, unchecked metadata | Certain | Minor | `SUB p1`; `TEX paper/submission/paper1-elsarticle.tex:20`; `paper/submission/editor-checklist.md` | Fill metadata, CRediT, funding, competing interests, licenses |

---

## P0 / P1 / P2 remediation list

### P0 — must be resolved before any resubmission

1. **Public evidence release.** Publish the schedules, replay scripts, environment/container, and a one-command replay with a DOI/tag. If this is impossible, remove the “reproducibility contract” contribution and the “reader can replay” claims (`MS p1`, `MS p18`; `MANIFEST.status`; `NOTE p13-7`).
2. **Fix the manifest and audit.** The factorized-ablation hash is stale (`MANIFEST.factorized_ablation = 9d788e…`; actual `e958a6…`); the audit says hashes match (`NOTE significant-figures:46`). Regenerate the manifest, fix the audit, and add a hash check.
3. **Resolve the CUDA timing non-monotonicity.** Rerun the six matched-search cells in one harness; report setup/JIT/per-generation/verification; remove the 22.2× claim until the timing is monotonic and explainable (`Table 5`; `EV matched-search`; `Fig 3`).
4. **Correct the level-term definition and units.** State the normalization and the mean-based penalty; remove “every period has a downward gradient” if the penalty is mean-based (`MS p5`; records).
5. **Decide the architecture claim.** Either add a controlled architecture-on/off ablation and a tuned CPU baseline at equal work, or remove the architecture-performance claim and present the paper as a design/case study (`MS p15`, `MS p17`; `Table 4`, `Table 5`).
6. **Either add an independent baseline or remove the quality/“fast enough” claims.** The paper currently says both “no independent baseline” and “fast enough for a 100,000-generation campaign” (`MS p2`, `MS p17`). Pick one.

### P1 — major revision

7. Report per-seed values, SD, and a 95% interval for the five-seed campaign; fix Table 3’s six-row/five-seed inconsistency; report the six-row statistics or exclude seed 7 (`Table 3`; `MS p12`).
8. Repeat the matched CPU/CUDA search over at least 5–10 seeds and report the paired distribution (`Table 5`; `EV matched-search`).
9. Justify the 70M/100/±1%/10,000 target values and add a full-budget target-weight/band sensitivity (`MS p5`–`MS p6`; `NOTE p13-8`).
10. Add a second landscape or stress instance, and/or a spatial-constraint case (`MS p16`, `MS p17`).
11. Add a 20-period flow/level profile figure with the 70M line and a landscape map/schedule figure (`Fig 1`–`Fig 3`; `MS p5`).
12. Correct the CPU-SA “204,413 operable blocks” mislabel and the “different decision set” inference; report the CPU-SA flow/level split (`MS p13`; `NOTE p13-6:22`).
13. Describe the GA operators and SA schedule; add them to the record schema (`MS p6`, `MS p11`; records).
14. Report the full effect-table build time, size, and nonzero count; report the candidate index size (50,096,749 options) (`MS p7`–`MS p8`; `EV …r1`).
15. Tag the code commits (`f60ce64` GPU, `f23d450` CPU) with releases; state data/code licenses (`MS p10`; `MS p4`; CPU-SA record `instance.license` null).
16. Fix the Discussion’s “combined path” claim: the CPU-refinement handoff was not measured (`MS p16` vs `MS p1`, `MS p9`).
17. Rewrite the abstract/title to match the evidence; reconcile four vs five layers (`MS p1`–`MS p2`).
18. Fix the precision errors: 54.8466 → 54.8, not 54.9; 5.1185% → 5.1%, not 5.0%; flow terms to six significant figures (2.72112, 1.33104, 0.0759245); 0.630 not 0.63 (`MS p13`–`MS p14`; `Table 2`, `Table 3`, `Table 5`; `NOTE significant-figures:24`).

### P2 — minor / clarity

19. Add units to all table columns (objective/flow/level/max error) (`Table 1`–`Table 5`; `NOTE numeric-reporting-policy:31`).
20. Fix the Table 3 title/rows and the “all five schedules” sentence (`MS p12`; `Table 3`).
21. Fix the `run_matched_search.sh` “Table 3” comment to “Table 5” (`TEX paper/experiments/run_matched_search.sh:2`).
22. Fix the wrapped/ambiguous Data availability URL and name the evidence repository/access status (`MS p18`).
23. Explain the 4.66 MB artifact contents (`MS p10`).
24. Clarify “23.1 s / 0.0931 s” batch size and add a batch-size sweep (`Table 4`).
25. Clarify the 5,000-block subset selection (first 5,000, not random) and the 50 moves (`MS p11`, `MS p13`).
26. Fix the cover letter’s “reader can replay” claim and the highlights’ “22-fold CPU/CUDA ratio” wording (`paper/submission/cover-letter.md`; `paper/submission/highlights.md`).
27. Fill the submission metadata (author, email, CRediT, funding, competing interests, licenses) (`SUB p1`; `TEX paper/submission/paper1-elsarticle.tex:20`; `paper/submission/editor-checklist.md`).
28. Add the duplicate-run determinism check (identical schedule SHA-256) to the manuscript; it is stronger than the current replay sentence (`EV …10000-r7`).
29. Expand “FRESH” at first use or add a footnote (`MS p1`; `NOTE naming-convention.md:3`).
30. Fix “The matched implementation comparison below” in Section 6.3 — the comparison is above, not below (`MS p17`).
31. Standardise the record metadata: `EV evidence/ws4-tsa24-gpu-ga-10000-r7/record.json` has `run.generations = 0` for a 10,000-generation run; the 1,000-generation record omits `run.generations`; the CPU-SA record has `instance.license = null`. Use one schema and one set of required fields.

---

## Journal-fit and fallback assessment

### EMS

The paper is a software/operations-research case study with a forest-planning application. EMS publishes software and model papers, but the environmental modelling contribution here is the input landscape and a harvest-flow target, not an environmental model or a validated application. There is no ecological validation, no management scenario, no spatial-constraint case, no second landscape, and no independent baseline. The paper’s own conclusion disclaims competitive landscape performance and operational impact (`MS p17`). The contribution is the architecture and a replay contract; the replay contract is private (`MS p18`). On the current evidence, EMS is the wrong venue. If the authors add a genuine environmental validation and a second landscape, the paper could fit as an EMS software/system paper; that is a new paper, not a revision of this one.

### SoftwareX

SoftwareX is a natural venue for a software architecture paper, but the current manuscript is a 21-page research article (8,574 words), not a short software-tool paper, and it lacks the software metadata a software venue would expect: a public code release, a version/tag, a license, documentation, tests, and a reusable example. The paper-specific code is private; the GPU code is on a feature branch; the CPU baseline is on a non-main commit (`MS p10`). SoftwareX would also require the artifact to be public. A condensed software paper (architecture, artifact, replay, one or two examples) could work after the P0 release and the timing fix.

### JORS

JORS (Journal of Open Research Software) would fit a reproducibility/software case study if the artifact is public, citable, and reusable. The current paper has the right instincts — exact replay, records, hashes — but the release is private and the manifest is stale. JORS is shorter than the current manuscript; the 21-page case study would need to be cut to the software/reproducibility core. The negative GPU/architecture result is acceptable for JORS if the software is the contribution, but the paper would need to state clearly what the software does and how to reuse it.

### Bottom line

The paper cannot go to EMS in this form. It is not ready for SoftwareX/JORS either, because the public artifact and one-command replay are missing and the manifest/timing issues must be fixed. The authors should choose the venue after the P0 work: if they add environmental validation and a second landscape, try EMS again; if they keep the architecture/replay focus, condense for SoftwareX/JORS with a public DOI.

---

## Recommendation and review-after-revision statement

**Recommendation:** **Reject** for Environmental Modelling & Software.

**Basis.** The paper does not meet the EMS contribution bar (M1), does not establish the architecture claim (M2), is not statistically defensible (M3), misdescribes the objective’s level term and units (M4), does not justify the target or test a second landscape (M5), withholds the evidence that is the core of its reproducibility claim (M6), contains a non-monotonic CUDA timing result that undermines a central table (M7), has no independent baseline (M8), and overclaims in the abstract/title relative to the body (M9). The paper is honest about many of these limits, but a limitations section is not a substitute for the missing experiments.

**Prepared to review after revision:** **No** for the current submission. I would be willing to review a **new** submission if:
1. the schedules, replay scripts, and one-command replay are public with a DOI/tag, and the manifest/audit hashes are correct;
2. the architecture claim is tested with a controlled architecture-on/off ablation and a tuned CPU baseline at equal work, or the performance claim is removed;
3. the CUDA timing is rerun and explained, or the 22.2× claim is removed;
4. the level-term definition/units are corrected, and the target values/sensitivity are justified;
5. the paper either adds an environmental validation/second landscape/spatial-constraint case (EMS) or is reframed and shortened for SoftwareX/JORS.

**Confidence:** High for the numerical, manifest, and evidence findings (I recomputed them from the tables/records and hashes). Moderate for the journal-fit judgment; it is based on the paper’s own scope statements and the submission materials, not on external literature.

---

## QA checklist

- **Evidence-only:** Every substantive praise/critique above has an `MS`, `Table`, `Fig`, `EV`, `NOTE`, `TEX`, or `MANIFEST` tag. No external literature was used. Where a claim depends on missing information, I say so (e.g., the full effect-table size, the GA/SA operators, the 70M provenance).
- **Anonymity/privacy:** No reviewer-identifying details or third-party personal information. The report is written for the authors and editor.
- **Tone:** Critical but professional; no sarcasm, no speculation about intent. The strongest language is reserved for verifiable evidence failures (manifest hash, non-monotonic timing, private evidence).
- **Bias hygiene:** Critiques are anchored to content and evidence, not prestige, subfield preference, or personal factors.
- **Arithmetic:** Recomputed Table 2/3 sums, the five-seed mean/median, the six-row mean/median, the 248×/22.2×/2.00e3 factors, the level-term identity, and the significant-figure roundings. See the appendix.
- **Hashes:** Recomputed all manifest hashes; all match except `paper/evidence/tsa24-factorized-ablation.json`.
- **Read-only:** No manuscript or evidence file was edited. The only file created is this report.

---

## Appendix: arithmetic and consistency checks

| Check | Result | Evidence |
|---|---|---|
| Table 2 flow + level = objective | Correct within rounding for all rows: 8,588,230 + 499.821 = 8,588,729.821 → 8,588,730; 76,026.9 + 513.832 = 76,540.732 → 76,540.7; 2.721 + 515.141 = 517.862 | `Table 2` |
| Table 3 flow + level = objective | Correct for every row | `Table 3` |
| Five-seed mean / median | 515.682 / 515.938 — correct for seeds 1–5 | `Table 3`; my calculation |
| Six-row mean / median (including seed 7) | 516.045 / 516.234 — differs from the reported five-seed values | `Table 3`; my calculation |
| 248× factorized | 23.1236789 / 0.0931495 = 248.2426 → 248 | `EV …factorized-ablation` |
| 22.2× matched | 528.756 / 23.866 = 22.156 → 22.2 | `EV …matched-search`; `Table 5` |
| 2.00e3 evaluation path | 1.0863925 / 0.0005419086 = 2,004.75 → 2.00e3 | `EV …eval-ablation` |
| Level term identity | 20 × 100 × (70,000,000 − mean)/70,000,000 equals the reported level for every seed to machine precision | `EV …r1`–`…r7`; `Table 2`, `Table 3` |
| 54.8466 s at three significant figures | **54.8 s**, not 54.9 s | `EV …eval-ablation`; `MS p13`; `NOTE significant-figures:24` |
| 5.1185% at one decimal | **5.1%**, not 5.0% | `Table 5`; `MS p14`; `Fig 3` |
| Flow terms at six significant figures | 2.7211207 → **2.72112**; 1.3310357 → **1.33104**; 0.07592449 → **0.0759245**; the tables report 2.721/1.331/0.076 | `Table 2`, `Table 3`; records |
| 1-generation CPU/CUDA ratio | 26.241 / 41.655 = 0.62996 → **0.630**, not 0.63 | `Table 5`; `EV …matched-search` |
| CPU-SA wall time | 1,875.12 s / 60 = 31.252 min → 31.3 min ✓ | `EV …cpu-sa`; `MS p13` |
| Campaign wall sum | r1–r5 wall sum = 3,995.8 s; record note = 4,004.77 s → 4.00e3 ✓ | `EV …r1`–`…r5`; `MS p12` |
| CUDA search monotonicity | 41.655 → 33.675 → 23.866 s for 1 → 10 → 100 generations; negative marginal cost | `EV …matched-search`; `Table 5`; `Fig 3` |
| Manifest factorized hash | Manifest `9d788e…`; actual `e958a6…` — mismatch | `MANIFEST.factorized_ablation`; `sha256sum paper/evidence/tsa24-factorized-ablation.json` |
| CPU-SA “204,413 operable blocks” | Note says “Scheduled blocks 204,413”; record `variables` = 208,255 | `NOTE p13-6:22`; `EV …cpu-sa`; `MS p13` |
| Record metadata | 10,000 record `run.generations = 0`; 1,000 record omits the field; CPU-SA `instance.license = null` | `EV …10000-r7`; `EV …1000-r7`; `EV …cpu-sa` |
| “4.00e3 s wall for all five runs” | Correct as a sum/record note; not the elapsed campaign time | `EV …r1` note; `MS p12` |

**End of report.**
