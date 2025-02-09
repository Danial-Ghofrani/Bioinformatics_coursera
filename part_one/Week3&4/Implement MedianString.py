def generaring_kmers(k):
    kmers=[""]
    for i in range(k):
        new_kmers = []
        for seq in kmers:
            for nucleotide in "ATCG":
                new_kmers.append(seq + nucleotide)
        kmers = new_kmers
    return kmers


def hamming_distaance(query1, query2):
    return sum(1 for x,y in zip(query1, query2) if x != y)


def Median_string(k, Dna):
    kmers = generaring_kmers(k)
    least_dis = float('inf')
    min_kmer = None
    for seq1 in kmers:
        sum_dis = 0

        for seq2 in Dna:
            min_dist = float('inf')

            for i in range(len(seq2)-k+1):

                kmer_in_dna = seq2[i:i+k]
                distance = hamming_distaance(seq1, kmer_in_dna)
                min_dist = min(min_dist, distance)

            sum_dis += min_dist

        if sum_dis < least_dis:
            least_dis = sum_dis
            min_kmer = seq1

    return least_dis, min_kmer


with open("dataset_30304_9.txt", "r") as file:  # Replace "filename.txt" with the actual file name
    content = file.read()

splited_content = content.splitlines()

k = int(splited_content[0])
Dna = splited_content[1].split()

print(Median_string(k, Dna))
