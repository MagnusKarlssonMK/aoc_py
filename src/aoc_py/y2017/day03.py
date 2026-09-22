"""
2017 day 3 - Spiral Memory

Part 1

This could be solved algebraicly, since the lower right corner is n^2 with n=1,3,5,7... In other words, given a
certain number, we can use this to calculate the corners for the value of 'n' that will contain this number, and from
there figure out the manhattan distance from the center. However, this is somewhat cumbersome, and doesn't carry over
at all for part 2, so instead I'll just stick with simply 'drawing' the spiral to find the answer. The input number
is still low enough that this is a somewhat reasonable approach in terms of execution speed.

Part 2

Pretty much the same thing, just with a small modification for how to keep track of the current number while
building the spiral.
"""

from aoc_py.util.point import Directions, Point


class InputData:
    def __init__(self, s: str) -> None:
        self.__nbr = int(s)

    def get_p1(self) -> int:
        head = Directions.ORIGIN
        direction = Directions.DOWN
        value = 1
        visited: set[Point] = {head}
        while value < self.__nbr:
            left_direction = direction.rotate_left()
            left_point = head + left_direction
            if left_point in visited:
                head += direction
            else:
                direction = left_direction
                head = left_point
            visited.add(head)
            value += 1
        return head.manhattan(Directions.ORIGIN)

    def get_p2(self) -> int:
        head = Directions.ORIGIN
        direction = Directions.DOWN
        value = 1
        visited: dict[Point, int] = {head: value}
        while value < self.__nbr:
            left_direction = direction.rotate_left()
            left_point = head + left_direction
            if left_point in visited:
                head += direction
            else:
                direction = left_direction
                head = left_point
            value = sum(
                [
                    visited.get(n, 0)
                    for n in [head + d for d in Directions.NEIGHBORS_ALL]
                ]
            )
            visited[head] = value
        return value


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
