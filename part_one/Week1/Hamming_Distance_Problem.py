def calculate_hamming_distance(genome1, genome2):
    hamming_distance = 0
    for i in range(0, len(genome1)):
        if genome1[i] == genome2[i]:
            hamming_distance = hamming_distance

        else:
            hamming_distance = hamming_distance + 1
        print(genome1[i], genome2[i])
    return hamming_distance


### Setting the function inputs:
# genome1= "GGGCCGTTGGT"
# genome2 = "GGACCGTTGAC"

file = open("dataset_30278_3.txt", "r")
genomes= file.read()
splited_genome = genomes.splitlines()
genome1 = splited_genome[0]
genome2 = splited_genome[1]



print(calculate_hamming_distance(genome1, genome2))
