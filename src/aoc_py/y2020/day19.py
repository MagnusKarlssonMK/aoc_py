"""
2020 day 19 - Monster Messages

A bit of regex generation and recursion.
"""

import re


class InputData:
    def __init__(self, rawstr: str) -> None:
        rules, messages = rawstr.split("\n\n")
        self.__messages = messages.splitlines()
        self.__rules: dict[int, list[list[str]]] = {}
        for rule in rules.splitlines():
            left, right = rule.split(": ")
            self.__rules[int(left)] = [
                [c.strip('"') for c in s.split()] for s in right.split(" | ")
            ]

    def __gen_regex(self, rule: int = 0, depth: int = 20) -> str:
        if depth == 0:
            return ""
        if self.__rules[rule][0][0].isdigit():
            return (
                "("
                + "|".join(
                    [
                        "".join([self.__gen_regex(int(s), depth - 1) for s in sub])
                        for sub in self.__rules[rule]
                    ]
                )
                + ")"
            )
        return self.__rules[rule][0][0]

    def get_p1(self) -> int:
        r = re.compile(self.__gen_regex())
        result = [r.fullmatch(msg) for msg in self.__messages]
        return len([valid for valid in result if valid])

    def get_p2(self) -> int:
        self.__rules[8] = [["42"], ["42", "8"]]
        self.__rules[11] = [["42", "31"], ["42", "11", "31"]]
        return self.get_p1()


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    r1 = p.get_p1()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
