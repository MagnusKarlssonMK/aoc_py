"""
2024 day 19 - Linen Layout

Counts the ways each design can be built by concatenating the available towel patterns.
A recursive solution with memoisation over the remaining suffix shares one cache across all
designs, so a suffix is only solved once. Part 1 counts the designs that are possible at all
while part 2 sums the number of distinct ways to build every design.
"""


class InputData:
    def __init__(self, rawstr: str) -> None:
        patterns, designs = rawstr.split("\n\n")
        self.__patterns = patterns.split(", ")
        self.__designs = designs.splitlines()

    def get_counts(self) -> tuple[int, int]:
        seen: dict[str, int] = {}
        result = [self.__count_ways(seen, design) for design in self.__designs]
        return sum(1 for n in result if n > 0), sum(result)

    def __count_ways(self, seen: dict[str, int], design: str) -> int:
        if design == "":
            return 1
        if design in seen:
            return seen[design]
        count = 0
        for pattern in self.__patterns:
            if design.startswith(pattern):
                count += self.__count_ways(seen, design[len(pattern) :])
        seen[design] = count
        return count


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_counts()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
