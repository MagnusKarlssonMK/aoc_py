"""
2015 day 12 - JSAbacusFramework.io

Uses the json module to load the data and then traverses it recursivly to count the content.
"""

import json


class InputData:
    def __init__(self, s: str) -> None:
        self.__json = json.loads(s)

    def get_number_sum(self, ignored: str = "") -> int:
        return self.__json_object_count(self.__json, ignored)

    def __json_object_count(self, json_input, ignored: str) -> int:
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
