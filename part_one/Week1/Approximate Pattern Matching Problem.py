def Approxime_Pattern_count(seq1, seq2, d):
    index_list=[]
    for i in range(0, len(seq2) - len(seq1) + 1):
        # print(seq2[i])
        seq2part = seq2[i:i+len(seq1)]
        # print(seq2part)
        hamming_distance = 0
        for j in range(0, len(seq1)):
            # print(len(seq1))
            # print(len(seq2part))
            if seq1[j] != seq2part[j]:
                hamming_distance = hamming_distance + 1
        if hamming_distance <= d:
                index_list.append(i)
        count = len(index_list)
    print(count)
    return index_list,

# seq1="ATTCTGGA"
# seq2="CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
# d=3

file = open("dataset_30278_6.txt", "r")
genome = file.read().strip()
splited_genome = genome.splitlines()
seq1 = splited_genome[0]
seq2 = splited_genome[1]
d = int(splited_genome[2])


print(*Approxime_Pattern_count(seq1,seq2,d), sep=" ")
