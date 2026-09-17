"""
2015 day 21 - RPG Simulator 20XX

Basic structure is a game consisting of a shop and two players (the player and the boss). Pretty much just generate
all possible equipment combinations from the shop and then simulate the battle to see who wins. The collected result
can then be used to determine the answers to both part 1 and 2.
"""

from collections.abc import Generator
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path


@dataclass(frozen=True)
class EquipmentItem:
    cost: int
    dmg: int
    armor: int


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
        for w in weapons:
            for a in armor:
                ringpairs = list(combinations(rings, 2))
                ringpairs.append((None, None))
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


class Player:
    def __init__(self, hp: int, dmg: int, armor: int) -> None:
        self.__base_hp: int = hp
        self.__base_dmg: int = dmg
        self.___base_armor: int = armor
        self.__equipped_item: EquipmentItem = EquipmentItem(0, 0, 0)
        self.__current_hp: int = self.__base_hp

    def new_equipment(self, new_eq: EquipmentItem) -> None:
        """Adds new equipment for player. The input is combined stats for all items."""
        self.__equipped_item = new_eq

    def reset_player(self) -> None:
        """Resets HP and removes any equipment."""
        self.__current_hp = self.__base_hp
        self.__equipped_item = EquipmentItem(0, 0, 0)

    def attack(self) -> int:
        """Returns outgoing damage from player."""
        return self.__base_dmg + self.__equipped_item.dmg

    def take_hit(self, incoming_dmg: int) -> bool:
        """Deal dmg to player, returns True if the hit kills the player."""
        self.__current_hp -= max(
            1, incoming_dmg - self.___base_armor - self.__equipped_item.armor
        )
        return self.__current_hp <= 0


class InputData:
    def __init__(self, boss_str: str, shopstr: str) -> None:
        self.__boss = Player(*parse_boss(boss_str))
        self.__player = Player(100, 0, 0)
        self.__shop = Shop(parse_shop(shopstr))

    def __player_wins(self, equipment: EquipmentItem) -> bool:
        """Plays a single round with a specific equipment loadout for the player. Returns True if player wins,
        False if the boss wins."""
        self.__player.new_equipment(equipment)
        rounds = 0
        while True:
            if rounds % 2 == 0:
                if self.__boss.take_hit(self.__player.attack()):
                    break
            else:
                if self.__player.take_hit(self.__boss.attack()):
                    break
            rounds += 1
        self.__player.reset_player()
        self.__boss.reset_player()
        return rounds % 2 == 0

    def get_loadouts(self) -> tuple[int, int]:
        """Runs the game simulation through all possible shop equipment loadouts and returns the answers
        to (part1, part2)."""
        winning_loadouts: list[EquipmentItem] = []
        losing_loadouts: list[EquipmentItem] = []
        for b in self.__shop.get_item_bundles():
            if self.__player_wins(b):
                winning_loadouts.append(b)
            else:
                losing_loadouts.append(b)
        winning_loadouts.sort(key=lambda x: x.cost)
        losing_loadouts.sort(key=lambda x: x.cost, reverse=True)
        r1 = winning_loadouts[0].cost if winning_loadouts else -1
        r2 = losing_loadouts[0].cost if losing_loadouts else -1
        return r1, r2


def parse_boss(s: str) -> tuple[int, int, int]:
    lines = s.splitlines()
    _, _, hp = lines[0].split()
    _, dmg = lines[1].split()
    _, armor = lines[2].split()
    return int(hp), int(dmg), int(armor)


def parse_shop(s: str) -> dict[str, dict[str, EquipmentItem]]:
    items: dict[str, dict[str, EquipmentItem]] = {}
    label = ""
    for block in s.split("\n\n"):
        for i, line in enumerate(block.splitlines()):
            tokens = line.split()
            if i == 0:
                label = tokens[0].strip(":")
                items[label] = {}
            else:
                if len(tokens) == 4:
                    items[label][tokens[0]] = EquipmentItem(
                        *list(map(int, tokens[1:4]))
                    )
                elif len(tokens) == 5:
                    items[label][tokens[0] + tokens[1]] = EquipmentItem(
                        *list(map(int, tokens[2:5]))
                    )
    return items


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    project_root = Path(__file__).resolve().parents[3]
    shop_path = project_root / "AdventOfCode-Input" / "2015" / "day21_shop.txt"
    if not shop_path.exists():
        raise FileNotFoundError(f"No shop input file at {shop_path}")
    shopdata = shop_path.read_text().strip("\n")
    p1 = p2 = "-1"
    p = InputData(inputdata, shopdata)
    r1, r2 = p.get_loadouts()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
