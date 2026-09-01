"""
2023 day 10 - Pipe Maze

Store the data in a grid, then for Part 1 simply walk through the system until returning to the start, then calculating
the answer by dividing the number of steps taken by 2. For part 2, calculate the answer by first determining the area
with the shoelace formula and then use that with Pick's theorem.
"""
from typing import Final

from aoc_py.util.point import Directions, Point


class InputData:
    __DIRECTIONS: Final = {
        "u": Directions.UP,
        "r": Directions.RIGHT,
        "d": Directions.DOWN,
        "l": Directions.LEFT,
    }
    #@typing.ClassVar
    __PIPES: Final = {
        "|": ("u", "d"),
        "-": ("l", "r"),
        "L": ("u", "r"),
        "J": ("u", "l"),
        "7": ("d", "l"),
        "F": ("d", "r"),
    }

    def __init__(self, rawstr: str) -> None:
        self.__grid = rawstr.splitlines()
        self.__startpoint: Point = Point(-1, -1)
        for y, row in enumerate(self.__grid):
            if (x := row.find("S")) >= 0:
                self.__startpoint = Point(x, y)
        # Note: when starting at 'S', take whatever direction we find first, it doesn't matter which way we walk
        for direction in InputData.__DIRECTIONS.values():
            v = self.__get_value(self.__startpoint + direction)
            if v == ".":
                continue
            if direction.reverse() in [
                InputData.__DIRECTIONS[p] for p in InputData.__PIPES[v]
            ]:
                self.__startdirection = direction
                break
        self.__pipepath: list[Point] = []

    def __get_value(self, pos: Point) -> str:
        return self.__grid[pos.y][pos.x]

    def __get_nextstepdir(self, pos: Point, indir: Point) -> Point:
        for outdir in InputData.__PIPES[self.__get_value(pos)]:
            if InputData.__DIRECTIONS[outdir] != indir.reverse():
                return InputData.__DIRECTIONS[outdir]
        return indir  # Should never happen, there should always be one out...

    def __traverse(self) -> None:
        self.__pipepath = []
        currentdir = self.__startdirection
        currentpos = self.__startpoint + currentdir
        self.__pipepath.append(self.__startpoint)
        while currentpos != self.__startpoint:
            self.__pipepath.append(currentpos)
            # Trust that the grid content will never lead us outside the grid, so skip boundary check of new pos
            currentdir = self.__get_nextstepdir(currentpos, currentdir)
            currentpos += currentdir

    def get_p1(self) -> int:
        if not self.__pipepath:
            self.__traverse()
        return len(self.__pipepath) // 2

    def get_p2(self) -> int:
        if not self.__pipepath:
            self.__traverse()
        # Calculate shoelace area
        area = 0
        for idx, _ in enumerate(self.__pipepath):
            area += (
                self.__pipepath[idx].x
                * self.__pipepath[(idx + 1) % len(self.__pipepath)].y
            ) - (
                self.__pipepath[(idx + 1) % len(self.__pipepath)].x
                * self.__pipepath[idx].y
            )
            # Note: we need to 'close the loop' and include also the combination of the first and last entries, thus
            # mod length for the idx + 1 point
        area = abs(area) // 2
        # Use Pick's theorem to get number of enclosed tiles
        return area + 1 - (len(self.__pipepath) // 2)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
        p1, p2 = "-1"
        p = InputData(inputdata)
        if part in (None, 1):
            p1 = str(p.get_p1())
        if part in (None, 2):
            p2 = str(p.get_p2())

        return p1, p2
