"""
2021 day 10 - Syntax Scoring

Part 1

Solve with recursive function.
Define a class for it to avoid having to pass the line throughout all function calls.

Part 2

Since we know the incomplete lines are not corrupt, i.e. no need to check validity anymore, we can simply
start from the back of the string, find the first closing bracket, find its corresponding opening bracket, then remove
that entire chunk (since we already know that interior has to be valid). Repeat that process until there are no more
closing brackets left, and the answer is found simply by reversing the order of the remaining opening brackets and
converting to their corresponding closing brackets.
"""

from typing import Final


def getsyntaxscore(char: str) -> int:
    match char:
        case ")":
            return 3
        case "]":
            return 57
        case "}":
            return 1197
        case ">":
            return 25137
        case _:
            return 0


def getautocompletescore(char: str) -> int:
    match char:
        case ")":
            return 1
        case "]":
            return 2
        case "}":
            return 3
        case ">":
            return 4
        case _:
            return 0


class NavigationLine:
    __OPENING_BRACKETS: Final = ("(", "{", "<", "[")
    __BRACKET_MAP: Final = {"(": ")", "{": "}", "<": ">", "[": "]"}

    def __init__(self, s: str) -> None:
        self.__line = s

    def validate_line(self) -> tuple[int, int]:
        idx = 0
        while idx < len(self.__line):
            res, i = self.__validate_chunk(idx)
            if res != 0:
                return res, i
            idx = i + 1
        return 0, idx

    def __validate_chunk(self, start_idx: int = 0) -> tuple[int, int]:
        if self.__line[start_idx] not in NavigationLine.__OPENING_BRACKETS:
            return 2, getsyntaxscore(self.__line[start_idx])
        if start_idx >= len(self.__line) - 1:
            return 1, start_idx + 1
        if (
            self.__line[start_idx + 1]
            == NavigationLine.__BRACKET_MAP[self.__line[start_idx]]
        ):
            return 0, start_idx + 1
        current_idx = start_idx + 1
        while current_idx < len(self.__line):
            res, i = self.__validate_chunk(current_idx)
            if res == 0:
                if i + 1 >= len(self.__line):
                    return 1, i
                if (
                    self.__line[i + 1]
                    == NavigationLine.__BRACKET_MAP[self.__line[start_idx]]
                ):
                    return 0, i + 1
                elif self.__line[i + 1] not in NavigationLine.__OPENING_BRACKETS:
                    return 2, getsyntaxscore(self.__line[i + 1])
                current_idx = i + 1
            else:
                return res, i
        return 1, current_idx

    def autocomplete(self) -> int:
        line = [c for c in self.__line]
        count = 0
        close_br = ""
        for idx in reversed(range(len(self.__line))):
            if line[idx] not in NavigationLine.__OPENING_BRACKETS:
                if count == 0:
                    close_br = line[idx]
                    count = 1
                elif line[idx] == close_br:
                    count += 1
                _ = line.pop(idx)
            elif count > 0:
                if NavigationLine.__BRACKET_MAP[line[idx]] == close_br:
                    count -= 1
                _ = line.pop(idx)
        resultlist = [
            getautocompletescore(NavigationLine.__BRACKET_MAP[c])
            for c in reversed(line)
        ]
        retval = 0
        for i in resultlist:
            retval *= 5
            retval += i
        return retval


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__lines: list[str] = rawstr.splitlines()
        self.__incomplete_lines: list[NavigationLine] = []

    def get_p1(self) -> int:
        retval = 0
        for line in self.__lines:
            newline = NavigationLine(line)
            result, score = newline.validate_line()
            if result == 2:
                retval += score
            elif result == 1:
                self.__incomplete_lines.append(newline)
        return retval

    def get_p2(self) -> int:
        scores = sorted(
            [incomplete.autocomplete() for incomplete in self.__incomplete_lines]
        )
        return scores[len(scores) // 2]


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    r1 = p.get_p1()  # Part 1 must always be run before part 2
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
