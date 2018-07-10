import sys
#calculates dpc for every sequence in file
def helper(inputFile,output,number,dipCounts):
    firstLine = True
    for line in inputFile:
        if (line.startswith('>') == False):
            newLine = line.rstrip('\n').rstrip('*').rstrip('\r')
            for aa in newLine:
                for bb in newLine:
                    dipCounts[str(aa+bb)] += 1
        else:
             # resitance number
            if firstLine:
                #do nothing and anticipate next line
                firstLine = False
            else :
                output.write(number)
                dim = 1
                for key in sorted(dipCounts.keys()):
                    output.write( " " + str(dim) + ":" +  str(  dipCounts[key]/400.0    )   )
                    dim += 1
                output.write('\n')
                #reset counts
                dipCounts = {x:1 for x in dipCounts}
    #for last sequence
    output.write(number)
    dim = 1
    for key in sorted(dipCounts.keys()):
        output.write( " " + str(dim) + ":" +  str(  dipCounts[key]/400.0    )   )
        dim += 1
    output.write('\n')
    #reset counts
    dipCounts = {x:1 for x in dipCounts}

def dpc(inputfilename1,inputfilename2, outputfilename):
    fin1 = open(inputfilename1, "r")
    fin2 = open(inputfilename2, "r")
    fout = open(outputfilename, "w")
    order = []
    sequences = {}
    counts = { 'R':0,'K':0,'D':0,'E':0 ,'Q':0,'N':0, 'H':0, 'S':0, 'T':0, 'Y':0, 'C':0,'W':0 ,'A':0, 'I':0,'L':0, 'M':0, 'F':0, 'V':0,'P':0, 'G':0 }
   
    dipCounts = {}
    for i in sorted(counts.keys()):
         for j in sorted(counts.keys()):
             dipCounts[str(i+j)] = 0

    helper(fin1,fout,"1",dipCounts)
    helper(fin2,fout,"-1",dipCounts)
    fin1.close()
    fin2.close()
    fout.close()
    



def main():
    
    for i in range(0,100):
        print("generating dpc.... "+ str(i) + "%",end='\r',flush=True)
        i1 = "Samples/resistant-sample" + str(i+1) + ".txt"
        i2 = "Samples/nonresistant-sample" + str(i+1) + ".txt"
        o = "DPC/proteinsDPC" +str(i+1) + ".data"    
        dpc(i1,i2,o)

    i1 = "originalData/resist_protein.txt"
    i2 = "originalData/notresist_protein.txt"
    o = "independentTest/proteinsDPC.data"    
    dpc(i1,i2,o)

    i1 = "originalData/independent_protein_set.txt"
    i2 = "originalData/blank.txt"
    o = "independentTest/proteinsDPC.test"    
    dpc(i1,i2,o)
    
main()

