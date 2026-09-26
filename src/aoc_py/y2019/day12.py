"""
2019 day 12 - The N-Body Problem

Part 1

Fairly straightforward simulation, just make sure to get the signs of gravity
and velocity calculations correct.

Part 2

Find the individual cycles for the (x, y, z) directions separately since they
are independent, and then use LCM to calculate the total cycle.
"""

from collections.abc import Iterator
from copy import deepcopy
from dataclasses import dataclass
from itertools import combinations
from math import lcm


@dataclass(frozen=True)
class Point3D:
    x: int
    y: int
    z: int

    @classmethod
    def parse_str(cls, s: str) -> Point3D:
        s = s.lstrip("<").rstrip(">")
        x, y, z = map(int, [p[2:] for p in s.split(", ")])
        return cls(x, y, z)

    def xyz(self) -> tuple[int, int, int]:
        return self.x, self.y, self.z

    def gravity(self, other: Point3D) -> Point3D:
        # Velocity change per axis, pointing toward `other`: -1, 0 or +1
        return Point3D(
            *((o - s > 0) - (o - s < 0) for s, o in zip(self.xyz(), other.xyz()))
        )

    def energy(self) -> int:
        return sum(abs(v) for v in self.xyz())

    def __add__(self, other: Point3D) -> Point3D:
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)


@dataclass
class Moon:
    position: Point3D
    velocity: Point3D

    def apply_gravity(self, other: Moon) -> None:
        self.velocity += self.position.gravity(other.position)

    def step(self) -> None:
        self.position += self.velocity

    def get_energy(self) -> int:
        return self.position.energy() * self.velocity.energy()

    def compare_dimensions(self, other: Moon) -> tuple[bool, bool, bool]:
        x = (self.position.x == other.position.x) and (
            self.velocity.x == other.velocity.x
        )
        y = (self.position.y == other.position.y) and (
            self.velocity.y == other.velocity.y
        )
        z = (self.position.z == other.position.z) and (
            self.velocity.z == other.velocity.z
        )
        return x, y, z


@dataclass
class MoonList:
    moons: list[Moon]

    @staticmethod
    def from_scans(scans: list[Point3D]) -> MoonList:
        return MoonList([Moon(start, Point3D(0, 0, 0)) for start in scans])

    def tick(self) -> None:
        for m1, m2 in combinations(self.moons, 2):
            m1.apply_gravity(m2)
            m2.apply_gravity(m1)
        for m in self.moons:
            m.step()

    def __iter__(self) -> Iterator[Moon]:
        return iter(self.moons)

    def total_energy(self) -> int:
        return sum(m.get_energy() for m in self)

    def matches_initial(self, start: MoonList) -> tuple[bool, bool, bool]:
        ok = (True, True, True)
        for m, s in zip(self, start):
            c = m.compare_dimensions(s)
            ok = (ok[0] and c[0], ok[1] and c[1], ok[2] and c[2])
        return ok


class InputData:
    def __init__(self, s: str) -> None:
        self.__scans = [Point3D.parse_str(line) for line in s.splitlines()]

    def get_p1(self) -> int:
        moons = MoonList.from_scans(self.__scans)
        for _ in range(1000):
            moons.tick()
        return moons.total_energy()

    def get_p2(self) -> int:
        moons = MoonList.from_scans(self.__scans)
        start = deepcopy(moons)
        cycles = [0, 0, 0]
        count = 0
        while any(c == 0 for c in cycles):
            count += 1
            moons.tick()
            for i, matched in enumerate(moons.matches_initial(start)):
                if cycles[i] == 0 and matched:
                    cycles[i] = count
        return lcm(*cycles)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
