# Paper 2 (JORS Issues in Research Software) — rc14 blocker review

**Manuscript:** “FRESH Solutions: an adapter and exact-replay harness for metaheuristic benchmarking” (Gregory Paradis, UBC FRESH Lab).
**Materials reviewed:** `paper2/submission/jors/paper2-jors.tex` / `.pdf` (8 pp., 3,816 words); supplement `.tex` / `.pdf` (4 pp.); `paper2/submission/jors/README.md`; `cover-letter.md`; `paper2/evidence/manifest-v0.1.0-candidate.json`; `paper2/evidence/RELEASE-CANDIDATE.md`; `paper2/REPLAY.md`; public `p14-evidence-rc14` release; `v0.9.3-p13rc1`; rc13 final review.
**Recommendation:** Major revision — not submission-ready.
**Prepared to review after revision:** Yes.

## Verdict

1. **MAJOR blockers: Yes — one.**
2. **REL-P0** — the rc14 release’s `paper2-REPLAY.md` asset still documents the stale default branch, so the public one-command replay reproduces the wrong evidence. The tag tree itself is correct; this is a release-packaging defect. Details below.
3. **Recommendation: major.**
4. **Submission-ready once minor suggestions are ignored: No.** The manuscript and the tagged tree are ready, but the public release asset still breaks the documented one-command replay. After replacing that asset and re-cutting the release, yes.

## Confidential comments to the editor

The scientific core is sound and should not be rejected. I independently replayed the full tag tree, verified every headline number against the committed evidence, and checked the manifest and release assets. The only blocker is public packaging: the rc14 release asset `paper2-REPLAY.md` is byte-identical to the rc13 asset and still tells readers to clone the default `main`, which is the stale P12.1 tree. The tag `p14-evidence-rc14` and its own `paper2/REPLAY.md` are correct, so the fix is bounded: replace the stale release asset and re-cut. This is a release-hygiene failure in a paper whose headline is one-command replay, not a new experiment or a scientific disagreement. I recommend major revision rather than reject because the artifact, once the asset is fixed, supports the manuscript.

## Summary

The manuscript is a credible JORS Issues in Research Software experience report: it describes a small adapter contract, resident state and a replay gate, QAP/TSP reference adapters, a convergence-controlled QAP framework check, a 20-instance QAP/BLS panel, a frozen mixed-depth TSP panel, broad screens, external LKH context, and a generic negative result. The negative results and scope discipline are strengths: the tabu reference is explicitly unvalidated and BLS is primary; the TSP panel is explicitly frozen/mixed-depth; the generic layer is a negative result, not a promoted method.

The statistics match the evidence. QAP tabu mean 0.30085%, BLS 0.09614%, paired difference −0.20471 pp, 15/16 non-tied instance means, 73/200 vs 161/200 optima. TSP mean 0.003945%, worst 0.18458%, 94/100 optima, 95/100 patience, five `brazil58` cap hits at the optimum. Framework CPU ratio 1.2390 (95% CI 1.1683–1.3098), with 40/40 patience stops, quality matches, and exact replays. The supplement’s QAP/TSP/framework tables and the `bur26` diversity table match the evidence. The build has no undefined citations or overfull boxes. 3,816 words is within JORS’s 3,000–4,000-word guidance; the 8-page PDF (6 text + 2 references) is above the rough 4–6-page guide, not a word-limit failure.

I verified the tag tree and full replay. `p14-evidence-rc14` resolves to `5f9d65d`; the submodule is `4583ad3`. A clean tag checkout with `QAPLIB_ROOT`/`TSPLIB_ROOT` set replayed 40 framework + 20 deep-TSP, 200 expanded-QAP, 200 BLS, 100 expanded-TSP, 40 generic, and 1,060 broad incumbents; 25 `esc8` records were skipped and five `brazil58` cap hits were reported. All 65 manifest `files` hashes pass; the JORS `.tex` (`c644…`), PDF (`0738…`), and supplement (`38f1…`) match the tag tree, and the two PDFs also match the release assets. The only replay-blocking failure is the release’s own replay asset.

## Major comment

### REL-P0 — The rc14 release asset `paper2-REPLAY.md` still clones the stale default branch and silently reproduces the wrong evidence

