"""
2023 day 14 - Parabolic Reflector Dish
"""

from aoc_py.util.grid import Grid
from aoc_py.util.point import Point


class InputData:
    def __init__(self, rawinput: str) -> None:
        self.grid: Grid = Grid(rawinput)

    def tilt_north(self):
        for x in range(self.grid.x_max):
            floor = 0
            for y in range(self.grid.y_max):
                current_point = Point(x, y)
                e = self.grid.get_element(current_point)
                if e == "#":
                    floor = y + 1
                elif e == "O":
                    if y > floor:
                        self.grid.set_point(Point(x, floor), "O")
                        self.grid.set_point(current_point, ".")
                    floor += 1

    def tilt_south(self):
        for x in range(self.grid.x_max):
            floor = self.grid.y_max - 1
            for y in reversed(range(self.grid.y_max)):
                current_point = Point(x, y)
                e = self.grid.get_element(current_point)
                if e == "#":
                    floor = y - 1
                elif e == "O":
                    if y < floor:
                        self.grid.set_point(Point(x, floor), "O")
                        self.grid.set_point(current_point, ".")
                    floor -= 1

    def tilt_east(self):
        for y in range(self.grid.y_max):
            floor = self.grid.x_max - 1
            for x in reversed(range(self.grid.x_max)):
                current_point = Point(x, y)
                e = self.grid.get_element(current_point)
                if e == "#":
                    floor = x - 1
                elif e == "O":
                    if x < floor:
                        self.grid.set_point(Point(floor, y), "O")
                        self.grid.set_point(current_point, ".")
                    floor -= 1

    def tilt_west(self):
        for y in range(self.grid.y_max):
            floor = 0
            for x in range(self.grid.x_max):
                current_point = Point(x, y)
                e = self.grid.get_element(current_point)
                if e == "#":
                    floor = x + 1
                elif e == "O":
                    if x > floor:
                        self.grid.set_point(Point(floor, y), "O")
                        self.grid.set_point(current_point, ".")
                    floor += 1

    def cycle(self):
        self.tilt_north()
        self.tilt_west()
        self.tilt_south()
        self.tilt_east()

    def get_load(self):
        return sum(
            [
                self.grid.y_max - (i // self.grid.x_max)
                for i, e in enumerate(self.grid.elements)
                if e == "O"
            ]
        )

    def get_p1(self) -> int:
        self.tilt_north()
        return self.get_load()

    def get_p2(self) -> int:
        target_cycles = 1_000_000_000
        seen: dict[str, int] = {}
        loads: list[int] = []

        for cycle in range(target_cycles):
            self.cycle()
            loads.append(self.get_load())
            k = str(self.grid.elements)
            if k in seen:
                previous = seen[k]
                idx = previous + ((target_cycles - 1 - previous) % (cycle - previous))
                return loads[idx]
            else:
                seen[k] = cycle
        return 0


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
