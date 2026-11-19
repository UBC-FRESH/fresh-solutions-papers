# Reviewer Report — Paper 2 (JORS, Issues in Research Software)

**Manuscript:** FRESH Solutions: an adapter and exact-replay harness for metaheuristic benchmarking
**Author:** Gregory Paradis, UBC FRESH Lab, University of British Columbia
**Materials reviewed:** `paper2/submission/jors/paper2-jors.tex`; `paper2/submission/jors/paper2-jors.pdf` (9 pp.); `paper2/submission/jors/paper2-jors-supplement.pdf` (2 pp.); `paper2/submission/jors/README.md`; `paper2/submission/jors/cover-letter.md`; `paper2/evidence/` and `paper2/evidence/manifest-v0.1.0-candidate.json`; public releases `p14-evidence-rc2` and `v0.9.3-p13rc1`; `notes/reviews/paper2-antagonistic-2026-11-11.md` (prior JoH review); `notes/plans/p14-journal-shift-2026-11-11.md`.
**Reviewer stance:** antagonistic JORS associate editor / Reviewer 2. I checked the headline numbers against the committed evidence, recomputed the BLS statistics from the per-run JSON, inspected the public release assets and the tagged source, and read the replay/container scripts. I did not rerun the campaigns.
**Recommendation:** **Major revision** — not submission-ready in the present form.
**Prepared to review after revision:** **Yes.**
**Refereeing openly:** No.
**Include in annual reviewer list:** No.

---

## Overrides (project-specific constraints)

- Target venue: **JORS, Issues in Research Software** — experience/reproducibility report, 3,000–4,000 words, roughly 4–6 pages, Vancouver-style numbered references, no mandatory LaTeX template. The format facts are taken from `notes/plans/p14-journal-shift-2026-11-11.md:139–142, 156–169`.
- Evidence tags: `MS pX` for the PDF page, `Table N` / `Fig N` for objects, and `file:line` or repository paths for evidence and code.
- No external literature is introduced. General domain judgment is applied only to the submission's own claims and evidence.
- All materials are treated as confidential. No reviewer-identifying details are included.

---

## 1. Document inventory

| Item | Status | Notes |
|---|---|---|
| `paper2-jors.pdf` | Present | 9 pages: 7 body pages + 2 reference pages; 2 figures, 2 tables, 28 references. |
| `paper2-jors.tex` | Present | 438 lines; clean build in the supplied log (no undefined citations/overfull boxes). |
| `paper2-jors-supplement.pdf` | Present | 2 pages; per-instance QAP/TSP/framework tables. |
| Word count | **Inconsistent** | Cover letter and release notes say **3,798**; `README.md:21` says **3,815**; `detex -n paper2-jors.tex \| wc -w` gives **3,801**. All are inside 3,000–4,000. |
| Page count | **Over guide** | 9 pages vs the rough 4–6 page guide (`notes/plans/p14-journal-shift-2026-11-11.md:232`). Body is 7 pages even after excluding references. |
| Evidence manifest | Present | 66 files; I recomputed every SHA-256: **0 missing, 0 mismatched**. It **does** include `qap-expanded-100k-10seed.json` and its summary. |
| Public release `p14-evidence-rc2` | Present, **wrong asset** | GitHub prerelease at tag `5d75c04`. The attached `paper2-jors.pdf` is the **rc1** manuscript (see M1). |
| Public release `v0.9.3-p13rc1` | Present | FRESH Solutions prerelease at commit `4583ad3`; Apache-2.0. |
| Container | Present, **untested/inconsistent** | Dockerfile pins `7d3c831` (campaign commit), not the replay commit `4583ad3`. |
| Author metadata | **Incomplete** | Name/email only; no ORCID, CRediT, funding, competing interests, or acknowledgements. |

---

## 2. Quick synopsis

The manuscript describes a Python harness with a small problem-adapter contract, resident assignment state, an exact replay gate, a stopping/budget taxonomy, and QAP/TSP reference adapters. It reports a 40-run framework-use check, a 200-run QAP/BLS panel, a 100-run mixed-depth TSP breadth panel, broad QAP/TSP screens, an external LKH capability check, and a generic adapter-only negative result.

The JORS experience-report framing is appropriate: the adapter boundary and replay protocol are real contributions, and the paper is unusually candid about failures. The prior JoH review's main statistical objection has been addressed: the BLS comparison now reports a cluster-by-instance interval and an instance-level sign test, and the replay script now covers the 200-run BLS panel. The TSP mixed depth is also disclosed per instance.

The submission is nevertheless not ready. The public artifact does not contain the manuscript under review; the availability section says both that the evidence is public and that it is not public; the per-record schema claim is false for the headline QAP/TSP panels; the manifest-completeness claim is false; the tabu reference is not credible on `bur26`; and the TSP panel is mixed-depth yet still used as a headline 94/100 result. The draft is also 9 pages against a 4–6 page guide and still reads too much like a solver comparison for an Issues in Research Software paper.

---

## 3. Confidential comments to the editor

I recommend **major revision**, not rejection. The paper now fits JORS much better than it fit JoH: the contribution is explicitly the harness, the replay contract, and the evidence protocol; the applied TSA24 case has been removed; the BLS inference is cluster-aware; and the TSP depth drift is disclosed. The authors have done the hard part of the reframing.

The submission package, however, is not internally consistent. The release cited as `p14-evidence-rc2` contains a PDF and tagged source that still say `p14-evidence-rc1`; the manuscript and the release are different versions. The availability paragraph simultaneously says the evidence is public, is a candidate, and is not public or archived. The paper promises wall and CPU time in every record but the 200-run QAP and 100-run TSP records have no `cpu_seconds`. The paper says the manifest does not cover the ten-seed QAP files, but it does, and all hashes verify. These are not cosmetic for a reproducibility venue; they are the claims the paper is making.

The scientific risks are also material. The tabu reference reaches **0/80** optima on `bur26` while BLS reaches **80/80**, with several tabu outcomes identical across all ten seeds. Calling this an "untuned reference" is not sufficient; a robust tabu should solve `bur26`. The TSP breadth panel mixes depth 4/3/2 and includes five wall-clock cap hits, so the 94/100 is descriptive, not a controlled result. Both can be handled by reframing and by cutting length, but they need explicit treatment.

