# Reviewer report — Paper 1, SoftwareX target draft

**Manuscript:** “WS4: a compiled-state software architecture with exact replay for landscape harvest scheduling”
**Target venue:** SoftwareX, Original Software Publication (OSP)
**Review copy:** `paper/submission/softwarex/paper1-softwarex.pdf` (8 pages, 2 figures, 3 content tables + metadata table)
**Source:** `paper/submission/softwarex/paper1-softwarex.tex`
**Package:** `paper/submission/softwarex/README.md`, `paper/submission/softwarex/cover-letter.md`, `paper/evidence/`, `paper/release/manifest-v0.2.0-candidate.json`
**Public releases checked:** `p14-evidence-rc2` (papers repo), `ws4-v0.2.0-p14rc1` (WS4 repo), `ws4-tsa24-evenflow-v1` (TSA24 artifact)
**Review date:** 2026-11-11
**Reviewer stance:** independent, antagonistic Reviewer 2 / associate editor

**Recommendation:** **Major revision — not submission-ready.**
**Prepared to review after revision:** **Yes**, if the P0 items are resolved and the mandatory SoftwareX “Impact” section is substantive. If the impact case cannot be evidenced and the replay cannot be made to work from the public artifact, the paper should be re-targeted to JORS rather than submitted here.
**Confidence:** High on the factual, licence, provenance, replay, and word-count findings. Moderate on the journal-fit judgment; it rests on the official OSP template/guide and the submission’s own scope statements.

---

## Overrides and scope of this review

- The target journal’s official OSP template and author guide are part of the submission criteria named in the task and acknowledged in `README.md:26-32`. I use them only for section, metadata-table, and length compliance, not for scientific claims. The official OSP template requires five sections — Motivation and significance; Software description; Illustrative examples; Impact; Conclusions — and a C1–C9 metadata table whose left column must not be altered. The guide’s limit is 4,000 words excluding title/authors/affiliations/references/metadata tables, including abstract, running text, captions, and footnotes, with a maximum of six figures.
- All substantive praise and criticism is tied to the submission materials, the evidence records, the public releases, or the official template. I did not import literature or claims from outside those materials.
- Arithmetic was recomputed from the records and tables. All manifest hashes were recomputed. The public release metadata was read through the GitHub API. No manuscript or evidence file was edited. The only file created is this report.
- The review is written for the authors and editor. It contains no reviewer-identifying details and no third-party personal information.

### Evidence tag key

| Tag | Meaning |
|---|---|
| `MS pX` | Manuscript PDF page X |
| `MS pX l.Y` | Manuscript PDF page X, printed line Y |
| `Table N`, `Fig N` | Manuscript table/figure |
| `TEX <path>:line` | LaTeX source line |
| `EV <path>` | Evidence record or script in the repository |
| `ARTIFACT <path>` | TSA24 public artifact file |
| `REL <tag>` | Public GitHub release |
| `MANIFEST` | `paper/release/manifest-v0.2.0-candidate.json` |
| `NOTE <path>` | Project note or plan |
| `README`, `COVER` | Submission package files |

---

## Document inventory

| Material | Observation |
|---|---|
| `paper1-softwarex.pdf` | 8 pages, 2 figures, 3 content tables + 1 metadata table, 18 references. Two-column `elsarticle` review build, not the official OSP template (`README.md:26-32`). |
| `paper1-softwarex.tex` | 30,327 bytes. Title and author metadata are real; no `author@example.invalid`. |
| Counted words | `python3 count_words.py` gives **3,869** (main text + data availability). Including content-table bodies gives **3,978** by my count. `README.md:16-19` says **3,874** and **3,979**. The 5-word discrepancy is stale package metadata; the 3,978 figure leaves only 22 words under the cap. |
| Abstract | 172 words by my count; `README.md:24` says 173. Within the 250-word limit but above the template’s “ca. 100 words” suggestion. |
| `README.md` | Still lists author/email, tag/DOI, and private-evidence placeholders that the draft and public releases have partly resolved (`README.md:51-60`). |
| `cover-letter.md` | Still says the release is “being prepared” and the repository/tag/DOI fields are “placeholders” (`COVER:15-18`). This is false for the code and evidence releases, which are public. |
| `paper/evidence/` | Five JSON records; the campaign records and schedules live in `evidence/ws4-tsa24-*`. |
| `MANIFEST` | All 28 listed hashes match the current files, including the previously stale `factorized_ablation` hash. But `MANIFEST.status` still says “candidate; no tag/release created; public schedules/replay release pending.” |
| `REL p14-evidence-rc2` | Public prerelease, published 2026-11-11. **Assets are five PDFs only**; schedules, replay scripts, and JSON are in the tagged source tree, not the release assets. |
| `REL ws4-v0.2.0-p14rc1` | Public prerelease, no assets. Target is `feature/gpu-acceleration`; the release body says “feature-branch commit, not a merged main-branch release.” |
| `REL ws4-tsa24-evenflow-v1` | Public, non-prerelease, with a 4.66 MB `tar.gz` asset containing `compiled/`, `evenflow_tsa24.yaml`, and `seed_oldest_first_tsa24.csv`. |

---

## Evidence ledger (claim → evidence → status)

