TEST_STRING_1 = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

TEST_STRING_2 = """$ cd /
$ ls
dir b
dir c
dir d
dir e
dir g
dir f
dir x
dir p
$ cd b
$ ls
100000 bfile
$ cd /
$ cd c
$ ls
dir c1
60000 cfile
$ cd c1
$ ls
450000 c1file
$ cd ..
$ cd /
$ cd d
$ ls
30000 dfile
$ cd /
$ cd e
$ ls
1000 efile
$ cd /
$ cd g
$ ls
100001 gfile
$ cd /
$ cd f
$ ls
39258222 ffile
$ cd /
$ cd x
$ ls
777 xroot
$ cd /
$ cd p
$ ls
dir q
dir x
100 pfile
$ cd q
$ ls
200 qfile
$ cd ..
$ cd x
$ ls
111 xfile
$ cd ..
$ cd /"""

from aoc_py.y2022.day07 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "95437"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "132499"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "24933642"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "411"
