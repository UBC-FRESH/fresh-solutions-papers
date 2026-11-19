# P13.7 clean-clone verification

Date: 2026-11-09
Status: passes locally; public visibility/DOI still approval-gated

## Commands

```bash
git clone --branch feature/p13-publication-hardening --recurse-submodules \
  /srv/shared-data/gep/ws4/fresh-solutions-papers /tmp/p13-clean
cd /tmp/p13-clean
QAPLIB_ROOT=/srv/shared-data/gep/ws4/tmp/bench-inventory/qaplib/QAPLIB \
TSPLIB_ROOT=/srv/shared-data/gep/ws4/tmp/bench-inventory/tsplib \
bash paper2/replay_all.sh
```

## Result

- 40 framework incumbents exact.
- 20 deep-TSP incumbents exact.
- 1,060 broad QAP/TSP incumbents exact; 25 `esc8` parse-error records skipped.
- 200 expanded QAP incumbents exact.
- 100 expanded TSP incumbents exact.
- 200 BLS incumbents exact.
- 40 generic-tabu incumbents exact.
- 5/100 expanded TSP cap hits reported as cap hits.

## Journal builds from the clean clone

- `paper/submission/paper1-elsarticle.tex`: builds, 29 pages.
- `paper2/submission/paper2-sn-jnl.tex`: builds, 27 pages.

## Remaining gate

The repository is still private and no tag/release/DOI has been created. A reviewer cannot run the
clone command until the visibility gate is approved.
