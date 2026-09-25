"""
2018 day 18 - Settlers of The North Pole

Game of life with three states instead of two, kind of.
Store the grid in a dict with the state for each coordinate and update according to the rules for each passing minute.
For part 2 we obviously don't want to brute force a trillion minutes, so instead try to find a cycle. The grid value
appears not to be unique enough for all inputs to use as hash for the seen states and look for repetitions based on
that, so instead generate a sorted tuple of the grid to use as key.
"""

from collections import Counter
from enum import Enum

from aoc_py.util.point import Directions, Point


class State(Enum):
    OPEN = "."
    TREES = "|"
    LUMBERYARD = "#"


class InputData:
    P1_TIME = 10
    P2_TIME = 1_000_000_000

    def __init__(self, rawstr: str) -> None:
        self.__grid: dict[Point, State] = {}
        for y, line in enumerate(rawstr.splitlines()):
            for x, c in enumerate(line):
                self.__grid[Point(x, y)] = State(c)

    def __step_minute(self) -> dict[Point, State]:
        result: dict[Point, State] = {}
        for point in self.__grid:
            surrounding = Counter(
                [
                    self.__grid[s]
                    for s in [point + d for d in Directions.NEIGHBORS_ALL]
                    if s in self.__grid
                ]
            )
            newstate = self.__grid[point]
            match self.__grid[point]:
                case State.OPEN:
                    if surrounding[State.TREES] >= 3:
                        newstate = State.TREES
                case State.TREES:
                    if surrounding[State.LUMBERYARD] >= 3:
                        newstate = State.LUMBERYARD
                case State.LUMBERYARD:
                    if (
                        surrounding[State.LUMBERYARD] == 0
                        or surrounding[State.TREES] == 0
                    ):
                        newstate = State.OPEN
            result[point] = newstate
        return result

    def __get_value(self) -> int:
        nbrs = Counter(self.__grid.values())
        return nbrs[State.TREES] * nbrs[State.LUMBERYARD]

    def __get_keyval(self):
        return tuple(sorted(self.__grid.items()))

    def get_total_resource_value(self) -> tuple[int, int]:
        p1 = p2 = 0
        time = 0
        seen = {}
        while True:
            time += 1
            self.__grid = self.__step_minute()
            value = self.__get_value()
            keyval = self.__get_keyval()
            if time == InputData.P1_TIME:
                p1 = value
            if keyval in seen:
                cycle = time - seen[keyval][0]
                offset = time - cycle
                p2_time = offset + ((InputData.P2_TIME - offset) % cycle)
                for v in seen:
                    if seen[v][0] == p2_time:
                        p2 = seen[v][1]
                        break
                break
            else:
                seen[keyval] = time, value
        return p1, p2


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_total_resource_value()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
