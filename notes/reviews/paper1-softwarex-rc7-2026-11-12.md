# Reviewer report — Paper 1, SoftwareX rc7

**Manuscript:** “WS4: a compiled-state software architecture with exact replay for landscape harvest scheduling”
**Target venue:** SoftwareX, Original Software Publication (OSP)
**Review copy:** `paper/submission/softwarex/paper1-softwarex.pdf` (10 PDF pages: 1 highlights page + 9 numbered pages; 2 figures; 3 content tables + the C1–C9 metadata table)
**Source:** `paper/submission/softwarex/paper1-softwarex.tex`
**Package:** `paper/submission/softwarex/README.md`, `paper/submission/softwarex/cover-letter.md`, `paper/release/manifest-v0.2.0-candidate.json`, `paper/release/RELEASE-CANDIDATE.md`, `LICENSING.md`, `README.md`, `paper/REPLAY.md`
**Public releases checked:** `p14-evidence-rc7` (papers repo, tag `ba257da`), `ws4-v0.2.0-p14rc1` (WS4 repo, tag `f60ce64`), `ws4-tsa24-evenflow-v1` (TSA24 artifact, asset SHA-256 `be8625…`)
**Previous review:** `notes/reviews/paper1-softwarex-rc4-2026-11-11.md`
**Review date:** 2026-11-12
**Reviewer stance:** independent antagonistic Reviewer 2 / associate editor. I checked only remaining submission blockers and regressions: public replay, SoftwareX section requirements, C1–C9 metadata/licence/capsule accuracy, provenance/assets/manifests, word/figure/page limits and template, and unsupported or stale claims. I did not re-run the campaigns.

**Verdict:** **Not submission-ready.**
**Recommendation:** **Major revision — do not submit rc7 to SoftwareX in its current form.** The scientific core and the headline replay arithmetic hold, and rc7 fixes the template and the “tested one-command” overclaim. The submission package does not: the documented public replay fails at the TSA24 step, required author declarations are absent, the metadata table’s capsule and licence rows are inaccurate, provenance is contradictory across the release and package docs, and the package’s own word count is wrong and likely over the cap.
**Prepared to review after revision:** **Yes**, if P0-1–P0-6 below are closed.
**Refereeing openly:** No.
**Include in annual reviewer list:** No.
**Confidence:** High on the replay, hash, word-count, metadata, licence, and provenance findings (I re-ran the replay, recomputed the hashes, and read the public release/assets). Moderate on the journal-fit and Impact judgment; it rests on the official OSP structure and the submission’s own scope statements.

---

## Top five residual issues

1. **The documented public replay still fails at the TSA24 step.** `paper/REPLAY.md:6-8` tells a reader to `git clone` the TSA24 repository and pass it as `TSA24_ROOT`. The default branch has no `compiled/` and no `evenflow_tsa24.yaml`; those files exist only in the `ws4-tsa24-evenflow-v1` release tarball. Following the instructions literally produces `FileNotFoundError: …/tsa24/evenflow_tsa24.yaml`. With the tarball extracted, `bash paper/replay_all.sh` replays all 11 records (`VALID`), so the arithmetic is sound; the setup instructions are not (`REPLAY.md:6-8`; `ARTIFACT`; `REL rc7` body; `check_benchmark_record.py:81-117`).
2. **The OSP section and declaration requirements are still not met.** §3 is “Validation and illustration,” not “Illustrative examples” (`TEX:262`); there is no command, configuration snippet, or expected output anywhere in the manuscript. §4 “Impact” is still a reuse/limitations section that explicitly disclaims adoption evidence (`TEX:409-447`). CRediT, funding, and competing-interest declarations are absent; the package’s own README lists them as blockers (`README.md:51-52`; `notes/plans/p15-final-submission-2026-11-12.md:22`).
3. **C3/C4/C8 in the metadata table are inaccurate.** C3 calls a public prerelease tag a “Permanent link to reproducible capsule”; the release is a prerelease with no DOI, and its assets are five PDFs plus `REPLAY.md`, not the evidence/schedules (`TEX:478`; `REL rc7`; the manuscript itself says “a DOI is still pending, so the replay contract is not yet an archival DOI service,” `TEX:444-445`). C4 says Apache-2.0, but the cited WS4 release body still says “Licence: MIT for repository code” (`TEX:479`; `REL ws4rc1`). C8 points to the repository root, not developer documentation (`TEX:483`).
4. **Provenance is still contradictory across the release, manifest, and package docs.** The rc7 tag’s root README says “P14 release candidate 4 (`p14-evidence-rc7`)” (`README.md:3`); the tagged manifest says “no tag/release created; public schedules/replay release pending” (`MANIFEST:24`); `RELEASE-CANDIDATE.md:3` says “local candidate only”; `LICENSING.md:12` names rc4; the SoftwareX README says the draft cites a commit, not a release, and that the evidence is private (`README.md:53-56`); the cover letter says the release is still “being prepared” with placeholder fields (`COVER:16-17`). The release body says “3,908 words” (`REL rc7`).
5. **The word count is wrong and the manuscript is likely over the 4,000-word cap.** `python3 count_words.py` prints 3,893 main + 40 availability = **3,933**, not the README/cover/release’s 3,908. Adding the three content-table bodies (27 + 36 + 32 tokens by the same tokenizer) gives about **4,028**, above the 4,000 cap. The README’s “including the three content-table bodies still gives 3,979” is false under either convention (`README.md:16-19`; `COVER:10`; `REL rc7` body).

---

## Overrides (project-specific constraints)

- Target journal: **SoftwareX, Original Software Publication**. The OSP structure used for compliance is five sections: Motivation and significance; Software description; Illustrative examples; Impact; Conclusions, with the mandatory C1–C9 code-metadata table. The guide’s length convention is 4,000 words excluding title/authors/affiliations/references/metadata tables, including abstract, running text, captions, and footnotes; maximum six figures (`notes/reviews/paper1-softwarex-rc4-2026-11-11.md:31`).
- The project’s own stop-ship list applies: public source/asset mismatch, replay failure on a headline table, and missing author/CRediT/funding/competing metadata are submission blockers (`notes/plans/p15-final-submission-2026-11-12.md:17-22`).
- All substantive praise and criticism is tied to the submission materials, evidence records, public releases, or the official template. No external literature was imported. The only file created by this review is this report; no manuscript, evidence, release, or package file was edited.

