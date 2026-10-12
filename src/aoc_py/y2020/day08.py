"""
2020 day 8 - Handheld Halting

Store the parsed program instructions in an InputData class, which also holds the accumulator
value. A method is called to run the program, which stops either when a loop is encountered or
when terminating successfully by reaching the row directly after the last instruction. To
repair the program, swap every nop/jmp one at a time and rerun until the program completes.
"""


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__accumulator = 0
        self.__instructions = [
            (left, int(right))
            for left, right in [line.split() for line in rawstr.splitlines()]
        ]

    def __run_program_to_loop(self) -> bool:
        """Returns True if run to completion (reaching the first index after the last row),
        False if loop encountered."""
        seen: set[int] = set()
        self.__accumulator = 0
        idx = 0
        while True:
            if idx in seen:
                return False
            seen.add(idx)
            cmd, value = self.__instructions[idx]
            if cmd == "jmp":
                idx = idx + value
            else:
                if cmd == "acc":
                    self.__accumulator += value
                idx += 1
            if idx == len(self.__instructions):
                return True
            idx = idx % len(self.__instructions)

    def get_boot_accumulator_value(self) -> int:
        _ = self.__run_program_to_loop()
        return self.__accumulator

    def repair(self) -> int:
        """Tries swapping all nop<->jmp until the program completes and returns the accumulator
        value once successful. Returns -1 if no solution found."""
        swap = {"nop": "jmp", "jmp": "nop"}
        for idx, (cmd, value) in enumerate(self.__instructions):
            if cmd == "acc":
                continue
            self.__instructions[idx] = (swap[cmd], value)
            if self.__run_program_to_loop():
                return self.__accumulator
            # else - not successful, reset
            self.__instructions[idx] = (cmd, value)
        return -1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_boot_accumulator_value())
    if part in (None, 2):
        p2 = str(p.repair())

    return p1, p2
