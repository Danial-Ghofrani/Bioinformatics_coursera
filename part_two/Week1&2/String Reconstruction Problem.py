def composition_kmers(k, dna):
    composotions = []
    for i in range(len(dna) -k +1):
        composotions.append(dna[i: i + k])

    return composotions

file = open("dataset_30153_3.txt", "r")
input = file.read().strip()
splited_input = input.splitlines()
k = int(splited_input[0])
dna = splited_input[1]

results = composition_kmers(k, dna)
print(*results, sep = " ")