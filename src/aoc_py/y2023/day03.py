"""
2023 day 3 - Gear Ratios

Store the symbols in a dict keyed by their point, and a dict of all parts holding the set of adjacent symbols for
each part. The neighbours of a part are the three rows around it, spanning its own columns plus one on each side.
For part 1, sum the values of the parts that have at least one symbol in their adjacent set.
For part 2, a single pass over the parts collects the values of the parts touching each gear, and every gear with
exactly two adjacent parts contributes the product of those two values.
"""

from collections import defaultdict
from collections.abc import Generator
from dataclasses import dataclass

from aoc_py.util.point import Point


@dataclass(frozen=True)
class Part:
    start: Point
    length: int
    value: int

    def get_adjacent_points(self) -> Generator[Point]:
        for y in range(self.start.y - 1, self.start.y + 2):
            for x in range(self.start.x - 1, self.start.x + self.length + 1):
                yield Point(x, y)


class InputData:
    def __init__(self, s: str) -> None:
        self.__parts: dict[Part, set[Point]] = {}
        self.__symbols: dict[Point, str] = {}
        parts: list[Part] = []
        for y, row in enumerate(s.splitlines()):
            number = 0
            start = -1
            for x, c in enumerate(row):
                if c.isdecimal():
                    if start < 0:
                        start = x
                    number = 10 * number + int(c)
                else:
                    if start >= 0:
                        parts.append(Part(Point(start, y), x - start, number))
                        number = 0
                        start = -1
                    if c != ".":
                        self.__symbols[Point(x, y)] = c
            if start >= 0:
                parts.append(Part(Point(start, y), len(row) - start, number))

        # Connect symbols to parts
        for part in parts:
            adj: set[Point] = set()
            for p in part.get_adjacent_points():
                if p in self.__symbols:
                    adj.add(p)
            self.__parts[part] = adj

    def get_p1(self) -> int:
        return sum([part.value for part, adj in self.__parts.items() if adj])

    def get_p2(self) -> int:
        gears: defaultdict[Point, list[int]] = defaultdict(list)
        for part, adj in self.__parts.items():
            for symbol in adj:
                if self.__symbols[symbol] == "*":
                    gears[symbol].append(part.value)
        return sum([vals[0] * vals[1] for vals in gears.values() if len(vals) == 2])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
