"""Generic sampled tabu search with LNS-style perturbations.

The search is driven only by the :class:`fresh_solutions.contracts.ProblemAdapter`
protocol and :class:`fresh_solutions.engine.ResidentAssignment`.  It never imports a
problem-specific module, reads a problem matrix, or uses a private delta update.  Each
iteration samples a declared number of proposals with ``adapter.propose``, evaluates
them exactly through the resident assignment, and keeps tabu memory on the variables
and values changed by accepted moves.
"""

from __future__ import annotations

import random
import time
from collections.abc import Mapping
from dataclasses import dataclass, field

from fresh_solutions.contracts import Change, Evaluation, ProblemAdapter
from fresh_solutions.engine import ResidentAssignment

TabuKey = int | tuple[int, int]


@dataclass(frozen=True)
class GenericTabuConfig:
    """Configuration for the generic sampled tabu search.

    Parameters
    ----------
    iterations : int, optional
        Maximum number of tabu iterations. Defaults to 20,000.
    patience : int or None, optional
        Stop after this many iterations without a new best. ``None`` disables the
        plateau rule. Defaults to 5,000.
    seed : int, optional
        Random seed for proposals, tenures, and perturbations. Defaults to 1.
    proposals : int, optional
        Number of adapter proposals sampled per iteration. Defaults to 16.
    min_tenure : int, optional
        Minimum tabu tenure in iterations. Defaults to 5.
    max_tenure : int, optional
        Maximum tabu tenure in iterations. Defaults to 15.
    tabu_attribute : str, optional
        ``"move"`` stores ``(variable, value)`` attributes and ``"variable"`` stores
        only the variable. Defaults to ``"move"``.
    perturb_after : int or None, optional
        Apply an LNS-style kick after this many iterations without a new best.
        ``None`` disables perturbation. Defaults to 1,000.
    perturb_interval : int, optional
        Minimum iterations between perturbations. Defaults to 1,000.
    perturb_moves : int, optional
        Number of adapter proposals applied in one perturbation kick. Defaults to 5.
    max_seconds : float or None, optional
        Optional wall-clock limit for the whole search. Defaults to None.
    """

    iterations: int = 20000
    patience: int | None = 5000
    seed: int = 1
    proposals: int = 16
    min_tenure: int = 5
    max_tenure: int = 15
    tabu_attribute: str = "move"
    perturb_after: int | None = 1000
    perturb_interval: int = 1000
    perturb_moves: int = 5
    max_seconds: float | None = None

    def __post_init__(self) -> None:
        """Validate the configuration."""
        if self.iterations < 1:
            raise ValueError("iterations must be positive")
        if self.patience is not None and self.patience < 1:
            raise ValueError("patience must be positive")
        if self.proposals < 1:
            raise ValueError("proposals must be positive")
        if self.min_tenure < 1 or self.max_tenure < self.min_tenure:
            raise ValueError("tenure must be positive and ordered")
        if self.tabu_attribute not in {"move", "variable"}:
            raise ValueError("tabu_attribute must be 'move' or 'variable'")
        if self.perturb_after is not None and self.perturb_after < 1:
            raise ValueError("perturb_after must be positive")
        if self.perturb_interval < 1:
            raise ValueError("perturb_interval must be positive")
        if self.perturb_moves < 0:
            raise ValueError("perturb_moves must not be negative")
        if self.max_seconds is not None and self.max_seconds <= 0.0:
            raise ValueError("max_seconds must be positive")


@dataclass(frozen=True)
class GenericTabuResult:
    """Best assignment and counters from one generic tabu run.

    Parameters
    ----------
    assignment : dict of int to int
        Best variable-to-option assignment.
    objective : float
        Exact objective of the best assignment.
    feasible : bool
        Hard feasibility of the best assignment.
    evaluations : int
        Number of exact evaluations performed.
    iterations : int
        Number of tabu iterations completed.
    accepted : int
        Number of accepted moves.
    tabu_rejections : int
        Number of sampled candidates rejected by tabu memory.
    tabu_overrides : int
        Number of iterations that accepted the best candidate despite tabu memory.
    perturbations : int
        Number of LNS-style kicks applied.
    stop_reason : str
        One of ``"patience"``, ``"max_iterations"``, ``"max_seconds"``, or
        ``"no_candidates"``.
    wall_seconds : float
        Elapsed wall-clock time.
    cpu_seconds : float
        Elapsed process CPU time.
    history : tuple of float
        Best-ever objective after each iteration.
    """

    assignment: dict[int, int]
    objective: float
    feasible: bool
    evaluations: int
    iterations: int
    accepted: int
    tabu_rejections: int
    tabu_overrides: int
    perturbations: int
    stop_reason: str
    wall_seconds: float
    cpu_seconds: float
    history: tuple[float, ...] = field(default_factory=tuple)

    def to_dict(self) -> dict[str, object]:
        """Return a JSON-ready result.

        Returns
        -------
        dict of str to object
            Result with sorted assignment keys.
        """
        return {
            "assignment": {str(key): value for key, value in sorted(self.assignment.items())},
            "objective": self.objective,
            "feasible": self.feasible,
            "evaluations": self.evaluations,
            "iterations": self.iterations,
            "accepted": self.accepted,
            "tabu_rejections": self.tabu_rejections,
            "tabu_overrides": self.tabu_overrides,
            "perturbations": self.perturbations,
            "stop_reason": self.stop_reason,
            "wall_seconds": self.wall_seconds,
            "cpu_seconds": self.cpu_seconds,
            "history": list(self.history),
        }


