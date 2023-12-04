LIMITS = {"red": 12, "green": 13, "blue": 14}


def open_file(file_name: str = "Day_2.txt") -> str:
    with open(file_name) as f:
        return f.read()


def get_game(line: str) -> list[str]:
    line_split = line.split(": ")
    return line_split[1].split("; ")


def is_round_possible(round: str) -> bool:
    result_dict = get_round_dict(round)

    for color in LIMITS:
        if result_dict[color] > LIMITS[color]:
            return False

    return True


def get_round_dict(round: str) -> dict[str, int]:
    result_dictionary = {"red": 0, "green": 0, "blue": 0}

    for colors in round.split(", "):
        for color in result_dictionary:
            if color in colors:
                result_dictionary[color] = int(colors.split(" ")[0])

    return result_dictionary


def get_game_value(game_number: int, game: list[str]) -> int:
    is_game_possible = all(is_round_possible(round) for round in game)
    return game_number * is_game_possible


def get_game_power(game: list[str]) -> int:
    min_blocks = {"red": 0, "green": 0, "blue": 0}

    for round in game:
        round_dict = get_round_dict(round)
        for color in min_blocks:
            min_blocks[color] = max(round_dict[color], min_blocks[color])

    return min_blocks["red"] * min_blocks["green"] * min_blocks["blue"]


def part_one(games_list: list[str]) -> int:
    return sum(
        get_game_value(game_number + 1, get_game(line))
        for game_number, line in enumerate(games_list)
    )


def part_two(games_list: list[str]) -> int:
    return sum(get_game_power(get_game(line)) for line in games_list)


def main():
    games_list = open_file().splitlines()

    print("Part 1: ", part_one(games_list))
    print("Part 2: ", part_two(games_list))


if __name__ == "__main__":
    main()
