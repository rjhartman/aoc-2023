from functools import cmp_to_key


def parse_hand(hand: str):
    values = hand.split(" ")
    values[1] = int(values[1])
    return values


def get_rank(hand):
    seen = {"W": 0}
    for card in hand:
        if card in seen:
            seen[card] += 1
        else:
            seen[card] = 1

    num_jokers = seen["W"]
    del seen["W"]
    counts = list(sorted(seen.values()))
    score = ((counts[-1] if len(counts) > 0 else 0) + num_jokers) * 2
    if len(counts) > 1:
        score += counts[-2]
    return score


CARDS = ["W"] + [str(x) for x in list(range(2, 10))] + ["T", "J", "Q", "K", "A"]


def comparator(a, b):
    hand_a = parse_hand(a)[0]
    hand_b = parse_hand(b)[0]
    rank_a = get_rank(hand_a)
    rank_b = get_rank(hand_b)
    if rank_a > rank_b:
        return 1
    if rank_a < rank_b:
        return -1

    for card_a, card_b in (
        (CARDS.index(x), CARDS.index(y)) for x, y in zip(hand_a, hand_b)
    ):
        if card_a > card_b:
            return 1
        if card_a < card_b:
            return -1


cmp = cmp_to_key(comparator)


def solve(lines):
    lines.sort(key=cmp)
    total = 0
    for i, line in enumerate(lines):
        _, bid = parse_hand(line)
        total += (i + 1) * bid
    return total


def solution_p1():
    lines = [l.strip() for l in open("input.txt", "r")]
    return solve(lines)


def solution_p2():
    lines = (l.strip() for l in open("input.txt", "r"))
    lines = [l.replace("J", "W") for l in lines]
    return solve(lines)


if __name__ == "__main__":
    print(f"Part 1: {solution_p1()}")
    print(f"Part 2: {solution_p2()}")
