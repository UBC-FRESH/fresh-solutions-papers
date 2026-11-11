# Reviewer report — Paper 1, SoftwareX rc4

**Manuscript:** “WS4: a compiled-state software architecture with exact replay for landscape harvest scheduling”
**Target venue:** SoftwareX, Original Software Publication (OSP)
**Review copy:** `paper/submission/softwarex/paper1-softwarex.pdf` (8 pages, 2 figures, 3 content tables + metadata table)
**Source:** `paper/submission/softwarex/paper1-softwarex.tex`
**Package:** `paper/submission/softwarex/README.md`, `paper/submission/softwarex/cover-letter.md`, `paper/release/manifest-v0.2.0-candidate.json`, `paper/release/RELEASE-CANDIDATE.md`
**Public releases checked:** `p14-evidence-rc4` (papers repo), `ws4-v0.2.0-p14rc1` (WS4 repo), `ws4-tsa24-evenflow-v1` (TSA24 artifact)
**Previous review:** `notes/reviews/paper1-softwarex-antagonistic-2026-11-11.md`
**Review date:** 2026-11-11
**Reviewer stance:** independent, antagonistic Reviewer 2 / associate editor

**Recommendation:** **Major revision — not submission-ready.**
**Prepared to review after revision:** **Yes**, if the P0 items below are closed. If the replay cannot be made to work from the public artifact, or if the Impact section remains a relabeled reuse section, the paper should be re-targeted to JORS rather than submitted to SoftwareX.
**Confidence:** High on the factual, replay, licence, provenance, table, and word-count findings. Moderate on the journal-fit and impact judgments; those rest on the official OSP template/guide and the submission’s own scope statements.

---

## Top five residual issues

1. **The public replay is still not delivered.** The replay scripts still expect paths that do not exist in the public TSA24 artifact, the release assets are PDFs only, and the conclusion still calls a “tested one-command replay” a next step. The replay gate also does not perform the coverage/candidate-membership checks the manuscript attributes to it (`EV evidence/ws4-tsa24-gpu-ga-100000-r1/replay.py:16-18`; `ARTIFACT`; `MS p6 l.453`; `MS p4 l.221-236`).
2. **The Impact section exists but has no impact evidence, and the OSP “Illustrative examples” section is still missing.** The new §4 is largely the old reuse/limitations material and explicitly disclaims adoption numbers. §3 remains “Validation and illustration,” a results section rather than a usage example (`MS p6 l.372-434`; `MS p4 l.258`; `README.md:26-32`).
3. **The metadata table is still not the official C1–C9 table, and the cited WS4 release still says MIT.** The licence value in the manuscript is now Apache-2.0, but the required “Permanent link to Reproducible Capsule” row is absent and C3–C8 are shifted; the WS4 release body still says “Licence: MIT for repository code” (`MS p7 Table 4`; `TEX:470-478`; `REL ws4-v0.2.0-p14rc1` body).
4. **Provenance is still contradictory across the package and the public artifact.** The `p14-evidence-rc4` tag’s source tree says “P14 release candidate 1,” and its tagged manifest says “no tag/release created”; the submission README, cover letter, release-candidate note, and licensing note are stale (`REL p14-evidence-rc4` tree; `MANIFEST`; `README.md:53-59`; `COVER:10-18`; `RELEASE-CANDIDATE.md:3`; `LICENSING.md:11-12`).
5. **The official SoftwareX template is not applied, and the package’s own word-count check is wrong.** The PDF is an 8-page two-column `elsarticle` draft, not the `cas-sc` OSP template; `count_words.py` gives 3,905, but adding the three content-table bodies gives about 4,005, not the README’s 3,979. Required declarations (CRediT, funding, competing interests, corresponding author) are absent (`README.md:16-32`; `REL p14-evidence-rc4` body; `MS p1-p8`).

---

## Overrides and scope of this review

- The target journal’s official OSP template and author guide are part of the submission criteria. I use them only for section, metadata-table, and length compliance, not for scientific claims. The OSP structure is five sections — Motivation and significance; Software description; Illustrative examples; Impact; Conclusions — with a C1–C9 metadata table whose left column must not be altered. The guide’s limit is 4,000 words excluding title/authors/affiliations/references/metadata tables, including abstract, running text, captions, and footnotes, with a maximum of six figures.
- All substantive praise and criticism is tied to the submission materials, the evidence records, the public releases, or the official template. No external literature was imported.
- Arithmetic was recomputed from the records and tables. All 28 manifest hashes were recomputed. The public release metadata was read through the GitHub API, and the TSA24 artifact tarball was inspected. No manuscript or evidence file was edited. The only file created is this report.
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
| `paper1-softwarex.pdf` | 8 pages, 2 figures, 3 content tables + 1 metadata table, 18 references. Two-column `elsarticle` review build, not the official OSP template (`README.md:28-32`; `MS p1-p8`). |
| `paper1-softwarex.tex` | 30,618 bytes. Title, author, affiliation, and email are real; no `author@example.invalid` in the manuscript. |
| Counted words | `python3 count_words.py` gives 3,905 (`count_words.py`; `README.md:16`). Including the three content-table bodies, my count is about 4,005, not the README’s 3,979 (`README.md:18`). |
| Abstract | 173 words by my count; `README.md:24` says 173. Within the 250-word limit but above the template’s “ca. 100 words” suggestion. |
| `README.md` | Word count 3,905 is correct; the 3,979 claim is not. The placeholder list is stale: author/email are real, the code is tagged, and the evidence release is public (`README.md:53-59`). |
| `cover-letter.md` | Still says “3,874-word” and that the software/evidence release is “being prepared” with placeholder repository/tag/DOI fields (`COVER:10-18`). This is false for the code and evidence releases. |
| `paper/evidence/` | Five campaign records plus scaling records. The five campaign records replay exactly; all 28 manifest hashes match. |
| `MANIFEST` | All 28 hashes match the current files, including the softwarex PDF and TEX. But `MANIFEST.status` still says “candidate; no tag/release created; public schedules/replay release pending” (`MANIFEST:24`). |
| `REL p14-evidence-rc4` | Public prerelease, published 2026-11-11. **Assets are five PDFs only**; schedules, replay scripts, and JSON are in the tagged source tree, not the release assets. The tag target is `8c25074`; the tag’s root README says “P14 release candidate 1” and the tagged manifest says no release. |
| `REL ws4-v0.2.0-p14rc1` | Public prerelease, no assets, target `feature/gpu-acceleration`, commit `f60ce64`. The release body says “Licence: MIT for repository code,” contradicting `LICENSE:1` and `pyproject.toml:12` (Apache-2.0). |
| `REL ws4-tsa24-evenflow-v1` | Public, non-prerelease, with a 4.66 MB `tar.gz` asset containing `compiled/`, `evenflow_tsa24.yaml`, and `seed_oldest_first_tsa24.csv`. |

---

## P0 closure status (rc4)

