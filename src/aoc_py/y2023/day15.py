"""
2023 day 15 - Lens Library
"""
from dataclasses import dataclass


def hash_algorithm(mystring: str) -> int:
    retval = 0
    for char in mystring:
        retval += ord(char)
        retval *= 17
        retval %= 256
    return retval


@dataclass(frozen=True)
class Lens:
    label: str
    strength: int


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__boxes: dict[int, list[Lens]] = {}
        self.__steps = rawstr.split(',')
        for word in self.__steps:
            if word.__contains__("="):
                label, foc_len = word.split("=")
                hash_val = hash_algorithm(label)
                if hash_val in self.__boxes:
                    for idx, box in enumerate(self.__boxes[hash_val]):
                        if box.label == label:
                            self.__boxes[hash_val][idx] = Lens(label, int(foc_len))
                            break
                    else:
                        self.__boxes[hash_val].append(Lens(label, int(foc_len)))
                else:
                    self.__boxes[hash_val] = [Lens(label, int(foc_len))]
            else:
                label = word.strip("-")
                hash_val = hash_algorithm(label)
                if hash_val in self.__boxes:
                    for idx, box in enumerate(self.__boxes[hash_val]):
                        if box.label == label:
                            _ =self.__boxes[hash_val].pop(idx)

    def get_p1(self) -> int:
        return sum([hash_algorithm(word) for word in self.__steps])

    def get_p2(self) -> int:
        return sum([box.strength * (i + 1) * (hash_val + 1) for hash_val in self.__boxes
                    for i, box in enumerate(self.__boxes[hash_val])])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
        p1, p2 = "-1"
        p = InputData(inputdata)
        if part in (None, 1):
            p1 = str(p.get_p1())
        if part in (None, 2):
            p2 = str(p.get_p2())

        return p1, p2
