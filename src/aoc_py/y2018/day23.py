"""
2018 day 23 - Experimental Emergency Teleportation

Part 1

Straightforward, just parse the nanobots and sort them according to radius to find the
largest one, then use manhattan distance to count how many other bots are in its range.

Part 2

Basically treating the nanobots as cubes and splits them into smaller and smaller with
A* until it's down to a single coordinate.
"""

import math
from collections.abc import Generator
from dataclasses import dataclass
from heapq import heappop, heappush
from itertools import count, product


@dataclass(frozen=True)
class Point3D:
    x: int
    y: int
    z: int

    def manhattan(self, other: Point3D) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

    def get_point(self) -> tuple[int, int, int]:
        return self.x, self.y, self.z


@dataclass(frozen=True)
class Rect:
    x: tuple[int, int]
    y: tuple[int, int]
    z: tuple[int, int]

    def get_point(self) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int]]:
        return self.x, self.y, self.z

    def get_zerodistance(self) -> int:
        return (
            min([abs(x) for x in self.x])
            + min([abs(y) for y in self.y])
            + min([abs(z) for z in self.z])
        )


@dataclass(frozen=True)
class Node:
    rect: Rect
    size: int

    def get_next_nodes(self) -> Generator[Node]:
        newsize = self.size // 2
        if newsize > 0:
            for steps in product(range(2), repeat=3):
                r = Rect(
                    *[
                        (
                            length + (s * newsize),
                            min(length + (s + 1) * newsize - 1, height),
                        )
                        for (length, height), s in zip(self.rect.get_point(), steps)
                    ]
                )
                yield Node(r, newsize)


@dataclass(frozen=True)
class Nanobot:
    point: Point3D
    radius: int

    @classmethod
    def parse_str(cls, s: str) -> Nanobot:
        pos, r = s.lstrip("pos=<").split(">, r=")
        pos = Point3D(*list(map(int, pos.split(","))))
        return Nanobot(pos, int(r))

    def intersects_node(self, r: Rect) -> bool:
        distance = 0
        for c, (length, height) in zip(self.point.get_point(), r.get_point()):
            if c < length:
                distance += length - c
            elif c > height:
                distance += c - height
            if distance > self.radius:
                return False
        return True

    def __lt__(self, other: Nanobot) -> bool:
        return self.radius < other.radius


class InputData:
    def __init__(self, s: str) -> None:
        self.__bots = sorted(
            [Nanobot.parse_str(line) for line in s.splitlines()], reverse=True
        )

    def get_p1(self) -> int:
        return sum(
            [
                1
                for bot in self.__bots
                if self.__bots[0].point.manhattan(bot.point) <= self.__bots[0].radius
            ]
        )

    def __get_node_prio(self, n: Node) -> tuple[int, int, int]:
        c = sum([1 for b in self.__bots if not b.intersects_node(n.rect)])
        return c, n.rect.get_zerodistance(), n.size

    def get_p2(self) -> int:
        minpoints = tuple(map(min, zip(*[b.point.get_point() for b in self.__bots])))
        maxpoints = tuple(map(max, zip(*[b.point.get_point() for b in self.__bots])))
        rect = Rect(
            *[(min(low, 0), max(high, 0)) for low, high in zip(minpoints, maxpoints)]
        )
        size = 2 ** (int(math.log2(max(maxpoints))) + 1)
        start = Node(rect, size)
        u = count()
        queue: list[tuple[int, int, int, int, Node]] = []
        heappush(queue, (*self.__get_node_prio(start), next(u), start))
        result = -1
        while queue:
            _, _, _, _, currentnode = heappop(queue)
            if currentnode.size == 1:
                result = currentnode.rect.get_zerodistance()
                break
            for nextnode in currentnode.get_next_nodes():
                heappush(queue, (*self.__get_node_prio(nextnode), next(u), nextnode))
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