| # | Prior P0 | Status | Evidence |
|---|---|---|---|
| 1 | Mandatory Impact section and impact evidence | **Partially closed — section added, evidence absent** | `MS p6 l.372-434`; `TEX:403`; the section says impact is “not in adoption numbers” (`MS p6 l.373-377`) and then describes hypothetical teams. No user, download, citation, teaching, or commercial-use evidence appears. §3 is still “Validation and illustration” (`MS p4 l.258`), not “Illustrative examples.” |
| 2 | Public one-command replay feasibility and prerequisites | **Open** | `EV evidence/ws4-tsa24-gpu-ga-100000-r1/replay.py:16-18`; `ARTIFACT` tarball; `paper/replay_all.sh:3-4`; `TEX:477`; `MS p6 l.453`. See M2. |
| 3 | Correct WS4 licence and metadata table | **Partially closed — licence value fixed; table and release body not** | `TEX:472` now says Apache-2.0; `LICENSE:1` and `pyproject.toml:12` agree. But the table still omits the reproducible-capsule row and shifts C3–C8 (`TEX:470-478`), and `REL ws4-v0.2.0-p14rc1` still says MIT. |
| 4 | Provenance/tag consistency across manuscript, README, cover letter, manifests, release assets | **Open** | `README.md:53-59`; `COVER:10-18`; `MANIFEST:24`; `RELEASE-CANDIDATE.md:3`; `LICENSING.md:11-12`; `REL p14-evidence-rc4` tree. See M4. |
| 5 | 4,000-word / 6-figure structure and official SoftwareX template status | **Open** | `README.md:16-32`; `REL p14-evidence-rc4` body says the official `cas-sc` template is still pending; the PDF is two-column `elsarticle`. The 3,979 count is wrong (about 4,005). |

---

## Confidential comments to the editor

**Recommendation: major revision; do not send this to production in its current form.**

This is a materially improved rc4. The mandatory-looking Impact section now exists, the licence value is corrected to Apache-2.0 in the manuscript, reference [17] now cites the release tag rather than a branch commit, the five-seed table and level equation remain correct, all 28 manifest hashes match, and the public TSA24 artifact is real. The authors continue to keep a disciplined claim boundary: no state-of-the-art claim, no independent baseline, no environmental validation.

The problem is that rc4 closes the easy half of each P0 and leaves the hard half. The Impact section is a real heading over largely prospective reuse material; it contains no evidence that anyone has used, cited, taught, or adopted WS4. The replay claim still fails at the public artifact: the replay scripts expect `config/ws4/targets/evenflow_tsa24.yaml` and `build/compiled`, while the artifact ships `evenflow_tsa24.yaml` and `compiled/` at its root. The conclusion still calls “a tested one-command replay” a next step, which is an admission that the central contribution has not been tested from the public package. The metadata table is still not the official C1–C9 table, and the cited WS4 release still says MIT. The rc4 tag’s own source tree says “P14 release candidate 1,” and its manifest says no release was created. These are not copyedits; they are the paper’s thesis about identity and replay failing its own test.

The software is credible and the core quantitative claims are supported. I would review a revised version, but I would not support acceptance until the replay works from the public artifact, the Impact/Illustrative examples structure is real, the metadata table and licence statements are consistent, and the package provenance is unified.

---

# Comments to the authors

## Summary

The draft describes WS4, a compiled-state architecture for landscape harvest scheduling, and illustrates it on one frozen TSA24/Prince George instance with a five-seed 100,000-generation GPU campaign and exact CPU replay. It is candid about its limits, and several rc3 problems are genuinely fixed: the Impact heading exists, the licence value is Apache-2.0, [17] cites the tag, and the word-count script now agrees with the README’s headline 3,905. It is not ready for SoftwareX: the replay does not run from the public artifact as documented, the Impact section has no impact evidence and the OSP “Illustrative examples” section is still missing, the metadata table is not the official table, the cited WS4 release still says MIT, provenance is contradictory in the rc4 tag tree and package docs, the official template is not applied, and the package’s 3,979-word claim is wrong.

---

## What the draft does well

These are real strengths and should survive the revision.

1. **The level equation is correct and evidence-consistent.** `MS p3 Eq. (4), l.160-165` gives `ℓ = 20 × 100 × (70M − v̄)/70M`. I recomputed it for all six seeds from `realized_level_mean_m3`: seed 1 gives 517.2904166, seed 2 512.5741387, seed 3 515.9377175, seed 4 514.7459646, seed 5 516.4541810, seed 7 515.1408611. The equation matches to machine precision. The draft also correctly says the level term is dimensionless and not a per-period hard floor.
2. **Table 2 is internally correct and excludes seed 7 from the five-seed statistics.** The mean 515.682 and median 515.938 are correct for seeds 1–5; flow + level = objective for every row (`MS p5 Table 2`; `EV evidence/ws4-tsa24-gpu-ga-100000-r1`–`r5`). This is a clean table.
3. **The claim boundary is disciplined.** The abstract, introduction, results, and conclusions all say there is no independent harvest-scheduling comparison, no state-of-the-art claim, and no environmental-modelling claim (`MS p1`; `MS p2 l.42-43`; `MS p5 l.366-371`; `MS p6 l.442-456`). The factorized and evaluation-path results are labelled as bounded microbenchmarks (`MS p5 l.352-357`).
4. **The record and replay design is coherent in principle.** The distinction between search reproducibility and result replayability (`MS p4 l.226-242`), the “record the CPU replay objective, not the device objective” rule (`MS p3 l.206-210`), and the “gate verifies the incumbent, not the trajectory” caveat (`MS p4 l.223-225`) are the right design instincts.
5. **The evidence hashes match the manifest.** I recomputed all 28 hashes in `MANIFEST`; every one matches, including the softwarex PDF and TEX. The release asset `paper1-softwarex.pdf` hash also matches the manifest (`REL p14-evidence-rc4`; `MANIFEST`).
6. **The public TSA24 artifact is real and the block count is correct.** `REL ws4-tsa24-evenflow-v1` contains a 4.66 MB `tar.gz`; `ARTIFACT compiled/blocks.parquet` has 458,708 rows, and the campaign records report 208,255 variables and 20 periods (`EV evidence/ws4-tsa24-gpu-ga-100000-r1/record.json`). The data are not the weak point.

---

## Major comments

### M1. The Impact section is present but does not make an impact case; the OSP “Illustrative examples” section is still missing

**Claim.** The draft now has a section titled “4. Impact” (`MS p6 l.372`; `TEX:403`), but its content is largely the old reuse/limitations material. The first paragraph explicitly says the impact is “measured in exact replay and reduced evaluation cost, not in adoption numbers” (`MS p6 l.373-377`). The rest describes hypothetical teams (“A team with a compiled model…”, “A team with a fast heuristic…”, “A team comparing search methods…”) and a generic integration pattern (`MS p6 l.378-405`). No user, download, citation, teaching, commercial-use, or citable-publication evidence appears in the manuscript, package, or public release materials I reviewed. The section is roughly 60 printed lines and includes a “Limitations” subsection (`MS p6 l.407-434`); the validation material spans about 110 printed lines (`MS p4-p5`). The OSP template calls Impact the main section of the article and requires an “Illustrative examples” section; the draft still has “Validation and illustration” (`MS p4 l.258`).

**Why it matters.** This is not a formatting issue. SoftwareX publishes software because of its (proven or credible) impact; the Impact section is the journal’s central review criterion. A heading over a reuse section will read as a relabeling exercise. The missing “Illustrative examples” section is also substantive: there is no command, configuration snippet, or expected output anywhere in the manuscript (`MS p4 l.249-252`), so a reader cannot see how to use the software.

