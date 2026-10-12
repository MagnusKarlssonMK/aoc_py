"""
2020 day 18 - Operation Order

Evaluate each expression with the shunting yard algorithm. Part 1 gives both operators equal
precedence (plain left to right); part 2 gives "+" higher precedence than "*". The only
difference is the precedence table handed to the evaluator.
"""

import operator
from collections.abc import Callable
from typing import Final

_OPERATORS: Final[dict[str, Callable[[int, int], int]]] = {
    "+": operator.add,
    "*": operator.mul,
}
_PRECEDENCE_P1: Final = {"+": 0, "*": 0}
_PRECEDENCE_P2: Final = {"+": 1, "*": 0}


def shunting_yard(line: str, precedence: dict[str, int]) -> int:
    # Turn the infix expression into reverse polish notation.
    output: list[str] = []
    opstack: list[str] = []
    for c in line:
        if c.isdigit():
            output.append(c)
        elif c in _OPERATORS:
            while (
                opstack
                and opstack[-1] != "("
                and precedence[opstack[-1]] >= precedence[c]
            ):
                output.append(opstack.pop())
            opstack.append(c)
        elif c == "(":
            opstack.append(c)
        elif c == ")":
            while (o := opstack.pop()) != "(":
                output.append(o)
    while opstack:
        output.append(opstack.pop())
    # Evaluate the reverse polish notation.
    evaluated: list[int] = []
    for o in output:
        if o in _OPERATORS:
            v2 = evaluated.pop()
            v1 = evaluated.pop()
            evaluated.append(_OPERATORS[o](v1, v2))
        else:
            evaluated.append(int(o))
    return evaluated[0]


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__lines = rawstr.splitlines()

    def get_p1(self) -> int:
        return sum(shunting_yard(line, _PRECEDENCE_P1) for line in self.__lines)

    def get_p2(self) -> int:
        return sum(shunting_yard(line, _PRECEDENCE_P2) for line in self.__lines)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
