user=input("Welcome to Multi-Finance!""\n Please enter your name to continue: ")
def print_program_menu(): #this function was created to print the menu
    print("\n---------------------------------------------------")
    print( "Hello,",(user),"please pick what area of finance you want focus on " )
    print("1. Personal Finance")
    print("2. Banking")
    print("3. Investing")
    print("4. Exit")
    print("---------------------------------------------------")

def Personal_Finance():
    print("---------------------------------------------------")
    print("Welcome to our Personal Finance section")
    print("1. Rule of 50/30/20")
    print("2. Rule of 25")
    print("3. Rule of 72")
    print("4. Return to main menu")
    print("---------------------------------------------------")

def Banking():
     print("---------------------------------------------------")
     print("Welcome to our Banking section")
     print("1. simple interest")
     print("2. Compound interest")
     print("3. Savings account interest increase")
     print("4. Return to main menu")
     print("---------------------------------------------------")
def Investing():
     print("---------------------------------------------------")
     print("Welcome to our Investing section")
     print("1. Stock gain or loss")
     print("2. ROI")
     print("3. How much a stock went up or down")
     print("4. Return to main menu")
     print("---------------------------------------------------")

def main():
    done = False
    while not done:
        print_program_menu() 
        userOption = input("Enter option: ")
        if userOption.isdigit()== False or int(userOption) <=0 or int(userOption)>6:
          print()
          print("Option invalid")
        else:
         userOption = int(userOption)
        if userOption ==1:
            finish = False
            while not finish:
             Personal_Finance()
             userOptionF=int(input("Enter an option: "))
             if userOptionF==1:
               print()
               income=int(input("What is your net monthly salary: $"))
               needs=income*0.50
               wants=income*0.30
               savings=income*0.20
               print("How you should spend:,""\n Needs:","$"+ str((needs)),"\n Wants:","$"+ str((wants)),"\nsavings:","$"+ str((savings),))
               print()
             elif userOptionF==2:
                print()
                retirement=float(input("How much do you want life off of annually? \n: "))
                retirement=retirement*25
                print("You will need","$"+str((retirement)),"for retirment over 25 years")
                print()
             elif userOptionF==3:
               print()
               rate=float(input("How much interest rate you hope to earn? %"))
               rate=72/rate
               print("he approximate number of years it will take for your investment to double is",rate,"years")
               print()
             elif userOptionF==4:
               finish=True
        elif userOption ==2:
           finish = False
           while not finish:
             Banking()
             userOptionF=int(input("Enter an option: "))
             if userOptionF==1:
               print()
               Principal=float(input("How much is your starting principal? $"))
               Interest=float(input("How much is your interest rate e.g. 15 for 15% "))
               Time=int(input("Enter the number of years: "))
               A=Principal*(1+Interest*Time)
               I= A - Principal
               print("The total amount accrued,","$"+str(A),"from simple interest on a principal of","$"+str(Principal))
               print("The total interest paid bieng", "$"+str(I),"over",Time,"years")
               print()
             elif userOptionF==2:
                print()
                P = int(input("How much is your starting principal? $ "))
                n = int(input("Enter number of compounding periods per year. "))
                r = float(input("Enter annual interest rate. e.g. 15 for 15% "))
                y = int(input("Enter the amount of years. "))

                FV = P * (((1 + ((r/100.0)/n)) ** (n*y)))
                I= FV - P
                print("The total amount accrued,","$"+str(round(FV,2)),"from compound interest on a principal of","$"+str(P))
                print("The total interest paid bieng", "$"+str(round(I,2)),"over",y,"years")
                print()
             elif userOptionF==3:
                P=float(input("Enter the initial balance: $"))
                R=float(input("Enter the savings rate in %: "))
                R=R/100
                D=float(input("Enter the yearly deposit amount: $"))
                n=float(input("Enter the number of years you want to calculate: "))
                years=1
                while years!= n+1:
                 (1 + R) * P + D
                 print("The account balance after",years, "year(s) will be $"+str((round((1 + R) * P + D,2))))
                 P=(1 + R) * P + D
                 D=D+D*0.10
                 years=years+1
             elif userOptionF==4:
                  finish=True
        elif userOption ==3:
           finish = False
           while not finish:
             Investing()
             userOptionF=int(input("Enter an option: "))
             if userOptionF==1:
               print()
               Stock=int(input("How much did you pay per stock? "))
               Share=int(input("How many shares do you want to sell? "))
               TotalA=Stock*Share
               Sold_S=int(input("How much is each stock selling for? "))
               TotalB= Sold_S*Share
               TotalC= TotalB - TotalA
               if TotalC > 0:
                print("Wow! You made", "$"+str(abs(TotalC)))
               else:
                print("Sorry but you lost","$"+str(TotalC))
             if userOptionF==2:
              INV=int(input("How much was your amount invested? "))
              Return=int(input("How much was your return? "))
              ROI=(Return - INV)/INV
              print("You have an ROI of","%"+str(ROI*100))
             if userOptionF==3:
              Stocks=(input("Name your stock: "))
              P_Stock=int(input("How much did you pay per stock? "))
              Sold_S=int(input("How much is each stock worth now? "))
              Gain_Loss=(Sold_S-P_Stock)/P_Stock
              if Gain_Loss > 0:
                print("Wow! You're",Stocks,"stock is up", "%"+str(round(Gain_Loss*100,2))+".", "You can hold or sell!")
              else:
                print("Sorry but you're",Stocks,"stock is down","%"+str((Gain_Loss*100))+".", "Cut your looses or hold")
            
             elif userOptionF==4:
                finish=True
        elif userOption==4:
          print("Thank you for using Multi-Finance")
          done=True    
            
if __name__ == "__main__":
    main()
