"""
2015 day 23 - Opening the Turing Lock
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Instruction:
    instr: str
    attr1: str
    attr2: str = ""


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__program = [
            Instruction(*[w.strip(",") for w in line.split()])
            for line in rawstr.splitlines()
        ]
        self.__registers: dict[str, int] = {"a": 0, "b": 0}

    def __run_program(self) -> None:
        """Runs the program. Ends when stack pointer goes out of range of the program."""
        s_p = 0
        while s_p < len(self.__program):
            nextinstr = self.__program[s_p]
            match nextinstr.instr:
                case "hlf":  # 'Half'
                    self.__registers[nextinstr.attr1] //= 2
                case "tpl":  # 'Triple'
                    self.__registers[nextinstr.attr1] *= 3
                case "inc":  # 'Increment'
                    self.__registers[nextinstr.attr1] += 1
                case "jmp":  # 'Jump'
                    s_p += int(nextinstr.attr1)
                    continue
                case "jie":  # 'Jump if even'
                    if self.__registers[nextinstr.attr1] % 2 == 0:
                        s_p += int(nextinstr.attr2)
                        continue
                case "jio":  # 'Jump if one' (NOT jump if odd...)
                    if self.__registers[nextinstr.attr1] == 1:
                        s_p += int(nextinstr.attr2)
                        continue
                case _:  # Undefined instruction, should never happen
                    pass
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
