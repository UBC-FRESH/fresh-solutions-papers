"""Breakout Local Search for the quadratic assignment problem.

This module is an independent baseline for the Paper 2 QAP panel.  It follows the
Breakout Local Search (BLS) design of Benlic and Hao (2013): a best-improvement
swap descent to a local optimum, followed by an adaptive perturbation.  The
perturbation strength ``L`` is reinitialised after an improving local optimum,
incremented when the search returns to the same local optimum, and set to
``LMax`` after ``T`` consecutive non-improving local optima.  Perturbations are
directed (tabu-guided least-degrading swaps), recency-based (least recently
applied swaps), or random, with probabilities driven by the non-improvement
counter ``omega``.

The search policy is deliberately different from the robust tabu search in
``fresh_solutions.adapters.qap_tabu``.  Robust tabu applies one best admissible
swap per iteration with a tenure rule.  BLS runs each descent to a local optimum
and uses the tabu list only inside directed perturbations.  The two methods
therefore consume a comparable move budget but explore different trajectories.

Instance data are read through :class:`fresh_solutions.adapters.QuadraticAssignment`.
Every returned objective is re-evaluated with the adapter, so a delta-arithmetic
defect cannot silently enter the evidence.

References
----------
Benlic, U., and Hao, J.-K. (2013). Breakout Local Search for the quadratic
assignment problem. *Applied Mathematics and Computation*, 219(9), 4800-4815.

Notes
-----
The published parameter defaults are used where they apply to this panel:
``L0 = 0.15 n``, ``LMax = rand[0.4 n, 0.6 n]``, ``T = 2500``,
``gamma = rand[0.9 n, 1.1 n]``, ``P0 = 0.75``, and ``Q = 0.7``.  The stop rule
is a move cap plus move patience rather than the paper's wall-clock budget, and
the run starts from the adapter's identity assignment to match the robust tabu
panel.  These choices are documented in the P13.2 report; the module must not be
read as a state-of-the-art claim.
"""

from __future__ import annotations

import math
import random
from collections.abc import Mapping
from dataclasses import dataclass, field

import numpy as np
from fresh_solutions.adapters.qap import QuadraticAssignment

try:  # pragma: no cover - the fallback is exercised only without the extra
    from numba import njit
except ImportError:  # pragma: no cover - environment dependent
    NUMBA_AVAILABLE = False
else:  # pragma: no cover - environment dependent
    NUMBA_AVAILABLE = True

_EPS = 1e-9
_HISTORY_CAP = 8192


def _no_jit(*args: object, **kwargs: object) -> object:
    """Return a decorator that leaves a function unchanged.

    Parameters
    ----------
    *args : object
        Positional arguments accepted by ``numba.njit``.
    **kwargs : object
        Keyword arguments accepted by ``numba.njit``.

    Returns
    -------
    object
        A decorator that returns the decorated function unchanged.
    """

    def decorate(function: object) -> object:
        return function

    return decorate


jit = njit if NUMBA_AVAILABLE else _no_jit


@dataclass(frozen=True)
class QapBlsConfig:
    """Configuration for the QAP Breakout Local Search baseline.

    Parameters
    ----------
    max_moves : int, optional
        Hard cap on applied swaps.  Defaults to 1,000,000, the same cap as the
        100k-patience robust tabu panel.
    patience : int, optional
        Stop after this many applied swaps without a new best objective.
        Defaults to 100,000, the same patience as the robust tabu panel.
    seed : int, optional
        Seed for the perturbation stream.  Defaults to 1.
    initial_strength : int or None, optional
        Default jump magnitude ``L0``.  ``None`` selects ``max(2, round(0.15 n))``,
        the published value for instance types I, III and IV.
    max_strength : int or None, optional
        Maximal jump magnitude ``LMax``.  ``None`` draws
        ``rand[0.4 n, 0.6 n]`` with the run seed.
    threshold : int, optional
        Number ``T`` of consecutive non-improving local optima before a strong
        perturbation.  Defaults to the published 2500.
    min_tenure : int or None, optional
        Lower bound of the move tabu tenure ``gamma``.  ``None`` selects
        ``ceil(0.9 n)``.
    max_tenure : int or None, optional
        Upper bound of the move tabu tenure ``gamma``.  ``None`` selects
        ``floor(1.1 n)``.
    directed_probability_floor : float, optional
        Smallest probability ``P0`` of a directed perturbation.  Defaults to
        the published 0.75.
    recency_share : float, optional
        Share ``Q`` of recency-based perturbations among non-directed
        perturbations.  Defaults to the published 0.7.
    """

    max_moves: int = 1_000_000
    patience: int = 100_000
    seed: int = 1
    initial_strength: int | None = None
    max_strength: int | None = None
    threshold: int = 2500
    min_tenure: int | None = None
    max_tenure: int | None = None
    directed_probability_floor: float = 0.75
    recency_share: float = 0.7

    def __post_init__(self) -> None:
        """Validate the configuration."""
        if self.max_moves < 1:
            raise ValueError("max_moves must be positive")
        if self.patience < 1:
            raise ValueError("patience must be positive")
        if self.initial_strength is not None and self.initial_strength < 1:
            raise ValueError("initial_strength must be positive")
        if self.max_strength is not None and self.max_strength < 1:
            raise ValueError("max_strength must be positive")
        if self.threshold < 1:
            raise ValueError("threshold must be positive")
        if self.min_tenure is not None and self.min_tenure < 1:
            raise ValueError("min_tenure must be positive")
        if self.max_tenure is not None and self.max_tenure < 1:
            raise ValueError("max_tenure must be positive")
        if (
            self.min_tenure is not None
            and self.max_tenure is not None
            and self.min_tenure > self.max_tenure
        ):
            raise ValueError("min_tenure must not exceed max_tenure")
        if not 0.0 <= self.directed_probability_floor <= 1.0:
            raise ValueError("directed_probability_floor must be in [0, 1]")
        if not 0.0 <= self.recency_share <= 1.0:
            raise ValueError("recency_share must be in [0, 1]")


