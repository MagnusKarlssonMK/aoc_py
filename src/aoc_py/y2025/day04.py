"""
2025 day 4 - Printing Department

Every point holding paper ('@') is queued up once, so only those points need their neighbors
scanned. Part 1 counts the paper points with fewer than four paper neighbors.

Part 2 is not a game of life: paper never grows back, so there is no need to work in rounds.
Identified points are cleared immediately and their still-paper neighbors are pushed back onto
the queue for re-evaluation; when the queue drains, the remaining paper is counted.
"""

from collections import deque
from copy import deepcopy
from typing import Final

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point

PAPER: Final = "@"
NOT_PAPER: Final = "."


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__paper_map: Grid = Grid(rawstr)

    def get_p1(self) -> int:
        total = 0
        paper_points: deque[Point] = deque(
            self.__paper_map.get_point(i)
            for i, e in enumerate(self.__paper_map.elements)
            if e == PAPER
        )
        while paper_points:
            p = paper_points.popleft()
            neighbors = sum(
                1
                for n in [p + d for d in Directions.NEIGHBORS_ALL]
                if self.__paper_map.get_element(n) == PAPER
            )
            if neighbors < 4:
                total += 1
        return total

    def get_p2(self) -> int:
        total = 0
        paper_map = deepcopy(self.__paper_map)
        paper_points: deque[Point] = deque(
            self.__paper_map.get_point(i)
            for i, e in enumerate(self.__paper_map.elements)
            if e == PAPER
        )
        while paper_points:
            p = paper_points.popleft()
            if paper_map.get_element(p) != PAPER:
                # The point has already been cleared after this entry got added to the queue
                continue
            neighbors: list[Point] = [
                n
                for n in [p + d for d in Directions.NEIGHBORS_ALL]
                if paper_map.get_element(n) == PAPER
            ]
            if len(neighbors) < 4:
                total += 1
                paper_map.set_point(p, NOT_PAPER)
                paper_points.extend(neighbors)
        return total


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