### Evidence tag key

| Tag | Meaning |
|---|---|
| `MS pX` | Manuscript printed page X (the unnumbered highlights page is not counted; printed page X is PDF page X+1) |
| `TEX:line` | LaTeX source line in `paper/submission/softwarex/paper1-softwarex.tex` |
| `Table N`, `Fig N` | Manuscript table/figure |
| `EV path` | Evidence record or script in the repository |
| `ARTIFACT path` | Extracted `ws4-tsa24-evenflow-v1` artifact |
| `REL rc7` | GitHub release `p14-evidence-rc7` |
| `REL ws4rc1` | GitHub release `ws4-v0.2.0-p14rc1` |
| `MANIFEST` | `paper/release/manifest-v0.2.0-candidate.json` |
| `README`, `COVER` | `paper/submission/softwarex/README.md`, `cover-letter.md` |

---

## Document inventory

| Material | Observation |
|---|---|
| `paper1-softwarex.pdf` | 10 pages: 1 highlights page + 9 numbered pages; 2 figures; 3 content tables + metadata table; 18 references. Official `cas-sc` class applied; page size 192 × 262 mm as the class specifies. |
| `paper1-softwarex.tex` | 504 lines. `cas-sc` document class, `cas-common.sty`, `cas-model2-names.bst`, and `elsarticle-num.bst` present. Title/author/affiliation/email/ corresponding-author mark are real. |
| Counted words | `python3 count_words.py` → 3,893 main + 40 availability = 3,933. Content-table bodies add about 95 tokens → about 4,028. |
| Abstract | 172–173 words. Within the 250-word limit but above the template’s “ca. 100” suggestion. |
| `README.md` | Stale: still describes an `elsarticle` build (`README.md:8-10`), gives 3,908/3,979 words (`README.md:16-19`), maps sections to “Validation/illustration; Reuse potential and limitations” (`README.md:29`), and lists already-public releases as placeholders/private (`README.md:53-56`). |
| `cover-letter.md` | Stale: 3,908 words; says the software/evidence release is “being prepared” with placeholder fields (`COVER:10, 16-17`). |
| `MANIFEST` | All 28 hashes match, including the SoftwareX PDF and TeX. `status` still says “candidate; no tag/release created; public schedules/replay release pending” (`MANIFEST:24`). |
| `REL rc7` | Public prerelease, tag `ba257da`, published 2026-11-12. Assets are five PDFs plus `REPLAY.md`; evidence, scripts, and manifests are in the tag’s source tree, not the release assets. The release body says “10 pages; 3,908 words” and claims replay prerequisites were fixed. |
| `REL ws4rc1` | Public prerelease, tag `f60ce64`, no assets. Body says “Licence: MIT for repository code,” contradicting `LICENSE:1` and `pyproject.toml:12` (Apache-2.0). |
| `ARTIFACT` | 4.66 MB `tar.gz`, SHA-256 `be8625…` matches `BENCHMARK_ARTIFACT.md`. Root contains `compiled/`, `evenflow_tsa24.yaml`, `seed_oldest_first_tsa24.csv`, `MANIFEST.sha256`. |

---

## P0 closure status (rc4 → rc7)

| # | Prior P0 | Status | Evidence |
|---|---|---|---|
| 1 | Public replay feasibility and prerequisites | **Still open** | `REPLAY.md:6-8` clones the TSA24 repo, which lacks the artifact files; literal run fails. Extracted tarball + tag clone replays 11/11. See M1. |
| 2 | Mandatory Impact section and Illustrative examples | **Still open** | `TEX:262` “Validation and illustration”; `TEX:409-447` Impact/Reuse/Limitations; no usage example; no adoption evidence. See M2. |
| 3 | Correct WS4 licence and metadata table | **Partially closed — table order fixed; capsule/licence rows not** | C1–C9 order is now correct (`TEX:476-484`). C3 is a prerelease, C4 is contradicted by `REL ws4rc1`, C8 points to the repo root. See M3. |
| 4 | Provenance/tag consistency across package and release | **Still open** | `README.md:3`; `MANIFEST:24`; `RELEASE-CANDIDATE.md:3`; `LICENSING.md:12`; `README.md:53-56`; `COVER:16-17`; `REL rc7` body. See M4. |
| 5 | 4,000-word / 6-figure structure and official template | **Partially closed — template applied; count wrong** | `cas-sc` is applied, 2 figures, 10 pages. Word count 3,933 / ~4,028, not 3,908/3,979. See M5. |
| 6 | Missing CRediT/funding/competing interests | **Still open** | No such text in `paper1-softwarex.tex` or the PDF; `README.md:51-52` lists them as blockers. See M2. |

---

## Confidential comments to the editor

**Recommendation: major revision; do not send this to production in its current form.**

rc7 is a real improvement in two places. The official `cas-sc` template is now applied, and the stale “tested one-command replay” claim has been removed from the manuscript. The C1–C9 table is now in the right order, the five-seed table and level equation remain correct, all 28 manifest hashes match, the release asset PDF is byte-identical to the submitted PDF, and the replay arithmetic itself is sound: with the TSA24 artifact extracted and the WS4 tag checked out, `bash paper/replay_all.sh` replayed all 11 records successfully.

The remaining failures are package and compliance failures, not experimental ones. The public replay instructions still cannot be followed literally: they clone the TSA24 repository, which does not contain the compiled artifact. The manuscript still has no “Illustrative examples” section, no command/config/output example, and no CRediT/funding/competing-interest declarations. C3 calls a prerelease a permanent capsule; C4 says Apache-2.0 while the cited WS4 release says MIT; C8 points at the repository root. The rc7 tag’s own README says “release candidate 4,” its manifest says no release was created, and the cover letter says the release is still being prepared. The package’s own word-count script contradicts the README, cover letter, and release body, and the manuscript appears to exceed 4,000 words once content tables are counted.

These are bounded fixes, but they are exactly the checks SoftwareX production and a careful reviewer will run. I would review a corrected version; I would not support submission of rc7.

---

# Comments to the authors

## Summary

