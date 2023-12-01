from typing import Optional


def get_integer(char: str) -> Optional[int]:
    try:
        return int(char)
    except ValueError:
        return None


def solution_p1() -> int:
    total = 0
    for line in open("input.txt", "r", encoding="utf-8"):
        first = next(c for c in map(get_integer, line) if c is not None)
        last = next(c for c in map(get_integer, reversed(line)) if c is not None)
        total += first * 10 + last
    return total


NUMBER_SPELLINGS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def find_number(line: str, reverse: bool) -> int:
    window = ""
    spellings = NUMBER_SPELLINGS[:]
    for c in reversed(line) if reverse else line:
        if (parsed := get_integer(c)) is not None:
            return parsed

        window = c + window if reverse else window + c
        spellings = [
            s for s in spellings if (s.endswith if reverse else s.startswith)(window)
        ]
        if len(spellings) == 1 and spellings[0] == window:
            return NUMBER_SPELLINGS.index(window) + 1

        if not spellings:
            spellings = NUMBER_SPELLINGS[:]
            while window := window[:-1] if reverse else window[1:]:
                if any(
                    (
                        (s.endswith if reverse else s.startswith)(window)
                        for s in NUMBER_SPELLINGS
                    )
                ):
                    break
            else:
                window = c


def solution_p2() -> int:
    total = 0
    for line in open("input.txt", "r", encoding="utf-8"):
        first = find_number(line, False)
        last = find_number(line, True)
        total += first * 10 + last
    return total


if __name__ == "__main__":
    print(f"Part 1 Answer: {solution_p1()}")
    print(f"Part 2 Answer: {solution_p2()}")
