# Reviewer Report — Paper 2 (Journal of Heuristics)

**Manuscript:** FRESH Solutions: a reproducible adapter harness for applied metaheuristic benchmarks
**Authors:** UBC FRESH Lab (main PDF; JoH variant uses placeholders)
**Materials reviewed:** `paper2/paper2-manuscript.pdf` (24 pp., 5 figures), `paper2/paper2-manuscript.tex`, `paper2/evidence/`, `paper2/evidence/manifest-v0.1.0-candidate.json`, `paper2/submission/paper2-sn-jnl.pdf` (28 pp.), `notes/reports/p13-2-qap-bls.md`, `notes/reports/p13-3-generic-tabu.md`, `notes/reports/p13-1-tsp-panel.md`, `notes/reports/p13-9-review-2026-11-09.md`, `notes/reports/significant-figures-review-2026-11-11.md`, `notes/reports/naming-convention.md`, plus the replay, runner, and validator scripts.
**Reviewer stance:** Reviewer 2 / skeptical associate editor. I checked the headline numbers against the committed evidence, ran the replay scripts read-only, and recomputed the paired statistics from the per-run JSON.
**Recommendation:** **Reject** for JoH in its current form.
**Prepared to review after revision:** **Yes**, conditional on a public artifact, corrected replay/schema, cluster-robust statistics, and a reframed contribution (or a SoftwareX/JORS resubmission).

---

## Overrides (project-specific constraints)

- Target journal: Journal of Heuristics (JoH), Springer Nature `sn-jnl` variant. I assess JoH fit as a heuristic/methodological contribution, not as a software release note.
- Evidence tags: `MS pX` for the main PDF page, `Table N` / `Fig N` for manuscript objects, and repository paths for evidence, runners, and replay scripts.
- No external literature is used. General domain judgment is applied only to the submission's own claims and evidence.
- The JoH formatting variant is not reviewed as a formatting exercise; content differences and metadata defects are noted only where they affect the submission's credibility.

---

## 1. Document inventory

| Item | Status | Notes |
|---|---|---|
| `paper2/paper2-manuscript.pdf` | Present | 24 pages, 5 figures, main `article` build. |
| `paper2/submission/paper2-sn-jnl.pdf` | Present | 28 pages, JoH `sn-jnl` variant; same abstract/content. |
| `paper2/paper2-manuscript.tex` | Present | 1,121 lines; 42 references; no undefined citations or LaTeX warnings in the logs. |
| `paper2/evidence/` | Present | 50+ JSON/JSONL files; manifest is a **candidate**, not a tagged release. |
| `paper2/evidence/manifest-v0.1.0-candidate.json` | Present | 64 files; one hash mismatch (`paper2/paper2-draft.md`). |
| `paper2/replay_all.sh` | Present | Runs, but the BLS step is miswired (see M3). |
| `paper2/check_evidence.py` | Present | Replays 40 framework QAP + 20 deep TSP; checks stored flags for expanded QAP, BLS, large-QAP, generic, LKH. |
| `paper2/README.md` | Present | Says **“DO NOT SUBMIT”** and “not a submission-ready article.” |
| `notes/reports/p13-9-review-2026-11-09.md` | Present | Internal review: Paper 2 “not submission-ready”; SoftwareX/JORS “safer target.” |
| `notes/reports/significant-figures-review-2026-11-11.md` | Present | Claims 24 pp., 9,357 words, 5 figures; claims manifest hashes match. |
| `notes/reports/naming-convention.md` | Present | FRESH uppercase; no title-case lab reference remains. |

---

## 2. Quick synopsis

- The paper specifies an adapter contract and an exact-replay evidence protocol for heuristic benchmarking, with QAP robust-tabut and TSP iterated Lin–Kernighan reference implementations. The engineering is competent, and the paper is unusually honest about failures and negative results.
- The empirical core is a 40-run framework-use check (four QAP instances × ten seeds; all match, 1.24× CPU), a 200-run QAP panel (tabu 0.301%, BLS 0.096%), a 100-run TSP expanded panel (94/100 optima, 95/100 patience, five `brazil58` cap hits), and a 40-run generic-tabu negative result.
- The headline numbers reproduce against the evidence I ran: 200/200 expanded QAP, 200/200 BLS (when explicitly pointed at the 10-seed file), 100/100 expanded TSP, 1,060/1,060 broad, 40/40 generic, 40 framework + 20 deep TSP.
- However, the paper is a **software/reproducibility report**, not a heuristic or methodological advance. The artifact is private/pending, the one-command replay does not cover the headline 10-seed BLS panel, the QAP expanded per-record schema is missing the fields the paper claims, the TSP adaptive-depth rule is contradicted by the evidence, and the BLS-vs-tabu inference ignores clustering.
- For JoH, these are not cosmetic: the paper’s own framing disclaims the kind of contribution the journal expects, and the reproducibility claim is not independently verifiable.

---

## 3. Confidential comments to the editor

I recommend **reject** for JoH. The manuscript is a careful software/reproducibility report with genuine strengths—clear adapter boundary, exact replay gate, honest failure accounting, and a serious BLS baseline—but it does not make a heuristic or methodological advance that meets JoH’s remit. The paper explicitly says the contribution is the harness, not a state-of-the-art solver (`MS p1`), and the conclusion says the next step is “a wider convergence panel, stronger independent baselines, and an approved evidence release” (`MS p21`). That is a candid admission that the current evidence is preliminary.

The central reproducibility claim is also not verifiable in the submitted form: the evidence repository is private and untagged (`MS p6`, `MS p7`, `MS p20`, `MS p21`; `paper2/evidence/RELEASE-CANDIDATE.md`), and the one-command replay does not cover the 200-run BLS panel used in Table 5 because `paper2/replay_all.sh:10` sets `QAP_BLS_EVIDENCE` but `paper2/replay_qap_bls.py:29` ignores it and defaults to the 5-seed file. The paper’s per-record schema claim (`MS p6`) is false for the 200-run QAP expanded panel, which has no `solver_commit`, `hardware`, `cpu_seconds`, or `budget` fields. The BLS-vs-tabu confidence interval is the naive pair-level bootstrap; a cluster-by-instance bootstrap is wider, and the pair-level sign test treats 200 runs as independent when there are 20 instances and 3 families.

I would be willing to review a substantially revised version, but I would not support a JoH acceptance without (a) a public tagged artifact and working one-command replay, (b) corrected per-record metadata and cluster-robust statistics, and (c) either a genuine methodological contribution or a transfer to SoftwareX/JORS. The paper is honest about its limits, which is to its credit; the limits are simply fatal for this venue.

---

## 4. Comments to the authors

### 4.1 Summary

The manuscript addresses a real problem: applying known metaheuristics to new problems is slowed by the engineering around the search—state, moves, feasibility, stopping rules, replay, and benchmark bookkeeping. The adapter contract, resident-state path, and replay gate are sensible design ideas, and the paper reports failures (generic tabu, `brazil58` cap hits, LKH large-tail gap) rather than hiding them. The QAP and TSP reference implementations are serious efforts, and the BLS baseline is a substantial addition.

The problem is that the paper is framed as a JoH heuristic contribution while its actual contribution is a software/reproducibility harness. The empirical results are a negative result for the tabu reference, a negative result for the generic layer, and a null result for framework quality (the framework matches the standalone objective and costs 1.24× CPU). The one methodological observation—budget/patience changes reported gaps—is already the subject of the benchmarking literature the paper cites. The artifact is private/pending, the one-command replay is miswired for the headline BLS panel, the QAP expanded per-record schema is incomplete, the TSP adaptive-depth protocol is contradicted by the evidence, and the BLS-vs-tabu inference is not cluster-aware. These are major issues, not polish.

