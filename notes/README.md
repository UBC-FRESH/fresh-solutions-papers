# Notes

Notes are the persistent, agent-friendly context for this project. They hold what a future reader, human or agent, needs and cannot get from the code, the issues, or the changelog alone.

- `notes/adr/NNNN-slug.md`: decisions. One decision per file. Never rewrite an accepted ADR; supersede it with a new one. Start from `adr/0000-template.md`.
- `notes/reference/`: facts with provenance. Record where each fact came from, how it was read, and what is uncertain.
- `notes/`: focused plans that are too long for `ROADMAP.md`. Link each one from its roadmap task, and keep it current while the task is active.
- `notes/reports/`: the close-out report for each phase. Start from `reports/phase-closeout-template.md`. The report is the evidence for the maintainer's approval.

Keep private material out of this directory.

- `design/programme.md`: the two-paper thesis, benchmark lanes, fairness rules, and risks.
- `reference/benchmark-corpus.md`: literature leads and data-availability status.

- `design/benchmark-record-schema.md`: P1 frozen schema for replayable benchmark records.

- `design/compiled-state-architecture.md`: P2 architecture claim, cache identity, and hybrid search contracts.
- `design/benchmark-adapter-contract.md`: P2 adapter surface and evidence rules.
- `design/replay-and-feasibility.md`: P2 exact-replay and hard-feasibility gate.

- `design/p3-benchmark-selection.md`: FHOPS selected as the first public target; Lockwood deferred as reconstructable.

- `design/fhops-ws4-comparison-decision.md`: P3.5 rejection of a direct FHOPS/WS4 comparison; FHOPS is baseline/reproducibility, not architecture peer.

- `design/paper1-thesis.md`: P4 frozen thesis, contributions, permissible claims, and limitation language.

- `design/paper1-archive.md`: P4 archive/reproduction procedure and known gaps.
- `reports/p4-review.md`: P4 claim audit and internal review.
