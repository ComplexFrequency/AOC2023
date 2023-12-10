from time import perf_counter

start_time = perf_counter()


NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)

DIRECTIONAL_MAP = {
    "|": {
        NORTH: NORTH,
        SOUTH: SOUTH,
    },
    "-": {
        EAST: EAST,
        WEST: WEST,
    },
    "L": {
        SOUTH: EAST,
        WEST: NORTH,
    },
    "J": {
        SOUTH: WEST,
        EAST: NORTH,
    },
    "7": {
        NORTH: WEST,
        EAST: SOUTH,
    },
    "F": {
        NORTH: EAST,
        WEST: SOUTH,
    },
}


def open_file(file_name: str = "Day_10.txt") -> str:
    with open(file_name) as f:
        return f.read()


def get_starting_point(lines: list[str]) -> tuple[int, int]:
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char == "S":
                return x, y


def add_tuples(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (a[0] + b[0], a[1] + b[1])


def get_next_direction(
    lines: list[str], current_point: tuple[int, int], current_direction: tuple[int, int]
) -> tuple[int, int]:
    character = lines[current_point[0]][current_point[1]]
    return DIRECTIONAL_MAP[character][current_direction]


def find_border_length(lines: list[str], starting_point: tuple[int, int]) -> int:
    current_direction = NORTH
    current_point = starting_point
    length = 0
    while True:
        current_point = add_tuples(current_point, current_direction)
        length += 1

        if current_point == starting_point:
            break

        current_direction = get_next_direction(lines, current_point, current_direction)

    return length


def part_one(lines: list[str], starting_point: tuple[int, int]) -> int:
    return find_border_length(lines, starting_point) // 2


def get_border_matrix(
    lines: list[str], starting_point: tuple[int, int]
) -> list[list[bool]]:
    current_direction = NORTH
    current_point = starting_point
    matrix = [[False for col in range(len(lines[0]))] for row in range(len(lines))]

    while True:
        current_point = add_tuples(current_point, current_direction)
        matrix[current_point[0]][current_point[1]] = True
        if current_point == starting_point:
            break

        current_direction = get_next_direction(lines, current_point, current_direction)

    return matrix


def get_number_of_border_crossings(
    lines: list[str],
    border_matrix: list[list[bool]],
    x: int,
    y: int,
) -> int:
    current_x = x
    number_of_crossings = 0
    while current_x >= 0:
        current_x -= 1
        if not border_matrix[current_x][y]:
            continue

        match lines[current_x][y]:
            case "-":
                number_of_crossings += 1

            case "L" | "J":
                entering_pipe = lines[current_x][y]
                current_x -= 1

                while lines[current_x][y] == "|":
                    current_x -= 1

                exiting_pipe = lines[current_x][y]
                if (entering_pipe, exiting_pipe) in (("L", "7"), ("J", "F")):
                    number_of_crossings += 1

    return number_of_crossings


def part_two(lines: list[str], border_matrix: list[list[bool]]) -> int:
    result = 0
    for x in range(1, len(lines) - 1):
        for y in range(1, len(lines[0]) - 1):
            if not border_matrix[x][y]:
                result += get_number_of_border_crossings(lines, border_matrix, x, y) % 2

    return result


def main():
    lines = open_file().splitlines()
    starting_point = get_starting_point(lines)
    print("Part 1: ", part_one(lines, starting_point))

    lines[starting_point[0]] = lines[starting_point[0]].replace("S", "|")
    border_matrix = get_border_matrix(lines, starting_point)
    print("Part 2: ", part_two(lines, border_matrix))


if __name__ == "__main__":
    main()
    print("Time elapsed: ", perf_counter() - start_time)
