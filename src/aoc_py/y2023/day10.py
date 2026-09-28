"""
2023 day 10 - Pipe Maze

Store the data in a grid, then for Part 1 simply walk through the system until returning to the start, then calculating
the answer by dividing the number of steps taken by 2. For part 2, calculate the answer by first determining the area
with the shoelace formula and then use that with Pick's theorem.
"""

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point


def get_connection_directions(c: str, outgoing: bool) -> tuple[Point, Point]:
    match c:
        case "-":
            return Directions.LEFT, Directions.RIGHT
        case "L":
            if outgoing:
                return Directions.UP, Directions.RIGHT
            else:
                return Directions.DOWN, Directions.LEFT
        case "J":
            if outgoing:
                return Directions.UP, Directions.LEFT
            else:
                return Directions.DOWN, Directions.RIGHT
        case "7":
            if outgoing:
                return Directions.DOWN, Directions.LEFT
            else:
                return Directions.UP, Directions.RIGHT
        case "F":
            if outgoing:
                return Directions.DOWN, Directions.RIGHT
            else:
                return Directions.UP, Directions.LEFT
        case _:  # '|'
            return Directions.UP, Directions.DOWN


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
            if (
                c := self.__grid.get_element(start_pos + d)
            ) != "" and d in get_connection_directions(c, False):
                current_dir = d
                break
        pipe_path = [start_pos]
        current_pos = start_pos + current_dir
        while current_pos != start_pos:
            pipe_path.append(current_pos)
            for d in get_connection_directions(
                self.__grid.get_element(current_pos), True
            ):
                # Every point has two connections - make sure we don't go back the way we came in
                if d.x != -current_dir.x or d.y != -current_dir.y:
                    current_dir = d
                    break
            current_pos += current_dir
        pipe_len = len(pipe_path)

        # Calculate shoelace area
        # Add start point to the end of the path to connect also the last entry
        pipe_path.append(start_pos)
        shoelace_area = (
            abs(
                sum(
                    (pipe_path[i].x * pipe_path[i + 1].y)
                    - (pipe_path[i + 1].x * pipe_path[i].y)
                    for i in range(pipe_len)
                )
            )
            // 2
        )
        # Use Pick's theorem to calculate the contained area
        area = shoelace_area + 1 - (pipe_len // 2)
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
