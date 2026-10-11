"""
2018 day 22 - Mode Maze

Generates the map dynamically as needed in a dictionary, sort of like a cache.

Part 1

The answer is simply the sum of the values of the region types of each location
in the square defined by the start and target nodes.

Part 2

Find the shortest path with an A* search over (x, y, tool) states, with a cost of
1 per step and 7 per tool swap, and the manhattan distance to the target as the
heuristic. The hot path represents states as plain ints and tuples rather than
Point/Node objects, since the hashing of those dominates the search.
"""

from enum import Enum
from heapq import heappop, heappush
from typing import Final

from aoc_py.util.point import Point


class Tool(Enum):
    TORCH = 0
    GEAR = 1
    NEITHER = 2


class Type(Enum):
    ROCKY = 0
    WET = 1
    NARROW = 2


class InputData:
    __SWAP_COST = 7
    __STEP_COST = 1
    # Per region type: the tool it forbids, and the two tools it allows (as Tool values).
    __FORBIDDEN: Final = {
        Type.ROCKY: Tool.NEITHER.value,
        Type.WET: Tool.TORCH.value,
        Type.NARROW: Tool.GEAR.value,
    }
    __ALLOWED: Final = {
        Type.ROCKY: (Tool.TORCH.value, Tool.GEAR.value),
        Type.WET: (Tool.GEAR.value, Tool.NEITHER.value),
        Type.NARROW: (Tool.TORCH.value, Tool.NEITHER.value),
    }

    def __init__(self, rawstr: str) -> None:
        lines = rawstr.splitlines()
        self.__depth = int(lines[0].split(": ")[1])
        self.__target = Point(*list(map(int, lines[1].split(": ")[1].split(","))))
        self.__start = Point(0, 0)
        self.__geoindex: dict[Point, int] = {}
        self.__regiontype: dict[tuple[int, int], Type] = {}

    def __get_geoindex(self, p: Point) -> int:
        if p in self.__geoindex:
            return self.__geoindex[p]
        i = 0
        if p not in (self.__start, self.__target):
            if p.y == 0:
                i = p.x * 16807
            elif p.x == 0:
                i = p.y * 48271
            else:
                i = self.__get_erosionlevel(
                    Point(p.x - 1, p.y)
                ) * self.__get_erosionlevel(Point(p.x, p.y - 1))
        self.__geoindex[p] = i
        return i

    def __get_erosionlevel(self, p: Point) -> int:
        return (self.__depth + self.__get_geoindex(p)) % 20183

    def __get_region_type(self, x: int, y: int) -> Type:
        region = self.__regiontype.get((x, y))
        if region is None:
            region = Type(self.__get_erosionlevel(Point(x, y)) % 3)
            self.__regiontype[(x, y)] = region
        return region

    def get_p1(self) -> int:
        return sum(
            self.__get_region_type(x, y).value
            for x in range(self.__target.x + 1)
            for y in range(self.__target.y + 1)
        )

    def get_p2(self) -> int:
        tx, ty = self.__target.x, self.__target.y
        goal_tool = Tool.TORCH.value
        forbidden = InputData.__FORBIDDEN
        allowed = InputData.__ALLOWED
        swap_cost = InputData.__SWAP_COST
        step_cost = InputData.__STEP_COST
        region_type = self.__get_region_type

        start = (self.__start.x, self.__start.y, goal_tool)
        # Queue entries are (weight + heuristic, time spent, x, y, tool).
        pqueue: list[tuple[int, int, int, int, int]] = [(tx + ty, 0, *start)]
        dist: dict[tuple[int, int, int], int] = {start: 0}
        timespent = 0
        while pqueue:
            _, timespent, x, y, tool = heappop(pqueue)
            if x == tx and y == ty and tool == goal_tool:
                break
            if timespent > dist[(x, y, tool)]:
                continue
            # Add the option to swap to the other tool allowed in this region.
            first, second = allowed[region_type(x, y)]
            newtool = second if tool == first else first
            newkey = (x, y, newtool)
            newtime = timespent + swap_cost
            if newtime < dist.get(newkey, newtime + 1):
                dist[newkey] = newtime
                heappush(
                    pqueue,
                    (newtime + abs(x - tx) + abs(y - ty), newtime, x, y, newtool),
                )
            # Move into each adjacent valid region while keeping the current tool.
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or tool == forbidden[region_type(nx, ny)]:
                    continue
                newkey = (nx, ny, tool)
                newtime = timespent + step_cost
                if newtime < dist.get(newkey, newtime + 1):
                    dist[newkey] = newtime
                    heappush(
                        pqueue,
                        (newtime + abs(nx - tx) + abs(ny - ty), newtime, nx, ny, tool),
                    )
        return timespent


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
