"""
2015 day 21 - RPG Simulator 20XX

The shop is fixed puzzle-description data rather than anything the puzzle's own input varies, so it
lives here as a literal instead of being read from disk. The day's input is only the boss, and the
player is fixed at 100 hit points with no damage and no armour of its own, which is why the puzzle's
published examples cannot be used as test inputs: every one of them also varies the player's stats.
The player always attacks first, which matters for ties.

A loadout is one weapon, zero or one piece of armour, and up to two distinct rings, which gives
5 * 6 * 22 = 660 loadouts. The ring count is 1 + 6 + C(6, 2): no rings, one ring, or a pair. Building
that set by taking pairs from [None] plus the six rings does not work on its own, because
combinations draws two distinct items and so never yields the empty pair; that has to be appended
separately.

Nothing in the fight needs simulating round by round. Both sides lose max(1, hit - armour) per
exchange, so a loadout wins exactly when the hits needed to kill the boss is no more than the hits
the boss needs to kill the player. Since the player strikes first, a tie is a win. The answers then
fall out of the cheapest winning loadout and the biggest losing one, scanning 660 loadouts is far
cheaper than playing each one out.
"""

from collections.abc import Generator
from dataclasses import dataclass
from itertools import combinations
from typing import Final


@dataclass(frozen=True)
class EquipmentItem:
    cost: int
    dmg: int
    armor: int


# Transcribed from the puzzle description
SHOP_DATA: Final[dict[str, dict[str, EquipmentItem]]] = {
    "Weapons": {
        "Dagger": EquipmentItem(8, 4, 0),
        "Shortsword": EquipmentItem(10, 5, 0),
        "Warhammer": EquipmentItem(25, 6, 0),
        "Longsword": EquipmentItem(40, 7, 0),
        "Greataxe": EquipmentItem(74, 8, 0),
    },
    "Armor": {
        "Leather": EquipmentItem(13, 0, 1),
        "Chainmail": EquipmentItem(31, 0, 2),
        "Splintmail": EquipmentItem(53, 0, 3),
        "Bandedmail": EquipmentItem(75, 0, 4),
        "Platemail": EquipmentItem(102, 0, 5),
    },
    "Rings": {
        "Damage+1": EquipmentItem(25, 1, 0),
        "Damage+2": EquipmentItem(50, 2, 0),
        "Damage+3": EquipmentItem(100, 3, 0),
        "Defense+1": EquipmentItem(20, 0, 1),
        "Defense+2": EquipmentItem(40, 0, 2),
        "Defense+3": EquipmentItem(80, 0, 3),
    },
}


class Shop:
    def __init__(self, shopdata: dict[str, dict[str, EquipmentItem]]) -> None:
        self.__weapons: dict[str, EquipmentItem] = shopdata["Weapons"]
        self.__armor: dict[str, EquipmentItem] = shopdata["Armor"]
        self.__rings: dict[str, EquipmentItem] = shopdata["Rings"]

    def get_item_bundles(self) -> Generator[EquipmentItem]:
        """Generates all possible allowed item combinations (Weapons=1, Armor=0..1, Rings=0..2).
        Yields each combination as a single composit EquipmentItem."""
        weapons = list(self.__weapons)
        armor = [None] + list(self.__armor)
        rings = [None] + list(self.__rings)
        ringpairs = list(combinations(rings, 2))
        # combinations picks two distinct rings, so it never produces the pair of no rings at all.
        ringpairs.append((None, None))
        for w in weapons:
            for a in armor:
                for r1, r2 in ringpairs:
                    dmg = self.__weapons[w].dmg
                    cost = self.__weapons[w].cost
                    arm = 0
                    if a:
                        arm += self.__armor[a].armor
                        cost += self.__armor[a].cost
                    for r in (r1, r2):
                        if r:
                            arm += self.__rings[r].armor
                            dmg += self.__rings[r].dmg
                            cost += self.__rings[r].cost
                    yield EquipmentItem(cost, dmg, arm)


class InputData:
    __PLAYER_HP: Final = 100

    def __init__(self, boss_str: str) -> None:
        boss_hp, boss_dmg, boss_armor = parse_boss(boss_str)
        self.__boss_hp: int = boss_hp
        self.__boss_dmg: int = boss_dmg
        self.__boss_armor: int = boss_armor
        self.__shop = Shop(SHOP_DATA)

    @staticmethod
    def __hits_needed(target_hp: int, dmg: int, armor: int) -> int:
        """Rounds to kill target_hp, where each hit lands for at least one."""
        return -(-target_hp // max(1, dmg - armor))

    def __player_wins(self, equipment: EquipmentItem) -> bool:
        """Whether this loadout beats the boss. The player strikes first, so landing the killing
        blow on the same exchange as the boss counts as a win."""
        player_hits = self.__hits_needed(
            self.__boss_hp, equipment.dmg, self.__boss_armor
        )
        boss_hits = self.__hits_needed(
            InputData.__PLAYER_HP, self.__boss_dmg, equipment.armor
        )
        return player_hits <= boss_hits

    def get_loadouts(self) -> tuple[int, int]:
        """Returns the cheapest winning loadout cost and the biggest losing one, which are the
        answers to (part1, part2)."""
        cheapest_win: int | None = None
        biggest_loss: int | None = None
        for b in self.__shop.get_item_bundles():
            if self.__player_wins(b):
                if cheapest_win is None or b.cost < cheapest_win:
                    cheapest_win = b.cost
            elif biggest_loss is None or b.cost > biggest_loss:
                biggest_loss = b.cost
        return (
            cheapest_win if cheapest_win is not None else -1,
            biggest_loss if biggest_loss is not None else -1,
        )


def parse_boss(s: str) -> tuple[int, int, int]:
    lines = s.splitlines()
    _, _, hp = lines[0].split()
    _, dmg = lines[1].split()
    _, armor = lines[2].split()
    return int(hp), int(dmg), int(armor)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    r1, r2 = InputData(inputdata).get_loadouts()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
