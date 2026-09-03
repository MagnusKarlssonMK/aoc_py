"""
2025 day 07 - Laboratories
"""

from typing import Final

from aoc_py.util.grid import Grid
from aoc_py.util.point import Point

START: Final = "S"
SPLITTER: Final = "^"


class InputData:
    def __init__(self, s: str) -> None:
        self.__grid = Grid(s)

    def solve(self) -> tuple[int, int]:
        split_count = 0
        x_counts = [
            1 if self.__grid.elements[x] == START else 0
            for x in range(self.__grid.x_max)
        ]

        for y in range(1, self.__grid.y_max):
            new_x_counts = [0 for _ in range(self.__grid.x_max)]
            for x in [i for i in range(self.__grid.x_max) if x_counts[i] > 0]:
                if (c := self.__grid.get_element(Point(x, y))) != "":
                    if c == SPLITTER:
                        split_count += 1
                        new_x_counts[x - 1] += x_counts[x]
                        new_x_counts[x + 1] += x_counts[x]
                    else:
                        new_x_counts[x] += x_counts[x]
            x_counts = new_x_counts
        return split_count, sum(x_counts)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.solve()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
