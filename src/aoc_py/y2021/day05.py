"""
2021 day 5 - Hydrothermal Venture
"""

from aoc_py.util.grid import Grid
from aoc_py.util.point import Point


def is_diagonal(p1: Point, p2: Point) -> bool:
    return p1.x != p2.x and p1.y != p2.y


def get_direction(p1: Point, p2: Point) -> Point:
    """Returns a normalized directional step vector from p1 to a p2 as a new Point."""
    dx = (p2.x - p1.x) // max(abs(p2.x - p1.x), abs(p2.y - p1.y), 1)
    dy = (p2.y - p1.y) // max(abs(p2.x - p1.x), abs(p2.y - p1.y), 1)
    return Point(dx, dy)


class OceanFloor:
    def __init__(self, x: int, y: int) -> None:
        self.__grid = Grid.new(x, y, "0")
        self.nbr_dangerous_points: int = 0

    def process_line(self, p1: Point, p2: Point) -> None:
        direction = get_direction(p1, p2)
        p = p1
        while True:
            match self.__grid.get_element(p):
                case "0":
                    self.__grid.set_point(p, "1")
                case "1":
                    self.__grid.set_point(p, "2")
                    self.nbr_dangerous_points += 1
                case _:
                    pass
            if p == p2:
                break
            p += direction


class InputData:
    def __init__(self, s: str) -> None:
        self.__x_max = self.__y_max = 0
        self.__straight_lines: list[tuple[Point, Point]] = []
        self.__diagonal_lines: list[tuple[Point, Point]] = []
        for line in s.splitlines():
            left, right = line.split(" -> ")
            p1 = Point.from_str(left)
            p2 = Point.from_str(right)
            if is_diagonal(p1, p2):
                self.__diagonal_lines.append((p1, p2))
            else:
                self.__straight_lines.append((p1, p2))
            self.__x_max = max(self.__x_max, p1.x, p2.x)
            self.__y_max = max(self.__y_max, p1.y, p2.y)

    def get_score(self) -> tuple[int, int]:
        ocean = OceanFloor(self.__x_max + 1, self.__y_max + 1)
        p1 = p2 = 0
        for straight_line in self.__straight_lines:
            ocean.process_line(*straight_line)
        p1 = ocean.nbr_dangerous_points

        for diagonal_line in self.__diagonal_lines:
            ocean.process_line(*diagonal_line)
        p2 = ocean.nbr_dangerous_points
        return p1, p2


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_score()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
