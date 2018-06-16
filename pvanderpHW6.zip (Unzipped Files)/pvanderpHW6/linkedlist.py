################################################
# iterator.py
# This module contains the solution to HW6
# Papa Nii Vanderpuye, CPS112
################################################

import iterator

class LinkedListNode:
    def __init__(self, item, nextNode):
        ''' Create a new node pointing to the given nextNode '''
        self._item = item
        self._next = nextNode

    def getItem(self):
        ''' Return the data stored for this '''
        return self._item

    def getNext(self):
        ''' Return the LinkedListNode this node points to '''
        return self._next

    def setItem(self, item):
        ''' Change the data this node holds '''
        self._item = item

    def setNext(self, nextNode):
        ''' Change the node that this node points to as next '''
        self._next = nextNode

class LinkedList:
    def __init__(self):
        ''' Create a new empty linked list '''
        self._head = None
        self._tail = None

        # Note: Value of length is 1 more than last index value
        # Just as with Python lists
        self._length = 0

    def getStartIter(self):
        """Returns a new iterator pointed at the beginning of the list."""
        return LinkedListFAIterator(self._head)

    def getLength(self):
        ''' Return nmber of nodes in linked list '''
        return self._length

    def isEmpty(self):
        ''' Return True if linked list has no nodes, False otherwise '''
        return self._length == 0

    def pushFront(self, item):
        ''' Add a new node to the front of the linked list '''
        # Step 1: Create a new node and 
        # let it point to the 1st node in the original list
        newNode = LinkedListNode(item, self._head)

        # Step2: Make self._tail refer to newNode if list is empty
        if self.isEmpty():
            self._tail = newNode

        # Step 3 Update reference to head and update length:
        self._head = newNode
        self._length += 1

    def popFront(self):
        ''' Remove the node currently at the front of the linked list 
            Return the value it holds  '''
        if self.isEmpty():
            raise IndexError("popFront: index out of bounds")

        # Save data held at front of list
        item = self._head.getItem()

        # New head needs to be whoever the current head points to 
        self._head = self._head.getNext()
        self._length -= 1

        # In case that was last item, update tail
        if self.isEmpty():
            self._tail = None

        return item

    def pushBack(self, item):
        ''' Add a new node to rear of linked list '''
        if self.isEmpty():
            self.pushFront(item)
        else:
            # Create a new node
            newNode = LinkedListNode(item, None)

            # Make the current tail point to the new node
            self._tail.setNext(newNode)

            # Now make the new node the tail
            self._tail = newNode
   
            self._length += 1

    def popBack(self):
        ''' Remove node at rear of linked list, return value it holds '''
        if self.isEmpty():
            raise IndexError("popBack: index out of bounds")
        elif self._length == 1:
            return self.popFront()
        else:
            # Still have to start from beginning
            # because we do not know which node comes before the tail
            node = self._head
            for i in range(self._length-2):
                node = node.getNext()

            # Get data at tail
            item = self._tail.getItem()
            
            # This is node right before tail. It will be new tail
            # So it must point to None
            node.setNext(None)
            self._tail = node

            self._length -= 1

            return item

    def search(self, item):
        ''' Performs linear search for item in linked list '''
        node = self._head
        for i in range(self._length):
            if node.getItem() == item:
                return True
            node = node.getNext()

        return False

    def remove(self, index):
        ''' Removes a node from list at any position and returns data it held '''
        if index < 0 or index >= self._length:
            raise IndexError("remove: Index out of bounds")
        elif index == self._length - 1:
            return self.popBack()
        elif index == 0:
            return self.popFront()
        else:
            previousNode = self._head
            
            # Go to one before the index so we can update it appropriately
            for i in range(index - 1):
                previousNode = previousNode.getNext()

            item = previousNode.getNext().getItem()
        
            # New next has to be the indexed node's next
            # But we don't have indexed node.  It's next is indexed node
            # and the next of that one is who we have to point to
            previousNode.setNext(previousNode.getNext().getNext())

            self._length -= 1

            return item

    def insert(self, index, item):
        ''' Insert a new node into any position into list '''
        if index<0 or index>= self._length:
            raise IndexError("insert: Index out of bounds")
        elif index == self._length - 1:
            return self.pushBack(item)
        elif index == 0:
            return self.pushFront(item)
        else:
            previousNode = self._head
            for i in range(index - 1):
                previousNode = previousNode.getNext()

            # Previous Node's next node is the node currently at the given index
            # It should be the new node's next
            newNode = LinkedListNode(item, previousNode.getNext())
            previousNode.setNext(newNode)
            self._length += 1

    def __getitem__(self, index):
        ''' Overloads indexing [] to return item at given index position '''
        if index < 0 or index >= self._length:
            raise IndexError("__getitem__: Index out of bounds")

        node = self._head
        for i in range(index):
            node = node.getNext()

        return node.getItem()

    def __setitem__(self, index, item):
        ''' Overloads indexing [] so that value at given
            given index position can be changed '''
        if index < 0 or index >= self._length:
            raise IndexError("__setitem__: Index out of bounds")

        node = self._head
        for i in range(index):
            node = node.getNext()

        node.setItem(item)

    def __contains__(self, item):
        ''' Overloaded  in/not in '''
        return self.search(item)

    def __len__(self):
        ''' Overloaded len() method '''
        return self._length

  

    def __str__(self):
        ''' String representation of linked list '''
        aStr = ''
        current = self._head
        while current != None:
            aStr = aStr + str(current.getItem()) + '-->'
            current = current.getNext()

        aStr = aStr + 'None'
        return aStr

    def __iter__(self):
        """Provides for loop functionality. Returns a new iterator pointed at the beginning of the list."""
        return self.getStartIter()


