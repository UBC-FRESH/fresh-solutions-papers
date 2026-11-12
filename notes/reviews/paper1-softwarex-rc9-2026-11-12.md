# Reviewer report — Paper 1, SoftwareX rc9

**Manuscript:** “WS4: a compiled-state software architecture with exact replay for landscape harvest scheduling”
**Target venue:** SoftwareX, Original Software Publication (OSP)
**Review copy:** `paper/submission/softwarex/paper1-softwarex.pdf` (10 PDF pages: 1 highlights page + 9 numbered pages; 2 figures; 3 content tables + the C1–C9 metadata table)
**Source:** `paper/submission/softwarex/paper1-softwarex.tex`
**Package:** `paper/submission/softwarex/README.md`, `paper/submission/softwarex/cover-letter.md`, `paper/release/manifest-v0.2.0-candidate.json`, `paper/release/RELEASE-CANDIDATE.md`, `LICENSING.md`, `README.md`, `paper/REPLAY.md`
**Public releases checked:** `p14-evidence-rc9` (papers repo, tag `dc2acdb`, public prerelease), `ws4-v0.2.0-p14rc1` (WS4 repo, public prerelease), `ws4-tsa24-evenflow-v1` (TSA24 artifact, SHA-256 `be8625…`)
**Previous review:** `notes/reviews/paper1-softwarex-rc7-2026-11-12.md`
**Review date:** 2026-11-12
**Reviewer stance:** independent antagonistic Reviewer 2 / associate editor. Final submission gate: I checked only remaining blockers and regressions. I re-ran the public replay, recomputed the manifest hashes, checked the rc9 release/assets, the C1–C9 table, the package prose, and the word-count convention. I did not re-run the search campaigns.

**Verdict:** **Not submission-ready.** rc9 closes the rc7 replay failure: the documented TSA24 tarball route now replays all 11 records `VALID`, and the WS4 release body, C3/C4/C8, the manifest hashes, and the rc9 PDF asset identity are correct. Four residual blockers remain: the manuscript is over the 4,000-word cap once content-table bodies are counted (3,977 + 105 = 4,082 under the journal’s stated convention); CRediT, funding, and competing-interest declarations are still absent; the rc9 tag’s own package prose still says rc8 / “local candidate only” / “release being prepared” / author placeholder and cites commit `f60ce64` rather than the released tag; and the OSP Impact and Illustrative example sections are still a reuse/limitations discussion and a one-paragraph replay instruction with no input, configuration, or output block. The scientific core, replay arithmetic, hashes, and C1–C9 table are otherwise sound; the remaining work is bounded, but this is not yet a submission package.

**Recommendation:** **Major revision — do not submit rc9.**
**Prepared to review after revision:** **Yes**, if P0-1–P0-4 below are closed.
**Refereeing openly:** No.
**Include in annual reviewer list:** No.
**Confidence:** High on the replay, hash, word-count, declaration, metadata, licence, and provenance findings. Moderate on the Impact judgment; it rests on the official OSP structure and the submission’s own scope statements.

---

## Overrides (project-specific constraints)

- Target journal: **SoftwareX, Original Software Publication**. The OSP structure is five sections: Motivation and significance; Software description; Illustrative examples; Impact; Conclusions, with the mandatory C1–C9 code-metadata table. The length convention is 4,000 words excluding title, authors, affiliations, references, and metadata tables, and including abstract, running text, captions, and footnotes; maximum six figures (`SoftwareX Guide for Authors`, accessed 2026-11-12; `notes/reviews/paper1-softwarex-rc4-2026-11-11.md:31`).
- The project’s own stop-ship list applies: replay failure on a headline table, public source/asset mismatch, and missing author/CRediT/funding/competing metadata are submission blockers (`notes/plans/p15-final-submission-2026-11-12.md:17-22`).
- All substantive praise and criticism is tied to the submission materials, evidence records, public releases, or the official template. No external literature was imported. The only file created by this review is this report; no manuscript, evidence, release, or package file was edited. Replay artifacts were created under `.opencode/tmp/opencode`.

### Evidence tag key

