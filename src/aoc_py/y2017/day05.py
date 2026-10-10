"""
2017 day 5 - Maze of Twisty Trampolines, All Alike

Straightforward; just step through the program with a stackpointer, while modifying the program along the way as
described in the instructions. The only difference between part 1 and 2 is the step for the program modification at
each jump, although this takes much longer to run.
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__instr = list(map(int, s.splitlines()))

    def get_p1(self) -> int:
        program = list(self.__instr)
        size = len(program)
        sp = count = 0
        while 0 <= sp < size:
            count += 1
            offset = program[sp]
            program[sp] += 1
            sp += offset
        return count

    def get_p2(self) -> int:
        program = list(self.__instr)
        size = len(program)
        sp = count = 0
        while 0 <= sp < size:
            count += 1
            offset = program[sp]
            program[sp] = offset - 1 if offset >= 3 else offset + 1
            sp += offset
        return count


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