class DoubleLinkedListNode(LinkedListNode):
    def __init__(self, item, nextNode, prevNode):
        super().__init__(item, nextNode)
        self.__prev = prevNode

    def getPrevious(self):
        
        return self.__prev

    def setPrevious(self, prevNode):
        self.__prev = prevNode


class DoubleLinkedList(LinkedList):
    def __init__(self):
        super().__init__()


    def pushFront(self, item):
        '''Overwrite the pushFront method. Fill the code here!'''
        if self.isEmpty():
            newNode = DoubleLinkedListNode(item, None, None)
            self._head = newNode
            self._tail = newNode
        else:
            newNode = DoubleLinkedListNode(item, self._head, None,)
            self._head.setPrevious(newNode)
            self._head = newNode
            
        self._length += 1    
        

    def getStartIterator(self):
        #returns a iterator starting at the head
        return DoublyLinkedListBAIterator(self._head)

    def getEndIterator(self):
         #returns a iterator starting at the tail
        return DoublyLinkedListBAIterator(self._tail)

    def __iter__(self):
        #overides the iter function
        return DoublyLinkedListBAIterator(self._head)

    def popFront(self):
        '''Overwrite the popFront method. Fill the code here!'''

        if self.isEmpty():
            raise IndexError("popFront: index out of bounds")
        else:
            removedItem =self._head
            self._head = self._head.getNext()
            self._length -= 1
            if self.isEmpty():
                self._tail =None
            else:
                self._head.setPrevious(None)

        return removedItem.getItem()

    def pushBack(self, item):
        '''Overwrite the pushBack method. Fill the code here!'''
        if self.isEmpty():
            self.pushFront(item)

        else:
            newNode = DoubleLinkedListNode(item, None, self._tail)
            self._tail.setNext(newNode)
            self._tail = newNode
            
            self._length += 1
            

    def popBack(self):
        
        '''Overwrite the popBack method. Fill the code here!'''
        if self.isEmpty():
            raise IndexError("popFront: index out of bounds")
        else:
            print(self._length,self.isEmpty())
            removedItem =self._tail
            self._tail = self._tail.getPrevious()
            self._length -= 1
            
            if self.isEmpty():
                self._head =None
            else:
                self._tail.setNext(None)
        

        return removedItem.getItem()

    def remove(self, index):
        '''Overwrite the remove method. Fill the code here!'''
        print(self._length,index)
        if self._length <= index or index<0:
           raise IndexError("remove: Index out of bounds")
        elif index == 0:
            return self.popFront()
        elif index == self._length-1:
            return self.popBack()
        else:
            previousNode = self._head
            for i in range (index-1):
                previousNode = previousNode.getNext()
            removingItem=previousNode.getNext()
            nextNode = removingItem.getNext()
            nextNode.setPrevious(previousNode)
            previousNode.setNext(nextNode)
            self._length -= 1
            return removingItem.getItem()

    def insert(self, index, item):
        '''Overwrite the insert method. Fill the code here!'''
        if index<0:
            raise IndexError("insert: Index out of bounds")
        elif index >= self._length - 1:
            return self.pushBack(item)
        elif index == 0:
            return self.pushFront(item)
        else:
            newNode = DoubleLinkedListNode(item, None, None)
            previousNode = self._head
            for i in range(index - 1):
                previousNode = previousNode.getNext()

            nextNode = previousNode.getNext()
            newNode.setPrevious(previousNode)
            newNode.setNext(nextNode)
            nextNode.setPrevious(newNode)
            previousNode.setNext(newNode)
            self._length += 1
            

            
        
    def __str__(self):
        ''' String representation of double linked list '''
        aStr = ''
        current = self._head
        while current != None:
            aStr = aStr + str(current.getItem()) + '<-->'
            current = current.getNext()

        aStr = aStr + 'None'
        return aStr
 
        

    
        
