import re
import math

REGEX = r"(?P<source>[A-Z]+) = \((?P<L>[A-Z]+), (?P<R>[A-Z]+)\)"


def parse_line(line: str):
    match = re.search(REGEX, line)
    return match["source"], match


def get_distance(start, mappings, directions):
    distance = 0
    source = start
    while True:
        for direction in directions:
            if source.endswith("Z"):
                return distance
            distance += 1
            source = mappings[source][direction]


def solution_p1():
    lines = [l.strip() for l in open("input.txt", "r")]
    directions = lines[0]
    mappings = {}
    for line in lines[2:]:
        source, destinations = parse_line(line)
        mappings[source] = destinations

    return get_distance("AAA", mappings, directions)


def solution_p2():
    lines = [l.strip() for l in open("input.txt", "r")]
    directions = lines[0]
    mappings = {}
    sources = []
    for line in lines[2:]:
        source, destinations = parse_line(line)
        mappings[source] = destinations
        if source.endswith("A"):
            sources.append(source)

    distances = [get_distance(source, mappings, directions) for source in sources]
    return math.lcm(*distances)


if __name__ == "__main__":
    print(f"Part 1: {solution_p1()}")
    print(f"Part 2: {solution_p2()}")
