"""
2022 day 18 - Boiling Boulders

Each cube face without a neighbouring cube contributes one unit of surface area, giving part 1 directly.
For part 2 the faces that border enclosed air are removed: a flood-fill from just outside the bounding box
marks every air cell connected to the outside, so an exposed face whose air neighbour is never reached must
border an interior pocket.
"""

from collections.abc import Generator
from dataclasses import dataclass


@dataclass(frozen=True)
class Point3d:
    x: int
    y: int
    z: int

    def get_adjacent(self) -> Generator[Point3d]:
        for d in ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)):
            yield self + Point3d(*d)

    def __add__(self, other: Point3d) -> Point3d:
        return Point3d(self.x + other.x, self.y + other.y, self.z + other.z)


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__exposed: dict[Point3d, set[Point3d]] = {}
        for line in rawstr.splitlines():
            self.__exposed[Point3d(*map(int, line.split(",")))] = set()
        for point in self.__exposed:
            for adj in point.get_adjacent():
                if adj not in self.__exposed:
                    self.__exposed[point].add(adj)
        # Flood-fill the exterior from just outside the bounding box. Every exposed face whose air
        # neighbour is never reached borders an enclosed pocket and must not count for part 2.
        lower = Point3d(
            min(p.x for p in self.__exposed) - 1,
            min(p.y for p in self.__exposed) - 1,
            min(p.z for p in self.__exposed) - 1,
        )
        upper = Point3d(
            max(p.x for p in self.__exposed) + 1,
            max(p.y for p in self.__exposed) + 1,
            max(p.z for p in self.__exposed) + 1,
        )
        seen: set[Point3d] = {lower}
        queue = [lower]
        while queue:
            current = queue.pop(0)
            for adj in current.get_adjacent():
                if (
                    lower.x <= adj.x <= upper.x
                    and lower.y <= adj.y <= upper.y
                    and lower.z <= adj.z <= upper.z
                    and adj not in self.__exposed
                    and adj not in seen
                ):
                    seen.add(adj)
                    queue.append(adj)
        self.__enclosed_air = sum(
            1
            for point in self.__exposed
            for a in self.__exposed[point]
            if a not in seen
        )

    def get_surface_area(self, remove_interior: bool = False) -> int:
        result = sum([len(adj) for adj in list(self.__exposed.values())])
        if remove_interior:
            result -= self.__enclosed_air
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_surface_area())
    if part in (None, 2):
        p2 = str(p.get_surface_area(True))

    return p1, p2
