"""
2015 day 25 - Let It Snow

The manual's code grid is filled one diagonal at a time from bottom-left to top-right: diagonal d holds (d, 1),
(d-1, 2), ..., (1, d), and each cell takes the next code of the sequence. The sequence starts at 20151125 and
each successive code is the previous one times 252533, modulo 33554393. Row and column therefore only decide
where a cell sits in that order, so a triangular number gives the cell's 0-based index and a single modular
exponentiation produces its code, rather than generating every code up to that position. The requested row and
column are the only input.
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
        """Uses triangular number calculation (n*(n+1))/2 to get the index, and then modular exponentiation for generating the code."""
        n = self.__col + self.__row - 1
        triangle_row = (n * (n + 1)) // 2
        index = triangle_row - self.__row

        return (
            self.__START_CODE * pow(self.__MULTIPLIER, index, self.__DIVISOR)
        ) % self.__DIVISOR


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_code())
    if part in (None, 2):
        p2 = "-"

    return p1, p2
