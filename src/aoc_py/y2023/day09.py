"""
2023 day 9 - Mirage Maintenance

Just a simple recursive function to generate the lines until a line of zeroes shows up.
For part 2, basically the same procedure just with reversed input data before running
the same function.
"""


def find_next_number(nbrs: list[int]) -> int:
    if not any(nbrs):
        return 0
    nextlevellist = [nbrs[i] - nbrs[i - 1] for i in range(1, len(nbrs))]
    return nbrs[-1] + find_next_number(nextlevellist)


class InputData:
    def __init__(self, s: str) -> None:
        self.__numbers: list[list[int]] = [
            list(map(int, line.split())) for line in s.splitlines()
        ]

    def get_p1(self) -> int:
        return sum(find_next_number(n) for n in self.__numbers)

    def get_p2(self) -> int:
        return sum(find_next_number(list(reversed(n))) for n in self.__numbers)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
