"""
2017 day 8 - I Heard You Like Registers

Map the input tokens onto operator functions, and collect the register names into a set while parsing.
Run through the program once: part 1 is the largest register value at the end, part 2 is the largest
value seen at any point during the run. Both answers come from a single pass.
"""

import operator as op
from collections.abc import Callable
from dataclasses import dataclass
from typing import Final


@dataclass(frozen=True)
class Instr:
    reg: str
    opr: Callable[[int, int], int]
    val: int
    cond_reg: str
    cond_opr: Callable[[int, int], bool]
    cond_val: int


class InputData:
    __OP_MAP: Final = {
        "inc": op.add,
        "dec": op.sub,
        ">": op.gt,
        ">=": op.ge,
        "<": op.lt,
        "<=": op.le,
        "==": op.eq,
        "!=": op.ne,
    }

    def __init__(self, s: str) -> None:
        self.__instr: list[Instr] = []
        self.__regs: set[str] = set()
        for line in s.splitlines():
            r, o, v, _, cr, co, cv = line.split()
            self.__instr.append(
                Instr(
                    r,
                    InputData.__OP_MAP[o],
                    int(v),
                    cr,
                    InputData.__OP_MAP[co],
                    int(cv),
                )
            )
            self.__regs.update((r, cr))

    def get_maxima(self) -> tuple[int, int]:
        """Return the largest register value at the end, and the largest value seen during the run."""
        regs = {r: 0 for r in self.__regs}
        peak = 0
        for i in self.__instr:
            if i.cond_opr(regs[i.cond_reg], i.cond_val):
                regs[i.reg] = i.opr(regs[i.reg], i.val)
                peak = max(peak, regs[i.reg])
        return max(regs.values()), peak


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_maxima()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
