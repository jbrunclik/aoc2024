#!/usr/bin/env python3


def parse_pages(filename):
    rules = []
    updates = []

    with open(filename) as f:
        for line in f:
            line = line.strip()
            if "|" in line:
                rules.append(tuple(map(int, line.split("|", 1))))
            elif "," in line:
                updates.append(list(map(int, line.split(","))))

    return rules, updates


def is_correct_order(update, rules):
    for left, right in rules:
        if left in update and right in update:
            if update.index(left) > update.index(right):
                return False
    return True


def get_middle_element(update):
    if len(update) % 2 != 1:
        raise ValueError("Update must have an odd number of elements.")
    return update[len(update) // 2]


def sum_correct_middle_elements(rules, updates):
    return sum(
        get_middle_element(update)
        for update in updates
        if is_correct_order(update, rules)
    )


def reorder_update(update, rules):
    for left, right in rules:
        if left in update and right in update:
            if update.index(left) > update.index(right):
                update.remove(left)
                update.insert(update.index(right), left)


def sum_incorrect_middle_elements(rules, updates):
    total = 0
    for update in updates:
        if not is_correct_order(update, rules):
            while not is_correct_order(update, rules):
                reorder_update(update, rules)
            total += get_middle_element(update)
    return total


rules, updates = parse_pages("day5.txt")

part1_sum = sum_correct_middle_elements(rules, updates)
print(f"part1: {part1_sum}")

part2_sum = sum_incorrect_middle_elements(rules, updates)
print(f"part2: {part2_sum}")
