# Reviewer Report — Paper 2 (JORS, Issues in Research Software), rc7

**Manuscript:** FRESH Solutions: an adapter and exact-replay harness for metaheuristic benchmarking
**Author:** Gregory Paradis, UBC FRESH Lab, University of British Columbia
**Materials reviewed:** `paper2/submission/jors/paper2-jors.tex`; `paper2-jors.pdf` (8 pp.); `paper2-jors-supplement.pdf` (3 pp.); `paper2/submission/jors/README.md`; `cover-letter.md`; `highlights.md`; `paper2/evidence/manifest-v0.1.0-candidate.json`; `paper2/evidence/RELEASE-CANDIDATE.md`; `container/Dockerfile`; `container/README.md`; public release `p14-evidence-rc7`; FRESH Solutions release `v0.9.3-p13rc1`; and the prior review `notes/reviews/paper2-jors-rc4-2026-11-11.md`.
**Reviewer stance:** Independent antagonistic JORS reviewer. I checked the remaining submission blockers and regressions only: public source/asset/tag consistency, one-command replay, availability/DOI/container/CPU claims, the tabu `bur26` scope and supplement diversity table, BLS framing and cluster statistics, JORS length/focus, mixed-depth TSP disclosure, and redistribution/author metadata. I recomputed the headline statistics, re-ran the headline replay panels, and checked the public release tree and assets. I did not rerun the campaigns.
**Recommendation:** **Major revision** — the scientific core is sound and every headline panel replays, but the public package and several manuscript claims are not yet submission-ready. The fixes are bounded and require no new experiments.
**Prepared to review after revision:** **Yes.**
**Refereeing openly:** No.
**Include in annual reviewer list:** No.

---

## Overrides (project-specific constraints)

- Target venue: **JORS, Issues in Research Software** — experience/reproducibility report, 3,000–4,000 words, roughly 4–6 pages, Vancouver-style numbered references, no mandatory LaTeX template (`notes/plans/p14-journal-shift-2026-11-11.md:140–142, 232`).
- Evidence tags: `MS pX` for the PDF page, `Table N` / `Fig N` for objects, `TEX:line` for the source, and `file:line` or `path` for repository evidence.
- The public release URLs were supplied with the review request; I treated them as part of the submission. No external literature is introduced.
- All materials are confidential. No reviewer-identifying details are included.
- The project’s own stop-ship list applies: public source/asset mismatch, replay failure on a headline table, and missing author/CRediT/funding/competing metadata are submission blockers (`notes/plans/p15-final-submission-2026-11-12.md:17–22`).

---

## 1. Document inventory

| Item | Status | Notes |
|---|---|---|
| `paper2-jors.pdf` | Present | 8 pages; body through p7, references p7–8; 2 tables, 1 figure; US Letter; blank PDF Title/Author/Subject/Keywords metadata. |
| `paper2-jors.tex` | Present | 438 lines; 3,788 words by `detex -n paper2-jors.tex \| wc -w`; no overfull/underfull warnings in the build log. |
| `paper2-jors-supplement.pdf` | Present | **3 pages**, not 2; framework, per-instance QAP, `bur26` diversity, and per-instance TSP tables. |
| `paper2/submission/jors/README.md` | Present, stale | Says supplement is 2 pages; still lists repository/DOI placeholders and “author metadata not supplied” (`README.md:33–41`); its blocking-issues list is partly obsolete (`README.md:43–72`). |
| `cover-letter.md` | Present, stale | Says the release is “being prepared” and the repository/DOI are placeholders (`cover-letter.md:16–19`), while rc7 is public and the manuscript has the URL. |
| `manifest-v0.1.0-candidate.json` | Present, partly stale | All 65 `files` hashes verify. `status` still says “no tag/release created”; `references` and `replay` hashes are stale. |
| `p14-evidence-rc7` | Present | Public prerelease at `ba257da5d3ce6ea40a4711db35cdd9fc65566325`. Assets `paper2-jors.pdf` (`4b2e03c5…`) and supplement (`c8ef8c8e…`) match the submitted files byte-for-byte. Tagged `.tex` (`e56c37d4…`) and supplement source (`adf4510d…`) also match. |
| `v0.9.3-p13rc1` | Present | Public prerelease at `4583ad3b74bdf94d6b46c98bb3e1caf1b9b0dad2`; Apache-2.0. |
| `container/Dockerfile` | Present, now pinned | Pins `python:3.12-slim@sha256:05a994d2…` (`Dockerfile:1`) and checks out `4583ad3` (`Dockerfile:6–7`). The manuscript still says it is not pinned. |
| `container/README.md` | Present, stale | Still says the base-image digest and solver checkout are missing (`container/README.md:19–20`). |
| Author metadata | **Incomplete** | Name/affiliation/email; CRediT and competing interests are now present (`MS p7`); no ORCID; no funding statement. |
| Release package metadata | **Contradictory** | Tagged `README.md:3` says “P14 release candidate 4 (`p14-evidence-rc7`)”; `LICENSING.md:12` says `p14-evidence-rc4`; manifest says no release; `paper2/README.md:4` says “not a submission-ready article”; cover letter says release is still being prepared. |

---

## 2. Verification performed

### 2.1 Public source and assets

- `sha256sum` of the submitted `paper2-jors.pdf` and supplement equals the `p14-evidence-rc7` release assets exactly (`4b2e03c5…`, `c8ef8c8e…`).
- `git show HEAD:paper2/submission/jors/paper2-jors.tex` hashes to the submitted `.tex` (`e56c37d4…`); the supplement source also matches.
- The rc7 tag resolves to `ba257da`, the current `HEAD` of the papers repository. The manuscript/PDF/asset identity is therefore **closed**.
- `v0.9.3-p13rc1` resolves to `4583ad3`; the `fresh-solutions` submodule in the papers repository also points to `4583ad3`.

### 2.2 Replay

With the submodule at `4583ad3` and the required roots:

