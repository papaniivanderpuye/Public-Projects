"""
This is code is my solution to the care storefront problem it creates a user interface on the command line
where the user an buy cars from its manually created inventory
"""
import car

#this function gets the car data from a txt file i created.
#it uses the car data to create car objects using the car class i created on car.py
def getData():
    carList = []
    try:
        carDataSheet = open("carData.txt","r")
    except IOError:
        print("No carData.txt file")
        
    carDataSheet.readline();    
    for line in carDataSheet:
        carInfo =(line[:-1]).split("\t")
        newCar = car.Car(carInfo[0],carInfo[1],carInfo[2],carInfo[3],carInfo[4],carInfo[5],carInfo[6],carInfo[7],carInfo[8],carInfo[9],carInfo[10])
        carList.append(newCar)  
        
    return carList
    
#this function takes a care object and uses its methods to pring all the information about it
def printInfo(car):
    mpg ="MPG: " + car.getMPG()    
    cylinder = "Cylinders: " + car.getCylinders()
    horseP = "Horse Power: " + car.getHorsePower() 
    weight ="Weight: " + car.getWeight()
    acceleration = "Acceleration: " + car.getAcceleration() 
    year =  "Year: " + car.getYear()
    origin = "Origin: " + car.getOrigin() 
    price = "Price: " + car.getPrice()
    displacement  = "Displacement: " + car.getDisplacement()
    unique = "Unique Property: " + car.getUniqueProp()
    
    print("\n" + "*"*40)
    print("Info for  '" + car.getModel() + "':")
    print("")
    print(mpg + (" "*(20-len(mpg)) ) + cylinder )
    print(horseP + (" "*(20-len(horseP))) + weight ) 
    print(year + (" "*(20-len(year))) + acceleration)
    print(origin + (" "*(20-len(origin))) + displacement  )
    print(unique ) 
    print(price)
    print("*"*40)

#this function prints the the cars added to the cart and prints the total price of them as well 
def viewCart(cart):
    total = 0;   
    print("\nItems in cart:")
    print("")
    
    for car in cart:
        price = car.getPrice()
        name = car.getModel()
        
        if (len(name)> 20):
            name = name[:21]
            
        print(name +(" "* (25-len(name)) ) + price )
        price = price.replace("$","")
        price = price.replace(",","")
        total += int(price)
        
    stringTotal = str(total)
    
    if(len(stringTotal)>3):
        stringTotal = stringTotal[:-3] + "," + stringTotal[-3:]
        
    print("- "*25)
    print("Total:" + (" "*19) + "$" + stringTotal) 
    
    return ("$" + stringTotal)
        
#this function prints a grid of the car names. it displays the cars like an online storefront       
def printGrid(carList):
    print("\nStorefront:")
    rowLimit =0;
    row ="||"
    print("-"*142)
    
    for i in range(len(carList)):      
        name = "(" + str(i+1) +") " +carList[i].getModel()
        
        if (len(name)> 20):
            name = name[:21]
            
        if (rowLimit==5): 
            print(row)
            print("-"*142)
            row = "||" + " " +name +(" "* (25-len(name)) )+ "||"
            rowLimit =1
            
        else:
            row += " " +name +(" "* (25-len(name)) )+ "||"
            rowLimit +=1   
            
    print(row)
    print("-"*142)
    
#main function excetutes the program and takes in the user input to perform various functions as a storefront 
#it adds items to a cart, checks out, and shows info on a car.  
def main():
    carList=getData()   
    quit = False
    cart =[]
    
    print("\nWelcome to VanMAX! you center for affordable vintage vehicles. \nWe have 20 items in our inventory for you today")
    printGrid(carList)
    
    while (not quit):   
        print("\na = add item to cart, v = view item information, c = proceed to cart to purchase items, d = display storefront again")
        letter = input("What would you like to do? (type letter and press enter):")
        
        #add item to cart
        if (letter.lower() == "a"):
            if (carList):
                stringNum = input("What car would you want to add to you cart? (type number and press enter):")
                number =int(stringNum)
                
                if (number<=len(carList)):            
                    selectedCar = carList[number-1]
                    cart.append(selectedCar)
                    del carList[number-1]            
                    print("\nThe car \n'"+ selectedCar.getModel() + "'\nhas been added to your cart")
                    printGrid(carList)
                    
                else:
                    print("\nSorry there is no car with that number")
            else:
                print("\nSorry there are no more cars in the inventory")
       
       #view item information
        elif (letter.lower() == "v"):        
            stringNum = input("What car info would you want to view? (type number and press enter): ")
            number =int(stringNum)
            
            if (number<=len(carList)):
                printInfo(carList[number-1])
                
                
            else:
                print("\nSorry there is no car with that number")
       
        #displays storefront again
        elif (letter.lower() == "d"): 
            printGrid(carList)
                
        #prints cart for checkout        
        elif (letter.lower() == "c"):
        
            if (cart):
                print("\nProceeding to cart...")
                total =viewCart(cart)
                goBack = False
                
                while (not goBack):            
                    print("\ny = Proceed with checkout, n = Cancel items in cart, b = Go back to Storefront ")
                    proceed = input("What would you want to do with cart? :")
                    
                    if (proceed.lower() == "y" ):
                        print( "\nThank you for shopping with us. You ordered " + str(len(cart)) + " items.")
                        print( "Your payment was " + total)
                        print("Have a great rest of your day!")
                        quit = True
                        goBack = True
                        
                    elif(proceed.lower()=="n"):
                        print("\nCanceling items in cart.... going back to storefront")
                        carList=getData()  
                        cart = []
                        goBack = True
                        printGrid(carList)
                        
                    elif(proceed.lower()=="b"):
                        print('\nGoing back to storefront......')
                        goBack = True
                        printGrid(carList)
                        
                    else:
                        print("\nSorry, invalid command, please type and enter one of the letters listed below")
                    
            else:
                print("\nSorry we cannot proceed because your cart is empty. please add items to purchase")            
             
        elif (letter.lower() == "q"):
             print("\nQuitting........")
             quit= True
        
        else:
            print("\nSorry, invalid command, please type and enter one of the letters listed below")
             
        print("")

main()











          
 