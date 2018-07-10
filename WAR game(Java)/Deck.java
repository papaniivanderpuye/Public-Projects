package WAR;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;


// Creates a deck object for cards
public class Deck extends ArrayList<Card>{
    
    //creating deck with full set of cards
	public Deck()
	{
		super();
		List<String> legalNames = new ArrayList<>(Arrays.asList("Clubs", "Diamonds", "Hearts", "Spades"));
		
		
		for (String temp : legalNames) 
		{
			for( int i=1 ; i <14;i++ )
			{
			    Card d = new Card(temp,i);
			    this.add(d);
			    
                
			}
		}
		
		
		

        
	
	}
	
	//creates an empty deck
	public static Deck makeEmptyDeck()
		{

		 Deck tmp = new Deck(new ArrayList<Card>());
		  return tmp;
	     }

    //creates a deck using a given list of cards
    public Deck(ArrayList<Card> ppp)
    {
        super();
        
        for (Card temp : ppp) 
		{
			this.add(temp);
		}
                
    }
    
    
    //shuffles cards using “FisherYates” algorithm.
    public void shuffle()
    {
        int  n;
        Random rand = new Random();
        for(int k= 0; k< 49; k++)
        {
            n = rand.nextInt((51- k) +1) + k;                        
            Card t = this.get(n);
            this.set( n, this.get(k) );
            this.set( k, t);
        }
    }
	
		
	//adds card to the bottom of the deck
	public void addCard(Card newC)
	{
		this.add(newC);
	}
	
	//returns card from the top of the deck
	public Card pullCard()
	{
		return this.remove(0);
	}
	
	

	



}