The draft describes WS4, a compiled-state architecture for landscape harvest scheduling, and illustrates it on one frozen TSA24/Prince George instance with a five-seed 100,000-generation GPU campaign and exact CPU replay. The scientific claim boundary remains disciplined, the five-seed table and level equation are correct, the official template is now applied, and every headline schedule replays when the artifact is unpacked correctly. I found no new scientific regression in the headline tables; the blockers are package and compliance failures. The submission is not ready: the documented replay setup fails at the TSA24 step, the OSP “Illustrative examples” section and required declarations are absent, the metadata table’s capsule/licence/documentation rows are inaccurate, provenance is contradictory across the release and package, and the package’s word count is wrong and likely over the cap.

---

## What the draft does well

These are real strengths and should survive the revision.

1. **The replay arithmetic is sound.** With the TSA24 release tarball extracted and the WS4 tag checked out, `bash paper/replay_all.sh` replayed all 11 records: 2 FHOPS baselines and 9 TSA24 records, including the five campaign seeds and the CPU-SA baseline. The failure is in the setup documentation, not the evaluator (`REL rc7`; `ARTIFACT`; `EV evidence/`).
2. **The official `cas-sc` template is now applied.** The PDF uses the 192 × 262 mm `cas-sc` layout, 2 figures, 3 content tables, and the C1–C9 metadata table. The old two-column `elsarticle` mismatch is closed (`TEX:1`; `MS p1-p9`).
3. **The metadata table is now in the official C1–C9 order.** C1 current version, C2 code link, C3 capsule, C4 licence, C5 versioning, C6 languages, C7 compilation, C8 documentation, C9 support email (`TEX:476-484`). The left-column order is correct; several values are not.
4. **The five-seed table and level equation remain correct.** The mean 515.682 and median 515.938 are correct for seeds 1–5; flow + level = objective for every row; the level equation matches the records (`MS p5 Table 2`; `TEX:189-193`; `EV …r1`–`…r5`).
5. **The claim boundary is disciplined.** The abstract, results, and conclusions say there is no independent harvest-scheduling comparison, no state-of-the-art claim, and no environmental-modelling claim. The “tested one-command replay” overclaim is gone; the conclusions now say “a tested container replay” is a remaining step (`TEX:39-40, 404-407, 458-463`).
6. **Provenance hashes and asset identity are correct.** All 28 manifest hashes match, including the SoftwareX PDF and TeX. The `p14-evidence-rc7` `paper1-softwarex.pdf` asset is byte-identical to the submitted PDF (`7dd44d…`), and the tag’s TeX is byte-identical to the submitted source (`349793…`). The TSA24 tarball hash matches `BENCHMARK_ARTIFACT.md` (`be8625…`).

---

## Major comments

### M1. The documented public replay fails at the TSA24 step, even though the replay itself works

**Claim.** `paper/REPLAY.md:6-8` tells a reader to clone `https://github.com/UBC-FRESH/femic-tsa24-instance` and pass it as `TSA24_ROOT`. `REPLAY.md:20-23` then says the replay scripts accept the public artifact layout (`compiled/`, `evenflow_tsa24.yaml`) or the historical build layout. The release body says “replay prerequisites … point to this release” (`REL rc7` body).

**Evidence.**
- The default branch of `femic-tsa24-instance` has no `compiled/` and no `evenflow_tsa24.yaml` at its root; a recursive tree listing contains neither path. Those files are in the `ws4-tsa24-evenflow-v1` **release asset** tarball, whose root contains `./compiled/` and `./evenflow_tsa24.yaml`.
- I followed the documented route literally: `git clone … femic-tsa24-instance tsa24`, then `TSA24_ROOT=tsa24 … check_benchmark_record.py --replay evidence/ws4-tsa24-gpu-ga-100000-r1/record.json`. It failed with `FileNotFoundError: …/tsa24/evenflow_tsa24.yaml`.
- I then downloaded and extracted `ws4-tsa24-evenflow-v1.tar.gz` and set `TSA24_ROOT` to the extracted directory. The same replay returned `VALID: ws4-tsa24-gpu-ga-100000-r1 (tsa24-evenflow-w100)`.
- With the extracted artifact, the WS4 tag checkout, and a FHOPS clone, `bash paper/replay_all.sh` returned `VALID` for all 11 records. The WS4 `main` clone also replayed, so the tag is not strictly required for this check, but the docs do not pin it.
- `REL rc7` assets are five PDFs plus `REPLAY.md`; the schedules and scripts are in the tag’s source tree, not the assets. A reader who downloads only the assets does not get the replay material.

**Why it matters.** The paper’s central contribution is the replay contract. If a reader cannot follow the published instructions from a clean clone, the contract is a design, not a delivered result. This is a headline replay failure, which the project’s own stop-ship list treats as blocking (`notes/plans/p15-final-submission-2026-11-12.md:21`).

**Action.** Change `REPLAY.md` to download and extract the artifact, not clone the repository:

```bash
curl -L -o "$TSA24_ROOT.tar.gz" \
  https://github.com/UBC-FRESH/femic-tsa24-instance/releases/download/ws4-tsa24-evenflow-v1/ws4-tsa24-evenflow-v1.tar.gz
mkdir -p "$TSA24_ROOT"
tar xzf "$TSA24_ROOT.tar.gz" -C "$TSA24_ROOT"
```

Then set `TSA24_ROOT` to the extracted directory and verify `be8625…`. Pin the WS4 checkout to `ws4-v0.2.0-p14rc1` (or state that `main` also replays). Either attach an evidence/scripts tarball to `p14-evidence-rc7` or state explicitly “download the source archive at tag `p14-evidence-rc7`; the release assets are PDFs only.” Re-run the clean-clone test and include the log.

---

### M2. The OSP “Illustrative examples” section and the required declarations are still missing

**Claim.** The manuscript is structured as Motivation and significance; Software description; Validation and illustration; Impact; Conclusions (`TEX:54, 88, 262, 409, 449`). The Impact section says its impact is “measured in exact replay and reduced evaluation cost, not in adoption numbers” and then describes hypothetical teams (`TEX:411-419`). The package’s README says the content maps to “Validation/illustration; Reuse potential and limitations” (`README.md:29`).

