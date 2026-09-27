"""
2019 day 25 - Cryostasis

- Step 1: The input program is a text adventure that you solve by hand, typing the commands shown above each
  prompt. Start at the Hull Breach and walk the ship, taking the eight safe items: dark matter, fixed point,
  food ration, astronaut ice cream, polygon, easter egg, weather machine, and asterisk. Avoid the lethal
  items: infinite loop , photons, giant electromagnet, molten lava, and escape pod.
- Step 2: Find the Security Checkpoint and then beyond that the pressure-sensitive floor, which only admits
  you while carrying exactly the right weight. You need to experiment depending on your input what the correct
  combination is. Once found, Santa then radios the airlock keypad code, which is the answer to part 1.
"""

import sys

from aoc_py.y2019.intcode import Intcode, IntResult


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__cpu = Intcode(list(map(int, rawstr.split(","))))

    def rescue_santa(self) -> None:
        while True:
            val, res = self.__cpu.run_program()
            if res == IntResult.WAIT_INPUT:
                print("> ")
                userinput = sys.stdin.readline()
                for c in userinput:
                    self.__cpu.add_input(ord(c))
            elif res == IntResult.OUTPUT:
                print(chr(val), end="")
            else:
                break


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    p.rescue_santa()
    if part in (None, 1):
        p1 = "-"
    if part in (None, 2):
        p2 = "-"

    return p1, p2
