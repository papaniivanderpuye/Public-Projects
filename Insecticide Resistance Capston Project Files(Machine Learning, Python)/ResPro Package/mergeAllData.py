import math
import sys

#code for generateing AAC,DPC,PAAC combined

def aacSet(sequence,counts): #returns list with frequency of each letter
    #counts number of times each letter appears
    for aa in sequence:
             counts[aa] +=  1      
    #making list for recording numbers       
    myList =[]
    #adding all numbers for frequency of each letter to the list
    for key in sorted(counts.keys()):
        myList.append(counts[key])        
    return myList

def dpcSet(sequence,dipCounts): #returns list with frequency of each 2 letters
    for aa in sequence:
        for bb in sequence:
            dipCounts[str(aa+bb)] += 1      
    #making list for recording numbers       
    myList =[]    
    #adding all numbers for frequency of each 2 letters to the list
    for key in sorted(dipCounts.keys()):
        myList.append(dipCounts[key])
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
        #I am getting the letters calcultations of the sequence based on the formula in
        #the pdf jing hu sent me
        for j in range(L - (i+1)):            
            R1 = sequence[j]
            #I am adding one because i starts from 0 
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
            mean = sum(values)/len(values)
            otherList =[(x-mean)**2 for x in values]
            deviation = math.sqrt( sum(otherList)/len(otherList) )
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
    
            

def helper(inputFile,output,number,hydroInfoFile):
    firstLine = True
    sequence =""
    listOfAAindexes = getAAIndexValues(hydroInfoFile) #get all 9 sets, list of dictionaries
    #this is for the hydro function
    indexDict = {'A':0,'L':1,'R':2,'K':3,'N':4,'M':5,'D':6,'F':7,'C':8,'P':9,'Q':10,'S':11,'E':12,'T':13,'G':14,'W':15,'H':16,'Y':17,'I':18,'V':19}
    
    for line in inputFile:
        if (line.startswith('>') == False):
            newLine = line.rstrip('\n').rstrip('*').rstrip('\r')
            sequence = sequence + newLine
        else:
            
            if firstLine:
                #do nothing and anticipate next line
                firstLine = False
            else:
                output.write(number)
                dim = 1
                #creat dictionary for aac function
                counts = { 'R':0,'K':0,'D':0,'E':0 ,'Q':0,'N':0, 'H':0, 'S':0, 'T':0, 'Y':0, 'C':0,'W':0 ,'A':0, 'I':0,'L':0, 'M':0, 'F':0, 'V':0,'P':0, 'G':0 }                
                dipCounts = {}
                for i in sorted(counts.keys()):
                    for j in sorted(counts.keys()):
                        dipCounts[str(i+j)] = 0    
                aacNum = aacSet(sequence,counts)
                dpcNum = dpcSet(sequence,dipCounts)
                deltaSetList = deltaSet(sequence)                
                hydroSetList = hydroSet(sequence,listOfAAindexes,indexDict)
                for value in aacNum:
                    output.write( " " + str(dim) + ":" +  str(value))
                    dim += 1
                for value in dpcNum:
                    output.write( " " + str(dim) + ":" +  str(value))
                    dim += 1
                for key in deltaSetList:
                    output.write( " " + str(dim) + ":" +  str(key))
                    dim += 1
                for key in hydroSetList:
                    output.write( " " + str(dim) + ":" +  str(key))
                    dim += 1
                output.write('\n')
                sequence = ""
    #for last sequence
    output.write(number)
    dim = 1
    #creat dictionary for aac function
    counts = { 'R':0,'K':0,'D':0,'E':0 ,'Q':0,'N':0, 'H':0, 'S':0, 'T':0, 'Y':0, 'C':0,'W':0 ,'A':0, 'I':0,'L':0, 'M':0, 'F':0, 'V':0,'P':0, 'G':0 }                
    dipCounts = {}
    for i in sorted(counts.keys()):
        for j in sorted(counts.keys()):
            dipCounts[str(i+j)] = 0    
    aacNum = aacSet(sequence,counts)
    dpcNum = dpcSet(sequence,dipCounts)
    deltaSetList = deltaSet(sequence)                
    hydroSetList = hydroSet(sequence,listOfAAindexes,indexDict)
    for value in aacNum:
        output.write( " " + str(dim) + ":" +  str(value))
        dim += 1
    for value in dpcNum:
        output.write( " " + str(dim) + ":" +  str(value))
        dim += 1
    for key in deltaSetList:
        output.write( " " + str(dim) + ":" +  str(key))
        dim += 1
    for key in hydroSetList:
        output.write( " " + str(dim) + ":" +  str(key))
        dim += 1
    output.write('\n')
    sequence = ""  

def main():
    h = "Hydrophobicity/hydroInfoFile.txt"
    
    for i in range(0,100):
        print("generating combined data..."+ str(i) + "%",end='\r',flush=True)
        i1 = open("Samples/resistant-sample" + str(i+1) + ".txt","r")
        i2 = open("Samples/nonresistant-sample" + str(i+1) + ".txt","r")
        o = open("Combined/proteinsCombined" +str(i+1) + ".data","w")    
        
        helper(i1,o,"1", h)
        helper(i2,o,"-1", h)

        i1.close()
        i2.close()
        o.close()
        
main()
