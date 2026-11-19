# P14: Journal-target shift and submission hardening

Date: 2026-11-11
Status: approved 2026-11-11; P0 corrections and target drafts built; release/author metadata outstanding
Targets:
- Paper 1: **SoftwareX** (primary), **JORS** fallback
- Paper 2: **JORS Issues in Research Software** (primary), **SoftwareX** fallback
- JORS Software Metapaper format: not suitable for the evidence paper
- JOSS: excluded
- EMS / JoH: not targets for current drafts

## Decision summary

Both adversarial reviews recommend reject at the current targets. The work is publishable, but as
software/reproducibility contributions:

- Paper 1 is a single-instance compiled-state architecture/software case. SoftwareX fits if the
  paper is shortened and framed as software.
- Paper 2 is a reusable adapter/replay harness with benchmark evidence. JORS *Issues in Research
  Software* fits as an experience/reproducibility report, but the current 8,900-word draft must be cut
  to the journal's 3,000--4,000-word limit. JORS Software Metapaper is a shorter 3-section software
  description and is not suitable for the BLS/TSP evidence.
- EMS/JoH would require a new environmental-validation or methodological study, not a rewrite of the
  current drafts.

## Non-negotiable gates

1. **Public artifact + immutable tag/DOI** for the software and evidence used by each paper.
2. **One-command replay** from a clean clone, with QAPLIB/TSPLIB provenance and a working container.
3. **P0 correctness fixes** below; no P0 may remain open.
4. **PI approval** of target, authors, affiliations, corresponding author, CRediT, funding,
   competing interests, APC, visibility, tag, release, DOI, and submission.

## Phase P14.0 — Freeze decisions and release path

- [ ] Approve target shift: Paper 1 SoftwareX; Paper 2 JORS.
- [ ] Approve public visibility/DOI for the papers evidence repository.
- [ ] Decide the software release identities:
  - WS4: public tag and license; current GPU commit is a feature-branch commit.
  - FRESH Solutions: public release tag; current evidence uses multiple commits.
  - TSA24 artifact: already public; confirm derived-artifact licence and hash.
- [ ] Confirm APC/institutional coverage for SoftwareX and JORS.
- [ ] Freeze author metadata and corresponding author.

Gate: one named approval list; no partial release.

## Phase P14.1 — Paper 1 correctness and evidence hygiene

- [ ] **Level term.** Replace the “every period carries a linear target” description with the exact
  equation `level = 20 × 100 × (70,000,000 − realized_mean)/70,000,000`, define all symbols and
  units, and remove per-period-gradient language that the equation does not support.
- [ ] **Table 3.** Either remove seed 7 or label it as a reference run; report five-seed statistics
  separately. Current six-row mean/median are 516.045/516.234, not 515.682/515.938.
- [ ] **Cold evaluation value.** Correct 54.9 to 54.8 s (`full_baseline_s = 54.8466`).
- [ ] **Manifest.** Regenerate `paper/release/manifest-v0.2.0-candidate.json`; the factorized
  ablation hash is stale. Add a real hash check to the audit.
- [ ] **Timing.** Rerun the 1/10/100-generation CPU/CUDA cells sequentially in one harness, or remove
  the 22.2× claim and Table 5. Current cells were launched concurrently and are contaminated.
- [ ] **Architecture claim.** Either add a controlled architecture-on/off ablation (sparse vs dense
  table, resident state vs full re-evaluation, cached vs rebuilt table) or label 248×/22.2×/2.00e3 as
  implementation microbenchmarks, not architecture evidence.
- [ ] **Baseline language.** Replace “204,413 operable blocks” with “scheduled/non-empty blocks”;
  report CPU-SA flow/level and stop implying a different decision set without evidence.
- [ ] **Abstract/title.** Reframe for SoftwareX: software architecture and exact replay; remove
  GPU-performance lead; do not imply an environmental-science contribution.
- [ ] **Figures.** Keep architecture, scaling, and one valid ablation; no invalid timing figure.

Gate: P0 Paper 1 closed; a clean Paper 1 rebuild has no stale claim.

## Phase P14.2 — Paper 2 correctness and evidence hygiene

- [ ] **Replay bug.** `paper2/replay_all.sh` sets `QAP_BLS_EVIDENCE`, but `paper2/replay_qap_bls.py`
  ignores it and defaults to the 5-seed file. Wire `--input qap-bls-10seed.json` explicitly; add a
  CI assertion for 200/200.
- [ ] **QAP expanded schema.** Stamp the 200 records with solver commit, replay commit, hardware,
  budget, and CPU (or explicit null); add a schema test; correct the manuscript’s schema claim.
