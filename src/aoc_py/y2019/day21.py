"""
2019 day 21 - Springdroid Adventure

- Step 1: Feed the WALK-mode springdroid instruction program to the intcode computer as ASCII byte values. The
  computer simulates the droid crossing the scaffold, leaping over holes when told to, and ends by outputting
  the amount of hull damage dealt; the solver keeps the last value produced before the run ends.
- Step 2: The same flow with the RUN-mode instruction program, which can read nine tiles ahead and commit to
  longer jump sequences. Both instruction strings are hard-coded; see the comments above them for the logic.
"""

from typing import Final

from aoc_py.y2019.intcode import Intcode, IntResult

# P1: leap whenever any of the three tiles directly ahead (A, B or C) is a hole and the landing tile D is solid:
# J = D AND NOT(A AND B AND C).
P1_PROGRAM: Final = """OR A T
AND B T
AND C T
NOT T J
AND D J
WALK
"""

# P2: leap when the tile right in front (A) is a hole, or when a hole in B or C is cleared by leaping onto a
# solid D while the tile four more ahead (H) is also solid, so the droid keeps its footing after landing:
# J = NOT A OR (D AND H AND (NOT B OR NOT C)).
P2_PROGRAM: Final = """NOT B J
NOT C T
OR T J
AND D J
AND H J
NOT A T
OR T J
RUN
"""


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__cpu = Intcode(list(map(int, rawstr.split(","))))

    def __run_program(self, springcode: str) -> int:
        inst = list(map(ord, springcode))
        output = -1
        for i in inst:
            self.__cpu.add_input(i)
        while True:
            val, res = self.__cpu.run_program()
            if res == IntResult.OUTPUT:
                output = val
            else:
                break
        return output

    def get_p1(self) -> int:
        self.__cpu.reboot()
        return self.__run_program(P1_PROGRAM)

    def get_p2(self) -> int:
        self.__cpu.reboot()
        return self.__run_program(P2_PROGRAM)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
