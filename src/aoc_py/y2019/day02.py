"""
2019 day 2 - 1202 Program Alarm

- Step 1: Parse the comma-separated program into an Intcode instance.
- Step 2: Part 1 restores the alarm state by overwriting address 1 with 12 and address 2 with 2, runs the
  program, then reads the value left at address 0.
- Step 3: Part 2 searches for the noun/verb pair that makes the program halt with the target output at
  address 0: try every combination, rebooting the computer for each attempt, and return 100 * noun + verb.
"""

from typing import Final

from aoc_py.y2019.intcode import Intcode

CORRECT_OUTPUT: Final = 19690720


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__cpu = Intcode(list(map(int, rawstr.split(","))))

    def get_p1(self) -> int:
        self.__cpu.override_program(1, 12)
        self.__cpu.override_program(2, 2)
        _ = self.__cpu.run_program()
        return self.__cpu.read_memory(0)

    def get_p2(self) -> int:
        for noun in range(100):
            for verb in range(100):
                self.__cpu.reboot()
                self.__cpu.override_program(1, noun)
                self.__cpu.override_program(2, verb)
                _ = self.__cpu.run_program()
                if self.__cpu.read_memory(0) == CORRECT_OUTPUT:
                    return noun * 100 + verb
        return -1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
