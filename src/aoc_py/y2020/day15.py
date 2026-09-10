"""
2020 day 15 - Rambunctious Recitation
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__startlist = [int(i) for i in s.split(",")]

    def playrounds(self, rounds: int) -> int:
        nbrs: dict[int, int] = {}
        for i in range(len(self.__startlist) - 1):
            nbrs[self.__startlist[i]] = i
        lastspoken = self.__startlist[-1]
        for turn in range(len(self.__startlist), rounds):
            speak = 0 if lastspoken not in nbrs else turn - nbrs[lastspoken] - 1
            nbrs[lastspoken] = turn - 1
            lastspoken = speak
        return lastspoken


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.playrounds(2020))
    if part in (None, 2):
        p2 = str(p.playrounds(30_000_000))

    return p1, p2
