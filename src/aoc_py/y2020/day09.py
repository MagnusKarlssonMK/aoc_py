"""
2020 day 9 - Encoding Error

Part 1 moves a preamble window of recent numbers forwards, checking each new number against
all pairs in its window until one that cannot be formed is found.

Part 2 grows a contiguous window forwards until its sum reaches the invalid number, trimming
the front whenever it overshoots, then adds the smallest and largest values in that window.
"""


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__nbrs = [int(line) for line in rawstr.splitlines()]
        # The real input uses a preamble of 25, while the small example uses 5.
        self.__preamble_length = 25 if len(self.__nbrs) >= 25 else 5
        self.__invalid_nbr = -1

    @staticmethod
    def __has_pair(window: list[int], target: int) -> bool:
        seen: set[int] = set()
        for value in window:
            if target - value in seen:
                return True
            seen.add(value)
        return False

    def get_p1(self) -> int:
        n = self.__preamble_length
        for i in range(n, len(self.__nbrs)):
            if not InputData.__has_pair(self.__nbrs[i - n : i], self.__nbrs[i]):
                self.__invalid_nbr = self.__nbrs[i]
                break
        return self.__invalid_nbr

    def get_p2(self) -> int:
        lo = 0
        total = 0
        for hi, value in enumerate(self.__nbrs):
            total += value
            while total > self.__invalid_nbr and lo <= hi:
                total -= self.__nbrs[lo]
                lo += 1
            if total == self.__invalid_nbr and hi - lo >= 1:
                window = self.__nbrs[lo : hi + 1]
                return min(window) + max(window)
        return -1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1 = p.get_p1()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
