# Reviewer report — Paper 1, SoftwareX rc15 (major-blocker review)

**Manuscript:** “WS4: a compiled-state software architecture with exact replay for landscape harvest scheduling”
**Target:** SoftwareX, Original Software Publication (OSP)
**Review copy:** `paper/submission/softwarex/paper1-softwarex.pdf` (10 PDF pages: 1 highlights page + 9 numbered pages; 3 figures; Table 1 plus the C1–C9 metadata table; 1-page supplement)
**Release checked:** papers `p14-evidence-rc15` (`19d3e59`); WS4 `ws4-v0.2.0-p14rc1` (`f60ce64`); TSA24 `ws4-tsa24-evenflow-v1` (`aaba8f3`; asset SHA-256 `be8625…`); FHOPS pin `135321b1…`
**Date:** 2026-11-19
**Scope:** read-only; no manuscript, evidence, or release edits. Replay artifacts were created under `.opencode/tmp/opencode/rc15-review`.

## Confidential comments to the editor

**Recommendation: minor revision; no major blocker.** The rc14 §2.3 blocker is closed. The paper now states that the released GPU path loads a caller-supplied table with no embedded dataset identity and no rebuild/verification, and the orphaned clause is gone (`TEX:153-162`; `PDF p2-p3`). The public artifacts and replay verify: the p14 tag is `19d3e59`, the WS4 tag is `f60ce64`, the release assets match the manifest and the local PDF/supplement/REPLAY, and a fresh public TSA24 tarball plus a clean WS4 tag clone reproduced all 11 records, including the five campaign seeds. The remaining items are factual, production, and packaging cleanup; none changes a reported number or the replay result.

## Summary

The experimental core and public artifacts are sound. The paper is a disciplined SoftwareX software note: it describes the compiled-state architecture, illustrates it on one frozen TSA24 instance, reports a 100,000-generation five-seed campaign, and is explicit about what the evidence does not establish. The rc14 table-identity overclaim is fixed. The remaining issues are a one-clause description of where the empty-schedule base totals live, a metadata mismatch in the 1,000-generation record, a level-range sentence in §3.2, and production/package staleness. None is acceptance-blocking; the manuscript is submission-ready after those corrections.

## Verification snapshot

- **Tags:** papers `p14-evidence-rc15` = `19d3e59c8a00fcd2e6ffc68e0d124672767deb3c`; WS4 `ws4-v0.2.0-p14rc1` = `f60ce6430ba17c2703c6fb7d0d07c598295f5a65`; TSA24 `ws4-tsa24-evenflow-v1` = `aaba8f33b445f2b8e5ef0e0aef615598a126df18`; FHOPS pin `135321b1f5a7a557823ea6241650a6431b4f121b` exists.
- **Hashes:** local `paper1-softwarex.tex` `d5d823…`, `.pdf` `54d60e…`, supplement `.tex` `3eb414…`, supplement `.pdf` `2d31ff…`, `paper/REPLAY.md` `aa6799…`, `paper/replay_all.sh` `a09f3d…`; all match the manifest. The release assets `paper1-softwarex.pdf` (`54d60e…`), `paper1-softwarex-supplement.pdf` (`2d31ff…`), and `paper1-REPLAY.md` (`aa6799…`) match the repository files. The TSA24 release tarball is `be8625…`; its internal `MANIFEST.sha256` verifies.
- **Replay:** with a fresh extraction of the public TSA24 tarball and a clean checkout of `ws4-v0.2.0-p14rc1`, `paper/replay_all.sh` returned `VALID` for all 11 records (2 FHOPS, 1 WS4 CPU-SA, and 8 WS4 GPU-GA). The five campaign seeds replayed to their stored objectives exactly; the 1,000-generation, 10,000-generation, and 100,000-generation seed-7 records also replayed within the recorded tolerance.
- **Numbers:** Table 1 and Table S1 match the records (objectives, flow/level split, realized-level ranges, and times); the five-seed mean 515.682 and median 515.938 match; the 5,000-block diagnostic matches (54.8 s cold, 1.09 s warm, 0.542 ms incremental, 2.00×10³, error 3.7×10⁻⁹). The artifact has 458,708 blocks and 208,255 operable blocks; the initial oldest-first seed objective is 1,722,144,291 (rounds to 1,722,140,000 in the text).
- **Display/length:** 3 figures; Table 1 plus the C1–C9 metadata table; supplement S1/S2; `python3 count_words.py` = 3,741 counted words (about 3,771 with the Table 1 body, still under 4,000); abstract under 250 words; three embedded highlights, each under 85 characters.

## Major comments

None. The rc14 major is closed: the current §2.3 describes a caller-supplied table, no embedded dataset identity, no rebuild or verification by `ws4 gpu-run`, and target reuse only when the required cells are in the basis (`TEX:153-162`). This is consistent with `ws4/opt/gpu_effects.py:419-467` and `ws4/cli.py:2546` at `f60ce64`. The submitted PDF contains the corrected text; the orphaned clause is gone (`PDF p2-p3`).

## Minor comments (non-blocking)

