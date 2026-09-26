"""
2019 day 18 - Many-Worlds Interpretation

- Step 1: Parse the grid into a set of walkable cells, the key positions, the door positions and the robot start
  position(s).
- Step 2: Build a graph whose nodes are the keys and the robot starts. An edge between two nodes is a BFS path
  through the open grid and carries two values: the number of steps and a bitmask of the doors that must be
  unlocked to use it. Keys block the BFS, so an edge never passes through an uncollected key; when several
  (steps, door-mask) pairs lead to the same key, the pair is kept unless another is no longer and no more
  demanding (dominance pruning).
- Step 3: One Dijkstra search over states (robot positions, collected-keys bitmask) finds the minimum number of
  steps to collect every key. Part 1 runs this with a single robot; Part 2 runs it with one robot per start.
- Step 4: For part 2 the grid is modified when the map has a single "@": the four orthogonal neighbours of the
  start are walled off and four robots are placed on the diagonal corners (inputs that already contain four "@"
  are used unchanged). Doors may be unlocked by a key collected by any robot, so all robots share one bitmask.
"""

from collections import deque
from heapq import heappop, heappush

from aoc_py.util.point import Point


class InputData:
    def __init__(self, s: str) -> None:
        self.__walkable: set[Point] = set()
        self.__keys: dict[str, Point] = {}
        self.__doors: dict[str, Point] = {}
        self.__starts: list[Point] = []
        for y, line in enumerate(s.splitlines()):
            for x, c in enumerate(line):
                point = Point(x, y)
                if c == "#":
                    continue
                self.__walkable.add(point)
                if c == "@":
                    self.__starts.append(point)
                elif c.islower():
                    self.__keys[c] = point
                elif c.isupper():
                    self.__doors[c] = point

    def get_p1(self) -> int:
        adjacency, all_keys = self.__build_graph(self.__walkable, self.__starts)
        return self.__search(adjacency, all_keys, 1)

    def get_p2(self) -> int:
        walkable = self.__walkable
        starts = self.__starts
        if len(starts) == 1:
            walkable, starts = self.__four_robot_layout()
        adjacency, all_keys = self.__build_graph(walkable, starts)
        return self.__search(adjacency, all_keys, len(starts))

    def __four_robot_layout(self) -> tuple[set[Point], list[Point]]:
        start = self.__starts[0]
        walkable = set(self.__walkable)
        for point in (
            start,
            Point(start.x, start.y - 1),
            Point(start.x, start.y + 1),
            Point(start.x - 1, start.y),
            Point(start.x + 1, start.y),
        ):
            walkable.discard(point)
        corners = [
            Point(start.x - 1, start.y - 1),
            Point(start.x + 1, start.y - 1),
            Point(start.x - 1, start.y + 1),
            Point(start.x + 1, start.y + 1),
        ]
        walkable.update(corners)
        return walkable, corners

    def __build_graph(
        self, walkable: set[Point], starts: list[Point]
    ) -> tuple[dict[int, tuple[tuple[int, int, int], ...]], int]:
        key_idx = {k: i for i, k in enumerate(sorted(self.__keys))}
        cell_char = {p: c for c, p in self.__keys.items()}
        cell_char.update({p: c for c, p in self.__doors.items()})
        sources: list[tuple[int, Point]] = [
            (key_idx[k], p) for k, p in self.__keys.items()
        ]
        for i, p in enumerate(starts):
            sources.append((len(key_idx) + i, p))
        adjacency: dict[int, tuple[tuple[int, int, int], ...]] = {}
        for src_idx, src_point in sources:
            adjacency[src_idx] = self.__key_paths(
                src_idx, src_point, walkable, cell_char, key_idx
            )
        return adjacency, (1 << len(key_idx)) - 1

    def __key_paths(
        self,
        src_idx: int,
        src_point: Point,
        walkable: set[Point],
        cell_char: dict[Point, str],
        key_idx: dict[str, int],
    ) -> tuple[tuple[int, int, int], ...]:
        best: dict[int, set[tuple[int, int]]] = {}
        seen: set[tuple[Point, int]] = {(src_point, 0)}
        queue: deque[tuple[Point, int, int]] = deque([(src_point, 0, 0)])
        while queue:
            point, doors, steps = queue.popleft()
            for delta in (Point(0, -1), Point(1, 0), Point(0, 1), Point(-1, 0)):
                nxt = point + delta
                if nxt not in walkable or (nxt, doors) in seen:
                    continue
                value = cell_char.get(nxt)
                if value is not None and value.islower():
                    target = key_idx[value]
                    if target != src_idx:
                        best.setdefault(target, set()).add((steps + 1, doors))
                    continue
                new_doors = doors
                if value is not None:
                    new_doors = doors | (1 << key_idx[value.lower()])
                seen.add((nxt, new_doors))
                queue.append((nxt, new_doors, steps + 1))
        paths: list[tuple[int, int, int]] = []
        for target, candidates in best.items():
            kept: list[tuple[int, int]] = []
            for steps, doors in sorted(candidates):
                if any(k[0] <= steps and not (k[1] & ~doors) for k in kept):
                    continue
                kept = [k for k in kept if not (steps <= k[0] and not (doors & ~k[1]))]
                kept.append((steps, doors))
            paths += [(target, steps, doors) for steps, doors in kept]
        return tuple(paths)

    def __search(
        self,
        adjacency: dict[int, tuple[tuple[int, int, int], ...]],
        all_keys: int,
        n_starts: int,
    ) -> int:
        positions = tuple(len(self.__keys) + i for i in range(n_starts))
        pqueue: list[tuple[int, tuple[int, ...], int]] = [(0, positions, 0)]
        visited: dict[tuple[tuple[int, ...], int], int] = {}
        while pqueue:
            steps, robots, have_keys = heappop(pqueue)
            if have_keys == all_keys:
                return steps
            state = (robots, have_keys)
            if visited.get(state, 10**18) <= steps:
                continue
            visited[state] = steps
            for i, robot in enumerate(robots):
                for nxt, cost, doors in adjacency.get(robot, ()):
                    if doors & ~have_keys:
                        continue
                    new_robots = list(robots)
                    new_robots[i] = nxt
                    heappush(
                        pqueue,
                        (steps + cost, tuple(new_robots), have_keys | (1 << nxt)),
                    )
        return -1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
