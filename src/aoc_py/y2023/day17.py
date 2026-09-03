"""
2023 day 17 - Clumsy Crucible

Sort of an A* solution (using the manhattan distance as heuristic) but with a bit more complicated state, since it also
needs to track direction. Certainly not fast, but gets the job done.
"""

from dataclasses import dataclass
from heapq import heappop, heappush

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point


@dataclass(frozen=True)
class State:
    pos: Point
    direction: Point
    steps: int

    def __lt__(self, other: State) -> bool:
        return self.steps < other.steps


class InputData:
    def __init__(self, s: str) -> None:
        self.__grid = Grid(s)

    def get_shortestpath(self, minsteps: int = 0, maxsteps: int = 3) -> int:
        state = State(Directions.ORIGIN, Directions.DOWN, 0)
        target = self.__grid.get_point(len(self.__grid.elements) - 1)
        visited = {}
        queue: list[tuple[int, int, State]] = []
        heappush(queue, (Directions.ORIGIN.manhattan(target), 0, state))
        state = State(Directions.ORIGIN, Directions.RIGHT, 0)
        heappush(queue, (Directions.ORIGIN.manhattan(target), 0, state))
        while queue:
            _, heat, state = heappop(queue)
            if state.pos == target and state.steps >= minsteps:
                return heat
            neighborstates: list[State] = []
            if state.steps >= minsteps:
                ccw = state.direction.rotate_left()
                neighborstates.append(State(state.pos + ccw, ccw, 1))
                cw = state.direction.rotate_right()
                neighborstates.append(State(state.pos + cw, cw, 1))
            if state.steps < maxsteps:
                neighborstates.append(
                    State(state.pos + state.direction, state.direction, state.steps + 1)
                )
            for ns in neighborstates:
                if (newheat_c := self.__grid.get_element(ns.pos)) != "":
                    newheat = int(newheat_c) + heat
                    if ns not in visited or newheat < visited[ns]:
                        visited[ns] = newheat
                        heappush(
                            queue, (newheat + ns.pos.manhattan(target), newheat, ns)
                        )
        return -1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_shortestpath())
    if part in (None, 2):
        p2 = str(p.get_shortestpath(4, 10))

    return p1, p2
