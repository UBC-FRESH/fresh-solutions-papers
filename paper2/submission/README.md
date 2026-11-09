# Paper 2 submission variant — Journal of Heuristics

Target: Journal of Heuristics (Springer Nature).

- `paper2-sn-jnl.tex` — `sn-jnl` conversion, `sn-mathphys-num` references, author placeholders.
- `sn-jnl.cls`, `sn-mathphys-num.bst` — official Springer Nature December 2024 package.
- `paper2-sn-jnl.pdf` — compiled review copy (27 pages).
- `cover-letter.md`, `highlights.md`.

Build:

```bash
cd paper2/submission
latexmk -pdf paper2-sn-jnl.tex
```

The author list, affiliations, corresponding author, CRediT, funding, and competing-interest
statements must be replaced with PI-approved metadata before submission. No submission is made from
this directory.
