import math
import sys
#calculates paac for every sequence in file

def aacSet(sequence,counts): #returns list with frequency of each letter
    #counts number of times each letter appears
    for aa in sequence:
             counts[aa] +=  1      
    #making list for recording numbers       
    myList =[]    
    #adding all numbers for frequency of each letter to the list
    for key in sorted(counts.keys()):
        myList.append(str( counts[key]) )    
    return myList
#checks if letters are the same
def deltaFunction(R1,R2):
    if (R1 == R2):
        return 1
    else:
        return 0
def deltaSet(sequence):    
    deltaSetList =[]
    L =len(sequence)
    myLambda = 10
    for i in range(myLambda):
        total = 0.0        
        #i am getting the letters calcultations of the sequence based on the formula in
        #the pdf jing hu sent me
        for j in range(L - (i+1)):            
            R1 = sequence[j]
            # I am adding one because i starts from 0
            #so it will not make sense considering the actual mathematical formula
            R2 = sequence[j +(i + 1)]             
            total += deltaFunction(R1,R2)
        deltaNumber = total/float(L-i)
        deltaSetList.append(str(deltaNumber))    
    return deltaSetList
#getting the actual values from the hydroFile

def getAAIndexValues(hydroInfoFile):
    alist=[]
    values = []
    fin= open(hydroInfoFile, "r")
    firstLine = True    
    for line in fin:
        if(firstLine):
            firstLine = False #moves on if it is the first line, otherwise, the values list will be empty before it calculates.

        elif ( 'A' not in line):
            newLine = line.rstrip('\n').rstrip('*').rstrip('\r')
            newList = newLine.split()
            for aa in newList:
                #adds all vallues to a list, order is as it was read
                values.append(float(aa))
        else:            
            #normalizes values
            mean = sum(values)/float(len(values))
            otherList =[(x-mean)**2 for x in values]
            deviation = math.sqrt( sum(otherList)/float(len(otherList)) )
            normalized = [(x-mean)/deviation for x in values]
            alist.append(normalized)            
            values=[]

    #copying the last lines
    mean = sum(values)/len(values)            
    otherList =[(x-mean)**2 for x in values]
    deviation = math.sqrt( sum(otherList)/len(otherList) )
    normalized = [(x-mean)/deviation for x in values]
    alist.append(normalized)
    values=[]            
    fin.close()    
    return alist
    
def hydroFunction(R1,R2,alist,indexDict):
    #uses the dictionary to get the index of each letter for the alist
    index1 = indexDict[R1]
    index2 = indexDict[R2]
    product = float(alist[index1]) * float(alist[index2])
    return product
    
def hydroSet(sequence,listOfAAindexes,indexDict):    
    hydroSetList =[]
    L =len(sequence)
    myLambda = 10
    for x in range(len(listOfAAindexes)):
        for i in range(myLambda):         
            total = 0.0;            
            #i am getting the letters calcultations of the sequence based on the formula in
            #the pdf jing hu sent me
            for j in range(L - (i+1)):                
                R1 = sequence[j]
                # I am adding one because i starts from 0
                #so it will not make sense considering the actual mathematical formula
                R2 = sequence[j +(i + 1)]
                total += hydroFunction(R1,R2,listOfAAindexes[x],indexDict)                
            hydroNumber = total/float(L-i)
            hydroSetList.append(str(hydroNumber))
    return hydroSetList

def helper(inputFile, output,number,hydroInfoFile):
    firstLine = True
    sequence =""
    listOfAAindexes = getAAIndexValues(hydroInfoFile) #get all 9 sets, list of dictionaries
    #this is for the hydro function
    indexDict = {'A':0,'R':1,'N':2,'D':3,'C':4,'Q':5,'E':6,'G':7,'H':8,'I':9,'L':10,'K':11,'M':12,'F':13,'P':14,'S':15,'T':16,'W':17,'Y':18,'V':19}
    x = 1
    for line in inputFile:
        if (line.startswith('>') == False):
            newLine = line.rstrip('\n').rstrip('*').rstrip('\r')
            sequence = sequence + newLine                
        else:
            # resitance number
            if firstLine:
                #do nothing and anticipate next line
                firstLine = False
            else:                
                output.write(number)
                dim = 1                
                #creat dictionary for aac function
                counts = { 'R':0,'K':0,'D':0,'E':0 ,'Q':0,'N':0, 'H':0, 'S':0, 'T':0, 'Y':0, 'C':0,'W':0 ,'A':0, 'I':0,'L':0, 'M':0, 'F':0, 'V':0,'P':0, 'G':0 }
                aacNum = aacSet(sequence,counts)
                deltaSetList = deltaSet(sequence)
                hydroSetList = hydroSet(sequence,listOfAAindexes,indexDict)
                #this writes the first 20 aac numbers
                for value in aacNum:
                    output.write( " " + str(dim) + ":" +  value)
                    dim += 1
                #this writes the delta set
                for key in deltaSetList:
                    output.write( " " + str(dim) + ":" +  key)
                    dim += 1
                #this writes the hydro set
                for key in hydroSetList:
                    output.write( " " + str(dim) + ":" +  key)
                    dim += 1                    
                output.write('\n')                
                #reset sequence
                sequence = ""
    #for last sequence
    output.write(number)
    dim = 1                
    #creat dictionary for aac function
    counts = { 'R':0,'K':0,'D':0,'E':0 ,'Q':0,'N':0, 'H':0, 'S':0, 'T':0, 'Y':0, 'C':0,'W':0 ,'A':0, 'I':0,'L':0, 'M':0, 'F':0, 'V':0,'P':0, 'G':0 }
    aacNum = aacSet(sequence,counts)
    deltaSetList = deltaSet(sequence)
    hydroSetList = hydroSet(sequence,listOfAAindexes,indexDict)
    #this writes the first 20 aac numbers
    for value in aacNum:
        output.write( " " + str(dim) + ":" +  value)
        dim += 1
    #this writes the delta set
    for key in deltaSetList:
        output.write( " " + str(dim) + ":" +  key)
        dim += 1
    #this writes the hydro set
    for key in hydroSetList:
        output.write( " " + str(dim) + ":" +  key)
        dim += 1                    
    output.write('\n')                
    #reset sequence
    sequence = "" 
    #I did not put a return at the end becuase it seems like it rewrites the whole output
    #file when it starts again for the -1 labels

def main():
    h = "Hydrophobicity/hydroInfoFile.txt"    
    for i in range(0,100):
        print("generating paac...."+ str(i) + "%",end='\r',flush=True)
        i1 = open("Samples/resistant-sample" + str(i+1) + ".txt","r")
        i2 = open("Samples/nonresistant-sample" + str(i+1) + ".txt","r")
        o = open("PAAC/proteinsPAAC" +str(i+1) + ".data","w")            
        helper(i1,o,"1", h)
        helper(i2,o,"-1", h)
        i1.close()
        i2.close()
        o.close()
    i1 = open("originalData/resist_protein.txt","r")
    i2 = open("originalData/notresist_protein.txt","r")
    o = open("independentTest/proteinsPAAC.data","w")            
    helper(i1,o,"1", h)
    helper(i2,o,"-1", h)
    i1 = open("originalData/independent_protein_set.txt","r")
    o = open("independentTest/proteinsPAAC.test","w")            
    helper(i1,o,"1", h)
    i1.close()
    i2.close()
    o.close()
    
        
main()