### 4.2 What works (evidence-based strengths)

1. **The adapter boundary is clearly specified.** The contract separates discrete state, exact evaluation, feasibility, mutation/crossover, and reversible moves, and the engine sees only that interface (`MS p3–4`). The distinction between `apply`/`undo` exact inverses and the adapter-owned permutation invariant is well stated (`MS p4`).
2. **The replay gate is the right idea.** A stored incumbent is re-evaluated through a new adapter state, not the optimizer’s cached counter (`MS p6`). The gate checks objective, feasibility, and permutation validity, and it fails closed (`MS p6–7`). This is a genuine methodological contribution to benchmark hygiene.
3. **The failure taxonomy is useful.** Plateau stop, safety-cap hit, budget exhaustion, and invalid replay are distinguished, and the denominator is visible (`MS p7`). The broad panels report 552/670 QAP patience stops and 236/390 TSP patience stops (`MS p7`, `Table 1`), and the TSP expanded table reports `brazil58` as `Patience 0/5` while `Optima 5/5` (`Table 7`, `MS p16`). This is better than most heuristic papers.
4. **The headline numbers are traceable.** I verified the QAP expanded table against `paper2/evidence/qap-expanded-100k-10seed-summary.json` (0.301% mean, 0.043% median, 5.695% worst, 73/200 optima), the BLS table against `paper2/evidence/qap-bls-10seed-summary.json` (0.096% mean, 1.369% worst, 161/200 optima), the TSP expanded table against `paper2/evidence/tsp-expanded-10k-summary.json` (0.004% mean, 0.185% worst, 94/100 optima, 95/100 patience), and the framework table against `paper2/evidence/framework-use-summary.json` (1.239 mean CPU ratio, 1.168–1.312 bootstrap CI). The arithmetic is consistent.
5. **The replay checks pass when run correctly.** With `QAPLIB_ROOT` and `TSPLIB_ROOT` set, `paper2/replay_qap_expanded.py` reports 200/200, `paper2/replay_qap_bls.py --input qap-bls-10seed.json` reports 200/200, `paper2/replay_tsp_expanded.py` reports 100/100, `paper2/replay_broad.py` reports 1,060/1,060, `paper2/replay_generic_tabu.py` reports 40/40, and the framework/deep-TSP replays report 60/60. The data are real; the packaging is the problem.
6. **The BLS baseline is a serious effort.** It reaches 161/200 optima, beats tabu on 15/20 instance means, and is honest about the `chr22a` exception (`Table 5`, `MS p13`). The exactness check against the adapter and the asymmetric `bur` correction are described in `notes/reports/p13-2-qap-bls.md`.
7. **The FRESH naming convention is followed.** “FRESH” is uppercase, “FRESH Solutions” is the artifact, and the lower-case adjective “fresh” has been replaced with “new” (`notes/reports/naming-convention.md`; `MS p1`, `MS p21`). No title-case lab reference remains.
8. **The significant-figures policy is mostly applied.** Gaps use three decimal places, counts are exact, ratios use three significant figures, and the table values match the evidence. The one exception is the applied-case flow term `2.721` (see m8).

### 4.3 Major comments

#### M1. JoH fit: this is a software/reproducibility report, not a heuristic or methodological advance

**Evidence.** The title and abstract frame the contribution as an “adapter harness” (`MS p1`). The Introduction says “The paper asks a narrow engineering question” (`MS p1–2`). The four contributions are the adapter contract, the replay protocol, two reference implementations, and a framework-use check (`MS p2`)—all engineering artifacts. The paper explicitly disclaims a state-of-the-art solver claim (`MS p1`, abstract), and the conclusion says “The next step is not a larger claim; it is a wider convergence panel, stronger independent baselines, and an approved evidence release” (`MS p21`). The empirical results are a negative result for the tabu reference (`MS p13`), a negative result for the generic layer (`MS p18`), and a null result for framework quality (the framework matches the standalone objective and costs 1.24× CPU; `MS p11`, `MS p18`). The one methodological observation—fixed budget vs 100k patience changes gaps (`MS p19`)—is a budget effect, and the paper cites the benchmarking work that already makes this point (`MS p2–3`: Barr et al., McGeoch, Beiranvand et al.).

**Why it matters.** JoH publishes heuristic methods, their analysis, and applications. A harness paper can fit only if it makes a methodological contribution beyond software engineering. The manuscript’s own framing says it does not. A JoH editor can reasonably desk-reject on scope; a reviewer should say so explicitly.

**Action.** Choose one:
- Reframe for **SoftwareX** or **JORS**, where the harness, replay protocol, and reference adapters are the contribution. SoftwareX would value the artifact and the reproducibility protocol; JORS would value the open software and the evidence release.
- Or add a genuine methodological study for JoH: e.g., a pre-registered stopping-rule/budget analysis across QAPLIB/TSPLIB families, with a hierarchical statistical model and a new insight beyond “more budget improves gaps.” Cut the software-release material and the applied case.

#### M2. The artifact is private, untagged, and not independently verifiable

**Evidence.** `MS p6` says “The evidence release itself is a candidate until the maintainer approves a tag.” `MS p7` says “The paper-specific evidence repository is not yet public.” `MS p20` says “The evidence release and tag remain pending.” `MS p21` says “The evidence tag and release remain pending maintainer approval.” The data availability statement (`MS p21`) points to relative paths (`paper2/evidence/framework-use.json`, `paper2/evidence/tsp-convergence-10k.json`), not a public URL or DOI. `paper2/evidence/RELEASE-CANDIDATE.md` says “No tag, release, visibility change, or DOI has been made.” `paper2/evidence/provenance-2026-11-03.json` says per-record metadata is “a release blocker.” `container/README.md` says “A full container recipe is not yet claimed.” `paper2/README.md` says **“DO NOT SUBMIT”** and “not a submission-ready article.”

**Why it matters.** The paper’s central claim is reproducibility. A private, untagged, unpinned artifact is not a reproducible artifact. The reviewer can run the scripts in this workspace, but a reader cannot. The title’s “reproducible” and the abstract’s “report the full distribution” are aspirational, not current.

**Action.** Publish the evidence repository with a tag/DOI, include instance provenance/hashes, provide a working container (base image digest, solver commit, QAPLIB/TSPLIB mounts), and make `replay_all.sh` self-contained. If the artifact cannot be public at review time, remove “reproducible” from the title/abstract and present the paper as a design report.

#### M3. The one-command replay does not cover the headline 10-seed BLS panel

**Evidence.** `paper2/replay_all.sh:10` sets `QAP_BLS_EVIDENCE=qap-bls-10seed.json`, but `paper2/replay_qap_bls.py:29` defines only `--input` with default `qap-bls-expanded.json`; it never reads `QAP_BLS_EVIDENCE`. Running `bash paper2/replay_all.sh` produces `100/100 exact replays` (the 5-seed, 100-run file), while Table 5 uses 200 runs (`MS p13`). `paper2/check_evidence.py:145–161` loads `qap-bls-10seed.json` but only checks the stored `exact_replay` flag; it does not re-evaluate the assignments. `notes/reports/claim-to-evidence-audit-2026-11-09.md` says `bash paper2/replay_all.sh` covers “200 BLS” exact; the actual one-command output is 100. When run explicitly with `--input qap-bls-10seed.json`, the 200/200 replay passes, so the data are sound—but the advertised one-command claim is false.

