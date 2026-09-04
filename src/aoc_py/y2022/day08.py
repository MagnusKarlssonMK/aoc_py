"""
2022 day 8 - Treetop Tree House
"""

import math
from collections.abc import Generator, Iterable

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point


class InputData:
    def __init__(self, s: str) -> None:
        self.__grid = Grid(s)
        self.__grid_scores = [
            [
                {d: -1 for d in Directions.NEIGHBORS_STRAIGHT}
                for _ in range(self.__grid.x_max)
            ]
            for _ in range(self.__grid.y_max)
        ]

    def get_p1(self) -> int:
        visible: set[Point] = set()
        for y in range(self.__grid.y_max):
            # From left:
            [
                visible.add(tree)
                for tree in self.__generatevisibletrees(-1, y, range(self.__grid.x_max))
            ]
            # From right:
            [
                visible.add(tree)
                for tree in self.__generatevisibletrees(
                    -1, y, reversed(range(self.__grid.x_max))
                )
            ]
        for x in range(self.__grid.x_max):
            # From above
            [
                visible.add(tree)
                for tree in self.__generatevisibletrees(x, -1, range(self.__grid.y_max))
            ]
            # From below
            [
                visible.add(tree)
                for tree in self.__generatevisibletrees(
                    x, -1, reversed(range(self.__grid.y_max))
                )
            ]
        return len(visible)

    def __generatevisibletrees(
        self, x: int, y: int, iterable: Iterable[int]
    ) -> Generator[Point]:
        tallest: int = -1
        for i in iterable:
            next_point = Point(x, i) if y == -1 else Point(i, y)
            value = int(self.__grid.get_element(next_point))
            if value > tallest:
                tallest = value
                yield next_point
                if tallest == 9:
                    break

    def __setdirectionscores(
        self, x: int, y: int, direction: Point, iterable: Iterable[int]
    ) -> None:
        scorelist = [0 for _ in range(10)]
        for i in iterable:
            next_point = Point(x, i) if y == -1 else Point(i, y)
            value = int(self.__grid.get_element(next_point))
            self.__grid_scores[next_point.y][next_point.x][direction] = scorelist[value]
            for j in range(10):
                scorelist[j] = (scorelist[j] + 1) if j > value else 1

    def get_p2(self) -> int:
        currentmax = 0
        for r in range(self.__grid.y_max):
            self.__setdirectionscores(-1, r, Directions.LEFT, range(self.__grid.x_max))
            self.__setdirectionscores(
                -1, r, Directions.RIGHT, reversed(range(self.__grid.x_max))
            )
        for c in range(self.__grid.x_max):
            self.__setdirectionscores(c, -1, Directions.UP, range(self.__grid.y_max))
            self.__setdirectionscores(
                c, -1, Directions.DOWN, reversed(range(self.__grid.y_max))
            )
        for r in range(self.__grid.y_max):
            for c in range(self.__grid.x_max):
                score = math.prod(self.__grid_scores[r][c].values())
                currentmax = max(score, currentmax)
        return currentmax


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
