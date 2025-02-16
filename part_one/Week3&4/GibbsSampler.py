import random

def score(motifs):
    """
    Calculate the score of a set of motifs based on the consensus.
    Lower score means higher similarity among motifs.
    """
    consensus_score = 0
    k = len(motifs[0])
    t = len(motifs)

    for i in range(k):
        column = [motif[i] for motif in motifs]
        max_freq = max(column.count(nuc) for nuc in "ACGT")
        consensus_score += (t - max_freq)

    return consensus_score

def profile_with_pseudocounts(motifs):
    """
    Generate a profile matrix with pseudocounts from a set of motifs.
    """
    t = len(motifs)
    k = len(motifs[0])
    pseudocount = 1
    profile = {nuc: [pseudocount] * k for nuc in "ACGT"}

    for i in range(k):
        column = [motif[i] for motif in motifs]
        for nuc in "ACGT":
            profile[nuc][i] += column.count(nuc)

    for nuc in "ACGT":
        profile[nuc] = [freq / (t + 4) for freq in profile[nuc]]

    return profile

def motifs_from_profile(profile, dna):
    """
    Generate the most probable motifs for each DNA sequence using the profile.
    """
    k = len(profile["A"])
    motifs = []

    for sequence in dna:
        max_prob = -1
        best_kmer = ""

        for i in range(len(sequence) - k + 1):
            kmer = sequence[i: i+k]
            prob = 1

            for j, nucleotide in enumerate(kmer):
                prob *= profile[nucleotide][j]

            if prob > max_prob:
                max_prob = prob
                best_kmer = kmer

        motifs.append(best_kmer)

    return motifs


def probability_of(kmer, profile):
    prob = 1.0
    for i, nucleotide in enumerate(kmer):
        prob *= profile[nucleotide][i]
    return prob

def weighted_random_choice(probabilities):
    r = random.uniform(0, sum(probabilities))
    cumulative = 0

    for i, prob in enumerate(probabilities):
        cumulative += prob
        if r < cumulative:
            return i


def gibbs_sampler(dna, k, t, n):

    motifs = [random.choice([dna[i][j:j+k] for j in range(len(dna[i]) - k + 1)]) for i in range(t)]
    best_motifs = motifs[:]

    for _ in range(n):
        i = random.randint(0, t - 1)
        reduced_motifs = motifs[:i] + motifs[i+1:]

        profile = profile_with_pseudocounts(reduced_motifs)
        kmers = [dna[i][j:j+k] for j in range(len(dna[i]) - k + 1)]

        probabilities = [probability_of(kmer, profile) for kmer in kmers]
        new_motif_index = weighted_random_choice(probabilities)

        motifs[i] = kmers[new_motif_index]

        if score(motifs) < score(best_motifs):
            best_motifs = motifs[:]

    return best_motifs


def run_gibbs_sampler(dna, k, t, n, iterations=20):
    """
    Run the RandomizedMotifSearch algorithm multiple times to find the best motifs.
    """
    best_motifs = None
    best_score = float('inf')

    for _ in range(iterations):
        motifs = gibbs_sampler(dna, k, t, n)
        current_score = score(motifs)

        if current_score < best_score:
            best_motifs = motifs
            best_score = current_score

    return best_motifs




with open("../Final_Project/MTgenome.txt", "r") as file:  # Replace "filename.txt" with the actual file name
    content = file.read()

splited_content = content.splitlines()

k, t, n = map(int, splited_content[0].split())
dna = splited_content[1:]


best_motifs = run_gibbs_sampler(dna, k, t, n)
print(' '.join(best_motifs))

