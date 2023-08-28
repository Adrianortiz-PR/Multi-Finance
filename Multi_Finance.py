user=input("Welcome to Multi-Finance!""\n Please enter your name to continue: ")

def print_program_menu():
    print("\n---------------------------------------------------")
    print("Hello,", user, "please pick an area of finance to focus on:")
    print("1. Personal Finance")
    print("2. Banking")
    print("3. Investing")
    print("4. Exit")
    print("---------------------------------------------------")

def handle_personal_finance():
    print("---------------------------------------------------")
    print("Welcome to our Personal Finance section")
    print("1. Rule of 50/30/20")
    print("2. Rule of 25")
    print("3. Rule of 72")
    print("4. Return to the main menu")
    print("---------------------------------------------------")
    
    user_option_f = int(input("Enter an option: "))
    
    if user_option_f == 1:
        print()
        income = float(input("What is your net monthly salary: $"))
        needs = income * 0.50
        wants = income * 0.30
        savings = income * 0.20
        print("How you should spend:\nNeeds: ${:.2f}\nWants: ${:.2f}\nSavings: ${:.2f}".format(needs, wants, savings))
        print()
    elif user_option_f == 2:
        print()
        retirement = float(input("How much do you want to live off of annually? $"))
        retirement = retirement * 25
        print("You will need ${:.2f} for retirement over 25 years".format(retirement))
        print()
    elif user_option_f == 3:
        print()
        rate = float(input("What interest rate do you hope to earn? %"))
        rate = 72 / rate
        print("The approximate number of years it will take for your investment to double is {:.2f} years".format(rate))
        print()
    elif user_option_f == 4:
        return
    else:
        print("Invalid option")

def handle_banking():
    print("---------------------------------------------------")
    print("Welcome to our Banking section")
    print("1. Simple Interest")
    print("2. Compound Interest")
    print("3. Savings Account Interest Increase")
    print("4. Return to the main menu")
    print("---------------------------------------------------")
    
    user_option = int(input("Enter an option: "))
    
    if user_option == 1:
        print()
        principal = float(input("Enter the starting principal: $"))
        interest_rate = float(input("Enter the interest rate (e.g., 15 for 15%): "))
        time_years = int(input("Enter the number of years: "))
        
        accrued_amount = principal * (1 + (interest_rate * time_years))
        interest_paid = accrued_amount - principal
        
        print("The total amount accrued is $", round(accrued_amount, 2))
        print("The total interest paid is $", round(interest_paid, 2))
        
    elif user_option == 2:
        print()
        principal = float(input("Enter the starting principal: $"))
        compounding_periods = int(input("Enter the compounding periods per year: "))
        interest_rate = float(input("Enter the annual interest rate (e.g., 15 for 15%): "))
        years = int(input("Enter the number of years: "))
        
        final_value = principal * ((1 + (interest_rate / 100 / compounding_periods)) ** (compounding_periods * years))
        interest_earned = final_value - principal
        
        print("The total amount accrued is $", round(final_value, 2))
        print("The total interest earned is $", round(interest_earned, 2))
        
    elif user_option == 3:
        initial_balance = float(input("Enter the initial balance: $"))
        savings_rate = float(input("Enter the savings rate in %: ")) / 100
        yearly_deposit = float(input("Enter the yearly deposit amount: $"))
        num_years = int(input("Enter the number of years: "))
        
        for year in range(1, num_years + 1):
            initial_balance = (1 + savings_rate) * initial_balance + yearly_deposit
            yearly_deposit += yearly_deposit * 0.10
            print(f"The account balance after {year} year(s) will be ${round(initial_balance, 2)}")
            
    elif user_option == 4:
        return
    else:
        print("Invalid option.")




def handle_investing():
    print("---------------------------------------------------")
    print("Welcome to our Investing section")
    print("1. Stock gain or loss")
    print("2. ROI")
    print("3. How much a stock went up or down")
    print("4. Return to the main menu")
    print("---------------------------------------------------")
    
    while True:
        user_option_investing = input("Enter an option: ")
        
        if user_option_investing == "1":
            print()
            stock_price_paid = float(input("How much did you pay per stock? "))
            shares_bought = int(input("How many shares did you buy? "))
            current_stock_price = float(input("How much is each stock selling for now? "))
            
            total_investment = stock_price_paid * shares_bought
            total_value_now = current_stock_price * shares_bought
            gain_loss = total_value_now - total_investment
            
            if gain_loss > 0:
                print("Congratulations! You made a profit of $", round(gain_loss, 2))
            elif gain_loss < 0:
                print("Sorry, you incurred a loss of $", round(abs(gain_loss), 2))
            else:
                print("Your investment has not changed in value.")
        
        elif user_option_investing == "2":
            print()
            initial_investment = float(input("How much was your initial investment? "))
            final_return = float(input("How much was your final return? "))
            roi = ((final_return - initial_investment) / initial_investment) * 100
            print("Your Return on Investment (ROI) is:", round(roi, 2), "%")
        
        elif user_option_investing == "3":
            print()
            stock_name = input("Name your stock: ")
            initial_stock_price = float(input("How much did you pay per stock? "))
            current_stock_price = float(input("How much is each stock worth now? "))
            
            price_change = current_stock_price - initial_stock_price
            percent_change = (price_change / initial_stock_price) * 100
            
            if price_change > 0:
                print(f"Congratulations! {stock_name} is up by {round(percent_change, 2)}%.")
            elif price_change < 0:
                print(f"Sorry, {stock_name} is down by {round(abs(percent_change), 2)}%.")
            else:
                print(f"{stock_name} has not changed in value.")
        
        elif user_option_investing == "4":
            break
        
        else:
            print("\nInvalid option. Please enter a valid choice.")




def main():
    user = input("Welcome to Multi-Finance!\nPlease enter your name to continue: ")
    done = False
    while not done:
        print_program_menu()
        user_option = input("Enter option: ")
        try:
            user_option = int(user_option)
            if user_option == 1:
                handle_personal_finance()
            elif user_option == 2:
                handle_banking()
            elif user_option == 3:
                handle_investing()
            elif user_option == 4:
                print("Thank you for using Multi-Finance")
                done = True
            else:
                print("\nOption invalid")
        except ValueError:
            print("\nPlease enter a valid option.")

if __name__ == "__main__":
    main()
