"""
2019 day 5 - Sunny with a Chance of Asteroids

- Step 1: Parse the comma-separated program into an Intcode instance.
- Step 2: Load the input value (1 for part 1, 5 for part 2) into the input queue and run the program.
- Step 3: The program reports its result as the first non-zero output; scan the outputs and return that
  value, or -1 if the program halts without producing one.
"""

from aoc_py.y2019.intcode import Intcode, IntResult


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__cpu = Intcode(list(map(int, rawstr.split(","))))

    def get_diagnostic_code(self, inputval: int) -> int:
        self.__cpu.reboot()
        self.__cpu.add_input(inputval)
        while True:
            val, res = self.__cpu.run_program()
            if res == IntResult.OUTPUT and val != 0:
                return val
            if res != IntResult.OUTPUT:
                return -1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_diagnostic_code(1))
    if part in (None, 2):
        p2 = str(p.get_diagnostic_code(5))

    return p1, p2
