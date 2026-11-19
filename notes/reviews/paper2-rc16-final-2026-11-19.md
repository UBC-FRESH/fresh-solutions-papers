# Paper 2 (JORS Issues in Research Software) — rc16 final major-blocker gate

**Manuscript:** “FRESH Solutions: an adapter and exact-replay harness for metaheuristic benchmarking” (Gregory Paradis, UBC FRESH Lab).
**Materials reviewed:** `paper2/submission/jors/paper2-jors.tex` / `.pdf` (8 pp., 3,830 words by `detex -n`); supplement `.tex` / `.pdf` (4 pp.); `paper2/submission/jors/README.md`; `cover-letter.md`; `highlights.md`; `paper2/evidence/manifest-v0.1.0-candidate.json`; `paper2/evidence/RELEASE-CANDIDATE.md`; `paper2/REPLAY.md`; public `p14-evidence-rc16` release and tag; public `v0.9.3-p13rc1` software release and tag; rc15 blocker review.
**Recommendation:** Minor revision — no major blockers.
**Prepared to review after revision:** Yes.

## Verdict

1. **MAJOR blockers: No.**
2. **Major blockers: none.**
3. **Recommendation: minor.**
4. **Submission-ready for JORS once minor suggestions are ignored: Yes.** “Submission-ready” here means ready to send to JORS, not accepted without review. The public release, tag, paper-2 assets, one-command replay, and every headline statistic verify. The remaining findings are a one-line manifest-ledger correction, stale package notes, a few wording/table/skeleton clarifications, and JORS production/metadata items. None changes a headline result, a table’s arithmetic, the replay, or the acceptance case. If “submission-ready” is read as a byte-perfect package, then the manifest hash in MINOR-01 should be corrected first; that is a one-line packaging fix, not an acceptance blocker.

## Confidential comments to the editor

The scientific core is sound and should not be rejected. This gate independently verified the rc16 tag and release, all three paper-2 release assets, the paper-2 manifest (all data hashes pass; one replay-script hash is stale), the full one-command replay, every headline statistic, the tabu/BLS scoping, and JORS scope/length. The prior rc15 factual minors are largely fixed: the 200-kick/20-patience wording, SciPy/BLS attribution, Figure 1 citation, 10k QAP manifest/replay coverage, and the paper’s replay count are correct. The remaining issues are small package-documentation and production items. I recommend minor revision, not major revision or rejection. The one concrete artifact-integrity item is a one-line manifest hash update; the documented replay itself passes.

## Summary

The manuscript is a credible JORS *Issues in Research Software* experience report. It describes a small adapter contract, resident state and a replay gate, QAP/TSP reference adapters, a convergence-controlled QAP framework check, a 20-instance QAP/BLS panel, a frozen mixed-depth TSP panel, broad screens, external LKH context, and a generic negative result. The negative results and scope discipline are strengths: the tabu reference is explicitly called untuned and unvalidated, BLS is the primary QAP quality reference, the TSP panel is explicitly frozen/mixed-depth, and the generic layer is reported as non-competitive rather than promoted.

The artifact’s data and replay verify end to end, with one stale manifest hash noted below. Tag `p14-evidence-rc16` resolves to `7e1b2990fc236e6d26771c248cc2b5ff09e9c446`; the release is public, a prerelease, and not a draft. The paper-2 assets match the tag: `paper2-jors.pdf` (373,615 bytes, sha256 `8ac97c26…`), `paper2-jors-supplement.pdf` (232,006 bytes, `38f17fab…`), and `paper2-REPLAY.md` (602 bytes, `f6a69c86…`). A clean clone of `--branch p14-evidence-rc16 --recurse-submodules` gives submodule `4583ad3b74bdf94d6b46c98bb3e1caf1b9b0dad2` (the `v0.9.3-p13rc1` commit). With complete `QAPLIB_ROOT`/`TSPLIB_ROOT` mirrors, `bash paper2/replay_all.sh` exits 0 and re-evaluates 40 framework + 20 deep-TSP, 20 QAP 10k, 200 expanded-QAP, 200 BLS, 100 expanded-TSP, 40 generic, and 1,060 broad incumbents; it reports 25 `esc8` skips and five `brazil58` cap hits.

