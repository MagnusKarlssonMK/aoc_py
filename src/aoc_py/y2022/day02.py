"""
2022 day 2 - Rock Paper Scissors
"""

from enum import Enum


class Hand(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    def get_score(self, other: Hand) -> int:
        if self == other:  # Draw
            return 3 + other.value + 1
        elif (self.value + 1) % 3 == other.value:  # Other wins
            return 6 + other.value + 1
        return other.value + 1

    def determine_response(self, guide: str) -> Hand:
        match guide:
            case "X":  # Lose
                return Hand((self.value + 2) % 3)
            case "Z":  # Win
                return Hand((self.value + 1) % 3)
            case _:  # Draw
                return self


class InputData:
    def __init__(self, rawstr: str) -> None:
        left_map = {"A": Hand.ROCK, "B": Hand.PAPER, "C": Hand.SCISSORS}
        self.__rounds: list[tuple[Hand, str]] = [
            (left_map[left], right)
            for left, right in [line.split() for line in rawstr.splitlines()]
        ]

    def get_p1(self) -> int:
        right_map = {"X": Hand.ROCK, "Y": Hand.PAPER, "Z": Hand.SCISSORS}
        return sum(
            [opponent.get_score(right_map[you]) for opponent, you in self.__rounds]
        )

    def get_p2(self) -> int:
        return sum(
            [
                opponent.get_score(opponent.determine_response(you))
                for opponent, you in self.__rounds
            ]
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
