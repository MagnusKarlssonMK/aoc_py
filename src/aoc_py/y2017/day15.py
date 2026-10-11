"""
2017 day 15 - Dueling Generators

Each generator is a linear congruential generator producing a 31-bit value, and the judge compares only the
low 16 bits. Part 1 judges 40 million consecutive pairs. Part 2 judges the first 5 million pairs where
generator A's value is a multiple of 4 and generator B's is a multiple of 8, with the two streams filtered
independently.

The pair counts are parameters so tests can judge a small number of pairs quickly; the real solver uses the
puzzle's defaults.
"""

from typing import Final

_FACTORS: Final = (16807, 48271)
_MULTIPLES: Final = (4, 8)
_DIVISOR: Final = 2147483647
_PAIRS: Final = (40_000_000, 5_000_000)


class InputData:
    def __init__(self, s: str) -> None:
        self.__startvalues = [int(line.split()[-1]) for line in s.splitlines()]

    def __judge(self, pairs: int, use_multiples: bool) -> int:
        a, b = self.__startvalues
        fa, fb = _FACTORS
        ma, mb = _MULTIPLES
        divisor = _DIVISOR
        matches = 0
        if use_multiples:
            for _ in range(pairs):
                a = a * fa % divisor
                while a % ma != 0:
                    a = a * fa % divisor
                b = b * fb % divisor
                while b % mb != 0:
                    b = b * fb % divisor
                if (a & 0xFFFF) == (b & 0xFFFF):
                    matches += 1
        else:
            for _ in range(pairs):
                a = a * fa % divisor
                b = b * fb % divisor
                if (a & 0xFFFF) == (b & 0xFFFF):
                    matches += 1
        return matches

    def get_p1(self, pairs: int = _PAIRS[0]) -> int:
        return self.__judge(pairs, False)

    def get_p2(self, pairs: int = _PAIRS[1]) -> int:
        return self.__judge(pairs, True)


def solve_parts(
    inputdata: str, part: int | None = None, pairs: tuple[int, int] | None = None
) -> tuple[str, str]:
    """pairs overrides the default judge counts, letting tests run a small number of pairs quickly."""
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1(pairs[0] if pairs else _PAIRS[0]))
    if part in (None, 2):
        p2 = str(p.get_p2(pairs[1] if pairs else _PAIRS[1]))

    return p1, p2
