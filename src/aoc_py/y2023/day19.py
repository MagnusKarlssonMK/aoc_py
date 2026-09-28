"""
2023 day 19 - Aplenty

Part 1

Fairly straightforward, just set up a way to organize the workflows and rules and run the input through and
see what comes out the other end.

Part 2

Yet another challenge in handling splitting ranges, mainly a headache trying to keep track of the layers of
dicts, ranges, lists etc.
"""

import operator
from collections.abc import Generator
from math import prod
from typing import Final

Partrating = dict[str, int]  # Parts = ['x', 'm', 'a', 's']
Partratingrange = dict[str, range]

PARTRANGE: Final = range(1, 4001)  # One to four thousand, for every part


class Rule:
    OPMAP: Final = {"<": operator.lt, ">": operator.gt}

    def __init__(self, rulestr: str) -> None:
        self.__condpart: str | None = None
        self.__condthrshold: int = 0
        self.__condoperation: str = ""
        tmp = rulestr.split(":")
        self.__ifpass = tmp[-1]
        if len(tmp) > 1:
            cond = tmp[0]
            self.__condoperation = ">" if ">" in cond else "<"
            self.__condpart, threshold = cond.split(self.__condoperation)
            self.__condthrshold = int(threshold)

    def getverdict(self, part: Partrating) -> str:
        return (
            ""
            if self.__condpart
            and not Rule.OPMAP[self.__condoperation](
                part[self.__condpart], self.__condthrshold
            )
            else self.__ifpass
        )

    def getrangesplit(
        self, inranges: Partratingrange
    ) -> Generator[tuple[str, Partratingrange]]:
        condpart = self.__condpart
        if condpart is None or self.__condthrshold not in inranges[condpart]:
            yield self.__ifpass, inranges
            return
        inrange = inranges[condpart]
        split = self.__condthrshold
        if self.__condoperation == ">":
            split += 1
        low = {**inranges, condpart: range(inrange.start, split)}
        high = {**inranges, condpart: range(split, inrange.stop)}
        if self.__condoperation == ">":
            yield "", low
            yield self.__ifpass, high
        else:
            yield "", high
            yield self.__ifpass, low


class InputData:
    def __init__(self, rawstr: str) -> None:
        wf, rt = rawstr.split("\n\n")
        self.__workflows: dict[str, list[Rule]] = {}
        for flow in wf.splitlines():
            label, rls = flow.strip("{}").split("{")
            self.__workflows[label] = [Rule(r) for r in rls.split(",")]
        self.__ratings: list[Partrating] = []
        for line in rt.splitlines():
            parts = line.strip("{}").split(",")
            self.__ratings.append(
                {p1: int(p2) for p1, p2 in (p.split("=") for p in parts)}
            )

    def __process_workflow(self, rating: Partrating) -> int:
        # Note: assumes that the input assures that every rating matches a workflow.
        currentworkflow = "in"
        while currentworkflow not in ("A", "R"):
            for rule in self.__workflows[currentworkflow]:
                if (verdict := rule.getverdict(rating)) != "":
                    currentworkflow = verdict
                    break
        return sum(rating.values()) if currentworkflow == "A" else 0

    def get_p1(self) -> int:
        return sum([self.__process_workflow(rating) for rating in self.__ratings])

    def get_p2(self) -> int:
        initialpartgroup: tuple[str, Partratingrange] = (
            "in",
            dict.fromkeys("xmas", PARTRANGE),
        )
        queue: list[tuple[str, Partratingrange]] = [initialpartgroup]
        verdict_a: list[Partratingrange] = []
        while queue:
            currentworkflow, ranges = queue.pop(0)
            if currentworkflow not in ("A", "R"):
                for rule in self.__workflows[currentworkflow]:
                    done = True
                    for newranges in rule.getrangesplit(ranges):
                        if newranges[0] != "":
                            queue.append(newranges)
                        else:
                            done = False
                            ranges = newranges[1]
                    if done:
                        break
            elif currentworkflow == "A":
                verdict_a.append(ranges)
        return sum(
            [
                prod([r.stop - r.start for r in a_ranges.values()])
                for a_ranges in verdict_a
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