| Tag | Meaning |
|---|---|
| `MS pX` | Manuscript printed page X (the unnumbered highlights page is not counted; printed page X is PDF page X+1) |
| `TEX:line` | LaTeX source line in `paper/submission/softwarex/paper1-softwarex.tex` |
| `Table N`, `Fig N` | Manuscript table/figure |
| `EV path` | Evidence record or script in the repository |
| `ARTIFACT` | Extracted `ws4-tsa24-evenflow-v1` artifact |
| `REL rc9` | GitHub release `p14-evidence-rc9` |
| `REL ws4rc1` | GitHub release `ws4-v0.2.0-p14rc1` |
| `MANIFEST` | `paper/release/manifest-v0.2.0-candidate.json` |
| `README`, `COVER` | `paper/submission/softwarex/README.md`, `cover-letter.md` |

---

## Residual blockers (P0)

### P0-1. The manuscript is over the 4,000-word cap under the journal’s convention

**Evidence.** `python3 count_words.py` prints 3,937 main + 40 availability = **3,977** (`README.md:16-18`; `COVER:10`; `REL rc9` body). The script deliberately strips `tabular` environments (`count_words.py:5-8,40-42`), so it excludes the three content-table bodies. Those bodies contain 27 + 42 + 36 = **105** tokens (`TEX:304-313`; `TEX:345-356`; `TEX:379-388`). Under the SoftwareX convention, only **metadata** tables are excluded; content-table text is not. The current total is therefore **4,082**, about 82 words over the cap. The package no longer claims 3,979 is below the cap, but it still reports 3,977 as the length without stating that it is using a non-journal convention (`README.md:16-18`; `paper/README.md:11-12`).

**Why it matters.** The journal states a maximum of 4,000 words with a specific inclusion list. A package whose own verification script contradicts the journal’s convention is a production/desk-check risk, and the paper is over the limit rather than merely close.

**Action.** Cut at least ~85 words from running text (the scaling/microbenchmark prose is the obvious place), or move the content-table bodies to a supplement. Re-count with the journal convention, state the convention in `README.md`, and update `COVER:10` and the `REL rc9` body.

### P0-2. Required author declarations are still absent

**Evidence.** No CRediT authorship contribution statement, funding statement, or competing-interest declaration appears in the TeX or PDF; the back matter contains only the Code metadata table and Data and code availability (`TEX:472-506`; `MS p8-p9`). The package itself lists them as blockers (`README.md:50-51`), and the project stop-ship list treats missing CRediT/funding/competing metadata as blocking (`notes/plans/p15-final-submission-2026-11-12.md:22`). The corresponding author and email are real, but that does not satisfy the declaration requirement.

**Why it matters.** These are standard Elsevier/SoftwareX production requirements and an explicit project stop-ship condition. Their absence is not a formatting preference.

**Action.** Add a CRediT statement, a funding statement (or “no external funding”), and a competing-interest declaration to the manuscript back matter. Update `README.md:50-51` so the blocker list reflects what is actually missing. If the submission system captures these fields instead, remove the stale placeholder and say where they are recorded.

### P0-3. Provenance and version statements inside the rc9 tag still contradict the manuscript and the public release

**Evidence.** The rc9 tag is `dc2acdb`, public, and is cited correctly in the manuscript (`TEX:255,483-485,505`; `REL rc9`). The package prose does not match:

- `README.md:3` says “P14 release candidate **8** (`p14-evidence-rc9`)” — label and tag disagree.
- `MANIFEST:24` says “public release candidate `p14-evidence-rc8`” — stale.
- `paper/release/RELEASE-CANDIDATE.md:3` says “local candidate only. No tag, release, visibility change, or DOI has been made” — false; rc9 is public.
- `README.md:50-56` still says the author/email are placeholders (`author@example.invalid`), the draft cites commit `f60ce64` on a feature branch rather than a release, the evidence release is “currently private,” and the documentation URL/support email are missing. All are false for rc9: the author/email are real (`TEX:23-26`), C1/C2 cite the `ws4-v0.2.0-p14rc1` tag (`TEX:483-484`), rc9 is public, and C8/C9 give the docs URL and email (`TEX:490-491`).
- `COVER:16-18` says the software/evidence release is “being prepared” and the repository/tag/DOI fields are “placeholders until that release is approved” — false; rc9 is published and the manuscript cites it.
- `paper/REPLAY.md:6` clones the default branch of WS4 rather than the cited `ws4-v0.2.0-p14rc1` tag; the replay works with `main` today, but the documented route is not version-locked to the paper.