| Claim in the manuscript | Evidence | Status |
|---|---|---|
| 458,708 compiled blocks; 208,255 operable; 20 periods | `ARTIFACT compiled/blocks.parquet` (458,708 rows); `EV evidence/ws4-tsa24-gpu-ga-100000-r1/record.json` (`variables` = 208,255, `periods` = 20) | **Supported** |
| Initial objective 1,722,140,000 | `EV …r1/record.json` `initial_seed_objective` = 1,722,144,291.34; 6 s.f. rounding = 1,722,140,000 | **Supported** |
| Level equation `20 × 100 × (70M − mean)/70M` | `MS p3 Eq. (4), l.160-165`; recomputed for all six seeds against `realized_level_mean_m3`; matches to machine precision | **Supported; a genuine improvement over the EMS draft** |
| Realized level 51.21–52.49M | `EV …r1`–`…r5` `realized_level_min_m3`/`max_m3`; global min 51.2126M, global max 52.4897M | **Supported as a global min–max, but the level penalty uses the mean (51.89–52.06M), which is not reported** |
| Table 1 scaling (1,000 / 10,000 / 100,000) | `EV …1000-r7`, `…10000-r7`, `…100000-r7`; 1,000-gen objective is 8,588,725.37, displayed as 8,588,730 at 6 s.f.; times 9.38/23.1, 89.8/157, 856/942 | **Supported; 1,000-gen “search time” is `time_to_best_s`, not `search_seconds`, and the 100k seed-7 wall time is ~18% longer than the five campaign runs** |
| Five-seed objectives 512.574–518.621; mean 515.682; median 515.938 | `MS p5 Table 2`; `EV …r1`–`…r5`; recomputed mean 515.6818, median 515.938 | **Supported; table and arithmetic correct** |
| All five schedules replay exactly | `EV …r1`–`…r5` `exact_replay = true`; `replay.out` shows exact objective | **Supported by record flags, but not reproducible from the public artifact as documented (see M2)** |
| 2.00e3 evaluation-path speedup; error 3.7e-9 | `EV evidence/ws4-tsa24-eval-ablation.json`: 1.0863925/0.0005419086 = 2,004.75; absolute error 3.725e-9 | **Supported from unrounded values; the table’s rounded 1.09/0.542 ms gives 2.01e3, and the error has no reference scale** |
| 248× factorized batch; 1.71e-6 max error | `EV paper/evidence/tsa24-factorized-ablation.json`: 23.1237/0.0931495 = 248.24; both paths report 1.7136e-6 | **Supported as a 64-genome/4-cell batch; the “exact evaluator” reference is undefined and the CPU path also has nonzero error** |
| No independent harvest-scheduling comparison or LP/MIP bound | `MS p1`; `MS p6 l.406-409`; no such result in `paper/evidence/` | **Supported; honest and consistent** |
| “The GPU code is a feature-branch commit, not a tagged release” | `MS p6 l.419-420`; but `REL ws4-v0.2.0-p14rc1` is a tag on `feature/gpu-acceleration`, and `MS p4 l.248-249` cites that release candidate | **Not supported; internal contradiction** |
| MIT licence for repository code | `MS p7 Table 4, C3`; actual `LICENSE:1` and `pyproject.toml:12` are **Apache-2.0**; the release body also says MIT | **Not supported; factual licence error** |
| Public evidence release contains schedules and replay scripts | `MS p6 l.420-422`; `MS p7 l.458-460`; `REL p14-evidence-rc2` assets are PDFs only; scripts are in the tag’s source tree | **Partially supported; the release page does not expose the replay material** |
| “One-command replay” | `MS p7 Table 4, C8` (`bash paper/replay_all.sh`); `paper/replay_all.sh:3-4` requires `WS4_ROOT` and `TSA24_ROOT`; `EV …r1/replay.py:16-18` hard-codes `config/ws4/targets/evenflow_tsa24.yaml` and `build/compiled`, which are not in the public artifact | **Not supported as documented; the conclusion calls a tested one-command replay a “next step” (`MS p6 l.443-446`)** |
| Four failure modes exposed by the record gate | `MS p3 l.232-240`; but the gate “verifies the incumbent, not the search trajectory” (`MS p3 l.219-225`) and the record has no dataset/table hash | **Not supported for “irreversible move” and “model change without a table rebuild”** |
| “Without the optimizer binary” | `MS p6 l.396-400`; `EV …r1/replay.py:8-20` imports `ws4.opt.engine` and `Optimizer` | **Not supported as written; it does not rerun the search, but it needs the optimizer library** |
| “The even-flow target selects the flattest profile” | `MS p3 l.168-170`; target `ARTIFACT evenflow_tsa24.yaml:1-12` penalizes deviations outside a ±1% band; three of five seeds have flow term 0.000, and a fourth is 0.076 | **Not supported; within the band the target has no “flattest” gradient** |
| 70M is “deliberately unattainable” | `MS p4 l.270-274`; `ARTIFACT evenflow_tsa24.yaml:2` says 70M is “slightly above the 2025 AAC 6,917,231” | **Supported as an outcome, but the AAC provenance is omitted and the “deliberately unattainable” framing is misleading** |
| Official OSP template applied | `README.md:26-32` explicitly says it is **not** the official template; the five sections and metadata rows do not match | **Not supported** |

---

## Confidential comments to the editor

**Recommendation: major revision; do not send this to production in its current form.**

This is a materially better manuscript than the EMS version. The level equation is now correct and matches the records; Table 2 excludes seed 7 and its mean/median are right; the 54.9→54.8 s error is fixed; the invalid 22.2× matched-search timing table and claim are gone; and the packaging has real public releases. The authors have also kept a disciplined claim boundary: they do not claim a state-of-the-art solver, an independent baseline, or environmental validation.

The problem is that the draft is still a compressed research article, not a SoftwareX Original Software Publication. The journal’s mandatory **Impact** section — which the OSP template calls “the main section of the article” — is absent. The closest material is “Reuse potential and limitations” (`MS p6 l.372-428`), which is prospective and largely a limitations list, not a case for impact with users, adoption, citable use, or changed practice. The paper’s own scope (“not a leaderboard entry,” “not a competitive solver,” `MS p6 l.447-450`) makes that case harder, not easier. The official template also requires “Illustrative examples”; the draft’s “Validation and illustration” (`MS p3-p5`) is a results section, not a usage example. A template swap will not fix this; it needs a structural rewrite.

There are also factual and packaging errors that would be embarrassing in production:

1. **Licence is wrong.** The metadata table says “MIT for repository code” (`MS p7 Table 4, C3`), but the WS4 repository at the release tag is **Apache-2.0** (`LICENSE:1`; `pyproject.toml:12`; `REL ws4-v0.2.0-p14rc1` body also says MIT, repeating the error). SoftwareX requires an approved licence and an accurate metadata table; this is a hard error.
2. **The replay claim does not survive contact with the public artifact.** The manuscript says the schedules and replay scripts are in the public evidence release and gives `bash paper/replay_all.sh` (`MS p6 l.420-422`; `MS p7 l.458-460`; Table 4 C8). The release assets are five PDFs; the scripts are in the tag’s source tree. Worse, `replay.py` hard-codes `config/ws4/targets/evenflow_tsa24.yaml` and `build/compiled` (`EV …r1/replay.py:16-18`), while the public artifact ships `evenflow_tsa24.yaml` and `compiled/` at its root (`ARTIFACT`; tarball listing). A reader who downloads the artifact cannot run the replay without undocumented symlinks. The conclusion then lists “a tested one-command replay” as a next step (`MS p6 l.443-446`), contradicting the metadata table and the release notes. This is the paper’s central contribution; it cannot be this loose.
3. **Provenance is contradictory.** The paper cites `ws4-v0.2.0-p14rc1` (`MS p4 l.248-249`; Table 4 C1–C2) but says “the GPU code is a feature-branch commit, not a tagged release” (`MS p6 l.419-420`); reference [17] still says “commit f60ce64” (`MS p8 l.545-547`); `MANIFEST.status` says no release was created; `README.md:51-60` and `COVER:15-18` still describe private/placeholder releases. These are stale statements from before the 2026-11-11 release, but they are in the submission.
4. **Template/metadata non-compliance.** The metadata table is not the official C1–C9 table: it repurposes C3 as “Legal code licence” and omits the required “Permanent link to Reproducible Capsule”; C4–C7 are shifted by one; C8 is a test/replay command instead of the documentation link. The caption still says “Placeholders must be replaced before submission” (`TEX:478`), an instruction that should have been deleted. The paper is built in two-column `elsarticle`, not the single-column OSP template (`README.md:26-32`).
5. **The word budget cannot absorb the missing section.** The draft is 3,869 words by the package’s counter and 3,978 including content-table bodies. The official cap is 4,000 excluding references and metadata tables but including abstract, running text, captions, and footnotes. A substantive Impact section plus an Illustrative example will add several hundred words; the draft is already at 99.5% of the cap. The current structure spends ~2 pages on validation/microbenchmarks and ~1 page on reuse/limitations; it needs a cut plan before it can be a compliant OSP.

My recommendation is therefore **major revision**, with a real risk of rejection if the Impact section is treated as a relabeling exercise. The software is a credible SoftwareX candidate; the manuscript is not yet a SoftwareX manuscript.

---

# Comments to the authors

## Summary

The draft describes WS4, a compiled-state architecture for landscape harvest scheduling, and illustrates it on one frozen TSA24/Prince George instance with a five-seed 100,000-generation GPU campaign and exact CPU replay. It is candid about its limits, and several P0 issues from the earlier review are genuinely fixed. It is not, however, ready for SoftwareX: the mandatory Impact section is missing, the paper reads as a compressed validation article rather than a software note, the replay scripts do not run from the public artifact as documented, the licence is stated incorrectly, the metadata table is not the official table, and the word count leaves no room for the missing section. The software is publishable at SoftwareX after a structural rewrite and a packaging pass; the current package is not.

---

## What the draft does well

These are real strengths, and they should survive the rewrite.

