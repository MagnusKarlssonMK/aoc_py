"""
2015 day 16 - Aunt Sue

Taking this as an exercise to use a fancy enum for representing the input items, while at the
same time containing the known property amounts and a lambda function for the validity condition
for part 2.
"""

from _collections_abc import Callable
from enum import Enum


class SueItem(Enum):
    target: int
    match_func: Callable[[int], bool]

    CHILDREN = ("children", 3, lambda x: x == 3)
    CATS = ("cats", 7, lambda x: x > 7)
    SAMOYEDS = ("samoyeds", 2, lambda x: x == 2)
    POMERANIANS = ("pomeranians", 3, lambda x: x < 3)
    AKITAS = ("akitas", 0, lambda x: x == 0)
    VIZSLAS = ("vizslas", 0, lambda x: x == 0)
    GOLDFISH = ("goldfish", 5, lambda x: x < 5)
    TREES = ("trees", 3, lambda x: x > 3)
    CARS = ("cars", 2, lambda x: x == 2)
    PERFUMES = ("perfumes", 1, lambda x: x == 1)

    def __new__(cls, s: str, t: int, f: Callable[[int], bool]):
        obj = object.__new__(cls)
        obj._value_ = s
        obj.target = t
        obj.match_func = f
        return obj

    def is_valid(self, parsed_value: int) -> bool:
        """Evaluates whether a given parsed value matches the Part 2 rules."""
        return self.match_func(parsed_value)


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__sues: list[list[tuple[SueItem, int]]] = []
        for line in rawstr.splitlines():
            _, tmp = line.split(": ", 1)
            parts = tmp.split(", ")
            items = []
            for part in parts:
                name, nbr = part.split(": ")
                items.append((SueItem(name), int(nbr)))
            self.__sues.append(items)

    def get_p1(self) -> int:
        result = 0
        for i, s in enumerate(self.__sues):
            if all(item.target == count for item, count in s):
                # Note that the Sue's are 1-indexed in the input
                result = i + 1
                break
        return result

    def get_p2(self) -> int:
        result = 0
        for i, s in enumerate(self.__sues):
            if all(item.is_valid(count) for item, count in s):
                # Note that the Sue's are 1-indexed in the input
                result = i + 1
                break
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
