import random

#generates a 100 random samples of data

fin1 = open("originalData/resist_protein.txt", "r")
fin2 = open("originalData/notresist_protein.txt", "r")

def helper(inputFile):
    firstLine = True
    newList = []
    for line in inputFile:
        if (line.startswith('>')):
            newList.append(line)
        else:
            newList[-1] = newList[-1] + line           
    return newList
                 
resistant = helper(fin1)
nonresistant =  helper(fin2)        
for i in range(0, 100):
    resistantSample =random.sample(resistant, 128)
    nonresistantSample =random.sample(nonresistant, 128)    
    open("Samples/resistant-sample" + str(i+1) + ".txt", 'w').writelines(resistantSample)
    open("Samples/nonresistant-sample" + str(i+1)+ ".txt", 'w').writelines(nonresistantSample)
