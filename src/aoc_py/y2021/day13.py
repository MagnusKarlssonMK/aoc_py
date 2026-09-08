"""
2021 day 13 - Transparent Origami
"""

from typing import override

from aoc_py.util.grid import Grid
from aoc_py.util.point import Point


class InputData:
    def __init__(self, rawstr: str) -> None:
        points, foldings = rawstr.split("\n\n")
        self.__dots = {Point.from_str(ps) for ps in points.splitlines()}
        self.__foldings = [
            (left.split()[2], int(right))
            for left, right in [line.split("=") for line in foldings.splitlines()]
        ]
        self.__height = -1
        self.__width = -1

    def __fold(self, index: int) -> None:
        axis, value = self.__foldings[index]
        new_dots: set[Point] = set()
        if axis == "x":
            for d in self.__dots:
                if d.x > value:
                    new_dots.add(Point(2 * value - d.x, d.y))
                else:
                    new_dots.add(d)
            self.__width = value
        else:  # y
            for d in self.__dots:
                if d.y > value:
                    new_dots.add(Point(d.x, 2 * value - d.y))
                else:
                    new_dots.add(d)
            self.__height = value
        self.__dots = new_dots

    def fold_and_get_dots(self) -> int:
        p1 = -1
        for idx, _ in enumerate(self.__foldings):
            self.__fold(idx)
            if idx == 0:
                p1 = len(self.__dots)
        return p1

    @override
    def __str__(self):
        grid = Grid.new(self.__width, self.__height, ".")
        for d in self.__dots:
            grid.set_point(d, "#")
        return str(grid)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    r1 = p.fold_and_get_dots()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = f"\n{p}"

    return p1, p2
