from time import perf_counter

start_time = perf_counter()


def open_file(file_name: str = "Day_12.txt") -> str:
    with open(file_name) as f:
        return f.read()


SOLUTIONS = {}


def dynamic_solve(row: str, rules: list[int], previous=".") -> int:
    key = row + ",".join(list(map(str, rules))) + previous
    if key in SOLUTIONS:
        return SOLUTIONS[key]

    if len(rules) == 0:
        SOLUTIONS[key] = int("#" not in row)
        return SOLUTIONS[key]

    if len(row) == 0:
        SOLUTIONS[key] = int(rules == [0])
        return SOLUTIONS[key]

    if rules and rules[0] < 0:
        SOLUTIONS[key] = 0
        return SOLUTIONS[key]

    if row[0] == "?":
        result_1 = dynamic_solve("#" + row[1:], rules[:], previous)
        result_2 = dynamic_solve("." + row[1:], rules[:], previous)
        SOLUTIONS[key] = result_1 + result_2
        return SOLUTIONS[key]

    match (previous, row[0]):
        case (".", "."):
            SOLUTIONS[key] = dynamic_solve(row[1:], rules[:], row[0])

        case (".", "#"):
            iteration_rules = rules.copy()
            iteration_rules[0] -= 1
            SOLUTIONS[key] = dynamic_solve(row[1:], iteration_rules, row[0])

        case ("#", "."):
            SOLUTIONS[key] = (rules[0] == 0) * dynamic_solve(row[1:], rules[1:], row[0])

        case ("#", "#"):
            iteration_rules = rules.copy()
            iteration_rules[0] -= 1
            SOLUTIONS[key] = dynamic_solve(row[1:], iteration_rules, row[0])

    return SOLUTIONS[key]


def part_one(lines: list[str]) -> int:
    return sum(
        dynamic_solve(row, list(map(int, rules.split(","))))
        for row, rules in map(str.split, lines)
    )


def unfold_record(record: str) -> str:
    row, rules = record.split()
    row = "?".join(([row] * 5))
    rules = ",".join(([rules] * 5))
    return row + " " + rules


def part_two(lines: list[str]) -> int:
    return sum(
        dynamic_solve(row, list(map(int, rules.split(","))))
        for row, rules in map(lambda line: str.split(line), lines)
    )


def main():
    lines = open_file().splitlines()
    print("Part 1: ", part_one(lines))
    print("Part 2: ", part_two(list(map(unfold_record, lines))))


if __name__ == "__main__":
    main()
    print("Time elapsed: ", perf_counter() - start_time)
