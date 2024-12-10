import functools
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


def problem1_part1(test: bool = False) -> str:
    ll, rl = _load_problem_one_data()

    ll.sort()
    rl.sort()

    dists = [abs(l - r) for l, r in zip(ll, rl)]
    return str(sum(dists))


def problem1_part2(test: bool = False) -> str:
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


def problem2_part1(test: bool = False) -> str:
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


def problem2_part2(test: bool = False) -> str:
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


def problem3_part1(test: bool = False) -> str:
    instructions = _load_problem_3_data()
    mul_pattern = re.compile(r"(mul\(\d{1,3},\d{1,3}\))")
    matches = mul_pattern.findall(instructions)
    num_pattern = re.compile(r"(\d{1,3})")
    pairs = [num_pattern.findall(e) for e in matches]
    products = [int(p[0]) * int(p[1]) for p in pairs]
    return str(sum(products))


def problem3_part2(test: bool = False) -> str:
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


class Letter:

    def __init__(self, char: str, row: int, col: int):
        self.char = char
        self.row = row
        self.col = col

    def __repr__(self):
        return f"{self.char} < row: {self.row}, col: {self.col} >"


def _load_problem4_data(test: bool = False) -> list[list[Letter]]:
    name = "problem4.txt" if not test else "test_problem4.txt"
    fl = _problem_data_file(name)
    data: list[list[str]] = []

    with open(fl) as f:
        for row, l in enumerate(f.readlines()):
            data.append([Letter(c, row, col) for col, c in enumerate(l.strip())])

    return data


def problem4_part1(test: bool = False) -> str:
    match: dict[str, str] = {"M": "A", "A": "S", "S": None}
    data = _load_problem4_data(test)
    rows = len(data)
    finds = 0

    for i, row in enumerate(data):
        cols = len(row)

        for j, letter in enumerate(row):
            if letter.char != "X":
                continue

            check_list: list[Letter] = []
            has_previous_row = i != 0
            has_next_row = i + 1 < rows
            has_previous_col = j != 0
            has_next_col = j + 1 < cols

            if has_previous_row:
                previous = data[i - 1]

                if has_previous_col:
                    check_list.append(previous[j - 1])

                check_list.append(previous[j])

                if has_next_col:
                    check_list.append(previous[j + 1])

            if has_previous_col:
                check_list.append(row[j - 1])

            if has_next_col:
                check_list.append(row[j + 1])

            if has_next_row:
                next = data[i + 1]

                if has_previous_col:
                    check_list.append(next[j - 1])

                check_list.append(next[j])

                if has_next_col:
                    check_list.append(next[j + 1])

            want = "M"
            letter_want = "M"

            while len(check_list) > 0:
                check = check_list.pop(0)

                if want == check.char:
                    want = match.get(check.char)

                    if want is None:
                        finds += 1
                        want = letter_want
                        continue

                    if letter.row < check.row:
                        if check.row + 1 < rows:
                            r = data[check.row + 1]
                        else:
                            r = None
                    elif letter.row == check.row:
                        r = row
                    else:
                        if check.row != 0:
                            r = data[check.row - 1]
                        else:
                            r = None

                    if r is not None:
                        if letter.col < check.col:
                            if check.col + 1 < cols:
                                check_list.insert(0, r[check.col + 1])
                        elif letter.col == check.col:
                            check_list.insert(0, r[check.col])
                        else:
                            if check.col != 0:
                                check_list.insert(0, r[check.col - 1])
                else:
                    want = letter_want

    return str(finds)


def problem4_part2(test: bool = False) -> str:
    data = _load_problem4_data(test)
    rows = len(data)
    finds = 0

    for i in range(1, rows - 1):
        row = data[i]
        cols = len(row)

        for j in range(1, cols - 1):
            letter = row[j]

            if letter.char == "A":
                top_left = data[letter.row - 1][letter.col - 1]
                top_right = data[letter.row - 1][letter.col + 1]
                bottom_left = data[letter.row + 1][letter.col - 1]
                bottom_right = data[letter.row + 1][letter.col + 1]

                if top_left.char == "M":
                    left_reverse = False
                elif top_left.char == "S":
                    left_reverse = True
                else:
                    continue

                if top_right.char == "M":
                    right_reverse = False
                elif top_right.char == "S":
                    right_reverse = True
                else:
                    continue

                if (
                    (left_reverse and bottom_right.char == "M")
                    or (not left_reverse and bottom_right.char == "S")
                ) and (
                    (right_reverse and bottom_left.char == "M")
                    or (not right_reverse and bottom_left.char == "S")
                ):
                    finds += 1

    return str(finds)


def _load_problem5_data(test: bool = False) -> tuple[dict[int, set[int]], list[list[int]]]:
    name = "problem5.txt" if not test else "test_problem5.txt"
    fl = _problem_data_file(name)
    rules: dict[int, set[int]] = {}
    updates: list[list[int]] = []

    with open(fl) as f:
        for line in f.readlines():
            if "|" in line:
                nums = line.strip().split("|")
                key = int(nums[0])
                value = int(nums[1])
                
                if key not in rules:
                    rules[key] = set()

                rules[key].add(value)

            elif "," in line:
                updates.append([int(n) for n in line.strip().split(",")])

    return rules, updates


def problem5_part1(test: bool = False) -> str:
    rules, updates = _load_problem5_data(test)
    valid_updates: list[list[int]] = []

    for update in updates:
        search = {n: i for i, n in enumerate(update)}
    
        for i, n in enumerate(update):
            if n not in rules:
                continue

            n_rules = rules[n]
            fail_rules = False

            for rule in n_rules:
                if rule not in search:
                    continue

                check_i = search[rule]
                
                if i >= check_i:
                    fail_rules = True
                    break

            if fail_rules:
                break

        if not fail_rules:
            valid_updates.append(update)

    mid_points = [vu[int(len(vu)/2)] for vu in valid_updates]
    return str(sum(mid_points))


def problem5_part2(test: bool = False) -> str:
    rules, updates = _load_problem5_data(test)
    corrected_updates: list[list[int]] = []
    invalid=[]

    for update in updates:
        search = {n: i for i, n in enumerate(update)}
    
        for i, n in enumerate(update):
            if n not in rules:
                continue

            n_rules = rules[n]
            fail_rules = False

            for rule in n_rules:
                if rule not in search:
                    continue

                check_i = search[rule]
                
                if i >= check_i:
                    fail_rules = True
                    break

            if fail_rules:
                break

        if not fail_rules:
            continue
        
        invalid.append(update)
        def _sort(a, b) -> int:
            a_rules = rules.get(a)

            if a_rules is None:
                return 0
            
            if b in a_rules:
                return -1
            else:
                return 1
        
        corrected_updates.append(sorted(update, key=functools.cmp_to_key(_sort)))

    mid_points = [vu[int(len(vu)/2)] for vu in corrected_updates]
    return str(sum(mid_points))




