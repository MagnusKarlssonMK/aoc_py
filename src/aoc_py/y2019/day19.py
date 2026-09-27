"""
2019 day 19 - Tractor Beam

- Step 1: Probe the beam at every coordinate of a 50 x 50 grid by feeding x and y into the intcode program and
  reading back its 0/1 response. The program serves one probe per run and the computer is rebooted after every
  query, so the number of affected points is just the sum of all 2500 responses.
- Step 2: Walk a 100 x 100 square down the beam: increase y while the upper-right corner (x + 99, y) is outside
  the beam, then increase x while the lower-left corner (x, y + 99) is outside it. Because the beam edges grow
  monotonically with x, both corners inside the beam means the whole square fits; the answer is x * 10000 + y.
"""

from aoc_py.y2019.intcode import Intcode, IntResult


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__cpu = Intcode(list(map(int, rawstr.split(","))))

    def __get_drone_status(self, x: int, y: int) -> int:
        self.__cpu.add_input(x)
        self.__cpu.add_input(y)
        val, res = self.__cpu.run_program()
        self.__cpu.reboot()
        if res == IntResult.OUTPUT:
            return val
        else:
            return -1

    def get_p1(self) -> int:
        self.__cpu.reboot()
        return sum(
            [self.__get_drone_status(x, y) for x in range(50) for y in range(50)]
        )

    def get_p2(self) -> int:
        self.__cpu.reboot()
        x = y = 0
        while not self.__get_drone_status(x + 99, y):
            y += 1
            while not self.__get_drone_status(x, y + 99):
                x += 1
        return x * 10000 + y


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
