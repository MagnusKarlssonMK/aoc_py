"""
2018 day 1 - Chronal Calibration

Part 1

Simply take the sum of the numbers.

Part 2

Iterate through the numbers, updating the frequency and storing it in a set, and break when finding a
repetition.
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__nbrs = [int(nbr.strip("+")) for nbr in s.splitlines()]

    def get_p1(self) -> int:
        return sum(self.__nbrs)

    def get_p2(self) -> int:
        i = 0
        freq = 0
        size = len(self.__nbrs)
        seen = {freq}
        while True:
            freq += self.__nbrs[i]
            if freq in seen:
                break
            seen.add(freq)
            i = (i + 1) % size
        return freq


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
