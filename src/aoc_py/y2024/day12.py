"""
2024 day 12 - Garden Groups
"""
from itertools import combinations

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__map = Grid(rawstr)

    def get_costs(self) -> tuple[int, int]:
        total_perimeter = total_sides = 0
        counted: set[Point] = set()
        for i, _ in enumerate(self.__map.elements):
            if (p := self.__map.get_point(i)) not in counted:
                area = perimeter = sides = 0
                group: set[Point] = set()
                queue: list[Point] = [p]
                neighbor_states: list[tuple[Point, int]] = []
                while queue:
                    current = queue.pop(0)
                    if current in counted:
                        continue
                    counted.add(current)
                    group.add(current)
                    area += 1
                    value_current = self.__map.get_element(current)

                    for dir in Directions.NEIGHBORS_STRAIGHT:
                        neighbor = current + dir
                        if (v := self.__map.get_element(neighbor)) != "":
                            if v == value_current:
                                queue.append(neighbor)
                                neighbor_states.append((dir, 1))
                            else:
                                perimeter += 1
                                neighbor_states.append((dir, 0))
                        else:
                            perimeter += 1
                            neighbor_states.append((dir, 0))
                    # Check the combinations of straight neighbors to evaluate corners
                    for (n1, v1), (n2, v2) in combinations(neighbor_states, 2):
                        if (n1.x == 0 and n2.x == 0) or (n1.y == 0 and n2.y == 0):
                            continue
                        if ((v1 == 0 and v2 == 0) or
                            (v1 == 1 and v2 == 1 and self.__map.get_element(current + n1 + n2) != value_current)):
                            sides += 1
                    neighbor_states.clear()
                total_perimeter += area * perimeter
                total_sides += area * sides
        return total_perimeter, total_sides


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
        p1, p2 = "-1"
        p = InputData(inputdata)
        r1, r2 = p.get_costs()
        if part in (None, 1):
            p1 = str(r1)
        if part in (None, 2):
            p2 = str(r2)

        return p1, p2
