# P13.5: Paper 1 architecture ablation

Parent: #81

## Why

The architecture claim is not separated from the GPU/implementation effect.

## Work

- [ ] Implement a CPU batched evaluator over the same sparse effect table.
- [ ] Run GPU vs CPU at the same population and generation count.
- [ ] Measure cache-load vs search.
- [ ] Measure effect table vs direct evaluator on a full or clearly bounded instance.
- [ ] Add a tuned CPU-GA/SA at equal work and equal wall time.
- [ ] If the effect is absent, retitle/reframe Paper 1 and remove the causal claim.

## Acceptance

- Controlled ablation table with exact replay.
- The paper either supports the architecture claim or explicitly becomes a reproducibility/software
  paper.
- No “GPU is faster” claim from an untuned comparator.
