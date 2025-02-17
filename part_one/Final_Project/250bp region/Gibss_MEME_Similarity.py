from collections import Counter
import logomaker
import pandas as pd


def hamming_distance(query1, query2):
    return sum(1 for x,y in zip(query1, query2) if x != y)

def consensus_motif(motifs):
    """Find the consensus sequence for a set of motifs."""
    k = len(motifs[0])  # Motif length
    consensus = ""

    for i in range(k):
        column = [motif[i] for motif in motifs]
        most_common = Counter(column).most_common(1)[0][0]
        consensus += most_common

    return consensus

def create_sequence_logo(motifs, title):
    """Generate a sequence logo for a motif set."""
    k = len(motifs[0])
    counts = {nuc: [0] * k for nuc in "ACGT"}

    for motif in motifs:
        for i, nuc in enumerate(motif):
            counts[nuc][i] += 1

    df = pd.DataFrame(counts)
    df = df.div(df.sum(axis=1), axis=0)  # Normalize

    logo = logomaker.Logo(df)
    logo.ax.set_title(title)





motifs_meme = ["AGGGCCGGAAGTCCCCAATG", "AGGGCCGGAAGTCCCCAATG", "AGGGGCGAAAGTCCCTTATC", "AGGGTCAATGGTCCCCAAGT", "AGGGTCAATGGTCCCCAAGT",
              "AGGGCCGTTAGTCCTTATCG", "AGGGCCGTAAGTCATCCACT", "AGGGCCAAAGGTCCTCCGCT", "AGGGCCAAAGGTCCTCCGCT", "TGAGGCTTTAGTCCCCAATC",
              "TGAGGCTTTAGTCCCCAATC", "CGGGACGTAAGTCCCTAACG", "ACGGGCTTAGGTCCTCAATG", "GGGGCCGAAGGTCCTCAAGA", "GGAGGCGATGGTCCCTAACC",
              "AGGGACCTAATTCCATATTT", "AGGGCCGAAAGTCCCATGCC", "AAAGTCGAAGGTTGTCAATT", "AGTGACGAAAGACCCCAGTG", "AAAGGCCTTATTCGTCAAGT",
              "AGAACCGAAGTTCGTTGAGT", "GGGGACCGAAGTCCCCGGGC"]


motifs_gibbs = ["TTCGTGACCGACGTCCCCAG", "GCCGGCGCCATCGAAGCCAG", "CTGGTCGCCACTGGAAAGGG", "CGGGCCACAATCGAAAGCCG", "GTGGTCGCGATCGAACCCGA", "CTTTTGGCCACCGGCGCTGG", "GTGGTCACTGCGGAGGAGCA",
               "GCGGGCCCGGCCGCCATCGG", "GAGGAGCACATGGCCGCCGA", "CTGGTGACCACCGCCGACGG", "GACGTCCGCGACGACGCGTG", "CCGGGCTCGAAGGAGGTTGG", "ATCATCGGCCAGGGCGCCGG", "GTGGTCGACAAGGTCGCCGA",
               "CTGATCCACACCGGCGACCG", "GCGGCGGCCTTGGCCGCCCG", "GTCGAGGCCGACGATGACAG", "GAGCGAACCATCTACCCCGA","GTGGTCACCATGGTGTCCGG", "GTGGTGGCCATTTGATGCCT", "GCCGTCGCCATTGTCGCGCA",
               "CTGCTCGCCCATGGCCCTCG", "GAGGTGGCCTACGGCGAGGA", "GAGGACGCCATCGGCCGCGA", "CTGGTCAGTCTCGACAGCGA", "AGGGTCGCCACGGCTGGCGA", "GTCGTCGGCCTCGGCGTCGG", "CTGGGCAGCGTTGCACTCGG",
               "GGGGGCCCGGACGGCCAGGG", 'ATGGTCAGCGCCTTCCCCGG', 'GATCGGGCCATCGCCGGCGG', 'GTGGGGACCAACGCCCCTGG', 'GTGATAACGCGCGGCGCCGG', 'GAGGGCTCCGACGTGCCGGT'
]



consensus_gibbs = consensus_motif(motifs_gibbs)
consensus_meme = consensus_motif(motifs_meme)

print(f"Gibbs Consensus: {consensus_gibbs}")
print(f"MEME Consensus:   {consensus_meme}")
print(f"Hamming Distance Between Consensus: {hamming_distance(consensus_gibbs, consensus_meme)}")

create_sequence_logo(motifs_gibbs, "GibbsSampler Motif Logo")
create_sequence_logo(motifs_meme, "MEME Motif Logo")