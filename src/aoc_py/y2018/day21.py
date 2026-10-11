"""
2018 day 21 - Chronal Conversion

Like day 19, we now need to disassemble the program even further. Again, trying
to extract the data from the input file, but there is no guarantee that it will
work without modifications for other inputs too if there are shifts in the
program lines - such inputs are rejected by the layout check in __init__.
"""

from typing import Final


class InputData:
    # Opcodes at the positions get_p1 reads its constants from. See the module docstring.
    __LAYOUT: Final = {
        6: "bori",
        7: "seti",
        8: "bani",
        10: "bani",
        11: "muli",
        12: "bani",
        19: "muli",
    }

    def __init__(self, s: str) -> None:
        self.__program = [
            (op, int(a), int(b), int(c))
            for op, a, b, c in [line.split() for line in s.splitlines()[1:]]
        ]
        if not all(
            len(self.__program) > pos and self.__program[pos][0] == op
            for pos, op in self.__LAYOUT.items()
        ):
            raise ValueError("unrecognized day 21 program layout")

    def get_p1(self, startval: int = 0) -> int:
        program = self.__program
        multiplier = program[11][2]
        and_mask = program[8][2]
        trim_mask = program[10][2]
        result = program[7][1]
        v3 = startval | program[6][2]
        while v3 != 0:
            result += v3 & and_mask
            result &= trim_mask
            result *= multiplier
            result &= program[12][2]
            v3 //= program[19][2]
        return result

    def get_p2(self) -> int:
        # Walk the hash chain until a value repeats; the answer is the last
        # distinct value seen before the cycle closes.
        seen: set[int] = set()
        startval = 0
        last = 0
        while True:
            startval = self.get_p1(startval)
            if startval in seen:
                return last
            seen.add(startval)
            last = startval


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
