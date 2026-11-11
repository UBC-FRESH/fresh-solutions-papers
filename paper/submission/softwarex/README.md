# Paper 1 — SoftwareX Original Software Publication draft

Target-specific conversion of the P0-corrected Paper 1 manuscript. This directory is a new draft; the
main manuscript, evidence, and EMS variant are unchanged.

## Files

- `paper1-softwarex.tex` — SoftwareX-style manuscript (`elsarticle`, preprint, 11 pt, numeric refs, line numbers).
- `paper1-softwarex.pdf` — compiled review copy.
- `elsarticle.cls`, `elsarticle-num.bst` — local class/style copies so the build is self-contained.
- `references-softwarex.bib` — copy of `paper/references.bib`; only the WS4 note capitalization is adjusted.
- `count_words.py` — reproducible word count for the convention below.

## Length and display items

- **Counted words: 3,905.** Counts abstract, running text, captions, and footnotes; excludes
  title/authors/affiliations, references, the metadata table, equations, and data-table bodies.
  Verify with `python3 count_words.py`. Including the three content-table bodies still gives 3,979,
  below the 4,000-word cap.
- **Figures: 2** (architecture, scaling). Limit is 6.
- **Tables: 3 content tables** (scaling, five-seed campaign, evaluation-path diagnostic) plus the
  **mandatory code-metadata table**. The manuscript has no separate table limit; the metadata table is
  excluded from the word count.
- **PDF: 8 pages (two-column draft; official template still to be applied)**, including references and metadata. Abstract: 173 words (SoftwareX limit 250).

## Template status

Built with `elsarticle` in 5p two-column mode with line numbers. This is **not** the official
SoftwareX Original Software Publication template. The official template (and its metadata-table layout)
must be applied before submission; the content is structured to map onto its five sections:
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
