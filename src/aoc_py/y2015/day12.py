"""
2015 day 12 - JSAbacusFramework.io

Uses the json module to load the data and then traverses it recursively to count the content.

Part 1 adds up every number anywhere in the document. Part 2 drops any object holding a value of "red", along with
everything nested inside it, and adds up what is left. The two are the same walk, so get_number_sum takes the string to
ignore and part 2 passes "red" while part 1 leaves it at its default.

The walk recurses once per level of nesting and sums on the way back out. An ignored object costs nothing to skip: it
returns 0 and the parent never looks inside it, which is what makes an object holding a red value drop its whole
subtree in one step.

The default of "" marks part 1 rather than None, and that has to be checked explicitly, because "" is itself a legal
JSON string. Without the ignored != "" test, part 1 would blank any object that happened to hold an empty string.

Two behaviours fall out of the isinstance ladder rather than being handled on purpose. A JSON boolean is an instance
of int in Python, so true counts as 1 and false as 0, while a float is not an int, so 1.5 contributes nothing at all.
The puzzle's documents hold only objects, arrays, numbers and strings, so neither case arises.
"""

import json
from typing import cast

# json.loads hands back Any, and walking it with isinstance narrows Any no further than Unknown, so the shapes the
# document can take get spelled out here instead.
type JsonValue = (
    None | bool | int | float | str | list[JsonValue] | dict[str, JsonValue]
)


class InputData:
    def __init__(self, s: str) -> None:
        self.__json = cast(JsonValue, json.loads(s))

    def get_number_sum(self, ignored: str = "") -> int:
        return self.__json_object_count(self.__json, ignored)

    def __json_object_count(self, json_input: JsonValue, ignored: str) -> int:
        if isinstance(json_input, dict):
            if ignored != "" and ignored in json_input.values():
                return 0
            else:
                return sum(
                    [
                        self.__json_object_count(json_input[j], ignored)
                        for j in json_input
                    ]
                )
        if isinstance(json_input, list):
            return sum([self.__json_object_count(j, ignored) for j in json_input])
        if isinstance(json_input, int):
            return json_input
        return 0  # strings have no value


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_number_sum())
    if part in (None, 2):
        p2 = str(p.get_number_sum("red"))

    return p1, p2
