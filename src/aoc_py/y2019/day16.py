"""
2019 day 16 - Flawed Frequency Transmission
"""

from typing import Final

import numpy as np


class InputData:
    __BASE_PATTERN: Final = [0, 1, 0, -1]
    __NBR_OF_PHASES: Final = 100
    __P2_REPEATS: Final = 10_000

    def __init__(self, s: str) -> None:
        self.__nbrs = [int(c) for c in s]

    def get_p1(self) -> str:
        nbrs = np.array(self.__nbrs)
        base_pattern = np.array(self.__BASE_PATTERN)
        patterns = np.zeros((nbrs.size, nbrs.size), int)
        for i in range(1, nbrs.size + 1):
            den = (i * base_pattern.size) - 1
            count = (nbrs.size + den - 1) // den
            patterns[i - 1, :] = np.tile(np.repeat(base_pattern, i), count)[
                1 : 1 + nbrs.size
            ]
        for _ in range(self.__NBR_OF_PHASES):
            nbrs = np.abs((nbrs * patterns).sum(axis=1)) % 10
        return "".join(map(str, nbrs[:8]))

    def get_p2(self) -> str:
        nbrs = np.array(self.__nbrs)
        offset = int("".join(map(str, nbrs[:7])))
        o_s = np.tile(nbrs, self.__P2_REPEATS)[offset:]
        for _ in range(self.__NBR_OF_PHASES):
            o_s = np.cumsum(o_s[::-1])[::-1] % 10
        return "".join(map(str, o_s[:8]))


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
