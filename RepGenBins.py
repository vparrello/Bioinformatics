'''
Created on Jun 2, 2021

@author: fig
'''
#Creates a table of Repgenid, Human readable name, Parkinsons Count, Controls count, % in Parkinsons, % of Controls

repgenlist = []
parkcount = {}
controlcount = {}
humanreadablename = {}
parktotal = 0
controltotal = 0
         
#create a dictionary connecting repgenids to human readable names
def namedict(filename):
    #open the file
    with open(filename, 'rt') as repgendoc:
        next(repgendoc)
        for line in repgendoc:
            line = line.rstrip('\n')
            column = line.split('\t')
            humanreadablename[column[0]] = column[1]
#Reads the XMatrix to count the number of bins for each repgen id.
def bincount(filename, outtable):
    global parktotal, controltotal 
    #opens file
    with open(filename,'rt') as textdoc:
        outtable.write('RepGenID\t' + 'HumanReadableName\t' + 'Parkinsons\t' + 'Controls\t' + '%Parkinsons\t' + '%Controls' + '\n')
        #create a list of repgenids and put them into a list
        line = next(textdoc)
        line = line.rstrip('\n')
        bins = line.split('\t')
        repgenlist.extend(bins[1:len(bins)-1])
        #initialize the repgen ids into dictionaries with zeros in them.
        for repgenid in repgenlist:
            parkcount[repgenid] = 0
            controlcount[repgenid] = 0
        #runs through the repgenids and counts for parkinsons
        for line in textdoc:
            line = line.rstrip('\n')
            counting = line.split('\t')
            val = counting[-1].strip()
            if val == '1.0':
                repcount(counting, parkcount)
                parktotal += 1
            else:
                repcount(counting, controlcount)
                controltotal += 1
        #Creates the percents for each repgenid in control and parkinsons
        for repgens in repgenlist:
            parkpercent = round(parkcount[repgens]/parktotal*100, 2)
            controlpercent = round(controlcount[repgens]/controltotal*100, 2)
            #writes the table for the repgens
            outtable.write(f"{repgens}\t {humanreadablename[repgens]}\t {parkcount[repgens]}\t {controlcount[repgens]}\t {parkpercent}\t {controlpercent}\n")
#goes through the repgenids and adds one to the count when it finds a 1.0
def repcount(line, diction):
    for i in range(1, len(line)-2, 1):
        val = line[i].strip()
        if val == '1.0':
            diction[repgenlist[i-1]] += 1 

    
namedict('rep100.names.tbl')
with open('ParkBinCount.tbl', 'w') as outtable:
    bincount('data.tbl', outtable)                   