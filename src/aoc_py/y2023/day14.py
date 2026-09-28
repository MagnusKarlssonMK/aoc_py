"""
2023 day 14 - Parabolic Reflector Dish

Every tilt is the same scan, differing only in the direction the rocks travel, so the grid is first
listed in the order the rocks roll, one line after another, and the scan then works purely on indices
into that list. Because the list starts at the end the rocks roll towards, the floor starts at zero
and only ever counts up, whichever way the dish happens to be tilted.

Part two spins the dish until the grid repeats. There are only three possible states for each cell,
so the number of distinct grids is finite and a repeat is guaranteed, which turns a billion spins
into a couple of hundred.
"""

from aoc_py.util.grid import Grid
from aoc_py.util.point import Point


class InputData:
    def __init__(self, rawinput: str) -> None:
        self.__grid: Grid = Grid(rawinput)

    def __tilt(self, cells: list[Point], linelength: int) -> None:
        """Rolls every round rock as far as it will go, where cells lists the grid in the order the
        rocks travel and each line of linelength cells is handled separately."""
        for start in range(0, len(cells), linelength):
            floor = start
            for idx in range(start, start + linelength):
                element = self.__grid.get_element(cells[idx])
                if element == "#":
                    floor = idx + 1
                elif element == "O":
                    if idx > floor:
                        self.__grid.set_point(cells[floor], "O")
                        self.__grid.set_point(cells[idx], ".")
                    floor += 1

    def tilt_north(self) -> None:
        x_max, y_max = self.__grid.x_max, self.__grid.y_max
        self.__tilt([Point(x, y) for x in range(x_max) for y in range(y_max)], y_max)

    def tilt_south(self) -> None:
        x_max, y_max = self.__grid.x_max, self.__grid.y_max
        self.__tilt(
            [Point(x, y) for x in range(x_max) for y in reversed(range(y_max))], y_max
        )

    def tilt_east(self) -> None:
        x_max, y_max = self.__grid.x_max, self.__grid.y_max
        self.__tilt(
            [Point(x, y) for y in range(y_max) for x in reversed(range(x_max))], x_max
        )

    def tilt_west(self) -> None:
        x_max, y_max = self.__grid.x_max, self.__grid.y_max
        self.__tilt([Point(x, y) for y in range(y_max) for x in range(x_max)], x_max)

    def cycle(self) -> None:
        self.tilt_north()
        self.tilt_west()
        self.tilt_south()
        self.tilt_east()

    def get_load(self) -> int:
        return sum(
            [
                self.__grid.y_max - (i // self.__grid.x_max)
                for i, e in enumerate(self.__grid.elements)
                if e == "O"
            ]
        )

    def get_p1(self) -> int:
        self.tilt_north()
        return self.get_load()

    def get_p2(self) -> int:
        target_cycles = 1_000_000_000
        seen: dict[tuple[str, ...], int] = {}
        loads: list[int] = []

        spins = 0
        while True:
            self.cycle()
            loads.append(self.get_load())
            key = tuple(self.__grid.elements)
            if key in seen:
                # The states repeat with a fixed period, so the load wanted for the last spin sits
                # somewhere inside the cycle that has just been found.
                firstspin = seen[key]
                period = spins - firstspin
                return loads[firstspin + ((target_cycles - 1 - firstspin) % period)]
            seen[key] = spins
            spins += 1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
