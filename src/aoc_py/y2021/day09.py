"""
2021 day 9 - Smoke Basin

Create methods to find the low point coordinates and basin coordinates of the input grid.
The latter uses a stripped down BFS to find any adjacent neighbor until value '9' is found.
This assumes (as also stated in the problem description) that all low points will be
surrounded by 9:s and not connected to any other low point.
"""

from collections.abc import Generator

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point


class InputData:
    def __init__(self, s: str) -> None:
        self.__grid = Grid(s)
        self.__lowpoints = {p for p in self.__find_low_points()}

    def __find_low_points(self) -> Generator[Point]:
        for i, c in enumerate(self.__grid.elements):
            p = self.__grid.get_point(i)
            for n in [p + d for d in Directions.NEIGHBORS_STRAIGHT]:
                if (n_c := self.__grid.get_element(n)) != "" and int(c) >= int(n_c):
                    break
            else:
                yield p

    def __find_basin_points(self, lowpoint: Point) -> set[Point]:
        seen: set[Point] = set()
        queue = [lowpoint]
        while queue:
            p = queue.pop(0)
            if p in seen:
                continue
            seen.add(p)
            for n in [p + d for d in Directions.NEIGHBORS_STRAIGHT]:
                if (
                    n not in seen
                    and (n_c := self.__grid.get_element(n)) != ""
                    and int(n_c) < 9
                ):
                    queue.append(n)
        return seen

    def get_p1(self) -> int:
        return sum([int(self.__grid.get_element(p)) + 1 for p in self.__lowpoints])

    def get_p2(self) -> int:
        basin_sizelist = sorted(
            [len(self.__find_basin_points(p)) for p in self.__lowpoints], reverse=True
        )
        return basin_sizelist[0] * basin_sizelist[1] * basin_sizelist[2]


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
