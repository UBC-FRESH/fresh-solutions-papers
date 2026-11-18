# Reviewer report — Paper 1, SoftwareX rc13

**Manuscript:** “WS4: a compiled-state software architecture with exact replay for landscape harvest scheduling”
**Target:** SoftwareX, Original Software Publication (OSP)
**Review copy:** `paper/submission/softwarex/paper1-softwarex.pdf` (10 PDF pages: 1 highlights page + 9 numbered pages; 3 figures; Table 1 plus the C1–C9 metadata table; 1-page supplement)
**Release checked:** papers `p14-evidence-rc13` (`b398642`); WS4 `ws4-v0.2.0-p14rc1` (`f60ce64`); TSA24 `ws4-tsa24-evenflow-v1` (SHA-256 `be8625…`)
**Date:** 2026-11-18
**Scope:** read-only; no manuscript, evidence, or release edits. Replay artifacts were created under `.opencode/tmp/opencode`.

## Confidential comments to the editor

**Recommendation: minor revision; do not accept as-is.** The experimental core and public artifacts verify: the PDF and supplement hashes match the release and manifest; the REPLAY.md asset matches the repository file and `replay_all.sh` matches the manifest; the TSA24 artifact hash and 458,708 compiled blocks match; two recorded replays I re-ran (`1000-r7`, `100000-r2`) matched their stored objectives, and `check_benchmark_record.py --replay` returned `VALID`.

The remaining issues are claim calibration and replay-package provenance, not new experiments. §2.3/§2.5 claim an effect-table identity check and four gate-caught failure modes that the released code/gate do not implement; §4’s output block is not the command’s output and the replay docs clone unpinned `main`; the factorized result uses code absent from the cited WS4 tag and an archive not in the public capsule. These are bounded but touch the paper’s central exact-replay contract, so I would not accept without correction.

## Summary

The manuscript is a disciplined, appropriately bounded SoftwareX software note. The architecture is clearly described, the TSA24 campaign and replay records are internally consistent, the five-seed and evaluation-path tables match the evidence, and the length, figure, abstract, CRediT, funding, competing-interest, and C1–C9 metadata requirements are largely met. The scientific claims are appropriately limited and the reported numbers are supported.

However, the paper’s central provenance/replay claims are stronger than the released implementation and gate, and the illustrative example is not a faithful transcript of the documented command. The experimental core is sound; the submission is not yet ready because those claims and the replay package need correction.

**Verification snapshot**

- Tags: papers `p14-evidence-rc13` = `b398642`; WS4 `ws4-v0.2.0-p14rc1` = `f60ce64`; TSA24 asset hash `be8625…`.
- Hashes: local PDF `d020cc…` and supplement `2d31ff…` match the release assets and manifest; all manifest path/hash entries match; record hashes match; the REPLAY.md asset matches `paper/REPLAY.md`.
- Replay: `replay.py` on `1000-r7` and `100000-r2` from the extracted TSA24 artifact matched the stored objectives; `check_benchmark_record.py --replay evidence/ws4-tsa24-gpu-ga-1000-r7/record.json` printed `VALID: ws4-tsa24-gpu-ga-1000-r7 (tsa24-evenflow-w100)`.
- Display/length: 3 figures; Table 1 plus the C1–C9 metadata table; supplement S1/S2; 3,919 counted words + 30 Table 1 body tokens = ~3,949; abstract under 250 words; three embedded highlights under 85 characters each.

## Major comments

