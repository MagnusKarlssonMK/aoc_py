"""
2022 day 3 - Rucksack Reorganization
"""

class InputData:
    __RANGELIST = ((range(ord('a'), ord('z') + 1), 1), (range(ord('A'), ord('Z') + 1), 27))

    def __init__(self, rawstr: str) -> None:
        self.__rucksacks = rawstr.splitlines()

    def get_p1(self) -> int:
        result = 0
        for rucksack in self.__rucksacks:
            left, right = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
            if len(shared := ''.join(set(left) & set(right))) > 0:
                result += sum([ord(shared[0]) - r0.start + r1 for r0, r1 in InputData.__RANGELIST
                               if ord(shared[0]) in r0])
        return result

    def get_p2(self) -> int:
        result = 0
        for r in range(0, len(self.__rucksacks), 3):
            s0, s1, s2 = self.__rucksacks[r: r + 3]
            if len(shared := ''.join(set(s0) & set(s1) & set(s2))) > 0:
                result += sum([ord(shared[0]) - r0.start + r1 for r0, r1 in InputData.__RANGELIST
                               if ord(shared[0]) in r0])
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
        p1, p2 = "-1"
        p = InputData(inputdata)
        if part in (None, 1):
            p1 = str(p.get_p1())
        if part in (None, 2):
            p2 = str(p.get_p2())

        return p1, p2
