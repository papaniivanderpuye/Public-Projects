import numpy as np
import os
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
    fin1 = open("AAC/Train/proteinsAAC" +str(f+1) + ".train", "r")
    fin2 = open("DPC/Train/proteinsDPC" +str(f+1) + ".train", "r")
    fin3 = open("PAAC/Train/proteinsPAAC" +str(f+1) + ".train", "r")
    #dataWrite = open("dataWrite3.train", "w")
    #testWrite = open("testWrite3.data", "w")
    listFin1 = fin1.read().splitlines() 
    listFin2 = fin2.read().splitlines() 
    listFin3 = fin3.read().splitlines() 
    numOfLines1 = len(listFin1)
    numOfLines2 = len(listFin2)
    numOfLines3 = len(listFin3)
    groups1 = np.array_split(listFin1, 10)
    groups2 = np.array_split(listFin2, 10)
    groups3 = np.array_split(listFin3, 10)
    TPlist = []
    FPlist = []
    TNlist = []
    FNlist = []
    
    #cross validation
    for i in range(len(groups1)): 
        dataWrite1 = open("AAC/SVMResults/dataWrite.train", "w")
        dataWrite2 = open("DPC/SVMResults/dataWrite2.train", "w")
        dataWrite3 = open("PAAC/SVMResults/dataWrite3.train", "w")
        testWrite1 = open("AAC/SVMResults/testWrite.data", "w")
        testWrite2 = open("DPC/SVMResults/testWrite2.data", "w")
        testWrite3 = open("PAAC/SVMResults/testWrite3.data", "w")
        
        for j in range(len(groups1)):
            if (j != i):
                for line in groups1[j]:    
                    dataWrite1.write(line + '\n')
                for line in groups2[j]:    
                    dataWrite2.write(line + '\n')
                for line in groups3[j]:    
                    dataWrite3.write(line + '\n')
        test1= groups1[i]
        test1 = [n.split() for n in test1]
        testTarget1 = [n[0] for n in test1]
        testData1 = [" ".join(n) for n in test1]
        test2= groups2[i]
        test2 = [n.split() for n in test2]
        testTarget2 = [n[0] for n in test2]
        testData2 = [" ".join(n) for n in test2]
        test3= groups3[i]
        test3 = [n.split() for n in test3]
        testTarget3 = [n[0] for n in test3]
        testData3 = [" ".join(n) for n in test3]

        #count = 0
        for line in testData1:
            testWrite1.write(line + '\n')
        for line in testData2:
            testWrite2.write(line + '\n')
        for line in testData3:
            testWrite3.write(line + '\n')

        dataWrite1.close()
        testWrite1.close()
        dataWrite2.close()
        testWrite2.close() 
        dataWrite3.close()
        testWrite3.close() 
    
        #need all values
        print("Training and Testing....." + str(f),end='\r',flush=True)        
        subprocess.call("./svm-train -c 2 -g 0.001953125 AAC/SVMResults/dataWrite.train", stdout=subprocess.PIPE,shell=True)
        subprocess.call("./svm-predict AAC/SVMResults/testWrite.data dataWrite.train.model AAC/SVMResults/results.out", stdout=subprocess.PIPE,shell=True)
        subprocess.call("./svm-train -c 2 -g 0.5 DPC/SVMResults/dataWrite2.train", stdout=subprocess.PIPE,shell=True)
        subprocess.call("./svm-predict DPC/SVMResults/testWrite2.data dataWrite2.train.model DPC/SVMResults/results2.out", stdout=subprocess.PIPE,shell=True)
        subprocess.call("./svm-train -c 2 -g 0.001953125 PAAC/SVMResults/dataWrite3.train", stdout=subprocess.PIPE,shell=True)
        subprocess.call("./svm-predict PAAC/SVMResults/testWrite3.data dataWrite3.train.model PAAC/SVMResults/results3.out", stdout=subprocess.PIPE,shell=True)

        resultFile1 = open("AAC/SVMResults/results.out", "r")
        resultFile2 = open("DPC/SVMResults/results2.out", "r")
        resultFile3 = open("PAAC/SVMResults/results3.out", "r")        
        results1 = resultFile1.read().splitlines()
        results2 = resultFile2.read().splitlines()
        results3 = resultFile3.read().splitlines()
        TP = 0
        FP = 0
        TN = 0
        FN = 0
    
        #record tp etc
        for p in range(len(results1)):
            #finds the popular vote on whether it is resistant or not
            verdict= [ results1[p],results2[p],results3[p] ]
            results = max(set(verdict), key=verdict.count)
                
            if results==testTarget1[p]=='1':
                TP += 1
            if results=='1' and testTarget1[p]!=results:
               FP += 1
            if testTarget1[p]==results=='-1':
               TN += 1    
            if results=='-1' and testTarget1[p]!=results:
               FN += 1

        TPlist.append(TP)
        FPlist.append(FP)
        TNlist.append(TN)
        FNlist.append(FN)
        resultFile1.close()
        resultFile2.close()
        resultFile3.close()
    
    #calculate average tp
    TP = float(sum(TPlist)) / (len(TPlist) )
    FP = float(sum(FPlist)) / (len(FPlist) )
    TN = float(sum(TNlist)) / (len(TNlist))
    FN = float(sum(FNlist)) / (len(FNlist))
    
    """"
    print("TP: ",TP)
    print("FP: ",FP)
    print("TN: ",TN)
    print("FN: ",FN)
    
    print("Sensitivity: ",TP/(TP+FN) )
    print("Specificity: ",TN/(TN+FP) )
    print("Accuracy: ",(TP+TN)/(TP+FP+FN+TN))
    print("Precision: ",TP/(TP+FP))
    print("MCC: ",( (TP * TN) - (FP * FN))/ ((TP + FP) * (FN + TN) * (FP + TN) * (TP + FN))**(0.5)  )
    """
    
    SensitivityList.append(TP/(TP+FN)) 
    SpecificityList.append(TN/(TN+FP))
    PrecisionList.append(TP/(TP+FP))
    AccuracyList.append((TP+TN)/(TP+FP+FN+TN)) 
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