**Action.** Make the Impact section an actual case. If there are no external users yet, say so once, then argue potential impact concretely: the public artifact, the exact replay/archival value for reviewers and instructors, the adapter pattern, the ability to swap search layers, and at least one worked workflow with inputs and outputs. Add an “Illustrative examples” section with one `gpu-run` command, a small config snippet, and the expected record/replay output. Cut or move the scaling and microbenchmark material to make room. If the authors cannot make that case without overclaiming, JORS is the better venue.

---

### M2. The public replay still does not work as documented, and the replay gate overclaims what it checks

**Claim.** The manuscript says the paper-specific schedules and replay scripts are in the public evidence release (`MS p6 l.426-429`; `MS p7 l.463-466`), and the metadata table gives a replay command (`MS p7 Table 4 C8`; `TEX:477`). It also says the next step is “a tested one-command replay” (`MS p6 l.453`). The replay gate is said to validate coverage and candidate membership (`MS p4 l.221-222`), and “four failure modes are exposed” with none silent in a passing record (`MS p4 l.232-236`).

**Evidence.**
- `EV evidence/ws4-tsa24-gpu-ga-100000-r1/replay.py:16-18` still hard-codes `INSTANCE / "config/ws4/targets/evenflow_tsa24.yaml"` and `INSTANCE / "build/compiled"`. The public artifact ships `evenflow_tsa24.yaml` and `compiled/` at its root (`ARTIFACT`; the tarball contains `tsa24x/evenflow_tsa24.yaml` and `tsa24x/compiled/`). I checked the artifact: `build/compiled` and `config/ws4/targets/evenflow_tsa24.yaml` are **missing**; `compiled` and `evenflow_tsa24.yaml` **exist**.
- `paper/replay_all.sh:3-4` requires `WS4_ROOT` and `TSA24_ROOT`; it does not set up the expected subdirectories. `TEX:477` adds `FHOPS_ROOT` and gives no working directory or expected output. The command is not runnable from a clean artifact as written.
- `REL p14-evidence-rc4` assets are five PDFs only (`paper1-manuscript.pdf`, `paper1-softwarex.pdf`, `paper2-jors.pdf`, `paper2-jors-supplement.pdf`, `paper2-manuscript.pdf`); the schedules and replay scripts are in the tag’s source tree. A reader who downloads the release assets does not get the replay material.
- The conclusion’s “a tested one-command replay” (`MS p6 l.453`) contradicts C8 and the release body’s claim that replay prerequisites are corrected.
- The gate claim is stronger than the code. `scripts/check_benchmark_record.py` validates the schema, schedule path, and hash, then runs the adjacent `replay.py`; `ws4/opt/engine.py:92-122` (`load_schedule_csv`) only parses the CSV, and `ws4/opt/incremental.py:164-184` (`IncrementalObjective.reset`) simply accumulates whatever schedule is loaded. I did not find a coverage or candidate-membership check. A partial schedule would evaluate silently; a stale table would not be detected because the record has no dataset/table hash (`EV …/record.json`).
- Of the “four failure modes,” the gate can catch a reported device objective (by comparing the CPU replay to the recorded value). It does not catch an irreversible move (that is a search-time apply/undo invariant), a model change without a table rebuild (no dataset/table identity), or a partial/infeasible schedule (no coverage check). The sentence “None is silent in a record that passes the gate” is therefore not supported.

**Why it matters.** The paper’s central contribution is the replay contract. If a reader cannot run the replay from the public artifact as documented, the contract is a design, not a delivered result. The current mismatch is exactly the kind of failure the paper claims to prevent.

**Action.** Parameterize the replay scripts to accept `compiled/` and `evenflow_tsa24.yaml` at the artifact root, or ship a small adapter/symlink script and document it. Give the exact command, working directory, environment variables, and expected output. Test it from a clean artifact and attach the log. Put the scripts/schedules in the release assets or explicitly say “download the source archive at tag `p14-evidence-rc4`.” Remove “tested one-command replay” from the next steps if it is tested, or remove the C8 replay claim if it is not. Either implement coverage/candidate-membership and dataset-identity checks or soften the “four failure modes” paragraph to the one check the gate actually performs. Say “without rerunning the search or using the GPU,” not “without calling the optimizer”: the replay path imports and constructs `Optimizer` (`EV …/replay.py:10-18`).

---

### M3. The licence value is fixed, but the metadata table is still not the official C1–C9 table, and the cited WS4 release still says MIT

**Claim.** `TEX:472` now says “Legal code licence: Apache-2.0 for WS4; the TSA24 artifact retains its own public terms.” That value is correct: `LICENSE:1` is Apache-2.0 and `pyproject.toml:12` is `license = "Apache-2.0"`. But the table is still not the official metadata table.

**Evidence.** The official OSP table rows are C1 current code version; C2 permanent link to code/repository; C3 permanent link to Reproducible Capsule; C4 legal code licence; C5 code versioning system; C6 languages/tools; C7 compilation requirements; C8 developer documentation; C9 support email. The draft has C3 = licence, C4 = versioning, C5 = languages, C6 = compilation, C7 = documentation, C8 = test/replay command (`TEX:470-478`; `MS p7 Table 4`). The required C3 capsule row is absent. C7 points to the repository root, not documentation. C8 is a test/replay command rather than the documentation link. C2 is a prerelease tag, not a capsule/permanent archive. The table caption no longer contains the stale placeholder sentence, which is an improvement.

The WS4 release body still says “Licence: MIT for repository code” (`REL ws4-v0.2.0-p14rc1` body), contradicting the manuscript and the repository. A reader who follows C2 sees the wrong licence. The TSA24 artifact terms are also stated only vaguely (“retains its own public terms”); the artifact itself says MIT for code/documentation, CC BY 4.0 for derived benchmark artifacts, and OGL-BC for source data (`ARTIFACT README.md`; `BENCHMARK_ARTIFACT.md`).

**Why it matters.** SoftwareX requires an approved licence, an accurate metadata table, and a reproducible capsule/DOI. A wrong licence in the cited release is a factual error; a shifted metadata table is a hard format noncompliance. Either can delay or block production.

**Action.** Rebuild the table in the official C1–C9 order. Add C3 “Permanent link to Reproducible Capsule” or state “not yet available” honestly; put the Apache-2.0 licence in C4; move versioning to C5, languages to C6, compilation to C7, documentation to C8, and the support email to C9. Move the test/replay command into “Data and code availability.” Correct the WS4 release body to Apache-2.0, or cite a release whose body is correct. State the TSA24 artifact terms precisely (MIT/CC BY 4.0/OGL-BC) in the data availability statement.

---

### M4. Provenance is still contradictory across the manuscript, package, and public artifact

**Claim.** The manuscript now cites `ws4-v0.2.0-p14rc1` consistently (`MS p4 l.248-249`; `MS p7 Table 4 C1-C2`; `MS p8 l.551-554`), and [17] no longer says “commit f60ce64” alone. That part is fixed. The package and the public artifact are not.

