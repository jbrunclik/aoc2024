#!/usr/bin/env python3

from collections import Counter

with open("day1.txt") as f:
    left, right = zip(*(map(int, line.split()) for line in f))

left = sorted(left)
right = sorted(right)

distance = sum(abs(l - r) for l, r in zip(left, right))
print(f"part1: {distance}")

counter = Counter(right)
similarity = sum(l * counter[l] for l in left)
print(f"part2: {similarity}")
