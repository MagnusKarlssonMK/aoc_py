"""
2018 day 3 - No Matter How You Slice It

Not very efficient solution since it stores and interates over every single coordinate. It might be possible to
create a solution just based on corners, but it would be MUCH more complicated.

Simply stores the claimed squares as coordinates in a counter dict, and gets the answer to Part 1 by counting how many
squares have been counted more than once.
While doing that, mark up the claims that don't have overlap just to prune what we need to check for Part 2. Then
go over those once more and find which one still doesn't have overlap after the entire dict has been built.
"""

from aoc_py.util.point import Point


class Claim:
    id: int
    corner: Point
    x_len: int
    y_len: int

    def __init__(self, s: str) -> None:
        id, _, p, dims = s.split()
        self.id = int(id.lstrip("#"))
        self.corner = Point.from_str(p.rstrip(":"))
        x, y = dims.split("x")
        self.x_len = int(x)
        self.y_len = int(y)


class InputData:
    def __init__(self, s: str) -> None:
        self.__claims = [Claim(line) for line in s.splitlines()]

    def get_overlap_and_id(self) -> tuple[int, int]:
        seen: dict[Point, int] = {}
        possible: list[int] = []
        for i, c in enumerate(self.__claims):
            overlap = False
            for x in range(c.corner.x, c.corner.x + c.x_len):
                for y in range(c.corner.y, c.corner.y + c.y_len):
                    p = Point(x, y)
                    if p not in seen:
                        seen[p] = 1
                    else:
                        seen[p] += 1
                        overlap = True
            if not overlap:
                possible.append(i)
        overlap_count = sum([1 for s in seen if seen[s] > 1])

        while possible:
            i = possible.pop(0)
            for x in range(
                self.__claims[i].corner.x,
                self.__claims[i].corner.x + self.__claims[i].x_len,
            ):
                for y in range(
                    self.__claims[i].corner.y,
                    self.__claims[i].corner.y + self.__claims[i].y_len,
                ):
                    p = Point(x, y)
                    if seen[p] > 1:
                        break
                else:
                    continue
                break
            else:
                return overlap_count, self.__claims[i].id
        return overlap_count, -1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_overlap_and_id()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