- [ ] **TSP adaptive depth.** Rerun the 20-instance panel under one pre-registered depth rule, or
  disclose the mixed legacy/adaptive depths and stop calling it a single protocol. Profile
  `brazil58`; explain the 3,600 s cap.
- [ ] **BLS inference.** Replace the pair-level bootstrap/sign test with cluster-by-instance (and
  family) intervals and an instance-level test; state the effective sample size.
- [ ] **Tabu credibility.** Diagnose or verify the tabu on `bur26`; report per-seed diversity; stop
  calling it a standard baseline unless verified against a published robust-tabu implementation.
- [ ] **Abstract/scope.** Distinguish four-instance deep panel from 20-instance expanded panel;
  include the five `brazil58` cap hits.
- [ ] **LKH.** Report LKH budget/config and the matching FRESH large-tail baseline; update stale
  71/100/0.092% documentation.
- [ ] **Applied case.** Remove the TSA24 applied case from Paper 2 or explicitly state it is not a
  FRESH Solutions adapter. It belongs in Paper 1/supplement.
- [ ] **Manifest/docs.** Regenerate manifest; remove `paper2-draft.md` or update it; resolve the
  `7d3c831`/`c7d1507`/`4583ad3` provenance conflict to one immutable replay/tag.
- [ ] **Metadata.** Fix JoH placeholder metadata is obsolete once JORS conversion begins; remove
  duplicate keywords and placeholder author/email.

Gate: P0 Paper 2 closed; one-command replay covers every table at the paper’s stated seed count.

## Phase P14.3 — Reruns and statistics

- [ ] Paper 1: sequential matched timing; or omit the timing comparison.
- [ ] Paper 1: optional architecture-on/off ablation; if not done, remove causal architecture claims.
- [ ] Paper 2: TSP panel rerun under one depth rule; record per-instance max_depth and wall time.
- [ ] Paper 2: BLS cluster-robust CI and instance-level test.
- [ ] Paper 2: tabu `bur26` diagnosis/verification and seed-diversity table.
- [ ] Paper 2: optional matched-start/matched-evaluation generic-tabu control; otherwise soften the
  negative-result claim to “this configuration is not competitive.”

Gate: every rerun has a solver commit, seed, budget, stop reason, exact replay, and hash.

## Phase P14.4 — Paper 1 SoftwareX conversion

Target structure:

1. Title, abstract, keywords.
2. Software metadata table: current code version, permanent link, licence, dependencies, repository,
   documentation, test command.
3. Motivation and significance.
4. Software description: compiled state, sparse effect/candidate indexes, resident accounting, GPU
   population search, exact CPU replay.
5. Validation/illustration: TSA24 case, scaling, one valid ablation, exact replay.
6. Reuse/limitations.
7. Conclusions, data/code availability, references.

Cut list:
- target-variant screen to supplement/repository;
- CPU-SA comparator prose;
- long failed-baseline discussion;
- detailed negative-result narrative;
- any invalid timing table/claim;
- environmental-validation claims that are not in the paper.

Target length: SoftwareX software-paper length (confirm current limit); the current 21-page draft is
too long. Move detail to the evidence repository and supplement.

Gate: SoftwareX metadata table complete; public code/data links resolve; no P0; target-specific cover
letter and highlights.

## Phase P14.5 — Paper 2 JORS Issues in Research Software conversion

JORS format facts (verified 2026-11-11): Software Metapapers are concise descriptions; Issues in
Research Software articles are experience/reproducibility papers limited to 3,000--4,000 words
(roughly 4--6 pages), Vancouver numbered references, no required LaTeX template; APC applies. Confirm
current APC/waiver before submission.

Target structure:

1. Title, abstract, keywords.
2. Introduction: reproducibility and benchmarking problem.
3. Software description: adapter contract, resident state, exact replay, stopping/budget protocol.
4. Reference implementations: QAP tabu, TSP ILK.
5. Validation: QAP 10-seed panel/BLS, TSP expanded panel, broad/LKH, generic negative result,
   framework overhead.
6. Reuse/limitations: no state-of-the-art claim, no third-party portability, software boundaries.
7. Availability: repository, tag/DOI, container, replay command.
8. Conclusions, references.

Length: move the detailed QAP/TSP/broad tables and long negative-result analysis to supplementary
material; keep one summary table for QAP/BLS and one for TSP, plus the replay/availability details.
The current 8,900-word draft must roughly halve.

