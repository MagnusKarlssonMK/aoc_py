"""
2015 day 22 - Wizard Simulator 20XX

A round of the fight is always the same fixed order. In hard mode the wizard loses a hit point at
the start of their own turn, then every running effect ticks (poison hurts the boss, recharge
restores mana, and all three timers drop by one), then the acting side moves. Anything that kills
the boss ends the fight on the spot, with no further tick, so a spell that lands the killing blow
needs no follow-up round at all.

Shield, poison and recharge cannot be cast again while already running, which is what stops the
search from looping forever on the same effect and keeps the choice at each turn a subset of the
five spells.

The cheapest win does not need a playthrough to be simulated. How much mana is still needed depends
only on the current position, so the recursion is memoised on the whole position: both hit points,
the mana, the three effect timers and whose turn it is. That turns a tree of spell orderings into a
walk over distinct positions, and it is what makes hard mode affordable -- the same position is
reachable by many different orderings of the same spells.
"""

from dataclasses import dataclass
from enum import Enum, auto
from functools import cache
from typing import Final


class Spells(Enum):
    MAGIC_MISSILE = auto()
    DRAIN = auto()
    SHIELD = auto()
    POISON = auto()
    RECHARGE = auto()


@dataclass(frozen=True)
class Spell:
    mana: int
    damage: int = 0
    heal: int = 0
    effect: Spells | None = None
    effect_value: int = 0
    effect_turns: int = 0


SPELLS: Final[dict[Spells, Spell]] = {
    Spells.MAGIC_MISSILE: Spell(53, damage=4),
    Spells.DRAIN: Spell(73, damage=2, heal=2),
    Spells.SHIELD: Spell(113, effect=Spells.SHIELD, effect_value=7, effect_turns=6),
    Spells.POISON: Spell(173, effect=Spells.POISON, effect_value=3, effect_turns=6),
    Spells.RECHARGE: Spell(
        229, effect=Spells.RECHARGE, effect_value=101, effect_turns=5
    ),
}


class InputData:
    """Holds the starting game data and finds the cheapest way to beat the boss."""

    def __init__(self, rawstr: str, wizardhp: int = 50, wizardmana: int = 500) -> None:
        lines = rawstr.splitlines()
        self.__boss_hp = int(lines[0].split()[-1])
        self.__boss_dmg = int(lines[1].split()[-1])
        self.__wizard_hp = wizardhp
        self.__wizard_mana = wizardmana

    def get_cheapest_win(self, hardmode: bool = False) -> int:
        """The least mana that beats the boss from the starting position, or -1 if unwinnable."""

        @cache
        def cheapest(
            boss_hp: int,
            wizard_hp: int,
            wizard_mana: int,
            poison: int,
            shield: int,
            recharge: int,
            player_turn: bool,
        ) -> int:
            """Cheapest mana still to spend from here, called at the top of a turn with the
            hard mode hit and the effect tick still pending."""
            if player_turn and hardmode:
                wizard_hp -= 1
                if wizard_hp <= 0:
                    return -1

            if poison > 0:
                boss_hp -= SPELLS[Spells.POISON].effect_value
            if recharge > 0:
                wizard_mana += SPELLS[Spells.RECHARGE].effect_value
            if boss_hp <= 0:
                return 0

            if poison > 0:
                poison -= 1
            if shield > 0:
                shield -= 1
            if recharge > 0:
                recharge -= 1

            if not player_turn:
                armor = SPELLS[Spells.SHIELD].effect_value if shield > 0 else 0
                wizard_hp -= max(1, self.__boss_dmg - armor)
                if wizard_hp <= 0:
                    return -1
                return cheapest(
                    boss_hp, wizard_hp, wizard_mana, poison, shield, recharge, True
                )

            running = {
                Spells.SHIELD: shield,
                Spells.POISON: poison,
                Spells.RECHARGE: recharge,
            }
            best = -1
            for data in SPELLS.values():
                if data.mana > wizard_mana:
                    continue
                # An effect spell cannot be cast again until the running one has expired.
                if data.effect is not None and running[data.effect] > 0:
                    continue
                if data.damage >= boss_hp:
                    # The hit kills outright, so the fight ends before anything else happens.
                    if best < 0 or data.mana < best:
                        best = data.mana
                    continue
                next_poison, next_shield, next_recharge = poison, shield, recharge
                if data.effect is Spells.POISON:
                    next_poison = data.effect_turns
                elif data.effect is Spells.SHIELD:
                    next_shield = data.effect_turns
                elif data.effect is Spells.RECHARGE:
                    next_recharge = data.effect_turns
                rest = cheapest(
                    boss_hp - data.damage,
                    wizard_hp + data.heal,
                    wizard_mana - data.mana,
                    next_poison,
                    next_shield,
                    next_recharge,
                    False,
                )
                if rest < 0:
                    continue
                if best < 0 or data.mana + rest < best:
                    best = data.mana + rest
            return best

        return cheapest(
            self.__boss_hp,
            self.__wizard_hp,
            self.__wizard_mana,
            0,
            0,
            0,
            True,
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_cheapest_win())
    if part in (None, 2):
        p2 = str(p.get_cheapest_win(True))

    return p1, p2
