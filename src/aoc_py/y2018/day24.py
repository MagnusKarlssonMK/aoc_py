"""
2018 day 24 - Immune System Simulator 20XX
"""

import re
from copy import deepcopy
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


@dataclass
class Group:
    uid: int
    team: Team
    units: int
    hp: int
    attackpower: int
    attacktype: DmgType
    initiative: int
    traits: list[Trait]

    @property
    def effective_power(self) -> int:
        return self.units * self.attackpower

    def get_dmgtaken(self, power: int, atype: DmgType) -> int:
        for t in self.traits:
            if t.damagetype == atype:
                if t.t == TraitType.IMMUNE:
                    return 0
                elif t.t == TraitType.WEAK:
                    return 2 * power
        return power

    def receive_dmg(self, power: int, atype: DmgType) -> int:
        lostunits = min(self.get_dmgtaken(power, atype) // self.hp, self.units)
        self.units -= lostunits
        return lostunits


class InputData:
    def __init__(self, rawstr: str) -> None:
        team = None
        uid = 1
        self.__groups: dict[int, Group] = {}
        for line in rawstr.splitlines():
            if len(line) > 0:
                if not line[0].isdigit():
                    team = Team(line.strip(":"))
                else:
                    units, hp, ap, init = list(map(int, re.findall(r"\d+", line)))
                    at = DmgType(re.findall(r"\d (\w+) damage at initiative", line)[0])
                    traits: list[Trait] = []
                    traitstr = re.findall(r"\(([^)]+)", line)
                    if traitstr:
                        for part in traitstr[0].split("; "):
                            words = part.split()
                            for t in words[2:]:
                                traits.append(
                                    Trait(TraitType(words[0]), DmgType(t.strip(", ")))
                                )
                    if team:
                        self.__groups[uid] = Group(
                            uid, team, units, hp, ap, at, init, traits
                        )
                    uid += 1

    def __get_winner_and_units(self, boost: int) -> tuple[Team, int]:
        groups = deepcopy(self.__groups)
        for g in groups:
            if groups[g].team == Team.IMMUNESYSTEM:
                groups[g].attackpower += boost

        while len({g.team for g in list(groups.values()) if g.units > 0}) > 1:
            # Target selection
            targets: dict[int, int] = {}
            attackerlist = sorted(
                [g for g in groups.values() if g.units > 0],
                key=lambda x: (x.effective_power, x.initiative),
                reverse=True,
            )
            for attacker in attackerlist:
                targetlist = sorted(
                    [
                        t
                        for t in attackerlist
                        if t.team != attacker.team and t.uid not in targets.values()
                    ],
                    key=lambda x: (
                        x.get_dmgtaken(attacker.effective_power, attacker.attacktype),
                        x.effective_power,
                        x.initiative,
                    ),
                    reverse=True,
                )
                for target in targetlist:
                    # So this is NOT obvious, but we should apparently skip over immune targets, and somehow that
                    # impacts the result.
                    if (
                        groups[target.uid].get_dmgtaken(
                            attacker.effective_power, attacker.attacktype
                        )
                        > 0
                    ):
                        targets[attacker.uid] = target.uid
                        break
            if not targets:
                return Team.INFECTION, -1

            # Combat
            totaldmg = 0
            for attacker in sorted(
                groups.values(), key=lambda x: x.initiative, reverse=True
            ):
                if groups[attacker.uid].units > 0 and attacker.uid in targets:
                    totaldmg += groups[targets[attacker.uid]].receive_dmg(
                        attacker.effective_power, attacker.attacktype
                    )
            if totaldmg == 0:
                # In case of deadlock of nothing mut immune dmg
                return Team.INFECTION, -1
        winner = Team.INFECTION  # Initialize to any, will be set in loop
        for g in groups:
            if groups[g].units > 0:
                winner = groups[g].team
                break
        return winner, sum([g.units for g in groups.values() if g.units > 0])

    def get_winning_units(self) -> tuple[int, int]:
        boost = 0
        p2 = -1
        winner, p1 = self.__get_winner_and_units(boost)
        while winner == Team.INFECTION:
            boost += 1
            winner, p2 = self.__get_winner_and_units(boost)
        return p1, p2


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_winning_units()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
