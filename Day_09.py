from time import perf_counter

start_time = perf_counter()


def open_file(file_name: str = "Day_09.txt") -> str:
    with open(file_name) as f:
        return f.read()


def reduce_line(line: list[int]) -> list[int]:
    result = []
    for i in range(len(line) - 1):
        result.append(line[i + 1] - line[i])
    return result


def part_one(lines: list[list[int]]) -> int:
    result = 0
    for line in lines:
        derivatives_matrix = [line]
        while not all(derivative == 0 for derivative in derivatives_matrix[-1]):
            derivatives_matrix.append(reduce_line(derivatives_matrix[-1]))

        result += sum(derivatives[-1] for derivatives in derivatives_matrix)
    return result


def part_two(lines: list[list[int]]) -> int:
    result = 0
    for line in lines:
        derivatives_matrix = [line]
        while not all(derivative == 0 for derivative in derivatives_matrix[-1]):
            derivatives_matrix.append(reduce_line(derivatives_matrix[-1]))

        first_derivatives = [derivatives[0] for derivatives in derivatives_matrix]
        zeroth_column = [0] * len(first_derivatives)

        for index in range(len(zeroth_column) - 2, -1, -1):
            zeroth_column[index] = first_derivatives[index] - zeroth_column[index + 1]

        result += zeroth_column[0]
    return result


def main():
    lines = open_file().splitlines()
    lines = [list(map(int, line.split())) for line in lines]
    print("Part 1: ", part_one(lines))
    print("Part 2: ", part_two(lines))


if __name__ == "__main__":
    main()
    print("Time elapsed: ", perf_counter() - start_time)
