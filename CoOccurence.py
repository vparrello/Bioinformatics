'''
Created on Jun 23, 2021

@author: fig
'''
#creates co-occurence value for each repgen set in the samples. 

def readheader(inputfile):
    """Reads the header of the file and returns an array of repgen ids."""
    header = next(inputfile)
    row = header.rstrip('\n')
    column = row.split('\t')
    repgens = column[1: -1]
    return repgens

def emptydict(repgenarray):
    """Creates an empty set as a value in a dictionary for each of the repgenids as keys."""
    empdict = {}
    for genomes in repgenarray:
        empdict[genomes] = set()
    return empdict

def fillset(inputfile, repgenarray, dictpark, dictcont):
    """Fills the empty sets in the dictionaries for parkinsons and controls with the samples where they are present. """
    for row in inputfile:
        row = row.rstrip('\n')
        column = row.split('\t')
        if formatsaver(column[-1]):
            for i in range(0, len(repgenarray)):
                if formatsaver(column[i+1]):
                    dictpark[repgenarray[i]].add(column[0])
        else:
            for i in range(0, len(repgenarray)):
                if formatsaver(column[i+1]):
                    dictcont[repgenarray[i]].add(column[0])

def formatsaver(col):
    """Takes a string and returns True of False based on the end of the row having 1.0"""
    park = False 
    if col.endswith('1.0'):
        park = True 
    return park
    
def occurencevalues(repgenarray, dictpark, dictcont, outfile):
    """Computes the occurence values for each repgenid."""
    headerrow = 'genome1\t' + 'genome2\t' + 'Parkinsons Occurrence\t' + 'Control Occurrence\n'
    outfile.write(headerrow)
    for i in range(0, len(repgenarray)):
        repgeni = repgenarray[i]
        setipark = dictpark[repgeni]
        seticont = dictcont[repgeni]
        for j in range(i+1, len(repgenarray)):
            repgenj = repgenarray[j]
            setjpark = dictpark[repgenj]
            setjcont = dictcont[repgenj]
            intpark = setipark.intersection(setjpark)
            intcont = seticont.intersection(setjcont)
            if len(setipark) == 0 and len(setjpark) == 0:
                copark = 0
            else:
                copark = len(intpark)* 200.0 / (len(setipark) + len(setjpark))
            if len(seticont) == 0 and len(setjcont) == 0:
                cocont = 0
            else:
                cocont = len(intcont)* 200.0 / (len(seticont) + len(setjcont))
            if copark >= 50.0 or cocont >= 50.0:
                outfile.write(f"{repgeni}\t {repgenj}\t {copark}\t {cocont}\n")
                
def occurencexmatrix(repgenarray, dictpark, dictcont, outfile):
    """Computes the co-occurence of the repgen pairs into the samples."""
    #GenomeID1/GenomeID2
    #Set of all the known couples
    #Set of couples in each sample

with open('data.tbl') as inputs:
    repgenarray = readheader(inputs)
    repgenspark = emptydict(repgenarray)
    repgenscont = emptydict(repgenarray)
    fillset(inputs, repgenarray, repgenspark, repgenscont)
with open('CoOccurence.tbl', 'w') as outfile:
    occurencevalues(repgenarray, repgenspark, repgenscont, outfile)