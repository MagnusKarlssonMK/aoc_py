"""
2020 day 15 - Rambunctious Recitation

Remember the turn each number was last spoken and keep reciting: a number seen before is
followed by the gap since its previous occurrence, otherwise by 0. Turns are tracked in an
array indexed by the spoken number. The 30 million round count of part 2 is kept as a module
constant so tests can lower it instead of playing the whole game.
"""

from array import array

PART1_ROUNDS = 2020
PART2_ROUNDS = 30_000_000


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__startlist = [int(i) for i in rawstr.split(",")]

    def play_rounds(self, rounds: int) -> int:
        last: array[int] = array("i", [-1]) * rounds
        for i in range(len(self.__startlist) - 1):
            last[self.__startlist[i]] = i
        spoken = self.__startlist[-1]
        for turn in range(len(self.__startlist), rounds):
            prev = last[spoken]
            last[spoken] = turn - 1
            spoken = 0 if prev < 0 else turn - prev - 1
        return spoken


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.play_rounds(PART1_ROUNDS))
    if part in (None, 2):
        p2 = str(p.play_rounds(PART2_ROUNDS))

    return p1, p2
