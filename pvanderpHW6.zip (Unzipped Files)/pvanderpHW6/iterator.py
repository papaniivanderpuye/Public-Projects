################################################
# iterator.py
# This module contains the solution to HW6
# Papa Nii Vanderpuye, CPS112
################################################

from abc import *

class ForwardIterator(metaclass=ABCMeta):
    """Provides the interface for a forward, read-only iterator."""


    @abstractmethod
    def getNext(self):
        """Moves the iterator to the next position"""
        return

    @abstractmethod
    def getItem(self):
        """Returns the item at the current position"""
        return

    @abstractmethod
    def getLoc(self):
        """Returns an object representing the iterator's current position (the type of this object may be specific to the container being iterated over). Returns None if the iterator has moved past the end of the collection."""
        return

    

    @abstractmethod
    def clone(self):
        """Return a new iterator pointing to the same location as this one"""
        return

    def __eq__(self, other):
        """Overloads the == operator. Returns True if the two iterators are pointing to the same location, False otherwise."""
        return self.getLoc() == other.getLoc()
    
    def __ne__(self, other):
        """Overloads the != operator. Returns the opposite of __eq__"""
        return not (self == other)

    def __next__(self):
        """Provides for loop funcionality. Returns the current item and moves the iterator to the next position. Raises StopIteration if the iterator has moved off of the collection."""
        if self.getLoc() == None:
            raise StopIteration
        else:
            item = self.getItem()
            self.getNext()
            return item


class ForwardAssignableIterator(ForwardIterator):
    #Provides the interface for a forward, assignable, read-only iterator.
    @abstractmethod
    def setItem(self,item):
        #sets an item in the iterator's position
        "string"



class PythonListFAIterator(ForwardAssignableIterator):
    #The interface for a Python, forward, assignable iterator.
    def __init__(self,aList,index):
        self.aList = aList
        self.index = index

    def getNext(self):
        #Moves the iterator to the next position
        self.index +=1
    
    def getItem(self):
        #Returns the item at the current position
        if len(self.aList)-1 < self.index or self.index < 0: 
            return None
        else:
            return self.aList[self.index]


    def setItem(self,item):
        ##sets an item in the iterator's position
        if len(self.aList)-1 < self.index or self.index < 0: 
            "Do Nothing"
        else:
            self.aList[self.index]=item


    def getLoc(self):
        #Returns an object representing the iterator's current position (the type of this object may be specific to the container being iterated over). Returns None if the iterator has moved past the end of the collection.
        if len(self.aList)-1 < self.index or self.index < 0:
            return None

        else:
            return self.index



    def clone(self):
        #Return a new iterator pointing to the same location as this one
        return PythonListFAIterator(self.aList,self.index)



    
class BidirectionalAssignableIterator(ForwardAssignableIterator):
    #Provides the interface for a forward and backward, assignable, read-only iterator.
    @abstractmethod
    def getPrevious():
        "Do Nothing"
    

class PythonListBAIterator(BidirectionalAssignableIterator):
    #The interface for a Python, forward, assignable iterator.
    def __init__(self,aList,index):
        self.aList = aList
        self.index = index

    def getNext(self):
        #Moves the iterator to the next position
        self.index +=1
    
    def getItem(self):
        #Returns the item at the current position
        if len(self.aList)-1 < self.index or self.index < 0: 
            return None
        else:
            return self.aList[self.index]


    def setItem(self,item):
        ##sets an item in the iterator's position
        if len(self.aList)-1 < self.index or self.index < 0: 
            "Do Nothing"
        else:
            self.aList[self.index]=item


    def getLoc(self):
        #Returns an object representing the iterator's current position (the type of this object may be specific to the container being iterated over). Returns None if the iterator has moved past the end of the collection.
        if len(self.aList)-1 < self.index or self.index < 0:
            return None

        else:
            return self.index



    def clone(self):
        #Return a new iterator pointing to the same location as this one
        return PythonListFAIterator(self.aList,self.index)



    
class BidirectionalAssignableIterator(ForwardAssignableIterator):
    #Provides the interface for a forward and backward, assignable, read-only iterator.
    @abstractmethod
    def getPrevious():
        "Do Nothing"
    

class PythonListBAIterator(BidirectionalAssignableIterator):
    #The interface for a Python, forward, assignable iterator.
    def __init__(self,aList,index):
        self.aList = aList
        self.index = index

    def getNext(self):
        #Moves the iterator to the next position
        self.index +=1
    
    def getItem(self):
        #Returns the item at the current position
        if len(self.aList)-1 < self.index or self.index < 0: 
            return None
        else:
            return self.aList[self.index]


    def setItem(self,item):
        #sets an item in the iterator's position
        if len(self.aList)-1 < self.index or self.index < 0: 
            "Do Nothing"
        else:
            self.aList[self.index]=item


    def getLoc(self):
        #Returns an object representing the iterator's current position (the type of this object may be specific to the container being iterated over). Returns None if the iterator has moved past the end of the collection.
        if len(self.aList)-1 < self.index or self.index < 0:
            return None

        else:
            return self.index



    def clone(self):
        #Return a new iterator pointing to the same location as this one
        return PythonListFAIterator(self.aList,self.index)



    
class BidirectionalAssignableIterator(ForwardAssignableIterator):
    #Provides the interface for a forward and backward, assignable, read-only iterator.
    @abstractmethod
    def getPrevious():
        #Moves the iterator to the previous position
        "Do Nothing"
    

class PythonListBAIterator(BidirectionalAssignableIterator):
    #The interface for a Python, forward and backward, assignable iterator.
    def __init__(self,aList,index):
        self.aList = aList
        self.index = index

    def getNext(self):
        #Moves the iterator to the next position
        if self.index <= len(self.aList)-1:
            self.index +=1

    def getPrevious(self):
        #Moves the iterator to the previous position
        if self.index >= 0:
            self.index -=1
    
    def getItem(self):
        #Returns the item at the current position
        if len(self.aList)-1 < self.index or self.index < 0: 
            return None
        else:
            return self.aList[self.index]


    def setItem(self,item):
        #sets an item in the iterator's position
        if len(self.aList)-1 < self.index or self.index < 0: 
            "Do Nothing"
        else:
            self.aList[self.index]=item


    def getLoc(self):
        #Returns an object representing the iterator's current position (the type of this object may be specific to the container being iterated over). Returns None if the iterator has moved past the end of the collection.

        if len(self.aList)-1 < self.index or self.index < 0:
            return None
        else:
            return self.index



    def clone(self):
        #Return a new iterator pointing to the same location as this one
        return PythonListBAIterator(self.aList,self.index)



