"""
2016 day 8 - Two-Factor Authentication

Pretty much just do the pixel transformations according to the instructions, use numpy to make the rotation operations
a bit easier.
"""

from dataclasses import dataclass
from enum import Enum

import numpy as np


class Operation(Enum):
    RECT = "rect"
    ROTATE_ROW = "row"
    ROTATE_COLUMN = "column"


@dataclass(frozen=True)
class Instruction:
    operation: Operation
    val1: int
    val2: int


class InputData:
    def __init__(self, s: str) -> None:
        self.__instructions: list[Instruction] = []
        for line in s.splitlines():
            tokens = line.split()
            op = Operation(tokens[0]) if len(tokens) == 2 else Operation(tokens[1])
            if op == Operation.RECT:
                x, y = tokens[1].split("x")
                self.__instructions.append(Instruction(op, int(x), int(y)))
            else:
                v1 = int(tokens[2].split("=")[1])
                v2 = int(tokens[-1])
                self.__instructions.append(Instruction(op, v1, v2))
        self.__screen_width = 50
        self.__screen_height = 6
        if len(self.__instructions) < 5:
            # Assume test input
            self.__screen_width = 7
            self.__screen_height = 3
        self.__grid = np.zeros((self.__screen_height, self.__screen_width))

    def get_lit_pixel_count(self) -> int:
        for instr in self.__instructions:
            match instr.operation:
                case Operation.RECT:
                    self.__grid[0 : instr.val2, 0 : instr.val1] = 1
                case Operation.ROTATE_COLUMN:
                    col = self.__grid[:, instr.val1]
                    rotated = list(col[-instr.val2 :]) + list(col[: -instr.val2])
                    self.__grid[:, instr.val1] = rotated
                case Operation.ROTATE_ROW:
                    row = self.__grid[instr.val1, :]
                    rotated = list(row[-instr.val2 :]) + list(row[: -instr.val2])
                    self.__grid[instr.val1, :] = rotated
        return int(np.sum(self.__grid))

    def draw_screen(self) -> str:
        displaytext = ""
        for row in range(self.__screen_height):
            for col in range(self.__screen_width):
                if self.__grid[row][col] == 0:
                    displaytext += " "
                else:
                    displaytext += "#"
            displaytext += "\n"
        return displaytext


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1 = p.get_lit_pixel_count()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = "\n" + p.draw_screen()

    return p1, p2
