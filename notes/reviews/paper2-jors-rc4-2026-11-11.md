# Reviewer Report — Paper 2 (JORS, Issues in Research Software), rc4

**Manuscript:** FRESH Solutions: an adapter and exact-replay harness for metaheuristic benchmarking
**Author:** Gregory Paradis, UBC FRESH Lab, University of British Columbia
**Materials reviewed:** `paper2/submission/jors/paper2-jors.tex`; `paper2/submission/jors/paper2-jors.pdf` (8 pp.); `paper2/submission/jors/paper2-jors-supplement.pdf` (2 pp.); `paper2/submission/jors/README.md`; `paper2/submission/jors/cover-letter.md`; `paper2/evidence/manifest-v0.1.0-candidate.json`; public release `p14-evidence-rc4`; FRESH Solutions release `v0.9.3-p13rc1`; and the prior review `notes/reviews/paper2-jors-antagonistic-2026-11-11.md`.
**Reviewer stance:** Independent antagonistic JORS associate editor / Reviewer 2. I checked the headline numbers against the committed evidence, recomputed the BLS statistics from the per-run JSON, verified the public release asset hashes and the tagged source, and inspected the replay/container scripts. I did not rerun the campaigns.
**Recommendation:** **Minor revision** — the science is now substantially sound, but the submission package is not yet submission-ready.
**Prepared to review after revision:** **Yes.**
**Refereeing openly:** No.
**Include in annual reviewer list:** No.

---

## Overrides (project-specific constraints)

- Target venue: **JORS, Issues in Research Software** — experience/reproducibility report, 3,000–4,000 words, roughly 4–6 pages, Vancouver-style numbered references, no mandatory LaTeX template (`notes/plans/p14-journal-shift-2026-11-11.md:140–142, 165–166, 232`).
- Evidence tags: `MS pX` for the PDF page, `Table N` / `Fig N` for objects, and `file:line` or repository paths for evidence and code.
- No external literature is introduced. General domain judgment is applied only to the submission's own claims and evidence.
- All materials are treated as confidential. No reviewer-identifying details are included.

---

## 1. Document inventory

| Item | Status | Notes |
|---|---|---|
| `paper2-jors.pdf` | Present | 8 pages: body through p7, references on p7–8; 2 figures, 2 tables, 28 references. |
| `paper2-jors.tex` | Present | 439 lines; 3,806 words by `detex -n paper2-jors.tex \| wc -w`; one overfull hbox (31.5 pt) at lines 381–386. |
| `paper2-jors-supplement.pdf` | Present | 2 pages; framework, per-instance QAP, and per-instance TSP tables. |
| Public release `p14-evidence-rc4` | Present | Public prerelease at tag `8c25074`; `paper2-jors.pdf` and supplement SHA-256 match the submitted files exactly (`a0ef06f4…`, `b377d9a5…`). |
| Tagged source | Matches manuscript | `git show p14-evidence-rc4:paper2/submission/jors/paper2-jors.tex` is byte-identical to the submitted `.tex`; the supplement is also identical. |
| Evidence manifest | Present, mostly consistent | 66 files; I recomputed every SHA-256: 0 missing, 0 mismatched. The manifest includes the ten-seed `qap-expanded-100k-10seed` files. Its `replay` entry is stale (`cdc8b45…` vs actual `3fb669…`), and its `status` still says “no tag/release created.” |
| FRESH Solutions release `v0.9.3-p13rc1` | Present | Public prerelease; tag resolves to `4583ad3`; Apache-2.0. |
| Container | Present, untested/inconsistent | `container/Dockerfile:6–7` checks out `7d3c831` (campaign commit, pre-GEO fix), not `4583ad3` or `c7d1507`. |
| Author metadata | **Incomplete** | Name/affiliation/email only; no ORCID, CRediT, funding, competing interests, or acknowledgements (`MS p1`; `paper2/submission/jors/README.md:37–39`). |
| Release package metadata | **Stale/contradictory** | The tagged source still contains `README.md:3` “release candidate 1 (`p14-evidence-rc1`)”, `LICENSING.md:11` “repository is not yet public”, `paper2/evidence/RELEASE-CANDIDATE.md:3` “local candidate only. No tag, release…”, and `paper2/paper2-draft.md:3` “INTERNAL DRAFT — NOT SUBMISSION-READY”. |

---

## 2. Quick synopsis

The manuscript describes a Python harness with a small problem-adapter contract, resident assignment state, an exact replay gate, a stopping/budget taxonomy, and QAP/TSP reference adapters. It reports a 40-run framework-use check, a 200-run QAP/BLS panel, a 100-run mixed-depth TSP breadth panel, broad QAP/TSP screens, an external LKH capability check, and a generic adapter-only negative result.

The JORS experience-report framing is appropriate, and the paper is much improved from the prior version. The release assets and tagged manuscript now match the submitted rc4 files; the availability contradictions (“public” vs “not public”) are gone; per-record CPU is now explicitly scoped (“where available”); the manifest does cover the ten-seed files; BLS is described as the primary QAP quality reference; and the TSP mixed depth is disclosed in the abstract and §3.3.

The submission is nevertheless not submission-ready. The manuscript still contains a literal `[DOI to be assigned]` placeholder and a paragraph that calls the artifact a “release blocker.” The public release package still contains stale documents that say the repository is not public, the release is a local candidate, and the paper is not submission-ready. The tabu reference is still called “robust” in the abstract and Table 1 while the text calls it “unvalidated,” and the 0/80 `bur26` result remains unexplained despite seed-invariant, near-optimal outcomes. The redistribution statement is false: eight QAPLIB/TSPLIB instance files are in the release. Author metadata and journal statements are missing. These are bounded fixes, but they are not cosmetic for a reproducibility venue.

---

## 3. Status of the five earlier P0s

