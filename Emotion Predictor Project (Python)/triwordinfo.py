def main():
    edict = {'happiness':0,'relief':0,'fun':0,'enthusiasm':0,'love':0,'sadness':0,'hate':0,'worry':0,'anger':0,'surprise':0,'empty':0,'neutral':0,'boredom':0}
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
    triword = {}
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



        ln[3] =ln[3].replace('.','')
        ln[3] =ln[3].replace('!','')
        ln[3] =ln[3].replace('?','')
        ln[3] =ln[3].replace(',','')
        ln[3] =ln[3].replace('"','')
        if edict[ln[1]] <101:
            edict[ln[1]] =  edict[ln[1]]+1
            ln[3] = ln[3].lower()
            wlist=ln[3].split()
            wordbefore = None
            wordbefore3 = None
            for word in wlist:
                if word[0]=='@':
                    wdict['@'] = wdict['@'] +1
                elif word in wdict:
                    wdict[word] = wdict[word]+1
                
                else:
                    wdict[word] =1
                if wordbefore != None:
                    tot = wordbefore +' '+word
                    if tot in doubleword:
                        doubleword[tot] = doubleword[tot] +1
                    else:
                        doubleword[tot] = 1

                    if wordbefore3 != None:
                        tot =wordbefore3+' '+wordbefore+' '+word
                        if tot in triword:
                            triword[tot]= triword[tot] + 1
                        else:
                            triword[tot] = 1
                wordbefore3 = wordbefore
                wordbefore = word
                
    f1.close()
    totlist=[]
    for item in wdict:
        if len(item)>1:
            if wdict[item] >10 and wdict[item]<500 :
                totlist.append(item)
    for item in doubleword:
        if len(item)>1:
            if doubleword[item] >10 and doubleword[item]<1000 :
                totlist.append(item)


    for item in triword:
        if len(item)>1:
            if triword[item] >5 and triword[item]<1000 :
                totlist.append(item)
    print(len(totlist))
    print(edict)
    #print(totlist)
    
    f2 =  open('data.txt','r')
    f2.readline()
    f3 = open('factors.txt','w')
    for line in f2:
        binary =[]
        for i in range(len(totlist)):
            binary.append('0')
        line = line.replace('\n','')
        ln = line.split('\t')
        #print(ln[3])

        binary.append(str(ln[3].count('.')))
        binary.append(str(ln[3].count(',')))
        binary.append(str(ln[3].count('!')))
        binary.append(str(ln[3].count('?')))
        ln[3] =ln[3].replace('.','')
        ln[3] =ln[3].replace('!','')
        ln[3] =ln[3].replace('?','')
        ln[3] =ln[3].replace(',','')
        ln[3] =ln[3].replace('"','')
        binary.append(str(len(ln[3])))
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
                binary[i] = '1'

        
        posc = ['happiness','relief','fun','enthusiasm','love']
        negc = ['sadness','hate','worry','anger']
        
        if ln[1] in posc or ln[1] in negc:
            #info.append(ln[1])
            if ln[1] in posc:
                binary.append('pos')
            else:
                binary.append('neg')

            string = ','.join(binary)
            string+='\n'
        
            f3.write(string)
        
        '''
        if ln[1] =='1':
            binary.append('pos')
        else:
            binary.append('neg')
        '''


        
        #binary.append(ln[1])
        #string = ','.join(binary)
        #string+='\n'
        #f3.write(string)
    f3.close()
    f2.close()
    #print(totlist)
main()        
