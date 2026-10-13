# Introduction

This is a collection of my Python solutions with varying degrees of quality to [Advent of Code](http://adventofcode.com) challenges, which 
I have been going through retroactively to blow the dust off my coding skills. Advent of Code is an annual event, with 
daily coding puzzles starting December 1, usually of gradually increasing complexity. I highly recommend these 
puzzles to anyone looking to improve their coding skills or learn a new language.

Note - The puzzles for past years can be found by clicking the 'Events' link on the top of the AoC page.

# Input files

It is assumed that the input data for each problem is stored in a file with a file structure like 
`/AdventOfCode-Input/<year>/day<xx>.txt`, where that parent folder is placed in the root folder of this repo.
If your naming, file structure or location is different, the paths in the "load_input" function in `src/runner.py`
needs to be modified accordingly.

# Running the solver

This package is managed using `UV`, which needs to be installed locally. Once installed, the solver can be run with the CLI tool.
To run the solver for a certain day, for example 2024 day 12:

```sh
uv run aoc-py 2024 12
```

To run only either part 1 or part 2:

```sh
uv run aoc-py 2024 12 --part 2
```

# Running tests

To run all unit tests:

```sh
uv run pytest
```

To specify and run tests only for a certain year, for example 2024:

```sh
uv run pytest tests/y2024
```

# Regression tests

In addition to the unit tests, there is a data driven regression suite that runs the
real solver for every puzzle that has both an input file and a stored answer file
under `AdventOfCode-Input/<year>`, and compares the output against that answer. It is
slow because it runs every implemented solver, so it is deselected from the default
test run. Run it with:

```sh
uv run pytest -m regression
```

Each answer file is named `day<xx>.answer` and contains part 1 and part 2 separated by
a line containing exactly `---`; single-part puzzles use `-` for part 2.

# Formatting, linting and type checking

Formatting is done with Ruff:

```sh
uv run ruff format
```

All code is written to pass default settings of `basedpyright` and `Ruff`.

```sh
uv run ruff check
```

```sh
uv run basedpyright
```

Note that both basedpyright and Ruff are added to the uv dev group, so new versions
needs to be bumped manually.

# Updating package versions

To update the versions of all external packages (within constraints in pyproject.toml):

```sh
uv sync --upgrade
```

To use the newest versions even if it crosses the floors:

```sh
uv sync --latest
```

To upgrade just the dev-group:

```sh
uv sync --upgrade-group dev
```
