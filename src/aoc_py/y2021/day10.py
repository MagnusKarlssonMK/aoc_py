"""
2021 day 10 - Syntax Scoring

Part 1

Walk each line once, keeping a stack of the brackets that are still open. A closing bracket that does not match
the one on top of the stack means the line is corrupt, and contributes the score of the offending closing
bracket. A line that ends with brackets still open is incomplete, and contributes nothing here.

Part 2

The scan of part 1 already leaves us the brackets that remain open, so there is no need to walk the lines
again. For each incomplete line, take those remaining opening brackets in reverse order, convert each to the
closing bracket it calls for, and read the resulting sequence of scores as a base 5 number. The answer is the
median of those numbers.
"""

from typing import Final

OPENING_BRACKETS: Final = ("(", "{", "<", "[")
BRACKET_MAP: Final = {"(": ")", "{": "}", "<": ">", "[": "]"}
CLOSING_MAP: Final = {v: k for k, v in BRACKET_MAP.items()}
SYNTAX_SCORES: Final = {")": 3, "]": 57, "}": 1197, ">": 25137}
COMPLETION_SCORES: Final = {")": 1, "]": 2, "}": 3, ">": 4}
VALID: Final = 0
INCOMPLETE: Final = 1
CORRUPT: Final = 2


def getsyntaxscore(char: str) -> int:
    return SYNTAX_SCORES.get(char, 0)


def getautocompletescore(char: str) -> int:
    return COMPLETION_SCORES.get(char, 0)


class NavigationLine:
    def __init__(self, s: str) -> None:
        self.__line = s

    def __scan(self) -> tuple[int, int, list[str]]:
        """Walk the line once, returning its status, its syntax score, and the brackets
        still open when the walk ended."""
        stack: list[str] = []
        for char in self.__line:
            if char in OPENING_BRACKETS:
                stack.append(char)
            elif stack and stack[-1] == CLOSING_MAP[char]:
                _ = stack.pop()
            else:
                return CORRUPT, getsyntaxscore(char), stack
        return (INCOMPLETE if stack else VALID), 0, stack

    def validate_line(self) -> tuple[int, int]:
        """Return the status of the line, and its syntax score, which is 0 unless corrupt."""
        status, score, _ = self.__scan()
        return status, score

    def autocomplete(self) -> int:
        """Score the closing brackets an incomplete line is waiting for."""
        _, _, stack = self.__scan()
        retval = 0
        for char in reversed(stack):
            retval *= 5
            retval += getautocompletescore(BRACKET_MAP[char])
        return retval


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__lines: list[str] = rawstr.splitlines()
        self.__incomplete_lines: list[NavigationLine] = []
        self.__syntax_score = 0
        for line in self.__lines:
            newline = NavigationLine(line)
            status, score = newline.validate_line()
            if status == CORRUPT:
                self.__syntax_score += score
            elif status == INCOMPLETE:
                self.__incomplete_lines.append(newline)

    def get_p1(self) -> int:
        return self.__syntax_score

    def get_p2(self) -> int:
        scores = sorted(
            [incomplete.autocomplete() for incomplete in self.__incomplete_lines]
        )
        return scores[len(scores) // 2]


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
