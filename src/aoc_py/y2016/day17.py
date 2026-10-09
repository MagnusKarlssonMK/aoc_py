"""
2016 day 17 - Two Steps Forward

A state carries its position plus the path taken (needed to hash the passcode). get_neighbors hashes passcode + path,
unlocks the doors named by the first four hex digits, and a deque BFS explores every path until it either dead-ends or
reaches the vault. Part 1 is the first path found (BFS, so it is the shortest) and Part 2 the length of the last.
"""

import hashlib
from collections import deque
from collections.abc import Generator
from dataclasses import dataclass

GRID_SIZE = 4

DIRECTIONS = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}


@dataclass(frozen=True)
class State:
    x: int
    y: int
    path: str = ""

    def get_neighbors(self, passcode: str) -> Generator[State]:
        h = hashlib.md5((passcode + self.path).encode()).hexdigest()
        for i, (d, (nx, ny)) in enumerate(DIRECTIONS.items()):
            new_x, new_y = self.x + nx, self.y + ny
            if 0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE and h[i] in "bcdef":
                yield State(new_x, new_y, self.path + d)


class InputData:
    def __init__(self, s: str) -> None:
        self.__passcode = s

    def get_paths(self) -> tuple[str, int]:
        """BFS every path to the vault; returns the shortest path and the longest path length."""
        queue = deque([State(0, 0)])
        found_paths: list[str] = []
        while queue:
            s = queue.popleft()
            if s.x == GRID_SIZE - 1 and s.y == GRID_SIZE - 1:
                found_paths.append(s.path)
                continue
            queue.extend(s.get_neighbors(self.__passcode))
        return found_paths[0], len(found_paths[-1])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_paths()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
