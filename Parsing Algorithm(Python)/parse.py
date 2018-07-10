import  csv
import datetime
from operator import itemgetter

#makes sure string formats are similar
def correction(sl):
    if sl[2] == "F":
        sl[2]= "Female"
    if sl[2] == "M":
        sl[2]= "Male"
    if "-" in sl[3]:
        sl[3] = sl[3].replace("-","/")
    return sl

#reads all input files makes sure list formats are similar       
def readFiles(input1,input2, input3):
    list1 = input1.readlines()
    list2 = input2.readlines()
    list3 = input3.readlines()    
    lineList = list1 +list2 + list3
    listsToOrder = []
    for line in lineList:
        stringList = []
        line = line.replace("\n", "")
        if "|" in line:            
            line = line.replace(" ","")          
            stringList = line.split('|')
            formatList = [stringList[0],stringList[1],stringList[3],stringList[5],stringList[4]]
            formatList = correction(formatList)           
        elif ',' in line:
            line = line.replace(" ","")
            stringList = line.split(',')
            formatList = [stringList[0],stringList[1],stringList[2],stringList[4],stringList[3]]
            formatList = correction(formatList)          
        else:
            stringList = line.split(' ')
            formatList = [stringList[0],stringList[1],stringList[3],stringList[4],stringList[5]]
            formatList = correction(formatList)              
        listsToOrder.append(formatList)
    return listsToOrder
    
#sorts by gender   
def byGender(iList):    
    sortedByName = sorted(iList, key=itemgetter(0))
    sortedByGender = sorted(sortedByName, key=itemgetter(2))    
    return sortedByGender
    
#sorts by date    
def byBirthDate(iList):    
    sortedByName = sorted(iList, key=itemgetter(0))
    #sortedByBirth = sorted(sortedByName, key=itemgetter(3))
    sortedByBirth = sorted(sortedByName, key=lambda x: datetime.datetime.strptime(x[3], "%m/%d/%Y"))
    return sortedByBirth

#sorts by name    
def byLastName(iList):    
    sortedByName = sorted(iList, key=itemgetter(0),reverse=True)
    return sortedByName

#this outputs the the lists to a given file
def writeToFile(list1,list2,list3,o):
    bigList = [list1,list2,list3]
    for i in range(0,3,1):
        list = bigList[i]
        o.write("Output " + str(i+1)+ ":" + "\n")
        for l in list:
            st = " ".join(l)
            o.write(st + "\n")
        if (i < 2):
            o.write("\n")
    return

#this is the main program that executes all functions
#it reads the three files, sorts them in the respective orders
#and outputs them in a file        
def parseFiles():
    f1 = open("space.txt", "r")
    f2 = open("comma.txt", "r")
    f3 = open("pipe.txt", "r")
    o = open("target_output.txt","w")  
    iList = readFiles(f1,f2,f3)
    
    #sorting
    genderOrder = byGender(iList)
    birthOrder = byBirthDate(iList)
    nameOrder = byLastName(iList) 
    
    #output
    writeToFile(genderOrder,birthOrder,nameOrder,o)
    

    

    
    
