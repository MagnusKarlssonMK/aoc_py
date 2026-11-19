"""
2023 day 10 - Pipe Maze

Store the data in a grid, then for Part 1 simply walk through the system until returning to the
start, then calculating the answer by dividing the number of steps taken by 2. For part 2,
calculate the answer by first determining the area with the shoelace formula and then use that with
Pick's theorem.
"""

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point


def next_direction(c: str, in_dir: Point) -> Point | None:
    match in_dir:
        case Directions.UP:
            match c:
                case "|":
                    return Directions.UP
                case "7":
                    return Directions.LEFT
                case "F":
                    return Directions.RIGHT
                case _:
                    return None
        case Directions.DOWN:
            match c:
                case "|":
                    return Directions.DOWN
                case "J":
                    return Directions.LEFT
                case "L":
                    return Directions.RIGHT
                case _:
                    return None
        case Directions.LEFT:
            match c:
                case "-":
                    return Directions.LEFT
                case "L":
                    return Directions.UP
                case "F":
                    return Directions.DOWN
                case _:
                    return None
        case Directions.RIGHT:
            match c:
                case "-":
                    return Directions.RIGHT
                case "J":
                    return Directions.UP
                case "7":
                    return Directions.DOWN
                case _:
                    return None


def get_area(p1: Point, p2: Point) -> int:
    return p1.x * p2.y - p2.x * p1.y


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
            if next_direction(neighbor, d) is not None:
                current_dir = d
                break

        current_pos = start_pos + current_dir
        pipe_len = 1
        shoelace_area = get_area(current_pos, start_pos)
        while current_pos != start_pos:
            if (c := self.__grid.get_element(current_pos)) != "" and (
                new_dir := next_direction(c, current_dir)
            ) is not None:
                current_dir = new_dir
                new_pos = current_pos + current_dir
                pipe_len += 1
                shoelace_area += get_area(new_pos, current_pos)
                current_pos = new_pos
            else:
                return -1, -1

        shoelace_area = abs(shoelace_area) // 2
        pipe_len //= 2
        # Use Pick's theorem to calculate the contained area
        area = shoelace_area + 1 - pipe_len
        return pipe_len, area


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_p1_p2()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)
    return p1, p2
