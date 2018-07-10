import platform
import subprocess
import os, shutil
#main file for creating and running data
def deleteFiles(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)
    return

def deleteExe(string):
    if os.path.isfile(string):
        os.remove(string)

subprocess.call("make", stdout=subprocess.PIPE,shell=True)
print("Welcome! This is the protein prediction program") 
item = input("Generate Data? type 'y' for yes:")

if (item=="y"):
    subprocess.call("python3 sample-generator.py", shell=True)
    print("generating samples...")  
    subprocess.call("python3 aac-calculator.py", shell=True)
    print("generating aac...100%")
    subprocess.call("python3 dpc-calculator.py ", shell=True)
    print("generating dpc... 100%")
    subprocess.call("python3 paac-calculator.py", shell=True)
    print("generating paac...100%")
    subprocess.call("python3 mergeAllData.py", shell=True)
    print("generating combined data...100%")
    subprocess.call("python mainshufflelines.py", shell=True)
    subprocess.call("python shufflelines.py", shell=True)
    print("data prepared           ")    

item = ""
deleteData = False
while(item != "q"):
    item = input("What would you like to test?\n1=AAC,2=DPC,3=PAAC,c=COMBINED,e=ENSEMBLE,t=independent,q=QUIT:")
    if (item == "1"):
        print("-------------AAC----------------")
        subprocess.call("python3 aacevaluation.py", shell=True)
        print("-----------------------------")
    elif (item == "2"):
        print("-------------DPC----------------")
        subprocess.call("python3 dpcevaluation.py", shell=True)
        print("-----------------------------")
    elif (item == "3"):
        print("-------------PAAC----------------")
        subprocess.call("python3 paacevaluation.py", shell=True)
        print("-----------------------------")
    elif (item == "c"):
        print("-------------COMBINED----------------")
        subprocess.call("python3 mergeEvaluation.py", shell=True)
        print("-----------------------------")
    elif (item == "e"):
        print("-------------ENSEMBLE----------------")
        subprocess.call("python3 ensembleEvaluation.py", shell=True)
        print("-----------------------------")
    elif (item == "t"):
        print("-------------INDEPENDENT SET----------------")
        subprocess.call("python3 independentSet.py", shell=True)
        print("-----------------------------")
    elif(item != "q"):
        print("invalid input..")

item = input("Delete data? type 'y' if yes:")
if(item== "y"):
    deleteList= ["AAC","DPC","PAAC","Combined"]
    for string in deleteList:
        deleteFiles(string)
        deleteFiles(string+"/Train")
        deleteFiles(string+"/SVMResults")
    deleteFiles("independentTest")
    deleteFiles("Samples")

print("Quiting progam..")
deleteExe("svm-train")
deleteExe("svm-scale")
deleteExe("svm-predict")