I would be willing to review a revision. I would not support sending the current version to production, and I would not support acceptance until (a) the release asset matches the submitted manuscript, (b) the availability/DOI status is unambiguous, (c) the per-record schema claim is either true or scoped, and (d) the tabu and TSP panels are either validated or explicitly demoted from headline status.

---

## 4. Comments to the authors

### 4.1 Summary

The manuscript addresses a genuine problem: applying known metaheuristics to new problems is slowed by the engineering around the search — state, moves, feasibility, stopping rules, replay, and benchmark bookkeeping. The adapter contract, resident-state path, and replay gate are sensible design ideas, and the paper reports failures (the tabu's `bur26` weakness, the `brazil58` cap hits, the generic layer's non-competitiveness, the missing per-record CPU) rather than hiding them. The QAP/TSP reference implementations are serious efforts, and the BLS baseline is a substantial addition.

The paper's centre of gravity is still wrong for JORS. The strongest contribution is the evidence boundary — the rule that a stored incumbent is re-evaluated by a new adapter before it becomes a result, and that the stop reason and denominator travel with the result — but the abstract and validation sections lead with gap comparisons. The paper also has several claim-to-evidence mismatches in the availability section, and the public release does not contain the version under review. These are major issues, not polish.

### 4.2 What works (evidence-based strengths)

1. **The adapter boundary is clearly specified.** The contract separates discrete state, exact evaluation, feasibility, mutation/crossover, and reversible moves, and the search layer sees only that interface (`MS p2`; `paper2-jors.tex:128–141`). The `apply`/`undo` exact-inverse requirement and the adapter-owned permutation invariant are well stated (`MS p2`).
2. **The replay gate is the right idea.** A stored incumbent is re-evaluated through a new adapter state, not the optimizer's cached counter (`MS p3`; `paper2-jors.tex:152–159`). The gate checks objective, feasibility, and permutation validity, and it fails closed.
3. **The stopping taxonomy is useful.** Plateau stop, safety-cap hit, budget exhaustion, and invalid replay are distinguished, and the denominator is visible (`MS p3`; `paper2-jors.tex:169–175`). This is better than most heuristic papers.
4. **The headline QAP/BLS/TSP/framework numbers reproduce.** I checked the QAP panel against `qap-expanded-100k-10seed.json` (0.301% mean, 0.043% median, 5.695% worst, 73/200 optima), the BLS panel against `qap-bls-10seed.json` (0.096% mean, 1.369% worst, 161/200 optima), the TSP panel against `tsp-expanded-10k.json` (0.004% mean, 0.185% worst, 94/100 optima, 95/100 patience), and the framework panel against `framework-use-summary.json` (1.239 mean CPU ratio, 1.168–1.310 bootstrap CI). The arithmetic is consistent.
5. **The BLS inference is now clustered.** The cluster-by-instance interval is the right primary summary. Recomputing from the per-run JSON gives **−0.2985 to −0.1129** (the paper rounds to −0.300 to −0.111), a point estimate of **−0.2047**, and **15/16** non-tied instance means (p = 5.19 × 10⁻⁴). This addresses the prior JoH review's main statistical objection.
6. **The one-command replay now covers the 200-run BLS panel.** `paper2/replay_all.sh:9,12` uses `QAP_EXPANDED_EVIDENCE=qap-expanded-100k-10seed.json` and `--input qap-bls-10seed.json`. This fixes the prior JoH review's M3.
7. **The TSP mixed depth is disclosed per instance.** `MS p5` states 17 depth 4, `lin105` depth 3, `d198`/`pr152` depth 2, and says it is not one adaptive-depth experiment. That is the right direction.
8. **The supplement is appropriate.** Full per-instance QAP/TSP tables and the framework panel are in the supplement, which is the right place for a 3,000–4,000-word JORS paper.

### 4.3 Venue fit by component

| Component | Current role | JORS fit | Recommendation |
|---|---|---|---|
| Adapter/replay contract | Core contribution, §2 | **Strong** | Keep; lead the abstract and introduction with it. |
| Framework overhead (1.24×) | §3.1, abstract, conclusion | **Moderate** | Keep as a short implementation-cost paragraph. Report the production-path ratio or label it a microbenchmark against the private-array path. |
| QAP/BLS panel | §3.2, Table 1, abstract | **Moderate** | Keep one table and two paragraphs as evidence-boundary validation; move the per-instance table to the supplement. Do not lead with the gap. |
| TSP breadth panel | §3.3, Table 2, abstract, conclusion | **Weak as headline; strong as a lesson** | Reframe as a protocol-drift lesson; rerun under one rule or demote the 94/100 to a descriptive sentence. |
| Broad screens | §3.4 | **Weak** | One paragraph or supplement; not a headline. |
| External LKH | §3.4 | **Weak** | One sentence or cut. It is capability-only and not matched time. |
| Generic negative result | §3.4 | **Strong as a lesson** | Keep one paragraph; state random starts and work; frame as "the adapter contract is not a search engine." |
| BLS inference | §3.2 | **Moderate** | Keep the cluster-by-instance interval; drop or caveat the 3-family bootstrap and the sign-test p-value. |

### 4.4 Major comments

#### M1. The public artifact is not the manuscript under review; the `p14-evidence-rc2` release contains rc1 (P0)

**Evidence.** The manuscript says the artifact is public as `p14-evidence-rc2` (`MS p1`; `paper2-jors.tex:46`) and points readers to `https://github.com/UBC-FRESH/fresh-solutions-papers/releases/tag/p14-evidence-rc2` (`MS p6`; `paper2-jors.tex:352`). The actual release asset at `.../releases/download/p14-evidence-rc2/paper2-jors.pdf` has SHA-256 `5ae7c528…` and its page 6 says **"release candidate `p14-evidence-rc1`"**; the tagged source at `5d75c04` also says rc1 (`git show 5d75c04:paper2/submission/jors/paper2-jors.tex`). The working-tree PDF has SHA-256 `942d373e…` and says rc2. The commit `7ab2260` ("Point target drafts at release candidate 2") is **one commit after** the release tag and is not in it.

