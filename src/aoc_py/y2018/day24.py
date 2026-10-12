"""
2018 day 24 - Immune System Simulator 20XX

Part 1

Simulate the battle between the two armies until only one of them has units left, and
report how many units the winner has.

Part 2

The immune system needs a boost to win. Try increasing the boost one at a time until
the immune system wins, and report the units it has left for the smallest such boost.
"""

import re
from copy import copy
from dataclasses import dataclass
from enum import Enum


class Team(Enum):
    IMMUNESYSTEM = "Immune System"
    INFECTION = "Infection"


class DmgType(Enum):
    COLD = "cold"
    FIRE = "fire"
    SLASHING = "slashing"
    RADIATION = "radiation"
    BLUDGEONING = "bludgeoning"


class TraitType(Enum):
    WEAK = "weak"
    IMMUNE = "immune"


@dataclass(frozen=True)
class Trait:
    t: TraitType
    damagetype: DmgType


@dataclass(eq=False)
class Group:
    team: Team
    units: int
    hp: int
    attackpower: int
    attacktype: DmgType
    initiative: int
    traits: list[Trait]

    def get_dmgtaken(self, power: int, atype: DmgType) -> int:
        for t in self.traits:
            if t.damagetype == atype:
                if t.t == TraitType.IMMUNE:
                    return 0
                return 2 * power
        return power

    def receive_dmg(self, power: int, atype: DmgType) -> int:
        lostunits = min(self.get_dmgtaken(power, atype) // self.hp, self.units)
        self.units -= lostunits
        return lostunits


class InputData:
    def __init__(self, rawstr: str) -> None:
        team = None
        self.__groups: list[Group] = []
        for line in rawstr.splitlines():
            if len(line) > 0:
                if not line[0].isdigit():
                    team = Team(line.strip(":"))
                else:
                    units, hp, ap, init = list(map(int, re.findall(r"\d+", line)))
                    at = DmgType(re.findall(r"\d (\w+) damage at initiative", line)[0])
                    traits: list[Trait] = []
                    traitstr: list[str] = re.findall(r"\(([^)]+)", line)
                    if traitstr:
                        for part in traitstr[0].split("; "):
                            words = part.split()
                            for t in words[2:]:
                                traits.append(
                                    Trait(TraitType(words[0]), DmgType(t.strip(", ")))
                                )
                    if team is not None:
                        self.__groups.append(
                            Group(team, units, hp, ap, at, init, traits)
                        )

    def __get_winner_and_units(self, boost: int) -> tuple[Team, int]:
        groups = [copy(g) for g in self.__groups]
        for g in groups:
            if g.team is Team.IMMUNESYSTEM:
                g.attackpower += boost

        while True:
            alive = [g for g in groups if g.units > 0]
            if len({g.team for g in alive}) < 2:
                break

            # Target selection, highest effective power (then initiative) first. A group
            # that can't hurt anything is left without a target, and already picked
            # targets are skipped.
            power = {g: g.units * g.attackpower for g in alive}
            targets: dict[Group, Group] = {}
            chosen: set[Group] = set()
            for attacker in sorted(
                alive, key=lambda g: (power[g], g.initiative), reverse=True
            ):
                best: Group | None = None
                bestkey: tuple[int, int, int] | None = None
                for t in alive:
                    if t.team is attacker.team or t in chosen:
                        continue
                    dmg = t.get_dmgtaken(power[attacker], attacker.attacktype)
                    if dmg == 0:
                        continue
                    key = (dmg, power[t], t.initiative)
                    if bestkey is None or key > bestkey:
                        bestkey, best = key, t
                if best is not None:
                    targets[attacker] = best
                    chosen.add(best)

            # Combat, in initiative order, using the power each attacker has left after
            # any losses earlier in the round.
            totaldmg = 0
            for attacker in sorted(alive, key=lambda g: g.initiative, reverse=True):
                if attacker.units > 0 and attacker in targets:
                    totaldmg += targets[attacker].receive_dmg(
                        attacker.units * attacker.attackpower, attacker.attacktype
                    )
            if totaldmg == 0:
                # Deadlock, nothing can hurt anything: the immune system did not win.
                return Team.INFECTION, -1
        return alive[0].team, sum(g.units for g in alive)

    def get_winning_units(self) -> tuple[int, int]:
        boost = 0
        winner, units = self.__get_winner_and_units(boost)
        p1 = units
        while winner is Team.INFECTION:
            boost += 1
            winner, units = self.__get_winner_and_units(boost)
        return p1, units


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_winning_units()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