1. **The level equation is now correct and evidence-consistent.** `MS p3 Eq. (4), l.160-165` gives `ℓ = 20 × 100 × (70M − v̄)/70M`. I recomputed it for all six seeds from `realized_level_mean_m3`: seed 1 gives 517.2904166, seed 2 512.5741387, seed 3 515.9377175, seed 4 514.7459646, seed 5 516.4541810, seed 7 515.1408611. The equation matches to machine precision. The draft also correctly says the level term is dimensionless and not a per-period hard floor. This was the most serious definitional problem in the EMS draft; it is fixed.
2. **Table 2 is internally correct and no longer mixes seed 7 into the five-seed statistics.** The mean 515.682 and median 515.938 are correct for seeds 1–5; flow + level = objective for every row; seed 7 is explicitly excluded (`MS p5 Table 2`; `MS p4-p5 l.306-326`). This is a clean table.
3. **The claim boundary is disciplined.** The abstract, introduction, results, and conclusions all say there is no independent harvest-scheduling comparison, no state-of-the-art claim, and no environmental-modelling claim (`MS p1`; `MS p2 l.42-43`; `MS p5 l.366-371`; `MS p6 l.442-450`). The factorized and evaluation-path results are labeled as bounded microbenchmarks (`MS p5 l.352-357`). This is better practice than most submissions.
4. **The record and replay design is coherent in principle.** The distinction between search reproducibility and result replayability (`MS p4 l.226-242`), the “record the CPU replay objective, not the device objective” rule (`MS p3 l.206-210`), and the “gate verifies the incumbent, not the trajectory” caveat (`MS p3 l.219-225`) are exactly the right design instincts.
5. **The evidence hashes now match the manifest.** I recomputed all 28 hashes in `MANIFEST`; every one matches, including `factorized_ablation`, which was stale in the EMS package. The underlying records are well structured and the campaign schedules are present in `evidence/`.
6. **The public TSA24 artifact is real.** `REL ws4-tsa24-evenflow-v1` is a public, non-prerelease artifact with a 4.66 MB `tar.gz`; it contains 458,708 blocks, the target YAML, and the initial seed (`ARTIFACT`; `EV …r1/record.json`). The data are not the weak point.

---

## Major comments

### M1. The paper does not meet SoftwareX’s mandatory Impact requirement

**Claim.** SoftwareX’s OSP template requires five sections: Motivation and significance; Software description; Illustrative examples; Impact; Conclusions. The draft has Motivation and significance; Software description; Validation and illustration; Reuse potential and limitations; Conclusions. There is no Impact section.

**Evidence.** `MS p3` begins “3. Validation and illustration”; `MS p6 l.372` begins “4. Reuse potential and limitations”; `MS p6 l.429` begins “5. Conclusions.” The official OSP template’s section 4 is “Impact,” and the template says: “This is the main section of the article and reviewers will weight it appropriately.” The template asks for new research questions, improvements to existing research, changes in daily practice, widespread use (downloads, users, citable publications), and commercial/spin-off use. The draft’s closest material is `MS p2 l.44-48` (“The intended users are groups with a compiled spatial model…”) and `MS p6 l.372-400` (“The architecture is reusable when…”). Neither cites a user, a citable publication using WS4, a download count, a teaching use, or a commercial setting. The conclusion says “not a leaderboard entry” and “not a competitive solver” (`MS p6 l.447-450`), which further undercuts an impact claim.

**Why it matters.** This is not a formatting issue. SoftwareX publishes software because of its (proven) potential impact; the Impact section is the journal’s central review criterion. A paper that describes an architecture and reports a single-landscape validation, but does not argue impact, is a research article compressed to eight pages. The editor can desk-reject on this alone, and a reviewer who applies the OSP template will mark the submission incomplete.

**Action.** Add a real Impact section, not a relabeled “Reuse potential.” It should make the strongest honest case available: who can use WS4, what they can do that they could not do before, what the replay contract changes for reviewers/archivists/instructors, and what the TSA24 case demonstrates about the software’s reach. If there are no external users or citable publications yet, say so and argue *potential* impact concretely: the public artifact, the exact replay, the adapter pattern, the ability to swap search layers, and the teaching value of an inspectable exact incremental evaluator. Cite the artifact and the release, and give at least one concrete workflow. If the authors cannot make that case without overclaiming, SoftwareX is the wrong venue and JORS is the better target.

---

### M2. The “public replay” claim is not delivered: the scripts do not run from the public artifact, and “one-command” is not one command

**Claim.** The manuscript says the paper-specific schedules and replay scripts are in the public evidence release (`MS p6 l.420-422`; `MS p7 l.458-460`), that a reader can obtain the same blocks/target/initial schedule (`MS p4 l.276-278`), and that the metadata table gives a replay command (`MS p7 Table 4, C8`). It also says the next step is “a tested one-command replay” (`MS p6 l.443-446`). These statements cannot all be true.

**Evidence.**
- `REL p14-evidence-rc2` is public, but its release assets are **five PDFs only** (`paper1-manuscript.pdf`, `paper1-softwarex.pdf`, `paper2-*.pdf`). The schedules, `replay.py` files, and JSON are in the tagged source tree, not the release assets. A reader who downloads the release assets does not get the replay material.
- `paper/replay_all.sh:3-4` requires `WS4_ROOT` and `TSA24_ROOT`; it is not a one-command replay from a clean clone.
- `EV evidence/ws4-tsa24-gpu-ga-100000-r1/replay.py:16-18` hard-codes `INSTANCE / "config/ws4/targets/evenflow_tsa24.yaml"` and `INSTANCE / "build/compiled"`. The public artifact ships `evenflow_tsa24.yaml` and `compiled/` at its root; its `BENCHMARK_ARTIFACT.md` “GPU rebuild” recipe uses `$TSA24_ROOT/compiled` and `$TSA24_ROOT/evenflow_tsa24.yaml`. There is no `config/ws4/targets/` or `build/compiled/` in the public artifact or in the tracked public `femic-tsa24-instance` tree (`ARTIFACT` tarball listing; public repo tree).
- The conclusion says “The next steps are a DOI and a tested one-command replay” (`MS p6 l.443-446`), which contradicts the metadata table’s replay command and the release note’s claim that the public clone passes `paper/replay_all.sh`.

**Why it matters.** The paper’s central contribution is the replay contract. If a reader cannot run the replay from the public artifact as documented, the contract is a design, not a delivered result. The current mismatch is exactly the kind of failure the paper claims to prevent.

**Action.** Make the replay path work from the public artifact. Either parameterize the replay scripts to accept `compiled/` and `evenflow_tsa24.yaml` at the artifact root, or ship a small adapter/symlink script and document it. Replace “one-command” with the exact command and the two environment variables, and show the expected output. Put the replay scripts and schedules in the release assets, not only the tag tree, or state explicitly “download the source archive at tag p14-evidence-rc2.” Remove “tested one-command replay” from the conclusion if it is already tested, or remove the C8 replay claim if it is not. Reconcile the release note, manifest, README, and cover letter with the public state.

---

### M3. The licence is wrong, and the metadata table is not the official table

**Claim.** The metadata table states “MIT for repository code” and “the TSA24 artifact retains its own public terms” (`MS p7 Table 4, C3`). The official OSP table expects C3 = “Permanent link to Reproducible Capsule,” C4 = “Legal Code License,” C5 = versioning, C6 = languages/tools, C7 = compilation, C8 = documentation, C9 = support email.

**Evidence.** `LICENSE:1` is “Apache License, Version 2.0”; `pyproject.toml:12` is `license = "Apache-2.0"`; the `ws4-v0.2.0-p14rc1` release body also says “Licence: MIT for repository code,” repeating the error. The TSA24 artifact’s own terms are MIT for code/documentation, CC BY 4.0 for derived benchmark artifacts, and OGL-BC for source data (`ARTIFACT BENCHMARK_ARTIFACT.md`, “Licence”). The draft’s C3 does not distinguish these. The metadata table’s C3 is a licence row, not a capsule; C4–C7 are shifted by one; C8 is a test/replay command, not a documentation link. The caption still says “Code metadata (mandatory). Placeholders must be replaced before submission” (`TEX:478`), an instruction the official template says to delete.

