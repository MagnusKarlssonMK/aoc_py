"""
2024 day 18 - RAM Run

The falling bytes are marked on a square memory grid and a breadth-first search finds the
shortest path from the origin to the opposite corner. Part 1 marks the first 1024 bytes,
while part 2 uses bisection over the number of marked bytes to find the last byte that still
leaves a path open. The grid size and the part 1 byte count are kept as module constants so
tests can shrink them.
"""

from collections import deque

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point

GRID_DIM = 71
PART1_BYTES = 1024


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__bytes = [Point.from_str(line) for line in rawstr.splitlines()]

    def __shortest_path(self, fallen: int) -> int | None:
        """BFS from the origin to the opposite corner on the grid with the first `fallen`
        bytes marked. Returns the number of steps, or None if the exit is unreachable."""
        grid = Grid.new(GRID_DIM, GRID_DIM, ".")
        for p in self.__bytes[:fallen]:
            grid.set_point(p, "#")
        exit = Point(GRID_DIM - 1, GRID_DIM - 1)
        seen: set[Point] = set()
        queue: deque[tuple[Point, int]] = deque([(Directions.ORIGIN, 0)])
        while queue:
            current, steps = queue.popleft()
            if current == exit:
                return steps
            if current in seen:
                continue
            seen.add(current)
            for neighbor in [current + d for d in Directions.NEIGHBORS_STRAIGHT]:
                if grid.get_element(neighbor) in ("", "#") or neighbor in seen:
                    continue
                queue.append((neighbor, steps + 1))
        return None

    def get_p1(self) -> int:
        steps = self.__shortest_path(PART1_BYTES)
        assert steps is not None
        return steps

    def get_p2(self) -> str:
        lowest = PART1_BYTES
        highest = len(self.__bytes)
        while lowest < highest - 1:
            tryval = (highest + lowest) // 2
            if self.__shortest_path(tryval) is not None:
                lowest = tryval
            else:
                highest = tryval
        byte = self.__bytes[lowest]
        return f"{byte.x},{byte.y}"


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = p.get_p2()

    return p1, p2
