"""
2022 day 24 - Blizzard Basin

Blizzards are stored per direction and their position at any minute is derived from the minute number, so the map itself
is never advanced. Because that map repeats with period lcm(width, height), the expedition state is (position, minute
mod period) and an A* search over that finite space finds the shortest crossing, using the manhattan distance to the
target as an admissible heuristic. Part 2 makes the crossing three times - there, back, and there again - with each leg
starting at the minute the previous one finished. If any leg is unreachable the finite frontier empties and the crossing
is reported as -1.
"""

from heapq import heappop, heappush
from math import lcm
from typing import Final

from aoc_py.util.point import Directions, Point

_BLIZZARD_DIRECTIONS: Final[dict[str, Point]] = {
    ">": Directions.RIGHT,
    "<": Directions.LEFT,
    "^": Directions.UP,
    "v": Directions.DOWN,
}


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__startpoint = Point(-1, -1)
        self.__exitpoint = Point(-1, -1)
        self.__blizzards: dict[Point, set[Point]] = {
            d: set() for d in Directions.NEIGHBORS_STRAIGHT
        }
        lines = rawstr.splitlines()
        self.__width: int = len(lines[0]) - 2  # Don't include the walls
        self.__height: int = len(lines) - 2
        self.__period: int = lcm(self.__width, self.__height)
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == "#":
                    continue
                if y == 0 and c == ".":
                    self.__startpoint = Point(x, y)
                elif y == self.__height + 1 and c == ".":
                    self.__exitpoint = Point(x, y)
                elif c in _BLIZZARD_DIRECTIONS:
                    self.__blizzards[_BLIZZARD_DIRECTIONS[c]].add(Point(x, y))

    def __is_occupied_at_step(self, point: Point, step: int) -> bool:
        if point == self.__startpoint or point == self.__exitpoint:
            return False
        for direction, v in self.__blizzards.items():
            start_x = 1 + (point.x - 1 - (step * direction.x)) % self.__width
            start_y = 1 + (point.y - 1 - (step * direction.y)) % self.__height
            if Point(start_x, start_y) in v:
                return True
        return False

    def __shortest_path(self, start: Point, end: Point, startstep: int = 0) -> int:
        queue: list[tuple[int, Point, int]] = []
        heappush(queue, (0, start, startstep))
        seen: set[tuple[Point, int]] = set()
        while queue:
            _, point, steps = heappop(queue)
            if point == end:
                return steps
            state = (point, steps % self.__period)
            if state in seen:
                continue
            seen.add(state)
            for d in [*Directions.NEIGHBORS_STRAIGHT, Directions.ORIGIN]:
                next_step = point + d
                if (
                    (
                        0 < next_step.y <= self.__height
                        and 0 < next_step.x <= self.__width
                    )
                    or next_step in (start, end)
                ) and not self.__is_occupied_at_step(next_step, steps + 1):
                    heappush(
                        queue,
                        (steps + 1 + next_step.manhattan(end), next_step, steps + 1),
                    )
        return -1

    def get_there_and_back_again(self) -> tuple[int, int]:
        a = self.__shortest_path(self.__startpoint, self.__exitpoint, 0)
        b = self.__shortest_path(self.__exitpoint, self.__startpoint, a)
        c = self.__shortest_path(self.__startpoint, self.__exitpoint, b)
        if -1 in (a, b, c):
            return -1, -1
        return a, c


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_there_and_back_again()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