**Why it matters.** The replay gate is the paper’s main methodological device. A miswired one-command replay is exactly the failure mode the gate is supposed to catch. It also means the headline BLS table is not covered by the advertised replay. The paper’s “The artifact is designed to fail closed” (`MS p7`) is not true for this path.

**Action.** Make `replay_qap_bls.py` read `QAP_BLS_EVIDENCE` (or change `replay_all.sh` to `--input qap-bls-10seed.json`), make `check_evidence.py` re-evaluate BLS assignments rather than trust flags, update the claim audit and `MS p6`, and add a CI test that asserts the 200/200 count.

#### M4. The per-record schema claim is false for the QAP expanded panel, and the validator description is stale

**Evidence.** `MS p6` says “the QAP-expanded, BLS, generic, and expanded-TSP files carry solver commit, hardware, stop reason, and exact-replay status but not per-record CPU time.” The 200 records in `paper2/evidence/qap-expanded-100k-10seed.json` contain no `solver_commit` (0/200), no `hardware` (0/200), no `cpu_seconds` (0/200), and no `budget` field; they carry `instance`, `seed`, `objective`, `optimality_gap_percent`, `iterations`, `stop_reason`, `wall_seconds`, `replay_objective`, `exact_replay`, and `converged_on_patience`. `MS p9` says “The per-run files carry the seed, budget, stop reason, and assignment”—the QAP expanded file has no budget. `MS p6` says “The validator replays the 40 framework, 20 deep-TSP, 20 large-QAP, 100 BLS, and 40 generic incumbents”; the actual `check_evidence.py` loads 200 BLS and 200 expanded QAP but only checks flags for them, and the one-command replay covers 100 BLS. The “20 large-QAP” is also a flag check, not a fresh replay (`check_evidence.py:225–233`). The internal review already flagged this as “partial” (`notes/reports/p13-9-review-2026-11-09.md`, G5), but the manuscript states it as if the files carry the fields.

**Why it matters.** The paper’s artifact claim is a per-record evidence schema. The headline QAP expanded table does not meet it; a reader cannot pin the solver commit or hardware for the 200-run table. This is a direct claim-to-evidence mismatch, not a minor omission.

**Action.** Stamp the QAP expanded records with `solver_commit`, `replay_solver_commit`, `hardware`, `iterations_budget`, and `cpu_seconds` (or explicitly state that CPU is missing). Add a JSON-schema test that fails on missing fields. Update `MS p6`/`MS p9` to state exactly which files meet which fields. If per-record CPU is not available, scope the claim to campaign-level provenance and do not claim the file carries it.

#### M5. The BLS-vs-tabu inference ignores clustering and overstates precision

**Evidence.** `MS p13` reports “paired mean difference −0.205 percentage points (bootstrap 95% CI −0.282 to −0.143)” and “a paired sign test on the 131 non-tied pairs would also be significant, but the instances are not independent, so we treat the interval as descriptive.” The reported CI is the naive pair-level bootstrap over 200 runs. Recomputing from `paper2/evidence/qap-bls-10seed.json` and `paper2/evidence/qap-expanded-100k-10seed.json`:
- naive pair-level bootstrap: **−0.282 to −0.143** (matches the paper);
- cluster-by-instance bootstrap: **−0.300 to −0.111**;
- cluster-by-family bootstrap: **−0.234 to −0.163**.
The instance-level sign test is **15/16 non-tied instance means lower** (p ≈ 5×10⁻⁴ two-sided), not 120/131 pairs (p ≈ 2.6×10⁻²⁴). The eight `bur26` variants are not independent replicates; several have 1–3 distinct outcomes across 10 seeds (`bur26c`, `bur26e`, `bur26g`, `bur26h` all 10 seeds identical), so the seed-level bootstrap is especially misleading.

**Why it matters.** The qualitative conclusion (BLS better) survives clustering, but the reported precision and significance are overstated. A JoH reviewer will check this. The paper’s sentence acknowledges the dependence but still reports the independence-based interval; that is contradictory.

**Action.** Report the cluster-robust CI and the instance-level sign test. Drop the pair-level p-value or label it descriptive. Add a mixed-effects/hierarchical model with instance and family random effects. State the effective sample size (20 instances, 3 families), not 200 runs.

#### M6. The tabu baseline is not credible on the `bur26` family; the negative result may be an implementation artifact

**Evidence.** `Table 4`/`Table 5` show tabu **0/10 optima on all eight `bur26` variants (0/80)**, with mean gaps 0.004–0.565% and identical outcomes across seeds for several variants; BLS reaches **10/10 on all eight (80/80)**. `paper2/evidence/qap-expanded-100k-10seed.json` shows only 1–3 distinct gap values per `bur26` instance across 10 seeds. The paper says the tabu uses a Numba general scan for asymmetric instances (`MS p10`) and the BLS uses an exact asymmetric correction (`notes/reports/p13-2-qap-bls.md`). The paper does not diagnose why the tabu is trapped, compare it to a published robust-tabu implementation, or report per-seed diversity.

**Why it matters.** The paper’s “negative result for the tabu reference” is used to argue the harness makes a stronger baseline visible (`MS p13`). If the tabu implementation is weak or defective, the comparison says little about robust tabu or the harness; it says the authors’ tabu is weak. The 0/80 result is a red flag, not a neutral baseline. The paper calls robust tabu “a standard QAP baseline” (`MS p2`), so a reader will expect it to solve some `bur26` instances.

**Action.** (a) Verify the tabu against a published robust-tabu implementation or Taillard’s published results on a few instances. (b) Diagnose the `bur26` trap (tenure, aspiration, restart, delta path). (c) Report per-seed distinct outcomes and a seed-sensitivity analysis. (d) If the tabu is deliberately untuned, say so and stop calling it a “standard baseline.” Consider a stronger tabu or a second baseline before claiming BLS is better.

#### M7. The TSP adaptive-depth protocol is contradicted by the committed evidence

**Evidence.** `MS p15` states “depth 4 for n<100, depth 3 for 100<=n<150, and depth 2 for n>=150; the depth is recorded per run.” `paper2/evidence/tsp-expanded-10k.json` records:
- `max_depth=4` for `ch150` (n=150), `bier127`, `ch130`, `eil101`, `gr120`, and all five `kro*100` instances;
- `max_depth=3` only for `lin105`;
- `max_depth=2` only for `d198` and `pr152`.
The stated rule would give `ch150` depth 2 and the 100<=n<150 instances depth 3. The current `paper2/run_tsp_expanded.py:86` implements the stated rule, but the evidence was generated under a different/mixed rule. `notes/reports/p13-1-tsp-panel.md` says the depth-4 `d198` pass exploded (>300 s per kick) and the runner was changed to adaptive depth; the evidence still shows a mixed panel. The `ch150` result (0.000%) is therefore a depth-4 result, not the stated depth-2 result.

**Why it matters.** The “adaptive depth trade-off is real” claim (`MS p15`) is not supported by a controlled comparison. The 20-instance panel was not run under one rule; the panel mixes depths across instances. The paper’s reproducibility claim is undermined by a protocol that changed during the campaign.

**Action.** Rerun the entire 20-instance panel under one pre-registered depth rule (or report a factorial depth comparison on the instances where both depths are feasible), record the code commit and per-run depth, and update `Table 7`/`MS p15`. Do not present a mixed-depth panel as a single adaptive-depth experiment.

