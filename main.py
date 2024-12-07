import typing
import argparse
import problems

solve_funcs: dict[str, dict[str, typing.Callable[[], str]]] = {
    "1": {"1": problems.problem1_part1, "2": problems.problem1_part2},
    "2": {"1": problems.problem2_part1, "2": problems.problem2_part2},
    "3": {"1": problems.problem3_part1, "2": problems.problem3_part2},
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="aoc_2024",
        description="run solve func for specified problem",
    )
    parser.add_argument("problem")
    parser.add_argument("--part", default="1", required=False)
    args = parser.parse_args()
    print(f"Running problem {args.problem} part {args.part}...")
    solve_fns = solve_funcs.get(args.problem)

    if solve_fns is None:
        print(f"No solution function defined for problem {args.problem}")
    else:
        solve_fn = solve_fns.get(args.part)

        if solve_fn is None:
            print(
                f"No solution function defined for part {args.part} of problem {args.problem}"
            )
        else:
            solution = solve_fn()
            print(f"Solution to problem {args.problem} part {args.part} is {solution}")