@dataclass(frozen=True)
class QapBlsResult:
    """Best assignment and counters from QAP Breakout Local Search.

    Attributes
    ----------
    assignment : dict of int to int
        Best permutation found.
    objective : float
        Objective re-evaluated through the QAP adapter.
    moves : int
        Applied swaps, including descent and perturbation moves.
    evaluations : int
        Candidate swaps examined by neighborhood scans.
    descent_moves : int
        Applied swaps made during local descent.
    perturbation_moves : int
        Applied swaps made during random or directed kicks.
    local_optima : int
        Number of local optima reached.
    random_perturbations : int
        Number of random perturbations.
    recency_perturbations : int
        Number of recency-based perturbations.
    directed_perturbations : int
        Number of tabu-guided directed perturbations.
    strong_perturbations : int
        Number of strong perturbations after ``T`` non-improving local optima.
    final_strength : int
        Jump magnitude ``L`` when the run stopped.
    initial_strength_used : int
        Default jump magnitude ``L0`` for the run.
    max_strength_used : int
        Maximal jump magnitude ``LMax`` drawn for the run.
    min_tenure_used : int
        Lower move-tabu tenure for the run.
    max_tenure_used : int
        Upper move-tabu tenure for the run.
    stop_reason : str
        ``"patience"`` or ``"max_moves"``.
    engine : str
        ``"numba"`` for the compiled symmetric path or ``"reference"`` for the
        exact pure-Python fallback.
    history : tuple of float
        Objective after each new best.
    """

    assignment: dict[int, int]
    objective: float
    moves: int
    evaluations: int
    descent_moves: int
    perturbation_moves: int
    local_optima: int
    random_perturbations: int
    recency_perturbations: int
    directed_perturbations: int
    strong_perturbations: int
    final_strength: int
    initial_strength_used: int
    max_strength_used: int
    min_tenure_used: int
    max_tenure_used: int
    stop_reason: str
    engine: str
    history: tuple[float, ...] = field(default_factory=tuple)

    def to_dict(self) -> dict[str, object]:
        """Return a JSON-ready result.

        Returns
        -------
        dict of str to object
            Serializable result fields.
        """
        return {
            "assignment": {str(key): value for key, value in sorted(self.assignment.items())},
            "objective": self.objective,
            "moves": self.moves,
            "evaluations": self.evaluations,
            "descent_moves": self.descent_moves,
            "perturbation_moves": self.perturbation_moves,
            "local_optima": self.local_optima,
            "random_perturbations": self.random_perturbations,
            "recency_perturbations": self.recency_perturbations,
            "directed_perturbations": self.directed_perturbations,
            "strong_perturbations": self.strong_perturbations,
            "final_strength": self.final_strength,
            "initial_strength_used": self.initial_strength_used,
            "max_strength_used": self.max_strength_used,
            "min_tenure_used": self.min_tenure_used,
            "max_tenure_used": self.max_tenure_used,
            "stop_reason": self.stop_reason,
            "engine": self.engine,
            "history": list(self.history),
        }


def _is_symmetric_zero_diagonal(problem: QuadraticAssignment) -> bool:
    """Return whether the symmetric delta-matrix update applies.

    Parameters
    ----------
    problem : QuadraticAssignment
        QAP instance.

    Returns
    -------
    bool
        ``True`` when both matrices are symmetric with a zero diagonal.
    """
    size = problem.variable_count
    for first in range(size):
        if problem.flows[first][first] != 0.0 or problem.distances[first][first] != 0.0:
            return False
        for second in range(first + 1, size):
            if (
                problem.flows[first][second] != problem.flows[second][first]
                or problem.distances[first][second] != problem.distances[second][first]
            ):
                return False
    return True


@jit(cache=True)
def _objective(
    flows: np.ndarray,
    distances: np.ndarray,
    assignment: np.ndarray,
) -> float:
    """Evaluate a permutation directly on the matrices.

    Parameters
    ----------
    flows : ndarray
        Flow matrix.
    distances : ndarray
        Distance matrix.
    assignment : ndarray
        Permutation of facilities over locations.

    Returns
    -------
    float
        Flow-distance objective.
    """
    size = assignment.shape[0]
    total = 0.0
    for first in range(size):
        facility = assignment[first]
        for second in range(size):
            total += flows[first, second] * distances[facility, assignment[second]]
    return total


