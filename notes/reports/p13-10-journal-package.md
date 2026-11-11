# P13.10 journal package checklist

Status: both journal variants compile; PI metadata/release approvals outstanding
Date: 2026-11-09
Issue: #91

## Prepared assets

- `paper/submission/cover-letter.md`
- `paper/submission/highlights.md`
- `paper/submission/paper1-elsarticle.tex` — EMS `elsarticle` variant, compiles to 28 pages.
- `paper/submission/elsarticle.cls`, `paper/submission/elsarticle-num.bst` — CTAN class/style.
- `paper2/submission/cover-letter.md`
- `paper2/submission/highlights.md`
- `paper2/submission/paper2-sn-jnl.tex` — JoH `sn-jnl` variant, compiles to 28 pages.
- `paper2/submission/sn-jnl.cls`, `paper2/submission/sn-mathphys-num.bst` — official Springer Nature class/style.
- `paper2/submission/README.md` — build and metadata requirements.
- `paper/submission/editor-checklist.md`, `paper2/submission/editor-checklist.md`.

## Paper 1 — Environmental Modelling & Software

- [x] `elsarticle` variant built; working draft remains `article`.
- [ ] Author list, affiliations, corresponding author, CRediT, funding, competing interests.
- [ ] Keywords and highlights (3–5 bullets).
- [ ] 40–60 references; current draft has 40.
- [x] 3 figures; current draft has 3.
- [x] 8,000–9,500 words; current draft 8,574.
- [ ] Public evidence DOI and one-command replay.
- [ ] Independent model baseline or explicit architecture/reproducibility scope.
- [ ] Matched CPU-GA/CPU batch and cache/search ablation or explicit scope.
- [ ] Cover letter that does not claim competitive landscape performance.
- [ ] Final claim-to-evidence audit.

## Paper 2 — Journal of Heuristics

- [x] JoH `sn-jnl` variant built; working draft remains `article`.
- [ ] Author list, affiliations, corresponding author, CRediT, funding, competing interests.
- [ ] Keywords and highlights.
- [ ] 40–60 references; current draft has 42.
- [x] 5 figures; current draft has 5.
- [x] 8,000–9,500 words; current draft 9,357.
- [ ] Public artifact DOI and one-command replay.
- [ ] Complete per-record metadata or explicit campaign-level scope.
- [ ] Independent QAP baseline: BLS present; matched-time comparison still limited.
- [ ] Third-party adapter/portability test or explicit removal of the claim.
- [ ] Cover letter that frames the harness and negative generic-layer result honestly.
- [ ] Final claim-to-evidence audit.

## Fallbacks

- SoftwareX / JORS for either paper if the contribution is intentionally a tool/software paper.
- COR is not a Paper 2 target unless a new methodological contribution is added.

## Gate

No submission without explicit PI approval of target, authors, artifact, and cover letter.
