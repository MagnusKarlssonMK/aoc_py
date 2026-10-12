"""
2024 day 20 - Race Condition

Parses the grid and stores the non-wall points in the order they appear along the single
path from S to E. A cheat is a shortcut between two points on that path whose manhattan
distance is within the allowed cheat duration; the time it saves is the number of path
steps between them minus that distance. For every point the surrounding diamond of offsets
is visited and looked up in an index built over the path (padded with a -1 border so no
bounds checks are needed). Part 1 allows two-step cheats, part 2 twenty-step cheats, and
both count the cheats saving at least GAIN picoseconds.
"""

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions

CHEAT_STEPS_PART1 = 2
CHEAT_STEPS_PART2 = 20
GAIN = 100


class InputData:
    def __init__(self, rawstr: str) -> None:
        grid = Grid(rawstr)
        self.__width = grid.x_max
        self.__height = grid.y_max
        end = grid.find("E")
        path = [grid.find("S")]
        while path[-1] != end:
            for neighbor in [path[-1] + d for d in Directions.NEIGHBORS_STRAIGHT]:
                if grid.get_element(neighbor) in ("", "#"):
                    continue
                if len(path) >= 2 and path[-2] == neighbor:
                    continue
                path.append(neighbor)
                break
        self.__path = [(p.x, p.y) for p in path]

    def __find_cheats(self, cheat_steps: int, gain: int) -> int:
        pad = cheat_steps
        padded_width = self.__width + 2 * pad
        index = [-1] * (padded_width * (self.__height + 2 * pad))
        for i, (x, y) in enumerate(self.__path):
            index[(y + pad) * padded_width + (x + pad)] = i
        offsets = [
            (dy * padded_width + dx, abs(dx) + abs(dy))
            for dx in range(-cheat_steps, cheat_steps + 1)
            for dy in range(-cheat_steps, cheat_steps + 1)
            if abs(dx) + abs(dy) <= cheat_steps
        ]
        total = 0
        for i, (x, y) in enumerate(self.__path):
            base = (y + pad) * padded_width + (x + pad)
            for shift, dist in offsets:
                if index[base + shift] - i - dist >= gain:
                    total += 1
        return total

    def get_p1(self) -> int:
        return self.__find_cheats(CHEAT_STEPS_PART1, GAIN)

    def get_p2(self) -> int:
        return self.__find_cheats(CHEAT_STEPS_PART2, GAIN)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