#### M8. The five `brazil58` cap hits are unexplained, and the 3,600 s cap is fragile

**Evidence.** `paper2/evidence/tsp-expanded-10k.json` shows `brazil58` (n=58, EXPLICIT UPPER_ROW) at 379–399 kicks in 3,600 s (~9 s/kick), while `bier127` (n=127) takes 2,109–2,310 s for ~1,010–1,089 kicks (~2 s/kick) and `ch150` (n=150) takes 441–632 s for 1,037–1,480 kicks. `Table 7` reports `brazil58` `Patience 0/5`, `Optima 5/5`; the paper says the runs hit the cap at the known optimum (`MS p15`). The paper attributes this to the 3,600 s cap but does not explain the per-kick cost or why an n=58 explicit-matrix instance is 4× slower per kick than n=127 `bier127`. `bier127` and `gr120` are within 1.7× of the cap, so the “95/100 patience” result is fragile.

**Why it matters.** The `brazil58` cap hit is not a solver failure—it reaches the optimum—but it is a protocol/performance anomaly. A reader cannot tell whether the cap is a safety limit or a hidden performance defect. The paper’s “only non-GEO instances” statement (`MS p15`) is true, but it may give the false impression that the parser issue is GEO-only; `brazil58` is a different path.

**Action.** Report a per-instance wall-time/exchange-test table for the expanded panel; profile `brazil58` (candidate-list construction, distance matrix, `_tour_from_edges`); explain the explicit-matrix path; consider a larger cap or a smaller patience for `brazil58`, or report the panel with and without `brazil58`.

#### M9. The GEO parser fix is disclosed but not audited, and the rerun records lack provenance

**Evidence.** `MS p15–16` says “The broad TSP and LKH panels were rerun after correcting a TSPLIB GEO conversion defect; the old runs contained objectives below the published optimum. No negative gap remains in the committed broad or LKH evidence.” The committed `paper2/evidence/broad-converged.json.gz` has 1,085 records: 1,035 have `solver_commit=7d3c831`, `replay_solver_commit=3aa241e`, `replay_status=not_replayed_broad_screen`; **50 GEO records (10 instances × 5 seeds) have `solver_commit=None`, `replay_solver_commit=None`, `replay_status=None`**, produced by `paper2/rerun_geo_tsp.py`, which does not stamp provenance. `paper2/benchmarks/README.md` still says LKH 71/100, mean 0.092% (the old run), while the manuscript says 75/100, 0.098% (the rerun). `paper2/README.md` says “GEO fix 4583ad3”; the BLS records say `replay_solver_commit=c7d1507`; the provenance says `4583ad3`; the container pins `7d3c831`.

**Why it matters.** A parser defect that produced below-optimum objectives is a correctness failure of the exact-replay claim. The paper reports the fix but not the affected instances, the before/after deltas, or a regression test. The 50 rerun GEO records are the least traceable records in the artifact. The stale 71/100 in the repo conflicts with the 75/100 in the paper.

**Action.** Add a GEO conversion regression test with known optima (e.g., `gr137`, `gr202`, `gr229`, `gr431`, `gr666`), report a before/after table for the affected broad/LKH records, stamp the 50 GEO records with solver/replay commits, update `paper2/benchmarks/README.md` and the LKH report, and state one immutable replay commit/tag. Explain why the 20-instance panel avoids GEO while the broad panel includes it.

#### M10. The generic adapter-only negative result is not a fair test of the adapter contract

**Evidence.** `MS p18` says the generic prototype ran “four QAP and four TSP instances, five seeds, 20,000 iterations, 16 proposals per iteration, and a 5,000-iteration patience rule” and is “not competitive”: QAP 3.848% vs 0.097%, TSP 127.978% vs 0.000%. `notes/reports/p13-3-generic-tabu.md` says the TSP starts from “a seeded random permutation because nearest-neighbour construction needs the distance matrix, which is outside the contract,” and the QAP starts from a seeded random assignment; the adapter-specific references use identity/nearest-neighbour/converged starts. The report also says “The reference comparison is not equal work”—the generic runs ~117k evaluations, while the tabu 20k iterations × full scan and the LK 2k kicks do much more. The manuscript’s “matched-budget control” matches iterations/kicks, not evaluations or CPU, and does not mention the random start.

**Why it matters.** The TSP 127.978% gap is largely a start-quality artifact; the QAP 3.848% gap is largely a sampled-neighbourhood artifact. The conclusion “the adapter contract is sufficient to run a search; it is not sufficient to replace a problem-specific neighbourhood” may be true, but the experiment does not isolate the cause. A JoH reviewer will see an unfair comparison.

**Action.** Report the starts, evaluations, and CPU for all three arms. Run matched-start controls (identity/nearest-neighbour starts for the generic layer) and matched-evaluation or matched-CPU controls. If the generic layer still loses, the negative result is credible; otherwise, soften the claim to “this configuration is not competitive.”

#### M11. The abstract and scope statements conflate the four-instance deep panel with the 20-instance expanded panel and omit the TSP cap hits

**Evidence.** `MS p1` says “A 10,000-kick-cap TSP campaign with 1,000-kick patience plateau-stopped on all 20 runs; the runs stopped after 1,000–1,380 kicks and all 20 reached the known optimum.” This is the 4-instance × 5-seed deep panel (`Table 6`), not the 20-instance × 5-seed expanded panel (`Table 7`), which has 94/100 optima, 95/100 patience, and five `brazil58` cap hits. A reader can easily read “all 20 runs” as the 20-instance panel. The Introduction says “The QAP convergence panel has four instances; the TSP convergence panel has four” (`MS p2`), omitting the 20-instance expanded convergence panels in `Table 1` (`MS p8`). The abstract also omits the 20-instance TSP panel and its cap hits, despite the paper’s stated commitment to reporting failures.

**Why it matters.** The abstract is the most-read part; it currently overstates TSP convergence and hides the main TSP failure. The scope statement is inconsistent with `Table 1`.

**Action.** Rewrite the abstract to distinguish “four-instance deep panel (20 runs)” from “20-instance expanded panel (100 runs; 94/100 optima, 95/100 patience, 5 `brazil58` cap hits).” Add the expanded panels to the Introduction’s scope. Ensure `Table 1` and the text use one taxonomy (deep convergence, expanded convergence, broad screen).

#### M12. The LKH capability comparison is one-sided and lacks the budget/FRESH baseline

**Evidence.** `MS p16` says “External LKH, at its stated budget and configuration, reaches 75 of 100 optima on the same large tail, mean gap 0.098%, median 0%, and worst 1.930%.” The budget/configuration is not stated in the manuscript; `paper2/evidence/lkh-provenance.json` says LKH 3.0.6, commit `9a51de3`, 600 s timeout, 5 seeds, 1 run. The same large tail (20 instances × 5 seeds) is correct (`lkh-large.json` and the broad TSP `n>300` band match), but the paper does not report FRESH’s result on that tail: `paper2/evidence/broad-converged-summary.json` says 1/100 optima, 3/100 patience, 97/100 cap, all-run mean 4.731%. Without that number, the reader cannot see the capability gap.

**Why it matters.** The LKH comparison is a key boundary result; it should be transparent about the budget and the FRESH baseline. As written, it reads as “LKH is better” without the matching FRESH statistic.

