## Course 1, week 1, exercise 1_1 1_2
import numpy as np


def patterncount(text, pattern):
    count = 0
    for i in range(0, len(text)-len(pattern) + 1):
        if text[i: i + len(pattern)] == pattern:
            count = count + 1

    return count


def frequentwords(text, k):
    best_pattern = None
    max_count = 0

    for i in range(0, len(text) - k + 1):
        pattern = text[i: i + k]
        pc = patterncount(text, pattern)

        if pc > max_count:
            max_count = pc
            best_pattern = pattern

    return max_count, best_pattern

print(frequentwords("ACCTGTCCATC", 3))