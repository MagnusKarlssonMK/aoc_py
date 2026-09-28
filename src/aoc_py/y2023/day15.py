"""
2023 day 15 - Lens Library

The HASH algorithm turns a string into a value between 0 and 255, and the two parts hand it
different things to chew on. Part 1 hashes the whole step, so the trailing focal length or dash is
part of the string, which is why rn=1 hashes to 30 rather than to the 0 that the bare label rn
gives. Part 2 buckets lenses on the hash of the label alone, keeping one box per hash value with
the lenses in the order they were inserted. The two rules look inconsistent, but hashing only the
label in part 1 would give 20 for the example rather than the expected 1320.

Part 2 then walks the boxes with both indices counting from one, so a lens of focal length f sitting
in position i of box h contributes f * i * (h + 1) to the total.
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
        self.__steps = rawstr.split(",")
        for word in self.__steps:
            if "=" in word:
                label, _, focal = word.partition("=")
                self.__insert(hash_algorithm(label), label, int(focal))
            else:
                label = word.rstrip("-")
                self.__remove(hash_algorithm(label), label)

    def __insert(self, hash_val: int, label: str, strength: int) -> None:
        """Puts a lens at the end of its box, replacing any lens that already carries the label."""
        box = self.__boxes.setdefault(hash_val, [])
        newlens = Lens(label, strength)
        for idx, lens in enumerate(box):
            if lens.label == label:
                box[idx] = newlens
                return
        box.append(newlens)

    def __remove(self, hash_val: int, label: str) -> None:
        """Takes the lens with this label out of its box, if the box holds it at all."""
        if hash_val in self.__boxes:
            box = self.__boxes[hash_val]
            self.__boxes[hash_val] = [lens for lens in box if lens.label != label]

    def get_p1(self) -> int:
        return sum([hash_algorithm(word) for word in self.__steps])

    def get_p2(self) -> int:
        return sum(
            [
                lens.strength * (i + 1) * (hash_val + 1)
                for hash_val in self.__boxes
                for i, lens in enumerate(self.__boxes[hash_val])
            ]
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
