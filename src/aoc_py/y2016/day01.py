"""
2016 day 1 - No Time for a Taxicab

Walk the taxicab instructions with the shared Point helpers from util.point, starting at the origin facing north.
Part 1 turns, then jumps each instruction's whole leg at once, and reports the manhattan distance of the point the
walk ends on. Part 2 turns the same way but steps one square at a time, keeping every visited square in a set and
stopping at the first square reached twice; the origin is in that set from the start, since that is where the walk
began, so a walk that returns to it reports zero rather than continuing to its final square. A walk that never
revisits a square has no part 2 answer, and reports -1 rather than some unrelated distance.
"""

from enum import Enum

from aoc_py.util.point import Directions, Point


class Rotation(Enum):
    LEFT = "L"
    RIGHT = "R"


class InputData:
    def __init__(self, s: str) -> None:
        self.__instructions = [
            (Rotation(line[0]), int(line[1:])) for line in s.split(", ")
        ]

    def get_p1(self) -> int:
        d = Directions.UP
        legs = [
            (d := d.rotate_left() if rotation == Rotation.LEFT else d.rotate_right())
            * steps
            for rotation, steps in self.__instructions
        ]
        return sum(legs, Directions.ORIGIN).manhattan(Directions.ORIGIN)

    def get_p2(self) -> int:
        pos = Directions.ORIGIN
        d = Directions.UP
        seen: set[Point] = {Directions.ORIGIN}
        for rotation, steps in self.__instructions:
            if rotation == Rotation.LEFT:
                d = d.rotate_left()
            else:
                d = d.rotate_right()
            for _ in range(steps):
                pos += d
                if pos in seen:
                    return pos.manhattan(Directions.ORIGIN)
                seen.add(pos)
        return -1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
