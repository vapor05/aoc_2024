import re

import utils


def _load_problem_3_data() -> str:
    fl = utils._problem_data_file("problem3.txt")

    with open(fl, "r") as f:
        data = f.read()

    return data


def part1(test: bool = False) -> str:
    instructions = _load_problem_3_data()
    mul_pattern = re.compile(r"(mul\(\d{1,3},\d{1,3}\))")
    matches = mul_pattern.findall(instructions)
    num_pattern = re.compile(r"(\d{1,3})")
    pairs = [num_pattern.findall(e) for e in matches]
    products = [int(p[0]) * int(p[1]) for p in pairs]
    return str(sum(products))


def part2(test: bool = False) -> str:
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
