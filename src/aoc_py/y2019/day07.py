"""
2019 day 7 - Amplification Circuit

- Step 1: Create five Intcode computers, all running the same program.
- Step 2: Part 1 chains the amplifiers in series: for every permutation of phases 0..4 feed each amplifier
  its phase followed by the previous amplifier's output, and keep the strongest final signal.
- Step 3: Part 2 runs the phases 5..9 in a feedback loop where the last amplifier's output feeds back into
  the first and each amplifier pauses after emitting an output; when the first amplifier halts the pulse
  stops, and the last signal produced is the result.
"""

from itertools import permutations

from aoc_py.y2019.intcode import Intcode, IntResult


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__amps = [Intcode(list(map(int, rawstr.split(",")))) for _ in range(5)]

    def get_p1(self) -> int:
        result = 0
        for phase_inputs in permutations(range(5)):
            out = 0
            for i, phase in enumerate(phase_inputs):
                self.__amps[i].add_input(phase)
                self.__amps[i].add_input(out)
                # Each amplifier emits a single value, then halts.
                out, _ = self.__amps[i].run_program()
                self.__amps[i].reboot()
            result = max(result, out)
        return result

    def get_p2(self) -> int:
        result = 0
        for phase_inputs in permutations(range(5, 10)):
            for i, amp in enumerate(self.__amps):
                amp.reboot()
                amp.add_input(phase_inputs[i])
            out = 0
            amp = 0
            while True:
                self.__amps[amp].add_input(out)
                val, res = self.__amps[amp].run_program()
                if res == IntResult.OUTPUT:
                    out = val
                else:
                    # The first amplifier to halt stops the pulse; the last signal emitted is the answer.
                    break
                amp = (amp + 1) % len(self.__amps)
            result = max(result, out)
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
