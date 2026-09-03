"""
2023 day 3 - Gear Ratios

Store the symbols in a dict with the type stored for each symbol, and then a dict for all parts which stores a list
of adjacent symbols for each part.
Then for part 1, simply iterate over the parts and get the sum of the values for the parts that have at least one
symbol in its adjacent list.
For part 2, instead iterate over the symbols and find the gears, and then iterate over the parts to see how many parts
that are adjacent for each gear.
"""

from collections.abc import Generator
from dataclasses import dataclass

from aoc_py.util.point import Point


@dataclass(frozen=True)
class Part:
    point: Point
    length: int
    value: int

    def get_adjacent_points(self) -> Generator[Point]:
        for y in range(self.point.y - 1, self.point.y + 2):
            for x in range(self.point.x - 1, self.point.x + self.length + 1):
                yield Point(x, y)


class InputData:
    def __init__(self, s: str) -> None:
        self.__parts: dict[Part, set[Point]] = {}
        self.__symbols: dict[Point, str] = {}
        number = 0
        parts: set[Part] = set()
        numberpoint = Point(0, 0)
        for y, row in enumerate(s.splitlines()):
            for x, c in enumerate(row):
                if c.isdecimal():
                    if number == 0:
                        numberpoint = Point(x, y)
                    number = 10 * number + int(c)
                else:
                    if number > 0:
                        parts.add(Part(numberpoint, x - numberpoint.x, number))
                        number = 0
                    if c != ".":
                        self.__symbols[Point(x, y)] = c
            if number > 0:
                parts.add(Part(numberpoint, len(row) - numberpoint.x, number))
                number = 0

        # Connect symbols to parts
        for part in parts:
            adj: set[Point] = set()
            for p in part.get_adjacent_points():
                if p in self.__symbols:
                    adj.add(p)
            self.__parts[part] = adj

    def get_p1(self) -> int:
        return sum([part.value for part in self.__parts if len(self.__parts[part]) > 0])

    def get_p2(self) -> int:
        result = 0
        for symbol, symbtype in self.__symbols.items():
            if symbtype == "*":
                adj_parts = [
                    part.value for part in self.__parts if symbol in self.__parts[part]
                ]
                if len(adj_parts) == 2:
                    result += adj_parts[0] * adj_parts[1]
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
