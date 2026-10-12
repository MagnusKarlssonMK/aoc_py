"""
2020 day 14 - Docking Data

Part 1 applies a bitmask to the value: bits where the mask is 1 are forced on and everything
else is kept. Part 2 applies the mask to the address instead: bits where the mask is 1 are
forced on, and every floating (X) bit is expanded into all combinations by enumerating the
submasks of the floating bit positions.
"""

from dataclasses import dataclass
from enum import Enum


class Action(Enum):
    MEM = "mem"
    MASK = "mask"


@dataclass(frozen=True)
class Instruction:
    action: Action
    val1: str
    val2: str = ""


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__instr: list[Instruction] = []
        for line in rawstr.splitlines():
            left, right = line.split(" = ")
            if left.startswith("mask"):
                self.__instr.append(Instruction(Action.MASK, right))
            else:
                self.__instr.append(Instruction(Action.MEM, left[4:-1], right))

    def get_p1(self) -> int:
        memory: dict[int, int] = {}
        and_mask = 0
        or_mask = 0
        for instr in self.__instr:
            if instr.action == Action.MASK:
                and_mask = int("".join("1" if c == "X" else "0" for c in instr.val1), 2)
                or_mask = int("".join("0" if c == "X" else c for c in instr.val1), 2)
            else:
                addr = int(instr.val1)
                val = int(instr.val2)
                memory[addr] = (val & and_mask) | or_mask
        return sum(memory.values())

    def get_p2(self) -> int:
        memory: dict[int, int] = {}
        ones = 0
        xbits = 0
        for instr in self.__instr:
            if instr.action == Action.MASK:
                ones = int(instr.val1.replace("X", "0"), 2)
                xbits = int(instr.val1.replace("1", "0").replace("X", "1"), 2)
            else:
                addr = (int(instr.val1) & ~xbits) | ones
                val = int(instr.val2)
                sub = xbits
                while True:
                    memory[addr | sub] = val
                    if sub == 0:
                        break
                    sub = (sub - 1) & xbits
        return sum(memory.values())


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
