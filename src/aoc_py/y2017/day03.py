"""
2017 day 3 - Spiral Memory

Part 1

This could be solved algebraicly, since the lower right corner is n^2 with n=1,3,5,7... In other words, given a
certain number, we can use this to calculate the corners for the value of 'n' that will contain this number, and from
there figure out the manhattan distance from the center. However, this is somewhat cumbersome, and doesn't carry over
at all for part 2, so instead I'll just stick with simply 'drawing' the spiral to find the answer. The input number
is still low enough that this is a somewhat reasonable approach in terms of execution speed.

Part 2

Pretty much the same thing, but the value of each cell is the sum of the already-written values of its eight
neighbours. Both parts share a generator that walks the spiral outward from the center.
"""

from collections.abc import Iterator
from itertools import islice

from aoc_py.util.point import Directions, Point


class InputData:
    def __init__(self, s: str) -> None:
        self.__target = int(s)

    def __spiral(self) -> Iterator[Point]:
        # Walk the spiral counter-clockwise, turning left whenever the cell to the left is already visited.
        head = Directions.ORIGIN
        direction = Directions.DOWN
        visited: set[Point] = {head}
        yield head
        while True:
            left = direction.rotate_left()
            if head + left in visited:
                head += direction
            else:
                direction = left
                head += left
            visited.add(head)
            yield head

    def get_p1(self) -> int:
        point = next(islice(self.__spiral(), self.__target - 1, None))
        return point.manhattan(Directions.ORIGIN)

    def get_p2(self) -> int:
        values: dict[Point, int] = {}
        value = 1
        points = self.__spiral()
        while value < self.__target:
            point = next(points)
            value = (
                1
                if point == Directions.ORIGIN
                else sum(
                    values.get(n, 0)
                    for n in (point + d for d in Directions.NEIGHBORS_ALL)
                )
            )
            values[point] = value
        return value


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
