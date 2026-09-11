"""
2015 day 2 - I Was Told There Would Be No Math
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__gifts = [
            tuple(sorted(map(int, line.split("x")))) for line in s.splitlines()
        ]

    def get_p1(self) -> int:
        return sum([3 * (l * w) + 2 * h * (w + l) for l, w, h in self.__gifts])

    def get_p2(self) -> int:
        return sum([2 * (l + w) + (l * w * h) for l, w, h in self.__gifts])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
