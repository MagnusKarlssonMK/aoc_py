"""
2017 day 6 - Memory Reallocation

Part 1

Store the memory banks in a class, and rebalance according to the description. Record the step at which each
configuration is first seen; when a configuration repeats, the number of steps taken is the part 1 answer.

Part 2

The distance between the first and second occurrence of the repeated configuration is the cycle length, i.e. the part 2
answer. Both values are produced by a single simulation.
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__banks = list(map(int, s.split()))

    def __rebalance(self, banks: list[int]) -> None:
        val = max(banks)
        i = banks.index(val)
        banks[i] = 0
        while val > 0:
            i = (i + 1) % len(banks)
            banks[i] += 1
            val -= 1

    def get_cycle_counts(self) -> tuple[int, int]:
        banks = list(self.__banks)
        seen: dict[tuple[int, ...], int] = {}
        steps = 0
        while (config := tuple(banks)) not in seen:
            seen[config] = steps
            self.__rebalance(banks)
            steps += 1
        return steps, steps - seen[config]


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    r1, r2 = InputData(inputdata).get_cycle_counts()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
