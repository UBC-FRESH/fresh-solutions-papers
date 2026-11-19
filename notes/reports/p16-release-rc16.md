# p14 evidence release candidate 16

Date: 2026-11-19
Status: public candidate after the rc15 independent reviews.

## Contents

- Paper 1: official SoftwareX `cas-sc`, 10 pages, 3,754 words, 3 figures, one content table + metadata;
  one-page supplement.
- Paper 2: JORS, 8 pages, 3,830 words, 1 figure, 2 compact tables; 4-page supplement.
- Public replay instructions for both papers.
- Software tags: WS4 `ws4-v0.2.0-p14rc1`; FRESH Solutions `v0.9.3-p13rc1`.

## Changes from rc15

- Corrected Paper 1's sparse-table base description, record replay wording, level range, metadata
  parentheses, docs link, and packaging count; removed the stale factorized cover-letter sentence.
- Corrected Paper 2's 200-kick/20-patience pilot wording, SciPy/BLS attribution, figure citation,
  10k QAP manifest/replay coverage, and replay count.
- Updated manifest hashes and release references.

## Verified

- `replay_qap_tabu.py`: 20/20 exact replays.
- Public clone replay of the prior full set: 200/200 QAP, 200/200 BLS, 100/100 TSP, 1,060 broad,
  40 generic, 40 framework + 20 deep TSP.
- Public TSA24 tarball/layout replay passes.
- Both target drafts and supplements compile.
- Local dashboard green.

## Still pending

- DOI/Zenodo and a tested container run.
- Fresh review of rc16 and PI approval.
- Journal page/layout acceptance.
