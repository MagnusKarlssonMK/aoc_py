"""
2023 day 11 - Cosmic Expansion

Stores the coordinates of galaxies in a Space class, and also generates lists of empty rows and columns. For Part 1,
the distance is then calculated with the manhattan distance between each pair of galaxies, and for each pair also
checking the number of empty rows/columns between them. Since the grid input doesn't change between Part 1 & 2 other
than the scaling of empty space, we can calculate the answers to both part 1 and 2 at the same time by not evaluating
the value of empty space until the last step everything has been assembled.
"""

from dataclasses import dataclass
from itertools import combinations

from aoc_py.util.point import Point


@dataclass(frozen=True)
class PointX(Point):
    def get_x_ranges(self, other: PointX) -> tuple[int, int]:
        return min(self.x, other.x), max(self.x, other.x)

    def get_y_ranges(self, other: PointX) -> tuple[int, int]:
        return min(self.y, other.y), max(self.y, other.y)


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__galaxies: list[PointX] = [
            PointX(x, y)
            for y, line in enumerate(rawstr.splitlines())
            for x, c in enumerate(line)
            if c == "#"
        ]

    def get_distance_sum(
        self, small_exp_rate: int = 2, large_exp_rate: int = 1_000_000
    ) -> tuple[int, int]:
        total_steps = 0
        total_emptyspace = 0
        x_occupied = {g.x for g in self.__galaxies}
        y_occupied = {g.y for g in self.__galaxies}
        x_empty = [x for x in range(max(x_occupied)) if x not in x_occupied]
        y_empty = [y for y in range(max(y_occupied)) if y not in y_occupied]
        for g1, g2 in combinations(self.__galaxies, 2):
            x_range = g1.get_x_ranges(g2)
            y_range = g1.get_y_ranges(g2)
            total_emptyspace += sum(
                [1 for x in x_empty if x_range[0] < x < x_range[1]]
            ) + sum([1 for y in y_empty if y_range[0] < y < y_range[1]])
            total_steps += g1.manhattan(g2)
        # Note: -1 on the expansion rates since those tiles are already counted once in normal steps
        return (
            total_steps + total_emptyspace * (small_exp_rate - 1),
            total_steps + total_emptyspace * (large_exp_rate - 1),
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_distance_sum()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
