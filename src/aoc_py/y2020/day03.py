"""
Store the tree map in a grid class, with a method to count the number of trees encountered for a certain input step
pattern. When checking the columns, take the column coordinate of the location mod number of columns in the grid,
in order to handle the expanding grid sideways.
"""

import math

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point


class InputData:
    def __init__(self, s: str) -> None:
        self.__grid = Grid(s)

    def __counttrees(self, step: Point) -> int:
        pos = Directions.ORIGIN
        count = 0
        while (c := self.__grid.get_element(pos)) != "":
            if c == "#":
                count += 1
            pos += step
            pos = Point(pos.x % self.__grid.x_max, pos.y)
        return count

    def get_p1(self) -> int:
        return self.__counttrees(Point(3, 1))

    def get_p2(self) -> int:
        return math.prod(
            [
                self.__counttrees(s)
                for s in (
                    Point(1, 1),
                    Point(3, 1),
                    Point(5, 1),
                    Point(7, 1),
                    Point(1, 2),
                )
            ]
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
