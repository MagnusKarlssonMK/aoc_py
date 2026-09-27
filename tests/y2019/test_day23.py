# Day 23 puzzle description gives no test input, so these are hand-crafted intcode programs that act as the
# network interface controllers. The same program runs on all 50 nodes; each node first receives its own
# address as input, then the solver processes the nodes round-robin, delivering routed packets and feeding -1
# to nodes that wait without queued input. When a full lap produces no traffic the NAT sends its stored packet
# to node 0, which is the delivery that part 2 detects as stabilised:
#
# - TEST_STRING_1: every node immediately sends packet (255, 5, 7) and then skips -1s; after the NAT reseeds
#   node 0 with (5, 7) it sends the same packet again, so the NAT Y stabilises at 7.
# - TEST_STRING_2: node 0 routes (1, 10, 20) to node 1, which forwards it to address 255; node 0 skips -1s
#   until the NAT reseeds it, then routes again, so node 1 forwards a second time and the NAT Y stabilises at
#   20. This variant also exercises packet routing and delivering queued input to a waiting node.
TEST_STRING_1 = """3,1000,104,255,104,5,104,7,3,1001,108,-1,1001,1003,1005,1003,8,3,1002,104,255,4,1001,4,1002,99"""

TEST_STRING_2 = """3,1000,108,0,1000,1003,1006,1003,33,104,1,104,10,104,20,3,1001,108,-1,1001,1004,1005,1004,15,3,1002,104,1,4,1001,4,1002,99,108,1,1000,1003,1006,1003,60,3,1001,108,-1,1001,1004,1005,1004,40,3,1002,104,255,4,1001,4,1002,1105,1,40,3,1001,108,-1,1001,1004,1005,1004,60"""

from aoc_py.y2019.day23 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "7"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "20"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "7"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "20"


def test_part2_3() -> None:
    p1, p2 = solve_parts(TEST_STRING_1)
    assert p1 == "7"
    assert p2 == "7"


def test_part2_4() -> None:
    p1, p2 = solve_parts(TEST_STRING_2)
    assert p1 == "20"
    assert p2 == "20"
