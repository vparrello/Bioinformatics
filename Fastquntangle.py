'''
Created on Aug 10, 2021

@author: fig
'''
import os

directory_name = input("Where are the files of your runs? ")

run_numbers = []
run_files_dict = {}
file_list = os.listdir(directory_name)


for file in file_list:
    run_numbers.append(file.strip(".fastq"))
for run in run_numbers:
    run_files_dict[run] = (run + '_1.fastq', run + '_2.fastq')
    
print("Found fastq files.")

if not os.path.isdir("Fastq_Paired_Reads"):
    os.mkdir("Fastq_Paired_Reads")

for file in file_list:
    data = iter(open(f"{directory_name}/{file}", "r", encoding="utf-8"))
    if file.startswith("."):
        pass
    else:
        print(f"Working on {file} now.")
        for line in data:
            run = file.strip(".fastq")
            if line.startswith("@") and ".1 " in line:
                output = open(f"Fastq_Paired_Reads/{run_files_dict[run][0]}", "a")
                output.write(line)
                output.write(next(data))
                output.write(next(data))
                output.write(next(data))
                output.close()
            elif line.startswith("@") and ".2 " in line:
                output = open(f"Fastq_Paired_Reads/{run_files_dict[run][1]}", "a")
                output.write(line)
                output.write(next(data))
                output.write(next(data))
                output.write(next(data))
                output.close
print("Finished fastq. Creating manifest file.")
with open("manifest.txt", "w+") as manifest:
    manifest.write("sample-id\t" + "forward-absolute-filepath\t" + "reverse-absolute-filepath\n")
    for key, value in run_files_dict.items():
        manifest.write(f"{key}\t" + os.path.abspath(f"Fastq_Paired_Reads/{value[0]}") + "\t" + os.path.abspath(f"Fastq_Paired_Reads/{value[1]}") + "\n")
print("All done!")    


