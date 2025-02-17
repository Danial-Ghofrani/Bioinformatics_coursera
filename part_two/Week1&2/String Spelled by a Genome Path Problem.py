def construct_genome(genes):
    genome = []
    l = len(genes[0])
    genome.append(genes[0])
    genes = genes[1:]
    for gene in genes:

        genome.append(gene[l-1:l])

    genome = "".join(genome)
    return genome

file = open("dataset_30182_3.txt", "r")
seqs = file.read()
genes = seqs.split(" ")


print(construct_genome(genes).strip())

