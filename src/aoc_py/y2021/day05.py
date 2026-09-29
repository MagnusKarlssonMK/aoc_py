"""
2021 day 5 - Hydrothermal Venture

Split the input into straight and diagonal line segments, tracking the largest coordinate
on each axis so that the ocean floor can be sized to fit. Each point on the floor is
promoted from clear to covered the first time a line reaches it, and from covered to
dangerous the first time a second line reaches it, so counting promotions counts every
dangerous point exactly once no matter how many lines happen to cross there.
Part 1 replays only the straight lines; Part 2 replays the diagonals onto the same floor.
"""

from aoc_py.util.grid import Grid
from aoc_py.util.point import Point


def is_diagonal(p1: Point, p2: Point) -> bool:
    """Returns True if the line from p1 to p2 changes both coordinates."""
    return p1.x != p2.x and p1.y != p2.y


def get_direction(p1: Point, p2: Point) -> Point:
    """Returns a normalized directional step vector from p1 to a p2 as a new Point."""
    dx = (p2.x - p1.x) // max(abs(p2.x - p1.x), abs(p2.y - p1.y), 1)
    dy = (p2.y - p1.y) // max(abs(p2.x - p1.x), abs(p2.y - p1.y), 1)
    return Point(dx, dy)


class OceanFloor:
    def __init__(self, x: int, y: int) -> None:
        self.__grid = Grid.new(x, y, "0")

    def process_line(self, p1: Point, p2: Point) -> int:
        """Marks every point along the line, returning the number of points that this
        makes dangerous, i.e. those covered here for the first time by two or more lines."""
        nbr_dangerous = 0
        direction = get_direction(p1, p2)
        p = p1
        while True:
            match self.__grid.get_element(p):
                case "0":
                    self.__grid.set_point(p, "1")
                case "1":
                    self.__grid.set_point(p, "2")
                    nbr_dangerous += 1
                case _:  # Grid only ever holds "0", "1" or "2"; here for exhaustiveness
                    pass
            if p == p2:
                break
            p += direction
        return nbr_dangerous


class InputData:
    def __init__(self, s: str) -> None:
        self.__x_max: int = 0
        self.__y_max: int = 0
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
        p1 = sum(ocean.process_line(*line) for line in self.__straight_lines)
        p2 = p1 + sum(ocean.process_line(*line) for line in self.__diagonal_lines)
        return p1, p2


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_score()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