The statistics match the evidence. Framework CPU ratio 1.2390 (bootstrap 95% CI 1.1683–1.3098); 40/40 patience, quality matches, and exact replays. QAP tabu mean 0.30085%, median 0.04268%, worst 5.69514%, 73/200 optima, 200/200 patience and replay; BLS mean 0.09614%, worst 1.36861%, 161/200 optima, 200/200 patience and replay. Paired mean difference 0.20471 pp; instance-cluster bootstrap 95% CI approximately 0.111–0.300 pp (paper’s −0.300 to −0.111); 15/16 non-tied instance means. Family means 0.421/0.234/0.240 (tabu) and 0.220/0.000/0.077 (BLS). TSP mean 0.003945%, worst 0.184577%, 94/100 optima, 95/100 patience, five `brazil58` cap hits (kicks 379–399). Broad QAP 134 instances/670 runs/552 patience/318 optima/converged mean 1.8233%/median 0/worst 36.4446%; broad TSP 78/390/236/195/mean 1.4597%, with 3/100 patience, 1 optimum, and 97 caps above n=300; LKH 75/100 optima, mean 0.09835%, median 0, worst 1.9301%, mean wall 15.013 s; generic QAP 3.8478% vs 0.0966%, TSP 127.978% vs 0.000%, about 116,868 exact evaluations per generic run.

JORS fit is acceptable. The paper is 3,830 words by `detex -n` (within the 3,000–4,000-word guidance), has two heading levels, an abstract, the expected declarations, 28 references, one figure, and two main tables. The 8-page PDF (6 text/figures/tables + 2 references) is above the journal’s rough 4–6-page guide but within the stated word limit; that is a production risk, not a word-limit failure or a rejection basis. The main fit risk is section placement: the paper reads partly like a Software Metapaper, but the abstract, cover letter, and “experience/reproducibility report” framing make the *Issues in Research Software* placement defensible.

## Verification ledger

| Check | Result | Evidence |
| --- | --- | --- |
| Release `p14-evidence-rc16` public and tagged | Pass | tag `7e1b2990…`; release published 2026-11-19T02:29:31Z; `isDraft=false`, `isPrerelease=true`; HTTP 200 |
| Software tag `v0.9.3-p13rc1` public | Pass | tag `4583ad3b…`; submodule `4583ad3b…`; HTTP 200 |
| Paper-2 release assets match tag | Pass | PDF `8ac97c26…`/373,615 B; supplement `38f17fab…`/232,006 B; replay asset `f6a69c86…`/602 B; byte-identical to tag |
| Manifest identity (manuscript/PDF/supplement) | Pass | `MAN:207-252`; manuscript `af846158…`, PDF `8ac97c26…`, supplement `987266ad…`, supplement PDF `38f17fab…` |
| Manifest evidence/data hashes | Pass | all 66 non-replay `files` entries, 11 path aliases, and four figure hashes match |
| Manifest replay-script hash | **Fail (MINOR-01)** | `MAN:190` and `MAN:227` say `3fb66945…` (the rc15 script); actual tag file is `e9cd3d8d…` |
| Release verification claim | **Stale (MINOR-01)** | `REL:9` says “manifest hashes match”; one does not |
| Clean one-command replay | Pass | clean tag clone; submodule `4583ad3`; `bash paper2/replay_all.sh` exit 0; 20/20 QAP 10k, 200/200 expanded QAP, 200/200 BLS, 100/100 expanded TSP, 1,060 broad, 40 generic, 40 framework + 20 deep TSP |
| `esc8` / `brazil58` disclosure | Pass | 25 `esc8` skips; 5 `brazil58` cap hits |
| Framework statistics | Pass | 40/40 patience, quality, replay; CPU ratio 1.2390 (1.1683–1.3098) |
| QAP/BLS statistics | Pass | 0.30085 vs 0.09614; diff 0.20471; CI approx. 0.111–0.300; 15/16; 73 vs 161 optima |
| TSP statistics | Pass | 0.003945 mean; 0.184577 worst; 94/100; 95/100; 5 caps |
| Broad/LKH/generic statistics | Pass | all headline numbers match summaries and raw records |
| 10k QAP coverage | Pass | `MAN:199-203`; `replay_all.sh:10`; 20/20 exact replays |
| Tabu scope | Pass | paper calls tabu untuned/unvalidated, BLS primary, no SOTA claim; supplement diversity table supports 0/80 `bur26` |
| JORS word length | Pass | 3,830 words by `detex -n`, within 3,000–4,000 |
| JORS page guide | Minor risk | 8 pages vs rough 4–6; not a formal limit |
| JORS structure/declarations | Pass | two heading levels, abstract, author contributions, funding, competing interests, data/code availability |

