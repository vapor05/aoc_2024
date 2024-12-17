import typing
import utils
from operator import add, mul


def _load_problem7_data(
    test: bool = False,
) -> list[tuple[int, list[int]]]:
    name = "problem7.txt" if not test else "test_problem7.txt"
    fl = utils._problem_data_file(name)
    data: list[tuple[int, list[int]]] = []

    with open(fl, "r") as f:
        for l in f.readlines():
            parts = l.strip().split(":")
            test_value = int(parts[0])
            values = [int(e) for e in parts[1].strip().split()]
            data.append((test_value, values))

    return data


def part1(test: bool = False) -> str:
    data = _load_problem7_data(test)
    valid: list[int] = []
    ops = [add, mul]

    for test_value, nums in data:
        is_valid = check(test_value, nums, ops)

        if is_valid:
            valid.append(test_value)

    return str(sum(valid))


def check(
    test_value: int, ns: list[int], ops: list[typing.Callable[[int, int], int]]
) -> bool:
    if len(ns) == 1:
        return test_value == ns[0]

    for op in ops:
        i = ns[0]
        j = ns[1]
        remaining = ns[2:]
        value = op(i, j)

        if value <= test_value:
            valid = check(test_value, [value, *remaining], ops)

            if valid:
                return True

    return False


def cat(a: int, b: int) -> int:
    return int(str(a) + str(b))


def part2(test: bool = False) -> str:
    data = _load_problem7_data(test)
    valid: list[int] = []
    ops = [add, mul, cat]

    for test_value, nums in data:
        is_valid = check(test_value, nums, ops)

        if is_valid:
            valid.append(test_value)

    return str(sum(valid))
