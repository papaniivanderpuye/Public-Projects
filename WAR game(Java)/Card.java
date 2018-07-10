package WAR;

import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

public class Card //creating card class
{
	
	
	// Private instance variables
	private String suit;
	private int value;
    private List<String> legalNames = new ArrayList<>(Arrays.asList("Clubs", "Diamonds", "Hearts", "Spades"));
	
	

	// Primary constructor- also checks to make sure suit name is correct
	public Card(String n, int v)
	{
	    
	    if (legalNames.contains(n) ) 
	    {
            suit = n;            
        }
	    
	    else{
	        System.out.println("Invalid Suit");
	        System.exit(0);
	    }
	    
		if ((v>=1 || v<=13)) 
	    {
            value = v;
        }
        
        else{
	        System.out.println("Invalid Value");
	        System.exit(0);
	    }
        
		
		
	}

	// return card suit name
	public String getSuit(){
		return suit;
	}

    //return card number
	public int getValue() {
		return value;
	}
	
	//return card as a string for printing
	public String toString()
	
	{
	    String printOut = "";
	    int bb = this.getValue();
		if (bb==1)
		{
		  printOut += "Ace";
		}
		
		else if (bb==11)
		{
		  printOut += "Jack";
		}
		
		else if (bb==11)
		{
		  printOut += "Queen";
		}
		
		else if (bb==1)
		{
		  printOut += "King";
		}
		
		else
		{
		  String stringForm = Integer.toString(bb);  
		  printOut += stringForm;
		}
		
    	printOut += " of ";
    	printOut += this.getSuit();
    	
    	return printOut;
	}
	
}


	

