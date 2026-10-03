"""
2022 day 20 - Grove Positioning System

Every number is tagged with its original position so that repeated values stay distinct. Decrypting walks the
original positions in order, cuts each number out of the circle and reinserts it the number of places given by
its own value, wrapping around modulo the length of the list without it. Part 2 first multiplies every number by
the encryption key and then mixes ten times. The grove coordinates are the values 1000, 2000 and 3000 places past
the 0.
"""

from typing import Final


class InputData:
    __GROVE_COORDINATES: Final = (1000, 2000, 3000)
    __ENCRYPTION_KEY: Final = 811589153
    __MIX_COUNT: Final = 10

    def __init__(self, s: str) -> None:
        self.__startnbrs = list(map(int, s.splitlines()))

    def __mix(self, values: list[int], count: int = 1) -> list[int]:
        tagged: list[tuple[int, int]] = list(enumerate(values))
        nbrs_len = len(values)
        for _ in range(count):
            for idx in range(nbrs_len):
                value = values[idx]
                pos = tagged.index((idx, value))
                del tagged[pos]
                tagged.insert((pos + value) % (nbrs_len - 1), (idx, value))
        return [value for _, value in tagged]

    def __grove_sum(self, mixed_nbrs: list[int]) -> int:
        zero = mixed_nbrs.index(0)
        return sum(
            mixed_nbrs[(zero + n) % len(mixed_nbrs)]
            for n in InputData.__GROVE_COORDINATES
        )

    def get_p1(self) -> int:
        return self.__grove_sum(self.__mix(self.__startnbrs))

    def get_p2(self) -> int:
        scaled = [n * InputData.__ENCRYPTION_KEY for n in self.__startnbrs]
        return self.__grove_sum(self.__mix(scaled, InputData.__MIX_COUNT))


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
