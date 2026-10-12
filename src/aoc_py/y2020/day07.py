"""
2020 day 7 - Handy Haversacks

Parse the bag rules into a dict mapping a bag colour to its contents. For part 1, search
outward from every bag to see whether the target bag can be found inside it; for part 2,
recursively count the bags required inside the target bag, memoising the totals.
"""

from collections import deque


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__rules: dict[str, list[tuple[int, str]]] = {}
        for line in rawstr.splitlines():
            outer, inner = line.split(" bags contain ")
            self.__rules[outer] = []
            if "no other" in inner:
                continue
            for content in inner.split(", "):
                nbr, bag_p1, bag_p2, _ = content.split()
                self.__rules[outer].append((int(nbr), f"{bag_p1} {bag_p2}"))
        self.__bagcontent_cache: dict[str, int] = {}

    def __can_contain(self, outer: str, target: str) -> bool:
        seen: set[str] = set()
        queue = deque(color for _, color in self.__rules[outer])
        while queue:
            color = queue.popleft()
            if color == target:
                return True
            if color not in seen:
                seen.add(color)
                queue.extend(c for _, c in self.__rules[color])
        return False

    def get_p1(self, bag: str) -> int:
        return sum(1 for key in self.__rules if self.__can_contain(key, bag))

    def get_p2(self, bag: str) -> int:
        return self.__count_content(bag) - 1  # -1 to not count the input bag itself

    def __count_content(self, bag: str) -> int:
        if bag in self.__bagcontent_cache:
            return self.__bagcontent_cache[bag]
        count = 1  # +1 to include the bag itself too, not just its content.
        for nbr, color in self.__rules[bag]:
            count += nbr * self.__count_content(color)
        self.__bagcontent_cache[bag] = count
        return count


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1("shiny gold"))
    if part in (None, 2):
        p2 = str(p.get_p2("shiny gold"))

    return p1, p2
