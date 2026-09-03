"""
2024 day 8 - Resonant Collinearity
"""

from dataclasses import dataclass
from itertools import combinations

from aoc_py.util.point import Point


@dataclass(frozen=True)
class PointX(Point):
    def get_anti_points(self, other: PointX, harmonic: int) -> tuple[PointX, PointX]:
        return (
            PointX(
                self.x + harmonic * (self.x - other.x),
                self.y + harmonic * (self.y - other.y),
            ),
            PointX(
                other.x + harmonic * (other.x - self.x),
                other.y + harmonic * (other.y - self.y),
            ),
        )


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__height = 0
        self.__width = 0
        self.__antennas: dict[str, list[PointX]] = {}
        for y, line in enumerate(rawstr.splitlines()):
            self.__height += 1
            if y == 0:
                self.__width = len(line)
            for x, c in enumerate(line):
                if c != ".":
                    if c in self.__antennas:
                        self.__antennas[c].append(PointX(x, y))
                    else:
                        self.__antennas[c] = [PointX(x, y)]

    def get_antinode_counts(self) -> tuple[int, int]:
        antinodes: set[PointX] = set()
        antinodes_w_harmonics: set[PointX] = set()
        for antennas in self.__antennas.values():
            for a1, a2 in combinations(antennas, 2):
                inside = True
                harmonic = 0
                while inside:
                    inside = False
                    an1, an2 = a1.get_anti_points(a2, harmonic)
                    if 0 <= an1.x < self.__width and 0 <= an1.y < self.__height:
                        inside = True
                        if harmonic == 1:
                            antinodes.add(an1)
                        antinodes_w_harmonics.add(an1)
                    if 0 <= an2.x < self.__width and 0 <= an2.y < self.__height:
                        inside = True
                        if harmonic == 1:
                            antinodes.add(an2)
                        antinodes_w_harmonics.add(an2)
                    harmonic += 1
        return len(antinodes), len(antinodes_w_harmonics)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_antinode_counts()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
