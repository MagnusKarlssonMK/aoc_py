"""
2022 day 24 - Blizzard Basin

To avoid having to continuously update the list of blizzards, instead store the blizzards in a per-direction dict,
and calculate dynamically whether a certain point will be occupied by at least one blizzard at a certain minute.
Use A* to traverse the map and find the shortest path, using the manhattan distance to the target as heuristic. The
time spent is effectively a third dimension in the space, since the possible neighbors changes with time, so we need
to include both position and time as key for the visited nodes.
The map state is cyclic since the winds will eventually return to the start position (lcm of width, height), but the
cycle is longer than the time spent to traverse the map, so there isn't much of a benefit to optimize making use of the
cycle.
"""

from heapq import heappop, heappush

from aoc_py.util.point import Directions, Point


class InputData:
    def __init__(self, rawstr: str) -> None:
        dirmap = {
            ">": Directions.RIGHT,
            "<": Directions.LEFT,
            "^": Directions.UP,
            "v": Directions.DOWN,
        }
        self.__startpoint = Point(-1, -1)
        self.__exitpoint = Point(-1, -1)
        self.__walls: set[Point] = set()
        self.__blizzards: dict[Point, set[Point]] = {
            d: set() for d in Directions.NEIGHBORS_STRAIGHT
        }
        lines = rawstr.splitlines()
        self.__width = len(lines[0]) - 2  # Don't include the walls
        self.__height = len(lines) - 2
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == "#":
                    self.__walls.add(Point(x, y))
                elif y == 0 and c == ".":
                    self.__startpoint = Point(x, y)
                elif y == self.__height + 1 and c == ".":
                    self.__exitpoint = Point(x, y)
                elif c in dirmap:
                    self.__blizzards[dirmap[c]].add(Point(x, y))

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
            if (point, steps) in seen:
                continue
            seen.add((point, steps))
            for d in [
                Directions.UP,
                Directions.RIGHT,
                Directions.DOWN,
                Directions.LEFT,
                Directions.ORIGIN,
            ]:
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
        return a, c


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_there_and_back_again()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
