// Parameter assignment for CS 330 - Spring 2009

// Papa Nii Vanderpuye
//The purpose of this Lab code is for me 
//to learn how to use the macro facility of C++
// to investigate pass-by-name, Jensen's Device, and overloading functions.

#include "tvector.h"
#include "tmatrix.h"

#include <iostream>
#include <iomanip>
#include <sstream>

#include <math.h>
using namespace std;



// this is a helper function to help print elements from vectors in a specific format.
void print(double number)
    {
       ostringstream convert; 
       int numbertoConvert = int((number*100));
       if(numbertoConvert == 0)
       {
           numbertoConvert = 100;
       }
       convert << numbertoConvert; 
       string numberString = convert.str();
       
       cout<< string((8 - numberString.length()),' ');
       cout<<number;
       
       return;
    }

// this is a helper function to help print elements from matrices in a specific format.    
void print2(double number)
    {
       ostringstream convert; 
       int numbertoConvert = int((number*100));
       if(numbertoConvert == 0)
       {
           numbertoConvert = 100;
       }
       convert << numbertoConvert; 
       string numberString = convert.str();
       
       cout<< string((10 - numberString.length()),' ');
       cout<<number;
       
       return;
    }


// this function takes a single vector paramater with elements of double type, 
// and fills it from standard input  
//precondition: vector given in parameter
//postcondion: vector is filled with new values taking from standard input	  
void read(tvector<double> & myVector)
{
    int size = myVector.size();
    for(int i =0; i<size; i++)
    {
        cin >> myVector[i];
    }
    
    return;
}


//This function takes a single vector parameter that has elements of double type and prints the 
//vector with 8 characters per value, printed with 2 digits after the decimal point.
//precondition: vectors given to print
//postcondition: numbers printed from elements in the vectors
void write(tvector<double>  & myVector)
	{
		int size = myVector.size();

		for(int i=0;i<size;i++)
		{
			print(myVector[i]);
		
		}

        cout << endl;
        return;
        
	}
	
//This function takes a single matrix parameter and that fills the 
//matrix from standard input by reading in row major order.
//precondition: matrix given in parameter
//postcondion: matrix is filled with new values taking from standard input	
void read(tmatrix<double> & myMatrix)
{
    int J =myMatrix.numrows();
    int K =myMatrix.numcols();
    for(int a=0;a<J;a++)
   {
       for(int b=0;b<K;b++)
       {
           cin >> myMatrix[a][b];
       }
                   
   }
   
   return;
   
}

//this function takes a single matrix parameter and writes the matrix to standard 
//output, in row major order. with 10 characters per value, printed 
//with 2 digits after the decimal point.
//precondition: matrix given to print
//postcondition: numbers printed from elements in the matrix
void write(tmatrix<double>  & myMatrix)
	{
	   int K =myMatrix.numrows();
       int L =myMatrix.numcols();
	    
	   for(int d=0;d<K;d++)
        {
            for(int e=0;e<L;e++)
                {
                    print2(myMatrix[d][e]);
                }
            cout<<endl;
        }
        cout<<endl;
        return;
	}
	

// Your Jensen's Device macro goes here
//this a macro that finds the sum of and expression involving and index
//it is given a start index and stop index
#define jensen(expr,index,start,stop,sum){\
	    double temp=0;\
	    for(index=start;index<stop;index++){\
	       temp += expr;\
	    }\
	    sum= temp;\
	}

// This function takes a vector as its only parameter and returns the norm of the vector. 
//The norm is the square root of the sum of the 
//squares of the vector's elements.
double norm(tvector<double> & myVector)
{
    
   double total;
   double norm;
   int i;
   jensen(myVector[i]*myVector[i],i,0,myVector.size(),total);
   
     
   norm = sqrt(total);
   
   return norm;
   
}

//This function takes two vectors and computes and returns their dot product.
//precondition: vectors given are of the same length
//postcondition: number returned that is the dot product of vectors
double multiply(tvector<double> & firstVector,tvector<double> & secondVector)
{
    
   double total;
   int i;
   jensen(firstVector[i]*secondVector[i],i,0,firstVector.size(),total);  
   return total;
   
}


//This function takes two matrices and computes and returns their product.
//precondition: matrices assummed to have compatible row and columns sizes for multiplication
//postcondition: new matrice is returned that is a product of given matrice parameters
tmatrix<double> & multiply(tmatrix<double> & firstMatrix,tmatrix<double> & secondMatrix)
{
    
    
    tmatrix<double> & productMatrix = *(new tmatrix<double>(firstMatrix.numrows(),secondMatrix.numcols(),0));
    int rowSize= firstMatrix.numrows();
    int colSize = secondMatrix.numcols();
    int newcolSize = firstMatrix.numcols();
    
    
    
    for(int a=0; a<rowSize; a++)
    
        {
            for(int b=0; b<colSize; b++)
    
                {
                    int i;
                    
                    jensen(firstMatrix[a][i]*secondMatrix[i][b],i,0,newcolSize,productMatrix[a][b]);
                    

                }
        }
        
    return productMatrix;
    
}


//This function reads integers, declares two vectors and two matrices
//and initializes each of them from standard input. 
//it then prints the norm for both vectors, the dot product of the vectors
//and the product of the the two matrices.
void driver()
{
   int J;
   int K;
   int L;
   
   cin >> J;
   cin >> K;
   cin >> L;
   
   
   
   cout << std::fixed;
   cout << std::setprecision(2);
   
   tvector<double> & firstVector = *(new tvector<double>(J) );
   read(firstVector);  
   cout<<"First Vector is:"<<endl;
   write(firstVector);
   cout<<"Norm is:"<<endl;
   print(norm(firstVector));
   cout<<endl;
   
   tvector<double> & secondVector = *(new tvector<double>(J) );
   read(secondVector);  
   cout<<"Second Vector is:"<<endl;
   write(secondVector);
   cout<<"Norm is:"<<endl;
   print(norm(secondVector));
   cout<<endl;
   
   cout<<"The dot product of the two vectors is:"<<endl;
   print(multiply(firstVector,secondVector));
   cout<<endl;
   
   
   tmatrix<double> & firstMatrix = *(new tmatrix<double>(J,K) );
   read(firstMatrix);  
   cout<<"First Matrix is:"<<endl;
   write(firstMatrix);

   
   
   tmatrix<double> & secondMatrix  = *(new tmatrix<double>(K,L) );
   read(secondMatrix);    
   cout<<" Second Matrix is"<<endl;
   write(secondMatrix);
   
   
    
   
    
    tmatrix<double> productMatrix = multiply(firstMatrix,secondMatrix);
    cout << "The product of the two Matrices is:"<<endl;
    write(productMatrix); 
    
    return;
}





//this function runs the driver
int main( )
{    
    driver();
    
    return 0;
    
}




