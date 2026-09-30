"""
2021 day 22 - Reactor Reboot

Stores each cuboid as its two opposite corners, as six plain coordinates.
(There's probably some more clever and less verbose ways to calculate the intersections for example.)
Basically run through the cuboids and find intersections and create 'negative' cuboids for the
intersecting areas, and then calculate the total volume from that.

The overlap test sits inline in the reboot loop instead of behind a method, since it is the
innermost loop of the whole solution: on a large input it runs some 15 million times, and the
method call per pair costs more than the arithmetic does. Only the overlaps, some 40000 of them,
become Cuboid instances.
Part 1 restricts the reboot to the cuboids that lie fully inside the region, but those same steps
also have to be applied to the unrestricted list for part 2, so both are done in a single pass.
"""

from typing import Final

P1_REGION_LIMIT: Final = 50


class Cuboid:
    def __init__(
        self, onoff: int, x1: int, x2: int, y1: int, y2: int, z1: int, z2: int
    ) -> None:
        self.is_on: int = onoff
        self.x1: int = x1
        self.x2: int = x2
        self.y1: int = y1
        self.y2: int = y2
        self.z1: int = z1
        self.z2: int = z2

    @classmethod
    def from_str(cls, s: str) -> Cuboid:
        left, right = s.split()
        is_on: int = 1 if left == "on" else -1
        xs, ys, zs = right.split(",")
        _, xs = xs.split("=")
        _, ys = ys.split("=")
        _, zs = zs.split("=")
        x = list(map(int, xs.split("..")))
        y = list(map(int, ys.split("..")))
        z = list(map(int, zs.split("..")))
        return cls(is_on, x[0], x[1], y[0], y[1], z[0], z[1])

    def is_inrange(self, limit: int) -> bool:
        return all(
            -limit <= corner <= limit
            for corner in (self.x1, self.x2, self.y1, self.y2, self.z1, self.z2)
        )

    def get_volume(self) -> int:
        return (
            self.is_on
            * (self.x2 - self.x1 + 1)
            * (self.y2 - self.y1 + 1)
            * (self.z2 - self.z1 + 1)
        )


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__reboot_steps: list[Cuboid] = [
            Cuboid.from_str(line) for line in rawstr.splitlines()
        ]

    @staticmethod
    def __reboot(processed_cuboids: list[Cuboid], cuboid: Cuboid) -> None:
        """Applies one reboot step to processed_cuboids. A negated cuboid is added for the
        overlap with each already processed cuboid, since the later step cancels out whatever
        the earlier one lit there, and the incoming cuboid itself is only kept when it is on.
        The negated cuboids go into a separate list so that they are not themselves tested
        for overlap against the step that is being applied."""
        x1, x2 = cuboid.x1, cuboid.x2
        y1, y2 = cuboid.y1, cuboid.y2
        z1, z2 = cuboid.z1, cuboid.z2
        new_intersections: list[Cuboid] = []
        for old in processed_cuboids:
            if (
                old.x1 > x2
                or old.x2 < x1
                or old.y1 > y2
                or old.y2 < y1
                or old.z1 > z2
                or old.z2 < z1
            ):
                continue
            new_intersections.append(
                Cuboid(
                    -old.is_on,
                    max(old.x1, x1),
                    min(old.x2, x2),
                    max(old.y1, y1),
                    min(old.y2, y2),
                    max(old.z1, z1),
                    min(old.z2, z2),
                )
            )
        processed_cuboids.extend(new_intersections)
        if cuboid.is_on == 1:
            processed_cuboids.append(cuboid)

    def get_answers(self) -> tuple[int, int]:
        """Reports the total volume of the lit region for Part 1 and Part 2. Part 1's
        region-limited reboot runs alongside Part 2's unrestricted one, so the input is only
        walked once."""
        limited_cuboids: list[Cuboid] = []
        all_cuboids: list[Cuboid] = []
        for cuboid in self.__reboot_steps:
            if cuboid.is_inrange(P1_REGION_LIMIT):
                self.__reboot(limited_cuboids, cuboid)
            self.__reboot(all_cuboids, cuboid)
        return (
            sum(c.get_volume() for c in limited_cuboids),
            sum(c.get_volume() for c in all_cuboids),
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    r1, r2 = InputData(inputdata).get_answers()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