**Evidence.**
- `README.md:53-59` still says the draft cites “commit `f60ce64` on a feature branch, not a release” and that the evidence release is “currently private.” Both are false: the draft cites the tag, and `p14-evidence-rc4` is public.
- `COVER:10-18` still says “3,874-word” and that the software/evidence release is “being prepared” with placeholder repository/tag/DOI fields. Both are false for the code and evidence releases.
- `MANIFEST:24` still says “candidate; no tag/release created; public schedules/replay release pending.”
- `RELEASE-CANDIDATE.md:3` still says “local candidate only. No tag, release, visibility change, or DOI has been made.”
- `LICENSING.md:11-12` still says “The repository is not yet public.”
- The `p14-evidence-rc4` tag target is commit `8c25074`; its root `README.md` says “P14 release candidate 1 (`p14-evidence-rc1`),” and its tagged `paper/release/manifest-v0.2.0-candidate.json` says no release was created. The release assets, however, are rc4 PDFs. The tag’s `paper/submission/softwarex/README.md` also still says 3,874 words.
- The WS4 release body says MIT (see M3).

**Why it matters.** A SoftwareX reviewer will click the links and compare them with the metadata. Contradictory provenance is a credibility problem even when the underlying artifact is good. The paper’s own thesis is that identity and replay matter; the package should model that discipline.

**Action.** Pick one provenance statement and use it everywhere: “WS4 `ws4-v0.2.0-p14rc1`, a public prerelease tag on `feature/gpu-acceleration` at commit `f60ce64`, not a merged main-branch release.” Update `README.md`, `COVER`, `MANIFEST.status`, `RELEASE-CANDIDATE.md`, and `LICENSING.md` to the public state. Cut a new release tag from a commit whose root README, softwarex README, and manifest agree with the release body and assets; or update the release assets/body to match the tag. State whether the campaign used the artifact’s `compiled/` tables or a byte-identical local build, and add the dataset/table hash to the record.

---

### M5. The official template is not applied, the package’s 3,979-word claim is wrong, and required declarations are missing

**Claim.** `README.md:28-32` explicitly says the draft is “**not** the official SoftwareX Original Software Publication template” and that the official template “must be applied before submission.” The rc4 release body also lists “Official SoftwareX `cas-sc` template and final page/format checks” as still pending. The PDF is an 8-page two-column `elsarticle` build (`MS p1-p8`).

**Evidence.** `python3 count_words.py` gives 3,905 (`count_words.py`; `README.md:16`). Adding the three content-table bodies gives about 4,005 (27 + 42 + 31 words, by my count), not the README’s 3,979 (`README.md:18`). The official cap is 4,000 words under the guide’s convention. Even under the package’s convention (table bodies excluded), 3,905 leaves only 95 words, and the README’s own conservative check is wrong. The manuscript has no CRediT authorship contribution statement, funding statement, competing-interest declaration, or corresponding-author marker; the README lists these as blockers (`README.md:53-54`).

**Why it matters.** A template swap is not cosmetic: the official `cas-sc` layout changes the page count and the metadata table. A 4,000-word cap with a false internal count is a submission risk. Missing declarations are standard Elsevier production requirements.

**Action.** Apply the official `cas-sc` template and rebuild the metadata table to its layout. Re-count with a transparent script, including content-table bodies, and state the convention. Cut the scaling/microbenchmark material or move it to the repository to leave a real margin. Add CRediT, funding, competing interests, and corresponding-author metadata before submission. Update `README.md` and `COVER` to the final counts and the actual release state.

---

### M6. The objective description is still incomplete: no mean level, no flow equation/reference period, an unsupported “flattest” claim, and no AAC provenance

**Claim.** The draft describes the level term as a normalized mean-level penalty (`MS p3 l.160-165`) and the even-flow target as a squared deviation outside a ±1% band (`MS p3 l.156-159`). It says “The even-flow target selects the flattest profile at the level where the two roles reach their best weighted compromise” (`MS p3 l.168-170`). It reports the realized level only as a per-seed min–max range (`MS p5 Table 2`), not the mean that drives the penalty.

**Evidence.**
- The target file defines the flow target with `flow_reference_period: 1`, `minimum: -1.0`, `maximum: 1.0`, weight 10,000, and 20 separate per-period level targets with `minimum: 70000000.0`, weight 100, `normalization: auto` (`ARTIFACT evenflow_tsa24.yaml:1-12` and following). The paper never states that the reference period is period 1, and it never gives the flow penalty equation.
- The level term is algebraically the sum of 20 per-period linear penalties; the paper’s “mean” equation is correct as an aggregate, but it does not say the implementation sums 20 per-period targets. A reader may think there is one target on the mean.
- The table reports `realized_level_min_m3`/`max_m3` per seed; the means are 51.8948, 52.0599, 51.9422, 51.9839, 51.9241, 51.9701M for seeds 1–5 and 7 (`EV …r1`–`…r7`). The headline level term cannot be checked from Table 2 without solving Eq. (4).
- The target file’s header says 70M is “slightly above the 2025 AAC 6,917,231.” The paper calls it “deliberately unattainable” (`MS p1`; `MS p4 l.272-273`) but never says it is the AAC or why 70M was chosen. That omission makes the 52M outcome look like an arbitrary target gap rather than a policy-relevant result.
- The “flattest profile” claim is not supported by a ±1% band penalty: within the band, the flow term is zero for three of five seeds (seed 5 is 0.076) (`MS p5 Table 2`), so the target does not create a “flattest” gradient there. The level term, not the flow target, drives the mean.

**Why it matters.** The objective is the central quantitative result. A reader must be able to reproduce the flow and level terms, and must know that the level penalty uses the mean, not the range. The AAC provenance is also the strongest available interpretation of the 52M result; omitting it weakens the paper’s relevance.

**Action.** Add the flow penalty equation and state the reference period (period 1). State that the implementation has 20 per-period level targets whose sum is Eq. (4), or say “the aggregate is equivalent to a mean-level penalty.” Add the mean realized level to Table 2 (and the abstract, if the range stays). State the 70M provenance: “the 2025 AAC is 6,917,231 m³/year; the target is 70M m³ per 10-year period, slightly above it.” Then interpret the 52M outcome honestly: the optimized estate meets the even-flow band but falls short of the AAC by ~18M m³ per period. Remove “selects the flattest profile” unless a profile figure shows it; say “the even-flow target penalizes deviations outside the ±1% band, and the level target pulls the mean upward.”

---

### M7. The record format and evidence hygiene do not support the “stable record” claim

**Claim.** The manuscript says the record carries the instance, availability, objective, feasibility, algorithm, version, configuration, seed, hardware, software, wall and search times, schedule path and SHA-256, exact-replay flag, and per-target residuals (`MS p4 l.226-230`). It also says a validator checks the schema, schedule path, and hash (`MS p4 l.230-231`).

**Evidence.** The 10,000-generation record still has `run.generations = 0` (`EV evidence/ws4-tsa24-gpu-ga-10000-r7/record.json`). The 1,000-generation record omits `run.search_seconds` and `run.generations`; the paper uses `time_to_best_s` as “search time” (`EV evidence/ws4-tsa24-gpu-ga-1000-r7/record.json`; `MS p4 l.287`). The campaign records have `instance.license = null` despite the public artifact terms (`EV evidence/ws4-tsa24-gpu-ga-100000-r1/record.json`). No record has a dataset/table hash, only `schedule_sha256`; the paper claims each stage writes an identity so the next stage can reject a mismatch (`MS p2 l.70-72`), but the replay cannot detect a different compiled table.

**Why it matters.** The paper claims a stable, inspectable record format. Null/missing fields and the absence of model identity undercut that claim. The 1,000-generation “search time” is especially awkward because Table 1’s caption says “search time is the GPU search budget” (`MS p5 Table 1`), but the record does not contain `search_seconds` for that run.

