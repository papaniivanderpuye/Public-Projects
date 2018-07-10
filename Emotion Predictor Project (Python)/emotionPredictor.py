import os

def emotionPredictor(inputText):

	#inputText= "i hate the world"
	inputFile = open("data.txt","w")
	inputFile.write("tweet_id" +"\t" +  "sentiment" +"\t" +  "author" +"\t" +  "content" +"\n")
	inputFile.write("1956967341" +"\t" +  "?" +"\t" +  "unknownUser" +"\t" +  inputText +"")
	inputFile.close()

	os.system("python gamebiwordinfo.py")
	os.system("java -cp Contents/Java/weka.jar  weka.classifiers.functions.MultilayerPerceptron -T factors.csv -l PredictionModel/MLP.model -p 0 > results.txt")


	answerFile = open("results.txt","r")
	answerFile.readline()
	line = answerFile.readline()

	while line.find("inst#") == -1:
		line = answerFile.readline()
	line = answerFile.readline()	

	lineList= line.split()
	print(lineList)
	answer = lineList[-2][2:]

	print(answer)

	return answer
