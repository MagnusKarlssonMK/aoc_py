from typing import override

from aoc_py.util.point import Point


class Grid:
    def __init__(self, s: str):
        """Creates a new Grid object based on the string input.
        Assumes that the input is in valid format."""
        lines = s.splitlines()
        self.x_max: int = len(lines[0])
        self.y_max: int = len(lines)
        self.elements: list[str] = [c for c in s if c != "\n"]

    @classmethod
    def new(cls, x_max: int, y_max: int, val: str) -> Grid:
        s = "\n".join([val * x_max for _ in range(y_max)])
        return cls(s)

    def get_element(self, p: Point) -> str:
        """Returns the element in a certain point in the grid.
        If the input point is out-of-bounds, an empty string is returned."""
        if 0 <= p.x < self.x_max and 0 <= p.y < self.y_max:
            return self.elements[(self.x_max * p.y) + p.x]
        else:
            return ""

    def find(self, item: str, reverse: bool = False) -> Point:
        """Searches the Grid for an element matching item. The first one found
        will be returned as a Point, searching top left to the right and then down.
        If reverse is True, the search starts from the bottom right and goes up and
        left, returning the last match. If no match is found, (-1, -1) is returned."""
        rng = (
            range(len(self.elements) - 1, -1, -1)
            if reverse
            else range(len(self.elements))
        )
        for i in rng:
            if self.elements[i] == item:
                return Point(i % self.x_max, i // self.x_max)
        return Point(-1, -1)

    def find_all(self, item: str) -> list[Point]:
        """Searches the Grid for all elements matching item, and returns a list
        of Point."""
        return [
            Point(i % self.x_max, i // self.x_max)
            for i, e in enumerate(self.elements)
            if e == item
        ]

    def get_index(self, p: Point) -> int:
        """Returns the index corresponding to a Point in the Grid element array.
        Will return -1 if the input Point is out-of-bounds."""
        if 0 <= p.x < self.x_max and 0 <= p.y < self.y_max:
            return self.x_max * p.y + p.x
        else:
            return -1

    def get_point(self, index: int) -> Point:
        """Returns the Point corresponding to a certain index. Typically used when iterating
        through elements in the grid."""
        x = index % self.x_max
        y = index // self.x_max
        return Point(x, y)

    def set_point(self, p: Point, v: str):
        """Sets the Point p to the value v. Will do nothing if p is out-of-bounds."""
        if 0 <= p.x < self.x_max and 0 <= p.y < self.y_max:
            self.elements[self.x_max * p.y + p.x] = v

    @override
    def __str__(self) -> str:
        r = ""
        for i, c in enumerate(self.elements):
            r += c
            if (i + 1) % self.x_max == 0:
                r += "\n"
        return r
