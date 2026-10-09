"""
2016 day 20 - Firewall Rules

Parse the input into tuples of low & high and sort the list. The sorting function will default to sort by first
element (i.e. lowest boundary) with no key specified.
For part 1, start with a candidate of 0 and walk the sorted ranges: as soon as the candidate falls below a range's
low it is not blocked, otherwise it is bumped to just past the range's high.
For part 2, count the addresses not covered by any blocked interval while tracking the highest blocked address seen
so far (starting at -1 so that a gap before the first range still includes address 0).
"""

MAX_IP = 2**32 - 1


class InputData:
    def __init__(self, s: str) -> None:
        self.__blocklist = sorted(
            tuple(map(int, line.split("-"))) for line in s.splitlines()
        )

    def get_p1(self) -> int:
        candidate = 0
        for low, high in self.__blocklist:
            if candidate < low:
                break
            if candidate <= high:
                candidate = high + 1
        return candidate

    def get_p2(self) -> int:
        allowed_total = 0
        highest_blocked = -1
        for low, high in self.__blocklist:
            if highest_blocked < low:
                allowed_total += low - highest_blocked - 1
            highest_blocked = max(high, highest_blocked)
        allowed_total += MAX_IP - highest_blocked
        return allowed_total


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
