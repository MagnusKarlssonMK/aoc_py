"""
2025 day 8 - Playground

Both parts run a disjoint-set (union-find) over the junction boxes, so all pairs are ordered
by squared euclidean distance up front (the square root is skipped since only the ordering
matters). Part 1 unions the closest MAX_CONNECTIONS_PART1 pairs and multiplies the sizes of
the three largest circuits. Part 2 keeps unioning in distance order until a single circuit
holds every box, returning the product of the x coordinates of the connecting pair.
"""

from dataclasses import dataclass
from itertools import combinations
from math import prod

MAX_CONNECTIONS_PART1 = 1000


@dataclass(frozen=True)
class Point3D:
    x: int
    y: int
    z: int

    @classmethod
    def from_str(cls, s: str) -> Point3D:
        x, y, z = map(int, s.split(","))
        return cls(x, y, z)

    def distance(self, other: Point3D) -> int:
        """Squared euclidean distance to another point."""
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        return dx * dx + dy * dy + dz * dz


class JunctionBox:
    def __init__(self, parent: int) -> None:
        self.parent: int = parent
        self.count: int = 1


def find(junctions: list[JunctionBox], x: int) -> int:
    """Finds the root of x, halving the path along the way."""
    while junctions[x].parent != x:
        junctions[x].parent = junctions[junctions[x].parent].parent
        x = junctions[x].parent
    return x


def union(junctions: list[JunctionBox], a: int, b: int) -> int:
    """Unions the sets containing a and b (by size) and returns the resulting size."""
    a, b = find(junctions, a), find(junctions, b)
    if a != b:
        if junctions[a].count < junctions[b].count:
            a, b = b, a
        junctions[b].parent = a
        junctions[a].count += junctions[b].count
    return junctions[a].count


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__boxes: list[Point3D] = [
            Point3D.from_str(line) for line in rawstr.splitlines()
        ]
        self.__connections: list[tuple[int, int]] = sorted(
            combinations(range(len(self.__boxes)), 2),
            key=lambda c: self.__boxes[c[0]].distance(self.__boxes[c[1]]),
        )

    def get_p1(self) -> int:
        junctions = [JunctionBox(i) for i in range(len(self.__boxes))]
        for i, j in self.__connections[:MAX_CONNECTIONS_PART1]:
            _ = union(junctions, i, j)
        return prod(sorted((j.count for j in junctions), reverse=True)[:3])

    def get_p2(self) -> int:
        junctions = [JunctionBox(i) for i in range(len(self.__boxes))]
        i = j = 0
        for i, j in self.__connections:
            if union(junctions, i, j) == len(self.__boxes):
                break
        return self.__boxes[i].x * self.__boxes[j].x


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
