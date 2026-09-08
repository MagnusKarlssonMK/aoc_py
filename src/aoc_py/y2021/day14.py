"""
2021 day 14 - Extended Polymerization

Rather than storing the actual string, store the developed polymer as a dict of pairs with a counter.
For every step, expand each pair into two new pairs and inherit the counter value for both.
"""

from collections import Counter


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__template, r = rawstr.split("\n\n")
        rules = [
            (left, right)
            for left, right in [line.split(" -> ") for line in r.splitlines()]
        ]
        self.__rules: dict[str, str] = {}
        self.__paircount: dict[str, int] = {}
        for left, right in rules:
            self.__rules[left] = right
        for i in range(len(self.__template) - 1):
            pair = self.__template[i] + self.__template[i + 1]
            self.__addpair(pair, 1)

    def __addpair(self, pair: str, count: int) -> None:
        if pair in self.__paircount:
            self.__paircount[pair] += count
        else:
            self.__paircount[pair] = count

    def run_steps(self) -> tuple[int, int]:
        p1 = -1
        for step in range(40):
            buffer: list[tuple[str, int]] = []
            for k, v in self.__paircount.items():
                buffer.append((k[0] + self.__rules[k], v))
                buffer.append((self.__rules[k] + k[1], v))
            self.__paircount.clear()
            for k, v in buffer:
                self.__addpair(k, v)
            if step == 9:
                p1 = self.getscore()
        return p1, self.getscore()

    def getscore(self) -> int:
        countlist: Counter[str] = Counter()
        for pair in list(self.__paircount.keys()):
            countlist[pair[0]] += self.__paircount[pair]
        countlist[self.__template[-1]] += 1
        return max(countlist.values()) - min(countlist.values())


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.run_steps()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