- `python3 paper2/check_evidence.py` → “replayed 40 QAP and 20 TSP incumbents; broad records 1085 with 7 summary rows; large-QAP records 20 exact; BLS records 200 exact; generic-tabu records 40 exact; LKH records 100 non-negative.”
- `python3 paper2/replay_qap_expanded.py` → 200/200 exact.
- `python3 paper2/replay_tsp_expanded.py` → 100/100 exact.
- `python3 paper2/replay_qap_bls.py --input qap-bls-10seed.json` → 200/200 exact.
- `python3 paper2/replay_generic_tabu.py` → 40/40 exact.
- `python3 paper2/replay_broad.py` → 1,060/1,060 exact; 25 `esc8` parse-error records skipped.

So the headline panels replay **when the correct solver submodule is present**. The failure is in the setup and version guard, not in the replay arithmetic (see M3).

### 2.3 Clean-clone test

I cloned the papers repository without initialising submodules and ran the paper’s documented command with the mounted benchmark roots:

```text
$ bash paper2/replay_all.sh
... validated provenance; replayed 40 QAP and 20 TSP incumbents; ...
broad mismatch: tsp ali535 seed 1
```

The clone had no `fresh-solutions` submodule. The scripts insert `ROOT.parent/"fresh-solutions"` into `sys.path` (`paper2/check_evidence.py:12–14`) but then silently fall back to the environment’s installed `fresh-solutions` 0.9.0. That older package lacks the GEO fix; the broad TSP record for `ali535` no longer matches. With no installed package, the same run would fail with `ModuleNotFoundError`. The scripts never assert the solver commit recorded in the evidence (`replay_solver_commit`).

### 2.4 Statistics and table transcriptions

- QAP tabu: 200 runs; mean 0.30085%, median 0.04268%, worst 5.69514%, 73/200 optima; all `patience`; 200/200 exact replay.
- BLS: 200 runs; mean 0.09614%, median 0%, worst 1.36861%, 161/200 optima; all `patience`; 200/200 exact replay.
- Paired BLS−tabu: point estimate −0.20471 pp; cluster-by-instance 95% interval −0.2991 to −0.1108; family-cluster interval −0.2337 to −0.163; 15/16 non-tied instance means; sign test p = 5.19 × 10⁻⁴. The paper’s arithmetic is correct.
- Framework: 40/40 exact, matched standalone and production objectives, all patience; mean CPU ratio 1.2390, 95% interval 1.1683–1.3098. The 1.239 is the mean of the 40 run-level ratios; the pooled ratio is 1.2151 and the mean of the four per-instance mean ratios is 1.2296. The paper does not state which aggregation it uses.
- TSP: 100 runs; mean 0.003945%, worst 0.18458%, 94/100 optima, 95/100 patience, 5 `brazil58` cap hits; depth counts 85/5/10 at depths 4/3/2. All 100 exact.
- Broad QAP: 134 instances, 670 runs, 552 patience, 318 optima, converged mean 1.823%, median 0%, worst 36.445%. Broad TSP: 78 instances, 390 runs, 236 patience, 195 optima, all-run mean 1.460%; `n>300`: 3/100 patience, 1 optima, 97 cap.
- LKH: 75/100 optima, mean 0.09835%, median 0%, worst 1.930%, mean wall 15.01 s.
- Generic: QAP 3.848% vs 0.097%; TSP 127.978% vs 0.000%; mean evaluations 117,117 (QAP) and 116,619 (TSP) per run.
- Supplement QAP and TSP per-instance tables transcribe the evidence correctly at the printed precision. The only visible issue is `bur26b`: two raw distinct gaps (0.564532, 0.565239) both print as 0.565, so the table looks self-contradictory (M7).

### 2.5 Manifest and container

- 65/65 `files` entries verify. The top-level `references` hash is stale (`fb8a770…` in the manifest vs `8b6230a…` actual) and the `replay` hash is stale (`cdc8b45…` vs `3fb6694…` actual). `status` says “candidate; no tag/release created” despite rc7.
- `container/Dockerfile` pins both the base digest and the solver checkout; `container/README.md` and `MS p6` say the opposite.

---

## 3. Quick synopsis

The manuscript describes a Python harness with a small problem-adapter contract, resident assignment state, an exact replay gate, a stopping/budget taxonomy, and QAP/TSP reference adapters. It reports a 40-run framework-use check, a 200-run QAP/BLS panel, a 100-run mixed-depth TSP breadth panel, broad QAP/TSP screens, an external LKH capability check, and a generic adapter-only negative result.

The scientific core is now in good shape. The QAP/BLS result is clustered, the TSP mixed depth is disclosed in the abstract, §3.3, and the conclusion, the tabu is no longer called “robust” in the headline objects, the redistribution statement is corrected, the supplement has a `bur26` diversity table, and the DOI placeholder and “release blocker” paragraph are gone. The remaining problems are not new experiments: they are a public package that still advertises rc4 and “no release,” two false availability claims, a replay path that is not self-verifying, missing funding/ORCID metadata, and a statistical summary that still overstates precision.

---

## 4. Status of the earlier rc4 P1 items

| rc4 item | Status | Evidence |
|---|---|---|
| **P1-1. Release package metadata** | **Open / regressed** | `README.md:3` says “release candidate 4 (`p14-evidence-rc7`)”; `LICENSING.md:12` says `p14-evidence-rc4`; `manifest…:200` says “no tag/release created”; `paper2/README.md:4` says “not a submission-ready article”; cover letter says release still being prepared. |
| **P1-2. DOI placeholder / “release blocker”** | **Closed** | The literal `[DOI to be assigned]` and the “release blocker” paragraph are gone; the DOI is described as pending, which is honest. Residual: the DOI status is repeated in the abstract, §4, and Data availability (`MS p1, p6, p7`). |
| **P1-3. Tabu label / diagnostic** | **Mostly closed** | “Robust” is removed from the abstract, Table 1, §2.4, Limitations, and the supplement; the text calls the tabu “unvalidated” and BLS the primary quality reference. A per-seed diversity table is now in the supplement. Residual: the main text does not refer to the table, and there is no sentence on whether 0/80 is a tuning issue or an implementation defect. |
| **P1-4. Redistribution / licence** | **Closed** | `MS p6` now says the four QAP and four TSP instance files are included under their original terms and QAPLIB/TSPLIB are not relicensed; `LICENSING.md` says the repository is public. Residual: `.zenodo.json` and `CITATION.cff` still declare MIT for the whole deposit. |
| **P1-5. Author metadata** | **Partly closed** | CRediT and competing interests are present (`MS p7`); the supplement byline now matches. Still missing: funding statement and ORCID (`paper2/submission/jors/README.md:37–39`). |

