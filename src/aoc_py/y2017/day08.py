"""
2017 day 8 - I Heard You Like Registers

Kind of trivial by mapping the input on the operator functions, and extracting the register names into a set during the
parsing of the input.
Just run through the program and get the answer to part 1 from the register with the max value at that time.
For part 2, simply keep track of the max value during the execution of the program. We can get both answers during
one runthrough of the program.
"""

import operator as op
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, Final


@dataclass(frozen=True)
class Instr:
    reg: str
    opr: Callable[[Any, Any], Any]
    val: int
    cond_reg: str
    cond_opr: Callable[[Any, Any], Any]
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

    def get_largest_reg_value(self) -> tuple[int, int]:
        regs = {r: 0 for r in self.__regs}
        maxval = 0
        for i in self.__instr:
            if i.cond_opr(regs[i.cond_reg], i.cond_val):
                regs[i.reg] = i.opr(regs[i.reg], i.val)
                maxval = max(maxval, regs[i.reg])
        return max(regs.values()), maxval


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_largest_reg_value()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
