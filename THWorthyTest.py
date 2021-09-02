import fileinput
import os

kmers_both = []
absolute_files = []
kmers_score_dict = {}

def kmer_search(kmers_both, data_line):
    global kmers_score_dict
    line = ''
    line = line.join(data_line)
    kmer_found = 0 
    for kmer in kmers_both:
        forward = kmer[0]
        backwards = kmer[1] 
        if forward in line:
            kmers_score_dict[kmer] += 1
            kmer_found += 1
        elif backwards in line:
            kmers_score_dict[kmer] += 1
            kmer_found += 1
    if kmer_found > 0:
        print(f"We found {kmer_found} kmers so far! Yay!")

with open("thor.hammers.1496.3136.txt") as file:
    raw_list = file.readlines()
    kmers_list = []
    for kmer in raw_list:
        kmers_list.append(kmer.strip('\n'))
    for kmer in kmers_list:
        reverse = kmer[::-1]
        compliment_table = reverse.maketrans("cgat", "gcta")
        compliment = reverse.translate(compliment_table)
        kmer_tuple = (kmer, compliment)
        kmers_both.append(kmer_tuple)
    for kmer in kmers_both:
        kmers_score_dict[kmer] = 0

file_list = os.listdir("CDiffFastA200")
for file in file_list:
    absolute_files.append("CDiffFastA200/"+ file)
counter=0
data=[]
for line in fileinput.input(absolute_files):
    if line.startswith(">"):
        kmer_search(kmers_both, data)
        data=[]
    else:
        data.append(line.strip('\n'))
    counter += 1
    if counter % 10000 == 0 :    
        print(f"This counts lines: {counter}")
kmer_search(kmers_both, data)
total_score = len(file_list)

with open("thor.hammers.worthy.scores200.txt", "w+") as output:
    output.write("kmer/reverse_compliment\t" + "kmer_score\t" + "kmer_percent\n")
    for key, value in kmers_score_dict.items():
        output.write(f"{key[0]}/{key[1]}\t{value}\t{round(int(value)/int(total_score)*100, 2)}\n")


#open thor.hammer.1496.3136 

#search through the files in CDiffFasta (for loop)
#count the number of files that contain the sequences
#are the kmers in at least 80% of the files present?
#
#convert DNA to its compliment(reverse the string)
 






