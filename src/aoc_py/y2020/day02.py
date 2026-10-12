"""
2020 day 2 - Password Philosophy

Part 1 counts how many times the required letter occurs and checks that it is within the
given range, while part 2 checks that exactly one of the two positions holds the letter.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Password:
    nbr_range: tuple[int, int]
    letter: str
    password: str

    def is_valid_count_policy(self) -> bool:
        return (
            self.nbr_range[0] <= self.password.count(self.letter) <= self.nbr_range[1]
        )

    def is_valid_position_policy(self) -> bool:
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
    def __init__(self, rawstr: str) -> None:
        self.__passwords: list[Password] = []
        for line in rawstr.splitlines():
            nbr_range, letter, password = line.split()
            lo, hi = map(int, nbr_range.split("-"))
            self.__passwords.append(Password((lo, hi), letter.strip(":"), password))

    def get_valid_passwords_count(self, new_policy: bool = False) -> int:
        if new_policy:
            return sum(1 for p in self.__passwords if p.is_valid_position_policy())
        return sum(1 for p in self.__passwords if p.is_valid_count_policy())


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_valid_passwords_count())
    if part in (None, 2):
        p2 = str(p.get_valid_passwords_count(True))

    return p1, p2
