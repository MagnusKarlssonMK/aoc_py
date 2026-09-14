"""
2015 day 11 - Corporate Policy

Convert the input to integers by subtracting the "offset" from 'a', to make it easier
to work with during the password generation.
"""

from typing import Final

OFFSET: Final = ord("a")
RANGE: Final = ord("z") - OFFSET
FORBIDDEN: Final = (ord("i") - OFFSET, ord("l") - OFFSET, ord("o") - OFFSET)


def is_password_valid(pwd: list[int]) -> bool:
    # Evaluates a password to see if it fulfills the validity conditions.
    if any(c in FORBIDDEN for c in pwd):
        return False

    rule_one = False
    for i in range(len(pwd) - 2):
        if pwd[i + 1] == pwd[i] + 1 and pwd[i + 2] == pwd[i + 1] + 1:
            rule_one = True
            break

    if not rule_one:
        return False

    rule_three: set[int] = set()
    for i in range(len(pwd) - 1):
        if pwd[i] == pwd[i + 1]:
            rule_three.add(pwd[i])

    return len(rule_three) > 1


def get_next_password(pwd: list[int]) -> list[int]:
    # Recursively generates the next possible password
    if len(pwd) == 0:
        # Should never happen, unless we start from a password above the last possible one
        # and we've tried to wrap around the first value
        return []

    if pwd[-1] == RANGE:
        tmp = list(pwd[: len(pwd) - 1])
        prefix = get_next_password(tmp)
        prefix.append(0)
        return prefix
    else:
        new_pwd = list(pwd)
        new_last = new_pwd.pop() + 1
        if new_last in FORBIDDEN:
            new_last += 1
        new_pwd.append(new_last)
        return new_pwd


class InputData:
    def __init__(self, s: str) -> None:
        self.__password = [ord(c) - OFFSET for c in s]

    def get_new_passwords(self) -> tuple[str, str]:
        pwd1 = list(self.__password)
        while not is_password_valid(pwd1):
            pwd1 = get_next_password(pwd1)
        pwd2 = get_next_password(pwd1)
        while not is_password_valid(pwd2):
            pwd2 = get_next_password(pwd2)
        p1 = "".join([chr(c + OFFSET) for c in pwd1])
        p2 = "".join([chr(c + OFFSET) for c in pwd2])
        return p1, p2


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_new_passwords()
    if part in (None, 1):
        p1 = r1
    if part in (None, 2):
        p2 = r2

    return p1, p2
