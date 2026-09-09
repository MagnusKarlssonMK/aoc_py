"""
2020 day 5 - Binary Boarding
"""

from itertools import pairwise


def decode(s: str, up: str, low: str, rng: range) -> int:
    lower, upper = rng.start, rng.stop
    for c in s:
        if c == up:
            upper -= (1 + upper - lower) // 2
        elif c == low:
            lower += (1 + upper - lower) // 2
    return lower


def decode_seat_id(rows: str, cols: str) -> int:
    return 8 * decode(rows, "F", "B", range(127)) + decode(cols, "L", "R", range(7))


class InputData:
    def __init__(self, s: str) -> None:
        self.__boardingpasses = sorted(
            [decode_seat_id(line[0:7], line[7:10]) for line in s.splitlines()]
        )

    def get_p1(self) -> int:
        return self.__boardingpasses[-1]

    def get_p2(self) -> int:
        for sid1, sid2 in pairwise(self.__boardingpasses):
            if sid2 == sid1 + 2:
                return sid2 - 1
        return -1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
