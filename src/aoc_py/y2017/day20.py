"""
2017 day 20 - Particle Swarm

Part 1: Note that the question is which particle will be closest *in the long term*, not the closest ever over the
entire trajectory. In the long term, the closest will be the one with the lowest acceleration. However, with my
input, there's multiple particles sharing the same lowest acceleration, and making a secondary sorting on initial
velocity is not safe since it depends on the relative direction between velocity and acceleration. Instead of
simulating step by step and hoping that a fixed number of steps is enough, we evaluate each particle's position
after `steps` steps in closed form:

    p(t) = p0 + v0 * t + a * t * (t + 1) / 2

and pick the one with the smallest distance from the origin at that point in time.

Part 2: Simulate the swarm, updating particles in place, and after every step remove all particles that share a
position with another particle.
"""

import re
from collections import Counter
from dataclasses import dataclass
from typing import Self


@dataclass(slots=True)
class Point3D:
    x: int
    y: int
    z: int

    def get_distance(self, other: Point3D) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

    def __add__(self, other: Point3D) -> Point3D:
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other: Point3D) -> Self:
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __mul__(self, factor: int) -> Point3D:
        return Point3D(self.x * factor, self.y * factor, self.z * factor)

    def copy(self) -> Point3D:
        return Point3D(self.x, self.y, self.z)


@dataclass(slots=True)
class Particle:
    point: Point3D
    vel: Point3D
    acc: Point3D

    def step(self) -> None:
        self.vel += self.acc
        self.point += self.vel

    def copy(self) -> Particle:
        return Particle(self.point.copy(), self.vel.copy(), self.acc.copy())


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__particles: list[Particle] = [
            Particle(Point3D(*nbrs[0:3]), Point3D(*nbrs[3:6]), Point3D(*nbrs[6:]))
            for nbrs in (
                list(map(int, re.findall(r"-?\d+", line)))
                for line in rawstr.splitlines()
            )
        ]

    def get_p1(self, steps: int = 1000) -> int:
        triangular = steps * (steps + 1) // 2
        distances = [
            (p.point + p.vel * steps + p.acc * triangular).get_distance(
                Point3D(0, 0, 0)
            )
            for p in self.__particles
        ]
        return distances.index(min(distances))

    def get_p2(self, steps: int = 1000) -> int:
        particles = [p.copy() for p in self.__particles]
        for _ in range(steps):
            for part in particles:
                part.step()
            counts = Counter((p.point.x, p.point.y, p.point.z) for p in particles)
            particles = [
                p for p in particles if counts[(p.point.x, p.point.y, p.point.z)] == 1
            ]
        return len(particles)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
