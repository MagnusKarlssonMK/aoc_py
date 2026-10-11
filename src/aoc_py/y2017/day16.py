"""
2017 day 16 - Permutation Promenade

Part 1

This is straightforward, just store the order of the programs in a list and perform the instructions. The
move opcodes are represented with an enum rather than their raw input characters.

Part 2

The main challenge here  - obviously we don't want to run 1B simulations, so instead, try to detect how
many rounds are needed until it starts over with the same value. When knowing that cycle length, we can use the stored
values to directly calculate what the value will be after 1B rounds.
"""

from dataclasses import dataclass
from enum import Enum


class MoveOp(Enum):
    SPIN = "s"  # rotate the programs right by arg1 positions
    EXCHANGE = "x"  # swap the programs at positions arg1 and arg2
    PARTNER = "p"  # swap the programs named arg1 and arg2


@dataclass(frozen=True)
class Move:
    op: MoveOp
    arg1: str = ""
    arg2: str = ""


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__moves = [
            Move(MoveOp(i[0]), *i[1:].split("/")) for i in rawstr.split(",")
        ]
        self.__programs = list("abcdefghijklmnop")
        self.__seen: list[str] = []

    def __perform_dance(self) -> str:
        for mv in self.__moves:
            match mv.op:
                case MoveOp.SPIN:
                    steps = int(mv.arg1)
                    self.__programs = (
                        self.__programs[-steps:] + self.__programs[:-steps]
                    )
                case MoveOp.EXCHANGE:
                    i1, i2 = int(mv.arg1), int(mv.arg2)
                    self.__programs[i1], self.__programs[i2] = (
                        self.__programs[i2],
                        self.__programs[i1],
                    )
                case MoveOp.PARTNER:
                    i1, i2 = (
                        self.__programs.index(mv.arg1),
                        self.__programs.index(mv.arg2),
                    )
                    self.__programs[i1], self.__programs[i2] = (
                        self.__programs[i2],
                        self.__programs[i1],
                    )
        return "".join(self.__programs)

    def get_p1(self) -> str:
        new_order = self.__perform_dance()
        self.__seen.append(new_order)
        return new_order

    def get_p2(self, rounds: int = 1_000_000_000) -> str:
        cycle_len = None
        while not cycle_len and len(self.__seen) < rounds:
            new_order = self.__perform_dance()
            if new_order == self.__seen[0]:
                cycle_len = len(self.__seen)
            self.__seen.append(new_order)
        if not cycle_len:
            # Reached the round target without ever repeating : Just return the latest order
            return self.__seen[-1]
        return self.__seen[
            (rounds - 1) % cycle_len
        ]  # rounds - 1 since initial value is not included in seen


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1 = p.get_p1()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