| Earlier P0 | Status | Evidence |
|---|---|---|
| **1. Release assets/source match the cited rc4 manuscript** | **Closed for the manuscript** | Release assets `paper2-jors.pdf` and `paper2-jors-supplement.pdf` match the submitted files byte-for-byte (`a0ef06f4…`, `b377d9a5…`); tagged `.tex` is identical; PDF says `p14-evidence-rc4` four times. Residual: the release package’s top-level docs still say rc1/not public (see M1). |
| **2. Availability status internally consistent; DOI handled honestly** | **Partly closed** | The “not public” and “candidate rather than a candidate” contradictions are removed (`MS p6`). But `[DOI to be assigned]` remains (`paper2-jors.tex:354`), the abstract says “DOI pending explicitly” (`MS p1`), and the “release blocker” paragraph remains (`MS p6`). Honest, but not submission-ready. |
| **3. Per-record schema/CPU/manifest claims match evidence** | **Mostly closed** | CPU is scoped (“where available”, `MS p3`), and the missing 0/300 CPU fields are disclosed (`MS p6`). The manifest includes the ten-seed files; 66/66 hashes verify. Residual: the broad-screen records use a different schema, and the manifest’s `replay` hash is stale. |
| **4. Tabu `bur26` credibility and BLS-primary framing** | **Partly closed** | BLS is called the primary QAP quality reference and the tabu is called “unvalidated” (`MS p5`). But “robust tabu” remains in the abstract (`MS p1`), Table 1 caption (`MS p4`), §2.4 (`MS p3`), Limitations (`MS p7`), and the supplement header. No diagnostic or per-seed diversity table is added. |
| **5. JORS length/focus and mixed-depth TSP framing** | **Largely closed** | Mixed depth is disclosed in the abstract (`MS p1`) and §3.3 (`MS p5`); the paper says it is “not a controlled factor.” Length is down to 8 pages (body ≈6.5 pages) from 9; word count 3,806 is inside 3,000–4,000. Residual: still above the rough 4–6 page guide; the conclusion omits “mixed-depth”; no “Lessons” section. |

---

## 4. Confidential comments to the editor

I recommend **minor revision**, not rejection. The paper now does what a JORS Issues in Research Software paper should do: it describes a real software boundary, reports both positive and negative results, and provides a public, replayable evidence set. The prior review’s most serious artifact objections have been addressed: the release contains the rc4 manuscript, the availability paragraph no longer says both “public” and “not public,” CPU is scoped, the manifest covers the ten-seed files, and BLS is primary.

The remaining problems are concentrated in three places. First, the submission package still contradicts its own status: the tagged source says rc1, “not yet public,” “local candidate only,” and “not submission-ready,” while the manuscript says the artifact is public. Second, the manuscript still contains a DOI placeholder and a “release blocker” paragraph; for a reproducibility venue, that reads as an internal checklist rather than a finished artifact. Third, the tabu reference is still labelled “robust” in the headline objects while the text says it is unvalidated; the 0/80 `bur26` result with seed-invariant outcomes needs either a diagnostic or a clean, consistent demotion.

None of these require new campaigns. They require a re-cut release, a consistent vocabulary, corrected licence/redistribution text, and author metadata. I would be willing to review a revision and would expect it to be acceptable after those fixes.

---

## 5. Comments to the authors

### 5.1 Summary

The manuscript addresses a genuine engineering problem: applying known metaheuristics to new problems is slowed by the machinery around the search — state, moves, feasibility, stopping, replay, and benchmark bookkeeping. The adapter contract, resident-state path, and replay gate are sensible design ideas. The paper is unusually candid about failures: the tabu’s `bur26` weakness, the `brazil58` cap hits, the generic layer’s non-competitiveness, and the missing per-record CPU. The QAP/TSP reference implementations are serious efforts, and the BLS baseline is a substantial addition.

The paper’s centre of gravity is now much closer to JORS. The abstract leads with the harness and the evidence boundary, the QAP/BLS comparison is clustered, and the TSP mixed depth is disclosed. The remaining issues are not about the quality of the empirical work; they are about claim consistency, artifact presentation, and submission readiness.

### 5.2 What works (evidence-based strengths)

1. **The adapter boundary is clearly specified.** The contract separates discrete state, exact evaluation, feasibility, mutation/crossover, and reversible moves, and the search layer sees only that interface (`MS p2`; `paper2-jors.tex:128–141`). The `apply`/`undo` exact-inverse requirement and the adapter-owned permutation invariant are well stated (`MS p2`).
2. **The replay gate is the right idea.** A stored incumbent is re-evaluated through a new adapter state, not the optimizer’s cached counter (`MS p3`; `paper2-jors.tex:152–159`). The gate checks objective, feasibility, and permutation validity, and it fails closed.
3. **The stopping taxonomy is useful.** Plateau stop, safety-cap hit, budget exhaustion, and invalid replay are distinguished, and the denominator is visible (`MS p3`; `paper2-jors.tex:169–175`). This is better than most heuristic papers.
4. **The headline QAP/BLS/TSP/framework numbers reproduce.** I checked the QAP panel against `qap-expanded-100k-10seed.json` (0.301% mean, 0.043% median, 5.695% worst, 73/200 optima), the BLS panel against `qap-bls-10seed.json` (0.096% mean, 1.369% worst, 161/200 optima), the TSP panel against `tsp-expanded-10k.json` (0.004% mean, 0.185% worst, 94/100 optima, 95/100 patience), and the framework panel against `framework-use-summary.json` (1.239 mean CPU ratio, 1.17–1.31 bootstrap interval). The arithmetic is consistent.
5. **The BLS inference is clustered.** The cluster-by-instance interval is the right primary summary. Recomputing from the per-run JSON gives **−0.2991 to −0.1108** (the paper rounds to −0.300 to −0.111), a point estimate of **−0.2047**, and **15/16** non-tied instance means (p = 5.19 × 10⁻⁴). This addresses the prior JoH review’s main statistical objection.
6. **The one-command replay now covers the BLS panel.** `paper2/replay_all.sh:9,12` uses `QAP_EXPANDED_EVIDENCE=qap-expanded-100k-10seed.json` and `--input qap-bls-10seed.json`. This fixes the prior JoH review’s M3.
7. **The TSP mixed depth is disclosed in the abstract and §3.3.** `MS p1` says “frozen, mixed-depth”; `MS p5` gives 17 depth 4, `lin105` depth 3, `d198`/`pr152` depth 2, and says it is not one adaptive-depth experiment. That is the right direction, and it is a real improvement over the prior draft.
8. **The supplement is appropriate.** Full per-instance QAP/TSP tables and the framework panel are in the supplement, which is the right place for a 3,000–4,000-word JORS paper.
9. **The paper is candid about scope.** It explicitly says the generic layer is not competitive, the tabu is an unvalidated reference, the LKH comparison is capability-only, and portability is demonstrated by two adapters written by the reference author (`MS p6–7`). This candour is a strength.

