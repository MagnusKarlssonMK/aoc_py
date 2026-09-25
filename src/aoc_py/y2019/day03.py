"""
2019 day 3 - Crossed Wires

Part 1

We can find all intersections by putting all coordinates in sets for each wire, and then find the common
points. Then the answer is given by the smallest manhattan distance from origin to intersection.

Part 2

We can get the distances by finding the index of each intersection's coordinate in the wire lists.
"""

from typing import Final

from aoc_py.util.point import Directions, Point


class Wire:
    __DIRMAP: Final = {
        "R": Directions.RIGHT,
        "L": Directions.LEFT,
        "U": Directions.UP,
        "D": Directions.DOWN,
    }

    def __init__(self, s: str) -> None:
        self.__instructions: list[tuple[Point, int]] = [
            (self.__DIRMAP[instr[0]], int(instr[1:])) for instr in s.split(",")
        ]

    def walk(self) -> list[Point]:
        pos = Directions.ORIGIN
        points = []
        for p, v in self.__instructions:
            for _ in range(v):
                pos += p
                if pos != Directions.ORIGIN:
                    points.append(pos)
        return points


class InputData:
    def __init__(self, s: str) -> None:
        self.__wires = [Wire(line) for line in s.splitlines()]

    def get_distances(self) -> tuple[int, int]:
        w1_points = self.__wires[0].walk()
        w2_points = self.__wires[1].walk()
        w1_set = set(w1_points)
        w2_set = set(w2_points)
        intersections = w1_set.intersection(w2_set)
        p1 = []
        p2 = []
        for i in intersections:
            p1.append(i.manhattan(Directions.ORIGIN))
            p2.append(2 + w1_points.index(i) + w2_points.index(i))
        return min(p1), min(p2)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_distances()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
