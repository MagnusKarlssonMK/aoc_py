"""
2021 day 6 - Lanternfish
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__states = [0 for _ in range(9)]
        for nbr in list(map(int, s.split(","))):
            self.__states[nbr] += 1

    def get_answers(self, p1_days: int = 80) -> tuple[int, int]:
        p1 = 0
        for day in range(256):
            self.__states[(day + 7) % 9] += self.__states[day % 9]
            if day == p1_days - 1:
                p1 = sum(self.__states)
        return p1, sum(self.__states)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_answers()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
