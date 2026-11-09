# Paper 1 evidence release candidate

Status: local candidate only. No tag, release, visibility change, or DOI has been made.

## Assets

- `paper/paper1-manuscript.pdf`
- `paper/paper1-manuscript.tex`
- `paper/figures/`
- `paper/references.bib`
- `paper/evidence/`
- `paper/replay_all.sh`
- `paper/release/manifest-v0.2.0-candidate.json`
- `paper/submission/paper1-elsarticle.tex` (journal variant)

## Verification

- `paper/replay_all.sh` passes.
- `paper/release/manifest-v0.2.0-candidate.json` hashes match.
- Dashboard green on the papers repository.

## Approval-gated actions

```bash
gh repo edit UBC-FRESH/fresh-solutions-papers --visibility public
gh release create paper1-evidence-v0.3.0 \
  --repo UBC-FRESH/fresh-solutions-papers \
  --title "Paper 1 evidence v0.3.0" \
  --notes-file paper/release/paper1-evidence-v0.1.0.md
```

A DOI requires an external Zenodo release action.
