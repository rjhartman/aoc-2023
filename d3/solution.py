from typing import Tuple, List
from functools import reduce

DIGITS = set(range(10))


def is_symbol(char: str) -> bool:
    return not (char.isdigit() or char == ".")


def get_number(line: str, start: int) -> Tuple[int, int]:
    number = line[start]
    begin = start
    i = start - 1
    while i >= 0 and (c := line[i]).isdigit():
        number = c + number
        begin = i
        i -= 1

    j = start + 1
    while j < len(line) and (c := line[j]).isdigit():
        number += c
        j += 1

    return int(number), begin


def get_surrounding_coordinates(x: int, y: int) -> List[Tuple[int, int]]:
    coords = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if not (i == x and j == y):
                coords.append((i, j))
    return coords


def solution_p1():
    numbers = {}
    lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if is_symbol(c):
                # These can never be out of bounds because the input data is nice to us.
                for i, j in get_surrounding_coordinates(x, y):
                    if lines[j][i].isdigit():
                        number, start = get_number(lines[j], i)
                        numbers[(start, j)] = number
    return sum(numbers.values())


def solution_p2():
    lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]
    total = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "*":
                numbers = {}
                for i, j in get_surrounding_coordinates(x, y):
                    if lines[j][i].isdigit():
                        number, start = get_number(lines[j], i)
                        numbers[(start, j)] = number
                if len(numbers) == 2:
                    total += reduce(lambda x, y: x * y, numbers.values())
    return total


if __name__ == "__main__":
    print(f"Part 1: {solution_p1()}")
    print(f"Part 2: {solution_p2()}")