**Why it matters.** SoftwareX requires an approved licence, an accurate metadata table, and a reproducible capsule/DOI. A wrong licence is a factual error, not a style issue; it can delay or block production. The stale placeholder caption signals that the manuscript is a draft, which is exactly what an editor should not see.

**Action.** Change C3 to the actual code licence, **Apache-2.0**, and state the artifact terms separately (MIT for artifact code/docs; CC BY 4.0 for derived benchmark artifacts; OGL-BC for source data). Rebuild the table to the official C1–C9 layout, including C3 “Permanent link to Reproducible Capsule” (or state “not yet available” honestly). Move the test/replay command into the Data and code availability section and use C8 for the documentation link. Delete the placeholder sentence. If a DOI/Zenodo capsule does not exist, say so in the table and in the Data availability statement; do not imply a permanent archival link that does not exist.

---

### M4. Provenance is contradictory across the manuscript and the package

**Claim.** The paper cites the release candidate `ws4-v0.2.0-p14rc1` (`MS p4 l.248-249`; `MS p7 Table 4, C1-C2`) but also says “The GPU code is a feature-branch commit, not a tagged release” (`MS p6 l.419-420`). Reference [17] still says “commit f60ce64” (`MS p8 l.545-547`). `MANIFEST.status` says “candidate; no tag/release created; public schedules/replay release pending.” `README.md:51-60` and `COVER:15-18` still describe private/placeholder releases.

**Evidence.** `REL ws4-v0.2.0-p14rc1` is a public prerelease tag on `feature/gpu-acceleration`; its body says “feature-branch commit, not a merged main-branch release.” So the code is tagged, but not merged to main. The manuscript’s “not a tagged release” is false; “not a merged main-branch release” would be true. The manifest was not updated after the release; it still says no release. The README says the evidence release is “currently private” and the draft cites `f60ce64` on a feature branch, both stale. The cover letter says the release is “being prepared” and the fields are “placeholders,” both stale.

**Why it matters.** A SoftwareX reviewer will click the links and compare them with the metadata. Contradictory provenance is a credibility problem even when the underlying artifact is good. The paper’s own thesis is that identity and replay matter; the package should model that discipline.

**Action.** Pick one provenance statement and use it everywhere: “WS4 `ws4-v0.2.0-p14rc1`, a public prerelease tag on `feature/gpu-acceleration` at commit `f60ce64`, not a merged main-branch release.” Update [17] to include the tag and commit. Update `MANIFEST.status`, `README.md`, `cover-letter.md`, and `RELEASE-CANDIDATE.md` to the public state. State whether the run used the public artifact’s `compiled/` tables or a byte-identical local build, and add the dataset/table hash to the record. The 1,000-generation record says “Local fixture, not a public dataset,” and the campaign records say “Local compiled build is derived,” while the paper says “public frozen artifact” (`EV …1000-r7/record.json`; `EV …r1/record.json`; `MS p4 l.260-262`); reconcile that.

---

### M5. The word count and section structure leave no room for the missing Impact section

**Claim.** The draft is 3,869 words by `count_words.py` and 3,978 including content-table bodies. The official cap is 4,000 words excluding references and metadata tables but including abstract, running text, captions, and footnotes. The draft is at 99.5% of the cap while missing two mandatory sections (Impact and a true Illustrative examples section).

**Evidence.** `python3 count_words.py` gives `main text + captions: 3827`, `data availability: 42`, `total counted: 3869`. My count including the three content-table bodies and excluding equations gives 3,978; including equations gives 4,020. `README.md:16-19` says 3,874 and 3,979. The official template requires five sections; the draft has “Validation and illustration” and “Reuse potential and limitations” instead of “Illustrative examples” and “Impact.” The current §3 is ~2 pages of results (`MS p3-p5`); §4 is ~1 page of reuse/limitations (`MS p6 l.372-428`).

**Why it matters.** The authors cannot simply apply the template and add an Impact section; the paper will exceed the cap. A compliant OSP needs a cut plan, not a formatting pass. The current paper is also 8 pages in two-column mode; the official single-column template will make it look longer, even if the word count is the binding constraint. The margin is 21–22 words depending on whether the README’s 3,979 or my 3,978 is used; either is too thin for a section that must argue impact.

**Action.** Before rewriting, decide what the software paper is *for* and cut accordingly. A workable plan: keep the architecture (short), one illustrative TSA24 example with the five-seed table and exact replay, and a real Impact section; move the 1,000/10,000/100,000 scaling table, the factorized 248× microbenchmark, and the 5,000-block evaluation diagnostic to the repository/supplement or compress them to a short paragraph. The paper’s current validation material is more than a software note needs. Re-run `count_words.py` after the rewrite and add the content-table bodies to the count; do not rely on a 21–22-word margin. Update `README.md` to the final count.

---

### M6. The objective description is better but still incomplete: no mean level, no flow equation, an unsupported “flattest” claim, and a hidden AAC provenance

**Claim.** The draft describes the level term as a normalized mean-level penalty (`MS p3 l.160-165`) and the even-flow target as a squared deviation outside a ±1% band (`MS p3 l.156-159`). It says “The even-flow target selects the flattest profile at the level where the two roles reach their best weighted compromise” (`MS p3 l.168-170`). It reports the realized level only as a per-seed min–max range (`MS p5 Table 2`), not the mean that drives the penalty.

**Evidence.**
- The target file defines the flow target with `flow_reference_period: 1`, `minimum: -1.0`, `maximum: 1.0`, weight 10,000, and 20 separate per-period level targets with `minimum: 70000000.0`, weight 100, `normalization: auto` (`ARTIFACT evenflow_tsa24.yaml:1-12` and following). The paper never states that the reference period is period 1, and it never gives the flow penalty equation.
- The level term is algebraically the sum of 20 per-period linear penalties; the paper’s “mean” equation is correct as an aggregate, but it does not say the implementation sums 20 per-period targets. A reader may think there is one target on the mean.
- The table reports `realized_level_min_m3`/`max_m3` per seed; the means are 51.8948, 52.0599, 51.9422, 51.9839, 51.9241, 51.9701M for seeds 1–5 and 7 (`EV …r1`–`…r7`). The headline level term cannot be checked from Table 2 without solving Eq. (4).
- The target file’s header says 70M is “slightly above the 2025 AAC 6,917,231.” The paper calls it “deliberately unattainable” (`MS p4 l.270-274`) but never says it is the AAC or why 70M was chosen. That omission makes the 52M outcome look like an arbitrary target gap rather than a policy-relevant result.
- The “flattest profile” claim is not supported by a ±1% band penalty: within the band, the flow term is zero for three of five seeds (seed 5 is 0.076) (`MS p5 Table 2`), so the target does not create a “flattest” gradient there. The level term, not the flow target, drives the mean.

**Why it matters.** The objective is the central quantitative result. A reader must be able to reproduce the flow and level terms, and must know that the level penalty uses the mean, not the range. The AAC provenance is also the strongest available interpretation of the 52M result; omitting it weakens the paper’s relevance.

**Action.** Add the flow penalty equation and state the reference period (period 1). State that the implementation has 20 per-period level targets whose sum is Eq. (4), or say “the aggregate is equivalent to a mean-level penalty.” Add the mean realized level to Table 2 (and the abstract, if the range stays). State the 70M provenance: “the 2025 AAC is 6,917,231 m³/year; the target is 70M m³ per 10-year period, slightly above it.” Then interpret the 52M outcome honestly: the optimized estate meets the even-flow band but falls short of the AAC by ~18M m³ per period. Remove “selects the flattest profile” unless a profile figure shows it; say “the even-flow target penalizes deviations outside the ±1% band, and the level target pulls the mean upward.”