**Action.** Add a small table or sentence with LKH budget/config, LKH 75/100, FRESH 1/100 optima, FRESH 97/100 cap, and the mean wall times (LKH 15.0 s; FRESH 600 s cap). State that the comparison is capability-only and not matched-time, and explain why.

#### M13. The framework overhead is measured against the slow private-array baseline, not the production path; the production time is not reported

**Evidence.** `MS p8` says “The production accelerated path is run as a third check, but its wall time is not used for the overhead estimate.” `MS p18` says “The measured CPU overhead is 1.24 (95% bootstrap CI 1.17–1.31); per-instance means range from 1.17 to 1.33. This is a real cost... small enough to be acceptable.” `paper2/evidence/framework-use.json` has `production_objective`, `production_iterations`, `production_stop_reason`, and `quality_matches_production`, but **no `production_wall_seconds` or `production_cpu_seconds`**. The production path is Numba-accelerated; the baseline is the pure-Python private-array path. The framework/production ratio is unknown.

**Why it matters.** The practical claim “small enough to be acceptable” depends on the baseline. If the production path is much faster, the framework overhead relative to the path users would actually run could be much larger than 1.24×. The paper should not compare to the slow baseline without reporting the production ratio.

**Action.** Record and report production wall/CPU time and the framework/production ratio. If the production path is not a fair baseline (different algorithm/acceleration), say so and soften “acceptable” to “a measured cost against the pure-Python baseline.” Also report the ratio of totals (1.215) alongside the mean of ratios (1.239) and a cluster-robust CI.

#### M14. The applied TSA24 case is not a harness adapter and does not support the harness claim

**Evidence.** `MS p20` says “The applied TSA24 case is a separate WS4 codebase, not a FRESH Solutions adapter. It is not part of the QAP/TSP convergence panel and is not used to claim universal portability.” But `MS p17` says it “is included to show that the adapter and evidence boundary survive a compiled spatial model.” If it is a separate codebase, it does not exercise the adapter/evidence boundary. `notes/reports/p13-4-portability-scope.md` calls it “a separate applied TSA24 adapter,” contradicting `MS p20`. The objective scales are not comparable: FRESH 515.682 vs CPU-SA 3.35045×10⁸ (`MS p17`); the paper says “budget illustration, not a matched-performance claim.” The five seeds are not listed; “seed-7” is outside a 1–5 set. The 1,000/10,000/100,000-generation records (8,588,730 / 76,540.7 / 515.682) show the objective is still moving; no convergence curve or longer run is reported.

**Why it matters.** The applied case adds length and a weak evidence claim; it does not demonstrate harness portability. The objective/scale comparison is confusing.

**Action.** Remove the applied case to a separate Paper 1 section, or explain exactly how it uses the FRESH Solutions adapter/evidence protocol, normalize the objectives, state the five seeds, and report a convergence curve. Do not use it as evidence for the harness unless it actually uses the harness.

#### M15. Provenance is inconsistent across the artifact: three solver commits and multiple stale documents

**Evidence.** `paper2/evidence/qap-bls-10seed.json` has `solver_commit=7d3c831`, `replay_solver_commit=c7d1507`; `paper2/evidence/provenance-2026-11-03.json` says `solver_commit=7d3c831`, `replay_solver_commit=4583ad3`; `paper2/README.md` says “GEO fix 4583ad3”; `notes/reports/p13-9-review-2026-11-09.md` says GEO fix `c7d1507`; `container/Dockerfile` pins `7d3c831`. The QAP expanded records have no solver commit; the 50 GEO broad records have no solver commit. The manuscript says “The published tables use the pinned public solver version” (`MS p6`) without naming it. `paper2/benchmarks/README.md` still says LKH 71/100, mean 0.092%; `paper2/README.md` says BLS stronger on 14 instance means (the 5-seed panel), while the manuscript says 15 (the 10-seed panel); `paper2-draft.md` says LKH 71/100 and “NOT SUBMISSION-READY.” The manifest has a hash mismatch for `paper2-draft.md` (`0a577571...` vs current `12f2a840...`), despite `notes/reports/significant-figures-review-2026-11-11.md` saying hashes match.

**Why it matters.** A reproducibility paper must have one immutable solver version/tag for each table. The current artifact has at least three commit hashes and stale docs. The provenance chain is not auditable; a reader cannot tell which commit produced which table.

**Action.** Create one immutable release tag (e.g., `paper2-evidence-v0.1.0`) with a commit hash. Update all records and the container to that tag. Regenerate the manifest and remove/update the stale draft/docs. Add a provenance table mapping each table to its evidence file, solver commit, replay commit, and hardware.

### 4.4 Minor comments

- **m1.** The title “FRESH Solutions: a reproducible adapter harness for applied metaheuristic benchmarks” is product-like and vague. A more descriptive title (e.g., “A reproducible adapter and exact-replay harness for QAP and TSP benchmarking”) would help readers and the editor (`MS p1`).
- **m2.** `Table 5`’s caption says both methods use a “1,000,000-move cap,” but the tabu budget is iterations, not moves (`MS p13`, `Table 1`). The report says one accepted move per iteration makes them comparable; state that equivalence explicitly.
- **m3.** `Table 5` shows BLS worst/optima but not tabu worst/optima; the tabu outlier `chr12a` 5.695% is only in the text. Add both distributions or a supplementary table (`MS p13`).
- **m4.** “Independent Breakout Local Search baseline” (`MS p1`, `MS p13`) is misleading: BLS is a reimplementation by the same authors, not an independent team. Use “separate” or “independently implemented” and state that it is not the original authors’ code.
- **m5.** The SciPy baseline uses “the same five seeds” (`MS p13`), while the BLS/tabu panel is ten seeds. Clarify that SciPy is a 5-seed comparison, not the 10-seed panel.
- **m6.** The instance-selection section says “The QAP panel spans n=12 to n=30” and “The TSP panel spans n=52 to n=150” (`MS p8–9`), but the expanded panels span n=12–50 and n=26–198. Use “deep panel” vs “expanded panel” consistently.
- **m7.** “The internal method is therefore a small/medium TSP solver” (`MS p15`) overstates the medium band: the broad `100<n<=300` band has 58/150 optima (`paper2/evidence/broad-converged-summary.json`). Say “small-instance solver with a weak medium tail.”
- **m8.** The applied-case flow term `2.721` has four significant figures, while `notes/reports/numeric-reporting-policy-2026-11-11.md` rule 3 requires six for flow terms. The realized level “51.21–52.49M” also has four. Either the values are exact to that precision or the policy was not applied (`MS p17`).
- **m9.** The applied case says “five seeds” but highlights “seed-7” (`MS p17`); seed 7 is outside 1–5. State the five seed values.
- **m10.** `MS p9` says the campaign runs on a “Linux container with 72 logical CPUs and 256 GB of RAM”; `paper2/evidence/provenance-2026-11-03.json` records 72 CPUs but no RAM, and `processor: x86_64` is not a processor string. Add the Xeon model and RAM to the provenance.
- **m11.** `container/Dockerfile` pins `7d3c831` (the campaign commit), not the GEO-fix replay commit; `container/README.md` says the full recipe is not claimed. Align the container with the immutable replay tag.
- **m12.** `paper2/evidence/manifest-v0.1.0-candidate.json` has a hash mismatch for `paper2/paper2-draft.md`; the significant-figures review says hashes match. Regenerate the manifest and remove the stale draft (`paper2-draft.md` says “NOT SUBMISSION-READY” and LKH 71/100).
- **m13.** `paper2/benchmarks/README.md` says LKH 71/100, mean 0.092%, and “600-second cap is used only for oversized runs”; the manuscript says 75/100, 0.098%, and the TSP broad cap has 154/390 hits. Update the stale README.
- **m14.** The JoH variant has **two** keyword blocks (`paper2/submission/paper2-sn-jnl.tex:36` `\keywords{...}` and `:40` a manual `\noindent\textbf{Keywords: ...}`), plus a placeholder email `author@example.invalid` and author line “UBC FRESH Lab1* 1*” (`paper2-sn-jnl.pdf` p1). Fix the metadata before submission.
- **m15.** `Fig 3` is captioned “Expanded QAP panel: mean and worst gap by instance size,” but the points are per-instance and several share the same n (eight `bur26` at n=26). Clarify that the x-axis is instance size, not an aggregated mean by size (`Fig 3`).
- **m16.** The paper repeats the patience/replay/negative-result caveats in the Introduction, Framework, Experimental design, QAP, TSP, Discussion, and Conclusion. A 20–30% cut would improve readability; the “laboratory notebook” metaphor (`MS p3–4`) and the “What would falsify the claim” section (`MS p20`) read like internal review material and can be shortened.
- **m17.** The data availability statement (`MS p21`) lists only framework-use and TSP convergence evidence; it omits the QAP expanded, BLS, generic, large-QAP, broad, and LKH evidence used in Tables 4, 5, 7, and the LKH text. List all evidence files or point to the manifest.
- **m18.** The paper says “The validator replays ... 100 BLS” (`MS p6`) but the BLS table uses 200 runs; the actual `check_evidence.py` loads 200 and the one-command replay runs 100. This is the stale claim in M3/M4; fix the text even if the data are sound.
- **m19.** The paper says “the QAP-expanded, BLS, generic, and expanded-TSP files carry solver commit, hardware...” (`MS p6`); the QAP expanded file does not. This is the factual error in M4.
- **m20.** The paper says “The per-run files carry the seed, budget, stop reason, and assignment” (`MS p9`); the QAP expanded file has no budget. Add `iterations_budget` or qualify the statement.

