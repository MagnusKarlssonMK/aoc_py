"""
2017 day 20 - Particle Swarm

Part 1: Note that the question is which particle will be closest *in the long term*, not the closest ever over the
entire trajectory. In the long term (i.e. t->inf), the closest will be the one with the lowest acceleration. However,
with my input, there's multiple particles sharing the same lowest acceleration, and making a secondary sorting on
initial velocity is not safe since it depends on the relative direction between velocity and acceleration.
So in lack of better ideas at the moment, I'll just stick with a bit of trial and error to try to find an estimate
of number of steps to run the simulation before it seems to stabilize.
"""

import re
from copy import deepcopy
from dataclasses import dataclass


@dataclass(frozen=True)
class Point3D:
    x: int
    y: int
    z: int

    def get_distance(self, other: Point3D) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

    def __add__(self, other: Point3D) -> Point3D:
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)


@dataclass(frozen=True)
class Particle:
    point: Point3D
    vel: Point3D
    acc: Point3D

    def step(self) -> Particle:
        vel = self.vel + self.acc
        point = self.point + vel
        return Particle(point, vel, self.acc)


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__particles: list[Particle] = [
            Particle(Point3D(*nbrs[0:3]), Point3D(*nbrs[3:6]), Point3D(*nbrs[6:]))
            for nbrs in [
                list(map(int, re.findall(r"-?\d+", line)))
                for line in rawstr.splitlines()
            ]
        ]

    def get_p1(self) -> int:
        particles = deepcopy(self.__particles)
        for _ in range(1000):
            for p, part in enumerate(particles):
                particles[p] = part.step()
        distances = [p.point.get_distance(Point3D(0, 0, 0)) for p in particles]
        return distances.index(min(distances))

    def get_p2(self) -> int:
        particles = deepcopy(self.__particles)
        for _ in range(1000):
            seen_points: set[Point3D] = set()
            collided_points: set[Point3D] = set()
            for p, part in enumerate(particles):
                particles[p] = part.step()
                if particles[p].point in seen_points:
                    collided_points.add(particles[p].point)
                else:
                    seen_points.add(particles[p].point)

            collided_particles: list[Particle] = []
            for cp in collided_points:
                for p in particles:
                    if p.point == cp:
                        collided_particles.append(p)
            for p in collided_particles:
                particles.remove(p)
        return len(particles)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
