from time import perf_counter

start_time = perf_counter()


def open_file(file_name: str = "Day_11.txt") -> str:
    with open(file_name) as f:
        return f.read()


def get_galaxies_positions(lines: list[str]) -> list[tuple[int, int]]:
    return [
        (row_index, col_index)
        for row_index, row in enumerate(lines)
        for col_index, col in enumerate(row)
        if col == "#"
    ]


def get_galaxy_distance(
    galaxy_1: tuple[int, int],
    galaxy_2: tuple[int, int],
    row_indexes: list[int],
    col_indexes: list[int],
    EXPANSION_FACTOR: int,
) -> int:
    topmost = min(galaxy_1[0], galaxy_2[0])
    bottommost = max(galaxy_1[0], galaxy_2[0])
    leftmost = min(galaxy_1[1], galaxy_2[1])
    rightmost = max(galaxy_1[1], galaxy_2[1])
    return (
        rightmost
        - leftmost
        + bottommost
        - topmost
        + (
            sum(topmost < row < bottommost for row in row_indexes)
            + sum(leftmost < col < rightmost for col in col_indexes)
        )
        * (EXPANSION_FACTOR - 1)
    )


def part_one(
    galaxies_positions: list[tuple[int, int]],
    row_indexes: list[int],
    col_indexes: list[int],
) -> int:
    return sum(
        get_galaxy_distance(galaxy_1, galaxy_2, row_indexes, col_indexes, 2)
        for index, galaxy_1 in enumerate(galaxies_positions)
        for galaxy_2 in galaxies_positions[index:]
    )


def part_two(
    galaxies_positions: list[tuple[int, int]],
    row_indexes: list[int],
    col_indexes: list[int],
) -> int:
    return sum(
        get_galaxy_distance(galaxy_1, galaxy_2, row_indexes, col_indexes, 1000000)
        for index, galaxy_1 in enumerate(galaxies_positions)
        for galaxy_2 in galaxies_positions[index:]
    )


def main():
    lines = open_file().splitlines()
    galaxies_positions = get_galaxies_positions(lines)
    row_indexes = [
        index
        for index in range(len(lines))
        if not any(char == "#" for char in lines[index])
    ]
    col_indexes = [
        index
        for index in range(len(lines[0]))
        if not any(line[index] == "#" for line in lines)
    ]
    print("Part 1: ", part_one(galaxies_positions, row_indexes, col_indexes))
    print("Part 2: ", part_two(galaxies_positions, row_indexes, col_indexes))


if __name__ == "__main__":
    main()
    print("Time elapsed: ", perf_counter() - start_time)
