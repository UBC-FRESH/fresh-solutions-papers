# p14 evidence release candidate 18

Date: 2026-11-19
Status: clean public candidate; supersedes rc17.

## Contents

- Paper 1: official SoftwareX `cas-sc`, 10 pages, 3,754 words, 3 figures, one content table + metadata;
  one-page supplement.
- Paper 2: JORS, 8 pages, 3,830 words, 1 figure, 2 compact tables; 4-page supplement.
- Public replay instructions for both papers.
- Software tags: WS4 `ws4-v0.2.0-p14rc1`; FRESH Solutions `v0.9.3-p13rc1`.

## Changes from rc17

- Removed the superseded 20-page `paper/paper1-manuscript.pdf` and 23-page
  `paper2/paper2-manuscript.pdf` from the submission tree.
- Archived the old working `.tex`, `.pdf`, and `.md` files under
  `notes/archive/working-manuscripts-2026-11-11/`.
- Pointed both Makefiles and READMEs at the final submission PDFs only.
- Updated target capsule links and manifest hashes.

No scientific claim, table, statistic, or evidence record changed.

## Verified

- Both target PDFs regenerated from rc18 sources: 10 pages / 3,754 words and 8 pages / 3,830 words.
- The linked tag tree contains only the final submission PDFs at the paper roots.
- `replay_qap_tabu.py`: 20/20 exact replays.
- Full public replay was verified at rc16, including the added 10k QAP command.
- All manifest file and alias hashes match.
- Local dashboard green.

## Still pending

- DOI/Zenodo and a tested container run.
- PI approval.
- Journal page/layout acceptance.
