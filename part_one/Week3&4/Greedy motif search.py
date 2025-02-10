def most_prob_kmer(seq, k, seq_matrix):
    max_prob = -0.1
    most_probable_kmer = ""

    for i in range(len(seq)-k+1):
        kmer = seq[i:i+k]
        prob = 1.0

        for j, nucleotide in enumerate(kmer):
            prob *= seq_matrix[nucleotide][j]

        if prob > max_prob:
            max_prob = prob
            most_probable_kmer = kmer

    return most_probable_kmer


def create_profile_matrix(motifs):
    k = len(motifs[0])
    t = len(motifs)
    profile = {nucleotide: [0] * k for nucleotide in "ACTG"}

    for i in range(k):
        column = [motif[i] for motif in motifs]
        for nucleotide in "ACGT":
            profile[nucleotide][i] = column.count(nucleotide) / t

    return profile


def score_motifs(motifs):
    k = len(motifs[0])
    t = len(motifs)
    score = 0

    for i in range(k):
        column = [motif[i] for motif in motifs]
        max_count = max(column.count(nucleotide) for nucleotide in "ACGT")
        score += t - max_count

    return score


def greedy_search(k, t, dna_list):
    best_motifs = [seq[:k] for seq in dna_list[:t]]
    for i in range(len(dna_list[0]) - k + 1):
        motifs = [dna_list[0][i: i + k]]

        for j in range(1,t):
            profile = create_profile_matrix(motifs)
            best_kmer = most_prob_kmer(dna_list[j], k, profile)
            motifs.append(best_kmer)

        if score_motifs(motifs) < score_motifs(best_motifs):
            best_motifs = motifs

    return best_motifs


def read_input_file(filename):
    with open(filename, 'r') as file:
        # First line contains t and k
        k, t = map(int, file.readline().split())
        # Second line contains the DNA sequences
        dna_sequences = file.readline().split()

    return dna_sequences, k, t


# Read the input file
filename = "dataset_30305_5.txt"  # Your input file
dna_sequences, k, t = read_input_file(filename)

# Call the greedy motif search function
best_motifs = greedy_search( k, t, dna_sequences)
print("Best motifs found:")
print(' '.join(best_motifs))