# Paper 2 — JORS Issues in Research Software draft

Target: **Journal of Open Research Software**, *Issues in Research Software* (experience and
reproducibility report). This is not a Software Metapaper. The journal has no mandatory LaTeX
template; this package uses a clean `article` build with `natbib` numeric citations.

## Files

- `paper2-jors.tex` — main manuscript source.
- `paper2-jors.pdf` — compiled manuscript.
- `paper2-jors-supplement.tex` — supplementary material with the full per-instance tables.
- `paper2-jors-supplement.pdf` — compiled supplement (2 pages).
- `references.bib` — unchanged copy of `paper2/references.bib`.
- `figures/` — copies of the two committed evidence figures; the architecture figure is inline TikZ.

Build with `latexmk -pdf paper2-jors.tex` and `latexmk -pdf paper2-jors-supplement.tex`.
The main build has no undefined citations, overfull boxes, or LaTeX warnings.

## Counts

- **Word count: 3,783** in the counted text (title through Data and code availability, including
  abstract, headings, table contents, and captions; excludes the reference list).
  Command: `detex -n paper2-jors.tex | wc -w`.
- **PDF pages: 8** (6 pages of text/figures/tables plus 2 pages of references).
- **Figures: 1** (architecture boundary; framework overhead is reported in text).
- **Tables: 2** in the main text (compact QAP/BLS family summary; compact TSP depth summary).
  The supplement contains the full 20-row QAP and TSP tables plus the four-instance framework table.
- **References: 28**, Vancouver-style numeric citations in square brackets, in order of first
  appearance. Style: `natbib` `[numbers,sort&compress]` with `unsrtnat`.
- **Replay count stated in the paper:** 40 framework + 20 deep-TSP + 200 expanded-QAP + 200 BLS +
  100 expanded-TSP + 40 generic + 1,060 broad incumbents.

## Placeholders

- Software repository: `[repository URL to be supplied at release]`.
- Archived artifact DOI: `[DOI to be assigned]`.
- Author list is the lab byline `UBC FRESH Lab, University of British Columbia`; corresponding
  author, individual authors, affiliations, ORCIDs, CRediT, funding, and competing-interest
  statements are not yet supplied.
- The repository and release tag are public; a DOI and tested container digest remain pending.
  The evidence set is the public release candidate `p14-evidence-rc10`.

## Blocking issues

1. **Public release / DOI.** The repository and tag are public; a DOI and a tested container digest
   remain pending.
2. **Exact release blocker.** Per-record CPU time is missing from the expanded-QAP and expanded-TSP
   evidence records. The candidate manifest covers the ten-seed `qap-expanded-100k-10seed` files used
   in Table 1; per-record CPU remains missing. The candidate cannot become an archival DOI release
   until that is resolved or the claim is explicitly scoped.
3. **Provenance identity.** All records now use replay commit `4583ad3`; the manifest and release tag
   are the remaining identity check.
4. **Archived repository document.** The old `paper2/paper2-draft.md` is archived at
   `notes/archive/paper2-draft-2026-11-03.md`; the public submission path is this JORS draft.
5. **Container.** The base image and solver checkout are pinned, but no container build has been
   executed in this session.
6. **TSP depth protocol.** The 20-instance panel is frozen and mixed-depth (17 at depth 4, `lin105`
   at 3, `d198` and `pr152` at 2). This is disclosed in the paper, but it is not a single
   pre-registered depth rule. Decide whether to rerun under one rule before submission.
7. **Tabu credibility.** The tabu reference reaches 0/80 optima on `bur26`. The paper states this as
   a property of this untuned reference, but it has not been verified against a published
   robust-tabu implementation or accompanied by a per-seed diversity table.
8. **Generic-layer comparison.** The generic negative result is not matched for start quality or
   work; the paper is scoped to “this configuration is not competitive.”
9. **APC/waiver.** Not confirmed. Do not state or imply that JORS is free; confirm the current APC
   and any institutional waiver separately.
10. **Journal metadata.** Cover letter, editor checklist, keywords confirmation, author metadata,
    CRediT, funding, and competing interests are still required at submission.
11. **Page guide.** The word count is inside the 3,000–4,000 limit, but the 10 pt `article` build is
    8 pages, above the journal’s rough 4–6 page guide. The publisher’s own typesetting may differ;
    do not cut below 3,000 words to chase the page estimate.

## Source discipline

The main manuscript, the evidence directory, and the obsolete JoH `sn-jnl` variant were not edited.
The figures reused here are the committed `paper2/figures/framework-overhead.pdf` and
`broad-gaps.pdf`. All numbers are taken from the current evidence summaries; the BLS inference uses
the corrected cluster-by-instance interval (−0.300 to −0.111), the family interval (−0.234 to
−0.163), and the 15/16 instance-level result.
