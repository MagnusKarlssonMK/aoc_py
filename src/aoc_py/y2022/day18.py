"""
2022 day 18 - Boiling Boulders
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

    def get_additional_air(self) -> Generator[Point3d]:
        for d in (
            (0, 1, 1),
            (0, 1, -1),
            (0, -1, 1),
            (0, -1, -1),
            (1, 0, 1),
            (-1, 0, 1),
            (1, 0, -1),
            (-1, 0, -1),
            (1, 1, 0),
            (-1, 1, 0),
            (1, -1, 0),
            (-1, -1, 0),
        ):
            yield self + Point3d(*d)

    def __add__(self, other: Point3d) -> Point3d:
        return Point3d(self.x + other.x, self.y + other.y, self.z + other.z)


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__adj: dict[Point3d, set[Point3d]] = {}
        for point in [
            Point3d(*list(map(int, line.split(",")))) for line in rawstr.splitlines()
        ]:
            self.__adj[point] = set()
        start = Point3d(999, 999, 999)
        air: set[Point3d] = set()
        for point in self.__adj:
            for adj in point.get_adjacent():
                if adj not in self.__adj:
                    self.__adj[point].add(adj)
                    air.add(adj)
                    if adj.x < start.x:
                        start = adj
            for additional_air in point.get_additional_air():
                if additional_air not in self.__adj:
                    air.add(additional_air)
        # Use BFS on the air from the start point which is guaranteed to be exterior, and any unreachable points are
        # interior pockets.
        queue = [start]
        seen: set[Point3d] = set()
        while queue:
            current = queue.pop(0)
            if current in seen:
                continue
            seen.add(current)
            for adj_air in current.get_adjacent():
                if adj_air in air:
                    queue.append(adj_air)
            air.remove(current)
        # Calculate number of points representing enclosed air
        self.__enclosed_air = 0
        for point in self.__adj:
            for a in air:
                if a in self.__adj[point]:
                    self.__enclosed_air += 1

    def get_surface_area(self, remove_interior: bool = False) -> int:
        result = sum([len(adj) for adj in list(self.__adj.values())])
        if remove_interior:
            result -= self.__enclosed_air
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_surface_area())
    if part in (None, 2):
        p2 = str(p.get_surface_area(True))

    return p1, p2
