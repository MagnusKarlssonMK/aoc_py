"""
2015 day 6 - Probably a Fire Hazard

Use numpy arrays to make things run decently fast.
"""

from enum import Enum

import numpy as np


class Operation(Enum):
    TOGGLE = " "
    TURN_ON = "n"
    TURN_OFF = "f"


class Instruction:
    op: Operation
    x1: int
    y1: int
    x2: int
    y2: int

    def __init__(self, s: str) -> None:
        self.op = Operation(s[6])
        left, right = s.split(" through ")
        left = left.split()[-1]
        self.x1, self.y1, self.x2, self.y2 = map(
            int, left.split(",") + right.split(",")
        )


class InputData:
    def __init__(self, s: str) -> None:
        self.__instructions: list[Instruction] = [
            Instruction(line) for line in s.splitlines()
        ]

    def get_p1(self) -> int:
        grid = np.zeros((1000, 1000))
        for instr in self.__instructions:
            match instr.op:
                case Operation.TURN_ON:
                    grid[instr.x1 : instr.x2 + 1, instr.y1 : instr.y2 + 1] = 1
                case Operation.TURN_OFF:
                    grid[instr.x1 : instr.x2 + 1, instr.y1 : instr.y2 + 1] = 0
                case Operation.TOGGLE:
                    grid[instr.x1 : instr.x2 + 1, instr.y1 : instr.y2 + 1] += 1
                    grid[instr.x1 : instr.x2 + 1, instr.y1 : instr.y2 + 1] %= 2
        return int(grid.sum())

    def get_p2(self) -> int:
        grid = np.zeros((1000, 1000))
        for instr in self.__instructions:
            match instr.op:
                case Operation.TURN_ON:
                    grid[instr.x1 : instr.x2 + 1, instr.y1 : instr.y2 + 1] += 1
                case Operation.TURN_OFF:
                    grid[instr.x1 : instr.x2 + 1, instr.y1 : instr.y2 + 1] -= 1
                    grid.clip(min=0, out=grid)
                case Operation.TOGGLE:
                    grid[instr.x1 : instr.x2 + 1, instr.y1 : instr.y2 + 1] += 2
        return int(grid.sum())


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
