# Manuscript plan for Papers 1 and 2

Status: active
Date: 2026-11-03

## Starting point

The current drafts are technical reports, not journal manuscripts:

- Paper 1: ~1,705 words.
- Paper 2: ~1,346 words.
- Neither has a complete reference list.
- Both are marked internal / not submission-ready.

Evidence and reproducibility are much further along than the prose. The plan below separates
evidence closure from manuscript construction and sets a defensible submission gate for each paper.

## Paper 1 — compiled-state landscape architecture

### Target

**Primary:** Environmental Modelling & Software.
**Fallback:** Canadian Journal of Forest Research or Forest Science (forest-planning framing).

Rationale: the defensible contribution is the compiled-state architecture, the public TSA24 artifact,
exact replay, and the GPU scaling record. This is a model/software contribution, not a claim of
state-of-the-art landscape optimisation against an independent model.

### Thesis

> A compiled-state, exact-replay architecture makes a 208k-block landscape search tractable and
> auditable, and a public frozen artifact makes the result independently replayable.

### Claims allowed

- Exact compiled-state accounting and replay on the TSA24 artifact.
- 100k-generation GPU-GA, five seeds, 512.574–518.621 objective range.
- Maximum even-flow interpretation with the deliberate 70M level aspiration and 51.3–52.4M realized
  level.
- Same-engine 1k/10k/100k scaling.
- Weak, untuned CPU-SA comparator; not a controlled performance proof.
- Architecture ablation, if the evidence is produced.

### Claims forbidden

- “Near-zero” objective.
- “Orders of magnitude” from the CPU-SA comparison.
- Competitive or state-of-the-art landscape claim.
- Independent model comparison (none exists).
- Partner-endorsed operational impact.

### Evidence gate before full drafting

Already available:

- public `ws4-tsa24-evenflow-v1` artifact, MIT/CC BY/OGL-BC terms, GPU rebuild recipe;
- 1k/10k/100k records, five seeds, exact replay;
- per-target flow/level residuals and realized level range;
- replay gate and schema/hash validation;
- CPU-SA 100k/30min baseline.

Still needed:

1. **Architecture ablation.**
   - direct evaluator vs compiled/effect-table evaluator at identical moves/seeds/evaluation counts;
   - cache load vs search time;
   - GPU batched population vs CPU batched population at identical population/generation.
2. **Matched CPU-GA baseline.**
   - same population, generations, seed, and evaluation count as GPU-GA, or a clearly stated
     equal-wall-time variant;
   - report objective and wall time.
3. **Target-feasibility note.**
   - document the maximum-even-flow construction and the deliberate 70M aspiration;
   - report why an exact MIP proof is impractical at this scale.
4. **Final artifact audit.**
   - confirm the release asset, license links, rebuild recipe, and SHA-256.

If (1) and (2) cannot be produced, the paper is still an architecture/reproducibility case study,
but the abstract and results must be narrowed accordingly.

### Outline and word budget

Target: **8,000–9,500 words** main text, 40–60 references.

| Section | Words | Content |
| --- | ---: | --- |
| Abstract | 250 | Problem, architecture, TSA24 scale, 100k result, artifact, limits |
| 1 Introduction | 900 | Forest-planning model complexity; reproducibility/engineering problem; contributions |
| 2 Related work | 1,200 | Spatial harvest scheduling, metaheuristics, GPU/parallel search, reproducibility |
| 3 Problem and model | 1,000 | TSA24 instance, target semantics, maximum-even-flow construction, objective |
| 4 Architecture | 1,800 | Compiled model, candidate/effect indexes, resident state, GPU/CPU handoff |
| 5 Experimental design | 1,000 | Hardware, seeds, budgets, replay, metrics, baselines |
| 6 Results | 1,800 | Scaling, seed distribution, residuals, ablation, CPU comparisons |
| 7 Discussion | 1,000 | What the architecture buys, what it does not, operational interpretation |
| 8 Limitations and conclusion | 600 | Public artifact, no independent model, exact-MIP limits, next work |

### Figures and tables

- Figure 1: architecture layers and data flow.
- Figure 2: effect-table/candidate-index structure.
- Figure 3: 1k/10k/100k scaling curve with seed range.
- Figure 4: realized harvest profile and target band/aspiration.
- Figure 5: architecture ablation (direct vs compiled; CPU vs GPU batch).
- Table 1: TSA24 instance and target definition.
- Table 2: run configurations and hardware.
- Table 3: 100k seed distribution.
- Table 4: residual decomposition.
- Table 5: CPU-SA/CPU-GA comparison with explicit budget caveats.

### Reviewer risks

1. “The 517.86 is a level-aspiration compromise, not a near-zero solution.” Address with the
   maximum-even-flow section and residual table.
2. “The CPU-SA is a straw man.” Label it weak/untuned; do not use it for a performance claim.
3. “208,255 blocks vs 458,708 compiled blocks.” Say “operable/candidate blocks” every time.
4. “No independent model.” Keep the architecture/reproducibility scope; do not claim competitive
   landscape performance.
5. “No architecture ablation.” Produce (1) above before submission.

### Submission gate

- Full draft ≥8,000 words.
- Complete references in journal style.
- Architecture ablation and matched CPU-GA run complete or scope narrowed.
- All claims mapped to records.
- Public artifact, license, and rebuild recipe verified.
- Maintainer approval before submission.

## Paper 2 — reproducible metaheuristic benchmark harness

