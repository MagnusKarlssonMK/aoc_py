"""
2016 day 17 - Two Steps Forward

Use a state class which also generates neighbor points, this time with a hash function to see which directions
are unlocked, meaning we also need to store the path taken to reach the point.
This is used in a simple BFS loop which runs until all paths either get locked in somewhere or reach the target,
and from the found paths the answer to part 1 is the first entry (the actual path), and the answer to part 2 is the
length of the last entry.
"""

import hashlib
from collections.abc import Generator
from dataclasses import dataclass

GRID_SIZE = 4


@dataclass(frozen=True)
class State:
    x: int
    y: int
    path: str = ""

    def get_neighbors(self, passcode: str) -> Generator[State]:
        h = hashlib.md5((passcode + self.path).encode()).hexdigest()
        for i, (d, (nx, ny)) in enumerate(
            {
                "U": (0, -1),
                "D": (
                    0,
                    1,
                ),
                "L": (-1, 0),
                "R": (1, 0),
            }.items()
        ):
            new_x, new_y = self.x + nx, self.y + ny
            if (
                0 <= new_x < GRID_SIZE
                and 0 <= new_y < GRID_SIZE
                and h[i] in ("b", "c", "d", "e", "f")
            ):
                yield State(new_x, new_y, self.path + d)


class InputData:
    def __init__(self, s: str) -> None:
        self.__passcode = s

    def get_shortestpath(self) -> tuple[str, int]:
        s = State(0, 0)
        found_paths: list[str] = []
        queue = [s]
        while queue:
            s = queue.pop(0)
            if s.x == GRID_SIZE - 1 and s.y == GRID_SIZE - 1:
                found_paths.append(s.path)
                continue
            queue.extend(s.get_neighbors(self.__passcode))
        return found_paths[0], len(found_paths[-1])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_shortestpath()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
