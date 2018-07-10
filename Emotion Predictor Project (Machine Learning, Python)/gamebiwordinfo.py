def main():
    print("working ")
    edict = {'happiness':0,'relief':0,'fun':0,'enthusiasm':0,'love':0,'sadness':0,'hate':0,'worry':0,'anger':0,'surprise':101,'empty':0,'neutral':101,'boredom':0}

    pos =[]
    neg =[]
    fpos =open('pos.txt','r')
    for line in fpos:
        line = line.replace('\n','')
        if ';' not in line and line!= '':
            pos.append(line)
    fpos.close()
    fneg = open('neg.txt','r')
    for line in fneg:
        line = line.replace('\n','')
        if ';' not in line and line!= '':
            neg.append(line)
    fneg.close()
    #edict = {'1': 0,'0': 0}
    wdict = {'@':0}
    doubleword = {}
    f1= open('data.txt','r')
    f1.readline()

    for line in f1:
        line = line.replace('\n','')
        ln = line.split('\t')
        #print(ln[3])

        tot = 0
        for item in edict:
            tot+= edict[item]
        if tot >1313:
            break

        '''
        wrt =True
        if len(ln)<4:
            wrt = False
            ln=['1','1','a','a']
        '''

      
                        
    f1.close()

    savedwords =  open('savedwords.txt','r')
    totlist= savedwords.read().splitlines() 
    print(len(totlist))
    #print(edict)
    #print(totlist)
    
    f2 =  open('data.txt','r')
    f2.readline()
    f3 = open('factors.csv','w')

    newList=totlist[:]



    newList.extend([".","comma","!","?", "char Count", "positive words","negative words","sentiment"])
    labels = '","'.join(newList)
    labels = '"' + labels + '"' + '\n'
    f3.write(labels)
     


    
    for line in f2:
        #print(line)
        binary =[]
        for i in range(len(totlist)):
            binary.append('0')
        line = line.replace('\n','')
        ln = line.split('\t')
        
        '''
        wrt =True
        if len(ln)<4:
            wrt = False
            ln=['1','1','a','a']
        '''
        
        binary.append(str(ln[3].count('.')))
        binary.append(str(ln[3].count(',')))
        binary.append(str(ln[3].count('!')))
        binary.append(str(ln[3].count('?')))
        binary.append(str(len(ln[3])))


        
        ln[3] =ln[3].replace('.','')
        ln[3] =ln[3].replace('!','')
        ln[3] =ln[3].replace('?','')
        ln[3] =ln[3].replace(',','')
        ln[3] =ln[3].replace('"','')
        tmp =ln[3].split()
        ln[3] = ' '.join(tmp)
        natural = ln[3]
        ln[3] = ln[3].lower()
        c =0
        #9
        for word in pos:
            #c+=1
            c+=ln[3].count(word)
        binary.append(str(c))
        c =0
        #10
        for word in neg:
            #c+=1
            c+=ln[3].count(word)
        binary.append(str(c))


        
        for i in range(len(totlist)):
            if totlist[i] in ln[3]:
                if totlist[i] in natural:
                    binary[i] = '1'
                else:
                    binary[i] = '1'

        
        posc = ['happiness','relief','fun','enthusiasm','love']
        negc = ['sadness','hate','worry','anger','boredom','empty']
        unknown = ['?']
        
       
        binary.append('neg')

        string = ','.join(binary)

        string=('' +string +''+ '\n')

        f3.write(string)

        binary[-1] = 'pos'

        string = ','.join(binary)

        string=('' +string +''+ '\n')

        f3.write(string)

        '''
        elif ln[1]!= 'surprise':
            binary.append('neut')
            string = ','.join(binary)
            string+='\n'
        
            f3.write(string)
            '''
      
        '''
        if ln[1] =='1':
            binary.append('pos')
        else:
            binary.append('neg')
        
        string = ','.join(binary)
        #string+=ln[3]
        string+='\n'
        if wrt==True:
            f3.write(string)
        '''
        
        #binary.append(ln[1])
        #string = ','.join(binary)
        #string+='\n'
        #f3.write(string)
    f3.close()
    f2.close()
    #print(totlist)
main()        
