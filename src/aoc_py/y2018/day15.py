"""
2018 day 15 - Beverage Bandits

Combat simulation where units move and attack in reading order each round.
Movement uses a two-phase BFS: a first pass from the unit to find the nearest
square in range of an enemy (ties broken by reading order), then a second
pass from that square to pick the first step of the path (again ties broken
by reading order).

Part 2 boosts the elf power until the elves win without losing a single elf.
Since a higher power can only help the elves, the search is a binary search;
combats for powers that lose an elf are aborted at the first elf death.
"""

from collections import deque
from copy import deepcopy
from dataclasses import dataclass

from aoc_py.util.point import Directions, Point


def get_adjacent(p: Point) -> list[Point]:
    return [p + d for d in Directions.NEIGHBORS_STRAIGHT]


@dataclass
class Unit:
    position: Point
    team: str
    power: int = 3
    hp: int = 200

    def __lt__(self, other: Unit) -> bool:
        return self.position < other.position


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__cavern: set[Point] = set()
        self.__units: list[Unit] = []
        for y, line in enumerate(rawstr.splitlines()):
            for x, char in enumerate(line):
                if char != "#":
                    self.__cavern.add(Point(x, y))
                    if char in ("E", "G"):
                        self.__units.append(Unit(Point(x, y), char))
        self.__start_units = deepcopy(self.__units)

    def __reset_units(self, elfpower: int = 3):
        self.__units = deepcopy(self.__start_units)
        for u in self.__units:
            if u.team == "E":
                u.power = elfpower

    def __move(self, unit: Unit) -> bool:
        """Returns False if there are no targets left, otherwise true."""
        targets = [t for t in self.__units if t.team != unit.team and t.hp > 0]
        if not targets:
            return False
        occupied = {
            u.position for u in self.__units if u.position != unit.position and u.hp > 0
        }
        open_cells = self.__cavern - occupied
        target_points: set[Point] = set()
        for target in targets:
            for adj in get_adjacent(target.position):
                if adj in open_cells:
                    target_points.add(adj)
        if not target_points or unit.position in target_points:
            return True
        # First pass: nearest square in range of an enemy, ties broken by reading order
        dist = {unit.position: 0}
        queue = deque([unit.position])
        best: tuple[int, Point] | None = None
        while queue:
            cur = queue.popleft()
            d = dist[cur]
            if best is not None and d > best[0]:
                break
            if cur in target_points and (best is None or (d, cur) < (best[0], best[1])):
                best = (d, cur)
            for nextpoint in get_adjacent(cur):
                if nextpoint in open_cells and nextpoint not in dist:
                    dist[nextpoint] = d + 1
                    queue.append(nextpoint)
        if best is None:
            return True  # targets exist but none reachable, so the unit stays put
        # Second pass: from the chosen square, find the first step towards it
        targetdist = {best[1]: 0}
        queue = deque([best[1]])
        while queue:
            cur = queue.popleft()
            for nextpoint in get_adjacent(cur):
                if nextpoint in open_cells and nextpoint not in targetdist:
                    targetdist[nextpoint] = targetdist[cur] + 1
                    queue.append(nextpoint)
        candidates = [
            adj
            for adj in get_adjacent(unit.position)
            if targetdist.get(adj) == best[0] - 1
        ]
        unit.position = min(candidates)
        return True

    def __attack(self, unit: Unit) -> bool:
        """Returns True if this attack killed an elf."""
        targets = [t for t in self.__units if t.team != unit.team and t.hp > 0]
        if not targets:
            return False
        target_points: set[Point] = set()
        for target in targets:
            for adj in get_adjacent(target.position):
                target_points.add(adj)
        if unit.position in target_points:
            # Find the target unit(s), sort if more than one, and then hit it
            surrounding_points = get_adjacent(unit.position)
            enemies = sorted(
                [(e.hp, e) for e in targets if e.position in surrounding_points]
            )
            # Note: stored as tuple with hp so that it gets sorted according to HP first and reading order second
            if enemies:
                victim = enemies[0][1]
                victim.hp -= unit.power
                return unit.team == "G" and victim.hp <= 0
        return False

    def __playround(self, elf_death_abort: bool = False) -> int:
        """
        Returns 0 if the full round was played, 1 if the combat ended mid-round, or
        -1 if an elf died while elf_death_abort is set.
        """
        game_ended = False
        for unit in sorted(self.__units):
            if unit.hp <= 0:
                continue
            if not self.__move(unit):
                game_ended = True
                break
            killed_elf = self.__attack(unit)
            if elf_death_abort and killed_elf:
                self.__units = [u for u in self.__units if u.hp > 0]
                return -1
        # Remove dead units
        self.__units = [unit for unit in self.__units if unit.hp > 0]
        return 1 if game_ended else 0

    def __game_over(self) -> bool:
        return len({unit.team for unit in self.__units}) < 2

    def get_combat_outcome(self, elf_death_abort: bool = False) -> tuple[int, str]:
        rounds = 0
        while not self.__game_over():
            result = self.__playround(elf_death_abort)
            if result == 0:
                rounds += 1
            elif result == -1:
                return -1, "D"
        return rounds * sum([u.hp for u in self.__units]), self.__units[0].team

    def get_boosted_elfs_outcome(self) -> int:
        elfcount = sum([1 for u in self.__start_units if u.team == "E"])

        def probe(power: int) -> tuple[bool, int]:
            self.__reset_units(power)
            outcome, winner = self.get_combat_outcome(elf_death_abort=True)
            ok = winner == "E" and (
                sum([1 for u in self.__units if u.team == "E"]) == elfcount
            )
            return ok, outcome

        # A higher elf power can only help the elves, so the smallest power for which
        # they win without losing an elf can be found with a binary search.
        lo, hi = 4, 100
        while lo < hi:
            mid = (lo + hi) // 2
            if probe(mid)[0]:
                hi = mid
            else:
                lo = mid + 1
        _, outcome = probe(lo)
        return outcome


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_combat_outcome()[0])
    if part in (None, 2):
        p2 = str(p.get_boosted_elfs_outcome())

    return p1, p2
