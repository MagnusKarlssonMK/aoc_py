"""
2021 day 11 - Dumbo Octopus

Use recursion to update all adjacent nodes when incrementing a node and it flashes.
"""

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point


class InputData:
    def __init__(self, s: str) -> None:
        self.__grid = Grid(s)
        self.__flashed: set[Point] = set()

    def __take_step(self) -> int:
        for p in [self.__grid.get_point(i) for i, _ in enumerate(self.__grid.elements)]:
            if p not in self.__flashed:
                self.__increment(p)
        flashed = len(self.__flashed)
        self.__flashed = set()
        return flashed

    def __increment(self, p: Point) -> None:
        if p not in self.__flashed:
            if (v := int(self.__grid.get_element(p))) < 9:
                self.__grid.set_point(p, str(v + 1))
            else:
                self.__grid.set_point(p, "0")
                self.__flashed.add(p)
                for adjacent in [
                    p + d
                    for d in Directions.NEIGHBORS_ALL
                    if self.__grid.get_element(p + d) != ""
                ]:
                    self.__increment(adjacent)

    def get_flashcounts(self) -> tuple[int, int]:
        max_flashes = self.__grid.x_max * self.__grid.y_max
        step_count = 0
        p1 = 0
        while (flashes := self.__take_step()) < max_flashes:
            step_count += 1
            if step_count <= 100:
                p1 += flashes
        return p1, step_count + 1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_flashcounts()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