**Evidence.**
- There is no “Illustrative examples” section. There is no command, configuration snippet, or expected output anywhere in the manuscript; a search for `gpu-run`, `python -m`, `bash`, `WS4_ROOT`, `TSA24_ROOT`, `lstlisting`, or `verbatim` returns nothing.
- The Impact section has no user, download, citation, teaching, commercial-use, or citable-publication evidence. Its first sentence explicitly disclaims adoption numbers. The “Reuse potential” subsection is a generic integration pattern; the “Limitations” subsection repeats the validation caveats (`TEX:421-447`).
- The Impact section refers to “the adapter” once (`TEX:414`) but the adapter interface is never described in §2. A reader cannot implement a component the paper does not define.
- No CRediT authorship contribution statement, funding statement, or competing-interest declaration appears in the TeX or PDF. The corresponding-author mark and email are present (`TEX:24-27`), but the other required declarations are not. The README itself lists them as blockers (`README.md:51-52`), and the project stop-ship list names missing author/CRediT/funding/competing metadata (`notes/plans/p15-final-submission-2026-11-12.md:22`).

**Why it matters.** SoftwareX publishes software because of its impact; the Impact section is a central review criterion, and the OSP structure expects an illustrative usage example. A validation-results section plus a reuse/limitations section will read as a relabeling exercise. Missing declarations are standard Elsevier production blockers.

**Action.** Add an “Illustrative examples” section with one `gpu-run` command, a small target/config snippet, and the expected record/replay output. Make the Impact section an actual case: if there are no external users yet, say so once, then argue the public artifact, exact replay/archival value for reviewers and instructors, the adapter pattern, and at least one worked workflow with inputs and outputs. Describe the adapter interface or remove the adapter claim. Add CRediT, funding (or “no external funding”), and competing-interest statements before submission. If the authors cannot make the impact case without overclaiming, JORS is the better venue.

---

### M3. C3/C4/C8 are not accurate, and the capsule is not a capsule

**Claim.** The metadata table says C3 is a “Permanent link to reproducible capsule,” C4 is “Apache-2.0 for WS4; the TSA24 artifact retains its own public terms,” and C8 is “Link to developer documentation” (`TEX:478-483`).

**Evidence.**
- **C3.** The link is `https://github.com/UBC-FRESH/fresh-solutions-papers/releases/tag/p14-evidence-rc7`. It is a public **prerelease**, not a DOI or archival capsule; the manuscript itself says “a DOI is still pending, so the replay contract is not yet an archival DOI service” (`TEX:444-445`). Its assets are five PDFs plus `REPLAY.md`; the evidence, schedules, and scripts are in the tag’s source tree, not the assets. A “permanent” link to a GitHub prerelease tag can be moved or deleted; it is not a reproducible capsule in the SoftwareX sense.
- **C4.** `LICENSE:1` is Apache-2.0 and `pyproject.toml:12` is `license = "Apache-2.0"`, so the manuscript value is correct for WS4. But `REL ws4rc1` (the release C2 points to) says “Licence: MIT for repository code; see the repository licence and the TSA24 artifact terms.” A reader who follows C2 sees the wrong licence. The TSA24 terms are also stated only vaguely; the artifact says MIT for code/documentation, CC BY 4.0 for derived benchmark artifacts, and OGL-BC for source data (`ARTIFACT README.md`; `BENCHMARK_ARTIFACT.md`).
- **C8.** The link is `https://github.com/UBC-FRESH/ws4`, the repository root. The repository has a `docs/` directory; the metadata row should point to developer documentation, not the root.
- **C2.** The “permanent link” is a release tag on a feature branch, not a DOI or a merged main-branch release. The release is a prerelease (`REL ws4rc1` body). This is not fatal if C3 is corrected and the prerelease status is stated, but “permanent” is overstated.
- **C7/C6 (minor).** C6 omits SciPy, which the paper uses; C7 does not give the CUDA/PyTorch versions or a concrete install command. These are completeness issues, not blockers.

**Why it matters.** SoftwareX requires an approved licence, an accurate metadata table, and a reproducible capsule/DOI. A wrong licence in the cited release is a factual error; calling a prerelease a permanent capsule is a hard metadata noncompliance. Either can delay or block production.

**Action.** Rebuild the metadata values: C3 either a DOI/archival capsule or “not yet available; public snapshot at `p14-evidence-rc7`”; C4 Apache-2.0 for WS4 and the precise TSA24 terms (MIT/CC BY 4.0/OGL-BC); C8 the `docs/` URL or docs site; C2 the tag plus commit and “prerelease, feature branch” status. Correct the `ws4-v0.2.0-p14rc1` release body to Apache-2.0, or cite a release whose body is correct. Move the replay command to “Data and code availability” and make it runnable.

---

### M4. Provenance is still contradictory across the release, manifest, and package docs

**Claim.** The manuscript cites `ws4-v0.2.0-p14rc1` and `p14-evidence-rc7` consistently (`TEX:255, 442-444, 476-478, 497-499`). The package should tell the same story.

**Evidence.**
- `README.md:3` says “Public release status: **P14 release candidate 4** (`p14-evidence-rc7`)” — the label and tag disagree.
- `MANIFEST:24` says “candidate; no tag/release created; public schedules/replay release pending.” rc7 is public.
- `RELEASE-CANDIDATE.md:3` says “local candidate only. No tag, release, visibility change, or DOI has been made.” False.
- `LICENSING.md:12` says the GitHub release candidate is `p14-evidence-rc4`. Stale.
- `paper/submission/softwarex/README.md:53-56` says the draft cites commit `f60ce64` on a feature branch, not a release, and that the evidence release is “currently private.” Both are false: the draft cites the tag, and rc7 is public.
- `cover-letter.md:16-17` says the software and evidence release are “being prepared” with placeholder repository/tag/DOI fields. False.
- `REL rc7` body says “10 pages; 3,908 words.” The page count is right; the word count is wrong (3,933 by the script).
- The rc7 tag’s source tree contains these stale files (the tag is `ba257da`, the current HEAD), so a reader who clicks C3 sees the contradictions.

**Why it matters.** A SoftwareX reviewer will click the links and compare them with the metadata. Contradictory provenance is a credibility problem even when the underlying artifact is good. The paper’s thesis is that identity and replay matter; the package should model that discipline.

