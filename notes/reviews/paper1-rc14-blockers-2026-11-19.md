# Reviewer report — Paper 1, SoftwareX rc14 (major-blocker review)

**Manuscript:** “WS4: a compiled-state software architecture with exact replay for landscape harvest scheduling”
**Target:** SoftwareX, Original Software Publication (OSP)
**Review copy:** `paper/submission/softwarex/paper1-softwarex.pdf` (10 PDF pages: 1 highlights page + 9 numbered pages; 3 figures; Table 1 plus the C1–C9 metadata table; 1-page supplement)
**Release checked:** papers `p14-evidence-rc14` (`5f9d65d`); WS4 `ws4-v0.2.0-p14rc1` (`f60ce64`); TSA24 `ws4-tsa24-evenflow-v1` (local extracted copy; recipe lists SHA-256 `be8625…`)
**Date:** 2026-11-19
**Scope:** read-only; no manuscript, evidence, or release edits. Replay artifacts were created under `.opencode/tmp/opencode/rc14-review`.

## Confidential comments to the editor

**Recommendation: major revision; do not accept as-is.** One major blocker remains. The rc13 overclaims about the replay gate (“four failure modes”) and the factorized 248× result are fixed; the replay route is now pinned in `REPLAY.md`, and the §4 transcript is the actual gate line. The remaining blocker is §2.3: the paper says the sparse effect table carries a dataset fingerprint, candidate order, target-cell geometry, horizon, period width, and table format version, and that a dataset change forces a rebuild. The cited tag’s `EffectTable.save/load` has no such identity fields; `ws4 gpu-run` loads a caller-supplied table, and the docs say it does not rebuild it. The submitted PDF also contains the orphaned clause “attach rows to the wrong model or chains.” This is a central architecture claim and an incomplete edit. The fix is textual and bounded; no new experiments are required.

## Summary

The experimental core and public artifacts verify. The PDF and supplement hashes match the release and manifest; the p14 tag is `5f9d65d`; the WS4 tag is `f60ce64`; the `REPLAY.md` asset matches the repository file; the TSA24 artifact plus the cited WS4 tag reproduced the stored objectives, and all five campaign records plus seed 7 replay with that tag. The five-seed, scaling, and evaluation-path numbers match the records. Length is 3,717 counted words, under 4,000; 3 figures; the abstract and embedded highlights are within the journal limits. The remaining problem is claim calibration in §2.3, not a new experiment.

## Verification snapshot

- **Tags:** papers `p14-evidence-rc14` = `5f9d65d2980e17709d6832cf077a3be714d168dd`; WS4 `ws4-v0.2.0-p14rc1` = `f60ce6430ba17c2703c6fb7d0d07c598295f5a65`; FHOPS pin `135321b1f5a7a557823ea6241650a6431b4f121b` exists.
- **Hashes:** local `paper1-softwarex.tex` `841517…`, `.pdf` `12cd85…`, supplement `.tex` `3eb414…`, supplement `.pdf` `2d31ff…`; all match the manifest, and the release assets match `paper1-softwarex.pdf` and `paper1-softwarex-supplement.pdf`. `paper/REPLAY.md` `aa6799…` matches the release asset; `paper/replay_all.sh` `a09f3d…` matches the manifest.
- **Replay:** with `ws4-v0.2.0-p14rc1`, the gate returned `VALID: ws4-tsa24-gpu-ga-1000-r7 (tsa24-evenflow-w100)` and `VALID` for the five 100,000-generation campaign records plus seed 7. The displayed §4 line is the actual gate output, not a paraphrase.
- **Numbers:** Table 1 and Table S1 match the records (objectives, flow/level split, realized-level ranges, and the times in Table 1); the five-seed mean 515.682 and median 515.938 match; the 5,000-block diagnostic matches (54.8 s cold, 1.09 s warm, 0.542 ms incremental, 2.00×10³, error 3.7×10⁻⁹).
- **Display/length:** 3 figures; Table 1 plus the C1–C9 metadata table; supplement S1/S2; `python3 count_words.py` = 3,717 words; abstract under 250; embedded highlights three, each under 85 characters.

## Major comments

