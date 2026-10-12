"""
2018 day 23 - Experimental Emergency Teleportation

Part 1

Straightforward, just parse the nanobots and sort them according to radius to find the
largest one, then use manhattan distance to count how many other bots are in its range.

Part 2

Treating the nanobots as boxes and splitting the bounding box into octants, best-first
by (bots out of range, distance to origin, size), until it's down to a single
coordinate. The hot path keeps the bots as plain (x, y, z, r) tuples, since the
hashing-free iteration matters far more than any attribute access would.
"""

from collections.abc import Generator
from dataclasses import dataclass
from heapq import heappop, heappush
from itertools import count, product


@dataclass(frozen=True)
class Rect:
    x: tuple[int, int]
    y: tuple[int, int]
    z: tuple[int, int]

    def get_zerodistance(self) -> int:
        return (
            max(self.x[0], -self.x[1], 0)
            + max(self.y[0], -self.y[1], 0)
            + max(self.z[0], -self.z[1], 0)
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
                        for (length, height), s in zip(
                            (self.rect.x, self.rect.y, self.rect.z), steps
                        )
                    ]
                )
                yield Node(r, newsize)


class InputData:
    def __init__(self, s: str) -> None:
        self.__bots = sorted(
            (self.__parse_bot(line) for line in s.splitlines()),
            key=lambda b: b[3],
            reverse=True,
        )

    @staticmethod
    def __parse_bot(s: str) -> tuple[int, int, int, int]:
        pos, r = s.lstrip("pos=<").split(">, r=")
        x, y, z = map(int, pos.split(","))
        return x, y, z, int(r)

    def get_p1(self) -> int:
        bx, by, bz, br = self.__bots[0]
        return sum(
            1
            for x, y, z, _ in self.__bots
            if abs(x - bx) + abs(y - by) + abs(z - bz) <= br
        )

    def __get_node_prio(self, n: Node) -> tuple[int, int, int]:
        lx, hx = n.rect.x
        ly, hy = n.rect.y
        lz, hz = n.rect.z
        count = 0
        for bx, by, bz, r in self.__bots:
            d = (
                max(lx - bx, bx - hx, 0)
                + max(ly - by, by - hy, 0)
                + max(lz - bz, bz - hz, 0)
            )
            if d > r:
                count += 1
        return count, n.rect.get_zerodistance(), n.size

    def get_p2(self) -> int:
        xs = [b[0] for b in self.__bots]
        ys = [b[1] for b in self.__bots]
        zs = [b[2] for b in self.__bots]
        xlo, xhi = min(xs), max(xs)
        ylo, yhi = min(ys), max(ys)
        zlo, zhi = min(zs), max(zs)
        rect = Rect(
            (min(xlo, 0), max(xhi, 0)),
            (min(ylo, 0), max(yhi, 0)),
            (min(zlo, 0), max(zhi, 0)),
        )
        size = 1 << max(xhi, yhi, zhi).bit_length()
        start = Node(rect, size)
        u = count()
        queue: list[tuple[int, int, int, int, Node]] = []
        heappush(queue, (*self.__get_node_prio(start), next(u), start))
        result = -1
        while queue:
            *_, currentnode = heappop(queue)
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
