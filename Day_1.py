from time import perf_counter

start_time = perf_counter()

NUMBERS_LIST = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def open_file(file_name="Day_1.txt"):
    with open(file_name) as f:
        return f.read()


def get_first_n(line: str, part_two: bool = False) -> int:
    for index, character in enumerate(line):
        if character.isnumeric():
            return int(character)

        if part_two:
            for i, spelled_number in enumerate(NUMBERS_LIST):
                if line[index:].startswith(spelled_number):
                    return i + 1


def get_last_n(line: str, part_two: bool = False) -> int:
    for index, character in enumerate(line[::-1]):
        if character.isnumeric():
            return int(character)

        if part_two:
            for i, spelled_number in enumerate(NUMBERS_LIST):
                if line[: len(line) - index].endswith(spelled_number):
                    return i + 1


def main():
    input_str = open_file()
    result_1, result_2 = 0, 0
    for line in input_str.splitlines():
        result_1 += 10 * get_first_n(line) + get_last_n(line)
        result_2 += 10 * get_first_n(line, True) + get_last_n(line, True)

    print("Part 1: ", result_1)
    print("Part 2: ", result_2)


if __name__ == "__main__":
    main()
    print("Time elapsed: ", perf_counter() - start_time)
