"""
2018 day 10 - The Stars Align

Pretty much just store the points move them around a few times and then print the resulting image.
The key point is to know when to break, which will be when the points are the most concentrated, i.e. the area of the
box containing the points is the smallest.
"""

import re
from dataclasses import dataclass

from aoc_py.util.point import Point


@dataclass
class Position:
    pos: Point
    vel: Point

    @classmethod
    def parse_str(cls, s: str) -> Position:
        nbrs = list(map(int, re.findall(r"-?\d+", s)))
        pos = Point(nbrs[0], nbrs[1])
        vel = Point(nbrs[2], nbrs[3])
        return Position(pos, vel)

    def step(self) -> Position:
        return Position(self.pos + self.vel, self.vel)


def get_bounds(positions: list[Position]) -> tuple[int, int, int, int]:
    xs = [p.pos.x for p in positions]
    ys = [p.pos.y for p in positions]
    return min(xs), max(xs), min(ys), max(ys)


def get_box_area(positions: list[Position]) -> int:
    min_x, max_x, min_y, max_y = get_bounds(positions)
    return (max_x - min_x) * (max_y - min_y)


def render_grid(positions: list[Position]) -> str:
    min_x, max_x, min_y, max_y = get_bounds(positions)
    grid = [["." for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    for p in positions:
        grid[p.pos.y - min_y][p.pos.x - min_x] = "#"
    return "\n" + "\n".join("".join(g) for g in grid)


class InputData:
    def __init__(self, s: str) -> None:
        self.__positions = [Position.parse_str(line) for line in s.splitlines()]

    def get_message(self) -> tuple[str, int]:
        positions = list(self.__positions)
        area = get_box_area(positions)
        seconds = 0
        message = ""
        while True:
            newpositions = [positions[i].step() for i, _ in enumerate(positions)]
            newarea = get_box_area(newpositions)
            if newarea < area:
                area = newarea
                positions = newpositions
                seconds += 1
            else:
                message = render_grid(positions)
                break
        return message, seconds


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_message()
    if part in (None, 1):
        p1 = r1
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
