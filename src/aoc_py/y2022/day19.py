"""
2022 day 19 - Not Enough Minerals

Searches the build orders that open the most geodes for each blueprint. Rather than simulating every minute,
the search fast-forwards: for each robot type it works out how long the factory must wait until that robot is
affordable, jumps ahead collecting resources the whole time, then builds it.

The resulting memoised depth-first branch-and-bound is pruned by
- Capping every resource at the most that could still be spent (its largest single-robot cost times the minutes
  left), so states differing only in an unspendable surplus collapse onto the same memo entry.
- Never building more robots of a type than the largest amount of its mineral any robot costs, since robots
  beyond that can never be spent.
- An optimistic upper bound (geodes already open plus the existing geode robots for the remaining minutes plus a
  geode robot built every remaining minute), abandoning a branch as soon as it can no longer beat the best result.
"""

import math
from enum import Enum
from functools import cache
from typing import Final

MISSING_COST: Final = 10**9  # cost given to robot types a blueprint doesn't mention


class Minerals(Enum):
    ORE = "ore"
    CLAY = "clay"
    OBSIDIAN = "obsidian"
    GEODE = "geode"


class Blueprint:
    def __init__(self, rawstr: str) -> None:
        bpid, costs = rawstr.split(": ")
        self.id: int = int(bpid.strip("Blueprint "))
        # Per robot the (ore, clay, obsidian, geode) cost. Missing robot types get an impossible cost.
        self.cost: dict[Minerals, tuple[int, int, int, int]] = {
            mineral: (MISSING_COST, MISSING_COST, MISSING_COST, MISSING_COST)
            for mineral in Minerals
        }
        self.maxcosts: dict[Minerals, int] = {mineral: 0 for mineral in Minerals}
        for cost in costs.strip(".").split(". "):
            dest, source = cost.split(" robot costs ")
            robot = Minerals(dest.split()[1])
            amounts = {mineral: 0 for mineral in Minerals}
            for s in source.split(" and "):
                nbr, mineral = s.split()
                mineral = Minerals(mineral)
                amounts[mineral] = int(nbr)
                self.maxcosts[mineral] = max(self.maxcosts[mineral], int(nbr))
            self.cost[robot] = (
                amounts[Minerals.ORE],
                amounts[Minerals.CLAY],
                amounts[Minerals.OBSIDIAN],
                amounts[Minerals.GEODE],
            )


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__blueprints = [Blueprint(line) for line in rawstr.splitlines()]

    def get_p1(self, timeleft: int) -> int:
        return sum(
            self.__get_bp_quantity(i, timeleft) * bp.id
            for i, bp in enumerate(self.__blueprints)
        )

    def get_p2(self, timeleft: int) -> int:
        return math.prod(
            self.__get_bp_quantity(i, timeleft)
            for i in range(min(3, len(self.__blueprints)))
        )

    def __get_bp_quantity(self, bpidx: int, time: int) -> int:
        bp = self.__blueprints[bpidx]
        costs = [bp.cost[mineral] for mineral in Minerals]
        # The most of each mineral a single robot costs; geodes are never spent, so never capped.
        max_spend = [bp.maxcosts[mineral] for mineral in Minerals]
        best = 0

        @cache
        def search(
            time_remaining: int,
            ore: int,
            clay: int,
            obsidian: int,
            geode: int,
            ore_robots: int,
            clay_robots: int,
            obsidian_robots: int,
            geode_robots: int,
        ) -> None:
            nonlocal best
            best = max(best, geode + geode_robots * time_remaining)
            if time_remaining <= 0:
                return
            if (
                geode
                + geode_robots * time_remaining
                + time_remaining * (time_remaining - 1) // 2
                <= best
            ):
                return
            resources = (ore, clay, obsidian, geode)
            robots = (ore_robots, clay_robots, obsidian_robots, geode_robots)
            # Build the most valuable robot first, so a good result is found early and prunes harder.
            # Robot/mineral index order is ore, clay, obsidian, geode.
            for idx in (3, 2, 1, 0):
                if idx != 3 and robots[idx] >= max_spend[idx]:
                    continue
                # Minutes until this robot is affordable, including the minute spent building it.
                build_minutes = 1
                feasible = True
                for m in range(4):
                    if costs[idx][m] == 0:
                        continue
                    if robots[m] == 0:
                        if resources[m] < costs[idx][m]:
                            feasible = False
                            break
                    elif resources[m] < costs[idx][m]:
                        wait = -(-(costs[idx][m] - resources[m]) // robots[m])
                        build_minutes = max(build_minutes, wait + 1)
                if not feasible or build_minutes > time_remaining:
                    continue
                remaining = time_remaining - build_minutes
                new_resources = [
                    resources[m] + build_minutes * robots[m] - costs[idx][m]
                    for m in range(4)
                ]
                for m in range(3):  # geodes are never spent, so they are never capped
                    new_resources[m] = min(new_resources[m], max_spend[m] * remaining)
                new_robots = list(robots)
                new_robots[idx] += 1
                search(
                    remaining,
                    new_resources[0],
                    new_resources[1],
                    new_resources[2],
                    new_resources[3],
                    new_robots[0],
                    new_robots[1],
                    new_robots[2],
                    new_robots[3],
                )

        search(time, 0, 0, 0, 0, 1, 0, 0, 0)
        return best


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1(24))
    if part in (None, 2):
        p2 = str(p.get_p2(32))

    return p1, p2
