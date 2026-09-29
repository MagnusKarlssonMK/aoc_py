"""
2021 day 14 - Extended Polymerization

Rather than storing the actual string, store the developed polymer as a dict of pairs with a counter.
For every step, expand each pair into two new pairs and inherit the counter value for both. The
starting pair counts have to accumulate, since a template can hold the same pair more than once.

Part 1 scores the polymer after 10 steps and Part 2 after 40, and both counts come out of the same
loop. Scoring counts the leading element of every pair, which leaves out the polymer's final element
because it only ever appears as the second element of the last pair; insertion never disturbs it, so
it is added back by hand.
"""

from collections import Counter
from typing import Final

P1_NBR_STEPS: Final = 10
P2_NBR_STEPS: Final = 40


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__template, r = rawstr.split("\n\n")
        rules = [
            (left, right)
            for left, right in [line.split(" -> ") for line in r.splitlines()]
        ]
        self.__rules: dict[str, str] = {}
        self.__initialpaircount: dict[str, int] = {}
        for left, right in rules:
            self.__rules[left] = right
        for i in range(len(self.__template) - 1):
            pair = self.__template[i] + self.__template[i + 1]
            self.__initialpaircount[pair] = self.__initialpaircount.get(pair, 0) + 1
        self.__paircount: dict[str, int] = dict(self.__initialpaircount)

    def __addpair(self, pair: str, count: int) -> None:
        if pair in self.__paircount:
            self.__paircount[pair] += count
        else:
            self.__paircount[pair] = count

    def run_steps(self) -> tuple[int, int]:
        """Develops the polymer for Part 2's number of steps, reporting the score after
        Part 1's number of steps on the way. The starting pair counts are restored first, so the
        polymer can be run more than once."""
        self.__paircount = dict(self.__initialpaircount)
        p1 = -1
        for step in range(P2_NBR_STEPS):
            buffer: list[tuple[str, int]] = []
            for k, v in self.__paircount.items():
                buffer.append((k[0] + self.__rules[k], v))
                buffer.append((self.__rules[k] + k[1], v))
            self.__paircount.clear()
            for k, v in buffer:
                self.__addpair(k, v)
            if step == P1_NBR_STEPS - 1:
                p1 = self.getscore()
        return p1, self.getscore()

    def getscore(self) -> int:
        countlist: Counter[str] = Counter()
        for pair in self.__paircount:
            countlist[pair[0]] += self.__paircount[pair]
        countlist[self.__template[-1]] += 1
        return max(countlist.values()) - min(countlist.values())


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.run_steps()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