Earlier P2 items that remain open: container claim (regressed), wrong repository in Data availability, family-cluster/sign-test overstatement, BLS-primary table order, page-length/focus, and the `4583ad3`/`c7d1507` replay stamp split.

---

## 5. Confidential comments to the editor

I recommend **major revision**, not rejection. The manuscript now does what a JORS Issues in Research Software paper should do: it describes a real software boundary, reports both positive and negative results, and provides a public, replayable evidence set. Every headline panel replays when the correct solver submodule is present; the QAP/BLS/TSP/framework numbers are correct; and the tabu weakness is scoped rather than hidden.

The remaining blockers are concentrated in the package, not the science. The rc7 tag’s own `README.md` says “release candidate 4,” its `LICENSING.md` says `p14-evidence-rc4`, its manifest says no release was created, and its cover letter says the release is still being prepared. A reader who follows the paper’s citation lands on an artifact that contradicts the paper. Separately, §4/§5 name the wrong repository for the harness and say the container is not pinned when the Dockerfile now pins both the base digest and the solver checkout. The paper also lacks a funding statement and ORCID, and the replay path is not self-verifying: from a clean clone it either fails or silently uses an installed solver version and then fails the broad TSP panel.

None of this requires a new campaign. A re-cut release, two corrected availability sentences, a funding/ORCID line, a complete replay prerequisites block with a solver-commit assertion, and a more careful statistical caveat would make the paper acceptable. I would be willing to review a revision.

---

## 6. Comments to the authors

### 6.1 Summary

The paper addresses a genuine engineering problem: applying known metaheuristics to new problems is slowed by the machinery around the search — state, moves, feasibility, stopping, replay, and benchmark bookkeeping. The adapter contract, resident-state path, and replay gate are sensible design ideas. The paper is unusually candid about failures: the tabu’s `bur26` weakness, the `brazil58` cap hits, the generic layer’s non-competitiveness, and the missing per-record CPU. The QAP/TSP reference implementations are serious efforts, and the BLS baseline is a substantial addition.

The paper’s centre of gravity is close to JORS. The abstract leads with the harness, the QAP/BLS comparison is clustered, the TSP mixed depth is disclosed in the abstract, §3.3, and the conclusion, and the supplement carries the per-instance detail. The remaining issues are claim consistency, artifact presentation, and submission readiness, not the quality of the empirical work.

### 6.2 What works (evidence-based strengths)

1. **The adapter boundary is clearly specified.** The contract separates discrete state, exact evaluation, feasibility, mutation/crossover, and reversible moves; the search layer sees only that interface (`MS p2`; `TEX:127–140`). The `apply`/`undo` exact-inverse requirement and the adapter-owned permutation invariant are well stated.
2. **The replay gate is the right idea.** A stored incumbent is re-evaluated through a new adapter state, not the optimizer’s cached counter (`MS p3`; `TEX:151–158`). The gate checks objective, feasibility, and permutation validity, and it fails closed.
3. **The stopping taxonomy is useful.** Plateau stop, safety-cap hit, budget exhaustion, and invalid replay are distinguished, and the denominator is visible (`MS p3`; `TEX:166–174`). This is better than most heuristic papers.
4. **The headline numbers reproduce.** I checked the QAP panel (0.301% mean, 0.043% median, 5.695% worst, 73/200 optima), the BLS panel (0.096% mean, 1.369% worst, 161/200 optima), the TSP panel (0.004% mean, 0.185% worst, 94/100 optima, 95/100 patience), the framework panel (1.239 CPU ratio, 1.168–1.310 interval), the broad panels, LKH, and the generic negative result. The arithmetic is consistent.
5. **The BLS inference is clustered.** The cluster-by-instance interval is the right primary summary. Recomputing from the per-run JSON gives −0.2991 to −0.1108 (the paper rounds to −0.300 to −0.111), a point estimate of −0.2047, and 15/16 non-tied instance means (p = 5.19 × 10⁻⁴). The arithmetic is correct; the interpretation needs one more caveat (M5).
6. **The one-command replay covers the BLS panel.** `paper2/replay_all.sh:9,12` uses `QAP_EXPANDED_EVIDENCE=qap-expanded-100k-10seed.json` and `--input qap-bls-10seed.json`. With the correct submodule, all panels replay.
7. **The TSP mixed depth is disclosed in the abstract, §3.3, and the conclusion.** `MS p1` says “frozen, mixed-depth”; `MS p5` gives 17 depth 4, `lin105` depth 3, and `d198`/`pr152` depth 2, and says it is not one adaptive-depth experiment; the conclusion repeats “mixed-depth” (`MS p7`). This closes the earlier inconsistency.
8. **The supplement is appropriate.** Full per-instance QAP/TSP tables, the framework panel, and a `bur26` diversity table are in the supplement, which is the right place for a 3,000–4,000-word paper.
9. **The paper is candid about scope.** It says the generic layer is not competitive, the tabu is an unvalidated reference, the LKH comparison is capability-only, and portability is demonstrated by two adapters written by the reference author (`MS p6–7`). This candour is a strength.

### 6.3 Major comments

#### M1. The public rc7 package still advertises rc4 and “no release” (P0)

**Evidence.** The manuscript says the artifact is public as `p14-evidence-rc7` (`MS p1`; `TEX:46`) and points readers to the rc7 release (`MS p6`; `TEX:345–347`). The release assets and the tagged manuscript match. But the tagged source — the artifact a reader downloads — still contains:

