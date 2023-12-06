from functools import reduce


def parse_line(line: str):
    return [int(x) for x in filter(None, line.split(":", maxsplit=1)[1].split(" "))]


def solution_p1():
    lines = [l.strip() for l in open("input.txt", "r")]
    times = parse_line(lines[0])
    distances = parse_line(lines[1])

    total = 1
    for time, distance in zip(times, distances):
        valid_times = []
        for i in range(0, time + 1):
            if (time - i) * i > distance:
                valid_times.append(i)
        total *= len(valid_times)
    return total


def total_line(line: str) -> int:
    return int("".join(filter(None, line.split(":", maxsplit=1)[1].split(" "))))


def solution_p2():
    lines = [l.strip() for l in open("input.txt", "r")]
    time = total_line(lines[0])
    distance = total_line(lines[1])
    total = 0
    for i in range(0, time + 1):
        if (time - i) * i > distance:
            total += 1
    return total


if __name__ == "__main__":
    print(f"Part 1: {solution_p1()}")
    print(f"Part 2: {solution_p2()}")
