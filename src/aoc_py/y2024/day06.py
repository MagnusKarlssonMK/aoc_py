"""
2024 day 6 - Guard Gallivant

Starts with creating a jump table based on the grid, storing how far in each direction
the guard can go before either encountering an obstacle or falling out-of-bounds. The
table is filled in linear time by walking each direction backwards, so every cell
inherits the reachable target of its neighbour ahead of it.

Then the base path the guard takes is simulated by moving step-by-step and recording
each point+direction pair along the way, until the guard walks off the grid boundary.
The answer to part 1 can then be found by calculating the length of a set of points,
generated from the point-part of the tuples in the base path list.

Then for part 2, iterate through each consecutive pair in the base path and put a
temporary obstacle in the second point, then use the jump table to step through the
grid and see if a loop is established. The number of loops found is the answer to part 2.
"""

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__grid = Grid(rawstr)

    def solve(self) -> tuple[int, int]:
        grid = self.__grid
        width, height, elements = grid.x_max, grid.y_max, grid.elements
        start_pos = grid.find("^")

        # Create jump table - list matching grid list, every element is a dict
        # [direction: [target point, out_of_bounds_flag]]. Processing each direction
        # from the far edge inwards makes the target of a cell either the cell itself
        # (a wall or boundary lies directly ahead) or the target of the next cell.
        jump_table: list[dict[Point, tuple[Point, bool]]] = [{} for _ in elements]
        for d in Directions.NEIGHBORS_STRAIGHT:
            y_range = range(height) if d.y <= 0 else range(height - 1, -1, -1)
            x_range = range(width) if d.x <= 0 else range(width - 1, -1, -1)
            for y in y_range:
                for x in x_range:
                    i = y * width + x
                    if elements[i] == "#":
                        continue
                    nx, ny = x + d.x, y + d.y
                    if not (0 <= nx < width and 0 <= ny < height):
                        jump_table[i][d] = Point(x, y), True
                    else:
                        ni = ny * width + nx
                        jump_table[i][d] = (
                            (Point(x, y), False)
                            if elements[ni] == "#"
                            else jump_table[ni][d]
                        )

        # Simulate part 1 and record the path
        current_point = start_pos
        current_dir = Directions.UP
        base_path: list[tuple[Point, Point]] = []
        while grid.get_element(current_point) != "":
            base_path.append((current_point, current_dir))
            next_point = current_point + current_dir
            if grid.get_element(next_point) == "#":
                current_dir = current_dir.rotate_right()
            else:
                current_point += current_dir

        p1 = len({p for p, _ in base_path})

        p2 = 0
        obstacles_tried: set[Point] = set()
        # Go through the base path in pairs. For every pair of points try to insert a new obstacle
        # in the second point and follow the new path from the first point. If both points
        # are the same, jump directly to the next pair since it means we made a turn on this
        # step. Keep track of which obstacles have been tried in case the same point appears
        # again later in the base path
        for i in range(len(base_path) - 1):
            cp, cd = base_path[i]
            new_obstacle, _ = base_path[i + 1]
            if new_obstacle in obstacles_tried or cp == new_obstacle:
                continue
            obstacles_tried.add(new_obstacle)

            visited: set[tuple[Point, Point]] = set()
            while True:
                state = cp, cd
                if state in visited:
                    p2 += 1
                    break
                visited.add(state)
                np, oob = jump_table[grid.get_index(cp)][cd]

                # Check if the new obstacle blocks this straight run. The cell
                # range is half-open: strictly ahead of the guard, up to and
                # including the cell the guard would otherwise have reached.
                sign = 1 if cd.x + cd.y > 0 else -1
                blocked = (
                    cd.x == 0
                    and cp.x == new_obstacle.x
                    and 0 < sign * (new_obstacle.y - cp.y) <= sign * (np.y - cp.y)
                ) or (
                    cd.y == 0
                    and cp.y == new_obstacle.y
                    and 0 < sign * (new_obstacle.x - cp.x) <= sign * (np.x - cp.x)
                )
                if blocked:
                    cp = Point(new_obstacle.x - cd.x, new_obstacle.y - cd.y)
                    cd = cd.rotate_right()
                elif oob:
                    break
                else:
                    cp = np
                    cd = cd.rotate_right()
        return p1, p2


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    r1, r2 = InputData(inputdata).solve()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
