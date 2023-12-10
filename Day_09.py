from time import perf_counter

start_time = perf_counter()


def open_file(file_name: str = "Day_09.txt") -> str:
    with open(file_name) as f:
        return f.read()


def differences(line: list[int]) -> list[int]:
    return [line[i + 1] - line[i] for i in range(len(line) - 1)]


def extrapolate(line: list[int]) -> list[int]:
    if all(x == 0 for x in line):
        return 0
    return line[-1] + extrapolate(differences(line))


def part_one(lines: list[list[int]]) -> int:
    return sum(extrapolate(line) for line in lines)


def part_two(lines: list[list[int]]) -> int:
    return sum(extrapolate(line[::-1]) for line in lines)


def main():
    lines = open_file().splitlines()
    lines = [list(map(int, line.split())) for line in lines]
    print("Part 1: ", part_one(lines))
    print("Part 2: ", part_two(lines))


if __name__ == "__main__":
    main()
    print("Time elapsed: ", perf_counter() - start_time)
