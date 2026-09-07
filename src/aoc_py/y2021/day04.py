"""
2021 day 4 - Giant Squid

Create a class to hold each bingo board with methods to draw a number.
Loop through the numbers for each bingo board and save the result for Part 1 on the first bingo.
Loop the boards in reverse order so that they can be popped safely when getting bingo, and keep
going until there is only one board left to get the score for Part 2.
"""


class BingoBoard:
    def __init__(self, rawstr: str) -> None:
        self.__nbrs: list[list[int]] = [
            (list(map(int, row.split()))) for row in rawstr.splitlines()
        ]
        self.__rowtotals = [0 for _, _ in enumerate(self.__nbrs)]
        self.__coltotals = [0 for _, _ in enumerate(self.__nbrs[0])]
        self.__matchnbrs: set[int] = set()

    def drawnumber(self, nbr: int) -> int:
        """Returns the card score if bingo, otherwise 0."""
        for row, _ in enumerate(self.__nbrs):
            for col, _ in enumerate(self.__nbrs[0]):
                if self.__nbrs[row][col] == nbr:
                    self.__matchnbrs.add(nbr)
                    self.__rowtotals[row] += 1
                    self.__coltotals[col] += 1
                    if self.__rowtotals[row] >= len(
                        self.__coltotals
                    ) or self.__coltotals[col] >= len(self.__rowtotals):
                        return self.__calculatescore(nbr)
        return 0

    def __calculatescore(self, lastnbr: int) -> int:
        nomatchsum = 0
        for row, _ in enumerate(self.__nbrs):
            for col, _ in enumerate(self.__nbrs[0]):
                if self.__nbrs[row][col] not in self.__matchnbrs:
                    nomatchsum += self.__nbrs[row][col]
        return lastnbr * nomatchsum


class InputData:
    def __init__(self, rawinput: str) -> None:
        blocks = rawinput.split("\n\n")
        self.__nbrs = list(map(int, blocks[0].split(",")))
        self.__boards = [BingoBoard(blocks[b_idx]) for b_idx in range(1, len(blocks))]

    def get_scores(self) -> tuple[int, int]:  # (Part1, Part2)
        p1_score = 0
        p2_score = 0
        for nbr in self.__nbrs:
            for b in reversed(range(len(self.__boards))):
                if (result := self.__boards[b].drawnumber(nbr)) > 0:
                    if p1_score == 0:
                        p1_score = result
                    if len(self.__boards) == 1:
                        p2_score = result
                    _ = self.__boards.pop(b)
        return p1_score, p2_score


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_scores()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
