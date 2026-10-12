"""
2024 day 25 - Code Chronicle

Every lock and key is reduced to a single number where each column's height is shifted into
its own nibble (the top or bottom border row is excluded, so heights never exceed five and
four bits per column are plenty). A lock is measured by its '#' count per column, a key by
its '.' count per column.

A lock and a key fit when the two heights added together stay at most five in every column.
Instead of unpacking each column, two is added to every nibble (0x22222) and the result is
masked with the top bit of each nibble (0x88888): a column summing to six or more carries
into its nibble's high bit and disqualifies the pair.

Part 2 has no puzzle of its own; the last day always ends with the fiftieth star.
"""

from collections.abc import Iterable

from aoc_py.util.grid import Grid

PADDING = 0x22222
OVERFLOW_MASK = 0x88888


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__locks: list[int] = []
        self.__keys: list[int] = []
        for item in rawstr.split("\n\n"):
            grid = Grid(item)
            marker = grid.elements[0]
            columns = [0] * grid.x_max
            for i, c in enumerate(grid.elements):
                if c == marker:
                    columns[i % grid.x_max] += 1
            if marker == "#":
                self.__locks.append(self.__pack(n - 1 for n in reversed(columns)))
            else:
                self.__keys.append(
                    self.__pack(grid.y_max - n - 1 for n in reversed(columns))
                )

    @staticmethod
    def __pack(depths: Iterable[int]) -> int:
        return sum(depth << (4 * i) for i, depth in enumerate(depths))

    def get_p1(self) -> int:
        return sum(
            1
            for lock in self.__locks
            for key in self.__keys
            if ((lock + key + PADDING) & OVERFLOW_MASK) == 0
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = "-"

    return p1, p2
