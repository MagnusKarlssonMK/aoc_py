"""
2020 day 5 - Binary Boarding

A boarding pass code maps directly onto its seat id in binary: F and L are 0 while B and R
are 1, so translating the letters and parsing the result as a base-2 number gives the id.
"""

from itertools import pairwise
from typing import Final

_SEAT_MAP: Final = str.maketrans("FBLR", "0101")


def decode_seat_id(code: str) -> int:
    return int(code.translate(_SEAT_MAP), 2)


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__boardingpasses = sorted(
            decode_seat_id(line) for line in rawstr.splitlines()
        )

    def get_p1(self) -> int:
        return self.__boardingpasses[-1]

    def get_p2(self) -> int:
        for sid1, sid2 in pairwise(self.__boardingpasses):
            if sid2 == sid1 + 2:
                return sid2 - 1
        return -1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
