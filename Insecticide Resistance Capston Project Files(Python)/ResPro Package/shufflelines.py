import random
import sys

#shuffles lines

for i in range(0,100):
    lines = open("Combined/proteinsCombined"+str(i +1) + ".data",'r').readlines()
    random.shuffle(lines)
    open("Combined/Train/proteinsCombined"+str(i +1) + ".train", 'w').writelines(lines)