**Evidence.** The asset at
`https://github.com/UBC-FRESH/fresh-solutions-papers/releases/download/p14-evidence-rc14/paper2-REPLAY.md`
is byte-identical to the rc13 asset (sha256 `e987a27e…`, 536 bytes). Its line 4 is:

```bash
git clone --recurse-submodules https://github.com/UBC-FRESH/fresh-solutions-papers
```

There is no `--branch`. That clones the repository default `main` at `04e533c` (P12.1), whose `paper2/README.md` says “DO NOT SUBMIT” and whose `paper2/replay_all.sh` runs only `check_evidence.py`, `replay_framework_use.py`, and `replay_tsp_convergence.py` (the old 60+20 framework/deep-TSP set), then exits 0. It does not run the paper’s 200 expanded-QAP, 200 BLS, 100 expanded-TSP, 40 generic, or 1,060 broad panels. The tag tree is correct: `p14-evidence-rc14` → `5f9d65d`; its `paper2/REPLAY.md` has `--branch p14-evidence-rc14` (sha256 `3b65f4df…`, 563 bytes), and a clean tag checkout replays all panels exactly. The manuscript’s one-command replay claim is at `MS p7`; the release page’s asset is the instruction a reader is most likely to follow.

**Why this changes acceptance.** The paper’s headline reproducibility claim is that a reader can replay the evidence with one command. As published, the release’s own asset sends the reader to a different, older evidence set and exits successfully. A reviewer who follows it cannot reproduce Tables 1–2 or the replay counts, and the failure is silent. That is a broken public replay, not a style issue. The tag tree being correct does not rescue the release asset, because the release page is the cited public artifact.

**Smallest fix.** Replace the `paper2-REPLAY.md` release asset with the tag’s `paper2/REPLAY.md` (add `--branch p14-evidence-rc14`); re-cut or edit the release so the asset matches the tag. Optionally add a commit assertion to `check_evidence.py`; that is useful but not required for acceptance. No new experiments are needed.

## Minor comments (not blockers)

- **MAN-P1 — Manifest PDF aliases are stale.** `manifest-v0.1.0-candidate.json:205-208, 227-230` still hash the rc13 PDF (`4cb0ae89…`) for `pdf` and `submission_pdf`, while the actual/tagged/release PDF is `0738fc6b…`; `jors_submission_pdf` is correct. All 65 `files` hashes pass, so the evidence set is intact, but `RELEASE-CANDIDATE.md:9` (“manifest hashes match”) is false for those aliases. Fix the two hashes (or drop the aliases) in the same re-cut.
- **REL-P2 — Release identity still says P16.** The release title/body say “P16 evidence release candidate 14” and root `README.md:3` says “P16 release candidate 14,” while the paper and manifest say `p14-evidence-rc14`. The tag URL is correct; this is a public-facing identity inconsistency. Change P16 to p14 in the release title/body and root README before submission.
- **DOC-P3 — Submission/package READMEs are stale.** `paper2/submission/jors/README.md:43-71` still labels CPU timing a “blocking issue” (the paper explicitly scopes it at `MS p7`), still asks whether to rerun the TSP depth panel (the paper discloses it as frozen), and still says the tabu result lacks a per-seed diversity table (the supplement now has one). `paper2/README.md:81` says BLS is stronger on 14 instance means (the paper/data say 15 of 16 non-tied), and `:119` states an adaptive depth rule (the paper uses a frozen per-instance depth: 17 at 4, `lin105` at 3, `d198`/`pr152` at 2). These are working notes, not the manuscript, but they contradict the submission and should be corrected.
- **SUPP-P4 — Adapter skeleton is not the actual protocol.** `SUPP p4` lists `feasible` as a method and omits `mutate`, `crossover`, and `evaluate_batch`; the actual `ProblemAdapter` protocol has `evaluate` returning an `Evaluation` with feasibility, plus `mutate`, `crossover`, `evaluate_batch`, `initial_assignment`, `random_assignment`, `variable_count`, `option_count`, and `option_at`. Either label the listing as pseudocode or align it with the protocol. Minor, but it is the paper’s central interface.
- **SUPP-P5 — `bur26b` diversity table displays a contradiction.** `SUPP p3` says `bur26b` has 2 distinct gaps but best = worst = 0.565; the raw values are 0.564532 and 0.565239, which round to the same 3-decimal value. Show 4 decimals or note the rounding. The “no optima” claim is unaffected.
- **TXT-P6 — SciPy sentence.** `MS p6` says “It uses NumPy and SciPy for the independent QAP baseline.” The reported BLS baseline uses NumPy; SciPy is used for the optional/unreported `quadratic_assignment` baseline and the broad screen. Reword or drop the SciPy clause.
- **FIT-P7 — 8 pages vs rough 4–6 page guide.** 3,816 words is within JORS’s 3,000–4,000-word guidance; the 8-page PDF is above the rough page guide, not a formal limit. Not a blocker; if the editor asks, move Table 2 or broad-screen detail to the supplement, but do not cut below 3,000 words.
- **META-P8 — ORCID/DOI metadata.** ORCID is strongly recommended, not required; the paper has no ORCID. The data statement has a DOI pending, consistent with the public RC. Add ORCID in the submission system if available; no manuscript change required.
- **HYG-P9 — Public hygiene.** `paper2/evidence/lkh-provenance.json` `command` contains machine-specific absolute paths (`/srv/shared-data/gep/ws4/...`); replace with placeholders. `RELEASE-CANDIDATE.md:16` still lists the obsolete JoH variant `paper2/submission/paper2-sn-jnl.tex`; remove it from the JORS asset list. `paper2/submission/jors/README.md:37-39` says “lab byline” while the manuscript has an individual author; `:75` says the main manuscript/evidence were not edited, but rc14 edited the JORS `.tex` and manifest. Minor package hygiene.
- **STAT-P10 — Cluster interval has no committed analysis script.** The QAP `−0.300 to −0.111` interval and family equal-weighting are computed from public per-run JSON but no script in `paper2/` reproduces them; the raw data and method are clear, and prior recomputation matches. Add a small `analyze_qap_bls.py` if aiming for full one-command reproducibility; not a blocker.

