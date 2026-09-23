"""
2017 day 15 - Dueling Generators

Just making a simple iterator and compare the generated values. Basically brute force, so
takes a fair amount of time to run (~10s for each part).
"""

from collections.abc import Generator
from typing import Final


class InputData:
    __FACTORS: Final = (16807, 48271)
    __MULTIPLES: Final = (4, 8)
    __DIVISOR: Final = 2147483647

    def __init__(self, s: str) -> None:
        self.__startvalues = [
            int(w[-1]) for w in [line.split() for line in s.splitlines()]
        ]

    def __generator(self, idx: int, use_multiples: bool = False) -> Generator[int]:
        v = self.__startvalues[idx]
        m = InputData.__MULTIPLES[idx] if use_multiples else 1
        while True:
            v = v * InputData.__FACTORS[idx] % InputData.__DIVISOR
            if v % m == 0:
                yield v & 0xFFFF

    def get_p1(self) -> int:
        generators = [self.__generator(i) for i, _ in enumerate(self.__startvalues)]
        return sum(
            [1 for _ in range(40_000_000) if next(generators[0]) == next(generators[1])]
        )

    def get_p2(self) -> int:
        generators = [
            self.__generator(i, True) for i, _ in enumerate(self.__startvalues)
        ]
        return sum(
            [1 for _ in range(5_000_000) if next(generators[0]) == next(generators[1])]
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