**Why it matters.** The paper's central claim is exact replay and an evidence boundary. The release itself is not an exact copy of the submitted manuscript: a reader who downloads the cited artifact gets a different version, with a different URL and a different release label. This is precisely the failure mode the replay gate is supposed to prevent. It also means the manuscript under review cannot be cited from the public artifact.

**Action.**
- Re-tag and re-release from the **exact submitted commit**; rebuild the PDF and supplement from the tagged source.
- Verify that the tagged `paper2-jors.tex` and the released `paper2-jors.pdf` contain `p14-evidence-rc2`, not rc1, and that the release asset SHA-256 matches the submitted PDF.
- Add a release check that greps the tagged source and extracted PDF text for the release string; fail the release if they disagree.
- Update the release notes and the cover letter with the exact tag, commit, and asset hashes.

#### M2. The availability section contradicts itself and contains a placeholder DOI (P0)

**Evidence.** Four statements in the submission cannot all be true:
- `MS p1` / `paper2-jors.tex:46`: "The artifact is public as release candidate `p14-evidence-rc2`; DOI pending explicitly."
- `MS p6` / `paper2-jors.tex:353–354`: "The evidence release is public, but it is a candidate rather than a candidate (`paper2-evidence-v0.1.0`) and is not public or archived at the time of writing."
- `MS p6` / `paper2-jors.tex:384`: "The repository and tag are public; a DOI and a tested container digest are still pending."
- `MS p7` / `paper2-jors.tex:431–432`: "The evidence candidate is `paper2-evidence-v0.1.0`; it is not yet tagged, archived, or public."

The DOI field is the literal placeholder `[DOI to be assigned]` (`MS p6`; `paper2-jors.tex:353`). The cover letter repeats that the repository and DOI fields are placeholders (`cover-letter.md:18–19`).

**Why it matters.** JORS's reproducibility/availability expectations depend on a stable, citable artifact. A reader cannot tell what is public, what is tagged, what is archived, and what is citable. A placeholder DOI in the submitted manuscript is a desk-return risk, and the "not public or archived" sentence directly contradicts the public release the paper cites.

**Action.**
- Replace the prose with a small **availability table**: software (repository, tag, commit, licence), evidence (repository, release tag, commit, DOI, licence), container (status), replay command.
- State one status per row. If the evidence is a public prerelease and the archival tag/DOI is pending, say exactly that once.
- Obtain or assign the DOI before submission; if that is impossible, state "DOI will be assigned on acceptance" in one place and remove the placeholder. Do not say both "public" and "not public."
- Delete "candidate rather than a candidate" and the "not public or archived" sentence.

#### M3. The per-record schema claim is false for the headline QAP/TSP panels (P0)

**Evidence.** `MS p3` / `paper2-jors.tex:153–155` says: "The record names ... the pinned solver version or commit, the seed, the iteration or kick budget, the stopping reason, the exact-replay result, and the wall and CPU time." `MS p6` / `paper2-jors.tex:380–381` then says: "Per-record CPU time is missing from the expanded-QAP and expanded-TSP records (the BLS and generic records carry it)." I parsed the JSON:
- `qap-expanded-100k-10seed.json`: **0/200** `cpu_seconds`; **200/200** `wall_seconds`, `solver_commit`, `replay_solver_commit`, `hardware`, `iterations_budget`.
- `tsp-expanded-10k.json`: **0/100** `cpu_seconds`; **100/100** `wall_seconds`, `max_depth`.
- `qap-bls-10seed.json`: **200/200** `cpu_seconds`; `generic-tabu.json`: **40/40** `cpu_seconds`.

`paper2/evidence/provenance-2026-11-03.json` also says the per-record schema is "a release blocker, not a completed per-record schema."

**Why it matters.** The artifact claim is a per-record evidence schema. The two headline panels fail it. A reader cannot audit the CPU side of the QAP/TSP tables, and the manuscript simultaneously promises and denies the field. This is a direct internal contradiction, not a minor omission.

**Action.**
- Either add `cpu_seconds` to the 300 QAP/TSP expanded records and re-run the replay, or change `MS p3` to "wall time and, where recorded, CPU time" and scope the schema claim explicitly.
- Remove "release blocker" language from the manuscript. A submitted paper should not advertise an incomplete artifact. If CPU cannot be recovered, say the QAP/TSP tables are gap-only and that CPU is reported only for the BLS, generic, and framework panels.
- Add a JSON-schema test that fails on missing fields, and run it in `replay_all.sh`.

#### M4. The manifest-completeness claim is false (P0)

**Evidence.** `MS p6` / `paper2-jors.tex:380–383` says "the candidate manifest does not yet cover the ten-seed `qap-expanded-100k-10seed` files used in Table 1." The manifest `paper2/evidence/manifest-v0.1.0-candidate.json` **does** include `paper2/evidence/qap-expanded-100k-10seed.json` and `qap-expanded-100k-10seed-summary.json`. It lists 66 files; I recomputed all 66 SHA-256 hashes and found **0 missing and 0 mismatched**. The JORS `README.md:48–50` says the manifest covers the ten-seed files; the manuscript says the opposite.

**Why it matters.** A false statement about the artifact's completeness undermines trust in the entire availability section. It also contradicts the release notes' claim that the public clone passes and the README's own status.

**Action.**
- Delete the manifest sentence and replace it with: "The candidate manifest covers the 66 evidence files, including the ten-seed QAP panel; all hashes verify as of [date]."
- Add a `sha256sum -c`-style check to `replay_all.sh` or `check_evidence.py`.
- If some files are intentionally excluded, list them and say why.

#### M5. The tabu reference is not credible on `bur26`; the QAP/BLS comparison is not a fair test of robust tabu (P1)

