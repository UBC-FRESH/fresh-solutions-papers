# P1 close-out: scope, literature, and benchmark corpus

Status: complete
Date: 2026-11-01
Issue: #2

## Result

P1 produced the benchmark programme and a frozen replay schema. It did not produce benchmark wins.

Deliverables:

- `notes/design/programme.md` — two-paper thesis, benchmark lanes, fairness rules, risks.
- `notes/reference/benchmark-corpus.md` — availability matrix for forestry, conservation, and general
  combinatorial benchmarks.
- `notes/design/benchmark-record-schema.md` — timing and comparison vocabulary.
- `schemas/benchmark-record.schema.json` — machine-readable record schema.
- Verified Lockwood and Moore DOI: `10.1139/x93-065`.

## Findings

1. The Lockwood and Moore citation is verified, but the original instance was not located. Its current
   status is **reconstructable candidate**.
2. FHOPS (`UBC-FRESH/fhops`, MIT, public) is the strongest public reproducibility anchor.
3. Most historical forestry papers require reconstruction or author contact; they are not public
   benchmarks by default.
4. Conservation prioritisation must remain a transfer lane, not a like-for-like harvest-scheduling
   comparison.
5. The general combinatorial libraries are the Paper 2 transfer suite.

## Verification

- `pytest`: 138 passed.
- Sphinx HTML with `-W`: pass.
- Workflow validator: 0 errors.
- JSON schema parses.
- No benchmark is marked as a win or public without an evidence status.

## Acceptance criteria

- Every benchmark row has an availability status and provenance. **Met.**
- The comparison protocol is recorded before results. **Met.**
- No benchmark is described as a win without exact replay. **Met.**

## Limits

- Bibliographic verification is not a full-text review of every paper.
- Original data availability still needs author/library requests for several historical papers.
- The first reconstruction target must be chosen in P2.

## Recommendation

Close P1. Start P2 only after the maintainer approves the P2 parent issue.
