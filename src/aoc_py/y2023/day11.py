"""
2023 day 11 - Cosmic Expansion

Stores the coordinates of the galaxies in the input, together with the rows and columns that hold at least one
galaxy. Part 1 and part 2 differ only in how wide the empty rows and columns become, so rather than counting the
empty lines between each pair of galaxies, the galaxies are moved to the coordinates they would have if the empty
rows and columns had already been widened, and the answer is then the sum of the manhattan distances between all
pairs. Doing it that way also means that each part is a calculation of its own instead of a shared one.
"""

from itertools import combinations

from aoc_py.util.point import Point


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__galaxies: list[Point] = [
            Point(x, y)
            for y, line in enumerate(rawstr.splitlines())
            for x, c in enumerate(line)
            if c == "#"
        ]
        self.__x_occupied = {g.x for g in self.__galaxies}
        self.__y_occupied = {g.y for g in self.__galaxies}

    @staticmethod
    def __get_expanded_positions(occupied: set[int], exp_rate: int) -> dict[int, int]:
        """Returns the position each occupied coordinate would have if every empty coordinate in
        between was widened to exp_rate tiles."""
        positions: dict[int, int] = {}
        extra = 0
        for coord in range(max(occupied) + 1):
            if coord not in occupied:
                extra += exp_rate - 1
            positions[coord] = coord + extra
        return positions

    def get_distance_sum(self, exp_rate: int) -> int:
        """Sums the manhattan distances between all pairs of galaxies, with every empty row and
        column widened to exp_rate tiles."""
        xs = self.__get_expanded_positions(self.__x_occupied, exp_rate)
        ys = self.__get_expanded_positions(self.__y_occupied, exp_rate)
        galaxies = [Point(xs[g.x], ys[g.y]) for g in self.__galaxies]
        return sum([g1.manhattan(g2) for g1, g2 in combinations(galaxies, 2)])

    def get_p1(self) -> int:
        return self.get_distance_sum(2)

    def get_p2(self) -> int:
        return self.get_distance_sum(1_000_000)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
