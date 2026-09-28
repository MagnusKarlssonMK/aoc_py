"""
2023 day 18 - Lavaduct Lagoon

Store the dig plan rather than a static grid, expanding it into the trench's vertices as we dig. Every lattice point in
or on the trench is then counted by half the shoelace sum plus half the total distance dug, plus one, which follows from
Pick's theorem. For part 2 the same dig plan is simply decoded out of the colour given in place of the step and
direction, so no separate implementation is needed.
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

    def __init__(self, rawstr: str) -> None:
        self.__digplan: list[DigPlan] = []
        for line in rawstr.splitlines():
            d, s, c = line.split()
            self.__digplan.append(
                DigPlan(InputData.__DIRECTIONS[d], int(s), c.strip("(#)"))
            )

    def __dig(self, swapped: bool) -> tuple[list[Point], int]:
        """Digs out the trench, returning its vertices and the total distance dug."""
        path = [Point(0, 0)]
        length = 0
        for planline in self.__digplan:
            if swapped:
                # The colour holds the distance in hex, then a digit indexing the
                # straight neighbours, which are listed in R, D, L, U order.
                direction = Directions.NEIGHBORS_STRAIGHT[int(planline.color[-1])]
                step = int(planline.color[:-1], 16)
            else:
                direction, step = planline.direction, planline.step
            path.append(path[-1] + direction * step)
            length += step
        return path, length

    def get_areapoints(self, swapped: bool = False) -> int:
        path, length = self.__dig(swapped)
        areasum = sum(
            [
                path[idx].determinant(path[(idx + 1) % len(path)])
                for idx, _ in enumerate(path)
            ]
        )
        return (abs(areasum) + length) // 2 + 1

    def get_p1(self) -> int:
        return self.get_areapoints()

    def get_p2(self) -> int:
        return self.get_areapoints(True)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
