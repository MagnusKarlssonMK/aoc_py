"""
2017 day 2 - Corruption Checksum

Part 1

Each row is sorted, so simply take the sum of the difference between the last (max) and the first (min) value of
each row.

Part 2

Instead use itertools to find the unique pair in each row that divides evenly, and accumulate the quotients.
"""

from itertools import combinations


class InputData:
    def __init__(self, s: str) -> None:
        self.__rows = [sorted(int(n) for n in line.split()) for line in s.splitlines()]

    def get_p1(self) -> int:
        return sum(line[-1] - line[0] for line in self.__rows)

    def get_p2(self) -> int:
        result = 0
        for line in self.__rows:
            for small, large in combinations(line, 2):
                if large % small == 0:
                    result += large // small
                    break
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
