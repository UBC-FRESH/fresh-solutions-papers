# P13.4 closeout: portability claim scoped, no third-party adapter

Status: closed as scoped, not as a third-party portability result
Date: 2026-11-09
Issue: #85

## Decision

No third-party adapter was added. The paper does not claim general portability. It provides two
public reference implementations (QAP robust tabu, TSP iterated Lin--Kernighan), a separate applied
TSA24 adapter, and an explicit future-work statement that a third adapter written by someone other
than the reference author is the stronger test.

This satisfies the P13.4 acceptance condition "claims are supported or removed": the unsupported
portability claim is removed, and the limitation is stated in the manuscript.

## Evidence of the current claim boundary

- `paper2/paper2-manuscript.tex:67` says "two public reference implementations".
- `paper2/paper2-manuscript.tex:1071` says a third-party adapter is future work and a stronger test.
- No "portable across problem families" or "third-party validated" claim appears in the manuscript.
- The QAP and TSP adapters share the contract; the applied TSA24 case is separate.

## Why not add a graph-colouring toy adapter

A graph-colouring adapter already exists as a small in-package toy, but adding it as evidence would
not establish third-party portability. It would invite a "toy only" objection and weaken the honest
scope. The paper keeps the stronger statement: two public reference implementations and a scoped
contract, not a universal portability claim.
