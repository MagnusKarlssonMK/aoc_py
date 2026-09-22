"""
2017 day 1 - Inverse Captcha

Part 1

Trivial, just apply a mod operation on the peek-ahead index for the wraparound at the end.

Part 2

Just change the offset in the peek-ahead from 1 to half the length of the number list.
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__nbrs = [int(c) for c in s]

    def get_captcha(self, halfway: bool = False) -> int:
        offset = 1 if not halfway else len(self.__nbrs) // 2
        return sum(
            [
                nbr
                for i, nbr in enumerate(self.__nbrs)
                if nbr == self.__nbrs[(i + offset) % len(self.__nbrs)]
            ]
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_captcha())
    if part in (None, 2):
        p2 = str(p.get_captcha(True))

    return p1, p2
