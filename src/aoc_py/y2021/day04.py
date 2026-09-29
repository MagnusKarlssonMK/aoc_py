"""
2021 day 4 - Giant Squid

Create a class to hold each bingo board with methods to draw a number.
Loop through the numbers for each bingo board and save the result for Part 1 on the first bingo.
Loop the boards in reverse order so that they can be popped safely when getting bingo, and keep
track of the score each bingo produces so that the last board to reach one can be reported for Part 2.
A board completing a line on the drawn number zero legitimately scores zero, so neither part may use
zero as a marker for "no bingo found yet".
"""


class BingoBoard:
    def __init__(self, rawstr: str) -> None:
        self.__nbrs: list[list[int]] = [
            (list(map(int, row.split()))) for row in rawstr.splitlines()
        ]
        self.__rowtotals = [0] * len(self.__nbrs)
        self.__coltotals = [0] * len(self.__nbrs[0])
        self.__matchnbrs: set[int] = set()

    def drawnumber(self, nbr: int) -> int | None:
        """Returns the card score if bingo, otherwise None."""
        for row, values in enumerate(self.__nbrs):
            for col, value in enumerate(values):
                if value == nbr:
                    self.__matchnbrs.add(nbr)
                    self.__rowtotals[row] += 1
                    self.__coltotals[col] += 1
                    if self.__rowtotals[row] >= len(
                        self.__coltotals
                    ) or self.__coltotals[col] >= len(self.__rowtotals):
                        return self.__calculatescore(nbr)
        return None

    def __calculatescore(self, lastnbr: int) -> int:
        nomatchsum = 0
        for values in self.__nbrs:
            for value in values:
                if value not in self.__matchnbrs:
                    nomatchsum += value
        return lastnbr * nomatchsum


class InputData:
    def __init__(self, rawstr: str) -> None:
        blocks = rawstr.split("\n\n")
        self.__nbrs: list[int] = list(map(int, blocks[0].split(",")))
        self.__boards: list[BingoBoard] = [BingoBoard(block) for block in blocks[1:]]

    def get_scores(self) -> tuple[int, int]:  # (Part1, Part2)
        p1_score = 0
        p2_score = 0
        found_first = False
        for nbr in self.__nbrs:
            for b in reversed(range(len(self.__boards))):
                if (result := self.__boards[b].drawnumber(nbr)) is not None:
                    if not found_first:
                        p1_score = result
                        found_first = True
                    # Every bingo overwrites this, so the value left at the end is the last board
                    # to reach bingo. That holds even if the drawn numbers run out before every
                    # board gets one.
                    p2_score = result
                    _ = self.__boards.pop(b)
        return p1_score, p2_score


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_scores()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
