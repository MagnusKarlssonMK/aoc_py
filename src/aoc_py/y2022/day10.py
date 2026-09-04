"""
2022 day 10 - Cathode-Ray Tube
"""

from dataclasses import dataclass
from enum import Enum


class Instruction(Enum):
    NOOP = "noop"
    ADDX = "addx"


@dataclass(frozen=True)
class Line:
    instr: Instruction
    value: int = -1


class InputData:
    def __init__(self, s: str) -> None:
        self.__program: list[Line] = []
        for line in s.splitlines():
            parts = line.split()
            if len(parts) == 1:
                self.__program.append(Line(Instruction(parts[0])))
            else:
                self.__program.append(Line(Instruction(parts[0]), int(parts[1])))

    def get_p1(self) -> int:
        def increment(cycle: int) -> int:
            intervals = [20, 60, 100, 140, 180, 220]
            return cycle if cycle in intervals else 0

        result = 0
        reg_x = 1
        cyclenbr = 0
        for p in self.__program:
            if p.instr == Instruction.NOOP:
                cyclenbr += 1
                result += reg_x * increment(cyclenbr)
            elif p.instr == Instruction.ADDX:
                cyclenbr += 1
                result += reg_x * increment(cyclenbr)
                cyclenbr += 1
                result += reg_x * increment(cyclenbr)
                reg_x += p.value
        return result

    def get_p2(self) -> str:
        crt = [["" for _ in range(40)] for _ in range(6)]

        def update_crt(cycle: int, x: int) -> None:
            crt[cycle // 40][cycle % 40] = "#" if abs(x - (cycle % 40)) <= 1 else " "

        reg_x = 1
        cyclenbr = 0
        for p in self.__program:
            if p.instr == Instruction.NOOP:
                update_crt(cyclenbr, reg_x)
                cyclenbr += 1
            elif p.instr == Instruction.ADDX:
                update_crt(cyclenbr, reg_x)
                cyclenbr += 1
                update_crt(cyclenbr, reg_x)
                cyclenbr += 1
                reg_x += p.value
        return "".join(["".join(line + ["\n"]) for line in crt])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = "\n" + p.get_p2()

    return p1, p2
