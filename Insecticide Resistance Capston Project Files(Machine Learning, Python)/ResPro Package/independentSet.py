import numpy as np
import os
import sys
import subprocess

#testing ensemble on an independent set

subprocess.call("./svm-train -c 2 -g 0.001953125 independentTest/proteinsAAC.train", stdout=subprocess.PIPE,shell=True)
subprocess.call("./svm-predict independentTest/proteinsAAC.test proteinsAAC.train.model independentTest/results.out", stdout=subprocess.PIPE,shell=True)
        
subprocess.call("./svm-train -c 2 -g 0.5 independentTest/proteinsDPC.train", stdout=subprocess.PIPE,shell=True)
subprocess.call("./svm-predict independentTest/proteinsDPC.test proteinsDPC.train.model independentTest/results2.out", stdout=subprocess.PIPE,shell=True)

subprocess.call("./svm-train -c 2 -g 0.001953125 independentTest/proteinsPAAC.train", stdout=subprocess.PIPE,shell=True)
subprocess.call("./svm-predict independentTest/proteinsPAAC.test proteinsPAAC.train.model independentTest/results3.out", stdout=subprocess.PIPE,shell=True)
        
        
resultFile1 = open("independentTest/results.out", "r")
resultFile2 = open("independentTest/results2.out", "r")
resultFile3 = open("independentTest/results3.out", "r")
results1 = resultFile1.read().splitlines()
results2 = resultFile2.read().splitlines()
results3 = resultFile3.read().splitlines()
fin1 =  open("independentTest/proteinsPAAC.test", "r")
listFin1 = fin1.read().splitlines()
testTarget1 = [n[0] for n in listFin1]

TP = 0
FP = 0
TN = 0
FN = 0
    
#record tp etc
for p in range(len(results3)):
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
        
print("Number Predicted Correctly: ",TP)
print("Number Predicted InCorrectly",FN)
