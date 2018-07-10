#include <iostream>

using namespace std;

#ifndef _LBVECTOR_H
#define _LBVECTOR_H

#include <cstdlib>
#include <cassert>
#include <iostream>

// templated vector class, partially based on Budd,
//                         Classic Data Structures in C++
// written 11/5/93, modified 3/23/94
// changed on 3/9/95 to make all methods inline (defined in class decl)
// changed on 10/14/99 to clean up for vector lab in CS 330
// changed on 10/14/04 to update for C++ changes
//////////////////////////////////////////////////////////////////////////
// updated Oct. 2014 by ___________________ to allow lower and upper bounds
//////////////////////////////////////////////////////////////////////////
//
// for a vector of Items use lbvector<Item>,
//                   e.g., lbvector <int> intvector;
//                   note: Item must have a default constructor
//
// constructors:
//   lbvector( )             -- default, vector of size 0 (no entries)
//   lbvector(LowerBound, UpperBound)      -- vector with (|UpperBound|- LowerBound +1 )  entries
//

//  lbvector(LowerBound, UpperBound,
//          Item fillValue)  VECTOR with (|LowerBound| + |UpperBound| +1 ) entries all == fillValue



//   lbvector(const lbvector & vec) -- copy constructor
//    
//   int capacity( )         -- returns capacity of vector
// 
//   void resize(LowerBound, UpperBound) 
//							 --  changes Lower and UpperBounds

//                           -- resizes the vector to (|LowerBound| + |UpperBound| +1 ) elements
//                              (can result in losing elements if
//                                   new (|LowerBound| + |UpperBound| +1 ) < old (|LowerBound| + |Upper Bound| +1 ))
//
//   void fill(Item fillValue)  -- set all entries equal to fillValue
//
//   operator =              -- assignment operator works properly
//   operator []             -- indexes both const and non-const vectors
//    
//
//  examples of use:
//     lbvector<double> dlist(-3,3); // list of (|-3|+|3| + 1) doubles
//     lbvector<double> dzlist(-3,3,0.0);  // list of (|-3|+|3| + 1) doubles initialized to 0.0
//
//     lbvector<String> slist(-2,5);       // list of (|-2|+|5| + 1)  strings
//
//     lbvector<int> ilist;               // has room for 0 ints
//
//
//  class invariant:
//	 - myZero  points to the zero between the Lower and Upper Bounds
//   - myList points to the beginning of the allocated space 
//   - myCapacity is the number of elements allocated


