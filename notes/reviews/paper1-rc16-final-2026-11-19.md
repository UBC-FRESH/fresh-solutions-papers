# Reviewer report — Paper 1, SoftwareX rc16 (final major-blocker gate)

**Manuscript:** “WS4: a compiled-state software architecture with exact replay for landscape harvest scheduling”
**Target:** SoftwareX, Original Software Publication (OSP)
**Review copy:** `paper/submission/softwarex/paper1-softwarex.pdf` (10 PDF pages: 1 highlights page + 9 numbered pages; 3 figures; Table 1 plus the C1–C9 metadata table; 1-page supplement)
**Release checked:** papers `p14-evidence-rc16` (`7e1b2990fc236e6d26771c248cc2b5ff09e9c446`); WS4 `ws4-v0.2.0-p14rc1` (`f60ce6430ba17c2703c6fb7d0d07c598295f5a65`); TSA24 `ws4-tsa24-evenflow-v1` (`aaba8f33b445f2b8e5ef0e0aef615598a126df18`; tarball SHA-256 `be862580…`); FHOPS pin `135321b1f5a7a557823ea6241650a6431b4f121b`
**Date:** 2026-11-19
**Scope:** read-only; no manuscript, evidence, or release edits. Replay artifacts were written under `.opencode/tmp/opencode/rc16-review`.

## Confidential comments to the editor

**Recommendation: accept; no major blocker.** The rc15 minor corrections that affect the manuscript are closed. The public tags and release assets verify, and a fresh public TSA24 tarball plus a clean WS4 tag clone (and the pinned FHOPS source) reproduced all 11 records. The remaining items are editorial or packaging cleanup; none changes a reported number, a table, or the replay result.

## Summary

The experimental core and public artifacts are sound. The paper is a disciplined SoftwareX software note: it describes the compiled-state architecture, illustrates it on one frozen TSA24 instance, reports a 100,000-generation five-seed campaign, and is explicit about what the evidence does not establish. The rc15 table-identity, replay-wording, level-range, metadata, table-count, cover-letter, and manifest-figure items are fixed. The only remaining findings are non-blocking wording, documentation, and package-cleanliness issues.

## Verification snapshot

- **Tags:** papers `p14-evidence-rc16` = `7e1b2990fc236e6d26771c248cc2b5ff09e9c446`; WS4 `ws4-v0.2.0-p14rc1` = `f60ce6430ba17c2703c6fb7d0d07c598295f5a65`; TSA24 `ws4-tsa24-evenflow-v1` = `aaba8f33b445f2b8e5ef0e0aef615598a126df18`; FHOPS pin `135321b1f5a7a557823ea6241650a6431b4f121b` exists. The WS4 tag has no binary release assets, but the tag source is public and cloneable; the paper’s C2 link resolves.
- **Hashes:** local `paper1-softwarex.tex` `5f938f…`, `.pdf` `e29613…`, supplement `.tex` `3eb414…`, supplement `.pdf` `2d31ff…`, `paper/REPLAY.md` `aa6799…`, `paper/replay_all.sh` `a09f3d…`, `realized-level.pdf` `ac31e5…`; all match the manifest. The release assets `paper1-softwarex.pdf` (`e29613…`), `paper1-softwarex-supplement.pdf` (`2d31ff…`), `paper1-REPLAY.md` (`aa6799…`), and `realized-level.pdf` (`ac31e5…`) match the repository files. The TSA24 release tarball is `be8625…`; its internal `MANIFEST.sha256` verifies.
- **Replay:** with a fresh extraction of the public TSA24 tarball, a clean checkout of `ws4-v0.2.0-p14rc1`, and the FHOPS source at `135321b1…`, `paper/replay_all.sh` returned `VALID` for all 11 records (2 FHOPS, 1 WS4 CPU-SA, and 8 WS4 GPU-GA). The five campaign seeds replayed to their stored objectives exactly; the 1,000-, 10,000-, and 100,000-generation seed-7 records also passed the recorded tolerance. The 1,000 record’s CPU replay is 8,588,725.370498514 against a stored 8,588,725.370498415; the paper’s 8,588,730 is the six-significant-figure display value.
- **Numbers:** Table 1 and Table S1 match the records (objectives, flow/level split, realized-level ranges, and times); the five-seed mean 515.682 and median 515.938 match; the 5,000-block diagnostic matches (54.8 s cold, 1.09 s warm, 0.542 ms incremental, 2.00×10³, error 3.7×10⁻⁹). The artifact has 458,708 blocks and 208,255 operable blocks; the initial oldest-first seed objective is 1,722,144,291 (rounds to 1,722,140,000 in the text).
- **Display/length:** 3 figures; Table 1 plus the C1–C9 metadata table; supplement S1/S2; `python3 count_words.py` = 3,754 counted words (under 4,000); abstract under 250 words; three embedded highlights, each under 85 characters.

## Prior-minor closure

