from aoc_py.y2019.intcode import Intcode, IntResult

# ----------- Helpers ------------


def _run_cpu(
    program: list[int], inputs: list[int] | None = None
) -> tuple[Intcode, list[int]]:
    cpu = Intcode(program)
    for value in inputs or []:
        cpu.add_input(value)
    output: list[int] = []
    while True:
        value, res = cpu.run_program()
        if res is IntResult.OUTPUT:
            output.append(value)
        elif res is IntResult.HALTED:
            break
        else:  # WAIT_INPUT: only reachable when the program out-asks its inputs
            break
    return cpu, output


# ----------- Arithmetic -----------


def test_arithmetic_position() -> None:
    samples = [
        ([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 3500),
        ([1, 0, 0, 0, 99], 2),
        ([2, 3, 0, 3, 99], 2),
        ([2, 4, 4, 5, 99, 0], 2),
        ([1, 1, 1, 4, 2, 5, 6, 0, 99], 30),
    ]
    for program, expected in samples:
        cpu, _ = _run_cpu(program)
        assert cpu.read_memory(0) == expected


def test_arithmetic_immediate() -> None:
    cpu, _ = _run_cpu([1002, 4, 3, 4, 33])
    assert cpu.read_memory(4) == 99
    cpu, _ = _run_cpu([1101, 100, -1, 4, 0])
    assert cpu.read_memory(4) == 99


# ----------- Input / output -----------


def test_io_echo() -> None:
    cpu, output = _run_cpu([3, 0, 4, 0, 99], [42])
    assert output == [42]
    assert cpu.read_memory(0) == 42


def test_io_buffered_inputs() -> None:
    _, output = _run_cpu([3, 0, 3, 1, 4, 0, 4, 1, 99], [5, 6])
    assert output == [5, 6]


def test_input_wait_resume() -> None:
    cpu = Intcode([3, 0, 4, 0, 99])
    value, res = cpu.run_program()
    assert (value, res) == (-1, IntResult.WAIT_INPUT)
    cpu.add_input(7)
    value, res = cpu.run_program()
    assert (value, res) == (7, IntResult.OUTPUT)
    value, res = cpu.run_program()
    assert (value, res) == (-1, IntResult.HALTED)


# ----------- Comparisons and jumps -----------


def test_equality_position() -> None:
    program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    assert _run_cpu(program, [8])[1] == [1]
    assert _run_cpu(program, [7])[1] == [0]


def test_diagnostic_jumps() -> None:
    program = [
        3,
        21,
        1008,
        21,
        8,
        20,
        1005,
        20,
        22,
        107,
        8,
        21,
        20,
        1006,
        20,
        31,
        1106,
        0,
        36,
        98,
        0,
        0,
        1002,
        21,
        125,
        20,
        4,
        20,
        1105,
        1,
        46,
        104,
        999,
        1105,
        1,
        46,
        1101,
        1000,
        1,
        20,
        4,
        20,
        1105,
        1,
        46,
        98,
        99,
    ]
    assert _run_cpu(program, [7])[1] == [999]
    assert _run_cpu(program, [8])[1] == [1000]
    assert _run_cpu(program, [9])[1] == [1001]


# ----------- Relative base -----------


def test_relative_base() -> None:
    quine = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    _, output = _run_cpu(quine)
    assert output == quine


def test_relative_write() -> None:
    # 21101: ADD with immediate first and second parameters and a relative-mode destination.
    _, output = _run_cpu([109, 2, 21101, 5, 3, 0, 4, 2, 99])
    assert output == [8]


# ----------- Large numbers -----------


def test_large_numbers() -> None:
    assert _run_cpu([1102, 34915192, 34915192, 7, 4, 7, 99, 0])[1] == [1219070632396864]
    assert _run_cpu([104, 1125899906842624, 99])[1] == [1125899906842624]


# ----------- Lifecycle -----------


def test_reboot() -> None:
    cpu = Intcode([3, 0, 4, 0, 99])
    cpu.add_input(5)
    _ = cpu.run_program()
    cpu.reboot()
    _, res = cpu.run_program()  # input buffer was cleared by reboot
    assert res is IntResult.WAIT_INPUT
    assert cpu.read_memory(0) == 3


def test_override_program() -> None:
    cpu = Intcode([1101, 0, 0, 0, 99])
    cpu.override_program(1, 5)
    cpu.override_program(2, 7)
    _, res = cpu.run_program()
    assert res is IntResult.HALTED
    assert cpu.read_memory(0) == 12
