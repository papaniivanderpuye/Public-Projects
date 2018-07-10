import os

def testing():

	#inputText= "i hate the world"

	#first convert txt to csv
	os.system("python convertToCsv.py")

	#run weka
	newFile= open('results.txt','w')
	os.system("java -cp Contents/Java/weka.jar  weka.classifiers.functions.MultilayerPerceptron  -L 0.3 -M 0.2 -N 100 -V 0 -S 0 -E 20 -H 2 -t factors.csv -o > results.txt")
	newFile.close()
	readFile = open('results.txt','r')

	#get values
	line =readFile.readline()
	while "Correctly Classified Instances" not in line:
		line =readFile.readline()

	line =readFile.readline()
	while "Correctly Classified Instances" not in line:
		line =readFile.readline()

	lineList = line.split()
	acc = ( float(lineList[4]) )/100

	while "Mean absolute error" not in line:
		line =readFile.readline()

	lineList = line.split()
	mean = ( float(lineList[3]) )

	
	print(str(mean) + "\t"+ str(acc) )
	
	readFile.close()
	return 0


testing()