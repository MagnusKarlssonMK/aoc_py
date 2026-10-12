"""
2024 day 17 - Chronospatial Computer

Interprets the eight opcodes of the chronospatial computer. Combo operands 0-3 are literal
values while 4, 5 and 6 refer to registers A, B and C. Part 1 runs the program once and
joins its output values. Part 2 grows the initial value of register A three bits at a time,
processing the program's digits from last to first and keeping every candidate whose first
output value matches the digit currently being placed.
"""

from enum import IntEnum


class Opcode(IntEnum):
    ADV = 0
    BXL = 1
    BST = 2
    JNZ = 3
    BXC = 4
    OUT = 5
    BDV = 6
    CDV = 7


class Computer:
    def __init__(self, a: int, b: int, c: int, program: list[int]) -> None:
        self.__a = a
        self.__b = b
        self.__c = c
        self.__program = program
        self.__ip = 0

    def reboot(self, a: int) -> None:
        """Resets B, C and the instruction pointer, setting A to the given value."""
        self.__a = a
        self.__b = 0
        self.__c = 0
        self.__ip = 0

    def __combo(self, operand: int) -> int:
        """Resolves a combo operand: 0-3 are literals, 4-6 are registers A, B and C."""
        return operand if operand <= 3 else (self.__a, self.__b, self.__c)[operand - 4]

    def run(self) -> list[int]:
        """Runs the program, returning the values written by the out opcode."""
        out: list[int] = []
        length = len(self.__program)
        while 0 <= self.__ip < length:
            operand = self.__program[self.__ip + 1]
            match Opcode(self.__program[self.__ip]):
                case Opcode.ADV:
                    self.__a >>= self.__combo(operand)
                    self.__ip += 2
                case Opcode.BXL:
                    self.__b ^= operand
                    self.__ip += 2
                case Opcode.BST:
                    self.__b = self.__combo(operand) % 8
                    self.__ip += 2
                case Opcode.JNZ:
                    self.__ip = operand if self.__a else self.__ip + 2
                case Opcode.BXC:
                    self.__b ^= self.__c
                    self.__ip += 2
                case Opcode.OUT:
                    out.append(self.__combo(operand) % 8)
                    self.__ip += 2
                case Opcode.BDV:
                    self.__b = self.__a >> self.__combo(operand)
                    self.__ip += 2
                case Opcode.CDV:
                    self.__c = self.__a >> self.__combo(operand)
                    self.__ip += 2
        return out


class InputData:
    def __init__(self, rawstr: str) -> None:
        registers, program = rawstr.split("\n\n")
        lines = registers.splitlines()
        self.__a = int(lines[0].split(": ")[1])
        self.__b = int(lines[1].split(": ")[1])
        self.__c = int(lines[2].split(": ")[1])
        self.__program = [int(n) for n in program.removeprefix("Program: ").split(",")]

    def get_p1(self) -> str:
        computer = Computer(self.__a, self.__b, self.__c, self.__program)
        return ",".join(str(n) for n in computer.run())

    def get_p2(self) -> int:
        computer = Computer(self.__a, self.__b, self.__c, self.__program)
        solutions = [0]
        for digit in reversed(self.__program):
            candidates: list[int] = []
            for prefix in solutions:
                for low in range(8):
                    test_a = (prefix << 3) | low
                    computer.reboot(test_a)
                    if (out := computer.run()) and out[0] == digit:
                        candidates.append(test_a)
            solutions = candidates
        return min(solutions)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = p.get_p1()
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
