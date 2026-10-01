"""
2024 day 6 - Guard Gallivant
"""

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point


class InputData:
    def __init__(self, s: str) -> None:
        self.__grid = Grid(s)

    def solve(self) -> tuple[int, int]:
        start_pos = self.__grid.find("^")

        # Create jump table - list matching grid list, every element is a dict [direction: [target point, out_of_bounds_flag]]
        jump_table: list[dict[Point, tuple[Point, bool]]] = [
            {} for _ in self.__grid.elements
        ]
        for d in Directions.NEIGHBORS_STRAIGHT:
            for i, c in enumerate(self.__grid.elements):
                if c == "#":
                    continue
                p = self.__grid.get_point(i)
                while True:
                    np = p + d
                    if (nc := self.__grid.get_element(np)) == "":
                        jump_table[i][d] = p, True
                        break
                    elif nc == "#":
                        jump_table[i][d] = p, False
                        break
                    p = np

        # Simulate part 1 and record the path
        current_point = start_pos
        current_dir = Directions.UP
        base_path: list[tuple[Point, Point]] = []
        while self.__grid.get_element(current_point) != "":
            base_path.append((current_point, current_dir))
            next_point = current_point + current_dir
            if self.__grid.get_element(next_point) == "#":
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
                np, oob = jump_table[self.__grid.get_index(cp)][cd]

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
