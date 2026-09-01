"""
2024 day 10 - Hoof It
"""
from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__grid = Grid(rawstr)
        self.__trailheads = [p for p in self.__grid.find_all("0")]

    def get_score_and_rating(self) -> tuple[int, int]:
        score = rating = 0
        for head in self.__trailheads:
            peaks: set[Point] = set()
            queue = [head]
            while queue:
                current = queue.pop(0)
                if self.__grid.get_element(current) == "9":
                    peaks.add(current)
                    rating += 1
                else:
                    for direction in Directions.NEIGHBORS_STRAIGHT:
                        neighbor = current + direction
                        if (c := self.__grid.get_element(neighbor)) != "" and int(c) == int(self.__grid.get_element(current)) + 1:
                            queue.append(neighbor)
            score += len(peaks)
        return score, rating


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
        p1, p2 = "-1"
        p = InputData(inputdata)
        r1, r2 = p.get_score_and_rating()
        if part in (None, 1):
            p1 = str(r1)
        if part in (None, 2):
            p2 = str(r2)

        return p1, p2
