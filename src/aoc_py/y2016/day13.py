"""
2016 day 13 - A Maze of Twisty Little Cubicles

Simple BFS solution, and implementing the neighbor generator function in a point class.
The only difference between Part 1 & 2 is in the stop condition for the search function; in part 1 we are looking
for a specific target node, while for part 2 we want to walk 50 steps and then check number of seen nodes.
"""

from collections.abc import Generator

from aoc_py.util.point import Directions, Point


def get_neighbors(p: Point, keyval: int) -> Generator[Point]:
    """Generates possible neighbors that are open space according to the specified algorithm."""
    for n in [p + d for d in Directions.NEIGHBORS_STRAIGHT]:
        x = n.x
        y = n.y
        if x < 0 or y < 0:
            continue
        val = (x * x) + (3 * x) + (2 * x * y) + y + (y * y) + keyval
        if val.bit_count() % 2 == 0:
            yield Point(x, y)


class InputData:
    def __init__(self, s: str) -> None:
        self.__favorite_nbr = int(s)

    def get_count(self, targetpoint: Point, steplimit: int) -> int:
        """BFS to find either the least number of steps to reach the target point (steplimit = 0), or count the
        number of reachable nodes within [steplimit > 0] steps."""
        currentpoint = Point(1, 1)
        seen: set[Point] = set()
        queue: list[tuple[Point, int]] = [(currentpoint, 0)]
        while queue:
            currentpoint, steps = queue.pop(0)
            if not steplimit and currentpoint == targetpoint:
                return steps
            if currentpoint in seen or (steplimit and steps > steplimit):
                continue
            seen.add(currentpoint)
            for p in get_neighbors(currentpoint, self.__favorite_nbr):
                queue.append((p, steps + 1))
        return len(seen)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_count(Point(31, 39), 0))
    if part in (None, 2):
        p2 = str(p.get_count(Point(0, 0), 50))

    return p1, p2
