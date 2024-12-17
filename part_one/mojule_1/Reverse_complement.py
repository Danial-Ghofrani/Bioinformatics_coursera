dataset_name ="dataset_30273_2 (1)"
file = open(f"{dataset_name}.txt", "r")
input = file.read()
Transcription_dict = {"A":"T" , "C":"G" , "G":"C" ,"T":"A"}
nucleotide_list = []
reverse_complement = []

for i in range(0, len(input) - 1):
    reverse_complement.append(Transcription_dict[input[i]])

final_seq = "".join(map(str, reversed(reverse_complement)))
RC = open("RC.txt", "w")
RC.write(final_seq)
RC.close()
