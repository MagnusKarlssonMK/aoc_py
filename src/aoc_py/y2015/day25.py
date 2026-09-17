"""
2015 day 25 - Let It Snow

A simple function to translate the input coordinate to code number according to the diagonally generated table in the
description text. This is then used to determine how many times to re-calculate the starting value, which will give
the answer.
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

    def __get_code_nbr(self) -> int:
        """Calculates the value according to the diagonally generated table."""
        nbr = sum(n for n in range(self.__col + 1))
        nbr += sum(n for n in range(self.__col, self.__col + self.__row - 1))
        return nbr

    def get_code(self) -> int:
        """Performs X recalculations of the start code, where X is given by the code number."""
        code_nbr = self.__get_code_nbr()
        code = InputData.__START_CODE
        for _ in range(code_nbr - 1):
            code = (code * InputData.__MULTIPLIER) % InputData.__DIVISOR
        return code


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_code())
    if part in (None, 2):
        p2 = "-"

    return p1, p2
