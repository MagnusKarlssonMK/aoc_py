"""
2023 day 21 - Step Counter

Part 1: Stores the rocks in a set, and finds reachable tiles within the step count limit using BFS, then count
only the ones that have odd/even number of steps (depending on whether the count limit is odd/even).
Part 2: Solves it with three-point-formula to determine the coefficients in a quadratic formula, and calculate the
answer from that.
"""

from collections.abc import Generator
from typing import Final

from aoc_py.util.point import Directions, Point

STEPS: Final = 64  # Number of steps the gardener takes in part 1
PRESSES: Final = 26501365  # Number of times the button is pressed in part 2


class InputData:
    def __init__(self, rawstr: str) -> None:
        lines = rawstr.splitlines()
        self.__height = len(lines)
        self.__width = len(lines[0])
        self.__start = Point(-1, -1)
        self.__rocks: set[Point] = set()
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == "S":
                    self.__start = Point(x, y)
                elif c == "#":
                    self.__rocks.add(Point(x, y))

    def __get_neighbors(self, p: Point, expand: bool) -> Generator[Point]:
        for neighbor in [p + d for d in Directions.NEIGHBORS_STRAIGHT]:
            if expand:
                # The garden repeats infinitely in all directions, so rocks are looked up modulo the grid size
                probe = Point(neighbor.x % self.__width, neighbor.y % self.__height)
            else:
                probe = neighbor
            if probe not in self.__rocks:
                yield neighbor

    def get_reachable(self, steps: int, expand: bool = False) -> int:
        """Counts the tiles reachable within `steps`, keeping only the ones whose step count has the same
        parity as `steps`, since the gardener lands on every other tile."""
        seen: set[Point] = set()
        reachable: set[Point] = set()
        bfs_queue = [(self.__start, 0)]
        while bfs_queue:
            u, count = bfs_queue.pop(0)
            if count <= steps:
                if count % 2 == steps % 2:
                    reachable.add(u)
                for v in self.__get_neighbors(u, expand):
                    if v not in seen:
                        bfs_queue.append((v, count + 1))
                        seen.add(v)
        return len(reachable)

    def get_p1(self) -> int:
        return self.get_reachable(STEPS)

    def get_p2(self) -> int:
        # The tile count is a quadratic in the number of times the garden repeats, so fit y = a*x^2 + b*x + c
        # to the counts at three step counts, one grid height apart.
        height = self.__height
        n = (height - 1) // 2
        y = [self.get_reachable(n + (height * i), True) for i in range(3)]
        c = y[0]
        b = ((4 * y[1]) - (3 * y[0]) - y[2]) // 2
        a = y[1] - y[0] - b
        x = (PRESSES - n) // height
        return a * x**2 + b * x + c


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
