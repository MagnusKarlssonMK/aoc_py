"""
2015 day 5 - Doesn't He Have Intern-Elves For This?

Part 1

Scan each line once, counting vowels and watching for a doubled letter, and give up on the line as soon as one of
the disallowed pairs ab, cd, pq or xy turns up. A line is nice when it has three or more vowels and at least one
doubled letter.

Part 2

The vowel rule is dropped and the other two are different: a letter that repeats with exactly one letter between
it, and two occurrences of the same pair of letters that do not overlap. The repeat check looks two characters
back, which is what "exactly one letter between them" means, and gives up early on the line if it fails. The pair
check leans on str.count, which counts non-overlapping occurrences, so a count above one means the pair occurs
twice without overlapping itself.

Note that a letter repeating three characters apart, with two letters in between, does not satisfy the repeat
rule. Reading it that way is an easy mistake, and admitting it turns the real answer from 55 into 80.
"""


class SantaString:
    def __init__(self, string: str) -> None:
        self.__string = string

    def is_nice(self) -> bool:
        vowels = 0
        previous = ""
        twice_in_a_row = False
        for c in self.__string:
            if previous + c in ("ab", "cd", "pq", "xy"):
                return False
            if previous == c:
                twice_in_a_row = True
            if c in ("a", "e", "i", "o", "u"):
                vowels += 1
            previous = c
        return twice_in_a_row and vowels >= 3

    def is_nice_newrules(self) -> bool:
        repeated_found = False
        for i in range(2, len(self.__string)):
            if self.__string[i] == self.__string[i - 2]:
                repeated_found = True
                break
        if not repeated_found:
            return False
        for i in range(len(self.__string) - 1):
            if self.__string.count(self.__string[i : i + 2]) > 1:
                return True
        return False


class InputData:
    def __init__(self, s: str) -> None:
        self.__strings = [SantaString(line) for line in s.splitlines()]

    def get_p1(self) -> int:
        return sum([1 if s.is_nice() else 0 for s in self.__strings])

    def get_p2(self) -> int:
        return sum([1 if s.is_nice_newrules() else 0 for s in self.__strings])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
