"""
Stores the SNAFU value in a simple class which then implements the 'add' function, which adds two SNAFU numbers
directly without converting to/from decimal. Then simply add all the numbers read from the input data.
"""

from itertools import zip_longest
from typing import Final, override


class Snafu:
    STRTOINT_MAP: Final = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
    INTTOSTR_MAP: Final = {v: k for k, v in STRTOINT_MAP.items()}

    def __init__(self, nbrstr: str) -> None:
        self.nbr: list[int] = [self.STRTOINT_MAP[c] for c in reversed(nbrstr)]
        # Store the number "backwards" so the first number in the list is the least significant value and so on
        # That way, the index in the list will correspond to the power coefficient for that same column

    def __add__(self, other: Snafu):
        retval = Snafu("")
        combined = list(map(sum, zip_longest(self.nbr, other.nbr, fillvalue=0)))
        carry = 0
        for c in combined:
            val = carry + c
            if val > 2:
                carry = 1
            elif val < -2:
                carry = -1
            else:
                carry = 0
            retval.nbr.append(((val + 2) % 5) - 2)
        if carry != 0:
            retval.nbr.append(carry)
        return retval

    @override
    def __str__(self):
        return "".join([self.INTTOSTR_MAP[i] for i in reversed(self.nbr)])


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__snafus = [Snafu(line) for line in rawstr.splitlines()]

    def get_console_nbr(self) -> Snafu:
        result = Snafu("0")
        for sn in self.__snafus:
            result += sn
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_console_nbr())

    return p1, "-"