### 5.3 Venue fit by component

| Component | Current role | JORS fit | Recommendation |
|---|---|---|---|
| Adapter/replay contract | Core contribution, §2 | **Strong** | Keep; lead the abstract and introduction with it. |
| Framework overhead (1.24×) | §3.1, abstract, conclusion | **Moderate** | Keep as a short implementation-cost paragraph. State the aggregation (mean of per-instance ratios; pooled ratio is 1.215). |
| QAP/BLS panel | §3.2, Table 1, abstract | **Moderate** | Keep one table and two paragraphs as evidence-boundary validation; put BLS first and label the tabu “reference (unvalidated).” |
| TSP breadth panel | §3.3, Table 2, abstract, conclusion | **Moderate** | Keep as a protocol-drift lesson; add “mixed-depth” to the conclusion. |
| Broad screens | §3.4 | **Weak** | One paragraph or supplement; not a headline. |
| External LKH | §3.4 | **Weak** | One sentence or cut. It is capability-only and not matched time. |
| Generic negative result | §3.4 | **Strong as a lesson** | Keep one paragraph; state random starts and work; frame as “the adapter contract is not a search engine.” |
| BLS inference | §3.2 | **Moderate** | Keep the cluster-by-instance interval; label the 3-family bootstrap informal and drop or stratify the sign-test p-value. |

### 5.4 Major comments

#### M1. The release package still contradicts its own public rc4 status (P1)

**Evidence.** The manuscript says the artifact is public as `p14-evidence-rc4` (`MS p1`; `paper2-jors.tex:46`) and points readers to `.../releases/tag/p14-evidence-rc4` (`MS p6`; `paper2-jors.tex:352–353`). The release assets and the tagged manuscript now match (P0-1 is closed for the manuscript). But the tagged source — the artifact a reader downloads — still contains:

- `README.md:3`: “Public release status: **P14 release candidate 1** (`p14-evidence-rc1`)”. The worktree was corrected to rc4 in `c334f19`, which is **one commit after** the tag (HEAD is two commits after).
- `paper2/evidence/RELEASE-CANDIDATE.md:3`: “Status: local candidate only. No tag, release, visibility change, or DOI has been made.”
- `LICENSING.md:11`: “The repository is not yet public.”
- `paper2/README.md:3–4`: “The paper is a working draft, not a submission-ready article.”
- `paper2/paper2-draft.md:3`: “Status: **INTERNAL DRAFT — NOT SUBMISSION-READY**”; line 165 still reports the old LKH 71/100 result.
- `paper2/submission/jors/cover-letter.md:16–19`: “the repository and DOI fields are placeholders until that release is approved.”
- `paper2/submission/jors/README.md:35–41`: “Software repository: `[repository URL to be supplied at release]`”; “individual authors … not yet supplied.”

**Why it matters.** The paper’s central claim is an exact, replayable evidence boundary. A reader who follows the citation lands on a release whose own README says rc1 and whose licence says the repository is not public. That is precisely the kind of provenance inconsistency the harness is supposed to prevent. It is not a scientific error, but it is a credibility error in the artifact the paper is selling.

**Action.**
- Re-cut the release from the final commit after updating `README.md`, `LICENSING.md`, `paper2/README.md`, `paper2/evidence/RELEASE-CANDIDATE.md`, the cover letter, the JORS `README.md`, and `paper2/paper2-draft.md`.
- Add a release check that greps the tagged source and extracted PDF text for `rc1`, `not yet public`, `NOT SUBMISSION-READY`, and `local candidate`; fail the release if found.
- Update the release notes with the exact tag, commit, and asset hashes.

#### M2. The DOI placeholder and the “release blocker” paragraph remain (P1)

**Evidence.** Four statements in the submission still read as internal release notes:

- `MS p1` / `paper2-jors.tex:46–47`: “The artifact is public as release candidate `p14-evidence-rc4`; DOI pending explicitly.”
- `MS p6` / `paper2-jors.tex:353–355`: “A DOI is `[DOI to be assigned]`; the GitHub release is a public prerelease, not yet an archival DOI record.”
- `MS p6` / `paper2-jors.tex:381–385`: “The release blocker is specific. Per-record CPU time is missing … the candidate manifest covers the ten-seed … files … The repository and tag are public; a DOI and a tested container digest are still pending. Per-record CPU must be supplied or the CPU claim explicitly scoped before an archival DOI record.”
- `MS p7` / `paper2-jors.tex:430–432`: “release candidate `p14-evidence-rc4`; DOI pending. … The evidence is the public release candidate `p14-evidence-rc4`; a DOI is pending.”

**Why it matters.** The contradiction is gone, and the pending status is honest. But a literal `[DOI to be assigned]` in a submitted manuscript is a desk-return risk, and “The release blocker is specific” tells the editor the artifact is not finished. The sentence “Per-record CPU must be supplied or the CPU claim explicitly scoped” is also internally redundant: `MS p3` already scopes the claim to “where available,” and `MS p6` already discloses the missing fields. The reader cannot tell whether the paper is claiming a scoped result or advertising an incomplete artifact.

**Action.**
- Replace `[DOI to be assigned]` with “A DOI will be assigned on acceptance” in one place, and remove the duplicate “DOI pending” from the Data and code availability section.
- Delete the “release blocker” paragraph from the manuscript. Put the release-engineering status in the cover letter and repository, not in the paper.
- If a DOI cannot be assigned before submission, say once: “The evidence is a public prerelease; an archival DOI will be assigned on acceptance.”
- Replace the prose with a small availability table: software (repository, tag, commit, licence), evidence (release tag, commit, DOI status, licence), container (status), replay command. One status per row.

#### M3. The tabu `bur26` result remains unexplained, and “robust” persists in the headline objects (P1)

**Evidence.** Table 1 reports tabu **0/80** optima on `bur` and BLS **80/80** (`MS p4`; `Table 1`). The supplement’s per-instance table shows tabu **0/10** on all eight `bur26` variants and BLS **10/10** (`paper2-jors-supplement.pdf`, QAP table). The gaps are 0.004–0.565%. The per-run JSON shows the outcomes are **seed-invariant** on several instances: `bur26c`, `bur26e`, `bur26g`, and `bur26h` each have **one distinct gap across all ten seeds**; `bur26a`, `bur26b`, and `bur26f` have two; `bur26d` has three (`paper2/evidence/qap-expanded-100k-10seed.json`).

