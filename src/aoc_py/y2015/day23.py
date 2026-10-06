"""
2015 day 23 - Opening the Turing Lock

A six-instruction machine with two registers, a and b. Both are non-negative integers and both
start at zero. The three jumps are all relative to the jump instruction itself rather than to the
instruction after it, and each is written with an explicit plus or minus offset.

Two details are easy to get wrong. jio tests for a register holding exactly one, not for oddness,
despite the name. And a jump of plus zero is a legal program that never terminates, which the
puzzle calls out on purpose -- so a run that loops forever is a property of the input rather than
something to guard against.

The run stops when the instruction pointer leaves the program in either direction. Only indices
inside the list name a defined instruction, so a jump past the start exits just as one past the end
does; treating a negative index as wrapping to the end of the list would let a stray backward jump
keep running indefinitely.

Part 1 runs the program from a zero in register a, part 2 from a one, so the two answers are read
from different paths through the same code. The mnemonic is parsed into an Operation on the way in,
so a program the machine does not understand is rejected while it is being read rather than
halfway through a run, and the dispatch below needs no fallback case.
"""

from dataclasses import dataclass
from enum import Enum


class Operation(Enum):
    HLF = "hlf"  # reg[attr1] //= 2
    TPL = "tpl"  # reg[attr1] *= 3
    INC = "inc"  # reg[attr1] += 1
    JMP = "jmp"  # sp += int(attr1), relative to this instruction
    JIE = "jie"  # sp += int(attr2) if reg[attr1] is even
    JIO = "jio"  # sp += int(attr2) if reg[attr1] is one


@dataclass(frozen=True)
class Instruction:
    instr: Operation
    attr1: str
    attr2: str = ""


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__program: list[Instruction] = []
        for line in rawstr.splitlines():
            words = [w.strip(",") for w in line.split()]
            self.__program.append(Instruction(Operation(words[0]), *words[1:]))
        self.__registers: dict[str, int] = {"a": 0, "b": 0}

    def __run_program(self) -> None:
        """Runs the program. Ends when the instruction pointer leaves the program in either
        direction, since only indices inside the list name a defined instruction."""
        s_p = 0
        while 0 <= s_p < len(self.__program):
            nextinstr = self.__program[s_p]
            match nextinstr.instr:
                case Operation.HLF:  # 'Half'
                    self.__registers[nextinstr.attr1] //= 2
                case Operation.TPL:  # 'Triple'
                    self.__registers[nextinstr.attr1] *= 3
                case Operation.INC:  # 'Increment'
                    self.__registers[nextinstr.attr1] += 1
                case Operation.JMP:  # 'Jump'
                    s_p += int(nextinstr.attr1)
                    continue
                case Operation.JIE:  # 'Jump if even'
                    if self.__registers[nextinstr.attr1] % 2 == 0:
                        s_p += int(nextinstr.attr2)
                        continue
                case Operation.JIO:  # 'Jump if one' (NOT jump if odd...)
                    if self.__registers[nextinstr.attr1] == 1:
                        s_p += int(nextinstr.attr2)
                        continue
            s_p += 1

    def get_b_reg(self, a_start_value: int = 0) -> int:
        """Triggers the program with the given start value and returns the value of the B-register."""
        self.__registers["a"] = a_start_value
        self.__registers["b"] = 0
        self.__run_program()
        return self.__registers["b"]


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_b_reg())
    if part in (None, 2):
        p2 = str(p.get_b_reg(1))

    return p1, p2
