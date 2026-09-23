"""
2017 day 16 - Permutation Promenade

Part 1

This is straightforward, just store the order of the programs in a list and perform the instructions.

Part 2

The main challenge here  - obviously we don't want to run 1B simulations, so instead, try to detect how
many rounds are needed until it starts over with the same value. When knowing that cycle length, we can use the stored
values to directly calculate what the value will be after 1B rounds.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Move:
    op: str
    arg1: str = ""
    arg2: str = ""


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__moves = [Move(i[0], *i[1:].split("/")) for i in rawstr.split(",")]
        self.__programs = [chr(c) for c in range(ord("a"), ord("p") + 1)]
        self.__seen: list[str] = []

    def __perform_dance(self) -> str:
        for mv in self.__moves:
            match mv.op:
                case "s":
                    self.__programs = (
                        self.__programs[-int(mv.arg1) :]
                        + self.__programs[: -int(mv.arg1)]
                    )
                case "x":
                    self.__programs[int(mv.arg1)], self.__programs[int(mv.arg2)] = (
                        self.__programs[int(mv.arg2)],
                        self.__programs[int(mv.arg1)],
                    )
                case "p":
                    i1, i2 = (
                        self.__programs.index(mv.arg1),
                        self.__programs.index(mv.arg2),
                    )
                    self.__programs[i1], self.__programs[i2] = (
                        self.__programs[i2],
                        self.__programs[i1],
                    )
                case _:
                    pass
        return "".join(self.__programs)

    def get_p1(self) -> str:
        new_order = self.__perform_dance()
        self.__seen.append(new_order)
        return new_order

    def get_p2(self) -> str:
        target_rounds = 1_000_000_000
        cycle_len = None
        while not cycle_len and len(self.__seen) < target_rounds:
            new_order = self.__perform_dance()
            if new_order == self.__seen[0]:
                cycle_len = len(self.__seen)
            self.__seen.append(new_order)
        if not cycle_len:
            # Just in case, let's hope we don't end up here! 1b loops without cycle would take a while...
            return self.__seen[-1]
        return self.__seen[
            (target_rounds - 1) % cycle_len
        ]  # Target - 1 since initial value is not included in seen


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1 = p.get_p1()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
