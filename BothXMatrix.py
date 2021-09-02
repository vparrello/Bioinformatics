'''
Created on May 1, 2021

@author: fig
'''
samplelist = []
finallist = {}
taxonbins = set()
bindict = {}

#Run numbers in a dictionary with floats for 1 = park and 0 = control
def definedruns(filename, kind):
    #opens file
    with open(filename,'rt') as textdoc:
        #runs through the runs and strips each line and separates by tabs
        for sample in textdoc:
            sample = sample.rstrip('\n')
            runs = sample.split('\t')         
            #checking for the header first 
            if runs[0] != 'sample_id':
                #Defines parkinsons or control based on the file type
                finallist[runs[0]] = kind
                #creates the keys for the dictionary as the ERR#s
                samplelist.append(runs[0]) 
                bindict[runs[0]] = set()
#finds all the taxon ids of the bins in both samples and controls
def taxonids(filename):
    #open the file!
    with open(filename, 'rt') as bindoc:
        #breaking apart the lines of the document and cleaning them
        for sample in bindoc:
            sample = sample.rstrip('\n')
            collum = sample.split('\t') 
            #take the last collum and split apart the taxon bin ids
            if collum[0] != 'sample_id':
                repgenid = collum[6]
                #adds the repgen id to the set connected to the sample name dictionary
                bindict[collum[0]].add(repgenid)
                taxonbins.add(repgenid)                 
#create a table based on if the taxonids are used by that run            
def unionbinsample():
    with open('Xmatrix', 'w') as outtable:
        #headers
        headerrow = 'sample\t' + '\t'.join(taxonbins) + '\tparkinsons\n'
        outtable.write(headerrow)
        #matching the values in the samples to the values in the collums
        for key in bindict:
            binset = bindict[key]
            #empty list to put the 1s and 0s in
            presencelist = []
            #checks for the headers
            for header in taxonbins:
                #is the header in the current sample's good bins
                if header in binset:
                    presencelist.append('1.0')
                else:
                    presencelist.append('0.0')
            outtable.write(key + '\t' + '\t'.join(presencelist) + '\t' + finallist[key] + '\n') 

definedruns('AlzCBinsG.tbl', '0.0') 
definedruns('AlzSBinsG.tbl', '1.0')      
taxonids('AlzCBinsG.tbl')
taxonids('AlzSBinsG.tbl')
unionbinsample()       
if __name__ == '__main__':
    pass