**Action.** Fix the 10,000 and 1,000 records or the schema. Add a dataset/table identity (hash or manifest digest) to every campaign record and to the validator. Label the 1,000-generation value as `time_to_best_s`, not search time, in Table 1 and the text. Add the duplicate-run determinism evidence from `EV …10000-r7` (“Two independent runs produced the identical schedule SHA-256”) to support the search-reproducibility claim. Populate `instance.license`.

---

### M8. The validation remains a single-landscape, no-spatial-constraint, no-baseline demonstration

**Claim.** The draft is explicit that the validation covers one landscape, one target construction, and one 20-period horizon, with no hard adjacency or opening-size constraints, and no independent model or LP/MIP bound (`MS p6 l.408-418`). That honesty is a strength. But the illustrative example still does not exercise the software’s spatial-structure claim, and the abstract still leads with the objective range.

**Evidence.** `MS p6 l.410-413`: “The reported run has no hard adjacency or opening-size constraints, so the software is not validated on the spatial-constraint case that motivates much of the literature.” `MS p6 l.413-416`: “There is no independent harvest-scheduling model or LP/MIP bound on the same instance, so the objective values are not a competitive quality result.” The abstract’s second sentence is the five-seed objective range (`MS p1`). The software’s own contract says spatial structure is part of the model, not a post-processing step (`NOTE ws4/AGENTS.md`); the example does not test it.

**Why it matters.** For SoftwareX, the illustrative example should demonstrate the software’s major functions. If spatial structure is a distinguishing feature, an example without spatial constraints does not demonstrate it. The absence of a baseline is acceptable if the paper is explicit that the example is a functionality/replay demonstration, not a quality result; the current abstract still invites the quality reading.

**Action.** If feasible, add a small adjacency or opening-size case (even a stress instance) or a second landscape. If not, reframe §3 as “Illustrative example: exact replay on a public instance” and move the quality-shaped numbers out of the abstract’s lead. State explicitly that the example demonstrates the compiled boundary, the sparse effect table, and the replay gate, not schedule quality.

---

## Minor comments

### Abstract, title, and front matter

1. `MS p1`: The abstract leads with “512.574–518.621 (mean 515.682)” before saying there is no independent comparison. The number is target-specific and not a quality result. Lead with the software capability and replay contract; move the objective range to the illustrative example, or state “on one public instance, under a deliberately unattainable level target” in the same sentence.
2. `MS p1`: “against a deliberately unattainable 70M aspiration” is not supported by the target file, which describes 70M as a linear minimum “slightly above the 2025 AAC 6,917,231” (`ARTIFACT evenflow_tsa24.yaml:1-2`). Replace with the AAC provenance or “above the level this estate achieves.”
3. `MS p1`: “A 5,000-block diagnostic reduces move-evaluation time by 2.00×10^3” — say “warm whole-schedule move evaluation” and “per move,” or a reader may think it is a full-instance simulation.
4. `MS p1`: “a 64-genome factorized batch runs 248 times faster on CUDA than on a single-device CPU path” — add “4-cell batch evaluation” so the scope is in the abstract, not only the body.
5. `MS p1`: The title is defensible and does not overclaim. Do not add “GPU speedup” or “state-of-the-art.”
6. `MS p1`: The abstract is 173 words; the OSP template suggests ca. 100. This is not a hard limit (250), but a shorter abstract would leave room for the missing declarations and a tighter Impact section.

### Introduction and related work

7. `MS p1-p2`: The related work cites search-method studies (simulated annealing, tabu/GA, eight heuristics) but no existing harvest-scheduling software. For a SoftwareX paper, the reader needs to know what software this replaces or extends. Add a short paragraph on existing systems (commercial or open-source) and state the distinction without a prestige claim.
8. `MS p2 l.44-48`: “The intended users are groups with a compiled spatial model…” is the only impact statement in the introduction. It is hypothetical. Move it to the Impact section and make it concrete.
9. `MS p2 l.57-62`: The CPU-refinement handoff is “designed but is not part of the measured campaign.” This is honest, but it adds words and may confuse the illustrative example. Either cut it or label it clearly as future work in the Impact/limitations section.
10. `MS p4 l.268-269`: “its objective is 1,722,140,000, dominated by even-flow deviations” — the initial flow/level split is not reported. Either report it or say “the initial objective is dominated by flow” without the unsupported split.

### Software description

11. `MS p2 l.102-103`: “The index is smaller than the full cross-product but richer than a binary harvest decision.” The record has `options: 50,096,749`; report the candidate index size and the per-block distribution. This is the kind of concrete software detail SoftwareX readers expect.
12. `MS p2-p3 l.139-156`: The effect table’s build time, storage size, and nonzero count are not reported. Only the factorized build (234 s) appears. Report the full table’s size/build/nonzeros, or state that they are in the repository.
13. `MS p3 l.156-159`: The flow reference period is period 1 per the target file; state it. Give the flow penalty equation or a precise formula.
14. `MS p3 l.160-165`: The level term is the sum of 20 per-period linear penalties; say so, or a reader will think there is one target on the mean. The equation itself is correct.
15. `MS p3 l.168-170`: “selects the flattest profile” is not supported by a ±1% band. Remove or support with a 20-period profile figure.
16. `MS p4 l.194-196`: “The replay contract applies to the final assignment, not the move decomposition” is good; make sure the “four failure modes” paragraph does not contradict it (M2).
17. `MS p4 l.249-252`: The command-line surface is described in one sentence, but there is no example command, config snippet, or output. SoftwareX’s Illustrative examples section needs at least one. Add a short `gpu-run`/replay example (the `BENCHMARK_ARTIFACT.md` recipe is a good start).
18. `MS p4 l.253-257`: “The large GPU effect table and caches are not part of the small public dataset artifact; they are rebuilt from the published recipe.” Good; give the recipe URL/path and the expected build time/size.
19. `MS p4 l.245-249`: The environment lacks the CUDA version, PyTorch version, driver, and CPU RAM. For a software paper that reports 248× and 856 s, state them or point to a lockfile/container.

### Validation and illustration

