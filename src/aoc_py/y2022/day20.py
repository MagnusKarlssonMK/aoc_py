"""
2022 day 20 - Grove Positioning System
"""

from collections import deque
from typing import Final


class InputData:
    __GROVE_COORDINATES: Final = (1000, 2000, 3000)
    __ENCRYPTION_KEY: Final = 811589153
    __MIX_COUNT: Final = 10

    def __init__(self, s: str) -> None:
        self.__startnbrs = list(map(int, s.splitlines()))

    def __mix(self, count: int = 1) -> list[int]:
        nbrs = deque(list(enumerate(list(self.__startnbrs))))
        nbrs_len = len(nbrs)
        for _ in range(count):
            for idx in range(nbrs_len):
                while nbrs[0][0] != idx:
                    nbrs.rotate(-1)
                i, v = nbrs.popleft()
                nbrs.rotate(-(v % (nbrs_len - 1)))
                nbrs.append((i, v))
        return [v for _, v in nbrs]

    def get_p1(self) -> int:
        mixed_nbrs = self.__mix()
        return sum(
            [
                mixed_nbrs[(mixed_nbrs.index(0) + n) % len(mixed_nbrs)]
                for n in InputData.__GROVE_COORDINATES
            ]
        )

    def get_p2(self) -> int:
        for i, n in enumerate(self.__startnbrs):
            self.__startnbrs[i] = n * InputData.__ENCRYPTION_KEY
        mixed_nbrs = self.__mix(InputData.__MIX_COUNT)
        return sum(
            [
                mixed_nbrs[(mixed_nbrs.index(0) + n) % len(mixed_nbrs)]
                for n in InputData.__GROVE_COORDINATES
            ]
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
