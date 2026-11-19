# P14 release candidate 2

Date: 2026-11-11
Status: public prerelease with sole-author metadata and target-journal drafts.

## Included

- Paper 1 working manuscript and SoftwareX target draft (8 pages, 3,874 counted words).
- Paper 2 working manuscript and JORS Issues in Research Software target draft (9 pages, 3,798 words).
- JORS supplement with full per-instance tables.
- QAP/TSP/TSA24 evidence, replay scripts, manifests, claim audit, significant-figures audit.
- Sole author: Gregory Paradis, UBC FRESH Lab, University of British Columbia.
- Software release candidates: WS4 `ws4-v0.2.0-p14rc1`; FRESH Solutions `v0.9.3-p13rc1`.

## Verification

- Public clone from this repository passes `paper2/replay_all.sh`:
  200/200 expanded QAP, 200/200 BLS, 100/100 expanded TSP, 1,060 broad, 40 generic,
  40 framework + 20 deep TSP.
- Public clone passes `paper/replay_all.sh` with WS4, TSA24, and FHOPS roots.
- SoftwareX and JORS drafts compile from the public clone.
- Local dashboard green.

## Still pending

- DOI/Zenodo deposit and tested container digest.
- Official SoftwareX template and final page/format checks.
- JORS page guide (9 pages vs roughly 4–6; word count inside limit).
- Tabu `bur26` verification and per-record CPU scope.
- Independent review of the target drafts.
- Final PI approval of the drafts for submission.
