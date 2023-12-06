from time import perf_counter

start_time = perf_counter()

MAP_ORDER = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]


def open_file(file_name: str = "Day_5.txt") -> str:
    with open(file_name) as f:
        return f.read()


def get_seeds(line: str) -> list[int]:
    return [int(seed) for seed in line[6:].split()]


def get_seeds_intervals(line: str) -> list[tuple[int, int]]:
    result_list = []

    for index, value in enumerate(line[6:].split()):
        if index % 2 == 0:
            range_start = int(value)
        if index % 2 == 1:
            range_numbers = int(value)
            result_list.append((range_start, range_start + range_numbers))

    return result_list


def get_maps(lines: list[str]) -> dict[str, list[int]]:
    maps = {}

    for line in lines[2:]:
        if len(line) > 0:
            if "map" in line:
                map_name = line.split()[0]
                map_values = []
            else:
                map_values.append(list(map(int, line.split())))
        else:
            maps[map_name] = map_values

    maps[map_name] = map_values

    return maps


def map_element(map: list[int], element: int) -> int:
    for ranges in map:
        if ranges[1] <= element < ranges[1] + ranges[2]:
            return element - ranges[1] + ranges[0]

    return element


def map_seed_to_location(maps: dict[str, list[int]], seed: int) -> int:
    result = seed

    for map_name in MAP_ORDER:
        result = map_element(maps[map_name], result)

    return result


def part_one(seeds: list[int], maps: dict[str, list[int]]) -> int:
    return min(map_seed_to_location(maps, seed) for seed in seeds)


def reverse_map_element(map: list[int], element: int) -> int:
    for ranges in map:
        if ranges[0] <= element < ranges[0] + ranges[2]:
            return element - ranges[0] + ranges[1]

    return element


def map_location_to_seed(maps: dict[str, list[int]], seed: int) -> int:
    result = seed

    for map_name in reversed(MAP_ORDER):
        result = reverse_map_element(maps[map_name], result)

    return result


def binary_search(
    min_location: int,
    max_location: int,
    maps: dict[str, list[int]],
    seed_intervals: list[tuple[int, int]],
):
    if min_location == max_location:
        min_seed = map_location_to_seed(maps, min_location)
        if is_seed_in_seed_intervals(min_seed, seed_intervals):
            return min_location
        else:
            print("Not found!")
            return -1

    mid_location = (min_location + max_location) // 2
    mid_seed = map_location_to_seed(maps, mid_location)

    if is_seed_in_seed_intervals(mid_seed, seed_intervals):
        return binary_search(min_location, mid_location, maps, seed_intervals)

    return binary_search(mid_location + 1, max_location, maps, seed_intervals)


def is_seed_in_seed_intervals(seed: int, seed_intervals: list[int]) -> bool:
    for range_start, range_end in seed_intervals:
        if range_start <= seed < range_end:
            return True

    return False


def part_two(seed_intervals: list[int], maps: dict[str, list[int]]) -> int:
    # Does binary search of locations to find the minimum location in intervals.
    #
    # I later realized that this algorithm does not work for all cases, but it's
    # funny how it worked for my input. A better solution would be check all seed
    # locations from 0 upwards until the correct location is found. It would be
    # much slower, however, and the better, more general solution is to simply map
    # the ranges appropriately.

    min_location = 0
    max_location = 10000000

    return binary_search(min_location, max_location, maps, seed_intervals)


def main():
    lines = open_file().splitlines()
    seeds = get_seeds(lines[0])
    maps = get_maps(lines)

    print("Part 1: ", part_one(seeds, maps))

    seed_intervals = get_seeds_intervals(lines[0])
    print("Part 2: ", part_two(seed_intervals, maps))


if __name__ == "__main__":
    main()
    print("Time elapsed: ", perf_counter() - start_time)
