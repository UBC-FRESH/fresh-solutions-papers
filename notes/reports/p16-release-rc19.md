# p14 evidence release candidate 19

Date: 2026-11-19
Status: clean public candidate; supersedes rc18.

## Contents

- Paper 1: official SoftwareX `cas-sc`, 10 pages, 3,754 words, 3 figures, one content table + metadata;
  one-page supplement.
- Paper 2: JORS, 8 pages, 3,830 words, 1 figure, 2 compact tables; 4-page supplement.
- Public replay instructions for both papers.
- Software tags: WS4 `ws4-v0.2.0-p14rc1`; FRESH Solutions `v0.9.3-p13rc1`.

## Changes from rc18

- Removed the obsolete EMS fallback `paper1-elsarticle.tex/.pdf` from the submission directory.
  That fallback used `\citet` with a numeric bibliography and rendered `(author?)` citations.
- Archived the fallback under `notes/archive/working-manuscripts-2026-11-11/` with a warning.
- Removed its stale aliases from the Paper 1 manifest.
- Updated both target capsule links.

No scientific claim, table, statistic, or evidence record changed.

## Verification

- SoftwareX PDF: 10 pages, 3,754 counted words, 18/18 citation links resolve, zero `(author?)`,
  `[?]`, or `??` markers.
- JORS PDF: 8 pages, 3,830 counted words, 24 citation links, zero broken markers.
- Clean-clone SoftwareX build reproduced the citation-bearing PDF.
- All manifest file and alias hashes match.
- Local dashboard green.

## Still pending

- DOI/Zenodo and a tested container run.
- PI approval.
- Journal page/layout acceptance.
