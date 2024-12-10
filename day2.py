#!/usr/bin/env python3


def parse_reports(filename):
    with open(filename) as f:
        return [list(map(int, line.split())) for line in f]


def get_diffs(report):
    return [b - a for a, b in zip(report, report[1:])]


def is_safe(report):
    diffs = get_diffs(report)
    return all(-3 <= diff < 0 for diff in diffs) or all(
        1 <= diff <= 3 for diff in diffs
    )


def count_safe_reports(reports):
    return sum(is_safe(report) for report in reports)


def count_safe_after_removal(reports):
    return sum(
        any(is_safe(report[:i] + report[i + 1 :]) for i in range(len(report)))
        for report in reports
    )


reports = parse_reports("day2.txt")

part1_safe = count_safe_reports(reports)
print(f"part1: {part1_safe}")

part2_safe = count_safe_after_removal(reports)
print(f"part2: {part2_safe}")
