# Cover letter draft — Journal of Heuristics

Dear Editor,

Please consider our manuscript, **"Fresh Solutions: a reproducible adapter harness for applied metaheuristic
benchmarks"**, for the Journal of Heuristics.

The paper studies a reproducibility problem that is central to heuristic search: an incumbent is not
a result unless a fresh adapter evaluation reproduces the stored objective and the record names the
instance, seed, budget, stopping reason, and provenance. We specify a small adapter contract, a
resident-state path, and an exact-replay protocol, then report both positive and negative evidence.

The positive evidence includes a 20-instance QAPLIB panel with ten seeds per instance. Robust tabu has
mean gap 0.301% and 73/200 optima; an independent Breakout Local Search baseline has mean 0.096% and
161/200 optima. BLS is lower on 120/200 seed-level runs, higher on 11, and equal on 69; family-balanced
means are 0.298% and 0.099%. A 20-instance TSP panel has 94/100 known optima, 95/100 patience stops,
and five `brazil58` wall-clock cap hits at the known optimum. A generic adapter-only tabu/LNS prototype
is explicitly non-competitive (QAP 3.848% vs 0.097%; TSP 127.978% vs 0.000%), which bounds the
framework claim.

We do not claim state-of-the-art heuristic performance or third-party portability. The paper provides
two public reference implementations and explicitly scopes a third-party adapter as future work. The
evidence repository is private pending an approved public release; we will provide the artifact and
one-command replay to reviewers.

Sincerely,

[Corresponding author name]
[Affiliation]
[Email]