**Action.** Pick one provenance statement and use it everywhere: “WS4 `ws4-v0.2.0-p14rc1`, a public prerelease tag at commit `f60ce64` on `feature/gpu-acceleration`; papers capsule `p14-evidence-rc7` at commit `ba257da`, public prerelease, DOI pending.” Update `README.md:3`, `MANIFEST:24`, `RELEASE-CANDIDATE.md:3`, `LICENSING.md:12`, `README.md:53-56`, `COVER:10-18`, and the release body. Re-cut the tag if the corrected files are not in the current tag, or add a corrected `README`/manifest to the release assets. Do not leave “rc4” in a file inside the rc7 tag.

---

### M5. The word count is wrong and the manuscript is likely over the 4,000-word cap

**Claim.** `README.md:16-19` says 3,908 counted words and “including the three content-table bodies still gives 3,979, below the 4,000-word cap.” `COVER:10` and the `REL rc7` body repeat 3,908.

**Evidence.**
- `python3 count_words.py` in `paper/submission/softwarex` prints `main text + captions: 3893`, `data availability: 40`, `total counted: 3933`. The package’s own verification command therefore contradicts the README by 25 words.
- The three content-table bodies contain 27, 36, and 32 tokens by the script’s tokenizer, about 95 tokens. Adding them to 3,933 gives about 4,028, above the 4,000 cap. Even if one excludes a handful of math tokens, the total is at or above 4,000.
- The README’s “3,979 including table bodies” is not reproducible from the current source; it is neither the script’s 3,933 nor the ~4,028 including tables.
- The official template is applied and the display-item count is fine: 2 figures (limit 6), 3 content tables plus the metadata table, 10 PDF pages including the highlights page and references.

**Why it matters.** A 4,000-word cap with a false internal count is a submission risk. The package’s own check is the first thing an editor or reviewer may run; it currently fails its own claim. If content-table bodies count, the manuscript is over the cap, not merely close.

**Action.** Re-count with a transparent convention. If the official convention includes content-table bodies, cut about 30–50 words (the scaling/microbenchmark material is the obvious place) and state the convention in the README. If the convention excludes table bodies, say so explicitly and stop claiming 3,979. Update `README.md:16-19`, `COVER:10`, and the release body to the final count. Consider shortening the 172-word abstract to leave margin.

---

### M6. The “four failure modes” claim is still stronger than the replay gate

**Claim.** The manuscript says the record format exposes four failure modes — a model change without a table rebuild, an irreversible move, a reported device objective, and a partial or infeasible schedule — and “None is silent in a record that passes the gate” (`TEX:244-246`). It also says the gate “checks the record fields without calling the optimizer” (`TEX:238`).

**Evidence.**
- `check_benchmark_record.py:151-166` validates the JSON schema, `result.exact_replay`, the schedule path, and the schedule SHA-256, then optionally runs the adjacent `replay.py` and compares its objective to the recorded objective. That is the gate.
- `ws4/opt/engine.py:93-128` (`load_schedule_csv`) only parses `block_id,treatment,offset`; it does not check coverage or candidate membership. `ws4/opt/incremental.py:362-392` (`IncrementalObjective.reset`) accumulates whatever schedule is loaded. I found no coverage or candidate-membership check in the gate.
- The records have `schedule_sha256` but no dataset/table hash; a stale compiled table would not be detected. The 10,000-generation record still has `run.generations = 0`; the 1,000-generation record lacks `run.search_seconds` and `run.generations`; campaign records have `instance.license = null`.
- `replay.py:10-18` imports and constructs `Optimizer` (`Optimizer.from_dataset`) and `IncrementalObjective`. The gate does not rerun the search, which is the important claim, but “without calling the optimizer” is not literally true.

**Why it matters.** The replay contract is the paper’s thesis. A gate that cannot detect a stale table or a partial schedule should not be described as exposing four failure modes with none silent. The claim is testable and currently false.

**Action.** Either implement the checks (coverage, candidate membership, dataset/table identity) or soften the paragraph to the one check the gate performs: “the gate verifies the recorded objective against the exact CPU replay and checks the schedule hash; it does not verify coverage, candidate membership, or model identity.” Say “without rerunning the search or using the GPU,” not “without calling the optimizer.” Fix the 10,000/1,000 record fields and add a dataset/table hash. Add the duplicate-run determinism evidence from `EV …10000-r7` (“two independent runs produced the identical schedule SHA-256”) to support the search-reproducibility claim.

---

## Minor comments

### Abstract, title, and front matter

1. `MS p1`: The abstract leads with the objective range (512.574–518.621) before saying there is no independent comparison. Lead with the software capability and replay contract; move the range to the illustrative example or qualify it in the same sentence as “one public instance, under a target-specific aspiration.”
2. `MS p1`: “248 times faster on CUDA than on a single-device CPU path” — add “4-cell batch evaluation” so the scope is in the abstract, not only the body.
3. `MS p1`: “against a deliberately unattainable 70M aspiration” is supported by `BENCHMARK_ARTIFACT.md:75-77`, but the manuscript never gives the 2025 AAC provenance (6,917,231 m³/year) that makes the 52M outcome interpretable. Add it in §3.
4. `MS p1`: The abstract is 172–173 words; the OSP template suggests ca. 100. Not a hard limit, but a shorter abstract leaves room for the missing declarations.
5. `MS p1`: The highlights are included as a separate first page in the manuscript. SoftwareX usually wants highlights as a separate submission file; consider removing the page from the manuscript PDF and submitting it separately.

### Software description

6. `TEX:185-186`: The even-flow target “compares each period with the reference period” but never states that the reference period is period 1 (`ARTIFACT evenflow_tsa24.yaml:6`). State it and give the flow penalty equation.
7. `TEX:189-193`: The level term is the sum of 20 per-period linear penalties in the implementation; the paper presents it as one mean-level equation. Say “the aggregate is equivalent to a mean-level penalty” or give the sum.
8. `TEX:197`: “selects the flattest profile” — the artifact says “selects the maximum even-flow level” (`BENCHMARK_ARTIFACT.md:75-77`). Within the ±1% band the flow penalty is zero, so “flattest” is imprecise; use the artifact’s wording or show a 20-period profile.
9. `TEX:238`: “without calling the optimizer” — see M6. Use “without rerunning the search.”
10. `TEX:255`: The environment lacks the CUDA version, PyTorch version, driver, and CPU RAM. For a software paper reporting 248× and 856 s, state them or point to a lockfile/container.