**Evidence.** Table 1 reports tabu **0/80** optima on `bur` and BLS **80/80** (`MS p4`; `Table 1`). The supplement's per-instance table shows tabu **0/10** on all eight `bur26` variants and BLS **10/10** (`paper2-jors-supplement.pdf`, QAP table). The tabu gaps are 0.004–0.565%, and several outcomes are **identical across all ten seeds**: `bur26c` 0.004, `bur26e` 0.009, `bur26g` 0.376, `bur26h` 0.368. The paper calls the method "robust tabu search" (`MS p3`; `paper2-jors.tex:187–190`) and explains the 0/80 as an "untuned reference implementation" (`MS p5`; `paper2-jors.tex:266–270`).

**Why it matters.** A robust tabu search should solve `bur26`; a 0/80 result with near-optimal gaps and seed-invariant outcomes suggests a trap or an implementation defect, not merely a tuning issue. If the tabu is weak, the BLS comparison says "BLS beats a weak tabu," not "BLS beats robust tabu." The negative result is then about the authors' tabu implementation, not about robust tabu or the harness. The paper's own framing ("the harness made a stronger baseline visible") is still defensible, but the "robust tabu" label is not.

**Action.**
- Verify the tabu against Taillard's published `bur26` results or a published robust-tabu implementation.
- Diagnose the trap (tenure, aspiration, asymmetric delta path, restart) and report per-seed diversity.
- If it cannot be fixed, rename it "tabu search reference (not validated)" and remove "robust"; make BLS the primary QAP reference and present the tabu as a cautionary baseline.
- Add a Limitations sentence: "We did not establish whether the 0/80 `bur26` result is a tuning or implementation issue."
- Soften "the harness made a stronger baseline visible" to "the harness made the tabu's weakness visible."

#### M6. The TSP breadth panel is mixed-depth and cap-limited, yet used as a headline 94/100 result (P1)

**Evidence.** `MS p5` / `paper2-jors.tex:274–288` says the panel uses "depth 4 for 17 instances, depth 3 for `lin105`, and depth 2 for `d198` and `pr152`"; it "combines runs produced under a legacy depth-4 setting and later runs at reduced depth after the original depth-4 pass on `d198` exceeded 300 seconds per kick"; and it is "not one adaptive-depth experiment." The abstract (`MS p1`) and conclusion (`MS p7`) still use **94/100** and **95/100** as headline results; the conclusion does not mention mixed depth. The 3,600 s cap is close to `bier127`'s mean 2,180 s and `gr120`'s 1,700 s (`tsp-expanded-10k-summary.json`), so a slower host could change the patience count. The paper acknowledges this at `MS p7`, but the abstract does not.

**Why it matters.** The panel is not a controlled experiment: it mixes protocols and includes five cap hits that reached the optimum. The 94/100 is descriptive, not a validation of a single method. For a reproducibility venue, the interesting result is the **protocol drift** — the panel changed mid-campaign, and per-run depth records are what make the drift visible. Presenting the number as a headline invites the criticism that the authors are reporting an uncontrolled result as a success.

**Action.**
- Reframe §3.3 as a "protocol drift" lesson: the panel was frozen after a mid-campaign depth change; per-run depth is recorded; the 94/100 is descriptive, not a controlled comparison.
- Move the full table to the supplement; keep one summary sentence and the five cap hits in the main text.
- In the abstract and conclusion, say "a frozen mixed-depth panel reached 94/100, with five cap hits; we do not interpret depth as a controlled factor."
- Alternatively, rerun the 20-instance panel under one pre-registered depth rule before submission. If the authors choose this, report both the original and rerun panels, not just the new one.

#### M7. JORS fit and length: 9 pages against a 4–6 page guide; the draft still reads like a solver paper (P1)

**Evidence.** The PDF is **9 pages** (7 body + 2 references), while the JORS guidance is roughly **4–6 pages** (`notes/plans/p14-journal-shift-2026-11-11.md:232`). The word count is 3,798/3,801/3,815, inside 3,000–4,000. The abstract is **256 words** and leads with the QAP/BLS gap (0.301/0.096) and the 1.24 CPU ratio, not the adapter/replay problem (`MS p1`). The validation section spends most of its space on the QAP/BLS panel (`MS p4–5`), the TSP panel (`MS p5`), the broad screens and LKH (`MS p5–6`), and the generic negative result (`MS p6`); the "lessons" are scattered through Limitations.

**Why it matters.** JORS Issues in Research Software wants an experience/reproducibility report, not a mini solver comparison. A 9-page submission may be desk-checked as over length even though the word count is inside the limit. The current balance also obscures the strongest contribution: the evidence boundary.

**Action.**
- Cut to roughly **6–7 pages total**:
  - QAP/BLS: one table + two paragraphs; move the per-instance table to the supplement.
  - LKH: one sentence or supplement; it is capability-only, not matched time.
  - Broad screens: one paragraph; keep the full distributions in the evidence.
  - Generic negative result: one paragraph; state random starts and work; frame as a lesson.
  - Framework overhead: one short "implementation cost" paragraph; report the production-path ratio or label it a microbenchmark against the private-array path.
- Add a short **"Lessons for reproducible benchmarking"** section with 4–5 bullets: the replay gate; budget/patience effects; protocol drift; a weak baseline can be exposed; the adapter contract is not a search engine.
- Rewrite the abstract to lead with the problem, the adapter contract, and the replay gate; keep the QAP/BLS/TSP numbers as brief evidence, not the headline.

#### M8. Provenance is split across two replay commits and the container pins a third (P1)

**Evidence.** The QAP expanded records carry `replay_solver_commit=4583ad3` (200/200); the BLS/TSP/generic records carry `replay_solver_commit=c7d1507` (200/100/40). The paper cites release candidate `v0.9.3-p13rc1`, which is `4583ad3`; the `fresh-solutions` submodule is also `4583ad3`. `c7d1507` is a different tree: the GitHub compare API reports the two commits diverged, with `fresh_solutions/adapters/tsp.py` refactored. The container Dockerfile checks out `7d3c831` (the campaign commit), not `4583ad3` or `c7d1507` (`container/Dockerfile:7`). The JORS `README.md:51–53` acknowledges the split; the manuscript does not.