@jit(cache=True, inline="always")
def _swap_gain(
    flows: np.ndarray,
    distances: np.ndarray,
    assignment: np.ndarray,
    first: int,
    second: int,
) -> float:
    """Return the old-minus-new objective gain of swapping two positions.

    Parameters
    ----------
    flows : ndarray
        Flow matrix.
    distances : ndarray
        Distance matrix.
    assignment : ndarray
        Current permutation.
    first : int
        First position.
    second : int
        Second position.

    Returns
    -------
    float
        Objective before the swap minus the objective after it.
    """
    size = assignment.shape[0]
    before_first = assignment[first]
    before_second = assignment[second]
    delta = 0.0
    for other in range(size):
        if other == first or other == second:  # noqa: SIM109 - numba tuple membership
            continue
        other_facility = assignment[other]
        delta += flows[first, other] * (
            distances[before_second, other_facility] - distances[before_first, other_facility]
        )
        delta += flows[other, first] * (
            distances[other_facility, before_second] - distances[other_facility, before_first]
        )
        delta += flows[second, other] * (
            distances[before_first, other_facility] - distances[before_second, other_facility]
        )
        delta += flows[other, second] * (
            distances[other_facility, before_first] - distances[other_facility, before_second]
        )
    delta += flows[first, first] * (
        distances[before_second, before_second] - distances[before_first, before_first]
    )
    delta += flows[second, second] * (
        distances[before_first, before_first] - distances[before_second, before_second]
    )
    delta += flows[first, second] * (
        distances[before_second, before_first] - distances[before_first, before_second]
    )
    delta += flows[second, first] * (
        distances[before_first, before_second] - distances[before_second, before_first]
    )
    return -delta


@jit(cache=True)
def _initial_gains(
    flows: np.ndarray,
    distances: np.ndarray,
    assignment: np.ndarray,
) -> np.ndarray:
    """Build the old-minus-new gain matrix.

    Parameters
    ----------
    flows : ndarray
        Flow matrix.
    distances : ndarray
        Distance matrix.
    assignment : ndarray
        Starting permutation.

    Returns
    -------
    ndarray
        Symmetric matrix of swap gains.
    """
    size = assignment.shape[0]
    gains = np.zeros((size, size), dtype=np.float64)
    for first in range(size):
        for second in range(first + 1, size):
            gain = _swap_gain(flows, distances, assignment, first, second)
            gains[first, second] = gain
            gains[second, first] = gain
    return gains


@jit(cache=True, inline="always")
def _pair_terms(
    flows: np.ndarray,
    distances: np.ndarray,
    position: int,
    location: int,
    left: int,
    right: int,
    left_location: int,
    right_location: int,
) -> float:
    """Return the four swap-delta terms contributed by one outside position.

    Parameters
    ----------
    flows : ndarray
        Flow matrix.
    distances : ndarray
        Distance matrix.
    position : int
        Position outside the swapped pair.
    location : float
        Location currently assigned to ``position``.
    left : int
        First position of the candidate swap.
    right : int
        Second position of the candidate swap.
    left_location : float
        Location assigned to ``left``.
    right_location : float
        Location assigned to ``right``.

    Returns
    -------
    float
        Contribution of ``position`` to the objective delta.
    """
    return (
        flows[position, left]
        * (distances[location, right_location] - distances[location, left_location])
        + flows[position, right]
        * (distances[location, left_location] - distances[location, right_location])
        + flows[left, position]
        * (distances[right_location, location] - distances[left_location, location])
        + flows[right, position]
        * (distances[left_location, location] - distances[right_location, location])
    )


@jit(cache=True, inline="always")
def _general_correction(
    flows: np.ndarray,
    distances: np.ndarray,
    assignment: np.ndarray,
    first: int,
    second: int,
    old_first: int,
    old_second: int,
    left: int,
    right: int,
) -> float:
    """Return the gain correction for an asymmetric QAP swap.

    For a pair not involving the swapped positions, only the two outside terms
    change.  The correction is exact for arbitrary flow and distance matrices.

    Parameters
    ----------
    flows : ndarray
        Flow matrix.
    distances : ndarray
        Distance matrix.
    assignment : ndarray
        Permutation after the swap.
    first : int
        First swapped position.
    second : int
        Second swapped position.
    old_first : float
        Location at ``first`` before the swap.
    old_second : float
        Location at ``second`` before the swap.
    left : int
        First position of the candidate swap.
    right : int
        Second position of the candidate swap.

    Returns
    -------
    float
        Gain correction to subtract from the previous matrix entry.
    """
    left_location = assignment[left]
    right_location = assignment[right]
    new_terms = _pair_terms(
        flows,
        distances,
        first,
        old_second,
        left,
        right,
        left_location,
        right_location,
    ) + _pair_terms(
        flows,
        distances,
        second,
        old_first,
        left,
        right,
        left_location,
        right_location,
    )
    old_terms = _pair_terms(
        flows,
        distances,
        first,
        old_first,
        left,
        right,
        left_location,
        right_location,
    ) + _pair_terms(
        flows,
        distances,
        second,
        old_second,
        left,
        right,
        left_location,
        right_location,
    )
    return new_terms - old_terms


