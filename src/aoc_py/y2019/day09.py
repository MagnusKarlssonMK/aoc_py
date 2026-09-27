"""
2019 day 9 - Sensor Boost

- Step 1: Parse the comma-separated program and load it into a single Intcode instance.
- Step 2: Feed the request value (1 for part 1, 2 for part 2) into the input queue and run the program to
  completion, keeping the value of every output it produces.
- Step 3: Return the last output value. The puzzle's test programs emit a single value, but the quine
  example outputs several, so the last value is the meaningful result in every case.
"""

from aoc_py.y2019.intcode import Intcode, IntResult


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__cpu = Intcode(list(map(int, rawstr.split(","))))

    def get_keycode(self, startval: int = 1) -> int:
        self.__cpu.reboot()  # Reset state before each run on the same instance
        self.__cpu.add_input(startval)
        result = -1
        while True:
            val, res = self.__cpu.run_program()
            if res == IntResult.OUTPUT:
                result = val
            else:
                break
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_keycode())
    if part in (None, 2):
        p2 = str(p.get_keycode(2))

    return p1, p2
