"""
2017 day 19 - A Series of Tubes

Pretty much just walking a path and recording letters along the way. Only switch direction when encountering a '+' node,
otherwise keep walking in current direction and record the character if it is not a pipe. Count how many steps it takes
to get to the end.
"""

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions


class InputData:
    def __init__(self, s: str) -> None:
        self.__grid = Grid(s)

    def get_path(self) -> tuple[str, int]:
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
                    left = current + direction.rotate_left()
                    if self.__grid.get_element(left) not in ["", " "]:
                        direction = direction.rotate_left()
                    else:
                        direction = direction.rotate_right()
                case " ":
                    break
                case "-" | "|":
                    pass
                case _:
                    path.append(v)
        return "".join(path), count


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_path()
    if part in (None, 1):
        p1 = r1
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