The text now says “we report this as a property of this untuned reference implementation” and “the tabu path as an unvalidated reference implementation” (`MS p5`; `paper2-jors.tex:266–271`). But the abstract still says “robust tabu search for the quadratic assignment problem” (`MS p1`), Table 1 says “robust tabu versus … BLS” (`MS p4`), §2.4 says “robust tabu search” (`MS p3`; `paper2-jors.tex:187–190`), the Limitations still say “no state-of-the-art claim for robust tabu” (`MS p7`), and the supplement header says “Robust tabu.”

**Why it matters.** A 0/80 result with near-optimal gaps and seed-invariant outcomes is more consistent with a deterministic trap or an implementation defect than with a tuning gap. Calling it “untuned” is an assertion, not a finding; the paper does not report per-seed diversity, a tenure/aspiration diagnosis, or a comparison with published `bur26` results. If the tabu is weak, the BLS comparison says “BLS beats a weak tabu,” not “BLS beats robust tabu.” The paper now says the latter, but the abstract and table still imply the former.

**Action.**
- Rename the method consistently: “tabu search reference (not validated)” in the abstract, Table 1, §2.4, Limitations, and the supplement. Remove “robust” wherever it is used as a quality claim.
- Add one sentence to Limitations: “We did not establish whether the 0/80 `bur26` result is a tuning issue or an implementation defect.”
- Add a per-seed diversity column or a short supplement table (distinct outcomes per instance, or per-seed gaps for `bur26`). This is the evidence that distinguishes a trap from tuning.
- If BLS is the primary QAP quality reference, put BLS first in Table 1 and label the tabu column “reference (unvalidated).”

#### M4. The per-record schema claim is still broader than the artifact (P2)

**Evidence.** `MS p3` / `paper2-jors.tex:153–155` says: “The record names … the pinned solver version or commit, the seed, the iteration or kick budget, the stopping reason, the exact-replay result, and the wall time; CPU time is recorded where available.” The headline QAP/TSP/BLS/generic records do carry these fields (with CPU only in BLS/generic). But the 1,085 broad-screen records use a **different schema**: `stop` instead of `stop_reason`, `wall` instead of `wall_seconds`, `replay_status` instead of `exact_replay`, `known` instead of `known_optimum`, and **50 records lack `solver_commit`/`replay_solver_commit`** (`paper2/evidence/broad-converged.json.gz`). The framework records nest `stop_reason`/`exact_replay` under `framework`.

The manifest’s `replay` entry is also stale: it records SHA-256 `cdc8b45…`, while the actual `paper2/replay_all.sh` is `3fb669…`. The manifest `status` says “candidate; no tag/release created; P12 framework-use and TSP convergence added” (`paper2/evidence/manifest-v0.1.0-candidate.json`).

**Why it matters.** A reproducibility paper’s schema claim should be auditable. The broad screen is secondary, but the paper says “the record” without qualification. The stale manifest entry means the manifest does not fully describe the current artifact, even though the 66 `files` hashes verify.

**Action.**
- Scope the schema claim to the QAP/TSP/BLS/generic panels, and document the broad-screen schema separately (or normalize it to the common field names).
- Add a JSON-schema check to `check_evidence.py` and run it in `replay_all.sh`.
- Refresh the manifest after the final release: update the `replay` hash, the `status`, and the `jors_submission_*` entries. Remove `paper2/paper2-draft.md` from the manifest or update it.

#### M5. The licence/redistribution statement is false (P1)

**Evidence.** `MS p6` / `paper2-jors.tex:356–358` says: “QAPLIB and TSPLIB instances are referenced by name and are not redistributed.” The tagged release contains eight instance files: `paper2/instances/{tai12a,tai20a,tai25a,tai30a}.dat` and `{berlin52,ch150,kroA100,kroB100}.tsp` (`git ls-tree -r p14-evidence-rc4 -- paper2/instances`). `paper2/instances/README.md` says “These are public benchmark instances. Preserve source attribution in any redistribution.” `LICENSING.md` says derived evidence is CC BY 4.0 “except where a source dataset imposes a different term.”

**Why it matters.** The paper’s redistribution claim is factually wrong; a JORS reviewer who checks the artifact will see the files. QAPLIB/TSPLIB may impose different terms, and the repository’s own licence file says so. A false claim about data redistribution is a credibility and compliance issue.

**Action.**
- Either remove the eight instance files from the release (keep them in a separately licensed data package) or correct the statement: “A small smoke-test subset of QAPLIB/TSPLIB instances is included with attribution in `paper2/instances/`; the full libraries are not redistributed.”
- Replace “intended for release under CC BY 4.0” with the actual licence, and update `LICENSING.md` to remove “The repository is not yet public.”

#### M6. Author metadata and journal-required statements are missing (P1)

**Evidence.** The manuscript has a single author and email (`MS p1`), but no ORCID, CRediT, funding, competing interests, or acknowledgements. `paper2/submission/jors/README.md:37–39` says “individual authors, affiliations, ORCIDs, CRediT, funding, and competing-interest statements are not yet supplied.” The supplement uses “UBC FRESH Lab” as the author, while the main text uses “Gregory Paradis” (`paper2-jors-supplement.tex:15`).

**Why it matters.** JORS submission requires these statements; a missing competing-interest or funding statement is a common desk-return. The supplement/main byline inconsistency is a small but visible defect.

**Action.**
- Add ORCID, CRediT, funding, competing interests, and acknowledgements before submission.
- Reconcile the supplement byline with the main manuscript.
- Confirm the corresponding author and affiliation.

#### M7. Provenance is split across two replay commits, and the container pins a third (P2)

**Evidence.** The QAP expanded records carry `replay_solver_commit=4583ad3` (200/200); the BLS/TSP/generic records carry `replay_solver_commit=c7d1507` (200/100/40). The paper cites `v0.9.3-p13rc1`, which is `4583ad3`. I checked the two trees: `git diff --stat 4583ad3 c7d1507 -- fresh_solutions` is **empty**; the `fresh_solutions/` source is identical, and the only differences are `CHANGE_LOG.md`, `ROADMAP.md`, `notes/README.md`, and a notes report. So the split is a **re-stamp/normalization issue**, not a code divergence. This is a weaker problem than the prior review’s M8 suggested, but it is still a provenance inconsistency.

