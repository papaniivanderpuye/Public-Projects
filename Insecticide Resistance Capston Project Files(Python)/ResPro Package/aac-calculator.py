import sys

#calculates aac for every sequence in file
def helper(inputFile,output,number,counts):
    firstLine = True
    lastLine= False
    
    for line in inputFile:
        if (line.startswith('>') == False):
            newLine = line.rstrip('\n').rstrip('*').rstrip('\r')
            for aa in newLine:
                counts[aa] +=  1                
        else:
            if firstLine:
                firstLine = False
            else : 
                output.write(number)
                dim = 1
                for key in sorted(counts.keys()): #check this
                    output.write( " " + str(dim) + ":" +  str(counts[key]))
                    dim += 1
                output.write('\n')
                #reset counts
                counts = {x:0 for x in counts}
    #for last sequence
    output.write(number)
    dim = 1
    for key in sorted(counts.keys()): #check this
        output.write( " " + str(dim) + ":" +  str(counts[key]))
        dim += 1
    output.write('\n')
    counts = {x:0 for x in counts} #change it to x:0       counts = {x:0 for x in counts} #change it to x:0 
        
def aac(inputfilename1,inputfilename2, outputfilename):
    
    fin1 = open(inputfilename1, "r")
    fin2 = open(inputfilename2, "r")
    fout = open(outputfilename, "w")
    order = []
    sequences = {}
    counts = { 'R':0,'K':0,'D':0,'E':0 ,'Q':0,'N':0, 'H':0, 'S':0, 'T':0, 'Y':0, 'C':0,'W':0 ,'A':0, 'I':0,'L':0, 'M':0, 'F':0, 'V':0,'P':0, 'G':0 }

    helper(fin1,fout,"1",counts)
    helper(fin2,fout,"-1",counts)
    fin1.close()
    fin2.close()
    fout.close()

def main():
    
    for i in range(0,100):
        print("generating aac...."+ str(i) + "%",end='\r',flush=True)
        i1 = "Samples/resistant-sample" + str(i+1) + ".txt"
        i2 = "Samples/nonresistant-sample" + str(i+1) + ".txt"
        o = "AAC/proteinsAAC" +str(i+1) + ".data"    
        aac(i1,i2,o)

    i1 = "originalData/resist_protein.txt"
    i2 = "originalData/notresist_protein.txt"
    o = "independentTest/proteinsAAC.data"    
    aac(i1,i2,o)

    i1 = "originalData/independent_protein_set.txt"
    i2 = "originalData/blank.txt"
    o = "independentTest/proteinsAAC.test"    
    aac(i1,i2,o)
    
main()

