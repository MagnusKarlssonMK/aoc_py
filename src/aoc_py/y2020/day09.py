"""
2020 day 9 - Encoding Error

Part 1

Straightforward - just search the preamble for a valid combination of two numbers that adds up to the following
number, and gradually move the preamble forwards until an invalid number is found.

Part 2

Scan through the list with a window in the form of a queue, adding numbers from the list until its sum is
larger than the target value, then popping the oldest values from the window until it is again smaller. Break when
the sum is equal to the target value, sort the values in the window and get the answer from the sum of the smallest
and the largest value.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Number:
    value: int

    def validatenumber(self, preamble: list[int]) -> bool:
        for i in range(len(preamble) - 1):
            for j in range(i + 1, len(preamble)):
                if preamble[i] + preamble[j] == self.value:
                    return True
        return False


class InputData:
    __preamble_length = 25

    def __init__(self, rawstr: str) -> None:
        self.__nbrs = [Number(int(c)) for c in rawstr.splitlines()]
        self.__invalid_nbr = -1
        if len(self.__nbrs) < 25:
            InputData.__preamble_length = 5  # Assume test input for smaller inputs

    def get_p1(self) -> int:
        preamble = [self.__nbrs[i].value for i in range(InputData.__preamble_length)]
        for i in range(InputData.__preamble_length, len(self.__nbrs)):
            if not self.__nbrs[i].validatenumber(preamble):
                self.__invalid_nbr = self.__nbrs[i].value
                break
            _ = preamble.pop(0)
            preamble.append(self.__nbrs[i].value)
        return self.__invalid_nbr

    def get_p2(self) -> int:
        window = [self.__nbrs[0].value]
        idx = 0
        result = 0
        while idx < len(self.__nbrs):
            if (wsum := sum(window)) == self.__invalid_nbr:
                windowsort = sorted(window)
                result = windowsort[0] + windowsort[-1]
                break
            if wsum > self.__invalid_nbr:
                _ = window.pop(0)
            else:
                idx += 1
                window.append(self.__nbrs[idx].value)
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    r1 = p.get_p1()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