## Prior rc15 minors: requested checks

| Prior rc15 item | Status | Evidence |
| --- | --- | --- |
| 200-kick/20-patience wording | **Fixed** | `MS p3` (`paper2-jors.tex:181`); `tsp-convergence-pilot-summary.json` has `kicks_budget=200`, `patience=20`; raw runs 24–36 kicks; 3/4 optima |
| SciPy/BLS attribution | **Fixed** | `MS p6` (`:356-358`): SciPy for the separate SciPy FAQ QAP baseline; BLS uses NumPy and optional Numba |
| Figure 1 citation | **Fixed** | `MS p2` (`:99`) cites `Figure~\ref{fig:architecture}`; PDF shows “Figure 1” |
| 10k QAP manifest/replay coverage | **Fixed in coverage; residual note** | `MAN:199-203` includes `qap-tabu.json` and summary; `replay_all.sh:10` replays it; replay 20/20. The text still does not say the 10k pilot uses five seeds vs ten for the 100k panel (MINOR-06). The manifest’s replay-script hash is stale (MINOR-01). |
| Replay count | **Fixed in paper; README duplicate remains** | `MS p6` (`:369-370`) lists 20 QAP 10k; implicit total 1,680. `README:30-31` lists 20 QAP 10k twice, summing to 1,700 (MINOR-02). |
| Submission README consistency | **Partially fixed** | Word count/rc16 references/replay count updated; author byline, family interval, tabu diversity, TSP rerun decision, CPU “blocker,” provenance identity, and source discipline remain stale (MINOR-02). |

Other rc15 minors fixed: the extra space before the period (`MS p4`, now “1.33.”) and Figure 1 citation. Remaining prior minors are listed below; none is acceptance-blocking.

## Major comments

None.

## Minor comments

I classify every item below as MINOR. Each is a local correction that does not change a headline result, a table’s arithmetic, or the public replay.

