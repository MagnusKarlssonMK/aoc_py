"""
2020 day 18 - Operation Order

Using the shunting yard algorithm. For part 2, the only difference is to check whether the top item on the operator
stack has higher precedence before popping it and putting it on the output stack.
"""

import operator
from typing import Final


def shunting_yard(line: str, is_advanced: bool) -> int:
    OPMAP: Final = {"+": operator.add, "*": operator.mul}
    # Generate the output buffer with shunting yard
    output: list[str] = []
    opstack: list[str] = []
    for c in line:
        if c.isdigit():
            output.append(c)
        elif c in OPMAP:
            while opstack:
                if opstack[-1] != "(" and (
                    not is_advanced or not (opstack[-1] == "*" and c == "+")
                ):
                    output.append(opstack.pop())
                else:
                    break
            opstack.append(c)
        elif c == "(":
            opstack.append(c)
        elif c == ")":
            while (o := opstack.pop()) != "(":
                output.append(o)
    while opstack:
        output.append(opstack.pop())
    # Evaluate the output buffer
    evaluated = []
    while output:
        o = output.pop(0)
        if o in OPMAP:
            v1 = int(evaluated.pop())
            v2 = int(evaluated.pop())
            evaluated.append(OPMAP[o](v1, v2))
        else:
            evaluated.append(o)
    return evaluated[0]


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__lines = rawstr.splitlines()

    def get_value_sum(self, isadvanced: bool = False) -> int:
        return sum([shunting_yard(line, isadvanced) for line in self.__lines])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_value_sum())
    if part in (None, 2):
        p2 = str(p.get_value_sum(True))

    return p1, p2
