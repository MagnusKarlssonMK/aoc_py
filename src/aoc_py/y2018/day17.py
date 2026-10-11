"""
2018 day 17 - Reservoir Research

Stores non-empty tiles in a dict with its current state (clay, resting, flowing). Then starting from the source at
point (500, 0), trail the water path with a DFS, falling down as far as possible, then checking left/right.
After the queue is exhausted, the answers can be found by counting the number of tiles in state 'resting'/'flowing'
for part 1, 'resting' for part 2.
"""

import re
from enum import Enum, auto

from aoc_py.util.point import Directions, Point


class Tile(Enum):
    CLAY = auto()
    RESTING = auto()
    FLOWING = auto()


class InputData:
    def __init__(self, s: str) -> None:
        self.__tiles: dict[Point, Tile] = {}
        for line in s.splitlines():
            a, b, c = list(map(int, re.findall(r"\d+", line)))
            for i in range(b, c + 1):
                x, y = (a, i) if line[0] == "x" else (i, a)
                self.__tiles[Point(x, y)] = Tile.CLAY
        self.__y_min = min(p.y for p in self.__tiles)
        self.__y_max = max(p.y for p in self.__tiles)

    def __fill_row(self, start: Point, direction: Point) -> Point:
        """Fill a horizontal row of flowing water until a wall or a non-solid
        floor stops the spread, returning the cell where the spread stopped."""
        cur = start
        below = cur + Directions.DOWN
        while (cur not in self.__tiles or self.__tiles[cur] == Tile.FLOWING) and (
            below in self.__tiles and self.__tiles[below] in (Tile.RESTING, Tile.CLAY)
        ):
            self.__tiles[cur] = Tile.FLOWING
            cur += direction
            below = cur + Directions.DOWN
        return cur

    def get_water_tile_count(self) -> tuple[int, int]:
        stack = [Point(500, 0)]
        while stack:
            p = stack.pop()
            if p.y > self.__y_max:
                continue
            below = p + Directions.DOWN
            if below not in self.__tiles or self.__tiles[below] == Tile.FLOWING:
                self.__tiles[p] = Tile.FLOWING
                stack.append(below)
            else:
                p_left = self.__fill_row(p, Directions.LEFT)
                p_right = self.__fill_row(p, Directions.RIGHT)

                if (
                    p_left in self.__tiles
                    and self.__tiles[p_left] == Tile.CLAY
                    and p_right in self.__tiles
                    and self.__tiles[p_right] == Tile.CLAY
                ):  # If delimited on both sides
                    for x in range(p_left.x + 1, p_right.x):
                        self.__tiles[Point(x, p.y)] = Tile.RESTING
                    stack.append(Point(p.x, p.y - 1))
                else:
                    if p_left not in self.__tiles:  # Left side open...
                        stack.append(p_left)
                    if p_right not in self.__tiles:  # Right side open...
                        stack.append(p_right)
        p1 = sum(
            1
            for t in self.__tiles
            if self.__tiles[t] in (Tile.RESTING, Tile.FLOWING)
            and self.__y_min <= t.y <= self.__y_max
        )
        p2 = sum(
            1
            for t in self.__tiles
            if self.__tiles[t] == Tile.RESTING and self.__y_min <= t.y <= self.__y_max
        )
        return p1, p2


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_water_tile_count()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
