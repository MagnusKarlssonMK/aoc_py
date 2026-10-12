"""
2020 day 10 - Adapter Array

Part 1

Sort the parsed input, add 0 at the start and max+3 at the end, then simply make a counter
object to put the value differences into.

Part 2

Walk the sorted ratings once, counting for each adapter how many different chains lead up to
it by summing the ways of the up to three preceding adapters within jolt range.
"""

from collections import Counter


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__ratings: list[int] = sorted(map(int, rawstr.splitlines()))
        self.__ratings.append(self.__ratings[-1] + 3)
        self.__ratings.insert(0, 0)

    def get_p1(self) -> int:
        diff: Counter[int] = Counter()
        for i in range(len(self.__ratings) - 1):
            diff[self.__ratings[i + 1] - self.__ratings[i]] += 1
        return diff[1] * diff[3]

    def get_p2(self) -> int:
        ways = {0: 1}
        for rating in self.__ratings[1:]:
            ways[rating] = (
                ways.get(rating - 1, 0)
                + ways.get(rating - 2, 0)
                + ways.get(rating - 3, 0)
            )
        return ways[self.__ratings[-1]]


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