- **MINOR-01 — The manifest’s `paper2/replay_all.sh` hash is stale.** `MAN:190` and `MAN:227` record `3fb6694599f3ea11c6986867ad6faf8dc93a88820016d1e7f0c97d15112f345c`, which is the rc15 script without the 10k line. The rc16 tag’s actual `paper2/replay_all.sh` is `e9cd3d8d310caeba2fa1bfe03e70e43e959c2eef2f16e6e4d24fb3f6c1860b0c`; the diff from rc15 is the added `python3 paper2/replay_qap_tabu.py --input qap-tabu.json` line. `REL:9` therefore overstates “manifest hashes match.” All data hashes pass and the replay passes, so this is a ledger/packaging error, not a broken replay or result. **Smallest fix:** replace both `3fb669…` entries with `e9cd3d8d…` (or regenerate the manifest), re-tag/re-release; alternatively change `REL:9` to “data hashes match; replay-script hash pending.” This should be fixed before submission, but it does not change the acceptance case.
- **MINOR-02 — The submission README still contradicts the manuscript/package.** `README:30-31` double-counts 20 QAP 10k (paper total 1,680, README text sums 1,700). `README:37-39` says the author list is the lab byline, while the manuscript and cover letter name Gregory Paradis. `README:47-50` still calls missing CPU timing an “Exact release blocker,” while `MS p6` (`:375-377`) explicitly scopes CPU timing. `README:51-52` says the manifest/tag are the “remaining identity check,” but both exist. `README:57-59` asks whether to rerun the TSP depth panel, while the paper says it is frozen (`MS p3`). `README:60-62` says there is no per-seed diversity table, but `SUPP p3` has one. `README:75-79` says the main manuscript/evidence were not edited and that the BLS inference uses the family interval (−0.234 to −0.163), while rc16 edited the JORS `.tex`/manifest and `MS p5` says the family interval is not reported. **Smallest fix:** refresh the README for rc16, delete resolved “Blocking issues,” and make its author/replay/statistics statements match the manuscript. Package notes, not the manuscript.
- **MINOR-03 — “Weak on asymmetric instances” is broader than the evidence.** `MS p7` (`:389`) says “The QAP reference is untuned and weak on asymmetric instances.” The weak case is the `bur26` family (0/80 optima); the asymmetric `chr` family has 41/50 optima and a 0.240% mean, close to BLS’s 41/50 optima. Section 3.2 correctly says “weak on the asymmetric `bur26` family” (`:260`). **Smallest fix:** narrow the limitations sentence to `bur26`. This is prior MINOR-03, still open.
- **MINOR-04 — `bur26b` diversity table displays a rounding contradiction.** `SUPP p3` (`:105`) reports “2 distinct gaps” with best = worst = 0.565. The raw values are 0.564532 and 0.565239, which both round to 0.565. **Smallest fix:** show four decimals (0.5645/0.5652) or add “rounding hides two values.” The “no optima” claim is unaffected. This is prior MINOR-05, still open.
- **MINOR-05 — Supplement adapter skeleton is not the protocol.** `SUPP p4` (`:176-182`) lists only `evaluate`, `feasible`, `propose`, `apply`, `undo`; it omits `mutate`, `crossover`, `evaluate_batch`, `initial_assignment`, `random_assignment`, `variable_count`, `option_count`, and `option_at`, and `evaluate` returns an `Evaluation` with feasibility. It is labeled “Minimal adapter skeleton,” but the paper’s central interface deserves alignment. **Smallest fix:** label it “pseudocode” or align it with `ProblemAdapter`. This is prior MINOR-06, still open.
- **MINOR-06 — The 10k pilot’s five-seed basis is still unstated.** `MS p3` (`:178-181`) compares 10k means (0.000/0.403/0.786/0.792) with 100k means (0.000/0.030/0.077/0.245). The 10k file has five seeds per instance (`qap-tabu.json`), while the 100k panel has ten (`qap-expanded-100k-10seed.json`). The 10k file is now in the manifest and replay (20/20), so the prior coverage gap is fixed; the text should say “five seeds” or add a footnote. This is prior MINOR-08 residual, not a result change.
- **MINOR-07 — Generic evaluation count is ambiguous.** `MS p7` (`:337-338`) says “The generic runs … use about 117,000 exact evaluations.” The actual mean is 116,868 per run; the 40-run total is 4,674,726. **Smallest fix:** “about 117,000 per run (4.7 million total)” so the work comparison is unambiguous. Minor clarity, not a result change.
- **MINOR-08 — Working package prose is stale.** `paper2/README.md:81` says BLS is stronger on “14 instance means” (the paper/data say 15 lower, one higher, four ties); `:119` says “Adaptive depth: 4 for n<100, 3 for 100<=n<150, 2 for n>=150” (the paper uses a frozen per-instance panel: 17 at depth 4, `lin105` at 3, `d198`/`pr152` at 2); `highlights.md:7` says “Software/evidence release and one-command replay are the remaining gate,” which rc16 has closed. **Smallest fix:** update or mark as working notes. This is prior MINOR-16, still open.
- **MINOR-09 — JORS style/metadata items.** The manuscript uses square-bracket numeric citations (`paper2-jors.tex:10`) where JORS’s author guidelines specify parentheses; the title/headings are sentence case where JORS describes title capitalization; table captions sit above the tables where JORS says underneath (`:232`, `:287`). The manuscript has no ORCID, the cover letter has no five suggested reviewers, and the APC/waiver is not confirmed. These are production/submission-metadata items, not scientific blockers. This is prior MINOR-12.
- **MINOR-10 — 8 pages vs rough 4–6-page guide.** 3,830 words is within 3,000–4,000; the PDF is 8 pages (6 text + 2 references). The journal calls the page figure “roughly”; do not cut below 3,000 words. If the editor asks, move Table 2 or broad-screen detail to the supplement. This is prior MINOR-13 and is explicitly not treated as a blocker here.
- **MINOR-11 — Licensing metadata conflict.** `CITATION.cff:12` says `license: MIT` for the whole deposit; `LICENSING.md:3-8` says code is MIT and manuscripts/evidence are CC BY 4.0; `.zenodo.json:10` says “other-open” with the split. **Smallest fix:** reconcile `CITATION.cff` before minting the DOI. The manuscript’s own Apache-2.0/MIT/CC BY 4.0 statement is clear. This is prior MINOR-14.
- **MINOR-12 — Third-party instance permission statement.** `paper2/instances/README.md` gives source URLs and says “Preserve source attribution,” but does not state an explicit licence or permission for the eight QAPLIB/TSPLIB files. **Smallest fix:** add a short owner/terms statement. Not a manuscript blocker. This is prior MINOR-15.
- **MINOR-13 — Public provenance contains a machine-specific path.** `paper2/evidence/lkh-provenance.json:20` has `/srv/shared-data/gep/ws4/...` in its `command` field. **Smallest fix:** replace with placeholders or environment variables. Hygiene, not a result issue. This is prior MINOR-11.
- **MINOR-14 — Default branch/tag checkout risk.** `paper2/REPLAY.md` pins `--branch p14-evidence-rc16`, and the release asset is correct. The manuscript’s §4 code block (`MS p6`, `:363-368`) gives the tag URL but the command block itself does not repeat the tag checkout, and `origin/main` remains stale. **Smallest fix:** add “from the p14-evidence-rc16 checkout” or a commit assertion; make `main` current. Residual risk, not a blocker. This is prior MINOR-10.
- **MINOR-15 — QAP/BLS cluster inference has no committed analysis script.** The paper reports the −0.300 to −0.111 interval, the −0.205 paired mean, and the 0.099%/0.298% family equal-weighting; these reproduce from the public per-run JSON (this gate recomputed 0.20471 and approximately 0.111–0.300), but no `paper2/analyze_qap_bls.py` is in the release. **Smallest fix:** add a small script or a supplement note with the resampling rule. Not a blocker because the raw data and method are clear and the values reproduce. This is prior MINOR-20.
- **MINOR-16 — Abstract length.** The abstract is about 260 words (255 by `detex` of the abstract text; the PDF reads at about 260). JORS’s published guidelines do not state an abstract limit; if the editor applies a 250-word house rule, trim 10 words. Not a blocker. This is prior MINOR-17.
- **MINOR-17 — Release-note wording.** The rc16 release body says “Updated manifest hashes,” but one replay-script hash is stale (MINOR-01). **Smallest fix:** correct the manifest and the release note together. This is prior MINOR-18.