- **§2.3 says the effect table stores the empty-schedule base totals; it does not.** `TEX:146-151`; `PDF p2`. The serialized `EffectTable` stores the rows, block starts, row index/extra rows, and basis metadata (`ws4/opt/gpu_effects.py:120-165`, `419-437`); the empty-schedule base is computed by `IncrementalObjective.reset` from `optimizer._base_values()` or `_simulator_base_values()` (`ws4/opt/incremental.py:362-377`; `ws4/opt/engine.py:1022-1063`). The resident-state invariant in §2.4 is correct. Rewrite the clause to say the table stores the rows and block row starts, and the resident state adds the base totals. This is a factual correction, not a result change.
- **§2.5 says the record stores the CPU replay objective; the 1,000-generation record stores the device objective.** `TEX:228-230`; `evidence/ws4-tsa24-gpu-ga-1000-r7/record.json`. The stored `result.objective` is 8,588,725.370498415 (device); the CPU replay is 8,588,725.370498514 (`replay.out`), a 9.9×10⁻¹¹ difference. The five campaign records and the 100,000-generation seed-7 record store the CPU replay. Either update the 1,000-generation record to the CPU replay value and re-cut the release, or soften the sentence to “the record stores a verified objective within the replay tolerance.” The reported 8,588,730 is unchanged at six significant figures. This record also lacks `run.search_seconds` (it has `time_to_best_s` = 9.381); consider adding it for schema consistency.
- **§3.2 level-range sentence does not match Table 1.** `TEX:291`; `PDF p5`. The text says the level term remains between 499.821 and 517.290, but Table 1's maximum is 515.141; 517.290 is seed 1 in Table S1. Use 515.141 in the scaling paragraph or say “across the reported runs.”
- **§3.5 has a broken sentence from the factorized removal.** `TEX:366`; `PDF p6`: “without changing the objective;  They do not establish…” Change to “without changing the objective. They do not establish…” (and remove the double space). This is a production error, not a claim change.
- **Production/format.** `TEX:464` C7 has empty parentheses (“multi-gigabyte memory ()”); `TEX:465` C8 links `tree/main/docs` rather than the cited tag; `PDF p2` has an empty `orcid(s):` line; `PDF p8` numbers the mandatory metadata table “Table 2”; `PDF p1` is a mostly blank highlights page. None affects the claims.
- **Packaging/provenance.** `cover-letter.md:13` still says “The factorized and evaluation-path results are labelled as bounded microbenchmarks,” but the paper no longer reports a factorized result. `highlights.md:6` repeats the factorized claim, and the file has five bullets (two over 85 characters) while the embedded set has three compliant bullets. `README.md:21-23` says “3 content tables” in the manuscript; the main PDF has Table 1 plus the metadata table, with S1/S2 in the supplement. `README.md:28-30` maps to “Reuse potential and limitations,” but the headings are “Impact” and “5.1 Limitations.” The manifest's `figures` list omits `realized-level.pdf` (`manifest-v0.2.0-candidate.json:41-44`). `supplement.tex:19-21` says “the public evidence release” without the tag. `paper/release/RELEASE-CANDIDATE.md:3` still says “local candidate only. No tag, release…”; `paper/README.md:18-27` still mentions the factorized result and “public release remains pending approval.” These are package cleanliness issues, not manuscript claims.
- **Replay example completeness.** `TEX:372-377`; `PDF p6` says “clone WS4” but not the pinned tag, the papers repository, or the FHOPS clone/pin. `paper/REPLAY.md:5-13` has the complete pinned route and it works. Add a sentence pointing to `paper/REPLAY.md`, or include the pin in the snippet. This is a clarity gap, not a broken replay.
- **Wording.** `TEX:236-238` says the gate checks fields “without calling the optimizer”; `replay.py` instantiates `Optimizer.from_dataset` but does not run the search. Change to “without rerunning the search or using the GPU.” `TEX:254` says “run a search with a configuration file,” but the shown `gpu-run` surface is CLI options. The paper has six numbered sections (“Validation and illustration” plus “Illustrative example”); the OSP content is covered, but aligning the headings with the five named OSP sections would be cleaner.
- **Administrative.** The paper discloses that a DOI/Zenodo and a tested container replay are pending (`TEX:412-414`, `TEX:427-428`; `README.md:51-53`). These are pre-acceptance submission steps, not manuscript blockers; the public release candidate and replay contract are usable now.

## Recommendation

**Minor revision; no major blockers.** The rc14 §2.3 blocker is closed, the public artifacts and all 11 recorded replays verify, and the reported numbers match the evidence. After the minor factual/production/packaging corrections, the manuscript is submission-ready for SoftwareX; the DOI/Zenodo and tested-container items remain disclosed pre-acceptance administrative steps, not scientific blockers.

## Prepared to review after revision

**Yes.** Refereeing openly: No. Include in annual reviewer list: No.

## Residual risk table

| Risk | Evidence | Severity | Mitigation |
|---|---|---|---|
| rc14 effect-table identity overclaim | `TEX:153-162`; `gpu_effects.py:419-467`; `cli.py:2546` | Closed | None; rc15 text matches the released path. |
| Effect-table base-totals description | `TEX:146-151`; `gpu_effects.py:120-165`, `419-437`; `incremental.py:362-377` | Low | Rewrite the clause; no result change. |
| 1,000-generation record stores device objective | `record.json`; `replay.out`; `TEX:228-230` | Low | Update the record or soften the sentence. |
| Level range vs Table 1 | `TEX:291`; Table 1; Table S1 | Low | Use 515.141 or “across the reported runs.” |
| Packaging/provenance | cover letter, `highlights.md`, `README.md`, manifest, `RELEASE-CANDIDATE.md`, `paper/README.md`, supplement | Low | Clean up before the next cut. |
| DOI/Zenodo and tested container | `README.md:51-53`; `TEX:412-414`, `TEX:427-428` | Medium (post-review) | Register DOI and test container before acceptance. |
