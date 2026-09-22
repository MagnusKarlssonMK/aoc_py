"""
2017 day 5 - Maze of Twisty Trampolines, All Alike

Straightforward; just step through the program with a stackpointer, while modifying the program along the way as
described in the instructions. The only difference between part 1 and 2 is the step for the program modification at
each jump, although this takes much longer to run.
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__instr = list(map(int, s.splitlines()))

    def get_exit_step_count(self, stranger: bool = False) -> int:
        program = list(self.__instr)
        sp = 0
        count = 0
        while 0 <= sp < len(program):
            count += 1
            val = program[sp]
            step = -1 if (stranger and val >= 3) else 1
            program[sp] += step
            sp += val
        return count


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_exit_step_count())
    if part in (None, 2):
        p2 = str(p.get_exit_step_count(True))

    return p1, p2
