"""
This file is a prgram that runs the simulation of picking candy 
from a back till one obtains three colors.
"""
import random

def allColorsThere(pulledOut):
    if("red" not in pulledOut):
        return False
    if("blue" not in pulledOut):
        return False
    if("green" not in pulledOut):
        return False
    return True
    
#the main function utilizez the allColorsThere() function to check if all 
#colors are pulled out before pulling out again
def main():
    print("\n"+("-"*20) +"Color Candy Probablity" + ("-"*21)+"\n")
    bag = ["red","red","red","blue","blue","blue","green","green","green"]
    pulledOut = []
    count = 0
    
    while (not allColorsThere(pulledOut) ):
        count += 1
        
        if( (3<=count) and (count <= 7) ):
            percentage= 0.0
            numberOfEachColor = [bag.count("red"),bag.count("blue"),bag.count("green")]
            
            if (numberOfEachColor.count(3) > 1):
                percentage = 0.0
                
            else:
                percentage = (float(3) / sum(numberOfEachColor))*100

            print ( "The likelihood that " + str(count) + " pulls will meet the requirement is : " + str(round(percentage,2) ) + "%" )
       
        random.shuffle(bag)
        candy = bag.pop()
        pulledOut.append(candy)
        print("Pulled candy " + str(count) + " from bag...." + candy + "!")
        print("")
        
    print("All color have been pulled!")
    print("-"*64)
    print("\nTotal times candy pulled out of bag to obtain condition: " + str(count) + "\n")

main()   