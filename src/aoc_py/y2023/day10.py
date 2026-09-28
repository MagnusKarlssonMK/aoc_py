"""
2023 day 10 - Pipe Maze

Store the data in a grid, then for Part 1 simply walk through the system until returning to the start, then calculating
the answer by dividing the number of steps taken by 2. For part 2, calculate the answer by first determining the area
with the shoelace formula and then use that with Pick's theorem.
"""

from typing import Final

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point

# The two directions each pipe segment connects, which are also the two directions it can be entered from.
CONNECTIONS: Final[dict[str, tuple[Point, Point]]] = {
    "|": (Directions.UP, Directions.DOWN),
    "-": (Directions.LEFT, Directions.RIGHT),
    "L": (Directions.UP, Directions.RIGHT),
    "J": (Directions.UP, Directions.LEFT),
    "7": (Directions.DOWN, Directions.LEFT),
    "F": (Directions.DOWN, Directions.RIGHT),
}


class InputData:
    def __init__(self, s: str) -> None:
        self.__grid = Grid(s)

    def get_p1_p2(self) -> tuple[int, int]:
        # Solves both part 1 and 2 in one pass
        start_pos = self.__grid.find("S")
        current_dir = Directions.UP
        # Find start direction. There can be two possible ways to move; it doesn't matter which one we
        # choose since it will be a circular path
        for d in Directions.NEIGHBORS_STRAIGHT:
            neighbor = self.__grid.get_element(start_pos + d)
            if d.reverse() in CONNECTIONS.get(neighbor, ()):
                current_dir = d
                break
        pipe_path = [start_pos]
        current_pos = start_pos + current_dir
        while current_pos != start_pos:
            pipe_path.append(current_pos)
            for d in CONNECTIONS[self.__grid.get_element(current_pos)]:
                # Every point has two connections - make sure we don't go back the way we came in
                if d != current_dir.reverse():
                    current_dir = d
                    break
            current_pos += current_dir
        pipe_len = len(pipe_path)

        # Calculate shoelace area
        areasum = sum(
            [
                p.determinant(pipe_path[(idx + 1) % len(pipe_path)])
                for idx, p in enumerate(pipe_path)
            ]
        )
        # Use Pick's theorem to calculate the contained area
        area = (abs(areasum) // 2) + 1 - (pipe_len // 2)
        return pipe_len // 2, area


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_p1_p2()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)
    return p1, p2
