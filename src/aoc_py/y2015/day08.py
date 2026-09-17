"""
2015 day 8 - Matchsticks

Scan each line for special characters.

Part 1

Count number of positions that does not represent an actual character.

Part 2

Count the characters that needs to be escaped.

"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__literals = s.splitlines()

    def get_p1(self) -> int:
        count = 0
        for line in self.__literals:
            count += 2  # Add 2 for the surrounding double quotes
            i = 1
            while i < len(line) - 1:
                if line[i] == "\\":
                    if line[i + 1] in ('"', "\\"):
                        count += 1
                        i += 1
                    elif line[i + 1] == "x":
                        count += 3
                        i += 3
                i += 1
        return count

    def get_p2(self) -> int:
        count = 0
        for line in self.__literals:
            count += 2  # Surrounding double quotes will expand by one character each
            for c in line:
                if c in ('"', "\\"):
                    count += 1
        return count


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
