# p14 evidence release candidate 15

Date: 2026-11-19
Status: public candidate after the rc14 independent reviews.

## Contents

- Paper 1: official SoftwareX `cas-sc`, 10 pages, 3,741 words, 3 figures, one content table + metadata;
  one-page supplement.
- Paper 2: JORS, 8 pages, 3,816 words, 1 figure, 2 compact tables; 4-page supplement.
- Public replay instructions for both papers.
- Software tags: WS4 `ws4-v0.2.0-p14rc1`; FRESH Solutions `v0.9.3-p13rc1`.

## Changes from rc14

- Corrected the Paper 1 sparse-effect-table description to match the released GPU path:
  caller-supplied table, no embedded dataset identity, explicit rebuild on dataset/candidate-order
  change, and target reuse only when the required cells are in the basis.
- Replaced the stale Paper 2 release replay asset with the tagged `paper2/REPLAY.md`.
- Updated manifest hashes and paper counts after the text fix.

## Verified

- Public clone replay: 200/200 QAP, 200/200 BLS, 100/100 TSP, 1,060 broad, 40 generic,
  40 framework + 20 deep TSP.
- Public TSA24 tarball/layout replay passes.
- Both target drafts and supplements compile.
- Local dashboard green.

## Still pending

- DOI/Zenodo and a tested container run.
- Fresh review of rc15 and PI approval.
- Journal page/layout acceptance.
