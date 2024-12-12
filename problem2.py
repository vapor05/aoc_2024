import utils


def _load_problem_2_data() -> list[list[int]]:
    fl = utils._problem_data_file("problem2.txt")
    reports: list[list[int]] = []

    with open(fl, "r") as f:
        for l in f.readlines():
            levels = [int(e) for e in l.strip().split()]
            reports.append(levels)

    return reports


def part1(test: bool = False) -> str:
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


def part2(test: bool = False) -> str:
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