template <class Item> class lbvector
{
public:
   // default constructor 0 elements
   // postcondition: vector of zero items constructed
   

   lbvector( ) 
   {
      myCapacity = 0;
      lower_B =0;
      upper_B = 0;
      myList = new Item [0];
      myZero = myList - lower_B;
   }
    
 
   // postcondition: vector of (|Lower Bound| + |Upper Bound| +1 ) items constructed 
   
   lbvector(int lowerBound, int upperBound) 
   {
   	  
      int size = (upperBound- lowerBound + 1);
      assert(size>= 0);   
      myCapacity = size;
      myList = new Item [size];
      assert(myList != 0);
      
      myZero = myList - lowerBound;  //my list is a pointer, so we are pointing to (lowerbound) positions behind where myList currently points to 
      
      lower_B=lowerBound;
      upper_B= upperBound;
      
   }
   
 
   // specify fill value
   // postcondition: constructed vector of (|Lower Bound| + |Upper Bound| +1 ) items,
   //                each item initialized to fillValue
   lbvector(int lowerBound, int upperBound, Item fillValue) 
   {
     
      int size = (upperBound- lowerBound + 1);
      assert(size >= 0);
      
      myCapacity = size;
      myList = new Item [size];
      assert(myList != 0);
      
      myZero = myList - lowerBound;  //my list is a pointer, so we are pointing to (lowerbound) positions behind where myList currently points to 
      
      lower_B =lowerBound;
      upper_B = upperBound;
      
      
      fill(fillValue);
   }


   // copy constructor
   //copies lower and upper bounds
   // used to create a new and complete copy of the object (vec)
   //    as when passing the object by value or returning object 
   //    as a result - need a deep copy when using dynamic memory
   // precondition: Item supports assignment
   // postcondition: constructed vector is an exact duplicate of vec        
   lbvector(const lbvector<Item> & vec) 
   {
      // allocate storage using Lower and Upper Bounds
      
      myCapacity = vec.myCapacity;
      myList = new Item [myCapacity];
      
      assert(myList != 0);
      
      // copy elements from vec
      for (int k = 0; k < vec.myCapacity; k++) {
         myList[k] = vec.myList[k];
      }       
      
      myZero = myList - vec.lower() ;
      lower_B =vec.lower();
      upper_B = vec.upper();
   }
    
   // free new'd storage
   // postcondition: dynamically allocated storage freed
   ~lbvector ( ) 
   {
      delete [] myList;
   }

   // assignment
   //    need a deep copy when using dynamic memory
   // precondition: Item supports assignment     
   // postcondition: self is assigned vec
   lbvector & operator = (const lbvector<Item> & vec) 
   {
      // don't assign to self!
      if (this != &vec) {
         // out with old list, in with new
         delete [] myList;
         myCapacity = vec.myCapacity;
         myList = new Item [myCapacity];
         
         
         assert(myList != 0);
            
         // copy elements from vec
         for (int k=0; k < vec.myCapacity; k++) {
            myList[k] = vec.myList[k];
         }
         
         lower_B =vec.lower();
         upper_B = vec.upper();
         myZero = vec.myZero;
      }
      return *this;           
   }

   // change size dynamically
   // change Lower and Upper Bounds
   // sets Myzero
   // precondition: vector has room for myCapacity entries     
   // postcondition: vector has room for newSize/((|Lower Bound| + |Upper Bound| +1 )) entries
   //          the first myCapacity of which are copies of original
   //          unless newSize < myCapacity, then truncated copy occurs
   void resize(int newLowerBound, int newUpperBound) 
    {
        int newSize = (newUpperBound- newLowerBound + 1);
        assert(newSize>= 0);
        int numToCopy = newSize < myCapacity ? newSize : myCapacity;
        
        // allocate new storage
        Item * newList = new Item[newSize];
        Item * myNewZero = newList - newLowerBound;
        assert(newList != 0);
        
        // copy retained values from old to new        
        for (int k=newLowerBound; k <= newUpperBound;k++) {
            if (lower()<=k && k<= upper())
                {
                    
                    myNewZero[k] = myZero[k];
                }

            }
            
        // return space no longer needed        
        delete [] myList;
            
            
        // update instance variables to reflect changes
        myCapacity = newSize;
        myList = newList;
        myZero = myNewZero;
        lower_B =newLowerBound;
        upper_B =newUpperBound;
            
        
      
    }
    
   // capacity of vector
   int capacity( ) const 
   {
      return myCapacity;
   }


   int lower( ) const
   {
     return lower_B;
   }

   int upper( ) const
   {
     return upper_B;
   }

   // postcondition: all entries are equal to fillValue
   void fill(Item fillValue) 
   {
      for (int k=lower(); k <= upper(); k++) {
         myZero[k] = fillValue;
         
      }
   }

   // safe indexing, returning reference
   // precondition: Lower Bound <= index <= Upper Bound
   // postcondition: return index-th item
   // exception: aborts if index is out-of-bounds
   Item & operator [] (int index) 
   {
      checkIndex(index);
      return myZero[index];     
   }
    
   // const index 
   // safe indexing, returning const reference to avoid modification
   // precondition: Lower Bound <= index <= Upper Bound
   // postcondition: return index-th item
   // exception: aborts if index is out-of-bounds
   const Item & operator [] (int index) const 
   {
      checkIndex(index);
      return myZero[index]; 
   }

private:
   Item * myList;  // the array of items
   Item * myZero;
   int lower_B;
   int upper_B;
   int myCapacity; // # things in vector (array), LowerBound,LowerBound+1,...,UpperBound -1,UpperBound)
   //myCapacity = (|Lower Bound| + |Upper Bound| +1 )
   


   // aborts with appropriate message if index is not in appropriate range
   // This means it will abort if Lower Bound <= index <= Upper Bound
   // use std:: to access names in std namespace
   void checkIndex (int index) const 
   {
     if (index < lower_B || upper_B < index) {
         std::cerr << "Illegal vector index: " << index
                   << " (max = " << upper() <<","<<" min = " <<lower() << ")" 
                   << std::endl;
         assert(index >= lower_B);
         assert(index <= upper_B);
      }
   }
};

#endif                // _LBVECTOR_H not defined
