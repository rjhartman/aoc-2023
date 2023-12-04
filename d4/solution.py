import re
from typing import Tuple, Set
import time

REGEX = r"Card\s+(?P<card_number>\d)+: (?P<winning>.*) \| (?P<held>.*)"


def get_winning_numbers(card: str) -> Set[str]:
    match = re.search(REGEX, card)
    winning = set(match["winning"].strip().split(" "))
    held = set(match["held"].strip().split(" "))
    if "" in winning:
        winning.remove("")
    if "" in held:
        held.remove("")
    return winning.intersection(held)


def solution_p1():
    total = 0
    with open("input.txt", "r", encoding="utf-8") as cards:
        for card in cards:
            winning_numbers = get_winning_numbers(card)
            if not winning_numbers:
                continue
            total += 1 * 2 ** (len(winning_numbers) - 1)
    return total


def solution_p2():
    cards = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]
    copies = {k: 1 for k in range(len(cards))}
    for i, card in enumerate(cards):
        winning_numbers = get_winning_numbers(card)
        for j in range(len(winning_numbers)):
            copies[i + j + 1] += copies[i]
    return sum(copies.values())


if __name__ == "__main__":
    print(f"Part 1: {solution_p1()}")
    print(f"Part 2: {solution_p2()}")
