import functools

import utils


def _load_problem5_data(
    test: bool = False,
) -> tuple[dict[int, set[int]], list[list[int]]]:
    name = "problem5.txt" if not test else "test_problem5.txt"
    fl = utils._problem_data_file(name)
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


def part1(test: bool = False) -> str:
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

    mid_points = [vu[int(len(vu) / 2)] for vu in valid_updates]
    return str(sum(mid_points))


def part2(test: bool = False) -> str:
    rules, updates = _load_problem5_data(test)
    corrected_updates: list[list[int]] = []
    invalid = []

    def _sort(a, b) -> int:
        a_rules = rules.get(a)

        if a_rules is None:
            return 0

        if b in a_rules:
            return -1
        else:
            return 1

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
        corrected_updates.append(sorted(update, key=functools.cmp_to_key(_sort)))

    mid_points = [vu[int(len(vu) / 2)] for vu in corrected_updates]
    return str(sum(mid_points))
