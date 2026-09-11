"""
2015 day 1 - Not Quite Lisp
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__steps = [1 if c == "(" else -1 for c in s]

    def get_p1(self) -> int:
        return sum(self.__steps)

    def get_p2(self) -> int:
        floor = 0
        result = -1
        for i, v in enumerate(self.__steps):
            floor += v
            if floor < 0:
                result = i + 1
                break
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