---

### M7. The “four failure modes” claim is not supported by the replay gate, and “without the optimizer binary” is not accurate

**Claim.** The paper says “Four failure modes are exposed: a model change without a table rebuild, an irreversible move, a reported device objective, and a partial or infeasible schedule. None is silent in a record that passes the gate” (`MS p3 l.232-240`). It also says a future reader can verify the objective “without the optimizer binary or the original GPU” (`MS p6 l.396-400`).

**Evidence.** The paper itself says “The replay gate ... verifies the incumbent, not the search trajectory” (`MS p3 l.219-225`). A gate that reads only the final assignment and the stored objective cannot detect an irreversible move in the search; that is a search-time apply/undo invariant, not a replay-gate check. The record schema has `instance.id` and `algorithm.version` but no dataset/table hash (`EV …r1/record.json`), so a model change without a table rebuild is not necessarily detectable by the gate. The replay path imports `ws4.opt.engine` and `Optimizer` (`EV …r1/replay.py:8-20`), so it does need the optimizer library; it does not need the GPU or a search rerun. The paper’s wording conflates “does not rerun the search” with “does not need the optimizer.”

**Why it matters.** The “evidence boundary” is the paper’s main conceptual contribution. Overstating what the gate catches undermines the very discipline the paper advocates. A reviewer who reads the record schema will see the gap.

**Action.** Distinguish the checks: the replay gate catches a reported device objective and a partial/infeasible schedule; apply/undo invariants catch irreversible moves during search; a table/dataset identity check catches a stale table. Add the dataset/table hash to the record and the validator, or soften the “four failure modes” sentence. Say “without rerunning the search or using the GPU,” not “without the optimizer binary.” Add the duplicate-run determinism evidence from `EV …10000-r7/record.json` (“Two independent runs produced the identical schedule SHA-256”) to support the search-reproducibility claim; the paper currently asserts reproducibility without showing that check.

---

### M8. The validation is honest but does not demonstrate the software’s distinguishing feature or its impact

**Claim.** The paper validates one landscape, one target, one 20-period horizon, with no spatial constraints and no independent baseline (`MS p6 l.401-409`). It says the architecture is reusable and that spatial structure is part of the model, but the reported run does not exercise adjacency, opening-size, or road-access constraints.

**Evidence.** `MS p6 l.403-406`: “The reported run has no hard adjacency or opening-size constraints, so the software is not validated on the spatial-constraint case that motivates much of the literature.” `MS p6 l.406-409`: “There is no independent harvest-scheduling model or LP/MIP bound on the same instance, so the objective values are not a competitive quality result.” The software repository’s own contract says “Spatial structure is part of the model, not a post-processing step” and “Fragments compile; blocks aggregate” (`NOTE ws4/AGENTS.md`). The paper’s illustrative example does not test that claim.

**Why it matters.** For SoftwareX, the illustrative example should demonstrate the software’s major functions. If the software’s distinctive feature is spatial structure, an example without spatial constraints does not demonstrate it. The paper can still be a software paper, but it must either add a spatial-constraint case or make the limitation central to the Impact/Illustrative examples sections. The absence of a baseline is acceptable if the paper is explicit that the example is a functionality/replay demonstration, not a quality result; the current abstract still leads with the objective range, which invites the quality reading.

**Action.** If feasible, add a small adjacency or opening-size case (even a stress instance) to the illustrative example, or a second landscape. If not, reframe §3 as “Illustrative example: exact replay on a public instance” and move the quality-shaped numbers (512–518) out of the abstract’s first sentence. State explicitly that the example demonstrates the compiled boundary, the sparse effect table, and the replay gate, not schedule quality. The Impact section can then argue that the replay/architecture is the reusable contribution, with the single-landscape validation as a worked example.

---

## Minor comments

### Abstract, title, and front matter

1. `MS p1`: The abstract leads with “a 100,000-generation five-seed campaign reaches 512.574–518.621 (mean 515.682)” before saying there is no independent comparison. The number is target-specific and not a quality result. Lead with the software capability and replay contract; move the objective range to the illustrative example, or state “on one public instance, under a deliberately unattainable level target” in the same sentence.
2. `MS p1`: “The level penalty is a normalized mean-level term, not a per-period floor: the realized level ranges from 51.21 to 52.49M…” The range is a global min–max across seeds and periods; the penalty uses the mean. Report the mean (51.89–52.06M) or say “per-period range across the five seeds.”
3. `MS p1`: “A 5,000-block diagnostic reduces move-evaluation time by 2.00×10^3” — say “warm whole-schedule move evaluation” and “per move,” or a reader may think it is a full-instance simulation.
4. `MS p1`: “a 64-genome factorized batch runs 248 times faster on CUDA than on a single-device CPU path” — add “4-cell batch evaluation” so the scope is in the abstract, not only the body.
5. `MS p1`: The title is defensible and does not overclaim. Do not add “GPU speedup” or “state-of-the-art.”
6. `MS p1`: The abstract is 172 words; the OSP template suggests ca. 100. This is not a hard limit (250), but a shorter abstract would leave room for the Impact section.

### Introduction and related work

7. `MS p1-p2`: The related work cites search-method studies (simulated annealing, tabu/GA, eight heuristics) but no existing harvest-scheduling software. For a SoftwareX paper, the reader needs to know what software this replaces or extends. Add a short paragraph on existing systems (commercial or open-source) and state the distinction without a prestige claim.
8. `MS p2 l.44-48`: “The intended users are groups with a compiled spatial model…” is the only impact statement. It is hypothetical. Move it to the Impact section and make it concrete.
9. `MS p2 l.57-62`: The CPU-refinement handoff is “designed but is not part of the measured campaign.” This is honest, but it adds words and may confuse the illustrative example. Either cut it or label it clearly as future work in the Impact/limitations section.
10. `MS p4 l.268-269`: “its objective is 1,722,140,000, dominated by even-flow deviations” — the initial flow/level split is not reported. Either report it or say “the initial objective is dominated by flow” without the unsupported split.

### Software description

11. `MS p2 l.102-103`: “The index is smaller than the full cross-product but richer than a binary harvest decision.” The record has `options: 50,096,749`; report the candidate index size and the per-block distribution. This is the kind of concrete software detail SoftwareX readers expect.
12. `MS p2-p3 l.139-156`: The effect table’s build time, storage size, and nonzero count are not reported. Only the factorized build (234 s) appears. Report the full table’s size/build/nonzeros, or state that they are in the repository.
13. `MS p3 l.156-159`: The flow reference period is period 1 per the target file; state it. Give the flow penalty equation or a precise formula.
14. `MS p3 l.160-165`: The level term is the sum of 20 per-period linear penalties; say so, or a reader will think there is one target on the mean. The equation itself is correct.
15. `MS p3 l.168-170`: “selects the flattest profile” is not supported by a ±1% band. Remove or support with a 20-period profile figure.
16. `MS p3 l.194-196`: “The replay contract applies to the final assignment, not the move decomposition” is good; make sure the “four failure modes” paragraph does not contradict it (M7).
17. `MS p4 l.249-252`: The command-line surface is described in one sentence, but there is no example command, config snippet, or output. SoftwareX’s Illustrative examples section needs at least one. Add a short `gpu-run`/replay example (the `BENCHMARK_ARTIFACT.md` recipe is a good start).
18. `MS p4 l.253-257`: “The large GPU effect table and caches are not part of the small public dataset artifact; they are rebuilt from the published recipe.” Good; give the recipe URL/path and the expected build time/size.
19. `MS p4 l.245-249`: The environment lacks the CUDA version, PyTorch version, driver, and CPU RAM. For a software paper that reports 248× and 856 s, state them or point to a lockfile/container.

