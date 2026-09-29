# pyright: reportAny=false, reportMissingTypeStubs=false, reportUnknownArgumentType=false, reportUnknownMemberType=false, reportUnknownVariableType=false

"""
2023 day 24 - Never Tell Me The Odds

Part 1 iterates over all combinations of intersections using itertools, and finds the intersection (if any) for
all combinations using x0, y0 = (b1*c2-b2*c1)/(a1*b2-a2*b1) , (c1*a2-c2*a1)/(a1*b2-a2*b1). y = x*dy/dx + c, so
a=dy, b=-dx, c can be found based on the given coordinate.

Part 2 uses the sympy equation solver to find the answer. I may have borrowed the basis for this solution from
people smarter than me...
"""

from dataclasses import dataclass
from itertools import combinations
from typing import Final

import sympy as sp

EXAMPLE_RANGE: Final = (7, 27)
INPUT_RANGE: Final = (200000000000000, 400000000000000)


@dataclass(frozen=True)
class Hailstone:
    x: int
    y: int
    z: int
    dx: int
    dy: int
    dz: int

    @classmethod
    def parse_str(cls, rawstr: str) -> Hailstone:
        left, right = rawstr.split(" @ ")
        x, y, z = (int(value) for value in left.split(","))
        dx, dy, dz = (int(value) for value in right.split(","))
        return cls(x, y, z, dx, dy, dz)

    def get_2d_intersection(self, other: Hailstone) -> tuple[bool, float, float]:
        """Calculates the intersection point (if any) of two hailstones in the XY plane. Also checks whether
        the intersection happens in the future. Returns a boolean to indicate whether any future intersection
        was found, and the X,Y coordinates for it."""
        a1, a2 = self.dy, other.dy
        b1, b2 = -self.dx, -other.dx
        if (d := (a1 * b2) - (a2 * b1)) == 0:
            return False, 0, 0
        c1 = -((self.x * self.dy) - (self.y * self.dx))
        c2 = -((other.x * other.dy) - (other.y * other.dx))
        x0 = ((b1 * c2) - (b2 * c1)) / d
        y0 = ((c1 * a2) - (c2 * a1)) / d
        if ((x0 > self.x and self.dx > 0) or (x0 < self.x and self.dx < 0)) and (
            (x0 > other.x and other.dx > 0) or (x0 < other.x and other.dx < 0)
        ):
            return True, x0, y0
        return False, x0, y0


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__hailstones: list[Hailstone] = [
            Hailstone.parse_str(line) for line in rawstr.splitlines()
        ]
        # The valid intersection range is a property of the puzzle input rather than something derivable
        # from the hailstones themselves, so the example and the real input have to be told apart by size.
        self.__xy_intersection_range: tuple[int, int] = (
            EXAMPLE_RANGE if len(self.__hailstones) < 10 else INPUT_RANGE
        )

    def get_p1(self) -> int:
        low, high = self.__xy_intersection_range
        intersections = 0
        for h1, h2 in combinations(self.__hailstones, 2):
            intersects, x, y = h1.get_2d_intersection(h2)
            if intersects and low <= x <= high and low <= y <= high:
                intersections += 1
        return intersections

    def get_p2(self) -> int:
        """Calculates and returns the score for part 2."""
        unknowns = sp.symbols("x y z dx dy dz t1 t2 t3")
        x, y, z, dx, dy, dz, *times = unknowns
        equations = []
        # Note: 3 stones is enough datapoints to find the solution, no need to go through the entire list
        for t, h in zip(times, self.__hailstones[:3]):
            equations.append(sp.Eq(x + t * dx, h.x + t * h.dx))
            equations.append(sp.Eq(y + t * dy, h.y + t * h.dy))
            equations.append(sp.Eq(z + t * dz, h.z + t * h.dz))
        solution = sp.solve(equations, unknowns).pop()
        return sum(solution[:3])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
