import re
import pathlib

input_dir = pathlib.Path(__file__).parent.joinpath("problem_data")


def _problem_data_file(fn: str) -> pathlib.Path:
    return input_dir.joinpath(fn)


def _load_problem_one_data() -> tuple[list[int], list[int]]:
    fl = _problem_data_file("problem1.txt")
    ll: list[int] = []
    rl: list[int] = []

    with open(fl, "r") as f:
        for l in f.readlines():
            nums = l.strip().split()
            ll.append(int(nums[0]))
            rl.append(int(nums[1]))

    return ll, rl


def problem1_part1() -> str:
    ll, rl = _load_problem_one_data()

    ll.sort()
    rl.sort()

    dists = [abs(l - r) for l, r in zip(ll, rl)]
    return str(sum(dists))


def problem1_part2() -> str:
    ll, rl = _load_problem_one_data()
    mult_map: dict[int, int] = {}

    for r in rl:
        if r not in mult_map:
            mult_map[r] = 1
        else:
            mult_map[r] += 1

    products = [l * mult_map.get(l, 0) for l in ll]
    return str(sum(products))


def _load_problem_2_data() -> list[list[int]]:
    fl = _problem_data_file("problem2.txt")
    reports: list[list[int]] = []

    with open(fl, "r") as f:
        for l in f.readlines():
            levels = [int(e) for e in l.strip().split()]
            reports.append(levels)

    return reports


def problem2_part1() -> str:
    reports: list[list[int]] = _load_problem_2_data()
    safe = []

    for report in reports:
        s = True

        if report[0] < report[1]:
            asc = True
        else:
            asc = False

        for i in range(len(report) - 1):
            if asc:
                if report[i] > report[i + 1]:
                    s = False
                    break
            else:
                if report[i] < report[i + 1]:
                    s = False
                    break

            diff = abs(report[i] - report[i + 1])

            if diff < 1 or diff > 3:
                s = False
                break

        if s:
            safe.append(report)

    return str(len(safe))


def problem2_part2() -> str:
    reports: list[list[int]] = _load_problem_2_data()
    safe = []

    for report in reports:
        bad_levels = 0

        if report[0] < report[1]:
            asc = True
        else:
            asc = False

        end = len(report)
        i = 0

        while i < end - 1:
            l = report[i]
            r = report[i + 1]
            skip_diff = False

            if asc:
                if l >= r:
                    bad_levels += 1
                    skip_diff = True
            else:
                if l <= r:
                    bad_levels += 1
                    skip_diff = True

            if not skip_diff:
                diff = abs(l - r)

                if diff < 1 or diff > 3:
                    bad_levels += 1
            i += 1

        if bad_levels < 2:
            safe.append(report)

    return str(len(safe))


def _load_problem_3_data() -> str:
    fl = _problem_data_file("problem3.txt")

    with open(fl, "r") as f:
        data = f.read()

    return data


def problem3_part1() -> str:
    instructions = _load_problem_3_data()
    mul_pattern = re.compile(r"(mul\(\d{1,3},\d{1,3}\))")
    matches = mul_pattern.findall(instructions)
    num_pattern = re.compile(r"(\d{1,3})")
    pairs = [num_pattern.findall(e) for e in matches]
    products = [int(p[0]) * int(p[1]) for p in pairs]
    return str(sum(products))


def problem3_part2() -> str:
    memory = _load_problem_3_data()
    instruction_pattern = re.compile(r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don\'t\(\))")
    matches = instruction_pattern.findall(memory)
    num_pattern = re.compile(r"(\d{1,3})")
    instructions = []

    for match in matches:
        mul = match[0]
        do = match[1]
        dont = match[2]

        if mul != "":
            pairs = num_pattern.findall(mul)
            instructions.append([int(pairs[0]), int(pairs[1])])
        elif do != "":
            instructions.append(do)
        elif dont != "":
            instructions.append(dont)
        else:
            raise Exception(f"wat: {match}")

    sum = 0
    do_mult = True

    for instruction in instructions:
        if isinstance(instruction, list):
            if do_mult:
                sum += instruction[0] * instruction[1]
        elif instruction == "do()":
            do_mult = True
        elif instruction == "don't()":
            do_mult = False
        else:
            raise Exception(f"invalid instruction {instruction}")

    return str(sum)


def problem4_part1() -> str:
    pass
    # check each cell for
    # if X
    #  then check all 8 neighbors for next letter
    #   if neighbor match next letter:
    #    check its 8 neighbors for next letter
    #     keep going until find all or find end
    #   if no matches go to next cell
    # if not go to next cell