**Why it matters.** A reproducibility paper needs one immutable replay identity per table. A reader cannot tell which commit produced which table, and the container does not reproduce either replay commit. The prior JoH review flagged three commits; the JORS draft still has three (`7d3c831`, `4583ad3`, `c7d1507`).

**Action.**
- Choose one immutable replay commit (preferably the public release tag), re-stamp all records, rebuild the container at that commit, and add a provenance table mapping each table to evidence file, solver commit, replay commit, and hardware.
- If `c7d1507` is required for the TSP/BLS/generic panels, publish it as the tag and explain why; do not leave the paper citing a different commit.
- Add a `check_evidence.py` assertion that every record's `replay_solver_commit` matches the cited release commit.

#### M9. The one-command replay is not a complete recipe, and the container is untested and pins the wrong commit (P1)

**Evidence.** `MS p6` / `paper2-jors.tex:368–372` says: "After mounting QAPLIB and TSPLIB, one command replays the evidence: `export QAPLIB_ROOT=...; export TSPLIB_ROOT=...; bash paper2/replay_all.sh`." This omits clone, submodule initialization, dependency installation, and the expected directory layout. `replay_all.sh` imports from the `fresh-solutions` submodule; a clean clone without `git submodule update --init --recursive` fails. The root `README.md:54–59` has the steps, but the paper does not.

The Dockerfile uses `FROM python:3.12-slim` (no digest) and `git checkout 7d3c831` (`container/Dockerfile:1–7`). The paper says the container is "not yet pinned to a base-image digest and solver checkout" (`MS p6`; `paper2-jors.tex:365–366`), but the solver checkout **is** pinned — to the wrong commit. `container/README.md` says the solver checkout is missing, which is also stale.

**Why it matters.** The paper's reproducibility claim rests on a one-command replay. A reader who follows the paper's two-line snippet may fail, and a reader who tries the container may replay against the campaign commit rather than the GEO-fix/replay commit. The container is optional, but if it is mentioned it should be accurate.

**Action.**
- Replace the snippet with a complete, tested sequence: `git clone --recursive <papers repo>`, `pip install -r container/requirements-evidence.txt`, set `QAPLIB_ROOT`/`TSPLIB_ROOT` with the expected layout, `bash paper2/replay_all.sh`; report the expected output counts (200/200 BLS, 200/200 QAP, 100/100 TSP, 40/40 generic, 40 framework + 20 deep TSP, 1,060 broad).
- Either remove the container claim or pin the base-image digest and the replay commit, build it, and report the test result.
- Update `container/README.md` to match the Dockerfile.

#### M10. The licence and data-redistribution statements are inaccurate/stale (P1)

**Evidence.** `MS p6` / `paper2-jors.tex:356–358` says: "QAPLIB and TSPLIB instances are referenced by name and are not redistributed." The repository and release include eight instance files: `paper2/instances/{tai12a,tai20a,tai25a,tai30a}.dat` and `{berlin52,ch150,kroA100,kroB100}.tsp` (`git ls-files`). `paper2/instances/README.md` says "These are public benchmark instances. Preserve source attribution in any redistribution." `LICENSING.md` says "The repository is not yet public. This file states the intended release licensing" — but the repository is public. The paper says the runners/evidence are "intended for release under CC BY 4.0" (`MS p6`; `paper2-jors.tex:356–357`), which is not an actual licence statement.

**Why it matters.** The paper's redistribution claim is factually wrong; a JORS reviewer checking the artifact will see the eight files. QAPLIB/TSPLIB may impose different terms, and the repository's own `LICENSING.md` says source datasets may have different terms. "Intended" is not a licence. A JORS submission needs a clear licence.

**Action.**
- Either remove the eight instance files from the release (keep them in a separate, clearly licensed data package) or correct the statement: "A small smoke-test subset of QAPLIB/TSPLIB instances is included with attribution in `paper2/instances/`; the full libraries are not redistributed."
- Update `LICENSING.md` to remove "not yet public" and state the actual terms for code, text/figures, derived evidence, and the included instances.
- In the paper, say "released under" rather than "intended for release."

#### M11. Author metadata and journal-required statements are missing (P1)

**Evidence.** The manuscript has a single author and email (`MS p1`), but no ORCID, CRediT, funding, competing interests, acknowledgements, or a citable DOI. The JORS `README.md:37–39` says "individual authors, affiliations, ORCIDs, CRediT, funding, and competing-interest statements are not yet supplied." The supplement uses "UBC FRESH Lab" as the author, while the main text uses "Gregory Paradis" (`paper2-jors-supplement.tex:14`).

**Why it matters.** JORS submission requires these statements; a missing competing-interest or funding statement is a common desk-return. The supplement/main byline inconsistency is a small but visible defect in a package that is otherwise carefully produced.

**Action.**
- Add ORCID, CRediT, funding, competing interests, and acknowledgements before submission.
- Reconcile the supplement byline with the main manuscript.
- Confirm the corresponding author and affiliation.

#### M12. The BLS inference is improved but still overstates precision in two places (P2)

**Evidence.** `MS p4–5` reports the cluster-by-instance CI **−0.300 to −0.111** (correct; my recomputation is −0.2985 to −0.1129), the family-cluster CI **−0.234 to −0.163**, and the 15/16 sign test **p = 5.2 × 10⁻⁴** (correct; my recomputation is 5.19 × 10⁻⁴). The family-cluster bootstrap resamples **3 families**; a 95% interval from 3 units is not reliable. The sign test treats 20 instances as independent, but the eight `bur26` variants are highly correlated and several have identical outcomes across seeds.

**Why it matters.** The qualitative conclusion (BLS lower) survives, but the family-cluster interval and the sign-test p-value are stronger than the design supports. The paper already says the comparison is descriptive; the statistics should match that framing.

**Action.**
- Keep the cluster-by-instance interval as the primary descriptive summary.
- Drop the family-cluster interval or label it an informal sensitivity check with only 3 clusters, not a 95% CI.
- Replace the sign-test p-value with a family-stratified permutation test or a hierarchical model, or report the 15/16 count without a p-value.
- State that the panel is a convenience sample, not a random sample of QAPLIB.

### 4.5 Minor comments

