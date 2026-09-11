"""
2023 day 24 - Never Tell Me The Odds

Part 1

Iterates over all combinations of intersections using itertools, and finds the intersection (if any) for
all combinations using x0, y0 = (b1*c2-b2*c1)/(a1*b2-a2*b1) , (c1*a2-c2*a1)/(a1*b2-a2*b1). y = x*dy/dx + c, so
a=dy, b=-dx, c can be found based on the given coordinate.

Part 2

Uses the sympy equation solver to find the answer. I may have borrowed the basis for this solution from
people smarter than me...
"""

from itertools import combinations

import sympy as sp


class Hailstone:
    def __init__(self, rawstr: str) -> None:
        left, right = rawstr.split(" @ ")
        self.__x, self.__y, self.__z = list(map(int, left.split(", ")))
        self.__dx, self.__dy, self.__dz = list(map(int, right.split(", ")))

    def get_2d_intersection(
        self, other: Hailstone
    ) -> tuple[bool, float, float]:  # Intersects, x, y
        """Calculates the intersection point (if any) of two hailstones in the XY plane. Also checks whether
        the intersection happens in the future. Returns a boolean to indicate whether any future intersection
        was found, and the X,Y coordinates for it."""
        a1, a2 = self.__dy, other.__dy
        b1, b2 = -self.__dx, -other.__dx
        if (d := (a1 * b2) - (a2 * b1)) == 0:
            return False, 0, 0
        c1 = -((self.__x * self.__dy) - (self.__y * self.__dx))
        c2 = -((other.__x * other.__dy) - (other.__y * other.__dx))
        x0 = ((b1 * c2) - (b2 * c1)) / d
        y0 = ((c1 * a2) - (c2 * a1)) / d
        if (
            (x0 > self.__x and self.__dx > 0) or (x0 < self.__x and self.__dx < 0)
        ) and (
            (x0 > other.__x and other.__dx > 0) or (x0 < other.__x and other.__dx < 0)
        ):
            return True, x0, y0
        return False, x0, y0

    def get_datapoints(self) -> tuple[int, int, int, int, int, int]:
        return self.__x, self.__y, self.__z, self.__dx, self.__dy, self.__dz


class InputData:
    def __init__(self, s: str) -> None:
        self.__hailstones: list[Hailstone] = [
            Hailstone(line) for line in s.splitlines()
        ]
        # Assume test input if less than 10 stones in input
        self.xy_intersection_range = (
            (7, 27)
            if len(self.__hailstones) < 10
            else (200000000000000, 400000000000000)
        )

    def get_p1(self) -> int:
        intersections = 0
        for h1, h2 in combinations(self.__hailstones, 2):
            intersects, x, y = h1.get_2d_intersection(h2)
            if (
                intersects
                and self.xy_intersection_range[0] <= x <= self.xy_intersection_range[1]
                and self.xy_intersection_range[0] <= y <= self.xy_intersection_range[1]
            ):
                intersections += 1
        return intersections

    def get_p2(self) -> int:
        """Calculates and returns the score for part 2."""
        unknowns = sp.symbols("x y z dx dy dz t1 t2 t3")
        x, y, z, dx, dy, dz, *time = unknowns
        equations = []
        # Note: 3 stones is enough datapoints to find the solution, no need to go through the entire list
        for t, h in zip(
            time, [self.__hailstones[stone].get_datapoints() for stone in range(3)]
        ):
            equations.append(sp.Eq(x + t * dx, h[0] + t * h[3]))
            equations.append(sp.Eq(y + t * dy, h[1] + t * h[4]))
            equations.append(sp.Eq(z + t * dz, h[2] + t * h[5]))
        solution = sp.solve(equations, unknowns).pop()
        return sum(solution[:3])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
