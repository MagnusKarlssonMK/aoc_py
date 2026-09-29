"""
2021 day 3 - Binary Diagnostic

The diagnostic report is a list of binary numbers, all of the same width. Counting how many ones occur in each
bit position across the whole report reveals the most and least common bit per position, which is enough for
part 1. For part 2 the same per-position counting is repeated on a shrinking subset: the oxygen rating keeps the
most common bit at each position and narrows the list, and the CO2 rating keeps the least common bit instead. A
position where the ones and zeroes are evenly split makes both answers legal, so we consistently break such a tie
toward one.
"""


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__lines: list[str] = rawstr.splitlines()
        self.__nbrbits: int = len(self.__lines[0])

    def __get_most_and_least_common(self, inlist: list[str]) -> tuple[str, str]:
        gamma = [0 for _ in range(self.__nbrbits)]
        for line in inlist:
            for i, c in enumerate(line):
                gamma[i] += int(c)
        for bit_idx in range(self.__nbrbits):
            gamma[bit_idx] = int(2 * gamma[bit_idx] >= len(inlist))
        epsilon = [1 - i for i in gamma]
        return "".join(list(map(str, gamma))), "".join(list(map(str, epsilon)))

    def get_p1(self) -> int:
        mostcommon, leastcommon = self.__get_most_and_least_common(self.__lines)
        return int(mostcommon, 2) * int(leastcommon, 2)

    def get_p2(self) -> int:
        return self.__getrating(0) * self.__getrating(1)

    def __getrating(self, most_least: int) -> int:
        nbrlist = list(self.__lines)
        for bit_idx in range(self.__nbrbits):
            if len(nbrlist) <= 1:
                break
            matchnbrs = self.__get_most_and_least_common(nbrlist)
            nbrlist = [
                line
                for line in nbrlist
                if line[bit_idx] == matchnbrs[most_least][bit_idx]
            ]
        return int(nbrlist[0], 2)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
