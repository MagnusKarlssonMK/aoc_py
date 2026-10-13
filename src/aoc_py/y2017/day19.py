"""
2017 day 19 - A Series of Tubes

Pretty much just walking a path and recording letters along the way. Only switch direction when encountering a '+' node,
otherwise keep walking in current direction and record the character if it is not a pipe. Count how many steps it takes
to get to the end. get_path_and_steps returns the letters found and the number of steps taken.

As a small extra bit of headache - the input uses spaces in the grid, and editors love to trim trailing whitespace.
Meaning that rows will not be of equal length, and using the input to create a Grid generates a broken grid if there
is trailing space on the first line. So the input read from file must first be padded with spaces according to its
longest row.
"""

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions


class InputData:
    def __init__(self, s: str) -> None:
        # Pad every line to the width of the widest line; otherwise Grid takes the
        # width from the first line, which breaks when trailing spaces have been
        # stripped from it.
        lines = s.splitlines()
        width = max(len(line) for line in lines)
        self.__grid = Grid("\n".join(line.ljust(width) for line in lines))

    def get_path_and_steps(self) -> tuple[str, int]:
        current = self.__grid.find("|")
        direction = Directions.DOWN
        path: list[str] = []
        count = 0
        while True:
            count += 1
            current += direction
            v = self.__grid.get_element(current)
            match v:
                case "+":
                    turn = direction.rotate_left()
                    if self.__grid.get_element(current + turn) in ("", " "):
                        direction = direction.rotate_right()
                    else:
                        direction = turn
                case " ":
                    break
                case "-" | "|":
                    pass
                case _:
                    path.append(v)
        return "".join(path), count


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    path, steps = InputData(inputdata).get_path_and_steps()
    if part in (None, 1):
        p1 = path
    if part in (None, 2):
        p2 = str(steps)

    return p1, p2
