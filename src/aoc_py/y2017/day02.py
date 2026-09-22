"""
2017 day 2 - Corruption Checksum

Part 1

Simply take the sum of the difference between the last and the first value of each list.

Part 2

Instead use itertools to find the combination of numbers in each list that yields an even division, and
accumulate the sum of the result of those divisions.
"""

from itertools import combinations


class InputData:
    def __init__(self, s: str) -> None:
        self.__nbrs = [sorted(int(n) for n in line.split()) for line in s.splitlines()]

    def get_p1(self) -> int:
        return sum([line[-1] - line[0] for line in self.__nbrs])

    def get_p2(self) -> int:
        result = 0
        for line in self.__nbrs:
            for p1, p2 in sorted(combinations(line, 2)):
                if p2 % p1 == 0:
                    result += p2 // p1
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