### Validation and illustration

20. `MS p4 l.260-262`: “The case study uses the public frozen artifact ws4-tsa24-evenflow-v1.” The 1,000-generation record says “Local fixture, not a public dataset,” and the campaign records say “The local compiled build is derived” (`EV …1000-r7/record.json`; `EV …r1/record.json`). State whether the run used the artifact’s `compiled/` tables or a byte-identical local build, and give the dataset/table hash.
21. `MS p4 l.270-274`: The 70M target is the 2025 AAC plus ~1.2% (`ARTIFACT evenflow_tsa24.yaml:2`), not an arbitrary aspiration. State the provenance; it makes the 52M gap interpretable.
22. `MS p5 Table 1`: The 1,000-gen objective is 8,588,725.37, displayed as 8,588,730 at 6 s.f.; the flow+level components are independently rounded and sum to 8,588,729.821. Add a note that rows are independently rounded, or report one more digit. The 1,000-gen “search” time is `time_to_best_s`, not `search_seconds`; label it accordingly.
23. `MS p5 Table 1`: The 100k seed-7 wall time (942 s) is ~18% longer than the five campaign runs (~798 s) and its memory is 8.26 GB vs 9.0 GB. The paper does not explain the difference. Either use a campaign run for the scaling row or state that seed 7 is a different configuration/run.
24. `MS p5 Table 2`: Add a mean realized level column. The min–max ranges are useful but do not let a reader check the level term.
25. `MS p5 Table 2`: The five-seed spread is called “small” without a standard deviation. Add SD (≈2.23) or say “descriptive range 6.05 objective units (1.2% of the mean).”
26. `MS p5 Table 3`: The displayed 1.09 s / 0.542 ms gives 2.01e3, not 2.00e3. Report 1.086 s and 0.5419 ms, or say “about 2.0×10^3 computed from unrounded values.”
27. `MS p5 Table 3`: The “Error” column has no units or reference scale. The 5,000-block objective is 10,942,260.80; the relative error is ~3.4×10^-16. Say “absolute error 3.7×10^-9 on a 1.09×10^7 objective” or add a relative-error column.
28. `MS p5 l.331-332`: “the first 5,000 blocks” — the evidence scope says “5000-block subset,” not “first.” State the selection rule (block ID order? spatial?) and why it is not random. The paper already says it is not a random sample; give the ordering.
29. `MS p5 l.344`: “the same 64-genome batch” — there is no prior 64-genome batch in the paper. Say “a 64-genome batch.”
30. `MS p5 l.349-350`: “maximum absolute error against the exact evaluator is 1.71×10^-6 on both paths” — if the CPU path is the exact evaluator, its error should be zero. Name the reference evaluator, give the objective scale, and explain why both paths have the same nonzero error. The evidence has `exact_max_error` for both CPU and CUDA, so the reference is a third evaluator; say so.
31. `MS p5 l.369-371`: “The retained CPU simulated-annealing run is untuned…” — the paper no longer describes that run. Either cut the sentence or explain what “retained” refers to.
32. `MS p5 l.366-371`: “They do not establish a controlled architecture-versus-implementation effect…” Good; keep this. It is the right caveat for the 248×/2.00e3 numbers.

### Reuse, limitations, conclusions

33. `MS p6 l.372-400`: “A team with a fast heuristic but no replay contract can wrap the heuristic in the adapter” — the adapter interface is not described in §2. Either describe the adapter contract or remove the claim. A reader cannot implement a component the paper does not define.
34. `MS p6 l.396-400`: “without the optimizer binary or the original GPU” — the replay imports `ws4.opt.engine`; say “without rerunning the search or using the GPU.”
35. `MS p6 l.401-409`: The limitations are clear, but the paper still leads with a target-specific objective. Move the “not a competitive quality result” caveat into the abstract or the first paragraph of §3.
36. `MS p6 l.419-422`: “The GPU code is a feature-branch commit, not a tagged release” — false; there is a public prerelease tag. Say “a public prerelease tag on a feature branch, not a merged main-branch release.”
37. `MS p6 l.443-446`: “The next steps are a DOI and a tested one-command replay” — contradicts C8 and the release note. Reconcile.
38. `MS p6 l.447-450`: “not a leaderboard entry… not a competitive solver” is honest but reads as a disclaimer. In the Impact section, say what the software *does* enable, not only what it does not claim.
39. `MS p7 Table 4, C1-C2`: C1 says “public prerelease”; C2 links to the release tag. Fine, but a final version/DOI is preferable. C3 is wrong (M3); C4–C7 are shifted by one and C8 is an extra test/replay row where the official table expects the documentation link.
40. `MS p7 Table 4, C6`: “multi-gigabyte memory (9.27 GB peak in the factorized batch)” — the campaign used 9.0 GB; state the minimum GPU memory and the CUDA/PyTorch versions.
41. `MS p7 Table 4, C7`: “Link to developer documentation: https://github.com/UBC-FRESH/ws4” — that is the repository root, not documentation. Point to `docs/` or the docs site.
42. `MS p7 Table 4, C8`: “Test command: python -m pytest; replay: bash paper/replay_all.sh” — no working directory, install step, or environment variables. Make it runnable (M2).
43. `MS p7 l.458-461`: “a DOI remain pending” — grammar: “remains.” Also, the sentence says the schedules are in the public release and then says a DOI is pending; clarify that the release is a prerelease, not an archival DOI.
44. `MS p7 l.453-457`: The data availability URL wraps awkwardly (`http s://…`), and the `femic-tsa24-instance` link breaks across lines. Use `\url{}` consistently and check the rendered PDF links.
45. `MS p8 l.545-547`: Reference [17] says “commit f60ce64” but the text cites the release candidate. Include the tag and commit, or cite the tag only.
46. `MS p7-p8`: The reference list is 18 entries; the related work is thin on software systems. Add 2–3 software/data citations if the Impact section discusses reuse; do not pad.

### Package and submission

47. `README.md:16-19`: “Counted words: 3,874” — the script gives 3,869. “Including the three content-table bodies still gives 3,979” — my count is 3,978. Lock the count after the final rewrite; the 21–22-word margin is too thin to leave stale.
48. `README.md:26-32`: The claimed five-section mapping is wrong: the official sections are Motivation and significance; Software description; Illustrative examples; Impact; Conclusions. Fix the README and the manuscript structure together.
49. `README.md:51-60`: The placeholder list is stale: the author/email are real; the code is tagged; the evidence release is public. Update it to the actual remaining blockers (DOI/capsule, CRediT/funding/competing interests, official template, Impact section, word count).
50. `COVER:15-18`: “The software and evidence release are being prepared as a tagged public artifact…” — false; both are public. Rewrite the cover letter to name the actual releases, the actual licence, and the actual replay command.
51. `COVER:10`: “3,874-word” — update to the final count.
52. `MANIFEST.status`: “candidate; no tag/release created; public schedules/replay release pending” — stale after `p14-evidence-rc2`. Update the status or add a note that the release exists and the manifest describes the frozen evidence snapshot.
53. `paper/release/RELEASE-CANDIDATE.md:3`: “local candidate only. No tag, release, visibility change, or DOI has been made.” Stale. Update or archive.
54. `paper/replay_all.sh:3-4`: Document `WS4_ROOT` and `TSA24_ROOT` in the manuscript/C8; the current command is not runnable as written (M2).
55. The package has no CRediT statement, funding statement, competing-interest declaration, or corresponding-author marker. Add them before submission; the README lists them as blockers.

### Evidence-record hygiene

