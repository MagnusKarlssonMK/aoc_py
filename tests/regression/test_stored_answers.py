"""End-to-end regression tests against the stored `.answer` files.

For every puzzle that has both an input (`day<DD>.txt`) and an expected answer
(`day<DD>.answer`) under `AdventOfCode-Input/`, plus a matching solver module,
this runs the real solver and checks both parts of its output.

The `.answer` format is part 1, then a line containing exactly `---`, then part
2. Leading and trailing newlines on each part are ignored (the ASCII-art answers
are framed by blank lines). Single-part puzzles store `-` for part 2.

These tests run the real solvers and are therefore slow, so the `regression`
marker deselects them from the default run. Run them with:

    uv run pytest -m regression
"""

import importlib.util
from collections.abc import Callable
from pathlib import Path
from typing import cast

import pytest
from _pytest.mark.structures import ParameterSet

from aoc_py.runner import get_solver, load_input

INPUT_ROOT = Path(__file__).resolve().parents[2] / "AdventOfCode-Input"

# Solvers that render their answer as ASCII art while the stored `.answer` file
# still holds the plain-text form (these are the days not yet implemented in the
# Rust repo). They are expected to fail until the answers are converted; a
# strict xfail means a day that starts passing flags itself, which is the signal
# to drop it from this set.
PENDING_ASCII_ART_ANSWERS = {
    (2018, 10),
    (2019, 8),
    (2019, 11),
    (2021, 13),
}


def _parse_answer(text: str) -> tuple[str, str]:
    part1, _, part2 = text.strip("\n").partition("\n---\n")
    return part1.strip("\n"), part2.strip("\n")


def _has_solver(year: int, day: int) -> bool:
    return importlib.util.find_spec(f"aoc_py.y{year}.day{day:02d}") is not None


def _collect_cases() -> list[ParameterSet]:
    cases: list[ParameterSet] = []
    for year_dir in sorted(INPUT_ROOT.glob("20*")):
        if not year_dir.is_dir() or not year_dir.name.isdigit():
            continue
        year = int(year_dir.name)
        for answer_path in sorted(year_dir.glob("day*.answer")):
            stem = answer_path.stem
            if not stem[3:].isdigit():
                continue
            day = int(stem[3:])
            if not (year_dir / f"{stem}.txt").is_file() or not _has_solver(year, day):
                continue
            expected = _parse_answer(answer_path.read_text())
            marks: list[pytest.MarkDecorator] = []
            if (year, day) in PENDING_ASCII_ART_ANSWERS:
                marks.append(
                    pytest.mark.xfail(
                        reason="`.answer` still uses the plain-text form",
                        strict=True,
                    )
                )
            cases.append(
                pytest.param(
                    year, day, expected, id=f"{year}-day{day:02d}", marks=marks
                )
            )
    return cases


@pytest.mark.regression
@pytest.mark.parametrize(("year", "day", "expected"), _collect_cases())
def test_stored_answer(year: int, day: int, expected: tuple[str, str]) -> None:
    solve = cast(
        Callable[[str, int | None], tuple[str, str]],
        get_solver(year, day).solve_parts,
    )
    got = tuple(part.strip("\n") for part in solve(load_input(year, day), None))
    assert got == expected
