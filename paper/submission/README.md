# Paper 1 submission variant

Target: Environmental Modelling & Software.

- `paper1-elsarticle.tex` — `elsarticle` preprint variant with placeholder author metadata.
- `elsarticle.cls` — generated from CTAN `elsarticle.dtx` (LPPL).
- `elsarticle-num.bst` — CTAN bibliography style.
- `paper1-elsarticle.pdf` — compiled review copy (29 pages, 11pt preprint).
- `cover-letter.md`, `highlights.md`.

Build:

```bash
cd paper/submission
latexmk -pdf paper1-elsarticle.tex
```

The author, affiliation, email, CRediT, funding, competing-interest, and corresponding-author
placeholders must be replaced by the PI-approved metadata before submission.