## Recommendation

**Minor revision — no major blockers.** The scientific content, statistics, tabu scope, TSP disclosure, public release, assets, manifest data hashes, and one-command replay all verify. The required changes are a one-line manifest hash correction (`MINOR-01`), a submission-README refresh (`MINOR-02`), a few wording/table/skeleton clarifications (`MINOR-03`–`MINOR-07`), package-documentation cleanup (`MINOR-08`, `MINOR-11`–`MINOR-14`), and JORS production/metadata items (`MINOR-09`, `MINOR-10`, `MINOR-16`, `MINOR-17`). None changes the acceptance case.

## Prepared to review after revision

**Yes.** I will check the corrected manifest hash, the refreshed submission README, the 10k five-seed disclosure, the `bur26` limitation wording, the `bur26b` table precision, and the adapter-skeleton label. I will also re-check the JORS style items if the editor requests them.

## Residual risk table

| Risk | Likelihood | Impact | Evidence | Mitigation |
| --- | --- | --- | --- | --- |
| Reader verifies the manifest and finds the stale replay-script hash | Medium | Low | `MAN:190,227`; actual `e9cd3d8d…` vs `3fb66945…`; `REL:9` | Update both entries or soften `REL:9`; re-tag |
| Reader follows stale package notes instead of the manuscript | Medium | Low | `paper2/submission/jors/README.md:30-31,37-39,47-62,75-79`; `paper2/README.md:81,119`; `highlights.md:7` | Refresh or archive the notes |
| Reader follows a stale `main` clone instead of the release asset | Low | Medium | `paper2/REPLAY.md` pins rc16; `origin/main` stale; `MS p6` code block | Make `main` current or add a tag-checkout warning |
| Reader sees “weak on asymmetric instances” and cannot reproduce the `chr` claim | Low | Low | `MS p7`; `chr` 41/50 optima and 0.240% mean | Narrow to `bur26` |
| 10k five-seed vs 100k ten-seed comparison is not stated | Low | Low | `MS p3`; `qap-tabu.json` 5 seeds; 100k 10 seeds | State “five seeds” |
| Generic “about 117,000 evaluations” is read as total | Low | Low | `MS p7`; mean 116,868 per run; 4,674,726 total | Say “per run” |
| 8-page PDF exceeds the rough 4–6-page guide | Medium | Low | PDF 8 pp.; 3,830 words within limit | Publisher typesetting; move a table only if the editor asks |
| JORS style items (brackets, title case, table captions) delay production | Medium | Low | `MS` citations/captions; JORS author guidelines | Copyedit before submission |
