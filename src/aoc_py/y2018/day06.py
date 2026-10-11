"""
2018 day 6 - Chronal Coordinates

Key point here is that the min and max values in each direction forms a "frame", and any location outside that will
extend to infinity. I.e. any coordinate having a location as 'closest' on or outside that area will have an infinite
area.

Part 1 just tracks, per cell, the nearest point (first/second smallest manhattan distance) and the area sizes.

Part 2 uses the fact that the manhattan distance sum separates into an x-part and a y-part, each computed in O(1)
per coordinate with sorted prefix sums.
"""

from bisect import bisect_right

from aoc_py.util.point import Point


class InputData:
    def __init__(self, s: str) -> None:
        self.__points = [Point.from_str(line) for line in s.splitlines()]

    def get_p1(self) -> int:
        points = self.__points
        xs = [p.x for p in points]
        ys = [p.y for p in points]
        x0, x1 = min(xs), max(xs)
        y0, y1 = min(ys), max(ys)
        counts: dict[int, int] = {}  # point index -> closest cells
        border: set[int] = set()  # point indices touched by the framing border
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                first = second = 10**9  # small and second-smallest distance
                first_i = -1
                for i, c in enumerate(points):
                    d = abs(x - c.x) + abs(y - c.y)
                    if d < first:
                        second = first
                        first = d
                        first_i = i
                    elif d < second:
                        second = d
                if first < second:  # skip cells that are equally close to two points
                    counts[first_i] = counts.get(first_i, 0) + 1
                    if x in (x0, x1) or y in (y0, y1):
                        border.add(first_i)
        return max(c for i, c in counts.items() if i not in border)

    def get_p2(self, max_total_distance: int = 10_000) -> int:
        points = self.__points
        n = len(points)
        xs = sorted(p.x for p in points)
        ys = sorted(p.y for p in points)
        prefix_x = [0] * (n + 1)
        prefix_y = [0] * (n + 1)
        for i in range(n):
            prefix_x[i + 1] = prefix_x[i] + xs[i]
            prefix_y[i + 1] = prefix_y[i] + ys[i]
        total_x, total_y = prefix_x[n], prefix_y[n]
        count = 0
        for x in range(xs[0], xs[-1] + 1):
            k = bisect_right(xs, x)
            fx = x * (2 * k - n) + total_x - 2 * prefix_x[k]
            for y in range(ys[0], ys[-1] + 1):
                k2 = bisect_right(ys, y)
                if (
                    fx + y * (2 * k2 - n) + total_y - 2 * prefix_y[k2]
                    < max_total_distance
                ):
                    count += 1
        return count


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
