"""
2017 day 12 - Digital Plumber

Programs form an undirected graph through their pipes. The answer to part 1 is the size of the connected
component containing program 0, and part 2 counts all connected components.
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__numbers: list[list[int]] = []
        for line in s.splitlines():
            _, right = line.split(" <-> ")
            self.__numbers.append([int(n) for n in right.split(", ")])

    def get_group_counts(self) -> tuple[int, int]:
        """Return the size of program 0's group, and the total number of groups."""
        size = len(self.__numbers)
        seen = [False] * size
        group_sizes: list[int] = []
        for i in range(size):
            if not seen[i]:
                seen[i] = True
                group_sizes.append(self.__search_programs(seen, i))
        return group_sizes[0], len(group_sizes)

    def __search_programs(self, seen: list[bool], index: int) -> int:
        total = 1
        for program_id in self.__numbers[index]:
            if not seen[program_id]:
                seen[program_id] = True
                total += self.__search_programs(seen, program_id)
        return total


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    r1, r2 = InputData(inputdata).get_group_counts()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
