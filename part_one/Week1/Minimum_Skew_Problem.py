def minimum_skew(genome):
    skew = 0
    min_skew = 0
    min_skew_index = -1
    for i in range(0, len(genome)-1):
        nucleotide = genome[i]
        if nucleotide == "C":
            skew = skew -1
        elif nucleotide == "G":
            skew = skew +1
        else:
            skew = skew
        # print(i + 1, skew)

        if skew < min_skew:
            min_skew = skew
            min_skew_index = i + 1

        elif skew == min_skew:
            print("there was a new skew found with the same value of:",min_skew,"the old skew placement(i) was:",min_skew_index)
            print("the new skew will be replaced automatically")
            min_skew = skew
            min_skew_index = i + 1



    return min_skew, min_skew_index





# genome = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"


file = open("dataset_30277_10.txt", "r")
genome = file.read()
print(minimum_skew(genome))
