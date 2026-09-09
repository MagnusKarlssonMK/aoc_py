"""
2020 day 1 - Report Repair

Simply loop through the list of numbers with 2/3 indices to check all combinations until a match is found.
"""

from typing import Final


class InputData:
    __TARGET: Final = 2020

    def __init__(self, s: str) -> None:
        self.__numbers = [int(line) for line in s.splitlines()]

    def get_p1(self) -> int:
        for i in range(len(self.__numbers) - 1):
            for j in range(i + 1, len(self.__numbers)):
                if self.__numbers[i] + self.__numbers[j] == InputData.__TARGET:
                    return self.__numbers[i] * self.__numbers[j]
        return -1

    def get_p2(self) -> int:
        for i in range(len(self.__numbers) - 2):
            for j in range(i + 1, len(self.__numbers) - 1):
                if (
                    pairsum := self.__numbers[i] + self.__numbers[j]
                ) < InputData.__TARGET:
                    for k in range(j + 1, len(self.__numbers)):
                        if pairsum + self.__numbers[k] == InputData.__TARGET:
                            return (
                                self.__numbers[i]
                                * self.__numbers[j]
                                * self.__numbers[k]
                            )
        return -1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