- `README.md:3`: “Public release status: **P14 release candidate 4** (`p14-evidence-rc7`); DOI pending.”
- `LICENSING.md:11–12`: “the GitHub release candidate is `p14-evidence-rc4`. A DOI is still pending.”
- `paper2/evidence/manifest-v0.1.0-candidate.json:200`: `"status": "candidate; no tag/release created; P12 framework-use and TSP convergence added"`.
- `manifest…:211`: `references.sha256` = `fb8a770…`; actual `paper2/references.bib` = `8b6230a…`.
- `manifest…:221`: `replay.sha256` = `cdc8b45…`; actual `paper2/replay_all.sh` = `3fb6694…`.
- `paper2/submission/jors/cover-letter.md:16–19`: “The software and evidence are being prepared as a public tagged release … the repository and DOI fields are placeholders until that release is approved.”
- `paper2/README.md:4`: “The paper is a working draft, not a submission-ready article”; `:12` “23 pages, 8,930 source words”; `:81` “BLS is stronger than tabu on 14 instance means” (the manuscript says 15).
- `paper2/submission/jors/README.md:35–39`: repository and DOI placeholders; “individual authors, affiliations, ORCIDs, CRediT, funding, and competing-interest statements are not yet supplied.”

**Why it matters.** The paper’s central claim is an exact, replayable evidence boundary. A reader who follows the citation lands on a release whose own README says rc4, whose licence says rc4, and whose manifest says no release was created. The cover letter is submitted to the editor and says the release is not ready. This is precisely the provenance inconsistency the harness is supposed to prevent. It is not a scientific error, but it is a credibility error in the artifact the paper is selling, and it triggers the project’s own “public source/asset mismatch” stop-ship.

**Action.** Re-cut the release from a cleaned tree:
- Set `README.md:3` and `LICENSING.md:12` to `p14-evidence-rc8` (or the final tag) and one DOI status.
- Update the manifest `status`, `references.sha256`, and `replay.sha256`; re-verify all `files` hashes.
- Update `paper2/README.md` (remove “working draft/not submission-ready”; correct the 23-page/8,930-word and 14-vs-15 statements) and the JORS `README.md` (remove closed placeholders and blocking issues).
- Rewrite the cover letter so it describes the public release and a DOI pending on acceptance, with no placeholders.
- Add a release check that greps the tagged tree for `rc4`, `rc1`, `no tag/release created`, `NOT SUBMISSION-READY`, `not a submission-ready`, and `placeholders until`; fail the release if found.

#### M2. The availability section contains two factual errors: wrong repository and a false container-pinning claim (P0/P1)

**Evidence.**

- `MS p7` / `TEX:429–431`: “The harness, reference implementations, runners, replay scripts, and evidence are in the FRESH https://github.com/UBC-FRESH/fresh-solutions-papers.” The harness and reference implementations are in `https://github.com/UBC-FRESH/fresh-solutions` (correctly stated at `MS p6` / `TEX:343–345`); the papers repository contains the runners, evidence, and manuscripts.
- `MS p6` / `TEX:358–359`: “A Dockerfile and requirements file are included, but the container recipe is not yet pinned to a base-image digest and solver checkout, so we do not claim a tested container.” The Dockerfile now pins `python:3.12-slim@sha256:05a994d2…` (`Dockerfile:1`) and checks out `4583ad3` (`Dockerfile:6–7`). The rc7 release notes say “Docker base image pinned and FRESH Solutions checkout pinned to the GEO-fix commit.”
- `container/README.md:19–20` still says the exact base image digest and solver submodule checkout are missing.

**Why it matters.** Availability and reproducibility are the paper’s contribution. One sentence sends readers to the wrong repository for the software; the other tells them the container is unpinned when it is pinned. A JORS reviewer who checks the artifact will see both errors immediately. The container may still be untested — that is a legitimate caveat — but “not pinned” is false.

**Action.**
- Split the links: harness/reference implementations → `fresh-solutions`; runners/evidence/replay → `fresh-solutions-papers`.
- Replace the container sentence with: “The Dockerfile pins the base image digest and the solver checkout, but the recipe has not been tested end-to-end; we do not claim a tested container,” or run it and claim the test.
- Update `container/README.md` to match the Dockerfile.

#### M3. One-command replay is conditional, not self-verifying (P0/P1)

**Evidence.**

- `MS p6` / `TEX:361–366`: “After mounting QAPLIB and TSPLIB, one command replays the evidence: `bash paper2/replay_all.sh`.” The snippet omits cloning the repository with submodules, installing `container/requirements-evidence.txt`, and obtaining the `fresh-solutions` checkout at `4583ad3`.
- `paper2/replay_all.sh:4–12` runs the scripts; each script inserts `ROOT.parent/"fresh-solutions"` into `sys.path` (`paper2/check_evidence.py:12–14`) but never asserts the imported solver commit.
- Clean-clone test: a clone without submodules ran `check_evidence.py` against an installed `fresh-solutions` 0.9.0 and then failed `broad mismatch: tsp ali535 seed 1`. With no installed package, it would fail with `ModuleNotFoundError`.
- The repo README has `git submodule update --init --recursive` (`README.md:59`), but the paper does not; `paper/REPLAY.md` covers Paper 1 only, not Paper 2.

**Why it matters.** A reproducibility paper’s headline claim is that a reader can replay the evidence. The current recipe works only in a prepared checkout. Worse, the fallback is silent: if a different `fresh_solutions` is installed, the scripts import it and may fail on a broad-panel record without saying that the solver version is wrong. The evidence records carry `replay_solver_commit` (`4583ad3` for the 200 QAP records; `c7d1507` for the 200 BLS, 100 TSP, and 40 generic records), but the replay code does not check it.

**Action.**
- Add a Paper 2 `REPLAY.md` or a prerequisites block in §4: clone with `--recurse-submodules` or run `git submodule update --init --recursive`; `pip install -r container/requirements-evidence.txt`; set `QAPLIB_ROOT`/`TSPLIB_ROOT`; then `bash paper2/replay_all.sh`.
- Add a commit/version assertion in `check_evidence.py` and the replay scripts: read the expected `replay_solver_commit` from the evidence, import `fresh_solutions`, and fail closed if the installed source is not the pinned commit (or if the submodule directory is empty).
- Test from a clean clone and attach the log; the paper can then say “tested” rather than “one command” without qualification.

