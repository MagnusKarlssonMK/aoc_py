"""
2022 day 9 - Rope Bridge
"""

from aoc_py.util.math import signum
from aoc_py.util.point import Directions, Point


def catchup(p1: Point, p2: Point) -> Point:
    return Point(p1.x + signum(p2.x), p1.y + signum(p2.y))


class InputData:
    def __init__(self, s: str) -> None:
        dirmap = {
            "U": Directions.UP,
            "D": Directions.DOWN,
            "L": Directions.LEFT,
            "R": Directions.RIGHT,
        }
        self.__motions = [
            (dirmap[left], int(right))
            for left, right in [line.split() for line in s.splitlines()]
        ]

    def get_nbr_tail_positions(self, nbr_knots: int) -> int:
        knotpos = [Directions.ORIGIN for _ in range(nbr_knots)]
        tail_seen: set[Point] = {Directions.ORIGIN}
        for direction, steps in self.__motions:
            for _ in range(steps):
                knotpos[0] += direction
                for i in range(1, nbr_knots):
                    diff = knotpos[i - 1] - knotpos[i]
                    if abs(diff.x) > 1 or abs(diff.y) > 1:
                        # Tail out of range and needs to catch up
                        knotpos[i] = catchup(knotpos[i], diff)
                tail_seen.add(knotpos[-1])
        return len(tail_seen)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_nbr_tail_positions(2))
    if part in (None, 2):
        p2 = str(p.get_nbr_tail_positions(10))

    return p1, p2
