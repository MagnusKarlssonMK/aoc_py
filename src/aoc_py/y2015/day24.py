"""
2024 day 24 - It Hangs in the Balance

Apparently this is a bit of a trick problem, since it turns out that the input is set up in a way that there is no need
to check if the remaining weights can be split evenly once a combination for the first crate has been found. So while I
first started thinking of rather wild recursive algorithms to traverse through, what's really needed is just to find
the list of the shortest combinations for the first crate, and then find the one whose product ('quantum entanglement')
is the smallest.
"""

from itertools import combinations
from math import prod


class InputData:
    def __init__(self, s: str) -> None:
        self.__weights = list(map(int, s.splitlines()))
        self.__totalweight: int = sum(self.__weights)

    def get_first_qe(self, nbr_groups: int = 3) -> int:
        groupsize = self.__totalweight // nbr_groups
        firstgroup_combos: list[int] = []
        for count in range(1, len(self.__weights) - (nbr_groups - 1)):
            for comb in combinations(self.__weights, count):
                if sum(comb) == groupsize:
                    firstgroup_combos.append(prod(comb))
            if firstgroup_combos:
                break
        return min(firstgroup_combos)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_first_qe())
    if part in (None, 2):
        p2 = str(p.get_first_qe(4))

    return p1, p2
