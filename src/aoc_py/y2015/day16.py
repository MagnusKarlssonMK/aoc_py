"""
2015 day 16 - Aunt Sue

Each Sue mentions only a few of the ten items, while the ticker tape records the true amount of
all ten. So a Sue is ruled out as soon as one of the items it does mention disagrees with the tape,
and any item it leaves out is simply unable to disqualify it. Part 1 compares for equality and part
2 swaps equality for the three comparison rules the puzzle states, which is why each item carries a
matcher alongside its target instead of the comparison being baked into the lookup.

This is also an exercise in a fancy enum. SueItem holds the target amount and the validity condition
for every item in one place, so the rules live next to the numbers they apply to rather than being
scattered through the matching loop.

The three matcher factories are what make that shape workable under a strict type checker. A bare
lambda in a tuple literal has no way to learn that its parameter is an int, since nothing in the
literal says so, and each unknown lambda then spreads into the type of the whole tuple.
"""

from _collections_abc import Callable
from enum import Enum


def _eq(amount: int) -> Callable[[int], bool]:
    return lambda x: x == amount


def _greater_than(amount: int) -> Callable[[int], bool]:
    return lambda x: x > amount


def _fewer_than(amount: int) -> Callable[[int], bool]:
    return lambda x: x < amount


class SueItem(Enum):
    target: int
    match_func: Callable[[int], bool]

    CHILDREN = ("children", 3, _eq(3))
    CATS = ("cats", 7, _greater_than(7))
    SAMOYEDS = ("samoyeds", 2, _eq(2))
    POMERANIANS = ("pomeranians", 3, _fewer_than(3))
    AKITAS = ("akitas", 0, _eq(0))
    VIZSLAS = ("vizslas", 0, _eq(0))
    GOLDFISH = ("goldfish", 5, _fewer_than(5))
    TREES = ("trees", 3, _greater_than(3))
    CARS = ("cars", 2, _eq(2))
    PERFUMES = ("perfumes", 1, _eq(1))

    def __new__(cls, s: str, t: int, f: Callable[[int], bool]):
        obj = object.__new__(cls)
        obj._value_ = s
        return obj

    def __init__(self, s: str, t: int, f: Callable[[int], bool]) -> None:
        # The value of the member is the item's name, which __new__ above sets so that the enum can
        # be looked up by name while parsing. The two attributes go in __init__ rather than __new__,
        # which is both the documented enum idiom for extra per-member data and the only place a
        # type checker counts as initialising them.
        self.target = t
        self.match_func = f

    def is_valid(self, parsed_value: int) -> bool:
        """Evaluates whether a given parsed value matches the Part 2 rules."""
        return self.match_func(parsed_value)


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__sues: list[list[tuple[SueItem, int]]] = []
        for line in rawstr.splitlines():
            _, tmp = line.split(": ", 1)
            parts = tmp.split(", ")
            items: list[tuple[SueItem, int]] = []
            for part in parts:
                name, nbr = part.split(": ")
                items.append((SueItem(name), int(nbr)))
            self.__sues.append(items)

    def get_p1(self) -> int:
        result: int | None = None
        for i, s in enumerate(self.__sues):
            if all(item.target == count for item, count in s):
                # Note that the Sue's are 1-indexed in the input
                result = i + 1
                break
        return result if result is not None else -1

    def get_p2(self) -> int:
        result: int | None = None
        for i, s in enumerate(self.__sues):
            if all(item.is_valid(count) for item, count in s):
                # Note that the Sue's are 1-indexed in the input
                result = i + 1
                break
        return result if result is not None else -1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