@jit(cache=True)
def _apply_swap(
    flows: np.ndarray,
    distances: np.ndarray,
    assignment: np.ndarray,
    gains: np.ndarray,
    first: int,
    second: int,
    symmetric: bool,
) -> float:
    """Apply a swap and update the gain matrix in O(n^2).

    Parameters
    ----------
    flows : ndarray
        Flow matrix.
    distances : ndarray
        Distance matrix.
    assignment : ndarray
        Permutation modified in place.
    gains : ndarray
        Gain matrix modified in place.
    first : int
        First position.
    second : int
        Second position.
    symmetric : bool
        Use the faster Taillard update when the instance is symmetric with a
        zero diagonal.

    Returns
    -------
    float
        Old-minus-new objective gain of the applied swap.
    """
    size = assignment.shape[0]
    gain = gains[first, second]
    first_facility = assignment[first]
    second_facility = assignment[second]
    assignment[first] = second_facility
    assignment[second] = first_facility
    old_gains = gains.copy()
    for left in range(size):
        for right in range(left + 1, size):
            if left == first or left == second or right == first or right == second:  # noqa: SIM109
                value = _swap_gain(flows, distances, assignment, left, right)
            elif symmetric:
                factor = (
                    flows[first, left]
                    - flows[first, right]
                    + flows[second, right]
                    - flows[second, left]
                )
                delta = (
                    distances[assignment[second], assignment[left]]
                    - distances[assignment[second], assignment[right]]
                    + distances[assignment[first], assignment[right]]
                    - distances[assignment[first], assignment[left]]
                )
                value = old_gains[left, right] - 2.0 * factor * delta
            else:
                value = old_gains[left, right] - _general_correction(
                    flows,
                    distances,
                    assignment,
                    first,
                    second,
                    first_facility,
                    second_facility,
                    left,
                    right,
                )
            gains[left, right] = value
            gains[right, left] = value
    return gain


@jit(cache=True)
def _best_descent(gains: np.ndarray) -> tuple[float, int, int]:
    """Return the best improving swap, if one exists.

    Parameters
    ----------
    gains : ndarray
        Current gain matrix.

    Returns
    -------
    tuple of float, int, int
        Gain and positions, or ``(0.0, -1, -1)`` at a local optimum.
    """
    size = gains.shape[0]
    best_gain = _EPS
    best_first = -1
    best_second = -1
    for first in range(size):
        for second in range(first + 1, size):
            value = gains[first, second]
            if value > best_gain:
                best_gain = value
                best_first = first
                best_second = second
    return best_gain, best_first, best_second


@jit(cache=True, inline="always")
def _near(first: float, second: float) -> bool:
    """Return whether two objectives are equal within floating tolerance.

    Parameters
    ----------
    first : float
        First objective.
    second : float
        Second objective.

    Returns
    -------
    bool
        ``True`` when the relative difference is at most ``1e-6``.
    """
    return abs(first - second) <= 1e-6 * max(1.0, abs(second))


@jit(cache=True)
def _best_directed(
    gains: np.ndarray,
    history: np.ndarray,
    iteration: int,
    tenure: int,
    best_objective: float,
    current: float,
) -> tuple[float, int, int]:
    """Return the best admissible directed-perturbation swap.

    The directed perturbation minimises the objective degradation among moves
    that have not been applied during the last ``tenure`` iterations.  A tabu
    move is admitted when it improves the best objective (aspiration).  Ties
    are broken uniformly at random.

    Parameters
    ----------
    gains : ndarray
        Current gain matrix.
    history : ndarray
        Iteration when each move was last applied.
    iteration : int
        Current global iteration counter.
    tenure : int
        Tabu tenure for this perturbation step.
    best_objective : float
        Best objective seen, used for aspiration.
    current : float
        Current objective.

    Returns
    -------
    tuple of float, int, int
        Gain and positions, or ``(0.0, -1, -1)`` when no move is admissible.
    """
    size = gains.shape[0]
    best_gain = -1.0e300
    count = 0
    for first in range(size):
        for second in range(first + 1, size):
            value = gains[first, second]
            candidate = current - value
            if history[first, second] + tenure >= iteration and candidate >= best_objective - _EPS:
                continue
            if value > best_gain + _EPS:
                best_gain = value
                count = 1
            elif abs(value - best_gain) <= _EPS:
                count += 1
    if count == 0:
        return 0.0, -1, -1
    target = int(np.random.randint(0, count))
    seen = 0
    for first in range(size):
        for second in range(first + 1, size):
            value = gains[first, second]
            candidate = current - value
            if history[first, second] + tenure >= iteration and candidate >= best_objective - _EPS:
                continue
            if abs(value - best_gain) <= _EPS:
                if seen == target:
                    return best_gain, first, second
                seen += 1
    return best_gain, -1, -1


