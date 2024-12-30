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



def minimum_skew_with_pandas(genome):
    """ this function calculates the skew using pandas!"""
    import numpy as np
    skew = np.zeros(len(genome)+1)
    for i in range (1, len(genome)+1):
        if genome[i-1] == "G":
            skew[i] = skew[i-1] + 1
        elif genome[i-1] == "C":
            skew[i] = skew[i-1] -1
        else:
            skew[i] = skew[i-1]
    min_skew = np.where(skew ==np.min(skew))
    return min_skew[0]



### Data importing
# genome = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
file = open("dataset_30277_10.txt", "r")
genome = file.read()


### Calling functions
print(minimum_skew(genome))
# print(minimum_skew_with_pandas(genome))




#todo it would be beautiful if i try to calculate the performance of these two methods and put the time comparison of them on linkdin.