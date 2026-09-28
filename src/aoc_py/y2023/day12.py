"""
2023 day 12 - Hot Springs

Memoized recursive solution. The recursion places one group of springs at a time: at each position the current
spring is either treated as operational, or the next group of inputkeys[0] springs is started there, which is only
allowed when none of those springs is a "." and the spring right after the group is not a "#". Placing a group
skips the spring right after it, which is what keeps two adjacent groups from being read as one longer group, and
leading dots are stripped along the way since a group can never start on one.
"""

from functools import cache


@cache
def calculate_combinations(springstring: str, inputkeys: tuple[int, ...]) -> int:
    if not inputkeys:
        return int("#" not in springstring)
    springlength = len(springstring)
    keylength = inputkeys[0]
    if springlength - sum(inputkeys) - len(inputkeys) + 1 < 0:
        return 0
    group_blocked = "." in springstring[:keylength]
    if springlength == keylength:
        return 0 if group_blocked else 1
    can_use = not group_blocked and (springstring[keylength] != "#")
    if springstring[0] == "#":
        return (
            calculate_combinations(
                springstring[keylength + 1 :].lstrip("."), inputkeys[1:]
            )
            if can_use
            else 0
        )
    skip = calculate_combinations(springstring[1:].lstrip("."), inputkeys)
    if not can_use:
        return skip
    return skip + calculate_combinations(
        springstring[keylength + 1 :].lstrip("."), inputkeys[1:]
    )


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__rows: list[tuple[str, tuple[int, ...]]] = []
        for line in rawstr.splitlines():
            springs, keystr = line.split()
            keys = tuple(int(c) for c in keystr.split(","))
            self.__rows.append((springs, keys))

    def get_arrangement_sum(self, foldcount: int = 1) -> int:
        return sum(
            [
                calculate_combinations(
                    "?".join([springs] * foldcount).lstrip("."), keys * foldcount
                )
                for springs, keys in self.__rows
            ]
        )

    def get_p1(self) -> int:
        return self.get_arrangement_sum(1)

    def get_p2(self) -> int:
        return self.get_arrangement_sum(5)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