@jit(cache=True)
def _least_recent(history: np.ndarray) -> tuple[int, int]:
    """Return a uniformly chosen least-recently-applied swap.

    Parameters
    ----------
    history : ndarray
        Iteration when each move was last applied.

    Returns
    -------
    tuple of int
        Positions of the chosen swap.
    """
    size = history.shape[0]
    oldest = 2**62
    count = 0
    for first in range(size):
        for second in range(first + 1, size):
            value = history[first, second]
            if value < oldest:
                oldest = value
                count = 1
            elif value == oldest:
                count += 1
    if count == 0:
        return 0, 1
    target = int(np.random.randint(0, count))
    seen = 0
    for first in range(size):
        for second in range(first + 1, size):
            if history[first, second] == oldest:
                if seen == target:
                    return first, second
                seen += 1
    return 0, 1


@jit(cache=True)
def _bls_kernel(
    flows: np.ndarray,
    distances: np.ndarray,
    assignment: np.ndarray,
    seed: int,
    max_moves: int,
    patience: int,
    initial_strength: int,
    max_strength: int,
    threshold: int,
    min_tenure: int,
    max_tenure: int,
    directed_floor: float,
    recency_share: float,
    symmetric: bool,
    history: np.ndarray,
) -> tuple[
    float,
    np.ndarray,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    float,
]:
    """Run BLS on symmetric zero-diagonal matrices.

    Parameters
    ----------
    flows : ndarray
        Flow matrix.
    distances : ndarray
        Distance matrix.
    assignment : ndarray
        Starting permutation.
    seed : int
        Random seed for perturbations.
    max_moves : int
        Applied-swap cap.
    patience : int
        Non-improving applied-swap patience.
    initial_strength : int
        Default jump magnitude ``L0``.
    max_strength : int
        Maximal jump magnitude ``LMax``.
    threshold : int
        Non-improving local-optimum threshold ``T``.
    min_tenure : int
        Lower bound of the move tabu tenure.
    max_tenure : int
        Upper bound of the move tabu tenure.
    directed_floor : float
        Smallest directed-perturbation probability ``P0``.
    recency_share : float
        Recency share ``Q`` among non-directed perturbations.
    symmetric : bool
        Use the fast Taillard gain update on symmetric zero-diagonal instances.
    history : ndarray
        Preallocated buffer for best-objective history.

    Returns
    -------
    tuple
        Best objective, best permutation, counters, stopping code, history
        length, final jump magnitude, and the initial objective.
    """
    size = assignment.shape[0]
    pair_count = size * (size - 1) // 2
    np.random.seed(seed)
    gains = _initial_gains(flows, distances, assignment)
    initial_objective = _objective(flows, distances, assignment)
    current = initial_objective
    best_objective = current
    best = assignment.copy()
    last_move = np.full((size, size), -1_000_000_000, dtype=np.int64)
    previous_local = current
    strength = initial_strength
    omega = 0
    iteration = 0
    evaluations = pair_count
    descent_moves = 0
    perturbation_moves = 0
    local_optima = 0
    random_perturbations = 0
    recency_perturbations = 0
    directed_perturbations = 0
    strong_perturbations = 0
    first_cycle = True
    last_improvement = 0
    history[0] = current
    history_len = 1
    stop_reason = 0
    stopped = False
    while iteration < max_moves and not stopped:
        while iteration < max_moves:
            gain, first, second = _best_descent(gains)
            if first < 0:
                break
            _apply_swap(flows, distances, assignment, gains, first, second, symmetric)
            current -= gain
            iteration += 1
            last_move[first, second] = iteration
            last_move[second, first] = iteration
            descent_moves += 1
            evaluations += pair_count
            if iteration - last_improvement >= patience:
                stop_reason = 1
                stopped = True
                break
        if stopped or iteration >= max_moves:
            break
        local_optima += 1
        if current < best_objective - _EPS:
            best_objective = current
            best = assignment.copy()
            last_improvement = iteration
            omega = 0
            if history_len < history.shape[0]:
                history[history_len] = best_objective
                history_len += 1
        elif not first_cycle and not _near(current, previous_local):
            omega += 1
        if first_cycle:
            first_cycle = False
            strength = initial_strength
        elif omega > threshold:
            strength = max_strength
            omega = 0
            strong_perturbations += 1
        elif _near(current, previous_local):
            strength = min(strength + 1, size)
        else:
            strength = initial_strength
        previous_local = current
        probability = max(np.exp(-omega / threshold), directed_floor)
        draw = np.random.random()
        if draw < probability:
            directed_perturbations += 1
            kind = 0
        elif draw < probability + (1.0 - probability) * recency_share:
            recency_perturbations += 1
            kind = 1
        else:
            random_perturbations += 1
            kind = 2
        for _ in range(strength):
            if iteration >= max_moves:
                break
            if kind == 0:
                tenure = int(np.random.randint(min_tenure, max_tenure + 1))
                gain, first, second = _best_directed(
                    gains,
                    last_move,
                    iteration,
                    tenure,
                    best_objective,
                    current,
                )
                if first < 0:
                    first = int(np.random.randint(0, size))
                    second = int(np.random.randint(0, size - 1))
                    if second >= first:
                        second += 1
            elif kind == 1:
                first, second = _least_recent(last_move)
            else:
                first = int(np.random.randint(0, size))
                second = int(np.random.randint(0, size - 1))
                if second >= first:
                    second += 1
            gain = _apply_swap(flows, distances, assignment, gains, first, second, symmetric)
            current -= gain
            iteration += 1
            last_move[first, second] = iteration
            last_move[second, first] = iteration
            perturbation_moves += 1
            evaluations += pair_count
            if current < best_objective - _EPS:
                best_objective = current
                best = assignment.copy()
                last_improvement = iteration
                omega = 0
                if history_len < history.shape[0]:
                    history[history_len] = best_objective
                    history_len += 1
            if iteration - last_improvement >= patience:
                stop_reason = 1
                stopped = True
                break
        if stopped:
            break
    return (
        best_objective,
        best,
        iteration,
        evaluations,
        descent_moves,
        perturbation_moves,
        local_optima,
        random_perturbations,
        recency_perturbations,
        directed_perturbations,
        strong_perturbations,
        stop_reason,
        history_len,
        strength,
        initial_objective,
    )