### Validation and illustration

11. `MS p4`: “its objective is 1,722,140,000, dominated by even-flow deviations” — the initial flow/level split is not reported. Either report it or say “the initial objective is dominated by flow” without the unsupported split.
12. `MS p5 Table 2`: Add a mean realized level column. The min–max ranges are useful but do not let a reader check the level term.
13. `MS p5 Table 1`: The 1,000-generation “search” time is `time_to_best_s` (9.3815), not a recorded `search_seconds`; the record has no `search_seconds`/`generations`. Label it `time_to_best_s` or fix the record.
14. `MS p5 Table 1`: The 10,000-generation record has `run.generations = 0`; this is a record-schema error. Fix the record or the schema.
15. `MS p5 Table 3`: The displayed 1.09 s / 0.542 ms gives 2.01×10³, not 2.00×10³. Report 1.086 s and 0.5419 ms, or say “about 2.0×10³ computed from unrounded values.” The “Error” column has no units or reference scale; add a relative-error column or state “absolute error 3.7×10⁻⁹ on a 1.09×10⁷ objective.”
16. `TEX:293`: “The level term remains between 499.821 and 517.290” sits in the seed-7 scaling subsection, but seed 7’s maximum is 515.141; 517.290 is seed 1. Say “across all reported runs” or use the seed-7 range 499.821–515.141.
17. `TEX:391`: “the same 64-genome batch” — there is no prior 64-genome batch in the paper. Say “a 64-genome batch.”
18. `TEX:406`: “The retained CPU simulated-annealing run is untuned…” — the paper no longer describes that run. Either cut the sentence or explain what “retained” refers to.
19. `TEX:394-395`: “maximum absolute error … 1.71×10⁻⁶ on both paths” — if the CPU path is the exact evaluator, its error should be zero. Name the reference evaluator and explain why both paths have the same nonzero error.
20. `TEX:334`: “The five-seed spread is small” — add the SD (≈2.23) or replace “small” with “a descriptive range of 6.05 objective units (1.2% of the mean).”

### Impact, limitations, conclusions

21. `TEX:414`: “wrap the heuristic in the adapter” — the adapter is not described anywhere else. Describe its interface or remove the claim.
22. `TEX:444-445`: “a DOI is still pending, so the replay contract is not yet an archival DOI service” — good and honest, but it directly contradicts C3’s “Permanent link to reproducible capsule.” Reconcile.
23. `TEX:458-463`: “not a leaderboard entry… not a competitive solver” is honest but reads as a disclaimer. In the Impact section, say what the software *does* enable, not only what it does not claim.

### Metadata and package

24. `TEX:477` (C2): The release tag is a prerelease, not a permanent DOI. Add the commit and “prerelease, feature branch” status, or use a DOI.
25. `TEX:479` (C4): State the TSA24 terms precisely (MIT/CC BY 4.0/OGL-BC), not “retains its own public terms.” Correct `REL ws4rc1` to Apache-2.0.
26. `TEX:481` (C6): Add SciPy. `TEX:482` (C7): Add CUDA/PyTorch versions and a concrete install command.
27. `TEX:483` (C8): Point to `https://github.com/UBC-FRESH/ws4/tree/main/docs` or the docs site, not the repository root.
28. `MS p8 Table 4` and `TEX:494-499`: The URLs break mid-word in the PDF (`relea ses`, `fresh -solutions`, `insta nce`, `ws4-v0.2. 0-p14rc1`). Use `xurl`/`\allowbreak` or a smaller font so the URLs remain copyable.
29. `README.md:8-10`: Still describes `elsarticle` and lists `elsarticle.cls`; the manuscript is `cas-sc`. Update the file list.
30. `README.md:16-19`: 3,908/3,979 are wrong; see M5.
31. `README.md:29`: The section mapping is wrong; the OSP structure is Motivation and significance; Software description; Illustrative examples; Impact; Conclusions.
32. `README.md:53-56`: The placeholder list is stale: the author/email are real, the code is tagged, and the evidence release is public. Replace with the actual remaining blockers (capsule/DOI, CRediT/funding/competing interests, Impact evidence, word count).
33. `COVER:10`: 3,908 — update to the final count.
34. `COVER:16-17`: “being prepared” and “placeholders” are false; name the actual releases, licence, and replay route.
35. `MANIFEST:24`: Update the status to the public rc7 state, or state that the manifest describes the frozen evidence snapshot while rc7 is the public release.
36. `RELEASE-CANDIDATE.md:3`: Update or archive; it says no tag/release was made.
37. `LICENSING.md:12`: Update rc4 → rc7.
38. `README.md:3`: “release candidate 4 (`p14-evidence-rc7`)” — make the label and tag agree.
39. PDF metadata: `Author` is blank. Set `\hypersetup{pdfauthor=...}` or the template equivalent before submission.
40. `paper1-softwarex.log`: Overfull `\hbox` (117 pt) at line 50. Check the highlights/title page layout.

---

## Risk table