- **m1.** Section title "QAP convergence panel and independent baseline" (`MS p4`) is misleading: BLS is a reimplementation by the same author, not an independent implementation. Use "separate" or "reimplemented" (`MS p7` already says "not the original authors' code").
- **m2.** Table 1's caption says "a 100,000-iteration or 100,000-move patience rule" and the text says "same declared move budget" (`MS p4`). State whether one tabu iteration equals one accepted swap and whether BLS moves include perturbation moves; if the budgets are only nominally matched, say so.
- **m3.** The abstract is 256 words (`MS p1`); confirm the JORS abstract limit. It also leads with 0.301/0.096 and 1.24, not the adapter/replay contribution.
- **m4.** Reconcile the word count: **3,798** (cover letter line 16, release notes), **3,815** (`README.md:21`), **3,801** (`detex -n paper2-jors.tex | wc -w`).
- **m5.** `MS p3` says "The TSP campaign ... all 20" — this is the four-instance deep panel (20 runs), not the 20-instance breadth panel. Say "all 20 deep-panel runs."
- **m6.** `MS p5` says `brazil58` is "about four times slower per kick than the larger `bier127`" and parenthesizes "explicit upper-row matrix," implying a cause that is not isolated. Say "we attribute this to the explicit-matrix path; we did not profile it," or add a profile.
- **m7.** `MS p7` says the internal LK exchange "lacks α-nearness, fractional cascading, and the full LKH gain criteria, **which is why** the larger tail is weak." This is a causal claim; use "we attribute" or "consistent with."
- **m8.** `MS p6` says the replay covers "1,060 broad incumbents" and "Twenty-five `esc8` parse-error records are skipped explicitly." State that the 25 are excluded from the denominator and why; the current sentence does not make the denominator explicit.
- **m9.** `MS p7` Data and code availability says "The harness ... are in the FRESH https://github.com/UBC-FRESH/fresh-solutions-papers" — the harness is in `fresh-solutions`; the papers repository contains the runners, evidence, and manuscripts. Fix the grammar and the link.
- **m10.** The data availability statement links the repository root, not the tagged release (`MS p7`; `paper2-jors.tex:429–430`). Link directly to the release tag.
- **m11.** The paper calls the release a "tag" and "public" but it is a **prerelease** (`gh release view` reports `isPrerelease: true`). Say "public prerelease" consistently and do not imply it is an archival tag.
- **m12.** The evidence is described as `paper2-evidence-v0.1.0` in the text but the public release is `p14-evidence-rc2`. Explain the relationship once, or use one label.
- **m13.** The `README.md` still says "Software repository: [repository URL to be supplied at release]" and "No claim is made that the artifact is public or archived" (`README.md:35–41`), while the manuscript claims public. Reconcile or remove the README from the submission package.
- **m14.** The cover letter says "the repository and DOI fields are placeholders until that release is approved" (`cover-letter.md:18–19`), but the release is already public. Update it.
- **m15.** The root `README.md` says "P14 release candidate 1 (`p14-evidence-rc1`)" while the paper cites rc2. Update.
- **m16.** `paper2/README.md` says BLS is stronger on **14** instance means; the manuscript says **15** (10-seed). Update.
- **m17.** PDF metadata is blank (Title, Author, Subject, Keywords) and the PDF is **US Letter** (612 × 792). Set `pdftitle`/`pdfauthor` via `hyperref` and confirm the JORS page size.
- **m18.** The supplement byline is "UBC FRESH Lab" while the main text is "Gregory Paradis." Align (`paper2-jors-supplement.tex:14`).
- **m19.** Terminology is inconsistent: "breadth panel," "expanded panel," "expanded-TSP," and "20-instance panel" are used interchangeably (`MS p1`, `p5`, `p6`). Pick one term and define it.
- **m20.** Table 1's family means are unweighted means of instance means; state this in the caption. The "All" row is run-level/equal-seed; clarify.
- **m21.** Table 2's depth-4 group includes `ch150` (n=150), which a reader may expect at depth 2 under an n-based rule. Add a footnote that the recorded depth is the legacy value, not the n-based rule.
- **m22.** `paper2/evidence/provenance-2026-11-03.json` has `"processor": "x86_64"` and the LKH provenance has a machine-specific `/srv/shared-data/...` path (`lkh-provenance.json:20`). Use the Xeon model and a portable command/placeholder.
- **m23.** The manifest includes `paper2/paper2-draft.md`, which says "INTERNAL DRAFT — NOT SUBMISSION-READY" and reports the old LKH 71/100 result (`paper2/paper2-draft.md:3`). Remove or update it before release; a reviewer browsing the manifest will see the stale draft.
- **m24.** The paper says "the candidate cannot be approved as an immutable tag" (`MS p6`; `paper2-jors.tex:383`). This is an internal release blocker; remove it from the manuscript and state the artifact status in the availability table.
- **m25.** The conclusion says "The next step ... is a pinned release with a DOI and tested container" (`MS p7`), which concedes the artifact is not ready. For JORS, the artifact should be ready at submission; frame these as future work only if the current artifact is otherwise complete.

---

## 5. Claim-to-evidence ledger

