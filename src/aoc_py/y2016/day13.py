"""
2016 day 13 - A Maze of Twisty Little Cubicles

Simple BFS solution, with the wall/open test and neighbor generation implemented as free functions.
Parts 1 & 2 share the same BFS walk; they only differ in the stop condition: Part 1 searches for a
specific target node, while Part 2 counts all nodes reachable within a step limit.
"""

from collections import deque
from collections.abc import Generator

from aoc_py.util.point import Directions, Point

TARGET = Point(31, 39)
STEP_LIMIT = 50


def is_open(x: int, y: int, keyval: int) -> bool:
    """Returns True when (x, y) is open space for the given favorite number."""
    val = (x * x) + (3 * x) + (2 * x * y) + y + (y * y) + keyval
    return val.bit_count() % 2 == 0


def get_neighbors(p: Point, keyval: int) -> Generator[Point]:
    """Generates the straight-line neighbors of p that are open space and inside the building."""
    for n in (p + d for d in Directions.NEIGHBORS_STRAIGHT):
        if n.x >= 0 and n.y >= 0 and is_open(n.x, n.y, keyval):
            yield n


class InputData:
    def __init__(self, s: str) -> None:
        self.__favorite_nbr = int(s)

    def _walk(self, steplimit: int | None) -> Generator[tuple[Point, int]]:
        """BFS from (1, 1), yielding each point once together with its shortest distance."""
        start = Point(1, 1)
        seen: set[Point] = {start}
        queue: deque[tuple[Point, int]] = deque([(start, 0)])
        while queue:
            currentpoint, steps = queue.popleft()
            yield currentpoint, steps
            if steplimit is not None and steps >= steplimit:
                continue
            for p in get_neighbors(currentpoint, self.__favorite_nbr):
                if p not in seen:
                    seen.add(p)
                    queue.append((p, steps + 1))

    def get_shortest_path(self, targetpoint: Point) -> int:
        """Returns the fewest number of steps from (1, 1) to targetpoint."""
        for currentpoint, steps in self._walk(None):
            if currentpoint == targetpoint:
                return steps
        return -1

    def get_reachable_count(self, steplimit: int) -> int:
        """Returns the number of distinct points reachable from (1, 1) within steplimit steps."""
        return sum(1 for _ in self._walk(steplimit))


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_shortest_path(TARGET))
    if part in (None, 2):
        p2 = str(p.get_reachable_count(STEP_LIMIT))

    return p1, p2
