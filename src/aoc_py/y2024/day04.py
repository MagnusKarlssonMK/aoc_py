"""
2024 day 4 - Ceres Search

Part 1

Scan the grid and investigate all nodes containing an 'X', and look in all
eight directions and see if XMAS is created.

Part 2

This time, scan for nodes containing an 'A' instead, form words from the
combination with the diagonal nodes to form the X, and see if the generated
word is eithes MAS or SAM.
"""


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__grid = [[c for c in line] for line in rawstr.splitlines()]
        self.__height = len(self.__grid)
        self.__width = len(self.__grid[0])

    def __get_grid_value(self, row: int, col: int) -> str:
        if row in range(self.__height) and col in range(self.__width):
            return self.__grid[row][col]
        return "."

    def get_p1(self) -> int:
        DIRECTIONS = (
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
        )
        total = 0
        for row, line in enumerate(self.__grid):
            for col, c in enumerate(line):
                if c == "X":
                    for d_row, d_col in DIRECTIONS:
                        if (
                            "X"
                            + self.__get_grid_value(row + d_row, col + d_col)
                            + self.__get_grid_value(row + 2 * d_row, col + 2 * d_col)
                            + self.__get_grid_value(row + 3 * d_row, col + 3 * d_col)
                            == "XMAS"
                        ):
                            total += 1
        return total

    def get_p2(self) -> int:
        total = 0
        for row, line in enumerate(self.__grid):
            for col, c in enumerate(line):
                if c == "A":
                    word1 = (
                        self.__get_grid_value(row - 1, col - 1)
                        + "A"
                        + self.__get_grid_value(row + 1, col + 1)
                    )
                    if word1 in ("MAS", "SAM"):
                        word2 = (
                            self.__get_grid_value(row + 1, col - 1)
                            + "A"
                            + self.__get_grid_value(row - 1, col + 1)
                        )
                        if word2 in ("MAS", "SAM"):
                            total += 1
        return total


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
