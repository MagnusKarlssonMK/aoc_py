"""
2020 day 6 - Custom Customs
"""


class Group:
    def __init__(self, s: str) -> None:
        self.__answers: list[str] = s.splitlines()

    def get_yes_count(self, everyone: bool) -> int:
        yes = set(self.__answers[0])
        if everyone:
            for a in self.__answers[1:]:
                yes = yes & set(a)
        else:
            for a in self.__answers[1:]:
                yes = yes | set(a)
        return len(yes)


class InputData:
    def __init__(self, s: str) -> None:
        self.__groups = [Group(g) for g in s.split("\n\n")]

    def get_yes_count(self, everyone: bool = False) -> int:
        return sum([group.get_yes_count(everyone) for group in self.__groups])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_yes_count())
    if part in (None, 2):
        p2 = str(p.get_yes_count(True))

    return p1, p2
