from time import perf_counter
from math import sqrt, floor, ceil, prod

start_time = perf_counter()


def open_file(file_name: str = "Day_6.txt") -> str:
    with open(file_name) as f:
        return f.read()


def get_race_times(lines: list[str]) -> list[int]:
    return list(map(int, lines[0][5:].split()))


def get_race_distances(lines: list[str]) -> list[int]:
    return list(map(int, lines[1][10:].split()))


def get_number_of_possible_times(race_time: int, record_distance: int) -> int:
    # equation is distance < t_wait*(time - t_wait)
    # -t_wait^2 + time*t_wait - distance > 0.1
    # t_wait = (-time +- sqrt(time^2 - 4*(-distance)))/2
    delta = sqrt(max(race_time**2 - 4 * record_distance, 0))
    p1 = (race_time - delta) / 2
    p2 = (race_time + delta) / 2
    return max(ceil(p2) - floor(p1) - 1, 0)


def part_one(race_times: list[int], race_distances: list[int]) -> int:
    return prod(
        get_number_of_possible_times(time, distance)
        for time, distance in zip(race_times, race_distances)
    )


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
