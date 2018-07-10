import os

inputText= "i hate the world"

inputFile = open("data.txt","w")

inputFile.write("tweet_id" +"\t" +  "sentiment" +"\t" +  "author" +"\t" +  "content" +"\n")

inputFile.write("1956967341" +"\t" +  "empty" +"\t" +  "unknownUser" +"\t" +  inputText +"\n")

os.system("python wordbinaries biwordinfo.py")

os.system("python wordbinaries biwordinfo.py")



