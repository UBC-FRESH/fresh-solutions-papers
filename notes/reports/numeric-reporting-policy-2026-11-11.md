# Numeric reporting policy

Date: 2026-11-11
Scope: Paper 1 and Paper 2 manuscripts, tables, figure captions, and journal variants.

## Rule

Full precision is retained in the evidence files. The papers report rounded values using the
following rules, applied by quantity rather than by whichever format appeared in an earlier draft.

1. **Counts, seeds, budgets, iterations, kicks, blocks, and runs** — exact integers, with thousands
   separators for readability.
2. **Optimality gaps and percentage errors** — three decimal places, in percentage points
   (0.001 percentage point). A value whose magnitude rounds to zero is written `0.000%`.
3. **Exact campaign objectives, flow terms, and level terms** — six significant figures. The mean,
   median, and per-seed values use the same precision. Full-precision values remain in the evidence.
4. **Screen and one-seed diagnostic objectives** — three significant figures, because they are not
   estimates of a converged campaign. This applies to the TSA24 target screen and the matched
   CPU/CUDA short-horizon search.
5. **Elapsed times and wall/search durations** — three significant figures. Timing differences below
   that are not interpreted.
6. **Ratios, speed factors, and CPU overheads** — three significant figures. Confidence intervals use
   the same precision as the point estimate.
7. **P-values and residual exactness checks** — two significant figures in scientific notation where
   needed; exact replay status is reported separately.
8. **Derived shares or percentages** — one decimal place unless they are optimality gaps, which use
   rule 2.

## Implementation

- Tables state the relevant unit in the column header.
- Figure axes use the full data; captions quote only the rounded values already reported in text or
  tables.
- Journal variants are regenerated from the same rounded sources.
