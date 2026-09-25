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

    def get_water_tile_count(self) -> tuple[int, int]:
        queue = [Point(500, 0)]
        while queue:
            p = queue.pop()
            if p.y > self.__y_max:
                continue
            below = p + Directions.DOWN
            if below not in self.__tiles or self.__tiles[below] == Tile.FLOWING:
                self.__tiles[p] = Tile.FLOWING
                queue.append(below)
            else:
                # Check left
                p_left_x = p.x
                p_left = Point(p.x, p.y)
                p_left_below = p_left + Directions.DOWN
                while (
                    p_left not in self.__tiles or self.__tiles[p_left] == Tile.FLOWING
                ) and (
                    p_left_below in self.__tiles
                    and (self.__tiles[p_left_below] in (Tile.RESTING, Tile.CLAY))
                ):
                    self.__tiles[p_left] = Tile.FLOWING
                    p_left_x -= 1
                    p_left = Point(p_left_x, p_left.y)
                    p_left_below = p_left + Directions.DOWN
                # Check right
                p_right_x = p.x
                p_right = Point(p.x, p.y)
                p_right_below = p_right + Directions.DOWN
                while (
                    p_right not in self.__tiles or self.__tiles[p_right] == Tile.FLOWING
                ) and (
                    p_right_below in self.__tiles
                    and (self.__tiles[p_right_below] in (Tile.RESTING, Tile.CLAY))
                ):
                    self.__tiles[p_right] = Tile.FLOWING
                    p_right_x += 1
                    p_right = Point(p_right_x, p_right.y)
                    p_right_below = p_right + Directions.DOWN

                if (
                    p_left in self.__tiles
                    and self.__tiles[p_left] == Tile.CLAY
                    and p_right in self.__tiles
                    and self.__tiles[p_right] == Tile.CLAY
                ):  # If delimited on both sides
                    for x in range(p_left.x + 1, p_right.x):
                        self.__tiles[Point(x, p.y)] = Tile.RESTING
                    queue.append(Point(p.x, p.y - 1))
                else:
                    if p_left not in self.__tiles:  # Left side open...
                        queue.append(p_left)
                    if p_right not in self.__tiles:  # Right side open...
                        queue.append(p_right)
        p1 = sum(
            [
                1
                for t in self.__tiles
                if self.__tiles[t] in (Tile.RESTING, Tile.FLOWING)
                and self.__y_min <= t.y <= self.__y_max
            ]
        )
        p2 = sum(
            [
                1
                for t in self.__tiles
                if self.__tiles[t] == Tile.RESTING
                and self.__y_min <= t.y <= self.__y_max
            ]
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
