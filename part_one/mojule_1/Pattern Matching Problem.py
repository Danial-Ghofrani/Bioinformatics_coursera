# Input: Two strings, Pattern and Genome.
# Output: A collection of space-separated integers specifying all starting positions where Pattern appears as a substring of Genome.

dataset_name = "dataset_30273_5 (3)"

file = open(f"{dataset_name}.txt", "r")
input = file.read()
splited_txt = input.splitlines()
query_1 = splited_txt[0]
query_2 = splited_txt[1]


def pattern_match(query_1, query_2):
    placement_list = []
    for i in range(0, len(query_2) + 1):
        if query_1 == query_2[i:i+len(query_1)]:
            placement_list.append(i)
        else:
            continue
    print(*placement_list, sep=' ')


vibro = open(f"Vibrio_cholerae.txt", "r")
genome = vibro.read().strip()
first_query = "CTTGATCAT"
second_query = genome
pattern_match(first_query, second_query)