def _swap_delta(
    problem: QuadraticAssignment,
    permutation: list[int],
    first: int,
    second: int,
) -> float:
    """Return the exact QAP objective delta for swapping two positions.

    Parameters
    ----------
    problem : QuadraticAssignment
        QAP instance.
    permutation : list of int
        Current permutation.
    first : int
        First position.
    second : int
        Second position.

    Returns
    -------
    float
        Objective after the swap minus the objective before it.
    """
    flows = problem.flows
    distances = problem.distances
    size = len(permutation)
    before_first = permutation[first]
    before_second = permutation[second]
    delta = 0.0
    for other in range(size):
        if other == first or other == second:  # noqa: SIM109 - numba tuple membership
            continue
        other_facility = permutation[other]
        delta += flows[first][other] * (
            distances[before_second][other_facility] - distances[before_first][other_facility]
        )
        delta += flows[other][first] * (
            distances[other_facility][before_second] - distances[other_facility][before_first]
        )
        delta += flows[second][other] * (
            distances[before_first][other_facility] - distances[before_second][other_facility]
        )
        delta += flows[other][second] * (
            distances[other_facility][before_first] - distances[other_facility][before_second]
        )
    delta += flows[first][first] * (
        distances[before_second][before_second] - distances[before_first][before_first]
    )
    delta += flows[second][second] * (
        distances[before_first][before_first] - distances[before_second][before_second]
    )
    delta += flows[first][second] * (
        distances[before_second][before_first] - distances[before_first][before_second]
    )
    delta += flows[second][first] * (
        distances[before_first][before_second] - distances[before_second][before_first]
    )
    return delta


def _delta_matrix(
    problem: QuadraticAssignment,
    permutation: list[int],
) -> list[list[float]]:
    """Recompute the full old-minus-new gain matrix.

    Parameters
    ----------
    problem : QuadraticAssignment
        QAP instance.
    permutation : list of int
        Current permutation.

    Returns
    -------
    list of list of float
        Symmetric gain matrix.
    """
    size = len(permutation)
    gains = [[0.0 for _ in range(size)] for _ in range(size)]
    for first in range(size):
        for second in range(first + 1, size):
            gain = -_swap_delta(problem, permutation, first, second)
            gains[first][second] = gain
            gains[second][first] = gain
    return gains


