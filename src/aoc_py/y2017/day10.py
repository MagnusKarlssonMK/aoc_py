"""
2017 day 10 - Knot Hash

Part 1 runs one round of reversals on the comma-separated lengths and multiplies the first two buffer values;
part 2 is the full knot hash (ASCII lengths, 64 rounds, dense xor) from util.knot.
"""

from aoc_py.util.knot import generate_hash, get_knot_hash


class InputData:
    def __init__(self, s: str) -> None:
        self.__inputstr = s

    def get_p1(self, buffer_len: int) -> int:
        lengths: list[int] = (
            [] if not self.__inputstr else [int(c) for c in self.__inputstr.split(",")]
        )
        numbers = generate_hash(lengths, buffer_len, 1)
        return numbers[0] * numbers[1]

    def get_p2(self, buffer_len: int) -> str:
        return get_knot_hash(self.__inputstr, buffer_len)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1(256))
    if part in (None, 2):
        p2 = p.get_p2(256)

    return p1, p2
