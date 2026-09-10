"""
2020 day 14 - Docking Data
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
            if left[:4] == "mask":
                self.__instr.append(Instruction(Action.MASK, right))
            else:
                self.__instr.append(Instruction(Action.MEM, left[4:].strip("]"), right))

    def get_p1(self) -> int:
        memory: dict[int, int] = {}
        bitmask = 0, 0
        for instr in self.__instr:
            if instr.action == Action.MASK:
                mask1 = mask2 = ""
                for c in instr.val1:
                    if c == "X":
                        mask1 += "1"
                        mask2 += "0"
                    else:
                        mask1 += "0"
                        mask2 += c
                bitmask = int(mask1, 2), int(mask2, 2)
            else:
                addr = int(instr.val1)
                val = int(instr.val2)
                memory[addr] = (val & bitmask[0]) | bitmask[1]
        return sum(list(memory.values()))

    def get_p2(self) -> int:
        memory: dict[int, int] = {}
        xmask = 0
        addrmasks = []
        for instr in self.__instr:
            if instr.action == Action.MASK:
                x = ""
                for c in instr.val1:
                    if c == "X":
                        x += "0"
                    else:
                        x += "1"
                xmask = int(x, 2)
                addrmasks = self.__mask_value(instr.val1)
            elif instr.action == Action.MEM:
                addr = int(instr.val1)
                val = int(instr.val2)
                for mask in addrmasks:
                    memory[(addr & xmask) | mask] = val
        return sum(list(memory.values()))

    def __mask_value(self, val: str) -> list[int]:
        if (idx := val.find("X")) != -1:
            return self.__mask_value(
                val[:idx] + "0" + val[idx + 1 :]
            ) + self.__mask_value(val[:idx] + "1" + val[idx + 1 :])
        else:
            return [int(val, 2)]


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
