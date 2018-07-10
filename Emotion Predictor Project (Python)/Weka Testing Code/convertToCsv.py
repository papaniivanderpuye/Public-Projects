
oldFILe = open('factors.txt','r')
newFile= open('factors.csv','w')

firstLine =oldFILe.readline()
firstLine =firstLine.strip()
first=firstLine.split(",")
length = len(first)

firstSen = []
#get labels
for i in range(length):
	firstSen.append("attribute " + str(i+0)  )

string = '","'.join(firstSen)
string=('"' +string +'"'+ '\n')
newFile.write(string)


#now get first line
string = '","'.join(first)
string=('"' +string +'"'+ '\n')
newFile.write(string)


#now write the rest of the lines
for line in oldFILe:
	line =line.strip()
	lineList =line.split(",")

	string = '","'.join(lineList)
	string=('"' +string +'"'+ '\n')
	newFile.write(string)


oldFILe.close()
newFile.close()