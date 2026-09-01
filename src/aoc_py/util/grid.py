from aoc_py.util.point import Point


class Grid:
    def __init__(self, s: str):
        '''Creates a new Grid object based on the string input.
        Assumes that the input is in valid format.'''
        lines = s.splitlines()
        self.x_max: int = len(lines[0])
        self.y_max: int = len(lines)
        self.elements: list[str] = [c for c in s if c != "\n"]

    def get_element(self, p: Point) -> str:
        '''Returns the element in a certain point in the grid.
        If the input point is out-of-bounds, an empty string is returned.'''
        if 0 <= p.x < self.x_max and 0 <= p.y < self.y_max:
            return self.elements[(self.x_max * p.y) + p.x]
        else:
            return ""

    def find(self, item: str) -> Point:
        '''Searches the Grid for an element matching item. The first one found
        will be returned as a Point, searching top left to the right and then down.
        If no match is found, (-1, -1) is returned.'''
        for i, e in enumerate(self.elements):
            if e == item:
                return Point(i % self.x_max, i // self.x_max)
        return Point(-1, -1)

    def get_index(self, p: Point) -> int:
        '''Returns the Point corresponding to an index in the Grid element array.
        Will return -1 if the input is out-of-bounds.'''
        if 0 <= p.x < self.x_max and 0 <= p.y < self.y_max:
            return self.x_max * p.y + p.x
        else:
            return -1

    def set_point(self, p: Point, v: str):
        '''Sets the Point p to the value v. Will do nothing if p is out-of-bounds.'''
        if 0 <= p.x < self.x_max and 0 <= p.y < self.y_max:
            self.elements[self.x_max * p.y + p.x] = v
