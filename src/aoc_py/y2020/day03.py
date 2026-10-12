"""
2020 day 3 - Toboggan Trajectory

Store the map in a Grid and walk a given step pattern, wrapping the column coordinate with
modulo the number of columns to handle the horizontally repeating map.
"""

import math

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__grid = Grid(rawstr)

    def __count_trees(self, step: Point) -> int:
        pos = Directions.ORIGIN
        count = 0
        while (c := self.__grid.get_element(pos)) != "":
            if c == "#":
                count += 1
            pos += step
            pos = Point(pos.x % self.__grid.x_max, pos.y)
        return count

    def get_p1(self) -> int:
        return self.__count_trees(Point(3, 1))

    def get_p2(self) -> int:
        return math.prod(
            self.__count_trees(step)
            for step in (
                Point(1, 1),
                Point(3, 1),
                Point(5, 1),
                Point(7, 1),
                Point(1, 2),
            )
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
