"""
2024 day 5 - Print Queue
"""

class InputData:
    def __init__(self, rawstr: str) -> None:
        rules, updates = rawstr.split("\n\n")
        self.__rules: set[tuple[int, int]] = {(int(left), int(right)) for left, right in
            [line.split('|') for line in rules.splitlines()]}
        self.__updates: list[list[int]] = [[int(n) for n in line.split(',')]
                                           for line in updates.splitlines()]

    def get_order_scores(self) -> tuple[int, int]:
        p1 = p2 = 0
        for update in self.__updates:
            sorted_update = sorted(update, key=lambda n1:
                                   sum([(n2, n1) in self.__rules for n2 in update]))
            if update == sorted_update:
                p1 += update[len(update) // 2]
            else:
                p2 += sorted_update[len(update) // 2]
        return p1, p2


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
        p1, p2 = "-1"
        p = InputData(inputdata)
        part1, part2 = p.get_order_scores()
        if part in (None, 1):
            p1 = str(part1)
        if part in (None, 2):
            p2 = str(part2)

        return p1, p2
