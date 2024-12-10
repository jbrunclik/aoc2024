#!/usr/bin/env python3

import re

MUL_RE = re.compile(r"mul\((?P<a>\d+),(?P<b>\d+)\)", re.MULTILINE)
INST_DO = "do()"
INST_DONT = "don't()"


def parse_expr(filename):
    with open(filename) as f:
        return f.read().strip()


def calculate_product(expr):
    return sum(int(a) * int(b) for a, b in MUL_RE.findall(expr))


def find_next_instruction(expr):
    next_dont = expr.find(INST_DONT)
    next_do = expr.find(INST_DO)

    if next_do == -1 and next_dont == -1:
        return len(expr), 0, False
    elif next_do == -1 or (next_dont != -1 and next_dont < next_do):
        return next_dont, len(INST_DONT), False
    else:
        return next_do, len(INST_DO), True


def calculate_instructions(expr):
    enabled = True
    total = 0

    while expr:
        next_index, skip_length, next_enabled = find_next_instruction(expr)
        subexpr = expr[:next_index]
        if enabled:
            total += calculate_product(subexpr)
        expr = expr[next_index + skip_length :]
        enabled = next_enabled

    return total


expr = parse_expr("day3.txt")

part1_total = calculate_product(expr)
print(f"part1: {part1_total}")

part2_total = calculate_instructions(expr)
print(f"part2: {part2_total}")
