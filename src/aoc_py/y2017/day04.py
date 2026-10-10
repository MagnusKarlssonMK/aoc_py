"""
2017 day 4 - High-Entropy Passphrases

Part 1

Simply make a set out of the words in every line and compare the lengths - if there are repeated words, the
length of the set will be smaller than the length of the list.

Part 2

For each line, make a set of the sorted letters of every word - anagrams collapse to the same entry, so comparing the
set size with the word count detects any two words that are anagrams.
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__phrases = [line.split() for line in s.splitlines()]

    def get_p1(self) -> int:
        return sum(len(line) == len(set(line)) for line in self.__phrases)

    def get_p2(self) -> int:
        return sum(
            len(line) == len({"".join(sorted(word)) for word in line})
            for line in self.__phrases
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
