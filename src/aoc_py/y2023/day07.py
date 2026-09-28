"""
2023 day 7 - Camel Cards

Create Hand class to store the cards and bid, and provides methods to calculate a power value that can be used to
sort the hands. The power value is generated as a hex value with the hand result in the MSB and card values in LSB,
this way the different hands can be sorted according to the rules.
The hand type comes from counting how many cards share each value, and for part 2 the jokers are wild cards that
join the largest group of cards, while still sorting below all the other cards.
"""

from collections import Counter
from dataclasses import dataclass
from enum import Enum
from typing import Final


class HandResults(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


CARDVALUES: Final[dict[str, str]] = {
    card: format(rank, "x") for rank, card in enumerate("23456789TJQKA", start=2)
}
JOKERVALUES: Final[dict[str, str]] = {**CARDVALUES, "J": "1"}


@dataclass(frozen=True)
class Hand:
    bid: int
    cards: list[str]

    @classmethod
    def parse_str(cls, s: str) -> Hand:
        left, right = s.split()
        return cls(int(right), list(left))

    def get_hand_power(self) -> int:
        """Returns the input to Part 1 for this hand."""
        return self.__getpower(False)

    def get_hand_power_jokers(self) -> int:
        """Returns the input to Part 2 for this hand."""
        return self.__getpower(True)

    def __getpower(self, jokers: bool) -> int:
        values = JOKERVALUES if jokers else CARDVALUES
        cardstring = "".join([values[c] for c in self.cards])
        return int(str(self.__getresult(jokers).value) + cardstring, 16)

    def __getresult(self, jokers: bool) -> HandResults:
        """Returns the type of the hand, where the jokers join the largest group of cards as wild cards."""
        if jokers:
            cards = [c for c in self.cards if c != "J"]
            jokercount = len(self.cards) - len(cards)
        else:
            cards = self.cards
            jokercount = 0
        counts = sorted(Counter(cards).values(), reverse=True) or [0]
        counts[0] += jokercount
        match counts:
            case [5]:
                return HandResults.FIVE_OF_A_KIND
            case [4, 1]:
                return HandResults.FOUR_OF_A_KIND
            case [3, 2]:
                return HandResults.FULL_HOUSE
            case [3, 1, 1]:
                return HandResults.THREE_OF_A_KIND
            case [2, 2, 1]:
                return HandResults.TWO_PAIR
            case [2, 1, 1, 1]:
                return HandResults.ONE_PAIR
            case _:
                return HandResults.HIGH_CARD


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__hands: list[Hand] = [
            Hand.parse_str(line) for line in rawstr.splitlines()
        ]

    def get_p1(self) -> int:
        hands = sorted(self.__hands, key=lambda hand: hand.get_hand_power())
        return sum([hand.bid * (rank + 1) for rank, hand in enumerate(hands)])

    def get_p2(self) -> int:
        hands = sorted(self.__hands, key=lambda hand: hand.get_hand_power_jokers())
        return sum([hand.bid * (rank + 1) for rank, hand in enumerate(hands)])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
