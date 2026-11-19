# P14 release candidate 1

Date: 2026-11-11
Status: initial public evidence release candidate; not a final article submission.

## What this release is

A public snapshot of the papers/evidence repository while the Paper 1 SoftwareX and Paper 2 JORS
submission drafts are being finalized. It is intentionally a **prerelease**; more releases will follow
as the drafts, author metadata, and final evidence tags are completed.

## Contents

- Paper 1 working manuscript and SoftwareX target draft.
- Paper 2 working manuscript and JORS target draft.
- QAP/TSP/TSA24 evidence, replay scripts, and evidence manifests.
- Claim-to-evidence and significant-figures audits.
- Target journal conversion directories.

## Known limitations

- The SoftwareX official template is not yet applied.
- The JORS draft is 8 pages against a rough 4–6 page guide, although its word count is inside 3,000–4,000.
- The TSP breadth panel is disclosed as a frozen mixed-depth panel; it is not a single-rule depth experiment.
- The tabu `bur26` result has not been verified against an independent robust-tabu implementation.
- Per-record CPU time is missing from expanded-QAP and expanded-TSP records; the paper scopes that.
- A DOI/Zenodo deposit is not yet minted. The GitHub release is not a DOI.

## Author and licence

Sole author: Gregory Paradis, UBC FRESH Lab, University of British Columbia.
Repository licence: MIT for code; see `LICENSING.md` for the manuscript and derived-artifact terms.

## Verification

- Public clone at tag `p14-evidence-rc1` passes `paper2/replay_all.sh`:
  200/200 expanded QAP, 200/200 BLS, 100/100 expanded TSP, 1,060 broad, 40 generic,
  40 framework + 20 deep TSP.
- Public clone passes `paper/replay_all.sh` with WS4, TSA24, and FHOPS roots.
- The SoftwareX draft builds to 8 pages; the JORS draft builds to 8 pages.

