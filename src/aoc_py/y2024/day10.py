"""
2024 day 10 - Hoof It

Each trailhead ('0') is walked uphill one step at a time to every reachable peak ('9').
The score counts the distinct peaks reachable from a trailhead, while the rating counts
the number of distinct trails, so the walk visits every path rather than stopping at the
first one.
"""

from collections import deque

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__grid = Grid(rawstr)
        self.__trailheads = self.__grid.find_all("0")

    def get_score_and_rating(self) -> tuple[int, int]:
        score = rating = 0
        for head in self.__trailheads:
            peaks: set[Point] = set()
            queue = deque([head])
            while queue:
                current = queue.popleft()
                current_elevation = int(self.__grid.get_element(current))
                if current_elevation == 9:
                    peaks.add(current)
                    rating += 1
                else:
                    for neighbor in [
                        current + d for d in Directions.NEIGHBORS_STRAIGHT
                    ]:
                        if (c := self.__grid.get_element(neighbor)) != "" and int(
                            c
                        ) == current_elevation + 1:
                            queue.append(neighbor)
            score += len(peaks)
        return score, rating


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_score_and_rating()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