**Why it matters.** A SoftwareX reviewer will click C3 and read the tag’s own README. A package that says “rc8” for an rc9 tag, “no release” for a public release, and “private” for a public capsule undermines the paper’s central identity/replay claim. This was a P0 in rc7 and is still open.

**Action.** Use one provenance statement everywhere: “Papers capsule `p14-evidence-rc9`, tag `dc2acdb`, public prerelease, DOI pending; WS4 `ws4-v0.2.0-p14rc1`, public prerelease at `f60ce64`.” Update `README.md:3`, `MANIFEST:24`, `RELEASE-CANDIDATE.md:3`, `README.md:50-56`, and `COVER:16-18`. Re-cut the tag if the corrected files are not in `dc2acdb`, or add corrected files to the release assets. Pin `REPLAY.md` to the cited WS4 tag, or state explicitly that `main` also replays.

### P0-4. The OSP Impact and Illustrative example sections still do not demonstrate software use

**Evidence.**

- **Impact.** The section opens by disclaiming adoption evidence — “measured in exact replay and reduced evaluation cost, not in adoption numbers” — then describes hypothetical teams (`TEX:416-426`; `MS p7`). It is followed by “Reuse potential” and “Limitations” (`TEX:428-445`). There is no user, download, citation, teaching, commercial-use, or concrete worked-reuse evidence. The “adapter” is mentioned once (`TEX:420-421`) but is not defined in §2. This is a reuse/limitations discussion, not an impact case.
- **Illustrative example.** The new §4 is one prose paragraph: extract the TSA24 tarball, clone WS4, set `WS4_ROOT`, `TSA24_ROOT`, and `FHOPS_ROOT`, run `bash paper/replay_all.sh`, expect `VALID` (`TEX:409-414`; `MS p6`). There is no command block, no configuration snippet, no actual output, and no example of the compile/build-table/search workflow. It demonstrates replay only, not the software in action.

**Why it matters.** SoftwareX publishes software because of its impact, and the OSP structure expects an illustrative usage example. The current sections satisfy the headings but not the demonstration requirement.

**Action.** Make Impact concrete: cite actual users, downloads, citations, teaching use, or commercial reuse; if none exist, say so once and then give a concrete worked reuse case with inputs, outputs, and cost, rather than generic hypothetical teams. Define or remove the adapter claim. Expand the Illustrative example with a `verbatim`/`lstlisting` block containing one real `gpu-run` command, a minimal target/config snippet, and the observed `VALID` output (or a record excerpt).

---

## What now passes (verification, not blockers)

| Check | Result | Evidence |
|---|---|---|
| Public replay from documented route | 11/11 `VALID` (2 FHOPS + 9 TSA24), including five campaign seeds and the CPU-SA baseline | `REPLAY.md:5-22`; extracted artifact SHA-256 `be8625…`; `bash paper/replay_all.sh` |
| TSA24 artifact hash | `be8625804b2a…` matches `BENCHMARK_ARTIFACT.md` | `ARTIFACT` |
| Manifest hashes | All 28 entries match, including `softwarex_manuscript` and `softwarex_pdf` | `MANIFEST`; recomputed `sha256sum` |
| Release asset identity | rc9 `paper1-softwarex.pdf` SHA-256 `9774a938…` is byte-identical to the submission | `REL rc9`; local PDF |
| Template and page count | Official `cas-sc` bundle; 10 PDF pages (1 highlights + 9 numbered); 2 figures; 3 content tables + metadata table | `TEX:1`; `pdfinfo`; `MS p1-p9` |
| C1–C9 table | All nine rows present and in order; C4 now Apache-2.0 (matching `LICENSE:1` and `pyproject.toml:12`); C8 now `docs/`; C3 honestly labelled “prerelease; DOI pending” | `TEX:483-491`; `REL ws4rc1` body now says Apache-2.0 |
| DOI / container | DOI pending and container replay untested, but both are disclosed as post-release steps | `TEX:451-452,466-467`; `REL rc9` body |

