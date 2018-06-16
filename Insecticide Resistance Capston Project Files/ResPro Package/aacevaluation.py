import platform
import numpy as np
import sys
import subprocess
import math

#code for running and evaluating cross validation

def findDeviation(values):
    mean = sum(values)/float(len(values))            
    otherList =[(x-mean)**2 for x in values]
    deviation = math.sqrt( sum(otherList)/float(len(otherList)) )
    return deviation

SensitivityList = []
SpecificityList = []
PrecisionList = []
AccuracyList = []
MCCList = []

for f in range(0,100):
    #get processed file
    fin1 = open("AAC/Train/proteinsAAC"+str(f+1) + ".train", "r")    
    listFin = fin1.read().splitlines() 
    numOfLines = len(listFin)
    groups = np.array_split(listFin, 10)
    TPlist = []
    FPlist = []
    TNlist = []
    FNlist = []    
    #cross validation
    for i in range(len(groups)): 
        dataWrite = open("AAC/SVMResults/dataWrite.train", "w")
        testWrite = open("AAC/SVMResults/testWrite.data", "w")
        for j in range(len(groups)):
            if (j != i):
                for line in groups[j]: 
                    dataWrite.write(line + '\n')
        test= groups[i]
        test = [n.split() for n in test]
        testTarget = [n[0] for n in test]
        testData = [" ".join(n) for n in test]
        count = 0
        for line in testData:
            testWrite.write(line + '\n')
        testWrite.close()
        dataWrite.close()
        print("Training and Testing....." + str(f),end='\r',flush=True)        
        subprocess.call("./svm-train -c 2 -g 0.001953125 AAC/SVMResults/dataWrite.train", stdout=subprocess.PIPE,shell=True)
        print("Training and Testing...  " + str(f),end='\r',flush=True)
        subprocess.call("./svm-predict AAC/SVMResults/testWrite.data dataWrite.train.model AAC/SVMResults/results.out", stdout=subprocess.PIPE,shell=True)
        resultFile = open("AAC/SVMResults/results.out", "r")
        results = resultFile.read().splitlines()  
        TP = 0
        FP = 0
        TN = 0
        FN = 0
        #record tp etc
        for p in range(len(results)):            
            if results[p]==testTarget[p]=='1':
                TP += 1                
            if results[p]=='1' and testTarget[p]!=results[p]:
               FP += 1
            if testTarget[p]==results[p]=='-1':
               TN += 1
            if results[p]=='-1' and testTarget[p]!=results[p]:
               FN += 1    
        TPlist.append(TP)
        FPlist.append(FP)
        TNlist.append(TN)
        FNlist.append(FN)
        dataWrite.close()
        testWrite.close() 
        resultFile.close()
    #calculate average tp
    TP = float(sum(TPlist)) / (len(TPlist) )
    FP = float(sum(FPlist)) / (len(FPlist) )
    TN = float(sum(TNlist)) / (len(TNlist))
    FN = float(sum(FNlist)) / (len(FNlist))        
    """
    print("TP: ",TP)
    print("FP: ",FP)
    print("TN: ",TN)
    print("FN: ",FN)
    
    print("Sensitivity: ",TP/(TP+FN) )
    print("Specificity: ",TN/(TN+FP) )
    print("precision: ",TP/(TP+FP))
    print("Accuracy: ",(TP+TN)/(TP+FP+FN+TN))
    print("MCC: ",( (TP * TN) - (FP * FN))/ ((TP + FP) * (FN + TN) * (FP + TN) * (TP + FN))**(0.5)  )
    """    
    SensitivityList.append(TP/(TP+FN)) 
    SpecificityList.append(TN/(TN+FP))
    PrecisionList.append(TP/(TP+FP))
    AccuracyList.append((TP+TN)/(TP+FP+FN+TN) )     
    if(TP==0 or TN==0 or FP == 0 or FN ==0):
        MCCList.append( ( (TP * TN) - (FP * FN))/ 1  )
    else:   
        MCCList.append( ( (TP * TN) - (FP * FN))/ ( (TP + FP) * (FN + TN) * (FP + TN) * (TP + FN) )**(0.5)  )
#calculate average evaluations
Sensitivity = float(sum(SensitivityList)) / (len(SensitivityList) )
Specificity = float(sum(SpecificityList)) / (len(SpecificityList) )
Precision = float(sum(PrecisionList)) / (len(PrecisionList) )
Accuracy = float(sum(AccuracyList)) / (len(AccuracyList) )
MCC = float(sum(MCCList)) / (len(MCCList) )
print("Sensitivity: ",round(Sensitivity,3),"±",round(findDeviation(SensitivityList),3) )
print("Specificity: ",round(Specificity,3),"±",round(findDeviation(SpecificityList),3) )
print("Accuracy: ",round(Accuracy,3),"±",round(findDeviation(AccuracyList),3) )
print("Precision: ",round(Precision,3),"±",round(findDeviation(PrecisionList),3) )
print("MCC: ",round(MCC,3)  ,"±",round(findDeviation(MCCList),3) )
