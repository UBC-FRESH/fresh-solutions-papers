# P12.3 status

Completed:

- Added `paper2/check_evidence.py`.
  - Validates the campaign provenance sidecar.
  - Replays 40 QAP framework incumbents and 20 TSP convergence incumbents.
  - Checks broad-panel record and summary fields.
- Added `paper2/broad_summary.py`.
  - Regenerates `broad-converged-summary.json` from the committed gzip.
  - Verified the regenerated summary is value-equivalent to the previous summary.
- Refactored `run_broad_converged.py`.
  - Uses the canonical summarizer.
  - Writes the list summary schema and a provenance sidecar.
  - Counts only `patience` as converged; cap hits are separate.
- Fixed the Lockwood citation to **Carey Lockwood and Tom Moore**.
- Paper 2 is 19 pages / 8,176 source words, 42 references.

Still blocked:

- Per-record solver/hardware/CPU metadata remains uneven; the manuscript now says so.
- Public evidence release and license remain pending approval.
- Paper 1 architecture experiment and reference expansion remain open.

No tag, release, or visibility change.
