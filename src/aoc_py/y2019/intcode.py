"""
Intcode computer used for several 2019 puzzles.

- Step 1: The program is stored in a sparse dict of address -> value, and any address that was never written
  reads as 0. Each instruction is decoded into an opcode plus one parameter mode per operand (position,
  immediate or relative, read right to left from the instruction word).
- Step 2: run_program() executes from the current instruction pointer until one of three things happens: the
  program halts, an input instruction finds an empty input buffer, or an output instruction fires. It returns
  a result code (HALTED, WAIT_INPUT or OUTPUT); the instruction pointer is left in a consistent state so the
  caller can add inputs or collect outputs and then resume.
- Step 3: reboot() restores the original program and clears the input buffer, instruction pointer, relative
  base and all memory. override_program() patches a single address before running, and read_memory() inspects
  any address afterwards.
"""

from enum import Enum


class OpCode(Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    RELATIVE_BASE = 9
    HALT = 99


class Mode(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


class IntResult(Enum):
    WAIT_INPUT = 0
    OUTPUT = 1
    HALTED = 2


class Intcode:
    def __init__(self, program: list[int]) -> None:
        self.__program = list(program)
        self.__inputbuffer: list[int] = []
        self.__pc = 0
        self.__relative = 0
        self.__memory: dict[int, int] = {i: nbr for i, nbr in enumerate(self.__program)}

    def reboot(self) -> None:
        self.__inputbuffer.clear()
        self.__pc = 0
        self.__relative = 0
        self.__memory = {i: nbr for i, nbr in enumerate(self.__program)}

    def add_input(self, value: int) -> None:
        self.__inputbuffer.append(value)

    def run_program(self) -> tuple[int, IntResult]:
        def __read(position: int) -> int:
            if position in self.__memory:
                return self.__memory[position]
            return 0

        def __write(position: int, value: int) -> None:
            self.__memory[position] = value

        def __get_value(m: Mode, param: int) -> int:
            if m == Mode.POSITION:
                return __read(param)
            if m == Mode.IMMEDIATE:
                return param
            return __read(self.__relative + param)  # Mode.RELATIVE

        while 0 <= self.__pc:
            op = __read(self.__pc)
            modes: list[Mode] = []
            modes.append(Mode(op // 10000))
            op %= 10000
            modes.insert(0, Mode(op // 1000))
            op %= 1000
            modes.insert(0, Mode(op // 100))
            op_code = OpCode(op % 100)
            p = [__read(i) for i in range(self.__pc + 1, self.__pc + 4)]
            match op_code:
                case OpCode.ADD:
                    dest = p[2] if modes[2] != Mode.RELATIVE else self.__relative + p[2]
                    __write(
                        dest, __get_value(modes[0], p[0]) + __get_value(modes[1], p[1])
                    )
                    self.__pc += 4
                case OpCode.MULTIPLY:
                    dest = p[2] if modes[2] != Mode.RELATIVE else self.__relative + p[2]
                    __write(
                        dest, __get_value(modes[0], p[0]) * __get_value(modes[1], p[1])
                    )
                    self.__pc += 4
                case OpCode.INPUT:
                    dest = p[0] if modes[0] != Mode.RELATIVE else self.__relative + p[0]
                    if self.__inputbuffer:
                        __write(dest, self.__inputbuffer.pop(0))
                        self.__pc += 2
                    else:
                        return -1, IntResult.WAIT_INPUT
                case OpCode.OUTPUT:
                    self.__pc += 2
                    return __get_value(modes[0], p[0]), IntResult.OUTPUT
                case OpCode.JUMP_IF_TRUE:
                    if __get_value(modes[0], p[0]) != 0:
                        self.__pc = __get_value(modes[1], p[1])
                    else:
                        self.__pc += 3
                case OpCode.JUMP_IF_FALSE:
                    if not __get_value(modes[0], p[0]):
                        self.__pc = __get_value(modes[1], p[1])
                    else:
                        self.__pc += 3
                case OpCode.LESS_THAN:
                    dest = p[2] if modes[2] != Mode.RELATIVE else self.__relative + p[2]
                    __write(
                        dest,
                        1
                        if __get_value(modes[0], p[0]) < __get_value(modes[1], p[1])
                        else 0,
                    )
                    self.__pc += 4
                case OpCode.EQUALS:
                    dest = p[2] if modes[2] != Mode.RELATIVE else self.__relative + p[2]
                    __write(
                        dest,
                        1
                        if __get_value(modes[0], p[0]) == __get_value(modes[1], p[1])
                        else 0,
                    )
                    self.__pc += 4
                case OpCode.RELATIVE_BASE:
                    self.__relative += __get_value(modes[0], p[0])
                    self.__pc += 2
                case OpCode.HALT:
                    break
        return -1, IntResult.HALTED

    def override_program(self, mempos: int, val: int) -> None:
        self.__memory[mempos] = val

    def read_memory(self, mempos: int) -> int:
        return self.__memory[mempos]
