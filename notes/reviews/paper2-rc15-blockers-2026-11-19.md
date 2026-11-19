# Paper 2 (JORS Issues in Research Software) — rc15 major-blocker review

**Manuscript:** “FRESH Solutions: an adapter and exact-replay harness for metaheuristic benchmarking” (Gregory Paradis, UBC FRESH Lab).
**Materials reviewed:** `paper2/submission/jors/paper2-jors.tex` / `.pdf` (8 pp., 3,816 words); supplement `.tex` / `.pdf` (4 pp.); `paper2/submission/jors/README.md`; `cover-letter.md`; `highlights.md`; `paper2/evidence/manifest-v0.1.0-candidate.json`; `paper2/evidence/RELEASE-CANDIDATE.md`; `paper2/REPLAY.md`; public `p14-evidence-rc15` release and tag; public `v0.9.3-p13rc1`; rc14 blocker review.
**Recommendation:** Minor revision — no major blockers.
**Prepared to review after revision:** Yes.

## Verdict

1. **MAJOR blockers: No.**
2. **Major blockers: none.**
3. **Recommendation: minor.**
4. **Submission-ready for JORS once minor suggestions are ignored: Yes.** “Submission-ready” here means ready to send to JORS, not accepted without review. The public release, tag, manifest, asset hashes, and one-command replay verify. The remaining findings are minor factual, style, metadata, and package-documentation corrections; none changes a headline result or the acceptance case.

## Confidential comments to the editor

The scientific core is sound and should not be rejected. I independently verified the rc15 tag and release assets, all manifest hashes, the full one-command replay, every headline statistic, the tabu/BLS scoping, and the JORS length/fit. The rc14 blocker (the release’s `paper2-REPLAY.md` asset cloning the stale default branch) is fixed: the asset now pins `--branch p14-evidence-rc15`, is byte-identical to the tag’s `paper2/REPLAY.md`, and a clean clone replays all 1,660 incumbents with the expected 25 `esc8` skips and five `brazil58` cap hits. The remaining issues are small factual slips, stale package notes, and production/style items. I recommend minor revision, not major revision or rejection.

## Summary

The manuscript is a credible JORS *Issues in Research Software* experience report: it describes a small adapter contract, resident state and a replay gate, QAP/TSP reference adapters, a convergence-controlled QAP framework check, a 20-instance QAP/BLS panel, a frozen mixed-depth TSP panel, broad screens, external LKH context, and a generic negative result. The negative results and scope discipline are strengths: the tabu reference is explicitly called untuned and unvalidated, BLS is the primary QAP quality reference, the TSP panel is explicitly frozen/mixed-depth, and the generic layer is reported as non-competitive rather than promoted.

The artifact verifies end to end. Tag `p14-evidence-rc15` resolves to `19d3e59`. Release assets: `paper2-jors.pdf` (373,295 bytes, sha256 `312cd7dc…`), `paper2-jors-supplement.pdf` (232,006 bytes, `38f17fab…`), and `paper2-REPLAY.md` (563 bytes, `499d3ecc…`); all three match the tag tree. The manifest’s 65 `files` entries, nine top-level manuscript/reference/PDF aliases, and four figure entries all pass (78/78); the manifest status, manuscript hash (`6c0667b3…`), PDF hash (`312cd7dc…`), supplement hash (`38f17fab…`), and supplement `.tex` hash (`987266ad…`) are correct. A clean clone of `--branch p14-evidence-rc15 --recurse-submodules` gives submodule `4583ad3` (the `v0.9.3-p13rc1` commit). With `QAPLIB_ROOT`/`TSPLIB_ROOT` set, `bash paper2/replay_all.sh` exits 0 and re-evaluates 40 framework + 20 deep-TSP, 200 expanded-QAP, 200 BLS, 100 expanded-TSP, 40 generic, and 1,060 broad incumbents; it reports 25 `esc8` skips and five `brazil58` cap hits.