---

## 5. Reviewer questions (Yes / No / N/A)

1. Does the manuscript make a heuristic or methodological advance suitable for JoH? **No.** The paper explicitly frames the contribution as a harness and disclaims a state-of-the-art solver claim (`MS p1`, `MS p21`).
2. Is the contribution clearly positioned against prior benchmarking/reproducibility work? **Partly.** It cites the right work (`MS p2–3`) but does not show a methodological advance beyond it.
3. Is the artifact publicly available and independently replayable? **No.** The evidence repository is private and untagged (`MS p6`, `MS p7`, `MS p20`, `MS p21`), and the one-command replay is miswired for the 10-seed BLS panel (`paper2/replay_all.sh:10`, `paper2/replay_qap_bls.py:29`).
4. Are the statistical comparisons valid and appropriately clustered? **No.** The reported CI and sign test treat 200 runs as independent; a cluster-by-instance bootstrap is wider (`MS p13`; recomputation from the per-run JSON).
5. Are the headline numbers traceable to the evidence? **Partly.** The QAP/TSP tables match the summary JSON, but the schema/validator/abstract overclaims (`MS p6`, `MS p9`, `MS p15–16`).
6. Is the TSP protocol consistent across the panel? **No.** The adaptive-depth rule is contradicted by `max_depth` values in `paper2/evidence/tsp-expanded-10k.json`, and the `brazil58` cap hit is unexplained (`MS p15`; `Table 7`).
7. Would I review a revision? **Yes**, conditional on the P0/P1 fixes and a reframed contribution.

---

## 6. Risk table

| # | Risk | Likelihood | Impact | Evidence | Mitigation |
|---|---|---|---|---|---|
| R1 | Artifact cannot be verified by readers/reviewers; “reproducible” claim fails | High | High | `MS p6`, `MS p7`, `MS p20`, `MS p21`; `paper2/evidence/RELEASE-CANDIDATE.md`; `container/README.md` | Public repo + tag/DOI; instance hashes; working container; self-contained replay |
| R2 | One-command replay does not cover the headline 10-seed BLS panel | High | High | `paper2/replay_all.sh:10`; `paper2/replay_qap_bls.py:29`; `paper2/check_evidence.py:145–161`; audit says 200 BLS | Fix env var/arg; re-evaluate BLS assignments; CI test for 200/200 |
| R3 | QAP expanded records lack solver/hardware/CPU/budget; schema claim false | High | High | `paper2/evidence/qap-expanded-100k-10seed.json` (0/200 fields); `MS p6`, `MS p9` | Stamp records; JSON-schema test; scope claim if CPU unavailable |
| R4 | BLS-vs-tabu inference overstates precision; sign test ignores clustering | High | High | `MS p13`; naive CI −0.282/−0.143 vs cluster −0.300/−0.111; 120/131 pairs vs 15/16 instances | Cluster-robust CI; instance-level test; mixed model |
| R5 | Tabu baseline not credible on `bur26`; negative result may be an implementation artifact | High | High | `Table 4`/`Table 5` 0/80 tabu vs 80/80 BLS; 1–3 distinct outcomes per `bur26` across 10 seeds | Verify against published robust tabu; diagnose/tune; report seed diversity |
| R6 | TSP adaptive-depth rule contradicted by evidence; panel run under mixed depths | High | High | `MS p15`; `paper2/evidence/tsp-expanded-10k.json` `max_depth=4` for ch150/bier127/ch130/eil101/gr120/kro*100; `run_tsp_expanded.py:86` | Rerun under one pre-registered rule; report per-instance depth/commit |
| R7 | `brazil58` cap hit unexplained; 3,600 s cap fragile | High | Medium | `Table 7`; `tsp-expanded-10k.json` 3,600 s at 379–399 kicks vs bier127 2,109–2,310 s at ~1,010–1,089 | Profile `brazil58`; report wall/exchange tests; explain explicit-matrix path |
| R8 | GEO parser fix not audited; 50 rerun records lack provenance; stale 71/100 vs 75/100 | Medium | High | `broad-converged.json.gz` 50 GEO `None`; `rerun_geo_tsp.py`; `paper2/benchmarks/README.md`; `lkh-provenance.json` | Regression test; before/after table; stamp GEO records; update docs |
| R9 | Generic tabu comparison unfair (random starts, unmatched work) | High | Medium | `MS p18`; `p13-3-generic-tabu.md`; `generic-tabu.json` `start: random`; ~117k evaluations vs full scans | Matched-start and matched-evaluation/CPU controls; state starts/work |
| R10 | Abstract/scope overclaims TSP all-20 and omits 20-instance panel/cap hits; LKH one-sided | High | Medium | `MS p1`, `MS p2`, `MS p15–16`, `Table 6`, `Table 7`; `broad-converged-summary.json` FRESH 1/100 vs LKH 75/100 | Rewrite abstract/scope; add LKH budget and FRESH baseline |
| R11 | JoH fit: no heuristic/methodological advance | High | High | `MS p1`, `MS p2`, `MS p21`; four contributions are engineering artifacts; conclusion admits preliminary evidence | Reframe to SoftwareX/JORS or add a methodological study |
| R12 | Provenance inconsistent (7d3c831 / c7d1507 / 4583ad3); stale docs; manifest mismatch | Medium | High | `qap-bls-10seed.json`; `provenance-2026-11-03.json`; `container/Dockerfile`; `paper2/README.md`; manifest hash mismatch | Single immutable tag; update records/container; regenerate manifest |
| R13 | Framework overhead measured only against slow private-array path; production time missing | Medium | Medium | `MS p8`, `MS p18`; `framework-use.json` no production time | Report production time/ratio; soften “acceptable” |
| R14 | Applied case is not a harness adapter; objective scales incomparable | Medium | Medium | `MS p17`, `MS p20`; `p13-4-portability-scope.md`; 515.682 vs 3.35045×10⁸ | Remove/move to Paper 1; explain adapter use; normalize objectives |
| R15 | Manifest/stale draft/JoH metadata defects | Low | Medium | `manifest-v0.1.0-candidate.json` hash mismatch; `paper2-draft.md` “NOT SUBMISSION-READY”; `paper2-sn-jnl.pdf` p1 duplicate keywords/placeholder | Regenerate manifest; remove draft; fix metadata |

