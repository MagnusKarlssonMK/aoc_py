"""
2016 day 12 - Leonardo's Monorail

Brute force solution, actually running en emulation of the input program.
A much faster solution could be made by analyzing the program and simplifying it.
"""

from dataclasses import dataclass
from enum import Enum


class Operation(Enum):
    CPY = "cpy"
    INC = "inc"
    DEC = "dec"
    JNZ = "jnz"


@dataclass(frozen=True)
class Instruction:
    instr: Operation
    arg1: str
    arg2: str = ""


class InputData:
    def __init__(self, s: str) -> None:
        self.__program = [
            Instruction(Operation(args[0]), *args[1:])
            for args in [line.split() for line in s.splitlines()]
        ]

    def get_a_register(self, initialize_c: bool = False) -> int:
        sp = 0
        regs = {reg: 0 for reg in ["a", "b", "c", "d"]}
        if initialize_c:
            regs["c"] = 1

        while 0 <= sp < len(self.__program):
            match self.__program[sp].instr:
                case Operation.CPY:
                    if self.__program[sp].arg2 in regs:
                        if self.__program[sp].arg1 in regs:
                            regs[self.__program[sp].arg2] = regs[
                                self.__program[sp].arg1
                            ]
                        else:
                            regs[self.__program[sp].arg2] = int(self.__program[sp].arg1)
                case Operation.INC:
                    if self.__program[sp].arg1 in regs:
                        regs[self.__program[sp].arg1] += 1
                case Operation.DEC:
                    if self.__program[sp].arg1 in regs:
                        regs[self.__program[sp].arg1] -= 1
                case Operation.JNZ:
                    a1 = (
                        regs[self.__program[sp].arg1]
                        if self.__program[sp].arg1 in regs
                        else int(self.__program[sp].arg1)
                    )
                    a2 = (
                        regs[self.__program[sp].arg2]
                        if self.__program[sp].arg2 in regs
                        else int(self.__program[sp].arg2)
                    )
                    if a1 != 0:
                        sp += a2
                        continue
            sp += 1
        return regs["a"]


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_a_register())
    if part in (None, 2):
        p2 = str(p.get_a_register(True))

    return p1, p2
