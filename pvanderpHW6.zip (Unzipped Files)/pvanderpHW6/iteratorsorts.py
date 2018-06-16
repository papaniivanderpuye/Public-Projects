################################################
# iteratorsorts.py
# This module contains the solution to HW6
# Papa Nii Vanderpuye, CPS112
################################################

def selectionSort(Fiter):
    #uses the forward assignable iterator to perform selections sort
    while Fiter.getItem() != None:
       previousClone = Fiter.clone()
       FitClone1 = Fiter.clone()
       Min = Fiter.getItem()
       while FitClone1.getItem() != None:
          if FitClone1.getItem() < Min:
             Min = FitClone1.getItem()
             previousClone = FitClone1
             FitClone1 = previousClone.clone()
          FitClone1.getNext()
       if previousClone.getLoc() != Fiter.getLoc():
          firstNum = Fiter.getItem()
          Fiter.setItem(previousClone.getItem())
          previousClone.setItem(firstNum)
       
       Fiter.getNext()

def insertionSort(Biter):
    ##uses the bidirectional assignable iterator to perform selections sort
    Biter.getNext()

    while Biter.getItem() != None:

        currentValue = Biter.clone()
        currentItem = currentValue.getItem()
        previousClone = Biter.clone()
        previousClone.getPrevious()

        while previousClone.getLoc()!= None and previousClone.getItem() >currentItem:
            currentValue.setItem(previousClone.getItem())
            currentValue.getPrevious()
            previousClone.getPrevious()

        
        currentValue.setItem(currentItem)
        Biter.getNext()
    
          