class LinkedListFAIterator(iterator.ForwardAssignableIterator):
      #The interface for a LinkedList, forward and backward, assignable iterator.
      def __init__(self,node):
          self.currentNode = node
            
      def getNext(self):
          #Return the LinkedListNode this node points to
          if self.currentNode != None:
              self.currentNode = self.currentNode.getNext()
    
      def getItem(self):
          #Returns the item at the current position
          if self.currentNode == None:
              return None
              
          return self.currentNode.getItem()


      def setItem(self,item):
          #Change the data this node holds
          if self.currentNode == None: 
             "Do Nothing"
          else:
            self.currentNode.setItem(item)


      def getLoc(self):
          #Returns an object representing the iterator's current position (the type of this object may be specific to the container being iterated over). Returns None if the iterator has moved past the end of the collection.
          return self.currentNode



      def clone(self):
        #Return a new iterator pointing to the same location as this one
        return LinkedListFAIterator(self.currentNode)          
    
                
                
class DoublyLinkedListBAIterator(iterator.BidirectionalAssignableIterator):
      #The interface for a DoubleLinkedList, forward and backward, assignable iterator.
      def __init__(self,node):
          self.currentNode = node
            
      def getNext(self):
          #Moves the iterator to the next position
          if self.currentNode != None:
              self.currentNode = self.currentNode.getNext()

      def getPrevious(self):
          #Moves the iterator to the previous position
          if self.currentNode != None:
              self.currentNode = self.currentNode.getPrevious()
    
      def getItem(self):
          #Return the data stored for this 
          if self.currentNode == None:
              return None
              
          return self.currentNode.getItem()


      def setItem(self,item):
          #Change the node that this node points to as next
          if self.currentNode == None: 
             "Do Nothing"
          else:
            self.currentNode.setItem(item)


      def getLoc(self):
          #Returns an object representing the iterator's current position (the type of this object may be specific to the container being iterated over). Returns None if the iterator has moved past the end of the collection.
          return self.currentNode



      def clone(self):
        #Return a new iterator pointing to the same location as this one
        return DoublyLinkedListBAIterator(self.currentNode)        





        
    