The container `Dockerfile:6–7` checks out `7d3c831` (the campaign commit, before the GEO fix), not `4583ad3` or `c7d1507`. The paper says “the container recipe is not yet pinned to a base-image digest and solver checkout” (`MS p6`; `paper2-jors.tex:365–367`), but the solver checkout **is** pinned — to the wrong commit. `container/README.md` says the solver checkout is missing, which is also stale.

**Why it matters.** A reproducibility paper needs one immutable replay identity per table. A reader cannot tell which commit produced which panel, and the container would replay against the campaign commit rather than the replay commit. The code-identical check reduces the scientific risk but does not remove the bookkeeping defect.

**Action.**
- Normalize all records to one replay commit (preferably the public release tag) and re-stamp the manifest.
- Fix the Dockerfile to check out the replay commit, or remove the container claim and the Dockerfile from the release.
- Correct the sentence about the solver checkout; it is pinned, but to `7d3c831`.
- Add a provenance table mapping each table to evidence file, solver commit, replay commit, and hardware.

#### M8. Statistical presentation still overstates precision in two places (P2)

**Evidence.** `MS p4–5` reports the cluster-by-instance CI **−0.300 to −0.111** (correct; my recomputation is −0.2991 to −0.1108), the family-cluster CI **−0.234 to −0.163**, and the 15/16 sign test **p = 5.2 × 10⁻⁴** (correct; my recomputation is 5.19 × 10⁻⁴). The family-cluster bootstrap resamples **3 families**; a 95% interval from 3 units is not reliable. The sign test treats 20 instances as independent, but the eight `bur26` variants are highly correlated and several have identical outcomes across seeds. The paper says “the effective sample is 20 instances in three families” but still reports the p-value without a sign-test-specific caveat; the preceding sentence caveats the intervals, not the test.

The 1.24 ratio is the **mean of the four per-instance ratios**; the pooled ratio (total framework CPU / total baseline CPU) is **1.215**. The paper does not state which aggregation it uses. The 95% CI 1.17–1.31 matches a cluster bootstrap of the mean of per-instance ratios.

**Why it matters.** The qualitative conclusion (BLS lower) survives, but the family-cluster interval and the sign-test p-value are stronger than the design supports. The 1.24 summary is defensible but should be defined.

**Action.**
- Keep the cluster-by-instance interval as the primary descriptive summary.
- Drop the family-cluster interval or label it an informal sensitivity check with only 3 clusters, not a 95% CI.
- Replace the sign-test p-value with a family-stratified permutation test or a hierarchical model, or report the 15/16 count without a p-value.
- State that the panel is a convenience sample, not a random sample of QAPLIB.
- State that 1.24 is the mean of per-instance ratios; report the pooled ratio (1.215) alongside it or in a footnote.

#### M9. JORS length/focus is close but still over the page guide (P2)

**Evidence.** The PDF is **8 pages** (body through p7, references on p7–8), down from 9. The word count is **3,806**, inside 3,000–4,000. The abstract is **256 words** and still spends two sentences on the tabu/BLS gaps before the TSP result. The guide is roughly **4–6 pages** (`notes/plans/p14-journal-shift-2026-11-11.md:140–142, 232`). The paper still has no dedicated “Lessons” section; the lessons are scattered through Limitations. The conclusion says “The TSP breadth panel reaches 94 of 100 known optima” without “mixed-depth” (`MS p7`).

**Why it matters.** A 8-page submission may be desk-checked as over length even though the word count is inside the limit. The current balance is much better, but a JORS editor may still see a solver comparison rather than an experience report. The conclusion’s omission of mixed depth is a small but real inconsistency with the abstract.

**Action.**
- Cut roughly one page: move Table 2 or the broad-screen details to the supplement; shorten the LKH paragraph; keep one QAP/BLS table.
- Add a short **“Lessons for reproducible benchmarking”** section with 4–5 bullets: the replay gate; budget/patience effects; protocol drift; a weak baseline can be exposed; the adapter contract is not a search engine.
- Add “mixed-depth” to the conclusion sentence.
- Consider shortening the abstract to ~200 words and leading with the adapter/replay contract, not the gap numbers.

### 5.5 Minor comments

