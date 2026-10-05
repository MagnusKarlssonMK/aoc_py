# Player always wins
TEST_STRING_1 = """Hit Points: 1
Damage: 0
Armor: 0"""

# Invincible boss
TEST_STRING_2 = """Hit Points: 1000
Damage: 100
Armor: 100"""

# This boss, and the two below, between them pin every non-zero cost, damage and armour value in
# the shop table: raising any one of them by one moves at least one of the two answers. They were
# picked by a greedy cover over a grid of bosses, three being the fewest that cover all 32 fields.
TEST_STRING_3 = """Hit Points: 40
Damage: 9
Armor: 7"""

TEST_STRING_4 = """Hit Points: 21
Damage: 10
Armor: 7"""

TEST_STRING_5 = """Hit Points: 35
Damage: 11
Armor: 8"""

from aoc_py.y2015.day21 import SHOP_DATA, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "8"


def test_part1_2() -> None:
    # No solution exists, boss always wins
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "-1"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "143"


def test_part1_4() -> None:
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "103"


def test_part1_5() -> None:
    p1, _ = solve_parts(TEST_STRING_5, 1)
    assert p1 == "180"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    # No solution exists, player always wins
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "-1"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "356"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "243"


def test_part2_4() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "235"


def test_part2_5() -> None:
    _, p2 = solve_parts(TEST_STRING_5, 2)
    assert p2 == "307"


# ----------- Both parts at once ------------


# This is the shape the runner itself uses.
def test_both_3() -> None:
    p1, p2 = solve_parts(TEST_STRING_3)
    assert p1 == "143"
    assert p2 == "243"


def test_both_5() -> None:
    p1, p2 = solve_parts(TEST_STRING_5)
    assert p1 == "180"
    assert p2 == "307"


# ----------- The shop table itself ------------


# The fields a boss cannot pin are the zero ones: a weapon's armour, or an armour piece's damage.
# Nothing distinguishes zero from one in those columns through the answers, so they are asserted
# directly. This also guards the transcription itself, which is a hand copy of the puzzle text.
def test_shop_table() -> None:
    assert {
        category: {
            name: (item.cost, item.dmg, item.armor) for name, item in items.items()
        }
        for category, items in SHOP_DATA.items()
    } == {
        "Weapons": {
            "Dagger": (8, 4, 0),
            "Shortsword": (10, 5, 0),
            "Warhammer": (25, 6, 0),
            "Longsword": (40, 7, 0),
            "Greataxe": (74, 8, 0),
        },
        "Armor": {
            "Leather": (13, 0, 1),
            "Chainmail": (31, 0, 2),
            "Splintmail": (53, 0, 3),
            "Bandedmail": (75, 0, 4),
            "Platemail": (102, 0, 5),
        },
        "Rings": {
            "Damage+1": (25, 1, 0),
            "Damage+2": (50, 2, 0),
            "Damage+3": (100, 3, 0),
            "Defense+1": (20, 0, 1),
            "Defense+2": (40, 0, 2),
            "Defense+3": (80, 0, 3),
        },
    }


# The loadout count is 5 weapons x 6 armour-or-nothing x 22 ring sets, and 22 is 1 + 6 + C(6, 2).
# A missing ring pair or a lost empty pair would both show up here as a different total.
def test_loadout_count() -> None:
    from aoc_py.y2015.day21 import Shop

    assert len(list(Shop(SHOP_DATA).get_item_bundles())) == 660
