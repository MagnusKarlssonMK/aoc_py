"""
2024 day 4 - Ceres Search

Part 1

Scan the grid for every 'X' and look in all eight directions to see if XMAS is
created.

Part 2

Scan for every 'A' instead and combine the two diagonals through it into an X.
The center is a valid X-MAS when both diagonals spell either MAS or SAM.
"""

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__grid = Grid(rawstr)

    def get_p1(self) -> int:
        grid = self.__grid
        width, height, elements = grid.x_max, grid.y_max, grid.elements
        total = 0
        for p in grid.find_all("X"):
            for d in Directions.NEIGHBORS_ALL:
                x, y = p.x + d.x, p.y + d.y
                if (
                    0 <= x < width
                    and 0 <= y < height
                    and elements[y * width + x] == "M"
                ):
                    x, y = x + d.x, y + d.y
                    if (
                        0 <= x < width
                        and 0 <= y < height
                        and elements[y * width + x] == "A"
                    ):
                        x, y = x + d.x, y + d.y
                        if (
                            0 <= x < width
                            and 0 <= y < height
                            and elements[y * width + x] == "S"
                        ):
                            total += 1
        return total

    def get_p2(self) -> int:
        grid = self.__grid
        width, height, elements = grid.x_max, grid.y_max, grid.elements
        total = 0
        for p in grid.find_all("A"):
            x, y = p.x, p.y
            if x < 1 or y < 1 or x >= width - 1 or y >= height - 1:
                continue
            diag1 = (
                elements[(y - 1) * width + x - 1] + elements[(y + 1) * width + x + 1]
            )
            diag2 = (
                elements[(y - 1) * width + x + 1] + elements[(y + 1) * width + x - 1]
            )
            if diag1 in ("MS", "SM") and diag2 in ("MS", "SM"):
                total += 1
        return total


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