- **m1.** The title “an adapter and exact-replay harness” is grammatically awkward. Use “an adapter- and exact-replay harness” or “an adapter and exact replay harness” (`MS p1`).
- **m2.** The abstract is 256 words; confirm the JORS abstract limit. “DOI pending explicitly” is not idiomatic; use “DOI pending” or “DOI will be assigned on acceptance” (`MS p1`).
- **m3.** The section title “QAP convergence panel and independent baseline” is misleading: BLS is a reimplementation by the same author, not an independent implementation. Use “separate” or “reimplemented” (`MS p4`; the text already says “separately implemented”).
- **m4.** Table 1’s “All” row is run-level (200 runs), while the family rows are unweighted means of instance means. State this in the caption. The text’s family-equal 0.298/0.099 is not the table’s 0.301/0.096; explain the difference (`MS p4`; `Table 1`).
- **m5.** If BLS is the primary QAP reference, put BLS first in Table 1 and label the tabu “reference (unvalidated).” The current table still reads as a tabu-first comparison (`MS p4`; `Table 1`).
- **m6.** The supplement’s QAP header says “Robust tabu,” contradicting the main text’s “unvalidated reference.” Align the labels (`paper2-jors-supplement.pdf`, QAP table).
- **m7.** Table 2’s depth-4 group includes `ch150` (n=150), which a reader may expect at depth 2 under an n-based rule; add a footnote that the recorded depth is the legacy value. Explain why `lin105` is depth 3 (`MS p5`; `Table 2`).
- **m8.** The conclusion says “The QAP panel shows that a patience rule changes the reported gaps relative to a short fixed budget.” That comparison is in §2.3, not the QAP panel. Rephrase (`MS p7`).
- **m9.** The LK causal claim “lacks α-nearness, fractional cascading, and the full LKH gain criteria, **which is why** the larger tail is weak” should be “we attribute” or “consistent with” (`MS p7`; `paper2-jors.tex:402–404`).
- **m10.** The Data and code availability section says “The harness … are in the FRESH https://github.com/UBC-FRESH/fresh-solutions-papers” — the harness is in `fresh-solutions`; the papers repository contains the runners, evidence, and manuscripts. Fix the grammar and the link (`MS p7`; `paper2-jors.tex:429–431`).
- **m11.** The Data and code availability section repeats “DOI pending” twice and the URL breaks across lines. State the DOI status once (`MS p7`).
- **m12.** `lkh-provenance.json:20` still contains a machine-specific path `/srv/shared-data/gep/ws4/tmp/LKH3/LKH`. Use a placeholder or repository-relative path.
- **m13.** The PDF metadata is blank (Title, Author, Subject, Keywords) and the page size is US Letter (612 × 792). Set `pdftitle`/`pdfauthor` via `hyperref` and confirm the JORS page size (`pdfinfo paper2-jors.pdf`).
- **m14.** The supplement byline is “UBC FRESH Lab” while the main text is “Gregory Paradis.” Align (`paper2-jors-supplement.tex:15`).
- **m15.** `paper2/submission/jors/README.md:21` says **3,815** words; the actual count is **3,806** (`detex -n paper2-jors.tex | wc -w`). `README.md:17` also claims “no overfull boxes,” but the build has a 31.5 pt overfull hbox at lines 381–386.
- **m16.** `paper2/README.md:3–4` still says “working draft, not a submission-ready article”; line 12 says “23 pages, 8,930 source words”; line 80 says “Independent BLS baseline”; line 81 says BLS is stronger on **14** instance means, while the manuscript says **15**. Update or remove.
- **m17.** `paper2/paper2-draft.md:3` says “INTERNAL DRAFT — NOT SUBMISSION-READY” and line 165 reports the old LKH **71/100** result. It is in the manifest and the public release. Remove it or update it.
- **m18.** `paper2/evidence/RELEASE-CANDIDATE.md:3` says “local candidate only. No tag, release, visibility change, or DOI has been made” and `manifest-v0.1.0-candidate.json` says “no tag/release created.” Both are false in the public rc4 release. Update.
- **m19.** `LICENSING.md:11` says “The repository is not yet public.” It is public. Update.
- **m20.** `paper2-jors.tex:165` says “a tag is not created until the maintainer approves the release.” The tag exists. Remove or rephrase.
- **m21.** `paper2-jors.tex:162` says the repository keeps “instance files or their provenance.” The repository includes the instance files; say so explicitly, with attribution.
- **m22.** `paper2/submission/jors/cover-letter.md:16–19` says “The software and evidence are being prepared as a public tagged release … the repository and DOI fields are placeholders until that release is approved.” The release is already public. Update.
- **m23.** `paper2/submission/jors/highlights.md` says “Software/evidence release and one-command replay are the remaining gate.” The release exists. Update or remove.
- **m24.** The §2.3 QAP budget comparison uses a **five-seed, 10,000-iteration** panel (`qap-tabu-summary.json`) against the **ten-seed, 100,000-patience** panel (`qap-expanded-100k-10seed-summary.json`). The paper does not state that the seeds differ. Say “in an earlier five-seed pilot” or report the same-seed comparison (`MS p3`; `paper2-jors.tex:177–180`).
- **m25.** The paper says BLS used “the same … start” (`MS p4`), but the QAP records do not store the start assignment or initial objective. Add the start rule/objective to the records or soften the claim.
- **m26.** The broad TSP screen’s seeds, kicks, patience, and 600-second cap are not stated in the main text. Add one sentence (`MS p6`).
- **m27.** The paper says “known optimum” for all QAP instances, but `tai30a` is “best known” in the evidence (`qap-tabu-summary.json`). Use “known or best-known value” in the table captions.
- **m28.** “The generic runs … use about 117,000 exact evaluations” is ambiguous: it is the mean per run (116,868), not the total. Say “about 117,000 evaluations per run” (`MS p6`).
- **m29.** The paper asserts the replay gate’s value but reports no final invalid replay. Add a short “what the gate caught (and did not)” paragraph, or state that no invalid replay survived, to make the gate’s role concrete (`MS p3`).
- **m30.** The paper’s related-work section is all metaheuristics/reproducibility; it has no software-engineering thread (API contracts, testing, dependency management). For JORS, one or two sentences on the software-design context would help (`MS p1–2`).

---

## 6. Claim-to-evidence ledger

| Claim | Location | Evidence | Status |
|---|---|---|---|
| Tabu 0.301% mean, 0.043% median, 5.695% worst, 73/200 optima | `MS p1`, `p4`; Table 1 | `qap-expanded-100k-10seed.json` | **Supported** (0.30085, 0.04268, 5.69514, 73). |
| BLS 0.096% mean, 1.369% worst, 161/200 optima | `MS p4`; Table 1 | `qap-bls-10seed.json` | **Supported** (0.09614, 1.36861, 161). |
| Paired difference −0.205; cluster CI −0.300 to −0.111; 15/16; p = 5.2 × 10⁻⁴ | `MS p4–5` | recomputed from per-run JSON | **Supported** (−0.20471; −0.2991 to −0.1108; 15/16; 5.19 × 10⁻⁴), with clustering caveat. |
| Family-cluster CI −0.234 to −0.163 | `MS p5` | recomputed | **Supported arithmetically**, but only 3 clusters; not a reliable 95% CI. |
| TSP 94/100 optima, 95/100 patience, 0.004% mean, 0.185% worst | `MS p1`, `p5`; Table 2 | `tsp-expanded-10k.json` | **Supported**; mixed-depth and cap-limited. |
| Framework 1.24 CPU ratio, CI 1.17–1.31, 40/40 matched and replayed | `MS p1`, `p4`; Fig 2 | `framework-use-summary.json` | **Supported** (1.239; 1.170–1.309; 40/40). Aggregation not stated; pooled ratio 1.215. |
| Broad QAP 134 instances, 552/670 patience, 318 optima, 1.823% converged mean, 36.445% worst | `MS p6` | `broad-converged-summary.json` | **Supported.** |
| Broad TSP 78 instances, 236/390 patience, 195 optima, 1.460% all-run mean; n>300: 3/100, 1 optima, 97 cap | `MS p6` | `broad-converged-summary.json` | **Supported.** |
| LKH 75/100 optima, 0.098% mean, 0% median, 1.930% worst, 15.0 s | `MS p6` | `lkh-large-summary.json` | **Supported.** |
| Generic QAP 3.848% vs 0.097%; TSP 127.978% vs 0.000%; ~117,000 evaluations | `MS p6` | `generic-tabu-summary.json` | **Supported** (3.8478, 0.0966, 127.978, 0.000, 116,868). |
| 1,060 broad incumbents; 25 `esc8` skipped | `MS p6` | `broad-converged.json.gz` (1,085 records; 25 `esc8`) | **Supported.** |
| Every record names solver commit, seed, budget, stop reason, replay, wall time; CPU where available | `MS p3` | QAP/TSP/BLS/generic records; broad records use different fields; 50 lack commits | **Partly supported**; scope the schema. |
| Manifest covers the ten-seed QAP files; 66/66 hashes verify | `MS p6` | `manifest-v0.1.0-candidate.json` | **Supported** for `files`; `replay` hash and `status` are stale. |
| QAPLIB/TSPLIB instances are not redistributed | `MS p6` | 8 instance files in the tagged release | **Not supported.** |
| Artifact is public as `p14-evidence-rc4` | `MS p1`, `p6` | release assets match; tagged source says rc1 in `README.md:3` | **Partly supported**; manuscript/PDF match, package docs contradict. |
| Tabu is “robust” | `MS p1`, `p3`, `p4`, `p7`; supplement | 0/80 on `bur26`; seed-invariant outcomes | **Not supported** as a validated robust-tabu claim; demoted in prose only. |
| TSP depth disclosed | `MS p1`, `p5` | 17/1/2 instances at depth 4/3/2; `max_depth` in records | **Supported**, but conclusion omits it. |
| DOI is pending, not assigned | `MS p1`, `p6`, `p7` | literal `[DOI to be assigned]` | **Honest but not submission-ready.** |

