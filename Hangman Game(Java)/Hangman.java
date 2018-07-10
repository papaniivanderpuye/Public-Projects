package hangman;
import java.text.DecimalFormat;
import java.util.Scanner;




public class Hangman
    {
        //private float account; //balance variable
        //generate account with 0 balance
        private String hiddenWord;
        private String guessedLetters = "";
        private String progress = "";
        private int attempts = 8;
        public Hangman()
        {
            hiddenWord = "badboujee";
            
            filter();
            
            for(int i =0; i<hiddenWord.length(); i ++)
                {
                    progress += "_";
                }
        }
        
        public int getAttempts()
        {
            return attempts;
        }
        
        public String getWord()
        {
            return hiddenWord;
        }
        
        private void filter()
        {
            String alpha = "abcdefgijklmnopqrstuvwxyz";
            String filtered = "";
            
            for (char c : hiddenWord.toCharArray()) 
            {
                if ( alpha.indexOf(c) >= 0)
                {
                    filtered += c;
                }
            }
            
           hiddenWord = filtered;
        }
        
        public boolean alreadyGuessed(char s)
        {
            if(guessedLetters.indexOf(s) >= 0 )
            {
                return true;
            }
            
            else
            {
                guessedLetters += s;
                return false;
            }
        }
        
        
        public void displayProg()
        {
            System.out.print("You have "); 
            System.out.print(attempts); 
            System.out.println(" guessed left."); 
            
            for (char c : progress.toCharArray()) 
            {
                System.out.print(c);
                System.out.print(" ");
            }
            
            System.out.println();
            
            
            
            
        }
        
        public void printPastLetters()
        {
            for (char c : guessedLetters.toCharArray()) 
            {
                System.out.print(c);
                System.out.print(", ");
            }
        }
        
        public boolean solve(String word)
        {
            return (progress.equals(word));
        }
        
        public boolean guessLetter(char g)
        {
            
            
            if(hiddenWord.indexOf(g) == -1)
            {
                attempts -= 1;
                return false;
            }
            
            else
            {
                
                String updated = "";
                
                for (int i =0; i<hiddenWord.length(); i ++) 
                {
                    char d = hiddenWord.charAt(i);
                    if ( d == g)
                    {
                        String letter= Character.toString(d);
                        updated += letter;
                    }
                    
                    else
                    {
                        String letter = Character.toString(progress.charAt(i));
                        updated += letter;
                    }
                }
                progress = updated;
                return true;
            }
            
    }

            
            
            
            
public static void main(String[] args)
        {
          
          Hangman myHangman = new Hangman();
          Scanner myScanner = new Scanner(System.in); 
          System.out.println("--- Let's Play Hangman! --- ");
          System.out.println("Guess 'quit' to stop the game at any time.");
          System.out.println("Guess 'letters' to see the letters you've already guessed. ");
          System.out.println("Guess 'solve' to attempt to solve the puzzle!");
          System.out.println();
          System.out.println("I'm thinking of a 8 letter word. Do you know what it is? ");
          while(true)
          {
              System.out.println("");
              if(myHangman.getAttempts() == 0)
                {
                    System.out.println("You have run out of attempts");
                    System.out.print("The word was :"); 
                    System.out.println(myHangman.getWord()); 
                    System.exit(0);
                    
                }  
                
              myHangman.displayProg();
              
              if(myHangman.solve(myHangman.getWord()))
                {
                    System.out.println("Congrats! You got the word!");
                    
                    System.exit(0);
                    
                }
                
              System.out.println("Guess a letter: ");
              
              String guess = myScanner.next();
              
              if (guess.length() == 1)
              
              {
                  char newLetter = guess.charAt(0);;
                  
                  if(myHangman.alreadyGuessed(newLetter))
                    {
                        System.out.println("You already guessed that letter!");
                    }
                    
                  else
                  {
                      if(myHangman.guessLetter(newLetter))
                      {
                          System.out.println("That letter is in the word! ");
                      }
                      
                      else
                      {
                          System.out.println("That letter is NOT in the word :( ");
                      }
                  }
                  
              }
              
              else
              {
                  if(guess.equals("solve"))
                  {
                      System.out.println("Ok what is the word I'm thinking of?");
                      String newWord = myScanner.next();
                      if(myHangman.solve(newWord))
                      {
                        System.out.println("Congrats! You got the word!");                   
                        
                      }
                      
                      else
                      {
                        System.out.println("That's wrong :(");  
                        System.out.print("The word was : "); 
                        System.out.println(myHangman.getWord()); 
                      }
                      
                      System.exit(0);
                  }
                  
                  else if(guess.equals("letters"))
                  {
                     System.out.println("Here is a list of letters you have already guessed");
                     
                     myHangman.printPastLetters();
                  }
                  
                  else if(guess.equals("quit"))
                  {
                     System.out.print("Ok, The word was : "); 
                     System.out.println(myHangman.getWord()); 
                     System.out.println();
                     System.exit(0);
                     
                  }
                  
                  else
                  {
                      System.out.println("Not valid input");
                  }
              }
          }
         }
            
           

        
           
        
    }
    
    

        
        


	