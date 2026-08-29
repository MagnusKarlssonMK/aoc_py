"""
2023 day 2 - Cube Conundrum
"""
from enum import Enum


class Color(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"


class Hand:
    def __init__(self, r: int, b: int, g: int) -> None:
        self.red: int = r
        self.blue: int = b
        self.green: int = g

    @classmethod
    def parse(cls, s: str) -> Hand:
        newhand = {color: 0 for color in Color}
        for n in s.split(", "):
            nbr, colorstr = n.split()
            newhand[Color(colorstr)] = int(nbr)
        return cls(r=newhand[Color.RED], b=newhand[Color.BLUE], g=newhand[Color.GREEN])

    def is_valid(self) -> bool:
        return all([self.red <= 12, self.blue <= 14, self.green <= 13])

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
        self.__hands = [Hand.parse(h) for h in handstring.split("; ")]

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
        p1, p2 = "-1"
        p = InputData(inputdata)
        if part in (None, 1):
            p1 = str(p.get_p1())
        if part in (None, 2):
            p2 = str(p.get_p2())

        return p1, p2