1. **§2.3 effect-table identity claim is unsupported, and the paragraph is broken.** `TEX:156-160`; `PDF p2-p3`; also `TEX:121-123`. The paper says the table identity includes the dataset fingerprint, candidate order, target-cell geometry, horizon, period width, and table format version, and that a dataset change forces a rebuild. In the cited tag `f60ce64`, `EffectTable.save` writes `cells`, `basis_accounts`, the CSR tensors, `row_index`, `blocks`, `build_seconds`, `max_row_width`, `block_starts`, and `extra_rows` (`ws4/opt/gpu_effects.py:419-437`); `load` reads only those keys (`:454-467`). There is no dataset fingerprint, candidate-order hash, horizon field, period-width field, or format-version field. `ws4 gpu-run` calls `EffectTable.load(table, device=device)` (`ws4/cli.py:2546`) without comparing it to the dataset or candidate cache. The docs say the table is “target-specific and is supplied by the caller; this command does not rebuild it” (`docs/reference/optimizer.rst:523-537`); only the simulator and candidate caches are content-fingerprinted (`ws4/opt/candidate_cache.py:100-134`). The record stores a schedule hash, not a dataset/effect-table hash. The clause “attach rows to the wrong model or chains” (`TEX:160`; `PDF p3`) is the orphaned remainder of the deleted “failure detector” sentence; it has no subject and is visible in the submitted PDF.

   **Why it changes acceptance.** The paper’s central architecture claims a cache-safety identity/rebuild guarantee that the cited public implementation does not provide. A reviewer who checks the tag will find the claim false, and the orphan shows the paragraph was not finished. The TSA24 results and replay are unaffected, but the software description is not accurate.

   **Smallest fix.** Rewrite §2.3’s last two sentences to state the actual behavior: the table is caller-supplied; it stores the sparse rows, block starts, and priced cell basis; it has no dataset fingerprint or format-version field; `gpu-run` does not rebuild or verify it; the simulator and candidate caches are content-fingerprinted; a dataset change requires an explicit rebuild; weight/priority changes reuse the table; target changes reuse it only when the required cells are already in the basis, otherwise the table must be extended or rebuilt. Delete the orphaned clause. Align §2.1’s “Each stage writes an artifact with an identity” sentence with the same facts. Optionally add a table hash/identity check if the stronger claim is wanted; that is larger than the textual fix. Rebuild the PDF, update the manifest/release hashes, and re-cut the release (rc15). The correction is roughly 100 words; the 3,717-word draft has 283 words of headroom.

## Minor comments (non-blocking)

- **Residual text/production.** `TEX:365` has “objective;  They” after the factorized removal; `TEX:463` C7 has empty parentheses “multi-gigabyte memory ()”; `TEX:347` still says “batch microbenchmark” though the batch result was removed; `TEX:478` C8 links `tree/main/docs` rather than the cited tag; `supplement.tex:19-21` says “the public evidence release” without the tag; `PDF p1` is a mostly blank highlights page; `PDF p2` has an empty `orcid(s):` line; the metadata table is numbered Table 2 after Table 1. None affects the claims.
- **Numbers/packaging.** `TEX:290` says the level term remains between 499.821 and 517.290; Table 1’s maximum is 515.141, and 517.290 is seed 1 in Table S1. The manifest’s `figures` list omits `realized-level.pdf`. `README.md:17-23` says three content tables while the main PDF has Table 1 plus the metadata table; `README.md:28-30` maps to “Reuse potential and limitations” while the headings are “Impact” + “5.1 Limitations.” `cover-letter.md:13` and `paper/README.md:27` still mention the removed factorized result. `paper/release/RELEASE-CANDIDATE.md:3` still says “local candidate only. No tag, release…”. `highlights.md:3-7` has five bullets, two over 85 characters; the embedded three are compliant.
- **Replay example completeness.** `TEX:372-377` says “clone WS4” but not the pinned tag, the papers repository, or the FHOPS clone/pin; `REPLAY.md:6-12` does. This is a clarity gap, not a broken replay: the release route is pinned and works.
- **Wording.** `TEX:236-238` says the gate checks fields “without calling the optimizer”; the replay script instantiates `Optimizer.from_dataset` but does not run the search. `TEX:253` says “run a search with a configuration file” although the shown `gpu-run` surface is CLI options. The Impact section remains hypothetical (“a planning team can…”). The manuscript has six numbered sections rather than the five named OSP sections. Optional cleanups.

## Recommendation

**Major revision.** The paper is not submission-ready as-is because the §2.3 claim is unsupported and the PDF has an orphaned clause. The fix is bounded and textual; no new experiments. After the correction and a re-cut release (rc15) with matching PDF/manifest/release hashes, the paper is submission-ready for SoftwareX; the remaining items are minor. This is not a reject: the TSA24 campaign, five-seed results, and all seven replays (the 1,000-generation anchor, the five campaign seeds, and seed 7) verify against the public tag.

## Prepared to review after revision

**Yes.** Refereeing openly: No. Include in annual reviewer list: No.

## Residual risk table

| Risk | Evidence | Severity | Mitigation |
|---|---|---|---|
| Effect-table identity claim | `TEX:156-160`; `PDF p2-p3`; `gpu_effects.py:419-467`; `cli.py:2546`; `optimizer.rst:523-537` | High (blocker) | Rewrite §2.3; delete orphan; rebuild/re-cut. |
| Replay example not self-contained | `TEX:372-377`; `REPLAY.md:6-12` | Low | Add clone/pin/FHOPS sentence. |
| Table 1 level range | `TEX:290`; Table 1; Table S1 | Low | Use 515.141 or say “across the reported runs.” |
| Packaging/provenance | manifest figures; README; cover letter; `RELEASE-CANDIDATE.md`; `highlights.md` | Low | Clean up before the next cut. |
| Production/format | C7; ORCID; metadata table numbering; highlights page | Low | Clean up before submission. |
| DOI/container | `TEX:409-414`; `README.md:49-54` | Medium (post-review) | Final release/DOI/container before acceptance. |
