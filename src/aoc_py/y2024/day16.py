"""
2024 day 16 - Reindeer Maze

A Dijkstra search over (cell, direction) states: moving forward costs 1 and turning
costs 1000. Part 1 is the cheapest cost to reach the exit. Part 2 walks the same search
backwards from every optimal exit state, following only exact-cost predecessors, and
counts the distinct cells that lie on at least one optimal route.
"""

from collections import deque
from heapq import heappop, heappush

from aoc_py.util.grid import Grid

# Direction order: 0 = right, 1 = down, 2 = left, 3 = up.
DIR_X = (1, 0, -1, 0)
DIR_Y = (0, 1, 0, -1)
INF = 1 << 60


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__maze = Grid(rawstr)

    def solve(self) -> tuple[int, int]:
        elements = self.__maze.elements
        x_max = self.__maze.x_max
        y_max = self.__maze.y_max
        start = self.__maze.get_index(self.__maze.find("S"))
        exit_idx = self.__maze.get_index(
            self.__maze.find("E")
        )  # -1 when there is no exit
        passable = [c != "#" for c in elements]

        dist = [INF] * (4 * len(elements))
        dist[start * 4] = 0  # Facing right (direction index 0).
        heap: list[tuple[int, int, int]] = [(0, start, 0)]
        fastest = INF
        while heap:
            cost, idx, dir_idx = heappop(heap)
            if cost > dist[idx * 4 + dir_idx]:
                continue
            if idx == exit_idx:
                fastest = min(fastest, cost)
                continue
            x = idx % x_max
            y = idx // x_max

            # Move forward one cell (cost 1).
            new_x = x + DIR_X[dir_idx]
            new_y = y + DIR_Y[dir_idx]
            if (
                0 <= new_x < x_max
                and 0 <= new_y < y_max
                and passable[new_y * x_max + new_x]
            ):
                new_idx = new_y * x_max + new_x
                new_cost = cost + 1
                key = new_idx * 4 + dir_idx
                if new_cost < dist[key]:
                    dist[key] = new_cost
                    heappush(heap, (new_cost, new_idx, dir_idx))

            # Rotate in place (cost 1000 each way).
            for new_dir in ((dir_idx + 1) % 4, (dir_idx - 1) % 4):
                new_cost = cost + 1000
                key = idx * 4 + new_dir
                if new_cost < dist[key]:
                    dist[key] = new_cost
                    heappush(heap, (new_cost, idx, new_dir))

        if fastest == INF:
            # No solution found at all
            return -1, -1

        queue: deque[tuple[int, int, int]] = deque()
        for dir_idx in range(4):
            if dist[exit_idx * 4 + dir_idx] == fastest:
                queue.append((exit_idx, dir_idx, fastest))
                dist[exit_idx * 4 + dir_idx] = INF

        best_seats: set[int] = set()
        while queue:
            idx, dir_idx, value = queue.popleft()
            best_seats.add(idx)
            if idx == start:
                continue
            x = idx % x_max
            y = idx // x_max

            # Reverse of moving forward: the predecessor sat behind us.
            new_x = x - DIR_X[dir_idx]
            new_y = y - DIR_Y[dir_idx]
            if (
                0 <= new_x < x_max
                and 0 <= new_y < y_max
                and passable[new_y * x_max + new_x]
            ):
                new_idx = new_y * x_max + new_x
                new_value = value - 1
                key = new_idx * 4 + dir_idx
                if dist[key] == new_value:
                    dist[key] = INF
                    queue.append((new_idx, dir_idx, new_value))

            # Reverse of rotating in place.
            for new_dir in ((dir_idx + 1) % 4, (dir_idx - 1) % 4):
                new_value = value - 1000
                key = idx * 4 + new_dir
                if dist[key] == new_value:
                    dist[key] = INF
                    queue.append((idx, new_dir, new_value))

        return fastest, len(best_seats)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    r1, r2 = InputData(inputdata).solve()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
