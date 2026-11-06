"""
2020 day 6 - Custom Customs

Represents the answer from each passenger as a 26-bit bitmap; one bit for each present character
in their answer. Then the answer for part 1 is simply to count the number of ones in the bitwise-or
of all answers in the group, and then take the sum of all groups. Similarly for part 2, with the
only difference that bitwise-and is used instead.
"""


def parse_answer(s: str) -> int:
    """Binary representation in a 26-bit integer."""
    acc = 0
    a = ord("a")
    for c in s:
        acc |= 1 << (ord(c) - a)
    return acc


class Group:
    def __init__(self, rawstr: str) -> None:
        self.__answers = [parse_answer(a) for a in rawstr.splitlines()]

    def get_any_yes_count(self) -> int:
        """Number of questions answered by at least one person in the group."""
        result = 0
        for a in self.__answers:
            result |= a
        return result.bit_count()

    def get_all_yes_count(self) -> int:
        """Number of questions answered by every person in the group."""
        result = 0xFFFFFFFF
        for a in self.__answers:
            result &= a
        return result.bit_count()


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