def _run_reference(
    problem: QuadraticAssignment,
    config: QapBlsConfig,
    permutation: list[int],
    initial_strength: int,
    max_strength: int,
    threshold: int,
    min_tenure: int,
    max_tenure: int,
    directed_floor: float,
    recency_share: float,
    history: np.ndarray,
) -> tuple[
    float,
    list[int],
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    float,
]:
    """Run BLS with exact O(n^3) gain recomputation.

    This path exists so the algorithm can be audited and exercised without
    Numba.  It is too slow for the serious panel and is never used for the
    committed evidence.

    Parameters
    ----------
    problem : QuadraticAssignment
        QAP instance.
    config : QapBlsConfig
        Search settings.
    permutation : list of int
        Starting permutation.
    initial_strength : int
        Default jump magnitude ``L0``.
    max_strength : int
        Maximal jump magnitude ``LMax``.
    threshold : int
        Non-improving local-optimum threshold ``T``.
    min_tenure : int
        Lower bound of the move tabu tenure.
    max_tenure : int
        Upper bound of the move tabu tenure.
    directed_floor : float
        Smallest directed-perturbation probability ``P0``.
    recency_share : float
        Recency share ``Q`` among non-directed perturbations.
    history : ndarray
        Preallocated buffer for best-objective history.

    Returns
    -------
    tuple
        The same fields as :func:`_bls_kernel`.
    """
    rng = random.Random(config.seed)
    size = len(permutation)
    current = problem.evaluate(dict(enumerate(permutation))).objective
    initial_objective = current
    gains = _delta_matrix(problem, permutation)
    best = permutation[:]
    best_objective = current
    last_move = [[-1_000_000_000] * size for _ in range(size)]
    previous_local = current
    strength = initial_strength
    omega = 0
    iteration = 0
    pair_count = size * (size - 1) // 2
    evaluations = pair_count
    descent_moves = 0
    perturbation_moves = 0
    local_optima = 0
    random_perturbations = 0
    recency_perturbations = 0
    directed_perturbations = 0
    strong_perturbations = 0
    first_cycle = True
    last_improvement = 0
    history[0] = current
    history_len = 1
    stop_reason = 0
    stopped = False

    def near(first: float, second: float) -> bool:
        return abs(first - second) <= 1e-6 * max(1.0, abs(second))

    def record() -> None:
        nonlocal best_objective, last_improvement, history_len, omega
        best_objective = current
        last_improvement = iteration
        omega = 0
        if history_len < history.shape[0]:
            history[history_len] = best_objective
            history_len += 1

    def apply(first: int, second: int) -> float:
        nonlocal gains
        gain = gains[first][second]
        permutation[first], permutation[second] = permutation[second], permutation[first]
        gains = _delta_matrix(problem, permutation)
        return gain

    while iteration < config.max_moves and not stopped:
        while iteration < config.max_moves:
            best_gain = _EPS
            best_first = -1
            best_second = -1
            for first in range(size):
                for second in range(first + 1, size):
                    value = gains[first][second]
                    if value > best_gain:
                        best_gain = value
                        best_first = first
                        best_second = second
            if best_first < 0:
                break
            current -= apply(best_first, best_second)
            iteration += 1
            last_move[best_first][best_second] = iteration
            last_move[best_second][best_first] = iteration
            descent_moves += 1
            evaluations += pair_count
            if iteration - last_improvement >= config.patience:
                stop_reason = 1
                stopped = True
                break
        if stopped or iteration >= config.max_moves:
            break
        local_optima += 1
        if current < best_objective - _EPS:
            best = permutation[:]
            record()
        elif not first_cycle and not near(current, previous_local):
            omega += 1
        if first_cycle:
            first_cycle = False
            strength = initial_strength
        elif omega > threshold:
            strength = max_strength
            omega = 0
            strong_perturbations += 1
        elif near(current, previous_local):
            strength = min(strength + 1, size)
        else:
            strength = initial_strength
        previous_local = current
        probability = max(math.exp(-omega / threshold), directed_floor)
        draw = rng.random()
        if draw < probability:
            directed_perturbations += 1
            kind = 0
        elif draw < probability + (1.0 - probability) * recency_share:
            recency_perturbations += 1
            kind = 1
        else:
            random_perturbations += 1
            kind = 2
        for _ in range(strength):
            if iteration >= config.max_moves:
                break
            if kind == 0:
                tenure = rng.randint(min_tenure, max_tenure)
                best_gain = -1.0e300
                best_first = -1
                best_second = -1
                ties = 0
                for first in range(size):
                    for second in range(first + 1, size):
                        value = gains[first][second]
                        candidate = current - value
                        if (
                            last_move[first][second] + tenure >= iteration
                            and candidate >= best_objective - _EPS
                        ):
                            continue
                        if value > best_gain + _EPS:
                            best_gain = value
                            best_first = first
                            best_second = second
                            ties = 1
                        elif abs(value - best_gain) <= _EPS:
                            ties += 1
                            if rng.randrange(ties) == 0:
                                best_first = first
                                best_second = second
                if best_first < 0:
                    best_first = rng.randrange(size)
                    best_second = rng.randrange(size - 1)
                    if best_second >= best_first:
                        best_second += 1
            elif kind == 1:
                oldest = 2**62
                best_first = -1
                best_second = -1
                ties = 0
                for first in range(size):
                    for second in range(first + 1, size):
                        value = last_move[first][second]
                        if value < oldest:
                            oldest = value
                            best_first = first
                            best_second = second
                            ties = 1
                        elif value == oldest:
                            ties += 1
                            if rng.randrange(ties) == 0:
                                best_first = first
                                best_second = second
                if best_first < 0:
                    best_first = 0
                    best_second = 1
            else:
                best_first = rng.randrange(size)
                best_second = rng.randrange(size - 1)
                if best_second >= best_first:
                    best_second += 1
            current -= apply(best_first, best_second)
            iteration += 1
            last_move[best_first][best_second] = iteration
            last_move[best_second][best_first] = iteration
            perturbation_moves += 1
            evaluations += pair_count
            if current < best_objective - _EPS:
                best = permutation[:]
                record()
            if iteration - last_improvement >= config.patience:
                stop_reason = 1
                stopped = True
                break
        if stopped:
            break
    return (
        best_objective,
        best,
        iteration,
        evaluations,
        descent_moves,
        perturbation_moves,
        local_optima,
        random_perturbations,
        recency_perturbations,
        directed_perturbations,
        strong_perturbations,
        stop_reason,
        history_len,
        strength,
        initial_objective,
    )