## Recommendation

**Major revision — not submission-ready.** The scientific content, statistics, tabu scope, TSP disclosure, and JORS fit are sound. The only acceptance blocker is the stale `paper2-REPLAY.md` release asset; the tag tree and the manuscript are otherwise ready. Once the asset is replaced (and, for cleanliness, the P16 strings and stale manifest aliases are corrected), I expect the paper to be ready for acceptance.

## Prepared to review after revision

**Yes.** I will check that the `paper2-REPLAY.md` release asset matches the tag’s `paper2/REPLAY.md` and includes `--branch p14-evidence-rc14`; that the release title/body no longer say P16; that the manifest’s `pdf`/`submission_pdf` hashes match `0738fc6b…` (or the aliases are removed); and that a clean clone of the asset’s command replays the full 1,660-incumbent set with 25 `esc8` skips and five `brazil58` cap hits.

## Residual risk table

| Risk | Likelihood | Impact | Evidence | Mitigation |
| --- | --- | --- | --- | --- |
| Reader follows the release’s `paper2-REPLAY.md`, clones stale `main`, and reports the old 60-incumbent replay as the paper’s evidence | High | High | release asset sha `e987a27e…`; `main` `04e533c`; `paper2/README.md` “DO NOT SUBMIT”; main `replay_all.sh` runs three scripts | Replace the asset with the tag’s `paper2/REPLAY.md`; re-cut |
| Reader uses the manifest’s `pdf`/`submission_pdf` alias and gets a hash mismatch | Medium | Low–Medium | manifest lines 205-208, 227-230; actual PDF `0738…`; `jors_submission_pdf` correct | Update the two hashes or drop the aliases |
| Reader sees “P16” release title/README and doubts the artifact is the paper’s p14 release | Medium | Low | release title/body; root `README.md:3` | Change P16 to p14 |
| 8-page PDF exceeds the rough 4–6 page guide | Medium | Low | PDF 8 pp.; 3,816 words within limit | Publisher typesetting; move a table only if the editor asks |
| Working `paper2/README.md` says 14 instance means and adaptive depth | Medium | Low | `paper2/README.md:81,119`; `MS p4–5`; `SUPP p3–4` | Update or remove the working prose |
