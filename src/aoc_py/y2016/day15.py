"""
2016 day 15 - Timing is Everything

Disc d (numbered from 1) has n positions and starts at position p, so it is at the goal at time t when
(p + t + d) % n == 0, i.e. t == -(p + d) (mod n). The input's position counts are pairwise coprime, so the
button-press time is the Chinese remainder of those congruences. The inverse in the CRT is the builtin
pow(a, -1, m); Part 2 adds an extra 11-position disc starting at position 0.
"""

import math
import re
from dataclasses import dataclass


def chinese_remainder(moduli: list[int], remainders: list[int]) -> int:
    prod = math.prod(moduli)
    result = 0
    for n, r in zip(moduli, remainders):
        partial = prod // n
        result += r * pow(partial, -1, n) * partial
    return result % prod


@dataclass
class Disc:
    nbr_positions: int
    start_position: int


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__discs = {
            i: Disc(n, p)
            for i, n, _, p in (
                map(int, re.findall(r"\d+", line)) for line in rawstr.splitlines()
            )
        }

    def get_buttonpress_time(self, extra_disc: bool = False) -> int:
        discs = dict(self.__discs)
        if extra_disc:
            discs[len(discs) + 1] = Disc(11, 0)
        moduli = [discs[d].nbr_positions for d in discs]
        remainders = [
            discs[d].nbr_positions
            - (discs[d].start_position + d) % discs[d].nbr_positions
            for d in discs
        ]
        return chinese_remainder(moduli, remainders)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_buttonpress_time())
    if part in (None, 2):
        p2 = str(p.get_buttonpress_time(True))

    return p1, p2
