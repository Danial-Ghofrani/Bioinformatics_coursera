import numpy as np

def most_prob_kmer(seq, k, seq_matrix):
    max_prob = -0.1
    most_probable_kmer = ""

    for i in range(len(seq)-k+1):
        kmer = seq[i:i+k]
        prob = 1.0

        for j, nucleotide in enumerate(kmer):
            if nucleotide == "A":
                prob *= seq_matrix[0][j]
            elif nucleotide == 'C':
                prob *= seq_matrix[1][j]
            elif nucleotide == 'G':
                prob *= seq_matrix[2][j]
            elif nucleotide == 'T':
                prob *= seq_matrix[3][j]

        if prob > max_prob:
            max_prob = prob
            most_probable_kmer = kmer

    return most_probable_kmer


filepath = "dataset_30305_3.txt"
with open(filepath, "r") as file:
    seq = file.readline().strip()
    k= int(file.readline().strip())

seq_matrix = np.loadtxt(filepath, skiprows=2)

print(most_prob_kmer(seq, k , seq_matrix))
