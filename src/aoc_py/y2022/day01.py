"""
2022 day 1 - Calorie Counting

Simply parse the input by storing the sum of each block of numbers in a list sorted
high-to-low. The first (largest) value is then the answer to part 1. For part 2, the
answer is given by the sum of the first three numbers.
"""


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__elfs = sorted(
            [sum(map(int, elf.splitlines())) for elf in rawstr.split("\n\n")],
            reverse=True,
        )

    def get_p1(self) -> int:
        return self.__elfs[0]

    def get_p2(self) -> int:
        return sum([self.__elfs[num] for num in range(3)])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
