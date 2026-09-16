"""
2015 day 18 - Like a GIF For Your Yard

Pretty much brute force; not fast.
"""

from collections import deque
from copy import deepcopy

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point


class InputData:
    def __init__(self, s: str) -> None:
        self.__grid = Grid(s)
        self.__corners = [
            Directions.ORIGIN,
            Point(self.__grid.x_max - 1, 0),
            Point(0, self.__grid.y_max - 1),
            Point(self.__grid.x_max - 1, self.__grid.y_max - 1),
        ]
        # Assume test input if small grid
        self.__nbr_steps: int = 4 if len(self.__grid.elements) < 40 else 100

    def get_p1(self) -> int:
        # changed: list[tuple[Point, str]] = []
        changed = deque()
        current_grid = deepcopy(self.__grid)
        for _ in range(self.__nbr_steps):
            for i, c in enumerate(current_grid.elements):
                p = current_grid.get_point(i)
                neighbors_on = sum(
                    1 if current_grid.get_element(n) == "#" else 0
                    for n in [p + d for d in Directions.NEIGHBORS_ALL]
                )
                if c == "#":
                    if neighbors_on not in range(2, 4):
                        changed.append((p, "."))
                elif neighbors_on == 3:
                    changed.append((p, "#"))
            while len(changed) > 0:
                p, c = changed.pop()
                current_grid.set_point(p, c)
        return sum(1 if c == "#" else 0 for c in current_grid.elements)

    def get_p2(self) -> int:
        # changed: list[tuple[Point, str]] = []
        changed = deque()
        current_grid = deepcopy(self.__grid)
        for corner in self.__corners:
            current_grid.set_point(corner, "#")
        for _ in range(self.__nbr_steps):
            for i, c in enumerate(current_grid.elements):
                p = current_grid.get_point(i)
                if p in self.__corners:
                    continue
                neighbors_on = sum(
                    1 if current_grid.get_element(n) == "#" else 0
                    for n in [p + d for d in Directions.NEIGHBORS_ALL]
                )
                if c == "#":
                    if neighbors_on not in range(2, 4):
                        changed.append((p, "."))
                elif neighbors_on == 3:
                    changed.append((p, "#"))
            while len(changed) > 0:
                p, c = changed.pop()
                current_grid.set_point(p, c)
        return sum(1 if c == "#" else 0 for c in current_grid.elements)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
