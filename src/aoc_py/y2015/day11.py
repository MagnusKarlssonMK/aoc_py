"""
2015 day 11 - Corporate Policy

Convert the input to integers by subtracting the "offset" from 'a', to make it easier
to work with during the password generation.

A valid password holds no i, l or o, contains a straight of three increasing letters, and contains at least two
different letters that are doubled. Part 1 wants the next valid password after the input and part 2 the one after
that, so a single search that keeps stepping forward answers both, and part 2 costs only the distance from the first
answer to the second rather than a second pass over everything below it.

The search treats the last character as the least significant digit and steps it upwards, carrying into the character
before it and wrapping from z back to a. A step that would land on a forbidden letter steps over it instead of
returning it, which drops about one candidate in nine before is_password_valid ever looks at it. That check cannot be
skipped in turn, because the input itself nearly always contains forbidden letters.

Nothing shorter than five characters can be valid, so an input that short is answered with the sentinel rather than
searched for.
"""

from typing import Final

OFFSET: Final = ord("a")
RANGE: Final = ord("z") - OFFSET
FORBIDDEN: Final = (ord("i") - OFFSET, ord("l") - OFFSET, ord("o") - OFFSET)
# The shortest password that can possibly be valid: a straight of three plus two doubled letters, where each doubled
# pair can share at most one position with the straight because no two letters inside a straight are equal.
MIN_LENGTH: Final = 5


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
        if len(self.__password) < MIN_LENGTH:
            return "-1", "-1"
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
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_new_passwords()
    if part in (None, 1):
        p1 = r1
    if part in (None, 2):
        p2 = r2

    return p1, p2
