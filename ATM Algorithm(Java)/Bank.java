package atm;
import java.text.DecimalFormat;




public class Bank
    {
        private float account; //balance variable
        //generate account with 0 balance
        public Bank()
        {
            account = 0;
        }
        
        //return account balance
        public float balance()
        {
            return account;
        }
        
        //remove money from account
        public int withdraw(float n)
        {
            
            if(n<0)
            {
                return 1;
            }
            else if(n> account)
            {
                return 2;
            }
            
            else
            {
                account -= n;
                return 0;
            }
            
        }
        
        //add money to account
        public boolean deposit(float n)
        {
            if(n<0)
            {
                return false;
            }
            account += n;
            return true;
        }
        
        
        //print account balance
        public String toString()
        {
           double roundOff = Math.round(account * 100.0) / 100.0;
           //String a = Double.toString(roundOff);
           //DecimalFormat df = new DecimalFormat("#.##");
           DecimalFormat df = new DecimalFormat();
           df.setMaximumFractionDigits(2);
           df.setMinimumFractionDigits(2);
           
           String a = df.format(roundOff);
           a = "$" + a;        
           return a;
           
           
           
        }
    }


	