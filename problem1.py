import utils


def _load_problem_one_data() -> tuple[list[int], list[int]]:
    fl = utils._problem_data_file("problem1.txt")
    ll: list[int] = []
    rl: list[int] = []

    with open(fl, "r") as f:
        for l in f.readlines():
            nums = l.strip().split()
            ll.append(int(nums[0]))
            rl.append(int(nums[1]))

    return ll, rl


def part1(test: bool = False) -> str:
    ll, rl = _load_problem_one_data()

    ll.sort()
    rl.sort()

    dists = [abs(l - r) for l, r in zip(ll, rl)]
    return str(sum(dists))


def part2(test: bool = False) -> str:
    ll, rl = _load_problem_one_data()
    mult_map: dict[int, int] = {}

    for r in rl:
        if r not in mult_map:
            mult_map[r] = 1
        else:
            mult_map[r] += 1

    products = [l * mult_map.get(l, 0) for l in ll]
    return str(sum(products))
