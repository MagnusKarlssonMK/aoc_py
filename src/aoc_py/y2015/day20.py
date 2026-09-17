"""
2015 day 20 - Infinite Elves and Infinite Houses

Seems kind of brute-force-y, but performs much better than attempts to build divisor generator solutions.
Basically simulates the present delivery by iterating over the elfs from 1 and up. Small optimization to keep track
of the lowest house found yet reaching the target to avoid iterating further over higher houses that have no chance of
winning.
"""


class InputData:
    __ELF_PRESENTS = 10
    __LAZY_ELF_PRESENTS = 11
    __LAZY_ELF_CAPACITY = 50

    def __init__(self, rawstr: str) -> None:
        self.__target = int(rawstr)

    def get_p1(self) -> int:
        houses = [10 for _ in range(self.__target // InputData.__ELF_PRESENTS)]
        # Note 1 - We are guaranteed to hit the target at t/10 since each elf delivers 10 times its number
        # Note 2 - Zero indexing houses, i.e. houses[0] == House_1
        # Note 3 - We know the first elf will visit all houses, so initialize houses to 10 to skip the first iteration
        upper_bound = len(houses)
        for elf in range(2, len(houses) + 1):
            for i in range(elf - 1, upper_bound, elf):
                houses[i] += InputData.__ELF_PRESENTS * elf
                if houses[i] >= self.__target:
                    upper_bound = min(upper_bound, i + 1)
        return upper_bound

    def get_p2(self) -> int:
        houses = [0 for _ in range(self.__target // InputData.__LAZY_ELF_PRESENTS)]
        upper_bound = len(houses)
        for elf in range(1, len(houses) + 1):
            presents = 0
            for presents, i in enumerate(range(elf - 1, upper_bound, elf)):
                houses[i] += InputData.__LAZY_ELF_PRESENTS * elf
                if houses[i] >= self.__target:
                    upper_bound = min(upper_bound, i + 1)
                if presents > InputData.__LAZY_ELF_CAPACITY:
                    break
        return upper_bound


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
