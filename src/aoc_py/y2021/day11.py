"""
2021 day 11 - Dumbo Octopus

Use recursion to update all adjacent nodes when incrementing a node and it flashes.
A single run of the grid serves both parts. The octopuses keep flashing after the step
on which the whole grid goes off, so part 1 has to keep stepping to 100 even once part
2's answer is known.
"""

from typing import Final

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point

P1_NBR_STEPS: Final = 100


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__rawstr = rawstr
        self.__grid = Grid(rawstr)
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
        """Returns the number of flashes over the first 100 steps and the number of the
        first step on which every octopus flashes at once."""
        self.__grid = Grid(self.__rawstr)
        max_flashes = self.__grid.x_max * self.__grid.y_max
        p1 = 0
        p2 = 0
        step_count = 0
        while p2 == 0 or step_count < P1_NBR_STEPS:
            step_count += 1
            flashes = self.__take_step()
            if step_count <= P1_NBR_STEPS:
                p1 += flashes
            if p2 == 0 and flashes == max_flashes:
                p2 = step_count
        return p1, p2


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_flashcounts()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