---

## 7. Reviewer questions (Yes / No / N/A)

1. Does the manuscript fit JORS Issues in Research Software? **Yes, in principle** — it is an experience/reproducibility report on an evidence boundary. The balance is better, but still slightly solver-comparison heavy.
2. Is the software contribution clearly described? **Mostly** — adapter contract, resident state, replay gate, stopping taxonomy. There is no short API/usage example or test evidence.
3. Is the artifact public and independently replayable? **Partly** — the manuscript/PDF/supplement match the release and the evidence is public; the package docs contradict the status, the DOI is a placeholder, and the one-command recipe omits clone/install/submodule steps.
4. Are the headline numbers traceable to the evidence? **Yes** — QAP/BLS/TSP/framework/broad/LKH/generic numbers match. The schema claim is broader than the broad-screen records.
5. Is the BLS inference appropriately clustered? **Partly** — cluster-by-instance interval is correct; family-cluster bootstrap (3 families) and sign test over correlated instances overstate precision.
6. Is the tabu baseline credible? **No, as a validated robust tabu** — 0/80 on `bur26` with seed-invariant, near-optimal outcomes suggests a trap or implementation defect; the paper demotes it in prose but not in the headline labels.
7. Is the TSP protocol consistent? **No** — mixed-depth by design, now disclosed; the 94/100 is descriptive, not controlled.
8. Is the manuscript within the length guidance? **Word count yes; page count no** — 3,806 words, 8 pages, body ≈6.5 pages vs the rough 4–6 page guide.
9. Would I review a revision? **Yes.**

---

## 8. Risk table

| # | Risk | Likelihood | Impact | Evidence | Mitigation |
|---|---|---|---|---|---|
| R1 | Release package contradicts its own public rc4 status (tagged README says rc1; licence says not public; draft says not submission-ready) | High | High | `p14-evidence-rc4:README.md:3`; `LICENSING.md:11`; `RELEASE-CANDIDATE.md:3`; `paper2/paper2-draft.md:3` | Re-cut the release after updating/deleting stale docs; add a release grep check. |
| R2 | DOI placeholder and “release blocker” paragraph remain | High | High | `MS p1`, `p6`, `p7`; `paper2-jors.tex:46, 354, 381–385, 431–432` | One availability table; “DOI assigned on acceptance”; move release notes to cover letter. |
| R3 | Tabu `bur26` 0/80 is an implementation artifact; “robust” label persists | High | High | Table 1; supplement; `qap-expanded-100k-10seed.json` (seed-invariant gaps) | Rename; add limitations sentence and per-seed diversity table; diagnose or fully demote. |
| R4 | Licence/redistribution claim is false; 8 instance files in the release | High | Medium | `MS p6`; `git ls-tree p14-evidence-rc4 -- paper2/instances`; `paper2/instances/README.md`; `LICENSING.md` | Correct the statement or remove the files; state actual licence. |
| R5 | Missing author metadata and journal statements | High | Medium | `MS p1`; `paper2/submission/jors/README.md:37–39` | Add ORCID, CRediT, funding, competing interests, acknowledgements. |
| R6 | Schema/manifest/provenance inconsistencies | Medium | Medium | Broad records; manifest `replay` hash; `4583ad3`/`c7d1507`; `Dockerfile:6–7` | Scope schema; refresh manifest; normalize replay commit; fix container. |
| R7 | Family-cluster CI and sign test overstate precision | Medium | Medium | `MS p4–5`; 3 families; correlated `bur26` | Label informal; drop or stratify p-value. |
| R8 | JORS page guide (8 pages vs 4–6) and solver-paper balance | Medium | Medium | `MS p1–7`; `notes/plans/...:232`; 3,806 words | Cut ~1 page; add lessons section; add mixed-depth to conclusion. |
| R9 | One-command replay not complete from a clean clone | Medium | Medium | `MS p6` snippet; `replay_all.sh` submodule import | Add clone/install/submodule/layout steps; test a clean clone. |
| R10 | Format/metadata defects | Low | Low | blank PDF metadata; US Letter; supplement byline; overfull hbox; README 3,815 vs 3,806 | Set metadata; align byline; fix overfull; update counts. |

**Top five residual risks (executive):**

1. **Release package contradicts its own status** (R1): the tagged source says rc1/not public/local candidate/not submission-ready. Mitigation: re-cut after cleaning the docs and add a release check.
2. **DOI placeholder and “release blocker” paragraph** (R2): the manuscript advertises an incomplete artifact. Mitigation: one availability table; “DOI assigned on acceptance”; remove process notes.
3. **Tabu `bur26` credibility** (R3): 0/80 with seed-invariant near-optimal gaps; “robust” label persists. Mitigation: rename, add a per-seed diversity table and a limitations sentence, or diagnose.
4. **False redistribution claim and missing author metadata** (R4/R5): factual/compliance errors and desk-return risk. Mitigation: correct the statement or remove the files; add ORCID/CRediT/funding/competing interests.
5. **Schema/provenance/statistics residuals** (R6/R7): broad-screen schema differs; manifest replay hash stale; replay commits split; family CI/sign test overstate precision. Mitigation: scope, refresh, normalize, caveat.

