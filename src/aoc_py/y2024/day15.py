"""
2024 day 15 - Warehouse Woes
"""

from collections import deque
from copy import deepcopy

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point


def point_from_dir(c: str) -> Point | None:
    """Converts a character to a direction. Returns None if there is no match."""
    match c:
        case ">":
            return Directions.RIGHT
        case "^":
            return Directions.UP
        case "v":
            return Directions.DOWN
        case "<":
            return Directions.LEFT
        case _:
            # There are line breaks in the input
            return None


def grid_make_wide(g: Grid) -> Grid:
    """Makes a new grid that is twice as wide."""
    x_max = 2 * g.x_max
    y_max = g.y_max
    newgrid = Grid.new(x_max, y_max, ".")
    for i, c in enumerate(g.elements):
        match c:
            case "@":
                newgrid.elements[2 * i] = c
            case "O":
                newgrid.elements[2 * i] = "["
                newgrid.elements[(2 * i) + 1] = "]"
            case _:
                newgrid.elements[2 * i] = c
                newgrid.elements[(2 * i) + 1] = c
    return newgrid


def grid_move_simple(g: Grid, pos: Point, dir: Point) -> bool:
    """Attempts to move simple (one-square) boxes recursively. Returns False if the move is not possible. Otherwise it performs the move and returns True."""
    nextpos = pos + dir
    match g.get_element(nextpos):
        case "#" | "":
            return False
        case "O" | "[" | "]":
            # Recursive move in case several boxes are lined up
            if grid_move_simple(g, nextpos, dir):
                # Make the move by swapping the characters
                c1 = g.get_element(pos)
                c2 = g.get_element(nextpos)
                g.set_point(pos, c2)
                g.set_point(nextpos, c1)
                return True
            else:
                return False
        case _:
            # Make the move by swapping the characters
            c1 = g.get_element(pos)
            c2 = g.get_element(nextpos)
            g.set_point(pos, c2)
            g.set_point(nextpos, c1)
            return True


def grid_move_double(g: Grid, pos: set[Point], dir: Point) -> None:
    """Attempts to move double (two-square)."""
    queue = deque(pos)
    while queue:
        from_point = queue.popleft()
        to_point = from_point + dir
        nextchr = g.get_element(to_point)
        if nextchr == ".":
            # _ = queue.popleft()
            c1 = g.get_element(from_point)
            g.set_point(from_point, nextchr)
            g.set_point(to_point, c1)
        else:
            queue.append(from_point)
            # queue.rotate(-1)


def grid_check_double(g: Grid, pos: Point, dir: Point, checked: set[Point]) -> bool:
    checked.add(pos)
    nextpos = pos + dir
    match g.get_element(nextpos):
        case "#" | "":
            return False
        case "[":
            rightpos = nextpos + Directions.RIGHT
            return grid_check_double(g, nextpos, dir, checked) and (
                rightpos in checked or grid_check_double(g, rightpos, dir, checked)
            )
        case "]":
            leftpos = nextpos + Directions.LEFT
            return grid_check_double(g, nextpos, dir, checked) and (
                leftpos in checked or grid_check_double(g, leftpos, dir, checked)
            )
        case _:
            return True


def grid_get_gps(g: Grid, needle: str) -> int:
    return sum(
        100 * (i // g.x_max) + i % g.x_max
        for i, c in enumerate(g.elements)
        if c == needle
    )


class InputData:
    def __init__(self, s: str) -> None:
        boxstr, movestr = s.split("\n\n")
        self.__grid = Grid(boxstr)
        self.__robot = self.__grid.find("@")
        self.__moves = [d for c in movestr if (d := point_from_dir(c)) is not None]

    def get_p1(self) -> int:
        bumped_grid = deepcopy(self.__grid)
        robot_pos = self.__robot
        for mv_dir in self.__moves:
            if grid_move_simple(bumped_grid, robot_pos, mv_dir):
                robot_pos += mv_dir
        return grid_get_gps(bumped_grid, "O")

    def get_p2(self) -> int:
        bumped_grid = grid_make_wide(self.__grid)
        robot_pos = Point(2 * self.__robot.x, self.__robot.y)
        for mv_dir in self.__moves:
            if mv_dir.y == 0:
                if grid_move_simple(bumped_grid, robot_pos, mv_dir):
                    robot_pos += mv_dir
            else:
                checked: set[Point] = set()
                if grid_check_double(bumped_grid, robot_pos, mv_dir, checked):
                    grid_move_double(bumped_grid, checked, mv_dir)
                    robot_pos += mv_dir
        return grid_get_gps(bumped_grid, "[")


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
