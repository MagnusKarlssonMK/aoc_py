"""
Store the trench in a class as a list of dig steps, i.e. expands as we dig through it without using any static grid.
After the dig commands have been carried out, the results are calculated with shoelace formula and Pick's theorem.
For part 2, simply convert the instructions before running the command.
"""

from dataclasses import dataclass
from typing import Final

from aoc_py.util.point import Directions, Point


@dataclass(frozen=True)
class DigPlan:
    direction: Point
    step: int
    color: str


class InputData:
    __DIRECTIONS: Final = {
        "R": Directions.RIGHT,
        "D": Directions.DOWN,
        "L": Directions.LEFT,
        "U": Directions.UP,
    }
    __DIRMAP: Final = {0: "R", 1: "D", 2: "L", 3: "U"}

    def __init__(self, rawstr: str) -> None:
        self.__digplan: list[DigPlan] = []
        for line in rawstr.splitlines():
            d, s, c = line.split()
            c = c.strip("(").strip(")").strip("#")
            self.__digplan.append(DigPlan(InputData.__DIRECTIONS[d], int(s), c))
        self.__digpath: list[Point] = []

    def __dig(self, swapped: bool) -> None:
        self.__digpath = [Point(0, 0)]
        for planline in self.__digplan:
            if swapped:
                planline = DigPlan(
                    InputData.__DIRECTIONS[InputData.__DIRMAP[int(planline.color[-1])]],
                    int(planline.color[0:5], 16),
                    planline.color,
                )
            self.__digpath.append(
                self.__digpath[-1] + (planline.direction * planline.step)
            )

    def __get_outlinelength(self) -> int:
        return sum(
            [
                self.__digpath[idx].manhattan(
                    self.__digpath[(idx + 1) % len(self.__digpath)]
                )
                for idx, _ in enumerate(self.__digpath)
            ]
        )

    def get_areapoints(self, swapped: bool = False) -> int:
        self.__dig(swapped)
        areasum = sum(
            [
                self.__digpath[idx].determinant(
                    self.__digpath[(idx + 1) % len(self.__digpath)]
                )
                for idx, _ in enumerate(self.__digpath)
            ]
        )
        length = self.__get_outlinelength()
        return (abs(areasum) // 2) + 1 + (length // 2)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_areapoints())
    if part in (None, 2):
        p2 = str(p.get_areapoints(True))

    return p1, p2
