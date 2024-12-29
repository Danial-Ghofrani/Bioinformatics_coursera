def hamming_distaance(query1, query2):
    return sum(1 for x,y in zip(query1, query2) if x != y)

def find_neighbors(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {"A","T","C","G"}
    neighborhood = set()
    suffix_neigbor = find_neighbors(pattern[1:],d)

    for text in suffix_neigbor:
        if hamming_distaance(pattern[1:], text) < d:
            for nucleotide in "ACTG":
                neighborhood.add(nucleotide + text)
        else:
            neighborhood.add(pattern[0] + text)

    return neighborhood


def frequent_word_with_mismatch(genome, k, d):
    frequency_map = {}
    for i in range(len(genome) -k +1):
        kmer = genome[i:i+k]
        neigborhood = find_neighbors(kmer, d)
        for neighbor in neigborhood:
            if neighbor in frequency_map:
                frequency_map[neighbor] += 1
            else:
                frequency_map[neighbor] = 1

    max_count = max(frequency_map.values())

    most_frequent_patterns = [
        key for key, value in frequency_map.items() if value == max_count
    ]

    return most_frequent_patterns


# pattern = "TCCCTAGCG"
# d = 3
# print(*find_neighbors(pattern, d), sep=" ")


file = open("dataset_30278_9.txt", "r")
genome = file.read()
k = 6
d = 3
print(frequent_word_with_mismatch(genome, k, d))