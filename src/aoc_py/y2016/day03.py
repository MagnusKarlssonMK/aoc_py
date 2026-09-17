"""
2016 day 3 - Squares With Three Sides

Mostly a parsing exercise, especially for Part 2. Also realizing that the condition for valid triangle can be boiled
down to just checking the sum of the two smallest sides agains the largest side; there is no need to check all
combinations.
"""


class Triangle:
    def __init__(self, side1: int, side2: int, side3: int) -> None:
        self.__sides = sorted([side1, side2, side3])

    def is_valid(self) -> bool:
        """A triangle is valid if the sum of any two sides is larger than the third side. Since the sides are already
        sorted in increasing order, we only need to check that the sum of the first two is larger than the third."""
        return self.__sides[0] + self.__sides[1] > self.__sides[2]


class InputData:
    def __init__(self, s: str) -> None:
        self.__triangles_row: list[Triangle] = []
        self.__triangles_col: list[Triangle] = []
        buffer: list[list[int]] = [[], [], []]
        for line in s.splitlines():
            nbrs = list(map(int, line.split()))
            self.__triangles_row.append(Triangle(*nbrs))
            for i, n in enumerate(nbrs):
                buffer[i].append(n)
                if len(buffer[i]) == 3:
                    self.__triangles_col.append(Triangle(*buffer[i]))
                    buffer[i] = []

    def get_p1(self) -> int:
        return sum([1 if t.is_valid() else 0 for t in self.__triangles_row])

    def get_p2(self) -> int:
        return sum([1 if t.is_valid() else 0 for t in self.__triangles_col])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
