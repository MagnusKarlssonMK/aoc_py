"""
2016 day 1 - No Time for a Taxicab

Create a Point class to represent current position and then:
Part 1: Simply walk through all off the instructions and take the manhattan distance of the point we end up in.
Part 2: Store the visited points in a set and stop when landing on a point that is already in that set and return the
manhattan distance of that point. Note that unlike part 1, this means that we need to walk every single point one step
at a time, and not directly jump the number of steps in the instruction in one giant step.
"""

from enum import Enum

from aoc_py.util.point import Directions, Point


class Rotation(Enum):
    LEFT = "L"
    RIGHT = "R"


class InputData:
    def __init__(self, s: str) -> None:
        self.__position = Directions.ORIGIN
        self.__direction = Directions.UP
        self.__instructions = [
            (Rotation(line[0]), int(line[1:])) for line in s.split(", ")
        ]

    def get_shortest_distance(self, findrepeat: bool = False) -> int:
        pos = self.__position
        d = self.__direction
        seen: set[Point] = set()
        for rotation, steps in self.__instructions:
            if rotation == Rotation.LEFT:
                d = d.rotate_left()
            else:
                d = d.rotate_right()
            if findrepeat:
                for _ in range(steps):
                    pos += d
                    if pos in seen:
                        return pos.manhattan(Directions.ORIGIN)
                    else:
                        seen.add(pos)
            else:
                pos += d * steps
        return pos.manhattan(Directions.ORIGIN)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_shortest_distance())
    if part in (None, 2):
        p2 = str(p.get_shortest_distance(True))

    return p1, p2