| # | Risk | Likelihood | Impact | Evidence | Mitigation |
|---|---|---|---|---|---|
| R1 | Desk reject / reviewer failure because the documented replay does not run from a clean clone | High | Fatal | `REPLAY.md:6-8`; `ARTIFACT`; `check_benchmark_record.py:81-117` | Download/extract the artifact; pin the WS4 tag; test from clean clone; attach evidence or state the source-archive route |
| R2 | Missing CRediT/funding/competing interests and no “Illustrative examples” section | Certain | Fatal | `TEX:262, 409-447`; `README.md:51-52`; `notes/plans/p15…:22` | Add declarations and a usage example; make Impact an impact case |
| R3 | Metadata/licence: C3 prerelease as capsule; C4 contradicted by WS4 release body; C8 root link | Certain | Fatal | `TEX:478-483`; `REL ws4rc1`; `LICENSE:1`; `pyproject.toml:12` | Rebuild C3/C4/C8/C2; correct the release body; state TSA24 terms |
| R4 | Provenance contradictions: rc7 tag README says rc4; manifest says no release; cover letter says “being prepared” | Certain | Major | `README.md:3`; `MANIFEST:24`; `RELEASE-CANDIDATE.md:3`; `LICENSING.md:12`; `README.md:53-56`; `COVER:16-17` | One provenance statement everywhere; re-cut the tag or add corrected files |
| R5 | Word count over the 4,000 cap; package’s own script contradicts README/cover/release | High | Major | `count_words.py`; `README.md:16-19`; `COVER:10`; `REL rc7` body | Re-count transparently; cut ~30–50 words; update all counts |
| R6 | “Four failure modes / none silent” overclaim; gate does not check coverage, candidate membership, or dataset identity | Medium–High | Major | `TEX:244-246`; `check_benchmark_record.py:151-166`; `ws4/opt/engine.py:93-128`; `ws4/opt/incremental.py:362-392` | Implement checks or soften the paragraph; add dataset/table hash |
| R7 | Record hygiene: 10k `generations=0`; 1k `search_seconds`/`generations` missing; `instance.license=null`; no dataset hash | Medium | Major | `EV …10000-r7`; `…1000-r7`; `…r1` | Fix schema/records; populate fields |
| R8 | Single landscape, no spatial constraints, no baseline: example does not demonstrate the distinguishing spatial feature | High | Major | `TEX:432-438`; `NOTE ws4/AGENTS.md` | Add a spatial stress case or reframe §3 as a functionality/replay example |
| R9 | Objective description incomplete: no flow equation/reference period, no AAC provenance, no mean level in Table 2 | Medium | Major | `TEX:185-197`; `ARTIFACT evenflow_tsa24.yaml:1-12`; `MS p5 Table 2` | Add flow equation, period 1, AAC, mean-level column |
| R10 | Public capsule assets do not contain the evidence/schedules; a reader who downloads assets cannot replay | High | Major | `REL rc7` assets; `REPLAY.md:20-23` | Attach an evidence/scripts tarball or document the source-archive route |

---

## P0 / P1 / P2 remediation list

### P0 — must be resolved before submission

1. **Make the documented replay work from the public artifact.** Replace the TSA24 clone instruction with download + extract of `ws4-tsa24-evenflow-v1.tar.gz`, verify `be8625…`, pin the WS4 tag, and test from a clean clone. Either attach evidence/scripts to the rc7 release or state “download the source archive at tag `p14-evidence-rc7`; assets are PDFs only.” Update `REPLAY.md` and the release body (`REPLAY.md:6-8, 20-23`; `REL rc7`).
2. **Add the missing OSP sections and declarations.** Add “Illustrative examples” with one command, a config snippet, and expected output. Make Impact an impact case, not a reuse/limitations section. Add CRediT, funding, and competing-interest statements (`TEX:262, 409-447`; `README.md:51-52`; `notes/plans/p15…:22`).
3. **Correct C3/C4/C8/C2 and the WS4 release body.** C3 a DOI/archival capsule or “not yet available; public snapshot at rc7”; C4 Apache-2.0 plus precise TSA24 terms; C8 docs URL; C2 tag + commit + prerelease status. Correct `REL ws4rc1` to Apache-2.0 (`TEX:476-484`; `REL ws4rc1`; `LICENSE:1`; `pyproject.toml:12`).
4. **Unify provenance across the release, manifest, and package.** Update `README.md:3`, `MANIFEST:24`, `RELEASE-CANDIDATE.md:3`, `LICENSING.md:12`, `README.md:53-56`, `COVER:10-18`, and the release body. Re-cut the tag if the corrected files are not in `ba257da`.
5. **Re-count and fit the 4,000-word cap.** Use `count_words.py` and state the convention; include content-table bodies; cut ~30–50 words; update README, cover letter, and release body (`README.md:16-19`; `COVER:10`; `REL rc7` body).
6. **Reconcile the “four failure modes” claim with the gate.** Implement coverage/candidate-membership/dataset-identity checks or soften the paragraph; fix “without calling the optimizer”; fix the 10k/1k record fields (`TEX:238, 244-246`; `check_benchmark_record.py:151-166`; `EV …10000-r7`; `…1000-r7`).

### P1 — major revision

7. Add the flow penalty equation and state the reference period (period 1); state that the level term is the sum of 20 per-period penalties (`TEX:185-193`; `ARTIFACT evenflow_tsa24.yaml:1-12`).
8. Add the 70M AAC provenance (2025 AAC 6,917,231 m³/year) and interpret the 52M gap (`TEX:195-197`; `ARTIFACT evenflow_tsa24.yaml:1-2`).
9. Add the mean realized level to Table 2; add SD or replace “small” (`MS p5 Table 2`; `TEX:334`).
10. Describe or remove the adapter claim (`TEX:414`).
11. Add a spatial-constraint/stress case or reframe §3 as a functionality/replay example and move the objective range out of the abstract’s lead (`TEX:432-438`).
12. Fix record schema/identity: `run.generations`, `search_seconds`, `instance.license`, dataset/table hash (`EV …10000-r7`; `…1000-r7`; `…r1`).
13. Add CUDA/PyTorch versions, driver, CPU RAM, and a concrete install command (`TEX:255`; `TEX:482`).
14. Add the duplicate-run determinism evidence (`EV …10000-r7`) to support the search-reproducibility claim.

### P2 — minor / clarity

15. Fix the 2.00×10³ vs 2.01×10³ precision and define the error reference/scale (`MS p5 Table 3`).
16. Fix “the same 64-genome batch” → “a 64-genome batch”; “4-cell batch evaluation” in the abstract (`TEX:391`; `MS p1`).
17. Label the 1,000-generation value as `time_to_best_s`, not search time (`MS p5 Table 1`; `EV …1000-r7`).
18. Fix the seed-7 level range 499.821–517.290 (`TEX:293`).
19. Fix the initial objective split claim (`MS p4`).
20. Fix URL line breaks in Table 4 and Data availability (`MS p8`; `TEX:494-499`).
21. Set PDF author metadata; check the 117 pt overfull box (`paper1-softwarex.log`).
22. Consider a 20-period flow/level profile figure or a software screenshot; the 3-point scaling figure is a weak use of the 6-figure budget (`Fig 2`).
23. Move highlights to a separate file if the journal requires it (`MS p1`).
24. Add an existing-software comparison to the introduction (`MS p1-p2`).

