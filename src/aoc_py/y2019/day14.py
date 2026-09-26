"""
2019 day 14 - Space Stoichiometry

Part 1

Store the reactions in a dict to be able to look up the yield and requirements for each chemical.
Then start from fuel and add to a shopping list what's needed, add and subtract from it as needed until only ore is
left.

Part 2

Re-use the function from part 1 by gradually increasing the fuel amount and check whether the output ore
has reached the target.
"""

from dataclasses import dataclass
from math import ceil
from typing import Final

ORE_AMOUNT: Final = 1_000_000_000_000


@dataclass(frozen=True)
class Chemical:
    amount: int
    name: str

    @classmethod
    def parse_str(cls, s: str) -> Chemical:
        a, n = s.split()
        return cls(int(a), n)


@dataclass(frozen=True)
class Reaction:
    result: Chemical
    requires: list[Chemical]

    @classmethod
    def parse_str(cls, s: str) -> Reaction:
        left, right = s.split(" => ")
        result = Chemical.parse_str(right)
        req = [Chemical.parse_str(c) for c in left.split(", ")]
        return cls(result, req)


class InputData:
    def __init__(self, s: str) -> None:
        self.__reactions: dict[str, Reaction] = {}
        for line in s.splitlines():
            r = Reaction.parse_str(line)
            self.__reactions[r.result.name] = r

    def get_p1(self, fuel_amount: int = 1) -> int:
        shopping_list: dict[str, int] = {"FUEL": fuel_amount}
        while (
            name := next(
                (k for k in shopping_list if k != "ORE" and shopping_list[k] > 0),
                None,
            )
        ) is not None:
            reaction = self.__reactions[name]
            multiplier = ceil(shopping_list[name] / reaction.result.amount)
            for c in reaction.requires:
                shopping_list[c.name] = (
                    shopping_list.get(c.name, 0) + multiplier * c.amount
                )
            shopping_list[name] -= reaction.result.amount * multiplier
        return shopping_list["ORE"]

    def get_p2(self) -> int:
        lower = 1
        upper = None
        while lower + 1 != upper:
            fuel = lower * 2 if not upper else (upper + lower) // 2
            if self.get_p1(fuel) <= ORE_AMOUNT:
                lower = fuel
            else:
                upper = fuel
        return lower


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
