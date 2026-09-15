"""
2015 day 17 - No Such Thing as Too Much

Simply use the 'combinations' function to generate combinations for all numbers of containers (1-max), and find the
ones matching the volume. Also store the length of the matches in a list to use for part 2, where that list is
sorted, and we then count number of entries for that length.
"""

from itertools import combinations


class InputData:
    def __init__(self, s: str) -> None:
        self.__containers = [int(n) for n in s.splitlines()]
        self.__combinations: list[int] = []
        # For handling different target amount for the smaller test input:
        self.__target_amount: int = 150 if sum(self.__containers) >= 150 else 25

    def get_p1(self) -> int:
        count = 0
        for comb_count in range(1, len(self.__containers) + 1):
            for c in combinations(self.__containers, comb_count):
                if sum(c) == self.__target_amount:
                    self.__combinations.append(len(c))
                    count += 1
        return count

    def get_p2(self) -> int:
        sortlist = sorted(self.__combinations)
        return sortlist.count(sortlist[0]) if len(sortlist) > 0 else 0


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    r1 = p.get_p1()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
