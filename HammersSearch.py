'''
Created on Aug 5, 2021

@author: fig
'''

import pandas as pd


data = pd.read_csv("RepGens.csv")
repgens = data.Rep100.to_list()
repgen_list = []
for repgen in repgens:
    no_gto = repgen.strip(".gto")
    repgen_list.append(no_gto)

with open("bash_command", "w+") as output:
    output.write("#!/bin/sh \n")
    for repgen in repgen_list:
        output.write(f"kmers.reps target Rep200A/GTO100 Rep200A/GTO100/{repgen}.gto --type DIR >Hammers100/{repgen}.hammer100.txt\n")


#create a separate list of gto names called gto numbers with the gto stripped from it.

