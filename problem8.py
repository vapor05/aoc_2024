import utils


def _load_problem8_data(test: bool = False) -> list[list[str]]:
    name = "problem8.txt" if not test else "test_problem8.txt"
    fl = utils._problem_data_file(name)
    data: list[list[str]] = []

    with open(fl, "r") as f:
        for l in f.readlines():
            data.append([c for c in l.strip()])

    return data


def part1(test: bool = False) -> str:
    data = _load_problem8_data(test)
    antennas: dict[str, list[tuple[int, int]]] = {}

    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if col != "." and col != "#":
                if col not in antennas:
                    antennas[col] = []

                antennas[col].append((i, j))

    rows = len(data)
    cols = len(data[0])
    antinodes: set[tuple[int, int]] = set()

    for antenna in antennas.values():
        for pos in antenna:
            positions = [e for e in antenna if e != pos]

            for other_pos in positions:
                an_row = (other_pos[0]- pos[0]) * 2
                an_col = (other_pos[1] - pos[1]) * 2
                an_row = an_row + pos[0]
                an_col = an_col + pos[1]

                if an_row >= 0 and an_row < rows and an_col >= 0 and an_col < cols:
                    antinodes.add((an_row, an_col))

    return str(len(antinodes))


def part2(test: bool = False) -> str:
    data = _load_problem8_data(test)
    antennas: dict[str, list[tuple[int, int]]] = {}

    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if col != "." and col != "#":
                if col not in antennas:
                    antennas[col] = []

                antennas[col].append((i, j))

    rows = len(data)
    cols = len(data[0])
    antinodes: set[tuple[int, int]] = set()

    for antenna in antennas.values():
        for pos in antenna:
            positions = [e for e in antenna if e != pos]
            
            for other_pos in positions:
                diff_row = (other_pos[0]- pos[0])
                diff_col = (other_pos[1] - pos[1])
                an_row = diff_row + pos[0]
                an_col = diff_col + pos[1]

                while an_row >= 0 and an_row < rows and an_col >= 0 and an_col < cols:
                    antinodes.add((an_row, an_col))
                    an_row = diff_row + an_row
                    an_col = diff_col + an_col

    return str(len(antinodes))