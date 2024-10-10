def find_clumps(Genome, k, L, t):
    clumps = set()
    n = len(Genome)

    for i in range(n - L + 1):
        window = Genome[i:i + L]
        kmer_counts = {}

        for j in range(L - k + 1):
            kmer = window[j:j + k]
            if kmer in kmer_counts:
                kmer_counts[kmer] += 1
            else:
                kmer_counts[kmer] = 1

        for kmer, count in kmer_counts.items():
            if count >= t:
                clumps.add(kmer)

    return list(clumps)


# Example usage:
Genome = "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGACTGAGTGAAGACTGAGTGAAGACTGAGTGAAGACTGAGTGAAGACTGAGTGAAGACTGAGTGAAGACTGAGTGAAGACTGAGTGAAGACTGAGTGAAGACTGAGTGAAGACTGAGTGAAGACTGAGTGAAGACTGAGTGAAGACTGAGTGAAGACTGAGTGAAGACTGAGTGAAGACTGAGTGAAGACTGAGTGAAGACTGAG"

print(find_clumps(Genome, 5, 50, 4))

