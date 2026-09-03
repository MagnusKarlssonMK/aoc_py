"""
2023 day 12 - Hot Springs

Memoized recursive solution, using the functools cache.
"""

from functools import lru_cache


@lru_cache
def calculatecombinations(springstring: str, inputkeys: tuple[int] | None) -> int:
    if not inputkeys:  # empty list
        return int(
            "#" not in springstring
        )  # return 1 if there are no '#' in the string, 0 otherwise
    springlength = len(springstring)
    keylength = inputkeys[0]
    if springlength - sum(inputkeys) - len(inputkeys) + 1 < 0:
        return 0
    issubstrings = any(springstring[x] == "." for x in range(keylength))
    if springlength == keylength:
        return 0 if issubstrings else 1
    can_use = not issubstrings and (springstring[keylength] != "#")
    if springstring[0] == "#":
        return (
            calculatecombinations(
                springstring[keylength + 1 :].lstrip("."), tuple(inputkeys[1:])
            )
            if can_use
            else 0
        )
    skip = calculatecombinations(springstring[1:].lstrip("."), inputkeys)
    if not can_use:
        return skip
    return skip + calculatecombinations(
        springstring[keylength + 1 :].lstrip("."), tuple(inputkeys[1:])
    )


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__rows: list[tuple[str, list[int]]] = []
        for line in rawstr.splitlines():
            springs, keystr = line.split()
            keys: list[int] = [int(c) for c in keystr.split(",")]
            self.__rows.append((springs, keys))

    def get_arrangement_sum(self, foldcount: int = 0) -> int:
        retval = 0
        for springs, keys in self.__rows:
            tmpkeys = list(keys) if foldcount == 0 else list(keys) * foldcount
            tmpsprings = (
                springs.lstrip(".")
                if foldcount == 0
                else "?".join([springs] * foldcount).lstrip(".")
            )
            retval += calculatecombinations(tmpsprings, (*tmpkeys,))
        return retval


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_arrangement_sum())
    if part in (None, 2):
        p2 = str(p.get_arrangement_sum(5))

    return p1, p2