---

## Recommendation and review-after-revision statement

**Recommendation:** **Major revision for SoftwareX. Do not submit rc7.**

**Basis.** The software and the core idea are credible. rc7 genuinely fixes the template and removes the “tested one-command” overclaim. The five-seed table, level equation, manifest hashes, asset identity, and replay arithmetic all hold. But the submission does not meet the SoftwareX OSP bar: the documented replay fails at the TSA24 step; the “Illustrative examples” section and required declarations are missing; C3 calls a prerelease a permanent capsule; C4 is contradicted by the cited WS4 release body; C8 points at the repository root; provenance is contradictory across the release and package; and the package’s word count is wrong and likely over the cap. These are P0 issues, not copyedits.

**Prepared to review after revision:** **Yes**, if:
1. the replay runs from the public artifact with a documented download/extract step, a pinned WS4 tag, a working directory, environment variables, and expected output, and the replay material is either in the capsule assets or explicitly routed to the tag source archive;
2. a true “Illustrative examples” section and a substantive Impact section are added, and CRediT/funding/competing-interest declarations are present;
3. C3/C4/C8/C2 and the WS4 release body are accurate, with a DOI/archival capsule or an honest “not yet available” statement;
4. provenance is unified across the manuscript, `README.md`, `MANIFEST`, `RELEASE-CANDIDATE.md`, `LICENSING.md`, the SoftwareX README, the cover letter, and the rc7 tag tree;
5. the word count is re-derived with a transparent convention, the manuscript fits 4,000 words including content-table bodies, and README/cover/release counts agree;
6. the “four failure modes” paragraph is reconciled with what the gate actually checks, and the 10k/1k record fields are fixed.

**Confidence:** High on the replay, hash, word-count, metadata, licence, and provenance findings (I re-ran the replay, recomputed the hashes, and read the public release/assets). Moderate on the journal-fit and Impact judgment; it is based on the official OSP structure and the paper’s own scope statements, not external literature.

---

## QA checklist

- **Evidence-only:** Every substantive praise/critique above has an `MS`, `TEX`, `EV`, `ARTIFACT`, `REL`, `MANIFEST`, `README`, or `COVER` tag. No external literature was used. The official OSP structure is used only for format/section compliance, as stated in “Overrides.”
- **Anonymity/privacy:** No reviewer-identifying details or third-party personal information. The report is written for the authors and editor.
- **Tone:** Critical but professional; no sarcasm, no speculation about intent. The strongest language is reserved for verifiable factual errors (replay setup, licence, capsule, provenance, word count).
- **Bias hygiene:** Critiques are anchored to content and evidence, not prestige, subfield preference, or personal factors.
- **Read-only:** No manuscript, evidence, release, or package file was edited. The only file created is this report. Temporary clones and the artifact extraction were made under the approved `.opencode/tmp/opencode` workspace.
- **Hashes:** All 28 manifest hashes match; the release PDF and tag TeX are byte-identical to the submission; the TSA24 tarball hash matches `BENCHMARK_ARTIFACT.md`.
- **Replay:** Literal documented route fails at the TSA24 clone. With the extracted artifact and tag checkout, 11/11 records replay `VALID`.

---

## Appendix: verification log

| Check | Result | Evidence |
|---|---|---|
| PDF page count | 10 PDF pages: 1 highlights + 9 numbered | `pdfinfo paper1-softwarex.pdf` |
| Figures / tables | 2 figures; 3 content tables + metadata table | `TEX`; `MS p1-p9` |
| Template | `cas-sc` 192 × 262 mm, official class | `TEX:1`; `cas-sc.cls:169-180` |
| Word count | 3,893 main + 40 availability = 3,933; ~4,028 incl. content tables | `python3 count_words.py`; table token count |
| README/cover/release count | 3,908 and 3,979 | `README.md:16-19`; `COVER:10`; `REL rc7` body |
| Manifest hashes | 28/28 match | `sha256sum` vs `MANIFEST` |
| Release PDF identity | `7dd44da9…` matches manifest and submission | `REL rc7` asset; local PDF |
| Tag TeX identity | `34979379…` matches submission | `git show ba257da:paper/submission/softwarex/paper1-softwarex.tex` |
| TSA24 tarball hash | `be8625…` matches `BENCHMARK_ARTIFACT.md` | `ARTIFACT` |
| Documented replay | Fails: `FileNotFoundError …/tsa24/evenflow_tsa24.yaml` | `REPLAY.md:6-8`; default branch tree |
| Extracted-artifact replay | `VALID: ws4-tsa24-gpu-ga-100000-r1` | `check_benchmark_record.py --replay` |
| Full replay | 11/11 `VALID` (2 FHOPS + 9 TSA24) | `bash paper/replay_all.sh` |
| WS4 tag checkout | `f60ce64`; replay works | `git clone --branch ws4-v0.2.0-p14rc1` |
| WS4 main checkout | `18f3bce`; replay also works | `git clone` default branch |
| WS4 licence | `LICENSE:1` Apache-2.0; `pyproject.toml:12` Apache-2.0 | local WS4 tag |
| WS4 release body | Says “MIT for repository code” | `REL ws4rc1` |
| rc7 assets | 5 PDFs + `REPLAY.md`; no evidence/scripts | `REL rc7` API |
| rc7 tag README | “P14 release candidate 4 (`p14-evidence-rc7`)” | `README.md:3` |
| Manifest status | “no tag/release created” | `MANIFEST:24` |
| Declarations | No CRediT/funding/competing text | `grep` on TeX/PDF |
| Usage example | No command/config/output | `grep` on TeX |
| Four-failure-mode gate | Schema/path/hash/objective only; no coverage/dataset identity | `check_benchmark_record.py:151-166`; `ws4/opt/engine.py:93-128`; `ws4/opt/incremental.py:362-392` |
| Record hygiene | 10k `generations=0`; 1k missing `search_seconds`/`generations`; `license=null` | `EV …10000-r7`; `…1000-r7`; `…r1` |

**End of report.**