| Item | Status | Evidence |
|---|---|---|
| Table base description | Fixed | `TEX:146-149`; `PDF p2`: rows and block row starts are stored; the evaluator computes the base. |
| Record/replay wording | Fixed | `TEX:228-231`; `PDF p3`: the record stores the reported objective and the gate checks the CPU difference. |
| Level range | Fixed | `TEX:292`; `PDF p4`: 499.821–515.141, matching Table 1 rather than seed 1’s 517.290. |
| Factorized cover-letter sentence | Fixed | `cover-letter.md:13` now says only the evaluation-path results are bounded diagnostics. |
| Metadata parentheses/docs link | Fixed | `TEX:465-466`; `PDF p8`: C7 has no empty parentheses; C8 links the `ws4-v0.2.0-p14rc1` docs tree (HTTP 200). |
| Table count | Fixed | `README.md:21-23`: one content table plus the mandatory metadata table; the supplement holds S1/S2. |
| Realized-figure manifest entry | Fixed | `manifest-v0.2.0-candidate.json:97-100`; hash `ac31e5…`; the figure is also a release asset. |

## Major comments

None. The previously identified major issues remain closed, and this gate found no unsupported result claim, broken public artifact/replay, missing required declaration, or fatal scope/fit problem.

## Minor comments (non-blocking)

- **§3.5 sentence punctuation.** `TEX:367`; `PDF p6`: “without changing the objective; they do not establish…” is a semicolon splice. Change to a period or recast as a parallel list; this is production polish only.
- **§2.5 “without calling the optimizer.”** `TEX:238`; `PDF p3`: `replay.py` instantiates `Optimizer.from_dataset` but does not run the search. Say “without rerunning the search or using the GPU” for precision.
- **§2.6 “run a search with a configuration file.”** `TEX:256`; `PDF p4`: the shown `gpu-run` surface uses CLI options, not a configuration file. Say “run a search from the command line” or point to the target/config files.
- **§4 replay snippet.** `TEX:374-379`; `PDF p6`: the snippet says “clone WS4” without the pinned tag, the papers repository, or the FHOPS clone/pin. `paper/REPLAY.md:5-13` has the complete route; add a pointer to it.
- **“selects the flattest profile.”** `TEX:197`; `PDF p3`: within the ±1% band the flow penalty is zero, so “flattest” is imprecise. Use the artifact’s “maximum even-flow level” wording or add a profile figure.
- **Supplement provenance.** `paper1-softwarex-supplement.tex:21`: “the public evidence release” lacks the `p14-evidence-rc16` tag. Add the tag for a self-contained supplement.
- **README section mapping.** `README.md:28-30` maps to “Reuse potential and limitations,” but the manuscript headings are “Impact” and “5.1 Limitations.” Align the README with the actual headings.
- **Stale highlights file.** `highlights.md:6` still mentions “Factorized … results,” and the file has five bullets (two over 85 characters) while the embedded PDF has three compliant bullets. The PDF highlights are correct; update or remove the draft file before upload.
- **Stale package notes.** `paper/README.md:36-44` still mentions the factorized result and “public release remains pending approval”; `paper/release/RELEASE-CANDIDATE.md:3` says “local candidate only. No tag, release…”. Both are contradicted by the public rc16 tag. Packaging cleanup only.
- **Cosmetic production.** `PDF p2` has an empty `orcid(s):` line; `PDF p8` numbers the metadata table “Table 2”; the highlights page is mostly blank. None affects the claims.
- **1,000-generation record schema.** The record has `time_to_best_s` but no `run.search_seconds`; Table 1’s 9.38 s is therefore an upper-bound/alias. Add `search_seconds` when the record is next cut for schema consistency.
- **Manifest `figures` list.** `manifest-v0.2.0-candidate.json:41-44` still lists only `matched-search.pdf` and `scaling.pdf`; the realized-level figure is covered by the separate `realized_level_figure` entry. This is consistent enough for the release, but moving it into `figures` would simplify the audit trail.

## Recommendation

**Accept; no major blockers.** The manuscript is submission-ready for SoftwareX once the minor editorial and packaging items are ignored or cleaned up. The DOI/Zenodo and tested-container items remain disclosed pre-acceptance administrative steps, not scientific blockers.

## Prepared to review after revision

**Yes.** Refereeing openly: No. Include in annual reviewer list: No.

## Residual risk table

| Risk | Evidence | Severity | Mitigation |
|---|---|---|---|
| Unsupported claim or broken replay | All 11 records replayed `VALID`; tags/assets/hashes verified | None | None. |
| Table/record mismatch | Table 1, Table S1, and the diagnostic match the records | None | None. |
| Level/realized-level interpretation | Table 1 and S1; Eq. 4; realized-level figure | None | The text now uses 515.141 and the per-seed ranges match. |
| Packaging staleness | `highlights.md`, `paper/README.md`, `RELEASE-CANDIDATE.md`, supplement tag | Low | Clean the markdown; no manuscript change. |
| DOI/Zenodo and tested container | `README.md:51-53`; `TEX:412-414`, `TEX:427-428` | Administrative | Disclosed; complete before acceptance as planned. |
