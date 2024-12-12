
import enum
import utils


def _load_problem6_data(
    test: bool = False,
) -> tuple[list[list[str]], tuple[int, int] | None]:
    name = "problem6.txt" if not test else "test_problem6.txt"
    fl = utils._problem_data_file(name)
    data: list[list[str]] = []
    guard_pos: tuple[int, int] | None = None

    with open(fl) as f:
        for row, l in enumerate(f.readlines()):
            cols = []

            for col, c in enumerate(l.strip()):
                c = c.strip()

                if c == "^":
                    guard_pos = (row, col)

                cols.append(c)
            
            data.append(cols)

    return data, guard_pos


class GuardFacing(enum.Enum):
    UP = "up"
    RIGHT = "right"
    DOWN = "down"
    LEFT = "left"


def _turn_right(gf: GuardFacing) -> GuardFacing:
    if gf == GuardFacing.UP:
        return GuardFacing.RIGHT
    elif gf == GuardFacing.RIGHT:
        return GuardFacing.DOWN
    elif gf == GuardFacing.DOWN:
        return GuardFacing.LEFT
    
    return GuardFacing.UP


def part1(test: bool = False) -> str:
    data, guard_pos = _load_problem6_data(test)

    if guard_pos is None:
        raise Exception("no guard starting position found")

    visited: list[tuple[int, int]] = [guard_pos]
    rows = len(data)
    cols = len(data[0])
    guard_row = guard_pos[0]
    guard_col = guard_pos[1]
    guard_facing = GuardFacing.UP
    steps = 0  

    while guard_row >= 0 and guard_row < rows and guard_col >= 0 and guard_col < cols:
        steps += 1

        if guard_facing == GuardFacing.UP:
            check_row = guard_row-1
            check_col = guard_col
        elif guard_facing == GuardFacing.RIGHT:
            check_row = guard_row
            check_col = guard_col+1
        elif guard_facing == GuardFacing.DOWN:
            check_row = guard_row+1
            check_col = guard_col
        else:
            check_row = guard_row
            check_col = guard_col-1

        # check if guard has gone off grid
        if check_row < 0 or check_row >= rows or check_col < 0 or check_col >= cols:
            break

        check = data[check_row][check_col]

        if check == '#':
            guard_facing = _turn_right(guard_facing)
        else:
            guard_row = check_row
            guard_col = check_col
            visited.append((guard_row, guard_col))

        if steps > 10000:
            raise Exception("too many steps")

    return str(len(set(visited)))


def _run_guard_path(data: list[list[str]], guard_pos: tuple[int, int]) -> tuple[list[tuple[int, int, GuardFacing]], bool]:
    visited: list[tuple[int, int, GuardFacing]] = [(guard_pos[0], guard_pos[1], GuardFacing.UP)]
    rows = len(data)
    cols = len(data[0])
    guard_row = guard_pos[0]
    guard_col = guard_pos[1]
    guard_facing = GuardFacing.UP
    steps = 0

    while guard_row >= 0 and guard_row < rows and guard_col >= 0 and guard_col < cols:
        steps += 1

        if guard_facing == GuardFacing.UP:
            check_row = guard_row-1
            check_col = guard_col
        elif guard_facing == GuardFacing.RIGHT:
            check_row = guard_row
            check_col = guard_col+1
        elif guard_facing == GuardFacing.DOWN:
            check_row = guard_row+1
            check_col = guard_col
        else:
            check_row = guard_row
            check_col = guard_col-1

        # check if guard has gone off grid
        if check_row < 0 or check_row >= rows or check_col < 0 or check_col >= cols:
            return visited, False

        check = data[check_row][check_col]

        if check == '#':
            guard_facing = _turn_right(guard_facing)
        else:
            guard_row = check_row
            guard_col = check_col
            new_pos = (guard_row, guard_col, guard_facing)

            if new_pos in visited:
                return visited, True
            
            visited.append((guard_row, guard_col, guard_facing))

        if steps > 10000:
            raise Exception("too many steps")

def part2(test: bool) -> str:
    data, guard_pos = _load_problem6_data(test)

    if guard_pos is None:
        raise Exception("no guard starting position found")
    
    visited, _ = _run_guard_path(data, guard_pos)
    check_points = set([(e[0], e[1]) for e in visited])
    print(len(check_points))
    loops = 0 
    i = 0    

    for row, col in check_points:
        i+=1
        print(i, end=",", flush=True)
        replace = data[row][col]
        
        if replace == "#" or replace == "^":
            continue

        data[row][col] = "#"
        _, has_loop = _run_guard_path(data, guard_pos)

        if has_loop:
            loops += 1

        data[row][col] = replace
        
    print("")
    return str(loops)