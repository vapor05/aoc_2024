import importlib
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="aoc_2024",
        description="run solve func for specified problem",
    )
    parser.add_argument("problem")
    parser.add_argument("--part", default="1", required=False)
    parser.add_argument("--test", action="store_true", required=False)
    args = parser.parse_args()
    print(f"Running problem {args.problem} part {args.part}...")
    problems = importlib.import_module(f"problem{args.problem}")

    try:
        solve_fn = getattr(problems, f"part{args.part}")
        solution = solve_fn(test=args.test)
        print(f"Solution to problem {args.problem} part {args.part} is {solution}")
    except AttributeError as ex:
        print(
            f"No solution function defined for part {args.part} of problem {args.problem}"
        )

    
