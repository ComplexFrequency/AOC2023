from time import perf_counter
from math import isqrt

start_time = perf_counter()


def open_file(file_name: str = "Day_06.txt") -> str:
    with open(file_name) as f:
        return f.read()


def get_race_times(lines: list[str]) -> list[int]:
    return list(map(int, lines[0][5:].split()))


def get_race_distances(lines: list[str]) -> list[int]:
    return list(map(int, lines[1][10:].split()))


def get_number_of_possible_times(race_time: int, record_distance: int) -> int:
    # The inequality to solve is distance < t_wait*(time - t_wait)
    # or -t_wait^2 + time*t_wait - distance > 0.
    #
    # Solution:
    # t_wait = (time +- sqrt(time^2 - 4*distance))/2
    #
    # Using isqrt completely avoids floating point arithmetic,
    # making this function faster and accurate for very large numbers.

    return max(isqrt(max(race_time**2 - 4 * record_distance, 0) + 1) - 1, 0)


def part_one(race_times: list[int], race_distances: list[int]) -> int:
    product = 1
    for time, distance in zip(race_times, race_distances):
        product *= get_number_of_possible_times(time, distance)
    return product


def part_two(race_times: list[int], race_distances: list[int]) -> int:
    second_race_time = int("".join(map(str, race_times)))
    second_race_distance = int("".join(map(str, race_distances)))
    return get_number_of_possible_times(second_race_time, second_race_distance)


def main():
    lines = open_file().splitlines()
    race_times = get_race_times(lines)
    race_distances = get_race_distances(lines)
    print("Part 1: ", part_one(race_times, race_distances))
    print("Part 2: ", part_two(race_times, race_distances))


if __name__ == "__main__":
    main()
    print("Time elapsed: ", perf_counter() - start_time)