56. `EV evidence/ws4-tsa24-gpu-ga-10000-r7/record.json`: `run.generations` is `0` for a 10,000-generation run. Fix the record or the schema; the paper claims a stable record format.
57. `EV evidence/ws4-tsa24-gpu-ga-1000-r7/record.json`: `run.search_seconds` and `run.generations` are missing; the paper uses `time_to_best_s` as “search time.” Add the field or state the substitution.
58. `EV evidence/ws4-tsa24-gpu-ga-100000-r1/record.json`: `instance.license` is `null`; the paper says the artifact has public terms. Populate it or state that the field is not applicable.
59. `EV evidence/ws4-tsa24-gpu-ga-1000-r7/record.json`: `instance.notes` says “Local fixture, not a public dataset” while the paper says “public frozen artifact”; the campaign records say “Local compiled build is derived.” Reconcile and add a dataset hash (M4).

---

## Risk table

| # | Risk | Likelihood | Impact | Evidence | Mitigation |
|---|---|---|---|---|---|
| R1 | Desk reject for missing SoftwareX Impact section / no software-impact evidence | High | Fatal | `MS p3-p6`; official OSP template §4; `README.md:26-32` | Add a substantive Impact section; or re-target to JORS |
| R2 | Replay claim fails: scripts path-mismatch the public artifact; “one-command” false; conclusion contradicts | High | Fatal | `MS p6 l.419-424`; `MS p7 l.458-461`; `EV …r1/replay.py:16-18`; `ARTIFACT`; `paper/replay_all.sh:3-4` | Parameterize paths; ship adapter/symlinks; document env vars; put scripts in release assets; reconcile text |
| R3 | Licence/metadata error: MIT vs Apache-2.0; missing C3 capsule; shifted C4–C7 and extra C8; stale placeholder caption | Certain | Fatal | `MS p7 Table 4, C3`; `LICENSE:1`; `pyproject.toml:12`; `TEX:478` | Correct to Apache-2.0; rebuild official C1–C9 table; delete placeholder |
| R4 | Provenance contradictions: feature branch vs tag; reference [17]; manifest/README/cover letter stale | Certain | Major | `MS p4 l.248-249`; `MS p6 l.419-420`; `MS p8 l.545-547`; `MANIFEST.status`; `README.md:51-60`; `COVER:15-18` | One provenance statement everywhere; update manifest/README/cover letter; add tag+commit to [17] |
| R5 | Word cap / structural mismatch: 3,978 incl tables; Impact section will exceed 4,000; official template not applied | High | Major | `README.md:16-24`; `count_words.py`; `MS p1-p6`; official template | Cut scaling/microbenchmark material; rewrite as OSP; re-count with tables |
| R6 | Objective overclaim/incompleteness: no mean level; no flow equation/reference period; “flattest” unsupported; 70M AAC hidden | Medium–High | Major | `MS p3 l.156-170`; `MS p5 Table 2`; `ARTIFACT evenflow_tsa24.yaml:1-12`; `EV …r1`–`…r7` | Add mean level, flow equation, period 1, AAC provenance; remove or support “flattest” |
| R7 | Evidence-boundary overclaim: “four failure modes”; “without optimizer binary”; search reproducibility not shown | Medium | Major | `MS p3 l.219-240`; `MS p6 l.396-400`; `EV …10000-r7` | Separate gate/search/table checks; say “without rerunning the search”; add duplicate-run check |
| R8 | Single landscape/no spatial constraints/no baseline: illustrative example does not demonstrate the distinguishing feature | High | Major | `MS p6 l.401-409`; `NOTE ws4/AGENTS.md` spatial-structure rule | Add a spatial-constraint/stress case or reframe the example; move quality-shaped numbers out of the abstract |
| R9 | Precision/table inconsistency: 2.00e3 vs 2.01e3; undefined error reference; “same batch”; 1,000-gen search-time label | Medium | Minor | `MS p5 Table 3`; `MS p5 l.344-350`; `EV eval-ablation`; `EV …1000-r7` | Report unrounded values or “about”; define reference/scale; fix wording |
| R10 | Package not ready: no DOI/capsule; no CRediT/funding/competing interests; stale README/cover letter | Certain | Major | `MS p7 Table 4`; `README.md:51-60`; `COVER:15-18` | Add DOI/Zenodo capsule; add declarations; update package docs |

---

## P0 / P1 / P2 remediation list

### P0 — must be resolved before submission

1. **Add the mandatory Impact section and a true Illustrative examples section.** Use the official OSP structure. Make the impact case concrete (users, reuse, replay/archival value, teaching), not a relabeled limitations section (`MS p3-p6`; official OSP template).
2. **Make the replay work from the public artifact.** Fix the `config/ws4/targets/…` and `build/compiled` paths in `EV …replay.py:16-18`; document the exact env vars and command; ship the scripts/schedules in the release assets or state the source-archive route; remove “tested one-command replay” from the next steps if it is already tested (`MS p6 l.419-446`; `MS p7 Table 4 C8`; `paper/replay_all.sh:3-4`).
3. **Correct the licence and metadata table.** Apache-2.0 for WS4 code; MIT/CC BY 4.0/OGL-BC for the TSA24 artifact as appropriate; rebuild the official C1–C9 table including the reproducible-capsule row; delete “Placeholders must be replaced before submission” (`MS p7 Table 4`; `TEX:478`; `LICENSE:1`; `pyproject.toml:12`).
4. **Reconcile provenance across the manuscript and package.** One statement for the code version (tag + commit + branch status); update [17], `MANIFEST.status`, `README.md`, `COVER`, and `RELEASE-CANDIDATE.md`; say whether the run used the public artifact or a byte-identical local build, and add the dataset hash (`MS p4 l.248-249`; `MS p6 l.419-420`; `MS p8 l.545-547`; `MANIFEST.status`).
5. **Apply the official template and fit the word cap.** Rewrite to the five OSP sections; cut the scaling/microbenchmark material or move it to the repository; re-count including content-table bodies; do not leave a 21–22-word margin (`README.md:16-24`; `count_words.py`).

### P1 — major revision

6. Report the mean realized level, give the flow equation and reference period (period 1), and state that the level term is the sum of 20 per-period penalties (`MS p3 l.156-165`; `MS p5 Table 2`).
7. State the 70M provenance (2025 AAC 6,917,231 m³/year) and interpret the 52M gap; remove “deliberately unattainable” if it obscures the AAC (`MS p4 l.270-274`; `ARTIFACT evenflow_tsa24.yaml:2`).
8. Remove or support “selects the flattest profile”; a ±1% band does not create a within-band gradient (`MS p3 l.168-170`; `MS p5 Table 2`).
9. Reconcile the “four failure modes” paragraph with the replay gate; add dataset/table identity to the record/validator or soften the claim; say “without rerunning the search or using the GPU,” not “without the optimizer binary” (`MS p3 l.219-240`; `MS p6 l.396-400`).
10. Add the duplicate-run determinism check (identical schedule SHA-256) to support the search-reproducibility claim (`EV …10000-r7/record.json`).
11. Add a real usage example: one `gpu-run`/replay command, a small config snippet, and the expected output. Point C7 to the docs, not the repo root; make C8 runnable (`MS p4 l.249-252`; `MS p7 Table 4 C7-C8`).
12. Report the candidate index size (50,096,749), the full effect-table size/build/nonzeros, and the full-instance evaluation time or explain why not (`MS p2 l.102-103`; `MS p5 l.328-330`; `EV …r1/record.json`).
13. Add a spatial-constraint/stress case or a second landscape; if not, reframe §3 as a functionality/replay example and move the objective range out of the abstract’s lead (`MS p6 l.401-409`).
14. Fix the record schema: `run.generations = 0` in the 10,000 record; missing `search_seconds`/`generations` in the 1,000 record; `instance.license = null` (`EV …10000-r7`; `…1000-r7`; `…r1`).

