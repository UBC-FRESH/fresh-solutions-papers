# P13.5 closeout: controlled architecture ablation

Status: complete as a controlled, scoped ablation
Date: 2026-11-09
Issue: #86

## Controlled results

### Factorized batch
- TSA24 factorized archive, 64 genomes, four mixed feature/product cells, three repeats.
- CPU 23.124 s; CUDA 0.0931 s; **248-fold** shorter CUDA batch time.
- Max exact-evaluator error 1.7e-6; GPU peak 9.27 GB; build 234.4 s.
- Batch evaluation only.

### Matched implementation search
- Same `gpu-run` implementation, full TSA24 model, population 64, seed 7, 1/10/100 generations.
- 100 generations: CPU search 528.756 s; CUDA search 23.866 s; exact both.
- CPU one-seed objective 7.11e7; CUDA 7.49e7; CPU is about 5% lower.
- The CPU path is a single torch device path, not a tuned multithreaded CPU-GA.
- No hardware-speed or quality claim is made.

### Evaluation path
- 5,000-block exact delta/apply vs whole-schedule evaluation: 0.542 ms vs 1.086 s, final objective
  matched to 3.7e-9.
- This is a bounded diagnostic, not full-instance scaling.

## Acceptance

- Controlled ablation table with exact replay: yes.
- Paper supports a reproducibility/software architecture claim, not a universal speed claim: yes.
- No "GPU is faster" claim from an untuned comparator: the text reports a time ratio and explicitly
  disclaims hardware and quality claims.

## Remaining, not claimed

- A tuned CPU-GA/CPU-SA at equal work and wall time.
- A full 100,000-generation CPU comparison.
- A cache-load/search split at equal work.
- Full effect-table-versus-direct evaluator comparison on the full instance.

These remain future work; the paper states them as limitations.
