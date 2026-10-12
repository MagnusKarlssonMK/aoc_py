"""
2020 day 23 - Crab Cups

The cup circle is held as a singly linked list in an array: cups[i] is the cup clockwise from cup i, so
each move is O(1) and part 2's ten million moves stay quick. Part 1 plays 100 moves and reads the cups
clockwise from cup 1; part 2 extends the circle to a million cups and multiplies the two cups after 1.
"""

PART1_MOVES = 100
PART2_MOVES = 10_000_000
CUP_COUNT = 1_000_000


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__inputnbrs = list(map(int, rawstr))
        self.__cups: list[int] = []
        self.__current = 0
        self.__reset()

    def __reset(self) -> None:
        self.__cups = [0] * (max(self.__inputnbrs) + 1)
        self.__current = self.__inputnbrs[0]
        previous = self.__inputnbrs[-1]
        for cup in self.__inputnbrs:
            self.__cups[previous] = cup
            previous = cup

    def __next_cup(self, cup: int) -> int:
        return cup - 1 if cup > 1 else len(self.__cups) - 1

    def __play_move(self) -> None:
        r = self.__current
        removed = [r := self.__cups[r] for _ in range(3)]
        destination = self.__next_cup(self.__current)
        while destination in removed:
            destination = self.__next_cup(destination)
        self.__cups[self.__current] = self.__cups[removed[-1]]
        self.__cups[removed[-1]] = self.__cups[destination]
        self.__cups[destination] = removed[0]
        self.__current = self.__cups[self.__current]

    def __order_after_cup1(self) -> str:
        value = 1
        return "".join(
            str(value := self.__cups[value]) for _ in range(len(self.__cups) - 2)
        )

    def get_p1(self, moves: int) -> int:
        for _ in range(moves):
            self.__play_move()
        result = int(self.__order_after_cup1())
        self.__reset()
        return result

    def get_p2(self, moves: int) -> int:
        m = max(self.__inputnbrs)
        last = self.__inputnbrs[-1]
        self.__cups.extend(range(m + 2, CUP_COUNT + 2))
        self.__cups[-1] = self.__cups[last]
        self.__cups[last] = m + 1
        for _ in range(moves):
            self.__play_move()
        result = self.__cups[1] * self.__cups[self.__cups[1]]
        self.__reset()
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1(PART1_MOVES))
    if part in (None, 2):
        p2 = str(p.get_p2(PART2_MOVES))

    return p1, p2
