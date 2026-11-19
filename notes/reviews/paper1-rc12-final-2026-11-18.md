# Final submission decision — Paper 1, SoftwareX rc12

**Date:** 2026-11-18 · **Scope:** read-only; rc12 tag `p14-evidence-rc12` (`b7a7e85`), PDF, supplement, package, manifest. Replay scripts unchanged since the rc9 11/11 `VALID` check.

## 1. Is rc12 submission-ready for SoftwareX?

**No.** The scientific core passes: 3,877 counted words plus ~31 words of content-table body are under 4,000; CRediT, funding, and competing-interest statements are present (`TEX:434-446`); the PDF and supplement hashes match `MANIFEST` and the rc12 assets. The remaining defects are production and provenance, not experimental.

## 2. Three highest-value fixes

1. **Repair the two visible production defects.** Delete or fill the empty §5.1 “Reuse potential” heading (`TEX:398`; `MS p6`); rc9 had a paragraph here (`dc2acdb:428-435`), and rc11 removed the text but kept the heading. Align the supplement numbering: the manuscript cites `Supplementary Table S1/S2` (`TEX:325,349`) but the supplement prints `Table 1/2` (`paper1-softwarex-supplement.tex:26,45`).

2. **Make the cover letter and package describe rc12, not a pending release.** `COVER:16-18` still says the release is “being prepared” and the tag/DOI are placeholders; `COVER:11` claims an “adapter” the manuscript never defines. `README.md:49-57` still lists `author@example.invalid`, commit `f60ce64`, private evidence, and missing docs/email; `RELEASE-CANDIDATE.md:3` says “local candidate only”; `MANIFEST:24` says `p16-evidence-rc12` while the tag is `p14-evidence-rc12`; `paper/REPLAY.md:6-7` clones unpinned `main`. Also correct the display inventory: `README.md:20-24` and the `REL rc12` body claim 3 figures and a realized-level figure; the PDF has 2 figures and 1 content table (`MS p1-p9`; `paper/figures/realized-level.pdf` is unreferenced). Add the figure and cite it in §3, or drop the claim.

3. **Finish the OSP demonstration.** §4 (`TEX:374-383`; `MS p6`) is only a `replay_all.sh` call: add a minimal target/config snippet and the observed `VALID` output (or a record excerpt). §5 (`TEX:385-396`; `MS p6-p7`) still uses hypothetical “a planning team can…” language: anchor it to one concrete audit/scenario use, or state there is no adoption evidence and give a worked reuse case. Keep additions within the ~90-word headroom.

## 3. Recommendation

**Minor revision.** Do not submit rc12 as-is; fixes 1–3 are bounded, require no new experiments, and leave the scientific claims unchanged. Rebuild, re-count, and re-cut the tag so the PDF, supplement, manifest, and release notes agree.
