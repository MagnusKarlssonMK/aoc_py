"""
2015 day 4 - The Ideal Stocking Stuffer
"""

from hashlib import md5


class InputData:
    def __init__(self, s: str) -> None:
        self.__secretkey = s

    def get_lowest_nbr(self, nbr_zeroes: int = 5) -> int:
        suffix = 0
        while True:
            candidate = md5((self.__secretkey + str(suffix)).encode()).hexdigest()[
                :nbr_zeroes
            ]
            if int(candidate, 16) == 0:
                break
            suffix += 1
        return suffix


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_lowest_nbr())
    if part in (None, 2):
        p2 = str(p.get_lowest_nbr(6))

    return p1, p2
