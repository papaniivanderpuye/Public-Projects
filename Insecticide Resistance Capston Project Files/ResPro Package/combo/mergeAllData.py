#code
import math

def aacSet(sequence,counts): #returns list with frequency of each letter

    #counts number of times each letter appears
    for aa in sequence:
             counts[aa] +=  1
      
    #making list for recording numbers       
    myList =[]
    
    #adding all numbers for frequency of each letter to the list
    for key in sorted(counts.iterkeys()):
        myList.append(counts[key])
        
    return myList

def dpcSet(sequence,dipCounts): #returns list with frequency of each 2 letters

    for aa in sequence:
        for bb in sequence:
            dipCounts[str(aa+bb)] += 1
      
    #making list for recording numbers       
    myList =[]
    
    #adding all numbers for frequency of each 2 letters to the list
    for key in sorted(dipCounts.iterkeys()):
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
    for i in range(L-1):
     
        total = 0.0
        
        #i am getting the letters calcultations of the sequence based on the formula in
        #the pdf jing hu sent me
        for j in range(L - i ):
            
            R1 = sequence[j]
            
            # I am adding one because i starts from 0 
            #so it will not make sense considering the actual mathematical formula
            R2 = sequence[j +i + 1] 
            
            total += deltaFunction(R1,R2)
            
        deltaNumber = total/float(L-i)
        deltaSetList.append(deltaNumber)
    
    return deltaSetList
    

#getting the actual values from the hydroFile
def getAAIndexValues(hydroInfoFile):
    alist=[]
    values = []
    fin= open(hydroInfoFile, "r")
    
    for line in fin:
        if ( line.contains('A')== False ):
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
            
    fin.close()
    
    return alist
    
    
    
    
    
def hydroFunction(R1,R2,alist,valueDict):
    
    #uses the dictionary to get the index of each letter for the alist
    index1 = indexDict[R1]
    index2 = indexDict[R2]
    
    product = float(alist[index1]) * float(alist[index2])
    
    return hydroFunction
    
    
def hydroSet(sequence,hydroInfoFile,listOfAAindexes,indexDict):
    
    hydroSetList =[]
    L =len(sequence)
    
        
   
    
    for x in range(len(listOfAAindexes)):
        for i in range(L-1):
         
            total = 0;
            
            #i am getting the letters calcultations of the sequence based on the formula in
            #the pdf jing hu sent me
            for j in range(L - i ):
                
                R1 = sequence[j]
                
                # I am adding one because i starts from 0 
                #so it will not make sense considering the actual mathematical formula
                R2 = sequence[j +i + 1] 
                
                total += hydroFunction(R1,R2,listOfAAindexes[x],indexDict)
                
            hydroNumber = total/(L-i)
            hydroSetList.append(hydroNumber)
    
    return hydroSetList
    
            

def helper(inputFile,output,number,counts,hydroInfoFile):
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
            # resitance number
            if firstLine:
                #do nothing and anticipate next line
                firstLine = False
                
            #it is not the a sequence name, 
            #it is the now looking at the next sequence, so now it 
            #is needs to record the last data it collected from the 
            #the last sequence before it moves on. that is what the code below does.
            else:
                
                
                
                #this writes the number 1 or -1 to show whether it is 
                #resistant or not
                output.write(number)
                
                #this is to record the dimenstion number on the file for 
                #the svm
                dim = 1
                
                #creat dictionary for aac function
                counts = { 'R':0,'K':0,'D':0,'E':0 ,'Q':0,'N':0, 'H':0, 'S':0, 'T':0, 'Y':0, 'C':0,'W':0 ,'A':0, 'I':0,'L':0, 'M':0, 'F':0, 'V':0,'P':0, 'G':0 }
                
                dipCounts = {}
                for i in sorted(counts.iterkeys()):
                    for j in sorted(counts.iterkeys()):
                        dipCounts[str(i+j)] = 0
    
                #this gets the acc numbers
                aacNum = aacSet(sequence,counts)
            
                #this gets the acc numbers
                dpcNum = aacSet(sequence,dipCounts)
                
                #get list of delta set
                deltaSetList = deltaSet(sequence)
                
                #this gets the hydro set
                hydroSetList = hydroSet(sequence,hydroInfoFile)
                
                
                
                #this writes the first 20 aac numbers
                for value in aacNum:
                    output.write( " " + str(dim) + ":" +  value)
                    dim += 1
                
                
                #this writes the first 20 aac numbers
                for value in dpcNum:
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
                
    return 0

    

def main():
    i1 = sys.argv[1]
    i2 = sys.argv[2]
    o = sys.argv[3]
    o = sys.argv[4]

    helper(i1,o,number,counts,h)
    helper(i2,o,number,counts,h)

    
main()