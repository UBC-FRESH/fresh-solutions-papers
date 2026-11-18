# Paper 2 (JORS Issues in Research Software) — rc12 final submission decision

**1. Submission-ready? No.**

The science, headline numbers, and file hashes are sound: the JORS PDF (`8056e2…`), supplement (`246df9…`), and `.tex` files match the public `p14-evidence-rc12` tag, and all 65 manifest hashes verify. The blockers are submission-package and provenance text, not new experiments.

**2. Three highest-value fixes**

1. **Cover letter contradicts the manuscript and the public release.** `cover-letter.md:13` claims “cluster-by-instance and family-cluster intervals”; the manuscript reports only the cluster-by-instance interval and explicitly says the family interval is not reported (`paper2-jors.tex:249–253`). `cover-letter.md:16–19` says the software/evidence are “being prepared” and the repository/DOI are “placeholders”; the tag is public (`MS p6`; `paper2-jors.tex:343–346`). Rewrite both passages to state the public rc12 release and the interval actually reported.

2. **The manifest and release-candidate notes identify the wrong release and assets.** `paper2/evidence/manifest-v0.1.0-candidate.json:200` says `p16-evidence-rc12`; no such tag exists—the public tag is `p14-evidence-rc12` (`MS p6`). The manifest still points `manuscript`/`submission_*` at `paper2-manuscript` and the obsolete `paper2-sn-jnl` files (`:202–207, 224–229`), and `paper2/evidence/RELEASE-CANDIDATE.md:13–19` lists those instead of the JORS PDF/TeX and supplement. Correct the status string and replace the stale entries with the JORS files; re-cut the tag/manifest.

3. **The submitted PDF says no tag exists.** `paper2-jors.tex:163–164` (“a tag is not created until the maintainer approves the release”) contradicts §Availability (`:343–346, 372`) and the public tag. The same stale statement is in `paper2/README.md:177–178`; the submission README still carries repository/DOI placeholders and a stale blocking list (`paper2/submission/jors/README.md:35–36, 43–72`). Remove the contradiction and update the status blocks.

**3. Recommendation: minor revision.**

All three are bounded text/metadata corrections; no new campaigns, analysis, or figure changes are required. With these fixed, rc12 is submission-ready.
