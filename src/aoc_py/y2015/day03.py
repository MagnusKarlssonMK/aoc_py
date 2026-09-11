"""
2015 day 3 - Perfectly Spherical Houses in a Vacuum
"""

from typing import Final

from aoc_py.util.point import Directions


class InputData:
    __DIRMAP: Final = {
        "^": Directions.UP,
        ">": Directions.RIGHT,
        "v": Directions.DOWN,
        "<": Directions.LEFT,
    }

    def __init__(self, s: str) -> None:
        self.__steps = [self.__DIRMAP[c] for c in s]

    def get_p1(self) -> int:
        santa = Directions.ORIGIN
        visited = {santa}
        for step in self.__steps:
            santa += step
            visited.add(santa)
        return len(visited)

    def get_p2(self) -> int:
        santa = Directions.ORIGIN
        robotsanta = Directions.ORIGIN
        visited = {santa}
        for i, step in enumerate(self.__steps):
            if i % 2 == 0:
                santa += step
                visited.add(santa)
            else:
                robotsanta += step
                visited.add(robotsanta)
        return len(visited)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
