"""
2019 day 11 - Space Police

- Step 1: Run the paint robot, which starts at the origin facing up on a black panel, using a single
  Intcode instance. Each cycle feeds the color of the current panel as input and reads a paint color
  and a turn direction (0=left, 1=right) from the next two outputs.
- Step 2: Record every panel that is painted at least once. Painting a panel the same color it already
  has still counts, so the same-color-as-input question is resolved by counting painted panels.
- Step 3: Part 1 returns the number of painted panels. Part 2 replays the robot starting on a white
  panel and renders each white panel on a dot-filled grid (with a leading newline) to read the
  registration identifier.
"""

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point
from aoc_py.y2019.intcode import Intcode, IntResult


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__cpu = Intcode(list(map(int, rawstr.split(","))))

    def __paint(self, startcolor: int) -> dict[Point, int]:
        # Colors: 0=black, 1=white
        painted: dict[Point, int] = {}  # point: color
        position = Directions.ORIGIN
        direction = Directions.UP
        color = startcolor
        while True:
            self.__cpu.add_input(color)
            color, _ = self.__cpu.run_program()
            val, res = self.__cpu.run_program()
            if res == IntResult.OUTPUT:
                painted[position] = color
                direction = (
                    direction.rotate_left() if val == 0 else direction.rotate_right()
                )
                position += direction
                color = painted.get(position, 0)
            else:
                break
        return painted

    def get_p1(self) -> int:
        self.__cpu.reboot()
        return len(self.__paint(0))

    def get_p2(self) -> str:
        self.__cpu.reboot()
        painted: dict[Point, int] = self.__paint(1)
        x_max = max(list(painted.keys()), key=lambda x: x.x).x + 1
        y_max = max(list(painted.keys()), key=lambda x: x.y).y + 1
        canvas = Grid.new(x_max, y_max, ".")
        for p, c in painted.items():
            if c == 1:
                canvas.set_point(p, "#")
        # Add line break in front to ensure the first line of the output starts without offset
        return "\n" + str(canvas)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
