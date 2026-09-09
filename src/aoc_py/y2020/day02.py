"""
2020 day 2 - Password Philosophy
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Password:
    nbr_range: list[int]
    letter: str
    password: str

    def is_valid(self, new_policy: bool) -> bool:
        if not new_policy:
            return (
                self.nbr_range[0]
                <= self.password.count(self.letter)
                <= self.nbr_range[1]
            )
        else:
            count = 0
            if len(self.password) >= self.nbr_range[0]:
                if self.password[self.nbr_range[0] - 1] == self.letter:
                    count += 1
                if (
                    len(self.password) >= self.nbr_range[1]
                    and self.password[self.nbr_range[1] - 1] == self.letter
                ):
                    count += 1
            return count == 1


class InputData:
    def __init__(self, s: str) -> None:
        self.__passwords = [
            Password(list(map(int, w[0].split("-"))), w[1].strip(":"), w[2])
            for w in [line.split() for line in s.splitlines()]
        ]

    def get_valid_passwords_count(self, newpolicy: bool = False) -> int:
        return sum([1 for p in self.__passwords if p.is_valid(newpolicy)])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_valid_passwords_count())
    if part in (None, 2):
        p2 = str(p.get_valid_passwords_count(True))

    return p1, p2
