from time import perf_counter

start_time = perf_counter()


def open_file(file_name: str = "Day_08.txt") -> str:
    with open(file_name) as f:
        return f.read()


def populate_graph(lines: list[str]) -> dict[str, dict[str, str]]:
    graph = {}
    for line in lines:
        graph[line[0:3]] = {"L": line[7:10], "R": line[12:15]}

    return graph


def part_one(graph, order) -> int:
    current_node = "AAA"
    result = 0

    while current_node != "ZZZ":
        step = result % len(order)
        current_node = graph[current_node][order[step]]
        result += 1

    return result


def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b

    return a


def least_common_multiple(numbers_list: list[int]) -> int:
    result = numbers_list[0]

    for i in numbers_list[1:]:
        result = result * i // greatest_common_divisor(result, i)

    return result


def part_two(starting_nodes, graph, order) -> int:
    results = []

    for current_node in starting_nodes:
        result = 0
        while current_node[2] != "Z":
            step = result % len(order)
            current_node = graph[current_node][order[step]]
            result += 1
        results.append(result)

    return least_common_multiple(results)


def main():
    lines = open_file().splitlines()
    graph = populate_graph(lines[2:])
    order = lines[0]
    print("Part 1: ", part_one(graph, order))

    starting_nodes = (key for key in graph.keys() if key[2] == "A")
    print("Part 2: ", part_two(starting_nodes, graph, order))


if __name__ == "__main__":
    main()
    print("Time elapsed: ", perf_counter() - start_time)