The statistics match the evidence. Framework CPU ratio 1.2390 (bootstrap 95% CI 1.1685–1.3128); 40/40 patience, quality matches, and exact replays. QAP tabu mean 0.30085%, median 0.04268%, worst 5.69514%, 73/200 optima, 200/200 patience and replay; BLS mean 0.09614%, worst 1.36861%, 161/200 optima, 200/200 patience and replay. Paired mean difference 0.20471 pp; instance-cluster bootstrap 95% CI 0.1115–0.2993 pp (paper’s −0.300 to −0.111); 15/16 non-tied instance means. Family means 0.421/0.234/0.240 (tabu) and 0.220/0.000/0.077 (BLS). TSP mean 0.003945%, worst 0.184577%, 94/100 optima, 95/100 patience, five `brazil58` cap hits. Broad QAP 134 instances/670 runs/552 patience/318 optima/mean 1.8233%/median 0/worst 36.4446%; broad TSP 78/390/236/195/mean 1.4597%, with 3/100 patience, 1 optimum, and 97 caps above n=300; LKH 75/100 optima, mean 0.09835%, median 0, worst 1.9301%, mean wall 15.013 s; generic QAP 3.8478% vs 0.0966%, TSP 127.978% vs 0.000%, about 116,868 exact evaluations.

JORS fit is acceptable. The paper is 3,816 words by `detex -n` (within the 3,000–4,000-word guidance), has two heading levels, an abstract, the expected declarations, and 28 references. The 8-page PDF (6 text/figures/tables + 2 references) is above the journal’s rough 4–6-page guide but within the stated word limit; that is a production risk, not a word-limit failure or a rejection basis. The main fit risk is section placement: the paper reads partly like a Software Metapaper, but the abstract, cover letter, and “experience/reproducibility report” framing make the *Issues in Research Software* placement defensible.

## Verification ledger

| Check | Result | Evidence |
| --- | --- | --- |
| Release `p14-evidence-rc15` public and tagged | Pass | tag `19d3e59`; release published 2026-11-19; `gh release view` and HTTP 200 |
| Release assets match tag | Pass | PDF `312cd7dc…`, supplement `38f17fab…`, replay asset `499d3ecc…` |
| Manifest hashes | Pass | 65 `files` + 9 manuscript/PDF aliases + 4 figures = 78/78 |
| Manifest identity | Pass | status `p14-evidence-rc15`; manuscript/PDF/supplement hashes match |
| Clean one-command replay | Pass | `--branch p14-evidence-rc15 --recurse-submodules`; submodule `4583ad3`; `replay_all.sh` exit 0; 1,660 incumbents; 25 `esc8` skips; 5 `brazil58` caps |
| Framework statistics | Pass | 40/40 patience, quality, replay; ratio 1.2390 (1.1685–1.3128) |
| QAP/BLS statistics | Pass | 0.30085 vs 0.09614; diff 0.20471; CI 0.1115–0.2993; 15/16; 73 vs 161 optima |
| TSP statistics | Pass | 0.003945 mean; 0.184577 worst; 94/100; 95/100; 5 caps |
| Broad/LKH/generic statistics | Pass | all headline numbers match summaries and raw records |
| Tabu scope | Pass | paper calls tabu untuned/unvalidated, BLS primary, no SOTA claim; supplement diversity table supports the 0/80 `bur26` result |
| JORS word length | Pass | 3,816 words by `detex -n`, within 3,000–4,000 |
| JORS page guide | Minor risk | 8 pages vs rough 4–6; not a formal limit |

## Major comments

None.

## Minor comments (all MINOR; none is an acceptance blocker)

I classify the items below as MINOR because each is a local correction that does not change a headline result, a table’s arithmetic, or the public replay. The two factual slips (`MINOR-01`, `MINOR-02`) should be fixed before submission, but they do not undermine the paper’s acceptance case.

