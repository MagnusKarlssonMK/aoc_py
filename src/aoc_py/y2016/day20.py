"""
2016 day 20 - Firewall Rules

Parse the input into tuples of low & high and sort the list. The sorting function will default to sort by first
element (i.e. lowest boundary) with no key specified.
Then start with a list of values +1 higher than the upper bound of each blocked range, and check one by one if it's
inside any blocked range; if it is, there is another blocked range overlapping, so we discard the current candidate
and try the next.
Similar deal for part 2, making use of the sorted list and keeping track of the upper bound we've checked for allowed
numbers while counting numbers not covered by blocked intervals.
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__blocklist = sorted(
            [
                (int(low), int(high))
                for low, high in [line.split("-") for line in s.splitlines()]
            ]
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
        highest_allowed = 0
        for low, high in self.__blocklist:
            if highest_allowed < low:
                allowed_total += low - highest_allowed - 1
            highest_allowed = max(high, highest_allowed)
        allowed_total += 2**32 - 1 - highest_allowed
        return allowed_total


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
