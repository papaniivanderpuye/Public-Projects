#this is the car class i use for the main program
#the class contains important attributes of a car includin on unique thing about it
class Car:

    def __init__(self,model,mpg,cylinders,displacement,horsepower,weight,acceleration,year,origin,price,uniqueProperty):
        self.__model = model
        self.__mpg = mpg
        self.__cylinders = cylinders
        self.__disp = displacement
        self.__horseP = horsepower
        self.__weight = weight
        self.__accel = acceleration
        self.__year = year
        self.__origin = origin
        self.__price = price
        self.__unique = uniqueProperty
        
    def getUniqueProp(self):
        return self.__unique
        
    def getModel(self):	
        
        return self.__model
   
    def getMPG(self):
        return self.__mpg
        
    def getCylinders(self):	
        return self.__cylinders
        
    def getDisplacement(self):
        return self.__disp
        
    def getHorsePower(self):
        return self.__horseP		
        
    def getWeight(self):
        return self.__weight		
        
    def getAcceleration(self):
        return self.__accel	
        
    def getYear(self):
        return self.__year		
        
    def getOrigin(self):
        return self.__origin		
        
    def getPrice(self):
        return self.__price