@dataclass(frozen=True)
class _Candidate:
    """One evaluated adapter proposal."""

    change: Change
    evaluation: Evaluation
    assignment: Mapping[int, int]
    tabu_keys: tuple[TabuKey, ...]
    tabu: bool


def _changed_variables(
    before: Mapping[int, int],
    after: Mapping[int, int],
) -> tuple[int, ...]:
    """Return the variables whose option changed between two assignments.

    Parameters
    ----------
    before : mapping of int to int
        Assignment before the move.
    after : mapping of int to int
        Assignment after the move.

    Returns
    -------
    tuple of int
        Changed variable positions in ascending order.
    """
    return tuple(variable for variable in after if before.get(variable) != after[variable])


def _tabu_keys(
    variables: tuple[int, ...],
    assignment: Mapping[int, int],
    attribute: str,
) -> tuple[TabuKey, ...]:
    """Build tabu keys for a set of changed variables.

    Parameters
    ----------
    variables : tuple of int
        Changed variable positions.
    assignment : mapping of int to int
        Assignment that supplies the option values.
    attribute : str
        ``"move"`` for ``(variable, value)`` keys or ``"variable"`` for variable keys.

    Returns
    -------
    tuple of (int or tuple of int and int)
        Tabu keys.
    """
    if attribute == "variable":
        return variables
    return tuple((variable, assignment[variable]) for variable in variables)


def _is_tabu(
    keys: tuple[TabuKey, ...],
    tabu_until: Mapping[TabuKey, int],
    iteration: int,
) -> bool:
    """Return whether any key is still tabu at the current iteration.

    Parameters
    ----------
    keys : tuple of (int or tuple of int and int)
        Candidate tabu keys.
    tabu_until : mapping of key to int
        Expiry iteration for each key.
    iteration : int
        Current iteration.

    Returns
    -------
    bool
        True when at least one key has a future expiry.
    """
    return any(tabu_until.get(key, 0) > iteration for key in keys)


def _evaluate_proposals(
    adapter: ProblemAdapter,
    state: ResidentAssignment,
    rng: random.Random,
    config: GenericTabuConfig,
    iteration: int,
    tabu_until: Mapping[TabuKey, int],
) -> tuple[list[_Candidate], int]:
    """Sample and exactly evaluate adapter proposals from the resident state.

    Parameters
    ----------
    adapter : ProblemAdapter
        Problem adapter.
    state : ResidentAssignment
        Current resident assignment.
    rng : random.Random
        Random source for proposals.
    config : GenericTabuConfig
        Search settings.
    iteration : int
        Current tabu iteration.
    tabu_until : mapping of key to int
        Tabu expiries.

    Returns
    -------
    tuple of list of _Candidate and int
        Evaluated feasible candidates and the number of exact evaluations used.
    """
    base = state.assignment
    candidates: list[_Candidate] = []
    evaluations = 0
    for _ in range(config.proposals):
        change = adapter.propose(base, rng)
        if change is None:
            continue
        state.apply(change)
        candidate_assignment = state.assignment
        candidate_evaluation = state.evaluate()
        state.undo(change)
        evaluations += 1
        if not candidate_evaluation.feasible:
            continue
        changed = _changed_variables(base, candidate_assignment)
        keys = _tabu_keys(changed, candidate_assignment, config.tabu_attribute)
        candidates.append(
            _Candidate(
                change=change,
                evaluation=candidate_evaluation,
                assignment=candidate_assignment,
                tabu_keys=keys,
                tabu=_is_tabu(keys, tabu_until, iteration),
            )
        )
    return candidates, evaluations


def _best_candidate(candidates: list[_Candidate]) -> _Candidate:
    """Return the feasible candidate with the lowest exact objective.

    Parameters
    ----------
    candidates : list of _Candidate
        Non-empty candidate list.

    Returns
    -------
    _Candidate
        Lowest-objective candidate; ties keep the first sampled proposal.
    """
    return min(candidates, key=lambda candidate: candidate.evaluation.objective)


