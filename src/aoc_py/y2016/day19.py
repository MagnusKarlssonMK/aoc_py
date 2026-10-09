"""
2016 day 19 - An Elephant Named Joseph

Part 1: Straight up the Josephus problem. By using binary representation, the answer can be found by shifting the most
significant 1 to the end.

Part 2: Modified variant of the Josephus problem. It can be solved in a similar manner by converting to base-3 number
and then doing similar modifications, but it gets quite a bit more complicated. Instead, find the largest power of 3
that is still smaller than the target, and then the answer can be found based on that. In short, the pattern resets
with 1 as winner on every 'new' / added digit in the base-3 representation (4, 10, 28...); in the first half in-between
those numbers, the winning number is incremented by 1, while in the second half the winning number is incremented by 2.
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__nbr_elves = int(s)

    def get_p1(self) -> int:
        # Note: the bin() conversion adds 0b at the start of the string; we want to skip those two characters.
        b = bin(self.__nbr_elves)
        return int(b[3:] + b[2], 2)

    def get_p2(self) -> int:
        if self.__nbr_elves <= 2:
            return 1
        # Find the largest power of 3 smaller than the number of elves
        pow3 = 1
        while 3 * pow3 < self.__nbr_elves:
            pow3 *= 3
        # If the number of elves is in the 'lower half' of the interval between base-3 values, the answer starts
        # on 1 and increases by 1; in the 'upper half' the answer increases by 2 for each number.
        if self.__nbr_elves <= 2 * pow3:
            return self.__nbr_elves - pow3
        rem = (self.__nbr_elves - 1) % pow3 + 1
        return self.__nbr_elves - pow3 + rem


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
