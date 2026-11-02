# Paper 1 scope decision

Status: decided
Date: 2026-11-02

## Decision

Scope Paper 1 as an **architecture and reproducibility paper** with a public
benchmark artifact. Do not claim a competitive win against the landscape
literature without an independent model baseline.

## What the evidence supports

- Exact compiled-state accounting on 208,255 TSA24 blocks.
- 100,000-generation GPU-GA: five seeds, objectives 512.574–518.621, exact replay.
- Independent CPU-SA search on the same model: 335,044,976.675435, 30-minute
  time limit, not converged.
- Public frozen artifact `ws4-tsa24-evenflow-v1`.
- Exact replay and schema-valid records.

## What it does not support

- An independent model comparison.
- A state-of-the-art landscape claim.
- A partner-endorsed operational impact claim.

## Consequence

Paper 1 can be written as a systems/forestry-informatics contribution now. If an
independent landscape model becomes available, the paper can be extended into a
competitive benchmark paper.
