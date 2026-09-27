"""
2023 day 4 - Scratchcards

Each card holds a set of winning numbers and the numbers that were drawn for it, and the matches of the card are the
numbers that appear in both sets.
For part 1, a card with matches is worth 2^(matches - 1) points, while a card without a single match is worth nothing.
For part 2, a card hands out one extra copy of each of the next matches cards, and the answer is the total number of
copies once every card has handed out its copies in card order.
"""


class Card:
    def __init__(self, s: str) -> None:
        winning, drawn = s.split(": ")[1].split(" | ")
        self.matchcount: int = len(
            {int(w) for w in winning.split()} & {int(d) for d in drawn.split()}
        )


class InputData:
    def __init__(self, s: str) -> None:
        self.__scratchcards = [Card(line) for line in s.splitlines()]

    def get_p1(self) -> int:
        return sum(
            [
                pow(2, card.matchcount - 1)
                for card in self.__scratchcards
                if card.matchcount
            ]
        )

    def get_p2(self) -> int:
        copies = [1] * len(self.__scratchcards)
        for i, card in enumerate(self.__scratchcards):
            for j in range(1, card.matchcount + 1):
                copies[i + j] += copies[i]
        return sum(copies)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
