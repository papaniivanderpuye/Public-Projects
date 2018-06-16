import random
import sys

#shuffles lines in generated data 

for i in range(0,100):
    lines1 = open("AAC/proteinsAAC" +str(i+1) + ".data",'r').readlines()
    lines2 = open("DPC/proteinsDPC" +str(i+1) + ".data",'r').readlines()
    lines3 = open("PAAC/proteinsPAAC" +str(i+1) + ".data",'r').readlines()
    
    c= list(zip(lines1,lines2,lines3))
    random.shuffle(c)
    lines1,lines2,lines3 = zip(*c)
    
    open("AAC/Train/proteinsAAC"+str(i+1) + ".train", 'w').writelines(lines1)
    open("DPC/Train/proteinsDPC"+str(i+1) + ".train", 'w').writelines(lines2)
    open("PAAC/Train/proteinsPAAC"+str(i+1) + ".train", 'w').writelines(lines3)


lines1 = open("independentTest/proteinsAAC.data",'r').readlines()
lines2 = open("independentTest/proteinsDPC.data",'r').readlines()
lines3 = open("independentTest/proteinsPAAC.data",'r').readlines()
c= list(zip(lines1,lines2,lines3))    
random.shuffle(c)    
lines1,lines2,lines3 = zip(*c)
open("independentTest/proteinsAAC.train", 'w').writelines(lines1)
open("independentTest/proteinsDPC.train", 'w').writelines(lines2)
open("independentTest/proteinsPAAC.train", 'w').writelines(lines3)