**Top five risks (executive):**

1. **Artifact not public/tagged** (R1): the paper’s central claim is not verifiable. Mitigation: public repo + tag/DOI + working container + self-contained replay.
2. **Replay miswired for the 10-seed BLS panel** (R2): the one-command check covers 100/100, not 200/200. Mitigation: fix `replay_qap_bls.py`/`replay_all.sh`, re-evaluate BLS assignments, add a CI assertion.
3. **BLS-vs-tabu inference and tabu credibility** (R4/R5): the comparison is not cluster-aware, and the tabu is 0/80 on `bur26`. Mitigation: cluster-robust analysis; verify/diagnose the tabu; report seed diversity.
4. **TSP protocol inconsistency and `brazil58` anomaly** (R6/R7): the adaptive-depth rule is contradicted by the evidence, and the cap hit is unexplained. Mitigation: rerun under one rule; profile `brazil58`; report per-instance wall times.
5. **JoH fit** (R11): no heuristic/methodological advance. Mitigation: reframe to SoftwareX/JORS or add a genuine methodological study.

---

## 7. P0 / P1 / P2 list

### P0 — must fix before any submission

- **P0-1. Public artifact.** Publish the evidence repository with a tag/DOI, instance provenance/hashes, a working container, and a self-contained `replay_all.sh` (`MS p6`, `MS p7`, `MS p20`, `MS p21`; `RELEASE-CANDIDATE.md`; `container/README.md`).
- **P0-2. One-command replay for the 10-seed BLS panel.** Fix `paper2/replay_all.sh:10` / `paper2/replay_qap_bls.py:29`; make `check_evidence.py` re-evaluate the 200 BLS assignments, not just flags; update the claim audit and `MS p6`.
- **P0-3. QAP expanded per-record schema.** Add `solver_commit`, `replay_solver_commit`, `hardware`, `iterations_budget`, and `cpu_seconds` to `qap-expanded-100k-10seed.json`; add a schema test; correct `MS p6`/`MS p9`.
- **P0-4. JoH fit.** Either reframe to SoftwareX/JORS or add a methodological contribution; the current paper explicitly disclaims a heuristic advance (`MS p1`, `MS p2`, `MS p21`).

### P1 — major, affects validity/credibility

- **P1-1.** Cluster-robust BLS-vs-tabu inference and instance-level sign test (`MS p13`).
- **P1-2.** Diagnose/verify the tabu on `bur26`; report per-seed diversity (`Table 4`, `Table 5`).
- **P1-3.** Rerun the TSP expanded panel under one adaptive-depth rule; correct `MS p15`/`Table 7` (`tsp-expanded-10k.json` `max_depth`).
- **P1-4.** Profile `brazil58`; report per-instance wall/exchange tests; explain the 3,600 s cap (`Table 7`).
- **P1-5.** Add a GEO regression test, before/after table, and provenance for the 50 rerun GEO records; update stale LKH 71/100 docs (`broad-converged.json.gz`, `rerun_geo_tsp.py`, `paper2/benchmarks/README.md`).
- **P1-6.** Fair generic-tabu comparison: state random starts, report evaluations/CPU, add matched-start and matched-work controls (`MS p18`, `p13-3-generic-tabu.md`).
- **P1-7.** Rewrite the abstract/scope to distinguish deep vs expanded TSP panels and include the `brazil58` cap hits (`MS p1`, `MS p2`, `MS p15–16`).
- **P1-8.** Add LKH budget/config and the FRESH 1/100 large-tail baseline (`MS p16`, `lkh-provenance.json`, `broad-converged-summary.json`).
- **P1-9.** Report production wall/CPU and the framework/production ratio; soften “acceptable” (`MS p8`, `MS p18`, `framework-use.json`).
- **P1-10.** Resolve the three solver commits (`7d3c831` / `c7d1507` / `4583ad3`) with one immutable tag; update the container and records (`provenance-2026-11-03.json`, `container/Dockerfile`).
- **P1-11.** Clarify the applied case: adapter or separate codebase; state seeds; normalize objectives; remove/move if not a harness case (`MS p17`, `MS p20`, `p13-4-portability-scope.md`).

### P2 — minor/clarity

- **P2-1.** Title/abstract wording; product-like title (`MS p1`).
- **P2-2.** `Table 5` units/asymmetry: tabu iterations vs BLS moves; show tabu worst/optima (`MS p13`).
- **P2-3.** “Independent BLS” wording (`MS p1`, `MS p13`).
- **P2-4.** SciPy 5-seed vs 10-seed panel (`MS p13`).
- **P2-5.** n-range wording for deep vs expanded panels (`MS p8–9`).
- **P2-6.** “Small/medium TSP solver” overstates the medium band (`MS p15`).
- **P2-7.** Broad QAP converged mean 1.823% vs all-run 1.723% selection effect (`MS p11`).
- **P2-8.** Applied-case flow term/level significant figures (`MS p17`; numeric policy).
- **P2-9.** Applied-case seed list (`MS p17`).
- **P2-10.** Hardware/RAM/processor string in provenance (`MS p9`; `provenance-2026-11-03.json`).
- **P2-11.** Container pins campaign commit, not replay commit (`container/Dockerfile`).
- **P2-12.** Manifest hash mismatch and stale draft (`manifest-v0.1.0-candidate.json`, `paper2-draft.md`).
- **P2-13.** Stale `paper2/benchmarks/README.md` LKH 71/100 and cap wording.
- **P2-14.** JoH variant duplicate keywords/placeholder email/author.
- **P2-15.** `Fig 3` caption “by instance size.”
- **P2-16.** Repetition, “laboratory notebook” metaphor, “what would falsify” section.
- **P2-17.** Data availability list omits QAP expanded/BLS/generic/large-QAP/broad/LKH evidence.
- **P2-18.** Stale “100 BLS” and “QAP-expanded carries solver commit” sentences (`MS p6`).

---

## 8. Evidence ledger

