"""
2016 day 25 - Clock Signal

Start with the code from day 23 as base.
Then add an operation for the 'out' transmission.
The input for this day doesn't use the TGL op code from day 23, but keeping it in here for consistency.

Now instead of starting with a specific value for the 'a' register, we need to loop until we find a working value and
return that. If the transmitted value doesn't follow the '0,1,0,1...' pattern, break and try the next a-value.
As long as it does follow that pattern, store the program state in a list and check if we have reached a state we have
seen before. If so, we know that we have a loop that will repeat, i.e. the exit condition have been met, so we have
found the answer.

This also adds yet another program optimization by replacing a large block of the input instructions with a new
integer division op code, which effectively swaps out a large part of the input program.
(This is kind of getting to the point where I might as well have just extracted the necessary numbers from the input
and make a direct calculation, instead of emulation with a modded program, but... this is more fun.)
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
    DIV = "div"  # reg[arg1] = initial reg[arg1] // 2, reg[arg2] = remainder (Custom OP)
    OUT = "out"  # transmit reg[arg1]


@dataclass(frozen=True)
class Instruction:
    instr: Operation
    arg1: str
    arg2: str = ""
    arg3: str = ""  # Needed only for the new Mul operation

    def get_toggled_op(self) -> Operation:
        instr = self.instr
        if self.arg2 == "":
            instr = Operation.DEC if instr == Operation.INC else Operation.INC
        else:
            instr = Operation.CPY if instr == Operation.JNZ else Operation.JNZ
        return instr


class InputData:
    def __init__(self, s: str) -> None:
        self.__program = [
            Instruction(Operation(args[0]), *args[1:])
            for args in [line.split() for line in s.splitlines()]
        ]
        self.__optimize_program()

    def get_a_register(self) -> int:
        i = 0
        while True:
            regs = Registers()
            regs.set_reg("a", i)
            toggle_list = [False for _ in range(len(self.__program))]
            sp = 0
            program_states: list[
                tuple[int, tuple[Instruction, ...], tuple[int, ...]]
            ] = []

            while 0 <= sp < len(self.__program):
                instr: Operation = (
                    self.__program[sp].instr
                    if not toggle_list[sp]
                    else self.__program[sp].get_toggled_op()
                )

                match instr:
                    case Operation.CPY:
                        regs.set_reg(
                            self.__program[sp].arg2,
                            regs.get_val(self.__program[sp].arg1),
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
                    case Operation.TGL:
                        x = regs.get_val(self.__program[sp].arg1)
                        x += sp
                        if 0 <= x < len(self.__program):
                            toggle_list[x] = not toggle_list[x]
                    case Operation.MUL:
                        a2 = regs.get_val(self.__program[sp].arg2)
                        a3 = regs.get_val(self.__program[sp].arg3)
                        v = regs.get_reg(self.__program[sp].arg1) + (a2 * a3)
                        regs.set_reg(self.__program[sp].arg1, v)
                    case Operation.ADD:
                        a1 = regs.get_val(self.__program[sp].arg1)
                        v = regs.get_reg(self.__program[sp].arg2) + a1
                        regs.set_reg(self.__program[sp].arg2, v)
                    case Operation.DIV:
                        v = regs.get_val(self.__program[sp].arg1)
                        regs.set_reg(self.__program[sp].arg1, v // 2)
                        regs.set_reg(self.__program[sp].arg2, v % 2)
                    case Operation.OUT:
                        transmitted = regs.get_val(self.__program[sp].arg1)
                        if transmitted != (len(program_states) % 2):
                            break
                        p_state = (sp, tuple(self.__program), tuple(regs.regs.values()))
                        if p_state in program_states:
                            return i
                        program_states.append(p_state)
                sp += 1
            i = i + 1

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

        # Check for possible substitution with a new Div operation
        # The divmod block: reg[arg1] = initial reg[arg1] // 2, reg[arg2] = the remainder bit, then fill the rest with no-ops
        for i in range(len(self.__program) - 17):
            if all(
                (
                    self.__program[i].instr == Operation.CPY,
                    self.__program[i + 1].instr == Operation.CPY,
                    self.__program[i + 2].instr == Operation.CPY,
                    self.__program[i + 1].arg1 == "0"
                    and self.__program[i + 1].arg2 == self.__program[i].arg1,
                    self.__program[i + 2].arg1 == "2",
                    self.__program[i].arg1 != self.__program[i].arg2
                    and self.__program[i].arg1 != self.__program[i + 2].arg2
                    and self.__program[i].arg2 != self.__program[i + 2].arg2,
                    self.__program[i + 3].instr == Operation.JNZ
                    and self.__program[i + 3].arg1 == self.__program[i].arg2
                    and self.__program[i + 3].arg2 == "2",
                    self.__program[i + 4].instr == Operation.JNZ
                    and self.__program[i + 4].arg1 == "1"
                    and self.__program[i + 4].arg2 == "6",
                    self.__program[i + 5].instr == Operation.DEC
                    and self.__program[i + 5].arg1 == self.__program[i].arg2,
                    self.__program[i + 6].instr == Operation.DEC
                    and self.__program[i + 6].arg1 == self.__program[i + 2].arg2,
                    self.__program[i + 7].instr == Operation.JNZ
                    and self.__program[i + 7].arg1 == self.__program[i + 2].arg2
                    and self.__program[i + 7].arg2 == "-4",
                    self.__program[i + 8].instr == Operation.INC
                    and self.__program[i + 8].arg1 == self.__program[i].arg1,
                    self.__program[i + 9].instr == Operation.JNZ
                    and self.__program[i + 9].arg1 == "1"
                    and self.__program[i + 9].arg2 == "-7",
                    self.__program[i + 10].instr == Operation.CPY
                    and self.__program[i + 10].arg1 == "2"
                    and self.__program[i + 10].arg2 == self.__program[i].arg2,
                    self.__program[i + 11].instr == Operation.JNZ
                    and self.__program[i + 11].arg1 == self.__program[i + 2].arg2
                    and self.__program[i + 11].arg2 == "2",
                    self.__program[i + 12].instr == Operation.JNZ
                    and self.__program[i + 12].arg1 == "1"
                    and self.__program[i + 12].arg2 == "4",
                    self.__program[i + 13].instr == Operation.DEC
                    and self.__program[i + 13].arg1 == self.__program[i].arg2,
                    self.__program[i + 14].instr == Operation.DEC
                    and self.__program[i + 14].arg1 == self.__program[i + 2].arg2,
                    self.__program[i + 15].instr == Operation.JNZ
                    and self.__program[i + 15].arg1 == "1"
                    and self.__program[i + 15].arg2 == "-4",
                    self.__program[i + 16].instr == Operation.JNZ
                    and self.__program[i + 16].arg1 == "0"
                    and self.__program[i + 16].arg2 == "0",
                )
            ):
                # Map to new op and fill the rest with no-ops
                self.__program[i] = Instruction(
                    Operation.DIV, self.__program[i].arg1, self.__program[i].arg2
                )
                for j in range(i + 1, i + 17):
                    self.__program[j] = Instruction(Operation.JNZ, "0", "0")


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_a_register())
    if part in (None, 2):
        p2 = "-"

    return p1, p2