### P2 — minor / clarity

15. Fix the 2.00e3 vs 2.01e3 precision and define the error reference/scale (`MS p5 Table 3`).
16. Fix “the same 64-genome batch” → “a 64-genome batch”; “4-cell batch evaluation” in the abstract (`MS p5 l.344`; `MS p1`).
17. Fix the 1,000-gen “search” time label (`time_to_best_s`) and add a rounding note to Table 1 (`MS p4 l.285-289`; `MS p5 Table 1`).
18. Add SD to the five-seed summary or replace “small” with a descriptive range (`MS p5 l.322-326`).
19. Fix “a DOI remain” → “remains”; check URL line breaks (`MS p7 l.458-461`; `MS p7 l.453-457`).
20. Update `README.md`/`COVER` word counts and stale placeholder/private claims (`README.md:16-24`, `51-60`; `COVER:10-18`).
21. Add CRediT, funding, competing-interest, corresponding-author metadata (`README.md:51-60`).
22. Consider a 20-period flow/level profile figure or a software screenshot; the current 3-point scaling figure is a weak use of the 6-figure budget (`Fig 2`; `MS p5`).
23. Add the dataset/table hash to the record; the schedule SHA-256 is already present, but the model/table identity is not (`MS p3 l.226-229`; `EV …r1`).

---

## Recommendation and review-after-revision statement

**Recommendation:** **Major revision** for SoftwareX. Not submission-ready.

**Basis.** The software and the core idea are credible, and the P0 corrections from the EMS review are real: the level equation is correct, the five-seed table is clean, the 54.8 s value is fixed, the invalid 22.2× timing claim is gone, and the manifest hashes now match. But the manuscript does not yet meet the SoftwareX OSP bar: the mandatory Impact section is missing; the paper is a compressed validation article rather than a software note; the replay scripts do not run from the public artifact as documented; the licence is stated incorrectly; the metadata table is not the official table; provenance is contradictory across the manuscript, manifest, README, and cover letter; and the word count leaves no room for the missing sections. These are P0 issues, not copyedits.

**Prepared to review after revision:** **Yes**, if:
1. a substantive Impact section and a true Illustrative examples section are added, and the paper is cut to fit the 4,000-word cap including content-table bodies;
2. the replay runs from the public artifact with a documented command and environment, and the “one-command”/next-step language is reconciled;
3. the licence is corrected to Apache-2.0 (with the artifact terms stated), and the metadata table is rebuilt to the official C1–C9 layout;
4. provenance is unified across the manuscript, [17], manifest, README, and cover letter;
5. the objective description reports the mean level, flow reference period/equation, and AAC provenance, and the “flattest”/“four failure modes”/“without optimizer” claims are corrected.

**Confidence:** High on the factual, licence, provenance, replay, and word-count findings (I recomputed hashes, counts, and arithmetic, and read the public releases). Moderate on the journal-fit judgment; it is based on the official OSP template/guide and the paper’s own scope statements, not on external literature.

---

## QA checklist

- **Evidence-only:** Every substantive praise/critique above has an `MS`, `Table`, `Fig`, `TEX`, `EV`, `ARTIFACT`, `REL`, `MANIFEST`, `README`, `COVER`, or `NOTE` tag. No external literature was used. The official OSP template/guide is used only for format/section compliance, as stated in “Overrides.”
- **Anonymity/privacy:** No reviewer-identifying details or third-party personal information. The report is written for the authors and editor.
- **Tone:** Critical but professional; no sarcasm, no speculation about intent. The strongest language is reserved for verifiable factual errors (licence, replay path, stale placeholders).
- **Bias hygiene:** Critiques are anchored to content and evidence, not prestige, subfield preference, or personal factors.
- **Arithmetic:** Recomputed the five-seed mean/median, Table 1/2 sums, 248×, 2.00e3, the level-term identity, the global level range, and the word counts. See the appendix.
- **Hashes:** Recomputed all 28 manifest hashes; all match. The manifest **status** is stale even though the hashes are correct.
- **Read-only:** No manuscript or evidence file was edited. The only file created is this report.

---

## Appendix: arithmetic and consistency checks

| Check | Result | Evidence |
|---|---|---|
| Five-seed mean / median | 515.6818 → 515.682; median 515.938 — correct for seeds 1–5 | `MS p5 Table 2`; `EV …r1`–`…r5` |
| Table 2 flow + level = objective | Correct for every row: 1.331+517.290=518.621; 0.000+512.574=512.574; 0.000+515.938=515.938; 0.000+514.746=514.746; 0.076+516.454=516.530 | `MS p5 Table 2` |
| Level-term identity | 20×100×(70,000,000−mean)/70,000,000 matches the reported level for all six seeds to machine precision | `EV …r1`–`…r7`; `MS p3 Eq. (4)` |
| Global realized level range | min 51.2126M (seed 1), max 52.4897M (seed 2) → 51.21–52.49M | `EV …r1`, `…r2` |
| Mean realized level (missing from Table 2) | 51.8948, 52.0599, 51.9422, 51.9839, 51.9241, 51.9701M for seeds 1–5, 7 | `EV …r1`–`…r7` |
| 248× factorized | 23.1236789 / 0.093149535 = 248.2426 → 248 | `EV paper/evidence/tsa24-factorized-ablation.json` |
| 2.00e3 evaluation path | 1.0863925 / 0.0005419086 = 2,004.75 → 2.00e3; displayed 1.09/0.542 ms = 2,011 → 2.01e3 | `EV evidence/ws4-tsa24-eval-ablation.json`; `MS p5 Table 3` |
| Absolute vs relative replay error | 3.725e-9 / 10,942,260.80 ≈ 3.4e-16 | `EV eval-ablation`; `MS p5 Table 3` |
| 1,000-gen objective | 8,588,725.37 → 8,588,730 at 6 s.f.; flow 8,588,225.55 → 8,588,230; level 499.8208 → 499.821 | `EV …1000-r7`; `MS p5 Table 1` |
| 1,000-gen “search” time | `time_to_best_s` = 9.3815, not `run.search_seconds` (absent); wall 23.13 | `EV …1000-r7` |
| Five-seed wall sum | 804.004+799.646+797.826+796.314+798.116 = 3,995.9 s → 4.00e3 | `EV …r1`–`…r5`; `MS p5 l.312-313` |
| Word count | `count_words.py`: 3,827 main + 42 availability = 3,869; incl content tables = 3,978; incl equations = 4,020 | `count_words.py`; `README.md:16-19` |
| Abstract length | 172 words (README says 173) | `MS p1`; `README.md:24` |
| Manifest hashes | 28/28 match, including `factorized_ablation` (`e958a6…`) | `MANIFEST`; `sha256sum` |
| Licence | `LICENSE:1` = Apache-2.0; `pyproject.toml:12` = Apache-2.0; manuscript C3 says MIT | `MS p7 Table 4 C3`; `LICENSE:1`; `pyproject.toml:12` |
| Public release assets | `p14-evidence-rc2` assets = 5 PDFs; no schedules/scripts/JSON; scripts are in the tagged tree | `REL p14-evidence-rc2` |
| Replay path | `replay.py` expects `config/ws4/targets/evenflow_tsa24.yaml` and `build/compiled`; artifact ships `evenflow_tsa24.yaml` and `compiled/` | `EV …r1/replay.py:16-18`; `ARTIFACT` tarball |
| Record schema | 10,000 record `run.generations = 0`; 1,000 record lacks `search_seconds`/`generations`; `instance.license = null` | `EV …10000-r7`; `…1000-r7`; `…r1` |

**End of report.**