20. `MS p4 l.260-262`: “The case study uses the public frozen artifact ws4-tsa24-evenflow-v1.” The campaign records say “Local compiled build is derived” (`EV …r1/record.json`). State whether the run used the artifact’s `compiled/` tables or a byte-identical local build, and give the dataset/table hash.
21. `MS p4 l.270-274`: The 70M target is the 2025 AAC plus ~1.2% (`ARTIFACT evenflow_tsa24.yaml:1-2`), not an arbitrary aspiration. State the provenance; it makes the 52M gap interpretable.
22. `MS p5 Table 1`: The 1,000-gen objective is 8,588,725.37, displayed as 8,588,730 at 6 s.f.; the flow+level components are independently rounded and sum to 8,588,729.821. Add a note that rows are independently rounded, or report one more digit. The 1,000-gen “search” time is `time_to_best_s`, not `search_seconds`; label it accordingly.
22a. `MS p4 l.300-302`: “The level term remains between 499.821 and 517.290” sits in the seed-7 scaling subsection, but seed 7’s maximum level term is 515.141; 517.290 is seed 1. Either say “across all reported runs” or use the seed-7 range 499.821–515.141.
23. `MS p5 Table 1`: The 100k seed-7 wall time (942 s) is ~18% longer than the five campaign runs (~798 s) and its memory is 8.26 GB vs 9.0 GB. The paper does not explain the difference. Either use a campaign run for the scaling row or state that seed 7 is a different configuration/run.
24. `MS p5 Table 2`: Add a mean realized level column. The min–max ranges are useful but do not let a reader check the level term.
25. `MS p5 l.323-326`: The five-seed spread is called “small” without a standard deviation. Add SD (≈2.23) or say “descriptive range 6.05 objective units (1.2% of the mean).”
26. `MS p5 Table 3`: The displayed 1.09 s / 0.542 ms gives 2.01e3, not 2.00e3. Report 1.086 s and 0.5419 ms, or say “about 2.0×10^3 computed from unrounded values.”
27. `MS p5 Table 3`: The “Error” column has no units or reference scale. The 5,000-block objective is 10,942,260.80; the relative error is ~3.4×10^-16. Say “absolute error 3.7×10^-9 on a 1.09×10^7 objective” or add a relative-error column.
28. `MS p5 l.355-358`: “A full-instance whole-schedule ablation is impractical… A cold whole-schedule evaluation took 54.8 s” — this is the 5,000-block subset, not the full 208,255-block instance. Say “subset schedule” in the text as well as the table caption.
29. `MS p5 l.360-361`: “The subset is not a random sample” — state the selection rule (block ID order? spatial?) and why it is not random.
30. `MS p5 l.385`: “the same 64-genome batch” — there is no prior 64-genome batch in the paper. Say “a 64-genome batch.”
31. `MS p5 l.387-389`: “maximum absolute error against the exact evaluator is 1.71×10^-6 on both paths” — if the CPU path is the exact evaluator, its error should be zero. Name the reference evaluator, give the objective scale, and explain why both paths have the same nonzero error. The evidence has `exact_max_error` for both CPU and CUDA, so the reference is a third evaluator; say so.
32. `MS p5 l.400-401`: “The retained CPU simulated-annealing run is untuned…” — the paper no longer describes that run. Either cut the sentence or explain what “retained” refers to.

### Impact, limitations, conclusions

33. `MS p6 l.378-388`: “A team with a fast heuristic but no replay contract can wrap the heuristic in the adapter” — the adapter interface is not described in §2. Either describe the adapter contract or remove the claim. A reader cannot implement a component the paper does not define.
34. `MS p6 l.405-406`: “without rerunning the search or needing the original GPU” is good and more accurate than the previous “without the optimizer binary.” Keep it.
35. `MS p6 l.426-429`: “The GPU code is public as release candidate ws4-v0.2.0-p14rc1” — true, but the release body says MIT and the tag is on a feature branch. Add the commit and branch status, and correct the release body (M3/M4).
36. `MS p6 l.453`: “The next steps are a DOI and a tested one-command replay” — contradicts C8 and the release note. Reconcile (M2).
37. `MS p6 l.455-456`: “not a leaderboard entry… not a competitive solver” is honest but reads as a disclaimer. In the Impact section, say what the software *does* enable, not only what it does not claim.
38. `MS p7 Table 4 C7`: “Link to developer documentation: https://github.com/UBC-FRESH/ws4” — that is the repository root, not documentation. Point to `docs/` or the docs site.
39. `MS p7 Table 4 C8`: “Test command: python -m pytest; replay: WS4_ROOT=... TSA24_ROOT=... FHOPS_ROOT=... bash paper/replay_all.sh” — no working directory, install step, or expected output. Make it runnable (M2).
40. `MS p7 l.459-467`: “a DOI remains pending” — grammar fixed. The data availability sentence says the schedules are in the public release and then says a DOI is pending; clarify that the release is a prerelease, not an archival DOI. The `http s://` line break is still visible in the PDF.
41. `MS p8 l.551-554`: Reference [17] now cites the tag correctly. Good. Consider adding the commit hash or the release date for exactness.

### Package and submission

42. `README.md:16-19`: The 3,905 count is correct; the 3,979 claim is not. Adding the three content-table bodies gives about 4,005. Lock the count after the rewrite and state the convention.
43. `README.md:28-32`: The claimed five-section mapping is wrong: the official sections are Motivation and significance; Software description; Illustrative examples; Impact; Conclusions. Fix the README and the manuscript structure together.
44. `README.md:53-59`: The placeholder list is stale: the author/email are real; the code is tagged; the evidence release is public. Update it to the actual remaining blockers (DOI/capsule, CRediT/funding/competing interests, official template, Impact evidence, word count).
45. `COVER:10`: “3,874-word” — update to 3,905 (or the final count).
46. `COVER:15-18`: “The software and evidence release are being prepared…” — false; both are public. Rewrite to name the actual releases, the actual licence, and the actual replay command.
47. `MANIFEST:24`: “candidate; no tag/release created; public schedules/replay release pending” — stale after `p14-evidence-rc4`. Update the status or add a note that the release exists and the manifest describes the frozen evidence snapshot.
48. `RELEASE-CANDIDATE.md:3`: “local candidate only. No tag, release, visibility change, or DOI has been made.” Stale. Update or archive.
49. `LICENSING.md:11-12`: “The repository is not yet public.” Stale. Update.
50. The package has no CRediT statement, funding statement, competing-interest declaration, or corresponding-author marker. Add them before submission; the README lists them as blockers.

### Evidence-record hygiene

51. `EV evidence/ws4-tsa24-gpu-ga-10000-r7/record.json`: `run.generations` is `0` for a 10,000-generation run. Fix the record or the schema; the paper claims a stable record format.
52. `EV evidence/ws4-tsa24-gpu-ga-1000-r7/record.json`: `run.search_seconds` and `run.generations` are missing; the paper uses `time_to_best_s` as “search time.” Add the field or state the substitution.
53. `EV evidence/ws4-tsa24-gpu-ga-100000-r1/record.json`: `instance.license` is `null`; the paper says the artifact has public terms. Populate it or state that the field is not applicable.
54. `EV evidence/ws4-tsa24-gpu-ga-100000-r1/record.json`: The record has `schedule_sha256` but no dataset/table hash. Add one so the replay can detect a stale table (M2/M7).

---

## Risk table

