"""
2022 day 4 - Camp Cleanup
"""

def get_nbrs(line: str) -> tuple[int, int, int, int]:
    left, right = line.split(",")
    a, b = left.split("-")
    c, d = right.split("-")
    return int(a), int(b), int(c), int(d)


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__pairs = [get_nbrs(line) for line in rawstr.splitlines()]

    def get_p1(self) -> int:
        return sum([1 for a, b, c, d in self.__pairs if a <= c <= d <= b or c <= a <= b <= d])

    def get_p2(self) -> int:
        return sum([1 for a, b, c, d in self.__pairs if a <= d and c <= b])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
        p1, p2 = "-1"
        p = InputData(inputdata)
        if part in (None, 1):
            p1 = str(p.get_p1())
        if part in (None, 2):
            p2 = str(p.get_p2())

        return p1, p2
