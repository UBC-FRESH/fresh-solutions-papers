# Paper 1 evidence release candidate

Status: public release candidate `p14-evidence-rc22`; DOI pending. The tag and release are public.

## Assets

- `paper/submission/softwarex/paper1-softwarex.pdf`
- `paper/figures/`
- `paper/references.bib`
- `paper/evidence/`
- `paper/replay_all.sh`
- `paper/release/manifest-v0.2.0-candidate.json`
- `paper/submission/softwarex/paper1-softwarex.tex` (SoftwareX submission)
- `paper/submission/softwarex/paper1-softwarex-supplement.tex`

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