| Evidence tag | Evidence (paraphrase) | Used for |
|---|---|---|
| `MS p1` | Abstract: harness, 40-run framework check, 20-instance QAP panel (0.301% vs BLS 0.096%), 1.24× CPU, “all 20” TSP deep runs; contribution is harness, not SOTA. | M1, M11, m1 |
| `MS p2` | Introduction: narrow engineering question; four contributions; “QAP convergence panel has four; TSP convergence panel has four.” | M1, M11 |
| `MS p3–4` | Adapter contract: state, moves, feasibility, apply/undo inverses. | Strength 1 |
| `MS p6` | Evidence protocol; per-record schema claim; “validator replays 40 framework, 20 deep-TSP, 20 large-QAP, 100 BLS, 40 generic”; release candidate. | M2, M3, M4, Strength 2 |
| `MS p7` | Artifact fail-closed; broad counts; “paper-specific evidence repository is not yet public.” | M2, Strength 3 |
| `MS p8` | Table 1 campaigns; production path wall time not used. | M13, P2-5 |
| `MS p9` | 72 CPUs/256 GB; per-run files carry seed/budget/stop/assignment; processor string claim. | M4, m10 |
| `MS p10` | QAP tabu, delta matrix for symmetric zero-diagonal, general scan for asymmetric. | M6 |
| `MS p11` | Table 2 framework panel; 1.24 (1.17–1.31); per-instance 1.17–1.33. | Strength 4, M13 |
| `MS p12` | Table 3 large QAP; Table 4 expanded QAP 20 instances/10 seeds/200 runs/73 optima/0.301%. | Strength 4, M6 |
| `MS p13` | Table 5 BLS vs tabu; 161/200; 120/11/69; −0.205 CI −0.282/−0.143; sign test; family balance. | M5, M6, Strength 6 |
| `MS p15` | TSP 10k campaign; adaptive depth 4/3/2; 95/100 patience; 5 `brazil58` cap hits; 94/100 optima; 0.004%. | M7, M8, M11 |
| `MS p16` | Table 7; GEO fix; LKH 75/100, 0.098%, 1.930%. | M8, M9, M12 |
| `MS p17` | Applied case: 208,255 blocks; 512.574–518.621; seed-7 515.141+2.721; 8,588,730/76,540.7; CPU-SA 3.35045e8. | M14, m8, m9 |
| `MS p18` | Generic tabu 3.848% vs 0.097%; TSP 127.978% vs 0.000%; matched-budget control 0.439%/0.004%; framework 1.24. | M10, M13 |
| `MS p19` | Stopping-rule comparison; 10k vs 100k gaps; limitations. | M1 |
| `MS p20` | Evidence release pending; applied TSA24 separate WS4 codebase. | M2, M14 |
| `MS p21` | Data availability; evidence tag pending; one-command replay needed. | M2, M11, m17 |
| `Table 4` | Expanded QAP 20 instances, 10 seeds, all patience, 73 optima. | M4, M6 |
| `Table 5` | BLS vs tabu, 161/200 vs 73/200; tabu `bur26` 0/10 all. | M5, M6 |
| `Table 6` | TSP deep panel, 20/20 optima, mean wall 754/605/688/604 s. | M11, Strength 4 |
| `Table 7` | TSP expanded, 94/100 optima, 95/100 patience, `brazil58` 0/5 patience. | M7, M8, M11 |
| `paper2/replay_all.sh:10` | Sets `QAP_BLS_EVIDENCE=qap-bls-10seed.json`. | M3 |
| `paper2/replay_qap_bls.py:29` | `--input` default `qap-bls-expanded.json`; ignores env var. | M3 |
| `paper2/check_evidence.py:145–161` | Loads BLS 200 but only checks `exact_replay`/`stop_reason` flags. | M3, M4 |
| `paper2/evidence/qap-expanded-100k-10seed.json` | 200 records; 0/200 `solver_commit`, `hardware`, `cpu_seconds`; no `budget`. | M4, P0-3 |
| `paper2/evidence/tsp-expanded-10k.json` | `max_depth=4` for ch150/bier127/ch130/eil101/gr120/kro*100; depth 3 only lin105; depth 2 d198/pr152; `brazil58` 3,600 s/379–399 kicks. | M7, M8 |
| `paper2/evidence/broad-converged.json.gz` | 1,085 records; 1,035 with commits; 50 GEO records `None`; no negative gaps. | M9 |
| `paper2/evidence/framework-use.json` | 40 QAP records; `production_objective`/`production_iterations` but no production time; CPU ratio 1.239. | M13, Strength 4 |
| `paper2/evidence/manifest-v0.1.0-candidate.json` | 64 files; `paper2-draft.md` hash mismatch. | M15, m12 |
| `paper2/evidence/provenance-2026-11-03.json` | `solver_commit=7d3c831`; `replay_solver_commit=4583ad3`; per-record metadata “release blocker.” | M2, M15 |
| `paper2/evidence/lkh-provenance.json` | LKH 3.0.6, commit `9a51de3`, 600 s, 5 seeds, 1 run. | M12 |
| `paper2/evidence/broad-converged-summary.json` | FRESH n>300: 1/100 optima, 3/100 patience, 97/100 cap, all mean 4.731%. | M12 |
| `notes/reports/p13-2-qap-bls.md` | 5-seed/100-run BLS report: 0.116%, 76/100; tabu 0.274%, 37/100; not equal work; 10-seed rerun supersedes. | M6, M15 |
| `notes/reports/p13-3-generic-tabu.md` | Generic TSP random start; not equal work; 3.848 vs 0.097, 127.978 vs 0.000. | M10 |
| `notes/reports/p13-1-tsp-panel.md` | Depth-4 d198 exploded; adaptive depth; `gr137` removed; 5 `brazil58` cap hits. | M7, M8, M9 |
| `notes/reports/p13-9-review-2026-11-09.md` | Paper 2 “not submission-ready”; SoftwareX/JORS safer; P0 public artifact/schema. | M1, M2, M4 |
| `notes/reports/significant-figures-review-2026-11-11.md` | 24 pp., 9,357 words, 5 figures; claims manifest hashes match. | M15, m12 |
| `notes/reports/naming-convention.md` | FRESH uppercase; no title-case lab; lower-case adjective replaced. | Strength 7 |
| `notes/reports/claim-to-evidence-audit-2026-11-09.md` | Says `replay_all.sh` covers 200 BLS; actual output 100. | M3 |

---

## 9. QA checklist (before submission)

- **Evidence-only:** every substantive claim above has a page/table/figure/evidence-path tag. Yes.
- **Arithmetic:** headline QAP/TSP/BLS/framework values recomputed from the JSON summaries; the table values match. The only mismatches are the schema/validator/adaptive-depth claims, which are documented above.
- **Anonymity/privacy:** no reviewer-identifying details; no third-party personal information beyond the submission materials. The JoH variant’s placeholder email is noted as a submission defect, not repeated as personal data.
- **Tone:** critical but professional; no sarcasm; critiques anchored to the submission.
- **Bias hygiene:** no prestige/subfield bias; the assessment is based on JoH scope, evidence traceability, and statistical validity.
- **External literature:** none used; no invented citations.
- **FRESH naming:** the manuscript uses “FRESH” and “FRESH Solutions” consistently; code identifiers are not prose uses. No naming issue.
- **Recommendation consistency:** reject for JoH; prepared to review a revision/resubmission conditional on P0/P1 fixes.

---

## 10. Bottom line

This is a well-intentioned and often careful software/reproducibility report. The harness idea is good, the replay gate is the right instinct, and the paper is more honest than most about negative results. But at JoH the paper is in the wrong venue and the current evidence package is not yet a reproducible artifact: the evidence is private/pending, the headline BLS panel is not covered by the one-command replay, the QAP expanded schema is incomplete, the TSP adaptive-depth protocol is contradicted by the evidence, and the BLS-vs-tabu inference overstates precision. I recommend **reject** for JoH, with encouragement to resubmit to **SoftwareX** or **JORS** after making the artifact public and fixing the replay/schema/statistics. If the authors prefer to stay at JoH, they need a genuine methodological study, not a larger harness report.
