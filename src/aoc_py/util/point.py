from dataclasses import dataclass
from typing import Final


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def from_str(self, s: str) -> Point:
        '''Creates a new point based on a string. Supports separators [',', '-'].
        Returns x=y=-1 and prints a warning if parsing fails.'''
        v = s.split(",")
        if len(v) == 2:
            return Point(int(v[0]), int(v[1]))
        v = s.split("-")
        if len(v) == 2:
            return Point(int(v[0]), int(v[1]))
        print(f"Can't parse point from string: {s}")
        return Point(-1, -1)

    def rotate_left(self) -> Point:
        '''Rotates the point left.'''
        return Point(self.y, -self.x)

    def rotate_right(self) -> Point:
        '''Rotates the point right.'''
        return Point(-self.y, self.x)

    def manhattan(self, other: Point) -> int:
        '''Calculates the manhattan distance between two points.'''
        return abs(self.x - other.x) + abs(self.y - other.y)

    def determinant(self, other: Point) -> int:
        '''Calculates the determinant of two points.'''
        return (self.x * other.y) - (self.y * other.x)

    def reverse(self) -> Point:
        '''Creates the reversed point.'''
        return Point(self.x * -1, self.y * -1)

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Point) -> Point:
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, m: int) -> Point:
        return Point(self.x * m, self.y * m)

    def __lt__(self, other: Point) -> bool:
        return self.y < other.y if self.y != other.y else self.x < other.x


class Directions:
    ORIGIN: Final = Point(0, 0)
    LEFT: Final = Point(-1, 0)
    RIGHT: Final = Point(1, 0)
    UP: Final = Point(0, -1)
    DOWN: Final = Point(0, 1)

    DIAG_R_D: Final = Point(1, 1)
    DIAG_L_D: Final = Point(-1, 1)
    DIAG_L_U: Final = Point(-1, -1)
    DIAG_R_U: Final = Point(1, -1)

    NEIGHBORS_STRAIGHT: Final = [RIGHT, DOWN, LEFT, UP]
    NEIGHBORS_ALL: Final = [RIGHT, DIAG_R_D, DOWN, DIAG_L_D, LEFT, DIAG_L_U, UP, DIAG_R_U]
