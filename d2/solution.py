import re
from typing import List, Iterable, Tuple
from functools import reduce

REGEX = r"Game (?P<id>\d+): (?P<list>.*)"
COLOR_LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def parse_line(line: str) -> Tuple[str, Iterable[List[str]]]:
    match = re.search(REGEX, line)
    return match["id"], (s.split(", ") for s in match["list"].split("; "))


def is_valid_set(s: List[str]) -> bool:
    for cubes in s:
        num, color = cubes.split(" ")
        if int(num) > COLOR_LIMITS[color]:
            return False
    return True


def solution_p1() -> int:
    total = 0
    for line in open("input.txt", "r", encoding="utf-8"):
        id, sets = parse_line(line)
        for s in sets:
            if not is_valid_set(s):
                break
        else:
            total += int(id)
    return total


def solution_p2() -> int:
    total = 0
    for line in open("input.txt", "r", encoding="utf-8"):
        maxes = {c: 0 for c in ["red", "green", "blue"]}
        _, sets = parse_line(line)
        for s in sets:
            for cubes in s:
                num, color = cubes.split(" ")
                maxes[color] = max(maxes[color], int(num))
        total += reduce(lambda x, y: x * y, maxes.values())
    return total


if __name__ == "__main__":
    print(f"Part 1: {solution_p1()}")
    print(f"Part 2: {solution_p2()}")
