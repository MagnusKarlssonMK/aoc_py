"""
2023 day 21 - Step Counter

Part 1: Stores the grid in a new class, and finds reachable tiles within the step count limit using BFS, then count
only the ones that have odd/even number of steps (depending on whether the count limit is odd/even).
Part 2: Solves it with three-point-formula to determine the coefficients in a quadratic formula, and calculate the
answer from that.
"""

from collections.abc import Generator

from aoc_py.util.point import Directions, Point


class InputData:
    def __init__(self, s: str):
        lines = s.splitlines()
        self.__height = len(lines)
        self.__width = len(lines[0])
        self.__start = Point(-1, -1)
        self.__rocks: set[Point] = set()
        for y, line in enumerate(s.splitlines()):
            for x, c in enumerate(line):
                if c == "S":
                    self.__start = Point(x, y)
                elif c == "#":
                    self.__rocks.add(Point(x, y))

    def __get_neighbors(self, coord: Point, expand: bool) -> Generator[Point]:
        for d in Directions.NEIGHBORS_STRAIGHT:
            neighbor = coord + d
            if expand:
                if (
                    Point(neighbor.x % self.__width, neighbor.y % self.__height)
                    not in self.__rocks
                ):
                    yield neighbor
            else:
                if Point(neighbor.x, neighbor.y) not in self.__rocks:
                    yield neighbor

    def get_p1(self, steps: int, expand: bool = False) -> int:
        seen: set[Point] = set()
        reachable: set[Point] = set()
        bfs_queue = [(self.__start, 0)]
        while bfs_queue:
            u, count = bfs_queue.pop(0)
            if count <= steps:
                if count % 2 == steps % 2:
                    reachable.add(u)
                for v in self.__get_neighbors(u, expand):
                    if v not in seen:
                        bfs_queue.append((v, count + 1))
                        seen.add(v)
        return len(reachable)

    def get_p2(self, maxstep: int) -> int:
        n = (self.__height - 1) // 2
        three_vec = [n + (self.__height * i) for i in range(3)]
        # y = a*x^2 + b*x + c
        y = [self.get_p1(i, True) for i in three_vec]
        c = y[0]
        b = ((4 * y[1]) - (3 * y[0]) - y[2]) // 2
        a = y[1] - y[0] - b
        x = (maxstep - n) // self.__height
        return (a * x**2) + (b * x) + c


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1(64))
    if part in (None, 2):
        p2 = str(p.get_p2(26501365))

    return p1, p2
