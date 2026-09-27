"""
2023 day 2 - Cube Conundrum

The bag holds 12 red, 14 blue and 13 green cubes in total, and every game is split into hands of cubes.
For part 1, sum the ids of the games where each single hand of the game fits inside the bag.
For part 2, ignore the bag: require only the largest number of cubes of each colour seen in any hand of the game,
and the power of the game is the product of those three maxima.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Final

BAG_RED: Final = 12
BAG_BLUE: Final = 14
BAG_GREEN: Final = 13


class Color(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"


@dataclass(frozen=True)
class Hand:
    red: int
    blue: int
    green: int

    @classmethod
    def parse_str(cls, s: str) -> Hand:
        counts: dict[Color, int] = {color: 0 for color in Color}
        for cube in s.split(", "):
            nbr, colorstr = cube.split()
            counts[Color(colorstr)] = int(nbr)
        return cls(counts[Color.RED], counts[Color.BLUE], counts[Color.GREEN])

    def is_valid(self) -> bool:
        return self.red <= BAG_RED and self.blue <= BAG_BLUE and self.green <= BAG_GREEN

    def get_hand_power(self) -> int:
        return self.red * self.blue * self.green

    def get_max(self, other: Hand) -> Hand:
        return Hand(
            max(self.red, other.red),
            max(self.blue, other.blue),
            max(self.green, other.green),
        )


class Game:
    def __init__(self, inputstr: str) -> None:
        gameidstring, handstring = inputstr.split(": ")
        self.gameid: int = int(gameidstring.split()[1])
        self.__hands = [Hand.parse_str(h) for h in handstring.split("; ")]

    def is_valid(self) -> bool:
        return all(hand.is_valid() for hand in self.__hands)

    def get_power(self) -> int:
        minimum_required = Hand(0, 0, 0)
        for hand in self.__hands:
            minimum_required = hand.get_max(minimum_required)
        return minimum_required.get_hand_power()


class InputData:
    def __init__(self, s: str) -> None:
        self.__games = [Game(line) for line in s.splitlines()]

    def get_p1(self) -> int:
        return sum([game.gameid for game in self.__games if game.is_valid()])

    def get_p2(self) -> int:
        return sum([game.get_power() for game in self.__games])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
