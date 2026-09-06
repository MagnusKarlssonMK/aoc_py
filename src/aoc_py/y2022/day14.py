"""
2022 day 14 - Regolith Reservoir

Simulates the falling sand by recording a trail so we can go back to
the previous position and continue from there when a grain either gets
locked in place or falls off the map into the abyss. This makes it so
that we don't need to start over from the start point for each grain,
which greatly reduces the number of iterations required.
"""

import itertools

from aoc_py.util.math import signum
from aoc_py.util.point import Directions, Point


class InputData:
    def __init__(self, s: str) -> None:
        self.__rockjoints: list[list[Point]] = [
            [Point.from_str(p) for p in line.split(" -> ")] for line in s.splitlines()
        ]

    def dropsand(self) -> tuple[int, int]:
        rocks: set[Point] = set()
        for joints in self.__rockjoints:
            for j1, j2 in itertools.pairwise(joints):
                delta = Point(signum(j2.x - j1.x), signum(j2.y - j1.y))
                p = j1
                while p != j2:
                    rocks.add(p)
                    p += delta
                rocks.add(p)
        max_y = max([p.y for p in rocks])
        start = Point(500, 0)
        current = start
        p1 = -1
        count = 0
        trail: list[Point] = []
        while True:
            if current in rocks:
                current = trail.pop()
            if current.y > max_y and p1 < 0:
                p1 = count
            if not (current + Directions.DOWN) in rocks and current.y < max_y + 1:
                trail.append(current)
                current += Directions.DOWN
            elif not (current + Directions.DIAG_L_D) in rocks and current.y < max_y + 1:
                trail.append(current)
                current += Directions.DIAG_L_D
            elif not (current + Directions.DIAG_R_D) in rocks and current.y < max_y + 1:
                trail.append(current)
                current += Directions.DIAG_R_D
            else:
                count += 1
                rocks.add(current)
            if current == start:
                break
        return p1, count


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.dropsand()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
