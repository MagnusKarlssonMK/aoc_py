"""
2025 day 3 - Lobby

Part 1

* Scan each row ("bank") excluding the last character (to make room for the second digit).
  Iterate character by character, from left to right, to find the value and position of the
  max number. Stop at the first 9 that is found, if any.
* Scan again (now including the last character), starting from the position after where
  the first digit was found, and similarly find the largest second digit.
* Combine the two digits to get the jolt value.

Part 2

Same as part 1, except repeat the search for digits 12 times instead of just 2.
"""

from typing import cast


class InputData:
    def __init__(self, s: str) -> None:
        self.__banks = [line for line in s.splitlines()]

    def __get_jolt(self, nbrof_digits: int) -> int:
        total = 0
        for bank in self.__banks:
            new_number = 0
            start_idx = 0
            for digit_idx in reversed(range(nbrof_digits)):
                next_digit = 0
                i = start_idx
                for x in range(i, len(bank) - digit_idx):
                    new_digit = int(bank[x])
                    if next_digit < new_digit:
                        next_digit = new_digit
                        start_idx = x + 1
                        if next_digit == 9:
                            break
                # Using cast as temporary fix for basedpyright issue with pow
                p = cast(int, 10 ** int(digit_idx))
                new_number += next_digit * p
            total += new_number
        return total

    def get_p1(self) -> int:
        return self.__get_jolt(2)

    def get_p2(self) -> int:
        return self.__get_jolt(12)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
