"""
2019 day 22 - Slam Shuffle

- Step 1: Parse the instructions into (technique, value) pairs. Each technique describes an affine map over the
  deck size, position -> a*position + b.
- Step 2: Part 1 simulates the shuffle on a physical deck of 10007 cards and reads off where card 2019 ends up.
- Step 3: Part 2 runs on a deck too large to simulate, so the whole shuffle is composed into a single affine map
  (a, b). The map is built backwards, so applying it to a final position directly yields the original index of
  the card found there; the increment inverses need modular exponentiation (the deck size is prime).
- Step 4: Repeating the shuffle N times composes the affine map N times, which is evaluated in closed form as a
  modular geometric series.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Final

P1_DECK_SIZE: Final = 10_007
P1_TARGET: Final = 2019
P2_DECK_SIZE: Final = 119315717514047
P2_SHUFFLE_TIMES: Final = 101741582076661
P2_TARGET: Final = 2020


class Techniques(Enum):
    CUT = "cut"
    DEAL_W_INC = "deal with increment"
    DEAL_INTO_NEW = "deal into new"


@dataclass(frozen=True)
class Shuffle:
    tech: Techniques
    value: int

    @classmethod
    def parse_str(cls, s: str) -> Shuffle:
        left, right = s.rsplit(maxsplit=1)
        t = Techniques(left)
        match t:
            case Techniques.CUT:
                return cls(t, int(right))
            case Techniques.DEAL_W_INC:
                return cls(t, int(right))
            case Techniques.DEAL_INTO_NEW:
                return cls(t, -1)


class InputData:
    def __init__(self, s: str) -> None:
        self.__shuffle_process = [Shuffle.parse_str(line) for line in s.splitlines()]

    def get_p1(self, deck_size: int = P1_DECK_SIZE, target: int = P1_TARGET) -> int:
        deck = list(range(deck_size))
        for s in self.__shuffle_process:
            match s.tech:
                case Techniques.CUT:
                    deck = deck[s.value :] + deck[: s.value]
                case Techniques.DEAL_W_INC:
                    newdeck = [0] * len(deck)
                    for i, card in enumerate(deck):
                        newdeck[i * s.value % len(deck)] = card
                    deck = newdeck
                case Techniques.DEAL_INTO_NEW:
                    deck = deck[::-1]
        return deck.index(target)

    def get_p2(
        self,
        deck_size: int = P2_DECK_SIZE,
        shuffle_count: int = P2_SHUFFLE_TIMES,
        target: int = P2_TARGET,
    ) -> int:
        a = 1
        b = 0
        for s in self.__shuffle_process:
            match s.tech:
                case Techniques.CUT:
                    b = (b + (a * s.value)) % deck_size
                case Techniques.DEAL_W_INC:
                    a = (a * pow(s.value, -1, deck_size)) % deck_size
                case Techniques.DEAL_INTO_NEW:
                    b = (b - a) % deck_size
                    a = (-a) % deck_size
        return (
            target * pow(a, shuffle_count, deck_size)
            + ((1 - pow(a, shuffle_count, deck_size)) * pow(1 - a, -1, deck_size) * b)
        ) % deck_size


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
