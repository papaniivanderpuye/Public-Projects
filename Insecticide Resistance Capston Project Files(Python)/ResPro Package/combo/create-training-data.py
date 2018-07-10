import os

os.system("python aac-calculator.py resist_protein.txt notresist_protein.txt proteinsAAC.data")

os.system("python dpc-calculator.py resist_protein.txt notresist_protein.txt proteinsDPC.data")

os.system("python paac-calculator.py resist_protein.txt notresist_protein.txt proteinsPAAC.data")

os.system("python mergeAllData.py resist_protein.txt notresist_protein.txt mergedDATA.data")

os.system("python shufflelines.py proteinsAAC.data proteinsAAC.train proteinsDPC.data proteinsDPC.train proteinsPAAC.data proteinsPAAC.train")


