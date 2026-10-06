"""
2015 day 24 - It Hangs in the Balance

The weights must be divided into three groups of equal total, four for part 2, and the answer is
the product, the so-called quantum entanglement, of the first group. That group is judged on how
few packages it holds before its product is even looked at, so get_first_qe walks first-group sizes
upward and stops at the first size that yields a usable group. The two parts differ only in the
number of groups, so the count is an argument and solve_parts calls the method once per part.

A combination that merely reaches the group total proves nothing on its own: the weights left over
have to divide among the remaining groups as well. Earlier revisions left that check out, trusting
the input to never need it. The input does mostly oblige, but a combination whose remainder happens
to be undividable is then taken at face value. For 3 4 4 6 7 8 9 9 10 the cheapest combination
reaching 20 is 3 7 10, yet the remainder 4 4 6 8 9 9 holds no subset summing to 20 at all, so the
product 210 belongs to no partition whatsoever and 216, from 3 8 9, is the real answer. _can_split
settles the remainder before a combination is accepted, and doing so costs nothing measurable: the
real input answers in the same handful of milliseconds it always did.

Weights that cannot be grouped are answered -1, which is what an empty input, a total that does
not divide evenly by the number of groups, and a total that divides but admits no split all have
in common. The same -1 already marks a part that was not asked for.
"""

from itertools import combinations
from math import prod


class InputData:
    def __init__(self, s: str) -> None:
        self.__weights = list(map(int, s.splitlines()))
        self.__totalweight: int = sum(self.__weights)

    def get_first_qe(self, nbr_groups: int = 3) -> int:
        if not self.__weights or self.__totalweight % nbr_groups:
            return -1
        groupsize = self.__totalweight // nbr_groups
        firstgroup_combos: list[int] = []
        lightest = sorted(self.__weights)
        cheapest = 0
        for count in range(1, len(self.__weights) + 1):
            # Once even the lightest count weights overshoot the group size, no combination of
            # that size or any larger one can reach it, and there is no reason to keep looking.
            cheapest += lightest[count - 1]
            if cheapest > groupsize:
                break
            for comb in combinations(self.__weights, count):
                if sum(comb) != groupsize:
                    continue
                rest = list(self.__weights)
                for weight in comb:
                    rest.remove(weight)
                if _can_split(rest, nbr_groups - 1, groupsize):
                    firstgroup_combos.append(prod(comb))
            if firstgroup_combos:
                return min(firstgroup_combos)
        return -1


def _can_split(pool: list[int], groups: int, groupsize: int) -> bool:
    remaining = sorted(pool, reverse=True)
    if not remaining:
        return groups == 0
    if remaining[0] > groupsize:
        return False
    caps = [groupsize] * groups
    return _fill(remaining, caps, 0)


# Hands each weight, largest first, to some group that still has room for it. Groups holding the
# same amount left are interchangeable, so once one of them has refused a weight the rest are
# skipped as well rather than being tried in turn.
def _fill(remaining: list[int], caps: list[int], index: int) -> bool:
    if index == len(remaining):
        return True
    tried: set[int] = set()
    for slot in range(len(caps)):
        if caps[slot] < remaining[index] or caps[slot] in tried:
            continue
        tried.add(caps[slot])
        caps[slot] -= remaining[index]
        if _fill(remaining, caps, index + 1):
            return True
        caps[slot] += remaining[index]
    return False


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_first_qe())
    if part in (None, 2):
        p2 = str(p.get_first_qe(4))

    return p1, p2
