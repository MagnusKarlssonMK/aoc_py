"""
2022 day 13 - Distress Signal
"""


def get_cbi(inputstr: str) -> int:
    """Analyzes a string starting with '[' in the first character and returns the Closing Bracket Index of the
    corresponding closing ']' bracket. Returns -1 if not found in string or first character is not a bracket."""
    if len(inputstr) < 2 or inputstr[0] != "[":
        return -1
    count = 0
    for idx, c in enumerate(inputstr):
        if c == "[":
            count += 1
        elif c == "]":
            count -= 1
        if count == 0:
            return idx
    return -1


class ElfList:
    """Constructor takes the AOC input in string format and parses it into list data. Comparison operators can be used
    to compare different list objects according to the AOC rules."""

    def __init__(self, s: str) -> None:
        """Assumes that the string has '[' in the first character and ']' in the last."""
        self.list: list[ElfList | int] = []
        i = 1
        while i < (len(s) - 1):
            if s[i] == "[":
                cbi = i + get_cbi(s[i:])
                self.list.append(ElfList(s[i : cbi + 1]))
                i = cbi
            elif s[i].isdigit():
                nbrs = s[i:].split(",")
                nbr = nbrs[0].strip("]")
                self.list.append(int(nbr))
                i += len(nbr)
            else:
                i += 1

    def issmallerthan(self, other: ElfList) -> int:
        for i in range(min(len(self.list), len(other.list))):
            first = self.list[i]
            second = other.list[i]
            if isinstance(first, int):
                if isinstance(second, int):
                    if first < second:
                        return 1
                    if first > second:
                        return -1
                else:
                    newlist = ElfList("[" + str(first) + "]")
                    test = newlist.issmallerthan(second)
                    if test != 0:
                        return test
            elif isinstance(second, int):
                newlist = ElfList("[" + str(second) + "]")
                test = first.issmallerthan(newlist)
                if test != 0:
                    return test
            else:
                test = first.issmallerthan(second)
                if test != 0:
                    return test
        if len(self.list) < len(other.list):
            return 1
        if len(self.list) > len(other.list):
            return -1
        return 0

    def __lt__(self, other: ElfList) -> bool:
        return self.issmallerthan(other) != -1


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__pairs: list[tuple[ElfList, ElfList]] = []
        for pair in rawstr.split("\n\n"):
            left, right = pair.split("\n")
            self.__pairs.append((ElfList(left), ElfList(right)))

    def get_p1(self) -> int:
        return sum(
            [idx + 1 for idx, pair in enumerate(self.__pairs) if pair[0] < pair[1]]
        )

    def get_p2(self) -> int:
        all_packet_list: list[ElfList] = []
        for p1, p2 in self.__pairs:
            all_packet_list.append(p1)
            all_packet_list.append(p2)
        divider_two = ElfList("[[2]]")
        divider_six = ElfList("[[6]]")
        all_packet_list.append(divider_two)
        all_packet_list.append(divider_six)
        all_packet_list.sort()
        return (all_packet_list.index(divider_two) + 1) * (
            all_packet_list.index(divider_six) + 1
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
