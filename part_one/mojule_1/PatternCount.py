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

# print(frequentwords("ACCTGTCCATC", 3))

def frequencytable(text, k):
    frequentmap = {}
    n = len(text)
    for i in range(0 , n-k+1):
        pattern = text[i:i+k]
        if pattern not in frequentmap.keys():
            frequentmap[pattern] = 1
        else:
            frequentmap[pattern] = frequentmap[pattern]

        return frequentmap

print(frequencytable("ACGTTTCACGTTTTACGG", 3))



def frequent_words(text, k):
    # Create a dictionary to count occurrences of k-mers
    kmer_counts = {}

    # Loop through the text to extract all k-mers
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        if kmer in kmer_counts:
            kmer_counts[kmer] += 1
        else:
            kmer_counts[kmer] = 1

    # Find the maximum frequency
    max_count = max(kmer_counts.values())

    # Collect all k-mers with the maximum frequency
    most_frequent_kmers = [kmer for kmer, count in kmer_counts.items() if count == max_count]

    # Return the result as a space-separated string
    return " ".join(most_frequent_kmers)


# Example usage
# text = "TTTAATACATTTTCTTCTCGAGACATCGACGTTTCGAGACATGCGGTTCTGAGCGGTTCTGACGACGTTTTTTAATACACGACGTTTCGACGTTTGCGGTTCTGACGAGACATTTTTCTTCTCGAGACATCGACGTTTCGAGACATGCGGTTCTGATTTAATACATTTTCTTCTGCGGTTCTGATTTAATACACGAGACATGCGGTTCTGATTTTCTTCTCGACGTTTCGACGTTTGCGGTTCTGATTTAATACAGCGGTTCTGACGAGACATTTTAATACACGACGTTTTTTTCTTCTCGACGTTTTTTTCTTCTTTTAATACACGACGTTTCGAGACATGCGGTTCTGACGAGACATCGAGACATTTTTCTTCTGCGGTTCTGAGCGGTTCTGATTTTCTTCTCGACGTTTGCGGTTCTGATTTTCTTCTCGACGTTTCGACGTTTGCGGTTCTGAGCGGTTCTGATTTAATACAGCGGTTCTGATTTTCTTCTCGAGACATTTTAATACAGCGGTTCTGATTTTCTTCTTTTTCTTCTTTTAATACACGACGTTTGCGGTTCTGAGCGGTTCTGACGAGACATCGAGACATTTTTCTTCTGCGGTTCTGAGCGGTTCTGAGCGGTTCTGAGCGGTTCTGATTTTCTTCTCGACGTTTCGAGACATTTTTCTTCTGCGGTTCTGATTTTCTTCTCGACGTTTTTTTCTTCTGCGGTTCTGATTTAATACACGAGACATCGAGACATCGAGACATCGACGTTTCGAGACATGCGGTTCTGAGCGGTTCTGACGACGTTTCGACGTTTTTTAATACACGAGACATCGACGTTTTTTAATACACGAGACATTTTTCTTCTTTTAATACATTTTCTTCTCGAGACATGCGGTTCTGACGACGTTTCGACGTTTCGAGACATTTTAATACATTTTCTTCTTTTAATACATTTAATACATTTTCTTCTCGACGTTT"
# k = 11
# print(frequent_words(text, k))



