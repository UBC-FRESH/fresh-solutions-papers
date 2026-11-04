# Approval gates and exact commands

Status: pending maintainer approval
Date: 2026-11-03

The following actions are **not** performed by the agent. Each requires explicit approval.

## 1. Public repository visibility

```bash
gh repo edit UBC-FRESH/fresh-solutions-papers --visibility public
```

Reason: the manuscript claims a public evidence release is intended, and reviewers need the
paper-specific schedules, runners, and replay scripts. The license files are present, but the
repository is private.

## 2. Paper 1 evidence release

```bash
gh release create paper1-evidence-v0.3.0 \
  --repo UBC-FRESH/fresh-solutions-papers \
  --title "Paper 1 evidence v0.3.0" \
  --notes-file paper/release/paper1-evidence-v0.1.0.md
```

Attach the evidence records, schedules, replay scripts, manuscript source, PDF, figures, and the
candidate manifest. Do not tag until the architecture/CPU-GA scope is settled.

## 3. Paper 2 evidence release

```bash
gh release create paper2-evidence-v0.2.0 \
  --repo UBC-FRESH/fresh-solutions-papers \
  --title "Paper 2 evidence v0.2.0" \
  --notes-file notes/reports/evidence-release-candidates.md
```

Attach the QAP/TSP convergence evidence, expanded panels, provenance sidecar, runners, replay scripts,
manuscript source, PDF, and figures.

## 4. Merge PR #77

```bash
gh pr merge 77 --repo UBC-FRESH/fresh-solutions-papers --squash --delete-branch
```

PR #77 is green but includes only the P12 claims/evidence/figures work. Merge after the final
claim-to-evidence review and after the public-release decision.

## 5. Submission

No manuscript submission command is prepared. Submission requires the target journal's current
author guidelines, author/affiliation metadata, and a final independent review.