---

## Confidential comments to the editor

**Recommendation: major revision; do not send rc9 to production.**

rc9 is a genuine improvement. The documented replay now works from the public TSA24 tarball (11/11 `VALID`), the WS4 release body says Apache-2.0, C4 and C8 are corrected, C3 no longer calls a prerelease a permanent capsule, and every manifest hash and the release PDF identity match. The scientific claim boundary remains disciplined.

The remaining blockers are package and compliance failures, not experimental ones: the word count is over the cap once content-table bodies are counted; CRediT/funding/competing-interest declarations are absent; the rc9 tag’s own README, manifest, release-candidate note, SoftwareX README, and cover letter still describe rc8, “no release,” “private” evidence, or a “release being prepared”; and the Impact/Illustrative sections still read as reuse/limitations plus a replay instruction rather than a demonstrated software case. These are bounded, and I would review a corrected version, but they are exactly the checks SoftwareX production and a careful reviewer will run.

---

## Comments to the authors

### Summary

The paper describes WS4, a compiled-state architecture for landscape harvest scheduling, and illustrates it on one frozen TSA24/Prince George instance with a five-seed 100,000-generation GPU campaign and exact CPU replay. The replay arithmetic, manifest hashes, asset identity, and C1–C9 table are sound, and the documented public replay now succeeds. The submission is not ready because the word count, required declarations, package provenance, and Impact/Illustrative demonstration still fall short of the SoftwareX OSP bar. The fixes are bounded; no new scientific regression was found.

### Major comments

1. **Fit the 4,000-word cap under the journal convention** (`README.md:16-18`; `count_words.py:5-8,40-42`; `TEX:304-313,345-356,379-388`; `COVER:10`; `paper/README.md:11-12`). The script’s 3,977 excludes content-table bodies; adding the 105 table tokens gives 4,082. Cut ~85 words or move table bodies to a supplement, then update every count.
2. **Add CRediT, funding, and competing-interest declarations** (`TEX:472-506`; `MS p8-p9`; `README.md:50-51`; `notes/plans/p15-final-submission-2026-11-12.md:22`). The package itself lists them as blockers.
3. **Unify provenance across the rc9 tag** (`README.md:3`; `MANIFEST:24`; `RELEASE-CANDIDATE.md:3`; `README.md:50-56`; `COVER:16-18`; `REPLAY.md:6`). The tag is `dc2acdb`, rc9, public; the prose still says rc8, “local candidate only,” “private,” and “being prepared.” Pin the WS4 tag in `REPLAY.md` or state that `main` also replays.
4. **Turn Impact and Illustrative example into a demonstrated case** (`TEX:409-426`; `MS p6-p7`). Impact needs concrete evidence or a concrete worked reuse case; the example needs a command/config/output block and should show more than replay.

### Minor comments

No minor comments are listed; cosmetic issues were intentionally excluded from this submission gate.

---

## QA checklist

- **Evidence-only:** Every substantive point above has an `MS`, `TEX`, `EV`, `ARTIFACT`, `REL`, `MANIFEST`, `README`, or `COVER` tag. The only external source is the SoftwareX Guide for Authors, used solely for the 4,000-word convention.
- **Anonymity/privacy:** No reviewer-identifying details or third-party personal information. The report is written for the authors and editor.
- **Tone:** Critical but professional; no sarcasm, no speculation about intent.
- **Bias hygiene:** Critiques are anchored to content and evidence, not prestige, subfield preference, or personal factors.
- **Read-only:** No manuscript, evidence, release, or package file was edited. The only file created is this report.
- **Hashes and replay:** All 28 manifest hashes match; the rc9 PDF asset is byte-identical to the submission; the documented replay route returned 11/11 `VALID`.

**End of report.**
