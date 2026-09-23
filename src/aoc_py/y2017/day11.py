"""
2017 day 11 - Hex Ed

Stores the hexgrid using axial coordinate system, i.e. based on 3d system (q, r, s) but with the third dimension
truncated, since the sum of all three must be zero, meaning that it can be calculated when necessary.
"""

from typing import Final

from aoc_py.util.point import Point

# Use the Point class to represent Hex coordinates in axial form (flat top hex tiles)
# x = q, y = r


class HexDirections:
    N: Final = Point(0, -1)
    NE: Final = Point(1, -1)
    SE: Final = Point(1, 0)
    S: Final = Point(0, 1)
    SW: Final = Point(-1, 1)
    NW: Final = Point(-1, 0)


def get_hex_distance(p1: Point, p2: Point) -> int:
    s1 = -(p1.x + p1.y)
    s2 = -(p2.x + p2.y)
    return (abs(p1.y - p2.y) + abs(p1.x - p2.x) + abs(s1 - s2)) // 2


class InputData:
    __STR_TO_POINT: Final = {
        "n": HexDirections.N,
        "ne": HexDirections.NE,
        "se": HexDirections.SE,
        "s": HexDirections.S,
        "sw": HexDirections.SW,
        "nw": HexDirections.NW,
    }

    def __init__(self, s: str) -> None:
        self.__moves = [self.__STR_TO_POINT[m] for m in s.split(",")]

    def get_distance(self) -> tuple[int, int]:
        start_location = Point(0, 0)
        current_location = Point(0, 0)
        current_distance = 0
        maxdistance = 0
        for move in self.__moves:
            current_location += move
            current_distance = get_hex_distance(current_location, start_location)
            maxdistance = max(maxdistance, current_distance)
        return current_distance, maxdistance


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_distance()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
