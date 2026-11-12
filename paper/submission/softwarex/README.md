# Paper 1 — SoftwareX Original Software Publication draft

Target-specific conversion of the P0-corrected Paper 1 manuscript. This directory is a new draft; the
main manuscript, evidence, and EMS variant are unchanged.

## Files

- `paper1-softwarex.tex` — official SoftwareX `cas-sc` manuscript.
- `paper1-softwarex.pdf` — compiled 10-page review copy.
- `cas-sc.cls`, `cas-common.sty`, `cas-model2-names.bst`, `thumbnails/` — official SoftwareX/Elsevier bundle files.
- `references-softwarex.bib` — copy of `paper/references.bib`; only the WS4 note capitalization is adjusted.
- `count_words.py` — reproducible word count for the convention below.

## Length and display items

- **Counted words: 3,977.** Counts abstract, running text, captions, and footnotes; excludes
  title/authors/affiliations, references, the metadata table, equations, and data-table bodies.
  Verify with `python3 count_words.py`.
- **Figures: 2** (architecture, scaling). Limit is 6.
- **Tables: 3 content tables** (scaling, five-seed campaign, evaluation-path diagnostic) plus the
  **mandatory code-metadata table**. The manuscript has no separate table limit; the metadata table is
  excluded from the word count.
- **PDF: 10 pages (official cas-sc template)**, including references and metadata. Abstract: 173 words (SoftwareX limit 250).

## Template status

Built with the official `cas-sc` SoftwareX bundle. Content is mapped to its required sections:
Motivation and significance; Software description; Validation/illustration; Reuse potential and
limitations; Conclusions.

Build:

```bash
cd paper/submission/softwarex
latexmk -pdf paper1-softwarex.tex
python3 count_words.py
```

## Naming and scope

- The lab is **UBC FRESH Lab**; **FRESH** stays uppercase.
- **WS4** is the forestry software described here. **FRESH Solutions** is the sibling general
  metaheuristic engine and is not the subject of this paper; the draft does not attribute WS4 evidence
  to FRESH Solutions.
- The paper is a software/reproducibility contribution. It makes no environmental-modelling claim and
  no independent harvest-scheduling validation claim.

## Placeholders and submission blockers

1. Author names, affiliations, corresponding author, email, CRediT, funding, and competing interests
   (`author@example.invalid`; metadata C9).
2. Repository tag/DOI for WS4: the draft cites commit `f60ce64` on a feature branch, not a release
   (metadata C1–C2).
3. Public evidence release with a DOI and one-command replay for the paper-specific schedules and
   replay scripts; these are currently private (Data availability; metadata C8).
4. Documentation URL and support email (metadata C7, C9).
5. Official SoftwareX template and any journal-specific metadata/format checks.
6. APC/institutional coverage and PI approval of the target shift.
7. Scope limitation, not a formatting fix: there is no independent harvest-scheduling baseline or
   tuned CPU/GPU comparison. The draft states this and does not claim one.
