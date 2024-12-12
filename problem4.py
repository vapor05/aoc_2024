
import utils


class Letter:

    def __init__(self, char: str, row: int, col: int):
        self.char = char
        self.row = row
        self.col = col

    def __repr__(self):
        return f"{self.char} < row: {self.row}, col: {self.col} >"


def _load_problem4_data(test: bool = False) -> list[list[Letter]]:
    name = "problem4.txt" if not test else "test_problem4.txt"
    fl = utils._problem_data_file(name)
    data: list[list[str]] = []

    with open(fl) as f:
        for row, l in enumerate(f.readlines()):
            data.append([Letter(c, row, col) for col, c in enumerate(l.strip())])

    return data


def part1(test: bool = False) -> str:
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


def part2(test: bool = False) -> str:
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
