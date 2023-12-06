from time import perf_counter

start_time = perf_counter()


def open_file(file_name: str = "Day_8.txt") -> str:
    with open(file_name) as f:
        return f.read()


def part_one(lines: list[str]) -> int:
    pass


def part_two(lines: list[str]) -> int:
    pass


def main():
    lines = open_file().splitlines()
    print("Part 1: ", part_one(lines))
    print("Part 2: ", part_two(lines))


if __name__ == "__main__":
    main()
    print("Time elapsed: ", perf_counter() - start_time)
