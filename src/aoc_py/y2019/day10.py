"""
2019 day 10 - Monitoring Station

Use atan2 to calculate angles between asteroids, with some extra trickery to compensate for the 'upside-down'
coordinate system.
"""

from collections import defaultdict
from math import atan2, degrees

from aoc_py.util.point import Point


def get_angle(p1: Point, p2: Point) -> float:
    return (
        degrees(atan2(p1.y - p2.y, p1.x - p2.x)) + 270
    ) % 360  # Rotate so that 0 is north


class InputData:
    def __init__(self, s: str) -> None:
        self.__asteroids = [
            Point(x, y)
            for y, line in enumerate(s.splitlines())
            for x, c in enumerate(line)
            if c == "#"
        ]

    def __count_visible(self, a1: Point) -> int:
        return len({get_angle(a1, a2) for a2 in self.__asteroids if a2 != a1})

    def __find_best(self) -> Point:
        return max(self.__asteroids, key=self.__count_visible)

    def get_p1(self) -> int:
        return self.__count_visible(self.__find_best())

    def get_p2(self, target: int = 200) -> int:
        best = self.__find_best()
        visible: defaultdict[float, list[tuple[Point, int]]] = defaultdict(list)
        for a in self.__asteroids:
            if a != best:
                visible[get_angle(best, a)].append((a, best.manhattan(a)))
        for asteroids in visible.values():  # Sort by distance
            asteroids.sort(key=lambda asteroid: asteroid[1])
        angles = sorted(visible)
        idx = 0
        winner = Point(-1, -1)
        vaporized = 0
        while angles and vaporized < target:
            winner, _ = visible[angles[idx]].pop(0)
            vaporized += 1
            if not visible[angles[idx]]:
                del angles[idx]
                if not angles:  # Safety guard in case the input data is too small
                    break
                idx -= 1
            idx = (idx + 1) % len(angles)
        return (100 * winner.x) + winner.y


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
