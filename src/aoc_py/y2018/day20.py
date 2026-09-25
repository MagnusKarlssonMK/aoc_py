"""
2018 day 20 - A Regular Map

Build a dictionary of distances while expanding the map through reading the regex and treating the input like a stack.
From that we can get the answer to part1 just by finding the maximum distance value in the dict, and the answer to
part 2 by counting the number of keys with a distance value of at least 1000.
"""

from typing import Final

from aoc_py.util.point import Directions, Point


class InputData:
    __DIRMAP: Final = {
        "N": Directions.UP,
        "E": Directions.RIGHT,
        "S": Directions.DOWN,
        "W": Directions.LEFT,
    }

    def __init__(self, rawstr: str) -> None:
        self.__path = rawstr[1:-1]

    def get_fewest_doors(self) -> tuple[int, int]:
        positions: list[Point] = []
        distances: dict[Point, int] = {}
        current_pos = Directions.ORIGIN
        previous_pos = Directions.ORIGIN
        for c in self.__path:
            if c == "(":
                positions.append(current_pos)
            elif c == ")":
                current_pos = positions.pop()
            elif c == "|":
                current_pos = Point(positions[-1].x, positions[-1].y)
            else:
                current_pos = current_pos + self.__DIRMAP[c]
                previous_distance = distances.get(previous_pos, 0)
                if current_pos in distances:
                    distances[current_pos] = min(
                        distances[current_pos], previous_distance + 1
                    )
                else:
                    distances[current_pos] = previous_distance + 1
            previous_pos = Point(current_pos.x, current_pos.y)
        p1 = max(distances.values())
        p2 = sum([1 for val in distances.values() if val >= 1000])
        return p1, p2


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_fewest_doors()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
