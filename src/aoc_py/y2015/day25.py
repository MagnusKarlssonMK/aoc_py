"""
2015 day 25 - Let It Snow
"""


class InputData:
    __START_CODE = 20151125
    __MULTIPLIER = 252533
    __DIVISOR = 33554393

    def __init__(self, s: str) -> None:
        _, right = s.rstrip(".").split("row ")
        row, col = right.split(", column ")
        self.__row = int(row)
        self.__col = int(col)

    def get_code(self) -> int:
        """Uses triangular number calculation (n*(n+1))/2 to get the index, and then modular-pow for generating the code."""
        n = self.__col + self.__row - 1
        triangle_row = (n * (n + 1)) // 2
        index = triangle_row - self.__row

        return (
            self.__START_CODE * mod_pow(self.__MULTIPLIER, index, self.__DIVISOR)
        ) % self.__DIVISOR


def mod_pow(base: int, exp: int, modulus: int) -> int:
    result = 1
    while exp > 0:
        if exp & 1 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exp >>= 1
    return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_code())
    if part in (None, 2):
        p2 = "-"

    return p1, p2