1. **The effect-table identity and “four failure modes” claims exceed the released implementation.** `MS p3` §2.3 (`TEX:157-161`) says the table identity includes a dataset fingerprint, candidate order, target-cell geometry, horizon, period width, and table format version, and that the identity check detects a stale table. In the cited WS4 tag `f60ce64`, `EffectTable.save/load` writes and reads the table payload (cells, tensors, row index/blocks, build time, block starts) but no dataset fingerprint, candidate-order hash, horizon, period-width, or format-version field (`ws4/opt/gpu_effects.py:363-465`); `ws4 gpu-run` loads a caller-supplied table with no comparison to the dataset or candidate cache (`ws4/cli.py:2494-2559`). The docs confirm the table is caller-supplied and “this command does not rebuild it” (`docs/reference/optimizer.rst:523-537`); only the simulator and candidate caches are content-fingerprinted (`ws4/opt/candidate_cache.py:100-134`). The record has a schedule hash but no dataset/table hash (`schemas/benchmark-record.schema.json:65-76`), so a stale table can attach rows to the wrong chains silently. The same section (`MS p4`; `TEX:244-246`) says four failure modes are exposed and “none is silent in a record that passes the gate.” The gate (`scripts/check_benchmark_record.py:151-166`) checks the schema, `exact_replay`, schedule existence/hash, and the replay objective within `rel_tol=1e-9, abs_tol=1e-5`; it does not check coverage, candidate membership, model/table identity, move history, or feasibility. The device/CPU differences in the records are ~1e-15 relative (e.g., r1 `518.6214523292266` vs `518.6214523292301`), so a reported device objective would pass; a partial schedule or irreversible move would not be caught. This contradicts the paper’s own caveat that the gate verifies the incumbent, not the search trajectory (`TEX:238-239`).

   **Action:** either implement the identity metadata/check and add dataset/table hashes to the record, or rewrite §2.3/§2.5 to state exactly what is checked and what is not. Change “without calling the optimizer” (`TEX:238`) to “without rerunning the search or using the GPU.” **Why it matters:** the paper’s thesis is the exact-state/replay contract; the reported numbers are unaffected, but the software claim is not yet true.

2. **The public replay route is not version-pinned, and the §4 transcript is not the command’s output.** `paper/REPLAY.md:6-7` clones the default branches of WS4 and FHOPS; `paper/replay_all.sh:3` says “pinned ws4 checkout” but nothing pins it. The paper cites `ws4-v0.2.0-p14rc1` (`f60ce64`), but a reader following the instructions gets current `main` (at review, `98e96ced`); the two TSA24 replays I ran still matched, but the search code is not the cited implementation. In §4 (`MS p6`; `TEX:393-397`), the displayed block adds `targets:`/`minimum:` lines that `replay_all.sh` does not print; the gate prints only `VALID: <record_id> (<instance_id>)` (`check_benchmark_record.py:201-203`), one per record (11 records). My run returned exactly `VALID: ws4-tsa24-gpu-ga-1000-r7 (tsa24-evenflow-w100)`. The `targets:`/`minimum:` lines are target configuration, not gate output. The text also says “clone WS4” but not the papers repository; the `paper/replay_all.sh` path and the FHOPS role need to be explicit.

   **Action:** pin `git -C "$WS4_ROOT" checkout ws4-v0.2.0-p14rc1` and the FHOPS commit used by the records in `REPLAY.md` and §4; show the actual gate output (or label it “excerpt”) and put the target snippet in a separate block; say to clone the papers repository and whether FHOPS is needed for the TSA24 subset. Re-cut the `REPLAY.md` asset after editing. **Why it matters:** this is the SoftwareX illustrative-example/replay requirement and the paper’s central “replayable” claim.

3. **The factorized 248× result is not reproducible from the cited release.** `MS p5-p6` §3.4 (`TEX:364-370`) and the abstract (`TEX:38-39`) report the 64-genome CPU/CUDA batch using “the TSA24 factorized archive.” The cited WS4 tag `f60ce64` has no `ws4/opt/factorized_effects.py` (`import ws4.opt.factorized_effects` fails with the tag and succeeds with public main `98e96ced`). The evidence command uses a local checkout `WS4_GPU_ROOT=/srv/shared-data/gep/ws4/ws4-gpu` (`paper/evidence/tsa24-factorized-ablation.json`, `commands`), and the required `runtime/factorized/tsa24-factorized.npz` is not in the release or repository; `paper/experiments/benchmark_factorized_switch.py:87` loads it but has no build option. A reader with the cited tag cannot run the benchmark.

   **Action:** cite the exact public WS4 commit that contains `factorized_effects.py` (e.g., main `98e96ced` or the commit actually used), add a build command or include the archive in the capsule, and sanitize the machine-specific path; or state in §3.4/Limitations that the factorized archive is a local diagnostic not covered by the public replay capsule. **Why it matters:** it is one of three reported validation results and an abstract number; it should be traceable even if bounded.

## Minor comments

