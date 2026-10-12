"""
2020 day 1 - Report Repair

Keep the numbers seen so far in a set, so that each new number can be matched against
the values needed to complete the target sum without rescanning the whole list. Part 1
looks for a single such pair, while part 2 fixes one number and looks for a pair that
completes the target.
"""

from typing import Final


class InputData:
    __TARGET: Final = 2020

    def __init__(self, rawstr: str) -> None:
        self.__numbers = [int(line) for line in rawstr.splitlines()]

    def get_p1(self) -> int:
        seen: set[int] = set()
        for n in self.__numbers:
            if (other := InputData.__TARGET - n) in seen:
                return n * other
            seen.add(n)
        return -1

    def get_p2(self) -> int:
        seen: set[int] = set()
        for i, a in enumerate(self.__numbers):
            for b in self.__numbers[i + 1 :]:
                if (c := InputData.__TARGET - a - b) in seen:
                    return a * b * c
            seen.add(a)
        return -1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
