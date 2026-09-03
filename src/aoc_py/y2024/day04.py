"""
2024 day 4 - Ceres Search

Part 1

Scan the grid and investigate all nodes containing an 'X', and look in all
eight directions and see if XMAS is created.

Part 2

This time, scan for nodes containing an 'A' instead, form words from the
combination with the diagonal nodes to form the X, and see if the generated
word is eithes MAS or SAM.
"""

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions


class InputData:
    def __init__(self, s: str) -> None:
        self.__grid = Grid(s)

    def get_p1(self) -> int:
        total = 0
        for i, c in enumerate(self.__grid.elements):
            p = self.__grid.get_point(i)
            if c == "X":
                for d in Directions.NEIGHBORS_ALL:
                    if (
                        "X"
                        + self.__grid.get_element(p + d)
                        + self.__grid.get_element(p + d * 2)
                        + self.__grid.get_element(p + d * 3)
                        == "XMAS"
                    ):
                        total += 1
        return total

    def get_p2(self) -> int:
        total = 0
        for i, c in enumerate(self.__grid.elements):
            p = self.__grid.get_point(i)
            if c == "A":
                word1 = (
                    self.__grid.get_element(p - Directions.DIAG_R_D)
                    + "A"
                    + self.__grid.get_element(p + Directions.DIAG_R_D)
                )
                if word1 in ("MAS", "SAM"):
                    word2 = (
                        self.__grid.get_element(p - Directions.DIAG_L_D)
                        + "A"
                        + self.__grid.get_element(p + Directions.DIAG_L_D)
                    )
                    if word2 in ("MAS", "SAM"):
                        total += 1
        return total


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