#### M4. Author metadata is still incomplete: no funding statement and no ORCID (P1)

**Evidence.** `MS p1` gives only name, affiliation, and email. `MS p7` has “Author contributions” and “Competing interests,” but no “Funding” or “Acknowledgements.” The submission README says “individual authors, affiliations, ORCIDs, CRediT, funding, and competing-interest statements are not yet supplied” (`paper2/submission/jors/README.md:37–39`), and the project’s own stop-ship list includes “Missing author/CRediT/funding/competing metadata required by the target” (`notes/plans/p15-final-submission-2026-11-12.md:22`).

**Why it matters.** A missing funding statement or ORCID is a common desk-return, and the project’s own checklist makes it a blocker. The supplement byline is now consistent with the main text, which is good; the remaining gap is the funding/ORCID metadata.

**Action.** Add a Funding statement (or “This research received no specific grant from any funding agency”) and an ORCID for the author. Confirm the corresponding author. Update the JORS README placeholders. If JORS requires additional declarations, add them in the same pass.

#### M5. The BLS inference still overstates precision (P1)

**Evidence.** `MS p4–5` / `TEX:249–257` reports:

- cluster-by-instance 95% interval −0.300 to −0.111 (correct; recomputation −0.2991 to −0.1108);
- family-cluster bootstrap −0.234 to −0.163 (correct arithmetic; only 3 families);
- 15/16 non-tied instance means and exact two-sided sign test p = 5.2 × 10⁻⁴ (correct arithmetic; 20 instances, 8 of them correlated `bur26` variants).

The caveat sentence says “The effective sample is 20 instances in three families, not 200 independent runs, so the clustered intervals are the appropriate summary,” but it does not distinguish the family bootstrap (3 clusters) from the instance bootstrap, and it does not attach a test-specific caveat to the sign test. The `bur26` variants are not independent: several have one to three distinct outcomes across all ten seeds (supplement diversity table), so the sign test’s independence assumption is not met.

**Why it matters.** The qualitative conclusion (BLS lower) survives, but the family-cluster interval and the p-value are stronger than the design supports. A statistically careful reviewer will flag this, and the paper’s own framing (“descriptive and clustered”) invites the check. This was rc4 M8 and remains open.

**Action.**
- Keep the cluster-by-instance interval as the primary descriptive summary.
- Label the family-cluster interval an informal sensitivity check with only 3 clusters, or drop it.
- Replace the sign-test p-value with a family-stratified permutation test or a hierarchical model, or report the 15/16 count without a p-value.
- State that the panel is a convenience sample, not a random sample of QAPLIB.
- State the 1.24 aggregation (mean of the 40 run-level CPU ratios; pooled ratio 1.215; mean of per-instance means 1.230) in §3.1 or a footnote.

### 6.4 Additional major/minor issues

#### M6. BLS-primary framing is still inconsistent

The text says “we treat BLS as the primary QAP quality reference and the tabu path as an unvalidated reference implementation” (`MS p5`; `TEX:261–262`). But Table 1 is titled “tabu reference versus … BLS” and lists the tabu columns first (`Table 1`; `TEX:230–247`); the abstract reports the tabu number first (`MS p1`; `TEX:39–41`); and the section title still says “QAP convergence panel and independent baseline” (`MS p4`; `TEX:218`). BLS is a separately implemented baseline by the same author, not an independent one. Either put BLS first and label the tabu “reference (unvalidated),” or explain why the package’s method is presented first while BLS is the quality yardstick. Rename “independent” to “separately implemented” (`MS p4`; `TEX:218`).

#### M7. Tabu `bur26`: scope is clean, but the diversity table is disconnected

The scope language is now appropriate: “a property of this untuned reference implementation, not … the tabu reference in general” (`MS p5`; `TEX:259–262`), and “unvalidated reference implementation” (`TEX:262`). The supplement adds a diversity table (`paper2-jors-supplement.tex:89–114`) that matches the records: distinct raw gaps are 2, 2, 1, 3, 1, 2, 1, 1 for `bur26a–h`; four instances have a single value. Two presentation gaps remain:

- The main text does not refer to the supplement diversity table. Add “see the supplement” and one sentence: “We did not establish whether the 0/80 result is a tuning issue or an implementation defect.”
- `bur26b` has two distinct raw gaps (0.564532, 0.565239) that both print as 0.565, so the row reads “2 distinct / best 0.565 / worst 0.565.” Show four decimals or add a footnote.

This is not a blocker; it is the evidence that distinguishes a deterministic trap from a tuning gap, and it should be visible.

#### M8. JORS length and focus: word count compliant, page count still high

The PDF is 8 pages; the body runs through p7 and the references occupy p7–8. The word count is 3,788, inside the 3,000–4,000 limit, and the supplement carries the detailed tables. The journal’s rough guide is 4–6 pages (`notes/plans/p14-journal-shift-2026-11-11.md:140–142`), so this remains a production risk even though the word count is compliant. The paper still reads more like a solver comparison than an experience report in places, and there is no dedicated “Lessons” section. The mixed-depth TSP disclosure is now complete in the abstract, §3.3, and the conclusion — that part is closed.

**Action.** Add a short “Lessons for reproducible benchmarking” section (4–5 bullets: the replay gate; budget/patience effects; protocol drift; a weak baseline can be exposed; the adapter contract is not a search engine). If the editor enforces the page guide, move Table 2 or the broad-screen details to the supplement; do not cut below 3,000 words or remove the negative results.

#### M9. Replay provenance is split across two commits (P2)

The 200 expanded-QAP records carry `replay_solver_commit=4583ad3`; the 200 BLS, 100 TSP, and 40 generic records carry `c7d1507`. The published release is `v0.9.3-p13rc1` = `4583ad3`. I compared the `fresh_solutions` trees at the two commits: 31 files, identical blob SHAs. So this is a re-stamp/bookkeeping inconsistency, **not** a code divergence. The science is not at risk, but a reader cannot map `c7d1507` to the cited release. Normalize all records to the released commit and re-stamp the manifest, or add a provenance table mapping each panel to its solver commit and replay commit.