- **MINOR-01 — “20-kick pilot” is mislabeled.** `MS p3` (`paper2-jors.tex:180`) says “a 20-kick pilot reached the optimum on three of four instances.” `paper2/evidence/tsp-convergence-pilot-summary.json` has `kicks_budget: 200` and `patience: 20`; the raw records show 24–36 kicks and patience stops. Change to “200-kick/20-patience pilot” (or “20-patience pilot”). The result itself (3/4 optima) is correct.
- **MINOR-02 — SciPy is attributed to the wrong baseline.** `MS p6` (`paper2-jors.tex:354-356`) says “It uses NumPy and SciPy for the independent QAP baseline.” The reported independent baseline is BLS, implemented with NumPy/Numba (`paper2/qap_bls.py`); SciPy is used for a separate, unreported `quadratic_assignment` baseline (`paper2/evidence/qap-scipy-expanded.json`) and the broad screen. Reword to “NumPy for the reference adapters and BLS; SciPy for an optional weaker baseline” or drop SciPy.
- **MINOR-03 — “Weak on asymmetric instances” is broader than the evidence.** `MS p7` (`paper2-jors.tex:386`) says “The QAP reference is untuned and weak on asymmetric instances.” The weak case is `bur26`; the asymmetric `chr` family has 41/50 optima and a 0.240% mean. Narrow to “weak on the asymmetric `bur26` family.”
- **MINOR-04 — `brazil58` kick range excludes one seed.** `MS p5` says “roughly 380–400 kicks”; the five records are 379, 381, 387, 397, 399. Say “about 380–400” is defensible, but “379–399” is exact. Cosmetic.
- **MINOR-05 — `bur26b` diversity table displays a contradiction.** `SUPP p3` (`paper2-jors-supplement.tex:105`) reports “2 distinct gaps” with best = worst = 0.565. The raw values are 0.564532 and 0.565239, which round to 0.565. Show four decimals or add “rounding hides two values.” The “no optima” claim is unaffected.
- **MINOR-06 — Supplement adapter skeleton is not the protocol.** `SUPP p4` lists `evaluate`, `feasible`, `propose`, `apply`, `undo`; it omits `mutate`, `crossover`, `evaluate_batch`, `initial_assignment`, `random_assignment`, `variable_count`, `option_count`, and `option_at`, and `evaluate` returns an `Evaluation` with feasibility. Label it “pseudocode” or align it with `ProblemAdapter`. This is the paper’s central interface, so the fix is worth making.
- **MINOR-07 — Extra space before a period.** `MS p4` (`paper2-jors.tex:207-208`) has “1.33 .” Cosmetic.
- **MINOR-08 — 10k-budget evidence is not in the manifest and uses five seeds.** `MS p3`’s 10,000-iteration means (0.000/0.403/0.786/0.792) come from `paper2/evidence/qap-tabu.json` (4 instances × 5 seeds), which is not in `manifest-v0.1.0-candidate.json` and is not replayed by `replay_all.sh`; the 100k means use ten seeds. Add the 10k file to the manifest/replay set or state the five-seed 10k vs ten-seed 100k comparison. The qualitative budget claim is still supported by the 20k/40k/80k data.
- **MINOR-09 — Submission README’s “Blocking issues” list is stale.** `paper2/submission/jors/README.md:43-71` still calls CPU timing an “Exact release blocker” (the manuscript scopes it at `MS p7`), asks whether to rerun the TSP depth panel (the paper discloses it as frozen), and says the tabu result lacks a per-seed diversity table (the supplement now has one). It also says “Author list is the lab byline” while the manuscript has an individual author, says the main manuscript/evidence were not edited while rc15 edited the JORS `.tex` and manifest, and says the BLS inference uses the family interval (−0.234 to −0.163) while the manuscript explicitly says the family interval is not reported. These are package notes, not the manuscript, but they contradict the submission.
- **MINOR-10 — Default branch is stale and the manuscript’s replay paragraph does not repeat the tag checkout.** `origin/main` is `04e533c` (P12.1); its `paper2/README.md` says “DO NOT SUBMIT” and its `replay_all.sh` runs only the old 60+20 set. The rc15 release asset and `paper2/REPLAY.md` pin `--branch p14-evidence-rc15`, so the documented one-command replay works; the manuscript’s §4 gives the tag URL but the command block itself does not say “from the p14-evidence-rc15 checkout.” Add that phrase (or a commit assertion) and make `main` current. Residual risk, not a blocker.
- **MINOR-11 — Public provenance contains machine-specific paths.** `paper2/evidence/lkh-provenance.json:20` has `/srv/shared-data/gep/ws4/...` in its `command` field. Replace with placeholders or environment variables. Hygiene, not a result issue.
- **MINOR-12 — JORS style/metadata items.** The manuscript uses square-bracket numeric citations (`[1]`) where JORS’s author guidelines specify parentheses; the title/headings are sentence case where JORS describes title capitalization; table captions sit above the tables where JORS says underneath. The manuscript has no ORCID, the cover letter has no five suggested reviewers, and the APC/waiver is not confirmed. The data statement has a public release URL but no DOI; acceptable while the DOI is pending, but confirm with the editor. These are production/submission-metadata items, not scientific blockers.
- **MINOR-13 — 8 pages vs rough 4–6-page guide.** 3,816 words is within 3,000–4,000; the PDF is 8 pages (6 text + 2 references). The journal calls the page figure “roughly”; do not cut below 3,000 words. If the editor asks, move Table 2 or broad-screen detail to the supplement.
- **MINOR-14 — Licensing metadata conflict.** `CITATION.cff` says `license: MIT` for the whole deposit; `LICENSING.md` says code is MIT and manuscripts/evidence are CC BY 4.0; `.zenodo.json` says “other-open” with the split. Reconcile `CITATION.cff` before minting the DOI. The manuscript’s own Apache-2.0/MIT/CC BY 4.0 statement is clear.
- **MINOR-15 — Third-party instance permission statement.** `paper2/instances/README.md` gives source URLs and says “Preserve source attribution,” but does not state an explicit licence or permission for the eight QAPLIB/TSPLIB files. Add a short owner/terms statement. Not a manuscript blocker.
- **MINOR-16 — Working package prose is stale.** `paper2/README.md:81` says BLS is stronger on “14 instance means” (the paper/data say 15 of 16 non-tied) and `:119` says “Adaptive depth: 4 for n<100, 3 for 100<=n<150, 2 for n>=150” (the paper uses a frozen per-instance panel: 17 at depth 4, `lin105` at 3, `d198`/`pr152` at 2). `highlights.md` says “Software/evidence release and one-command replay are the remaining gate,” which rc15 has now closed. Update or mark as working notes.
- **MINOR-17 — Abstract length.** The abstract is 260 words. JORS’s published guidelines do not state an abstract limit; if the editor applies a 250-word house rule, trim 10 words. Not a blocker.
- **MINOR-18 — Release-note wording.** The rc15 release body says “Updated manifest hashes and paper counts after the text fix”; the paper counts did not change (8 pages, 3,816 words). Cosmetic.
- **MINOR-19 — Figure 1 is not cited in the body.** The manuscript defines `\label{fig:architecture}` but never uses `\ref{fig:architecture}` or the words “Figure 1”; JORS’s submission checklist requires all figures to be cited in the text. Add “Figure 1” at the evidence-boundary paragraph in §2.1. The two tables are cited (`Table~\ref{tab:qap}`, `Table~\ref{tab:tsp}`).
- **MINOR-20 — QAP/BLS cluster inference has no committed analysis script.** The paper reports the −0.300 to −0.111 interval, the −0.205 paired mean, and the 0.099%/0.298% family equal-weighting; I reproduced them from the public per-run JSON, but no `paper2/analyze_qap_bls.py` (or equivalent) is in the release. Add a small script or a supplement note with the resampling rule. Not a blocker because the raw data and method are clear and the values reproduce.

