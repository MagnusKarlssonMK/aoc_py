"""
2020 day 13 - Shuttle Search

Solved using the Chinese Remainder Theorem, and making use of the fact that the id:s are pairwise coprime.
"""


class InputData:
    def __init__(self, s: str) -> None:
        estimate, buslist = s.splitlines()
        self.__estimate = int(estimate)
        self.__buslist = [
            (int(v), i) for i, v in enumerate(buslist.split(",")) if v != "x"
        ]

    def get_p1(self) -> int:
        bestbus = min(
            [(busid, busid - (self.__estimate % busid)) for busid, _ in self.__buslist],
            key=lambda x: x[1],
        )
        return bestbus[0] * bestbus[1]

    def get_p2(self) -> int:
        remainder = 0
        coefficient = 1
        for busid, idx in self.__buslist:
            for i in range(1, busid):
                if (coefficient * i) % busid == 1:
                    remainder = (
                        (((-idx % busid) - remainder) * i) % busid
                    ) * coefficient + remainder
                    coefficient *= busid
                    break
        return remainder


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