| # | Risk | Likelihood | Impact | Evidence | Mitigation |
|---|---|---|---|---|---|
| R1 | Desk reject for an Impact section without impact evidence / missing Illustrative examples | High | Fatal | `MS p6 l.372-434`; `MS p4 l.258`; `README.md:28-32` | Add a real impact case and a usage example; or re-target to JORS |
| R2 | Replay claim fails: scripts path-mismatch the public artifact; “one-command” false; conclusion contradicts | High | Fatal | `EV …/replay.py:16-18`; `ARTIFACT`; `MS p6 l.453`; `TEX:477` | Parameterize paths; ship adapter; document env/cwd/output; test from clean artifact; reconcile text |
| R3 | Metadata/licence: table not official C1–C9; WS4 release body says MIT | Certain | Fatal | `MS p7 Table 4`; `TEX:470-478`; `REL ws4-v0.2.0-p14rc1` body | Rebuild table; correct release body; state artifact terms |
| R4 | Provenance contradictions: rc4 tag tree says rc1; tagged manifest says no release; README/COVER/RELEASE-CANDIDATE/LICENSING stale | Certain | Major | `REL p14-evidence-rc4` tree; `MANIFEST:24`; `README.md:53-59`; `COVER:10-18`; `RELEASE-CANDIDATE.md:3` | One provenance statement everywhere; cut a clean tag; update docs |
| R5 | Template/word cap: `cas-sc` not applied; 3,979 claim wrong; no declarations | High | Major | `README.md:16-32`; `REL p14-evidence-rc4` body; `count_words.py` | Apply template; re-count; cut; add declarations |
| R6 | Evidence-boundary overclaim: gate does not check coverage/irreversible move/stale table | Medium–High | Major | `MS p4 l.221-236`; `EV …/replay.py`; `ws4/opt/incremental.py:164-184` | Implement checks or soften the “four failure modes” claim |
| R7 | Objective overclaim/incompleteness: no mean level; no flow equation/reference period; “flattest” unsupported; AAC hidden | Medium–High | Major | `MS p3 l.156-170`; `MS p5 Table 2`; `ARTIFACT evenflow_tsa24.yaml:1-12` | Add mean level, flow equation, period 1, AAC provenance; remove/support “flattest” |
| R8 | Record hygiene: 10k `generations=0`; 1k search time missing; no dataset hash | Medium | Major | `EV …10000-r7`; `…1000-r7`; `…r1` | Fix schema/records; add dataset/table hash |
| R9 | Single landscape/no spatial constraints/no baseline: example does not demonstrate the distinguishing feature | High | Major | `MS p6 l.408-418`; `NOTE ws4/AGENTS.md` | Add a spatial stress case or reframe the example |
| R10 | Package not ready: no DOI/capsule; stale README/cover letter; no CRediT/funding/competing interests | Certain | Major | `MS p7 Table 4`; `README.md:53-59`; `COVER:10-18` | Add DOI/capsule and declarations; update package docs |

---

## P0 / P1 / P2 remediation list

### P0 — must be resolved before submission

1. **Make the replay work from the public artifact.** Fix the `config/ws4/targets/…` and `build/compiled` paths in `EV …/replay.py:16-18`; document the exact env vars, working directory, and expected output; ship the scripts/schedules in the release assets or state the source-archive route; remove “tested one-command replay” from the next steps if it is already tested (`MS p6 l.426-453`; `MS p7 Table 4 C8`; `paper/replay_all.sh:3-4`).
2. **Add a substantive Impact section and a true Illustrative examples section.** Use the official OSP structure. Make the impact case concrete (users, reuse, replay/archival value, teaching), not a relabeled limitations section (`MS p3-p6`; official OSP template).
3. **Rebuild the metadata table to the official C1–C9 layout and correct the licence statements.** Apache-2.0 for WS4 code; MIT/CC BY 4.0/OGL-BC for the TSA24 artifact as appropriate; add the reproducible-capsule row or state “not yet available”; move the test/replay command to Data availability; correct the WS4 release body (`MS p7 Table 4`; `TEX:470-478`; `LICENSE:1`; `pyproject.toml:12`; `REL ws4-v0.2.0-p14rc1` body).
4. **Reconcile provenance across the manuscript and package.** One statement for the code version (tag + commit + branch status); update [17], `MANIFEST.status`, `README.md`, `COVER`, `RELEASE-CANDIDATE.md`, and `LICENSING.md`; cut a clean rc4 tag whose source tree and release body match the assets; say whether the run used the public artifact or a byte-identical local build, and add the dataset hash.
5. **Apply the official template, fit the word cap, and add declarations.** Rewrite to the five OSP sections; cut the scaling/microbenchmark material or move it to the repository; re-count including content-table bodies; add CRediT, funding, competing interests, and corresponding-author metadata (`README.md:16-32`; `count_words.py`).

### P1 — major revision

6. Report the mean realized level, give the flow equation and reference period (period 1), and state that the level term is the sum of 20 per-period penalties (`MS p3 l.156-165`; `MS p5 Table 2`).
7. State the 70M provenance (2025 AAC 6,917,231 m³/year) and interpret the 52M gap; remove “deliberately unattainable” if it obscures the AAC (`MS p4 l.270-274`; `ARTIFACT evenflow_tsa24.yaml:1-2`).
8. Remove or support “selects the flattest profile”; a ±1% band does not create a within-band gradient (`MS p3 l.168-170`; `MS p5 Table 2`).
9. Reconcile the “four failure modes” paragraph with the replay gate; implement coverage/candidate-membership and dataset-identity checks or soften the claim; say “without rerunning the search or using the GPU,” not “without calling the optimizer” (`MS p4 l.221-236`; `MS p6 l.405-406`).
10. Add the duplicate-run determinism check (identical schedule SHA-256) to support the search-reproducibility claim (`EV …10000-r7/record.json`).
11. Add a real usage example: one `gpu-run`/replay command, a small config snippet, and the expected output. Point C7 to the docs, not the repo root; make C8 runnable (`MS p4 l.249-252`; `MS p7 Table 4 C7-C8`).
12. Report the candidate index size (50,096,749), the full effect-table size/build/nonzeros, and the full-instance evaluation time or explain why not (`MS p2 l.102-103`; `MS p5 l.328-330`; `EV …r1/record.json`).
13. Add a spatial-constraint/stress case or a second landscape; if not, reframe §3 as a functionality/replay example and move the objective range out of the abstract’s lead (`MS p6 l.408-418`).
14. Fix the record schema and identity fields: `run.generations = 0` in the 10,000 record; missing `search_seconds`/`generations` in the 1,000 record; `instance.license = null`; no dataset/table hash (`EV …10000-r7`; `…1000-r7`; `…r1`).
15. Add CRediT, funding, competing-interest, and corresponding-author metadata (`README.md:53-54`).

### P2 — minor / clarity

16. Fix the 2.00e3 vs 2.01e3 precision and define the error reference/scale (`MS p5 Table 3`).
17. Fix “the same 64-genome batch” → “a 64-genome batch”; “4-cell batch evaluation” in the abstract (`MS p5 l.385`; `MS p1`).
18. Fix the 1,000-gen “search” time label (`time_to_best_s`) and add a rounding note to Table 1 (`MS p4 l.287`; `MS p5 Table 1`).
19. Add SD to the five-seed summary or replace “small” with a descriptive range (`MS p5 l.323-326`).
20. Fix the seed-7 wall-time discrepancy or explain it (`MS p5 Table 1`; `EV …100000-r7`).
21. Fix “a DOI remain” → “remains”; the grammar is fixed, but check the `http s://` line breaks (`MS p7 l.459-467`).
22. Update `README.md`/`COVER` word counts and stale placeholder/private claims (`README.md:16-24`, `53-59`; `COVER:10-18`).
23. Consider a 20-period flow/level profile figure or a software screenshot; the current 3-point scaling figure is a weak use of the 6-figure budget (`Fig 2`; `MS p5`).
24. Add the dataset/table hash to the record; the schedule SHA-256 is already present, but the model/table identity is not (`MS p2 l.70-72`; `EV …r1`).
25. Report CUDA/PyTorch versions, driver, and CPU RAM (`MS p4 l.245-249`; `MS p7 Table 4 C6`).
26. Point C7 to `docs/` or the docs site, not the repository root (`MS p7 Table 4 C7`).
27. State the TSA24 artifact terms precisely (MIT/CC BY 4.0/OGL-BC) in Data availability (`MS p7 l.459-467`; `ARTIFACT README.md`).
28. Add a short existing-software comparison to the introduction (`MS p1-p2`).