### 6.5 Minor comments

- **m1.** The title “an adapter and exact-replay harness” is grammatically awkward. Use “an adapter- and exact-replay harness” or “an adapter and exact replay harness” (`MS p1`).
- **m2.** The abstract is 257 words. Confirm the JORS abstract limit. “A DOI is pending” is not idiomatic in an abstract; state the DOI status once in §4 instead (`MS p1`; `TEX:46`).
- **m3.** `TEX:208` has “1.17 to 1.33 .” — remove the space before the period.
- **m4.** State the 1.24 aggregation: it is the mean of the 40 run-level CPU ratios; the pooled ratio is 1.215 and the mean of per-instance means is 1.230 (`MS p4`; `TEX:207`; supplement framework table).
- **m5.** PDF metadata is blank (Title, Author, Subject, Keywords) and the page size is US Letter. Set `pdftitle`/`pdfauthor` via `hyperref` and confirm the JORS page size (`pdfinfo paper2-jors.pdf`).
- **m6.** `paper2/submission/jors/README.md:12` says the supplement is 2 pages; it is 3. `:24` says “6 pages of text/figures/tables plus 2 pages of references”; the body is 7 pages and the references start on p7. Update the counts.
- **m7.** `lkh-provenance.json:20` still contains the machine-specific path `/srv/shared-data/gep/ws4/tmp/LKH3/LKH`. Use a placeholder or repository-relative path.
- **m8.** The BLS claim “used the same … start” (`MS p4`; `TEX:223–224`) is not recorded in the QAP/BLS records (no start assignment or initial objective). Add the start rule/objective to the records or soften to “the same seed and start rule.”
- **m9.** “The generic runs … use about 117,000 exact evaluations” (`MS p6`; `TEX:336`) is per run (mean 117,117 QAP, 116,619 TSP), not total. Say “about 117,000 evaluations per run.”
- **m10.** Table 2’s depth-4 group includes `ch150` (n=150), which a reader may expect at depth 2 under an n-based rule; add a footnote that the recorded depth is the legacy value. Explain why `lin105` is depth 3 (`MS p5`; `Table 2`).
- **m11.** The conclusion says “The QAP panel shows that a patience rule changes the reported gaps relative to a short fixed budget” (`MS p7`; `TEX:411–412`). That comparison is in §2.3, not the QAP panel. Rephrase.
- **m12.** The LK causal claim “lacks α-nearness, fractional cascading, and the full LKH gain criteria, **which is why** the larger tail is weak” should be “we attribute” or “consistent with” (`MS p7`; `TEX:392–393`).
- **m13.** The DOI status is repeated in the abstract, §4, and Data availability (`MS p1`, `p6`, `p7`). State it once.
- **m14.** `.zenodo.json` and `CITATION.cff` declare `license: MIT` for the whole deposit, while `LICENSING.md` says manuscript text/figures and derived evidence are CC BY 4.0. Reconcile before the DOI is minted.
- **m15.** `paper2/README.md:76` still says “QAP robust tabu” and `:81` says 14 instance means (the paper says 15). Update or remove the stale working-manuscript prose.
- **m16.** The release assets are PDFs plus `REPLAY.md`; the evidence and scripts are in the tagged source tree. That is acceptable, but the paper should say “download the source at tag `p14-evidence-rc7`” rather than implying the assets alone contain the replay material.

---

## 7. Claim-to-evidence ledger

| Claim | Location | Evidence | Status |
|---|---|---|---|
| Tabu 0.301% mean, 0.043% median, 5.695% worst, 73/200 optima | `MS p1`, `p4`; Table 1 | `qap-expanded-100k-10seed.json` | **Supported** (0.30085, 0.04268, 5.69514, 73). |
| BLS 0.096% mean, 1.369% worst, 161/200 optima | `MS p4`; Table 1 | `qap-bls-10seed.json` | **Supported** (0.09614, 1.36861, 161). |
| Paired difference −0.205; cluster CI −0.300 to −0.111; 15/16; p = 5.2 × 10⁻⁴ | `MS p4–5` | recomputed from per-run JSON | **Supported arithmetically** (−0.20471; −0.2991 to −0.1108; 15/16; 5.19 × 10⁻⁴), with the clustering caveat in M5. |
| Family-cluster CI −0.234 to −0.163 | `MS p5` | recomputed | **Supported arithmetically**, but only 3 clusters; not a reliable 95% CI. |
| TSP 94/100 optima, 95/100 patience, 0.004% mean, 0.185% worst | `MS p1`, `p5`; Table 2 | `tsp-expanded-10k.json` | **Supported**; mixed-depth and cap-limited. |
| Framework 1.24 CPU ratio, CI 1.17–1.31, 40/40 matched and replayed | `MS p1`, `p4` | `framework-use.json` | **Supported** (1.2390; 1.1683–1.3098; 40/40). Aggregation not stated (M5/m4). |
| Broad QAP 134 instances, 552/670 patience, 318 optima, 1.823% converged mean, 36.445% worst | `MS p6` | `broad-converged-summary.json` | **Supported.** |
| Broad TSP 78 instances, 236/390 patience, 195 optima, 1.460% all-run mean; n>300: 3/100, 1 optima, 97 cap | `MS p6` | `broad-converged-summary.json` | **Supported.** |
| LKH 75/100 optima, 0.098% mean, 0% median, 1.930% worst, 15.0 s | `MS p6` | `lkh-large-summary.json` | **Supported.** |
| Generic QAP 3.848% vs 0.097%; TSP 127.978% vs 0.000%; ~117,000 evaluations | `MS p6` | `generic-tabu-summary.json` | **Supported** (3.8478, 0.0966, 127.978, 0.000, 117,117 / 116,619 per run). |
| 1,060 broad incumbents; 25 `esc8` skipped | `MS p6` | `broad-converged.json.gz` (1,085 records; 25 `esc8`) | **Supported.** |
| Every record names solver commit, seed, budget, stop reason, replay, wall time; CPU where available | `MS p3` | QAP/TSP/BLS/generic records; broad records use different fields | **Partly supported**; the broad schema still differs (`stop`, `wall`, etc.). |
| Manifest covers the ten-seed QAP files; hashes verify | `MS p6` | `manifest-v0.1.0-candidate.json` | **Supported** for `files` (65/65); `status`, `references`, and `replay` are stale. |
| Artifact is public as `p14-evidence-rc7` | `MS p1`, `p6` | release assets match; tagged docs say rc4/no release | **Partly supported**; manuscript/PDF match, package docs contradict (M1). |
| Harness is in `fresh-solutions-papers` | `MS p7` | harness is in `fresh-solutions` | **Not supported** (M2). |
| Container recipe is not pinned | `MS p6` | `Dockerfile:1,6–7` pins base digest and checkout | **Not supported** (M2). |
| QAPLIB/TSPLIB instances are not redistributed | `MS p6` | 4 QAP + 4 TSP files included with attribution | **Corrected**; statement now accurate. |
| Tabu 0/80 `bur26` is a property of this untuned reference | `MS p5`; supplement | seed-invariant/near-invariant outcomes; diversity table | **Supported as scope**; main text should cite the table (M7). |
| TSP depth disclosed | `MS p1`, `p5`, `p7` | 85/5/10 runs at depth 4/3/2; conclusion says mixed-depth | **Supported.** |
| One command replays the evidence | `MS p6` | works with submodule + deps; clean clone fails | **Conditional** (M3). |
| Author metadata complete | `MS p1`, `p7` | no funding/ORCID | **Not supported** (M4). |

