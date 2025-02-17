import math
import numpy as np

def Motifs_percent_count(motifs):
    percent_count = {"A": [], "C": [], "G": [], "T": []}
    for l in range(len(motifs[0])):
        count = {"A": 0, "C": 0, "G": 0, "T": 0}
        for motif in motifs:
            text = motif[l]
            count[text] += 1
        # print(count)
        for key in percent_count.keys():
            percent_count[key].append(count[key] / len(motifs))
    print(percent_count)
    return percent_count


def entropy(p):
    entropy = 0
    for prob in p:
        if prob > 0:
            entropy = entropy - prob * np.log2(prob)
    return entropy


motifs = 'TCGGGGGTTTTT CCGGTGACTTAC ACGGGGATTTTC TTGGGGACTTTT AAGGGGACTTCC TTGGGGACTTCC TCGGGGATTCAT TCGGGGATTCCT TAGGGGAACTAC TCGGGTATAACC'.split()
percent_count = Motifs_percent_count(motifs)

total_entropy = 0.0
for l in range(len(motifs[0])):
    p = [percent_count["A"][l], percent_count["C"][l], percent_count["G"][l], percent_count["T"][l]]
    total_entropy += entropy(p)


print(total_entropy)