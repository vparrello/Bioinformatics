'''
Created on Aug 10, 2021

@author: fig
'''
import fileinput
import os

kmers_both = []
absolute_files = []
genome_list = []
genome_dict = {}

def kmer_search(kmers_both, data_line, name_of_file):
    global genome_dict
    line = ''
    line = line.join(data_line)
    kmer_found = 0
    genome = name_of_file.lstrip("../CDiffFastA200/") 
    if not genome.startswith("1"):
        print(genome)
    for kmer in kmers_both:
        forward = kmer[0]
        backwards = kmer[1] 
        if forward in line:
            genome_dict[genome.strip(".fna")] += ", " + "".join(forward)
            kmer_found += 1
        elif backwards in line:
            genome_dict[genome.strip(".fna")] += ", " +"".join(backwards)
            kmer_found += 1
    if kmer_found > 0:
        print(f"We found {kmer_found} kmers so far! Yay!")

with open("../thor.hammers.1496.3136.txt") as file:
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


file_list = os.listdir("../CDiffFastA200")
for file in file_list:
    absolute_files.append("../CDiffFastA200/"+ file)
    genome_list.append(file.strip(".fna"))
for genome in genome_list:
    genome_dict[genome]= ""
counter=0
data=[]
for line in fileinput.input(absolute_files):
    file_name = fileinput.filename()
    if line.startswith(">"):
        kmer_search(kmers_both, data, file_name)
        data=[]
    else:
        data.append(line.strip('\n'))
    counter += 1
    if counter % 10000 == 0 :    
        print(f"This counts lines: {counter}")
kmer_search(kmers_both, data, file_name)

with open("thor.hammers.present200.txt", "w+") as output:
    output.write("genome_id\t" + "kmer_present\n")
    for key, value in genome_dict.items():
        output.write(f"{key}\t{value}\n")
