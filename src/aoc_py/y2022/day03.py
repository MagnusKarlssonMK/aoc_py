"""
2022 day 3 - Rucksack Reorganization

Priority is fixed by the alphabet: a-z score 1-26 and A-Z score 27-52, so each rucksack's
contribution is the priority of the single item its two compartments have in common. Part 1
splits every rucksack in half, part 2 intersects each consecutive group of three whole
rucksacks instead.

Both parts lean on a guarantee the puzzle makes and the solution relies on: exactly one item
is shared, per rucksack in part 1 and per group of three in part 2. Nothing here checks for
that, so an input violating it would be scored from whichever shared item happened to come
first rather than reported. Every rucksack in the real input honours it.
"""

from typing import Final

PRIORITIES: Final = (
    (range(ord("a"), ord("z") + 1), 1),
    (range(ord("A"), ord("Z") + 1), 27),
)


def get_priority(c: str) -> int:
    """Returns the priority of a single item, being its offset within the lowercase or the
    uppercase run of the alphabet."""
    return sum(
        [ord(c) - rng.start + offset for rng, offset in PRIORITIES if ord(c) in rng]
    )


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__rucksacks: list[str] = rawstr.splitlines()

    def get_p1(self) -> int:
        result = 0
        for rucksack in self.__rucksacks:
            halfway = len(rucksack) // 2
            left, right = rucksack[:halfway], rucksack[halfway:]
            result += get_priority("".join(set(left) & set(right))[0])
        return result

    def get_p2(self) -> int:
        result = 0
        for r in range(0, len(self.__rucksacks), 3):
            s0, s1, s2 = self.__rucksacks[r : r + 3]
            shared = "".join(set(s0) & set(s1) & set(s2))
            result += get_priority(shared[0])
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