Cut list:
- applied TSA24 case (move to Paper 1);
- repeated caveats and “laboratory notebook” passages;
- long internal-review-style discussion;
- SciPy baseline can remain as a short weak external check, not a headline.
- JoH `sn-jnl` variant is obsolete. JORS has no required LaTeX template; use a clean `article`
  build with Vancouver numbered references and follow the Issues in Research Software word limit.

Gate: JORS software-paper structure; public FRESH Solutions tag; one-command replay 200/200 BLS,
200/200 QAP expanded, 100/100 TSP expanded, 1,060 broad, 40 generic, 40 framework + 20 deep TSP.

## Phase P14.6 — Public release and clean-clone verification

- [ ] One public evidence repository or two paper-specific releases.
- [ ] Tag/DOI; immutable solver commit; container digest.
- [ ] Clean clone + `bash replay_all.sh` for Paper 2; Paper 1 replay path tested.
- [ ] `paper/` and `paper2/` manifests agree with files.
- [ ] Data/code availability statements contain public URLs/DOIs, not relative paths.
- [ ] Container tested; no “untested” claim remains.

Gate: a clean clone on a machine with QAPLIB/TSPLIB mounts reproduces every table.

## Phase P14.7 — Independent re-review

- [ ] New independent reviewer for Paper 1 (SoftwareX criteria) using the personal review template.
- [ ] New independent reviewer for Paper 2 (JORS criteria) using the same template.
- [ ] Acceptance threshold: no P0; no unsupported claim; all headline tables replay; public links
  resolve; reviewer recommendation at least minor revision for the target venue.
- [ ] If either reviewer recommends reject, fix or re-target; do not submit.

## Phase P14.8 — Submission package

- [ ] Target templates: SoftwareX `elsarticle`; current JORS/Ubiquity template.
- [ ] Author metadata, corresponding author, CRediT, funding, competing interests.
- [ ] Cover letter, highlights, keywords, editor checklist.
- [ ] Final PDFs and clean builds.
- [ ] Submission only after explicit PI approval.

## Stop-ship list

- Private evidence repository or missing DOI.
- P0 correctness issue open.
- Invalid 22.2× timing claim.
- TSP depth protocol still mixed without disclosure.
- BLS one-command replay still 100/100.
- QAP expanded schema still missing fields.
- Any “reproducible” claim not backed by a public one-command replay.
- Placeholder authors/emails.
- No target-venue fit statement.

## Decisions needed from PI

1. Approve Paper 1 → SoftwareX and Paper 2 → JORS.
2. Approve public release/DOI/container.
3. Confirm APC/institutional coverage.
4. Provide author/affiliation/corresponding/CRediT/funding metadata.
5. Decide: rerun the invalid Paper 1 timing and TSP depth panel, or remove those claims.
6. Decide: remove the TSA24 applied case from Paper 2 and keep it in Paper 1.


## Execution checkpoint — 2026-11-11

Completed:
- Paper 1 P0: level-term equation, Table 3 seed-7 labeling, 54.8 s, manifest hash, invalid 22.2× timing removed.
- Paper 2 P0: BLS replay 200/200, QAP expanded metadata stamped, TSP mixed depth disclosed with per-instance depth, cluster-robust BLS statistics, applied TSA24 case removed.
- Target drafts: `paper/submission/softwarex/paper1-softwarex.tex` (3,874 counted words, 8 pages, 2 figures); `paper2/submission/jors/paper2-jors.tex` (3,798 words, 8 pages, 2 figures + supplement).
- Both target drafts compile; Paper 1 replay passes with `WS4_ROOT`, `TSA24_ROOT`, `FHOPS_ROOT`; Paper 2 replay passes 200/200 BLS and all other panels.

Still blocking:
- Public release/DOI/container and immutable WS4/FRESH Solutions tags.
- PI author/affiliation/CRediT/funding/competing-interest metadata and APC decision.
- Official SoftwareX `cas-sc` template application (current draft is a two-column `elsarticle` review build).
- JORS page estimate (8 pages vs rough 4–6) and final target formatting.
- Tabu `bur26` verification, TSP depth rerun-vs-disclosure decision, and per-record CPU scope.
- New independent reviews of the target drafts.


## Release checkpoint — 2026-11-11

- Public repository: https://github.com/UBC-FRESH/fresh-solutions-papers (public).
- Evidence prerelease: `p14-evidence-rc4`.
- WS4 prerelease: `ws4-v0.2.0-p14rc1` at `f60ce64`.
- FRESH Solutions prerelease: `v0.9.3-p13rc1` at `4583ad3`.
- Sole author metadata: Gregory Paradis, UBC FRESH Lab, University of British Columbia.
- DOI/Zenodo, container digest, official SoftwareX template, final independent review, and final PI approval remain.