---

## 9. P0 / P1 / P2 list

### Earlier P0 status

- **P0-1 (release asset/tag mismatch): CLOSED** for the manuscript, PDF, and supplement. The release assets match the submitted files exactly, and the tagged `.tex` is identical.
- **P0-2 (availability/DOI): PARTLY CLOSED.** The contradictions are removed; the DOI status is honest. Residual: literal `[DOI to be assigned]` and the “release blocker” paragraph.
- **P0-3 (per-record CPU/schema): PARTLY CLOSED.** CPU is scoped and the missing fields are disclosed; the manifest covers the ten-seed files. Residual: the broad-screen schema differs, and the manifest’s `replay` hash/status are stale.
- **P0-4 (tabu `bur26`/BLS primary): PARTLY CLOSED.** BLS is primary in prose and the tabu is called unvalidated; “robust” persists in the abstract/table/supplement, and no diagnostic is added.
- **P0-5 (length/focus/mixed-depth TSP): LARGELY CLOSED.** Mixed depth is disclosed in the abstract and §3.3; length is down to 8 pages. Residual: still above the 4–6 page guide; conclusion omits mixed depth; no lessons section.

### P1 — major, affects submission readiness/credibility

- **P1-1. Release package metadata.** Tagged source says rc1/not public/local candidate/not submission-ready; re-cut and clean (`README.md:3`; `LICENSING.md:11`; `RELEASE-CANDIDATE.md:3`; `paper2/paper2-draft.md:3`; cover letter; JORS `README.md`).
- **P1-2. DOI/blocker.** Replace the placeholder and remove the “release blocker” paragraph (`MS p1`, `p6`, `p7`).
- **P1-3. Tabu label/diagnostic.** Rename “robust” consistently; add a limitations sentence and per-seed diversity table, or diagnose (`MS p1`, `p3`, `p4`, `p5`, `p7`; supplement).
- **P1-4. Redistribution/licence.** Correct “not redistributed”; update `LICENSING.md` (`MS p6`; 8 instance files in the tag).
- **P1-5. Author metadata.** Add ORCID, CRediT, funding, competing interests, acknowledgements; align supplement byline (`MS p1`; supplement).

### P2 — minor/clarity

- **P2-1.** Scope the per-record schema; document the broad-screen schema; refresh the manifest `replay` hash/status (`MS p3`; manifest).
- **P2-2.** Normalize `4583ad3`/`c7d1507` record stamps; fix or remove the container (`Dockerfile:6–7`; `MS p6`).
- **P2-3.** Label the family-cluster interval informal; drop/stratify the sign-test p-value; state the 1.24 aggregation (`MS p4–5`).
- **P2-4.** Cut ~1 page; add a “Lessons” section; add “mixed-depth” to the conclusion (`MS p1–7`).
- **P2-5.** Table 1 caption: family means unweighted; “All” row run-level; BLS first if primary (`Table 1`).
- **P2-6.** Table 2: depth-4 `ch150` footnote; explain `lin105` depth 3 (`Table 2`).
- **P2-7.** Section title “independent baseline” → “separate/reimplemented baseline” (`MS p4`).
- **P2-8.** Data availability: wrong repo for the harness; duplicate DOI; URL break (`MS p7`).
- **P2-9.** LK causal overclaim (“which is why”) → “we attribute” (`MS p7`).
- **P2-10.** `lkh-provenance.json` machine-specific path; PDF metadata/page size; overfull hbox; word-count discrepancies.
- **P2-11.** Stale `paper2/README.md`, `paper2/paper2-draft.md`, `highlights.md`, `LICENSING.md`, `RELEASE-CANDIDATE.md`, `paper2/submission/jors/README.md`.
- **P2-12.** 10k vs 100k comparison mixes 5-seed and 10-seed panels; state or match (`MS p3`).
- **P2-13.** “Same start” for BLS not recorded in QAP records; add the start rule/objective or soften (`MS p4`).
- **P2-14.** Broad TSP screen parameters (seeds/kicks/patience/cap) missing (`MS p6`).
- **P2-15.** “Known optimum” vs “best known” for `tai30a`; use “known or best-known value” (`Table 1`; supplement).
- **P2-16.** “About 117,000 exact evaluations” per run, not total (`MS p6`).
- **P2-17.** No replay-gate failure example; add a short “what the gate caught (and did not)” paragraph (`MS p3`).
- **P2-18.** Related work lacks a software-engineering thread; add one or two sentences (`MS p1–2`).

---

## 10. Overall assessment

The paper is a genuine JORS-style experience report with a real software contribution and an unusually honest evidence culture. The adapter contract, replay gate, and stopping taxonomy are the right things to publish, and the negative results are appropriate for the venue if framed as lessons rather than rankings. The headline numbers reproduce; the BLS inference is clustered; the TSP depth drift is disclosed; and the release now contains the rc4 manuscript.

The submission is close but not yet submission-ready. The release package still contradicts its own public status, the manuscript still contains a DOI placeholder and a “release blocker” paragraph, the tabu is still called “robust” in the headline objects while the text calls it unvalidated, the redistribution statement is false, and the author metadata is missing. These are bounded fixes; none requires a new campaign. The tabu can be handled by a consistent demotion plus a per-seed diversity table, or by a short diagnostic if the authors want to keep the “robust” label.

I recommend **minor revision**. After the P1 fixes and a re-cut release, this would be a credible JORS paper. If the editor regards the DOI/package-status issues as P0, the same comments support a major-revision decision, but the scientific core does not need to be redone.

---

## 11. QA checklist (before submission)

- **Evidence-only:** every substantive claim has a citation tag. Yes.
- **Anonymity/privacy:** no reviewer-identifying details; no third-party personal information beyond the materials. Yes.
- **Tone:** professional, constructive, inclusive. Yes.
- **Bias hygiene:** critiques anchored to the submission’s content and evidence, not prestige or subfield preference. Yes.
- **Actionability:** each major comment names a file/page, why it matters, and a bounded action. Yes.
- **Venue fit:** the review assesses JORS Issues in Research Software, not JoH or SoftwareX criteria. Yes.
