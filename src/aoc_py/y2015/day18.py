"""
2015 day 18 - Like a GIF For Your Yard

Uses a sets of (x,y) tuples rather than the regular grid/point utilities,
since it makes the solution significantly faster.
"""

from typing import Final


class InputData:
    __NEIGHBORS: Final = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
    ]

    def __init__(self, s: str) -> None:
        self.__live = set()
        for y, line in enumerate(s.splitlines()):
            for x, c in enumerate(line):
                if c == "#":
                    self.__live.add((x, y))
        lines = s.splitlines()
        self.__x_max, self.__y_max = len(lines[0]), len(lines)
        self.__corners = {
            (0, 0),
            (self.__x_max - 1, 0),
            (0, self.__y_max - 1),
            (self.__x_max - 1, self.__y_max - 1),
        }
        self.__nbr_steps: int = 4 if len(self.__live) < 20 else 100

    def get_p1(self) -> int:
        on_points = self.__live
        counts: dict[tuple[int, int], int] = {}
        for _ in range(self.__nbr_steps):
            for x, y in on_points:
                for dx, dy in self.__NEIGHBORS:
                    pos = (x + dx, y + dy)
                    counts[pos] = counts.get(pos, 0) + 1
            on_points = {
                pos
                for pos, n in counts.items()
                if 0 <= pos[0] < self.__x_max
                and 0 <= pos[1] < self.__y_max
                and (n == 3 or (n == 2 and pos in on_points))
            }
            counts.clear()
        return len(on_points)

    def get_p2(self) -> int:
        on_points = self.__live | self.__corners
        counts: dict[tuple[int, int], int] = {}
        for _ in range(self.__nbr_steps):
            for x, y in on_points:
                for dx, dy in self.__NEIGHBORS:
                    pos = (x + dx, y + dy)
                    counts[pos] = counts.get(pos, 0) + 1
            new_on = {
                pos
                for pos, n in counts.items()
                if 0 <= pos[0] < self.__x_max
                and 0 <= pos[1] < self.__y_max
                and (n == 3 or (n == 2 and pos in on_points))
            }
            on_points = new_on | self.__corners
            counts.clear()
        return len(on_points)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
