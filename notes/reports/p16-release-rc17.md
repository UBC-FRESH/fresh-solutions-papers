# p14 evidence release candidate 17

Date: 2026-11-19
Status: final public candidate after the rc16 independent gate.

## Contents

- Paper 1: official SoftwareX `cas-sc`, 10 pages, 3,754 words, 3 figures, one content table + metadata;
  one-page supplement.
- Paper 2: JORS, 8 pages, 3,830 words, 1 figure, 2 compact tables; 4-page supplement.
- Public replay instructions for both papers.
- Software tags: WS4 `ws4-v0.2.0-p14rc1`; FRESH Solutions `v0.9.3-p13rc1`.

## Changes from rc16

- Corrected the Paper 2 manifest hash for `paper2/replay_all.sh` after adding the 10k QAP replay.
- Aligned package notes, author metadata, replay counts, highlights, and release-status documents.
- Updated both target drafts to the rc17 capsule link.

No scientific claim, table, statistic, or evidence record changed from rc16.

## Verified

- `replay_qap_tabu.py`: 20/20 exact replays.
- Public clone replay of the full set from rc16, including the added 10k QAP command:
  200/200 QAP, 200/200 BLS, 100/100 TSP, 1,060 broad, 40 generic, 40 framework + 20 deep TSP.
- All manifest file and alias hashes match.
- Both target drafts and supplements compile.
- Local dashboard green.

## Still pending

- DOI/Zenodo and a tested container run.
- PI approval.
- Journal page/layout acceptance.