def _resolve_parameters(
    size: int,
    config: QapBlsConfig,
) -> tuple[int, int, int, int]:
    """Resolve optional BLS parameters for one instance.

    Parameters
    ----------
    size : int
        Number of locations.
    config : QapBlsConfig
        Search settings.

    Returns
    -------
    tuple of int
        Initial jump magnitude ``L0``, maximal jump magnitude ``LMax``, and
        the lower and upper move-tabu tenures.
    """
    initial = (
        config.initial_strength
        if config.initial_strength is not None
        else max(2, round(0.15 * size))
    )
    if config.max_strength is not None:
        maximum = config.max_strength
    else:
        draw = random.Random(config.seed)
        lower = max(initial + 1, round(0.4 * size))
        upper = max(lower, round(0.6 * size))
        maximum = draw.randint(lower, upper)
    min_tenure = config.min_tenure if config.min_tenure is not None else max(2, round(0.9 * size))
    max_tenure = (
        config.max_tenure if config.max_tenure is not None else max(min_tenure, round(1.1 * size))
    )
    return initial, maximum, min_tenure, max_tenure


def run_qap_bls(
    problem: QuadraticAssignment,
    config: QapBlsConfig,
    initial: Mapping[int, int] | None = None,
) -> QapBlsResult:
    """Run Breakout Local Search over QAP facility swaps.

    Parameters
    ----------
    problem : QuadraticAssignment
        QAP instance.
    config : QapBlsConfig
        Search settings.
    initial : mapping of int to int or None, optional
        Starting assignment.  Defaults to the adapter's identity assignment,
        matching the robust tabu panel.

    Returns
    -------
    QapBlsResult
        Best assignment, adapter-replayed objective, and stop evidence.

    Raises
    ------
    RuntimeError
        When the delta-tracked objective disagrees with the adapter's exact
        evaluation.
    """
    size = problem.variable_count
    starting = initial if initial is not None else problem.initial_assignment()
    start_evaluation = problem.evaluate(starting)
    permutation = [starting[index] for index in range(size)]
    initial_strength, max_strength, min_tenure, max_tenure = _resolve_parameters(size, config)
    history = np.zeros(_HISTORY_CAP, dtype=np.float64)
    if NUMBA_AVAILABLE:
        flows = np.asarray(problem.flows, dtype=np.float64)
        distances = np.asarray(problem.distances, dtype=np.float64)
        outcome = _bls_kernel(
            flows,
            distances,
            np.asarray(permutation, dtype=np.int64),
            config.seed,
            config.max_moves,
            config.patience,
            initial_strength,
            max_strength,
            config.threshold,
            min_tenure,
            max_tenure,
            config.directed_probability_floor,
            config.recency_share,
            _is_symmetric_zero_diagonal(problem),
            history,
        )
        engine = "numba"
    else:
        outcome = _run_reference(
            problem,
            config,
            permutation,
            initial_strength,
            max_strength,
            config.threshold,
            min_tenure,
            max_tenure,
            config.directed_probability_floor,
            config.recency_share,
            history,
        )
        engine = "reference"
    (
        tracked_objective,
        best,
        moves,
        evaluations,
        descent_moves,
        perturbation_moves,
        local_optima,
        random_perturbations,
        recency_perturbations,
        directed_perturbations,
        strong_perturbations,
        stop_reason,
        history_len,
        strength,
        initial_objective,
    ) = outcome
    tolerance = 1e-6 * max(1.0, abs(start_evaluation.objective))
    if abs(initial_objective - start_evaluation.objective) > tolerance:
        raise RuntimeError(
            "delta objective disagrees with the adapter at the initial assignment: "
            f"{initial_objective} != {start_evaluation.objective}"
        )
    assignment = {index: int(value) for index, value in enumerate(best)}
    final = problem.evaluate(assignment)
    if abs(final.objective - tracked_objective) > tolerance:
        raise RuntimeError(
            "delta objective disagrees with the adapter at the incumbent: "
            f"{tracked_objective} != {final.objective}"
        )
    return QapBlsResult(
        assignment=assignment,
        objective=final.objective,
        moves=int(moves),
        evaluations=int(evaluations),
        descent_moves=int(descent_moves),
        perturbation_moves=int(perturbation_moves),
        local_optima=int(local_optima),
        random_perturbations=int(random_perturbations),
        recency_perturbations=int(recency_perturbations),
        directed_perturbations=int(directed_perturbations),
        strong_perturbations=int(strong_perturbations),
        final_strength=int(strength),
        initial_strength_used=int(initial_strength),
        max_strength_used=int(max_strength),
        min_tenure_used=int(min_tenure),
        max_tenure_used=int(max_tenure),
        stop_reason="patience" if stop_reason == 1 else "max_moves",
        engine=engine,
        history=tuple(float(value) for value in history[:history_len]),
    )
