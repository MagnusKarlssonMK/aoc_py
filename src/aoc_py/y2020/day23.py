"""
2020 day 23 - Crab Cups

Storing the cup list as a singly linked list in an array, to avoid slow list operations since we need to do a lot
of moves for part 2.
"""

from dataclasses import dataclass


@dataclass
class LinkList:
    cups: list[int]

    def get_next(self, val: int) -> int:
        return val - 1 if val > 1 else len(self.cups) - 1

    def get_order(self) -> str:
        value = 1
        return "".join(
            [str(value := self.cups[value]) for _ in range(len(self.cups) - 2)]
        )


class InputData:
    def __init__(self, s: str) -> None:
        self.__inputnbrs = list(map(int, s))
        self.__list = LinkList([0 for _ in range(max(self.__inputnbrs) + 1)])
        self.__current = 0
        self.__reset()

    def __reset(self) -> None:
        self.__list = LinkList([0 for _ in range(max(self.__inputnbrs) + 1)])
        self.__current = self.__inputnbrs[0]
        previous = self.__inputnbrs[-1]
        for cup in self.__inputnbrs:
            self.__list.cups[previous] = cup
            previous = cup

    def __play_move(self) -> None:
        r = self.__current
        removed = [r := self.__list.cups[r] for _ in range(3)]
        destination = self.__list.get_next(self.__current)
        while destination in removed:
            destination = self.__list.get_next(destination)
        self.__list.cups[self.__current] = self.__list.cups[removed[-1]]
        self.__list.cups[removed[-1]] = self.__list.cups[destination]
        self.__list.cups[destination] = removed[0]
        self.__current = self.__list.cups[self.__current]

    def get_p1(self, moves: int = 100) -> int:
        for _ in range(moves):
            self.__play_move()
        result = int(self.__list.get_order())
        self.__reset()
        return result

    def get_p2(self, moves: int = 10_000_000) -> int:
        m = max(self.__inputnbrs)
        last = self.__inputnbrs[-1]
        self.__list.cups.extend(range(m + 2, 1_000_002))
        self.__list.cups[-1] = self.__list.cups[last]
        self.__list.cups[last] = m + 1
        for _ in range(moves):
            self.__play_move()
        return self.__list.cups[1] * self.__list.cups[self.__list.cups[1]]


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
