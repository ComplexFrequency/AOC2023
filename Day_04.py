from time import perf_counter

start_time = perf_counter()


def open_file(file_name: str = "Day_04.txt") -> str:
    with open(file_name) as f:
        return f.read()


def get_game_value(line: str) -> int:
    winning_numbers = get_winning_numbers(line)
    return 2 ** (winning_numbers - 1) if winning_numbers else 0


def get_winning_numbers(line: str) -> int:
    game = line.replace("  ", " ").split(" | ")
    rules = list(map(int, game[0].split(": ")[1].split(" ")))
    cards = list(map(int, game[1].split(" ")))
    return sum(1 if card in rules else 0 for card in cards)


def part_one(lines: list[str]) -> int:
    return sum(get_game_value(line) for line in lines)


def part_two(lines: list[str]) -> int:
    number_of_cards = [1] * 209

    for game, line in enumerate(lines):
        winning_numbers = get_winning_numbers(line)
        i = game
        while winning_numbers > 0:
            i = i + 1
            number_of_cards[i] = number_of_cards[i] + number_of_cards[game]
            winning_numbers = winning_numbers - 1

    return sum(number_of_cards)


def main():
    lines = open_file().splitlines()

    print("Part 1: ", part_one(lines))
    print("Part 2: ", part_two(lines))


if __name__ == "__main__":
    main()
    print("Time elapsed: ", perf_counter() - start_time)
