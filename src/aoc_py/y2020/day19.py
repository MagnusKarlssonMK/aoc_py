"""
2020 day 19 - Monster Messages

Check whether rule 0 can consume each whole message. Rules are matched recursively: matching a
rule from a given position yields the set of positions it can end at, threading positions
through the tokens of each alternative and unioning the alternatives. This handles the
recursive rules of part 2 directly, without unrolling them or using regex.
"""

from typing import Final

_P2_OVERRIDES: Final = {
    8: [["42"], ["42", "8"]],
    11: [["42", "31"], ["42", "11", "31"]],
}


def _match_rule(
    rules: dict[int, list[list[str]]],
    rule: int,
    text: str,
    pos: int,
    memo: dict[tuple[int, int], set[int]],
) -> set[int]:
    key = (rule, pos)
    if key in memo:
        return memo[key]
    ends: set[int] = set()
    for alternative in rules[rule]:
        positions = {pos}
        for token in alternative:
            reached: set[int] = set()
            for p in positions:
                if token.isdigit():
                    reached |= _match_rule(rules, int(token), text, p, memo)
                elif p < len(text) and text[p] == token:
                    reached.add(p + 1)
            positions = reached
            if not positions:
                break
        ends |= positions
    memo[key] = ends
    return ends


class InputData:
    def __init__(self, rawstr: str) -> None:
        rulelines, messages = rawstr.split("\n\n")
        self.__messages = messages.splitlines()
        self.__rules: dict[int, list[list[str]]] = {}
        for line in rulelines.splitlines():
            left, right = line.split(": ")
            self.__rules[int(left)] = [
                [token.strip('"') for token in alt.split()]
                for alt in right.split(" | ")
            ]

    def __count_matches(self, rules: dict[int, list[list[str]]]) -> int:
        return sum(
            1
            for msg in self.__messages
            if len(msg) in _match_rule(rules, 0, msg, 0, {})
        )

    def get_p1(self) -> int:
        return self.__count_matches(self.__rules)

    def get_p2(self) -> int:
        return self.__count_matches({**self.__rules, **_P2_OVERRIDES})


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