---

## 8. Reviewer questions (Yes / No / N/A)

1. Does the manuscript fit JORS Issues in Research Software? **Yes, in principle** — it is an experience/reproducibility report on an evidence boundary. It is still slightly solver-comparison heavy, and a short “Lessons” section would improve the fit.
2. Is the software contribution clearly described? **Mostly** — adapter contract, resident state, replay gate, stopping taxonomy. There is no short API/usage example or test evidence.
3. Is the artifact public and independently replayable? **Partly** — the manuscript/PDF/supplement match the rc7 tag and all panels replay with the correct submodule; the package docs contradict the status, the one-command recipe is conditional, and the scripts do not assert the solver commit.
4. Are the headline numbers traceable to the evidence? **Yes** — QAP/BLS/TSP/framework/broad/LKH/generic numbers match. The schema claim is broader than the broad-screen records.
5. Is the BLS inference appropriately clustered? **Partly** — the cluster-by-instance interval is correct; the family-cluster bootstrap (3 families) and the sign test over correlated instances overstate precision.
6. Is the tabu baseline credible? **No, as a validated robust tabu** — 0/80 on `bur26` with near-invariant outcomes; the paper now scopes it as an unvalidated reference, and the supplement has the diversity evidence. The main text should cite it.
7. Is the TSP protocol consistent? **No by design** — mixed-depth, now disclosed in the abstract, §3.3, and the conclusion; the 94/100 is descriptive, not controlled.
8. Is the manuscript within the length guidance? **Word count yes; page count no** — 3,788 words, 8 pages, body ≈7 pages vs the rough 4–6 page guide.
9. Would I review a revision? **Yes.**

---

## 9. Risk table

| # | Risk | Likelihood | Impact | Evidence | Mitigation |
|---|---|---|---|---|---|
| R1 | Release package contradicts its own rc7 status (README/LICENSING say rc4; manifest says no release; cover letter says still being prepared) | High | High | `README.md:3`; `LICENSING.md:12`; `manifest…:200`; `cover-letter.md:16–19`; `paper2/README.md:4` | Re-cut after cleaning the docs; refresh the manifest; add a release grep check. |
| R2 | Availability section names the wrong repository and falsely says the container is not pinned | High | High | `MS p7`; `MS p6`; `Dockerfile:1,6–7`; `container/README.md:19–20` | Split the links; correct the container sentence; update the container README. |
| R3 | One-command replay is not hermetic or self-verifying; clean clone uses the wrong solver | High | High | `MS p6`; `replay_all.sh`; clean-clone failure at `ali535`; no commit assertion | Add prerequisites, a Paper 2 `REPLAY.md`, and a solver-commit assertion; test a clean clone. |
| R4 | Missing funding statement and ORCID | High | Medium | `MS p1`, `p7`; `jors/README.md:37–39`; `p15` stop-ship | Add funding/ORCID; update the README. |
| R5 | BLS inference overstates precision (3-family bootstrap; sign test over correlated `bur26`) | Medium | Medium | `MS p4–5`; supplement diversity table | Keep cluster-by-instance; label/drop the family interval; replace/drop the p-value; state the aggregation. |
| R6 | BLS-primary framing inconsistent (tabu-first table/abstract; “independent baseline”) | Medium | Low | `MS p1`, `p4`; Table 1 | Put BLS first or explain; rename “independent.” |
| R7 | Tabu `bur26` diversity table disconnected from the main text; `bur26b` row looks contradictory | Medium | Low | `MS p5`; supplement table | Cite the supplement; add the tuning-vs-defect sentence; show 4 decimals or a footnote. |
| R8 | JORS page guide (8 pages vs 4–6) and solver-comparison balance | Medium | Medium | `MS p1–7`; plan lines 140–142; 3,788 words | Add a Lessons section; move Table 2 or broad details to the supplement; do not cut below 3,000 words. |
| R9 | Replay stamps split `4583ad3`/`c7d1507` | Medium | Low | 200 QAP vs 200 BLS + 100 TSP + 40 generic records | Normalize/re-stamp; note the trees are identical. |
| R10 | Format/metadata defects (blank PDF metadata, US Letter, supplement 2 vs 3 pages, stale README counts) | Low | Low | `pdfinfo`; `jors/README.md:12,24` | Set metadata; align counts; confirm page size. |

**Top five residual risks (executive):**