---

## Recommendation and review-after-revision statement

**Recommendation:** **Major revision** for SoftwareX. Not submission-ready.

**Basis.** The software and the core idea are credible, and several rc3 corrections are real: the Impact heading exists, the licence value is Apache-2.0, [17] cites the tag, the README headline count is 3,905, the five-seed table and level equation are correct, all 28 manifest hashes match, and the public TSA24 artifact is real. But rc4 does not meet the SoftwareX OSP bar: the replay does not run from the public artifact as documented; the Impact section has no impact evidence and the OSP “Illustrative examples” section is still missing; the metadata table is not the official C1–C9 table; the cited WS4 release still says MIT; provenance is contradictory in the rc4 tag tree and package docs; the official template is not applied; the package’s 3,979-word claim is wrong; and required declarations are absent. These are P0 issues, not copyedits.

**Prepared to review after revision:** **Yes**, if:
1. the replay runs from the public artifact with a documented command, environment, working directory, and expected output, and the “one-command”/next-step language is reconciled;
2. a substantive Impact section and a true Illustrative examples section are added, and the paper is cut to fit the 4,000-word cap including content-table bodies;
3. the licence is Apache-2.0 in the manuscript and the cited release, and the metadata table is rebuilt to the official C1–C9 layout including the reproducible-capsule row;
4. provenance is unified across the manuscript, [17], manifest, README, cover letter, release-candidate note, licensing note, and the rc4 tag tree;
5. the official `cas-sc` template is applied and CRediT/funding/competing-interest/corresponding-author metadata is added;
6. the objective description reports the mean level, flow reference period/equation, and AAC provenance, and the “flattest”/“four failure modes”/“without calling the optimizer” claims are corrected.

**Confidence:** High on the factual, licence, provenance, replay, table, and word-count findings (I recomputed hashes, counts, and arithmetic, and read the public releases and artifact). Moderate on the journal-fit and impact judgment; it is based on the official OSP template/guide and the paper’s own scope statements, not on external literature.

---

## QA checklist

- **Evidence-only:** Every substantive praise/critique above has an `MS`, `Table`, `Fig`, `TEX`, `EV`, `ARTIFACT`, `REL`, `MANIFEST`, `README`, `COVER`, or `NOTE` tag. No external literature was used. The official OSP template/guide is used only for format/section compliance, as stated in “Overrides.”
- **Anonymity/privacy:** No reviewer-identifying details or third-party personal information. The report is written for the authors and editor.
- **Tone:** Critical but professional; no sarcasm, no speculation about intent. The strongest language is reserved for verifiable factual errors (replay path, licence, provenance, word count).
- **Bias hygiene:** Critiques are anchored to content and evidence, not prestige, subfield preference, or personal factors.
- **Arithmetic:** Recomputed the five-seed mean/median/SD, Table 1/2 sums, 248×, 2.00e3, the level-term identity, the global level range, and the word counts. See the appendix.
- **Hashes:** Recomputed all 28 manifest hashes; all match. The manifest **status** is stale even though the hashes are correct.
- **Read-only:** No manuscript or evidence file was edited. The only file created is this report.

---

## Appendix: arithmetic and consistency checks

| Check | Result | Evidence |
|---|---|---|
| Five-seed mean / median / SD | 515.6818 → 515.682; median 515.938; SD 2.2338; range 6.0473 — correct for seeds 1–5 | `MS p5 Table 2`; `EV …r1`–`…r5` |
| Table 2 flow + level = objective | Correct for every row: 1.331+517.290=518.621; 0.000+512.574=512.574; 0.000+515.938=515.938; 0.000+514.746=514.746; 0.076+516.454=516.530 | `MS p5 Table 2` |
| Level-term identity | 20×100×(70,000,000−mean)/70,000,000 matches the reported level for all six seeds to machine precision | `EV …r1`–`…r7`; `MS p3 Eq. (4)` |
| Global realized level range | min 51.2126M (seed 1), max 52.4897M (seed 2) → 51.21–52.49M | `EV …r1`, `…r2` |
| Mean realized level (missing from Table 2) | 51.8948, 52.0599, 51.9422, 51.9839, 51.9241, 51.9701M for seeds 1–5, 7 | `EV …r1`–`…r7` |
| 248× factorized | 23.1236789 / 0.093149535 = 248.2426 → 248 | `EV paper/evidence/tsa24-factorized-ablation.json` |
| 2.00e3 evaluation path | 1.0863925 / 0.0005419086 = 2,004.75 → 2.00e3; displayed 1.09/0.542 ms = 2,011 → 2.01e3 | `EV evidence/ws4-tsa24-eval-ablation.json`; `MS p5 Table 3` |
| Absolute vs relative replay error | 3.725e-9 / 10,942,260.80 ≈ 3.4e-16 | `EV eval-ablation`; `MS p5 Table 3` |
| 1,000-gen objective | 8,588,725.37 → 8,588,730 at 6 s.f.; flow 8,588,225.55 → 8,588,230; level 499.8208 → 499.821 | `EV …1000-r7`; `MS p5 Table 1` |
| 1,000-gen “search” time | `time_to_best_s` = 9.3815; `run.search_seconds` is absent; wall 23.13 | `EV …1000-r7` |
| Five-seed wall sum | 804.004+799.646+797.826+796.314+798.116 = 3,995.9 s → 4.00e3 | `EV …r1`–`…r5`; `MS p5 l.312-313` |
| Word count | `count_words.py`: 3,865 main + 40 availability = 3,905; adding three content-table bodies ≈ 4,005; README says 3,979 | `count_words.py`; `README.md:16-19` |
| Abstract length | 173 words (README says 173) | `MS p1`; `README.md:24` |
| Manifest hashes | 28/28 match, including `softwarex_pdf` and `softwarex_manuscript` | `MANIFEST`; `sha256sum` |
| Release asset hash | `paper1-softwarex.pdf` asset `823e3c…` matches the manifest and local PDF | `REL p14-evidence-rc4`; `MANIFEST` |
| Licence | `LICENSE:1` = Apache-2.0; `pyproject.toml:12` = Apache-2.0; manuscript C3 says Apache-2.0; WS4 release body says MIT | `MS p7 Table 4 C3`; `LICENSE:1`; `pyproject.toml:12`; `REL ws4-v0.2.0-p14rc1` body |
| Public release assets | `p14-evidence-rc4` assets = 5 PDFs; no schedules/scripts/JSON; scripts are in the tagged tree | `REL p14-evidence-rc4` API |
| Replay path | `replay.py` expects `config/ws4/targets/evenflow_tsa24.yaml` and `build/compiled`; artifact has `evenflow_tsa24.yaml` and `compiled/` | `EV …r1/replay.py:16-18`; `ARTIFACT` tarball |
| Tag source provenance | rc4 tag target `8c25074`; tag root README says rc1; tagged manifest says no release; tag softwarex README says 3,874 | `REL p14-evidence-rc4` tree |
| Record schema | 10,000 record `run.generations = 0`; 1,000 record lacks `search_seconds`/`generations`; `instance.license = null`; no dataset/table hash | `EV …10000-r7`; `…1000-r7`; `…r1` |
| Artifact block count | 458,708 rows in `blocks.parquet`; 208,255 variables in campaign records | `ARTIFACT compiled/blocks.parquet`; `EV …r1/record.json` |

**End of report.**
