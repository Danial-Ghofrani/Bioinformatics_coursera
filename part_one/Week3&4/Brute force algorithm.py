def hamming_distance(seq1, seq2):
    return sum (1 for x,y in zip(seq1,seq2) if x != y)

def generating_neighborhood(sequence, d):
    if d == 0 :
         return {sequence}
    if len(sequence) == 1:
        return {"A", "T", "C", "G"}
    neighborhood = set()
    suffix_seq= generating_neighborhood(sequence[1:],d)
    for seq in suffix_seq:
        if hamming_distance(seq, sequence[1:]) == d:
            neighbor = sequence[0] + seq
            neighborhood.add(neighbor)
        else :
            for nucleotide in "ACTG":
                neighbor = nucleotide + seq
                neighborhood.add(neighbor)

    return neighborhood

def motifEnumeration(DNA, k, d):
    patterns = set()
    for string in DNA:
        for i in range(len(string)-k+1):
            kmer = string[i:i+k]

            neighborhood = generating_neighborhood(kmer,d)

            for neighbor in neighborhood:
                all_match = True

                for string in DNA:
                    found_match = False

                    for j in range(len(string)-k+1):
                        subseq = string[j:j+k]

                        if hamming_distance(neighbor, subseq) <=d:
                            found_match = True
                            break

                    if not found_match:
                        all_match = False
                        break

                if all_match:
                    patterns.add(neighbor)

    return patterns



DNA = ["CATACTTTATTGCACCTCCATGCCT","GAGAACTATAGTTCTCAGACCTTTA","AGGTGCCCAGGGTGAAGCCGCAGAC","GCTACTCAGCAACGTTTTTACAGAC", "CATACCTGTTACGTAGTGCGGTTGA", "CTCCTAGGTGTCGTGCATACGGCTT"]
k = 5
d = 1

print(*motifEnumeration(DNA, k, d), sep=" ")