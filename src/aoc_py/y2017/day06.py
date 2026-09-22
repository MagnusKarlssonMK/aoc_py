"""
2017 day 6 - Memory Reallocation

Part 1

Store the memory banks in a class, and rebalance according to the description. Store the current configuration
in a set after every rebalancing and check if we have a repeated value.

Part 2

We saved the state of the memory banks after part 1, so simply run the checker again to get the answer for the
next cycle.
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__banks = list(map(int, s.split()))

    def __rebalance(self) -> None:
        val = max(self.__banks)
        i = self.__banks.index(val)
        self.__banks[i] = 0
        while val > 0:
            i = (i + 1) % len(self.__banks)
            self.__banks[i] += 1
            val -= 1

    def get_cycles_count(self) -> int:
        seen_configs = {tuple(self.__banks)}
        while True:
            self.__rebalance()
            next_cfg = tuple(self.__banks)
            if next_cfg in seen_configs:
                return len(seen_configs)
            seen_configs.add(next_cfg)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1 = p.get_cycles_count()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(p.get_cycles_count())

    return p1, p2
