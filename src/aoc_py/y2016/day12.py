"""
2016 day 12 - Leonardo's Monorail

Back porting the optimizations done for the input program done for day 23 to make
the emulation run much faster.
"""

from dataclasses import dataclass
from enum import Enum


class Registers:
    regs: dict[str, int]

    def __init__(self) -> None:
        self.regs = {r: 0 for r in ["a", "b", "c", "d"]}

    def get_reg(self, reg: str) -> int:
        return self.regs.get(reg, 0)

    def set_reg(self, reg: str, val: int) -> None:
        if reg in self.regs:
            self.regs[reg] = val

    def inc_reg(self, reg: str) -> None:
        if reg in self.regs:
            self.regs[reg] += 1

    def dec_reg(self, reg: str) -> None:
        if reg in self.regs:
            self.regs[reg] -= 1

    def get_val(self, s: str) -> int:
        return self.regs[s] if s in self.regs else int(s)


class Operation(Enum):
    CPY = "cpy"  # reg[arg2] = arg1
    INC = "inc"  # reg[arg1] += 1
    DEC = "dec"  # reg[arg1] -= 1
    JNZ = "jnz"  # sp += arg2 if arg1 not zero
    TGL = "tgl"  # instruction arg1 steps from sp toggled
    MUL = "mul"  # reg[arg1] += arg2 * arg3 (Custom OP, doesn't actually exist in input)
    ADD = "add"  # reg[arg2] += arg1 (Custom OP, doesn't actually exist in input)


@dataclass(frozen=True)
class Instruction:
    instr: Operation
    arg1: str
    arg2: str = ""
    arg3: str = ""  # Needed only for the new Mul operation


class InputData:
    def __init__(self, s: str) -> None:
        self.__program = [
            Instruction(Operation(args[0]), *args[1:])
            for args in [line.split() for line in s.splitlines()]
        ]
        self.__optimize_program()

    def get_a_register(self, initialize_c: bool = False) -> int:
        sp = 0
        regs = Registers()
        if initialize_c:
            regs.set_reg("c", 1)

        while 0 <= sp < len(self.__program):
            match self.__program[sp].instr:
                case Operation.CPY:
                    regs.set_reg(
                        self.__program[sp].arg2, regs.get_val(self.__program[sp].arg1)
                    )
                case Operation.INC:
                    regs.inc_reg(self.__program[sp].arg1)
                case Operation.DEC:
                    regs.dec_reg(self.__program[sp].arg1)
                case Operation.JNZ:
                    a1 = regs.get_val(self.__program[sp].arg1)
                    a2 = regs.get_val(self.__program[sp].arg2)
                    if a1 != 0:
                        sp += a2
                        continue
                case Operation.MUL:
                    a2 = regs.get_val(self.__program[sp].arg2)
                    a3 = regs.get_val(self.__program[sp].arg3)
                    v = regs.get_reg(self.__program[sp].arg1) + (a2 * a3)
                    regs.set_reg(self.__program[sp].arg1, v)
                case Operation.ADD:
                    a1 = regs.get_val(self.__program[sp].arg1)
                    v = regs.get_reg(self.__program[sp].arg2) + a1
                    regs.set_reg(self.__program[sp].arg2, v)
            sp += 1
        return regs.get_val("a")

    def __optimize_program(self) -> None:
        # First, check for possible substitutions with new Mul operation
        # This needs to be done first, since its first three steps are the same as for Add
        for i in range(len(self.__program) - 4):
            if all(
                (
                    self.__program[i].instr == Operation.INC,
                    self.__program[i + 1].instr == Operation.DEC,
                    self.__program[i + 2].instr == Operation.JNZ
                    and self.__program[i + 2].arg2 == "-2"
                    and self.__program[i + 2].arg1 == self.__program[i + 1].arg1,
                    self.__program[i + 3].instr == Operation.DEC,
                    self.__program[i + 4].instr == Operation.JNZ
                    and self.__program[i + 4].arg2 == "-5"
                    and self.__program[i + 4].arg1 == self.__program[i + 3].arg1,
                )
            ):
                # Map to new op, reset the counter registers and fill the rest with no-ops
                self.__program[i] = Instruction(
                    Operation.MUL,
                    self.__program[i].arg1,
                    self.__program[i + 1].arg1,
                    self.__program[i + 3].arg1,
                )
                self.__program[i + 1] = Instruction(
                    Operation.CPY, "0", self.__program[i + 1].arg1
                )
                self.__program[i + 2] = Instruction(
                    Operation.CPY, "0", self.__program[i + 3].arg1
                )
                self.__program[i + 3] = Instruction(Operation.JNZ, "0", "0")
                self.__program[i + 4] = Instruction(Operation.JNZ, "0", "0")

        # Check for possible substitutions with new Add operation
        for i in range(len(self.__program) - 2):
            if all(
                (
                    self.__program[i].instr == Operation.INC,
                    self.__program[i + 1].instr == Operation.DEC
                    or self.__program[i + 1].instr == Operation.INC,
                    self.__program[i + 2].instr == Operation.JNZ
                    and self.__program[i + 2].arg1 == self.__program[i + 1].arg1
                    and self.__program[i + 2].arg2 == "-2",
                )
            ):
                # Actually an addition operation, taken in many steps of +1 - substitute with new op, reset counter register and fill rest with no-op
                self.__program[i] = Instruction(
                    Operation.ADD, self.__program[i + 1].arg1, self.__program[i].arg1
                )
                self.__program[i + 1] = Instruction(
                    Operation.CPY, "0", self.__program[i + 1].arg1
                )
                self.__program[i + 2] = Instruction(Operation.JNZ, "0", "0")
            elif all(
                (
                    self.__program[i].instr == Operation.DEC,
                    self.__program[i + 1].instr == Operation.INC,
                    self.__program[i + 2].instr == Operation.JNZ
                    and self.__program[i + 2].arg1 == self.__program[i].arg1
                    and self.__program[i + 2].arg2 == "-2",
                )
            ):
                # Actually an addition operation, taken in many steps of +1 - substitute with new op, reset counter register and fill rest with no-op
                self.__program[i] = Instruction(
                    Operation.ADD, self.__program[i].arg1, self.__program[i + 1].arg1
                )
                self.__program[i + 1] = Instruction(
                    Operation.CPY, "0", self.__program[i + 2].arg1
                )
                self.__program[i + 2] = Instruction(Operation.JNZ, "0", "0")


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_a_register())
    if part in (None, 2):
        p2 = str(p.get_a_register(True))

    return p1, p2
