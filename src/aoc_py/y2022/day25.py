"""
2022 day 25 - Full of Hot Air

SNAFU numbers are added column by column, without ever converting to or from decimal. Each digit is kept at its decimal
value (0, 1, 2, -1, -2), and adding one column from each number plus the carry gives a value in [-5, 5]. Folding that
back into a base-5 digit and a -1/0/1 carry is just ((value + 2) mod 5) - 2. The console number is the sum of every
line. Part 2 has no puzzle of its own, so it is reported as "-".
"""

from itertools import zip_longest
from typing import Final, override

_STR_TO_INT: Final[dict[str, int]] = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
_INT_TO_STR: Final[dict[int, str]] = {v: k for k, v in _STR_TO_INT.items()}


class Snafu:
    def __init__(self, nbrstr: str) -> None:
        # Store the number backwards, so index i holds the coefficient for the 5**i column.
        self.__nbr: list[int] = [_STR_TO_INT[c] for c in reversed(nbrstr)]

    def __add__(self, other: Snafu) -> Snafu:
        retval = Snafu("")
        combined = list(map(sum, zip_longest(self.__nbr, other.__nbr, fillvalue=0)))
        carry = 0
        for c in combined:
            val = carry + c
            if val > 2:
                carry = 1
            elif val < -2:
                carry = -1
            else:
                carry = 0
            retval.__nbr.append(((val + 2) % 5) - 2)
        if carry != 0:
            retval.__nbr.append(carry)
        return retval

    @override
    def __str__(self) -> str:
        return "".join(_INT_TO_STR[i] for i in reversed(self.__nbr))


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__snafus = [Snafu(line) for line in rawstr.splitlines()]

    def get_console_number(self) -> Snafu:
        result = Snafu("0")
        for sn in self.__snafus:
            result += sn
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_console_number())
    if part in (None, 2):
        p2 = "-"

    return p1, p2
