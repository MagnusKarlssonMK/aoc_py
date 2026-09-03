"""
2023 day 4 - Scratchcards
"""


class Card:
    def __init__(self, s: str) -> None:
        all_numbers = s.split(": ")[1]
        parts = all_numbers.split(" | ")
        winning_numbers = {int(p) for p in parts[0].split()}
        draw_numbers = {int(c) for c in parts[1].split()}
        self.wincount: int = len(winning_numbers & draw_numbers)
        self.score: int = 0 if self.wincount <= 0 else pow(2, self.wincount - 1)


class InputData:
    def __init__(self, s: str) -> None:
        self.__scratchcards = [Card(line) for line in s.splitlines()]

    def get_p1(self) -> int:
        return sum([card.score for card in self.__scratchcards])

    def get_p2(self) -> int:
        copylist = [1 for _ in range(len(self.__scratchcards))]
        for i, card in enumerate(self.__scratchcards):
            for j in range(1, card.wincount + 1):
                copylist[i + j] += copylist[i]
        return sum(copylist)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
