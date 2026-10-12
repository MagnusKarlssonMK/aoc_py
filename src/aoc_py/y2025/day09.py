"""
2025 day 9 - Movie Theater

Part 1

Store every rectangle that can be formed by two red tiles (skipping adjacent tiles, which only
span a line) and return the largest area.

Part 2

Also build the closed polygon's axis-aligned edges. Walking the rectangles from largest to
smallest, the first one whose interior is not crossed by any edge is the largest valid
rectangle. Checking every edge per rectangle is brute force, but stopping at the first valid
rectangle keeps the number of checks down.
"""

from dataclasses import dataclass

from aoc_py.util.point import Point


@dataclass(frozen=True)
class Rectangle:
    area: int
    upper_left: Point
    lower_right: Point

    @classmethod
    def from_points(cls, p1: Point, p2: Point) -> Rectangle:
        min_x, max_x = min(p1.x, p2.x), max(p1.x, p2.x)
        min_y, max_y = min(p1.y, p2.y), max(p1.y, p2.y)
        area = (1 + max_x - min_x) * (1 + max_y - min_y)
        return cls(area, Point(min_x, min_y), Point(max_x, max_y))


@dataclass(frozen=True)
class Line:
    base_point: Point
    length: int
    is_horizontal: bool

    @classmethod
    def from_points(cls, p1: Point, p2: Point) -> Line:
        if p1.x == p2.x:
            return cls(Point(p1.x, min(p1.y, p2.y)), abs(p1.y - p2.y), False)
        return cls(Point(min(p1.x, p2.x), p1.y), abs(p1.x - p2.x), True)

    def intersects_rectangle(self, r: Rectangle) -> bool:
        # A line fully inside the rectangle also counts, since all lines are contiguous: if one
        # edge is inside then another edge must cross somewhere, so the rectangle is invalid.
        if self.is_horizontal:
            return (
                r.upper_left.y < self.base_point.y < r.lower_right.y
                and self.base_point.x < r.lower_right.x
                and self.base_point.x + self.length > r.upper_left.x
            )
        return (
            r.upper_left.x < self.base_point.x < r.lower_right.x
            and self.base_point.y < r.lower_right.y
            and self.base_point.y + self.length > r.upper_left.y
        )


class InputData:
    def __init__(self, rawstr: str) -> None:
        red_tiles = [Point.from_str(line) for line in rawstr.splitlines()]
        self.__rectangles: list[Rectangle] = [
            Rectangle.from_points(red_tiles[i], red_tiles[j])
            for i in range(len(red_tiles) - 2)
            for j in range(i + 2, len(red_tiles))
        ]
        self.__lines: list[Line] = [
            Line.from_points(red_tiles[i], red_tiles[i + 1])
            for i in range(len(red_tiles) - 1)
        ]
        self.__lines.append(Line.from_points(red_tiles[-1], red_tiles[0]))

    def __is_rectangle_valid(self, r: Rectangle) -> bool:
        return not any(line.intersects_rectangle(r) for line in self.__lines)

    def get_p1(self) -> int:
        return max(r.area for r in self.__rectangles)

    def get_p2(self) -> int:
        largest = 0
        for rectangle in sorted(self.__rectangles, key=lambda r: r.area, reverse=True):
            if self.__is_rectangle_valid(rectangle):
                largest = rectangle.area
                break
        return largest


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
