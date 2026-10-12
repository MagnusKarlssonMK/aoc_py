"""
2024 day 21 - Keypad Conundrum

The numeric keypad and the directional keypad are both parsed into key positions. Moving
between two keys produces a run of direction presses followed by an activation, and when
both vertical and horizontal movement is needed the order is chosen to route around the
empty corner. Part 1 materialises the sequence typed by two chained directional robots,
while part 2 tracks how many times each distinct move subsequence is needed through
twenty-five robots, so the sequence lengths never have to be built explicitly.
"""

from collections.abc import Sequence

NUMPAD = "789\n456\n123\n.0A"
DIRPAD = ".^A\n<v>"

ROBOTS_PART1 = 2
ROBOTS_PART2 = 25


class Keypad:
    def __init__(self, rawstr: str) -> None:
        self.__keys: dict[str, tuple[int, int]] = {}
        self.__positions: set[tuple[int, int]] = set()
        for y, line in enumerate(rawstr.splitlines()):
            for x, c in enumerate(line):
                if c == ".":
                    continue
                self.__keys[c] = (x, y)
                self.__positions.add((x, y))

    def get_commands(self, path: Sequence[str]) -> list[str]:
        """Presses needed to type the given keys, starting from the "A" key."""
        result: list[str] = []
        current = "A"
        for nxt in path:
            result.extend(self.__get_step(current, nxt))
            current = nxt
        return result

    def get_commands_counter(self, path: Sequence[str]) -> dict[tuple[str, ...], int]:
        """Like get_commands, but returns how many times each move subsequence is used."""
        result: dict[tuple[str, ...], int] = {}
        current = "A"
        for nxt in path:
            step = tuple(self.__get_step(current, nxt))
            result[step] = result.get(step, 0) + 1
            current = nxt
        return result

    def __get_step(self, from_key: str, to_key: str) -> list[str]:
        fx, fy = self.__keys[from_key]
        tx, ty = self.__keys[to_key]
        dx = tx - fx
        dy = ty - fy
        x_keys = [">"] * dx if dx > 0 else ["<"] * -dx
        y_keys = ["v"] * dy if dy > 0 else ["^"] * -dy
        if dx > 0 and (fx, ty) in self.__positions:
            return y_keys + x_keys + ["A"]
        if (tx, fy) in self.__positions:
            return x_keys + y_keys + ["A"]
        return y_keys + x_keys + ["A"]


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__codes = rawstr.splitlines()

    def get_p1(self) -> int:
        num_pad = Keypad(NUMPAD)
        dir_pad = Keypad(DIRPAD)
        seqs = [num_pad.get_commands(code) for code in self.__codes]
        for _ in range(ROBOTS_PART1):
            seqs = [dir_pad.get_commands(seq) for seq in seqs]
        return sum(
            len(seq) * self.__code_to_num(code) for seq, code in zip(seqs, self.__codes)
        )

    def get_p2(self) -> int:
        num_pad = Keypad(NUMPAD)
        dir_pad = Keypad(DIRPAD)
        seq_counter = [{tuple(num_pad.get_commands(code)): 1} for code in self.__codes]
        for _ in range(ROBOTS_PART2):
            new_seqs: list[dict[tuple[str, ...], int]] = []
            for counter in seq_counter:
                new_seq: dict[tuple[str, ...], int] = {}
                for sub_seq, qty in counter.items():
                    for key, count in dir_pad.get_commands_counter(sub_seq).items():
                        new_seq[key] = new_seq.get(key, 0) + count * qty
                new_seqs.append(new_seq)
            seq_counter = new_seqs
        return sum(
            sum(len(key) * count for key, count in counter.items())
            * self.__code_to_num(code)
            for counter, code in zip(seq_counter, self.__codes)
        )

    @staticmethod
    def __code_to_num(code: str) -> int:
        return int(code[:-1])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
