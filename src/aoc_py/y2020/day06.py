"""
2020 day 6 - Custom Customs
"""


class Group:
    def __init__(self, rawstr: str) -> None:
        self.__answers = [set(a) for a in rawstr.splitlines()]

    def get_any_yes_count(self) -> int:
        """Number of questions answered by at least one person in the group."""
        return len(self.__answers[0].union(*self.__answers[1:]))

    def get_all_yes_count(self) -> int:
        """Number of questions answered by every person in the group."""
        return len(self.__answers[0].intersection(*self.__answers[1:]))


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__groups = [Group(g) for g in rawstr.split("\n\n")]

    def get_yes_count(self, everyone: bool = False) -> int:
        if everyone:
            return sum(group.get_all_yes_count() for group in self.__groups)
        return sum(group.get_any_yes_count() for group in self.__groups)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_yes_count())
    if part in (None, 2):
        p2 = str(p.get_yes_count(True))

    return p1, p2
