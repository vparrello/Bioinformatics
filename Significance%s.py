'''
Created on Jun 1, 2021

@author: fig
'''
repgens = {}
#key is the repgen id and the value is the number of parkinsons and controls in a tuple.
parktotal = 0
rowtotal = 0

#function to create the dictionary of repgen IDs
def repgenlist(Matrixfile):
    #list of the repgen ids in order.
    repgenindex = ()
    with open(Matrixfile, 'r') as masterlist: 
        for sample in masterlist:
            sample = sample.rstrip('\n')
            collum = sample.split('\t') 
            if collum[0] == 'sample':
                repgenindex = collum[1:len(collum)-1]
                for repgenid in repgenindex:
                    repgens[repgenid] = [0,0]
            else:
                global parktotal
                global rowtotal
                parkindex = int(float(collum[len(collum)-1]))
                parktotal += parkindex 
                rowtotal += 1
                for collumnindex in range(1,len(collum)-1):
                    if collum[collumnindex] == '1':
                        repgenid = repgenindex[collumnindex-1]
                        tuplething = repgens[repgenid]
                        tuplething[parkindex] += 1
                        
def signiflist():
    controltotal = rowtotal - parktotal
    with open('SignificanceTable.tbl', 'w') as outtable:
        headerrow = 'RepGenID' + '\tAlzheimersTotal' + '\tControlTotal' + '\tAlzheimersPercent' + '\tControlPercent' + '\n'
        outtable.write(headerrow)
        for repgenid in repgens:
            repgenlist = repgens[repgenid]
            #create a row of numbers based on the totals and parkinsons stuff
                       
            
          
repgenlist('Xmatrix.tbl')
signiflist()  
print('All done!')