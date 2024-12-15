#!/usr/bin/env python3


def parse_letters(filename):
    with open(filename) as f:
        return [list(line.strip()) for line in f]


def extract_strings(letters):
    max_y, max_x = len(letters), len(letters[0])
    strings = []

    # Rows and reversed rows
    strings.extend("".join(row) for row in letters)
    strings.extend("".join(row[::-1]) for row in letters)

    # Columns and reversed columns
    for x in range(max_x):
        column = [letters[y][x] for y in range(max_y)]
        strings.append("".join(column))
        strings.append("".join(column[::-1]))

    # Diagonals (Top-Left to Bottom-Right)
    for diag_start in range(-(max_y - 1), max_x):
        diagonal = [
            letters[y][diag_start + y]
            for y in range(max_y)
            if 0 <= diag_start + y < max_x
        ]
        if diagonal:
            strings.append("".join(diagonal))
            strings.append("".join(diagonal[::-1]))

    # Diagonals (Top-Right to Bottom-Left)
    for diag_start in range(max_x + max_y - 1):
        diagonal = [
            letters[y][diag_start - y]
            for y in range(max_y)
            if 0 <= diag_start - y < max_x
        ]
        if diagonal:
            strings.append("".join(diagonal))
            strings.append("".join(diagonal[::-1]))

    return strings


def count_xmas_words(letters):
    strings = extract_strings(letters)
    return sum(string.count("XMAS") for string in strings)


def get_surroundings(letters, x, y):
    max_y, max_x = len(letters), len(letters[0])

    if x == 0 or y == 0 or x == max_x - 1 or y == max_y - 1:
        return None

    return [
        letters[y - 1][x - 1 : x + 2],
        letters[y][x - 1 : x + 2],
        letters[y + 1][x - 1 : x + 2],
    ]


def check_mas_cross(surroundings):
    patterns = [
        [["M", None, "S"], [None, "A", None], ["M", None, "S"]],
        [["S", None, "M"], [None, "A", None], ["S", None, "M"]],
        [["M", None, "M"], [None, "A", None], ["S", None, "S"]],
        [["S", None, "S"], [None, "A", None], ["M", None, "M"]],
        [["S", None, "S"], [None, "A", None], ["M", None, "M"]],
        [["M", None, "S"], [None, "A", None], ["M", None, "S"]],
        [["S", None, "M"], [None, "A", None], ["S", None, "M"]],
    ]

    def matches_pattern(surroundings, pattern):
        for y in range(3):
            for x in range(3):
                if pattern[y][x] is not None and surroundings[y][x] != pattern[y][x]:
                    return False
        return True

    return any(matches_pattern(surroundings, pattern) for pattern in patterns)


def count_xmas_cross(letters):
    max_y, max_x = len(letters), len(letters[0])
    count = 0

    for y in range(max_y):
        for x in range(max_x):
            surroundings = get_surroundings(letters, x, y)
            if surroundings is not None and check_mas_cross(surroundings):
                count += 1

    return count


letters = parse_letters("day4.txt")

part1_count = count_xmas_words(letters)
print(f"part1: {part1_count}")

part2_count = count_xmas_cross(letters)
print(f"part2: {part2_count}")
