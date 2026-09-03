"""
2023 day 6 - Wait For It

Uses quadratic formula to calculate the two points where the score intersects the old record. One of the surprising
challenges was to round them off in the right direction, to also account for the few cases where the solution was
exactly the same value as the old record.
"""

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Race:
    time: int
    distance: int

    def get_score(self) -> int:
        minvelocity = (
            math.floor((self.time - math.sqrt(self.time**2 - (4 * self.distance))) / 2)
            + 1
        )
        maxvelocity = (
            math.ceil((self.time + math.sqrt(self.time**2 - (4 * self.distance))) / 2)
            - 1
        )
        return 1 + maxvelocity - minvelocity


class InputData:
    def __init__(self, s: str) -> None:
        t, d = s.splitlines()
        timelist = list(map(int, t.split()[1:]))
        distancelist = list(map(int, d.split()[1:]))
        self.__races = [
            Race(timelist[idx], distancelist[idx]) for idx, _ in enumerate(timelist)
        ]

    def get_p1(self) -> int:
        return math.prod([race.get_score() for race in self.__races])

    def get_p2(self) -> int:
        t = int("".join([str(race.time) for race in self.__races]))
        d = int("".join([str(race.distance) for race in self.__races]))
        megarace = Race(t, d)
        return megarace.get_score()


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
