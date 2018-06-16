inputFile = open("independent_protein_set.txt","r")
i =0
for line in inputFile:
    if('>' in line):
        
        if (line.startswith('>') == True):
           i +=1 
print(i)   
            
