from time import perf_counter
from typing import Callable

start_time = perf_counter()


def open_file(file_name: str = "Day_07.txt") -> str:
    with open(file_name) as f:
        return f.read()


def is_five_of_a_kind(hand: str) -> bool:
    return len(set(hand)) == 1


def is_four_of_a_kind(hand: str) -> bool:
    return len(set(hand)) == 2 and hand.count(hand[0]) in (1, 4)


def is_full_house(hand: str) -> bool:
    return len(set(hand)) == 2 and hand.count(hand[0]) in (2, 3)


def is_three_of_a_kind(hand: str) -> bool:
    return (
        len(set(hand)) == 3
        and hand.count(hand[0]) in (1, 3)
        and hand.count(hand[1]) in (1, 3)
    )


def is_two_pairs(hand: str) -> bool:
    return (
        len(set(hand)) == 3
        and hand.count(hand[0]) in (1, 2)
        and hand.count(hand[1]) in (1, 2)
        and hand.count(hand[2]) in (1, 2)
    )


def is_one_pair(hand: str) -> bool:
    return len(set(hand)) == 4


def is_high_hand(hand: str) -> bool:
    return len(set(hand)) == 5


type_order = [
    is_five_of_a_kind,
    is_four_of_a_kind,
    is_full_house,
    is_three_of_a_kind,
    is_two_pairs,
    is_one_pair,
    is_high_hand,
]

card_to_value_map = {
    "A": 15,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "1": 1,
}


def get_hand_value(hand: str) -> int:
    return (
        card_to_value_map[hand[0]] * 16**4
        + card_to_value_map[hand[1]] * 16**3
        + card_to_value_map[hand[2]] * 16**2
        + card_to_value_map[hand[3]] * 16
        + card_to_value_map[hand[4]]
    )


def get_hand_rank(hand: str) -> int:
    for index, function in enumerate(type_order):
        if function(hand):
            return (7 - index) * 16**5


def get_line_fitness(line: str) -> int:
    hand = line[:5]
    return get_hand_rank(hand) + get_hand_value(line)


def get_line_fitness_p2(line: str) -> int:
    hand = line[:5].replace("J", "1")

    if "1" in hand:
        max_fitness = 0

        for card in card_to_value_map:
            modified_hand = hand.replace("1", card)
            hand_fitness = get_hand_rank(modified_hand) + get_hand_value(hand)
            max_fitness = max(max_fitness, hand_fitness)

        return max_fitness

    return get_line_fitness(hand)


def part_one(lines: list[str]) -> int:
    return sum(
        index * int(line.split()[1])
        for index, line in enumerate(sorted(lines, key=get_line_fitness), start=1)
    )


def part_two(lines: list[str]) -> int:
    return sum(
        index * int(line.split()[1])
        for index, line in enumerate(sorted(lines, key=get_line_fitness_p2), start=1)
    )


def main():
    lines = open_file().splitlines()
    print("Part 1: ", part_one(lines))
    print("Part 2: ", part_two(lines))


if __name__ == "__main__":
    main()
    print("Time elapsed: ", perf_counter() - start_time)