| Claim | Location | Evidence | Status |
|---|---|---|---|
| Tabu 0.301%, BLS 0.096% | `MS p1`, `p4`; Table 1 | `qap-expanded-100k-10seed-summary.json`, `qap-bls-10seed-summary.json` | **Supported** (0.30085, 0.09614). |
| Cluster-by-instance CI −0.300 to −0.111 | `MS p1`, `p4–5` | recomputed from per-run JSON | **Supported** (−0.2985 to −0.1129). |
| 15/16 sign test, p = 5.2 × 10⁻⁴ | `MS p5` | recomputed | **Supported**, but clustering caveat. |
| 94/100 TSP optima, 95/100 patience | `MS p1`, `p5`; Table 2 | `tsp-expanded-10k.json` | **Supported**, but mixed-depth and cap-limited. |
| 1.24 CPU ratio, CI 1.17–1.31 | `MS p1`, `p4`; Fig 2 | `framework-use-summary.json` | **Supported** against the private-array baseline. |
| Every record names CPU time | `MS p3` | QAP/TSP expanded: 0/300 `cpu_seconds` | **Not supported.** |
| Manifest does not cover 10-seed QAP | `MS p6` | Manifest includes both files; 66/66 hashes match | **Not supported.** |
| Evidence is not public | `MS p7` | Public `p14-evidence-rc2` release | **Not supported.** |
| Artifact is `p14-evidence-rc2` | `MS p1`, `p6` | Release asset says rc1; tag source says rc1 | **Not supported** (asset/tag mismatch). |
| QAPLIB/TSPLIB not redistributed | `MS p6` | 8 instance files in `paper2/instances/` | **Not supported.** |
| One-command replay | `MS p6` | `replay_all.sh` works, but recipe omits clone/install/submodule | **Partly supported.** |
| All 200 BLS replay | `MS p4`, `p6` | `replay_all.sh:12` uses `qap-bls-10seed.json`; release notes say 200/200 | **Supported.** |
| TSP depth disclosed | `MS p5` | 17/1/2 instances at depth 4/3/2; `max_depth` in records | **Supported**, but headline framing is not. |
| Tabu is "robust" | `MS p3`; Table 1 | 0/80 on `bur26`, seed-invariant outcomes | **Not supported** as a robust-tabu claim. |

---

## 6. Reviewer questions (Yes / No / N/A)

1. Does the manuscript fit JORS Issues in Research Software? **Yes, in principle** — it is an experience/reproducibility report on an evidence boundary. The current balance is too solver-comparison heavy.
2. Is the software contribution clearly described? **Yes** — adapter contract, resident state, replay gate, stopping taxonomy.
3. Is the artifact public and independently replayable? **No** — DOI placeholder, release asset rc1, contradictory availability statement, incomplete one-command recipe.
4. Are the headline numbers traceable to the evidence? **Mostly** — QAP/BLS/TSP/framework numbers match; manifest/CPU/schema claims do not.
5. Is the BLS inference appropriately clustered? **Partly** — cluster-by-instance interval is correct; family-cluster bootstrap (3 families) and sign test over correlated instances overstate precision.
6. Is the tabu baseline credible? **No** — 0/80 on `bur26` with near-optimal gaps suggests a trap/defect; not verified against published robust tabu.
7. Is the TSP protocol consistent? **No** — mixed-depth by design, disclosed; the 94/100 is descriptive, not controlled.
8. Is the manuscript within the length guidance? **Partly** — word count yes; page count no (9 vs 4–6).
9. Would I review a revision? **Yes.**

---

## 7. Risk table

| # | Risk | Likelihood | Impact | Evidence | Mitigation |
|---|---|---|---|---|---|
| R1 | Public release contains the wrong manuscript (rc1 vs rc2); the artifact cannot be cited as the version under review | High | High | Asset `p14-evidence-rc2/paper2-jors.pdf` SHA `5ae7c528…`, p6 says rc1; tag `5d75c04` says rc1; working PDF says rc2 | Re-tag/re-release from the submitted commit; verify PDF/tex hashes; add release check. |
| R2 | Availability section is self-contradictory; DOI placeholder | High | High | `MS p1`, `p6`, `p7`; `paper2-jors.tex:46, 353–354, 384, 431–432` | One availability table; one status per artifact; DOI or "assigned on acceptance." |
| R3 | Per-record CPU schema claim is false for QAP/TSP panels | High | High | `MS p3` vs `MS p6`; 0/200 + 0/100 `cpu_seconds` | Add CPU fields or scope the claim; remove "release blocker." |
| R4 | Manifest claim is false | High | Medium | `MS p6`; manifest includes 10-seed files; 66/66 hashes match | Delete claim; add hash check. |
| R5 | Tabu `bur26` 0/80 is an implementation artifact; BLS comparison not fair | High | High | Table 1; supplement; seed-invariant outcomes | Verify/diagnose or reframe as "tabu reference (not validated)." |
| R6 | TSP mixed-depth/cap-limited panel used as headline | High | Medium | `MS p5`; Table 2; 17/1/2 depth; 5 cap hits | Reframe as protocol-drift lesson or rerun under one rule. |
| R7 | JORS page guide (9 vs 4–6) and solver-paper balance | High | Medium | `README.md:24`; plan line 232; abstract/validation balance | Cut broad/LKH; shorten QAP/BLS; add lessons. |
| R8 | Provenance split across `7d3c831`/`4583ad3`/`c7d1507`; container wrong commit | Medium | High | Record fields; `container/Dockerfile:7`; README blocking issue 3 | One immutable replay commit; update records/container. |
| R9 | One-command replay not reproducible from a clean clone | Medium | High | `MS p6` snippet; `replay_all.sh` submodule import | Complete clone/install/submodule recipe; test clean clone. |
| R10 | Licence/redistribution statement wrong; 8 instances in repo | Medium | Medium | `MS p6`; `git ls-files`; `LICENSING.md` | Correct statement or remove instances; update licence. |
| R11 | Metadata missing (ORCID, CRediT, funding, competing interests) | Medium | Medium | `MS p1`; README:37–39 | Add before submission. |
| R12 | Family-cluster bootstrap/sign test overstate precision | Medium | Medium | `MS p4–5`; 3 families; correlated `bur26` | Drop/caveat family interval; stratify or drop p-value. |
| R13 | Stale README/cover letter/release notes | High | Low | `README.md:35–41`; `cover-letter.md:18–19` | Reconcile with manuscript. |
| R14 | PDF metadata/page size/supplement byline | Low | Low | `pdfinfo` blank; US Letter; supplement byline | Set metadata; confirm A4; align byline. |

**Top five risks (executive):**

1. **Release asset is the wrong manuscript** (R1): the paper cites rc2, but the release contains rc1. Mitigation: re-tag/re-release from the submitted commit and verify hashes.
2. **Availability is self-contradictory and DOI is a placeholder** (R2): the paper says both public and not public. Mitigation: one availability table, one status per artifact, DOI.
3. **Per-record CPU/manifest claims are false** (R3/R4): the schema and manifest statements do not match the evidence. Mitigation: add fields or scope the claims; delete the false manifest sentence.
4. **Tabu `bur26` credibility** (R5): 0/80 with seed-invariant outcomes undermines the QAP/BLS comparison. Mitigation: verify/diagnose or reframe the tabu as an unvalidated baseline.
5. **JORS length/focus and TSP headline** (R6/R7): 9 pages vs 4–6, and a mixed-depth panel used as a headline. Mitigation: cut and reframe; add a lessons section.