def _apply_perturbation(
    adapter: ProblemAdapter,
    state: ResidentAssignment,
    rng: random.Random,
    moves: int,
) -> tuple[Evaluation, int]:
    """Apply a generic LNS-style kick and evaluate the resulting state.

    Parameters
    ----------
    adapter : ProblemAdapter
        Problem adapter.
    state : ResidentAssignment
        Resident assignment to perturb.
    rng : random.Random
        Random source for proposals.
    moves : int
        Number of sequentially applied adapter proposals.

    Returns
    -------
    tuple of Evaluation and int
        Exact evaluation after the kick and one evaluation count.
    """
    for _ in range(moves):
        change = adapter.propose(state.assignment, rng)
        if change is None:
            continue
        state.apply(change)
    return state.evaluate(), 1


def run_generic_tabu(
    adapter: ProblemAdapter,
    config: GenericTabuConfig,
    *,
    initial: Mapping[int, int] | None = None,
) -> GenericTabuResult:
    """Run generic sampled tabu search with optional LNS perturbations.

    Parameters
    ----------
    adapter : ProblemAdapter
        Problem adapter supplying proposals, exact evaluation, and apply/undo.
    config : GenericTabuConfig
        Search settings.
    initial : mapping of int to int or None, optional
        Starting assignment. None uses the adapter's initial assignment.

    Returns
    -------
    GenericTabuResult
        Best assignment, exact objective, counters, stop reason, and timings.
    """
    rng = random.Random(config.seed)
    state = ResidentAssignment(adapter, initial)
    started_wall = time.perf_counter()
    started_cpu = time.process_time()
    current = state.evaluate()
    best = current
    best_assignment = dict(state.assignment)
    evaluations = 1
    accepted = 0
    tabu_rejections = 0
    tabu_overrides = 0
    perturbations = 0
    iterations = 0
    last_improvement = 0
    last_perturbation = 0
    tabu_until: dict[TabuKey, int] = {}
    history: list[float] = [best.objective]
    stop_reason = "max_iterations"

    for iteration in range(1, config.iterations + 1):
        elapsed = time.perf_counter() - started_wall
        if config.max_seconds is not None and elapsed >= config.max_seconds:
            stop_reason = "max_seconds"
            break
        iterations = iteration
        candidates, used = _evaluate_proposals(
            adapter,
            state,
            rng,
            config,
            iteration,
            tabu_until,
        )
        evaluations += used
        if not candidates:
            stop_reason = "no_candidates"
            break

        tabu_rejections += sum(1 for candidate in candidates if candidate.tabu)
        admissible = [
            candidate
            for candidate in candidates
            if not candidate.tabu or candidate.evaluation.objective < best.objective
        ]
        if admissible:
            chosen = _best_candidate(admissible)
        else:
            chosen = _best_candidate(candidates)
            tabu_overrides += 1

        base = state.assignment
        state.apply(chosen.change)
        current = chosen.evaluation
        accepted += 1
        tenure = rng.randint(config.min_tenure, config.max_tenure)
        removed = _tabu_keys(
            _changed_variables(base, chosen.assignment),
            base,
            config.tabu_attribute,
        )
        for key in removed:
            tabu_until[key] = iteration + tenure

        if current.objective < best.objective:
            best = current
            best_assignment = dict(state.assignment)
            last_improvement = iteration

        if config.patience is not None and iteration - last_improvement >= config.patience:
            history.append(best.objective)
            stop_reason = "patience"
            break

        if (
            config.perturb_after is not None
            and config.perturb_moves > 0
            and iteration - last_improvement >= config.perturb_after
            and iteration - last_perturbation >= config.perturb_interval
        ):
            perturbed, used = _apply_perturbation(
                adapter,
                state,
                rng,
                config.perturb_moves,
            )
            evaluations += used
            current = perturbed
            perturbations += 1
            last_perturbation = iteration
            if current.objective < best.objective:
                best = current
                best_assignment = dict(state.assignment)
                last_improvement = iteration

        history.append(best.objective)

    return GenericTabuResult(
        assignment=best_assignment,
        objective=best.objective,
        feasible=best.feasible,
        evaluations=evaluations,
        iterations=iterations,
        accepted=accepted,
        tabu_rejections=tabu_rejections,
        tabu_overrides=tabu_overrides,
        perturbations=perturbations,
        stop_reason=stop_reason,
        wall_seconds=time.perf_counter() - started_wall,
        cpu_seconds=time.process_time() - started_cpu,
        history=tuple(history),
    )
