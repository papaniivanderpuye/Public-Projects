package atm;
import java.util.Scanner;


public class BankDriver
{
    public static void main(String[] args)
    {
        atm.Bank myBank = new atm.Bank(); //creating a new bank object
        System.out.println("Welcome to the MAD bank!"); 
        

        // 
        Scanner myScanner = new Scanner(System.in); //creating scanner object for user input
        
        System.out.print("Current balance: ");
        String v = myBank.toString();
        System.out.print(v);
        
        char g = 's';
        while(g != 'q') //while loope for user interface
        {
            
            System.out.println();
            System.out.println("What would you like to do? ");
            System.out.println("(q)uit (d)eposit (w)ithdraw (c)heck balance");
            
            System.out.print(": ");
            
            String n = myScanner.next();
            
            if(n.length() == 1)
            {
                g = n.charAt(0);
                
                if(g == 'c')
                {
                    System.out.print("Current balance: "); //for printing current balance
                    v = myBank.toString();
                    System.out.println(v);
                }
                
                else if(g == 'd')
                {
                   System.out.println("How much would you like to deposit?"); // for adding money to account
                   float t = myScanner.nextFloat();
                   
                   if(myBank.deposit(t) == false)
                   {
                     System.out.println("You cannot deposit a negative number");  
                   }
                   
                }
                
                else if(g == 'w')
                {
                   System.out.println("How much would you like to withdaw?"); //fpr subtracting money from account
                   float f = myScanner.nextFloat();
                   int result = myBank.withdraw(f);
                   if(result == 1)
                   {
                     System.out.println("You cannot withdraw a negative number");  
                   }
                   
                   else if(result == 2)
                   {
                     System.out.println("Insufficient funds");  
                   }
    
                   
                }
                
                else if(g != 'q')
                   {
                     System.out.println("Please type a valid command");  
                   }
            }
            
            else
            {
                System.out.println("Please type a valid command ");
            }

            
        }
        
        
}

}