---

## 8. P0 / P1 / P2 list

### P0 — must fix before any submission

- **P0-1. Release asset/tag mismatch.** Re-tag and re-release from the exact submitted commit; ensure the `p14-evidence-rc2` asset and tagged source both say rc2 and match the submitted PDF (`MS p1`, `p6`; release asset; tag `5d75c04`).
- **P0-2. Availability/DOI.** Replace the contradictory prose with one availability table; remove "candidate rather than a candidate" and "not public or archived"; obtain/assign the DOI or state one consistent pending status (`MS p6`, `p7`; `paper2-jors.tex:46, 353–354, 384, 431–432`).
- **P0-3. Per-record CPU schema.** Either add `cpu_seconds` to the 300 QAP/TSP records or scope the `MS p3` claim; remove "release blocker" language (`MS p3`, `p6`; evidence JSON).
- **P0-4. Manifest claim.** Delete the false "manifest does not cover the ten-seed files" sentence; the manifest covers them and all 66 hashes verify (`MS p6`; manifest).

### P1 — major, affects validity/credibility

- **P1-1. Tabu `bur26`.** Verify/diagnose the 0/80 result or rename the tabu as an unvalidated reference; make BLS the primary QAP reference (`Table 1`; supplement; `MS p3–5`).
- **P1-2. TSP mixed depth.** Reframe the 94/100 as a descriptive protocol-drift result or rerun under one rule; remove it from headline status (`MS p1`, `p5`, `p7`; Table 2).
- **P1-3. JORS length/focus.** Cut to ~6–7 pages; reduce broad/LKH; shorten QAP/BLS; add a "Lessons" section; rewrite the abstract to lead with the adapter/replay contract (`MS p1`, `p4–6`; `README.md:24`; plan line 232).
- **P1-4. Provenance/container.** Choose one immutable replay commit; re-stamp records; update the Dockerfile; add a provenance table (`7d3c831`/`4583ad3`/`c7d1507`; `container/Dockerfile:7`).
- **P1-5. One-command replay.** Add clone/install/submodule/ layout instructions; test a clean clone; either remove the container claim or pin and test it (`MS p6`; `replay_all.sh`; `container/`).
- **P1-6. Licence/redistribution.** Correct the "not redistributed" claim; remove the 8 instance files or state their inclusion; update `LICENSING.md` to remove "not yet public" (`MS p6`; `paper2/instances/`; `LICENSING.md`).
- **P1-7. Metadata.** Add ORCID, CRediT, funding, competing interests, acknowledgements (`MS p1`; README:37–39).
- **P1-8. Stale package documents.** Reconcile `README.md`, `cover-letter.md`, root `README.md`, `paper2/README.md`, and release notes with the manuscript (`README.md:21, 35–41`; `cover-letter.md:16–19`).
- **P1-9. BLS wording/budget.** Rename "independent baseline" to "separate/reimplemented baseline"; state the budget equivalence (`MS p4`).

### P2 — minor/clarity

- **P2-1.** Family-cluster bootstrap with 3 families and sign test over correlated instances (`MS p4–5`).
- **P2-2.** Abstract length (256 words) and lead (`MS p1`).
- **P2-3.** Word-count discrepancy 3,798/3,801/3,815 (`README.md:21`; `cover-letter.md:16`).
- **P2-4.** Terminology: breadth/expanded/20-instance panel (`MS p1`, `p5`, `p6`).
- **P2-5.** Table captions: family means are unweighted; depth-4 `ch150` footnote (`Table 1`, `Table 2`).
- **P2-6.** Causal overclaims for `brazil58` and the LK tail (`MS p5`, `p7`).
- **P2-7.** Data availability grammar/link; harness vs papers repo (`MS p7`).
- **P2-8.** PDF metadata/page size; supplement byline (`pdfinfo`; `paper2-jors-supplement.tex:14`).
- **P2-9.** Portable provenance commands; remove `/srv/shared-data/...` (`lkh-provenance.json:20`).
- **P2-10.** Remove stale `paper2/paper2-draft.md` from the manifest/release (`manifest`; `paper2-draft.md:3`).
- **P2-11.** Add seeds (1–10, 1–5) and exact package versions to the main text (`MS p4–5`; `provenance-2026-11-03.json`).
- **P2-12.** Add a short "what the replay gate caught (and did not)" paragraph; the current text asserts the gate's value but reports no final invalid replay (`MS p3`).

---

## 9. Overall assessment

The paper is a genuine JORS-style experience report with a real software contribution and an unusually honest evidence culture. The adapter contract, replay gate, and stopping taxonomy are the right things to publish, and the negative results are appropriate for the venue if framed as lessons rather than rankings.

The current submission is not ready. The release does not contain the manuscript under review, the availability statement contradicts itself, the per-record schema and manifest claims are false, the tabu reference is not credible on `bur26`, and the TSP panel is mixed-depth yet used as a headline. These are fixable, but they are not formatting issues; they go to the paper's central claim of exact, replayable evidence.

I recommend **major revision**. After the P0/P1 fixes, a shorter, more experience-focused version would be a credible JORS paper.

---

## 10. QA checklist (before submission)

- **Evidence-only:** every substantive claim has a citation tag. Yes.
- **Anonymity/privacy:** no reviewer-identifying details; no third-party personal information beyond the materials. Yes.
- **Tone:** professional, constructive, inclusive. Yes.
- **Bias hygiene:** critiques anchored to the submission's content and evidence, not prestige or subfield preference. Yes.
- **Actionability:** each major comment names a file/page, why it matters, and a bounded action. Yes.
- **Venue fit:** the review assesses JORS Issues in Research Software, not JoH or SoftwareX criteria. Yes.
