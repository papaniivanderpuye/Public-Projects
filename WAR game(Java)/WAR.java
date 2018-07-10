package WAR;

import java.util.Scanner;
import java.util.Random;


class WAR //implements user interface for WAR game
{
	public static void main(String[] args) //creates Decks and starts the game using the user's input.
	{				
		Deck startingDeck = new Deck();
		Deck userDeck = Deck.makeEmptyDeck();
		Deck compDeck = Deck.makeEmptyDeck();
		Deck drawDeck = Deck.makeEmptyDeck();
		Card comp; 
		Card user;
		boolean draw = false;
		String ans;
		Scanner myScanner = new Scanner(System.in);
		
		startingDeck.shuffle();
		
	    for( int i=0 ; i <26;i++ )
			{
			    userDeck.add(startingDeck.pullCard());
			    compDeck.add(startingDeck.pullCard());			                    
			}
			
		System.out.println("---- Welcome to WAR! ----");
		System.out.println("You and the computer will each draw a card, whoever has the higher card wins the pair!");
			
		while(true)
		  {
		      if(!(draw))
		      {
		      System.out.println();
		      System.out.print("Your Cards : ");
		      System.out.print(userDeck.size() );
		      System.out.print("         Computer's Cards : ");
		      System.out.println(compDeck.size() );
	           }
	           
		      if(userDeck.isEmpty())
		      {
		        System.out.println("You are out of cards!");
		        System.out.println("You have lost the Game :(");
		        System.exit(0);
		          
		      }
		      if(compDeck.isEmpty())
		      {
		        System.out.println("Your opponent is out of cards!");
		        System.out.println("You have won the Game!");
		        System.exit(0);
		          
		      }
		      
		      if( !(draw) )
		      {
		      System.out.println("Press enter to draw a card!");
		      System.out.println("Press 'Q' or 'q' to quit");
		      
	          }
	          
	          ans = myScanner.nextLine();
		      ans = ans.toLowerCase();

		      if(ans.equals("q"))
		          {
		            System.out.println("Quitting game...");
		            System.exit(0);
		            
		          }
		          
		      else if(ans.equals(""))
		      {
		          comp = compDeck.pullCard();
		          user = userDeck.pullCard();
		          System.out.print("(you) ");
		          System.out.print(user);
		          System.out.print("  <>  ");
		          System.out.print(comp);
		          System.out.println(" (computer)");
		          
		          //checking which value is bigger and then giving the card to the winner          
		          if (comp.getValue() > user.getValue())
		              {
		                  draw = false;
		                  compDeck.addCard(user);
		                  compDeck.addCard(comp);
		                  
		                  while( !(drawDeck.isEmpty()) )
		                  {
		                      compDeck.addCard(drawDeck.pullCard());		                      
		                  }		                  
		                  System.out.println("Your lost!");		                  
		              }
		              
		          else if (comp.getValue() < user.getValue())
		              {
		                  draw = false;
		                  userDeck.addCard(comp);
		                  userDeck.addCard(user);
		                  
		                  while( !(drawDeck.isEmpty()) )
		                  {
		                      userDeck.addCard(drawDeck.pullCard());		                      
		                  }		                  
		                  System.out.println("Your won!");
		              }
		           //saving cards when there is a draw  
		           else
		           {
		               draw = true;  		           
		               drawDeck.addCard(comp);
		               drawDeck.addCard(user);
		               System.out.println("          This means WAR!");		                   
		               System.out.print("          (there are ");
		               System.out.print(drawDeck.size());
		               System.out.print(" cards at stake, plus ");
		               System.out.print(comp);
                       System.out.print(" and ");
		               System.out.println(user);              
		               System.out.println("          Press enter to continue");
		            }
		      }		      
		      else
		      {
		          System.out.println("Invalid input");
		      }
		  }
	}
}