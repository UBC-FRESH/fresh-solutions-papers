# Cover letter draft — Environmental Modelling & Software

Dear Editor,

Please consider our manuscript, **"Compiled landscape optimisation: exact resident state and GPU population search for harvest
scheduling"**, for Environmental Modelling & Software.

The paper addresses a practical software-engineering problem in environmental modelling: landscape
planning models are difficult not only because the objective is complex, but because the model, exact
accounting state, and search move are usually rebuilt together. We describe a compiled-state
architecture that separates a stable compiled model, compact candidate and sparse effect indexes,
exact resident accounting, and batched GPU population search with exact CPU replay.

The evidence is deliberately bounded. We evaluate a public frozen TSA24 landscape with 208,255
operable blocks, report a 100,000-generation five-seed GPU campaign with exact CPU replay, and report
negative or non-competitive results where they occurred. A 64-genome factorized batch is 248 times
shorter on CUDA than on a single-device CPU path with maximum exact-evaluator error 1.7e-6. A
100-generation matched implementation run uses 22-fold less CUDA search time, with a slightly worse
one-seed objective; the CPU path is not tuned, so we do not turn that into a hardware claim.

We do **not** claim state-of-the-art landscape optimization, competitive performance against an
independent harvest-scheduling model, or partner-endorsed operational impact. The contribution is the
architecture and the evidence boundary: a reader can inspect, replay, and challenge every reported
incumbent.

The TSA24 artifact is public. The paper-specific schedules and replay scripts remain in the project
evidence repository pending the approved public evidence release. We would be glad to provide any
additional material.

Sincerely,

[Corresponding author name]
[Affiliation]
[Email]
