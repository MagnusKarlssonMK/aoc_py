"""
2017 day 12 - Digital Plumber
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__numbers = [
            list(map(int, right.split(", ")))
            for _, right in [line.split(" <-> ") for line in s.splitlines()]
        ]

    def solve(self) -> tuple[int, int]:
        size = len(self.__numbers)
        seen = [False for _ in range(size)]
        program_groups = []
        for i in range(size):
            if not seen[i]:
                seen[i] = True
                program_groups.append(self.__search_programs(seen, i))
        return program_groups[0], len(program_groups)

    def __search_programs(self, seen: list[bool], index: int) -> int:
        total = 1
        for program_id in self.__numbers[index]:
            if not seen[program_id]:
                seen[program_id] = True
                total += self.__search_programs(seen, program_id)
        return total


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.solve()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
