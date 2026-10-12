"""
2025 day 7 - Laboratories

Solve both parts simultaneously with a running counter per column:

* Start with a counter vector for the first row, zero everywhere except the start point ('S'),
  which is one.
* Move top-to-bottom; for every row build a new counter vector where each column either keeps
  its count (no splitter) or passes it to the two neighbours (splitter). Count every split.
* After the last row, part 1 is the number of splits and part 2 is the sum of the counters.
"""

from typing import Final

from aoc_py.util.grid import Grid
from aoc_py.util.point import Point

START: Final = "S"
SPLITTER: Final = "^"


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__grid: Grid = Grid(rawstr)

    def solve(self) -> tuple[int, int]:
        split_count = 0
        x_counts = [
            1 if self.__grid.elements[x] == START else 0
            for x in range(self.__grid.x_max)
        ]

        for y in range(1, self.__grid.y_max):
            new_x_counts = [0] * self.__grid.x_max
            for x, count in enumerate(x_counts):
                if count == 0:
                    continue
                if (c := self.__grid.get_element(Point(x, y))) != "":
                    if c == SPLITTER:
                        split_count += 1
                        new_x_counts[x - 1] += count
                        new_x_counts[x + 1] += count
                    else:
                        new_x_counts[x] += count
            x_counts = new_x_counts
        return split_count, sum(x_counts)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.solve()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
