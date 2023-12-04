def open_file(file_name: str = "Day_3.txt") -> str:
    with open(file_name) as f:
        return f.read()


def get_neighbors(
    row_index: int, col_index: int, row_len: int, col_len: int
) -> list[tuple[int, int]]:
    neighbors = []

    for row in (-1, 0, 1):
        for col in (-1, 0, 1):
            adj_row = row + row_index
            adj_col = col + col_index
            if (
                0 <= adj_row < row_len
                and 0 <= adj_col < col_len
                and (row, col) != (0, 0)
            ):
                neighbors.append((adj_row, adj_col))

    return neighbors


def get_adjacent_numbers_set(lines: list[str]) -> set[tuple[int, int]]:
    row_len = len(lines)
    col_len = len(lines[0])
    numbers_set = set()
    for row_index, row in enumerate(lines):
        for column_index, column in enumerate(row):
            if not column.isnumeric() and column != ".":
                neighbors = get_neighbors(row_index, column_index, row_len, col_len)
                for neighbor in neighbors:
                    neigh_row = neighbor[0]
                    neigh_col = neighbor[1]
                    if lines[neigh_row][neigh_col].isnumeric():
                        numbers_set.add(neighbor)
    return numbers_set


def complete_the_number(
    lines: list[str], point: tuple[int, int]
) -> tuple[int, set[tuple[int, int]]]:
    row = point[0]
    column = point[1]
    num_string = ""
    seen = set()

    while column >= 0 and lines[row][column].isnumeric():
        num_string = lines[row][column] + num_string
        seen.add((row, column))
        column = column - 1

    column = point[1] + 1
    while column < len(lines[0]) and lines[row][column].isnumeric():
        num_string = num_string + lines[row][column]
        seen.add((row, column))
        column = column + 1

    return int(num_string), seen


def sum_the_numbers(
    lines: list[str], adjacent_numbers_set: set[tuple[int, int]]
) -> int:
    seen = set()
    row_len = len(lines)
    col_len = len(lines[0])
    result = 0

    for row in range(row_len):
        for col in range(col_len):
            point = (row, col)
            if point in adjacent_numbers_set and point not in seen:
                num, new_seen = complete_the_number(lines, (point))
                result += num
                seen.update(new_seen)

    return result


def get_gear_powers(lines: list[str]) -> list[int]:
    row_len = len(lines)
    col_len = len(lines[0])
    numbers_list = []

    for row_index, row in enumerate(lines):
        for column_index, character in enumerate(row):
            if character == "*":
                resulting_set = set()
                total_seen = set()
                neighbors = get_neighbors(row_index, column_index, row_len, col_len)

                for neighbor in neighbors:
                    neigh_row = neighbor[0]
                    neigh_col = neighbor[1]
                    if lines[neigh_row][neigh_col].isnumeric():
                        num, seen = complete_the_number(lines, neighbor)
                        if neighbor not in total_seen:
                            resulting_set.add(num)
                        total_seen.update(seen)

                if len(resulting_set) == 2:
                    result = 1
                    for num in resulting_set:
                        result *= num
                    numbers_list.append(result)

    return numbers_list


def part_one(lines: list[str]) -> int:
    return sum_the_numbers(lines, get_adjacent_numbers_set(lines))


def part_two(lines: list[str]) -> int:
    return sum(get_gear_powers(lines))


def main():
    lines = open_file().splitlines()
    print("Part 1: ", part_one(lines))
    print("Part 2: ", part_two(lines))


if __name__ == "__main__":
    main()
