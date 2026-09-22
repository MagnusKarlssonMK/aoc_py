"""
2017 day 4 - High-Entropy Passphrases

Part 1

Simply make a set out of the words in every line and compare the lengths - if there are repeated words, the
length of the set will be smaller than the length of the list.

Part 2

For each line, make a set of characters for every word, and check all combinations of those words to see if
there is any overlap.
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__passphrases = [w.split() for w in [line for line in s.splitlines()]]

    def get_p1(self) -> int:
        return sum([1 for line in self.__passphrases if len(line) == len(set(line))])

    def get_p2(self) -> int:
        result = 0
        for line in self.__passphrases:
            sortedwords = ["".join(sorted(word)) for word in line]
            if len(sortedwords) == len(set(sortedwords)):
                result += 1
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
