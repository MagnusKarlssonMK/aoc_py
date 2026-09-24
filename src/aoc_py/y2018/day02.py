"""
2018 day 2 - Inventory Management System

Part 1

Simply count the characters in each string, and keep track of how many times a string has a character with
exactly 2 / 3 repetitions. Guess I could have used count from itertools, but meh.

Part 2

Go through the combinations of strings and generate a string of the matching characters; if its length is
exactly 1 smaller, we found the match.
"""

from itertools import combinations


class InputData:
    def __init__(self, s: str) -> None:
        self.__lines = s.splitlines()

    def get_p1(self) -> int:
        twos = threes = 0
        for line in self.__lines:
            counts = {}
            for c in line:
                counts[c] = 1 if c not in counts else counts[c] + 1
            if 2 in counts.values():
                twos += 1
            if 3 in counts.values():
                threes += 1
        return twos * threes

    def get_p2(self) -> str:
        result = ""
        for one, two in combinations(self.__lines, 2):
            common = "".join([c for i, c in enumerate(one) if one[i] == two[i]])
            if len(common) == len(one) - 1:
                result = common
                break
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = p.get_p2()

    return p1, p2