## Recommendation

**Minor revision — no major blockers.** The scientific content, statistics, tabu scope, TSP disclosure, public release, manifest, asset hashes, and one-command replay all verify. The required changes are small factual corrections (`MINOR-01`–`MINOR-04`), supplement clarity and the cluster-inference script (`MINOR-05`–`MINOR-06`, `MINOR-20`), the 10k manifest/replay coverage (`MINOR-08`), package-documentation cleanup (`MINOR-09`–`MINOR-11`, `MINOR-16`), and JORS production/metadata items (`MINOR-12`–`MINOR-15`, `MINOR-17`, `MINOR-19`). None changes the acceptance case.

## Prepared to review after revision

**Yes.** I will check the corrected 200-kick/20-patience pilot, the SciPy/BLS wording, the `bur26` scope, the 10k manifest/replay coverage, and that the submission README no longer calls scoped items “blocking.” I will also re-check the JORS style items if the editor requests them.

## Residual risk table

| Risk | Likelihood | Impact | Evidence | Mitigation |
| --- | --- | --- | --- | --- |
| Reader follows a stale `main` clone instead of the release asset | Low | Medium | `origin/main` `04e533c`; `paper2/README.md` “DO NOT SUBMIT”; release asset pins `p14-evidence-rc15` | Make `main` current or add a tag-checkout warning |
| Reader sees “20-kick pilot” and cannot reproduce the budget | Medium | Low | `MS p3`; `tsp-convergence-pilot-summary.json` has 200 kicks/20 patience | Correct to “200-kick/20-patience” |
| Reader reproduces the BLS baseline expecting SciPy | Low | Low | `MS p6`; `qap_bls.py` uses NumPy/Numba | Reword the SciPy clause |
| 10k QAP numbers are not in the manifest/replay | Low | Low | `qap-tabu.json`; manifest lacks it | Add it or state the source/seed count |
| 8-page PDF exceeds the rough 4–6-page guide | Medium | Low | PDF 8 pp.; 3,816 words within limit | Publisher typesetting; move a table only if the editor asks |
| JORS style items (brackets, title case, table captions) delay production | Medium | Low | `MS` citations/captions; JORS author guidelines | Copyedit before submission |
| Default-branch package notes contradict the manuscript | Medium | Low | `paper2/submission/jors/README.md:43-71`; `paper2/README.md:81,119` | Update the working notes |