### Target

**Primary:** Journal of Heuristics.
**Fallback:** ACM Journal of Experimental Algorithmics for the experimental/reproducibility framing;
SoftwareX or Journal of Open Research Software if the paper is intentionally a tool paper.

Rationale: the current evidence supports a harness + reference-adapters contribution. Journal of
Heuristics requires a framework-use experiment or a strong benchmark-methodology contribution. If
neither is produced, submit to a software/tool venue, not a heuristics journal.

### Thesis

> A stable adapter/replay contract plus committed reference implementations makes applied
> metaheuristic comparisons reproducible, and the harness can expose both strong results and
> large-instance failures without hiding them.

### Claims allowed

- Adapter/replay contract, exact replay, checkpointing, convergence records.
- QAP robust tabu and TSP ILK reference implementations.
- Broad QAP/TSP panel with honest tails.
- External LKH as an optional capability reference.
- Mixed SciPy baseline; no universal dominance.

### Claims forbidden

- General-framework experiment without a generic-engine result.
- Graph-colouring public adapter (toy only).
- “Portfolio improvement” unless mean statistics improve.
- Best-of-five vs mean comparisons.
- State-of-the-art QAP/TSP.
- LKH as part of the Apache-licensed package.

### Evidence gate before full drafting

Already available:

- QAP certified, broad, large multi-start, SciPy baseline;
- TSP ILK four-instance result, kicks ablation, broad panel;
- committed broad runner with provenance and parse-error separation;
- LKH provenance and external boundary;
- public TSA24 applied case and license.

Still needed:

1. **Framework-use experiment.**
   - Implement one headline path through the generic adapter/engine contract, e.g. QAP tabu or TSP LK
     with engine-managed state/apply/undo.
   - Measure overhead and exact replay against the standalone path.
   - If this cannot be done credibly, choose the SoftwareX/JORS framing.
2. **Statistical comparison.**
   - mean/median/worst with consistent statistics;
   - report all pairwise comparisons, not only wins;
   - state budgets and cap hits.
3. **Evidence release candidate.**
   - freeze the current evidence set and tag only after approval.

### Outline and word budget

Target: **8,000–9,500 words** main text, 40–60 references.

| Section | Words | Content |
| --- | ---: | --- |
| Abstract | 250 | Harness problem, contract, reference adapters, mixed evidence, limits |
| 1 Introduction | 900 | Reproducibility/engineering problem in applied metaheuristics |
| 2 Related work | 1,200 | QAP/TSP heuristics, benchmarking, reproducibility, software frameworks |
| 3 Framework | 1,800 | Adapter contract, exact state, replay, checkpoints, population/hybrid layers |
| 4 Reference implementations | 1,200 | QAP tabu, TSP ILK, LKH boundary |
| 5 Experimental design | 1,000 | Instances, seeds, budgets, convergence, exact replay, statistics |
| 6 Results | 1,800 | QAP/TSP main results, broad panel, tails, ablation, framework overhead |
| 7 Discussion | 900 | What the harness buys; framework-use evidence; limits |
| 8 Limitations and conclusion | 500 | Large TSP, independent baselines, external LKH, evidence release |

### Figures and tables

- Figure 1: adapter/evidence architecture.
- Figure 2: benchmark workflow and replay gate.
- Figure 3: QAP gap distribution by size band.
- Figure 4: TSP ILK vs LKH gap/time boundary.
- Figure 5: framework overhead (if experiment completed).
- Table 1: instance panels and exclusions.
- Table 2: QAP certified results.
- Table 3: QAP broad/large/SciPy results with consistent statistics.
- Table 4: TSP ILK/ablation/broad panel.
- Table 5: LKH boundary and provenance.
- Table 6: replay/provenance metadata.

### Reviewer risks

1. “Your framework thesis is untested.” Produce the framework-use experiment or reframe as a tool
   paper.
2. “Your broad panel is not reproducible.” The runner and provenance are now committed; include
   them and the parse-error accounting.
3. “Your baselines are weak.” Report SciPy honestly as a weak mixed baseline; add a stronger QAP
   baseline if possible.
4. “Your TSP abstract overclaims.” Keep the ILK result at four instances; label the broad panel
   separately.
5. “LKH is doing the work on large TSP.” Keep LKH external and clearly outside the Fresh Solutions
   claim.

### Submission gate

- Full draft ≥8,000 words.
- Complete references in journal style.
- Framework-use experiment completed, or the paper explicitly reframed as a tool paper.
- All comparisons statistically consistent and budget-matched or clearly labelled.
- Evidence manifest and release candidate frozen.
- Maintainer approval before submission.

## Cross-cutting work packages

1. **Freeze claims.** Both drafts keep “internal, not submission-ready” until gates pass.
2. **Close evidence gaps.** Paper 1 architecture ablation + matched CPU-GA; Paper 2 framework-use
   experiment.
3. **Build the bibliography.** Replace “References to verify” with a complete, formatted list.
4. **Build figures/tables from records.** No hand-copied numbers.
5. **Write sections in order.** Problem/related work → methods → experiments → results → discussion.
6. **Internal review.** Check every claim against a record and every number against a script.
7. **Journal formatting and submission package.** Only after the draft gate; approval required.

## Stop conditions

- No new heuristic experiments beyond the evidence gaps above.
- No state-of-the-art or universal claims.
- No submission while an independent baseline or framework-use claim is missing.
- No tag/release/submission without explicit maintainer approval.
