import importlib
import time
from collections.abc import Callable
from pathlib import Path
from types import ModuleType
from typing import cast


def load_input(year: int, day: int) -> str:
    project_root = Path(__file__).resolve().parents[2]
    path = project_root / "AdventOfCode-Input" / str(year) / f"day{day:02d}.txt"
    if not path.exists():
        raise FileNotFoundError(f"No input file at {path}")
    return path.read_text().strip("\n")

def get_solver(year: int, day: int) -> ModuleType:
    module_name = f"aoc_py.y{year}.day{day:02d}"
    try:
        return importlib.import_module(module_name)
    except ModuleNotFoundError:
        raise ModuleNotFoundError(f"No solver found for {year} day {day}")

""" Loads input and dispatches to the corresponding solver. """
def run(year: int, day:int, part: int | None = None) -> None:
    inputdata = load_input(year, day)
    solver = get_solver(year, day)

    start_time = time.perf_counter()
    solver_func = cast(Callable[[str, int | None], tuple[str, str]], solver.solve_parts)
    (p1, p2) = solver_func(inputdata, part)
    end_time = time.perf_counter()
    if part in (None, 1):
        print(f"Part 1: {p1}")
    if part in (None, 2):
        print(f"Part 2: {p2}")
    print(f"Total time (ms): {round(1000 * (end_time - start_time), 3)}")