- **Length.** `python3 count_words.py` gives 3,919; among tables, the journal excludes only the metadata table, so add the 30-token Table 1 body: ~3,949, about 51 words under the 4,000 cap (`README.md:17-19`; `TEX:304-313`). State the journal convention in the README and cover letter, and offset any text added for Major 1–3.
- **Packaging/provenance.** `MANIFEST:24` says `p16-evidence-rc13`; the tag is `p14-evidence-rc13`. `paper/release/RELEASE-CANDIDATE.md:3` still says “local candidate only. No tag, release…” and lists old assets/approval commands. `README.md:21-23` says three content tables in the manuscript, but the PDF has Table 1 plus the metadata table and S1/S2 in the supplement; `README.md:28-30` maps to “Reuse potential and limitations,” but the actual headings are “Impact” + “5.1 Limitations.” Align these with the release body/P16 report.
- **Highlights.** `highlights.md:3-7` has five bullets, two over the 85-character guidance (90 and 95), and differs from the manuscript’s three compliant bullets (`TEX:42-46`). Submit one compliant set as the separate file.
- **C8.** `TEX:478` links to `tree/main/docs`; the cited code is the tag. Pin to `tree/ws4-v0.2.0-p14rc1/docs` or the docs site.
- **Table 1 range.** `MS p5`; `TEX:293` says the level term remains between 499.821 and 517.290, but Table 1’s maximum is 515.141; 517.290 is seed 1 in Table S1. Say “across the reported runs” or use 515.141.
- **Supplement/manifest.** The supplement says “the public evidence release” without a URL/tag (`supplement.tex:19-21`); add the tag. The manifest’s `figures` list covers `scaling.pdf` and `matched-search.pdf` but not the new `realized-level.pdf` (`MANIFEST:41-44`); add its hash if the manifest is the audit record.
- **Production/format.** The PDF has a mostly blank highlights page (`PDF p1`), an empty `orcid(s):` line (`PDF p2`), and the mandatory code-metadata table is numbered Table 2 after the content table; confirm the current SoftwareX template’s expected ordering/labels. The required sections are present, but the manuscript has six numbered sections (a separate “Validation and illustration” plus “Illustrative example”); consider merging §3/§4 or explaining the extra section.
- **Impact.** `MS p7` still uses hypothetical “a planning team can…” language; one concrete audit/scenario walkthrough or an explicit “no adoption evidence” sentence would strengthen it. The measured replay/evaluation-cost impact is already stated, so this is not a blocker.

## Recommendation

**Minor revision.** The experimental core, public artifacts, and replay are sound; Major 1–3 are bounded claim/documentation/provenance fixes and require no new experiments. The manuscript is not ready to accept as-is because the first two comments go to the paper’s central replay contract. After correction, re-count with the journal convention, rebuild, and re-cut the release so the PDF, supplement, manifest, and REPLAY asset agree.

## Prepared to review after revision

**Yes.** Refereeing openly: No. Include in annual reviewer list: No.

## Residual risk table

| Risk | Evidence | Severity | Mitigation |
|---|---|---|---|
| Effect-table identity / stale-table detection absent | `TEX:157-161`; `ws4/opt/gpu_effects.py:363-465`; `ws4/cli.py:2546`; `candidate_cache.py:100-134` | High | Implement identity metadata/check and record hashes, or rewrite §2.3/§2.5. |
| Gate overclaim / “four failure modes” | `TEX:244-246`; `check_benchmark_record.py:151-166`; schema `65-76` | High | State what the gate checks and does not check; add dataset/table hash if implemented. |
| Replay route unpinned; §4 transcript not faithful | `REPLAY.md:6-7`; `TEX:393-397`; actual gate output | Medium–High | Pin WS4/FHOPS commits; show actual output/excerpt; re-cut asset. |
| Factorized result provenance | Tag lacks `factorized_effects.py`; local path; missing `.npz` | Medium | Cite public commit; add build/archive; sanitize; or label local diagnostic. |
| Word cap | ~3,949 / 4,000 | Medium | Count journal convention; offset additions. |
| DOI/container/final release | `README.md:51-53`; `TEX:425` | Medium | Post-review; final tag/DOI before acceptance. |
| Packaging/format inconsistencies | Manifest `p16` vs tag `p14`; stale `RELEASE-CANDIDATE.md`; README table count/mapping; highlights; C8; Table 1 range | Low | Clean up before submission. |
| Impact/section structure | `MS p7`; six numbered sections | Low | Add one concrete reuse case; align with OSP template. |