1. **Release package contradicts rc7** (R1): the tag’s own docs say rc4, no release, not submission-ready, and the cover letter says the release is still being prepared. Mitigation: re-cut a clean release and add a release grep check.
2. **Availability factual errors** (R2): the harness link points to the papers repository; the container sentence says “not pinned” when the Dockerfile pins both. Mitigation: split the links and correct the sentence.
3. **One-command replay is conditional** (R3): a clean clone either fails or silently uses an installed solver; no commit guard. Mitigation: complete prerequisites, add a Paper 2 replay doc, assert the solver commit, test a clean clone.
4. **Missing funding/ORCID** (R4): a desk-return risk and a project stop-ship. Mitigation: add both.
5. **BLS inference overstates precision** (R5): the family bootstrap has 3 clusters and the sign test treats correlated `bur26` variants as independent. Mitigation: keep the cluster-by-instance interval, label/drop the family interval, replace/drop the p-value.

---

## 10. P0 / P1 / P2 list

### P0 — stop-ship

- **P0-1. Release package metadata contradicts rc7.** `README.md:3`; `LICENSING.md:12`; `manifest…:200`; `cover-letter.md:16–19`; `paper2/README.md:4`; `jors/README.md:35–39`. Re-cut the release after cleaning the docs and refreshing the manifest.
- **P0-2. One-command replay is not hermetic or self-verifying.** `MS p6`; `replay_all.sh`; clean-clone failure at `ali535`; no solver-commit assertion. Add prerequisites and a commit guard, and test a clean clone.

### P1 — major, affects submission readiness/credibility

- **P1-1. Availability factual errors.** Wrong repository for the harness (`MS p7`); false “not pinned” container claim (`MS p6`; `Dockerfile:1,6–7`; `container/README.md:19–20`).
- **P1-2. Author metadata incomplete.** No funding statement, no ORCID (`MS p1`, `p7`; `jors/README.md:37–39`).
- **P1-3. BLS inference overstates precision.** Family-cluster bootstrap with 3 clusters; sign test over correlated `bur26` (`MS p4–5`).
- **P1-4. Manifest is stale.** `status`, `references.sha256`, and `replay.sha256` are wrong even though 65/65 `files` verify (`manifest…:200,211,221`). This is part of P0-1 but worth a separate check.

### P2 — minor/clarity

- **P2-1.** BLS-primary framing: Table 1 tabu-first; section title “independent baseline”; abstract tabu-first (`MS p1`, `p4`; Table 1).
- **P2-2.** Tabu `bur26`: cite the supplement diversity table; add the tuning-vs-defect sentence; fix the `bur26b` rounding (`MS p5`; supplement).
- **P2-3.** JORS page guide: add a “Lessons” section; move Table 2 or broad details to the supplement if needed (`MS p1–7`).
- **P2-4.** Replay stamps split `4583ad3`/`c7d1507`; the `fresh_solutions` trees are identical, so normalize/re-stamp (`qap-expanded-100k-10seed.json`; `qap-bls-10seed.json`; `tsp-expanded-10k.json`; `generic-tabu.json`).
- **P2-5.** State the 1.24 aggregation; pooled 1.215, mean of per-instance means 1.230 (`MS p4`; supplement).
- **P2-6.** PDF metadata blank; US Letter; supplement 3 pages vs README 2; body-page count (`pdfinfo`; `jors/README.md:12,24`).
- **P2-7.** LKH machine-specific path (`lkh-provenance.json:20`).
- **P2-8.** BLS “same start” not recorded; soften or add the start rule (`MS p4`).
- **P2-9.** Generic “about 117,000 evaluations” is per run (`MS p6`).
- **P2-10.** Table 2 `ch150` depth-4 footnote; explain `lin105` depth 3 (`MS p5`; Table 2).
- **P2-11.** Conclusion attributes the budget effect to the QAP panel; LK “which is why” causal claim (`MS p7`).
- **P2-12.** DOI repeated; title grammar; “1.17 to 1.33 .” spacing; `.zenodo.json`/`CITATION.cff` MIT vs CC BY (`MS p1`, `p4`, `p6`, `p7`).

---

## 11. Overall assessment

The paper is a genuine JORS-style experience report with a real software contribution and an unusually honest evidence culture. The adapter contract, replay gate, and stopping taxonomy are the right things to publish, and the negative results are appropriate for the venue if framed as lessons rather than rankings. The headline numbers reproduce; the BLS inference is clustered; the TSP depth drift is disclosed in the abstract, §3.3, and the conclusion; the tabu is scoped as unvalidated; the redistribution statement is corrected; and the supplement now carries the diversity evidence.

The submission is close but not yet submission-ready. The public rc7 package still advertises rc4 and “no release,” the manuscript names the wrong repository for the harness and falsely says the container is not pinned, the author metadata lacks funding/ORCID, the replay path is conditional and not self-verifying, and the BLS inference still overstates precision. These are bounded fixes; none requires a new campaign. After a re-cut release, two corrected availability sentences, a funding/ORCID line, a complete replay prerequisites block with a solver-commit assertion, and a more careful statistical caveat, this would be a credible JORS paper.

**Exact recommendation.** **Major revision.** Do not submit rc7. Prepare rc8 with the five fixes above; re-run `bash paper2/replay_all.sh` from a clean clone with the submodule and requirements; re-verify the two PDF hashes and the manifest; then submit. No new experiments are required. If the editor treats package metadata as a pre-submission check rather than a revision, the same list supports a minor-revision decision; the scientific core does not need to be redone.

---

## 12. QA checklist (before submission)

- **Evidence-only:** every substantive claim has a citation tag. Yes.
- **Anonymity/privacy:** no reviewer-identifying details; no third-party personal information beyond the materials. Yes.
- **Tone:** professional, constructive, inclusive. Yes.
- **Bias hygiene:** critiques anchored to the submission’s content and evidence, not prestige or subfield preference. Yes.
- **Actionability:** each major comment names a file/page, why it matters, and a bounded action. Yes.
- **Venue fit:** the review assesses JORS Issues in Research Software, not JoH or SoftwareX criteria. Yes.
- **Scope discipline:** only remaining submission blockers and regressions were checked; completed experiments were not reopened. Yes.
